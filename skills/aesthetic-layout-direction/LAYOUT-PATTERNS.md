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

### Motion safety
- Headline `y: +20px, 350ms power3.out`: safe for all Latin weights and CJK 400–700 at 72–140px (velocity 57px/s — well within CJK 700w limit of 133px/s)
- Vertical mask reveal: clip-path animation, zero motion blur — safe at any size
- Data count-up / metric hit: numeric `textContent` or `innerHTML` change, no translate — safe
- Annotation fade `300ms sine.inOut`: opacity-only exit, always safe
- **Clean hold minimum**: title 1.5s; data section 1.0s per metric; no element mid-fade at frame boundary
- **CJK tracking**: display headline 72–140px 700–900w → `letter-spacing: −0.03em`; add video modifier `−0.01em` for animated clips → final `−0.04em`; uppercase metadata 12–18px → `+0.10em`
- **Unsafe for this school**: do not add horizontal X-translate to headline entry; left-slide is too fast if distance > 40px at 350ms

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

### Motion safety
- Product scale `1.04 → 1.00, 900ms sine.inOut`: delta 4%, 6.6px/s at 100px object → imperceptible motion blur; safe
- Title mask reveal `700ms sine.inOut`: clip-path, zero motion blur — always safe
- Subclaim fade `500ms power2.inOut`: opacity-only; safe
- Ambient drift `scale 1.0 → 1.01, 6s sine.inOut`: 1% delta over 6s — below any perceptible threshold; safe
- **Clean hold minimum**: 3.0s+; this school's long quiet holds are the safety feature — do not shorten below 2.0s
- **CJK tracking**: editorial serif or grotesque 88–110px 300–400w → `letter-spacing: −0.01em`; never tight-track this school; add video modifier `−0.01em` → final `−0.02em`; maintain generous open feel
- **Unsafe for this school**: do not add stagger burst, word-by-word fly-in, or any translate > 24px — violates the slow, unhurried motion posture

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

### Motion safety
- **Legibility window**: every motion sequence must produce a clean hold ≥ 0.5s where text is fully opaque and untranslated — this is the "focal moment" rule; enforce with GSAP `to({}, {duration: 0.5})` after every resolve
- **Type travel velocity**: words or characters traveling across frame must resolve within Latin/CJK velocity limits; for X-translate entries at display size (64px+), max 80px at 0.3s for Latin 900w, 30px at 0.3s for CJK 900w; long cross-frame paths must take ≥ 0.8s
- **Variable font morph** (weight 100→900): no translate during morph — weight change alone is safe; do not combine translate + weight-morph in the same tween
- **CJK scatter/resolve**: if CJK characters scatter individually, treat each as CJK 900w object — max scatter offset 24px per character; character grouping to resolve as a unit is always safer than per-character scatter
- **CJK tracking on resolved state**: resolved phrase 64px variable font → `letter-spacing: −0.02em`; video modifier `−0.01em` → final `−0.03em`
- **Camera push/pull**: scale transforms on the root canvas affect all text; if camera-push is simulated with `scale(1.0 → 1.05)` on a wrapper, text must be in a separate unscaled container

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

### Motion safety
- `steps(1)` snap: zero motion duration = zero motion blur; always safe regardless of type size
- Color accent `power4.in, 80ms`: background element, no text on it during motion — safe
- Long hold 2.0s: the brutal stillness IS the motion strategy; do not truncate
- **CJK tracking**: display 200–300px 900w → `letter-spacing: −0.05em`; add video modifier `−0.01em` → final `−0.06em`; density at this scale is intentional mass, do not open-track
- **CJK at bleed scale**: never use translate-entrance for CJK text at 200px+ — snap in with `steps(1)` only; motion blur on dense strokes at that velocity is catastrophic
- **Smash cut (instant frame swap)**: safe; the hard cut IS the animation; never replace with a fade unless switching to a different school entirely
- **Unsafe for this school**: `back.out`, `elastic`, `bounce`, any rotation, any opacity fade on the headline — all violate the raw zero-affect aesthetic AND create artifacts at 200px stroke densities

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

