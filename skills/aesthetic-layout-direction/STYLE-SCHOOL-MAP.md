# Style School Map — Video DNA Reference

This document maps all 6 design schools to video-native tokens. Values are specified for rendered motion-graphic video at 1280×720 (standard) and noted for 3840×2160 (4K) where they differ. All hex values are sRGB. All font sizes are in CSS px units at the render canvas size. All GSAP eases are named for direct use in GSAP 3.x timelines.

## Quick Reference Table

| School | Video Register | Energy (1–10) | Motion Posture | Sonic Character |
|---|---|---|---|---|
| 1 — Information Architecture | Data Authority / Broadcast | 4 | Institutional: baseline slide, data hit, ticker | Dry percussive: scoreboard thud, short tick, broadcast snap |
| 2 — Editorial / Minimalist | Premium Launch / Quiet Luxury | 2 | Restrained: slow fade, long hold, intentional silence | Soft material: paper turn, cloth, low cinematic pulse |
| 3 — Motion / Experimental | Kinetic Brand / Generative | 9 | Generative: particle resolve, morph, full-state transform | Electric texture: synthetic transient, processed air, generative noise |
| 4 — Brutalist / Raw | Brand Drop / Poster Motion | 7 | Aggressive: slam cut, long uncomfortable hold, snap to place | Hard print: dry stamp impact, paper slice, vinyl noise |
| 5 — Warm Humanist | Inspirational / Lifestyle / Educational | 4 | Gentle: bouncy on joy, breathing on calm, slow swell | Soft organic: airy whoosh, warm riser, soft organic hit |
| 6 — Modern Tool / Builder SaaS | Product Demo / Technical | 6 | Snappy: cubic-bezier(0.22,1,0.36,1), micro-feedback, product behavior | Clean digital: UI click, precise whoosh, controlled lock |

---

## School 1 — Information Architecture
**Video register: Data Authority / Broadcast**

### Named Anchors
- **Paula Scher / Pentagram** — typographic authority, type-as-image, institutional weight
- **Edward Tufte** — maximum data-ink, chartless decoration, sparklines in prose
- **Bloomberg Terminal** — mission-critical density, amber-on-navy, monospaced tabular data
- **Massimo Vignelli** — Swiss grid discipline, baseline alignment, systematic hierarchy
- **NYT editorial broadsheet** — rule lines, byline precision, evidence-first layout

### Web Recipes to Reference
- `pentagram.md` — hero type at bleed scale, flat color blocks, two-color system
- `tufte-dataink.md` — data-ink ratio, side-notes, direct labels, small multiples
- `bloomberg-terminal.md` — multi-pane density, amber accent, monospace, hairline borders
- `vignelli-swiss-helvetica.md` — strict grid, Helvetica as system, baseline alignment
- `nyt-the-daily.md` — rule lines, editorial hierarchy, byline structure

### Palette (video-optimized, 1280×720)
| Role | Hex | Note |
|---|---|---|
| Background (light) | `#F5F0E8` | Warm paper off-white — never `#FFFFFF` |
| Background (dark) | `#08111A` | Deep navy-black; slightly warmer than web terminal for video gamma |
| Surface panel (dark) | `#111C2E` | Raised pane background; data panels and chart containers |
| Surface raised (dark) | `#192440` | Tertiary surface; highlighted row, active pane |
| Primary text (dark bg) | `#E8ECF4` | Near-white, high-contrast prose and data labels |
| Ink (light bg) | `#1A1614` | Warm ink, not pure black |
| Data amber | `#FFA02F` | Bloomberg signature; primary metrics, key headlines |
| Data positive | `#00B96B` | Price-up, success, positive delta |
| Data negative | `#F23645` | Price-down, alert, negative delta |
| Hairline border | `#2A3554` | Panel dividers; 1px only |
| Muted label | `#5E6680` | Secondary labels, axis text, lower-thirds metadata |
| Accent (Pentagram cobalt) | `#1E3FFF` | Pentagram/type-poster mode only — not terminal |
| Accent (Scher red) | `#B83A1F` | For flat color blocks under oversized display type |
| Forbidden palette | — | Cyan glow, purple, neon, neutral `#808080` as primary, gradient fills |

