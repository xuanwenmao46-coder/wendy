# Video Recipe Translations

Translates web-design-engineer school DNA into video-native design tokens for motion-graphic production
(HyperFrames / GSAP + Remotion). For each recipe: palette, typography, frame composition, motion posture,
sonic character, and the anti-slop check that separates this school from generic AI output.

Resolution baseline: **1280×720 @ 30fps**. All px values at this resolution.
Source recipes live in `web-design-engineer/references/style-recipes/`.

---

### Linear — Quiet Authority
School: Modern Tool / Builder SaaS
Source: web-design-engineer/references/style-recipes/linear.md

Palette (video-native):
  bg: #08090A (warm dark ground, not pure black — the warmth reads on screen; pure black looks flat)
  fg: #F7F8F8 (primary label text; cool white, not paper white)
  accent: #5E6AD2 (Linear purple — < 5% of pixel area; one pill label, one data point, never a background)
  surface-1: #16171C (card panels, info modules; must float above bg with hairline, not glow)
  material: flat matte with hairline 1px borders at rgba(255,255,255,0.06); no glass, no blur, no texture

Typography (video roles):
  display: Inter Tight 600, 64px — tight tracking -0.02em; for hero claims only (3–5 words max)
  support: Inter 400, 28px — secondary statements, lh 1.5; never italic
  data: Geist Mono 400, 22px — counters, shortcut chips, inline stats; color #9CA3AF
  weight contrast: 400 vs 600 (no 900 — weight restraint IS the recipe)
  forbidden: Poppins, Raleway, Roboto; anything with default web-safe feel

  optical corrections (typography-optics):
    display: Inter Tight 600, 64px → tracking -0.02em (Table 2: 56–72px 600w)
    support: Inter 400, 28px → tracking 0.00em (Table 2: 20–28px 400w)
    data: Geist Mono → tracking 0em strictly; tabular-nums enforced
    CJK display (if Chinese): 64px 700w → -0.02em (-0.03em with video modifier)
    mixed CJK+Latin line: Latin font-size ×1.09 OR Latin weight drop to 400 when CJK is 600
    uppercase chip labels: +0.08em (e.g. "RENDER · 28–30s")

Frame Composition:
  hero: type block anchored left at 8% inset, vertical center ±15%; 55% of frame width maximum
  secondary: product UI panel right-half, clipped at right edge; frame-within-frame treatment
  negative space: 30–40% of frame — the empty top-right quadrant is intentional breathing room
  grid: 12-col at 1280px, 24px gutters; every element snaps to column boundary

Motion Posture:
  entrance: type slides from x:-24px, opacity 0→1, cubic-bezier(0.22,1,0.36,1), 380ms
  hold: 1.8s minimum on any readable claim; do not rush the still frame
  transition: scene change via 240ms opacity cross-dissolve — no wipes, no slides
  forbidden motion: bounce, spring physics, elastic ease, scaling above 1.05×
  motion safety: CJK display at 64px max Y 36px at 0.38s (within safe zone); Latin 600w at 64px max Y 50px at 0.38s; minimum clean hold 1.8s per claim; no text element may animate with linear ease
  GSAP ease: "power3.out" for layout moves; "none" for instant state flips on UI panels

Sonic Character:
  material metaphor: brushed aluminum — precise, clean, no resonance tail
  bed: no music bed; silence between hits is part of the luxury
  micro-feedback: dry click, ~8ms, -18dB — when UI panels snap into place
  accent hit: short muted metallic tap, ~60ms, -12dB — on accent purple reveal
  final lock: single clean key-press sound, 80ms, -10dB — the brand celebrates keyboard-first
  forbidden sounds: whoosh sweeps, cinematic boom, any reverb tail > 200ms, notification chimes

Anti-slop check:
  Generic AI would: add purple glow, animate everything simultaneously at 500ms ease-in-out, center all text
  This recipe demands: asymmetric layout, hairline borders doing all the elevation work, motion that is snappy
    but never bouncy, silence treated as designed space, and the accent purple appearing exactly once per clip

---

### Aesop — Apothecary Ceremony
School: Editorial / Minimalist
Source: web-design-engineer/references/style-recipes/aesop.md

Palette (video-native):
  bg: #E8E4D9 (warm chamois — a daytime recipe; this is a light-ground school, never invert to dark)
  fg: #1B1B1B (true near-black ink; body copy and primary labels)
  accent: #7A4623 (amber bottle — appears as a single rule line, seal mark, or thin underline; < 3% of frame)
  surface: #F0EDE4 (cream card when a backing panel is needed; always slightly warmer than bg)
  material: uncoated paper — matte, no gloss, no reflection; subtle paper grain overlay at 4% opacity

Typography (video roles):
  display: GT Sectra or Lyon Text, weight 400 italic, 72px — literary, unhurried; set in italic always
  support: Söhne or Helvetica Now, weight 400, 22px — UI labels, small caps 11px / ls 0.12em
  data: same Söhne at 18px, muted #7A8470 — never a monospace font in this recipe
  weight contrast: 400 italic (display) vs 400 roman (support) — contrast through posture, not weight
  forbidden: any bold (> 500 weight), Inter, any sans at display size, any font with "geometric" personality

  optical corrections (typography-optics):
    display: GT Sectra italic 400, 72px → tracking +0.01em (intentional open; Aesop signature overrides optical table default)
    support: Söhne 400, 22px → tracking 0.00em
    small-caps labels: Söhne 400, 11px → tracking +0.12em
    CJK display (if Chinese): 72px 400w → -0.01em (CJK requires optical correction even when Latin opens; never open-track CJK)
    mixed-script: avoid mixing CJK+Latin in this school; if unavoidable, Latin as small-caps label only
    line-height display: 1.20 (single line), 1.25 (two lines)
    line-height body: 1.55

