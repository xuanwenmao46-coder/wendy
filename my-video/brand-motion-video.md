---
name: brand-motion-video
description: Generate a 60-second brand identity motion video in Swiss Grid / Motion Graphics style. The user describes their brand name, signature colors, tagline, target audience and keywords — this skill produces a complete HyperFrames composition with 8 narrative scenes, Bicep-style BGM, and SFX. Use when a user says "make me a brand video", "create a motion identity film", "brand showcase video", or describes a brand and asks for a video.
---

# Brand Motion Video — Swiss Grid × Motion Graphics

Generates a 60-second brand identity motion film following the **FORMA v4 narrative structure**:
Brand Detection → Color System → Grid + User Matrix → Typography → Data Viz → Target Audience → Convergence → Final Lockup.

---

## Step 1 — Gather Brand Information

Ask the user for the following. If they don't provide something, use the defaults shown.

| Variable | What to ask | Default |
|----------|-------------|---------|
| `BRAND_NAME` | Brand name (all caps works best) | `BRAND` |
| `COLOR_PRIMARY` | Signature / accent color (hex) | `#C6FF00` |
| `COLOR_DARK` | Dark background color | `#0C0C0C` |
| `COLOR_LIGHT` | Light background color | `#F2F2EE` |
| `TAGLINE` | One-line brand tagline | `Brand Identity System` |
| `WEBSITE` | Brand website or CTA | `brand.studio` |
| `YEAR` | Year | `2026` |
| `DISCIPLINE` | What the brand does | `Motion Design` |
| `SCOPE` | Brand scope/category | `Brand Identity` |
| `FOUNDED` | Founded year | `2024` |
| `KEYWORDS` | 4 brand DNA words (comma-separated) | `IDENTITY, MOTION, SYSTEM, PRECISION` |
| `AUDIENCE_1..6` | 6 target audience types | See defaults below |
| `STAT_1..6` | 6 data stats matching each audience | See defaults below |

**Default audiences + stats:**
```
AUDIENCE_1 = CREATIVE DIRECTORS    STAT_1 = 28–42 / AGE RANGE
AUDIENCE_2 = BRAND DESIGNERS       STAT_2 = 300K+ / MARKET SIZE
AUDIENCE_3 = STARTUP FOUNDERS      STAT_3 = SERIES A–C / FUNDING STAGE
AUDIENCE_4 = TECH LEADS            STAT_4 = SCALE ↑ / GROWTH STAGE
AUDIENCE_5 = MOTION ARTISTS        STAT_5 = FORMA FIT ✓ / BRAND ALIGNMENT
AUDIENCE_6 = BRAND STUDIOS         STAT_6 = ISO 9001 / QUALITY STD
```

**Color description prompts:**
- If user says "dark green + black": PRIMARY=`#1A5C2A`, DARK=`#0A0A0A`, LIGHT=`#F0F4EE`
- If user says "electric blue + white": PRIMARY=`#0057FF`, DARK=`#080810`, LIGHT=`#F4F6FF`
- If user says "coral red + cream": PRIMARY=`#FF4D2E`, DARK=`#120808`, LIGHT=`#FFF5F2`
- If user says "gold + black": PRIMARY=`#D4A017`, DARK=`#0C0A00`, LIGHT=`#FEFAE8`

---

## Step 2 — Generate Audio (gen_audio.py)

Before writing the HTML, generate the audio assets. Create `gen_audio.py` in the project root:

