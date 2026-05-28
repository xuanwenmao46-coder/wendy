# Video Frame Layout Patterns

Composition rules for motion-graphic video frames, primary format **1280×720 (16:9)** with 9:16
adaptation notes. Covers six design schools derived from the web-design-engineer recipe set.

## Foundational Principle

Video frame composition is not web layout. Three things change everything:

1. **Time**: the viewer cannot control pace; every element must earn its screen time in the hold
2. **Motion**: layout is not static — elements arrive, live, and leave; every position decision is also
   a motion decision
3. **The paused poster test**: pause the video on any frame and ask — does this work as a still poster?
   If the answer is no, the layout has failed regardless of how good the motion feels

Every frame in this document should pass the paused poster test. Design the still first; animate second.

Safe margins for all 16:9 at 1280×720:
- Text safe area: 80px inset from all edges (6.25% horizontal, 11% vertical)
- Action safe area: 48px inset from all edges
- Subtitle zone: bottom 80–140px, 80px inset from sides
- Final lockup zone: center-bottom third (y: 420–640px, x: 160–1120px)

---

Every frame must pass the **Paused Poster Test**: freeze any frame mid-clip. Can a viewer identify the primary subject, understand the visual hierarchy, and feel the design school's character within 2 seconds? If not, the composition has failed.

Layout in video differs from web layout in three ways:
1. **Time**: elements enter, hold, and exit; the composition is experienced sequentially, not scanned.
2. **Viewing distance**: minimum 60cm from screen; fine detail below 16px at 720p is invisible.
3. **Motion context**: composition must work as a still AND guide the eye's path through the motion sequence.

---

## School 1 — Information Architecture: "Data Grid Authority"

### Primary pattern
```
┌─────────────────────────────────────────────────┐
│  LABEL / SOURCE         │   EDITION / DATE       │ ← 32px metadata strip
├─────────────────────────┼───────────────────────┤
│                         │                       │
│  HEADLINE               │  DATA PANEL           │ ← hero region (56% of height)
│  (72–140px, col 1–7)    │  (chart / metric)     │
│                         │  col 8–12             │
├─────────────────────────┴───────────────────────┤
│  Supporting claim · subclaim · annotation       │ ← 28px support strip
└─────────────────────────────────────────────────┘
```

**Hero element**: bold headline or primary metric — left 55–60% of width
**Secondary**: data panel (chart, table, sparkline) — right 35–40% of width
**Negative space**: column gutters and top margin (32px); margin creates structure, not decoration
**Edge anchoring**: all text left-aligned; data panel right-aligned within its column; no center alignment
**Safe area**: 48px all edges at 720p

### Motion beat structure
- `[0.00s]` — frame is visible with structure (grid, background, labels); data hidden
- `[0.30s]` — headline slides in from left (`y: +20px` → 0, `power3.out`, 350ms)
- `[0.80s]` — data panel reveals via vertical mask from bottom (400ms `power3.out`)
- `[1.40s]` — data count-up or metric hit (0.4s `power4.out`)
- `[3.00s+]` — hold; annotation or secondary datum fades in (300ms `sine.inOut`)
- `[Exit]` — hard cut or typographic wipe

### 9:16 adaptation
- Stack pattern: headline (top 40%), data panel (middle 35%), metadata strip (bottom 25%)
- Headline scales to 80–100px; data panel becomes card-width (full bleed with 48px padding)
- Never scale the 16:9 layout and crop — redesign as vertical

### Forbidden layouts
Centered text, rounded card grid, product hero image, diagonal composition, gradient background.

---

## School 2 — Editorial / Minimalist: "Hero Isolation"

### Primary pattern
```
┌─────────────────────────────────────────────────┐
│                                                 │
│         [NEGATIVE SPACE — 40%+ of frame]        │ ← top/left/right breathing room
│                                                 │
│   PRODUCT / SUBJECT (photographic treatment)    │ ← hero object, 50–60% of frame width
│   centered or left-anchored                     │
│                                                 │
│                                                 │
│ HEADLINE (editorial serif, 88–110px)            │ ← anchor bottom-left or right
│ Subclaim (quiet sans, 28px)                     │
└─────────────────────────────────────────────────┘
```

**Hero element**: product image or subject with clean light source — never a diagram or icon
**Title block**: anchors bottom-left or bottom-right; never centered under the product
**Negative space**: minimum 40%; whitespace is a deliberate structural element, not a gap to fill
**Edge anchoring**: one edge may bleed (editorial crop); product may exit frame edge
**Safe area**: 64px all edges; hero should never be cropped by platform UI

