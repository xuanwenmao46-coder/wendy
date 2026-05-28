---
name: aesthetic-layout-direction
description: Translates web design schools (25 named recipes anchored on real designers and studios) into video-native design tokens for motion-graphic clips, brand films, product launches, and data stories. Use when the clip needs a specific aesthetic anchor beyond generic labels like "Premium Launch" or "Editorial Tech", when two consecutive clips feel visually indistinguishable, when the user references a named designer/studio/brand as inspiration, or when high-end-video-design returns a vague or AI-generic palette. This skill runs as Step 4.5 in flagship-video-director, after the Aspect Ratio Gate and before the Style Selection Layer. Dependencies: web-design-engineer.
dependencies: [web-design-engineer]
---

# Aesthetic Layout Direction

Use this skill to bridge the web design system's 25 named recipes into video-native design tokens. The output of this skill feeds directly into `high-end-video-design`, `motion-graphic-design`, `typography-selection`, and `sound-design-for-motion`.

## Core Principle

Generic labels produce generic output. A design school anchored on a named designer or studio produces specific results.

Kenya Hara editorial minimalism is not the same as "minimalist premium." Pentagram typographic authority is not the same as "bold editorial." Field.io kinetic identity is not the same as "motion-forward." Bloomberg Terminal data density is not the same as "data-driven." Mailchimp warm humanism is not the same as "friendly and approachable."

When the brief says "premium", the agent picks black/cyan/gradient — every time. When the brief says "Aesop chamois register with serif-body and amber-rule accent", the agent has no room to be generic.

Named anchors constrain the output space. Constrained output spaces produce better clips.

## Position in the Director Workflow

This skill runs as **Step 4.5** in `flagship-video-director`:

```
Step 4.  Aspect Ratio / Responsiveness Gate
Step 4.5 ← AESTHETIC LAYOUT DIRECTION (this skill)
Step 5.  Style Selection Layer
Step 6.  video_ad vs moving_slide decision
...
```

Run this skill after the canvas size and ratio are locked, and before writing any palette, font, or motion choices into `DESIGN.md`. The tokens produced here replace the vague adjectives that would otherwise drive the Style Selection Layer.

## The Six Video Schools

### School 1 — Information Architecture
**Video register: Data Authority / Broadcast**

Anchored on Pentagram/Paula Scher, Edward Tufte, Bloomberg Terminal, and Massimo Vignelli's Swiss-grid discipline. In video, this school asserts authority through typographic scale and data density rather than mood or emotion. The frame is organized, not decorated. Typography does the heavy lifting — a single bold grotesque at hero scale, or monospaced tabular data that fills the panel. Color is used to encode meaning, not to create atmosphere. Motion is institutional: baseline slides, data hits, metric counts, lower-third snaps. The soundtrack is percussive and dry — a broadcast scoreboard thud, not a cinematic swell. Best for: data stories, financial product demos, broadcast packages, B2B brand films where "we know our numbers" is the message.

### School 2 — Editorial / Minimalist
**Video register: Premium Launch / Quiet Luxury**

Anchored on Kenya Hara/MUJI, Apple HIG, Aesop, Dieter Rams/Braun, and Monocle magazine. In video, this school achieves impact through restraint — large negative space, a single hero object, serif or refined sans typography at body weight. The frame is never crowded. Product imagery is photographed (or treated as photographed), not rendered as a UI diagram. Color is a palette of near-neutrals: warm off-white grounds, ink foreground, a single amber or sage accent used once per scene. Motion is imperceptible until it isn't — slow reveals at 600–900ms, no bouncy easing, intentional silence between beats. Best for: luxury product launches, high-consideration B2C, premium SaaS, lifestyle brand films where "we are confident enough to be quiet" is the message.

### School 3 — Motion / Experimental
**Video register: Kinetic Brand / Generative**

