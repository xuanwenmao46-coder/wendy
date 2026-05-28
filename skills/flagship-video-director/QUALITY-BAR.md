# Quality Bar

Use this before final render and before calling a clip a flagship candidate.

## Scoring

Score each category from 1-5:

- `impact`: Does the first second create attention?
- `motion`: Are there multiple intentional beats, not one preset?
- `focus`: Does the viewer know where to look?
- `style`: Does the clip have a recognizable visual register?
- `readability`: Does the key message land still long enough?
- `reusability`: Can this become a reusable skill/preset?
- `memorability`: Can the visual idea be described in one sentence?
- `video_native`: Does it feel like a continuous video event rather than animated slides?

## Hero Threshold

To treat a clip as a hero-tier RAG seed:

- impact >= 4
- motion >= 4
- focus >= 4
- style >= 4
- reusability >= 4
- memorability >= 4
- video_native >= 4

If a clip fails two or more categories, revise before indexing as a flagship seed.

## Red Flags

Reject or revise:

- It looks like a PPT slide with animated transitions.
- It is structured as 4-6 equal pages with title/subtitle/card layouts.
- The same left-title/right-object composition repeats across most beats.
- Transitions are wipes that hide page changes instead of match cuts or object transformations.
- The product/metaphor does not visibly do anything.
- Every element fades/slides with the same easing.
- There is no first-second hit.
- The visual concept cannot be summarized.
- Motion makes text unreadable.
- Text overlaps a visually similar color block, so the paused frame loses contrast.
- It is all style and no user scenario.
- It uses weak product/image assets as the hero.
- It has random particles, HUD, or glows with no narrative role.
- It has high-contrast flashing over 3Hz.

## Minimum Acceptance

A good clip should be expressible as:

```text
For [scenario], this clip uses [visual concept] and [motion pattern] to make [message] memorable.
```

For video ads, also express it as:

```text
Across the clip, [persistent object/system] transforms from [starting state] into [final product/value state].
```

Example:

```text
For growth reports, this clip uses a scoreboard-style number impact and chart tear to make the metric feel consequential.
```
