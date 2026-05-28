# CJK Rules

Rules for Chinese, Japanese, and Korean text in video production. Treat these as hard constraints, not suggestions.

---

## Rule 1 — Density Compensation

**CJK weight is visually heavier than the same `font-weight` value in Latin.**

At equivalent `font-size` and `font-weight: 900`:
- A Latin 黑体 character (e.g. "A") uses ~40–60% of the em square with thin counters
- A CJK 黑体 character (e.g. "想") fills ~80–90% of the em square with dense strokes

This means 900-weight CJK at 100px reads as heavier, darker, and visually noisier than 900-weight Latin at the same size.

**Correction options (choose one):**

| Situation | Fix |
|---|---|
| CJK at 900 weight feels too heavy against design intent | Drop to 700. Re-check contrast against background. |
| Design requires 900 CJK but needs to feel lighter | Increase letter-spacing by +0.01em and increase font-size by ~5% |
| Mixing CJK 900 + Latin 900 on the same screen | Latin will look lighter — see Rule 3 |

Do not compensate by reducing `opacity`. Reducing opacity on text makes it illegible in compressed video.

---

## Rule 2 — CJK Minimum Sizes for Video

These are not soft guidelines. Below these sizes, CJK glyphs compress to mush in H.264 at standard bitrates.

| Role | Minimum size at 720p | Minimum size at 1080p | Minimum size at 4K |
|---|---|---|---|
| Display | 64px | 96px | 192px |
| Headline | 36px | 54px | 108px |
| Support | 24px | 36px | 72px |
| Metadata label | 16px | 24px | 48px |
| Subtitle zone | 22px | 33px | 66px |
| **Hard minimum** | **16px** | **24px** | **48px** |

Below the hard minimum: do not use CJK. Replace with Latin or remove the element.

---

## Rule 3 — Mixed-Line Compensation (CJK + Latin on Same Line)

**The problem**: Latin glyphs have ascenders, descenders, and an x-height of approximately 50–70% of cap-height. CJK glyphs fill the full em square. At identical `font-size`, CJK appears larger and heavier than Latin.

Result: a line like `创作引擎 · STUDIO` looks visually unbalanced — the Chinese part dominates and the Latin part looks like a caption.

**Detection**: any inline element that contains both CJK characters and Latin characters in the same visual line.

**Three correction strategies — pick based on design intent:**

### Strategy A: Latin Size Boost (recommended for balanced mixed lines)
```css
/* If parent is font-size: 28px, weight: 400 */
.latin-inline { font-size: 1.09em; } /* +9% optical equalization */
```
Use when: the Latin text is a label, subtitle, or equal-weight co-headline.
Amount: +8% to +12% depending on the Latin typeface's x-height ratio.

### Strategy B: Latin Weight Drop (recommended for UI chips, metadata)
```css
/* Parent CJK: font-weight: 700 */
.latin-inline { font-weight: 400; } /* one step lighter */
```
Use when: the Latin content is supplementary information (e.g. `RENDER · 28–30s`).
The lighter weight compensates for the perceived lightness of Latin glyphs.

### Strategy C: Accept the Hierarchy (intentional weight contrast)
Do nothing. Let the CJK dominate. This is a valid design choice when:
- The Latin is a secondary label under CJK display text
- The size difference is intentional (e.g. `想法很多` at 104px with `PROBLEM` at 12px)
- The school is Brutalist / Raw (weight contrast IS the aesthetic)

**Default**: use Strategy A for mixed lines at Support and Headline sizes. Use Strategy C when the size difference is 3× or more.

---

## Rule 4 — Punctuation Handling

### Full-Width Punctuation (全角标点)
Chinese punctuation — ，。！？；：「」【】— is full-width (1em wide). Default CJK fonts render these with built-in side bearing that creates visual padding.

In video at display sizes, adjacent full-width punctuation creates large gaps:
- `想法很多，` — the ，at 104px adds ~52px of space before the next character
- This is correct for body text but excessive for display headlines

**Fix**: For display CJK text with inline punctuation, use `font-feature-settings: "halt" 1` if the font supports it (reduces punctuation side-bearing). Alternatively, apply a negative margin to punctuation elements:

