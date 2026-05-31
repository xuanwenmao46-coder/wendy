---
name: color-director
description: Encodes the Color Director layer of the Aesthetic Governor System. Transforms color from an afterthought into a deliberate science — atmosphere, psychology, and brand expression governed by the 70/20/10 palette law, 6 palette modes, 8 LUT references, and film grain directives. Runs as part of Step 4.0 in flagship-video-director, within the Aesthetic Governor pipeline. Read by high-end-video-design and aesthetic-layout-direction before any palette decisions are finalized.
---

# Color Director

## Core Principle

Color is not decoration. Color is atmosphere, psychology, and brand. Every color relationship in every frame is a decision — not a default, not a preference, not "what looks nice." The Color Director makes no random decisions. Color has no accidents.

The directive: if you cannot name the emotional and psychological function of every color in the frame, the palette is not designed — it is arbitrary. Arbitrary palettes produce generic output. The Color Director exists to prevent that.

---

## The 70/20/10 Palette Law

Every scene in every clip obeys this ratio:

- **70% Dominant** — the ground color. Background, large surfaces, negative space. This is the emotional register of the scene. The viewer lives in this color.
- **20% Supporting** — secondary surfaces, panels, typographic masses, mid-ground elements. This color *serves* the dominant; it does not compete with it.
- **10% Accent** — a single decisive color hit. Used **once per scene**. The accent is the punctuation mark, not the sentence.

### Violation Patterns and Corrections

| Violation | What it looks like | Correction |
|---|---|---|
| Two accents per scene | Two separate bright hues fighting for attention (e.g., cyan title + orange CTA in the same frame) | Choose one. Remove the other entirely or desaturate it to near-neutral. |
| Accent above 10% | A color that was supposed to be accent ends up in large areas — buttons, panels, headings all in the same vibrant hue | Reduce accent to a single rule, seal mark, or underline. Everything else to neutral. |
| Supporting color too close to dominant | Monochrome collapse: 70% and 20% differ only by shade, the frame reads as one undifferentiated block | Add brightness contrast between dominant and supporting. Separate by at least 15 points in L* (CIELAB). |
| No dominant — all equal weight | Four or five different hues at roughly equal presence, the frame feels chaotic | Pick one color. Desaturate the others. Let one ground dominate. |
| Warm dominant + cold accent + neutral support all at full saturation | The "premium tech" fallacy: dark navy + cyan + white = looks like every SaaS landing page | Desaturate the supporting layer. Let the accent do the full emotional work. |

---

## Palette Mode Taxonomy

### Mode 1 — Monochrome
*Single hue desaturated, elevated with grain.*

**Visual character:** All values derive from a single hue pulled toward neutral gray. Shadows have depth; highlights have texture, never blow out. Film grain is mandatory — without it, digital monochrome reads as underpowered.

