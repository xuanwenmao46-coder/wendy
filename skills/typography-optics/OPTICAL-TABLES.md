# Optical Tables

These tables encode the physical relationship between font-size, font-weight, and letter-spacing for video production at 1280×720 base resolution (scale all values linearly for 4K).

Letter-spacing values are in `em` units and apply as CSS `letter-spacing`. They represent corrections to the default `0` — use them as the final value, not as an offset to add to a design system token.

---

## How to Read These Tables

1. Find the text role (Display / Headline / Support / Metadata / Data).
2. Find the font-size column that matches your planned size.
3. Find the weight row.
4. The cell gives the corrected tracking value.
5. Apply the **CJK modifier** if the script is Chinese/Japanese/Korean.
6. Apply the **Video modifier** if the text appears on screen for < 3 seconds or is animated.

---

## Table 1 — Latin / Grotesk / Serif Display

For: condensed grotesks, editorial serifs, humanist sans at headline sizes.

| Weight | 72–88px | 88–110px | 110–140px |
|---|---|---|---|
| 300 | −0.01em | −0.01em | 0em |
| 400 | −0.01em | −0.02em | −0.02em |
| 500 | −0.01em | −0.02em | −0.03em |
| 600 | −0.02em | −0.03em | −0.03em |
| 700 | −0.02em | −0.03em | −0.04em |
| 800 | −0.03em | −0.04em | −0.05em |
| 900 | −0.03em | −0.05em | −0.06em |

**Condensed grotesks** (Barlow Condensed, DM Mono, etc.): tighten by an additional −0.01em at all weights.

**All-caps display** (uppercase labels used at display size): loosen by +0.02em regardless of weight.

---

## Table 2 — Latin Body and Support

For: humanist sans, neutral grotesks at readable paragraph and label sizes.

| Weight | 16–20px | 20–28px | 28–40px | 40–56px | 56–72px |
|---|---|---|---|---|---|
| 300 | +0.01em | 0em | 0em | −0.01em | −0.01em |
| 400 | 0em | 0em | −0.01em | −0.01em | −0.02em |
| 500 | 0em | −0.01em | −0.01em | −0.02em | −0.02em |
| 600 | 0em | −0.01em | −0.02em | −0.02em | −0.03em |
| 700 | −0.01em | −0.01em | −0.02em | −0.03em | −0.03em |

---

## Table 3 — Latin Uppercase Labels and Metadata

For: pill labels, section tags, UI chips, source captions. All-caps only.

These run counter to the display direction: small caps at small sizes need WIDE tracking to compensate for the lack of ascender/descender variation.

| Weight | 10–12px | 12–14px | 14–18px |
|---|---|---|---|
| 300–400 | +0.10em | +0.08em | +0.07em |
| 500–600 | +0.09em | +0.08em | +0.06em |
| 700 | +0.08em | +0.07em | +0.06em |

Mixed-case labels (not all-caps): use Table 2 values.

---

## Table 4 — CJK (Chinese / Japanese / Korean) Display

For: 黑体, 宋体, 圆体, any CJK variable font at headline and display sizes.

CJK characters are stroke-dense square glyphs. At large sizes and heavy weights, `letter-spacing: 0` produces visible crowding because the visual counters inside each glyph are already small.

| Weight | 64–80px | 80–100px | 100–130px | 130px+ |
|---|---|---|---|---|
| 300 | 0em | 0em | −0.01em | −0.01em |
| 400 | −0.01em | −0.01em | −0.02em | −0.02em |
| 500 | −0.01em | −0.02em | −0.02em | −0.03em |
| 700 | −0.02em | −0.02em | −0.03em | −0.04em |
| 900 | −0.02em | −0.03em | −0.04em | −0.05em |

---

## Table 5 — CJK Body and Support

For: Chinese paragraph text, support labels, subtitle-zone captions.

| Weight | 18–24px | 24–32px | 32–48px | 48–64px |
|---|---|---|---|---|
| 300 | +0.02em | +0.01em | 0em | −0.01em |
| 400 | +0.01em | 0em | −0.01em | −0.01em |
| 700 | 0em | −0.01em | −0.01em | −0.02em |
| 900 | −0.01em | −0.01em | −0.02em | −0.03em |

---

## Table 6 — Mono / Data

**No letter-spacing, ever.**

```css
font-variant-numeric: tabular-nums;
letter-spacing: 0; /* explicit, no exceptions */
```

If you are tempted to open tracking on mono labels: don't. Tabular number alignment depends on fixed advance widths. Tracking breaks column alignment.

Uppercase mono labels (e.g. `RENDER · 28–30s`) are the one exception: use `+0.04em` maximum to compensate for the optical density of uppercase mono at small sizes. Never more.

---

## Video Modifier: −0.01em Rule

Apply an additional −0.01em tightening on top of the table value for any text that:
- Appears in a video (not a static web page)
- Is CJK script at display size (64px+)
- Is animated with any motion (translate, fade, scale)

**Why**: Video compression (H.264, HEVC) introduces blockiness in high-frequency regions. Dense stroke + wide spacing amplifies block artifacts between characters. Tightening by −0.01em reduces the artifact surface area without making the text feel cramped.

This modifier is additive. Example: CJK 900 at 100px → table value is −0.03em → with video modifier → **−0.04em**.

---

## Line-Height Reference

Line-height is not tracked in the tables above but is part of optical spacing. Use these baselines:

| Role | Latin | CJK |
|---|---|---|
| Display (72px+) | 0.95–1.05 | 1.00–1.10 |
| Headline (48–72px) | 1.05–1.15 | 1.10–1.20 |
| Support / Body (24–40px) | 1.35–1.50 | 1.40–1.55 |
| Metadata / Label (12–20px) | 1.20–1.30 | 1.30–1.40 |

CJK requires more line-height than Latin at all sizes because the character bounding box fills the full em square — ascenders and descenders do not create natural visual separation between lines.

---

## Quick-Reference: Common Video Typography Tokens

| Scenario | Size | Weight | Script | Corrected tracking |
|---|---|---|---|---|
| Hero display, Linear-style | 96–110px | 900 | Latin | −0.05em |
| Hero display, 黑体 impact | 96–110px | 900 | CJK | −0.04em (−0.05em with video mod) |
| Headline bilingual | 60–72px | 700 | Mixed | Latin −0.03em / CJK −0.02em |
| Support paragraph | 26–32px | 400 | CJK | 0em |
| UI chip label | 11–13px | 400 | Latin uppercase | +0.08em |
| Timeline node label | 11–13px | 400 | Mono uppercase | +0.04em |
| CTA button text | 18–22px | 700 | Latin | −0.01em |
| Data counter | any | any | Mono | 0em, tabular-nums |