Frame Composition:
  hero: product object occupies 35–45% of frame, anchored left or right with generous margin on the other side
  secondary: a single sage prop (linen fold, dried sprig) placed in the opposing quadrant; never centered
  negative space: 45–55% — Aesop's emptiness is the message; fill anxiety is the enemy
  grid: loose 6-col; content rarely exceeds 50% of frame width; asymmetry is structural, not decorative

Motion Posture:
  entrance: 800ms opacity fade — literally just a dissolve; the object appears as if light shifted
  hold: 3.0s minimum; Aesop is never in a hurry
  transition: cross-dissolve only, 600ms; or a slow vertical curtain at 900ms linear
  forbidden motion: slide, scale, bounce, rotation, any y-axis translate > 8px
  motion safety: opacity-only strictly; no translate on CJK text; Latin product text max opacity transition only at 600–900ms; minimum hold 3.0s; freeze-frame test required at 1.5s into hold
  GSAP ease: "sine.inOut" for ambient; "none" (opacity only) for entrances

Sonic Character:
  material metaphor: ceramic — soft resonance, no sharp transients
  bed: yes — a very quiet room tone or near-silent ambient, -28dB, 20–40Hz warmth only
  micro-feedback: no clicks; silence acknowledges the transition
  accent hit: a single low ceramic bowl strike, 200ms decay, -16dB — used at most once per clip
  final lock: imperceptible; fade to ambient, then silence
  forbidden sounds: whoosh, digital click, any SFX that reads as "tech", percussion of any kind

Anti-slop check:
  Generic AI would: use the warm palette but center everything, add a soft glow on the product, and
    use a friendly sans at weight 500 with opacity-in animation at 400ms ease-out
  This recipe demands: italic serif at display, radical asymmetry, no bold weight anywhere, motion that
    is so slow it feels like the viewer is looking at a photograph coming slowly into focus

---

### Pentagram — Type as Image
School: Information Architecture / Graphic Identity
Source: web-design-engineer/references/style-recipes/pentagram.md

Palette (video-native):
  bg: #FFFFFF (paper white — this recipe lives in high contrast; the ground is a surface for type)
  fg: #000000 (true black — Pentagram does not soften its ink)
  accent: #1E3FFF (cobalt — used as a flat color block behind or under type; never as text color)
  alt-bg: #F4F1E7 (cream ground for warmth variant; ink stays black)
  material: flat offset print — no texture, no grain, no gradients of any kind; two colors maximum

Typography (video roles):
  display: Helvetica Now Display 900 or Druk Wide Heavy, 120–160px — the type IS the frame
  support: same family at 400, 20px — small, precise, baseline-locked; captions in column gutter
  data: tabular figures from the display family; right-aligned; no separate data font
  weight contrast: 400 vs 900 — the gap should feel violent
  forbidden: multiple type families, any rounded grotesque, Futura, Circular, any "friendly" sans

  optical corrections (typography-optics):
    display: Helvetica Now Display / Druk Wide Heavy 900, 120–160px → tracking -0.03em to -0.05em (Table 2: 96px+ 900w)
    support: same family 400, 20px → tracking 0.00em
    data: tabular figures from display family → tracking 0em; tabular-nums enforced; right-aligned
    CJK display (if Chinese): 120px 700w+ → -0.04em (-0.05em with video modifier); never allow positive tracking
    uppercase or all-caps display: tracking -0.03em (optical tightening overrides typographic open-tracking instinct at this scale)
    line-height display: 0.92–0.96 (intentional collision; the letterpress grid absorbs it)

Frame Composition:
  hero: single word or short phrase at 120–160px, allowed to bleed past left or right frame edge
  secondary: one flat color block (accent or bg) occupies 30–50% of frame; text lays over it
  negative space: 20–30% — less than other minimalist recipes; space here is seized by type mass
  grid: 12-col, strict; but the headline intentionally violates the left or right margin by 40–80px

Motion Posture:
  entrance: type slides in on its baseline — x-axis only, from -frame-width to position, 420ms
  hold: 2.0s minimum; the typographic poster needs time to be read and felt
  transition: hard cut or 120ms flash-to-white; never a smooth dissolve
  forbidden motion: rotation, scale, bounce, any y-translate; type is always horizontal
  motion safety: x-axis slide only; CJK text at 120px+ max X travel 80px at 0.42s; Latin 900w at 120px+ max X travel 120px at 0.42s; hold minimum 2.0s; no text element may animate on y-axis under any circumstance
  GSAP ease: "power4.out" for headline slam; "steps(1)" for flash cuts between scenes

Sonic Character:
  material metaphor: letterpress impact — physical, immediate, paper-on-press
  bed: no bed; silence between the hits is structural
  micro-feedback: no — Pentagram does not have micro-interactions
  accent hit: single sharp impact, 40ms attack, -8dB — lands exactly when headline reaches position
  final lock: same impact at 50% volume — or total silence
  forbidden sounds: whoosh, anything that implies movement before landing, reverb tails > 100ms

Anti-slop check:
  Generic AI would: fade the headline up gracefully, use a slightly rounded sans, add a subtle drop shadow,
    and balance the composition symmetrically around the center axis
  This recipe demands: type that slams, a margin break that feels intentional, only two colors in the frame,
    and motion that is about baseline slides not opacity — the type arrives, it does not float in

---

### Tufte-Dataink — Evidence on Paper
School: Information Architecture / Data Visualization
Source: web-design-engineer/references/style-recipes/tufte-dataink.md

Palette (video-native):
  bg: #FBFAF6 (warm paper — a light-ground recipe; the warmth prevents eye strain on data-dense frames)
  fg: #1B1B1A (warm ink — slightly brown-black; never cool gray)
  accent-1: #A6300E (warm red data series — for primary trend line or key data point)
  accent-2: #3E4A5C (cool slate data series — for comparison series; these two and no others)
  material: uncoated archival paper — matte, textured at 3% grain; reference lines in #D8D2C2

