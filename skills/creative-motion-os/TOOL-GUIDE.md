---
title: CMOS V5 Tool Guide
---

# Tool Guide — Creative Motion Operating System V5

Two production tools ship with CMOS V5. Both are standalone Python scripts with no dependency beyond numpy and FFmpeg.

---

## Tool 1 — PremiumColorReducer

**File:** `tools/premium_color_reducer.py`
**Purpose:** Intercepts any AI-generated color and maps it to the nearest color in a curated Swiss/Morandi palette using CIE L*a*b* Delta E distance.

### Why L*a*b* and not RGB distance?

RGB distance is perceptually wrong. The Euclidean distance between `[0,0,255]` and `[0,0,200]` in RGB is 55. The perceptual distance (how different they look to a human eye) is much smaller than the distance between `[255,200,0]` and `[255,240,0]` — but RGB gives those the same score. CIELAB is designed so that equal numerical distances correspond to equal perceived differences. A Delta E of 1.0 is the threshold of human perception.

### Palettes

| Palette name | Description | Use for |
|---|---|---|
| `swiss_morandi` | Paper gray, charcoal, forest green, slate, flesh pink | Default; intercept any AI output |
| `editorial_luxury` | Warm ivory, fog white, graphite, stone, cobalt, burgundy, acid yellow | Mode A color narrative |
| `festival` | Near black, ultra white, acid green, electric purple, hot pink, signal red, ultra yellow | Mode B color narrative |

### Usage

**Install:**
```bash
pip install numpy
```

**Single color — CLI:**
```bash
# Map a cheap AI blue to the nearest Swiss/Morandi color
python tools/premium_color_reducer.py --rgb 0,0,255

# Map from hex
python tools/premium_color_reducer.py --hex "#7B68EE"

# Use editorial luxury palette
python tools/premium_color_reducer.py --hex "#7B68EE" --palette editorial_luxury

# Show the active palette
python tools/premium_color_reducer.py --show-palette --palette festival
```

**Single color — Python:**
```python
from tools.premium_color_reducer import PremiumColorReducer

reducer = PremiumColorReducer(palette_name="swiss_morandi")

# Map RGB
ai_cyan = [0, 255, 255]
premium = reducer.map_to_premium_color(ai_cyan)
print(premium)  # (47, 62, 70) — mapped to slate gray

# Map hex
premium_hex = reducer.map_to_premium_hex("#00FFFF")
print(premium_hex)  # "#2F3E46"
```

**Batch processing — CLI:**
```bash
# colors.json: ["#FF0000", "#00FF00", [0, 0, 255], "#FF00FF"]
python tools/premium_color_reducer.py --batch colors.json --out mapped.json
```

**Batch processing — Python:**
```python
colors = [
    [0, 0, 255],       # cheap blue
    "#FF6B35",         # AI orange
    [200, 100, 255],   # AI purple glow
    "#00FFFF",         # AI cyan
]
results = reducer.map_batch(colors)
for r in results:
    print(f"{r['input_hex']} → {r['output_hex']}  ΔE={r['delta_e']}")
```

**Custom palette:**
```python
custom = {
    "background": ("#F5EFE4", "Warm ivory ground"),
    "text":        ("#1A1A1A", "Charcoal black"),
    "accent":      ("#1B3A8C", "Cobalt blue"),
}
reducer = PremiumColorReducer(custom_palette=custom)
```

### Demo output
```
PREMIUM PALETTE: SWISS_MORANDI
────────────────────────────────────────────────────────────
  #EAEAEA  [234,234,234]  paper_gray         纸张感浅灰底色
  #1A1A1A  [ 26, 26, 26]  charcoal_black     极端对比深炭黑
  #0F2D1E  [ 15, 45, 30]  forest_green       优雅暗森林绿
  #2F3E46  [ 47, 62, 70]  slate_gray         沉稳石板灰
  #D8B4A6  [216,180,166]  flesh_pink         低饱和复古肉粉
────────────────────────────────────────────────────────────

DEMO — mapping AI-generated colors to premium palette:
       INPUT  →       OUTPUT   ΔE
     #0000FF  →      #2F3E46   68.9  (cheap blue)
     #FF0000  →      #D8B4A6   54.2  (signal red)
     #00FF00  →      #0F2D1E   73.1  (lime green)
     #FFC800  →      #D8B4A6   42.0  (gold)
     #C864FF  →      #2F3E46   58.3  (AI purple)
     #00FFFF  →      #2F3E46   66.4  (AI cyan)
```

---

## Tool 2 — AudioSync

**File:** `tools/audio_sync.py`
**Purpose:** Detects the most impactful moment in an audio track (Stage 1), then generates an FFmpeg command to shift the audio so that moment aligns with the animation's impact frame (Stage 2).

### The Problem It Solves

When an animation has a text slam at `t=1450ms`, and the audio track's bass hit is at `t=200ms`, the viewer hears the impact 1250ms before seeing it. The sync engine adds 1250ms of silence before the audio, so both events land on the same frame.