```python
"""
Brand Motion Video — Audio Generator
130 BPM Bicep-style BGM + 7 SFX layers
Run: python3 gen_audio.py
Outputs: audio/bgm.wav + audio/sfx-*.wav
"""
import numpy as np, wave, os, struct

os.makedirs("audio", exist_ok=True)
SR = 44100
BPM = 130
BEAT = 60.0 / BPM

def write_wav(path, data, sr=SR):
    data = np.clip(data, -1, 1)
    pcm = (data * 32767).astype(np.int16)
    with wave.open(path, 'w') as f:
        f.setnchannels(2 if pcm.ndim == 2 else 1)
        f.setsampwidth(2)
        f.setframerate(sr)
        f.writeframes(pcm.astype('<i2').tobytes())

def sine(freq, dur, sr=SR):
    t = np.linspace(0, dur, int(sr * dur), endpoint=False)
    return np.sin(2 * np.pi * freq * t)

def iir_lp(sig, fc, sr=SR):
    rc = 1.0 / (2 * np.pi * fc)
    dt = 1.0 / sr
    a = dt / (rc + dt)
    out = np.zeros_like(sig)
    out[0] = a * sig[0]
    for i in range(1, len(sig)):
        out[i] = out[i-1] + a * (sig[i] - out[i-1])
    return out

# ── BGM (60s Bicep-style) ──
DUR = 60
N = int(SR * DUR)
t = np.linspace(0, DUR, N, endpoint=False)
bgm = np.zeros(N)

# Kick: 4-on-the-floor
kick_times = np.arange(0, DUR, BEAT)
for kt in kick_times:
    i = int(kt * SR)
    d = int(0.18 * SR)
    if i + d >= N: continue
    env = np.exp(-np.linspace(0, 12, d))
    freq_sweep = np.linspace(160, 40, d)
    phase = np.cumsum(2 * np.pi * freq_sweep / SR)
    bgm[i:i+d] += 0.85 * env * np.sin(phase)

# Clap: beats 2+4
clap_times = np.arange(BEAT, DUR, 2 * BEAT)
for ct in clap_times:
    i = int(ct * SR)
    d = int(0.09 * SR)
    if i + d >= N: continue
    noise = np.random.randn(d) * np.exp(-np.linspace(0, 18, d))
    bgm[i:i+d] += 0.38 * iir_lp(noise, 3200)

# Hi-hat: 16th notes
hat_times = np.arange(0, DUR, BEAT / 4)
for ht in hat_times:
    i = int(ht * SR)
    d = int(0.045 * SR)
    if i + d >= N: continue
    noise = np.random.randn(d) * np.exp(-np.linspace(0, 22, d))
    bgm[i:i+d] += 0.14 * iir_lp(noise, 8000)

# Open hat: offbeat 8ths
ohat_times = np.arange(BEAT / 2, DUR, BEAT)
for ot in ohat_times:
    i = int(ot * SR)
    d = int(0.09 * SR)
    if i + d >= N: continue
    noise = np.random.randn(d) * np.exp(-np.linspace(0, 10, d))
    bgm[i:i+d] += 0.18 * iir_lp(noise, 10000)

# Bass: A-minor pattern
bass_notes = [55, 55, 82, 55, 49, 55, 44, 82]
bar_dur = 4 * BEAT
for bi in range(int(DUR / (bar_dur / 2)) + 1):
    for ni, freq in enumerate(bass_notes):
        st = bi * bar_dur / 2 + ni * (BEAT / 2)
        if st >= DUR: break
        i, d = int(st * SR), int(0.22 * SR)
        if i + d >= N: continue
        env = np.exp(-np.linspace(0, 8, d))
        note = np.sin(2 * np.pi * freq * np.arange(d) / SR)
        note += 0.3 * np.sin(2 * np.pi * freq * 2 * np.arange(d) / SR)
        bgm[i:i+d] += 0.35 * env * iir_lp(note, 600)

# Chord pads: Am-F-C-G (detuned 3-voice)
chord_seq = [[220,262,330],[175,220,262],[131,165,196],[196,247,294]]
for ci, ch in enumerate(chord_seq):
    for rep in range(int(DUR / (4 * bar_dur)) + 1):
        st = (ci * bar_dur + rep * 4 * bar_dur)
        if st >= DUR: break
        i, d = int(st * SR), min(int(bar_dur * SR), N - int(st * SR))
        if d <= 0: continue
        pad = np.zeros(d)
        for freq in ch:
            for det in [-0.3, 0, 0.3]:
                tt = np.arange(d) / SR
                pad += np.sin(2 * np.pi * (freq + det) * tt)
        env = np.ones(d)
        env[:int(0.08*SR)] = np.linspace(0, 1, int(0.08*SR))
        env[-int(0.15*SR):] = np.linspace(1, 0, int(0.15*SR))
        bgm[i:i+d] += 0.055 * iir_lp(pad * env, 1800)

# Arp: A-minor pentatonic
arp_notes = [110,165,131,196,147,196,131,165,110,165,147,220,165,196,147,165]
for ai, freq in enumerate(arp_notes * (int(DUR / (len(arp_notes) * BEAT / 4)) + 2)):
    st = ai * BEAT / 4
    if st >= DUR: break
    i, d = int(st * SR), int(0.08 * SR)
    if i + d >= N: continue
    env = np.exp(-np.linspace(0, 14, d))
    bgm[i:i+d] += 0.095 * env * np.sin(2 * np.pi * freq * np.arange(d) / SR)

# Master LPF sweep + stereo
sweep = np.interp(t, [0, 10, 30, 60], [600, 8000, 6000, 4000])
left = np.zeros(N)
right = np.zeros(N)
for i in range(N):
    fc = sweep[i]
    if i == 0:
        left[i] = right[i] = bgm[i]
    else:
        rc = 1.0 / (2 * np.pi * fc)
        a = (1/SR) / (rc + 1/SR)
        left[i]  = left[i-1]  + a * (bgm[i] - left[i-1])
        right[i] = right[i-1] + a * (bgm[max(0,i-616)] - right[i-1])

bgm_stereo = np.stack([left * 0.9, right * 0.9], axis=1)
write_wav("audio/bgm.wav", bgm_stereo)
print("bgm.wav done")

# ── SFX ──
def sfx_impact(dur=0.6):
    N = int(SR * dur)
    t = np.arange(N) / SR
    env = np.exp(-t * 9)
    sub = np.sin(2 * np.pi * np.linspace(80, 28, N) * t) * 0.9
    trans = np.random.randn(N) * np.exp(-t * 35) * 0.3
    return iir_lp((sub + trans) * env, 300)

def sfx_whoosh(dur=0.32):
    N = int(SR * dur)
    t = np.arange(N) / SR
    noise = np.random.randn(N)
    freq_env = np.linspace(400, 2800, N)
    env = np.sin(np.pi * t / dur) ** 0.7
    sig = np.zeros(N)
    for i in range(N):
        if i == 0: sig[i] = noise[i]
        else:
            rc = 1.0 / (2 * np.pi * freq_env[i])
            a = (1/SR) / (rc + 1/SR)
            sig[i] = sig[i-1] + a * (noise[i] - sig[i-1])
    return sig * env * 0.55

def sfx_tick(dur=0.06):
    N = int(SR * dur)
    t = np.arange(N) / SR
    return iir_lp(np.random.randn(N) * np.exp(-t * 80), 6000) * 0.7

def sfx_type(dur=0.12):
    N = int(SR * dur)
    t = np.arange(N) / SR
    click = np.sin(2 * np.pi * 2200 * t) * np.exp(-t * 50)
    noise = np.random.randn(N) * np.exp(-t * 40)
    return iir_lp(click * 0.4 + noise * 0.15, 5000)

def sfx_acid_sweep(dur=0.25):
    N = int(SR * dur)
    t = np.arange(N) / SR
    freq = np.linspace(300, 1800, N)
    phase = np.cumsum(2 * np.pi * freq / SR)
    env = np.sin(np.pi * t / dur)
    return iir_lp(np.sin(phase) * env * 0.6, 3000)

def sfx_matrix(dur=8.0):
    N = int(SR * dur)
    t = np.arange(N) / SR
    sig = np.zeros(N)
    for i in range(0, N, int(SR * 0.12)):
        d = int(SR * 0.06)
        if i + d >= N: break
        freq = 800 + (i % 7) * 200
        env = np.exp(-np.arange(d) / SR * 20)
        sig[i:i+d] += np.sin(2*np.pi*freq*np.arange(d)/SR) * env * 0.25
    noise_gate = np.random.randn(N) * 0.04 * np.clip(np.sin(2*np.pi*1.5*t), 0, 1)
    return iir_lp(sig + noise_gate, 4000)

def sfx_collapse(dur=7.0):
    N = int(SR * dur)
    t = np.arange(N) / SR
    impact_env = np.exp(-t * 2.5)
    sub = np.sin(2 * np.pi * np.linspace(60, 18, N) * t) * 0.75 * impact_env
    rumble = np.random.randn(N) * 0.15 * impact_env
    sweep_env = np.exp(-(t - 1) ** 2 / 0.5)
    sweep_freq = np.linspace(2000, 80, N)
    phase = np.cumsum(2 * np.pi * sweep_freq / SR)
    sweep = np.sin(phase) * sweep_env * 0.4
    return iir_lp(sub + rumble + sweep, 3500)

for name, fn in [
    ("sfx-impact", sfx_impact),
    ("sfx-whoosh", sfx_whoosh),
    ("sfx-tick", sfx_tick),
    ("sfx-type", sfx_type),
    ("sfx-acid-sweep", sfx_acid_sweep),
    ("sfx-matrix", sfx_matrix),
    ("sfx-collapse", sfx_collapse),
]:
    sig = fn()
    write_wav(f"audio/{name}.wav", sig)
    print(f"{name}.wav done")

print("All audio generated.")
```

