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
- **Letter-spacing (Latin):** Display grotesque 96px+ 900w: −0.04em. Display grotesque 72–96px 700w: −0.02em. Monospace: 0 (tabular natural). Uppercase metadata 12–18px: +0.10em.
- **Letter-spacing (CJK):** Display 96px+ 900w: −0.04em (−0.05em with video modifier). Display 72–96px 700w: −0.03em. Support labels: 0.00em. Uppercase CJK metadata: +0.06em.
- **Mixed-script lines:** Latin receives −1 weight step when adjacent to CJK 900w, or Latin font-size +10%.
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
- **Motion safety limits:** CJK display text (72px+): max translate Y 40px at 0.3s; max translate X 24px at 0.3s. Latin display 900w: max Y 50px at 0.3s. Below these limits, stroke density creates unreadable motion blur. Minimum clean hold: 2.0s on data panels, 1.5s on Pentagram type displays.
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
- **Letter-spacing (Latin):** Display serif 72–100px 400w: 0.00 to +0.02em — intentionally open; this is a school signature, not an optical error. Small-caps labels 18–20px: +0.10–0.14em. Body 32–38px: 0.00em.
- **Letter-spacing (CJK):** If CJK appears in this school (rare), display 72–100px 400w: −0.01em (CJK density requires tightening even when the Latin version is open). Support: 0.00em. Never open-track CJK display in this school.
- **Mixed-script lines:** Avoid where possible in Editorial/Minimalist — the visual density contrast is too high. If unavoidable, set CJK at display scale and Latin as a small-caps label in a separate line.
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
- **Motion safety limits:** Opacity-only preferred (0px translation). If translation used: max Y 12px — the school's constraint makes any larger offset read as wrong. CJK in this school: opacity-only strictly. Minimum clean hold: 3.0s (Aesop/MUJI), 2.5s (Apple HIG).
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
**Video register: Kinetic Brand / Generative**

### Named Anchors
- **Field.io** — generative type sequences, particle systems, design as motion system
- **Active Theory** — cinematic WebGL, camera moves through 3D space, single maximum impact moment
- **Resn** — narrative-driven interaction, scroll-as-camera, story as visual event

### Web Recipes to Reference
- `field-io.md` — generative hue cycles, long-tail eases, full-state transforms, variable font axes
- `active-theory.md` — full-screen hero scene, physics-driven particles, single dramatic payoff
- `resn-storytelling.md` — narrative arc, single payoff frame, sound integrated from scene start

### Palette (video-optimized, 1280×720)
| Role | Hex | Note |
|---|---|---|
| Background | `#08080C` | Near-black with subtle blue cast; not pure black |
| Generative primary | `#0CE0E5` | Deep cyan — one of the two generative anchor hues |
| Generative secondary | `#5B2EFF` | Electric violet — the other anchor hue |
| Type on dark | `#FFFFFF` | High-contrast white; type must survive any generative background |
| Secondary type | `#A0A4B0` | Cool gray for secondary labels |
| Particle trace | procedural | Hue-rotated from the two generative anchors; not a fixed hex |

- **Note:** The palette is a starting state. The generative system cycles hue, value, and saturation through the motion sequence. The hex values above are the anchors the cycle begins from, not a fixed frame palette.

### Typography (1280×720 px)
| Role | Family | Weight / Axes | Size at 720p | Size at 4K |
|---|---|---|---|---|
| Display (variable) | Söhne Variable / Editorial New Variable / Recursive | morph wght 300→900 during sequence | 80–140px | 220–400px |
| Body | single neutral grotesque | 400 | 28–34px | 80–96px |
| Label | same as body | 400 | 18–22px | 52–64px |

- **Variable axes:** Use GSAP to animate `wght`, `wdth`, or `opsz` axes. The type morphing is the motion — not a decoration on top of it.
- **Weight arc:** 300 at particle/dissolve state → 900 at resolve/lockup. The resolve is the visual payoff.
- **Letter-spacing (Latin):** Condensed/variable at 96px+ 900w: −0.05 to −0.08em (extreme compression is the school voice). Variable font: tracking controlled by `font-variation-settings`. Standard display: −0.03 to −0.05em.
- **Letter-spacing (CJK):** −0.04em at display size (match Latin compression energy). Video modifier −0.01em always applied. CJK must look as compressed as Latin in this school — never open-track.
- **Mixed-script lines:** Full compression on both scripts. Latin and CJK should appear equally dense. Latin +5% size for optical equalization.
- **Forbidden:** Static serif type. Bold-only grotesque without variable axis. Inter at default weight. Long body text passages.