### Typography (1280×720 px)
| Role | Family | Weight | Size at 720p | Size at 4K |
|---|---|---|---|---|
| Display (Pentagram) | Helvetica Now / Söhne Breit / Druk | 800–900 | 96–140px (bleed to edge) | 280–400px |
| Display (Terminal) | IBM Plex Mono / JetBrains Mono | 400–700 | 48–72px | 140–200px |
| Data label | IBM Plex Mono / Berkeley Mono | 400 | 22–28px | 64–80px |
| Axis / metadata | IBM Plex Mono | 400 | 16–18px | 48–54px |
| Body (Tufte mode) | ET Book / Lyon Text / Equity | 400 | 28–32px | 80–96px |
| Support (Pentagram) | same grotesque as display | 400 | 26–34px | 76–96px |

- **Weight contrast:** Pentagram: 400 (support) vs 900 (display) — maximum. Terminal: mono 400 throughout — no weight contrast.
- **Letter-spacing:** Display grotesque: -0.02em. Monospace: 0 (tabular natural). Uppercase metadata: +0.10em.
- **Tabular numerals:** Always `font-variant-numeric: tabular-nums` on every data value without exception.
- **Forbidden:** Inter at default weight, Roboto, rounded grotesques, italic on numbers, decorative serifs, Georgia.

### Composition
- **Grid:** 12-column strict, 24–32px gutters at 720p. Baseline grid alignment for every text element.
- **Hero element:** In Pentagram mode — type occupies 60–80% of frame height, bleeds past safe area intentionally. In Terminal mode — 4–6 data panels, multi-pane with hairline dividers.
- **Focal points:** 2 maximum — primary metric/headline + one supporting datum or source. Never 3.
- **Negative space:** 20–35%. This school fills space with data, not air. Empty space means missing data.
- **Edge anchoring:** Title pinned top-left or bottom-left, hard against frame edge. No centered compositions except final Pentagram poster lockup.
- **Decorative elements:** None. No illustration, no photography as atmosphere, no gradient fills.

### Motion Posture
- **Entrance:** Baseline slide-up (y: 24px → 0, opacity 0 → 1, 250–400ms, `power3.out`) or instant flip (terminal data updates, 80ms blink flash). No fade-ins for primary data.
- **Hold:** Data holds 2.0–3.5s minimum. The viewer must read the data. Pentagram type holds 1.5–2.5s at hero scale.
- **Transition:** Hard cut between Pentagram poster frames. Lower-third snap (0.3s, `steps(4)`) for data swaps. Ticker: uniform `linear`, no easing.
- **Energy level:** 4/10 — authoritative, not aggressive. Motion serves legibility.
- **GSAP eases:** `power3.out` for baseline slides. `power4.out` for data hit counts. `linear` for ticker scroll. `steps(4)` for data flips. Never `back.out`, `elastic`, `bounce`.
- **Key forbidden motion:** Particle systems, camera push-in, morphing type, bouncy spring, scale reveals on data panels, any effect that reads as "fancy."

### Sonic Character
- **Material metaphor:** Metal and dry broadcast electronics. A trading floor, not a cinema.
- **Transient shape:** Dry snap and short percussive thud. Immediate attack, decay under 80ms. No reverb tail.
- **Density:** Medium — scoreboard thud on each metric reveal, short tick on data update, broadcast snap on lower-third. One cue per 1.5–2.0s of active motion.
- **Bed:** Low broadcast ambience at -28dBFS or none. Never music.
- **Forbidden sounds:** Cinematic swells, soft whooshes, airy risers, warm string pads, UI glass clicks, SaaS product sounds, organic nature sounds.

### Best For
Data story clips, financial brand films, quarterly results presentations, B2B SaaS product films where authority matters more than warmth, broadcast package lower-thirds, dashboard demos, statistical explainers.