Run it: `python3 gen_audio.py`

---

## Step 3 — Write the Composition (index.html)

Replace every `{{VARIABLE}}` with the user's values. The structure is fixed — only the brand tokens change.

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="hyperframes-composition" content="true">
<meta name="composition-id" content="{{BRAND_ID}}">
<meta name="composition-duration" content="60">
<meta name="composition-width" content="1920">
<meta name="composition-height" content="1080">
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{width:1920px;height:1080px;overflow:hidden;background:{{COLOR_DARK}};font-family:'Bebas Neue',sans-serif}
#root{position:absolute;inset:0;overflow:hidden}
#stage{position:absolute;inset:0}
#grid-tex{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.03) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.03) 1px,transparent 1px);background-size:40px 40px;z-index:1}
.flood{position:absolute;inset:0;pointer-events:none}
#fl-acid{z-index:50;background:{{COLOR_PRIMARY}};clip-path:polygon(0 0,0 0,0 100%,0 100%)}
#fl-white{z-index:50;background:{{COLOR_LIGHT}};clip-path:polygon(0 0,0 0,0 100%,0 100%)}
#fl-black{z-index:50;background:{{COLOR_DARK}};clip-path:polygon(0 0,0 0,0 100%,0 100%)}
#fl-brand{z-index:52;display:flex;align-items:center;justify-content:center;font-family:'Bebas Neue',sans-serif;font-size:280px;letter-spacing:-.02em;opacity:0;color:{{COLOR_DARK}}}

/*
  PASTE ALL CSS BLOCKS HERE
  (copy from the working composition — S01 through S08)
  Replace color values:
    #C6FF00  → {{COLOR_PRIMARY}}
    #0C0C0C  → {{COLOR_DARK}}
    #F2F2EE  → {{COLOR_LIGHT}}
    rgba(198,255,0,...) → rgba({{COLOR_PRIMARY_RGB}},...)
*/

