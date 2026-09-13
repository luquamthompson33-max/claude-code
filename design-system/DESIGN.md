# ACID INK — Design System

An **acid-brutalist streetwear** design system, extracted from the Pascal Nueross
tattoo site + moodboard. The mood: near-black canvas, one hi-vis lime, heavy
grotesk headlines, raw marker script, and mono bracket labels. Built to feel
hand-made and loud — never templated, never AI-generic.

> **Live reference:** open `design-system/index.html` in a browser to see every
> token and component rendered.

---

## 1. Color

One dark ground, one signature accent, everything else neutral. The whole system
lives or dies on **restraint with the lime** — if it glows everywhere, it stops
hitting.

| Token | Hex | Role |
|---|---|---|
| `--ink` | `#0C0C0C` | Page canvas. The default. Everything sits on it. |
| `--ink-2` | `#161616` | Raised surfaces — cards, panels, wells. |
| `--ink-3` | `#202020` | Hairline borders, dividers. |
| `--acid` | `#CDEA00` | **Primary accent.** CTAs, labels, active state, arrows. |
| `--acid-deep` | `#B4C400` | Large full-bleed blocks (so lime isn't blinding at scale). |
| `--acid-bright` | `#DAFF1F` | Marker script + graffiti highlights **only**. |
| `--blue` | `#2C2CFF` | Rare secondary punch. One hit per page, max. |
| `--paper` | `#F2F2EC` | Body copy on dark; inverted surfaces. |
| `--smoke` | `#A6A6A0` | Secondary text, captions. |
| `--smoke-dim` | `#6B6B66` | Meta, eyebrows, muted labels. |

**Ratio of thumb:** ~80% ink · ~15% paper/smoke text · ~5% acid. The blue is
a spice, not an ingredient.

---

## 2. Typography

Four roles, four fonts. All free on Google Fonts.

| Role | Font | Weight | Treatment |
|---|---|---|---|
| **Display** | Anton | 400 | Uppercase, `letter-spacing:.005em`, line-height `.86–.92`. Massive. |
| **Heading** | Archivo | 900 | Uppercase, `letter-spacing:-.01em`. Section + card headers. |
| **Marker** | Permanent Marker | — | Accent only. `rotate(-3deg)`, in `--acid-bright`. 1–2 hero words. |
| **Body** | Archivo | 500 | `line-height:1.5`, max `60ch`, in `--smoke`/`--paper`. |
| **Label / mono** | Space Mono | 400 | Uppercase, `letter-spacing:.08em`, wrapped in `[ brackets ]`. |

```css
--f-display: "Anton", sans-serif;
--f-grotesk: "Archivo", -apple-system, "Segoe UI", sans-serif;
--f-marker:  "Permanent Marker", cursive;
--f-mono:    "Space Mono", ui-monospace, monospace;
```

**Type scale (display, clamp for fluid):**

- Hero title — `clamp(56px, 13vw, 180px)`
- Section title — `clamp(40px, 7vw, 84px)`
- Card / row heading — `20–34px`, weight 900
- Body — `15–17px`
- Label / meta — `11–13px`

### The bracket label
Every small piece of metadata is a mono label in square brackets — the system's
signature tell. In HTML use the `.label` class (brackets are added via CSS
`::before`/`::after`) or write them literally:

`[ ABOUT ]` · `[ MY STYLE ]` · `[ INKED PRECISION, 2025 ]` · `[ MOBILE 375 PX ]`

### The ghost word
A giant `--f-display` word (`#151515`, barely above the canvas) sits behind the
hero and section transitions, bleeding off the edges. It's texture, not content —
low contrast on purpose.

---

## 3. Components

| Component | Notes |
|---|---|
| **Button — acid** | `--acid` fill, ink text, uppercase 800. Hover: nudge `-2px,-2px` + hard `4px 4px` shadow (no blur). |
| **Button — ghost** | Transparent, `--ink-3` border. Hover: border + text go acid. |
| **Button — paper** | White fill for the one loud CTA on dark. |
| **Style list** | Big uppercase rows, bottom-border divider, `↘` chevron. Hover: text→acid, pad-left `8px`. |
| **FAQ accordion** | Lives inside an `--acid-deep` full-bleed block. `<details>`/`<summary>`, `+` rotates to `×` on open. |
| **Chips / labels** | Mono, bordered. Variants: outline, acid outline, acid fill, blue fill. |
| **Media card** | Grayscale image, mono tag, corner acid triangle flag. |

**Interaction language:** hard offsets and hard shadows (`4px 4px 0`), never soft
blur. Arrows slide on hover. No rounded corners anywhere — everything is a sharp
rectangle.

---

## 4. Layout

- **Grid:** max-width `1180px`, `24px` side gutters, generous vertical rhythm
  (`~88px` section padding).
- **Sections** are separated by a single `--ink-3` hairline top border.
- **Signature blocks** (like the FAQ) break to full-bleed `--acid-deep` to reset
  the eye — dark, dark, dark, then one lime wall.
- **Responsive:** two-column grids collapse to one under `720px`; the ghost word
  scales to `44vw`; body never scrolls sideways.

---

## 5. Principles

1. **Black is the ground.** Near-black is default; light surfaces are punctuation.
2. **One acid, held back.** A single lime does all accent work. Restraint = impact.
3. **Type is the image.** Oversized grotesk + ghost words carry layouts. Photos support.
4. **Leave a human mark.** Marker script, off-angle rotation, hand arrows. One deliberate break in every clean grid.

### Do
- Set headlines huge, tight, uppercase.
- Use `[ bracketed mono ]` for every small label.
- Reserve marker script for 1–2 hero words.
- Keep photos grayscale + high contrast; add color only as a lime mark.
- Let one ghost word bleed off the canvas.

### Don't
- Introduce a second bright accent color.
- Use lime for long runs of body text.
- Round corners or add soft drop shadows.
- Center paragraphs or go timid on scale.
- Ship anything that reads templated, safe, or AI-generic.

---

## 6. Voice & tone

Direct, confident, a little defiant. Short declaratives. Streetwear-meets-studio.
Reference lines from the source: *"Trust your crazy idea." · "Stay human!" ·
"Some stories are better written in ink than in words." · "My skin, my story."*

---

*ACID INK · Design System v1.0*