### Motion beat structure
- `[0.00s]` — empty warm ground; hold 0.3s
- `[0.30s]` — product fades in slowly (900ms `sine.inOut`); enters from slight scale (1.04 → 1.0)
- `[1.20s]` — title appears: slow mask reveal left-to-right (700ms `sine.inOut`)
- `[2.00s]` — subclaim fades in (500ms `power2.inOut`)
- `[3.00s+]` — hold; optional slow ambient drift (scale 1.0 → 1.01 over 6s `sine.inOut`)
- `[Exit]` — opacity fade (600ms)

### 9:16 adaptation
- Hero object expands to 70% of frame height (portrait-centered)
- Title moves to top (above hero) or overlays bottom third with backing plate
- Generous negative space preserved: 35%+ above or below hero
- Font scales: display 100–120px in portrait

### Forbidden layouts
Feature card row, data panel, HUD overlay on product, centered title under product, anything that reads as "presentation slide."

---

## School 3 — Motion / Experimental: "Kinetic Event"

### Primary pattern
```
┌─────────────────────────────────────────────────┐
│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
│░ GENERATIVE / MOTION EVENT ░░░░░░░░░░░░░░░░░░│ ← full-frame choreography
│░ type morphs, elements travel, system builds ░│
│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
│░ [WORD] ← enters from left              EXIT →│ ← type paths cross frame
│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
│              [FOCAL MOMENT: legible for 0.5s] │ ← the one readable landing
│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
└─────────────────────────────────────────────────┘
```

**Hero element**: the motion EVENT — no single static object; the frame is always in transition
**Focal moment**: every 2–4s, a moment of legibility — one word, one image, one readable claim — before the motion continues
**Negative space**: dynamic — appears as elements exit; not designed in advance
**Edge anchoring**: elements intentionally exit and enter through edges — this is a compositional rule, not an error

### Motion beat structure
- `[0.00s]` — generator launches: particles, generative type, or camera push
- `[0.60s]` — first legible moment: one word or image lands cleanly (hold 0.5s min)
- `[1.20s]` — motion continues: transformation, match cut, or camera tunnel
- `[2.00s]` — second legible moment: key claim or product name
- `[3.00s]` — crescendo: multiple elements choreographed to beat
- `[4.00s]` — final lockup: one frame that summarizes (1.0–1.5s hold)
- `[Exit]` — designed transition (morph, wipe, or blackout)

### 9:16 adaptation
- Motion paths redesign for vertical: left/right travel → up/down travel
- Legible moments recompose for portrait (centered, not left/right split)
- Camera moves: pull-back or push-in replaces horizontal pan

### Forbidden layouts
Static card, text entering from bottom and staying, product image with annotated labels, any frame that works as a standalone poster without the surrounding motion.

---

## School 4 — Brutalist / Raw: "Type Mass"

### Primary pattern — Option A: Full Bleed Type
```
┌─────────────────────────────────────────────────┐
│                                                 │
│  WORD    WORD    WORD                           │ ← 200–300px, bleed past edge
│  WORD    WORD    WORD                           │   no safe area respected
│  WORD    WORD    WORD                           │
│                                                 │
│                    [single color accent block]  │
└─────────────────────────────────────────────────┘
```

### Primary pattern — Option B: Absolute Desert
```
┌─────────────────────────────────────────────────┐
│                                                 │
│                                                 │
│                                                 │
│              WORD                               │ ← one word, 180px, exact center
│                                                 │   or extreme offset
│                                                 │
│                                                 │
└─────────────────────────────────────────────────┘
```

**Hero element**: the typographic mass — either overwhelming or uncomfortably alone
**Color accent**: one hard color block (never gradient) that interrupts the composition
**Negative space**: either 0% (full bleed type) or 90%+ (desert) — never comfortable middle
**Edge anchoring**: type may bleed all four edges; baseline may not align with safe area

### Motion beat structure
- `[0.00s]` — immediate hard cut to full-bleed type OR absolute silence
- `[0.00s–0.05s]` — type snaps in with no ease (`steps(1)`)
- `[0.50s]` — color accent slaps in from edge (`power4.in`, 80ms)
- `[2.00s]` — uncomfortably long hold — no motion, no ambient drift
- `[3.00s]` — smash cut to next state OR text swaps in place (instant)
- `[Exit]` — blackout or cut; never a fade

### 9:16 adaptation
- Scale type to fill portrait frame — bleed on all sides in portrait feels even more aggressive
- Color slap adapts: becomes a horizontal band instead of vertical

### Forbidden layouts
Rounded corner card, soft shadow, product hero image, feature list, warm background, gentle entrance animation.

---

## School 5 — Warm Humanist: "Organic Warmth"

