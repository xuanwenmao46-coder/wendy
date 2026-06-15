"""
Medeo Brand Motion Video audio generator.

Creates a 60-second electronic BGM bed plus short SFX cues used by index.html.
Uses only the Python standard library so the project has no Python dependency.
Run from this directory:

    python3 gen_audio.py
"""

import math
import os
import random
import struct
import wave

SR = 44100
BPM = 130
BEAT = 60.0 / BPM
random.seed(42)


def clamp(value):
    return max(-1.0, min(1.0, value))


def write_wav(path, samples, stereo=False):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with wave.open(path, "wb") as handle:
        handle.setnchannels(2 if stereo else 1)
        handle.setsampwidth(2)
        handle.setframerate(SR)
        frames = bytearray()
        if stereo:
            for left, right in samples:
                frames.extend(struct.pack("<hh", int(clamp(left) * 32767), int(clamp(right) * 32767)))
        else:
            for sample in samples:
                frames.extend(struct.pack("<h", int(clamp(sample) * 32767)))
        handle.writeframes(frames)


def exp_env(t, speed):
    return math.exp(-t * speed)


def low_noise():
    return random.uniform(-1.0, 1.0)


def make_bgm():
    duration = 60.0
    total = int(duration * SR)
    bass_notes = [55.0, 55.0, 82.41, 55.0, 49.0, 55.0, 43.65, 82.41]
    chords = [
        (220.0, 261.63, 329.63),
        (174.61, 220.0, 261.63),
        (130.81, 164.81, 196.0),
        (196.0, 246.94, 293.66),
    ]
    out = []
    prev_left = 0.0
    prev_right = 0.0
    for i in range(total):
        t = i / SR
        beat_phase = t % BEAT
        eighth = int(t / (BEAT / 2))
        sixteenth_phase = t % (BEAT / 4)
        sample = 0.0

        if beat_phase < 0.18:
            p = beat_phase / 0.18
            freq = 155.0 - 115.0 * p
            sample += 0.75 * exp_env(beat_phase, 13.0) * math.sin(2.0 * math.pi * freq * beat_phase)

        if (int(t / BEAT) % 2 == 1) and beat_phase < 0.10:
            sample += 0.20 * exp_env(beat_phase, 22.0) * low_noise()

        if sixteenth_phase < 0.038:
            sample += 0.07 * exp_env(sixteenth_phase, 65.0) * low_noise()

        note = bass_notes[eighth % len(bass_notes)]
        note_phase = t % (BEAT / 2)
        sample += 0.20 * exp_env(note_phase, 7.0) * (
            math.sin(2.0 * math.pi * note * t) + 0.35 * math.sin(2.0 * math.pi * note * 2.0 * t)
        )

        chord = chords[int(t / (4 * BEAT)) % len(chords)]
        pad = 0.0
        for freq in chord:
            pad += math.sin(2.0 * math.pi * freq * t) + 0.5 * math.sin(2.0 * math.pi * (freq + 0.37) * t)
        sample += 0.025 * pad

        arp = [110.0, 164.81, 130.81, 196.0, 146.83, 196.0, 130.81, 164.81]
        arp_freq = arp[int(t / (BEAT / 4)) % len(arp)]
        sample += 0.055 * exp_env(sixteenth_phase, 18.0) * math.sin(2.0 * math.pi * arp_freq * t)

        # Soft low-pass smoothing and delayed right channel for width.
        prev_left = prev_left * 0.82 + sample * 0.18
        prev_right = prev_right * 0.84 + sample * 0.16
        out.append((prev_left * 0.72, prev_right * 0.68))
    write_wav("audio/bgm.wav", out, stereo=True)


def make_impact():
    total = int(0.60 * SR)
    return [
        (
            0.85 * exp_env(i / SR, 8.0) * math.sin(2.0 * math.pi * (82.0 - 44.0 * (i / total)) * (i / SR))
            + 0.25 * exp_env(i / SR, 38.0) * low_noise()
        )
        for i in range(total)
    ]


def make_whoosh(duration=0.34):
    total = int(duration * SR)
    data = []
    prev = 0.0
    for i in range(total):
        t = i / SR
        env = math.sin(math.pi * t / duration) ** 0.7
        prev = prev * 0.76 + low_noise() * 0.24
        data.append(prev * env * 0.55)
    return data


def make_tick(duration=0.06):
    total = int(duration * SR)
    return [0.65 * exp_env(i / SR, 85.0) * (0.6 * math.sin(2.0 * math.pi * 2200.0 * (i / SR)) + 0.4 * low_noise()) for i in range(total)]


def make_type():
    total = int(0.12 * SR)
    return [0.45 * exp_env(i / SR, 45.0) * (math.sin(2.0 * math.pi * 1800.0 * (i / SR)) + 0.35 * low_noise()) for i in range(total)]


def make_acid_sweep():
    total = int(0.28 * SR)
    data = []
    for i in range(total):
        t = i / SR
        p = i / max(1, total - 1)
        freq = 260.0 + 2100.0 * p
        env = math.sin(math.pi * p)
        data.append(0.50 * env * math.sin(2.0 * math.pi * freq * t))
    return data


def make_matrix():
    total = int(8.0 * SR)
    data = [0.0] * total
    for start in range(0, total, int(0.12 * SR)):
        dur = int(0.055 * SR)
        freq = 780.0 + ((start // int(0.12 * SR)) % 7) * 180.0
        for j in range(dur):
            idx = start + j
            if idx >= total:
                break
            data[idx] += 0.22 * exp_env(j / SR, 24.0) * math.sin(2.0 * math.pi * freq * (j / SR))
    return [sample + 0.025 * math.sin(2.0 * math.pi * 2.0 * (i / SR)) * low_noise() for i, sample in enumerate(data)]


def make_collapse():
    total = int(7.0 * SR)
    data = []
    for i in range(total):
        t = i / SR
        p = i / max(1, total - 1)
        sub = 0.65 * exp_env(t, 2.1) * math.sin(2.0 * math.pi * (64.0 - 42.0 * p) * t)
        sweep = 0.25 * math.exp(-((t - 1.1) ** 2) / 0.38) * math.sin(2.0 * math.pi * (1900.0 - 1750.0 * p) * t)
        data.append(sub + sweep + 0.09 * exp_env(t, 2.5) * low_noise())
    return data


def main():
    make_bgm()
    write_wav("audio/sfx-impact.wav", make_impact())
    write_wav("audio/sfx-whoosh.wav", make_whoosh())
    write_wav("audio/sfx-tick.wav", make_tick())
    write_wav("audio/sfx-type.wav", make_type())
    write_wav("audio/sfx-acid-sweep.wav", make_acid_sweep())
    write_wav("audio/sfx-matrix.wav", make_matrix())
    write_wav("audio/sfx-collapse.wav", make_collapse())
    print("Generated audio/bgm.wav and 7 SFX files.")


if __name__ == "__main__":
    main()
