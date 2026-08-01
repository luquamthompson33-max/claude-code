"""
Simulated-process color separation for the Kun Khmer artwork, black garment.

Input : sep/src/source.png  (RGBA, transparent background)
Output: sep/out/  -> per-ink grayscale channels (white = ink density),
                     a simulated-on-black preview, and a layered PSD.
"""
import numpy as np
from PIL import Image
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from psd_writer import write_psd

SRC = os.path.join(os.path.dirname(__file__), "src", "source.png")
OUT = os.path.join(os.path.dirname(__file__), "out")
os.makedirs(OUT, exist_ok=True)

# ---- ink spot colors (RGB) used for preview + PSD layer color ----
INK = {
    "White":  (240, 240, 238),
    "Tan":    (206, 178, 150),
    "Brown":  ( 99,  70,  58),
    "Red":    (130,  32,  30),
    "Black":  ( 18,  12,  11),   # deepest linework; = shirt on black garment
}
GARMENT = (13, 13, 13)  # black shirt

def smooth(e0, e1, x):
    t = np.clip((x - e0) / (e1 - e0 + 1e-6), 0.0, 1.0)
    return t * t * (3 - 2 * t)

def band(x, lo0, lo1, hi0, hi1):
    return smooth(lo0, lo1, x) * (1.0 - smooth(hi0, hi1, x))

def main():
    im = Image.open(SRC).convert("RGBA")
    arr = np.asarray(im).astype(np.float32)
    r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]
    a = arr[:, :, 3] / 255.0
    H, W = a.shape

    mx = np.maximum(np.maximum(r, g), b)
    mn = np.minimum(np.minimum(r, g), b)
    delta = mx - mn
    S = delta / (mx + 1e-6)                            # saturation 0..1
    Ln = (0.299 * r + 0.587 * g + 0.114 * b) / 255.0   # luma 0..1
    hue = np.abs(60.0 * (g - b) / (delta + 1e-6))      # deg from red; ~0 red, ~15+ skin

    # --- isolate the saturated dark-red family from the warm sepia ramp ---
    # true red = red-dominant AND high saturation AND hue close to red (skin is
    # warmer/yellower with g noticeably > b, so it fails the hue gate).
    red_dom = ((r >= g) & (r >= b)).astype(np.float32)
    sat_term = smooth(0.42, 0.62, S)
    hue_term = 1.0 - smooth(6.0, 16.0, hue)
    redness = red_dom * sat_term * hue_term            # 0 on skin, 1 on title/shorts/blood
    warm = 1.0 - redness

    # --- channel densities (0..1), tonal so they halftone smoothly ---
    base = smooth(0.12, 0.44, Ln)                     # white underbase ramp (0 in deep shadow)
    white = a * np.maximum(warm * base, redness * 0.62)
    tan   = a * warm * band(Ln, 0.36, 0.56, 0.72, 0.92)
    brown = a * warm * band(Ln, 0.10, 0.28, 0.46, 0.68)
    red   = a * redness
    black = a * warm * (1.0 - smooth(0.05, 0.20, Ln)) # deepest lines only (skip screen on black shirt)

    channels = {"White": white, "Tan": tan, "Brown": brown, "Red": red, "Black": black}

    # --- save grayscale channel positives (white = ink) ---
    for name, dens in channels.items():
        Image.fromarray((np.clip(dens, 0, 1) * 255).astype(np.uint8), "L").save(
            os.path.join(OUT, f"channel_{name}.png"))

    # --- simulated preview on black garment ---
    canvas = np.zeros((H, W, 3), np.float32) + np.array(GARMENT, np.float32)
    for name in ["White", "Brown", "Tan", "Red", "Black"]:   # base first, lines last
        d = np.clip(channels[name], 0, 1)[:, :, None]
        canvas = canvas * (1 - d) + np.array(INK[name], np.float32) * d
    preview = np.clip(canvas, 0, 255).astype(np.uint8)
    Image.fromarray(preview, "RGB").save(os.path.join(OUT, "preview_on_black.png"))

    # --- layered PSD: garment + one layer per ink (RGB=ink, alpha=density) ---
    layers = []
    bg = np.zeros((H, W, 3), np.uint8) + np.array(GARMENT, np.uint8)
    layers.append({"name": "GARMENT (black)", "rgb": bg,
                   "alpha": np.full((H, W), 255, np.uint8)})
    for name in ["Black", "Brown", "Tan", "Red", "White"]:   # PSD bottom->top
        d = np.clip(channels[name], 0, 1)
        rgb = np.zeros((H, W, 3), np.uint8) + np.array(INK[name], np.uint8)
        layers.append({"name": f"{name} screen", "rgb": rgb,
                       "alpha": (d * 255).astype(np.uint8)})
    write_psd(os.path.join(OUT, "kun_khmer_seps.psd"), preview, layers)

    # coverage report
    print("channel      ink coverage (of art)")
    for name, dens in channels.items():
        print(f"  {name:6s}     {(dens[a>0.5]>0.04).mean()*100:5.1f}%   avg dens {dens[a>0.5].mean()*100:4.1f}%")
    print("size:", (W, H))

if __name__ == "__main__":
    main()
