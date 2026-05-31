---
name: aesthetic-governor
description: Top-level aesthetic governance layer that intercepts every video production pipeline before any design decision is made. Establishes unified visual language through 6 sequential directors (Creative, Art, Typography, Color, Motion, Photography/Cinematography), enforces museum-level quality standards, mandates physical imperfection against AI smoothness, and produces an Aesthetic Governor Brief that all downstream skills must honor. Run as Step 4.0 in flagship-video-director, after canvas/ratio lock and before aesthetic-layout-direction, style selection, or any font/color/motion choices. Without this layer, AI agents default to generic output; with it, every visual decision is intentional, defensible, and benchmarked against the finest references in design history.
dependencies: [aesthetic-layout-direction, high-end-video-design, typography-selection, motion-graphic-design]
---

# Aesthetic Governor System

## Mission

No random visual decisions are allowed. Every frame, cut, typographic choice, color relationship, and motion easing must be traceable to an intentional creative decision made before the first line of code is written. The Aesthetic Governor exists because AI generation systems are statistically correct but aesthetically undirected: they produce outputs that are technically coherent and visually average. The pipeline `User Content × AI Generation = Output` produces output that could have been made by any system, at any time, for any purpose. The Governor replaces that equation with `User Content × Art Direction System × AI Generation = Output` — inserting a creative brain between intent and execution. That brain is not a checklist; it is a system of six sequential directors, each owning a distinct layer of the visual language, each capable of vetoing downstream work that contradicts their brief. The Governor runs once per production and produces a binding contract that all downstream skills must honor. Nothing downstream is permitted to override the Governor's decisions silently. If a downstream skill cannot satisfy the brief, it escalates — it does not improvise.

---

## The Governor Pipeline

The six directors run in strict sequence. Each director's output is a constraint set for the next. A director never works in isolation; each inherits the decisions of all directors above them and narrows the solution space further. The final brief is the intersection of all six constraint sets.

---

### Director 1 — Creative Director

**Owns:** The unified aesthetic language for the entire production. The Creative Director makes the single highest-stakes decision: what kind of visual world does this video inhabit? Not a genre label. Not a mood adjective. A named, defensible creative position that can be held consistently across every frame.

**Decisions made:**
- The primary creative benchmark: one named reference from the quality canon (see below) that defines the aspirational ceiling for this production.
- The secondary creative benchmark: a second reference that introduces productive tension with the primary, creating a specific hybrid that is not generically "premium" or "cinematic."
- The creative premise: one sentence that states what this video *is* as a designed artifact, not what it contains. Example: "A Saint Laurent campaign shot through the grammar of a Tadao Ando exhibition catalogue."
- The hierarchy of expression: which layer carries the primary meaning — typography, image, motion, color, or space — and in what order the remaining layers serve.
- The aesthetic forbidden list: 5 specific moves that would contradict the creative premise and must not appear under any circumstance.

**Quality benchmarks — the Creative Director holds the brief against:**
- Apple Keynote Films (2007–2019): product as protagonist, restraint as confidence, silence as emphasis
- A24 Cinematography: texture over spectacle, human scale, available light as philosophy
- Saint Laurent Campaigns (Hedi Slimane era): rock noir, high contrast, analog grain, sexual tension through absence
- Loewe Visual Identity (Jonathan Anderson era): craft-object photography, intellectual wit, material worship, institutional serif
- Hermès Motion Design: deceleration as luxury, white space that costs something, handcraft mythology in motion
- Dieter Rams Design Principles: less but better, back to purity, honest materials, useful over decorative
- Naoto Fukasawa Minimalism: objects that disappear into use, design that needs no explanation
- Tadao Ando Spatial Composition: concrete silence, light as material, emptiness as architecture
- Paula Scher Typography: type at the scale of architecture, color blocks as argument, authority without decoration
- Massimo Vignelli Grid Systems: the grid is the ideology, everything on the baseline, nothing arbitrary

