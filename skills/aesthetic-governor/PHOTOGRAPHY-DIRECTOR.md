---
title: Photography Director
system: Aesthetic Governor System
layer: Cinematography / Shot Direction
version: 1.0.0
status: production
last_updated: 2026-05-31
---

# Photography Director

## Core Principle

Every frame is a still photograph first. Before motion is considered, the frame must work as a held image — composition, light, tonal weight, subject placement, and depth must all resolve into a coherent photograph. If the frame fails as a still, it fails as a moving image. Motion does not rescue a poorly composed frame; it amplifies its failures.

Camera movement, when employed, must earn its place through dramatic or communicative necessity. Movement that exists because the editor was filling time, because the generator defaulted to motion, or because stillness felt too "boring" is illegitimate movement. It will read as cheap.

Static shots with internal motion — a subject moving through a held frame, light shifting across a still composition, typography entering a perfectly held environment — are the highest status camera language available. They signal confidence. They say the frame is strong enough to hold without needing to move.

The Camera Director's first instinct is stillness. Motion is approved, not defaulted.

---

## Composition Principles

### 1. Rule of Thirds

**Production Rule:** Divide the frame into a 3×3 grid. The primary subject — the element that carries the scene's meaning — is placed at one of the four intersection points. The most common premium placement is the left-center or right-center intersection, with the subject facing or oriented toward the larger negative space.

**Where Not to Place:** Center frame is forbidden in premium composition unless the subject is a geometric form or symmetrical product that requires axial alignment. Center framing reads as amateur snapshot or deliberate conceptual statement — there is no middle ground. If center framing is used, it must be an explicit choice with a clear reason, not a default.

The primary subject is never placed in the outer 15% of the frame (frame-edge contact). This creates discomfort without intention. If a subject is near the frame edge, it is a deliberate cut or a deliberate tension — it must be one or the other, never accidental.

---

### 2. Negative Space

**Production Rule:** Negative space is not empty space. It is active compositional force. The empty areas of a frame carry the visual weight of the subject — they define what the subject is by defining what surrounds it.

Minimum negative space allocations by school:

| School | Minimum Negative Space | Character |
|---|---|---|
| Minimalist Precision | 55% | The frame is mostly void. The subject is an island. |
| Editorial Luxury | 45% | Subject has breathing room. Luxury cannot feel crowded. |
| Bold Statement | 30% | Negative space is the color contrast, not void |
| Warm Human | 40% | Space is filled with warm atmosphere, not hard void |
| Dark Premium | 50% | Dark ground is the negative space |
| Monochrome Film | 45% | Tonal void as compositional tool |

"Intentional void" means the negative space has been specifically shaped. A subject in the lower-right intersection with intentional void in the upper-left has a directionality — the eye travels from subject to void and the void communicates something (possibility, loneliness, anticipation). Negative space with no directional intention is just an undercomposed frame.

---

### 3. Foreground Layering

**Production Rule:** Depth in a video frame is achieved through the separation of foreground, mid-ground, and background planes. In the absence of 3D rendering or physical depth of field, depth must be constructed compositionally.

Practical foreground layering techniques for AI-generated and produced video:

- **Hard edge foreground element (10–20% frame coverage):** A sharp edge — architectural corner, product edge, desk surface edge — placed in the foreground plane, slightly out of focus or at the frame border, implies the camera is inside a space rather than observing a flat image.
- **Surface plane at bottom of frame:** The inclusion of a surface (table top, floor plane, paper texture) at the bottom 15–20% of the frame immediately establishes a real-world spatial relationship.
- **Atmospheric separation:** If the foreground element is identifiably closer through focus or tonal value (slightly darker or lighter than the mid-ground), the brain reads depth.

**The 3D render exception:** Specifying foreground layering in AI generation prompts (e.g., "shallow depth of field, foreground element slightly blurred, out of focus foreground") is more reliable than attempting composited layering in post. Prompt for it at generation time.

---

### 4. Leading Lines

**Production Rule:** Leading lines direct the eye through the frame toward the primary subject or the intended focal point. In video, leading lines that point toward the subject anchor the viewer's attention across the duration of the shot.

Categories of leading lines in premium video:

- **Architectural lines:** Edges of walls, floor-ceiling junctions, window frames, doorways. These are the most reliable leading lines because they are inherent to the environment, not constructed.
- **Product lines:** The edge geometry of the product itself — a laptop edge, a bottle silhouette, a book spine — creates leading lines from the product toward the viewer or toward associated elements.
- **Typographic leading lines:** When typography is present in frame, the baseline of headline text creates a horizontal leading line. Vertical type alignment creates vertical leading lines. These should be used to direct attention toward the primary visual subject, not away from it.
- **Light falloff lines:** The boundary between a lit area and shadow creates an implicit leading line. When this boundary is straight (hard light through a window) it functions as a compositional line.

**The forbidden leading line:** A leading line that directs attention out of the frame — toward the frame edge rather than toward the subject — creates visual exit rather than visual engagement. Check the direction of all leading lines before rendering.

---

### 5. Asymmetric Balance

**Production Rule:** Asymmetric balance is the deliberate distribution of visual weight across a frame in a way that is unequal in placement but equal in total weight. A large, light object on the left can be balanced by a small, dark object on the right. A subject near center-left can be balanced by a typographic element at upper-right.

When to use asymmetric balance: In all editorial and premium contexts. Symmetric balance (centered subject, bilateral symmetry) is the compositional default of graphic design templates and should be overridden in favor of asymmetric balance in any context requiring visual sophistication.

How to break symmetry deliberately:
- Shift the primary subject 15–25% off-center.
- Introduce a secondary visual element at a different position, size, or tonal weight to counterbalance.
- Use negative space as one side of the balance — the void balances the weight of the subject.

The failure of asymmetric balance: An asymmetric composition that feels unresolved is not balanced asymmetrically — it is simply unbalanced. The test is whether the frame feels intentional when viewed at a distance. If something feels "wrong" or "off," the balance has failed. Correct by adjusting the weight relationship between the subject and the counterbalancing element.

---

### 6. Depth Framing

**Production Rule:** Depth framing uses in-frame elements to create a secondary frame around the primary subject. This second frame — a doorway, a window, an arch, the gap between two foreground elements, the negative space between two vertical elements — places the primary subject inside a contained visual field, increasing its importance and creating a sense of discovered intimacy.

**Frame within a frame techniques for premium video:**
- Doorway framing: Subject is visible through an architectural opening. The opening is in the foreground plane; subject is in the mid-ground.
- Window frame overlap: The edges of a window frame appear at the sides of the shot, enclosing the primary visual field.
- Object gap framing: Two objects in the foreground are separated by a gap through which the subject is seen — desk items, shelving, architectural elements.
- Edge elements: Partial elements at the frame edges (a blurred shoulder, a wall edge, a surface corner) establish that the camera is inside a physical space, which frames the entire mid-ground as a contained world.

Depth framing is the compositional tool most frequently missing from AI-generated video content. Specifying it in prompts — "shot through a doorway," "framed by foreground elements," "frame within a frame composition" — significantly increases the spatial sophistication of generated material.

---

## Camera Movement Taxonomy

Three acceptable camera languages for premium video. No others.

### 1. Slow Zoom In / Out

**Definition:** A continuous, minimal magnification change creating the impression of the camera moving toward or away from a subject. Distinguished from a digital crop zoom — the entire frame scales proportionally with no reframing.

**Rate:** Maximum 3% magnification change per second at 1080p. At 4K, maximum 2% per second. A 5-second zoom in covers approximately 10–15% total magnification change. Any faster reads as a push or dramatic zoom — a different technique not permitted in premium production.

**Easing:** Ease in, ease out (both ends). No linear zoom. The acceleration curve should be barely perceptible — the viewer should feel the zoom without being able to identify the exact moment it begins or ends.

**When to Use:**
- Slow zoom IN: Building emphasis on a static subject over time. Pulling the viewer toward a detail or face. Increasing intimacy in a testimonial or portrait segment.
- Slow zoom OUT: Revealing context. Moving from detail to environment. Creating a sense of release or completion at the end of a sequence.

**When Forbidden:** Product detail shots (zooming changes the perspective relationship with the product — use a held static instead), any sequence where the primary content is text (zooming text creates unnecessary motion tension), consecutive zooms in the same direction within a single sequence.

---

### 2. Slow Pan Left / Right

**Definition:** A horizontal rotation of the camera about its vertical axis, traversing a scene at a controlled rate. Distinct from a tracking shot (which involves physical translation of the camera).