### Composition
- **Grid:** Irregular and intentional. Content lands in unexpected positions. The grid appears and disappears as part of the motion system.
- **Hero element:** The entire frame is the hero during the generative phase. The final resolve frame centers type or product for the lockup.
- **Focal points:** Shifts during the sequence — 0 fixed focal points in the generative phase (distributed attention), 1 strong focal point at the lockup.
- **Negative space:** Variable — generative phase may fill the frame; lockup returns to strong negative space.
- **Edge anchoring:** Particles and type may bleed past safe area during the generative phase. The lockup must respect safe areas.

### Motion Posture
- **Entrance:** Particle field resolves into type — letters coalesce from distributed points over 1.5–2.5s. Or: full-canvas color/light state changes over 0.8–1.2s.
- **Hold:** Generative phase: no hold — continuous transformation. Lockup: 2.0–3.0s strong hold.
- **Transition:** Full-state transform — the entire canvas state changes at once. No wipes or fades between generative phases.
- **Energy level:** 9/10 — the highest-energy school. Motion is never decorative; it is the primary content.
- **GSAP eases:** `cubic-bezier(0.83, 0, 0.17, 1)` for long-tail generative curves. `expo.out` for type resolve. `power4.inOut` for full-state transforms. `elastic.out(1, 0.3)` for physics-driven entries.
- **Motion safety limits:** This school intentionally pushes boundaries but text must resolve. CJK 900w display: max Y 30px at 0.3s (dense strokes + fast motion = blur at any larger offset). Latin 900w condensed: max Y 50px at 0.3s. Variable font axis animation: ensure text is fully legible at every intermediate state — test freeze-frames during morphing. Minimum legible hold: 1.5s even in fast-paced Experimental clips.
- **Key forbidden motion:** PPT-style individual element fade-ins with stagger. Static feature cards appearing one at a time. Anything that looks like a SaaS demo. The system must feel alive at all times.

### Sonic Character
- **Material metaphor:** Electric field and synthesized air. The sound of energy becoming form.
- **Transient shape:** Synthetic transient with a processed tail — attack 10–30ms, tail 300–800ms processed through reverb or granular. Not organic, not mechanical.
- **Density:** Dense during the generative phase — continuous low texture bed with punctuation events. Sparse at the lockup — one strong resolve hit, then silence.
- **Bed:** Low granular or spectral texture bed throughout the generative phase, 6–10dB below the peak transients. This school requires a music or texture bed; silence in the generative phase feels broken.
- **Forbidden sounds:** Acoustic instruments in the generative phase. Warm organic sounds. Paper, cloth, wood. Hard dry hits with no tail. SaaS UI clicks.

### Best For
Brand films and launch moments for creative studios or agencies, entertainment product trailers, AR/VR product launches, festival title sequences, anything where the visual experience of watching the clip is itself the product being sold.

### Forbidden Elements
- Static layouts that reveal sequentially
- Any scene that could be paused and mistaken for a slide deck
- Warm or organic color palette (chamois, amber, paper) anywhere
- Serif body type
- Long text passages that require reading — this school is for witnessing, not reading

### Anti-Slop Check
- **Generic AI output would:** Add a particle system as a background effect behind text cards, apply a glowing cyan aura to the product name, use a slow parallax scroll, call it "cinematic."
- **This school does instead:** The particles *are* the type — letters literally coalesce from a distributed generative field over 2 seconds, the variable font morphs from weight 300 to 900 as it resolves, color cycles from electric violet to deep cyan through the sequence, and the lockup is a held silence with a single processed synthetic hit at full resolve.

---

## School 4 — Brutalist / Raw
**Video register: Brand Drop / Poster Motion**

### Named Anchors
- **Bloomberg Businessweek (Turley/Ma era)** — typographic violence, magazine grid abused, copy-as-image
- **Are.na (Honest Web)** — system fonts weaponized, content over chrome, honest web in poster form
- **Balenciaga post-2017** — default browser styling as luxury signal, Helvetica at absurd scale

