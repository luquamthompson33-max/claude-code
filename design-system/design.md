# RUNISM — Design System

**Version 1.0 · "New Generation"**

RUNISM is a running community with the ambition of flight. The brand borrows
the discipline and optimism of aerospace — precision marks, deep space, the thin
blue line of atmosphere — and points it at the most human act there is: putting
one foot in front of the other, again.

> **We are Runism. Run again.**

---

## 1. Brand Foundation

| | |
|---|---|
| **Essence** | Motion, altitude, community. Every runner is a launch. |
| **Personality** | Precise, calm, quietly bold. Confident enough to whisper. |
| **Promise** | Run again. There is always another horizon and a crew waiting on it. |

**Attributes:** aerospace-minimal · high contrast · human-centered · endless horizon · community-first · next generation

The design language is intentionally restrained. Black and white carry ~90% of
every layout; the signature blue is used sparingly, as a moment of atmosphere and
light. Generous negative space — "open sky" — is a core asset, not empty room to fill.

---

## 2. Logo

### The Mark
A **four-point spark** — a compass star stretched along the horizon line. It reads
three ways at once: a burst of speed, a distant star, and a runner's stride at full
extension. The horizontal points are dominant (~2.4× the vertical), keeping the mark
low and fast.

The mark is a concave four-point star. Reference SVG path (viewBox `0 0 100 60`):

```html
<svg viewBox="0 0 100 60">
  <path d="M98 30 Q50 30 50 12 Q50 30 2 30 Q50 30 50 48 Q50 30 98 30 Z" fill="#FFFFFF"/>
</svg>
```

### The Wordmark
`RUNISM` set in a clean grotesque (Archivo / Helvetica-class), **weight 600**,
**all caps**, with generous **0.42em letter-spacing**. Never condense, never
change the tracking.

### Primary Lockup
Mark + wordmark, horizontal, separated by a gap equal to roughly one letter-width.
The mark's vertical center aligns to the wordmark's optical center.

### Color Variants
- **On light** → mark and wordmark in Ink `#080B18`.
- **On space / on photography** → mark and wordmark in White `#FFFFFF`.
- One-color only. The mark is never a gradient or a second accent color.

### Clearspace
Minimum clearspace on all sides = **the height of the mark (×)**. Nothing —
type, image edges, other logos — enters this zone.

### Minimum Size
- Digital: wordmark cap-height ≥ 10px (lockup ≈ 90px wide).
- Print: lockup ≥ 24mm wide.

### Misuse — never
- ❌ Rotate or skew the mark or lockup.
- ❌ Recolor the mark (no orange, no gradients, no brand-adjacent blues on the mark itself).
- ❌ Condense, extend, or re-track the wordmark.
- ❌ Crowd the lockup or place it in a box/badge.
- ❌ Place the light lockup on a busy mid-tone image without a scrim.

---

## 3. Color

The palette is a **vertical journey**: from the black of space, through the thin
blue band of atmosphere, up to the near-white light of the horizon.

### Core
| Token | Name | Hex | Use |
|---|---|---|---|
| `--ink` | Ink | `#000000` | Posters, pure black type, maximum contrast |
| `--space` | Space | `#080B18` | Primary dark background |
| `--space-2` | Space 2 | `#0D1530` | Raised dark surfaces, gradient midpoint |
| `--white` | White | `#FFFFFF` | Primary light background, reversed type |

### Signature Blue
| Token | Name | Hex | Use |
|---|---|---|---|
| `--atmosphere` | Atmosphere | `#2E5C9B` | Primary accent, links, secondary buttons |
| `--sky` | Sky | `#A9CCE8` | Hover states, highlights, gradient light |
| `--horizon` | Horizon | `#DCEBF7` | Palest light, gradient top, tints |

### Neutrals / UI
| Token | Name | Hex | Use |
|---|---|---|---|
| `--steel` | Steel | `#4A5468` | Body text on light |
| `--ash` | Ash | `#8A94A6` | Muted text on dark |
| `--cloud` | Cloud | `#E7EBF1` | Borders, dividers on light |
| `--fog` | Fog | `#F4F6F9` | Light section background |

### Signature Gradients
- **Atmosphere** (hero, posters) — a radial glow rising from the bottom edge:
  `radial-gradient(120% 90% at 50% 120%, #DCEBF7, #A9CCE8 24%, #2E5C9B 52%, #0D1530 78%, #000 100%)`
- **Edge** (cards, panels, business cards) — a horizontal wash into light:
  `linear-gradient(90deg, #080B18, #0D1530 55%, #2E5C9B 78%, #A9CCE8 100%)`

### Ratio & Accessibility
- Target ~60% dark / 30% light / 10% blue in any given composition.
- Body text: Steel `#4A5468` on White, or White/Ash on Space — both pass WCAG AA.
- Never set body copy in Sky or Horizon; those are for large shapes and highlights only.

