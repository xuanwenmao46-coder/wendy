---
name: typography-optics
description: Applies optical scaling corrections to video typography after fonts and schools have been selected. Covers three problems typography-selection does not solve: (1) size-to-tracking relationships — the physical law that weight × size × spacing must maintain optical tension; (2) CJK script compensation — Chinese characters behave differently from Latin at every size and weight; (3) motion stability — text in video must survive animation, freeze-frame, and JPEG compression simultaneously. Call this skill on every clip that contains Chinese text, mixed-script lines, or animated text entrances.
dependencies: [typography-selection, aesthetic-layout-direction]
---

# Typography Optics

Font choice is branding. Optical correction is craft. This skill handles the second problem.

`typography-selection` tells you WHAT to use. This skill tells you HOW to use it without making it look wrong.

## Position in Workflow

```
aesthetic-layout-direction  →  school, named anchor, palette
typography-selection        →  font names, role assignments, weight contrast
typography-optics           ←  you are here: correct tracking, fix mixed lines, check motion
high-end-video-design       →  final implementation
```

Call this skill after `typography-selection` has produced a typography brief. Pass it:
- The font names and weights chosen
- The video dimensions and base size
- Whether the script is CJK-only, Latin-only, or mixed
- The animation patterns (fade, slide, scale)

## The Three Problems

### Problem 1 — Optical Scaling

**The rule**: As font-size increases, tracking must decrease. As font-weight increases, tracking must decrease further.

This is not a style choice. It is a perceptual consequence of how stroke density and counter space interact at different scales. Ignoring it produces type that looks "pasted" at large sizes and "airless" at small sizes.

AI default behavior: apply the same letter-spacing token to all sizes. This is wrong at every end of the scale.

→ Correction table: [OPTICAL-TABLES.md](OPTICAL-TABLES.md)

### Problem 2 — CJK Script Compensation

Chinese characters are square-framed and stroke-dense. At equivalent font-size and weight:
- A 900-weight 黑体 character at 100px carries ~30% more visual mass than a 900-weight Latin character
- The default CSS `letter-spacing: 0` produces visible crowding in CJK at large sizes
- When Latin appears next to CJK in the same line, Latin appears lighter and optically smaller due to x-height difference
- CSS `letter-spacing` adds space AFTER each character, including the last — in Chinese full-width text this creates uneven rhythm if punctuation is mixed

These are not subjective preferences. They are optical facts that require correction.

→ CJK rules: [CJK-RULES.md](CJK-RULES.md)

### Problem 3 — Motion Stability

Video adds a dimension web typography ignores: time. Text must be legible:
- During motion (translate, fade, scale)
- At the exact freeze frame when a screen recorder pauses
- After JPEG/H.264 compression artifacts
- At the viewer's typical viewing distance (TV: 3m, monitor: 0.6m, phone: 0.35m)

Fast-moving dense-stroke text disintegrates. Small metadata labels survive translation but not rotation. CJK at 80px is safe to translate; CJK at 24px is not.

→ Motion rules: [MOTION-STABILITY.md](MOTION-STABILITY.md)

## Required Workflow

1. Receive the typography brief from `typography-selection` (font names, role assignments, school).
2. Identify the script profile: `CJK-only` / `Latin-only` / `Mixed` / `Mixed+Mono`.
3. For each text role (Display, Headline, Support, Data, Metadata), look up the corrected tracking value from OPTICAL-TABLES.md using the assigned size and weight.
4. If script is Mixed: apply CJK-RULES.md mixed-line compensation to any line that contains both scripts.
5. Check each animated text element against MOTION-STABILITY.md. Flag any that are at-risk. Propose a fix.
6. Produce the output contract below.

## Output Contract

Write this block before handing off to implementation:

```markdown
## Typography Optics Correction

- Script profile: [CJK-only / Latin-only / Mixed / Mixed+Mono]

- Display role:
  - Font: [name], Size: [px], Weight: [N]
  - Raw tracking: [what typography-selection specified or "unspecified"]
  - Corrected tracking: [value from OPTICAL-TABLES.md]
  - Reason: [one sentence — density / size / weight driver]

- Headline role:
  - Font: [name], Size: [px], Weight: [N]
  - Corrected tracking: [value]

- Support role:
  - Font: [name], Size: [px], Weight: [N]
  - Corrected tracking: [value]

- Data/Mono role:
  - Tracking: 0em (tabular-nums enforced, no exceptions)

- Metadata labels:
  - Font: [name], Size: [px], Weight: [N]
  - Corrected tracking: [value]
  - Case: [uppercase / mixed] → [apply label-tracking bonus if uppercase]

- CJK density flag: [yes / no]
  - If yes → weight compensation: [description]
  - If yes → video tightening: [−0.01em applied on top of table value]

- Mixed-line compensation:
  - [none / Latin font-size +X% / Latin weight −1 step / not applicable]
  - Affected elements: [list]

- Motion safety audit:
  - [element] at [size]px / [animation type] → [safe / at-risk / unsafe]
  - Fix for at-risk: [concrete change]

- Final CSS tokens (ready to implement):
  --t-display-tracking:  [value];
  --t-headline-tracking: [value];
  --t-support-tracking:  [value];
  --t-data-tracking:     0em;
  --t-meta-tracking:     [value];
  --t-lh-display:        [value];
  --t-lh-body:           [value];
```

## Anti-defaults

These are the most common AI typography errors this skill corrects:

| AI default | Correct behavior |
|---|---|
| Same `letter-spacing` at all sizes | Tracking tightens as size increases |
| `letter-spacing: 0` on 100px 黑体 900 | `-0.03em` to `-0.04em` |
| Latin and Chinese at identical font-size on same line | Latin needs +8–12% size OR −1 weight step |
| `letter-spacing: 0.1em` on uppercase metadata | ✓ This one is actually correct — keep |
| Line-height 1.0 on Chinese body text | Chinese needs `line-height: 1.4` minimum |
| Animating 18px support text with y:80px translate | Unsafe — reduce offset or increase size |
| `letter-spacing` on mono/data columns | Never. Breaks tabular alignment. |

## References

- Optical tracking tables by size, weight, script: [OPTICAL-TABLES.md](OPTICAL-TABLES.md)
- CJK character compensation and mixed-line rules: [CJK-RULES.md](CJK-RULES.md)
- Video animation stability and freeze-frame rules: [MOTION-STABILITY.md](MOTION-STABILITY.md)
