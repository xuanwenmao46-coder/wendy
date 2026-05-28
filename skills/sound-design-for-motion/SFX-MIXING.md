# SFX Mixing Reference

## Sound Selection

Map visual jobs to sound categories:

| Visual job | Preferred SFX | Timing note |
| --- | --- | --- |
| Fast title/card movement | whoosh | Start 2-6 frames before the visual lands |
| Product, number, or claim reveal | impact | Land exactly on the reveal frame |
| HUD panel or UI module change | ui_click/interface | Keep short and lower volume |
| Scene slash, broadcast cut, signal marker | stinger | Use sparingly; it becomes a punctuation mark |
| Scan, flicker, glitch, data error | digital/glitch | Use short bursts, not continuous noise |

## Volume Starting Points

Use these as first-pass values:

```text
whoosh: 0.24-0.48
impact: 0.36-0.72
low impact: 0.32-0.62
ui click: 0.28-0.55
stinger: 0.22-0.42
```

Always add a limiter after mixing:

```text
alimiter=limit=0.92
```

## FFmpeg Mix Pattern

This pattern creates a silent stereo bed, delays each SFX, mixes them, and copies the video stream:

```bash
ffmpeg -y \
  -i input.silent.mp4 \
  -i whoosh.mp3 \
  -i hit.mp3 \
  -filter_complex "anullsrc=channel_layout=stereo:sample_rate=48000:d=7[base];[1:a]aresample=48000,volume=0.35,adelay=420|420[a1];[2:a]aresample=48000,volume=0.58,adelay=920|920[a2];[base][a1][a2]amix=inputs=3:duration=first:normalize=0,alimiter=limit=0.92[aout]" \
  -map 0:v:0 -map "[aout]" \
  -c:v copy -c:a aac -b:a 192k -shortest \
  output.mp4
```

## Python Script Pattern

For multiple clips, prefer a script with a `CLIPS` list:

```python
CLIPS = [
    {
        "video": ROOT / "01-example" / "01-example.mp4",
        "events": [
            (0.10, "whoosh_scifi.mp3", 0.45),
            (0.92, "impact_low.mp3", 0.62),
            (2.08, "ui_click.mp3", 0.42),
        ],
    },
]
```

Rules:

- Copy `clip.mp4` to `clip.silent.mp4` before first mix.
- If `clip.silent.mp4` already exists, use it as the clean source.
- Write to `clip.with-sfx.tmp.mp4`, then replace the final file.
- Fail if any referenced SFX file is missing.
- Run `ffprobe` after each output and fail if no audio stream exists.

## Verification

Check one file:

```bash
ffprobe -v error -select_streams a -show_entries stream=codec_name,channels -of csv=p=0 clip.mp4
```

Expected:

```text
aac,2
```

Check a gallery:

```bash
python -c "import subprocess, pathlib; root=pathlib.Path('clips-lab/flagship-motion-clips'); videos=sorted(v for v in root.glob('*/*.mp4') if not v.name.endswith('.silent.mp4')); [print(v, subprocess.check_output(['ffprobe','-v','error','-select_streams','a','-show_entries','stream=codec_name,channels','-of','csv=p=0',str(v)], text=True).strip()) for v in videos]"
```

## HTML Gallery

If the MP4s now contain sound and the user expects to hear it:

```html
<video src="clip.mp4" controls loop playsinline></video>
```

Remove `muted` unless the gallery is designed for silent autoplay.

## License Notes

For downloaded audio, keep a manifest with:

- filename
- source page
- license
- category
- intended use
- download or resolved URL when available

Do not redistribute raw SFX as a standalone sample pack unless the license allows it. Using SFX inside rendered videos is usually different from reselling the audio files themselves.