**Failure looks like:**
- A creative premise that is a genre adjective: "cinematic," "premium," "modern," "clean."
- Two benchmarks from the same school that do not create tension (Apple + MUJI = both restraint, no friction).
- A creative premise that changes per scene rather than holding across the full duration.
- Forbidden list items that are generic ("no Comic Sans," "no low resolution") rather than specific to this brief.
- A brief that any reasonable AI agent could have produced without reading the user's content.

---

### Director 2 — Art Director

**Owns:** The visual register, negative space strategy, and compositional grammar. The Art Director translates the Creative Director's language into spatial decisions: where things live in the frame, how much of the frame they occupy, what they are next to, and what is deliberately absent.

**Decisions made:**
- The compositional posture: edge-anchored asymmetry, centered authority, bleed-and-crop, horizon-line discipline, or extreme off-axis.
- The negative space mandate: the exact target percentage of the frame that must remain visually empty, and what that emptiness communicates (confidence, luxury, tension, breath, or institutional weight).
- The focal point hierarchy: exactly two focal points per frame — primary and secondary — with defined roles, positions, and size relationships.
- The visual weight distribution: which quadrant of the frame carries the most visual mass, and how that changes across the timeline.
- The image treatment language: how photographic, illustrative, or synthetic material is framed, cropped, graded, and plated.
- The grid signature: the underlying structural system (column grid, optical grid, or deliberate gridlessness) and whether it is visible or latent.

**Quality benchmarks:**
- Beggars Banquet record sleeve photography: extreme crop, brutal contact with the edge, negative space as accusation
- Loewe campaign photography: object isolation, white ground, shadow as design element, material close-up
- MoMA permanent collection wall labels: institutional margin, breathing room as curatorial statement
- Oliviero Toscani Benetton campaigns: frame-filling image that requires no headline
- Wolfgang Tillmans photography: anti-compositional composition — apparently random, structurally airtight

**Failure looks like:**
- Centered composition as a default rather than a deliberate choice.
- Three or more objects of equal visual weight competing for dominance.
- Negative space that is leftover rather than designed: elements pushed to the center, emptiness at the edges by accident.
- A frame that would look identical if reflected horizontally (bilateral symmetry without intention).
- Background material that was placed to fill space rather than to create a specific atmospheric register.
- Art direction that changes between scenes for no structural reason, making the video feel like a slideshow.

---

### Director 3 — Typography Director

**Owns:** Kinetic type behavior, optical kerning at render size, dynamic tracking, weight contrast strategy, and the relationship between type scale and the visual hierarchy established by the Art Director.

**Decisions made:**
- The typographic voice: one primary typeface and role (display, body, data), one secondary, with specific weights and optical sizes at the render canvas.
- The scale system: exact px values for display, body, and label type at 1280×720, with ratios that hold at other render sizes.
- The tracking and kerning philosophy: optical or metric, and specific letter-spacing values per role and size (not "tight" — actual em values).
- The weight contrast ratio: the relationship between the heaviest and lightest weight in the system, and whether that contrast is the primary tension or a supporting one.
- Kinetic type behavior: how type enters (masked reveal, word-by-word stagger, scale-from-zero, baseline slide), how long it reads, and how it exits — with specific duration and easing per role.
- Line-breaking philosophy: where the typographer would manually break lines for optical balance, not where the CSS engine breaks them by container width.
- The CJK and mixed-script protocol if applicable: density compensation, vertical rhythm, and the modification to tracking values.
- Forbidden type moves: the specific typographic choices that would contradict the visual register (e.g., italic in a Swiss-grid system, loose tracking in a brutalist poster, gradient text in any context).

**Quality benchmarks:**
- Wim Crouwel grid typography: every character on the grid, no optical exception, system as author
- Paula Scher Pentagram posters: type at the scale of the building it describes
- Neville Brody Face magazine: type that performs, editorial and sequential
- Vignelli Associates NYC subway signage: hierarchy through scale and weight alone, no decoration
- Emigre magazine (Zuzana Licko): type as image material, legibility as negotiated rather than given

