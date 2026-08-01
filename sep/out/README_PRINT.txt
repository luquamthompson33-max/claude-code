KUN KHMER — SCREENPRINT SEPARATIONS (full set)
Simulated process • Black garment • 1333 x 2000 px
Assumed output: 300 dpi = 4.44 x 6.67 in • Halftone: 45 LPI
=================================================================

WHAT'S IN HERE
--------------
kun_khmer_seps.psd     Layered master. Open in Photoshop. Layers bottom->top:
                         GARMENT (black)  = the shirt (do NOT print)
                         Black            = deepest linework (SKIP on black shirt)
                         Brown
                         Tan
                         Red
                         White Underbase
                         White Highlight
                       Each ink layer = solid ink color, layer transparency =
                       that screen's printable density.

grayscale/             8-bit continuous-tone channels, WHITE = ink.
                       Use these to tweak (Curves) or to re-halftone yourself.
                         white_underbase.png  white_highlight.png
                         tan.png  brown.png  red.png  black.png

film/                  1-bit AM halftone films @ 45 LPI, BLACK = ink.
                       Print these to transparency and burn. Angles baked in:
                         white_underbase 22.5°   white_highlight 22.5°
                         tan 7.5°   brown 52.5°   red 82.5°   black 45°

preview_on_black.png   Continuous-tone simulation on a black shirt.
preview_halftone.png   Simulation built from the actual halftone dots.

INK COLORS (starting point — match to your Pantone stock)
---------------------------------------------------------
White  ~ #F0F0EE (underbase) / #FFFFFF (highlight)
Tan    ~ #CEB296     light skin
Brown  ~ #63463A     shadow skin / temple / linework
Red    ~ #82201E     title, blood splatter, shorts
Black    = garment shows through — no screen on a black shirt

PRINT ORDER (flash between as needed)
-------------------------------------
1. White Underbase   (flash-cure)
2. Brown
3. Tan
4. Red
5. White Highlight   (final white hit for the brightest sparkle)

PRINTING FROM PHOTOSHOP
-----------------------
- Straight from the PSD: turn off GARMENT + Black, print each ink layer
  through your RIP (let the RIP dot it), OR
- Use the ready-made films in film/ (already dotted at 45 LPI) — place each
  on its own transparency, output at 100% / 300 dpi, and burn.
- To re-dot a grayscale channel yourself: Image > Mode > Bitmap >
  Halftone Screen, 45-55 LPI, round dot, angle per the list above.

NOTES / LIMITS
--------------
- Source is 1333x2000, so this is dialed for a small-to-medium front print
  (~4.5" @ 300 dpi, ~9" @ 150 dpi). Scaling larger lowers effective dpi and
  coarsens the dot — for a big front print, supply higher-res art.
- The grainy look in some films is the artwork's own distress texture, not
  the halftone. That grain reads great as a worn/vintage print.
- Auto seps are a strong starting point, not gospel — nudge channel
  densities to taste before you burn.