### Forbidden Elements
- Any color not in palette (especially cyan/purple glow)
- Photography or illustration as decoration
- Rounded corners on data panels
- Gradient fills of any kind
- Centered composition without deliberate poster reason
- Bouncy or spring-based motion
- Conversational or warm microcopy

### Anti-Slop Check
- **Generic AI output would:** Use a dark background with cyan accent, add glowing HUD rings around metrics, apply a light-leak gradient, set the headline in Inter Bold 700.
- **This school does instead:** Sets the headline in Druk 900 at 130px on a flat cobalt field (Pentagram), or fills the frame with amber monospace data on deep navy panels with 1px hairline dividers (Terminal). No glows. No rings. No gradient. The type is the visual.

---

## School 2 — Editorial / Minimalist

**Named anchors**: Kenya Hara / MUJI, Apple HIG, Aesop, Dieter Rams / Braun, Monocle magazine.
**Web recipes**: `muji-kenya-hara`, `apple-hig`, `aesop`, `dieter-rams-braun`, `monocle-magazine`

### Palette (video-native, 1280×720)
- **Background**: `#F2EDE6` (warm chamois/paper) or `#FAFAF8` (near-white with warmth)
- **Foreground**: `#1C1814` (warm near-black — not pure `#000000`)
- **Accent**: `#8B6914` (amber/gold rule) or `#5C6B4C` (sage) — single rule line or seal mark only; < 3% of frame
- **Material**: matte surface, slight paper texture if used; no glass, no sheen, no grain unless photographic
- **Forbidden palette**: cyan, purple, neon, saturated colors, cool grays, pure white, gradient of any kind

### Typography (1280×720 px)
- **Display**: Editorial serif (e.g., Canela Light 300, Freight Display Pro, or GT Sectra Regular) — 80–120px; generous tracking (-0.01em)
- **Support**: Quiet humanist sans (e.g., Söhne Buch 350 or Aktiv Grotesk Light 300) — 26–34px; generous line-height (1.55)
- **Data**: Tabular humanist sans or restrained serif with `font-variant-numeric: tabular-nums` — 20–26px; same palette as support
- **Metadata**: small, tracked, upper case — 14–18px; same weight as support
- **Weight contrast**: 300 vs 300 (restrained) or 300 vs 700 for one emphasis element
- **Letter-spacing**: -0.01em display; +0.10em on upper metadata
- **Forbidden**: condensed sans for display, bold display serif, italic as decoration (only for quotes), Inter, Poppins, system sans

### Composition
- **Grid**: loose — rule of thirds; deliberate off-center placement; no strict column snap
- **Hero element**: product or subject owns 50–65% of frame in clean, well-lit isolation; editorial treatment (not diagram)
- **Focal points**: 2 — subject/product + title or claim; everything else is metadata
- **Negative space**: 40–55%; whitespace is the primary visual material, not leftover
- **Edge anchoring**: title may anchor bottom-left or right; product may bleed one edge deliberately
- **Text safe areas**: 64px from edges; no subtitle running under hero object

### Motion Posture
- **Entrance**: slow fade or slow mask reveal (600–900ms); `sine.inOut` or `power2.inOut`
- **Hold**: 2–3s for primary element; long deliberate pauses between reveals
- **Transition**: opacity cross-fade (400–600ms) or slow mask slice; never a wipe plate; never hard cut
- **GSAP eases**: `sine.inOut` for ambient; `power2.inOut` for entrance; `linear` for continuous ambient motion
- **Energy level**: 2 / 10 — meditative; any higher feels wrong for this school
- **Ambient motion**: very slow product rotation or drift (0.02deg/frame), or none
- **Forbidden motion**: kinetic type hits, shape bursts, stinger cuts, bounce, spring, any entrance faster than 400ms

