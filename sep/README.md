# Screen-print color separation

Tooling to turn the *Kun Khmer* artwork into print-ready color separations.

## Target print settings
- **Garment:** black
- **Method:** simulated process (spot inks + halftones)
- **Output:** single layered `.psd`, one named layer per screen + merged preview
- **Ink stack (to confirm against source):** White (underbase + highlights) ·
  Tan (skin midtones) · Brown (skin shadows / temple) · Dark Red (title, blood, shorts)

## Files
- `psd_writer.py` — dependency-free layered-PSD writer (emits Adobe PSD format
  directly; `pytoshop` won't build here). Validated with `psd-tools`.

## Status
Pipeline built and validated. **Blocked on the real high-res source file** —
the separation must run on the original artwork (300 dpi at print size), not the
low-res flattened preview, or halftones carry compression noise.

## Next step
Drop the high-res `.psd`/`.png`/`.tiff` into the session, then run the
separation to produce `kun_khmer_seps.psd`.
