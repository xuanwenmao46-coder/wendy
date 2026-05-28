---
name: high-end-video-design
description: Creates refined, non-generic visual direction for HyperFrames clips, product launch videos, motion graphics, title cards, data clips, and branded animation. Use when the user asks for fancy/high-end design, product launch visuals, layout, typography, art direction, DESIGN.md, or says output feels generic, cheap, AI-ish, or 土味.
---

# High-End Video Design

Use this skill before writing animation code. The job is to design the static frame and visual system first, then let motion serve that design.

## Required Workflow

1. If `aesthetic-layout-direction` has already established a design school (e.g., "Aesop Editorial/Minimalist", "Linear Modern Tool"), extract its video-native tokens (palette hex, composition posture, material, type voice) and use them as the primary source for steps 2 and 3. The school selection takes precedence over the register list below when both exist.
2. Define the design register that best expresses the chosen school: luxury, editorial, technical, cinematic, playful, brutalist, warm, handmade, documentary, broadcast, or poster.
3. Choose target aspect ratio and responsiveness rules before layout.
3. Choose the full style layer before layout: palette, visual language, typography voice, motion posture, and sound posture.
4. Write or update `DESIGN.md` before building HyperFrames HTML.
5. If the clip uses product images or downloaded assets, apply `image-art-direction` before accepting the asset as hero.
6. Apply `typography-selection` before choosing final fonts or rendering.
7. Design the hero frame as a poster: one clear focal point, one secondary focal point, strong negative space, visible structure.
8. Only after the static frame works, define motion: entrance order, holds, transitions, ambient movement.
9. Run an anti-slop audit before implementation.

## Design Register

Choose one register per clip:

- **Premium Launch**: restrained, spacious, material-driven, product image as hero.
- **Editorial Tech**: grid, sharp typography, data used as evidence, not decoration.
- **Cinematic Reveal**: dark values, controlled contrast, fewer but stronger elements.
- **Maximal Type**: oversized typography, bold cropping, text as image.
- **Data Authority**: chart-first, precise labels, tabular numbers, little decoration.

Do not mix registers without a reason.

## Style Layer Selection

Every clip needs explicit style decisions before implementation. Choose concrete options, not vague adjectives.

**When `aesthetic-layout-direction` has established a named school, use its video-native token output as the starting point.** School → style mapping:

| Design School | Palette family | Material | Typography mood | Sonic posture |
|---|---|---|---|---|
| Information Architecture | monochrome editorial / data authority | flat poster / UI panel | institutional / data-first | percussive / editorial |
| Editorial / Minimalist | luxury neutral / dawn warm | paper / film grain / matte | literary / calm humanist | premium restrained / soft |
| Motion / Experimental | cyber dark / custom reactive | light beam / generative | compressed poster / variable | cinematic / designed soundscape |
| Brutalist / Raw | fashion poster / ink paper | flat poster / print | brutal / compressed poster | percussive / aggressive |
| Warm Humanist | organic nature / dawn warm | cloth / paper / organic | literary / playful humanist | organic / soft |
| Modern Tool / Builder SaaS | cyber metal (warm dark variant) | UI panel / glass | technical / data-first | digital / editorial |

If no school was selected, choose from:

- **Palette family:** dawn warm, ink paper, monochrome editorial, cyber metal, sports broadcast, luxury neutral, fashion poster, organic nature, data authority, warning red, or custom.
- **Material system:** glass, paper, metal, film grain, ink, cloth, plastic, smoke, light beam, UI panel, photographic shadow, or flat poster.
- **Image/shape language:** abstract metaphor, cinematic landscape, product photography, UI machinery, data interface, collage, oversized type, documentary lower-third, or symbolic object.
- **Typography mood:** literary, technical, institutional, luxury, brutal, playful, compressed poster, calm humanist, or data-first.
- **Sonic posture:** soft, cinematic, percussive, digital, editorial, organic, premium restrained, or aggressive.
- **Sonic material:** glassy UI, dry paper, print stamp, metal hit, soft air, low trailer pulse, broadcast snap, organic cloth, camera shutter, vinyl/noise, or custom.

Use the topic and video type to separate styles:

- Inspirational: warm/cinematic/organic or paper/ink; fewer hard UI sounds; text should feel human, not like SaaS metadata.
- Product intro: precise/technical/material; product behavior and UI sounds can lead.
- Brand ad: poster/collage/photographic; typography and color can be more opinionated.
- Data story: authoritative/tabular/broadcast; numbers and hits own the frame.
- Explainer: editorial/broadcast; fast labels and stingers can lead, but keep readability.

If the selected style resembles the previous clip too closely, change at least two layers: palette, type, visual language, or sound.

## Sonic Style Layer