.clip{position:absolute;inset:0;opacity:0;pointer-events:none}
</style>
</head>
<body>
<div id="root" data-composition-id="{{BRAND_ID}}" data-width="1920" data-height="1080" data-start="0" data-duration="60" style="overflow:hidden">
<div id="stage" data-layout-allow-overflow="true">
<!-- scenes go here -->
</div>
</div>
<script src="node_modules/gsap/dist/gsap.min.js"></script>
<script>
(function(){
var gsap = window.gsap;
var tl = gsap.timeline({ paused:true });
/* ... GSAP timeline ... */
window.__timelines = window.__timelines || {};
window.__timelines["{{BRAND_ID}}"] = tl;
})();
</script>
</body>
</html>
```

### Token substitution map

When writing the HTML from scratch using this skill, make these substitutions throughout:

| Token | Replace with |
|-------|-------------|
| `{{BRAND_NAME}}` | e.g. `FORMA` |
| `{{BRAND_ID}}` | slugified brand name, e.g. `forma-v1` |
| `{{TAGLINE}}` | e.g. `Brand Identity System` |
| `{{WEBSITE}}` | e.g. `forma.studio` |
| `{{YEAR}}` | e.g. `2026` |
| `{{FOUNDED}}` | e.g. `2026` |
| `{{DISCIPLINE}}` | e.g. `MOTION DESIGN` |
| `{{SCOPE}}` | e.g. `BRAND IDENTITY` |
| `{{COLOR_PRIMARY}}` | e.g. `#C6FF00` |
| `{{COLOR_DARK}}` | e.g. `#0C0C0C` |
| `{{COLOR_LIGHT}}` | e.g. `#F2F2EE` |
| `{{COLOR_PRIMARY_RGB}}` | comma-separated RGB of primary, e.g. `198,255,0` |
| `{{KW1}}..{{KW4}}` | 4 brand DNA keywords |
| `{{COL_NAME_1}}` | Color 1 name, e.g. `PRIMARY` |
| `{{COL_HEX_1}}` | Color 1 hex |
| `{{COL_DESC_1}}` | Color 1 description 3 lines |
| `{{AUD_NAME_1}}..{{AUD_NAME_6}}` | 6 audience persona names |
| `{{AUD_STAT_NUM_1}}..{{AUD_STAT_NUM_6}}` | 6 stat numbers |
| `{{AUD_STAT_LABEL_1}}..{{AUD_STAT_LABEL_6}}` | 6 stat labels |

---

## Step 4 — 8-Scene Narrative Structure (Fixed)

This structure is **non-negotiable** — it gives the video its narrative arc. Only the content tokens change.

```
00-10s  S01  BRAND DETECTION
             System scan line sweeps → "BRAND DETECTED" → brand name letter-by-letter
             → 4 brand DNA keywords flash in sequence → progress bar fills

10-17s  S02  COLOR SYSTEM
             3 color blocks diagonal wipe in → labels + hex codes + descriptions

17-25s  S03  GRID + USER MATRIX
             12-column grid builds → user profile data labels appear at intersections
             (AGE / ROLE / CONTEXT / SECTOR / SCALE / REACH)

25-33s  S04  TYPOGRAPHY
             Brand name large → brand words in Bebas Neue → tracking breath animation

33-38s  S05  DATA VISUALIZATION
             Line chart grows → bar chart rises → ring counter counts to N%
             → system nodes connect

38-50s  S06  TARGET AUDIENCE MATRIX
             "TARGET AUDIENCE" headline → 12 cards (4×3) stagger in:
             alternating [persona card dark] [stat card acid/white]
             Each persona card has SVG human silhouette + CRT scanlines

50-57s  S07  MODULE CONVERGENCE
             16 brand system fragments (scattered) → all converge to center
             → brand name expands from center (back.out spring)

57-60s  S08  FINAL LOCKUP
             Primary color background → brand name large → tagline → website CTA
```

---

## Step 5 — Scene-by-Scene Implementation

### S01 Brand Detection (0–10s)

**Key elements:**
- `#s01-scanline` — 2px line, `height:2px`, sweeps `y:0 → y:1082` over 1.5s
- `#s01-init` — "SYSTEM INITIALIZING · BRAND ANALYSIS MODULE" in Space Grotesk 13px, primary color
- `#s01-detected` — "BRAND DETECTED" in Space Grotesk 22px, letter-spacing 0.55em
- `.s1l` — one div per letter of brand name, Bebas Neue 320px, stagger 0.12s apart
- `.s1-kw` — brand DNA keywords, Bebas Neue 72px, flash in at 0.5s intervals
- `#s01-progress` — width: 0 → 600px over 1s
- Transition at 9.74s: `#fl-black` diagonal wipe + brandFlash

