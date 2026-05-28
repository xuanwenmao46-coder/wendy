# Aesthetic Quality Audit

Use this after generating a clip design brief or a rendered frame, and before declaring implementation complete. Run after the visual brief, after Remotion Studio preview, and after final render.

**Critique the design, not the designer.** Be specific, grounded in the named school's DNA, and actionable — not vague taste claims.

---

## The Five Dimensions

### 1. Philosophy Alignment

Does every design decision trace back to the named design school and anchor?

| Score | Standard |
|---|---|
| 9–10 | Every element — palette, type, composition, motion, sound — embodies the named anchor. Nothing reads as "borrowed from elsewhere." |
| 7–8 | Direction is correct; 1–2 minor drift moments (e.g., a slightly rounded corner in Brutalist, a warm accent in Tool/SaaS). |
| 5–6 | Intent visible, but cross-school contamination dilutes character (e.g., "minimalist" with 5 feature cards, or "brutal" with a soft ease-in). |
| 3–4 | Named the school but borrowed only surface traits (dark background ≠ Experimental; white space ≠ Editorial Minimalist). |
| 1–2 | No detectable relationship to the named school; could belong to any of the 6. |

**What to look for**:
- Are the named anchor's signature moves present? (Pentagram → type as structural image; Aesop → serif-only, one accent, product as protagonist; Linear → hairline borders, warm dark, < 5% accent)
- Do palette, type, motion, and sound agree on the same school — or does the palette say "Minimalist" while the motion says "Experimental"?
- Are any of the school's **forbidden elements** present? (See STYLE-SCHOOL-MAP.md — each school lists 6+ forbidden elements specific to its DNA)
- Could this design be mistaken for a different school? If yes, identify which school it drifted toward.

**School-specific alignment checks**:
- **Information Architecture**: Is every text block left-aligned? Is the grid strict? Is there exactly 1 accent element? Is all data mono + tabular?
- **Editorial / Minimalist**: Is negative space ≥ 40%? Is the product treated photographically (not diagrammatically)? Is the motion energy ≤ 2/10?
- **Motion / Experimental**: Is the design in continuous motion? Is there a legible landing every 2–4s? Is the motion continuous rather than episodic?
- **Brutalist / Raw**: Is the type at absurd scale? Is the palette pure contrast? Is there zero ease on motion? Is something deliberately uncomfortable?
- **Warm Humanist**: Does it feel human-made? Is the palette warm? Is the motion organic? Is there sound warmth (no UI clicks)?
- **Modern Tool / Builder SaaS**: Is the product UI visible and in action? Are borders hairline (1px)? Is the accent < 5% of pixels?

---

### 2. Visual Hierarchy

In 2 seconds, does a viewer know where to look first, second, and third?

| Score | Standard |
|---|---|
| 9–10 | Primary / secondary / tertiary reads are unambiguous. Squint test: hierarchy survives blurring. |
| 7–8 | Primary clear; 1–2 secondary elements compete; minor muddy zone. |
| 5–6 | Title vs. body distinguishable, but subtitle, caption, metadata collapse into same visual weight. |
| 3–4 | Information sits flat — no obvious entry point. |
| 1–2 | Chaotic — the eye finds no resting place. |

**What to look for**:
- **Squint test**: squint until the frame blurs. Is the primary element still the brightest, largest, or most distinct point? If the data panel and the headline look the same weight when blurred, the hierarchy has failed.
- **Size ratio**: display vs. support ≥ 2.5× (ideally 4–6× for hero display at 720p)
- **Color/weight building 3–4 levels**: hero size + accent color at level 1; support size at level 2; metadata at level 3
- **Whitespace directing gaze**: negative space should frame and isolate the primary element, not create confusion about where to look
- **Motion serving hierarchy**: does the first element to animate correspond to the primary information?

---

### 3. Craft Quality

Pixel-level execution: alignment, spacing discipline, color control.

| Score | Standard |
|---|---|
| 9–10 | Every element aligns, spacing is systematic, color is controlled (≤ 4 values), fonts consistent. |
| 7–8 | Refined overall; 1–2 minor spacing or alignment inconsistencies. |
| 5–6 | Basically aligned, but spacing is ad-hoc, color count is loose, font weights drift. |
| 3–4 | Obvious alignment errors, chaotic spacing, 6+ colors, mixed font weights without logic. |
| 1–2 | Looks like a rough draft; no visible design system. |