**Failure looks like:**
- Font size chosen to fit the container rather than to express hierarchy.
- Default tracking: no letter-spacing property set at all, relying on the font's built-in metrics at a size they were not designed for.
- Weight contrast of less than 300 weight units between display and body (300 vs 400, 700 vs 800 — both are failures).
- Type that enters simultaneously with competing visual elements, producing a frame where nothing reads first.
- Animated type where the motion velocity exceeds the tracking value's ability to remain legible during travel.
- Mixed typefaces that share the same optical personality with no communicative differentiation.
- Kerning corrections absent on display type above 80px — at that size, metric kerning is visibly broken on most pairs.

---

### Director 4 — Color Director

**Owns:** Palette science, the 70/20/10 ratio, color temperature strategy, LUT reference for video grade, and the relationship between color and the emotional register defined by the Creative Director.

**Decisions made:**
- The primary palette: background, foreground, and surface colors with exact hex values, temperature notation (warm/cool/neutral), and the perceptual role of each.
- The accent color: one accent only, with its usage constraint (maximum percentage of frame area, maximum frequency of appearance, specific permitted contexts).
- The 70/20/10 distribution: the base field color occupies 70% of the average frame area; the secondary color (panels, type, structural elements) occupies 20%; the accent occupies 10% or less. This ratio is measured across the full duration of the clip, not per frame.
- The color temperature arc: whether the production holds one temperature throughout, or shifts temperature to communicate a state change, and at what exact beat that shift occurs.
- The forbidden palette moves: specific colors, combinations, and techniques that would contradict the brief (e.g., "no cyan-on-black," "no gradient fills," "no warm-cool split within a single panel").
- The LUT reference: one named color grade that defines the video's tonal behavior — not a filter, but a complete tonal map covering shadow density, midtone warmth, highlight rolloff, and saturation ceiling.
- Contrast discipline: the minimum luminance contrast between text and background (WCAG AA as a floor, not a ceiling — luxury and editorial contexts often require higher contrast), and how that minimum is maintained during animated color transitions.

**Quality benchmarks:**
- Wes Anderson film palettes: constructed palette as character, every hue at exact saturation, symmetry of warmth
- Wong Kar-wai cinematography: neon bleed, color as memory, overexposed warmth in shadow
- Bottega Veneta campaigns: warm shadow, muted earth, one electric accent per season
- Dieter Rams Braun products: off-white, cool gray, one warm accent — the object describes itself
- Pantone Colour of the Year announcement design: single color as total environment

**Failure looks like:**
- Palette chosen because it looks good at the design stage, not because it communicates the correct temperature for this specific content.
- Accent color appearing in more than three locations per frame or constituting more than 15% of frame area.
- Black defined as `#000000` or white as `#FFFFFF` — true black and white have no warmth, no material, no photographic quality. Use `#0E0C0A` for rich black; `#F7F4EE` for paper white.
- Background and surface colors with identical hue and a luminance difference of less than 8% — they read as the same color at render size.
- Color saturation that varies between scenes without a structural reason — the palette must behave consistently unless a deliberate arc has been specified.
- LUT defined as a generic label ("cinematic warm," "filmic") without a named reference or specific tonal description.

---

### Director 5 — Motion Director

**Owns:** Cinematic easing, temporal rhythm, the compression/release system, and the relationship between motion velocity and the emotional register defined by the Creative Director.

**Decisions made:**
- The rhythm profile for this production (see Dynamic Rhythm System below) — one primary profile per clip, with a documented rationale.
- The easing vocabulary: specific GSAP ease names for each motion category (entrance, hold, exit, micro-feedback, accent hit), not generic adjectives.
- The compression/release arc: the sequence of high-density and low-density moments across the clip timeline, with approximate timestamps and durations.
- Duration discipline: the minimum hold duration for any primary text (readable landings), the maximum duration for any entrance animation (attention cost budget), and the silence budget — how much of the clip should be perceptually still.
- The beat map skeleton: 3–6 named beats with timestamps, emotional function, and dominant motion vocabulary per beat.
- Forbidden motion moves: specific easing types, transition patterns, or animation behaviors that would contradict the brief (e.g., spring physics in a luxury context, bounce easing in a brutalist context, fade-in on a poster that requires instant impact).
- The motion-to-content ratio: the proportion of the timeline where motion is the primary communicator versus where stillness allows the content to read.

