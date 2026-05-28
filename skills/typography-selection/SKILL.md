---
name: typography-selection
description: Selects, audits, and embeds typography for high-end HyperFrames clips, product launch videos, posters, title cards, data visualizations, and branded motion graphics. Use when choosing fonts, creating DESIGN.md typography, fixing ugly/default fonts, downloading font files, or preparing @font-face for rendered video.
---

# Typography Selection

Use this before writing final clip HTML. Fonts are not decoration; they define the voice of the video.

## Required Workflow

1. Define the text roles: display, support, data, metadata.
2. Define the brand voice: premium, editorial, technical, brutal, soft, playful, institutional.
3. Match the typography voice to the style layer chosen for the video topic/type.
4. Choose font contrast by role, not by habit.
5. Verify the font files are available locally or can be downloaded.
6. Add explicit `@font-face` in the clip project before render.
7. Run HyperFrames lint; fix font warnings.

## Role Model

- **Display**: the main voice. Large, characterful, often 72-140px.
- **Support**: explanatory text. Quiet, readable, 26-38px.
- **Data**: numbers, timestamps, measurements. Monospace or tabular numbers.
- **Metadata**: labels, edition, source, captions. Small but intentional, 16-22px.

## Pairing Rules

- Pair by contrast: serif + sans, condensed + wide, display + mono.
- Avoid two similar sans-serifs.
- Use one expressive font and one receding font.
- Weight contrast must be visible: 300 vs 900 beats 400 vs 700.
- For data, always use `font-variant-numeric: tabular-nums`.

## Text Contrast Rules

- Text color and the color block behind it must be clearly separated by brightness, hue, or a dedicated backing plate.
- Do not allow similar colors to overlap just because the palette looks stylish. Warm white on yellow, yellow on cream, cyan on light blue, and magenta on red usually fail in motion and paused frames.
- If a color slice, wipe, or poster block crosses headline text, plan an inversion, mask, outline, or layout split before coding.
- Audit the final lockup as a still image. If the key words are not readable in one glance, change the color relationship before adjusting animation.

## Banned Defaults

Do not use these for premium work unless the brand explicitly requires them:

- Arial
- Inter
- Roboto
- Open Sans
- Noto Sans
- Poppins
- Sora
- Outfit
- Lato
- Trebuchet MS
- Georgia as final launch display
- System UI as final design

System fonts may be temporary only.

## Product Launch Defaults

Good directions:

- High-contrast serif display + quiet grotesk support + mono data.
- Condensed grotesk display + humanist sans support + mono data.
- Elegant editorial serif + minimal metadata sans.

Avoid:

- Tech video with generic geometric sans everywhere.
- Luxury video with old web serif and default sans.
- Data frame with proportional numbers.

## School-Anchored Typography

When `aesthetic-layout-direction` has selected a design school, use the school's typography anchor as the **primary guide** — it overrides generic topic-based suggestions below:

| Design School | Display voice | Support voice | Data voice | Weight contrast | Characteristic |
|---|---|---|---|---|---|
| Information Architecture | Bold condensed sans or confident serif | Compact neutral sans | Mono, tabular mandatory | 700 vs 900 | Grid-rigorous, no decorative letterforms |
| Editorial / Minimalist | Refined editorial serif or precise grotesque | Very quiet humanist sans | Mono or tabular serif | 300 vs 800 | Generous tracking on display; generous line-height |
| Motion / Experimental | Variable font or extreme condensed; type transforms on beat | Near-invisible or absent | Optional mono | Extreme (100 vs 900) | Typography IS motion; static type is not acceptable |
| Brutalist / Raw | One extreme-weight typeface at absurd scale | System font or near-invisible | System mono | 900 only | Deliberate crudeness; no "designed" refinement |
| Warm Humanist | Warm editorial serif with personality | Friendly humanist sans | Avoid cold mono; use tabular humanist sans | 400 vs 700 | Generous line-height; no tight tracking |
| Modern Tool / Builder SaaS | Humanist sans or condensed grotesk | Mono or semi-mono; keyboard chip aesthetic | Mono, strict tabular | 400 vs 700 | Labels feel like UI metadata, not decoration |

If no school was selected, use topic-based choices:

## Topic-Based Typography Choices

Do not use the same large bold sans style for every clip. Pick typography that changes the viewer's feeling:

- **Inspirational / emotional:** human, literary, warm, or editorial; use generous spacing and calmer metadata. Avoid making it look like a SaaS launch unless the theme demands it.
- **AI / SaaS product:** precise, engineered, compressed, or technical; metadata can be mono; display type should feel controlled.
- **Brand / lifestyle:** expressive display, poster type, high contrast, or fashion editorial; typography can be oversized and image-like.
- **Data story:** tabular numeric voice, compact labels, high confidence; readability beats personality.
- **Explainer / news:** broadcast-like, bold hierarchy, lower-third friendly; use fast but stable readable blocks.
- **Luxury:** restrained contrast, elegant display, quieter support text; avoid cheap glow and generic geometric sans.

If no strong font file is available, write the fallback risk in the brief and compensate through layout, weight contrast, spacing, and material treatment. Do not silently accept a default-looking font.

## Font File Requirement

Rendered video needs stable fonts. Before final render:

- Store fonts in `assets/fonts/`.
- Use `@font-face` with local relative paths.
- Name project-local font families, e.g. `Launch Display`, `Launch Text`, `Launch Mono`.
- Run `npx hyperframes lint` and fix all font warnings.

Example:

```css
@font-face {
  font-family: "Launch Display";
  src: url("assets/fonts/display.woff2") format("woff2");
  font-weight: 300 900;
}
```

## Output Contract

Before implementation, write:

```markdown
## Typography Direction
- Design school:
- Named anchor:
- Brand voice:
- School / topic rationale:
- Display role:
- Support role:
- Data role:
- Pairing logic:
- Font files:
- Fallback risk:
- Sizes:
- Color/overlap contrast:
- Anti-default checks:
```

## References

- For pairing patterns, read [TYPE-PAIRINGS.md](TYPE-PAIRINGS.md).
- For render embedding, read [FONT-EMBEDDING.md](FONT-EMBEDDING.md).
- For audit criteria, read [TYPE-AUDIT.md](TYPE-AUDIT.md).
- **For school-based typography anchoring (Aesop editorial serif, Linear humanist sans, Bloomberg mono authority, etc.), use `aesthetic-layout-direction` first.**
- **For optical tracking correction, CJK compensation, and motion stability — run `typography-optics` after this skill produces the brief. typography-selection chooses fonts; typography-optics makes them optically correct.**