Typography (video roles):
  display: ET Book or Equity, weight 400, 48px — the chart title is small by design; data is the hero
  support: ET Book italic, 20px — inline annotations, side-note callouts; placed at right margin 8%
  data: Söhne or a humanist sans, 14px, color #5C5550 — axis labels, direct data labels at endpoints
  weight contrast: 400 (display) vs 400 italic (annotation) — this recipe never goes above 500
  forbidden: monospace fonts, bold above 500, legend boxes, any chart border or frame

  optical corrections (typography-optics):
    display: ET Book / Equity 400, 48px → tracking -0.01em (Table 2: 40–56px 400w; paper-set serif reads slightly tight on screen)
    support: ET Book italic 400, 20px → tracking 0.00em
    data labels: humanist sans (Söhne) 400, 14px → tracking +0.02em (small-size legibility boost at this scale)
    CJK annotation (if Chinese): 20px 400w → -0.01em; never mix CJK with ET Book at display size
    axis labels: tracking 0.00em; tabular-nums enforced; never letter-space data figures
    line-height annotations: 1.60 (to separate marginalia from chart area visually)

Frame Composition:
  hero: the data visualization occupies 65–75% of frame; everything else supports it
  secondary: annotation callouts float in right margin at 8% inset; 3–4 maximum
  negative space: 20% — but filled with marginalia, not empty; emptiness here means failed data density
  grid: organic — anchored to the data coordinate system, not to a layout grid; chart bleeds are acceptable

Motion Posture:
  entrance: chart lines draw via strokeDashoffset 0→1, 1200ms, linear ease — data accumulates honestly
  hold: 2.5s on any completed chart; annotations enter after chart is fully drawn, staggered 200ms apart
  transition: wipe left-to-right, 600ms — like turning a page in a book; no flash, no dissolve
  forbidden motion: chart bars that pop or bounce, numbers that count up dramatically, any motion for drama
  motion safety: line draw at strictly linear ease — no acceleration; annotations max Y 12px at 0.4s power2.out; CJK annotation text no translate at all (opacity-only); hold 2.5s on completed chart; no element may use ease-in-out
  GSAP ease: "none" (linear) for line draw; "power2.out" for annotation slides; never "elastic" or "back"

Sonic Character:
  material metaphor: pencil on paper — soft friction, no digital sheen
  bed: yes — a nearly inaudible paper ambient, -32dB, just enough to fill the silence
  micro-feedback: quiet pencil scratch, 30ms, -22dB — when an annotation appears
  accent hit: no hit; data arrival is calm, not dramatic
  final lock: a soft page turn sound, 180ms, -18dB — or silence
  forbidden sounds: any "impact" SFX, countdown beeps, swoosh, anything that editorializes the data

Anti-slop check:
  Generic AI would: animate bars popping up with bounce, add glowing data points, use a dark dashboard
    background, include a legend box, and make the chart title 3× too large
  This recipe demands: a warm paper ground, line charts (not bars) with direct labels, annotations in
    the right margin (not tooltips), and motion that feels like the data is being drawn by a careful hand

---

### Bloomberg Terminal — Mission-Critical Density
School: Information Architecture / Data Operations
Source: web-design-engineer/references/style-recipes/bloomberg-terminal.md

Palette (video-native):
  bg: #0A0E1A (deep navy-black — not pure black; the navy keeps it from feeling like a void)
  fg: #E8ECF4 (chrome white — secondary and body data; no pure white)
  accent: #FFA02F (amber — the signature; appears on the most important data label in each panel)
  positive: #00B96B (price-up / good delta — used only when encoding directional data)
  negative: #F23645 (price-down / alert — used only when encoding directional data)
  material: no texture; elevation through hairline borders at #2A3050; no glass, no blur

Typography (video roles):
  display: IBM Plex Mono 400, 24px — the "headline" in terminal world is still monospaced
  support: IBM Plex Mono 400, 16px — body data, panel labels; tabular figures, right-aligned columns
  data: IBM Plex Mono 400, 13px — dense rows; this is the minimum readable at 1280×720
  weight contrast: 400 throughout — emphasis through color (amber) not weight
  forbidden: any proportional sans or serif, rounded fonts, anything > 400 weight, anything > 24px

  optical corrections (typography-optics):
    display: IBM Plex Mono 400, 24px → tracking 0em strictly; tabular-nums enforced; monospace optical neutrality
    support: IBM Plex Mono 400, 16px → tracking 0em; right-aligned columns require tabular-nums always
    data: IBM Plex Mono 400, 13px → tracking 0em; no adjustment at this size — mono grid must hold
    CJK labels (if Chinese): avoid; if unavoidable at 16px → tracking -0.01em; never mix CJK at 24px display
    amber accent text: tracking 0em — do not open-track the primary metric; weight emphasis is via color only
    column alignment: all numeric columns right-aligned; all label columns left-aligned; no exceptions

Frame Composition:
  hero: the data pane — 4–6 visible panels divided by 1px hairline borders; no hero "object"
  secondary: amber-labeled primary metric in the top-left panel; all other panels are support
  negative space: < 10% — this is a density recipe; empty space signals incomplete data
  grid: strict 2×3 or 3×2 multi-pane; pane borders at exactly 1px #2A3050; no rounded corners

Motion Posture:
  entrance: panels flash in sequentially, 80ms per panel, 40ms stagger — like a terminal boot sequence
  hold: data panels stay visible and "live"; counter values update with 80ms flash on changed digits
  transition: instant cut between scenes — no easing, no dissolve; terminals do not animate scene changes
  forbidden motion: eased transitions, any scale, any rotation, opacity fades > 80ms, anything decorative
  motion safety: all panel changes steps(1) only — no interpolation between states; digit flash strictly 80ms; CJK text if present must be static (no flash, no update animation); hold means data is live but text does not move; no element may use any easing curve
  GSAP ease: "steps(1)" for all state changes; "none" for ticker scroll (uniform CSS linear animation)