**Quality benchmarks:**
- Kubrick tracking shots: the camera observes, never follows — velocity is constant, intention is total
- Saul Bass title sequences: every graphic event is necessary, nothing decorates, shape becomes meaning
- Vince Lombardi Films slow motion: deceleration as the act of seeing something clearly
- Daft Punk "Around the World" video: repetition as rhythm, motion as meter, persistence as meaning
- Tarsem Singh "Losing My Religion" video: tableau held long enough to become a painting

**Failure looks like:**
- Every element in the frame is in motion simultaneously — the viewer's eye has no rest point.
- Entrance animations that take longer than the content they reveal justifies (spending 800ms to reveal a three-word label is a motion cost the copy cannot repay).
- Easing curves that feel identical across all motion categories — no differentiation between a primary hit and secondary support motion.
- A clip that reaches its peak visual density at the beginning and decelerates into the lockup, rather than building compression toward a release.
- Transitions that are technically smooth but semantically arbitrary — the transition type carries no meaning about the relationship between the incoming and outgoing content.
- Spring or bounce physics applied to type or UI elements in any register that is not explicitly playful or warm-humanist.

---

### Director 6 — Photography / Cinematography Director

**Owns:** Compositional language for photographic and video material, camera language (real or simulated), and the physical imperfection system that prevents the production from reading as AI-generated.

**Decisions made:**
- The camera language: whether the production uses a fixed observational frame, simulated push-in/pull-back, crop-reframe, or multi-axis movement — and the specific behavioral rules for each.
- The photographic register for all still and moving image material: what it was shot on (or should be treated as if shot on), what focal length defines the visual language, and how shallow or deep the field of focus should read.
- The image treatment protocol: how source material is graded, cropped, masked, and plated to conform to the palette and compositional grammar established by the Art Director.
- The physical imperfection mandate: specific imperfections to introduce at what intensity (see Premium Texture System below), and how they are distributed across the frame and timeline.
- The visual imperfection budget: how much imperfection is appropriate for this production's register (a luxury fashion campaign accepts grain and lens breath; a medical device product demo does not).
- The lens character: whether the production reads as optically rectilinear (architectural, institutional) or optically distorted (intimate, editorial, analog), and the specific CSS/GSAP/SVG implementation that achieves this.
- The shadow and light philosophy: where light enters the frame from, how shadows fall, and whether the lighting is ambient (diffuse, soft, even) or dramatic (directional, structured, high contrast).

**Quality benchmarks:**
- Roger Deakins cinematography: natural light that knows it is being designed, shadow as character, wide-angle intimacy
- Juergen Teller photography: flash on face, wrong exposure, completely correct composition
- Wolfgang Tillmans (as cinematographer): ordinary objects made strange by placement, light that is technically accidental
- Nan Goldin The Ballad of Sexual Dependency: available light as confession, grain as authenticity
- Hiro commercial photography: object at perfect scale against infinite white, light that defines rather than illuminates

**Failure looks like:**
- Video material that reads as stock footage: generic camera angles, flat color, no editorial intention in the crop.
- Photographic material placed at its original aspect ratio without any directorial intervention — the crop is the direction.
- A frame where the light source is undefined or inconsistent across the composition, producing ambient glow from no origin.
- Physical imperfection absent entirely, producing the characteristic AI-generated plastic quality (see Premium Texture System below).
- Camera movement (real or simulated) that exists to fill time rather than to change what the viewer knows about the subject.
- Depth of field simulated at a focal length inconsistent with the stated lens character (a 50mm portrait depth-of-field simulation on an architectural wide shot contradicts the visual grammar).