### Web Recipes to Reference
- `bloomberg-businessweek-turley.md` — aggressive palette, oversized grotesque at bleed scale, grid-breaking
- `are-na.md` — system typography, flat white ground, zero decoration, content-dense
- `balenciaga-post-2017.md` — Helvetica only, all-caps, zero motion, anti-luxury luxury

### Palette (video-optimized, 1280×720)
| Role | Hex | Note |
|---|---|---|
| Ground | `#FFFFFF` | Pure white — the most honest background in this school |
| Ground (dark) | `#000000` | Pure black — maximum contrast, equal honesty |
| Ink | `#000000` | Dead black; no warm or cool cast |
| Signal orange | `#FF3D00` | Businessweek high-alert; hero color block under type |
| Signal yellow | `#FFE800` | Businessweek signal; color block or type overlay |
| Blueprint blue | `#001AFF` | Businessweek alert blue |
| Off-white surface | `#F5F4F0` | Balenciaga mode — dead-toned aesthetic |
| Rule: | — | Never more than 3 colors per frame. One color block + black + white. The block is the whole concept. |

### Typography (1280×720 px)
| Role | Family | Weight | Size at 720p | Size at 4K |
|---|---|---|---|---|
| Display (Businessweek) | Founders Grotesk / Druk / ABC Whyte / Druk Wide | 800–900 | 120–200px (bleed past frame) | 340–560px |
| Display (Balenciaga) | Helvetica Now / Arial | 400–700, all-caps | 100–160px | 280–450px |
| Display (Are.na) | system serif (Georgia / Times) | 400 | 64–88px | 180–240px |
| Body | small serif contrast | 400 | 20–26px | 56–72px |
| Caption | same as body, italic | 400 italic | 16–20px | 46–56px |

- **Scale rule:** Headlines set so large they bleed past the safe area by 10–20%. Letters touching the frame edge. This is the signature move.
- **Weight contrast:** Maximum in Businessweek (900 display vs 400 body). None in Balenciaga (one weight only). Are.na uses no weight contrast at all.
- **Letter-spacing (Latin):** Display 130px+ 900w: −0.03 to −0.05em. Never open-track in Brutalist — tightness amplifies the aggressive mass. Body (if present, system font): 0.00em.
- **Letter-spacing (CJK):** Display 130px+ 900w: −0.04em (−0.05em with video modifier). The brutalist mass is achieved through scale, not open spacing. CJK density at this weight + size IS the brutalist material.
- **Mixed-script lines:** Use scale contrast as the mixer — massive CJK at 160px, Latin at 24px system font. Never mix scripts at the same visual weight in Brutalist.
- **Forbidden:** Multiple type families. Custom display fonts in Balenciaga mode (Helvetica/Arial only). Gradient text. Elegant serifs.

### Composition
- **Grid:** Deliberately broken. Content pushed off-grid, sometimes touching or overflowing edges.
- **Hero element:** The headline is the hero. No product photography competing with type. Photography, if present, is a silhouetted cutout on a color field, awkwardly cropped on purpose.
- **Focal points:** 1 — the oversized type or the color block. Everything else recedes.
- **Negative space:** Near zero in Businessweek (type fills the frame). Extreme in Balenciaga (vast empty white around one centered word). Never a comfortable middle.
- **Edge anchoring:** Left-aligned hard against the frame edge. No centering except Balenciaga dead-center lockup.

### Motion Posture
- **Entrance:** Slam-cut to position — type appears in 0–1 frames with no ease. Or: type drops from above in 0.15s, `power4.in` — fast in, instant stop, no bounce.
- **Hold:** Uncomfortably long — 2.5–5.0s on single frames. The discomfort is the design.
- **Transition:** Hard cut. No fades, no wipes, no transitions. The cut is the motion.
- **Energy level:** 7/10 — high energy through aggression and uncomfortable silence, not through speed.
- **GSAP eases:** `power4.in` for type drops. `steps(1)` for instant state flips. `linear` for any ticker-style movement. Never `sine`, `back`, `elastic`.
- **Motion safety limits:** Hard cuts have zero motion blur issue. For the rare slides: CJK 900w at 160px — max X translate 0 (slam cuts only); Y translate acceptable at 60px only if duration is 0.1s or less (snap, not slide). Latin 900w: max Y 60px at 0.1s snap. The motion should feel violent, not sweeping. Minimum hold after slam: 1.5s confrontational hold — the viewer must feel uncomfortable, not confused.
- **Key forbidden motion:** Any smooth ease that softens the impact. Particle systems. Gradient transitions between states. Any motion describable as "elegant" or "refined."

