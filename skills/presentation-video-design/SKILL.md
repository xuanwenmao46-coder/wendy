---
name: presentation-video-design
description: Designs premium PPT-like video clips, slide-style motion pages, pitch-deck visuals, data story pages, product explainers, and skill preview galleries. Use when creating HyperFrames/GSAP clips that should feel like high-quality presentation design, investor decks, launch keynotes, consulting slides, or when the user says a video feels basic, generic, low-end, or not like a good PPT.
---

# Presentation Video Design

Use this before implementing clip HTML or GSAP motion when the desired artifact is a moving slide, pitch-deck page, explainer page, or presentation-style clip. The goal is to design a moving slide, not decorate a webpage.

If the user asks for a product ad, brand film, social video, launch spot, or says the result feels too much like PPT, do not let this skill define the whole scene structure. Use it only for information hierarchy, then hand the clip back to `flagship-video-director` and `motion-graphic-design` for video-first continuity.

## Core Principle

Every clip must answer:

- What should the viewer understand in 2 seconds?
- What is the single dominant visual idea?
- Which elements are essential, supporting, or optional?
- What can be omitted if the user does not provide enough input?
- Is this truly a moving slide, or should it be a continuous video event?

If the answer is unclear, simplify the page before adding animation.

## Boundary: Moving Slide vs Video Ad

Use moving-slide structure when the user wants a deck-like page, report page, pitch section, learning card, or single takeaway.

Avoid moving-slide structure when the user wants:

- A 15s+ product intro or launch film.
- A brand advertisement.
- A social ad that should feel like a real video.
- A clip that already feels too PPT-like.

For video ads, this skill may define the takeaway and type hierarchy, but the final structure must be an event chain: input -> transformation -> product behavior -> proof/usage -> final lockup.

## Required Workflow

1. Define the slide job: cover, takeaway, data story, comparison, timeline, feature grid, visual metaphor, or transition.
2. Write a one-sentence takeaway. Do not use a neutral label like "Monthly Revenue"; write the actual conclusion.
3. Rank information into primary, secondary, tertiary, and source/caption.
4. Pick a layout pattern from [SLIDE-TYPES.md](SLIDE-TYPES.md).
5. Apply `typography-selection` for type roles and embedded fonts.
6. Apply `image-art-direction` if the clip uses product images, screenshots, renders, icons, or downloaded visuals.
7. Define design tokens: palette, type scale, spacing scale, radius, stroke, shadow/material.
8. Define motion as presentation choreography: reveal the idea first, evidence second, context last.
9. If the user wants energy, motion graphics, kinetic type, stingers, flashes, or says it feels too PPT-like, apply `motion-graphic-design`.
10. Run the quality audit in [QUALITY-AUDIT.md](QUALITY-AUDIT.md).

## Skill Modules To Compose

Use these as reusable sub-skills when designing a clip:

- **Cover System**: keynote opening, hero title, brand mark, visual hook.
- **Takeaway System**: one claim, large type, one proof object, minimal context.
- **Data Story System**: insight headline, highlighted data, low chartjunk, clear annotation.
- **Comparison System**: before/after, option A/B, competitor matrix, tradeoff cards.
- **Timeline System**: sequence, roadmap, process, user journey, cause-and-effect.
- **Feature System**: product visual plus 3-5 feature blocks, with one dominant feature.
- **Visual Metaphor System**: abstract shapes that explain growth, speed, connection, safety, scale.
- **Transition System**: scene continuity based on shared geometry, masks, wipes, camera moves, or typographic match cuts.

## Layout Rules

- Use one dominant idea per frame.
- Prefer one strong composition over many equal cards.
- Anchor to a grid: 3-4 vertical lines and consistent margins.
- Leave intentional negative space. Whitespace is a design element.
- Make the first read obvious: title/key number/image must outrank all details.
- Use bento/cards only when grouping helps understanding.
- Do not center everything unless the page is a deliberate title, quote, or final lockup.
- If the same title/subtitle/card layout repeats across multiple scenes, stop and redesign as a continuous video event.

## Data Story Rules

- Chart title must be the insight, not the chart type.
- Highlight one data series or value with accent color; mute the rest.
- Choose chart by message: bar for comparison, line for trend, pie only for simple part-to-whole, big number for impact.
- Remove chartjunk: heavy gridlines, decorative 3D, random icons, redundant labels.
- Add source/caption only as tertiary information.

## Motion Rules

- Motion serves reading order, not spectacle.
- Stage attention: primary element enters first, evidence follows, details settle last.
- Use easing as language: calm ease-out for premium, snap for UI/product, slow mask for cinematic, spring only for expressive moments.
- Use anticipation and follow-through sparingly to avoid robotic movement.
- Keep most clips readable while paused on the hero frame.
- Avoid animating every element with the same preset.

## Optional / Skippable Inputs

When user input is missing, degrade gracefully:

- Missing palette: use project brand/default palette.
- Missing image: switch to type-led or abstract visual metaphor layout.
- Missing data: use takeaway, comparison, or feature page instead of fake charts.
- Missing body copy: use title + proof object + caption.
- Missing transition: use clean hard cut or simple opacity, not decorative wipes.
- Too much text: summarize into one takeaway and 2-3 supporting fragments.

## Output Contract

Before implementation, produce this brief:

```markdown
## Presentation Video Direction
- Slide job:
- One-sentence takeaway:
- Audience:
- Primary read:
- Secondary read:
- Optional/skippable inputs:
- Layout pattern:
- Data/image role:
- Typography direction:
- Palette/material:
- Motion choreography:
- Anti-patterns to avoid:
```

Then create the clip or update `DESIGN.md`.

## References

- For slide patterns, read [SLIDE-TYPES.md](SLIDE-TYPES.md).
- For quality checks, read [QUALITY-AUDIT.md](QUALITY-AUDIT.md).
- For visual design baseline, combine with `high-end-video-design`.
- For image selection, combine with `image-art-direction`.
- For fonts, combine with `typography-selection`.
- For energetic animation, kinetic typography, text-block flashes, and broadcast-style motion, combine with `motion-graphic-design`.
