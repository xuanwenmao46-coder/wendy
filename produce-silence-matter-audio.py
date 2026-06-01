#!/usr/bin/env python3
"""
Audio Production for silence-of-matter.mp4
- English TTS via espeak-ng + SSML (en-gb-x-rp, Received Pronunciation)
  Ultra-slow, low pitch — meditative, contemplative register
- Background ambient piano (very low mix)
- Composed with video using ffmpeg
"""

import subprocess, os
from pathlib import Path

VIDEO_IN   = str(Path(__file__).parent / "silence-of-matter.mp4")
VIDEO_OUT  = str(Path(__file__).parent / "silence-of-matter-audio.mp4")
MUSIC_FILE = str(Path(__file__).parent / "skills/video-podcast-maker/assets/snow-stevekaldes-piano-397491.mp3")
TMP        = "/tmp/silence-matter-audio"
os.makedirs(TMP, exist_ok=True)

# (start_ms, ssml_body)
# Text appears when the line's opacity begins rising in the GSAP timeline
SSML_TEMPLATE = """<?xml version="1.0"?>
<speak xmlns="http://www.w3.org/2001/10/synthesis" version="1.0" xml:lang="en-GB">
  {body}
</speak>"""

TTS_LINES = [
    # S1 text rises at 2.8s
    (
        2800,
        '<prosody rate="x-slow" pitch="-6st" volume="92">'
        'There is no urgency<break time="500ms"/>here.'
        '</prosody>',
    ),
    # S2 text rises at 11.2s
    (
        11200,
        '<prosody rate="x-slow" pitch="-5st" volume="92">'
        'Only matter,<break time="600ms"/>as it is.'
        '</prosody>',
    ),
    # S3 text rises at 20.0s
    (
        20000,
        '<prosody rate="x-slow" pitch="-5st" volume="92">'
        'texture<break time="400ms"/>defines<break time="400ms"/>memory.'
        '</prosody>',
    ),
    # S4 text rises at 29.0s
    (
        29000,
        '<prosody rate="x-slow" pitch="-7st" volume="92">'
        'form disappears.<break time="1000ms"/>'
        '<emphasis level="strong">essence remains.</emphasis>'
        '</prosody>',
    ),
    # S5 text rises at 40.8s
    (
        40800,
        '<prosody rate="x-slow" pitch="-6st" volume="92">'
        'A quiet study<break time="500ms"/>of material.'
        '</prosody>',
    ),
]

TOTAL_MS  = 45000
MUSIC_VOL = 0.10   # very quiet — sound never dominant over visual
TTS_VOL   = 0.94

# ── Step 1: Generate SSML TTS clips ───────────────────────────────────────
print("Generating SSML TTS clips (ultra-slow contemplative register)...")
tts_files = []
for i, (start_ms, body) in enumerate(TTS_LINES):
    ssml = SSML_TEMPLATE.format(body=body)
    ssml_file = f"{TMP}/tts_{i:02d}.ssml"
    out_wav   = f"{TMP}/tts_{i:02d}.wav"
    Path(ssml_file).write_text(ssml)
    subprocess.run([
        "espeak-ng", "-v", "en-gb-x-rp",
        "-m", "-a", "92",
        "-f", ssml_file,
        "-w", out_wav,
    ], check=True, capture_output=True)
    dur = float(subprocess.check_output([
        "ffprobe", "-v", "quiet",
        "-show_entries", "format=duration", "-of", "csv=p=0", out_wav,
    ]).decode().strip())
    tts_files.append((out_wav, start_ms, dur))
    preview = body.replace('<', ' ').replace('>', ' ')
    preview = ' '.join(preview.split())[:38]
    print(f"  [{i}] {preview} → {dur:.2f}s @ {start_ms}ms")

# ── Step 2: Silent base ────────────────────────────────────────────────────
print("Creating silence base...")
silence = f"{TMP}/silence.wav"
subprocess.run([
    "ffmpeg", "-y", "-f", "lavfi",
    "-i", "anullsrc=r=44100:cl=mono",
    "-t", f"{TOTAL_MS/1000:.3f}", silence,
], check=True, capture_output=True)

# ── Step 3: Position each TTS clip ────────────────────────────────────────
print("Building voiceover track...")
inputs  = ["-i", silence]
filters = []
mix_in  = "[0]"

for i, (wav, start_ms, _) in enumerate(tts_files):
    inputs += ["-i", wav]
    idx = i + 1
    filters.append(
        f"[{idx}]adelay={start_ms}|{start_ms},volume={TTS_VOL}[d{i}]"
    )
    mix_in += f"[d{i}]"

n_mix = len(tts_files) + 1
filters.append(
    f"{mix_in}amix=inputs={n_mix}:normalize=0:dropout_transition=0[voice]"
)

voice_track = f"{TMP}/voice.wav"
subprocess.run([
    "ffmpeg", "-y", *inputs,
    "-filter_complex", ";".join(filters),
    "-map", "[voice]", voice_track,
], check=True, capture_output=True)

# ── Step 4: Mix voice + ambient piano ─────────────────────────────────────
print("Mixing ambient music + voice...")
t   = TOTAL_MS / 1000
fin = f"{TMP}/final_audio.aac"
subprocess.run([
    "ffmpeg", "-y",
    "-i", voice_track,
    "-i", MUSIC_FILE,
    "-filter_complex",
    f"[0]volume=1.0[v];"
    f"[1]atrim=0:{t},volume={MUSIC_VOL},"
    f"afade=t=in:st=0:d=4,afade=t=out:st={t-5}:d=5[m];"
    f"[v][m]amix=inputs=2:normalize=0[out]",
    "-map", "[out]",
    "-c:a", "aac", "-b:a", "192k",
    "-t", f"{t:.3f}",
    fin,
], check=True, capture_output=True)

# ── Step 5: Compose ────────────────────────────────────────────────────────
print("Composing final video...")
subprocess.run([
    "ffmpeg", "-y",
    "-i", VIDEO_IN,
    "-i", fin,
    "-c:v", "copy",
    "-c:a", "aac", "-b:a", "192k",
    "-map", "0:v:0", "-map", "1:a:0",
    "-shortest",
    VIDEO_OUT,
], check=True, capture_output=True)

size = os.path.getsize(VIDEO_OUT) / 1024 / 1024
print(f"\nDone: {VIDEO_OUT} ({size:.1f}MB)")

for f in Path(TMP).glob("*"):
    f.unlink()
Path(TMP).rmdir()