### Sonic Character
- **Material metaphor:** Print and paper — the sound of offset printing, vinyl, and physical media.
- **Transient shape:** Dry thud and print stamp. Hard attack, minimal sustain, instant decay. Like a rubber stamp landing on paper.
- **Density:** Sparse but hard — one strong impact per cut, silence in the holds.
- **Bed:** Vinyl noise or low print-room ambience at -24dBFS. Silence is equally valid.
- **Forbidden sounds:** Cinematic swells, airy whooshes, SaaS UI sounds, organic warmth, anything that would suit School 2 or School 5.

### Best For
Fashion brand drop videos, editorial title sequences, counter-culture product launches, campaign films for brands that want to feel like they do not care whether you like them, poster-style typographic announcements.

### Forbidden Elements
- Smooth motion of any kind
- More than 3 colors per frame
- Rounded corners or soft UI affordances
- Warm or organic color palette
- Photography as atmosphere or background texture
- Any design element describable as "refined," "tasteful," or "polished"

### Anti-Slop Check
- **Generic AI output would:** Use a dark background with glowing white type, add a slow reveal animation, apply a subtle gradient, call it "editorial bold."
- **This school does instead:** Sets a single word in Druk 900 at 180px, pure black on flat signal orange `#FF3D00`, bleeds the text past the top and bottom of the frame, cuts to a white frame in 0 frames, holds for 4 seconds. No glow. No reveal. No gradient. The violence of the cut is the motion design.

---

## School 5 — Warm Humanist
**Video register: Inspirational / Lifestyle / Educational**

### Named Anchors
- **Mailchimp (Freddie era, c.2018–2022)** — hand-drawn illustration, warm yellow, personality in microcopy
- **Stripe Press** — books as objects, cream and ink, warm editorial photography, foil-stamp accent
- **Headspace / Calm** — soft pastels, breathing animation, rounded everything, gentle guidance

### Web Recipes to Reference
- `mailchimp-freddie.md` — yellow brand, hand-drawn illustration, pill buttons with black outline, warm microcopy
- `stripe-press.md` — bone ground, wide-set serif italic, book-object photography, foil-stamp accent color
- `headspace-meditation.md` — warm peach ground, rounded forms, breathing animation, muted rotating accents

### Palette (video-optimized, 1280×720)
| Role | Hex | Note |
|---|---|---|
| Background (Mailchimp hero) | `#FFE01B` | Mailchimp yellow — full frame hero moment only |
| Background (Stripe Press) | `#F1ECDE` | Warm bone — paper of a well-made book |
| Background (Headspace) | `#FFE2C5` | Warm peach — morning light |
| Body surface | `#FFFFFF` | Clean white for content sections away from the hero |
| Ink (Mailchimp) | `#241C15` | Warmer than standard black |
| Ink (Stripe Press) | `#1A1A18` | Very warm near-black for editorial serif body |
| Dark teal (Headspace) | `#1B3A47` | Calming authority color |
| Secondary | `#88837C` | Warm gray for captions and metadata |
| Coral accent | `#FF4D74` | Mailchimp pop — very sparingly, one use per scene max |
| Foil teal (Stripe Press) | `#1B4B5A` | Book-specific; never as fill |
| Foil sienna (Stripe Press) | `#A04A2A` | Book-specific; never as fill |
| Lavender (Headspace) | `#B0A5D1` | Muted rotating accent — one per scene |

### Typography (1280×720 px)
| Role | Family | Weight | Size at 720p | Size at 4K |
|---|---|---|---|---|
| Display (Mailchimp) | Helvetica Now Display / Söhne / Inter Tight | 700–800 | 72–100px | 200–280px |
| Display (Stripe Press) | GT Sectra / Domaine Display | 400–500, wide italic | 72–96px | 200–270px |
| Display (Headspace) | Apercu / GT America Rounded | 600 | 64–88px | 180–240px |
| Body | same family as display | 400 | 32–38px | 88–108px |
| Script accent (Mailchimp) | Caveat / a single handwritten face | 400 | 36–44px sparingly | 100–120px |

