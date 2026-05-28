---
name: flagship-video-director
description: Directs high-end, highly stylized video clips by assembling scene strategy, presentation design, motion graphics, sound design, typography, image direction, flagship references, and RAG-ready metadata. Use when creating any new video clip, flagship sample, fancy product video, motion-graphic ad, data story, explainer, brand drop, app demo, or when the user wants extreme style, strong motion, sound effects, creative direction, or production-ready video prompts.
---

# Flagship Video Director

Use this as the top-level skill for creating videos. It orchestrates the other skills and turns a user prompt into a strong clip direction before implementation.

## Mission

Make clips that feel designed, not generated.

The clip must have:

- A real user scenario.
- One strong visual concept.
- A clear information hierarchy.
- A continuous visual event, not a sequence of decorated slides.
- A memorable motion idea.
- A sound-design pass when the output is a rendered MP4 or gallery preview.
- A final lockup that can be paused and understood.
- RAG-ready metadata for future reuse.

## Required Workflow

1. Parse the user prompt into scenario, content, audience, format, and desired energy.
2. Choose one primary scenario from [SCENARIO-PLAYBOOK.md](SCENARIO-PLAYBOOK.md).
3. Select a flagship reference direction from [FLAGSHIP-REFERENCES.md](FLAGSHIP-REFERENCES.md).
4. Run the Aspect Ratio / Responsiveness Gate below before layout, style, or animation decisions.
4.5. Apply `aesthetic-layout-direction` to anchor the visual school before any style or palette decisions. If the user names a designer, studio, or brand as aesthetic reference (e.g., "Aesop-feeling", "Linear-style", "Bloomberg data authority"), map directly to that school. Otherwise, present 3 schools from different design territories as differentiated directions and let the user choose. Translate the chosen school's DNA into video-native design tokens (palette, typography voice, composition posture, motion posture, sonic character) before step 5.
5. Run the Style Selection Layer below before writing `DESIGN.md` or code. Style selection must be grounded in the design school established in step 4.5; all palette, typography, and sonic choices must trace back to the named anchor's DNA, not to generic labels.
6. Decide whether the output is a `moving_slide` or a `video_ad`. For 15s+ product intros, brand ads, launch films, and social ads, default to `video_ad`.
7. For `video_ad`, write the continuous event first: what object/system changes from second 0 to the final lockup.
8. Apply `presentation-video-design` only for information hierarchy, not as the scene structure.
9. Apply `high-end-video-design` to define visual register and anti-slop constraints.
10. Apply `typography-selection` before final font choices.
11. Apply `image-art-direction` if the clip uses product images, screenshots, people, icons, video materials, or downloaded assets.
12. When images or video materials are used, classify each one as `full-screen atmosphere material` or `image information material` before layout.
13. If narration/TTS/audio is provided or expected, run the Narration Timing Gate below before finalizing the beat map.
14. Apply `motion-graphic-design` to define beats, kinetic type, stingers, bursts, holds, and final lockup.
15. Apply `sound-design-for-motion` when the clip will be rendered, previewed, or delivered as MP4; map SFX cues around narration and motion beats.
16. Run the Video-First Gate below before implementation.
17. Produce the director brief using the output contract below.
18. Implement only after the brief is coherent.
19. Run the quality bar in [QUALITY-BAR.md](QUALITY-BAR.md).
20. Write or update RAG seed metadata using [RAG-METADATA.md](RAG-METADATA.md) for valuable clips.

## Composition Formula

Every clip is assembled from these slots:

```text
Scenario + Content Module + Visual Register + Motion Pattern + Timing Profile + Final Lockup
```

Examples:

```text
product_launch + product_summon + techno_luxury + scan_burst + burst_hold + logo_lockup
data_story + big_number + sports_broadcast + data_hit + impact_hold + metric_lockup
brand_drop + oversized_type + poster_motion + mask_slice + stinger_cut + word_lockup
```

## Aspect Ratio / Responsiveness Gate

Use this gate for every clip because templates may need to work across devices and screen sizes.

Before style, layout, or animation:

- Choose the target aspect ratio and canvas size: `16:9`, `9:16`, `1:1`, `4:5`, or custom. If the user does not specify, default to `16:9` for gallery/desktop previews and note that other ratios are not guaranteed.
- Define safe areas for text, product images, captions, subtitles, and final lockup. Account for platform UI overlays when relevant.
- Decide whether the clip is single-ratio only or adaptable across ratios.

响应式与自适应 (Responsiveness & Adaptability)

考虑到模板可能需要在不同设备和屏幕尺寸上使用。

- **布局规则 (Layout Rules):** 元素在不同屏幕尺寸下的定位和大小调整方式（例如：居中、靠左、相对父容器的百分比、最小/最大尺寸限制）。
- **断点 (Breakpoints):** 在哪些屏幕宽度下，动画或布局需要进行调整。
- **可变参数 (Variable Parameters):** 哪些参数可以根据外部数据或用户输入进行调整（例如：文本内容、图片源、数据值）。

Implementation requirements:

- Prefer ratio-aware CSS variables for core layout values: margins, title width, object scale, focal point, safe area, and font sizes.
- Avoid hard-coding all positions if the clip is intended as a reusable template.
- For HyperFrames, the root canvas can be fixed for render, but the design brief must state how to adapt it to other target ratios.
- If animation paths depend on absolute pixel positions, document how they should change at each breakpoint.

## Aspect Ratio Adaptation Gate

Use this gate whenever adapting an existing clip from one ratio to another, especially `16:9` -> `9:16`.

Rules:

- Do not treat adaptation as scale-and-crop. Re-compose the clip for the target ratio.
- Each `screen` must define a new visual center of gravity for the target ratio.
- Each `text_screen` must have a target-ratio typography plan: title scale, line breaks, backing plate, side rail, metadata, decorative type, and intended negative space.
- Large empty space must be intentional. If a text page has more than roughly 35-40% unused blank area with no structural role, redesign it.
- Each `action_screen` must reposition the hero object, supporting objects, and motion path for the target ratio.
- Horizontal modules must be redesigned:
  - left/right split -> top/bottom stack, center-axis layout, or card-over-hero layout.
  - horizontal timeline -> vertical rail, stacked timeline, or compressed bottom rail.
  - feature-card row -> vertical sequence, carousel stack, or radial cluster.
  - wide preview/product frame -> portrait-safe crop or centered card with supporting labels.
- Text and action can change screen order if the target ratio needs it. Preserve story logic, not the original spatial arrangement.
- Re-audit final lockup, captions, subtitles, and CTA for the target platform safe area.
- If the adapted clip is rendered as a separate file, create a separate directory or filename. Do not overwrite the source ratio unless explicitly requested.

Reject the adaptation if:

- The target-ratio version is produced only by scaling the old canvas.
- Text pages look like small blocks floating in a tall empty canvas.
- A horizontal timeline, card row, or split layout is kept unchanged in portrait.
- The old animation paths send elements out of frame or leave the main action too small.
- The design brief does not state what changed for the new ratio.

Reject the brief before coding if:

- It assumes `1280x720` but claims to be a reusable template without layout rules.
- Important text, subtitles, or product objects would be cropped in `9:16`, `1:1`, or platform-safe areas.
- Variable text length, image source, data value, or logo size can break the layout and no min/max constraints are specified.

## Style Selection Layer

Before designing or coding, choose a style system from the clip's topic, type, audience, and emotional job. Do not reuse the last clip's palette, font, motion, or SFX just because it worked once.

Select and write down:

- **Theme category:** product intro, brand ad, inspirational, explainer, data story, app demo, fashion/lifestyle, education, cinematic trailer, or other.
- **Emotional register:** confident, urgent, warm, cinematic, playful, premium, brutal, editorial, calm, mysterious, rebellious, or technical.
- **Color palette:** background, foreground, accent, material color, and forbidden colors. Palette must fit the theme. Example: inspirational may use warm dawn/paper/film grain; AI product may use precise cyan/metal; fashion may use hard poster colors.
- **Visual language:** photographic, abstract metaphor, UI machinery, editorial poster, broadcast package, cinematic landscape, data interface, collage, hand-crafted paper, or luxury material.
- **Typography voice:** display style, support style, metadata style, weight contrast, and whether text should feel literary, technical, loud, soft, premium, or institutional.
- **Diagram / animation modules:** the visual explanation primitives used by the clip, such as route map, state machine, before/after split, timeline, node network, orbit system, progress curve, matrix, stacked layers, dashboard, storyboard strip, or topographic map.
- **Motion language:** kinetic type, camera path, object morph, match cut, montage, slow reveal, stinger cuts, UI assembly, data hit, or organic flow.
- **Sound language:** cinematic hits, soft organic whooshes, UI clicks, editorial stingers, glitch/digital, warm risers, low trailer pulses, or restrained ambience.
- **Sound design hierarchy:** bed/air, micro-feedback, transition cues, accent hits, final lock, and intentional silence.
- **Sonic identity:** the reference sound material, transient shape, density, space, and forbidden cues. Sonic identity guides timbre; it must not override what the motion beat needs.

Style selection must create differentiation:

- A motivational video should not automatically look like a SaaS product launch.
- A brand ad should not automatically use the same black/cyan HUD system as an AI tool.
- A calm or emotional clip should not be scored like a hard tech demo.
- If two consecutive clips share the same palette, typography, and sound profile, justify it explicitly or redesign one layer.
- If two consecutive clips use the same whoosh/hit/click palette, redesign the sonic identity even if the visual timing changed.
- If a clip feels empty, increase micro-feedback, transition texture, or a low bed before blaming the visual design.
- If the clip uses multiple diagram modules, define which module owns each time range and how the previous module exits.

Reject the brief before coding if:

- The style choices are generic words like "high-end", "cinematic", or "tech" without a named design school, concrete palette, typography, visual, and sound decisions.
- A design school was named (e.g., "minimalist") but the palette, motion posture, or sonic character belong to a different school (e.g., minimalist claim + kinetic type burst + heavy UI click sounds = contradiction).
- The chosen school's forbidden elements appear in the brief (e.g., Editorial/Minimalist clip with a neon accent or dense card grid).
- The palette is only a dark gradient plus glow.
- The font choice is only a local fallback without a voice rationale.
- The clip has no diagram, object behavior, illustration, photographic subject, or animation module beyond text cards.
- The brief introduces multiple large modules but does not define a lifecycle or screen/clip alternation plan.
- The sound plan is "add SFX" rather than a specific sonic style matched to motion beats.
- The sound plan only lists timestamps and generic assets, without a sonic identity or forbidden cues.
- The sound plan uses style as a hard filter and leaves active motion under-scored.

## Video-First Gate

Use this gate for 15s+ product intros, brand ads, social ads, launch clips, and anything the user says should feel less like PPT.

Before implementation, answer:

- What is the continuous event? Example: messy inputs are absorbed by a product engine and emitted as a finished video.
- What changes on screen every 2-4 seconds without becoming a new slide?
- Which object persists across beats as the viewer's anchor?
- What are the camera moves or framing changes: push-in, pull-back, crop, orbit, tunnel, macro detail, or reveal?
- Which transition is a match cut or object transformation, not a wipe hiding a slide change?
- What product behavior is visible: UI generating, timeline assembling, render progress, preview playback, export, scan, or selection?

Reject the brief before coding if it has:

- 4-6 separate pages with title/subtitle/card layouts.
- The same left-title/right-object composition in most beats.
- A flowchart, timeline, or feature cards as the main scene for more than 3 seconds.
- Text explaining the product while the visual only decorates it.
- Entrance animations followed by long static holds.
- Large text permanently layered above action footage or product motion.
- Global camera scale applied to a parent that also contains readable text.

For long ads, it is acceptable and often better to cut between clips/screens:

- Use `text_screen` for 1-2 second punchlines.
- Use `action_screen` for 3-6 second product behavior or metaphor motion.
- Do not force a one-take composition if it causes text/action collisions.
- Text screens and action screens should have separate safe areas and separate animated containers.
- If zooming, zoom only the action container; keep text containers independent and unscaled.
- For diagram-heavy clips, use alternating `text_clip` and `diagram_clip` beats when readability would suffer from stacking.
- Every major module must have an exit: fade out, scale down, mask out, collapse into background, or transition into the next module.