**CSS pattern:**
```css
#s01-scanline{position:absolute;left:0;width:1920px;height:2px;
  background:linear-gradient(90deg,transparent,{{COLOR_PRIMARY}} 50%,transparent);opacity:0;z-index:20;top:0}
.s1l{position:absolute;font-family:'Bebas Neue',sans-serif;font-size:320px;
  line-height:1;color:{{COLOR_LIGHT}};letter-spacing:-.02em;top:310px;opacity:0}
.s1-kw{position:absolute;top:780px;font-family:'Bebas Neue',sans-serif;
  font-size:72px;letter-spacing:.06em;opacity:0}
#kw1{left:80px;color:{{COLOR_PRIMARY}}}
#kw2{left:380px;color:rgba({{COLOR_LIGHT_RGB}},.7)}
#kw3{left:640px;color:rgba({{COLOR_LIGHT_RGB}},.5)}
#kw4{left:870px;color:rgba({{COLOR_LIGHT_RGB}},.35)}
```

**GSAP pattern:**
```js
/* S01 */
tl.set("#s01", { opacity:1 }, 0);
/* scan */
tl.set("#s01-scanline", { y:0, opacity:1 }, 0.3);
tl.to("#s01-scanline", { y:1082, duration:1.5, ease:"power1.inOut" }, 0.3);
tl.set("#s01-scanline", { opacity:0 }, 1.85);
/* init text */
tl.to("#s01-init", { opacity:1, duration:.2 }, 0.35);
tl.to("#s01-signal", { opacity:1, duration:.2 }, 0.8);
/* BRAND DETECTED */
tl.to("#s01-det-bar", { width:400, duration:.35, ease:"power3.out" }, 2.0);
tl.to("#s01-detected", { opacity:1, duration:.25 }, 2.2);
/* brand name letters */
["#s1-F","#s1-O","#s1-R","#s1-M","#s1-A"].forEach(function(id,i){
  tl.to(id, { opacity:1, y:0, duration:.15, ease:"power4.out" }, 3.0 + i*0.12);
});
/* keyword analysis */
tl.to("#s01-kw-label", { opacity:1, duration:.2 }, 4.2);
["#kw1","#kw2","#kw3","#kw4"].forEach(function(id,i){
  tl.fromTo(id, { opacity:0, x:-20 }, { opacity:1, x:0, duration:.2, ease:"power3.out" }, 4.5 + i*0.5);
});
/* progressive dimming of earlier keywords */
tl.to("#kw1", { color:"rgba({{COLOR_LIGHT_RGB}},.35)", duration:.15 }, 5.5);
tl.to("#kw2", { color:"rgba({{COLOR_LIGHT_RGB}},.35)", duration:.15 }, 6.0);
tl.to("#kw3", { color:"rgba({{COLOR_LIGHT_RGB}},.4)", duration:.15 }, 6.0);
/* progress */
tl.to("#s01-progress", { width:600, opacity:1, duration:1.0, ease:"power2.inOut" }, 6.5);
tl.to("#s01-prog-label", { opacity:1, duration:.3 }, 7.2);
tl.to("#s01-counter", { opacity:1, duration:.3 }, 7.5);
/* out */
tl.fromTo("#fl-black",
  { clipPath:"polygon(0 0,0 0,0 100%,0 100%)" },
  { clipPath:"polygon(0 0,100% 0,100% 100%,0 100%)", duration:.22, ease:"power4.in" }, 9.74);
brandFlash(9.74, false, .25);
tl.set("#s01", { opacity:0 }, 10.0);
tl.set("#fl-black", { clipPath:"polygon(0 0,0 0,0 100%,0 100%)" }, 10.01);
```

### S02 Color System (10–17s)

**Key elements:**
- 3 color blocks (`#cb-pri`, `#cb-sec`, `#cb-acc`) diagonal wipe in at 10.05/10.18/10.31s
- Labels + hex codes + descriptions stagger in
- Blocks diagonal wipe out at 16.55/16.62/16.69s

```js
function diagonalIn(id, t, dur) {
  dur = dur || .22;
  tl.fromTo(id,
    { clipPath:"polygon(0 0,0 0,0 100%,0 100%)" },
    { clipPath:"polygon(0 0,100% 0,100% 100%,0 100%)", duration:dur, ease:"power3.out" }, t);
}
function diagonalOut(id, t, dur) {
  dur = dur || .2;
  tl.to(id, { clipPath:"polygon(40% 0,100% 0,100% 100%,70% 100%)", duration:dur*.55, ease:"power2.in" }, t);
  tl.to(id, { clipPath:"polygon(100% 0,100% 0,100% 100%,100% 100%)", duration:dur*.45, ease:"power2.in" }, t+dur*.55);
}
```

### S03 Grid + User Matrix (17–25s)

**Key elements:**
- 11 vertical + 7 horizontal SVG lines, stagger in
- 77 background intersection dots at opacity 0.12
- 6 data label divs (`.gd-label`) appear at grid intersections from t=20.0s

