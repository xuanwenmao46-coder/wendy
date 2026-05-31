---
name: photography-director
description: Encodes the Photography and Cinematography Director layer of the Aesthetic Governor System. Governs composition principles, camera vocabulary, motion level constraints (0–100 for AI generators), lighting language, and physical imperfection directives that prevent AI-smoothness. Runs as part of Step 4.0 in flagship-video-director. Read by high-end-video-design before any shot design or AI video generation decisions are made.
---

# Photography Director

## Core Principle

The camera is not neutral. Every framing choice, every camera move (or deliberate non-move), every light direction, every depth decision is an argument about what matters. The Photography Director makes that argument before the first asset is created.

The directive: no shot is designed by default. Default framing is centered, eye-level, wide, and clean. Default framing produces forgettable output. Every composition in this production must be chosen from a vocabulary of intentional principles — and every AI image or video generation must be constrained by those principles before the prompt is submitted.

---

## The Six Composition Principles

### Principle 1 — Asymmetric Weight Distribution

**Rule:** The primary subject does not occupy the center of the frame. Place it at one third, at the edge, or in deliberate tension with the frame boundary.

**Production rules:**
- Subject placement: use a horizontal third (left third or right third) for most single-subject shots.
- Allow the subject to be partially cropped by the frame edge for tight product or portrait work — this signals confidence, not error.
- The *negative space* is compositionally active, not leftover. It must have enough area and visual quality (texture, tone, light) to hold the eye.
- Avoid perfectly centered single-subject compositions unless the subject has bilateral symmetry and the shot is monumental in intent (a single product as sculpture, a face as icon).

---

### Principle 2 — Depth and Layering

**Rule:** The frame must have at least two distinct planes of visual interest. Flat frames read as diagram, not photograph.

**Production rules:**
- Near plane: an in-focus or intentionally shallow-focus element in the near field.
- Subject plane: the primary subject at its optimal focal distance.
- Background plane: a controlled background — not neutral gray or white unless the product demands it. A wall with texture, a surface with grain, a space with depth.
- Depth of field is a creative decision, not a technical default. Very shallow depth reads as product photography precision. Deep focus reads as environmental storytelling.
- In video frames: objects at different z-distances must be visible, even if the background is blurred or dimmed.

---

### Principle 3 — Light as Architecture

**Rule:** Light direction determines the emotional character of the shot. Frontally lit subjects are flat. Raking light (45°–90° from the side) creates form. Backlight creates silhouette and depth.

**Production rules:**
- Default to single-source directional light unless the design intent requires otherwise.
- Shadows are not problems — they are the other half of the composition. A shadow with strong direction adds form, weight, and presence.
- Highlight rolloff: highlights must roll off gently into the brightest tone. Hard-clipped highlights read as digital error, not brightness.
- Shadow density: retain detail in shadows (never crush to pure black in warm or editorial modes). Exception: monochrome and brutalist modes permit deep shadows with minor detail.
- Color temperature: define one light temperature per scene and hold it. Warm key + cool fill is acceptable. Two sources of the same temperature read as flat.

---

### Principle 4 — The Empty Frame

**Rule:** The most powerful compositional device in premium photography is empty space that has been designed, not leftover. Negative space must earn its area.

**Production rules:**
- Minimum negative space target: 35–50% of frame area in editorial and luxury registers.
- Negative space must have tonal quality — a warm off-white, a deep near-black, a textured surface. Pure neutral gray negative space is digital default, not designed.
- Empty sky, open ground, white wall, dark ground — all are legitimate subjects, not backgrounds.
- Typography, captions, and supporting elements live in negative space — place them in the visual void of the image, not on top of the subject.

---

### Principle 5 — Human Scale Reference

**Rule:** When human subjects appear, the camera relates to them at a scale that establishes a specific emotional relationship. Wide shots create context; medium shots create story; close-ups create intimacy.

**Production rules:**
- Choose one primary scale per scene and commit to it. Scale changes within a scene must be motivated by narrative, not variety.
- Avoid the "polite medium": subject centered, shoulders to knees, expression forward. This is the most forgettable framing in photography. Push closer or pull wider.
- In portraits: allow partial cropping — top of head, chin, or shoulder may exit the frame. Tight framing on the face is more powerful than showing the full head with margin.
- Environment inclusion: when the environment is part of the story, allow the subject to be small within it. The figure-to-environment ratio communicates who is dominant.

---

### Principle 6 — Still Life and Object Composition

