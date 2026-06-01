#!/usr/bin/env python3
"""
Audio for silence-of-matter-v2.mp4
5 SSML TTS lines timed to the v2 GSAP timeline:
  S2 text @ 9.2s    "There is no urgency here."
  S3 text @ 16.5s   "Only matter, as it is."
  S3 cap  @ 19.8s   "texture defines memory."  (very quiet)
  S5 text @ 34.5s   "Form disappears. Essence remains."
  S6 text @ 42.8s   "A quiet study of material."
"""

import subprocess, os
from pathlib import Path

VIDEO_IN   = str(Path(__file__).parent / "silence-of-matter-v2.mp4")
VIDEO_OUT  = str(Path(__file__).parent / "silence-of-matter-v2-audio.mp4")
MUSIC_FILE = str(Path(__file__).parent / "skills/video-podcast-maker/assets/snow-stevekaldes-piano-397491.mp3")
TMP        = "/tmp/silence-v2-audio"
os.makedirs(TMP, exist_ok=True)

SSML_TEMPLATE = """<?xml version="1.0"?>
<speak xmlns="http://www.w3.org/2001/10/synthesis" version="1.0" xml:lang="en-GB">
  {body}
</speak>"""

TTS_LINES = [
    (9200,
     '<prosody rate="x-slow" pitch="-6st" volume="90">'
     'There is no urgency<break time="550ms"/>here.'
     '</prosody>'),
    (16500,
     '<prosody rate="x-slow" pitch="-5st" volume="90">'
     'Only matter,<break time="600ms"/>as it is.'
     '</prosody>'),
    (19800,
     '<prosody rate="x-slow" pitch="-4st" volume="72">'
     'texture<break time="380ms"/>defines<break time="380ms"/>memory.'
     '</prosody>'),
    (34500,
     '<prosody rate="x-slow" pitch="-7st" volume="90">'
     'form disappears.<break time="1100ms"/>'
     '<emphasis level="strong">essence remains.</emphasis>'
     '</prosody>'),
    (42800,
     '<prosody rate="x-slow" pitch="-6st" volume="88">'
     'A quiet study<break time="500ms"/>of material.'
     '</prosody>'),
]

TOTAL_MS  = 45000
MUSIC_VOL = 0.095
TTS_VOL   = 0.94

print("Generating SSML TTS (en-gb-x-rp)...")
tts_files = []
for i, (start_ms, body) in enumerate(TTS_LINES):
    ssml = SSML_TEMPLATE.format(body=body)
    ssml_f = f"{TMP}/t{i}.ssml"
    wav_f  = f"{TMP}/t{i}.wav"
    Path(ssml_f).write_text(ssml)
    subprocess.run(["espeak-ng", "-v", "en-gb-x-rp", "-m", "-a", "90",
                    "-f", ssml_f, "-w", wav_f], check=True, capture_output=True)
    dur = float(subprocess.check_output(
        ["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
         "-of", "csv=p=0", wav_f]).decode().strip())
    tts_files.append((wav_f, start_ms, dur))
    print(f"  [{i}] → {dur:.2f}s @ {start_ms}ms")

print("Building silence base...")
sil = f"{TMP}/silence.wav"
subprocess.run(["ffmpeg", "-y", "-f", "lavfi", "-i",
                f"anullsrc=r=44100:cl=mono", "-t",
                f"{TOTAL_MS/1000:.3f}", sil], check=True, capture_output=True)

print("Mixing voice track...")
inputs  = ["-i", sil]
filters = []
mix_in  = "[0]"
for i, (wav, start_ms, _) in enumerate(tts_files):
    inputs += ["-i", wav]
    filters.append(f"[{i+1}]adelay={start_ms}|{start_ms},volume={TTS_VOL}[d{i}]")
    mix_in += f"[d{i}]"
filters.append(f"{mix_in}amix=inputs={len(tts_files)+1}:normalize=0:dropout_transition=0[voice]")
voice = f"{TMP}/voice.wav"
subprocess.run(["ffmpeg", "-y", *inputs, "-filter_complex", ";".join(filters),
                "-map", "[voice]", voice], check=True, capture_output=True)

print("Mixing music...")
t   = TOTAL_MS / 1000
fin = f"{TMP}/final.aac"
subprocess.run(["ffmpeg", "-y",
    "-i", voice, "-i", MUSIC_FILE,
    "-filter_complex",
    f"[0]volume=1.0[v];[1]atrim=0:{t},volume={MUSIC_VOL},"
    f"afade=t=in:st=0:d=4,afade=t=out:st={t-5}:d=5[m];"
    f"[v][m]amix=inputs=2:normalize=0[out]",
    "-map", "[out]", "-c:a", "aac", "-b:a", "192k",
    "-t", f"{t:.3f}", fin], check=True, capture_output=True)

print("Composing final video...")
subprocess.run(["ffmpeg", "-y",
    "-i", VIDEO_IN, "-i", fin,
    "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
    "-map", "0:v:0", "-map", "1:a:0", "-shortest",
    VIDEO_OUT], check=True, capture_output=True)

size = os.path.getsize(VIDEO_OUT) / 1024 / 1024
print(f"\nDone: {VIDEO_OUT} ({size:.1f}MB)")

for f in Path(TMP).glob("*"): f.unlink()
Path(TMP).rmdir()