Sonic Character:
  material metaphor: mechanical keyboard — each keystroke is physical and purposeful
  bed: yes — a very quiet fan hum or electrical buzz, -34dB; the terminal is always running
  micro-feedback: dry mechanical key click, 12ms, -14dB — on every panel data update
  accent hit: slightly louder click cluster (3 rapid), -10dB — when amber metric changes value
  final lock: a single bell tone, 120ms, -12dB — the classic terminal alert; used only once per clip
  forbidden sounds: music beds, whoosh, anything warm or organic, reverb of any kind

Anti-slop check:
  Generic AI would: use dark background but soften it to charcoal, round the panel corners, use a sans
    headline at 36px, animate numbers with a count-up bounce, and add a glowing accent color
  This recipe demands: pure monospaced type at 13–24px, hairline panel borders at exactly 1px, amber
    used for exactly one data label per panel, and transitions that are instant — terminals do not animate

---

### Muji-Kenya Hara — Ma (Emptiness as Fullness)
School: Editorial / Minimalist
Source: web-design-engineer/references/style-recipes/muji-kenya-hara.md

Palette (video-native):
  bg: #F4F2EC (warm paper off-white — never #FFFFFF; the warmth is the discipline)
  fg: #2A2A28 (warm ink, never pure black; slightly brown to stay on the warm paper ground)
  accent: none — if forced, a single MUJI red #C8161D as a 2px rule or corner mark; < 1% of frame
  secondary: #7C7B76 (muted warm gray — captions, section labels; the only second tone)
  material: uncoated Japanese paper — the lightest possible grain at 2% opacity; no texture drama

Typography (video roles):
  display: Söhne 400 or Inter Tight 400, 48px — weight 400 only; the restraint is the statement
  support: same family, 18px, #7C7B76, letter-spacing +0.02em — section labels: "01 — Cotton"
  data: no separate data voice; use support style for any factual label
  weight contrast: none — this recipe is all weight 400; variation through size (48px vs 18px) only
  forbidden: any bold, any weight above 500, any warm-toned serif, any decorative font

  optical corrections (typography-optics):
    display: Söhne / Inter Tight 400, 48px → tracking -0.01em (Table 2: 40–56px 400w; restraint extends to optical tightening)
    support: same family 400, 18px → tracking +0.02em (section labels need slight open for legibility at 18px)
    section label format: Söhne 400, 18px, +0.02em — "01 — Cotton" pattern; the em dash is structural
    CJK display (if Chinese): 48px 400w → -0.01em; section label CJK at 18px → 0.00em (no open-tracking CJK)
    mixed-script: if CJK product name at display, Latin label below in support style only; never same line
    line-height display: 1.50 (weight 400 at 48px benefits from generous leading to amplify the negative space)
    line-height support: 1.65

Frame Composition:
  hero: a single product object, photographed or rendered, 25–35% of frame — small by design
  secondary: a plain one-line label in support style, placed below or beside at comfortable distance
  negative space: 55–65% — the frame is mostly empty; this is structural, not a mistake
  grid: centered column, max 60% of frame width; object never touches frame edges

Motion Posture:
  entrance: 900ms opacity fade, pure — no position change; the object materializes from the ground
  hold: 4.0s minimum; Ma requires duration; the viewer must sit with the emptiness
  transition: 700ms cross-dissolve; between clips there is a brief (400ms) hold of pure #F4F2EC bg
  forbidden motion: slide, scale, rotation, any y-translate whatsoever; motion here is only light change
  motion safety: opacity-only at 900ms — no position delta under any circumstance; CJK text and Latin text treated identically (both opacity-only); minimum hold 4.0s; the 400ms pure-bg hold between clips is mandatory, not optional
  GSAP ease: "sine.inOut" opacity only; position should not change at all during the clip

Sonic Character:
  material metaphor: Japanese rice paper — near-silent; the grain of the material without any surface
  bed: yes — a 20Hz–40Hz room tone at -36dB; presence without sound
  micro-feedback: none — Muji does not click
  accent hit: none — there is no hit in this recipe; arrival is the message
  final lock: a single breath of silence — hold the ambient for 1 full second after the last element
  forbidden sounds: any percussive SFX, music with melody, any SFX that reads as "designed"

Anti-slop check:
  Generic AI would: use the off-white palette but center-justify the text, pad it generously (not radically),
    add a subtle drop shadow to the product, use weight 500 for the headline, and fade up over 500ms
  This recipe demands: radical negative space (> 55%), weight 400 only, no shadow on the product, an
    opacity-only entrance at 900ms, and silence so quiet the viewer notices the room

---

### Apple HIG — One Thought, One Stage
School: Editorial / Minimalist
Source: web-design-engineer/references/style-recipes/apple-hig.md

Palette (video-native):
  bg: #FFFFFF (paper-pure white for product-reveal moments) or #000000 (deep black for film hero moments)
  fg: #1D1D1F (Apple's not-quite-black — warmer and softer than true black)
  accent: #0071E3 (system blue — appears once per clip as a text-link or a single CTA label; < 4%)
  muted: #86868B (captions, eyebrow labels, secondary copy; this is Apple's secondary voice)
  material: clinical glass — precision, no grain, no warmth; product surface handles all the texture

