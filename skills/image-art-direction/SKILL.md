---
name: image-art-direction
description: Evaluates, selects, and art-directs images for high-end HyperFrames clips, product launch videos, hero frames, posters, thumbnails, and branded motion graphics. Use when a clip needs product photos, downloaded images, mockups, screenshots, transparent PNGs, or when an image looks low-quality, generic, cheap, dated, or unsuitable for premium design.
---

# Image Art Direction

Use this before building a clip that depends on an image. The first decision is whether the image is good enough to be the hero.

## Intake

For each image, identify:

- Subject: product, person, UI, object, environment, abstract asset.
- Format: transparent PNG, JPG photo, SVG, screenshot, render, icon, video clip, texture, full-screen ambience.
- Quality: resolution, crop, lighting, realism, compression, visual age.
- Role: hero, background, detail inset, proof, texture, or reject.
- Rights/source: local, official asset, stock, generated, Wikimedia, unknown.

## Asset Placement Roles

Before placing any image or video in the frame, classify it as one of two primary roles:

### Full-Screen Atmosphere Asset

Use for mood, depth, texture, environment, motion ambience, or brand feeling.

Rules:

- It may be full-bleed, cropped, blurred, color-graded, darkened, masked, or looped.
- It should support the foreground hierarchy, not become the message.
- It must not contain critical information the viewer needs to read.
- Keep contrast low enough for text, product, and UI overlays to remain readable.
- If placed behind text, add a plate, gradient scrim, blur, darken, or mask to protect readability.
- Motion should be slow or environmental unless it is a deliberate transition.
- Good examples: abstract light beams, paper grain, city blur, soft product b-roll, atmospheric smoke, texture video, macro material background.
- Bad examples: busy photo behind small text, readable UI screenshot used as a background, high-contrast stock footage fighting the headline.

### Image Information Asset

Use when the image/video carries content the viewer must understand: product screenshot, UI state, data chart, photo evidence, user proof, before/after frame, document, map, or example output.

Rules:

- It should occupy a deliberate information container: card, device frame, panel, crop window, proof strip, inset, gallery slot, or hero frame.
- Preserve enough size and clarity for the intended read. Do not bury it under heavy blur, glow, tint, or low opacity.
- Add a label, caption, annotation, or callout if the image is evidence.
- Respect aspect ratio unless a crop is part of the design.
- Do not use an information asset as a decorative full-screen background behind important text.
- If it is too detailed to read at final size, crop to the meaningful part or replace it with a designed abstraction.
- Good examples: app screenshot in a phone frame, product render as hero object, chart inside a data panel, proof photo in a bordered card.
- Bad examples: tiny dashboard screenshot, chart used as texture, product photo hidden behind giant decorative effects.

Reject the placement if:

- The asset role is unclear.
- A full-screen atmosphere asset steals attention from the actual subject.
- An image information asset is too small, too filtered, or too obscured to read.
- Text is placed over a busy or similarly bright image without a readability treatment.

## Hero Image Gate

Reject or downgrade an image as hero if:

- It looks like old clipart, dated 3D, generic stock, or low-end mockup.
- Resolution is too low for 1280x720 hero scale.
- Lighting does not match the intended scene.
- Edges are jagged or transparency is poor.
- It carries a visible watermark, UI clutter, or random background.
- It has no product desirability: no material, no silhouette, no detail.

If an image fails the hero gate, do not force it into a premium launch. Use it as a small inset, mask it into a card, crop to detail, or ask for/generate a better asset.

## Preferred Sources

Prioritize:

1. Official product renders or press kit images.
2. High-quality transparent mockups from a trusted source.
3. Generated product render with clear art direction.
4. Clean UI screenshot placed inside a high-quality device frame.
5. Stock/Wikimedia only for tests, not final premium launch.

## Treatment Patterns

Choose one:

- **Hero object**: large product, 45-65% of frame, soft shadow, clear light source.
- **Editorial crop**: product crosses edge, text wraps around empty space.
- **Museum plinth**: product centered on matte surface with label and proof point.
- **Macro detail**: crop a feature detail, use typography as the second subject.
- **Poster card**: weak JPG placed in a designed card with matte, border, and caption.
- **Screen mockup**: UI screenshot inside a clean device frame, no tiny UI text.
- **Atmosphere plate**: full-screen image/video treated as low-contrast ambience with protected foreground safe areas.
- **Information panel**: screenshot/photo/chart placed in a clear card, frame, proof strip, or annotation container.

## Product Launch Rules

- Product image must be larger than all decorative elements.
- HUD may annotate one real feature; it must not decorate the product.
- If the product is weak, design around silhouette, crop, or material detail.
- Avoid mixing multiple product images unless showing a lineup.
- Add a believable light source before adding glows.

## Output Contract

Before implementation, write:

```markdown
## Image Direction
- Source:
- License/rights:
- Hero suitability: pass / downgrade / reject
- Reason:
- Role in frame:
- Placement role: full-screen atmosphere / image information / hero / texture / reject
- Treatment:
- Crop/scale:
- Readability protection:
- Lighting/shadow:
- Risks:
```

## References

- For scoring criteria, read [IMAGE-AUDIT.md](IMAGE-AUDIT.md).
- For treatment examples, read [IMAGE-TREATMENTS.md](IMAGE-TREATMENTS.md).