**Rate:** Maximum 5% of frame width per second for premium applications. A 4-second pan covers approximately 20% of horizontal range. Faster pans require motion blur to read as intentional — without motion blur, fast pans read as camera shake or mistake.

**Easing:** Ease in, hold at target speed, ease out. The target speed (middle of the pan) is constant. The ramp-in and ramp-out prevent jarring starts and stops. Total easing occupies approximately 20% of total pan duration at each end (so a 4-second pan: 0.8s ease in, 2.4s constant, 0.8s ease out).

**When to Use:**
- Revealing a horizontal environment — a workspace, a product lineup, an architectural surface.
- Following a subject's horizontal movement through a scene.
- Connecting two related elements by panning from one to the other.

**When Forbidden:** When the subject of the shot is static and there is no environmental information to reveal (a slow pan across a neutral background with a static subject is purposeless movement). Panning away from the primary subject without a clear destination. Two successive pans in opposite directions within the same sequence — this creates visual disorientation.

---

### 3. Static Shot with Moving Elements

**Definition:** The camera position, angle, and focal length are held completely fixed. All motion within the frame is internal — subjects move through the frame, light changes, typography enters and exits, atmospheric elements (steam, fabric, particles) move.

**Why This Is the Highest Status:** Static shots demonstrate compositional confidence. The composition is so resolved that it does not need movement to sustain viewer engagement. Internal motion — a person moving through a perfectly composed environment, a product revealing itself through moving light — is more sophisticated than camera movement because it puts the composition first and motion second.

**What "Internal Motion" Means:**
- A subject walking through a held frame (the camera does not follow — the subject enters, crosses, exits while the frame holds).
- Light changing across a static surface — a cloud shadow crossing a desk, golden hour light shifting across a wall.
- Typography or graphic elements entering and exiting a held environmental frame.
- Atmospheric motion — steam rising from a product, fabric settling, a page turning.
- Depth-of-field rack on a static composition — one element comes into focus as another goes soft.

**The Production Note:** In AI video generation, "static camera" with "internal motion" is a specific instruction. Specify: "static camera, no camera movement, subject moves through frame" to prevent generators from defaulting to camera motion. Internal motion is the hardest to generate by default — it requires explicit instruction.

---

## Motion Level Guide

For AI video generators using a 0–100 motion level scale. Apply to any generator that exposes this parameter.

### 0–15: Maximum Restraint

**Use Cases:** Luxury product stills with minimal atmospheric motion, editorial photography with barely-perceptible light shift, museum-quality presentation, hero brand moments requiring held contemplation.
**What is Moving:** Atmospheric breath only — very slight air movement, imperceptible light shift, the finest grain animation.
**Character:** The footage is nearly indistinguishable from a still image on first viewing. The motion is discovered, not presented.
**Schools:** Minimalist Precision, Editorial Luxury at its most severe, Monochrome Film.

---

### 16–35: Measured

**Use Cases:** Premium SaaS product sequences, calm brand narrative, interview segments, workspace environments, content where trust and stability are the primary register.
**What is Moving:** Slow internal motion — a cursor moving through an interface, a hand placing an object, subtle atmospheric movement in a background element. No camera movement unless explicitly permitted.
**Character:** Motion is present and readable but does not accelerate or urgently direct attention.
**Schools:** All schools at their measured register. Safe default for premium B2B content.

---

### 36–60: Active

**Use Cases:** Feature demonstrations, product workflow sequences, how-it-works segments, product interaction, explainer sequences where step-by-step communication is load-bearing.
**What is Moving:** Clear purposeful motion — interface interactions, product being used, hands moving through tasks, elements building in sequence.
**Character:** The viewer's eye follows motion through the frame. Motion is functional — it communicates a process.
**Schools:** Bold Statement in its functional mode. Warm Human at its most engaged.

---

### 61–80: High Energy

**Use Cases:** Brand film climax sequences, kinetic montage, launch moments, product reveal sequences requiring excitement.
**What is Moving:** Multiple elements in motion, faster transitions, energetic subject movement.
**Character:** The viewer must track motion actively. Useful in short bursts — 5–10 seconds maximum before returning to a lower motion register.
**Schools:** Bold Statement at its most energetic. Any school in a climax moment.

---

### 81–100: FORBIDDEN FOR PREMIUM WORK

**Why Forbidden:** Motion levels above 80 in AI video generators produce the specific artifacts that mark output as AI-generated: temporal jitter, subject deformation across frames, background instability, motion blur applied inconsistently, facial features that shift between frames.

