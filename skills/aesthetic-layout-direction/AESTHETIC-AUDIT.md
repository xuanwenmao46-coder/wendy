# Aesthetic Quality Audit

A 5-dimension scoring rubric adapted from web design critique principles for video. Use this after
generating a clip design brief or a rendered frame, and before declaring implementation complete. Run
after the visual brief, after Remotion Studio preview, and after final render.

**Critique the design, not the designer.** Be specific, grounded in the named school's DNA, and
actionable — not vague taste claims. "The colors feel premium" is not a critique. "The `#5E6AD2` accent
appears on 6 elements — Linear uses it on < 5% of pixel area, which means at most 1–2 elements per
frame at 1280×720" is a critique.

---

## The Five Dimensions

### 1. Philosophy Alignment

Does every frame trace back to the named design school and anchor? This is the primary gate: a clip
that scores 9+ on all other dimensions but fails here is still the wrong clip.

| Score | Standard |
|---|---|
| 9–10 | Every element — palette, type, composition, motion, sound — embodies the named anchor. Nothing reads as "borrowed from elsewhere." Signature moves are present and specific. |
| 7–8 | Direction is correct; 1–2 minor drift moments (e.g., a slightly rounded corner in Brutalist, a warm accent in Tool/SaaS). Core DNA is intact. |
| 5–6 | Intent visible, but cross-school contamination dilutes character (e.g., "minimalist" with 5 feature cards, or "brutal" with a soft ease-in). The school is recognizable but compromised. |
| 3–4 | Named the school but borrowed only surface traits. Dark background ≠ Experimental. White space ≠ Editorial Minimalist. Amber ≠ Aesop unless the serif is present. |
| 1–2 | No detectable relationship to the named school; could belong to any of the 6. Generic output. |

**What to look for (5 specific checks)**:
1. Are the named anchor's **signature moves** present and visible? (Pentagram → type as structural image; Aesop → one serif voice, one amber rule, product as protagonist; Linear → hairline 1px borders, warm dark #08090A, purple < 5%)
2. Do palette, type, motion, and sound **agree on the same school** — or does the palette say "Minimalist" while the motion says "Experimental"? All four dimensions must point to the same register.
3. Are any of the school's **forbidden elements** present? Each recipe in VIDEO-RECIPES.md lists specific forbidden type families, forbidden motion patterns, and forbidden sounds. Check each one.
4. **Could this frame be mistaken for a different school?** If yes, name which school it drifted toward and fix the single element causing the drift.
5. **The named recipe vs. the school**: "Editorial / Minimalist" is a school; "Aesop" is a recipe. A score of 9 requires recipe-level fidelity, not just school-level fidelity. Does it read as Aesop specifically (chamois + amber amber rule + italic serif, no bold) rather than just "minimal"?

**School-specific alignment checks**:
- **Information Architecture** (pentagram, tufte-dataink, bloomberg-terminal): Is every text block left-aligned? Is the grid strict? Is there exactly 1 accent element? Is all data encoded by color, not decoration?
- **Editorial / Minimalist** (aesop, muji-kenya-hara, apple-hig): Is negative space ≥ 40%? Is the product treated photographically? Is motion energy ≤ 2/10? For a score of 8+, negative space must exceed 40% of the frame — not 38%, not "generous". Measure it.
- **Motion / Experimental** (field-io): Is the design in continuous motion? Is there a legible landing every 2–4s? Is the generative system the hero — not a background decoration behind a flat layout?
- **Brutalist / Raw** (bloomberg-businessweek-turley): Is the type at absurd scale (≥ 160px at 720p)? Is the palette exactly 3 colors? Is there zero easing on motion? Is something deliberately uncomfortable?
- **Warm Humanist** (mailchimp-freddie, stripe-press): Does it feel human-made? Is the palette warm-spectrum only? Is the motion organic? Is there a real illustrator's hand or a photographed object?
- **Modern Tool / Builder SaaS** (linear, vercel-mesh): Is the product UI visible and in active state? Are borders hairline (1px, not 2px)? Is the accent < 5% of pixel area (count the colored pixels)?

