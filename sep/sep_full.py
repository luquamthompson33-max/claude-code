"""
Full print-ready separation set for the Kun Khmer artwork (black garment).

Produces, in sep/out/:
  grayscale/  per-screen 8-bit channels (WHITE = ink)   [editing/compositing]
  film/       per-screen 1-bit AM halftones (BLACK = ink) [print to transparency]
  preview_on_black.png       simulated print on black
  preview_halftone.png       simulated print from the halftone films
  kun_khmer_seps.psd         layered: garment + one layer per screen
  README_PRINT.txt

Screens: White Underbase, White Highlight, Tan, Brown, Red (+ Black reference).
"""
import numpy as np
from PIL import Image
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from psd_writer import write_psd

HERE = os.path.dirname(__file__)
SRC = os.path.join(HERE, "src", "source.png")
OUT = os.path.join(HERE, "out")
GRAY = os.path.join(OUT, "grayscale")
FILM = os.path.join(OUT, "film")
for d in (OUT, GRAY, FILM):
    os.makedirs(d, exist_ok=True)

DPI = 300          # assumed output resolution (1333x2000 -> ~4.44 x 6.67 in)
LPI = 45           # halftone frequency (tee-friendly at this resolution)

INK = {
    "White Underbase": (240, 240, 238),
    "White Highlight": (255, 255, 255),
    "Tan":             (206, 178, 150),
    "Brown":           ( 99,  70,  58),
    "Red":             (130,  32,  30),
    "Black":           ( 18,  12,  11),
}
# halftone angle per screen (deg) — staggered to avoid moire
ANGLE = {
    "White Underbase": 22.5, "White Highlight": 22.5,
    "Tan": 7.5, "Brown": 52.5, "Red": 82.5, "Black": 45.0,
}
GARMENT = (13, 13, 13)

def smooth(e0, e1, x):
    t = np.clip((x - e0) / (e1 - e0 + 1e-6), 0.0, 1.0)
    return t * t * (3 - 2 * t)

def band(x, a, b, c, d):
    return smooth(a, b, x) * (1.0 - smooth(c, d, x))

def halftone(gray01, angle_deg, lpi=LPI, dpi=DPI):
    """AM (clustered round-dot) halftone. Returns uint8, 255=ink(black on film)."""
    h, w = gray01.shape
    cell = dpi / float(lpi)
    th = math.radians(angle_deg)
    ys, xs = np.mgrid[0:h, 0:w].astype(np.float32)
    u = xs * math.cos(th) + ys * math.sin(th)
    v = -xs * math.sin(th) + ys * math.cos(th)
    fu = (u / cell) % 1.0 - 0.5
    fv = (v / cell) % 1.0 - 0.5
    T = np.sqrt(fu * fu + fv * fv) / 0.70710678   # 0 center .. 1 corner
    ink = (gray01 > T).astype(np.uint8) * 255      # dot grows with density
    return ink

def main():
    im = Image.open(SRC).convert("RGBA")
    arr = np.asarray(im).astype(np.float32)
    r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]
    a = arr[:, :, 3] / 255.0
    H, W = a.shape

    mx = np.maximum(np.maximum(r, g), b)
    mn = np.minimum(np.minimum(r, g), b)
    delta = mx - mn
    S = delta / (mx + 1e-6)
    Ln = (0.299 * r + 0.587 * g + 0.114 * b) / 255.0
    hue = np.abs(60.0 * (g - b) / (delta + 1e-6))

    red_dom = ((r >= g) & (r >= b)).astype(np.float32)
    redness = red_dom * smooth(0.42, 0.62, S) * (1.0 - smooth(6.0, 16.0, hue))
    warm = 1.0 - redness

    base = smooth(0.12, 0.44, Ln)
    underbase = a * np.maximum(warm * base, redness * 0.62)   # broad white base
    highlight = a * warm * smooth(0.70, 0.90, Ln)             # top whites only
    tan   = a * warm * band(Ln, 0.36, 0.56, 0.72, 0.92)
    brown = a * warm * band(Ln, 0.10, 0.28, 0.46, 0.68)
    red   = a * redness
    black = a * warm * (1.0 - smooth(0.05, 0.20, Ln))         # reference / non-black garment

    channels = {
        "White Underbase": underbase, "White Highlight": highlight,
        "Tan": tan, "Brown": brown, "Red": red, "Black": black,
    }

    def fname(name): return name.lower().replace(" ", "_")

    # grayscale channels (white = ink) + halftone films (black = ink)
    for name, dens in channels.items():
        d = np.clip(dens, 0, 1)
        Image.fromarray((d * 255).astype(np.uint8), "L").save(
            os.path.join(GRAY, f"{fname(name)}.png"), dpi=(DPI, DPI))
        ht = halftone(d, ANGLE[name])                 # 255 = ink
        film = Image.fromarray(255 - ht, "L").convert("1")   # invert: black = ink
        film.save(os.path.join(FILM, f"{fname(name)}_{LPI}lpi.png"), dpi=(DPI, DPI))

    # simulated preview (continuous tone) on black
    def composite(get):
        canvas = np.zeros((H, W, 3), np.float32) + np.array(GARMENT, np.float32)
        for name in ["White Underbase", "Brown", "Tan", "Red", "White Highlight"]:
            dcol = np.clip(get(name), 0, 1)[:, :, None]
            canvas = canvas * (1 - dcol) + np.array(INK[name], np.float32) * dcol
        return np.clip(canvas, 0, 255).astype(np.uint8)

    preview = composite(lambda n: channels[n])
    Image.fromarray(preview, "RGB").save(os.path.join(OUT, "preview_on_black.png"), dpi=(DPI, DPI))

    # simulated preview built from the actual halftone dots
    ht_dens = {n: (halftone(np.clip(channels[n], 0, 1), ANGLE[n]).astype(np.float32) / 255.0)
               for n in channels}
    preview_ht = composite(lambda n: ht_dens[n])
    Image.fromarray(preview_ht, "RGB").save(os.path.join(OUT, "preview_halftone.png"), dpi=(DPI, DPI))

    # layered PSD: garment + one layer per screen (RGB = ink, alpha = density)
    layers = [{"name": "GARMENT (black)",
               "rgb": np.zeros((H, W, 3), np.uint8) + np.array(GARMENT, np.uint8),
               "alpha": np.full((H, W), 255, np.uint8)}]
    for name in ["Black", "Brown", "Tan", "Red", "White Underbase", "White Highlight"]:
        d = np.clip(channels[name], 0, 1)
        layers.append({"name": name,
                       "rgb": np.zeros((H, W, 3), np.uint8) + np.array(INK[name], np.uint8),
                       "alpha": (d * 255).astype(np.uint8)})
    write_psd(os.path.join(OUT, "kun_khmer_seps.psd"), preview, layers)

    print(f"Output {W}x{H}px, assumed {DPI}dpi ({W/DPI:.2f} x {H/DPI:.2f} in), halftone {LPI} LPI")
    print("screen              coverage  avg-density")
    for name, dens in channels.items():
        m = dens[a > 0.5]
        print(f"  {name:16s}   {(m>0.04).mean()*100:5.1f}%     {m.mean()*100:4.1f}%")

if __name__ == "__main__":
    main()