High motion levels do not create a "more dynamic" result. They create the AI aesthetic — the shimmering, unstable, slightly-wrong quality that viewers recognize even without being able to name it. The 81–100 range must not be used in any premium production context regardless of the desired energy level. Achieve high energy through editing rhythm (shorter clip duration, faster cut rate) and internal motion, not through increasing the generator's motion parameter.

---

## Lighting Language

### Preferred Lighting Descriptions (for prompts and production direction)

| Term | Definition | Use Case |
|---|---|---|
| Chiaroscuro | Strong contrast between light and shadow, with shadow occupying significant frame area | Portrait, narrative brand film, Dark Premium aesthetic |
| Volumetric light | Light that is visible as it passes through atmosphere — shafts, beams, dust motes | Scenes requiring grandeur, workspace environment, craft and material storytelling |
| Soft natural diffusion | Light that has passed through a diffusing medium — overcast sky, sheer curtain, bounce — creating soft shadows with no hard terminator | Lifestyle, warm human, product shot with texture emphasis |
| Rembrandt lighting | One primary light source at 45°, creating a triangle of light on the shadow-side cheek | Portrait, interview, human-forward brand storytelling |
| Window light | Natural or simulated daylight entering from one side, with a clear directional source and a shadow side | Editorial, workspace, product, almost any non-night context |
| Practical light | Visible light sources within the frame — a desk lamp, a screen, a candle — as the apparent source of illumination | Interior narrative sequences, warm human contexts, intentional intimacy |

### Forbidden Lighting Descriptions and Conditions

| Forbidden | Why |
|---|---|
| HDR lighting | Creates the specific over-processed quality of consumer photography. Simultaneous highlight and shadow detail that exceeds photographic range reads as digital manipulation. |
| Neon lighting (unless explicitly thematic) | Neon creates saturated color throws that violate all palette modes except specific uses in Bold Statement. |
| Ring light catch in eyes | The circular ring-light catchlight is the mark of social media content production. It is immediately legible as non-cinematic. |
| Flat even lighting | Lighting that eliminates shadows eliminates depth. Flat lighting is the enemy of dimensional photography. |
| Lens flare (formulaic) | Automated or AI-generated lens flare is always recognizable as artificial. Real lens flare is the product of specific optical conditions. Specify "no lens flare" unless working with a cinematographer who will control its application. |
| Backlit with blown highlights | A subject backlit against a window with white-clipped highlights is technically incorrect exposure. The romantic version of this requires careful control of highlight rolloff — if you cannot control the highlight, avoid the setup. |

---

## Physical Imperfection Directives

Physical imperfections are the signatures of real photographic capture. Introducing calibrated imperfection into AI-generated footage advances its read as photographed rather than generated.

### Lens Breathing

**What It Is:** The slight change in apparent focal length that occurs when a real camera lens racks focus — the field of view very slightly widens or narrows as the focus distance changes. This is a physical property of real optical systems.

**How to Simulate:** In prompt-based generation, specify "lens breathing" or "subtle focal shift." In compositing, apply a very slight (0.5–1.5%) scale variation tied to any focus rack event. The scale change is barely perceptible — its function is to suggest an optical system is present.

**Magnitude by Zoom Level:**
- Wide lens (16–24mm equivalent): 0.3–0.8% scale change per full focus travel.
- Normal lens (35–50mm equivalent): 0.5–1.2% scale change per full focus travel.
- Telephoto (85–135mm equivalent): 1.0–2.0% scale change per full focus travel.
- Do not simulate lens breathing in the absence of a focus event — breathing without a focus change is incorrect and readable as artificial.

---

### Vignette

**What It Is:** A reduction in exposure at the frame edges and corners, attributable to natural optical falloff in real lenses.

**When to Use:** In all non-Bold-Poster contexts, a subtle vignette contributes to the "photographed" quality of the frame by directing attention toward the center and reducing the graphic flatness of digital capture.

**Maximum Opacity:** 25% opacity for a standard editorial vignette. Above 25%, the vignette becomes visible as a post-production effect rather than an optical characteristic.

**Shape:**
- **Spherical vignette:** Used in portrait and product contexts. Centers on the subject.
- **Cinematic (horizontal) vignette:** The left and right edges are darkened more than the top and bottom edges, consistent with the characteristic falloff of anamorphic lenses. Used in cinematic brand film contexts. Slightly more sophisticated read than spherical vignette.
- Never use a perfectly circular hard-edged vignette — this reads as a graphic design element, not an optical property.