**Label positions** (relative to 1920×1080 canvas — adjust to avoid overlap):
```
gdl1: left:285px  top:95px   → USER PROFILE / AGE {{USER_AGE}}
gdl2: left:445px  top:365px  → ROLE / {{USER_ROLE}}
gdl3: left:765px  top:500px  → CONTEXT / {{USER_CONTEXT}}
gdl4: left:1085px top:230px  → SECTOR / {{USER_SECTOR}}
gdl5: left:1405px top:635px  → SCALE / {{USER_SCALE}}
gdl6: left:1565px top:95px   → REACH / {{USER_REACH}}
```

### S04 Typography (25–33s)

**Key elements:**
- `#tw1` — brand name, 240px, dark bg scene uses COLOR_DARK text
- `#tw2` — keyword 1, 160px, outlined in primary color
- `#tw3` — keyword 2, 200px
- `#tw4` — subtitle string, 88px, low opacity
- `#tw5` — ghost brand name, 300px, 6% opacity (right edge)
- Scene background: `{{COLOR_LIGHT}}`
- Text color: `{{COLOR_DARK}}`

**Tracking breath on brand name:**
```js
tl.to("#tw1", { letterSpacing:"0.06em", duration:.45, ease:"power2.out" }, 26.26);
tl.to("#tw1", { letterSpacing:"-0.01em", duration:.3,  ease:"power2.in"  }, 26.72);
```

### S05 Data Visualization (33–38s)

**Key elements:**
- Line chart: `stroke-dasharray:800; stroke-dashoffset:800 → 0`
- Bar chart: `attr:{y, height}` animate from baseline up
- Ring counter: `onUpdate` callback counts 0 → target%
- Node graph: `stroke-dashoffset:200 → 0` for each connector line

**Ring counter pattern:**
```js
tl.set("#ring-pct", { opacity:1 }, 35.1);
var _rc = { v:0 };
tl.to(_rc, { v:{{RING_TARGET}}, duration:.75, ease:"power2.out",
  onUpdate: function() {
    var el = document.getElementById("ring-pct");
    if (el) el.textContent = Math.round(_rc.v) + "%";
  }
}, 35.1);
```

### S06 Target Audience Matrix (38–50s)

**Layout:** 4 columns × 3 rows = 12 cells, each 480×320px, starting at y=120 (below 120px headline)

**Cell pattern — persona card (dark/mid bg):**
```html
<div class="pc pc-mid" id="pc00">
  <div class="pc-deco" style="color:{{COLOR_PRIMARY}}">{{INITIAL}}</div>
  <div class="pc-content">
    <svg class="pc-silhouette" viewBox="0 0 80 96" style="width:72px;height:86px" xmlns="http://www.w3.org/2000/svg">
      <circle cx="40" cy="28" r="20" fill="rgba({{COLOR_PRIMARY_RGB}},.14)" stroke="{{COLOR_PRIMARY}}" stroke-width="1.5"/>
      <rect x="28" y="24" width="8" height="3" rx="1.5" fill="{{COLOR_PRIMARY}}" opacity=".7"/>
      <rect x="44" y="24" width="8" height="3" rx="1.5" fill="{{COLOR_PRIMARY}}" opacity=".7"/>
      <path d="M32 37 Q40 43 48 37" fill="none" stroke="{{COLOR_PRIMARY}}" stroke-width="1.2" opacity=".55"/>
      <path d="M6 96 Q6 64 40 60 Q74 64 74 96" fill="rgba({{COLOR_PRIMARY_RGB}},.1)" stroke="{{COLOR_PRIMARY}}" stroke-width="1.5"/>
    </svg>
    <div class="pc-tag" style="color:rgba({{COLOR_PRIMARY_RGB}},.5)">AUDIENCE 0{{N}}</div>
    <div class="pc-name" style="color:{{COLOR_LIGHT}}">{{AUD_NAME_N}}</div>
  </div>
</div>
```

**Cell pattern — stat card (primary color bg):**
```html
<div class="pc pc-acid" id="pc01">
  <div class="pc-content" style="justify-content:center">
    <div class="pc-stat-num" style="color:{{COLOR_DARK}}">{{AUD_STAT_NUM_1}}</div>
    <div class="pc-stat-sub" style="color:rgba({{COLOR_DARK_RGB}},.6)">{{AUD_STAT_LABEL_1}}</div>
  </div>
</div>
```

**12-cell layout (row × col):**
```
[0,0] persona 1 — dark    [0,1] stat 1 — primary   [0,2] persona 2 — dark    [0,3] stat 2 — light
[1,0] stat 3 — primary    [1,1] persona 3 — dark    [1,2] stat 4 — light      [1,3] persona 4 — dark
[2,0] persona 5 — dark    [2,1] stat 5 — primary    [2,2] persona 6 — dark    [2,3] stat 6 — light
```