Sound is part of the visual style, not a post-production garnish. But style is not a hard asset filter. Design the sound hierarchy first, then use style to shape the timbre and restraint.

Before rendering, define:

- **Material metaphor:** what the sound feels made of, such as paper, metal, glass, rubber, air, ink, machinery, camera, broadcast package, or UI plastic.
- **Transient shape:** soft swell, dry snap, hard thud, tick, scrape, shutter, stamp, glitch burst, or low pulse.
- **Space:** dry/close, room, cinematic tail, wide stereo, mono poster hit, or ambient bed.
- **Density:** sparse, medium, rhythmic, continuous bed, or only scene marks.
- **Forbidden cues:** sounds that would make this clip feel like another style or previous clip.

Then define the sound-design roles:

- **Bed / air:** very low background texture if the motion feels empty.
- **Micro-feedback:** small ticks, taps, rustles, hovers, or marker sounds for repeated small actions.
- **Transition cue:** slice, whoosh, snap, stinger, or air movement on screen changes.
- **Accent hit:** only for primary reveals, claims, stamps, metrics, or lockups.
- **Final lock:** the sonic punctuation for the last frame.

Examples:

- Brand poster/collage: dry print-stamp impacts, paper-slice noise, short editorial snaps; avoid soft motivational whooshes and SaaS UI ticks.
- Inspirational: airy swells, soft organic whooshes, restrained low hits; avoid dense clicks and hard poster impacts.
- SaaS/product: clean UI ticks, digital whooshes, controlled mechanical locks; avoid paper/organic sounds unless conceptually justified.
- Data/broadcast: scoreboard thumps, short ticks, lower-third snaps; avoid long cinematic risers that blur metric timing.

## Composition Rules

- Build around a hero object, not around effects.
- Use edge anchoring and asymmetry; avoid centered stacks unless it is a deliberate final lockup.
- Product image should own 40-65% of the frame in launch videos.
- Keep 2 focal points: product/image + title, or data + conclusion.
- Use structural devices: margins, rules, crop zones, panels, typographic blocks.
- Prefer fewer large elements over many medium cards.

## Image / Video Material Placement

When adding image or video material to a frame, define its role before layout:

- **Full-screen atmosphere material:** mood, texture, environment, cinematic depth, or brand ambience.
- **Image information material:** screenshot, product photo, evidence image, chart, document, map, example output, or any visual the viewer must understand.

Placement rules:

- Full-screen atmosphere material can sit behind the design, but must be graded, blurred, darkened, masked, or plated so foreground text and product elements stay readable.
- Full-screen atmosphere material should not carry essential information. If the viewer must read it, it is not atmosphere.
- Image information material needs a deliberate container: hero frame, card, device mockup, proof strip, panel, crop window, or annotated inset.
- Image information material must be large and clean enough to understand in the final render.
- Do not place key text directly over busy image information material.
- Do not downgrade a product screenshot or proof image into decorative texture unless the script does not require it to be understood.
- If the image/video is weak, crop to a strong detail, put it in a designed card, or ask for/generate a better asset instead of stretching it full-screen.

Anti-patterns:

- A UI screenshot used as a blurry background while the voiceover depends on it.
- A stock video background brighter than the headline.
- A product photo too small to function as a hero object.
- Full-screen b-roll with no foreground hierarchy or readability protection.

## Responsiveness & Adaptability

For reusable video templates, define this before implementation:

- **Aspect ratio:** target ratio and render canvas, such as `16:9 1280x720`, `9:16 1080x1920`, `1:1 1080x1080`, or custom.
- **Layout Rules:** how elements reposition and resize across screen sizes: centered, left/right anchored, percentage-based, grid-based, relative to parent, min/max size constraints.
- **Breakpoints:** screen widths or aspect ratios where layout or animation changes, such as desktop landscape, square, portrait, or mobile-safe.
- **Variable Parameters:** which fields can change from external data or user input: text content, image source, logo, data value, CTA, accent color, duration, narration file.
- **Safe areas:** text, captions, product image, logo, final lockup, and platform UI zones.

Rules:

- If the output is a one-off render, still state `single-ratio` and the exact canvas size.
- If the output is a reusable template, avoid layout that only works at one fixed resolution.
- Use CSS variables for margins, type sizes, hero scale, panel widths, and focal-point coordinates when values may change by ratio.
- Define text min/max widths and font-size ranges so variable copy does not break the composition.
- Motion paths that depend on absolute pixels must have breakpoint-specific alternatives.

## Ratio Adaptation Design Rules

When adapting an existing composition to a different ratio, redesign the frame rather than resizing it:

- Start from the target canvas, not from the source canvas.
- Define a new visual center of gravity for each screen.
- `text_screen` must be redesigned as target-ratio typography, not copied from the source ratio:
  - portrait: use larger type, deliberate line breaks, backing plates, side rails, metadata, oversized background words, or vertical rhythm.
  - square: use stronger central lockups, compact hierarchy, and reduced line length.
  - landscape: use wider comparison, split staging, or horizontal motion paths.
- `action_screen` must move the hero object and supporting modules to fit the new frame. The hero should not become a small object floating in the middle.
- Horizontal components must be converted to target-ratio components: rows to stacks, split layouts to top/bottom, wide previews to portrait-safe cards, timelines to vertical or stacked rails.
- Negative space must have a design role: framing, contrast, pause, or platform safe area. Empty leftover space is a layout failure.
- Re-check typography after adaptation; line breaks that worked in `16:9` often fail in `9:16`.
- Re-check animation paths after adaptation; old x/y travel often looks wrong in a new ratio.

## Typography Rules

- Headlines: 72-140px for 1280x720; body: 26-38px; labels: 16-22px.
- Use dramatic weight contrast, e.g. 300 vs 900.
- Avoid default-feeling choices: Arial, Inter, Roboto, Open Sans, Noto Sans, Poppins, Sora.
- Pair by communicative role: display voice, data voice, support voice.
- For numbers, always use `font-variant-numeric: tabular-nums`.
- Text should be readable in two seconds. Cut words before reducing size.

## Color And Material

- Pick one background, one foreground, one accent, and one material color.
- Avoid cyan-on-black plus purple glow unless explicitly requested.
- Avoid gradient text. Use solid type, outlines, masks, or large crop instead.
- Tint neutrals toward the palette; dead gray feels undesigned.
- Use material contrast: paper, glass, metal, ceramic, ink, shadow, grain.

## Color Overlap Gate

Before implementation and final render, audit every text/color-block overlap:

- Do not place text directly on a color block with similar hue, brightness, or saturation. Warm white on acid yellow, pale yellow on cream, cyan on light blue, magenta on red, and black on deep navy are all likely failures.
- If a moving color slice crosses readable text, the crossed area must intentionally invert, mask, darken, or move behind a separate high-contrast plate.
- Decorative color blocks may pass behind type only when the text remains clearly readable in a paused frame and during motion.
- For poster/motion-graphic styles, high style does not excuse low readability. Use contrast as part of the design, not as a last-minute fix.
- When in doubt, separate the layers: move the color block, add an ink/cream backing plate, switch text color, or clip the color block around the text safe area.

## Product Image Direction

- Treat product imagery as photography, not an icon.
- If the image is mediocre, improve the frame with crop, shadow, matte, reflection, or oversized placement.
- Avoid drowning the product in HUD. HUD should annotate, not decorate.
- Product launch default: one hero image, one large title block, one proof point, one understated detail layer.

## Anti-Slop Audit

Before building, reject these unless intentionally justified:

- Blue/purple neon gradient as the whole concept.
- Generic HUD circles around everything.
- Gradient text.
- Three identical feature cards.
- Everything centered and equally weighted.
- Tiny web UI text.
- Random glows with no light source.
- Decorative elements that do not support hierarchy.
- Text placed over a color block with similar brightness or hue, making the paused frame hard to read.
- A template claiming multi-device use without aspect ratio, layout rules, breakpoints, or variable parameters.
- A portrait adaptation that is only a scaled/cropped landscape layout.
- Text pages with small type blocks floating in a mostly empty portrait frame.

## Output Contract

When planning a clip, produce:

```markdown
## Design Direction
- Design school:
- Named anchor:
- Register:
- Audience:
- One-sentence visual idea:
- Style layer:
- Aspect ratio:
- Responsiveness/adaptability:
- Layout rules:
- Breakpoints:
- Variable parameters:
- Hero frame:
- Image direction:
- Image/video material role:
- Asset placement:
- Typography:
- Palette:
- Material/visual language:
- Sound posture:
- Product/image treatment:
- Layout:
- Motion posture:
- Anti-patterns to avoid:
```

Then create or update `DESIGN.md` using `DESIGN-TEMPLATE.md`.

## References

- For a reusable template, read [DESIGN-TEMPLATE.md](DESIGN-TEMPLATE.md).
- For product launch guidance, read [PRODUCT-LAUNCH.md](PRODUCT-LAUNCH.md).
- For audit criteria, read [ANTI-SLOP-AUDIT.md](ANTI-SLOP-AUDIT.md).
- For image quality and treatment, use the `image-art-direction` skill.
- For font choice and embedding, use the `typography-selection` skill.
- **For anchoring the visual design to a named school (Aesop, Linear, Pentagram, Field.io, etc.) before style decisions, use `aesthetic-layout-direction`.**