Anchored on Field.io, Active Theory, and Resn. In video, this school is the most native of all six — it was built for the moving image. The design is the motion: generative type, particle systems, choreographed multi-element entries, camera moves through 3D space, and moments where the entire visual state transforms. Color is bold and procedural — one or two generative hues cycled through hue rotation, electric and saturated against a near-black ground. Typography is a variable font that morphs on its own axes during the sequence. Motion energy is 9–10 out of 10 — long-tail eased curves, expo-out, quintic. Best for: brand films, agency showreels, launch moments, entertainment product trailers, anything where "the visit is the experience" applies to the video.

### School 4 — Brutalist / Raw
**Video register: Brand Drop / Poster Motion**

Anchored on Are.na (Honest Web), Bloomberg Businessweek Turley-era, and Balenciaga post-2017. In video, this school weaponizes the hard cut and the oversized type as image. The headline sets at 200px+ and bleeds past the safe area. Color is signal-aggressive — alert orange, signal yellow, blueprint blue on white, or dead Helvetica black on white with no decoration. Motion is jarring, not smooth: slam cuts, type that snaps into place with no ease, frames that hold uncomfortably long or cut uncomfortably fast. Silence is used as a weapon, not as luxury. Best for: fashion brand drops, editorial title sequences, counter-culture product launches, anything that needs to feel like it does not care whether you like it.

### School 5 — Warm Humanist
**Video register: Inspirational / Lifestyle / Educational**

Anchored on Mailchimp Freddie era, Stripe Press, and Headspace. In video, this school earns trust through warmth, texture, and human imperfection. Mailchimp's register uses hand-drawn illustration, warm yellow, and personality in every caption. Stripe Press's register uses book-object photography, wide-set serif italic, and cream grounds that feel like paper. Headspace's register uses soft pastels, breathing animations, and rounded everything. Motion is gentle — bouncy only when joyful, never harsh. Micro-feedback is soft: paper rustle, soft air, airy swells. Best for: educational content, community product launches, wellness brands, creator tools, anything where "we are on your side" is more important than "we are the best."

### School 6 — Modern Tool / Builder SaaS
**Video register: Product Demo / Technical**

Anchored on Linear, Vercel, Raycast, and Notion pre-AI. In video, this school is the canonical product demo register — dark-ground UI, hairline borders, keyboard-shortcut chips, the actual product UI as the hero object. Linear's register is warm-dark and restrained. Raycast's register adds glass and per-extension color. Notion pre-AI's register is structured blocks with editorial breathing room. Motion is snappy but not bouncy: cubic-bezier(0.22, 1, 0.36, 1), 350–450ms for layout moves, 150ms for micro-feedback. The product performs a visible action in every beat. Best for: product demos, onboarding films, feature launches, app trailers where the audience needs to see the tool work.

## Required Workflow

1. **Identify the clip context.** Read the clip's topic, audience, emotional register, and video type from the director brief. Note whether it is a product demo, brand film, data story, inspirational, explainer, or launch clip.

2. **Check for a named anchor.** Has the user or brief named a designer, studio, brand, or specific recipe (e.g., "Kenya Hara feel", "Pentagram-style typography", "like Linear's launch video", "Mailchimp warmth")? If yes, map that name directly to a school and recipe. Skip step 3.

3. **Propose three schools if no anchor exists.** Present three candidate schools with one sentence of reasoning each. Ask the director to choose, or make a recommendation with justification. Do not proceed with a school that has not been confirmed.

4. **Load the web recipe.** Read the corresponding recipe file from `web-design-engineer/references/style-recipes/`. Extract: palette hex values, typography weights and roles, spacing rhythm, radius character, motion easing, and signature moves.

5. **Translate to video tokens.** For each web recipe value, produce a video-native equivalent using the translation rules in this document and the school-specific mappings in [STYLE-SCHOOL-MAP.md](STYLE-SCHOOL-MAP.md). Web tokens are for screen layout; video tokens are for 1280x720 or 3840x2160 rendered frames at 30fps.

6. **Write to the brief.** Write the full output contract block below into the director brief. This block is the single source of truth for all downstream skills.