Typography (video roles):
  display: SF Pro Display 600, 72px — lh 1.08; for short hero claims (4–7 words); tracked at -0.015em
  support: SF Pro Text 400, 24px, #86868B — the sub-claim; appears below display after a 200ms delay
  data: SF Pro Display 600, 80px — for hero stats (e.g., "12.9""); the numeral is display-weight
  weight contrast: 400 (#86868B) vs 600 (#1D1D1F) — contrast through weight AND color simultaneously
  forbidden: Inter (at default weight), Helvetica (too generic), any warm serif, any geometric sans

  optical corrections (typography-optics):
    display: SF Pro Display 600, 72px → tracking -0.02em (Table 2: 56–72px 600w)
    support: SF Pro Text 400, 24px → tracking 0.00em (Table 2: 20–28px 400w)
    data: SF Pro Display 600, 80px → tracking -0.02em (Table 2: 72–96px 600w; hero numerals tighten like display)
    CJK display (if Chinese): 72px 600w → -0.02em (-0.03em with video modifier)
    mixed CJK+Latin: Latin font-size ×1.09 OR Latin weight drop to 400 when CJK is 600
    uppercase eyebrow labels: tracking +0.08em (e.g. "IPHONE 16 PRO")
    line-height display: 1.08 (as specified; do not loosen — the tight lh is structural)

Frame Composition:
  hero: product object centered, 40–50% of frame height; the stage belongs to the product
  secondary: headline above product (top 25% of frame) or below (bottom 25%); never overlapping product
  negative space: 40–50% — the white space is what makes the product feel expensive
  grid: centered single-column; bilateral symmetry is accepted here; Apple centers unapologetically

Motion Posture:
  entrance: product scales up 0.92→1.00, opacity 0→1, 550ms cubic-bezier expo-out — the reveal is slow
  hold: 2.5s minimum; the product deserves contemplation
  transition: 350ms cross-dissolve between scenes; Ken Burns slow zoom (0.98→1.03 over 8s) on hero image
  forbidden motion: bounce, spring, rotation, any motion that draws attention away from the product
  motion safety: product scale entrance 0.92→1.00 max delta 8%; CJK display at 72px no position translate — opacity only; Latin 600w at 72px max Y 40px at 0.55s expo.out; minimum hold 2.5s; Ken Burns zoom delta ≤ 5% over 8s — imperceptible on any single frame
  GSAP ease: "expo.out" (cubic-bezier(0.16,1,0.3,1)) for all entrances; "sine.inOut" for Ken Burns

Sonic Character:
  material metaphor: tempered glass — clean resonance, precision ring, no warmth
  bed: no music bed; ambient silence with slight room presence at -38dB
  micro-feedback: a single soft high-frequency chime, 80ms, -14dB — on product reveal only
  accent hit: none separate; the chime IS the accent
  final lock: 300ms fade of the ambient — the clip ends in silence
  forbidden sounds: whoosh, dramatic impact, warm tones (cello, piano), any sound implying effort

Anti-slop check:
  Generic AI would: center the product but surround it with feature callout bullets, add a glow below the
    product, use Inter 500 for the headline, and animate everything at once at 400ms ease-in-out
  This recipe demands: the product alone on the stage, one headline before or after (not during), weight 600
    not 500, a 550ms entrance that feels like a curtain rising, and a single soft chime at reveal

---

### Field.io — The Frame Generates Itself
School: Motion / Experimental
Source: web-design-engineer/references/style-recipes/field-io.md

Palette (video-native):
  bg: #0B0B0F (near-black — the generative light sources will handle all color)
  fg: #FFFFFF (high-contrast white type; short labels only — the motion is the message)
  accent: #0CE0E5→#5B2EFF (deep cyan to electric violet — used as light traces in the generative field)
  secondary: #A0A4B0 (cool gray — support labels, if any text is needed beyond the display phrase)
  material: light emission — surfaces are lit from within; no surface texture; glow IS the material

Typography (video roles):
  display: Söhne Variable or Inter Display Variable, weight morphs 200→800 during entrance, final 64px
  support: same family, fixed weight 300, 20px — one short label max; the motion does the talking
  data: none — this recipe has no data role; if data is needed, use a different recipe
  weight contrast: the contrast is kinetic — watch the weight change, not a static heavy/light pairing
  forbidden: any static font use at fixed weight, serif fonts, body copy paragraphs, monospace

  optical corrections (typography-optics):
    display: variable weight 200→800, final 64px → tracking -0.02em at resolved state (Table 2: 56–72px; apply at final weight, not during morph)
    support: same family 300, 20px → tracking 0.00em
    weight-morph phase: tracking interpolates from 0.00em (at 200w) to -0.02em (at 800w) — do not snap tracking
    CJK display (if Chinese): 64px final → -0.02em (-0.03em with video modifier); tracking change also interpolates during weight morph
    mono equivalent: none — this recipe has no data role; if added, tracking 0em and tabular-nums
    line-height display: 1.10 (tight; the kinetic nature of the font substitutes for generous leading)

Frame Composition:
  hero: the generative field (particle system / mesh) occupies the full frame; type resolves from it
  secondary: a one-phrase label (5 words max) resolves at frame center from the particle system
  negative space: 0% by definition — the field fills the frame; but perceived density varies with scene
  grid: none — composition is emergent from the generative system; avoid imposed grid structure

Motion Posture:
  entrance: letters resolve from particle scatter, staggered per-character, 1200ms total, expo.out per char
  hold: 1.5s on the resolved phrase; field continues slow drift during hold (do not freeze it)
  transition: the field state transforms — hue shift or density change — over 800ms; no cut, no dissolve
  forbidden motion: slide, hard cut, static holds, any motion that reads as "presentation template"
  motion safety: per-character resolve stagger max 80ms between characters (total 1200ms over ≤15 chars); CJK characters if present resolve as single unit (no per-stroke stagger); Latin 800w at 64px max positional scatter radius 40px before resolve; hold 1.5s minimum — field drift during hold must be ≤ 4px/s apparent velocity; no text element may use linear ease
  GSAP ease: "expo.out" (cubic-bezier(0.83,0,0.17,1)) for character resolve; "sine.inOut" for field drift

Sonic Character:
  material metaphor: electromagnetic field — a physical hum that is also a light source
  bed: yes — a layered drone, 60–80Hz + 120Hz, -22dB; pulsing slowly at 0.1Hz rate
  micro-feedback: subtle particle-texture rustle, 40ms bursts at -20dB — as characters resolve
  accent hit: a harmonic resonance sweep, 600ms, -10dB — when the phrase fully resolves
  final lock: the drone fades 1200ms; last thing heard is the high harmonic tail
  forbidden sounds: dry clicks, impact SFX, anything percussive, anything with a sharp transient attack

Anti-slop check:
  Generic AI would: use a dark background with a purple-to-cyan gradient overlay, add floating particle dots
    as decoration, and reveal the headline with a simple opacity fade at 600ms ease-in-out
  This recipe demands: the type must emerge from the field (not float over it), the generative system must
    respond or appear to respond to the phrase content, and the sonic bed must feel like the field has mass

---

### Bloomberg Businessweek Turley — Typographic Violence
School: Brutalist / Raw
Source: web-design-engineer/references/style-recipes/bloomberg-businessweek-turley.md

Palette (video-native):
  bg: #FFFFFF (pure white for maximum contrast — or #000000 for inverted variant; no other bg colors)
  fg: #000000 (true black type on white; or #FFFFFF on black invert)
  accent: #FF3D00 (alert orange) or #FFE800 (signal yellow) or #001AFF (alert blue) — pick one per clip
  alt: none — maximum 3 colors total including bg and fg; the third color is the accent block
  material: offset newsprint — slightly rough; a halftone dot pattern at 3% opacity gives print registration feel

Typography (video roles):
  display: Druk Wide Heavy or Founders Grotesk 900, 160–200px — the type overflows the frame intentionally
  support: Plantin or Mercury, weight 400 italic, 14px — small, almost invisible; captions in corner
  data: same display family, 90px, tinted in accent color — for a single critical number or word
  weight contrast: 400 italic (7px optical size serif) vs 900 grotesque (200px) — maximum possible gap
  forbidden: tasteful design choices, rounded corners on type, Inter, any font below weight 700 at display

  optical corrections (typography-optics):
    display: Druk Wide Heavy / Founders Grotesk 900, 160–200px → tracking -0.04em to -0.05em (Table 2: 96px+ 900w; violence requires optical tightening or gaps read as broken)
    support: Plantin / Mercury 400 italic, 14px → tracking 0.00em (caption size; no adjustment needed)
    data: display family 900, 90px → tracking -0.03em (Table 2: 72–96px 900w)
    CJK display (if Chinese): 160px 900w → -0.05em (-0.06em with video modifier; extreme size demands extreme tightening)
    all-caps display: tracking -0.04em minimum (optical gap at 160–200px all-caps is magnified; tighten aggressively)
    accent-color data word: same tracking as display; do not open-track for color differentiation

Frame Composition:
  hero: type at 160–200px, clipped by frame edges intentionally — letters bleed off left, right, or top
  secondary: a flat accent color block (50–60% of frame) behind the type; no gradient, no texture
  negative space: < 15% — this recipe refuses negative space; tension comes from compression
  grid: anti-grid — content pushed against edges; elements touch the frame boundary by design

Motion Posture:
  entrance: type slams in from off-frame — x:-200px to position in 200ms, power4.out — no anticipation
  hold: 1.5s — the poster must be read but also felt as an assault
  transition: hard cut only — black flash (2 frames, 66ms) between scenes; no dissolve
  forbidden motion: easing that softens the impact, fade-in, any entrance slower than 200ms
  motion safety: slam travel distance x:-200px in 200ms — do not reduce travel to soften; CJK text if present must slam as Latin does (no opacity-only substitution in this recipe); 66ms black flash between scenes is mandatory (2 frames at 30fps); hold 1.5s; no text element may use any ease except power4.out or steps(1)
  GSAP ease: "power4.out" for slams; "steps(1)" for flash cuts; never "sine", never "back"

Sonic Character:
  material metaphor: offset press — mechanical, ink-on-paper physical impact
  bed: no music bed — silence creates tension between slams
  micro-feedback: none
  accent hit: a sharp impact transient, 20ms attack, -6dB — simultaneous with type slam landing; loud
  final lock: same impact at -8dB with a 60ms noise burst afterward — the press registers the paper
  forbidden sounds: music, whoosh, warm sounds, any sound that implies movement before landing

Anti-slop check:
  Generic AI would: use bold type but scale it to fit within the frame, add slight motion blur to the slam,
    soften the accent color to a muted orange-red, and use a cross-dissolve between scenes
  This recipe demands: type that visibly bleeds the frame, a single flat accent color at full saturation,
    an impact sound loud enough to make the viewer blink, and hard cuts with no dissolve whatsoever

---

### Mailchimp Freddie — Warm-Handed Character
School: Warm Humanist
Source: web-design-engineer/references/style-recipes/mailchimp-freddie.md

Palette (video-native):
  bg: #FFE01B (Mailchimp yellow — for hero/brand moments) or #FFFFFF (for body content scenes)
  fg: #241C15 (warm near-black — never pure black; the warmth prevents harshness against yellow)
  accent: #FF4D74 (hot pop-pink — sparingly; one pill, one underline, one illustration detail; < 4%)
  cream: #FBEFE3 (warm cream surface — backing panel behind illustration or body text block)
  material: uncoated matte with hand-drawn line texture; illustration elements have deliberate imperfection

Typography (video roles):
  display: Söhne 700 or Helvetica Now Display 700, 72px — friendly weight, not violent; lh 1.1
  support: same family 400, 24px — warm, conversational; personality in the copy matters as much as font
  data: same family 700, 48px — for a key metric; styled like a friendly announcement, not a dashboard
  weight contrast: 400 vs 700 — enough gap to create hierarchy but not intimidation
  forbidden: Inter at 400 (too cold), any weight above 800, any serif, any monospace

  optical corrections (typography-optics):
    display: Söhne / Helvetica Now Display 700, 72px → tracking -0.02em (Table 2: 56–72px 600–700w)
    support: same family 400, 24px → tracking 0.00em (Table 2: 20–28px 400w)
    data: same family 700, 48px → tracking -0.01em (Table 2: 40–56px 700w; friendly weight still tightens)
    CJK display (if Chinese): 72px 700w → -0.02em (-0.03em with video modifier)
    mixed CJK+Latin: Latin font-size ×1.09 OR Latin weight drop to 400 when CJK is 700; warmth is preserved
    line-height display: 1.10 (friendly but not cramped; back.out bounce needs lh room)
    line-height support: 1.50

Frame Composition:
  hero: Freddie-style illustration element (character, line-drawn prop) in 40% of frame, tilted ±5°
  secondary: headline text block in opposing quadrant; never both centered; always asymmetric
  negative space: 25–35% — warmer and tighter than pure minimalist schools; space feels inhabited
  grid: loose — elements follow an illustrator's instinct, not a strict grid; slight tilt is structural

Motion Posture:
  entrance: illustration bounces in — y:-20px, scale 0.9→1.0, cubic-bezier back.out(1.4), 500ms
  hold: 2.0s — the character should feel like it's there, present, looking at you
  transition: a friendly wipe (yellow flood fill left-to-right, 300ms) then reveal next scene
  forbidden motion: serious/stiff easing, sharp cuts, anything that removes the playfulness
  motion safety: illustration bounce y:-20px scale 0.9→1.0 — overshoot from back.out(1.4) must not exceed scale 1.04 at peak; CJK text if present uses power2.out only (no back.out on CJK — overshoot illegible); text elements max Y travel 12px at 500ms power2.out; hold 2.0s; yellow wipe must complete in 300ms with no easing
  GSAP ease: "back.out(1.4)" for illustration entrances; "power2.out" for text; "none" for yellow wipe

Sonic Character:
  material metaphor: wood and felt — warm, organic, a little bouncy
  bed: yes — a warm acoustic guitar bed or upright bass loop at -24dB; friendly, not corporate
  micro-feedback: a soft marimba tap, 60ms, -16dB — when a text element pops in
  accent hit: a warm "boing" spring sound, 180ms, -12dB — when the illustration bounces in
  final lock: a short upward musical sting (two notes), 300ms, -10dB — resolves with warmth
  forbidden sounds: digital clicks, impact SFX, dark drones, anything that reads as "corporate"

Anti-slop check:
  Generic AI would: use the yellow but center everything, use an AI-generated illustration style that has
    no consistent hand, animate with ease-in-out, and play a generic upbeat music track underneath
  This recipe demands: a real illustrator's line style (consistent hand), asymmetric composition with the
    illustration tilted, a back.out ease on the illustration entrance, and sound that feels handmade

---

### Stripe Press — Books as Objects
School: Warm Humanist (with editorial bones)
Source: web-design-engineer/references/style-recipes/stripe-press.md

Palette (video-native):
  bg: #F1ECDE (warm bone — not white; the warmth signals editorial care, not digital convenience)
  fg: #1A1A18 (very warm near-black — the warmth is essential; cool black reads as tech)
  accent: #1B4B5A (deep teal) or #A04A2A (burnt sienna) — one foil-stamp color per clip, never both
  surface: #E6DCC4 (darker warm surface for cloth-texture section breaks or backing panels)
  material: cloth-bound book cover — subtle textile grain at 4% opacity; shadow under objects is real

Typography (video roles):
  display: GT Sectra Display 400 italic or Domaine Display 400 italic, 80px — italic is mandatory
  support: Source Serif 400, 22px — body serif for sub-claims and quotes; lh 1.65
  data: Söhne 400, 16px, color #736D5A — for UI-role labels only; never at display size
  weight contrast: 400 italic display vs 400 roman support — differentiation through posture, not weight
  forbidden: sans at display size, any bold above 500, pure white ground, cold-cast neutrals

  optical corrections (typography-optics):
    display: GT Sectra Display / Domaine Display 400 italic, 80px → tracking -0.01em (Table 2: 72–96px 400w italic; slight tightening, never open; editorial warmth comes from the italic not from tracking)
    support: Source Serif 400, 22px → tracking 0.00em
    pull-quote oversized: display font 400 italic, 40px → tracking 0.00em (Table 2: 40–56px 400w; no correction needed at this size)
    data label: Söhne 400, 16px → tracking 0.00em
    CJK display (if Chinese): 80px 400w → -0.01em (-0.02em with video modifier); italic posture inapplicable to CJK — use upright weight 400 with tracking correction only
    mixed-script: if CJK title on book cover, Latin support label below in Source Serif roman only
    line-height display: 1.20 (italic at 80px; generous but not loose)
    line-height support: 1.65 (as specified)

Frame Composition:
  hero: the physical book object (cover photograph or render), occupying 40% of frame — the object is precious
  secondary: a pull-quote in oversized italic serif (display font, 40px), hung at left margin
  negative space: 40–50% — the object should have room to breathe and cast a shadow that reaches nothing
  grid: editorial column — centered with wide margins; pull-quotes hang into the left margin space

Motion Posture:
  entrance: book rotates gently (0→4° then back to 0°) as it fades in over 800ms — a physical reveal
  hold: 3.0s minimum; the book cover deserves study; the viewer should read the title in the hold
  transition: 1200ms cross-dissolve — slow like turning a page; Ken Burns on cover photography at 0.98→1.02
  forbidden motion: fast cuts, scale snaps, bounce, anything that makes the book feel cheap
  motion safety: book rotation 0→4°→0° max delta 4° — do not increase for drama; opacity entrance 800ms minimum; CJK text on book cover no rotation animate (opacity-only if CJK title present); Ken Burns zoom delta ≤ 4% over duration — imperceptible per-frame; hold 3.0s minimum; 1200ms dissolve is a hard floor
  GSAP ease: "sine.inOut" for rotation; "expo.out" for initial opacity; "sine.inOut" for Ken Burns

Sonic Character:
  material metaphor: cloth and paper — the texture of a well-made book, the resistance of a good binding
  bed: yes — a quiet string pad or very low piano note, -26dB; warm, not saccharine
  micro-feedback: a soft page-turn texture, 120ms, -18dB — at scene transitions
  accent hit: a single piano note (warm mid-register), 400ms decay, -12dB — when book comes to rest
  final lock: the string pad fades 800ms; the last thing is the warmth of the room
  forbidden sounds: digital SFX, impact transients, anything bright or high-frequency, music with rhythm

Anti-slop check:
  Generic AI would: use the warm cream palette but display the book cover as a flat 2D tile in a grid,
    use a sans headline at 500 weight, cross-dissolve at 300ms, and play a light acoustic guitar bed
  This recipe demands: the book as a photographed physical object with shadow, display italic serif only,
    a 1200ms dissolve that feels like turning a page, and sound that feels like cloth, not guitar strings

---

### Vercel Mesh — Precision Punctured by Light
School: Modern Tool / Builder SaaS
Source: web-design-engineer/references/style-recipes/vercel-mesh.md

Palette (video-native):
  bg: #000000 (true black — Vercel does not soften to charcoal; the ground is pure)
  fg: #EDEDED (off-white primary text — not pure white; prevents eye-strain harshness on black)
  accent: gradient mesh — #0070F3 (cyan-blue) fading into #FF0080 (magenta), feathered to black edges
  cta: #FFFFFF (white solid button label — maximum contrast; no gradient on the CTA itself)
  material: black glass with a single internal light source (the mesh); everything else is matte

Typography (video roles):
  display: Geist Sans 500 or Inter Tight 600, 68px — precision weight; not too heavy, not too light
  support: Geist Sans 400, 24px, #888888 — secondary statement; secondary label color is medium gray
  data: Geist Mono 400, 20px — deploy logs, terminal commands, version strings; the mono is essential
  weight contrast: 400 (#888888) vs 500–600 (#EDEDED) — contrast through weight AND luminosity
  forbidden: warm-toned fonts, serif of any kind, purple→pink gradient on text (the AI cliché)

  optical corrections (typography-optics):
    display: Geist Sans 500 / Inter Tight 600, 68px → tracking -0.02em (Table 2: 56–72px 500–600w)
    support: Geist Sans 400, 24px → tracking 0.00em (Table 2: 20–28px 400w)
    data: Geist Mono 400, 20px → tracking 0em strictly; tabular-nums enforced; monospace optical neutrality
    CJK display (if Chinese): 68px 600w → -0.02em (-0.03em with video modifier)
    mixed CJK+Latin: Latin font-size ×1.09 OR Latin weight drop to 400 when CJK is 600
    terminal/code text: Geist Mono tracking 0em always; do not adjust for line length
    line-height display: 1.12 (precision; looser than Bloomberg Terminal but tighter than humanist recipes)

Frame Composition:
  hero: the gradient mesh occupies full frame in the first beat, then collapses to 30% as hero
  secondary: a terminal-style readout or product UI screenshot enters right half, 45% of frame
  negative space: 25–35% — the black ground IS the negative space; it should feel deliberate
  grid: 12-col strict; mesh bleeds frame; all text and UI elements snap to grid

Motion Posture:
  entrance: mesh drifts slowly into frame (transform: translate(-8px, -6px)→(0,0) over 20s loop)
  hold: the mesh is always in slow motion — it never fully stops; hold means text holds while mesh drifts
  transition: 300ms opacity cross-fade on text; mesh continues uninterrupted through transitions
  forbidden motion: mesh that stops entirely, bright gradient animations, anything that draws from the
    purple-pink-blue AI cliché gradient; the mesh must be cool and restrained
  motion safety: text entrance max Y 20px at 380ms power3.out; CJK display at 68px max Y 30px at 0.38s; mesh drift velocity ≤ 0.5px/frame (8px over 20s loop) — imperceptible on any single frame; hold means text is static while mesh drifts; 300ms cross-fade on text is a hard ceiling; no text element may animate with linear ease
  GSAP ease: "sine.inOut" for mesh drift; "power3.out" (cubic-bezier(0.16,1,0.3,1)) for text entrances

Sonic Character:
  material metaphor: electromagnetic interference — a precision machine's cooling fan heard through glass
  bed: yes — a low-frequency sine wave drone at 55Hz, -28dB; the mesh hums
  micro-feedback: a short digital key-click, 8ms, -16dB — when code/terminal text appears
  accent hit: a clean sine sweep upward (200ms), -10dB — when the mesh collapses and product reveals
  final lock: drone fades 600ms; the last frame is as silent as the mesh is still
  forbidden sounds: whoosh, music with melody, warm instruments, any SFX that implies warmth

Anti-slop check:
  Generic AI would: use dark background but pick a bright purple-to-cyan gradient, animate the mesh
    dramatically, use weight 700 on the headline, and add glow halos around every UI element
  This recipe demands: the mesh feathered completely to black at the edges (not a visible rectangle),
    only one mesh per clip (never two), Geist or Inter Tight at 500–600 (not 700), and a sonic bed that
    sounds like the server room — cold, precise, never warm
