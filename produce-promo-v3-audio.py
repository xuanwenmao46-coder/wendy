#!/usr/bin/env python3
"""
Audio Production for promo-v3.mp4
- Chinese TTS via espeak-ng (offline, Mandarin cmn)
- Background music from assets
- Compose with video using ffmpeg
"""

import subprocess, os, json
from pathlib import Path

# ── Config ─────────────────────────────────────────────────────────────────
VIDEO_IN   = str(Path(__file__).parent / "promo-v3.mp4")
VIDEO_OUT  = str(Path(__file__).parent / "promo-v3-audio.mp4")
MUSIC_FILE = str(Path(__file__).parent / "skills/video-podcast-maker/assets/snow-stevekaldes-piano-397491.mp3")
TMP        = "/tmp/promo-v3-audio"
os.makedirs(TMP, exist_ok=True)

# TTS: (text, start_ms, speed_wpm, pitch)
# Timed to match the animation scenes in promo-v3.html
TTS_LINES = [
    ("想法很多，成片总卡住。",               900,  145, 58),
    ("脚本、画面、节奏，被拆成一堆零散任务。", 4600,  140, 55),
    ("输入主题，创作引擎启动。",              9600,  145, 58),
    ("系统自动处理全部流程。",               14200, 150, 58),
    ("脚本、画面、动效，连续编排。",          19300, 145, 58),
    ("把复杂交给系统，",                     22600, 135, 55),
    ("把表达，留给你。",                     24400, 130, 52),
    ("开始创作。",                           27800, 140, 55),
]

TOTAL_MS  = 31000    # video duration + small tail
MUSIC_VOL = 0.18     # background music level (under TTS)
TTS_VOL   = 0.92     # TTS level

# ── Step 1: Generate TTS clips ─────────────────────────────────────────────
print("Generating TTS clips...")
tts_files = []
for i, (text, start_ms, speed, pitch) in enumerate(TTS_LINES):
    out = f"{TMP}/tts_{i:02d}.wav"
    subprocess.run([
        "espeak-ng", "-v", "cmn",
        f"-s{speed}", f"-p{pitch}", "-a95",
        "-w", out, text,
    ], check=True, capture_output=True)
    dur = float(subprocess.check_output([
        "ffprobe", "-v", "quiet",
        "-show_entries", "format=duration", "-of", "csv=p=0", out,
    ]).decode().strip())
    tts_files.append((out, start_ms, dur))
    print(f"  [{i}] {text[:16]}... → {dur:.2f}s (starts at {start_ms}ms)")

# ── Step 2: Create silent base track (full video duration) ─────────────────
print("Creating silence base...")
silence = f"{TMP}/silence.wav"
subprocess.run([
    "ffmpeg", "-y", "-f", "lavfi",
    "-i", f"anullsrc=r=44100:cl=mono",
    "-t", f"{TOTAL_MS/1000:.3f}", silence
], check=True, capture_output=True)

# ── Step 3: Delay each TTS clip and mix all ────────────────────────────────
print("Building voiceover track...")
# Build one big filter_complex
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
print(f"  Voiceover: {voice_track}")

# ── Step 4: Mix voice + background music ───────────────────────────────────
print("Mixing music + voice...")
final_audio = f"{TMP}/final_audio.aac"
subprocess.run([
    "ffmpeg", "-y",
    "-i", voice_track,
    "-i", MUSIC_FILE,
    "-filter_complex",
    f"[0]volume=1.0[v];[1]atrim=0:{TOTAL_MS/1000},volume={MUSIC_VOL},afade=t=out:st={TOTAL_MS/1000-2}:d=2[m];[v][m]amix=inputs=2:normalize=0[out]",
    "-map", "[out]",
    "-c:a", "aac", "-b:a", "192k",
    "-t", f"{TOTAL_MS/1000:.3f}",
    final_audio
], check=True, capture_output=True)
print(f"  Mixed: {final_audio}")

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

# Cleanup
for f in Path(TMP).glob("*"):
    f.unlink()
Path(TMP).rmdir()