---

## 4. Typography

The system runs on a **single grotesque family** in three roles.

| Role | Family | Weight | Treatment |
|---|---|---|---|
| **Display** | Archivo Expanded (fallback: Helvetica Neue / Arial) | 900 / 800 | Uppercase, tight `-0.01em`, line-height 0.92–0.98 |
| **Wordmark / Label** | Archivo | 600 / 700 | Uppercase, tracking 0.16em (labels) → 0.42em (wordmark) |
| **Body** | Inter (fallback: Helvetica Neue / Arial) | 400 / 500 | Sentence case, line-height 1.6 |

**Rules**
- Headlines are **always uppercase**. Body copy is **always sentence case**.
- Display type is heavy and wide — it should feel engineered, not decorative.
- Never mix a serif or a script into the system.

### Type Scale
| Step | Size | Weight | Notes |
|---|---|---|---|
| Display / D1 | `clamp(48px, 9vw, 132px)` | 900 | Hero, posters · 0.92 lh · -0.01em |
| Title / H2 | `clamp(30px, 4.4vw, 56px)` | 800 | Section titles · 0.98 lh |
| Sub / H3 | 20–28px | 700 | Sub-heads |
| Label | 12–13px | 700 | Uppercase · 0.16–0.28em tracking |
| Body | 16–18px | 400 | 1.6 line-height |

Web font loading (optional, graceful fallback to system grotesques):
```
Archivo, Archivo Expanded, Inter — via Google Fonts
```

---

## 5. Layout & Grid

- **Spacing** — 8-pt scale: `8 · 16 · 24 · 40 · 64 · 96 · 140`.
- **Grid** — 12 columns, 24px gutter, content max-width **1180px**.
- **The horizon line** — anchor content to a strong baseline and let the top of a
  composition breathe like open sky. Asymmetry with a heavy base reads as
  "grounded but reaching."
- **Corners** — 2px radius (near-sharp). The brand is precise, not rounded.

---

## 6. Components

- **Buttons** — tracked-out uppercase labels (0.16em), 15×28px padding, 2px radius.
  - *Primary*: White fill / Ink text → hover to Sky.
  - *Sky*: Atmosphere fill / White text → hover to Sky / Ink.
  - *Ghost*: transparent, hairline border → hover border to full contrast.
- **Cards & panels** — hairline borders (`rgba(255,255,255,.12)` on dark,
  `rgba(8,11,24,.10)` on light), subtle surface tint.
- **Membership / business card** — Edge gradient header with reversed lockup,
  white lower half for contact details (see Elliot Ward card reference).
- **Stat tile** — Atmosphere gradient background, Display-weight number, tracked
  uppercase caption.
- **Chips / tags** — pill-shaped, hairline border, tracked uppercase label.

---

## 7. Imagery & Application

- **Photography** is high-key and blown-out: backlit runners against bright sky,
  the curve of the earth from altitude, atmospheric blue.
- **Direction** — faces up, chins to the horizon. Effort and light over grit.
- **Logo over image** — small, calm, single-color, respecting clearspace; add a
  subtle scrim only where legibility requires it.
- **Posters** — heavy Display type top-anchored, atmosphere gradient below,
  small centered lockup at the base ("WE ARE RUNISM. RUN AGAIN COMMUNITY").

---

## 8. Voice & Tone

**Say less. Mean more.** Short, certain lines. Confident but never loud.
Communal, never corporate.

- **Tagline:** *Run again.*
- **Rally:** *We are Runism. Run again community.*
- **Ethos:** *New generation. Endless horizon. Every runner is a launch.*

**Do** — use "we" and "community"; keep lines short; let white space carry weight;
stay optimistic about distance and about people.

**Don't** — hype, jargon, or exclamation stacks ("crush your goals!!!"); fear-based
fitness talk; long paragraphs where one line will do.

---

## Design Tokens (quick reference)

```css
:root {
  /* Core */
  --ink: #000000;  --space: #080B18;  --space-2: #0D1530;  --white: #FFFFFF;
  /* Signature blue */
  --atmosphere: #2E5C9B;  --sky: #A9CCE8;  --horizon: #DCEBF7;
  /* Neutrals */
  --steel: #4A5468;  --ash: #8A94A6;  --cloud: #E7EBF1;  --fog: #F4F6F9;
  /* Type */
  --display: "Archivo Expanded","Helvetica Neue",Arial,sans-serif;
  --grotesk: "Archivo","Helvetica Neue",Arial,sans-serif;
  --body:    "Inter","Helvetica Neue",Arial,sans-serif;
  /* Spacing (8pt) */
  --s1:8px; --s2:16px; --s3:24px; --s4:40px; --s5:64px; --s6:96px; --s7:140px;
  --radius:2px; --maxw:1180px;
}
```

See `index.html` in this folder for the living, rendered version of this system.