### Motion safety
- Illustration fade `800ms sine.inOut`: opacity-only; safe at any illustration size
- Scale drift `1.0 → 1.01, 5s sine.inOut`: 1% delta over 5s; perceptually invisible motion blur — safe
- Headline mask `600ms power2.inOut`: clip reveal; zero motion blur — safe
- Subclaim and texture fades: opacity-only; safe
- **Clean hold minimum**: 3.0s; organic warmth requires time to breathe — never shorten below 2.5s
- **CJK tracking**: warm editorial serif 88–100px 400–700w → `letter-spacing: 0.00em` (generous, matching school's open posture); `line-height: 1.45–1.60`; never tight-track in this school
- **Unsafe for this school**: kinetic type burst, word-by-word fly-in, `power4.out` impact entrances, any stagger delay < 100ms — these break the warmth and introduce motion artifacts that clash with soft material

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

### Motion safety
- UI frame appearance `100ms fade`: UI chrome is a background element, fast fade is safe
- Claim entrance `250ms power3.out`: Latin 56–72px 400–700w at 250ms — safe; CJK equivalent at 56–72px needs ≥ 300ms to avoid blur
- Product behavior loop: UI state changes are DOM/CSS changes with no text translate — safe
- Hard cut / mask exit `200ms`: safe
- **Clean hold minimum**: 1.5s for feature claim; UI behavior loop counts as the anchor, not as hold time for the text
- **CJK tracking**: humanist sans 56–72px 400–700w → `letter-spacing: −0.02em`; add video modifier `−0.01em` → final `−0.03em`; keyboard chip labels 11–14px uppercase → `+0.06em`; mono data `letter-spacing: 0` always
- **Mixed CJK+Latin on claim line**: Latin receives `+10%` font-size boost or drops one weight step; do not let CJK dominate the claim without a size strategy
- **Unsafe for this school**: rotation on UI panels, `bounce`/`elastic` on any UI element, `linear` ease on claim text — linear ease creates visible blur throughout the tween duration

### 9:16 adaptation
- UI panel stacks above claim text in portrait
- UI panel scales to full width with 24px padding; height 45% of portrait frame
- Claim text becomes portrait-safe: 2 lines max, 64px
- Nav chrome adapts: hamburger or compact chip row

### Forbidden layouts
Gradient background behind UI, heavy HUD on top of product, floating product image without UI context, feature cards, warm organic composition, any centered layout for text.

---

---

## Recipe-Specific Layout Notes

The six school patterns above define the grammar. These per-recipe notes define the dialect.

### linear — Panel Asymmetric, Left Text / Right UI
```
[ 80px ] [ HEADLINE 64px left        ] [ void 5%] [ UI PANEL, clipped right edge ]
         [ sub-claim 28px            ]            [ hairline borders 1px         ]
         [ mono chip row 22px        ]            [ surface #16171C              ]
         [ --- text block max 520px  ]            [ right edge may clip frame    ]
```
- The void between text block and UI panel (≈ 5% of width) is a deliberate breath
- Product UI panel clips the right frame edge — this signals confidence, not sloppiness
- Headline must not extend past x: 540px; keep it in the left half
- The accent purple #5E6AD2 appears in exactly one element within the UI panel (a pill, a highlight)
- Beat: [0.0s] dark frame + hairlines → [0.4s] headline slides x:-24px → [0.8s] UI panel mask reveals top→bottom → [1.2s] accent pill appears → hold

### aesop — Object Left, Italic Right
```
[ 15%   ] [ OBJECT 35%              ] [ 10% void ] [ ITALIC SERIF 72px        ] [ 10% ]
           [ small, unhurried         ]             [ no bold, ever            ]
           [ 1 prop only below        ]             [ small caps label 11px    ]
           [ no shadow halo           ]             [ 1px amber rule           ]
```
- The 10% void between object and text is structural — never fill it
- Object vertical center: y 240–480px; text block vertical center: same y-range
- Label in small caps sits at top-left (y: 80px, x: 80px) as a quiet anchor
- The only amber (#7A4623) in the frame is a single 1px rule below the label
- Beat: [0.0s] chamois bg → [0.8s] object fades in (opacity only) → [1.6s] italic serif fades in → [2.2s] small caps label → hold 3.0s minimum

### pentagram — Type Bleeds, Color Block Underneath
```
[ HEADLINE 160px — CLIPS LEFT EDGE BY 40–80px                        ]
[                                                                     ]
[ FLAT COBALT #1E3FFF BLOCK — 55% of frame, behind type               ]
[ no gradient, no texture, exact rectangle                           ]
[                                                                     ]
[                      tiny serif caption 14px italic, bottom-right  ]
```
- Headline baseline: y 300–400px (visual center-of-frame or above)
- Left character clips at x: -40 to -80px — this is required, not optional
- Color block: x 0–820px, y 160–580px (behind the clipping headline)
- Caption: x 800–1200px, y 640–660px — the only small element; it anchors the scale
- Beat: [0.0s] white frame → [0.1s] color block slams from right (160ms power4.out) → [0.2s] headline slides from left (baseline move only) → [0.4s] caption fades in → hold 2.0s → hard cut

### tufte-dataink — Chart Primary, Annotation Right Margin
```
[ 80px ] [ CHART TITLE 48px serif         ] [ RIGHT MARGIN 8%    ]
         [ chart occupies y: 80–580px      ] [ annotation 20px ×3 ]
         [ x: 80–1100px                   ] [ staggered entries   ]
         [ direct labels at line endpoints ] [                     ]
         [ no legend box, no chart border  ] [                     ]
         [ axis labels 14px humanist sans  ] [                     ]
```
- Chart area: x 80–1100px, y 80–600px; right margin x 1100–1200px reserved for annotations
- Chart title: y 40–75px, x 80px (left-aligned, never centered)
- Annotations float in right margin, 3–4 maximum, staggered 200ms after chart draw completes
- Direct labels sit at each line's right endpoint within the chart area (never in a legend box)
- Beat: [0.0s] warm paper bg → [0.4s] chart axes draw (strokeDashoffset) → [1.2s] lines draw linear over 1200ms → [2.4s] annotations slide in from x+8px, staggered 200ms → hold 2.5s

### bloomberg-terminal — 3×2 Pane Grid, Hairline Authority
```
┌──────────────────┬──────────────────┬──────────────────┐
│ PANEL A (amber)  │ PANEL B (white)  │ PANEL C (white)  │
│ primary metric   │ secondary data   │ secondary data   │
│ 24px mono amber  │ 16px mono white  │ 16px mono white  │
├──────────────────┼──────────────────┼──────────────────┤
│ PANEL D (green+  │ PANEL E (red-)   │ PANEL F (amber)  │
│ delta up data    │ delta down data  │ header label     │
│ 13px mono rows   │ 13px mono rows   │ 13px mono rows   │
└──────────────────┴──────────────────┴──────────────────┘
```
- Pane borders: exactly 1px #2A3050 — no rounding, no shadow, no glow
- Panel A (top-left): always the primary amber metric; the eye goes there first
- Panels D/E: green/red delta encoding only for actual directional data; never decorative
- All fonts: IBM Plex Mono 400; all sizes between 13–24px; nothing larger
- Beat: [0.0s] navy-black bg → [0.4s] 6 panel borders draw simultaneously → [0.8s] amber labels flash per-panel staggered 40ms → [1.4s] data rows populate top-to-bottom 20ms per row → hold with "live" value blinks 80ms

### muji-kenya-hara — Single Object, Radical Void
```
[ 15%  ] [        ] [ OBJECT 25–35% of frame      ] [        ] [ 15%  ]
         [        ] [ centered in frame             ] [        ]
         [        ] [ small, unhurried              ] [        ]
         [        ] [ no shadow, no halo, no prop   ] [        ]
         [ 10%  ] [ label "01 — Cotton" 18px       ] [ 10%  ]
                    [ y: 520–560px, left of center  ]
```
- Object maximum height: 35% of 720px = 252px; deliberately small on the ground
- No prop, no second object — Muji is more austere than Aesop
- Section label: weight 400, letter-spacing +0.02em, muted #7C7B76, left of center
- The frame is 55–65% empty — this emptiness is the entire message
- Beat: [0.0s] #F4F2EC bg (pure, no texture) → [0.9s] object opacity fade in (900ms, position unchanged) → [1.8s] section label fades in → hold 4.0s minimum → [5.8s] fade to bg over 700ms

### apple-hig — Centered Stage, Product as Star
```
[ 10% ] [                  CENTER STAGE                  ] [ 10% ]
         [                                                ]
         [ HEADLINE 72px SF Pro Display 600              ]
         [ y: 80–150px, centered                         ]
         [                                                ]
         [ PRODUCT OBJECT y: 180–540px, centered          ]
         [ 40–50% of frame height                        ]
         [                                                ]
         [ sub-claim 24px, #86868B, centered, y: 570px   ]
         [ CTA text-link #0071E3, centered, y: 620px     ]
```
- True bilateral symmetry — Apple earns the centered layout; don't assume others can
- Product object must be a photographed or rendered 3D object, not a flat diagram
- Headline sits in top 20% of frame; nothing else lives above it
- Blue #0071E3 appears once: the CTA text-link; nowhere else in the frame
- Beat: [0.0s] white bg → [0.3s] product scales 0.92→1.00 + opacity, 550ms expo.out → [0.8s] headline fades in → [1.0s] sub-claim fades in 200ms later → [1.2s] CTA appears → hold 2.5s

### field-io — Full-Frame Generative System
```
[ GENERATIVE FIELD: particle / mesh / light traces, full bleed        ]
[ #0B0B0F ground with #0CE0E5→#5B2EFF light emission                  ]
[                                                                      ]
[           resolved phrase: 5 words max, 64px variable font          ]
[           weight 200 (scatter) → weight 800 (resolved)              ]
[           x: center ± 160px, y: 280–440px                           ]
[                                                                      ]
[           support label: 20px weight 300, y: 480–520px, centered    ]
```
- The field has no outer margin — it fills every pixel of the frame
- Type resolves within the standard text safe area despite the full-bleed field
- The field continues to drift during the hold — it never freezes
- No additional elements: no UI panels, no cards, no secondary headline
- Beat: [0.0s] field at low density → [0.4s] density builds over 800ms → [1.2s] chars scatter in → [1.8s] chars snap to position, weight morphs 200→800 → [2.2s] support label fades in → hold 1.5s → [3.7s] hue shift transition 800ms

### bloomberg-businessweek-turley — Type Slam, Color Block
```
[ SINGLE WORD / SHORT PHRASE at 160–200px — LEFT CLIP ← ←           ]
[ characters: leftmost clips frame edge at x: -40 to -80px           ]
[                                                                     ]
[ FLAT ACCENT BLOCK (orange #FF3D00 OR yellow #FFE800 OR blue #001AFF)]
[ x: 0–900px, y: 100–620px — behind the type, exact rectangle       ]
[                                                                     ]
[                              caption 14px Plantin italic, y: 645px ]
```
- Color block is a hard-edged rectangle — no gradient, no shadow, no feathering at any corner
- The type bleeds the left frame edge; a secondary word may also bleed the bottom edge
- Maximum 3 colors in the frame: bg (#FFFFFF or #000000) + type + accent block
- Caption is the only element that respects the safe area; everything else ignores it
- Beat: [0.0s] white frame (120ms silence) → [0.1s] color block slams from right 160ms power4.out → [0.2s] headline slams from left 200ms power4.out + impact SFX → [0.4s] caption opacity fade → hold 1.5s → [2.0s] 66ms black flash hard cut

### mailchimp-freddie — Illustration Left, Headline Right, Asymmetric
```
[ 80px ] [ ILLUSTRATION 40%           ] [5%] [ HEADLINE 72px Söhne 700 ] [ 80px ]
          [ hand-drawn character       ]     [ sub-claim 24px          ]
          [ tilted +5° (not centered)  ]     [ pill CTA button         ]
          [ facing/gesturing right     ]     [                         ]
          [ warm yellow bg floods left ]     [ warm near-black text    ]
```
- Illustration tilt: exactly +5° rotation — not 0°, not 10°; this slight imperfection is the recipe
- Illustration "faces" the text block — the character's gaze creates a reading direction
- Yellow #FFE01B floods the left 50% of the frame as the bg (not just behind the illustration)
- Pill button: border 2px #241C15, fill transparent or #FFE01B; not a filled dark button
- Beat: [0.0s] yellow bg left / white bg right → [0.3s] illustration bounces in: y:-20px, scale 0.9→1.0, back.out(1.4), 500ms → [0.8s] headline fades in power2.out → [1.1s] sub-claim 200ms later → [1.4s] pill button pops in → hold 2.0s

### stripe-press — Book Object Left, Pull-Quote Right
```
[ 80px ] [ BOOK OBJECT 40%            ] [ 10% ] [ PULL QUOTE italic 40px  ] [ 80px ]
          [ photographed, real shadow  ]         [ GT Sectra italic        ]
          [ cloth texture visible      ]         [ hung x: 60px (in margin)]
          [ foil color on spine        ]         [ author credit 16px sans ]
          [ warm bone bg #F1ECDE       ]         [ hairline rule 1px below ]
```
- Book shadow falls toward bottom-right; it must be real (box-shadow with multiple layers)
- Pull-quote hangs slightly into the left margin: x 60px (inside the 80px safe area limit, barely)
- Foil-stamp accent (#1B4B5A deep teal OR #A04A2A burnt sienna — one, never both) on book spine
- The hairline rule below the author credit is the only structural line in the frame
- Beat: [0.0s] warm bone bg + cloth grain → [0.6s] book fades in + 4° rotation settle, 800ms → [1.4s] foil color fades onto book 400ms → [1.8s] italic quote fades in x+16→0, 600ms → [2.4s] author + rule fade in → hold 3.0s → cross-dissolve 1200ms

### vercel-mesh — Black Ground, Mesh Light Source, Clean Type
```
[ GRADIENT MESH — full frame, feathered to black at all edges        ]
[ #0070F3→#FF0080 at very low saturation; never a visible rectangle  ]
[                                                                     ]
[ HEADLINE 68px Geist Sans 500             ] [ VOID ]                ]
[ x: 80px, y: 260–340px (left-anchored)   ]                          ]
[ sub-claim 24px #888888 below, 24px gap  ]                          ]
[                                          ]                          ]
[ product UI / terminal readout right half ] [ right edge clip OK   ] ]
```
- The mesh must feather completely to black at all four frame edges — never a visible gradient shape
- Mesh drifts continuously: translate(-8px,-6px)→(0,0) over 20s loop; never frozen
- Type is always left-anchored; the right half holds the product/terminal element
- Only one mesh per clip — never two overlapping mesh areas
- Beat: [0.0s] black frame + mesh drifting (already in motion) → [0.4s] headline slides x:-24px→0, power3.out, 380ms → [0.6s] sub-claim fades in → [0.8s] terminal/product readout reveals right half, top-to-bottom mask → hold; mesh drifts throughout

---

## Frame Anatomy Cheatsheet

| School | Recipe Examples | Hero % | Neg. Space % | Text Block Position | Edge Treatment | GSAP ease |
|---|---|---|---|---|---|---|
| Modern Tool / SaaS | linear, vercel-mesh | 45% (type+UI) | 30–40% | Left-anchored 80px | UI clips right edge | power3.out |
| Editorial / Minimalist | aesop, muji-kenya-hara | 35% (object) | 50–65% | Right of or below object | Strict 80px all edges | sine.inOut |
| Editorial / Minimalist | apple-hig | 45% (product) | 40–50% | Above + below (centered) | Strict 80px all edges | expo.out |
| Info Architecture | pentagram | 70% (type) | < 20% | Type IS the layout | Intentional type bleed | power4.out |
| Info Architecture | bloomberg-terminal | 30% per pane | < 10% | Panes fill edge-to-edge | Edge-to-edge grid | steps(1) |
| Info Architecture | tufte-dataink | 65% (chart) | 20–25% | Right margin annotation | Chart inset, 80px | none (linear) |
| Brutalist / Raw | bloomberg-businessweek-turley | 70% (type) | < 15% | Type bleeds frame | Intentional type bleed | power4.out |
| Warm Humanist | mailchimp-freddie | 40% (illus.) | 25–30% | Right of illustration | Strict 80px all edges | back.out(1.4) |
| Warm Humanist | stripe-press | 40% (book) | 35–45% | Right of book (italic) | Strict 80px all edges | sine.inOut |
| Motion / Experimental | field-io | 100% (field) | 0% (varied) | Center-resolving type | Full bleed, no margin | expo.out |