- **Weight contrast:** Mailchimp: 400 (body) vs 800 (hero). Stripe Press: 400 only — size contrast only. Headspace: 400 vs 600.
- **Italic:** Wide-set italic used for Stripe Press emphasis — a key signature move of that sub-register.
- **Letter-spacing (Latin):** Display editorial serif 72–96px 400–700w: 0.00 to +0.01em — gentle and open. Humanist sans support 26–36px 400w: 0.00em. Labels 16–20px: +0.04 to +0.06em. Never tight-track in this school.
- **Letter-spacing (CJK):** Display 72–96px 400–700w: −0.01em (CJK minimum correction; resist going tighter — warmth requires some air). Support: 0.00em. Labels: +0.03em.
- **Mixed-script lines:** Latin font-size +10% for equalization. Keep both scripts at warm, uncompressed weight. Never drop CJK below 400w in Warm Humanist — weight is warmth.
- **Forbidden:** Cold sans-serif in any role for Headspace/Mailchimp. Geometric grotesque that reads as SaaS. Monospace. Condensed type.

### Composition
- **Grid:** Generous. Mailchimp allows asymmetric illustration placement — tilted, unexpected. Stripe Press is strictly left-aligned editorial. Headspace centers the mascot with generous surrounding space.
- **Hero element:** Mailchimp: hand-drawn illustration 35–50% of frame. Stripe Press: book photography 55–65% of frame. Headspace: mascot or breathing circle centered.
- **Focal points:** 2 — illustration/photo + title. Or 1 — centered character with title below.
- **Negative space:** 30–45% in Mailchimp mode, 40–55% in Stripe Press, 45–60% in Headspace. Feels like breathing room, not designed emptiness.
- **Texture:** Subtle paper grain or cloth texture at 4–8% opacity over the background is School 5's material system.

### Motion Posture
- **Entrance:** Soft opacity fade 400–600ms `sine.inOut`. Illustration may scale 0.95 → 1.0. Bouncy lift (1.04 scale with `back.out(1.6)`) on CTA or joyful Mailchimp moments only.
- **Hold:** 1.5–2.5s — warm but not uncomfortably long. The clip should feel like breathing.
- **Transition:** Crossfade 500ms or soft upward drift (4–8px translate Y) during dissolve. Never hard cut.
- **Energy level:** 4/10 for Stripe Press/Headspace. 6/10 for Mailchimp joyful moments.
- **GSAP eases:** `sine.inOut` for body motion. `back.out(1.6)` for joyful Mailchimp bounces. `power1.out` for Stripe Press book reveals. Never `power4`, `expo`, or hard spring physics.
- **Motion safety limits:** Bouncy motion (`back.out(1.2)`) is allowed for illustration elements only, not text. Text animations: max Y 36px at 0.4s `power2.out`. CJK display 72–96px: max Y 36px at 0.4s. Minimum clean hold: 2.0s on inspirational claims, 1.5s on supporting statements. Do not rush emotional content.
- **Key forbidden motion:** Hard cuts. Slam-cuts. High-energy kinetic type. Particle systems. Anything urgent, aggressive, or cold.

### Sonic Character
- **Material metaphor:** Soft organic — paper pages, warm room air, a human voice in a quiet space.
- **Transient shape:** Soft swell — attack 80–120ms, warm tail 400–800ms. Rounded, never sharp.
- **Density:** Sparse to medium — 2–4 cues per 10 seconds. Space between cues should feel like a held breath.
- **Bed:** Warm low string pad or soft piano at -20dBFS. Or airy room tone. Always quiet under narration.
- **Forbidden sounds:** Hard impacts, digital whooshes, broadcast snaps, cold synthetic textures, SaaS UI clicks, mechanical locks.

### Best For
Educational explainer videos, community brand films, creator tool launches, wellness product onboarding, nonprofit campaigns, founder story films, anything where the viewer needs to feel the brand is on their side rather than selling at them.