---

### 2. Visual Hierarchy

In 2 seconds paused on any frame, does a viewer know what matters? This is the squint test: blur
your vision until only mass, color, and scale survive. The primary element must dominate that blur.

| Score | Standard |
|---|---|
| 9–10 | Primary / secondary / tertiary reads are unambiguous in 2 seconds. Squint test: hierarchy survives full blur. Paused poster test: the still frame works as a standalone image. |
| 7–8 | Primary clear; 1–2 secondary elements compete at roughly equal visual weight; minor muddy zone at the third level. |
| 5–6 | Title vs. body distinguishable, but subtitle, caption, and metadata collapse into the same visual weight. Three levels compress to two. |
| 3–4 | Information sits flat — equal-weight elements at every tier; no obvious entry point; the eye drifts. |
| 1–2 | Chaotic — the eye finds no resting place; multiple elements compete for primary attention simultaneously. |

**What to look for (5 specific checks)**:
1. **Squint test**: blur the frame. Is the primary element (hero type, product object, data panel) still the brightest, largest, or most distinct point? If the headline and a supporting caption have similar visual mass when blurred, hierarchy has failed.
2. **Size ratio**: display vs. support must be ≥ 2.5× at 720p. At 1280×720: if support is 24px, display should be at least 60px. Ideally 4–6× for hero display moments.
3. **Color as hierarchy**: the accent color should appear at the highest priority level only. If the accent color is on both the headline AND a metadata label, it is doing zero hierarchy work.
4. **Negative space directing gaze**: the empty region should frame the primary element. If the negative space is evenly distributed around the frame, it is not directing the eye — it is just absent content.
5. **Motion serving hierarchy**: the first element to animate or appear should be the most important. If a decorative element enters before the hero, the motion narrative has inverted the hierarchy.

**School-specific hierarchy notes**:
- **Editorial / Minimalist** (aesop, muji-kenya-hara): a score of 8+ on hierarchy requires negative space > 40% of frame actively framing the hero object. If the negative space is not directing the eye, subtract 2 points.
- **Information Architecture** (bloomberg-terminal, tufte-dataink): hierarchy is encoded through color and position, not scale. Amber = primary data; chrome white = secondary; muted gray = tertiary. If all three are the same color family, hierarchy score cannot exceed 6.
- **Brutalist / Raw** (bloomberg-businessweek-turley): hierarchy is intentionally compressed — the type mass IS the hierarchy. A score of 9 means the type scale alone creates the reading order, without any supporting visual weight contrast needed.

---

### 3. Craft Quality

Pixel-level execution: alignment, spacing system, color discipline, font consistency. Craft quality
is where good design intent becomes (or fails to become) good design execution.

| Score | Standard |
|---|---|
| 9–10 | Every element aligns to a system. Spacing follows a consistent multiplier. Color uses ≤ 4 values. Font weights follow the chosen pairing without drift. Text is ≥ 26px at 720p. |
| 7–8 | Refined overall; 1–2 minor spacing or alignment inconsistencies; color count is controlled; font family is consistent even if weights drift once. |
| 5–6 | Basically aligned, but spacing is ad-hoc (elements placed by eye, not system); color count is loose (5–6 values); font weight drifts between instances of the same text role. |
| 3–4 | Obvious alignment errors; chaotic spacing; 6+ distinct colors; mixed font families or weights without systematic logic; text below 24px at 720p. |
| 1–2 | Looks like a rough draft — no visible design system, no alignment discipline, font choice arbitrary. |