---

## Global Art Direction Rules

These rules apply universally and cannot be overridden by any individual director or downstream skill.

**Rule 1 — No random visual decisions.**
Every element in every frame must be traceable to a specific decision in the Governor Brief. If a team member or agent cannot explain why a visual element exists and what decision it enacts, the element is removed. Decoration that cannot be defended is not decoration — it is noise.

**Rule 2 — Every element intentionally designed.**
Size, position, color, weight, duration, and relationship to neighboring elements are all active decisions. Default values — browser default type size, CSS default letter-spacing, auto layout, inherited color — are rejections of responsibility. Every CSS property that matters is set explicitly, with intent.

**Rule 3 — Unified aesthetic language established before any shot is chosen.**
The Governor Brief is complete before any image is sourced, any font is loaded, any color value is committed to code. Downstream skills do not refine the aesthetic language; they implement it. If a downstream skill proposes a change to a Governor decision, it writes an escalation, not a silent substitution.

**Rule 4 — Visual hierarchy controlled by luxury branding, museum exhibition, and fashion campaign principles.**
The hierarchy principles that govern this system are those of a Prada campaign, not a SaaS landing page. In a Prada campaign: one thing is primary, it is given space, everything else recedes. In a SaaS landing page: five things compete at equal weight, none of them win. The hierarchy model is the former.

**Rule 5 — The brief is binding until it is revised.**
If a downstream skill produces output that contradicts the brief, it is out-of-brief, not "a creative interpretation." The correction path is: identify the contradiction, return to the Governor, revise the relevant director's brief, re-implement.

**Rule 6 — Generic is a failure mode, not a style.**
"Premium," "cinematic," "minimal," "clean," and "modern" are not styles. They are the linguistic form that generic output takes when it needs to sound intentional. Every directive in this system replaces generic adjectives with named references, specific measurements, and exact technical values.

---

## Dynamic Rhythm System

Rhythm in video is the management of cognitive load over time. The viewer can absorb high-density, high-motion, high-information passages only when they are followed by passages of compression, stillness, and breath. A clip that holds peak density throughout produces viewer fatigue; a clip that holds low density throughout produces disengagement. The Governor mandates an explicit rhythm profile for every production.

**The compression/release law:**
Density alternates with emptiness. Motion alternates with stillness. Fast sequences are balanced by breathing space. Every moment of high cognitive cost must be followed by a moment of low cognitive cost, sized proportionally to the cost just incurred. A two-second burst sequence demands at least 1.2 seconds of stillness before the next burst. A five-second technical explanation demands a 2–3 second breath before the next complex beat.

### Rhythm Profiles

Every clip must be assigned one primary rhythm profile before implementation. The profile defines the default ratio of compression to release and the character of each.

**Explosive**
- Compression ratio: 70% dense, 30% release
- Compression character: simultaneous multi-element entrances, fast stagger (30–60ms), high kinetic energy, short holds (0.3–0.8s)
- Release character: single-element lockup, extended hold (2–3s), minimal motion, strong silence in the soundtrack
- Typical use: launch moments, brand drops, trailer hooks, opening sequences
- Forbidden: slow fade entrances, gentle easing, passive camera

**Editorial**
- Compression ratio: 50% dense, 50% release
- Compression character: sequential stagger (80–120ms), deliberate entrance order, one element moves at a time
- Release character: full typographic or compositional lockup held for reading, ambient micro-movement only, defined silence
- Typical use: product demos, feature launches, explanation sequences, case study videos
- Forbidden: simultaneous multi-element entrances, spring physics, motion that competes with the content being read

**Luxury**
- Compression ratio: 25% dense, 75% release
- Compression character: single-element reveals at 600–900ms, extreme restraint, the reveal event itself is the drama
- Release character: extended silence, near-static frame, the held still image as the primary communication event
- Typical use: fashion campaign, high-consideration product launch, brand identity films, premium lifestyle
- Forbidden: any bounce or spring, multiple simultaneous events, fast stagger, kinetic type bursts, transition wipes

