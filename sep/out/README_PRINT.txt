KUN KHMER — SCREENPRINT COLOR SEPARATION
Simulated process • Black garment • 1333 x 2000 px
=========================================================

FILES
-----
kun_khmer_seps.psd    Layered separation. Open in Photoshop.
                      Bottom -> top layers:
                        GARMENT (black)  = the shirt (do NOT print)
                        Black screen     = deepest linework (SKIP on black shirt)
                        Brown screen
                        Tan screen
                        Red screen
                        White screen     = underbase + highlights
                      Each ink layer = solid ink color at that screen's
                      density (layer transparency = the printable channel).

channel_*.png         Grayscale film positives, one per screen.
                      WHITE = ink / dot,  BLACK = no ink.
preview_on_black.png  Simulated print result on a black shirt.

INK COLORS (starting point — match to your Pantone stock)
---------------------------------------------------------
White   ~ #F0F0EE   (underbase + highlight, one screen)
Tan     ~ #CEB296   light skin
Brown   ~ #63463A   shadow skin / temple / linework
Red     ~ #82201E   title, blood splatter, shorts
(Black    garment shows through — no screen needed)

PRINT ORDER (flash between as needed)
-------------------------------------
1. White underbase  (flash)
2. Brown
3. Tan
4. Red
5. White highlight  (optional 2nd hit of White screen)

TO HALFTONE IN PHOTOSHOP
------------------------
Each channel is 8-bit grayscale (continuous tone). To make dots:
  Image > Mode > Bitmap > Halftone Screen.
Suggested: 45–55 LPI for auto/manual on a tee.
Angles: keep White/Brown/Tan/Red on different angles (e.g. 22.5°,
52.5°, 7.5°, 82.5°) to avoid moiré, or run all at 22.5° if using
a diffusion/stochastic dot instead.

NOTES
-----
- This is an automated simulated-process sep from a 1333x2000 source.
  Good for a small-to-medium front print (~4.5" wide @ 300 dpi, ~9"
  @ 150 dpi). For a large front print, supply higher-res art.
- The Black screen is included for reference / non-black garments.
  On a black shirt, leave it un-burned so the shirt reads as black.
- Tweak individual channel densities (Curves) to taste before
  halftoning — auto seps are a strong starting point, not gospel.