**GSAP stagger:**
```js
var pcRow0 = ["#pc00","#pc01","#pc02","#pc03"];
var pcRow1 = ["#pc10","#pc11","#pc12","#pc13"];
var pcRow2 = ["#pc20","#pc21","#pc22","#pc23"];
pcRow0.forEach(function(id,i){ tl.fromTo(id, { opacity:0, y:20 }, { opacity:1, y:0, duration:.3, ease:"power3.out" }, 38.7 + i*0.15); });
pcRow1.forEach(function(id,i){ tl.fromTo(id, { opacity:0, y:20 }, { opacity:1, y:0, duration:.3, ease:"power3.out" }, 39.4 + i*0.15); });
pcRow2.forEach(function(id,i){ tl.fromTo(id, { opacity:0, y:20 }, { opacity:1, y:0, duration:.3, ease:"power3.out" }, 40.1 + i*0.15); });
/* pulse at 44s */
["#pc00","#pc02","#pc11","#pc13","#pc20","#pc22"].forEach(function(id,i){
  tl.to(id, { scale:1.02, duration:.25, ease:"power2.out" }, 44.0 + i*0.15);
  tl.to(id, { scale:1.0,  duration:.2,  ease:"power2.in"  }, 44.25 + i*0.15);
});
```

### S07 Module Convergence (50–57s)

**16 fragment blocks** — mix of primary/dark/light backgrounds, labeled with brand system components (FORMA/COLOR/GRID/TYPE/DATA/MOTION/BRAND/LAYOUT/SYSTEM/SCALE/SHAPE/OUTPUT/DESIGN/AUDIT/DEPLOY/BRAND)

**Positions:** scattered at corners + edges (avoid the center 600×300px zone)

**GSAP convergence:**
```js
/* appear quickly */
fragIds.forEach(function(id,i){ tl.to(id, { opacity:1, duration:.08 }, 50.1 + i*0.05); });
/* converge: all fly to center, scale to 0 */
fragIds.forEach(function(id,i){
  tl.to(id, { x:960, y:540, scale:.04, opacity:0, duration:1.2, ease:"power2.in" }, 51.4 + i*0.04);
});
/* brand name expands from center after convergence */
tl.fromTo("#s07-brand",
  { opacity:0, scale:.06, xPercent:-50, yPercent:-50 },
  { opacity:1, scale:1, xPercent:-50, yPercent:-50, duration:.6, ease:"back.out(1.4)" }, 53.0);
tl.to("#s07-tagline", { opacity:1, duration:.4 }, 53.7);
```

> **Critical:** Do NOT set CSS `transform` on `#s07-brand` or `#s07-tagline`. Use only GSAP `xPercent`/`yPercent` for centering. CSS transform + GSAP transform conflict causes the element to jump.

### S08 Final Lockup (57–60s)

**Background:** `{{COLOR_PRIMARY}}`  
**Brand name:** `{{COLOR_DARK}}`, 240px Bebas Neue  
**Tagline:** `{{COLOR_DARK}}` 50% opacity  
**Website:** `{{WEBSITE}}`, bottom center, 42px Bebas, 55% opacity  
**Footer left:** `{{BRAND_NAME}} STUDIO © {{YEAR}}`  
**Footer right:** descriptor string  

---

## Step 6 — Audio Track Index Map

| Track | Content | Notes |
|-------|---------|-------|
| 10 | BGM (60s) | Volume 0.38 |
| 11 | Impact group + main SFX | Impacts 0.05–0.25s; sweeps + whooshes at transitions |
| 12 | Secondary SFX | Whoosh echoes; tick series |
| 13 | Tertiary ticks | Matrix build ticks |
| 14–15 | Impact overflow | Impact 4+5 (opening only) |
| 16 | Sweep layer | acid-sweep at major transitions |

**No two audio clips on the same track may overlap.** Always check start + duration before assigning a track.

**Transition audio timing** (for 8-scene structure):
```
 0.05s  impact cluster (tracks 11-15)
 0.40s  scan whoosh (track 16)
 2.50s  type ticks for BRAND DETECTED (11-12)
 3.00s  type ticks for brand letters (11-12)
 4.50s  keyword ticks ×4 at 0.5s intervals (11-12)
 9.74s  acid-sweep S01→S02 (track 16)
10.05s  whoosh echoes (11-12)
17.30s  grid tick series ×6 at 0.1s intervals (11-12)
24.74s  whoosh S03→S04 (track 11)
25.20s  type ticks for typography (track 16, not 11)
32.74s  acid-sweep S04→S05 (track 11)
33.05s  whoosh echo (track 12)
37.74s  whoosh S05→S06 (track 12)
38.00s  sfx-matrix 8s (track 11)
38.30s  matrix build ticks ×6 (tracks 12-13)
49.70s  fl-black flash
50.00s  sfx-collapse 7s (track 11)
56.74s  acid-sweep S07→S08 (track 12)
```

---

## Step 7 — Helpers (always include in `<script>`)

