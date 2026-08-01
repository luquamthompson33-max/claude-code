"""
Minimal layered-PSD writer for screen-print color separations.

Writes an 8-bit RGB PSD with N named raster layers (one per ink) plus a
composited merged image. Each layer stores full-canvas RGBA so Photoshop
shows each separation as its own layer you can toggle, recolor, or halftone.

No third-party PSD lib required (pytoshop won't build here) -- this emits the
Adobe Photoshop File Format directly with struct + numpy.
Spec ref: Adobe Photoshop File Format Specification.
"""
import struct
import numpy as np


def _pascal(s: str) -> bytes:
    b = s.encode("latin-1", "replace")[:255]
    out = bytes([len(b)]) + b
    # pad to even length
    if len(out) % 2:
        out += b"\x00"
    return out


def _rle_pack_row(row: bytes) -> bytes:
    """PackBits compression of a single scanline."""
    out = bytearray()
    i, n = 0, len(row)
    while i < n:
        # look for a run of >=3 equal bytes
        run = 1
        while i + run < n and row[i + run] == row[i] and run < 128:
            run += 1
        if run >= 3:
            out.append(256 - (run - 1))
            out.append(row[i])
            i += run
        else:
            # literal run
            start = i
            i += 1
            while i < n:
                if i + 2 < n and row[i] == row[i + 1] == row[i + 2]:
                    break
                if i - start >= 127:
                    break
                i += 1
            lit = row[start:i]
            out.append(len(lit) - 1)
            out.extend(lit)
    return bytes(out)


def _compress_channel(chan: np.ndarray):
    """RLE-compress a HxW uint8 channel -> (data, list_of_rowbytelengths)."""
    h, w = chan.shape
    counts = []
    packed = bytearray()
    for r in range(h):
        pr = _rle_pack_row(chan[r].tobytes())
        counts.append(len(pr))
        packed.extend(pr)
    return bytes(packed), counts