```
Before:  [bass hit at 200ms] ──────── [video impact at 1450ms]
After:   [silence 1250ms] [bass hit at 1450ms] = [video impact at 1450ms]
```

### Requirements

```bash
# System
which ffmpeg   # must be on PATH
which ffprobe  # must be on PATH

# Python
pip install numpy
```

### Usage

**Most common — auto-detect peak and align:**
```bash
python tools/audio_sync.py --audio track.wav --anim-start 1450
```

**Output:**
```
Detecting audio peak in: track.wav
Peak detected at: 200ms (-12.3dBFS)

────────────────────────────────────────────────────────────
  AUDIO SYNC ENGINE — CMOS V5
────────────────────────────────────────────────────────────
  Animation impact point : 1450 ms  (1.450s)
  Audio peak point       : 200 ms   (0.200s)
  Required offset        : +1250 ms
  Strategy               : DELAY — pad 1250ms silence at start
  FFmpeg command         : ffmpeg -y -i "track.wav" -af "adelay=1250|1250" "aligned_audio.wav"
────────────────────────────────────────────────────────────
```

**Execute the alignment (add `--run`):**
```bash
python tools/audio_sync.py --audio track.wav --anim-start 1450 --run
# Creates: aligned_audio.wav
```

**Detect peak only:**
```bash
python tools/audio_sync.py --audio track.wav --detect-only
# Output: {"Audio_Peak_Time": 200, "Peak_Value_dB": -12.3, ...}
```

**From animation JSON (CMOS pipeline format):**
```bash
# animation.json: {"Animation_Start_Time": 1450}
python tools/audio_sync.py --audio track.wav --video-json animation.json --run
```

**Python API:**
```python
from tools.audio_sync import detect_audio_peak, align_audio_to_animation, run_alignment

# Stage 1: detect
audio_data = detect_audio_peak("track.wav", method="rms")
print(audio_data["Audio_Peak_Time"])  # e.g. 200

# Stage 2: align
video_data = {"Animation_Start_Time": 1450}
result = align_audio_to_animation(
    video_data, audio_data,
    input_audio="track.wav",
    output_audio="aligned_audio.wav",
)
print(result["ffmpeg_command"])
print(result["offset_ms"])     # +1250
print(result["strategy"])      # "delay"

# Execute
run_alignment(result)
```

**Multi-beat alignment (when animation has multiple impact points):**
```python
from tools.audio_sync import align_multiple_beats

beats = [
    {"label": "title_slam",    "time_ms": 800,  "priority": 1},  # most important
    {"label": "data_hit",      "time_ms": 3200, "priority": 2},
    {"label": "cta_entrance",  "time_ms": 8400, "priority": 3},
]
result = align_multiple_beats(beats, audio_file="track.wav", output_audio="aligned.wav")
```

### Peak Detection Methods

| Method | How it works | Best for |
|---|---|---|
| `rms` (default) | Finds 50ms window with highest RMS energy | Musical tracks, rhythmic SFX |
| `peak` | Finds loudest single sample frame | Impact hits, single transients |

### Integration with CMOS Pipeline

In the CMOS pipeline, the animation JSON produced by the motion director includes `Animation_Start_Time` for each major beat. Pass the most important beat to AudioSync before final composition:

```python
# motion_brief.json (from motion-graphic-design)
{
  "beats": [
    {"label": "intro_text",  "time_ms": 600,  "priority": 3},
    {"label": "hero_slam",   "time_ms": 1200, "priority": 1},  # ← primary sync
    {"label": "data_reveal", "time_ms": 4800, "priority": 2},
  ]
}

# Run sync
python tools/audio_sync.py \
  --audio sfx_track.wav \
  --video-json motion_brief.json \
  --output aligned_sfx.wav \
  --run
```

Then compose the aligned audio with the rendered video:
```bash
ffmpeg -i promo.mp4 -i aligned_sfx.wav \
  -c:v copy -c:a aac -b:a 192k \
  -map 0:v:0 -map 1:a:0 \
  promo_with_audio.mp4
```

---

## Combined CMOS Pipeline Example

```python
from tools.premium_color_reducer import PremiumColorReducer
from tools.audio_sync import detect_audio_peak, align_audio_to_animation, run_alignment

# 1. Intercept AI-generated palette from image generator
ai_colors = ["#0000FF", "#00FFFF", "#7B68EE", "#FF6B35"]
reducer = PremiumColorReducer(palette_name="editorial_luxury")
premium_colors = [reducer.map_to_premium_hex(c) for c in ai_colors]
print("Corrected palette:", premium_colors)
# ['#1B3A8C', '#2A2A2A', '#3D3D3D', '#F5EFE4']

# 2. Align audio to animation
audio_data = detect_audio_peak("sfx_boom.wav")
video_data = {"Animation_Start_Time": 1200}  # hero text arrives at 1.2s
result = align_audio_to_animation(video_data, audio_data,
                                  input_audio="sfx_boom.wav",
                                  output_audio="sfx_aligned.wav")
run_alignment(result)
print(f"Audio aligned: offset={result['offset_ms']}ms, strategy={result['strategy']}")
```