**Technical**
- Compression ratio: 60% dense, 40% release
- Compression character: data hits, metric counts, UI assembly sequences, fast label entrances (50–80ms stagger), precise mechanical easing
- Release character: labeled lockup held for comprehension, single metric emphasized per beat, product behavior visible and still
- Typical use: SaaS product demo, data story, feature comparison, technical explainer
- Forbidden: organic easing, film grain, slow atmospheric reveals, any motion that reads as emotional rather than informational

**Humanist**
- Compression ratio: 40% dense, 60% release
- Compression character: gentle word-by-word entrances (100–150ms stagger), soft scale-from-zero, warm easing (sine.inOut, power1.out)
- Release character: full sentence or thought held comfortably, ambient warmth maintained (soft bed sound, gentle ambient motion), breathing room
- Typical use: educational content, wellness brands, community product videos, creator tool launches, emotional storytelling
- Forbidden: slam cuts, hard mechanical easing, aggressive kinetic bursts, cold typography, empty silence used as tension (silence here is rest, not weapon)

---

## Museum-Level Refinement Rule

Before any visual element is finalized — before any frame goes to render, before any DESIGN.md is accepted — every element must pass the Museum Test.

**The Museum Test:**
> "Would this element appear in a museum exhibition, a luxury brand campaign, a film festival title sequence, or a design annual publication?"

This is not a metaphor. Apply it literally.

- **Museum exhibition**: Does this element have the compositional authority, material quality, and conceptual precision of an object in a permanent collection? Is it presented with the confidence that it needs no explanation? Would it survive being the only thing on the wall?

- **Luxury brand campaign**: Does this element communicate value through what it omits as much as what it includes? Does it treat the viewer as someone with taste, rather than someone who needs to be persuaded?

- **Film festival title sequence**: Does this element have a reason to exist in motion? Does it use its duration to communicate something that a static frame cannot? Would a festival audience hold this in memory?

- **Design annual publication**: Would a design publication reproduce this frame as evidence of the state of the art? Or would an editor describe it as "competent," "polished," or "well-executed" — the taxonomy of the forgettable?

**Application:**
If the answer to any of the four questions above is "probably not," the element is not yet at the required level. Refine further. Specific corrections precede generic ones: "the tracking on this label is 0.02em too loose for its weight and size" is a refinement; "make it look more high-end" is not.

**No element should appear generic, template-like, or AI-generated.** These three failure modes have distinct signatures:

- *Generic*: the design choice is statistically the most common choice for this type of content. It is not wrong; it is indistinguishable from everything else in its category.
- *Template-like*: the composition, typography, or color system shows the underlying grid or pattern that generated it. The scaffolding is visible. The element looks like it came from a library, not from a decision.
- *AI-generated*: the element has the characteristic smoothness of a probability-weighted average: perfect gradients that shade to nothing, typography that is technically correct and optically inert, compositions that are balanced because nothing has enough weight to tip them.

---

## Premium Texture System — Anti-AI-Smoothness Rule

AI-generated visuals carry a characteristic signature that viewers identify as "cheap automation" even when they cannot name the mechanism: perfect surface smoothness, light that comes from everywhere and casts no shadows, colors at exact spectral values with no contamination, typography that sits on its baseline with mathematical precision and no optical tension. This aesthetic signals that no human made a decision here — a probability engine produced the most statistically acceptable result.

The Governor mandates a controlled introduction of physical imperfection at the level appropriate to the production's register. This is not a filter applied after the fact. It is a design decision specified in the brief and implemented deliberately.

### The Imperfection Mandate

