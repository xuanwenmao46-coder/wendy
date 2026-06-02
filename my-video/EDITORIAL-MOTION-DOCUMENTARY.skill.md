# Editorial Motion Documentary Skill

---

```yaml
name: editorial-motion-documentary
description: >
  Use when the goal is a premium editorial investigative video — VOX × Bloomberg × NYT × 
  Pentagram visual language. Covers the complete pipeline from narrative architecture through 
  HyperFrames implementation, motion design, audio system, and final render. Trigger when the 
  user wants a data-driven story that feels like a magazine investigation, not an infographic 
  presentation. Do NOT use for brand ads, product demos, or TTS explainer podcasts.
category: Editorial Video Design
version: 1.0.0
effort: high
```

---

## What This Skill Produces

A self-contained investigative documentary short (45–90s) that feels like a printed premium 
magazine being read in real time. Every frozen frame passes the **Print Test**: if paused and 
exported as a JPEG, it must look like a publishable editorial spread — not a presentation slide.

**Reference targets**: The Social Dilemma · Vox Explained · Apple Event Intro · 
Bloomberg Quicktake · NYT Visual Journalism · Pentagram Motion · Buck · Ordinary Folk

---

## Part 1 — Narrative Architecture

### The Investigative Arc (mandatory)

Never use the data → chart → conclusion structure. Always use:

```
Investigation → Find clues → Find people → Find evidence → Find truth → Conclusion
```

Emotional curve locked to this order:

```
Curiosity → Investigation → Discovery → Suspicion → Confirmation → Shock → Reflection
```

### Shot Intention Rule

Every shot has ONE primary objective. Choose from:

| Objective | Description |
|-----------|-------------|
| Raise a question | No answers given, only suspicion created |
| Present evidence | One piece of credibility-building material |
| Introduce a person | Human connection, emotional entry point |
| Reveal data | A number discovered inside a document, not floating |
| Build tension | Density increases, convergence begins |
| Deliver conclusion | The cost, the truth, the scale |
| Provoke reflection | Remove everything, leave the audience alone |

If a shot tries to do two objectives simultaneously — split it into two shots.

### Chapter Template (8 chapters, ~68–90s)

| Chapter | Time | Purpose | Emotion |
|---------|------|---------|---------|
| 01 · THE INVESTIGATION | 0–8s | Raise suspicion. No answers. | Curiosity |
| 02 · EVIDENCE BOARD | 8–18s | Build credibility through accumulation | Investigation |
| 03 · ONE PERSON | 18–28s | Human connection, time fragmentation | Discovery |
| 04 · THE DISCOVERY | 28–38s | Data embedded in documents, not floating | Suspicion |
| 05 · ESCALATION | 38–50s | Information density peaks, everything converging | Confirmation |
| 06 · THE COST | 50–60s | Impact. One number. One moment. | Shock |
| 07 · COLLAPSE | 60–67s | All complexity stripped. One concept remains. | Compression |
| 08 · ENDING | 67–72s | Silence. One question. | Reflection |

Adjust chapter count and timing to content, but maintain the arc order.

---

## Part 2 — Visual Design System

### Palette (locked, no exceptions)

```
Background:   #ffffff  (pure white — the paper)
Primary text: #000000  (black — ink)
Secondary:    #555555  (gray — captions, sources, metadata)
Accent:       #cc0000  (red — annotation circles, underlines, stamps ONLY)
Dark chapter: #0a0a0a  (near-black — used ONLY for CH01 archive atmosphere)
```

Forbidden colors: neon, blue gradients, purple, cyan, gold, any glow.

### Typography

```
Font stack:  'Helvetica Neue', Helvetica, Arial, sans-serif
Courier New: timestamps, research codes, data values (monospace credibility)
```

Weight contrast is the primary typographic tool:

| Role | Weight | Size (1080p) |
|------|--------|--------------|
| Masthead / investigation label | 400 tracked | 10–12px |
| Section headline | 800 | 52–80px |
| Hero title | 800 | 96–140px |
| Data revelation | 800 | 200–280px |
| Body / quote | 400–700 | 13–28px |
| Caption / source | 300–400 tracked | 9–12px |
| Archive codes | 400 mono | 9–11px |

