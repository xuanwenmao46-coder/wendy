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
**Video register: Premium Launch / Quiet Luxury**

### Named Anchors
- **Kenya Hara / MUJI** — emptiness as fullness, off-white as value, near-silence
- **Apple HIG** — clarity, deference, depth through restraint
- **Aesop** — apothecary refinement, serif-body as conversation, amber rule accent
- **Dieter Rams / Braun** — less but better, function as the only ornament
- **Monocle magazine** — editorial confidence, photography as evidence, serif body

### Web Recipes to Reference
- `muji-kenya-hara.md` — off-white ground, 60–80% empty space, tiny small-caps labels, hairline rules
- `aesop.md` — chamois palette, transitional serif, amber accent used once, asymmetric layout
- `apple-hig.md` — clarity through space, deference to content, material depth without decoration
- `dieter-rams-braun.md` — grid discipline, no ornament, function as beauty
- `monocle-magazine.md` — editorial serif, rule lines, photography as evidence

### Palette (video-optimized, 1280×720)
| Role | Hex | Note |
|---|---|---|
| Background | `#F2EFE8` | Warm paper off-white — never pure `#FFFFFF`; video gamma slightly warmer |
| Background (dark mode) | `#1A1814` | Warm near-black for dark premium mode; not pure black |
| Surface | `#EAE6DC` | Slightly darker warm cream for panels or product plinth |
| Primary text | `#2A2A28` | Warm ink — never `#000000` |
| Secondary text | `#7C7B76` | Muted warm gray for labels and metadata |
| Hairline | `#D0CCC2` | Rule lines — the only ornament; 1px at 720p |
| Accent (Aesop amber) | `#7A4623` | Use at most once per scene — single rule or seal mark |
| Accent (MUJI red) | `#C8161D` | Corner mark only; never fill or CTA color |
| Forbidden | — | Saturated blues, purples, cyans, greens as fills; any gradient |

### Typography (1280×720 px)
| Role | Family | Weight | Size at 720p | Size at 4K |
|---|---|---|---|---|
| Display (serif) | GT Sectra / Lyon Text / Suisse Works | 400, italic available | 72–100px | 200–280px |
| Display (humanist sans) | Söhne / Calibre / Inter Tight | 400–500 max | 64–88px | 180–240px |
| Body | same family as display | 400 | 32–38px | 88–108px |
| Label / small-caps | Söhne / Helvetica Now | 400, small-caps | 18–20px | 52–60px |

- **Weight contrast:** Minimal. Use 400 throughout. Never bolder than 500 (MUJI rule). Use size contrast instead of weight contrast.
- **Letter-spacing:** Display: 0.00–0.02em (open, never tight). Small-caps labels: +0.10–0.14em. Body: 0.
- **Italic:** Available for serif display — a key signature move. Never italic on labels.
- **Forbidden:** Bold weights 600+, condensed grotesques, gradient text, Inter at default weight, any sans at display scale without editorial intent, Poppins, system sans.

### Composition
- **Grid:** Asymmetric. Title bottom-left, product image right-center or right-top. Never a centered stack.
- **Hero element:** Single product object — 40–55% of frame area. Photographed (or treated as photographed), not diagrammed. Surrounded by intentional empty space.
- **Focal points:** 1–2 maximum. Product/image + one title block. Never a feature card row.
- **Negative space:** 40–60% intentional emptiness. This is not leftover space — it is the primary design material.
- **Edge anchoring:** Titles anchor bottom or left edge. Metadata pins top-right with small-caps label. Product floats upper or right zone.
- **Photography treatment:** Warm-graded, raking light from top-left, single soft shadow. Never stock-photo brightness or saturation.

### Motion Posture
- **Entrance:** Slow opacity fade 600–900ms `sine.inOut`. Product may scale from 0.96 to 1.0 during reveal (barely perceptible). No slide, no wipe, no mask.
- **Hold:** 2.0–4.0s. This school holds long. Silence between reveals is deliberate and designed.
- **Transition:** Crossfade 800ms `sine.inOut`. No wipes, no slices, no cuts.
- **Energy level:** 2/10 — the motion should feel like the product breathing, not announcing itself.
- **GSAP eases:** `sine.inOut` throughout. `power1.out` for product scale micro-reveal. Never `power4`, `expo`, `back`, `elastic`.
- **Key forbidden motion:** Kinetic type, particle systems, mask slices, camera zoom, stagger-burst entries, spring physics. The frame must feel like it is inhaling, not launching.

### Sonic Character
- **Material metaphor:** Paper and cloth. The sound of a well-made object placed on a linen surface.
- **Transient shape:** Soft swell with a short tail. Attack 30–60ms rise. Decay 200–400ms. No hard transient edge.
- **Density:** Very sparse — 1–2 cues per clip. Long silence between. Silence is the primary sound design choice.
- **Bed:** Very low cloth ambience at -28dBFS or none.
- **Forbidden sounds:** UI clicks, digital swooshes, data hits, synthetic beeps, broadcast snaps, hard impacts, any SaaS product sound.

### Best For
Luxury product launches, high-consideration B2C (cosmetics, skincare, furniture, premium food), premium SaaS brand films, lifestyle goods campaigns, editorial journalism films, B2C products where restraint signals confidence.

### Forbidden Elements
- Any saturated color applied as fill or background
- Bold typography (weight 600+) in any role
- Bouncy motion of any kind
- Centered stack of feature cards
- Photography treated as a wallpaper background
- Multiple competing focal points
- Any animation faster than 400ms

### Anti-Slop Check
- **Generic AI output would:** Use black background, add soft purple glow around the product, set the headline in Inter Bold 700, apply gradient text on the product name.
- **This school does instead:** Grounds the product on `#F2EFE8` warm chamois, allows 50% of the frame to sit empty, sets the title in GT Sectra 400 at 88px with no decoration, places one amber 1px rule below the product name, and lets the reveal breathe for 900ms without any secondary motion.

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