### Primary pattern
```
┌─────────────────────────────────────────────────┐
│                                                 │
│  [ILLUSTRATION / PHOTO — warm, human]           │ ← hero: 55% of frame, slight off-center
│  soft light source, natural color               │
│                                                 │
│  Headline (warm serif, 88–100px)                │ ← left or right of hero
│  Subclaim (friendly sans, 30px)                 │   generous line-height
│                                                 │
│  [optional: hand-drawn mark / texture]          │ ← bottom accent; never decorative HUD
└─────────────────────────────────────────────────┘
```

**Hero element**: illustration, photograph, or person — warm and human; never a diagram or data panel
**Title block**: adjacent to hero, not under it; generous whitespace between illustration and text
**Negative space**: 35–45%; feels organic rather than designed
**Edge anchoring**: loose — slight imperfection in placement is acceptable and human

### Motion beat structure
- `[0.00s]` — warm ground appears; illustration fades in gently (800ms `sine.inOut`)
- `[0.80s]` — headline appears via soft mask (600ms `power2.inOut`)
- `[1.50s]` — subclaim fades in (400ms `sine.inOut`)
- `[2.00s+]` — optional hand-drawn mark or texture appears softly
- `[3.00s+]` — gentle ambient motion: illustration breathes (scale 1.0 → 1.01 over 5s)
- `[Exit]` — soft dissolve (500ms)

### 9:16 adaptation
- Hero illustration fills portrait top 55%; title occupies bottom 40%
- Warm backing plate for text readability in portrait
- Hand-drawn marks scale to fit portrait frame

### Forbidden layouts
Cold gray background, data chart hero, centered symmetrical layout, HUD, feature card grid, motion that prioritizes kinetic energy over warmth.

---

## School 6 — Modern Tool / Builder SaaS: "UI Machinery"

### Primary pattern
```
┌─────────────────────────────────────────────────┐
│ ● [product name]     [nav chip]    [action chip]│ ← 32px UI chrome strip
├─────────────────────────────────────────────────┤
│                                                 │
│  ┌──────────────────────────────────────────┐  │
│  │  PRODUCT UI / BEHAVIOR IN MOTION         │  │ ← hero: 65% of frame height
│  │  (generating, selecting, rendering...)   │  │   hairline 1px border
│  └──────────────────────────────────────────┘  │
│                                                 │
│ CLAIM (humanist sans, 56–72px)                  │ ← below or beside UI, left-anchor
│ Detail (compact sans, 24px)                     │
└─────────────────────────────────────────────────┘
```

**Hero element**: the product UI in active state — always performing an action, never static
**UI chrome**: minimal but present — a thin strip that contextualizes the product
**Title block**: left-anchored below the UI; never overlapping the product
**Negative space**: 25–35%; tight by editorial standards, but every pixel earns its place
**Edge anchoring**: UI panel center or slight right-offset; title left-aligned flush

### Motion beat structure
- `[0.00s]` — UI frame appears (100ms fade); hairline borders visible
- `[0.20s]` — product behavior starts: UI state changes (cursor, selection, generation)
- `[1.00s]` — claim text enters (250ms `power3.out`)
- `[1.50s–4s]` — product behavior loop continues as anchor; claim holds
- `[4.00s]` — product state reaches completion (render progress hits 100%, final state)
- `[Exit]` — hard cut or precise mask (200ms)

### 9:16 adaptation
- UI panel stacks above claim text in portrait
- UI panel scales to full width with 24px padding; height 45% of portrait frame
- Claim text becomes portrait-safe: 2 lines max, 64px
- Nav chrome adapts: hamburger or compact chip row

### Forbidden layouts
Gradient background behind UI, heavy HUD on top of product, floating product image without UI context, feature cards, warm organic composition, any centered layout for text.

---

## Frame Anatomy Cheatsheet

| School | Hero % of frame | Negative space % | Text block position | Edge treatment | Motion energy |
|---|---|---|---|---|---|
| Information Architecture | 40–55% (text+data) | 25–40% | Left column or bottom strip | Grid-locked, no bleed | 3–4 / 10 |
| Editorial / Minimalist | 50–65% (object) | 40–55% | Bottom-left or right anchor | Deliberate edge crop OK | 2 / 10 |
| Motion / Experimental | 100% (motion event) | Dynamic | In motion; 0.5s legible landing | Intentional bleed/exit | 8–10 / 10 |
| Brutalist / Raw | 70–100% (type mass) | 0% or 90%+ | Fills frame or isolated | Bleed on purpose | 7–9 or 1 / 10 |
| Warm Humanist | 50–60% (illustration) | 35–45% | Adjacent to hero, generous space | Loose, organic | 4–6 / 10 |
| Modern Tool / Builder SaaS | 55–65% (product UI) | 25–35% | Below or beside UI, left-anchor | Grid-locked | 5–6 / 10 |