---

### Chromatic Aberration

**What It Is:** The separation of color channels at high-contrast edges, caused by different wavelengths of light refracting at slightly different angles through a real lens. Reads as a very slight color fringe — typically a red/cyan split — at the edges of high-contrast elements.

**Use:** Subtle only. Maximum 1–2px channel separation at 1080p. Applied at the frame edges and corners only — chromatic aberration in real lenses is minimal at center frame and increases toward the edges.

**When Appropriate:** Editorial photography contexts, film emulation, fashion, documentary-style footage. The chromatic aberration signal reads as: "this was captured with a real lens."

**When Forbidden:** Product beauty shots requiring color accuracy, SaaS UI demonstrations where interface colors must read correctly, Bold Poster mode (the graphic clarity of this mode is violated by any optical imperfection).

---

### Motion Blur on Fast Moves

**What It Is:** The smearing of a moving subject across the sensor during a single frame's exposure time. In real photography at 1/50th second shutter (the 180° rule at 25fps), subjects moving faster than approximately 30% of frame width per second will show visible motion blur.

**Required Above Certain Velocity Thresholds:**
- Subject displacement > 15% of frame width per frame: Motion blur required. A moving subject with no motion blur reads as composited or rotoscoped, not filmed.
- Camera pan > 10% of frame width per frame: Background motion blur required.
- Fast-cut transition that includes a whip-pan: Full-frame motion blur at the peak of the pan is required for the transition to read as camera-based rather than edit-based.

**Implementation:** Specify "motion blur" and "cinematic shutter angle" in AI generation prompts. In compositing, apply directional blur at a magnitude proportional to the velocity of the moving element. The direction of blur must match the direction of motion.

**Forbidden:** Applying motion blur to elements that are not in motion (static elements in frame should be sharp while moving elements blur — mixed sharp/blurred correctly identifies what is and is not moving), applying motion blur at maximum values regardless of velocity (scale blur to speed).

---

## Composition Audit Checklist

Run this checklist before rendering any scene.

- [ ] **1. Still Frame Test.** Pause the clip at the primary held moment and examine it as a still photograph. Does the composition work independently of the motion? Is the subject placed at a compositional intersection point? Is the negative space intentional and directional? If the still frame fails, the motion will not save it.

- [ ] **2. Motion Level Verified.** Confirm the motion level (or equivalent parameter) is within the approved range for the content type. Confirm no value above 80 has been submitted to any AI generator in this sequence. If high energy is required, confirm it is achieved through editing rhythm, not motion level increase.

- [ ] **3. Camera Movement Justified.** Identify any camera movement in the sequence. For each movement, confirm it is one of the three approved camera languages (Slow Zoom, Slow Pan, Static with Internal Motion). Confirm each movement has an identified communicative purpose. Eliminate all movements that cannot be justified.

- [ ] **4. Negative Space Minimum Met.** Estimate the percentage of the frame occupied by non-subject material. Confirm it meets the minimum negative space threshold for the active design school. If the frame feels crowded, identify the lowest-value element and remove or reduce it.

- [ ] **5. Foreground Depth Present.** Confirm at least one depth indicator is present in the frame — a foreground element, a surface plane at the bottom of frame, or atmospheric separation between planes. If the frame reads as flat (subject floating against background with no spatial context), add a foreground element or respecify the generation with depth layering instructions.

- [ ] **6. Leading Lines Checked.** Identify all strong linear elements in the frame (edges, light boundaries, architectural lines). Confirm each leading line directs attention toward the subject or toward the intended focal point. Identify and correct any leading line that directs the eye toward the frame edge or away from the subject.

- [ ] **7. Lighting Source Identifiable.** Confirm that a single dominant light source is identifiable in the frame — shadow direction is consistent, highlight shape is consistent with a real light source. If multiple light sources create competing shadows or ambiguous directionality, the lighting setup is incoherent and must be corrected in generation or composite.

- [ ] **8. Physical Imperfections Applied.** Confirm at minimum: grain is applied at the correct opacity for the content type, a vignette is present at or below 25% opacity, and any moving elements above the velocity threshold have motion blur applied. Confirm chromatic aberration is absent unless the context explicitly permits it.