def write_psd(path, merged_rgb, layers):
    """
    merged_rgb: HxWx3 uint8 array (the flattened composite preview).
    layers: list of dicts: {name, rgb (HxWx3 uint8), alpha (HxW uint8)}.
            Layers are written bottom-to-top in list order.
    """
    H, W, _ = merged_rgb.shape
    merged_rgb = np.ascontiguousarray(merged_rgb, dtype=np.uint8)

    # ---- File header ----
    hdr = b"8BPS" + struct.pack(">H", 1)            # signature, version 1 (PSD)
    hdr += b"\x00" * 6                               # reserved
    hdr += struct.pack(">H", 3)                      # channels (RGB)
    hdr += struct.pack(">II", H, W)                  # rows, cols
    hdr += struct.pack(">H", 8)                      # depth
    hdr += struct.pack(">H", 3)                      # color mode = RGB

    color_mode = struct.pack(">I", 0)               # empty color mode data
    image_resources = struct.pack(">I", 0)          # empty image resources

    # ---- Layer records ----
    layer_records = bytearray()
    layer_pixel_blocks = []  # channel image data per layer, in order

    for ly in layers:
        rgb = np.ascontiguousarray(ly["rgb"], dtype=np.uint8)
        alpha = np.ascontiguousarray(ly["alpha"], dtype=np.uint8)
        top, left, bottom, right = 0, 0, H, W
        layer_records += struct.pack(">iiii", top, left, bottom, right)

        # 4 channels: A(-1), R(0), G(1), B(2)
        chan_ids = [-1, 0, 1, 2]
        chan_arrays = [alpha, rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]]
        layer_records += struct.pack(">H", len(chan_ids))

        chan_datas = []
        for cid, arr in zip(chan_ids, chan_arrays):
            packed, _ = _compress_channel(arr)
            # channel data = compression id (2 bytes) + rle counts + packed
            h = arr.shape[0]
            counts_bytes = b"".join(
                struct.pack(">H", len(_rle_pack_row(arr[r].tobytes()))) for r in range(h)
            )
            cdata = struct.pack(">H", 1) + counts_bytes + packed  # 1 = RLE
            chan_datas.append(cdata)
            layer_records += struct.pack(">hI", cid, len(cdata))

        layer_pixel_blocks.append(chan_datas)

        layer_records += b"8BIM"                     # blend mode signature
        layer_records += b"norm"                     # normal blend
        layer_records += struct.pack(">B", 255)      # opacity
        layer_records += struct.pack(">B", 0)        # clipping
        layer_records += struct.pack(">B", 0)        # flags
        layer_records += struct.pack(">B", 0)        # filler

        # extra data: mask (0), blending ranges (0), name (pascal, padded to 4)
        name_p = _pascal(ly["name"])
        # unicode layer name (luni) so Photoshop shows the real name
        uni = ly["name"]
        luni = struct.pack(">I", len(uni)) + uni.encode("utf-16-be")
        if len(luni) % 2:
            luni += b"\x00"
        luni_block = b"8BIM" + b"luni" + struct.pack(">I", len(luni)) + luni

        extra = struct.pack(">I", 0)                 # layer mask data len 0
        extra += struct.pack(">I", 0)                # blending ranges len 0
        # pad pascal name to multiple of 4
        while len(name_p) % 4:
            name_p += b"\x00"
        extra += name_p
        extra += luni_block
        layer_records = layer_records[:-0] if False else layer_records
        layer_records += struct.pack(">I", len(extra)) + extra

    # channel image data (all layers, in order)
    chan_image_data = bytearray()
    for blocks in layer_pixel_blocks:
        for cdata in blocks:
            chan_image_data += cdata

    layer_count = len(layers)
    layer_info_body = struct.pack(">h", layer_count) + bytes(layer_records) + bytes(chan_image_data)
    if len(layer_info_body) % 2:
        layer_info_body += b"\x00"
    layer_info = struct.pack(">I", len(layer_info_body)) + layer_info_body

    global_mask = struct.pack(">I", 0)
    layer_and_mask_body = layer_info + global_mask
    layer_and_mask = struct.pack(">I", len(layer_and_mask_body)) + layer_and_mask_body

    # ---- Merged image data (RLE) ----
    merged = bytearray(struct.pack(">H", 1))         # compression = RLE
    all_counts = bytearray()
    all_packed = bytearray()
    for c in range(3):
        chan = np.ascontiguousarray(merged_rgb[:, :, c])
        for r in range(H):
            pr = _rle_pack_row(chan[r].tobytes())
            all_counts += struct.pack(">H", len(pr))
            all_packed += pr
    merged += all_counts + all_packed

    with open(path, "wb") as f:
        f.write(hdr)
        f.write(color_mode)
        f.write(image_resources)
        f.write(layer_and_mask)
        f.write(merged)
    return path


if __name__ == "__main__":
    # self-test: 3 synthetic layers on a small canvas
    H, W = 64, 96
    merged = np.zeros((H, W, 3), np.uint8)
    layers = []
    for name, color, box in [
        ("RED", (200, 30, 40), (5, 5, 40, 40)),
        ("TAN", (210, 170, 120), (20, 30, 55, 80)),
        ("WHITE", (245, 245, 245), (30, 50, 60, 90)),
    ]:
        rgb = np.zeros((H, W, 3), np.uint8)
        a = np.zeros((H, W), np.uint8)
        t, l, b, r = box
        rgb[t:b, l:r] = color
        a[t:b, l:r] = 255
        merged[t:b, l:r] = color
        layers.append({"name": name, "rgb": rgb, "alpha": a})
    write_psd("/home/user/claude-code/sep/_selftest.psd", merged, layers)
    # read back with PIL to validate structure
    from PIL import Image
    im = Image.open("/home/user/claude-code/sep/_selftest.psd")
    print("PSD opened:", im.size, im.mode)
    try:
        n = 0
        while True:
            im.seek(n)
            print("  layer", n, im.tell())
            n += 1
    except EOFError:
        pass
    print("self-test OK")
