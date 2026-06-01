#!/usr/bin/env python3
"""
Audio Production for cmos-v5-demo.mp4
- English TTS via espeak-ng + SSML markup (en-gb-x-rp, Received Pronunciation)
  SSML gives natural prosody: strategic pauses, pitch variation, emphasis
- Background piano from assets
- Composed with video using ffmpeg
"""

import subprocess, os
from pathlib import Path

VIDEO_IN   = str(Path(__file__).parent / "cmos-v5-demo.mp4")
VIDEO_OUT  = str(Path(__file__).parent / "cmos-v5-demo-audio.mp4")
MUSIC_FILE = str(Path(__file__).parent / "skills/video-podcast-maker/assets/snow-stevekaldes-piano-397491.mp3")
TMP        = "/tmp/cmos-v5-audio"
os.makedirs(TMP, exist_ok=True)

# Each entry: (ssml_text, start_ms)
# SSML gives natural pause/pitch/rate control — much more expressive than plain text
# Timed to GSAP animation beats in cmos-v5-demo.html:
#   S1: CREATIVE @0.25s  MOTION @0.7s  OPERATING @1.15s  V5 @1.8s
#   S2: USER CONTENT @4.15s  ART DIRECTION @4.85s  AI GEN @5.55s  RESULT @6.15s
#   S3: header @8.2s  directors @8.55→13.05s
#   S4: label @14.55s  PENTAGRAM? @15.3s  YES. @17.2s
#   S5: CMOS @19.9s  rule @20.6s  tagline @21.3s

SSML_TEMPLATE = """<?xml version="1.0"?>
<speak xmlns="http://www.w3.org/2001/10/synthesis" version="1.0" xml:lang="en-GB">
  {body}
</speak>"""

TTS_LINES = [
    # Scene 1: Identity stack — architectural, slow, commanding
    (
        300,
        '<prosody rate="x-slow" pitch="-3st" volume="95">'
        'Creative.<break time="420ms"/>'
        'Motion.<break time="420ms"/>'
        'Operating.'
        '</prosody>',
    ),
    # Scene 2: Equation — deliberate buildup
    (
        4200,
        '<prosody rate="slow" pitch="-2st" volume="95">'
        'User content.<break time="280ms"/>'
        'Art direction.<break time="280ms"/>'
        '<emphasis level="strong">A.I. generation.</emphasis>'
        '</prosody>',
    ),
    (
        6250,
        '<prosody rate="x-slow" pitch="-4st" volume="95">'
        '<emphasis level="strong">World-class output.</emphasis>'
        '</prosody>',
    ),
    # Scene 3: Director pipeline — firm, staccato authority
    (
        8600,
        '<prosody rate="slow" pitch="-2st" volume="95">'
        'Ten directors.<break time="350ms"/>'
        'One pipeline.'
        '</prosody>',
    ),
    (
        13150,
        '<prosody rate="x-slow" pitch="-5st" volume="95">'
        'Anti-A.I. detector.'
        '</prosody>',
    ),
    # Scene 4: Quality test — tension then release
    (
        15000,
        '<prosody rate="slow" pitch="-2st" volume="95">'
        'Would this be accepted<break time="180ms"/>'
        'by <emphasis level="strong">Pentagram?</emphasis>'
        '</prosody>',
    ),
    (
        17350,
        '<prosody rate="x-slow" pitch="-6st" volume="95">'
        '<emphasis level="strong">Yes.</emphasis>'
        '</prosody>',
    ),
    # Scene 5: Final lockup — monumental
    (
        20200,
        '<prosody rate="x-slow" pitch="-4st" volume="95">'
        'C. M. O. S.<break time="400ms"/>V. 5.'
        '</prosody>',
    ),
    (
        21500,
        '<prosody rate="slow" pitch="-3st" volume="95">'
        'Every frame,<break time="250ms"/>directed.'
        '</prosody>',
    ),
]

TOTAL_MS  = 25500
MUSIC_VOL = 0.18
TTS_VOL   = 0.96

# ── Step 1: Generate SSML TTS clips ───────────────────────────────────────
print("Generating SSML TTS clips (espeak-ng en-gb-x-rp)...")
tts_files = []
for i, (start_ms, ssml_body) in enumerate(TTS_LINES):
    ssml = SSML_TEMPLATE.format(body=ssml_body)
    ssml_file = f"{TMP}/tts_{i:02d}.ssml"
    out_wav   = f"{TMP}/tts_{i:02d}.wav"
    Path(ssml_file).write_text(ssml)
    subprocess.run([
        "espeak-ng", "-v", "en-gb-x-rp",
        "-m",           # markup mode (SSML)
        "-a", "95",
        "-f", ssml_file,
        "-w", out_wav,
    ], check=True, capture_output=True)
    dur = float(subprocess.check_output([
        "ffprobe", "-v", "quiet",
        "-show_entries", "format=duration", "-of", "csv=p=0", out_wav,
    ]).decode().strip())
    tts_files.append((out_wav, start_ms, dur))
    preview = ssml_body.replace('<', ' ').replace('>', ' ')
    preview = ' '.join(preview.split())[:40]
    print(f"  [{i}] {preview}... → {dur:.2f}s @ {start_ms}ms")

# ── Step 2: Silent base track ──────────────────────────────────────────────
print("Creating silence base...")
silence = f"{TMP}/silence.wav"
subprocess.run([
    "ffmpeg", "-y", "-f", "lavfi",
    "-i", "anullsrc=r=44100:cl=mono",
    "-t", f"{TOTAL_MS/1000:.3f}", silence,
], check=True, capture_output=True)

# ── Step 3: Delay each TTS clip and amix all ──────────────────────────────
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

# ── Step 4: Mix voice + background piano ──────────────────────────────────
print("Mixing music + voice...")
t   = TOTAL_MS / 1000
fin = f"{TMP}/final_audio.aac"
subprocess.run([
    "ffmpeg", "-y",
    "-i", voice_track,
    "-i", MUSIC_FILE,
    "-filter_complex",
    f"[0]volume=1.0[v];"
    f"[1]atrim=0:{t},volume={MUSIC_VOL},"
    f"afade=t=in:st=0:d=2,afade=t=out:st={t-3}:d=3[m];"
    f"[v][m]amix=inputs=2:normalize=0[out]",
    "-map", "[out]",
    "-c:a", "aac", "-b:a", "192k",
    "-t", f"{t:.3f}",
    fin,
], check=True, capture_output=True)

# ── Step 5: Compose video + audio ─────────────────────────────────────────
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
