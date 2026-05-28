# Motion Graphic Patterns

These modules are designed for HyperFrames + GSAP implementation.

## Beat Timeline

Default 6s structure:

- 0.00-0.45: anticipation or ambient setup.
- 0.45-1.20: first major hit.
- 1.20-2.20: detail burst / supporting evidence.
- 2.20-3.60: readable hold / visual development.
- 3.60-4.80: second hit or transition.
- 4.80-6.00: final lockup.

## Shape Burst

Purpose: create impact around a word, number, or product.

- Elements: 8-20 lines/dots/rectangles.
- Motion: scale/opacity/radius from focal point, staggered by angle.
- Easing: `expo.out`, then quick fade.
- Use sparingly; one burst per clip is often enough.

## Stinger Cut

Purpose: fast redirect between scenes.

- Elements: full-screen blocks, diagonal masks, large type fragments.
- Duration: 0.4-1.0s.
- Logic: cover screen -> swap scene -> reveal.
- Works for: news, feature reveal, transition, section break.

## Text Block Flash Grid

Purpose: make multiple ideas feel fast and energetic.

- Elements: 6-12 compact text blocks.
- Motion: alternating opacity, scale, y, and mask.
- Rule: only 2-4 blocks should be readable; others can be texture.
- Use a final hero block to summarize the meaning.

## Data Impact Hit

Purpose: make a metric feel important.

- Elements: big number, delta badge, chart spark, annotation.
- Motion: number counts up, badge snaps in, chart draws, highlight pulses.
- Hold: final number must be readable for 1s+.

## Camera Push / Parallax

Purpose: add dimensionality without 3D.

- Elements: foreground text, midground cards, background shapes.
- Motion: scale foreground up slightly, move background slower.
- Easing: `sine.inOut` or `power3.out`.
- Rule: subtle parallax feels expensive; excessive zoom feels template-like.

## Smear Illusion

Purpose: make fast movement feel designed.

- HTML/CSS approximation:
  - duplicate moving element as an echo layer.
  - scaleX or scaleY during the fastest frames.
  - blur/opacity on echo only.
  - remove smear before final landing.
- Timing: smear exists for 2-6 frames, not the whole movement.

## Reactive Echo

Purpose: add secondary motion after a main hit.

- Elements: outline copy, shadow copy, small bars, particles.
- Motion: echo expands/fades 0.05-0.15s after main element.
- Rule: echoes should support the hero, not become the hero.

## In / Change / Out State Machine

Use for reusable broadcast graphics:

- **In**: graphic enters and establishes identity.
- **Change**: text/data updates while container stays stable.
- **Out**: graphic exits quickly without stealing attention.

This is useful for lower thirds, scoreboards, labels, callouts, and product annotations.
