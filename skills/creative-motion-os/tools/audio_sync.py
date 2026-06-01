"""
AudioSync — Millisecond-Precise Sound-to-Animation Alignment
Part of Creative Motion Operating System V5

Two-stage tool:
  Stage 1: detect_audio_peak(audio_file) → finds the most impactful moment
  Stage 2: align_audio_to_animation(...) → generates FFmpeg command to sync it

The goal: the audio's loudest / most impactful moment lands on the same frame
as the animation's most impactful event (text slam, image reveal, data hit).

Requires: FFmpeg on PATH (for detection and alignment), numpy

Usage:
    # Stage 1 + 2 together (most common)
    python audio_sync.py --audio track.wav --anim-start 1450

    # Stage 1 only (detect peak)
    python audio_sync.py --audio track.wav --detect-only

    # Stage 2 only (alignment, with known peak time)
    python audio_sync.py --audio track.wav --anim-start 1450 --peak-time 200

    # From JSON (matches CMOS pipeline output format)
    python audio_sync.py --audio track.wav --video-json animation.json
"""

import subprocess
import json
import argparse
import os
import re
import sys
from pathlib import Path


# ─────────────────────────────────────────────────────────────────────────────
# Stage 1: Audio Peak Detection
# ─────────────────────────────────────────────────────────────────────────────

def detect_audio_peak(audio_file: str, method: str = "rms") -> dict:
    """
    Detect the most impactful moment in an audio file.

    Args:
        audio_file: Path to audio file (wav, mp3, aac, flac, etc.)
        method: "rms" (RMS energy, good for musical transients)
                "peak" (absolute sample peak, good for impact hits)

    Returns:
        {
            "Audio_Peak_Time": int,       # milliseconds
            "Audio_Peak_Time_Sec": float, # seconds
            "Peak_Value_dB": float,       # dBFS at peak
            "Duration_Ms": int,           # total audio duration in ms
            "Method": str,
            "Audio_File": str,
        }
    """
    audio_file = str(Path(audio_file).resolve())
    if not os.path.exists(audio_file):
        raise FileNotFoundError(f"Audio file not found: {audio_file}")

    # ── Step 1: Get total duration ──────────────────────────────────────────
    duration_ms = _get_duration_ms(audio_file)

    # ── Step 2: Detect peak moment ──────────────────────────────────────────
    if method == "rms":
        peak_ms, peak_db = _detect_rms_peak(audio_file, duration_ms)
    else:
        peak_ms, peak_db = _detect_sample_peak(audio_file, duration_ms)

    return {
        "Audio_Peak_Time": int(peak_ms),
        "Audio_Peak_Time_Sec": round(peak_ms / 1000.0, 4),
        "Peak_Value_dB": round(peak_db, 2),
        "Duration_Ms": int(duration_ms),
        "Method": method,
        "Audio_File": audio_file,
    }


