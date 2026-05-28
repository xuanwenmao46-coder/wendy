---
name: sound-design-for-motion
description: Designs and mixes narration, TTS, sound effects, and beat-synced audio for motion-graphic videos, HyperFrames clips, product launch clips, data hits, HUD animations, UI demos, transitions, stingers, and gallery MP4 previews. Use when adding audio, ASR/TTS timing, SFX, whooshes, hits, clicks, risers, stingers, beat-synced sound, or FFmpeg audio mixing to a video clip.
---

# Sound Design For Motion

Use this skill after the visual motion beats are defined and before final delivery. The goal is not to add random audio; it is to make motion feel physical, timed, and intentional.

## Core Principle

Sound is motion hierarchy in audio form.

Every sound must answer:

- What visual beat does it support?
- Should it feel sharp, heavy, digital, soft, or cinematic?
- Does it improve focus, or does it clutter the clip?

## Required Workflow

1. Read the clip's style layer, motion direction, beat map, GSAP labels, rendered video timing, and any narration/TTS audio.
2. If narration/TTS audio exists, run ASR first and extract sentence or phrase timestamps. Use those timestamps as the main timing skeleton.
3. If no narration audio exists yet, use the script or estimated read timing, and mark the timing as estimated until final TTS arrives.
4. Design the sound hierarchy first: narration, bed, transition, micro-feedback, accent hit, final lock, and silence.
5. Choose a sonic identity as a reference constraint, not a hard filter. Style should guide timbre and restraint, but the actual selection must serve the motion beat.
6. Mark audio beats by visual density and narration density. A quiet 5-8 second clip may need 2-4 cues; a busy motion-graphic clip may need 5-9 cues plus a very low bed.
7. Choose SFX by visual job:
   - `whoosh`: movement, swipe, card entry, camera push.
   - `impact`: number hit, product reveal, title lock, hard cut.
   - `ui_click`: button press, panel open, HUD tick, small state change.
   - `stinger`: scene transition, notification, final signal, section marker.
   - `glitch/digital`: scan, error, data flicker, broadcast interruption.
8. Keep levels conservative. For narrated clips, make speech the primary track and place SFX below it. Start around `0.08-0.42` for common cues, higher only for true hero hits, and use a limiter.
9. Mix narration and SFX into the MP4 with FFmpeg, keeping the video stream copied when possible.
10. Save original silent video as `*.silent.mp4` before overwriting.
11. Verify every final MP4 has an audio stream with `ffprobe`.
12. Update any HTML gallery that had `muted` on `<video>` tags if the user should hear audio.
13. Record source/license metadata for downloaded SFX.

## Default Asset Pattern

For this project, prefer local assets in:

```text
clips-lab/assets/sfx/
```

Use `pixabay-sfx-manifest.json` or equivalent source manifests to check:

- filename
- source page
- license
- intended category
- suggested use

## Sound Design Before Style

Style is a reference factor, not the primary selection rule. The primary rule is sound design:

- **Narration:** Is there a speech/TTS track? If yes, ASR it first and let phrase timing drive the visual/audio beat map.
- **Bed:** Should the clip have a low ambience, texture, or air bed? Use this to prevent empty motion, but keep it quiet.
- **Motion feedback:** What small movements deserve ticks, swishes, page sounds, UI clicks, or marker cues?
- **Transitions:** What cuts, screen changes, match cuts, or camera moves need whoosh, slice, stinger, or air movement?
- **Accent hits:** Which 2-5 moments carry the main impact? Do not make every cue a hit.
- **Final lock:** What sound makes the final frame feel resolved?
- **Silence:** Which holds should stay quiet so text can breathe?

After this hierarchy is clear, use sonic identity to pick or process the assets.

## Narration / TTS Handling

For narrated clips:

- Run ASR on the final speech file before the final render.
- Use phrase boundaries to place screen changes, major reveals, and final lockups.
- Write the transcript timing into `DESIGN.md` as `ASR/TTS beat map`.
- Keep SFX under narration unless the moment is intentionally a transition before or after a phrase.
- Do not place loud impacts in the middle of important spoken words.
- If the speech duration is shorter than the original visual plan, retime the visual plan to the speech instead of leaving long empty holds.
- If the speech file may arrive later, mark audio timing as `estimated` and revisit after TTS generation.

For non-narrated clips:

- Skip ASR.
- Use the motion beat map, music grid, or SFX rhythm as the timing skeleton.

## Sound Style Selection

Sound should differentiate video types as clearly as color or typography:

- **Inspirational / emotional:** soft whooshes, warm rises, restrained low hits, long air, fewer UI clicks. Avoid harsh single-frequency beeps and busy tech ticks.
- **AI / SaaS product:** precise UI clicks, digital whooshes, controlled impacts, clean stingers.
- **Brand / lifestyle:** editorial stingers, poster hits, energetic cuts, less HUD-like detail.
- **Data story:** heavy metric impacts, short ticks, broadcast-style punctuation.
- **Explainer / news:** sharp stingers, quick lower-third cues, restrained glitch bursts.
- **Luxury / premium:** low-volume cinematic hits, soft material whooshes, lots of silence.

## Sonic Identity Layer

Before mixing, write this before choosing assets:

```text
sonic_identity:
  emotional tone:
  material metaphor:
  transient shape:
  space:
  allowed SFX families:
  forbidden SFX families:
  density:
  loudest moments:
```

Rules:

- Do not reuse the previous clip's whoosh/hit/click palette just because the timestamps changed.
- If two clips share the same assets, transform the identity through filtering, trimming, spacing, and hierarchy: dry vs roomy, short vs tailed, soft vs percussive, mono vs wide.
- A brand poster clip should not sound like a SaaS interface; an inspirational clip should not sound like a data broadcast package.
- The final mix must be explainable in one sentence, e.g. "dry print-stamp impacts and paper slices," not "some whooshes and hits."
- If the available local SFX pack is too generic, use restrained filtering and layering to create a clear material identity rather than adding more of the same.
- Do not under-score a clip just to preserve style purity. If the motion is active, add enough micro-feedback and transition texture for the motion to feel physical.

## Beat Map Template

Before mixing, write or infer:

```text
clip:
  0.00s setup / ambient tick
  0.40s title or object entry -> whoosh
  0.90s hero reveal -> impact
  1.40s UI/data state change -> click or interface cue
  2.20s lockup or transition -> stinger or low hit
```

## Mixing Details

For concrete FFmpeg patterns, audio timing rules, verification commands, and reusable script structure, read [SFX-MIXING.md](SFX-MIXING.md).

## Quality Bar

A good sound pass should:

- Make the first second feel more alive.
- Reinforce the biggest visual beat.
- Give active motion enough tactile feedback to avoid feeling empty.
- Leave room between sounds.
- Avoid harsh clipping or constant loudness.
- Still work if the viewer watches once without headphones.
- Preserve a silent backup.

## Anti-Patterns

- Do not add one sound to every GSAP tween.
- Do not use long music beds unless the user asks for music.
- Do not let impacts cover text readability moments.
- Do not overwrite original videos without a backup.
- Do not use assets with unclear license or missing source page.
- Do not reuse the previous clip's sound palette without checking whether the new topic needs a different sonic identity.
- Do not use synthetic noise/beeps as a final sound pass when licensed local SFX assets are available.
- Do not make every clip a variation of the same whoosh + hit + click stack.
