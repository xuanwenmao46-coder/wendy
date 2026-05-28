# Assembly Workflow

Use this workflow when turning a user prompt into a clip.

## 1. Interpret The Prompt

Extract:

- Scenario: product, data, explainer, concept, brand, app, CTA.
- Format: 16:9, 9:16, 1:1, duration, platform.
- Content: title, body, data, image, UI, product, logo, CTA.
- Audio: narration/TTS file, voiceover, music bed, SFX-only, or no audio yet.
- Energy: calm, premium, fast, explosive, experimental.
- Constraints: brand colors, no flashing, commercial safe, specific language.

If something is missing, choose a sensible default and mark it as skippable.

## 1.25 Aspect Ratio / Responsiveness

Before visual style and animation, define:

- Target aspect ratio: `16:9`, `9:16`, `1:1`, `4:5`, or custom.
- Canvas size for the current render.
- Whether the clip is single-ratio or adaptable.
- Safe areas for titles, subtitles, product images, logos, captions, and platform UI overlays.

响应式与自适应 (Responsiveness & Adaptability)

考虑到模板可能需要在不同设备和屏幕尺寸上使用。

- **布局规则 (Layout Rules):** 元素在不同屏幕尺寸下的定位和大小调整方式（例如：居中、靠左、相对父容器的百分比、最小/最大尺寸限制）。
- **断点 (Breakpoints):** 在哪些屏幕宽度下，动画或布局需要进行调整。
- **可变参数 (Variable Parameters):** 哪些参数可以根据外部数据或用户输入进行调整（例如：文本内容、图片源、数据值）。

For reusable templates, write these rules into `DESIGN.md` before implementation. If no alternate ratio is required, explicitly mark `single-ratio`.

### Ratio Adaptation Checklist

When adapting an existing clip to a new ratio:

- Do not only scale, crop, or letterbox the old render.
- For every screen, define the new target-ratio visual center of gravity.
- For every `text_screen`, redesign the typography layout for the new ratio: title size, line breaks, backing plate, side rail, metadata, and negative space.
- For every `action_screen`, redesign hero position, supporting object placement, and motion path.
- Convert horizontal structures:
  - left/right split -> top/bottom stack or center-axis layout.
  - timeline row -> vertical rail, stacked rail, or compressed bottom rail.
  - card row -> vertical sequence, layered stack, or radial cluster.
- Check that no screen has large accidental blank space.
- Write what changed in `DESIGN.md` under `ratio adaptation`.
- Render to a separate directory or filename unless the user explicitly asks to overwrite.

## 1.5 Narration / ASR Timing

This step is conditional:

- If the user provides narration, TTS, voiceover, or any speech audio file, run ASR before designing the final timeline.
- Extract sentence or phrase timestamps and use them as the main timing skeleton.
- Write the result into the director brief and `DESIGN.md` as `ASR/TTS beat map`.
- Build visual clip boundaries around phrase starts, phrase ends, and meaningful pauses.
- If no audio exists yet but a script exists, estimate timings and mark them as `estimated`.
- If final TTS is generated later, rerun ASR and retime the visual timeline before final render.
- If the clip is not narrated, skip ASR and use the motion beat map.

## 2. Choose The Clip Job

Pick one:

- Hook: attract attention in the first second.
- Explain: make an idea understandable.
- Prove: show data or evidence.
- Sell: make a product/feature desirable.
- Brand: create a memorable visual identity.
- Transition: connect scenes.
- Close: lock the message and CTA.

## 3. Build The Director Brief

Use:

```markdown
## Flagship Video Direction
- Scenario:
- Audience:
- One-sentence concept:
- User value:
- Primary visual:
- Aspect ratio:
- Layout rules:
- Breakpoints:
- Variable parameters:
- Text strategy:
- Motion strategy:
- Narration/TTS timing:
- Sound strategy:
- Beat map:
- Style register:
- Inputs needed:
- Skippable inputs:
- Final lockup:
- RAG tags:
- Anti-patterns to avoid:
```

## 4. Select Modules

Choose:

- `scene_job`: hook, title, data_story, feature, explainer, metaphor, outro.
- `visual_register`: broadcast, cinematic, techno_luxury, poster_motion, data_terminal, brutalist, editorial.
- `motion_pattern`: kinetic_type_hit, flash_stack, product_summon, data_hit, mask_slice, shape_burst, smear, match_cut.
- `timing_profile`: single_hit, burst_hold, stinger_cut, beat_sequence, in_change_out.
- `content_module`: big_number, product_core, UI_cards, keyword_stack, network_system, brand_word.

## 5. Design Beat Map

Default 7s flagship structure:

- 0.00-0.35: setup or anticipation.
- 0.35-1.20: first hit.
- 1.20-2.20: burst/detail reveal.
- 2.20-3.80: readable hold/development.
- 3.80-5.20: second switch or emphasis.
- 5.20-7.00: final lockup.

For short clips, compress but keep at least: hit -> hold -> lockup.

For narrated clips, replace the default timing profile with the ASR/TTS beat map. Do not force a 30s template if the narration is 19s or 23s; match the delivered audio and leave only a short final hold when needed.

## 6. Implement

For HyperFrames:

- Use local `gsap.min.js`.
- Use `gsap.timeline({ paused: true })`.
- Assign `window.__timelines.root = tl`.
- Keep timed elements stable with `id`, `class="clip"`, `data-start`, `data-duration`, `data-track-index`.
- Use CSS variables or named constants for layout values that may change across aspect ratios.
- Document breakpoint-specific position, scale, and font-size changes when the template is adaptable.
- Avoid external network assets during render.
- Use CSS/SVG-generated visuals when no assets are provided.

## 7. Verify

- Run HyperFrames lint.
- Fix all errors and warnings when practical.
- Render preview MP4.
- If narration exists, verify final video duration against the narration duration and confirm the audio stream exists.
- If adaptability was promised, check that layout rules, breakpoints, and variable parameters are documented.
- If this is a ratio adaptation, verify that each text/action screen was re-composed rather than only scaled or cropped.
- Add gallery entry when making multiple clips.
- Write RAG metadata if the clip is useful as a seed.