**Rule:** Products, objects, and tools must be photographed with the same compositional intentionality as portraits. The object has a face, a profile, and a best angle — find them.

**Production rules:**
- Show the defining detail: the quality that makes this object specific must be visible — texture, material, edge quality, mechanism, proportion.
- Surface relationship: the object must relate to its surface. A product floating in void reads as catalog. A product resting on a considered surface reads as editorial.
- Shadow play: intentional shadows from direct light sources reveal form and add presence. Shadowless frontal shots read as product catalogs.
- Scale context: include an element that establishes scale — a hand, a familiar object, a reference surface.

---

## Camera Vocabulary

Three and only three camera languages are permitted for premium work. Choose one per shot; do not combine them in a single movement.

### Language 1 — Slow Zoom
**Movement:** Camera scale increases or decreases slowly over the duration of the shot.

**Rate limit:** Maximum **3% scale change per second**. At 3%/s, a 5-second shot moves from 1.00× to 1.15× scale — a barely perceptible approach that the viewer feels rather than notices.

**Direction:**
- Zoom in (push): subject grows in frame → creates intimacy, emphasis, arrival.
- Zoom out (pull): subject shrinks → creates context, distance, reveal.

**Easing:** Always ease in and out. `cubic-bezier(0.25, 0.10, 0.25, 1.00)` for standard; `cubic-bezier(0.45, 0, 0.55, 1)` for ambient drift.

**Forbidden:** Never combine slow zoom with a pan in the same movement. Never exceed 3%/second. Never zoom into a frame that does not have detail worth approaching.

---

### Language 2 — Slow Pan
**Movement:** Camera translates horizontally across the subject or environment.

**Rate limit:** Maximum **5% of frame width per second**. At this rate, a 5-second pan covers 25% of the scene width — a deliberate reveal, not a search.

**Direction:**
- Left to right: follows the natural reading direction; creates ease and flow.
- Right to left: creates friction, reversal, or resolution.

**Easing:** Same as slow zoom. Begin from rest, accelerate to rate, decelerate to rest. Never constant velocity (linear panning reads as security camera, not cinema).

**Forbidden:** Never combine with zoom. Never pan to find a subject — the subject should be at the endpoint, not discovered mid-pan. Never pan faster than 5% frame width per second.

---

### Language 3 — Static Shot with Moving Elements
**Movement:** The camera does not move. Only elements within the frame have motion.

**Status:** This is the highest-status camera language for premium and luxury work. Restraint in camera movement signals confidence. The composition is strong enough to hold the frame without assistance.

**What moves:**
- Subject actions (product interactions, hand gestures, text elements entering/exiting).
- Environmental elements (fabric moving, liquid pouring, light changing).
- Typographic elements (arriving, settling, departing).

**Easing:** Element-level easing follows `motion-graphic-design` and `aesthetic-governor` motion posture rules.

**Why this is the default:** Camera movement is a compensation strategy — when the composition is weak, movement distracts from its weakness. Strong compositions do not require compensation. Default to static shot; introduce camera movement only when the shot's narrative requires it.

---

## Motion Level Guide (0–100 for AI Video Generators)

When AI video generation tools are in the pipeline, the motion level parameter controls how much movement is generated. This parameter has a hard ceiling for premium work.

| Level Range | Register | Use cases |
|---|---|---|
| **0–15** | Maximum restraint | Luxury editorial, still-life, luxury product photography treated as video, fashion campaign stills with minimal drift |
| **16–35** | Measured movement | Premium SaaS, quiet brand film, editorial data story, architectural photography in motion |
| **36–60** | Active | Feature demo, product workflow, explainer, documentary |
| **61–80** | High energy | Brand film, launch event, kinetic sequence, dance or sport |
| **81–100** | **FORBIDDEN** | This range produces temporal jitter, subject deformation, loss of compositional control, and the characteristic AI-generated aesthetic. It is incompatible with premium work. Do not use under any circumstance. |

**Rule:** When in doubt, use a lower number. A motion level that is too low produces a stable, slightly static clip — acceptable. A motion level that is too high produces degradation — unacceptable.

---

## Lighting Language

### Directional Key Light
The primary light source gives the subject direction, form, and presence. Frontally diffuse light erases form. Directional light creates it. For every scene, specify:
- **Key light angle:** 0° (front) / 45° (three-quarter) / 90° (side raking) / 135° (rim/hair) / 180° (backlight)
- **Key light temperature:** warm (2700–3200K), neutral (4000–4500K), cool (5600–6500K), or mixed (intentional discord)