```css
.display-punct { letter-spacing: -0.3em; margin-right: 0.3em; }
```

Only needed when: font-size > 72px AND the punctuation appears mid-line (not end-of-line).

### Half-Width Punctuation in Mixed Text
When writing bilingual UI labels like `创作引擎 · STUDIO`, use the centered dot `·` (U+00B7, half-width) rather than `·` (U+30FB, ideographic centered dot). At mono sizes, the half-width version spaces better with Latin letters.

### Line-End Punctuation
In video subtitles and captions: do not end a line with a full-width comma if the line ends before filling the text box. The visual gap it creates reads as a layout error in motion.

---

## Rule 5 — Line Height for CJK

**Never use `line-height: 1` or `line-height: 1.2` for CJK body or support text.**

CJK characters fill the em square fully. Unlike Latin, there is no natural visual space between lines created by ascender/descender gaps. `line-height: 1.2` produces lines that appear to touch.

| Content type | CJK line-height | Latin equivalent |
|---|---|---|
| Display headline (single line) | 1.0–1.1 | 0.9–1.0 |
| Two-line headline | 1.1–1.2 | 1.0–1.1 |
| Support / body paragraph | 1.45–1.60 | 1.35–1.50 |
| Subtitle zone (video captions) | 1.30–1.40 | 1.25–1.35 |
| UI chip / pill label | 1.0 (single line, controlled height) | 1.0 |

---

## Rule 6 — Simplified vs. Traditional Characters

Simplified Chinese (简体字, used in Mainland China, Singapore) and Traditional Chinese (繁體字, used in Taiwan, Hong Kong, Macau) share the same CSS but require different fonts.

AI systems often default to Simplified Chinese even for Traditional Chinese content. This is an error.

| Audience | Font to use | Font to avoid |
|---|---|---|
| Mainland / Singapore | Noto Sans SC, Source Han Sans SC | any TC-only font |
| Taiwan / HK / Macau | Noto Sans TC, Source Han Sans TC | any SC-only font |
| Unknown / both | Noto Sans SC (SC renders safely in most TC contexts) | Don't mix SC and TC fonts |

In `font-family` declarations: specify explicitly. `'Noto Sans SC'` ≠ `'Noto Sans TC'`. Do not use generic `'Noto Sans'` without the region suffix.

---

## Rule 7 — Vertical Text (竖排)

Vertical Chinese text (`writing-mode: vertical-rl`) is not a video production pattern for most use cases. Do not use it unless the design school explicitly requires it (calligraphic / cultural heritage contexts).

If used:
- Latin letters and numbers do not rotate correctly by default — wrap in `<span style="text-orientation: mixed">`
- Line-height applies to horizontal distance between vertical lines: use 1.8–2.4 (wider than horizontal)
- Punctuation behaves differently — full-width punctuation rotates automatically; Latin punctuation does not

---

## CJK Font Decision Tree

```
Does the video contain Chinese text?
│
├─ Yes → Is it Simplified (Mainland/SG) or Traditional (TW/HK)?
│         │
│         ├─ Simplified → Noto Sans SC weight 300/400/700/900
│         │               (avoid Noto Sans without SC suffix)
│         │
│         └─ Traditional → Noto Sans TC weight 300/400/700/900
│
├─ Yes, also contains Japanese → Noto Sans JP (shared CJK codepoints)
│
└─ Yes, mixed with Latin text →
    Apply Rule 3 (mixed-line compensation)
    Use CJK font as font-family[0], Latin font as font-family[1]
    Example: font-family: 'Noto Sans SC', 'Geist', sans-serif
    The browser uses the CJK font for CJK codepoints, Latin font for Latin codepoints.
```

---

## Common Errors Checklist

Before implementation, verify none of these are present:

- [ ] `letter-spacing` not adjusted for CJK at 80px+ (should be −0.02em or tighter)
- [ ] Mixed CJK+Latin line with no size or weight compensation
- [ ] `line-height: 1.2` or less on CJK body/support text
- [ ] Font-family using `'Noto Sans'` without SC/TC/JP suffix
- [ ] Full-width punctuation mid-headline at 80px+ without side-bearing fix
- [ ] CJK text below 16px at 720p
- [ ] `opacity` used to make CJK text appear lighter (use weight instead)