### Forbidden Elements
- Cold palette (blues, cyans, purples unless Headspace warm dark teal)
- Aggressive or hard motion
- Monospaced or condensed type
- Dense data or feature card grids
- Any motion describable as "hard," "precise," or "technical"

### Anti-Slop Check
- **Generic AI output would:** Use a white background, add a soft motivational whoosh, set the headline in Poppins 700, add a slow left-to-right wipe, paste a stock illustration from a library.
- **This school does instead:** Floods the hero frame with Mailchimp yellow `#FFE01B`, places a hand-drawn illustration tilted 6° off-axis at 45% frame width, sets the headline in Inter Tight 800 with a 3px black outline on the pill CTA, uses a single warm organic soft-swell on the hero reveal, and holds for 2 seconds before the next beat — confident enough to be still.

---

## School 6 — Modern Tool / Builder SaaS
**Video register: Product Demo / Technical**

### Named Anchors
- **Linear** — warm dark, hairline detail, restraint as confidence, developer-tool premium
- **Vercel** — pure black canvas, product as hero, deployment as dramatic event
- **Raycast** — glassy command-palette aesthetic, per-extension color, keyboard-first culture
- **Notion (pre-AI era)** — structured block hierarchy, editorial breathing room, product as workspace

### Web Recipes to Reference
- `linear.md` — warm near-black ground, hairline borders `rgba(255,255,255,0.06)`, purple accent <5%, snappy ease
- `raycast.md` — glass palette floating card, shortcut chips, extension color dots, spring on hero
- `notion-pre-ai.md` — block structure, neutral ground, product behavior as the visual event
- `vercel-mesh.md` — pure black, white type, deployment as the dramatic narrative