7. **Pass tokens to downstream skills.** The output contract is read by:
   - `high-end-video-design` → palette, composition posture, negative space intent
   - `motion-graphic-design` → motion posture, forbidden motion patterns, energy level
   - `typography-selection` → typography voice, weight contrast, size guidance
   - `sound-design-for-motion` → sonic character, material metaphor, forbidden sounds

## School Selection Rules

**Rule 1 — Match the emotional job, not the surface feel.**
A product that looks "premium" might need School 6 (trust through product visibility) rather than School 2 (trust through restraint). Ask: does the clip need to *show* the product working, or *suggest* the product's character? Showing → School 6. Suggesting → School 2.

**Rule 2 — Data volume determines school.**
If the clip carries 5+ data points, charts, metrics, or comparison tables, default to School 1. Data in any other school gets overwhelmed by the visual style. Tufte's principle: the chart should be the page.

**Rule 3 — Motion budget determines school.**
Schools 3 and 4 require motion-first production. Do not assign School 3 (Kinetic Brand) to a clip with a tight time budget or a largely static visual plan. School 3 is the most labor-intensive. If the motion plan is modest, use School 6 with snappy micro-feedback instead.

**Rule 4 — Audience warmth requirement determines school.**
Consumer audiences with a care or wellness positioning require School 5. Technical audiences with a builder identity require School 6. Creative/cultural audiences may take School 4. Institutions and B2B require School 1 or 2. When in doubt, School 2 is the safest elevation move; School 5 is the safest warmth move.

**Rule 5 — Forbidden cross-contamination.**
Do not mix:
- School 1 (Data Authority) palette with School 5 (Warm Humanist) motion style. Amber terminal type should not breathe like Headspace circles.
- School 3 (Kinetic Brand) particle systems with School 2 (Quiet Luxury) negative space. Generative motion fills space; quiet luxury requires it empty.
- School 4 (Brutalist) type scale with School 6 (Builder SaaS) UI chrome. Oversized Druk type does not sit inside a hairline-border panel.
- School 6 (Tool Demo) with School 2 (Quiet Luxury) unless the product is explicitly positioned as quiet premium software (Linear is the one exception).
- Any school with gradient-text, neon glow, or centered-stack-of-cards unless the school explicitly permits it. None of the 6 do.

## Web-to-Video Token Translation

Web recipes specify values for screen layout (96dpi, scrollable, interactive). Video requires different values for rendered frames (1280x720 or 3840x2160, 30fps, non-interactive).

| Web value | Video translation rule |
|---|---|
| Font size px (web body 16–18px) | Scale ×2.2 for 1280×720; ×4.4 for 3840×2160. Body → 36–40px at 720p. |
| Display size (web 48–80px) | Video display: 72–140px at 720p; 200–280px at 4K. |
| Spacing rhythm (web 8/16/24/40) | Multiply by 2 at 720p: 16/32/48/80. Scale ×4 for 4K. |
| Border-radius (web 6–16px) | Halve for video where visible; often 0 or 4px at 720p. |
| Animation duration (web 150–450ms) | Use directly for micro-feedback; multiply ×1.3 for main reveals at 30fps. |
| Web easing cubic-bezier(0.22,1,0.36,1) | Direct GSAP equivalent; map to `expo.out` or `power4.out`. |
| Web opacity transitions | Use as-is; pair with GSAP `autoAlpha` not CSS `opacity`. |
| Web color (sRGB) | Use directly; verify contrast at 720p render size. Darken bg by 5% for video gamma. |

## Output Contract

After identifying the school and anchor, write this block into the director brief:

```markdown
## Aesthetic Layout Direction

**Design school:** [School N — Name]
**Named anchor:** [e.g., Kenya Hara/MUJI or Field.io or Bloomberg Terminal]
**Why this school:** [1–2 sentences: why this school fits this clip's topic, audience, and emotional job]
**Web recipes referenced:** [filenames, e.g., muji-kenya-hara.md, aesop.md]

**Video register:** [e.g., Premium Launch / Quiet Luxury]

**Palette**
- Background: [hex] — [note, e.g., warm paper off-white, never pure white]
- Foreground: [hex] — [note]
- Accent: [hex] — [note, e.g., used only on single rule or seal mark, <3% of frame]
- Material: [hex] — [note, e.g., surface for panels or cards]
- Forbidden palette moves: [e.g., no gradients, no cyan, no purple glow]

**Typography voice**
- Display: [family, weight, size at 1280×720, role]
- Support: [family, weight, size at 1280×720, role]
- Data/label: [family, weight, size at 1280×720, role]
- Weight contrast: [e.g., 300 vs 800, or 400 only — no bold]
- Letter-spacing: [e.g., -0.02em on display, +0.10em on small-caps labels]
- Forbidden type moves: [e.g., no italic, no condensed, no Inter at default weight]

**Composition posture**
- Grid: [e.g., 12-column with 32px gutters, or asymmetric edge-anchor]
- Hero placement: [e.g., product owns 55–65% of frame, top-left anchor]
- Focal points: [count and roles, e.g., 2: product image + title block]
- Negative space: [target %, e.g., 40–50% intentional empty — not leftover]
- Edge anchoring: [rules, e.g., title pinned bottom-left, metadata top-right]

**Motion posture**
- Entrance style: [e.g., slow fade 600ms ease-out, or slam-cut with no ease]
- Hold duration: [e.g., 1.5–2.5s for primary beats; silence between reveals]
- Transition type: [e.g., baseline slide, mask slice, or instant cut]
- Energy level: [1–10, e.g., 3 — restrained, deliberate]
- GSAP ease: [specific ease, e.g., sine.inOut for ambient; power4.out for hits]
- Forbidden motion: [e.g., no bounce, no spring physics, no parallax, no particle burst]

**Sonic character**
- Material metaphor: [e.g., paper and ink, glass and metal, soft air]
- Transient shape: [e.g., dry snap, soft swell, dry thud, tick]
- Density: [sparse / medium / dense]
- Forbidden sounds: [e.g., no SaaS UI clicks, no cinematic swells, no whooshes]

**Forbidden elements — what would betray this school's DNA in video:**
- [list 4–6 specific betrayals, e.g., gradient text, centered card stack, animated particle background]

**Anti-slop check:**
- Generic AI output would: [describe what a naive model would do]
- This school does instead: [describe the specific, differentiated choice]
```

## Anti-Slop Protocol

Before accepting the output of this skill, verify:

- The palette contains at least one hex value not found in cyan/purple/gradient combinations.
- The typography voice names a specific family and weight, not just "a sans-serif".
- The motion posture specifies a GSAP ease, not just "smooth" or "elegant".
- The sonic character names a material metaphor, not just "cinematic" or "subtle".
- The forbidden elements list contains at least 4 items that are specific to this school, not generic.
- The anti-slop check describes what a naive model would do and how this school differs.

If any of these fields are vague, return to step 4 and reload the web recipe.

## References

- For school-to-video DNA mapping, hex values, typography specs, and composition rules: [STYLE-SCHOOL-MAP.md](STYLE-SCHOOL-MAP.md)
- For video layout patterns and composition templates: [LAYOUT-PATTERNS.md](LAYOUT-PATTERNS.md)
- For video-specific aesthetic audit criteria: [AESTHETIC-AUDIT.md](AESTHETIC-AUDIT.md)
- For raw web recipe source files: `web-design-engineer/references/style-recipes/`
- For overall video production orchestration: `flagship-video-director/SKILL.md`
- For visual style direction and DESIGN.md: `high-end-video-design/SKILL.md`
- For GSAP choreography and beat maps: `motion-graphic-design/SKILL.md`
- For SFX and audio mixing: `sound-design-for-motion/SKILL.md`
- For font selection and embedding: `typography-selection/SKILL.md`
