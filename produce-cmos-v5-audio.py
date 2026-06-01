#!/usr/bin/env python3
"""
Audio Production for cmos-v5-demo.mp4
- English TTS via espeak-ng (en-gb-x-rp, Received Pronunciation)
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

# (text, start_ms, speed_wpm, pitch)
# Timed to GSAP animation beats in cmos-v5-demo.html
TTS_LINES = [
    # S1: CREATIVE/MOTION/OPERATING stack 0.25→1.8s — three words staggered
    ("Creative. Motion. Operating.",          300,  120, 52),
    # S2: Equation 4.15→6.15s — elements arrive left-staggered
    ("User content. Art direction. AI generation.", 4150, 125, 52),
    ("World-class output.",                  6200,  118, 50),
    # S3: Director roll header 8.2s, last director at 13.05s
    ("Ten directors. One pipeline.",          8500,  122, 52),
    ("Anti-AI detector.",                    13100,  115, 48),
    # S4: Quality test — question then YES. slam at 17.2s
    ("Would this be accepted by Pentagram?", 14950,  118, 50),
    ("Yes.",                                 17300,  100, 46),
    # S5: Final lockup — CMOS appears 19.9s, tagline 21.3s
    ("C. M. O. S.  V5.",                    20100,  108, 48),
    ("Every frame, directed.",               21400,  115, 50),
]

TOTAL_MS  = 25500
MUSIC_VOL = 0.20
TTS_VOL   = 0.95

# ── Step 1: Generate TTS clips ─────────────────────────────────────────────
print("Generating TTS clips...")
tts_files = []
for i, (text, start_ms, speed, pitch) in enumerate(TTS_LINES):
    out = f"{TMP}/tts_{i:02d}.wav"
    subprocess.run([
        "espeak-ng", "-v", "en-gb-x-rp",
        f"-s{speed}", f"-p{pitch}", "-a95",
        "-w", out, text,
    ], check=True, capture_output=True)
    dur = float(subprocess.check_output([
        "ffprobe", "-v", "quiet",
        "-show_entries", "format=duration", "-of", "csv=p=0", out,
    ]).decode().strip())
    tts_files.append((out, start_ms, dur))
    print(f"  [{i}] {text[:28]}... → {dur:.2f}s @ {start_ms}ms")

# ── Step 2: Silent base track ──────────────────────────────────────────────
print("Creating silence base...")
silence = f"{TMP}/silence.wav"
subprocess.run([
    "ffmpeg", "-y", "-f", "lavfi",
    "-i", "anullsrc=r=44100:cl=mono",
    "-t", f"{TOTAL_MS/1000:.3f}", silence
], check=True, capture_output=True)

# ── Step 3: Delay each TTS clip and mix ───────────────────────────────────
print("Building voiceover track...")
inputs  = ["-i", silence]
filters = []
mix_in  = "[0]"

for i, (tts_f, start_ms, _dur) in enumerate(tts_files):
    inputs += ["-i", tts_f]
    idx = i + 1
    filters.append(f"[{idx}]adelay={start_ms}|{start_ms},volume={TTS_VOL}[d{i}]")
    mix_in += f"[d{i}]"

n_mix = len(tts_files) + 1
filters.append(f"{mix_in}amix=inputs={n_mix}:normalize=0:dropout_transition=0[voice]")

voice_track = f"{TMP}/voice.wav"
subprocess.run([
    "ffmpeg", "-y", *inputs,
    "-filter_complex", ";".join(filters),
    "-map", "[voice]", voice_track
], check=True, capture_output=True)

# ── Step 4: Mix voice + background piano ──────────────────────────────────
print("Mixing music + voice...")
final_audio = f"{TMP}/final_audio.aac"
subprocess.run([
    "ffmpeg", "-y",
    "-i", voice_track,
    "-i", MUSIC_FILE,
    "-filter_complex",
    f"[0]volume=1.0[v];[1]atrim=0:{TOTAL_MS/1000},volume={MUSIC_VOL},"
    f"afade=t=in:st=0:d=1.5,afade=t=out:st={TOTAL_MS/1000-2.5}:d=2.5[m];"
    f"[v][m]amix=inputs=2:normalize=0[out]",
    "-map", "[out]",
    "-c:a", "aac", "-b:a", "192k",
    "-t", f"{TOTAL_MS/1000:.3f}",
    final_audio
], check=True, capture_output=True)

# ── Step 5: Compose video + audio ─────────────────────────────────────────
print("Composing final video...")
subprocess.run([
    "ffmpeg", "-y",
    "-i", VIDEO_IN,
    "-i", final_audio,
    "-c:v", "copy",
    "-c:a", "aac", "-b:a", "192k",
    "-map", "0:v:0", "-map", "1:a:0",
    "-shortest",
    VIDEO_OUT
], check=True, capture_output=True)

size = os.path.getsize(VIDEO_OUT) / 1024 / 1024
print(f"\nDone: {VIDEO_OUT} ({size:.1f}MB)")

for f in Path(TMP).glob("*"):
    f.unlink()
Path(TMP).rmdir()