### Sonic Character
- **Material metaphor**: soft air, linen, matte ceramic — quiet and close
- **Transient shape**: soft swell with no attack; barely-perceptible ambient fade
- **Density**: very sparse — 1–2 SFX for a 30s clip; silence is the primary "sound"
- **Bed**: low sustained air or room tone — just enough to prevent emptiness
- **Micro-feedback**: none, or an almost inaudible page-breath
- **Accent hit**: one restrained low-frequency sine hit for the main product reveal — no transient
- **Final lock**: silence, or a single sustained low note that fades to nothing
- **Forbidden sounds**: whoosh, UI click, stinger, any sharp transient, cinematic impact, drum hit

### Best for
Luxury product launches, high-consideration B2C (cosmetics, fashion, furniture, premium food), premium SaaS brand films, personal brand / portfolio, editorial journalism, lifestyle brand identity.

### Forbidden elements
Neon or saturated accent, gradient background, HUD, any card grid, kinetic text burst, data visualization, feature list, any element that reads as "SaaS", hard shadows.

---

## School 3 — Motion / Experimental

**Named anchors**: Field.io, Active Theory, Resn.
**Web recipes**: `field-io`, `active-theory`, `resn-storytelling`

### Palette (video-native, 1280×720)
- **Background**: `#080808` (near-black) or deep saturated dark (`#0D0A1A`)
- **Foreground**: `#F0EDE8` (warm off-white) or reactive procedural color
- **Accent**: one electric hue — `#00EFCE` (electric mint), `#FF3D00` (signal red), `#C8FF00` (acid yellow); cycling through hue space is permitted if choreographed
- **Material**: generative, no fixed material — elements feel like data objects, not physical materials
- **Forbidden palette**: muted warm neutrals, paper, linen, corporate blue, gradient gradient (only structured hue cycling allowed)

### Typography (1280×720 px)
- **Display**: variable font preferred (e.g., Fraunces, Recursive) or extreme condensed (Compakt, Barlow Condensed 100–900) — 96–200px; transforms on beat
- **Support**: mono or near-invisible; text serves motion, not the other way around
- **Data**: mono; displayed only when the data IS the visual event
- **Weight contrast**: variable axis (wght: 100 to 900 animated) or extreme static contrast
- **Forbidden**: static body text blocks; centered unmoving type; default-weight unmodified sans

### Composition
- **Grid**: non-standard — deliberate off-grid, rotated, or generative positioning
- **Hero element**: the motion event is the hero — no single static object; multiple elements in choreography
- **Focal points**: fluid — the eye is guided by motion path, not fixed composition
- **Negative space**: dynamic — negative space appears and disappears as part of the motion
- **Edge anchoring**: elements cross edges; bleed is intentional; frame crop is a design decision

### Motion Posture
- **Entrance**: physics — `expo.out`, spring physics, quintic, or custom cubic; fast (100–300ms) with anticipation
- **Hold**: brief or none — the design lives in transition, not in stasis
- **Transition**: match cut, object morph, camera tunnel, or wipe that IS the design
- **GSAP eases**: custom cubic-bezier, `elastic.out(1, 0.3)`, `expo.out`; never `linear` for hero motion
- **Energy level**: 8–10 / 10 — continuous; any hold longer than 1.5s needs strong visual justification
- **Forbidden motion**: static entrance + hold + exit pattern; slide transition; card grid animation; anything "presentation-like"

### Sonic Character
- **Material metaphor**: electronic synthesis — the sound is designed, not recorded
- **Transient shape**: custom-designed; may be a swell that morphs into a hit; electronic texture
- **Density**: continuous or dense — music and SFX are integrated, not separate
- **Bed**: electronic ambient texture — this school permits and often requires a music bed
- **Accent hit**: choreographed to motion beat; the hit IS the visual event
- **Final lock**: orchestrated — silence, or a sustained frequency that holds with the final frame
- **Forbidden sounds**: generic SFX pack whoosh, random impact, SaaS UI click

### Best for
Brand films, agency showreels, launch moments for entertainment products, experimental title sequences, festival IDs, anything where the medium itself is the message.