### Palette (video-optimized, 1280×720)
| Role | Hex | Note |
|---|---|---|
| Background (Linear) | `#08090A` | Near-black with warm undertone — not pure black |
| Background (Raycast) | `#0F0F11` | Charcoal with hint of blue |
| Background (Vercel) | `#000000` | Pure black — the one case where pure black is correct |
| Background (Notion) | `#F7F6F3` | Slightly warm white |
| Surface 1 | `#16171C` | First raised surface — panel backgrounds |
| Surface 2 | `#1E1F25` | Second raised surface — card backgrounds |
| Surface raised | `#26272E` | Highest surface — modal or active state |
| Hairline border | `rgba(255,255,255,0.06)` | The Linear signature — faint, precise, everywhere |
| Primary text | `#F7F8F8` | Near-white |
| Secondary text | `#9CA3AF` | Cool gray |
| Muted text / chips | `#6B7280` | Keyboard shortcut chips, metadata |
| Accent (Linear) | `#5E6AD2` | Linear purple — <5% of frame pixels; never as background |
| Accent (Raycast) | `#FF6363` | Raycast red — on icons and key CTAs only |
| Extension colors | per-tile | Lime `#84CC16`, coral `#FB923C`, lavender `#A78BFA`, cyan `#22D3EE` — small dots only |
| Forbidden | — | Purple-pink-blue gradient as background, cyan glow as atmosphere, warm cream (School 5's territory) |

### Typography (1280×720 px)
| Role | Family | Weight | Size at 720p | Size at 4K |
|---|---|---|---|---|
| Display | Inter Tight / Söhne / Geist Sans | 600 | 72–100px | 200–280px |
| Body | Inter / Geist Sans | 400–500 | 28–32px | 80–88px |
| Mono (code, shortcuts) | GeistMono / JetBrains Mono / Berkeley Mono | 400–500 | 22–26px | 64–72px |
| Label | Inter | 400 | 18–20px | 52–58px |

- **Weight contrast:** 400 (body) vs 600 (display). Never heavier than 700. Confidence through precision, not through weight.
- **Letter-spacing (Latin):** Display humanist sans 80–110px 700w: −0.02 to −0.03em. Support 26–36px 400w: 0.00em. Mono data labels 20–26px: 0.00em (tabular, no exception). Uppercase UI chips 11–13px: +0.08em.
- **Letter-spacing (CJK):** Display 80–110px 700–900w: −0.03em (−0.04em with video modifier). Support 26–36px 400w: 0.00em. Mixed Chinese+Mono label rows: CJK at 0.00em, Mono at 0.00em — let character contrast do the visual work.
- **Mixed-script lines:** This school most commonly mixes CJK + Latin + Mono in the same line. Apply: Latin font-size +9%, Mono at same size as Latin, CJK as base. Example: `创作引擎 · STUDIO` → CJK 28px, Latin 30.5px (+9%), Mono 28px.
- **Keyboard chips:** Mono font, `rgba(255,255,255,0.06)` dim background, 1px hairline border `rgba(255,255,255,0.10)`, 18–22px at 720p.
- **Forbidden:** Arial, Roboto, Open Sans. Serif in any role. Gradient text. Condensed grotesque.

### Composition
- **Grid:** 12-column, 24–32px gutters. Precise — the grid is visible through the panel structure.
- **Hero element:** The actual product UI is the hero — a floating command palette (Raycast), a deployment log (Vercel), an issue board (Linear). UI occupies 55–70% of frame and is large enough to read at video resolution.
- **Focal points:** 2 — product UI + headline or product UI + metric.
- **Negative space:** 20–35%. Less than other schools — the product needs to be visible and legible.
- **Edge anchoring:** Product UI centered or right-anchored. Headline top-left or bottom-left. Keyboard shortcuts visible inside the product UI frame.
- **Panel depth:** Use the surface layer system (Background → Surface 1 → Surface 2 → Surface raised) to create apparent depth without shadows or glows.

### Motion Posture
- **Entrance:** Snappy `cubic-bezier(0.22, 1, 0.36, 1)` at 350–450ms for layout reveals. 150ms `power2.out` for micro-feedback on UI elements. The product UI should perform a visible action every beat.
- **Product behavior loop:** UI state changes are the hero motion — a new issue appears, a deployment completes, a command executes. The transition is the product working.
- **Hold:** 1.0–2.0s per beat. Shorter than other schools — product demo clips are information-dense.
- **Transition:** Product behavior loop as transition. Or precise mask 200ms. No crossfades except Notion mode.
- **Energy level:** 6/10 — confident and precise, not aggressive, not slow.
- **GSAP eases:** `cubic-bezier(0.22, 1, 0.36, 1)` (the Linear ease) for layout moves. `power2.out` for micro-feedback. `back.out(1.6)` only for Raycast glass palette appearing (spring is Raycast's brand). `steps(1)` for instant UI state changes. Never `sine.inOut` (too slow), never `elastic` (too bouncy).
- **Motion safety limits:** `power3.out` entrance Y 24–36px at 0.3–0.4s — within safe zone for all text sizes used. Mono/data snap entrances: max Y 16px at 0.2s `power4.out`. CJK display 80–110px: max Y 36px at 0.35s — exactly at safe boundary; do not exceed. UI panel assembly X movements: max X 24px at 0.25s. Minimum clean hold: 1.8s on feature claims, 0.8s on each task list item reveal.
- **Key forbidden motion:** Particle systems. Generative effects. Long slow fades. Gradient transitions. Camera zoom applied to the text container. Anything making the UI unreadable during the reveal.

### Sonic Character
- **Material metaphor:** Precision digital — the sound of a well-engineered machine.
- **Transient shape:** Clean digital click with a short controlled tail. Attack <10ms, tail 40–80ms. Precise, not harsh.
- **Density:** Medium — one UI click per significant product action, one precise whoosh per layout transition, one impact per major reveal. No more than 1 cue per 0.8s of active motion.
- **Bed:** Very low digital texture at -28dBFS or none. Product sounds lead.
- **Forbidden sounds:** Organic textures (paper, cloth, breath). Cinematic swells. Hard poster stamp impacts. Warm risers. Any sound that would suit School 2 or School 5.

### Best For
Product demo clips, onboarding films, feature launch videos, changelog animations, developer tool brand films, B2B SaaS ads where showing the product working is more convincing than characterizing the brand.

### Forbidden Elements
- Organic or warm visual textures (chamois, paper grain, cloth)
- Serif type in any role
- Bold weights above 700
- Gradient fills on background or type
- Photography of people as hero elements (Linear rule)
- Long meditative holds (>2.5s) without product activity
- Any decoration removable without changing information density

### Anti-Slop Check
- **Generic AI output would:** Use a dark background with glowing cyan accent, set the product screenshot at 40% opacity as an atmosphere layer, add a slow pan across the UI, apply gradient text to the product name.
- **This school does instead:** Grounds the frame on `#08090A` warm near-black, places the actual product UI at 65% of frame width in a sharp Surface 1 panel (`#16171C`) with 1px hairline borders (`rgba(255,255,255,0.06)`), snaps the UI state from empty to populated in 350ms with `cubic-bezier(0.22, 1, 0.36, 1)`, plays a clean UI click at -16dBFS on each item's appearance, and holds the populated state for 1.5s before the next beat. The product is the visual. The motion is the product working.

---

## School Selection Decision Tree

```
Is there a named anchor (designer/studio/brand) in the brief?
  YES → Map directly to school. Load that recipe file.
  NO ↓

Does the clip carry 5+ data points, charts, or metrics?
  YES → School 1 (Information Architecture)
  NO ↓

Is the product a developer tool, command palette, or B2B SaaS?
  YES → School 6 (Modern Tool / Builder SaaS)
  NO ↓

Is the clip for a creative studio, agency, or brand launch moment?
  YES → School 3 (Motion / Experimental)
  NO ↓

Is the brand in fashion, counter-culture, or anti-luxury luxury?
  YES → School 4 (Brutalist / Raw)
  NO ↓

Is the primary register warm, human, educational, or lifestyle?
  YES → School 5 (Warm Humanist)
  NO ↓

Is the product high-consideration, premium, or requires restraint?
  YES → School 2 (Editorial / Minimalist)
  NO → Return to director and ask for named anchor or more context.
```

---

## Cross-Reference: Web Recipe → School → Video Register

| Web recipe file | School | Video register |
|---|---|---|
| `pentagram.md` | 1 — Information Architecture | Data Authority / Broadcast |
| `tufte-dataink.md` | 1 — Information Architecture | Data Authority / Broadcast |
| `bloomberg-terminal.md` | 1 — Information Architecture | Data Authority / Broadcast |
| `vignelli-swiss-helvetica.md` | 1 — Information Architecture | Data Authority / Broadcast |
| `nyt-the-daily.md` | 1 — Information Architecture | Data Authority / Broadcast |
| `muji-kenya-hara.md` | 2 — Editorial / Minimalist | Premium Launch / Quiet Luxury |
| `apple-hig.md` | 2 — Editorial / Minimalist | Premium Launch / Quiet Luxury |
| `aesop.md` | 2 — Editorial / Minimalist | Premium Launch / Quiet Luxury |
| `dieter-rams-braun.md` | 2 — Editorial / Minimalist | Premium Launch / Quiet Luxury |
| `monocle-magazine.md` | 2 — Editorial / Minimalist | Premium Launch / Quiet Luxury |
| `field-io.md` | 3 — Motion / Experimental | Kinetic Brand / Generative |
| `active-theory.md` | 3 — Motion / Experimental | Kinetic Brand / Generative |
| `resn-storytelling.md` | 3 — Motion / Experimental | Kinetic Brand / Generative |
| `are-na.md` | 4 — Brutalist / Raw | Brand Drop / Poster Motion |
| `bloomberg-businessweek-turley.md` | 4 — Brutalist / Raw | Brand Drop / Poster Motion |
| `balenciaga-post-2017.md` | 4 — Brutalist / Raw | Brand Drop / Poster Motion |
| `mailchimp-freddie.md` | 5 — Warm Humanist | Inspirational / Lifestyle / Educational |
| `stripe-press.md` | 5 — Warm Humanist | Inspirational / Lifestyle / Educational |
| `headspace-meditation.md` | 5 — Warm Humanist | Inspirational / Lifestyle / Educational |
| `linear.md` | 6 — Modern Tool / Builder SaaS | Product Demo / Technical |
| `vercel-mesh.md` | 6 — Modern Tool / Builder SaaS | Product Demo / Technical |
| `raycast.md` | 6 — Modern Tool / Builder SaaS | Product Demo / Technical |
| `notion-pre-ai.md` | 6 — Modern Tool / Builder SaaS | Product Demo / Technical |
| `mid-century-modern.md` | 2 or 5 — depends on warmth | Premium Launch or Lifestyle |
| `y2k-retrofuturism.md` | 3 or 4 — depends on aggression | Kinetic Brand or Brand Drop |
