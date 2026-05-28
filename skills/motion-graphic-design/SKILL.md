---
name: motion-graphic-design
description: Designs energetic motion graphics, kinetic typography, text-block flashes, broadcast-style stingers, dynamic title sequences, emphasis beats, and GSAP choreography for HyperFrames clips. Use when a video feels too PPT-like, static, basic, slow, or lacks motion energy, visual impact, rhythmic emphasis, animated text blocks, or motion-graphic polish.
---

# Motion Graphic Design

Use this after the information structure is clear, but before writing final GSAP code. The job is to turn a good frame into a video with rhythm, impact, and directed attention.

## Core Principle

Motion is hierarchy over time.

Do not simply move every element. Decide what should hit, pulse, snap, smear, reveal, hold, and exit.

For ad-like videos, motion must also create continuity. The viewer should feel one visual event unfolding, not a series of animated presentation pages.

## Required Workflow

1. Identify the emotional tempo: explosive, editorial, broadcast, luxury, technical, playful, or urgent.
2. Mark 3-6 beats in the clip timeline: intro, first hit, detail burst, focus hold, transition, final lock.
3. Decide the hero motion: kinetic type, shape burst, mask reveal, camera push, data hit, or stinger.
4. Split text into blocks, words, or letters only when it improves rhythm.
5. Assign motion intensity by hierarchy: hero words get stronger movement; support text gets quieter motion.
6. Add secondary motion: trailing blocks, echo lines, pulse, overshoot, parallax, or reactive particles.
7. Preserve readable landings: important text should settle for at least 0.5 seconds.
8. Avoid unsafe flashing: do not flash high-contrast full-screen elements faster than 3 times per second.
9. For 15s+ ads, define camera/framing changes and object continuity before implementing scene transitions.
10. Run the motion audit in [MOTION-AUDIT.md](MOTION-AUDIT.md).

## Motion Modules

Use these as composable skill modules:

- **Kinetic Type Hit**: words pop, slide, rotate, or scale into position with staggered emphasis.
- **Text Block Flash**: multiple typographic blocks blink, swap, pulse, or step through like an edit montage.
- **Mask Slice Reveal**: horizontal/vertical masks cut text and panels into the frame.
- **Shape Burst**: lines, blocks, dots, or frames expand from a focal point to create impact.
- **Broadcast Stinger**: fast 0.4-1.0s transition jolt that redirects attention.
- **Lower Third Energy**: compact info overlay with in/change/out animation states.
- **Data Hit**: chart or number lands with a sharp accent, then calms for reading.
- **Match-Cut Transition**: one shared shape, word, or line becomes the next scene.
- **Smear / Stretch Illusion**: fast moving text or shapes stretch briefly during travel, then settle cleanly.
- **Camera Tunnel**: the frame pushes through one object, UI panel, or light aperture into the next beat.
- **Product Behavior Loop**: visible product/UI states keep working between beats: generating, selecting, assembling, rendering, exporting.
- **Object Morph**: a prompt chip becomes a script strip, script strip becomes storyboard, storyboard becomes timeline, timeline becomes final video.

## Diagram / Animation Module Library

For concept, explainer, inspirational, product, and brand videos, choose at least one visual explanation module before coding. Do not rely only on text blocks.

- **Route Map**: a path draws across a map, nodes unlock, labels attach to decisions or milestones.
- **State Machine**: current state changes through labeled states, good for mindset/process transformation.
- **Progress Curve**: line chart, energy curve, confidence curve, or recovery curve animates over time.
- **Node Network**: scattered nodes connect into meaning, useful for complexity-to-clarity stories.
- **Layer Stack**: transparent layers assemble, peel, or align to show structure.
- **Before / After Split**: two states compare, then a divider moves or morphs.
- **Timeline Rail**: beats or actions lock onto a rail with a moving playhead.
- **Dashboard / Meter**: gauges, counters, and small labels visualize internal state.
- **Topographic Map**: contour lines, elevation, route, and marker reveal a journey or challenge.
- **Storyboard Strip**: frames assemble into a sequence, useful for narrative transformation.

Rules:

- Pick modules that match the topic. Inspirational can use route maps, state machines, progress curves, or topographic maps; product demos can use UI assembly, timeline rails, or dashboards.
- Animate the module as the main actor. Text should annotate the module, not replace it.
- Use SVG strokes, masks, `strokeDashoffset`, transforms, and GSAP staggers for precise diagram motion.
- If a clip feels ordinary, add a stronger module before adding more decoration.

## Timing Defaults

- Micro entrance: 0.2-0.4s.
- Main title hit: 0.6-1.2s.
- Stinger: 0.4-1.0s.
- Readable hold: 0.5s minimum for important text; 1.0-2.0s for dense information.
- Detail burst: 3-8 small elements within 0.4-0.9s.
- Final lockup: 0.8-1.5s.