**What to look for**:
- **Spacing system**: does the clip use a consistent spacing multiplier? (16/32/48/80 at 720p — or the school's chosen scale)
- **Same-class element consistency**: do all metadata labels use the same size, weight, and position rules? Do all UI chip labels look identical?
- **Color discipline**: count the distinct colors in the frame. Premium work uses ≤ 4 (background + foreground + accent + material). More than 4 requires justification.
- **Font consistency**: is the font family the same across all instances of the same text role? Are weights following the chosen pairing, not drifting?
- **Edge alignment**: text blocks should align to defined edges, not float arbitrarily. Check that left edges line up, that bottom baselines are consistent within a region.
- **Video-specific craft checks**:
  - Text ≥ 26px at 720p (16px web ≈ 35px video at arm's length)
  - Product image is sharp at render size (not blurry or over-compressed)
  - No JPEG artifact visible on background or hero image at final resolution
  - No text color / background color near-match that makes reading difficult in motion

---

### 4. Motion Coherence

Does the motion reinforce the aesthetic school, or fight it?

| Score | Standard |
|---|---|
| 9–10 | Every motion choice — ease, duration, energy, transition type — is consistent with the school's motion posture. |
| 7–8 | Motion is mostly correct; 1–2 beats use the wrong energy or ease (e.g., a `back.out` spring in an Editorial/Minimalist clip). |
| 5–6 | Motion is technically competent but feels wrong for the school; the clip could belong to a different aesthetic. |
| 3–4 | Motion contradicts the school (slow reverence for a Brutalist clip; aggressive slam cuts in Warm Humanist). |
| 1–2 | Motion feels random relative to any identifiable aesthetic. |

**What to look for**:
- **Ease accuracy**: does the GSAP ease match the school? (`sine.inOut` for Editorial; `steps(1)` for Brutalist; `expo.out` for Experimental; `power3.out` for Tool/SaaS)
- **Energy level match**: does the motion energy (1–10) match the school's defined level? (See STYLE-SCHOOL-MAP.md Quick Reference)
- **Transition type**: hard cut (Brutalist), soft dissolve (Editorial), match-cut or morph (Experimental), precision mask (Tool/SaaS), organic fade (Warm Humanist), typographic wipe (Information Architecture)
- **Hold duration**: do holds feel right for the school? (Editorial: 2–3s; Brutalist: 0.1s flash OR uncomfortable 3s; Tool/SaaS: 0.8–1.2s)
- **Forbidden motion check**: has the school's forbidden motion appeared? (Bounce in Editorial, particle burst in Information Architecture, slow fade in Brutalist)
- **Motion narrative**: does the motion sequence have a structure (intro → hit → hold → out) that matches the beat map? Is every major beat visually acknowledged?

---

### 5. Sonic Harmony

Does the sound fit the material metaphor of the chosen school?

| Score | Standard |
|---|---|
| 9–10 | Sound is indistinguishable from the visual school — if you close your eyes, you can still identify the school from the audio alone. |
| 7–8 | Sound fits the school; 1 cue drifts to another school's sonic character. |
| 5–6 | Sound is generic — present and functional, but no specific school identity. |
| 3–4 | Sound contradicts the school (cinematic swell for Brutalist; UI click for Warm Humanist). |
| 1–2 | Sound is wrong — causes cognitive dissonance with the visual design. |

**What to look for**:
- **Material metaphor match**: does the sonic material (paper/metal/glass/organic/electronic) match the school? (See STYLE-SCHOOL-MAP.md sonic section per school)
- **Transient shape accuracy**: dry snap (Information Architecture/Brutalist) or soft swell (Editorial/Warm Humanist) or custom electronic (Experimental) or precise click (Tool/SaaS)
- **Density appropriateness**: is the SFX count right for the school? (Sparse 3–5: Info Arch, Editorial; Dense/continuous: Experimental; Medium: Tool/SaaS, Warm Humanist)
- **Forbidden sound check**: does the clip use a sound explicitly forbidden by the school? (Warm organic whoosh for Brutalist; UI click for Editorial/Minimalist; cinematic swell for Tool/SaaS)
- **Narration integration**: if narration exists, do SFX land at phrase boundaries, not inside spoken words? Is narration the primary audio track and SFX subordinate?
- **Silence usage**: does the clip use silence intentionally? (Editorial and Brutalist both use silence, for opposite reasons — luxury restraint vs. aggressive confrontation)

---

## Per-School Common Failures

### Information Architecture
1. **Color range creep** — accent used on 4+ elements; becomes decorative, not structural. Fix: restrict accent to one structural element only.
2. **Generic sans for display** — Inter, Roboto, Poppins. Fix: replace with bold condensed (Barlow Condensed 800, Neue Haas Grotesk 75 Black).
3. **Soft audio** — warm whoosh or cinematic swell. Fix: replace with dry snap or scoreboard thud; remove reverb.

### Editorial / Minimalist
1. **Insufficient negative space** — frame is 70%+ filled. Fix: remove elements until negative space reaches 40%+.
2. **Wrong motion energy** — any entrance faster than 400ms, or any bounce/spring. Fix: slow everything to 600–900ms `sine.inOut`.
3. **Warm humanist confusion** — illustration or friendly illustration instead of product/object as hero. Fix: use clean photographic treatment; remove illustration.

### Motion / Experimental
1. **Static hold too long** — more than 1.5s without motion event. Fix: add continuous secondary motion or reduce hold; design lives in transition.
2. **Legible landing missing** — viewer cannot read the primary message. Fix: add one 0.5s+ legible landing every 2–4s.
3. **Generic SFX** — whoosh pack used without sonic design. Fix: design the soundscape; the sound must be as intentional as the visual.

### Brutalist / Raw
1. **Soft ease used** — `ease-out`, `power2.out`, any spring. Fix: replace with `steps(1)` or `power4.in` for snaps; hard cut for transitions.
2. **Comfortable middle ground** — 30–50% negative space feels designed. Fix: go to 0% (full bleed) or 90%+ (desert); eliminate the comfortable.
3. **Warm audio** — soft whoosh or organic sound. Fix: replace with dry stamp, paper slice, or vinyl crackle; no reverb.

### Warm Humanist
1. **Cold palette drift** — cool gray or pure white background. Fix: tint background to warm: `#FFF8EE` or `#F5EDD6`.
2. **UI click sound** — the most common error. Fix: replace with soft air, paper rustle, or warm low note; never UI mechanical sound.
3. **Information density too high** — feature card grid or data panel. Fix: one warm visual, one warm headline; remove everything else.

### Modern Tool / Builder SaaS
1. **Purple-pink gradient background** — the defining AI-default cliché for this school. Fix: use warm dark ground `#111110` + single accent < 5%.
2. **Product image without behavior** — product shown as static screenshot. Fix: animate UI state (generating, selecting, progress); product must perform.
3. **Organic motion** — slow fade, parallax, or spring physics. Fix: replace with precise `power3.out` micro-entrances; UI assembly animation.

---

## Output Template

Copy this when delivering a critique:

```markdown
## Aesthetic Audit

**Overall: X.X / 10** — [Excellent (8+) / Good (6–7.9) / Needs work (4–5.9) / Failing (<4)]

**Design school**: [School name]
**Named anchor**: [Designer/studio/brand]

**By dimension**:
- Philosophy Alignment: X / 10 — [one sentence: where it lands, what drifted]
- Visual Hierarchy: X / 10 — [one sentence: squint test result, where hierarchy fails]
- Craft Quality: X / 10 — [one sentence: spacing, color count, font consistency]
- Motion Coherence: X / 10 — [one sentence: ease accuracy, energy level, forbidden motion]
- Sonic Harmony: X / 10 — [one sentence: material metaphor match, forbidden sound found]

### Keep
- [Specific things done well, in design language: "The amber rule used exactly once creates the Pentagram structural accent without becoming decorative" — not "the colors are nice"]

### Fix (sorted by severity)

**1. [Issue name]** — ⚠️ Critical / ⚡ Important / 💡 Polish
- Current: [what it looks like now, specific]
- School expects: [what the named anchor's DNA requires]
- Fix: [concrete change with values — "replace `sine.out` 400ms with `power3.out` 250ms", not "make it faster"]

**2. [Issue name]** — ⚠️ / ⚡ / 💡
…

### Quick Wins (top 3 if you only have 5 minutes)
- [ ] [Highest-impact, lowest-effort fix for this school]
- [ ] [Second]
- [ ] [Third]
```

---

## Audit Anti-Patterns

❌ **Vague aesthetic claims**: "the colors feel off" — unacceptable. "The `#3B82F6` accent is a SaaS-blue cliché; the Aesop school requires amber/sage at < 3% of frame" — correct.

❌ **Praising "cinematic" or "premium" without school grounding**: if the word "cinematic" appears in praise without explaining which school's cinematic quality it expresses, it means nothing.

❌ **Accepting any dark palette as "premium"**: dark background alone is not premium. It may be Brutalist (high contrast), Experimental (generative), or Tool/SaaS (warm dark). Premium without restraint and careful detail is just dark.

❌ **Confusing motion energy with quality**: fast motion is not better motion. Editorial/Minimalist at energy level 2/10 done correctly beats sloppy Experimental at 9/10.

❌ **Mixing severity**: a critical philosophy failure (wrong school entirely) listed alongside a polish note (1px spacing inconsistency) in the same tier. Always sort ⚠️ → ⚡ → 💡.

❌ **More than 7 fix items**: group related issues ("five spacing inconsistencies across metadata labels" = one item).

❌ **Accepting "I couldn't find the right SFX"**: for School 2 (Editorial), the right choice is silence; for School 3 (Experimental), design the sound; for School 4 (Brutalist), use a dry stamp. The school always has an answer — the asset gap is solvable.