## Narration Timing Gate

Use this gate whenever the clip has, may have, or will later receive narration, TTS, voiceover, podcast audio, or a user-provided speech file.

Before locking the visual beat map:

- If a narration/TTS audio file exists, transcribe it first with ASR and extract sentence or phrase timestamps.
- Treat ASR timestamps as the primary timing skeleton for narrated clips. Visual beats should land on phrase starts, phrase ends, or meaningful pauses.
- Write the transcript timing into `DESIGN.md` as an `ASR/TTS beat map`.
- Retiming the visual timeline is preferred over stretching or cutting narration awkwardly.
- If no narration audio exists yet, design from the script with estimated timings, but mark the beat map as `estimated`. When final TTS arrives, rerun ASR and update the visual timeline before final render.
- If the clip has no narration and is purely music/SFX-driven, skip ASR and use the motion beat map as the timing skeleton.

Reject the brief before coding if:

- A provided speech file is ignored and the visual timeline is still based only on a guessed duration.
- The final MP4 uses narration but `DESIGN.md` has no transcript timing or voiceover beat map.
- SFX are placed by style timestamps instead of around the spoken phrase boundaries and visible motion.

## Default Creative Bias

When the user asks for "fancy", "有审美", "motion graph", "主打", "高级", or "更炸":

- Prefer a bold flagship concept over a safe template.
- Use fewer elements with stronger roles.
- Make text participate in motion.
- Give the first second a hit moment.
- Use at least 3 timeline beats.
- Avoid PPT-like slow reveals unless the user asks for calm luxury.
- For ads, make the product or metaphor perform an action. Do not let typography carry the whole pitch.

## Director Brief Output

Before implementation, write:

```markdown
## Flagship Video Direction
- Scenario:
- Audience:
- One-sentence concept:
- User value:
- Primary visual:
- Continuous event:
- Camera/framing strategy:
- Product behavior:
- Aspect ratio:
- Responsiveness/adaptability:
- Layout rules:
- Breakpoints:
- Variable parameters:
- Image/video material roles:
- Asset placement strategy:
- Design school:
- Named anchor(s):
- Style layer:
- Palette:
- Visual language:
- Typography voice:
- Diagram/animation modules:
- Clip/module lifecycle:
- Text strategy:
- Motion strategy:
- Narration/TTS timing:
- Sound design hierarchy:
- Sonic identity:
- Sound strategy:
- Beat map:
- Style register:
- Inputs needed:
- Skippable inputs:
- Final lockup:
- RAG tags:
- Anti-patterns to avoid:
```

## Implementation Rules

- For HyperFrames, register a deterministic timeline on `window.__timelines.root`.
- Prefer GSAP timelines with labels: `intro`, `hit`, `burst`, `hold`, `switch`, `lockup`.
- Do not rely on external CDN assets for rendering; use local assets or CSS/SVG-generated visuals.
- Each timed element should have stable `id`, `class="clip"`, `data-start`, `data-duration`, and `data-track-index`.
- Run HyperFrames lint and fix errors/warnings before final render.
- Render a preview MP4 and place it in a gallery page when creating multiple clips.
- If adding sound, preserve silent source MP4s as `*.silent.mp4`, mix SFX with FFmpeg, verify audio streams with `ffprobe`, and remove `muted` from gallery videos when the user should hear sound.

## References

- For scenario patterns, read [SCENARIO-PLAYBOOK.md](SCENARIO-PLAYBOOK.md).
- For flagship examples, read [FLAGSHIP-REFERENCES.md](FLAGSHIP-REFERENCES.md).
- For assembly workflow, read [ASSEMBLY-WORKFLOW.md](ASSEMBLY-WORKFLOW.md).
- For quality scoring, read [QUALITY-BAR.md](QUALITY-BAR.md).
- For RAG metadata, read [RAG-METADATA.md](RAG-METADATA.md).
- **For anchoring the visual aesthetic to a named design school before style decisions, use `aesthetic-layout-direction`.**