At 30fps, very fast movement should use anticipation, overshoot, blur/smear illusion, or short distance. Long linear travel looks cheap.

For 30s ad clips, avoid 5 equal six-second holds. Prefer uneven rhythm: fast setup, medium transformation, quick montage, short proof, strong final lock.

## Anti-PPT Motion Gate

Before coding, reject motion plans that rely on:

- `scene 1 title + subtitle`, `scene 2 title + subtitle`, repeated for most of the video.
- A wipe or scan plate that merely hides a slide change.
- Static feature cards, orbit cards, or flowchart nodes as the main action.
- Elements entering, holding, and lightly floating with no transformation.
- Text explaining value while graphics only sit beside it.

Upgrade by adding:

- A persistent anchor object that travels through the whole clip.
- At least 2 camera/framing changes that alter scale or viewpoint.
- At least 1 match cut where an object from one beat becomes the next beat.
- At least 1 visible product behavior loop, such as timeline assembly, preview playback, export progress, or UI selection.
- Continuous secondary motion that supports the story, not random particles.

## Text / Action Split

When text covers important action or camera zooms crop content, split the ad into screens instead of forcing one continuous layer stack:

- `text_screen`: 1-2 seconds, large readable punchline, minimal or no product action behind it.
- `action_screen`: 3-6 seconds, product behavior fills the frame, only small labels or captions.
- Keep text outside any container that receives strong camera scale, pan, or rotation.
- Use flash, match cut, object morph, or audio hit to connect screens.
- Never keep a large headline at the top layer while the main animation is trying to perform underneath it.

## Layer Lifecycle Gate

Before coding, every visible module must have a lifecycle:

```text
module_name:
  in:
  hold:
  out:
  next_owner:
```

Rules:

- Do not leave old diagram modules on screen unless they are intentionally dimmed into background context.
- Only one module should be the primary actor at a time: text, map, state machine, curve, product UI, or final lockup.
- If the next beat introduces a new module, the previous module must either exit, collapse into a small background mark, or be replaced by a match cut.
- Text clips and animation clips may alternate. This is preferred when both need full attention.
- A 30s clip should not accumulate all modules until the final frame unless the concept is explicitly "system build-up" and the final composition remains readable.
- In GSAP, implement lifecycle with named functions such as `showScreen`, `hideScreen`, `showModule`, `retireModule`, not only entrance tweens.

Reject the implementation if:

- Multiple large modules remain fully visible and compete for focus.
- A state machine, route map, curve, and large headline are all active at once.
- The timeline adds new layers but has no corresponding `.to(... autoAlpha: 0 ...)`, scale-down, mask-out, or screen switch.

## GSAP Choreography Rules

- Prefer one timeline with named labels: `intro`, `hit`, `burst`, `hold`, `out`.
- Use stagger groups instead of simultaneous fades.
- Combine at most 2-3 transform properties per text unit: position + opacity + scale is enough.
- Use different eases for different roles:
  - `power4.out` or `expo.out` for big type hits.
  - `back.out(1.6)` for controlled overshoot.
  - `steps()` or quick opacity pulses for editorial flashes.
  - `sine.inOut` for ambient motion.
- Build text blocks as separate spans/divs when you need independent timing.
- Keep layout stable; animate transform/opacity/clip-path/masks more than layout properties.

## Kinetic Text Rules

- Animate by block for readability; by word for rhythm; by letter only for short hero words.
- Give key words larger amplitude, color, and timing.
- Use pauses between word reveals to create weight.
- Avoid moving dense paragraphs. Summarize first.
- Text can flicker, but the message must land still.
- For Chinese text, prefer phrase/block animation over per-character chaos unless the word count is very small.

## Output Contract

Before implementation, produce:

```markdown
## Motion Graphic Direction
- Tempo:
- Timeline beats:
- Hero motion:
- Persistent anchor:
- Camera/framing changes:
- Match-cut moments:
- Product behavior loops:
- Diagram/animation modules:
- Layer lifecycle:
- Text split strategy:
- Emphasis words/blocks:
- Secondary motion:
- Transition logic:
- Readability holds:
- Safety limits:
- GSAP labels:
```

## References

- For kinetic type patterns, read [KINETIC-TYPE.md](KINETIC-TYPE.md).
- For reusable motion modules, read [MOTION-PATTERNS.md](MOTION-PATTERNS.md).
- For audit criteria, read [MOTION-AUDIT.md](MOTION-AUDIT.md).
- For slide/information structure, combine with `presentation-video-design`.
- **For text motion velocity limits, CJK blur safety, minimum hold durations, and GSAP ease legibility guide — run `typography-optics/MOTION-STABILITY.md` before finalizing any tween that moves text. Stroke-dense scripts (CJK 900w) require stricter velocity budgets than Latin. Never `linear` on text; never `bounce`/`elastic` at any size.**