**Film grain.**
Subtle grain at 3–8% opacity, matching the grain structure of the film stock that corresponds to the production's LUT reference. Grain should animate (not be a static texture), should be denser in shadows than highlights (replicating photochemical behavior), and should be sized to the render canvas (grain that is 2px at 720p becomes 1px at 4K — scale it up). Grain is present on all atmospheric material and on any frame that would otherwise read as computer-generated. Grain is never present on UI elements, data overlays, or typographic elements — it lives on the photographic and spatial layer only.

**Lens breathing on slow zooms.**
When the production uses push-in or pull-back camera movement (real or simulated), the zoom should exhibit subtle focal length drift — a very slight, imperceptible softening of the frame edges as the zoom progresses. This replicates the optical behavior of a real zoom lens under focus breathing. Implementation: a 0.2–0.5% scale oscillation on the atmospheric layer, at 2–4 second intervals, with sine.inOut easing. This should never be perceptible as an effect; it should only be perceptible as "this was shot, not generated."

**Natural shadow variation.**
Shadows in the composition are not mathematically perfect gradients. They have a slight directional asymmetry, a soft edge that transitions over 8–15% of the shadow's diameter rather than over a precise CSS blur radius, and a color that tilts toward the cool end of the temperature scale (shadows are slightly blue-shifted relative to the midtones of a warm-light source). In implementation: use multiple overlapping gradient layers with slightly different opacity, angle, and color temperature rather than a single CSS box-shadow.

**Light falloff and vignette.**
Every frame that uses atmospheric photographic material has a vignette: a gradual luminance reduction toward the frame edges, between 15–30% opacity depending on register, matching the optical behavior of a lens at its maximum aperture. The vignette is not circular (radial-gradient with equal x and y) — it is slightly elliptical, taller than it is wide, as a real lens produces. For luxury register: vignette is subtle (15–18%). For editorial and brutalist: vignette may be pronounced (25–35%). For technical and data-authority: vignette is absent — clarity is the value.

**Surface texture in backgrounds.**
Backgrounds that would read as flat color in a generated context are given material identity. For paper registers: a very low-opacity noise layer (2–4% opacity) that reads as paper tooth. For glass or metal registers: a subtle specular gradient (3–6% opacity) that suggests a light source. For concrete or matte registers: a directional grain (4–8% opacity) that follows a physical orientation. Never synthetic perfection: the background should read as a material that exists in the world, not as a CSS color value.

### Imperfection Levels

| Level | Description | Use |
|---|---|---|
| `none` | No physical imperfection. Technically perfect surfaces. | UI-only product demos, data visualizations, technical diagrams — contexts where perfection is the message |
| `subtle` | Grain at 3–4%, vignette at 15%, minimal shadow variation, no lens breath | Premium launch, luxury register, editorial minimalist — imperfection is felt, not seen |
| `medium` | Grain at 5–6%, vignette at 20–22%, shadow variation, gentle lens breath | Warm humanist, editorial tech, cinematic — imperfection is a quality signal |
| `pronounced` | Grain at 7–8%, vignette at 28–35%, strong shadow character, visible lens behavior | Fashion campaign, film-register cinematic, analog-aesthetic brand — imperfection is the aesthetic |

---

## The Governor Output Contract

Before any downstream skill runs, the Governor produces the following brief. This brief is the single source of truth for all subsequent decisions. It is written once, at the beginning of the production, and does not change unless a formal revision is escalated back to the Governor.

```markdown
## Aesthetic Governor Brief

- Rhythm profile: [explosive / editorial / luxury / technical / humanist]
- Primary creative benchmark: [one named reference, e.g., "Saint Laurent Hedi Slimane campaigns, 2013–2015"]
- Art direction language (3 words max): [e.g., "stark analog authority"]
- Typography posture: [one sentence: typeface role, weight contrast, kinetic behavior, e.g., "Extended-weight grotesque at bleed scale, tracked loose at −0.01em, mask-reveals left-to-right over 400ms at power4.out"]
- Color register: [background hex, foreground hex, accent hex, LUT reference, temperature note]
- Motion register: [primary GSAP ease, compression/release ratio, forbidden motion types]
- Cinematography language: [camera language, focal length character, depth of field posture]
- Texture/imperfection level: [none / subtle / medium / pronounced]
- Forbidden aesthetic moves (5 items specific to this brief):
  1. [specific, not generic — e.g., "no simultaneous multi-element entrances" not "no cheap effects"]
  2.
  3.
  4.
  5.
- Museum test: [the single sentence that defines if this clip passes — e.g., "Every paused frame could be a spread in a Phaidon monograph without alteration"]
```