### Paper Texture (always active)

```css
body {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' 
    width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' 
    baseFrequency='0.75' numOctaves='4' stitchTiles='stitch'/%3E%3CfeColorMatrix 
    type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='300' height='300' 
    filter='url(%23n)' opacity='0.025'/%3E%3C/svg%3E");
}
```

### Photo Treatment (CSS-only, no real images needed)

```css
.photo-halftone {
  background:
    repeating-linear-gradient(0deg, #000 0, #000 1px, transparent 1px, transparent 5px),
    repeating-linear-gradient(90deg, #000 0, #000 1px, transparent 1px, transparent 5px);
  background-color: #bbb;
  filter: contrast(1.4);
}
```

### Persistent Layer (z-index 100, always visible)

Every frame contains this layer regardless of chapter:

```
Top rule:      2px black line at y=0
Masthead:      "THE [TOPIC] — AN EDITORIAL INVESTIGATION" · 10px · tracked
Bottom rule:   1px black line at y=1070px
Left margin:   1px vertical rule at x=60px
Right margin:  1px vertical rule at x=1860px
Chapter label: bottom-left · "CH.0X / CHAPTER NAME" · 11px
Archive code:  bottom-right · "REF-2024-00X" · 11px gray
```

---

## Part 3 — Frame Density Rules

### The Print Test

> If this frame were frozen and printed as a magazine page, would it look like a premium 
> editorial publication? If no — redesign it.

### Minimum Frame Layers

Every frame must contain at minimum **4 information layers**:

1. Primary content (the current chapter's main message)
2. Document context (newspaper header, research report frame, archive label)
3. Supporting annotation (source citation, page number, FIG reference)
4. Background texture layer (paper, faded newspaper column, watermark)

### No Isolated Numbers Rule

**Wrong:**
```
127
```

**Correct:**
```
FIG. 04-A
─────────────────────────────────────────
Average daily phone checks: 127 TIMES
─────────────────────────────────────────
"Participants checked devices 127.3 times/day..."
Source: Stanford Digital Wellness Study, 2024 · N=12,400
```

All data lives inside: research reports · newspaper layouts · interview transcripts · 
document cards. Never floats independently on empty backgrounds.

### No Standalone Charts Rule

Charts must live INSIDE a newspaper, report, or document. A ring chart on a white background 
is a PowerPoint. A ring chart inside an ATTENTION REPORT document page is editorial.

---

## Part 4 — The ATTENTION Motif System

Use for any concept with a central keyword that the investigation is really about.

### Integration Method (NOT decoration)

The keyword must appear **naturally within content** — never as decorative repetition.

Correct integration points:
- Newspaper headline: `ATTENTION ECONOMY REACHES $4.1 TRILLION`
- Research paper title: `ATTENTION RESEARCH QUARTERLY — Vol 8`
- Interview transcript: `"We designed for ATTENTION CAPTURE. Everything else was secondary."`
- Advertisement copy: `BUY ATTENTION MARKET REACH — 2.4B DAILY IMPRESSIONS`
- Report section: `ATTENTION LOSS STUDY — Case 07`
- Archive label: `ATTENTION REPORT / ATTENTION STUDY REF 004`

### Frequency Escalation

The keyword should appear with increasing frequency across chapters:

```
CH01:  1×  (hidden, document tag)
CH02:  3×  (stamps, small labels)
CH03:  4×  (annotations)
CH04:  5×  (embedded in report headers)
CH05:  8×  (across all 5 media zones)
CH06:  background at 5% opacity
CH07:  62× (3 waves: 12 → 20 → 30 instances)
CH08:  0   (everything stripped — silence)
```

### The Flood (CH07)

The keyword tiles the full canvas in 3 waves, each with escalating density and smaller type sizes. 
At peak: entire screen is covered. All text simultaneously turns `#c00`. Then instant disappearance.

This is the emotional climax. The audience should feel overwhelmed, then relieved by the silence.

---

## Part 5 — Motion Language

### Paper Physics (only allowed motion system)

All movements must feel physically connected to paper and print:

| Motion type | GSAP implementation |
|-------------|---------------------|
| Document arrival | `y: -25, rotation: ±3deg → 0, back.out(1.4), 0.45s` |
| Paper settle (after chaos) | `x: chaosOffset, rotation: ±20deg → final, back.out(1.6), 0.7s` |
| Annotation reveal | `strokeDashoffset: pathLength → 0, power2.inOut, 0.8s` |
| Highlight wipe | `scaleX: 0 → 1, transformOrigin: left, 0.4s` |
| Paper exit | `y: 0 → -60, opacity: 1 → 0, power2.in, 0.4s` |
| Micro-breathing | `rotation: ±0.4deg, sine.inOut, yoyo, repeat` |
| Text skew entrance | `x: -40, skewX: -4 → 0, power3.out, 0.55s` |
| 3D document slide | `x: 120, rotationY: 8 → 0, power3.out, 0.6s` |

### Chaos → Order (Evidence Board pattern)

All documents appear simultaneously in scattered chaos positions, then each slides to its 
organized final position. This is the most memorable entrance pattern for investigation boards.

```javascript
// Phase 1 (t=0): all cards appear at offset chaos positions
cards.forEach(c => tl.set(c.id, { x: c.chaosX, y: c.chaosY, rotation: c.chaosR, opacity: 1 }, t));

// Phase 2 (t+0.4): staggered settlement to final positions
cards.forEach((c, i) => {
  tl.to(c.id, { x: 0, y: 0, rotation: c.finalRot, duration: 0.7, ease: 'back.out(1.6)' }, t + 0.4 + i * 0.3);
});
```

### Forbidden Motions

```
❌ Zoom blur / scale pop
❌ Glitch / RGB split
❌ Camera shake
❌ Flash cut (high contrast, >3Hz)
❌ Sci-fi HUD elements
❌ Neon glow
❌ Bounce / elastic easing
❌ Linear easing on any text
```

### SVG Annotation Drawing

Red circles, underlines, and connecting threads use `strokeDashoffset` for draw-on effect:

```css
.annotation-svg path {
  stroke-dasharray: 200;
  stroke-dashoffset: 200;
}
```
```javascript
tl.to('.annotation-svg path', { strokeDashoffset: 0, duration: 0.8, ease: 'power2.inOut' }, t);
```

---

## Part 6 — HyperFrames Implementation

### Project Requirements

```
Framework:    HyperFrames + GSAP
Canvas:       1920 × 1080px (16:9)
Duration:     60–90 seconds
Frame rate:   30fps
Output:       H.264, ~1–2 Mbps video + AAC 256k stereo audio
```

### Required HTML Structure

```html
<meta name="viewport" content="width=1920, height=1080" />

<div id="root" 
     data-composition-id="root" 
     data-start="0" 
     data-duration="72" 
     data-width="1920" 
     data-height="1080">

  <!-- Persistent layer: always visible, z-index 100 -->
  <div id="persist">...</div>

  <!-- Chapter containers -->
  <div id="ch01" class="scene clip" data-start="0" data-duration="8" data-track-index="10">
    ...
  </div>
  <!-- etc -->
</div>
```

### Clip Element Rules

Every timed element:
```html
<div class="clip" 
     data-start="[seconds]" 
     data-duration="[seconds]" 
     data-track-index="[unique integer]">
```

Track index must be unique across ALL elements. Organize by chapter:
- Persistent layer: 0–9
- CH01: 10–29 · CH02: 30–49 · CH03: 50–69 · CH04: 70–89
- CH05: 80–99 · CH06: 100–119 · CH07: 120–179 · CH08: 180–199

### GSAP Timeline Registration

```javascript
const tl = gsap.timeline({ paused: true });
window.__timelines = window.__timelines || {};
window.__timelines.root = tl;
```

Hard-kill every chapter container at chapter end:
```javascript
tl.set('#ch01', { opacity: 0 }, 8.0);
tl.set('#ch02', { opacity: 0 }, 18.0);
// etc
```

### Determinism Rules

```
✅ Allowed: hardcoded position arrays, LCG pseudo-random with fixed seed
❌ Forbidden: Math.random(), Date.now(), fetch(), setTimeout()
```

### Validation

After every edit, run:
```bash
cd my-video && npm run check
```

Fix ALL errors before rendering. Warnings are acceptable.

---

## Part 7 — Audio System (Three Layers)

### Architecture

```
BGM        -16dB   Minimal tech pulse. The clock moving forward.
SFX        -8dB    UI feedback. Every information event has a sound.
Transitions -10dB   Paper physics sounds. Slides, folds, scrapes.
Ambience   -20dB   Room texture. Paper and air. Barely perceptible.
```

### BGM — Minimal Tech Pulse

- **Tempo**: 80–90 BPM. Steady. No drops. No build-up to a chorus.
- **Character**: sine sub (52–60Hz) + harmonic, soft attack, quick decay
- **Reference feel**: a server rack processing. A clock. Not music — time.
- **Structure**:
  ```
  0–34s:    Normal pulse, quiet
  34–50s:   Low-pass filter closes gradually (darker, heavier)
  50–60s:   Pulse stops. Only low drone remains.
  60–67s:   Subtle tension pulse returns
  67s+:     Complete silence
  ```
- **Low drone**: continuous ~42Hz sine, gets louder 34–60s, creates physical weight
- **Forbidden**: drops, risers, cymbal swells, epic brass, future bass, trap hats

### SFX Design Per Section

| Time | Visual event | Sound | NOT |
|------|-------------|-------|-----|
| CH01 flash words | Word appears | `soft_click` 820Hz, 18ms | whoosh |
| CH01 title | Line slides in | `tok` mid-low, 85ms | impact boom |
| CH02 chaos | Cards scatter | single `paper_slide` shhk | sci-fi |
| CH02 settle | Each card lands | `soft_click` per card, panned | heavy thud |
| CH02 threads | Line draws | `paper_slide` directional | laser |
| CH02 stamps | Stamp appears | `ui_tap` 600Hz, 22ms | stamp boom |
| CH03 photo | Portrait reveals | `tok` | |
| CH03 log rows | Each row appears | `clock_tick` 1150Hz, 25ms | typewriter |
| CH04 findings | Block slides in | `digital_pulse` 68Hz, 200ms | chord hit |
| CH04 circles | Annotation draws | `ui_tap` | stamp |
| CH05 zones | Zone drops in | `tok` per zone, panned | whoosh |
| CH05 pulse | ATTENTION beats | `digital_pulse` × 4 | rise swell |
| CH06 collapse | Docs converge | soft `paper_slide` × 3 | explosion |
| CH06 9 YEARS | Number appears | `single_thump` — ONE hit | trailer boom |
| CH07 flood | Words appear | `tick_fast` rapid stagger | nothing |
| CH07 heartbeat | ATTENTION grows | `heartbeat` 72 BPM undercurrent | |
| CH08 black screen | Silence | nothing | anything |
| CH08 text appears | "Your attention..." | `piano_note` single D4, 2.8s decay | music swell |

### SFX Synthesis Reference (Pure Python, no dependencies)

Generate all sounds programmatically — no external audio files needed:

```python
import wave, math, array

SR = 44100

def soft_click():
    # 820Hz sine, 18ms, exp decay, LP filtered at 1800Hz
    n = int(0.018 * SR)
    tone = [math.sin(2*math.pi*820*i/SR) * math.exp(-160*i/SR) for i in range(n)]
    return lp1(tone, 1800)

def paper_slide(seed=9999):
    # LCG noise, 70ms, BP 2000Hz, exp decay
    ...

def single_thump():
    # Sine sweep 90→30Hz, 350ms, NO sub-bass boom
    # This is weight, not drama
    ...

def piano_note(freq=293.66):  # D4 — reflective
    # Fundamental + 2nd + 3rd harmonic, piano envelope (instant attack, 2.8s decay)
    ...
```

Key principle: **The 9 YEARS reveal gets ONE thump. Not an impact + sub + reverb. Just weight.**

### Timing Alignment

Piano note must be placed at the video timestamp when the black screen appears, 
not at the end of the video file. Calculate:

```
piano_t = part1_duration + (blackscreen_t_in_original - ending_start_in_original)
```

### Mix and Master

```python
# Soft limiter — tanh waveshaping, not hard clip
limit = 0.92
out = [math.tanh(v / limit) * limit for v in buf]
```

Output as stereo interleaved 16-bit WAV, 44100Hz, then encode to AAC 256k via FFmpeg.

---

## Part 8 — Production Pipeline

### Step 1: Narrative Brief

Write before any design:
```
Topic:
Central concept / keyword:
Emotional arc (7 stages):
Chapter count and duration:
The one question this film asks:
The one truth it reveals:
```

### Step 2: Frame Design (per chapter)

For each chapter, specify:
- Primary content element
- Document/paper wrapper (what type of publication)
- Data/annotation layer (source, FIG reference, archive code)
- Background texture layer
- Entry animation pattern
- Exit animation pattern
- ATTENTION keyword integration point

### Step 3: HTML Composition

1. Build persistent layer first
2. Add chapter containers with correct `data-start`/`data-duration`
3. Fill each chapter with 4+ information layers
4. Add all SVG annotation elements
5. Run `npm run check` — 0 errors required

### Step 4: GSAP Timeline

1. Set chapter visibility hard-kills first (`tl.set('#chXX', { opacity: 0 }, t)`)
2. Add chapter animations using absolute time position (4th argument)
3. Wire SFX calls via `tl.call(SFX.fn, [], t)`
4. Add micro-details last (breathing, cursor blink, clock tick bed)

### Step 5: Audio Generation

1. Generate BGM layer (pulse + drone + ambience)
2. Generate SFX layer (all cues at exact timestamps)
3. Mix at specified dB levels
4. Apply tanh master limiter
5. Write stereo WAV

### Step 6: Render and Splice

```bash
# Render video (no audio — Web Audio not captured by renderer)
npm run render

# Mix audio into video
ffmpeg -i render.mp4 -i sfx_track.wav -map 0:v -map 1:a \
  -c:v libx264 -crf 16 -c:a aac -b:a 256k output.mp4
```

If preserving a preferred ending from another render:
```bash
# Extract ending with frame-accurate trim filter
ffmpeg -i source.mp4 \
  -vf "trim=start=47,setpts=PTS-STARTPTS,scale=2880:1080,crop=1920:1080:480:0,setsar=1" \
  -an ending.mp4

# Add audio (-shortest prevents audio overrun)
ffmpeg -i ending.mp4 -i ending_audio.wav \
  -map 0:v -map 1:a -c:v copy -c:a aac -b:a 256k -shortest ending_with_audio.mp4

# Concatenate (force fps=30)
ffmpeg -i part1.mp4 -i part2.mp4 \
  -filter_complex "[0:v]fps=30[v0];[1:v]fps=30[v1];[v0][0:a][v1][1:a]concat=n=2:v=1:a=1[v][a]" \
  -map "[v]" -map "[a]" -c:v libx264 -c:a aac final.mp4
```

---

## Part 9 — Quality Bar

### The Print Test (run before render)

Pause the video at 5 random frames. For each frame ask:

> If this were printed in a magazine, would it look publishable?

- YES → proceed
- NO → redesign that frame before rendering

### Anti-Pattern Checklist

```
❌ Any number floating alone on empty background
❌ Any chart not inside a publication/document
❌ More than 30% of a frame is empty white space with no structural role
❌ The word ATTENTION repeated as decoration (not embedded in content)
❌ Transitions that are wipes hiding slide changes
❌ Glitch, RGB split, neon, glow, HUD elements
❌ BGM with drops, risers, or emotional highs
❌ More than ONE thump/impact sound at the data revelation moment
❌ Music continuing over the final black screen text
❌ Hard cut to ending with mismatched aspect ratio or frame rate
```

### Success Criteria

```
✅ Every frame: 4+ information layers
✅ All data: embedded in document context
✅ Motion: paper physics only
✅ ATTENTION: natural compound phrases (ATTENTION ECONOMY, not ATTENTION × 50)
✅ Audio: 3 layers, correct dB mix
✅ Piano note: timed to black screen onset
✅ Ending: frame-accurate trim, matching aspect ratio, correct fps
✅ npm run check: 0 errors
✅ Frozen frame passes Print Test
```

### Minimum Expressible Form

The finished film should be expressible as:

```
For [audience], this film uses [visual concept — investigation board / research archive]
and [motion pattern — paper physics / chaos-to-order] to make [central truth] feel
like a discovered fact, not a presented statistic.
```

---

## Part 10 — Reference Design Schools

| School | Key traits | Apply when |
|--------|-----------|-----------|
| **Bloomberg Visual** | Dense data layers, tight grid, black rule lines | Finance, economy, statistics |
| **VOX Explainer** | Large type, evidence build, strong captions | Social phenomena, behaviour |
| **NYT Visual Journalism** | Photo halftone, column layout, archive aesthetic | Human stories, investigation |
| **Swiss Editorial** | Helvetica, grid, weight contrast, no decoration | Clean authority, research |
| **Pentagram Motion** | Typographic precision, negative space as design | Concept-first, single idea |

All five schools share: **monochrome base · paper texture · information density · 
no decoration without narrative purpose**.

---

## Appendix — Chapter Design Templates

### CH01: The Investigation Begins (dark, 0–8s)

```
Background: #0a0a0a
Scanner light: white gradient sweeps left→right, 1.8s, opacity 0.05
Background fragments: newspaper text at opacity 0.15, 3 positions, various rotations
Flash sequence: 7 keywords × 0.4s each, 96px white bold, center
Title: 3 lines × 120px, white, skewX entrance stagger
Series label: small red tracked caps below title
```

### CH02: Evidence Board (white, 8–18s)

```
Background: #ffffff
6 document cards: rotations ±1–3deg, hardcoded positions
Chaos entrance: all appear simultaneously at offset positions, settle staggered 0.3s
Red threads: SVG stroke-dashoffset draw-on after cards settle
Intersection node: small SVG circle with keyword
Stamp labels: 3× small red tracked text, scattered
```

### CH03: One Person (white, 18–28s)

```
Left half: halftone photo block (CSS grid), portrait label, caption
Right half: "THE DAILY LOG" header (red), log rows (time / activity / duration)
Log rows: stagger 1.2s each, clock_tick SFX per row
Red line: draws across highlighted row (scaleX 0→1, 1.2s)
Pull quote: italic, 36px, y:20→0 entrance
Typewriter cursor: steps down with each row, opacity blink
```

### CH04: The Discovery (white, 28–38s)

```
Full-page research report aesthetic
Header: institution name + "DRAFT" + "PAGE 14"
FINDING blocks: 3 sequential, slide from right with rotationY 8→0
Each block: FINDING 0X / FIG reference / bold 48px value / quote / source
Red annotation circles: SVG draw-on after each finding appears
CONFIRMED stamp: rotated -5deg, red border, appears after FINDING 03
```

### CH07: The Flood (white, 60–67s)

```
Wave 1 (t=60–63): 12 ATTENTION compounds, hardcoded positions, sizes 14–48px
Wave 2 (t=63–65): 20 more, smaller, fills gaps
Wave 3 (t=65–67): 30 more, 8–14px, canvas nearly full
t=66.0: all text → color #c00 simultaneously
t=67.0: all text → opacity 0 over 0.2s (instant disappearance)
```

### CH08: The Ending (black, 67–72s)

```
t=67.0: all cleared, background → #000
t=67.2–67.7: pure black hold
t=68.7: "Your attention" · 52px white · opacity fade 0.6s
t=69.8: "is your life." · same style
t=71.0: "What will you spend it on?" · 28px · #888
Audio: piano_note (D4) begins at t=63 of master audio track
       (aligns with black screen onset in joined video)
No music from t=67s. No SFX. Only the piano tail decaying.
```