### Fill and Shadow Ratio
The contrast between the lit side and the shadow side determines the emotional weight of the shot.
- **Low ratio (2:1 or less):** Soft, even, accessible — appropriate for warm humanist and educational registers
- **Medium ratio (4:1):** Standard editorial — dimensionality without drama
- **High ratio (6:1 or more):** Dramatic, authoritative, noir — appropriate for monochrome, duotone, and brutalist registers

### Forbidden Lighting
- Ring light artifacts (the concentric circle reflected in eyes or product surfaces) — reads as YouTube, not editorial
- Flash fill that erases all shadow from the subject — looks like passport photo, not design
- Multiple visible hotspots on a single product surface — inconsistent light sources signal bad production
- Perfect even lighting across the full frame — this is photo studio default, not designed space

---

## Physical Imperfection Directives

AI-generated and digitally rendered material has inherent smoothness — it is too perfect. Physical media has inherent imperfection — it is real. These four directives introduce the imperfections that signal authenticity.

### Directive 1 — Lens Breathing
**What it is:** A very slow, barely perceptible change in the focal length over the duration of a shot, simulating the mechanical breath of an optical lens held by a human operator.

**Implementation:** Scale 1.000 to 1.012 over 4–6 seconds, then back to 1.000, using `cubic-bezier(0.45, 0, 0.55, 1)`. This is below the threshold of conscious perception — the viewer does not notice the zoom but feels the presence.

**Do not:** Apply lens breathing to text elements. Apply only to image layers or background elements.

---

### Directive 2 — Vignette
**What it is:** A subtle darkening at the frame edges, simulating the light falloff characteristic of wide aperture lenses.

**Implementation:**
```css
/* CSS vignette overlay */
.vignette-overlay {
  position: fixed;
  inset: 0;
  pointer-events: none;
  background: radial-gradient(
    ellipse at center,
    transparent 60%,
    rgba(0,0,0,0.18) 100%
  );
  z-index: 8999;
}
```

**Strength by register:**
- Luxury editorial: 0.12–0.18 opacity at edge
- Premium SaaS / dark ground: 0.08–0.12 opacity at edge
- Brutalist / bold poster: none — vignette softens what must be hard

---

### Directive 3 — Chromatic Aberration (Minimal)
**What it is:** Extremely subtle color fringing at high-contrast edges, simulating the chromatic aberration of real optical lenses.

**Implementation:** A 1–2px horizontal offset of a very low-opacity red channel layer on high-contrast edges. Visible only on close inspection; felt as "photographic quality" overall.

**Constraint:** Maximum 2px offset. Maximum 0.15 opacity. Apply only at hard edges between very bright and very dark values. If in doubt, omit — overdone chromatic aberration is an aesthetic cliché.

---

### Directive 4 — Motion Blur on Fast Elements
**What it is:** When elements travel quickly across the frame (kinetic type, object entries), a directional blur in the direction of travel simulates shutter exposure.

**Implementation:** CSS `filter: blur(Xpx)` applied briefly during the fastest portion of the travel, then removed as the element decelerates.

**Rule:** Apply blur only to elements moving faster than 200px/0.1s (2000px/s). For slower movements, no blur is needed or appropriate. Never apply blur to a stationary element.

---

## Composition Audit Checklist

Before finalizing any shot design or AI generation prompt, verify:

1. **Composition principle is named.** One of the six principles above has been selected and the framing decision is traceable to it.
2. **Camera language is locked.** One of the three camera languages (Slow Zoom / Slow Pan / Static) has been designated. No other movement is permitted.
3. **Motion level is within range.** For AI generation, the motion level is ≤ 80. For premium work, it is ≤ 60.
4. **Negative space is designed.** The empty areas of the frame have tonal quality — they are not neutral gray or default white.
5. **Light direction is defined.** The key light angle and temperature are specified. The shadow side of the subject is visible.
6. **At least one imperfection directive is active.** Film grain (COLOR-DIRECTOR.md), vignette, lens breathing, or motion blur must be present. Frictionless digital perfection is not permitted.
7. **Composition passes the empty-frame test.** If all text and graphic elements were removed, would the remaining image still be a well-composed photograph? If no — the visual design is carrying a weak shot. Fix the shot first.
8. **AI prompt contains composition language.** If AI generation is in the pipeline, the prompt includes: framing description, light direction, depth-of-field intent, and motion level parameter.