The brief is a contract. Downstream skills must read it before producing any output and must cite it when making decisions.

---

## Position in the Director Workflow

The Aesthetic Governor runs as **Step 4.0** in `flagship-video-director`:

```
Step 3.  Flagship reference direction selected
Step 4.  Aspect Ratio / Responsiveness Gate (canvas and ratio locked)
Step 4.0 ← AESTHETIC GOVERNOR (this skill) — Governor Brief produced
Step 4.5  Aesthetic Layout Direction (design school anchored to Governor Brief)
Step 5.  Style Selection Layer (all decisions must be consistent with Governor Brief)
Step 6.  video_ad vs moving_slide decision
Step 9.  high-end-video-design (DESIGN.md written against Governor Brief)
Step 10. typography-selection (must honor Typography Director's brief)
Step 11. image-art-direction (must honor Art and Photography Directors' briefs)
Step 14. motion-graphic-design (must honor Motion Director's brief and rhythm profile)
```

The Governor Brief produced at Step 4.0 is the aesthetic constitution for the production. Every downstream step operates within it. No downstream skill may introduce palette, typographic, motion, or compositional choices that contradict the Governor Brief without a formal escalation to Step 4.0 to revise the relevant director's decisions.

**What the Governor does not do:**
- The Governor does not produce code. It produces constraints that govern the code.
- The Governor does not select specific fonts or exact hex palette values — that specificity is the work of downstream skills, operating within the Governor's constraints.
- The Governor does not write `DESIGN.md` — that is `high-end-video-design`'s output contract.
- The Governor does not place or time individual elements — that is `motion-graphic-design`'s responsibility.

**What happens if the Governor is skipped:**
The pipeline reverts to `User Content × AI Generation = Output`. Downstream skills will make individually defensible decisions that collectively produce no unified aesthetic language. The result will be polished and generic. The Governor is not optional for any production where the quality bar requires museum-level refinement.

---

## References

- For design school anchoring and video-native token translation: [`aesthetic-layout-direction/SKILL.md`](../aesthetic-layout-direction/SKILL.md)
- For school-to-video DNA mapping, palette hex values, and composition rules: [`aesthetic-layout-direction/STYLE-SCHOOL-MAP.md`](../aesthetic-layout-direction/STYLE-SCHOOL-MAP.md)
- For video layout patterns and composition templates: [`aesthetic-layout-direction/LAYOUT-PATTERNS.md`](../aesthetic-layout-direction/LAYOUT-PATTERNS.md)
- For anti-slop audit criteria and rejection protocol: [`high-end-video-design/ANTI-SLOP-AUDIT.md`](../high-end-video-design/ANTI-SLOP-AUDIT.md)
- For specific color science, LUT references, and palette construction: [`COLOR-DIRECTOR.md`](COLOR-DIRECTOR.md)
- For photographic treatment, lens character, and image grading: [`PHOTOGRAPHY-DIRECTOR.md`](PHOTOGRAPHY-DIRECTOR.md)
- For the full school recipe library: [`aesthetic-layout-direction/STYLE-SCHOOL-MAP.md`](../aesthetic-layout-direction/STYLE-SCHOOL-MAP.md)
- For flagship quality benchmark references: [`flagship-video-director/FLAGSHIP-REFERENCES.md`](../flagship-video-director/FLAGSHIP-REFERENCES.md)
- For overall production orchestration and step sequencing: [`flagship-video-director/SKILL.md`](../flagship-video-director/SKILL.md)