### Forbidden elements
Static card, centered layout, text-explains-visual pattern, gentle fade, any element that could exist in a PowerPoint.

---

## School 4 — Brutalist / Raw

**Named anchors**: Are.na / Honest Web, Bloomberg Businessweek (Turley era), Balenciaga post-2017.
**Web recipes**: `are-na`, `bloomberg-businessweek-turley`, `balenciaga-post-2017`

### Palette (video-native, 1280×720)
- **Background**: `#FFFFFF` (pure white — on purpose) or `#000000` (pure black — on purpose)
- **Foreground**: `#000000` on white, or `#FFFFFF` on black — maximum contrast, no warmth
- **Accent**: single high-voltage color — `#FF4500` (signal orange), `#FFEC00` (emergency yellow), `#0055FF` (blueprint blue) — used as a single color slap, not as decoration
- **Material**: flat, none — no glass, no grain, no shadow; the typography IS the material
- **Forbidden palette**: warm neutrals, off-white, cream, muted tones, gradients, multi-color palettes

### Typography (1280×720 px)
- **Display**: one extreme-weight typeface at absurd scale — Helvetica Neue Black 200–300px; Druk Wide Bold; ABC Monument Grotesk Black — bleeds past frame edge deliberately
- **Support**: same typeface at 400 weight, or system font (Arial) intentionally
- **Data**: mono, or absent — this school treats data as confrontational, not explanatory
- **Weight contrast**: 900 only — or 400 vs 900; no middle weights except for emphasis reversal
- **Letter-spacing**: -0.04em on display (tightly kerned for mass); 0 on support
- **Forbidden**: elegant serif, rounded sans, any font with personality (personality is weakness in this school)

### Composition
- **Grid**: deliberately broken or hyper-rigid — no "designed" middle ground
- **Hero element**: the word IS the hero; type fills 70–100% of frame, cropped
- **Focal points**: 1 — the type mass or the color event; nothing competes
- **Negative space**: zero (everything filled) OR extreme (95% empty, one word); no comfortable middle
- **Edge anchoring**: type bleeds all four edges, or sits at exact center at enormous scale — no "nice" placement
- **Text safe areas**: ignored intentionally — the discomfort IS the design

### Motion Posture
- **Entrance**: instant cut or hard snap with no easing — `steps(1)` or `power4.in` into immediate stop
- **Hold**: uncomfortably long (2–4s) or uncomfortably short (0.1–0.3s flash)
- **Transition**: smash cut; frame flicker; inverted flash — never smooth
- **GSAP eases**: `steps(1)` for snaps; `power4.in` for aggressive arrives; `linear` for holds; NO `back.out`, `elastic`, `bounce`
- **Energy level**: 7–9 / 10 for aggressive; 1 / 10 for dead-pan long holds — no middle
- **Forbidden motion**: smooth ease-out, gentle fade, parallax, any motion that tries to be beautiful

### Sonic Character
- **Material metaphor**: dry paper tear, stamp, vinyl crackle, newsprint — physical, cheap, lo-fi
- **Transient shape**: hard stamp or dry crackle — no reverb, mono, close-mic
- **Density**: sparse but confrontational — 2–4 SFX; each one lands with force
- **Bed**: silence or barely-audible static — never music bed unless it is also harsh
- **Accent hit**: sharp stamp for text arrival; vinyl click for cut
- **Final lock**: silence or a brief noise burst — never a sustained resonant note
- **Forbidden sounds**: any "premium" audio — cinematic swell, soft whoosh, warm riser, UI click

### Best for
Fashion brand drops, editorial music video title sequences, counter-culture product launches, art/culture brands, anything that positions itself against "nice design."

### Forbidden elements
Rounded corners, soft shadow, gradient background, warm palette, elegant font, any motion that tries to smooth the experience, any element that could be mistaken for "polished."

---

## School 5 — Warm Humanist