```js
function diagonalIn(id, t, dur) {
  dur = dur || .22;
  tl.fromTo(id,
    { clipPath:"polygon(0 0,0 0,0 100%,0 100%)" },
    { clipPath:"polygon(0 0,100% 0,100% 100%,0 100%)", duration:dur, ease:"power3.out" }, t);
}
function diagonalOut(id, t, dur) {
  dur = dur || .2;
  tl.to(id, { clipPath:"polygon(40% 0,100% 0,100% 100%,70% 100%)", duration:dur*.55, ease:"power2.in" }, t);
  tl.to(id, { clipPath:"polygon(100% 0,100% 0,100% 100%,100% 100%)", duration:dur*.45, ease:"power2.in" }, t+dur*.55);
}
function brandFlash(t, lightBg, dur) {
  dur = dur || .5;
  tl.set("#fl-brand", { color: lightBg ? "{{COLOR_DARK}}" : "{{COLOR_PRIMARY}}", opacity:0 }, t - .01);
  tl.to("#fl-brand", { opacity:.9, duration:.1, ease:"power4.in" }, t);
  tl.to("#fl-brand", { opacity:0, duration:.2, ease:"power2.out" }, t + dur - .2);
}
```

**brandFlash call sites** (lightBg = true when transition floods a light/primary color bg):
```js
brandFlash(9.74,  false);   // S01→S02 dark flood
brandFlash(16.74, false);   // S02→S03 dark flood (adjust if using white)
brandFlash(24.74, true);    // S03→S04 white flood
brandFlash(32.74, false);   // S04→S05 dark mask
brandFlash(37.74, true);    // S05→S06 primary flood
brandFlash(49.7,  false);   // S06→S07 dark flood
brandFlash(56.74, true);    // S07→S08 primary flood
```

---

## Step 8 — Lint + Render Checklist

After writing `index.html`, always run before rendering:

```bash
npm run check
```

**Common errors and fixes:**

| Error | Fix |
|-------|-----|
| `overlapping_clips_same_track` | Move one audio clip to a higher track index |
| `gsap_css_transform_conflict` | Remove CSS `transform:translate(-50%,-50%)` from GSAP-animated elements; use `xPercent:-50, yPercent:-50` in the tween instead |
| `timeline_id_mismatch` | Ensure `data-composition-id` on root `#root` div matches `window.__timelines["{{BRAND_ID}}"]` key |
| `root_composition_missing_data_start` | Add `data-start="0" data-duration="60"` to root div |
| `media_missing_id` | Every `<audio>` element needs a unique `id` attribute |

**Render:**
```bash
npm run render
```

Expected output: `renders/{{project}}_{{date}}.mp4` (~3.5–4.5 MB for 60s)

---

## Quick Reference — Complete Variable Checklist

Before writing any HTML, confirm you have all of these:

```
□ BRAND_NAME       (all caps, e.g. NEXUS)
□ BRAND_ID         (slug, e.g. nexus-v1)
□ COLOR_PRIMARY    (hex, e.g. #FF4D2E)
□ COLOR_PRIMARY_RGB (comma RGB, e.g. 255,77,46)
□ COLOR_DARK       (hex, e.g. #0C0808)
□ COLOR_DARK_RGB   (comma RGB, e.g. 12,8,8)
□ COLOR_LIGHT      (hex, e.g. #FFF5F2)
□ COLOR_LIGHT_RGB  (comma RGB, e.g. 255,245,242)
□ TAGLINE          (e.g. "Creative Technology Studio")
□ WEBSITE          (e.g. nexus.studio)
□ YEAR             (e.g. 2026)
□ FOUNDED          (e.g. 2024)
□ DISCIPLINE       (e.g. CREATIVE TECHNOLOGY)
□ SCOPE            (e.g. BRAND & PRODUCT)
□ KW1 KW2 KW3 KW4 (brand DNA, e.g. CREATE / BUILD / SCALE / SHIP)
□ AUD_NAME_1..6    (persona names)
□ AUD_STAT_NUM_1..6 (stat numbers, e.g. 25-40, 500K+, ×3)
□ AUD_STAT_LABEL_1..6 (stat labels)
□ USER_AGE USER_ROLE USER_CONTEXT USER_SECTOR USER_SCALE USER_REACH (grid labels)
□ RING_TARGET      (ring chart percentage, e.g. 78)
```

---

## Example Prompt → Output

**User says:**
> "我的品牌叫 NEXUS，做创意技术的，主色是珊瑚红 #FF4D2E，深色背景，目标客户是创业公司和产品设计师"

**Claude extracts:**
```
BRAND_NAME = NEXUS
COLOR_PRIMARY = #FF4D2E
COLOR_PRIMARY_RGB = 255,77,46
COLOR_DARK = #120808
COLOR_DARK_RGB = 18,8,8
COLOR_LIGHT = #FFF5F2
COLOR_LIGHT_RGB = 255,245,242
TAGLINE = Creative Technology Studio
DISCIPLINE = CREATIVE TECHNOLOGY
KW1 = CREATE  KW2 = BUILD  KW3 = SCALE  KW4 = LAUNCH
AUD_NAME_1 = STARTUP FOUNDERS
AUD_NAME_2 = PRODUCT DESIGNERS
AUD_NAME_3 = TECH LEADS
AUD_NAME_4 = CREATIVE DIRECTORS
AUD_NAME_5 = VENTURE STUDIOS
AUD_NAME_6 = GROWTH TEAMS
```

Then generates `gen_audio.py` → runs it → writes full `index.html` with all substitutions → `npm run check` → `npm run render`.