**Production rules:**
- Select a hue temperature: warm silver (skin and paper), cold steel (industrial), warm sepia (archival). These are not different hues — they are different tonal biases within the achromatic range.
- Maintain a minimum tonal range: pure black (#0A0A0A) to warm white (#F4F1EC). Never crush blacks to pure digital black.
- Film grain at medium level (0.06–0.12 opacity) is the minimum requirement. Pronounced grain (0.13–0.20) for maximum impact.
- No saturation in any element. If a product, logo, or UI element is color, desaturate it or treat it in black and white.
- Typography: white or near-white on dark ground, or warm black on light ground. No color type.

**Best for:** Peter Lindbergh portraiture register, A24 drama, archival brand films, editorial documentary, fine art product photography.

---

### Mode 2 — Duotone
*Two tones — one warm, one cool — mixed with editorial precision.*

**Visual character:** The image or scene is colored with exactly two tones: a warm tone (shadow value) and a cool tone (highlight value), or a ground hue and a light hue in the opposite temperature. The transition zone between them is the artistic center of the image.

**Production rules:**
- Define Shadow Tone and Highlight Tone before any other decision. Example: shadow tone #1A0F0A (deep warm brown), highlight tone #D4E8F0 (cool blue-white).
- The transition must be visible but not abrupt — 30–40% of tonal range is the blend zone.
- Typography must use one of the two established tones, not a third color.
- The accent (10%) may be a pure version of one tone pushed to maximum saturation.
- Grain at subtle-to-medium (0.04–0.10) reinforces the film-process quality.

**Best for:** Fashion campaign, high-end editorial poster, music video title cards, brand films for beauty/fragrance.

---

### Mode 3 — Restrained Editorial
*Three neutrals + one accent held below 10% of the frame.*

**Visual character:** The discipline of restraint. The palette is built almost entirely of neutrals — warm whites, stone grays, cool linens, warm taupes — with a single accent that appears once per scene, quietly and deliberately. The viewer notices the accent because everything else is not-accent.

**Production rules:**
- Select three neutrals with clear value separation: light ground (~L* 92), mid surface (~L* 68), dark type (~L* 18).
- The accent is introduced exactly once per scene — a hairline rule, a seal mark, a single underlined word, a colored icon. Nothing else receives the accent hue.
- Never use gradient, glow, or semi-transparent accent. The accent is flat and intentional.
- Typography is the dominant visual element. Color does not compete with it.
- Grain is optional; if used, keep it subtle (0.02–0.05).

**Best for:** Aesop brand register, Loewe editorial, museum exhibition, architectural photography, luxury heritage brand.

---

### Mode 4 — Bold Poster
*Hard flat colors at maximum contrast.*

**Visual character:** No gradients. No grain. No texture. Flat planes of color at maximum contrast ratios — the palette is a graphic decision, not a photographic one. Typography and color blocks are the image.

**Production rules:**
- Maximum 4 colors in any scene. Typically 2–3.
- All colors are fully saturated or fully desaturated. No mid-saturation "safe" colors.
- Contrast ratio between text and background must be ≥ 7:1 (WCAG AAA as a starting point; push further for impact).
- Background is either maximum black or maximum white. No "dark gray" backgrounds.
- Never use photography or imagery that competes with the flat graphic field. If photography must appear, crop it hard and let it become a shape.

**Best for:** Bloomberg Businessweek Turley era, Pentagram typographic authority, Balenciaga brand drops, editorial title sequences.

---

### Mode 5 — Warm Neutral
*Off-whites, natural earthy tones, golden light.*

**Visual character:** The palette of material warmth — hand-pressed paper, unfinished linen, warm wood, aged leather, golden hour window light. This palette earns trust through organic imperfection, not through polish.

**Production rules:**
- Ground color: warm off-white, never pure white. Range: #F5EFE4 to #EDE4D3. Pure #FFFFFF is forbidden.
- Supporting surfaces: earthy tones — warm beige, natural stone, aged cream. Never cool gray.
- Accent: a single warm punctuation — amber (#C49A3C), terracotta (#C4614A), warm sage (#8B9E6B). Used once.
- Type color: warm near-black (#1A1410) or warm dark brown (#2C1810), never pure #000000.
- Grain is appropriate and preferred at subtle level (0.04–0.08).

**Best for:** MUJI / Fukasawa register, Stripe Press, editorial craft, artisan product, educational warmth, cookbook aesthetic.

---

### Mode 6 — Dark Ground
*Deep near-black, warm dark surfaces, precision accents.*

**Visual character:** The builder's aesthetic — a dark workspace that makes precision visible. The ground is dark but not dead black; it has warmth or depth. UI chrome, product surfaces, and data elements glow against the dark field. Accents are specific and restrained.

**Production rules:**
- Background: near-black with warmth or subtle chromatic character. Range: #0B0D0F to #131620. Never pure #000000.
- Surface colors: dark with slight warmth — #1A1D24, #1E2130, #242830. Hairline borders at #2A2E38.
- Accent: one precision hue — not cyan, not purple glow. Linear blue (#5B6AEB), amber (#C49A3C), terminal green (#3DDC84), or warm red (#E05C48). One only.
- Typography: near-white (#F0F2F5) at 87% opacity for body, full white (#FFFFFF) for emphasis only.
- No glow. No gradient text. No neon. Precision without spectacle.

**Best for:** Linear, Vercel, Raycast product demos; dark-mode feature launches; technical product films; developer tool brand.

---

## LUT Reference Library

LUT references describe the visual *character* to achieve — not specific file names. Match these characters in post-processing, grading, or AI image generation prompt injection.

### LUT 1 — Kodak TRI-X 400 Emulation
**Character:** Deep organic grain at every exposure level. Blacks that retain shadow detail without crushing. Midtones with a slight warm silver cast. Highlights that bloom softly rather than clip. The defining quality is grain *presence* — visible as texture, not as noise.

**When to use:** Documentary register, Peter Lindbergh portraiture, editorial black-and-white, anything that must feel photographed rather than rendered.

**Grain strength:** Medium to pronounced (0.08–0.18 opacity).

---

### LUT 2 — Fuji Superia 400
**Character:** Warm shadows with a slight green-yellow cast in midtones. Skin tones lean golden. Blues have a slight teal quality. The overall feel is nostalgic, warm, slightly overexposed — summer memory, not precision photography.

**When to use:** Warm humanist register (Mailchimp, Headspace), lifestyle brand, creator tool identity, anything evoking analog nostalgia.

**Grain strength:** Subtle to medium (0.04–0.10 opacity).

---

### LUT 3 — Cinematic Teal-Orange (Detuned)
**Character:** The detuned version only — shadows pulled toward desaturated teal, highlights shifted warm amber, but neither pushed past 30% saturation shift. The result reads as "color-graded film" without becoming the internet's default Instagram cinema palette.

**When to use:** Only in editorial brand film or product launch contexts where the subject is clearly premium. Forbidden in any clip that already risks feeling generic.

**Grain strength:** Subtle (0.03–0.06 opacity).

**Warning:** The *standard* teal-orange is among the most overused grade in digital video. Use the detuned version only. If the skin tones look orange, dial back.

---

### LUT 4 — Bleach Bypass
**Character:** Lifted blacks (shadows never reach pure black), desaturated midtones and highlights, increased overall contrast. The result is harsh, industrial, slightly desaturated — as if the color was pulled out of a frame that still remembers having it.

**When to use:** Brutalist/Raw school, editorial counter-culture, anything that needs to feel unpolished and confrontational.

**Grain strength:** Medium to pronounced (0.10–0.20 opacity).

---

### LUT 5 — Day-for-Night
**Character:** Cooled highlights (blue-white), crushed shadows, desaturated midtones with a blue-gray cast. The image reads as nighttime even if shot in daylight. Moonlit quality without actual darkness.

**When to use:** Atmospheric brand intros, mystery/tension narrative openings, luxury dark-register fashion.

**Grain strength:** Subtle (0.03–0.07 opacity). Heavy grain in day-for-night reads as low budget.

---

### LUT 6 — Warm Print
**Character:** Amber lift in shadows, warm paper-yellow in midtones, slight desaturation of cool tones. Resembles a warm photographic print or offset-printed magazine page.

**When to use:** Warm Neutral palette mode (Mode 5), editorial book aesthetic, heritage brand, archival feel.

**Grain strength:** Subtle to medium (0.05–0.10 opacity).

---

### LUT 7 — Magazine Matte
**Character:** Lifted blacks (blocked at ~L* 10, never full black), slightly desaturated highlights (never blown), flattened contrast in midtones. The overall effect is the color science of a high-end printed magazine — precise, a little flat, extremely legible.

**When to use:** Restrained Editorial mode (Mode 3), luxury product photography, museum print aesthetic, editorial layouts where type and image share the same surface.

**Grain strength:** Subtle or none (0.00–0.05 opacity).

---

### LUT 8 — Studio Neutral
**Character:** Accurate, balanced, slightly warm neutral. No color cast. Blacks are clean, whites are paper-white, skin tones are accurate, highlights are not clipped. This is a calibrated starting point, not a stylistic statement.

**When to use:** Technical demos, product UI recording, dark ground presentations where product accuracy matters more than mood. Also use as a base before any other LUT is applied — always start neutral, then grade.

**Grain strength:** None to subtle (0.00–0.03 opacity).

---

## Film Grain Implementation

Film grain is not a filter applied to hide weaknesses. It is a texture directive that corrects the inherent smoothness of AI-generated and digitally rendered material. Digital perfection reads as uncanny. Physical media reads as real.

### Grain Level Definitions

| Level | Opacity Range | SVG Noise Scale | Application |
|---|---|---|---|
| None | 0.00 | — | Studio product accuracy; technical UI demos |
| Subtle | 0.02–0.05 | 0.5–0.7 | Editorial minimalism, restrained luxury, dark ground mode |
| Medium | 0.06–0.12 | 0.7–1.0 | Standard premium register, warm neutral, duotone |
| Pronounced | 0.13–0.20 | 1.0–1.4 | Monochrome, bleach bypass, brutalist, Lindbergh register |

### CSS Implementation

```css
/* Grain overlay — position: fixed, z-index above content but below UI chrome */
.grain-overlay {
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: 9000;
  opacity: var(--grain-opacity, 0.06);
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
  background-repeat: repeat;
  background-size: 256px 256px;
  mix-blend-mode: overlay;
  animation: grain-shift 0.15s steps(1) infinite;
}

@keyframes grain-shift {
  0%  { transform: translate(0, 0); }
  25% { transform: translate(-3px, 2px); }
  50% { transform: translate(2px, -2px); }
  75% { transform: translate(3px, 3px); }
}
```

**Rules:**
- Grain must animate (shift position every 2–4 frames) to avoid feeling like a static filter.
- Use `mix-blend-mode: overlay` for most modes; `mix-blend-mode: soft-light` for warm neutral mode.
- On dark ground mode (#0B–#13 backgrounds), reduce grain opacity by 20% — dark grounds amplify grain.
- Never apply grain only to image elements; it must cover the full frame uniformly.

---

## Color Constraint System for AI Generators

When AI tools (image generation, video generation) are in the pipeline, color decisions must be encoded as prompt language — both positive injections (what to create) and negative injections (what to suppress).

### Universal Negative Color Prompts

Apply these to every AI generation call regardless of palette mode:

```
negative: cyan glow, neon outlines, gradient text, purple haze, blue-purple gradient background, 
oversaturated HDR, high contrast neon, Instagram filter, digital color grading, 
lens flare, artificial bokeh rainbow, chromatic aberration for effect (not subtle imperfection), 
color splash effect, selective coloring, background separation color grading
```

### Universal Positive Color Prompts

```
positive: analog color science, film-accurate color grading, controlled palette, 
intentional tonal range, shadow detail preserved, highlight rolloff not clipped
```

### Palette-Mode–Specific Injections

**Monochrome:**
```
positive: black and white, silver gelatin print quality, rich shadow detail, grain visible at every tonal level
negative: color, sepia toning, hand-colored effect
```

**Duotone:**
```
positive: two-tone editorial palette, [warm tone name] shadows, [cool tone name] highlights, fashion campaign color science
negative: full color photography, rainbow spectrum, natural color
```

**Restrained Editorial:**
```
positive: neutral palette, warm off-white tones, single color accent used sparingly, museum-quality color restraint
negative: bright saturated colors, multiple accent colors, vivid contrasting hues
```

**Bold Poster:**
```
positive: flat graphic color, high contrast, limited palette, [specific hues], no photographic gradients
negative: photographic color, gradients, texture, shadow volume, illustration detail
```

**Warm Neutral:**
```
positive: warm natural tones, golden hour light, off-white and amber palette, analog warmth, paper texture
negative: cool blue tones, digital white (#FFFFFF), gray backgrounds, cold light
```

**Dark Ground:**
```
positive: dark background, near-black environment, precision accent highlights, controlled low-key lighting
negative: bright backgrounds, high key lighting, overexposed highlights, light backgrounds
```

---

## Forbidden Color Moves by School

Each design school has specific color violations that betray its DNA. These are in addition to the universal violations above.

| School | Forbidden color moves |
|---|---|
| Information Architecture | Gradient backgrounds, warm palette, soft pastels, any color used for mood rather than data encoding |
| Editorial / Minimalist | Saturated accent > 10%, multiple accent colors, digital white (#FFFFFF), gradient overlays, glowing elements |
| Motion / Experimental | Safe neutrals, muted palette, restrained accent — this school requires bold generative color |
| Brutalist / Raw | Soft pastels, warm neutral palette, gradient, anything "pretty" or "balanced" |
| Warm Humanist | Cold blues, dark ground mode, corporate neutrals, clinical whites, high contrast brutal palette |
| Modern Tool / Builder SaaS | Warm print tones, editorial neutrals, fashion duotone — the dark ground must read as precision, not atmosphere |

---

## Color Audit Checklist

Before finalizing any design output, verify:

1. **70/20/10 ratio holds.** The dominant color is present in approximately 70% of the frame area. The accent appears in < 10% and no more than once.
2. **Palette mode is consistent.** Every element in the frame reads as the same mode. No warm neutral surface next to a bold poster background.
3. **LUT character is defined.** A specific LUT reference from the library above has been named. "Cinematic" is not a LUT reference.
4. **Film grain level is specified and implemented.** The grain overlay is present in the rendered output. Verify by pausing the clip and inspecting a held frame.
5. **Forbidden color moves are absent.** Run each element against the school-specific forbidden list and the universal forbidden list.
6. **AI generator prompts are written.** If any AI image or video generation is in the pipeline, positive and negative color injections are in the brief.

If any item fails, return to the palette decision and correct it before proceeding to motion or typography.