**Named anchors**: Mailchimp Freddie era, Stripe Press, Headspace / Calm.
**Web recipes**: `mailchimp-freddie`, `stripe-press`, `headspace-meditation`

### Palette (video-native, 1280×720)
- **Background**: `#FFF8EE` (warm cream) or `#F5EDD6` (paper tan) — Mailchimp yellow (`#FFE01B`) as full background for joyful moment only
- **Foreground**: `#1A1410` (warm near-black) or `#2D2420` (chocolate)
- **Accent**: `#E8721A` (terracotta) or `#4A7A5C` (sage green) or `#4A6FA5` (soft blue) — used warmly, at 10–20% of frame
- **Material**: paper texture (Stripe Press), slight warm grain, cloth-like softness — never glass or metal
- **Forbidden palette**: cold gray, pure white, cyan, purple, neon, dark ground backgrounds (unless it's a night scene in a story)

### Typography (1280×720 px)
- **Display**: warm editorial serif (e.g., Freight Display, Canela Text, or Bookerly) — 72–110px; generous line-height; not tight-tracked
- **Support**: friendly humanist sans (e.g., Nunito 400, Aktiv Grotesk 300, or DM Sans 400) — 28–36px; extra line-height (1.6)
- **Data**: humanist sans with `font-variant-numeric: tabular-nums` — avoid cold mono for emotional content
- **Weight contrast**: 400 vs 700 — visible but not harsh; this school never uses 900
- **Letter-spacing**: 0 to +0.02em on display (open, not tight); +0.06em on metadata
- **Forbidden**: condensed typeface, mono for body, bold display that feels aggressive, Inter at tight tracking

### Composition
- **Grid**: organic — illustration or photography anchors the frame; text plays a supporting role
- **Hero element**: illustration/photography/person owns 50–60% of frame; warm and human
- **Focal points**: 2–3 — subject + title + supporting warmth element (texture, hand-drawn mark)
- **Negative space**: 35–45%; feels like breathing room, not designed emptiness
- **Edge anchoring**: loose — elements placed warmly, not rigidly; slight imperfection is acceptable
- **Text safe areas**: 48px from edges; keep caption below hero, not overlapping

### Motion Posture
- **Entrance**: gentle fade or soft mask reveal (500–800ms); `sine.inOut` or `power2.out`
- **Hold**: 1.5–2.5s; pace feels conversational, like a friend explaining
- **Transition**: dissolve or soft wipe; never hard cut unless for emotional emphasis
- **GSAP eases**: `sine.inOut` throughout; occasional `back.out(1.3)` for bouncy joyful moments (Mailchimp register only)
- **Energy level**: 4 / 10 for Stripe Press/Headspace; 6 / 10 for Mailchimp joyful moments
- **Forbidden motion**: kinetic type burst, sharp stinger, slam cut, bounce-heavy spring (except Mailchimp), speed smear

### Sonic Character
- **Material metaphor**: warm paper, wood, cloth — tactile and human
- **Transient shape**: soft swell, gentle click, page rustle — attack is soft, tail is warm
- **Density**: sparse to medium — 3–6 SFX with plenty of breathing room
- **Bed**: soft acoustic texture (light piano, gentle strings, or warm ambience) — this school permits and often benefits from a music bed
- **Micro-feedback**: paper rustle, soft air, gentle chime — small and warm
- **Accent hit**: warm low note or soft marimba hit for reveals — never sharp
- **Final lock**: warm sustained chord or gentle piano note — something that feels like resolution
- **Forbidden sounds**: UI click, digital stinger, hard mechanical impact, neon buzz, cold electronic texture

### Best for
Educational explainers, community product launches, creator tool demos, wellness / health brand films, personal brand / founder story, children's product, anything where trust and warmth are the primary brand values.

### Forbidden elements
Cold gray, neon, HUD elements, feature bullet lists, hard cuts, mechanical motion, any element that reads as "corporate" or "technical."

---

## School 6 — Modern Tool / Builder SaaS

**Named anchors**: Linear, Vercel, Raycast, Notion pre-AI.
**Web recipes**: `linear`, `vercel-mesh`, `raycast`, `notion-pre-ai`

### Palette (video-native, 1280×720)
- **Background**: `#111110` (warm dark — not pure black; Linear's warm 1px-border world) or `#0A0A0A` for Vercel precision
- **Foreground**: `#EDEBE6` (warm near-white — not pure white)
- **Accent**: `#6366F1` (Linear violet) or `#E8FF47` (Raycast highlight) or `#FFFFFF` (pure white for Vercel contrast) — < 5% of pixel area; never used as a background
- **Border**: `#2A2925` hairline at 1px (Linear) or `rgba(255,255,255,0.10)` (Vercel glass)
- **Material**: UI glass or flat warm dark — no paper, no organic texture, no film grain
- **Forbidden palette**: purple-pink-blue gradient as background, cyan glow, neon orb, warm cream background (belongs to School 5)

### Typography (1280×720 px)
- **Display**: humanist sans or condensed grotesk — Inter Display 600, Geist 700, or Söhne Halbfett 500 — 72–110px; controlled
- **Support**: same family at 400 weight — 26–32px
- **Data/labels**: mono with strict tabular (`font-variant-numeric: tabular-nums`) — IBM Plex Mono, JetBrains Mono — 18–24px; keyboard chip aesthetic (rounded rect container, 1px border)
- **Weight contrast**: 400 vs 700; never 300 (too romantic for this school)
- **Letter-spacing**: -0.02em on display; +0.04em on mono label chips
- **Forbidden**: Inter at default weight (0.0em tracking looks lazy for this school), geometric rounded sans like Nunito, decorative serif

### Composition
- **Grid**: structured — 12-column, 16px gutters at 720p; elements respect column edges
- **Hero element**: the UI or product interface IS the hero — visible, functional, large (55–65% of frame)
- **Focal points**: 2 — product UI/behavior + claim text; metadata and labels as supporting
- **Negative space**: 25–35%; purposeful but not luxurious — this school is information-dense by nature
- **Edge anchoring**: title anchors top or bottom; product UI centered or right-anchored; labels inline
- **Text safe areas**: 48px from edges; subtitles below UI; captions top-right for metadata

### Motion Posture
- **Entrance**: fast micro-entrance (150–250ms `power3.out`) for UI elements; main reveal at 350–500ms
- **Product behavior loop**: UI state changes (generating, selecting, rendering, exporting) run continuously as the anchor — this is the hero motion
- **Transition**: hard cut between scenes or precise mask (200ms); no cross-fade unless intentional
- **GSAP eases**: `power3.out` for entrances; `power4.out` for snap reveals; `steps(1)` for instant state changes
- **Energy level**: 5–6 / 10 — precise and active, but never frenetic
- **Forbidden motion**: slow fade, organic parallax, bounce spring physics, particle burst, generative motion

### Sonic Character
- **Material metaphor**: glass and precision plastic — like a high-end mechanical keyboard
- **Transient shape**: clean dry click, precise whoosh (tight, short, no reverb), mechanical lock
- **Density**: medium — 5–8 SFX; one per major UI state change; micro-feedback for repeated small actions
- **Bed**: none or very low digital ambience
- **Micro-feedback**: UI click / keyboard tick for repeated small interactions
- **Accent hit**: clean precise impact for primary reveal or metric drop
- **Final lock**: a single mechanical lock or brief digital confirmation — resolved, not dramatic
- **Forbidden sounds**: warm organic whoosh, cinematic swell, paper sound, vinyl crackle, any "premium soft" audio

### Best for
AI/SaaS product launches, feature demo clips, developer tool identity videos, startup pitch clips, dashboard data storytelling, technical explainers.

### Forbidden elements
Purple-pink gradient background, floating neon orbs, heavy HUD decoration, warm paper texture, slow organic fade, soft inspirational music bed, any element that reads as "lifestyle" rather than "tool."