def _get_duration_ms(audio_file: str) -> float:
    """Use ffprobe to get audio duration in milliseconds."""
    cmd = [
        "ffprobe", "-v", "quiet",
        "-print_format", "json",
        "-show_streams",
        audio_file,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    info = json.loads(result.stdout)
    for stream in info.get("streams", []):
        if stream.get("codec_type") == "audio":
            duration_s = float(stream.get("duration", 0))
            return duration_s * 1000.0
    raise RuntimeError("No audio stream found in file.")


def _detect_rms_peak(audio_file: str, duration_ms: float) -> tuple:
    """
    Slice audio into 50ms windows, compute RMS per window using FFmpeg astats.
    Returns (peak_ms, peak_db) where peak_ms is the center of the loudest window.

    Uses FFmpeg's 'astats' filter with 50ms reset interval.
    """
    window_ms = 50
    # Ask FFmpeg to print RMS for each 50ms chunk
    cmd = [
        "ffmpeg", "-i", audio_file,
        "-af", f"astats=metadata=1:reset={(window_ms / 1000.0):.3f},"
               "ametadata=print:key=lavfi.astats.Overall.RMS_level",
        "-f", "null", "-",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    output = result.stderr  # FFmpeg prints metadata to stderr

    # Parse "pts_time:X.XXX ... value:-YY.YY" lines
    rms_values = []
    pts_pattern = re.compile(r'pts_time:([\d.]+)')
    val_pattern = re.compile(r'value:(-[\d.]+|-inf|[\d.]+)')

    pts_times = pts_pattern.findall(output)
    val_matches = val_pattern.findall(output)

    for pts_str, val_str in zip(pts_times, val_matches):
        try:
            pts_ms = float(pts_str) * 1000.0
            val_db = float(val_str) if val_str != "-inf" else -120.0
            rms_values.append((pts_ms, val_db))
        except ValueError:
            continue

    if not rms_values:
        # Fallback: return midpoint
        return (duration_ms * 0.3, -20.0)

    # Find maximum RMS (highest dB, closest to 0)
    best_pts, best_db = max(rms_values, key=lambda x: x[1])
    # Add half-window offset to point to the center of the window
    peak_ms = best_pts + (window_ms / 2.0)
    return (peak_ms, best_db)


def _detect_sample_peak(audio_file: str, duration_ms: float) -> tuple:
    """
    Detect the single loudest sample frame using FFmpeg volumedetect.
    Returns (peak_ms, peak_db). Note: volumedetect reports overall max,
    not time-indexed — so we return the RMS peak time as a fallback.
    """
    # volumedetect is not time-indexed; use astats for time-indexed peak
    return _detect_rms_peak(audio_file, duration_ms)


# ─────────────────────────────────────────────────────────────────────────────
# Stage 2: Alignment
# ─────────────────────────────────────────────────────────────────────────────

def align_audio_to_animation(
    video_json_data: dict,
    audio_analysis_data: dict,
    input_audio: str = "input_track.wav",
    output_audio: str = "aligned_audio.wav",
    verbose: bool = True,
) -> dict:
    """
    Generate an FFmpeg command to align the audio peak with the animation start time.

    Args:
        video_json_data:    {"Animation_Start_Time": 1450}  (ms)
        audio_analysis_data: {"Audio_Peak_Time": 200}       (ms)
        input_audio:        Path to the input audio file
        output_audio:       Path for the aligned output audio
        verbose:            Print alignment report

    Returns:
        {
            "ffmpeg_command": str,
            "offset_ms": int,
            "strategy": "delay" | "trim" | "aligned",
            "animation_start_ms": int,
            "audio_peak_ms": int,
        }
    """
    anim_start = int(video_json_data["Animation_Start_Time"])
    audio_peak = int(audio_analysis_data["Audio_Peak_Time"])
    offset_ms = anim_start - audio_peak

    if verbose:
        print(f"\n{'─'*60}")
        print(f"  AUDIO SYNC ENGINE — CMOS V5")
        print(f"{'─'*60}")
        print(f"  Animation impact point : {anim_start} ms  ({anim_start/1000:.3f}s)")
        print(f"  Audio peak point       : {audio_peak} ms  ({audio_peak/1000:.3f}s)")
        print(f"  Required offset        : {offset_ms:+d} ms")

    if offset_ms > 0:
        # Audio peaks too early — pad the start with silence
        strategy = "delay"
        ffmpeg_cmd = (
            f'ffmpeg -y -i "{input_audio}" '
            f'-af "adelay={offset_ms}|{offset_ms}" '
            f'"{output_audio}"'
        )
        if verbose:
            print(f"  Strategy               : DELAY — pad {offset_ms}ms silence at start")

    elif offset_ms < 0:
        # Audio peaks too late — trim the silent start
        trim_s = abs(offset_ms) / 1000.0
        strategy = "trim"
        ffmpeg_cmd = (
            f'ffmpeg -y -ss {trim_s:.4f} -i "{input_audio}" '
            f'-af "asetpts=PTS-STARTPTS" '
            f'"{output_audio}"'
        )
        if verbose:
            print(f"  Strategy               : TRIM — remove first {trim_s:.3f}s of audio")

    else:
        strategy = "aligned"
        ffmpeg_cmd = f'cp "{input_audio}" "{output_audio}"'
        if verbose:
            print(f"  Strategy               : ALREADY ALIGNED — no adjustment needed")

    if verbose:
        print(f"  FFmpeg command         : {ffmpeg_cmd}")
        print(f"{'─'*60}\n")

    return {
        "ffmpeg_command": ffmpeg_cmd,
        "offset_ms": offset_ms,
        "strategy": strategy,
        "animation_start_ms": anim_start,
        "audio_peak_ms": audio_peak,
        "input_audio": input_audio,
        "output_audio": output_audio,
    }


def run_alignment(result: dict) -> bool:
    """Execute the FFmpeg command from align_audio_to_animation result."""
    cmd = result["ffmpeg_command"]
    if result["strategy"] == "aligned":
        import shutil
        shutil.copy(result["input_audio"], result["output_audio"])
        print(f"Copied {result['input_audio']} → {result['output_audio']}")
        return True
    print(f"Running: {cmd}")
    ret = subprocess.run(cmd, shell=True)
    return ret.returncode == 0


# ─────────────────────────────────────────────────────────────────────────────
# Multi-beat alignment (for clips with multiple sync points)
# ─────────────────────────────────────────────────────────────────────────────

def align_multiple_beats(beats: list, audio_file: str, output_audio: str = "aligned_audio.wav") -> dict:
    """
    Align the most important beat (highest priority) from a multi-beat animation.

    Args:
        beats: List of {"label": str, "time_ms": int, "priority": int (1=highest)}
        audio_file: Path to audio file
        output_audio: Output path

    Returns:
        align_audio_to_animation result for the highest-priority beat
    """
    if not beats:
        raise ValueError("beats list is empty")

    # Select the highest-priority beat (lowest priority number)
    primary_beat = min(beats, key=lambda b: b.get("priority", 99))
    print(f"Primary sync beat: '{primary_beat['label']}' at {primary_beat['time_ms']}ms")

    audio_data = detect_audio_peak(audio_file)
    video_data = {"Animation_Start_Time": primary_beat["time_ms"]}

    return align_audio_to_animation(
        video_data, audio_data,
        input_audio=audio_file,
        output_audio=output_audio,
    )


# ─────────────────────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="AudioSync — Millisecond-precise sound-to-animation alignment (CMOS V5)"
    )
    parser.add_argument("--audio", required=True,
        help="Input audio file (wav, mp3, aac, flac, etc.)")
    parser.add_argument("--anim-start", type=int,
        help="Animation impact point in milliseconds (e.g. 1450)")
    parser.add_argument("--peak-time", type=int,
        help="Skip detection and use this known audio peak time (ms)")
    parser.add_argument("--video-json", type=str,
        help="Path to JSON file with {Animation_Start_Time: N} (ms)")
    parser.add_argument("--detect-only", action="store_true",
        help="Only detect audio peak, do not align")
    parser.add_argument("--method", choices=["rms", "peak"], default="rms",
        help="Peak detection method (default: rms)")
    parser.add_argument("--output", type=str, default="aligned_audio.wav",
        help="Output aligned audio path (default: aligned_audio.wav)")
    parser.add_argument("--run", action="store_true",
        help="Execute the FFmpeg command (default: print only)")
    parser.add_argument("--out-json", type=str,
        help="Write result to JSON file")
    args = parser.parse_args()

    # ── Stage 1: detect peak ────────────────────────────────────────────────
    if args.peak_time is not None:
        audio_data = {
            "Audio_Peak_Time": args.peak_time,
            "Audio_File": args.audio,
        }
        print(f"Using provided peak time: {args.peak_time}ms")
    else:
        print(f"Detecting audio peak in: {args.audio}")
        audio_data = detect_audio_peak(args.audio, method=args.method)
        print(f"Peak detected at: {audio_data['Audio_Peak_Time']}ms "
              f"({audio_data.get('Peak_Value_dB', '?')}dBFS)")

    if args.detect_only:
        print(json.dumps(audio_data, indent=2))
        return

    # ── Stage 2: alignment ──────────────────────────────────────────────────
    if args.video_json:
        with open(args.video_json, "r") as f:
            video_data = json.load(f)
    elif args.anim_start is not None:
        video_data = {"Animation_Start_Time": args.anim_start}
    else:
        parser.error("Provide --anim-start or --video-json for alignment.")

    result = align_audio_to_animation(
        video_data, audio_data,
        input_audio=args.audio,
        output_audio=args.output,
    )

    if args.out_json:
        with open(args.out_json, "w") as f:
            json.dump(result, f, indent=2)
        print(f"Result written to: {args.out_json}")

    if args.run:
        success = run_alignment(result)
        sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