**What to look for (5 specific checks)**:
1. **Spacing system**: does the clip use a consistent multiplier? The recipe's web spacing (e.g., 8/16/24/40px for Linear) scales to approximately 16/32/48/80px at 720p. If element gaps are arbitrary (23px, 37px, 41px), it is ad-hoc, not a system.
2. **Same-class consistency**: do all metadata labels share the same size, weight, and position rules? Do all UI chip labels look identical in every frame? If the same text role has two different treatments, subtract 1.5 points minimum.
3. **Color discipline**: count distinct color values in the frame. Premium work uses ≤ 4 (bg + fg + accent + material). Each additional color beyond 4 must be justified by the recipe (e.g., bloomberg-terminal's green/red for directional data). Decoration colors never count as justified.
4. **Font consistency**: is the font family the same across all instances of the same text role? Are weights following the recipe's defined pairing (e.g., Linear: 400 support vs. 600 display — never 700, never Inter at default 400)? Drift in weight signals template behavior, not recipe fidelity.
5. **Video-specific craft checks**:
   - Text minimum: 26px at 720p (16px web ≈ 35px video at arm's length viewing distance)
   - Hero image: sharp at 1280×720 render size; no JPEG artifact visible on bg or hero
   - Text legibility during motion: the text must be readable while animating — test by pausing 1–3 frames before the landing position
   - No text/background near-match: a 3:1 contrast ratio minimum at all animated positions, not just the final hold

**School-specific craft notes**:
- **bloomberg-terminal**: craft score cannot exceed 7 if any font is not monospaced, any border is > 1px, or any corner has radius > 2px. These are not polish items — they are recipe requirements.
- **muji-kenya-hara**: craft score requires font weight ≤ 400 (no 500, no 600). A single bold element drops the score by 2 points. Weight restraint is the craft discipline.
- **field-io**: craft is evaluated on the generative system's quality — does the particle/mesh system behave consistently? Does the type resolve cleanly from the field, or does it feel disconnected?

---

### 4. Motion Coherence

Does the motion reinforce the aesthetic school, or fight it? Motion posture is part of the recipe —
a school's GSAP ease, hold duration, transition type, and forbidden motion patterns are as specific
as its hex palette. Mismatched motion is visible within the first 2 seconds.

| Score | Standard |
|---|---|
| 9–10 | Every motion choice — ease, duration, energy level, transition type — is consistent with the school's motion posture. Forbidden motion is absent. The clip would be identifiable by motion alone even with the palette removed. |
| 7–8 | Motion is mostly correct; 1–2 beats use the wrong energy or ease (e.g., a `back.out` spring in an Editorial/Minimalist clip; a 600ms dissolve in a Brutalist cut-sequence). |
| 5–6 | Motion is technically competent but feels wrong for the school; the clip could belong to a different aesthetic. The easing may be correct but the duration is wrong, or vice versa. |
| 3–4 | Motion actively contradicts the school (slow reverence for a Brutalist clip; aggressive slam cuts in Warm Humanist; a generative particle system for an Information Architecture data story). |
| 1–2 | Motion feels random — no discernible logic relative to any aesthetic school. Default ease-in-out used throughout. |

**What to look for (5 specific checks)**:
1. **Ease accuracy**: does the GSAP ease name match the school's recipe? `sine.inOut` for Editorial/Minimalist; `steps(1)` for Brutalist; `expo.out` / `cubic-bezier(0.83,0,0.17,1)` for Experimental; `power3.out` for Tool/SaaS; `power4.out` for Information Architecture type hits; `back.out(1.4)` for Warm Humanist illustration bounces. A wrong ease is a wrong school.
2. **Energy level match** (1–10 scale): Editorial/Minimalist: 2; Information Architecture: 3–4; Warm Humanist: 4–6; Tool/SaaS: 5–6; Brutalist: 7–9; Motion/Experimental: 8–10. If the clip's observable energy level is more than 2 points off, it has failed motion coherence regardless of how well-executed the motion is.
3. **Transition type accuracy**: hard cut (Brutalist only); 1200ms cross-dissolve (Stripe Press); 600ms dissolve (Editorial/Minimalist); precision mask left-to-right (Information Architecture/Tufte); instant state flip (Bloomberg Terminal); hue-shift field state change (Field.io); yellow flood wipe (Mailchimp Freddie). Using a dissolve where a hard cut belongs is a school violation.
4. **Hold duration discipline**: Muji/Aesop: 3–4s minimum hold; Apple HIG: 2.5s; Linear: 1.8s; bloomberg-businessweek-turley: 1.5s; field-io: 1.5s; bloomberg-terminal: continuous (no hold). If the hold is shorter than the recipe minimum, information is not landing. If there is no hold at all, the clip has not been designed — it has been animated.
5. **Forbidden motion check**: identify the school's forbidden motion from VIDEO-RECIPES.md and verify absence. Examples: bounce/spring in any Editorial school; slow ease-out in Brutalist; opacity-only fade in Field.io; dramatic count-up in Tufte-dataink; eased transitions in Bloomberg Terminal.

**School-specific motion notes**:
- **aesop / muji-kenya-hara**: a score of 8+ requires that no element moves its position during the clip — opacity only. Any x/y/scale animation that exceeds 8px drops the score to ≤ 6. Motion here is light, not movement.
- **bloomberg-businessweek-turley**: a score of 8+ requires at least one hard cut (zero-frame transition) in the clip. If every transition is eased, the clip has not committed to the school.
- **field-io**: a score of 8+ requires the generative system to be in motion during the hold — not frozen. If the field pauses while the type holds, the motion coherence has failed; the field is the motion, not a backdrop.
- **linear / vercel-mesh**: the motion posture is "snappy but not bouncy". `back.out` eases are explicitly forbidden. A single bounce in the clip drops Philosophy Alignment AND Motion Coherence each by 1.5 points.

---

### 5. Sonic Harmony

Does the sonic character match the material metaphor of the chosen design school? Sound is not
decoration — it is part of the aesthetic. If you close your eyes during a well-scored clip, the
school should still be identifiable. "Cinematic swell over everything" is the sonic equivalent of
a purple-pink gradient: a sign of no school, not a school.

| Score | Standard |
|---|---|
| 9–10 | Sound is indistinguishable from the visual school — the material metaphor (brushed aluminum, ceramic, letterpress, electromagnetic) is audible. Identify the school from audio alone. |
| 7–8 | Sound fits the school; 1 cue drifts to another school's sonic character (e.g., one warm whoosh in a Terminal clip; one UI click in an Aesop clip). |
| 5–6 | Sound is present and functional but generic — a stock SFX pack with no school-specific character. Could belong to any of 4+ schools. |
| 3–4 | Sound contradicts the school: cinematic swell for Brutalist; UI click for Warm Humanist; reverb tail > 200ms for a school that uses dry sounds; silence where a bed is required. |
| 1–2 | Sound causes active cognitive dissonance with the visual design — the audio school and the visual school are clearly different schools. |

**What to look for (5 specific checks)**:
1. **Material metaphor match**: each school has a named sonic material. Check VIDEO-RECIPES.md for the recipe's "material metaphor." Brushed aluminum (linear) ≠ ceramic (aesop) ≠ letterpress (pentagram) ≠ electromagnetic (field-io) ≠ cloth (stripe-press) ≠ mechanical keyboard (bloomberg-terminal). If the sound does not evoke the material, the metaphor has failed.
2. **Transient shape accuracy**: dry click < 12ms (bloomberg-terminal, linear); soft swell 400ms+ (stripe-press, aesop); sharp impact transient 20ms (bloomberg-businessweek-turley, pentagram); harmonic sweep 200–600ms (field-io); no transient / pure fade (muji-kenya-hara). A transient with a mismatched attack envelope signals the wrong school.
3. **Density appropriateness**: Editorial schools (aesop, muji, apple-hig): 2–3 sonic events per clip maximum; silence is designed. Tool/SaaS (linear, vercel-mesh): 3–5 sparse events; clicks + one accent hit. Brutalist: 1–2 very loud events; silence is a weapon. Experimental (field-io): continuous bed + staggered micro-events; density matches field density. Warm Humanist: 4–6 events with a music bed.
4. **Forbidden sound check**: from VIDEO-RECIPES.md, each recipe lists "forbidden sounds". Check explicitly: no reverb tail > 200ms for linear; no clicks for aesop; no music with rhythm/melody for stripe-press; no whoosh sweeps for bloomberg-terminal; no percussive SFX for muji-kenya-hara.
5. **Silence usage**: silence is not absent sound — it is designed space. Editorial/Minimalist schools use silence as luxury restraint. Brutalist schools use silence as aggressive confrontation before a slam. If silence occurs in a Warm Humanist clip, something has gone wrong. If a music bed runs through an Aesop clip, something has gone wrong.

**School-specific sonic notes**:
- **aesop**: the correct response to "I couldn't find a ceramic bowl SFX" is: use silence. The school does not require SFX — it requires appropriate SFX or none. A single soft ceramic strike is ideal; anything louder or drier betrays the material.
- **bloomberg-terminal**: the bed must not be audible music. A fan hum or electrical buzz at -34dB is the bed. Any melodic element, even at low volume, is a school violation. Terminals hum — they do not sing.
- **field-io**: the drone bed is not optional. A field-io clip with dry silence between events sounds wrong. The electromagnetic drone is the sonic equivalent of the particle system — it must be continuous.
- **bloomberg-businessweek-turley**: the impact SFX should be loud enough to make the viewer blink. If the impact sounds apologetic (< -12dB), it has not committed to the school. The recipe calls for -6dB on the main slam. Use it.

---

## Per-School Common Failures

Per-recipe failures follow. These are the top 3 most common audit failures for each recipe, observed
across real production sessions. Each has a specific fix — not "make it better" but a concrete change.

### linear (Modern Tool / Builder SaaS)
1. **Accent color over-use** — Linear purple `#5E6AD2` appears on headline, sub-claim, button, AND chip label. Fix: remove the accent from all but one element in the frame; the accent earns its meaning from scarcity.
2. **Warm dark replaced with pure black** — `#000000` bg instead of `#08090A`. This is a 4-value shift but it removes the "warm dark" that separates Linear from generic dark-mode AI. Fix: use exactly `#08090A` as the bg ground.
3. **Bouncy entrance on UI panel** — `back.out` or spring physics on a panel reveal. Fix: replace with `power3.out` mask reveal from top to bottom; Linear does not bounce.

### aesop (Editorial / Minimalist)
1. **Bold type at any size** — any font weight above 400 anywhere in the frame. Fix: remove bold; use italic for emphasis instead; Aesop is all regular weight and italic, zero bold.
2. **Object centered with text centered below** — the composition reads as a standard product slide. Fix: asymmetric layout: object left 35% of frame, text block in the right third; never center-center stacking.
3. **Amber accent overused** — the `#7A4623` amber appears on 3+ elements. Fix: amber is one 1px rule or seal mark only; everything else is ink or sage; the amber earns its power from appearing once.

### pentagram (Information Architecture)
1. **Type fits within the frame** — the headline stays inside the safe area, centered and comfortable. Fix: scale the type to 160px+ and clip the left or right character past the frame edge; the bleed is the signature.
2. **Multiple type families** — a serif for the caption, a sans for the headline, and a mono for data. Fix: one grotesque family only; the caption uses the same family at a small weight; the discipline of one family is the recipe.
3. **Soft transition used** — a cross-dissolve or 300ms opacity fade between scenes. Fix: hard cut (zero frames) or a 120ms white flash; Pentagram does not smooth transitions.

### tufte-dataink (Information Architecture)
1. **Bar chart used instead of line chart** — bar charts invite pop animations and decorative treatment. Fix: use line charts with direct labels at endpoints; Tufte considers bar charts a low-information-density choice.
2. **Legend box present** — a separate legend area encoding color to series label. Fix: remove the legend; label the lines directly at their right endpoints; the direct label is Tufte's signature move.
3. **Dramatic number count-up animation** — a metric counter animating from 0 to 94% over 1s with bounce. Fix: no dramatic animation on data; the line draw at linear ease IS the animation; data arrives honestly, not theatrically.

### bloomberg-terminal (Information Architecture)
1. **Font size above 24px** — a "headline" at 36px or 48px in one of the panels. Fix: the terminal has no headline concept; the amber label at 24px is the maximum; all body data is 13–16px monospaced.
2. **Rounded corners on any panel** — border-radius > 2px anywhere in the layout. Fix: set `border-radius: 0` on every element; terminals are square; any rounding breaks the school immediately.
3. **Eased transitions between scenes** — a 300ms cross-dissolve between data states. Fix: instant cut (`steps(1)` or hard cut); terminals do not animate scene changes; they update instantly.

### muji-kenya-hara (Editorial / Minimalist)
1. **Object too large** — product takes up 50%+ of frame height. Fix: scale down to 25–35% of frame height; the object should feel small in a generous space, not dominant; Muji's power is the space around the object.
2. **Weight 500 or 600 used** — any font weight above 400. Fix: set all weights to 400; weight 500 may feel "barely bold" but it breaks the recipe's discipline; this recipe is weight-400-only.
3. **Motion with position change** — element slides in from x:-24px or y:-16px. Fix: opacity fade only (0→1 over 900ms); Muji elements do not move position; they materialize from the ground.

### apple-hig (Editorial / Minimalist)
1. **Feature bullets or call-outs around the product** — the product is surrounded by annotated arrows or label callouts. Fix: the product is alone on the stage; all other information lives above or below, never overlapping; the stage belongs to the product.
2. **Gradient or glow on the background** — a tech-atmosphere gradient mesh behind the product on white. Fix: the white ground is pure white `#FFFFFF` or pure black `#000000`; no gradient, no mesh, no atmosphere; Apple's gradients are on the product surface, not the background.
3. **Inter at default weight 400 for display** — the headline reads in Inter 400 rather than SF Pro Display 600. Fix: use SF Pro Display 600 or Inter Tight 600; the weight 600 + tight tracking -0.015em is part of the Apple recipe; Inter 400 is the generic web default.

### field-io (Motion / Experimental)
1. **Generative field as background decoration** — a flat colored ground with particles floating on top as decoration; the type is a flat overlay on the field. Fix: the type must EMERGE from the field, not float over it; character positions should originate from particle positions in the field system.
2. **Field freezes during the text hold** — the generative system pauses while the resolved phrase holds. Fix: the field continues to drift during the hold at all times; the hold is about the text being still, not the field; the field is always in motion.
3. **Dry ambient instead of electromagnetic drone** — silence or a stock SFX click as the bed. Fix: the bed is a layered 60–80Hz + 120Hz drone at -22dB pulsing at 0.1Hz; the field hums; without the hum, the school is not present.

### bloomberg-businessweek-turley (Brutalist / Raw)
1. **Tasteful font choice** — rounded grotesque (Futura, Circular, Nunito) at weight 700. Fix: replace with Druk Wide Heavy or Founders Grotesk 900; the typeface must feel aggressive at 160px; rounded friendly grotesques look polite at any size.
2. **Accent color softened** — `#FF8C42` (soft orange) instead of `#FF3D00` (alert orange). Fix: use full-saturation signal colors exactly: `#FF3D00`, `#FFE800`, or `#001AFF`; the recipe calls for alert-level saturation, not tonal warmth.
3. **Smooth transition used** — any eased motion or cross-dissolve. Fix: hard cut only; if transition is needed, use a 66ms (2-frame) black flash; Turley-era Businessweek does not ease into anything.

### mailchimp-freddie (Warm Humanist)
1. **AI-generated illustration style** — a Midjourney or DALL-E illustration that has no consistent hand. Fix: use a single human illustrator's style throughout; the consistency of the hand is the recipe; generic AI illustration lacks the character specificity that makes Freddie Freddie.
2. **Centered composition** — illustration centered, text centered below. Fix: illustration left 40%, tilted +5°, text block right 40%; the asymmetry and tilt are structural; removing them removes the school.
3. **Music bed with corporate energy** — upbeat generic background music. Fix: use a warm acoustic or upright-bass bed at -24dB; the music must feel hand-played, not produced; corporate music beds betray the hand-made ethos.

### stripe-press (Warm Humanist)
1. **Book displayed as a flat tile** — the book cover shown as a flat 2D image in a grid or card. Fix: the book is a photographed physical object with a real cast shadow; it must have dimensionality; cloth texture should be visible on the spine.
2. **Sans-serif at display size** — a bold grotesque headline instead of the display italic serif. Fix: GT Sectra or Domaine Display, weight 400, italic, at 80px; no bold, no sans at display; the italic serif IS the school.
3. **Cross-dissolve at 300ms** — a fast transition between book and quote frames. Fix: 1200ms cross-dissolve; Stripe Press transitions are as slow as turning a page; fast dissolves break the reverence the school requires.

### vercel-mesh (Modern Tool / Builder SaaS)
1. **Bright purple-to-cyan gradient used** — the exact AI cliché the recipe is replacing; visible as a rectangular gradient shape against a dark bg. Fix: the mesh must be feathered completely to black at all edges; there must be no visible gradient rectangle shape; the mesh is atmospheric, not decorative.
2. **More than one mesh in the clip** — hero mesh + section break mesh + card hover glow = three meshes. Fix: one mesh per clip; it appears in the hero or one section break; selective use is what makes it feel deliberate.
3. **Weight 700 on the headline** — Inter 700 or Geist 700 instead of the specified 500–600. Fix: Geist Sans 500 or Inter Tight 600; the precise weight is part of the recipe; weight 700 moves toward assertive and away from the "precision tool" register.

---

## Output Template

Copy this block when delivering a critique. All fields are required. Vague fields (e.g., "colors
could be better") are not accepted — the template enforces specificity.

```markdown
## Aesthetic Audit — [Clip Name or ID]

**Overall: X.X / 10** — [Excellent (8.0–10) / Good (6.0–7.9) / Needs work (4.0–5.9) / Failing (< 4.0)]
Calculated as: (Philosophy + Hierarchy + Craft + Motion + Sonic) ÷ 5

**Design school**: [e.g., School 2 — Editorial / Minimalist]
**Named anchor / recipe**: [e.g., Aesop Skincare — aesop.md]
**Video register**: [e.g., Premium Launch / Quiet Luxury]

**Score by dimension**:
| Dimension | Score | Key finding |
|---|---|---|
| 1. Philosophy Alignment | X / 10 | [One sentence: what school trait is present, what drifted] |
| 2. Visual Hierarchy | X / 10 | [One sentence: squint test result; what the primary element is; what competes] |
| 3. Craft Quality | X / 10 | [One sentence: spacing system, color count, font weight discipline] |
| 4. Motion Coherence | X / 10 | [One sentence: named GSAP ease used, energy level, forbidden motion present/absent] |
| 5. Sonic Harmony | X / 10 | [One sentence: material metaphor match, named SFX issue or confirmation] |

### Keep
- [Specific things done well — design language only. Example: "The amber rule `#7A4623` used at exactly
  one instance as a 1px underline creates the Aesop accent without becoming decorative." Not: "the colors
  are nice" or "the layout feels clean."]
- [Second specific strength]
- [Third specific strength — optional if fewer exist]

### Fix (sorted by severity — Critical ⚠️ first, Polish 💡 last)

**⚠️ 1. [Issue name]**
- Current: [Exact description — hex values, px sizes, ease names, specific elements — "The headline uses
  Inter 400 at 64px, centered, on a `#1E1E1E` background."]
- School requires: [What the recipe specifically calls for — "aesop.md requires GT Sectra 400 italic at
  72px, left-anchored, on chamois `#E8E4D9` ground; no sans at display size, ever."]
- Fix: [Concrete change with values — "Replace Inter 400 with GT Sectra or Lyon Text, weight 400, set
  italic. Move from centered to left x:80px anchor. Change bg to `#E8E4D9`."]

**⚡ 2. [Issue name]**
- Current: [specific]
- School requires: [specific]
- Fix: [specific with values]

**💡 3. [Issue name]** — [Polish / optional improvement]
- Current: [specific]
- School requires: [specific]
- Fix: [specific with values]

[Continue for up to 7 items. If more than 7 issues exist, group related issues into one item.]

### Quick Wins (top 3 if you have only 5 minutes)
- [ ] [Highest-impact / lowest-effort fix specific to this school and clip]
- [ ] [Second quick win]
- [ ] [Third quick win]

### School-specific verdict
[One paragraph: does this clip pass as a representative example of the named recipe? What is the
single most school-specific element that is working correctly? What is the single biggest betrayal
of the recipe's DNA? Would a practitioner of this school recognize the clip as being in their school?]
```

---

## Anti-Patterns in Video Aesthetic Critique

These are ways a critique can be technically present but practically useless. The audit should be
a tool that improves the clip, not a tool that generates approval or avoids the hard conversation.

❌ **Vague aesthetic claims without hex values, px sizes, or named eases**
Unacceptable: "the colors feel off." Acceptable: "The accent `#3B82F6` is a default SaaS blue; the
aesop recipe requires `#7A4623` amber appearing at exactly one instance in the frame."

❌ **Praising 'cinematic' or 'premium' without school grounding**
If the word "cinematic" appears in praise without specifying which school's motion posture is being
expressed, it is meaningless. Stripe Press is cinematic at 1200ms cross-dissolves and 4° book
rotation. Field.io is cinematic through generative particle choreography. These are not the same
cinematic. Naming the school is required.

❌ **Accepting any dark palette as 'premium'**
Dark background is not a school. `#000000` with purple-to-cyan gradient is the AI default. `#08090A`
with hairline borders is Linear. `#0A0E1A` with amber monospaced data is Bloomberg Terminal. `#0B0B0F`
with an electromagnetic field is Field.io. Premium requires discipline in WHAT is on the dark ground,
not just the ground itself.

❌ **Confusing motion energy with motion quality**
A Field.io clip at energy level 9/10 done poorly is worse than an Aesop clip at energy level 2/10
done precisely. Speed is not a quality signal. Restraint within the school's energy level is the
quality signal. Do not score motion coherence higher because the clip is energetic.

❌ **Treating 'minimalist' as a positive independent of the named recipe**
"The layout feels minimal and clean" is not a compliment in a Pentagram review — Pentagram is NOT
minimal. It is typographically aggressive. A "clean" Pentagram clip is an under-executed Pentagram
clip. Always evaluate against the named recipe, not against a generic aesthetic preference.

❌ **Missing the distinction between school and recipe**
"Editorial/Minimalist" is a school. "Aesop" is a recipe within that school. A clip that is
editorial minimalist in the school sense may score 5 on Philosophy Alignment if the recipe is Aesop
specifically and the chamois ground, italic serif, and amber accent are absent. Score at recipe level,
not school level.

❌ **Mixing severity tiers without a reason**
A philosophy failure (wrong school palette entirely) and a polish note (1px spacing inconsistency in
metadata labels) are not the same severity. Philosophy failures are ⚠️ Critical. Execution polish is
💡. Listing both in the same tier signals that the critic does not understand what matters.

❌ **More than 7 fix items without grouping**
If more than 7 issues are identified, group related issues: "five spacing inconsistencies across
all metadata labels" = one ⚡ item, not five separate items. More than 7 items signals the critic is
cataloging problems, not prioritizing them. The Quick Wins section exists specifically for this reason.

❌ **Accepting 'I couldn't find the right SFX' as a reason for wrong sound**
Every school has a sound direction that does not require a specific file. Aesop: use silence or a
single low ceramic bowl strike — no exotic SFX required. Bloomberg Terminal: a dry keyboard click is
in any SFX pack. Field.io: a 60–80Hz sine drone can be synthesized. Muji: silence is correct. The
school always provides an answer; the asset gap is always solvable.

❌ **Praising 'motion variety' in a school that demands consistency**
Linear and Bloomberg Terminal are schools of motion restraint. If the clip has 6 different entrance
animations on 6 different elements, that is not "variety" — it is a failure to apply the school's
consistent motion posture. Praising variety in a restraint school signals the critic is evaluating
generic motion quality, not school fidelity.

❌ **Accepting 'soft dark mode' as Bloomberg Terminal**
Dark background + amber accents + monospaced font = not automatically Bloomberg Terminal. The
terminal requires: pane grid (not a single panel), 0px border-radius, 13–24px font range only, and
instant (steps(1)) state changes. Soft dark mode with amber accents is AI-generated finance aesthetic,
not Bloomberg Terminal. The distinction is in the density, the pane grid, and the font ceiling.
