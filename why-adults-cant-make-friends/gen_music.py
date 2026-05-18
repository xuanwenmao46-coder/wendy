"""
Relaxing ambient music synthesizer:
  - Piano arpeggios (harmonic overtones + natural decay)
  - Soft string pad (slow attack, chorus detune, lowpass warmth)
  - Subtle bass root notes
  - Room reverb
  - Progression: Cmaj7 → Am7 → Fmaj7 → G  (60 BPM, 4-beat chords)
"""
import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, sosfilt

SR = 44100
DUR = 75


def hz(note, octave):
    names = {'C':0,'C#':1,'D':2,'D#':3,'E':4,'F':5,'F#':6,'G':7,'G#':8,'A':9,'A#':10,'B':11}
    return 440.0 * 2 ** ((names[note] + (octave - 4) * 12) / 12.0)


def piano(freq, dur, amp=1.0):
    """Piano tone: harmonics with exponential decay."""
    n = int(SR * dur)
    t = np.arange(n, dtype=np.float64) / SR
    wave = (
        1.00 * np.sin(2*np.pi*freq*1*t) * np.exp(-t * 3.2) +
        0.55 * np.sin(2*np.pi*freq*2*t) * np.exp(-t * 5.0) +
        0.28 * np.sin(2*np.pi*freq*3*t) * np.exp(-t * 7.0) +
        0.14 * np.sin(2*np.pi*freq*4*t) * np.exp(-t * 9.5) +
        0.07 * np.sin(2*np.pi*freq*5*t) * np.exp(-t * 12.0) +
        0.03 * np.sin(2*np.pi*freq*6*t) * np.exp(-t * 15.0)
    )
    atk = max(1, int(0.008 * SR))
    wave[:atk] *= np.linspace(0, 1, atk)
    return wave * amp


def string_pad(freqs, dur, amp=1.0):
    """Warm string pad: slow attack, chorus, lowpass."""
    n = int(SR * dur)
    t = np.arange(n, dtype=np.float64) / SR
    wave = np.zeros(n)
    for f in freqs:
        wave += 0.60 * np.sin(2*np.pi * f       * t)
        wave += 0.20 * np.sin(2*np.pi * f*1.003 * t)   # slight chorus
        wave += 0.20 * np.sin(2*np.pi * f*0.997 * t)
        wave += 0.10 * np.sin(2*np.pi * f*2     * t) * 0.4  # gentle 2nd harmonic
    # Slow fade-in, smooth fade-out
    atk = min(int(2.0 * SR), n)
    rel = min(int(1.2 * SR), n)
    env = np.ones(n)
    env[:atk] = np.linspace(0, 1, atk)
    env[max(0, n-rel):] = np.linspace(1, 0, min(rel, n))
    wave *= env
    # Lowpass for warmth (cut harsh highs)
    sos = butter(4, 700.0 / (SR / 2.0), btype='low', output='sos')
    wave = sosfilt(sos, wave)
    return wave * amp


def add_reverb(sig, wet=0.38):
    """Simple plate reverb via delayed echoes."""
    delays_gains = [
        (int(SR * 0.028), 0.45),
        (int(SR * 0.065), 0.32),
        (int(SR * 0.110), 0.22),
        (int(SR * 0.170), 0.14),
        (int(SR * 0.250), 0.08),
    ]
    result = np.zeros_like(sig)
    for d, g in delays_gains:
        result[d:] += sig[:-d] * g
    return sig * (1 - wet) + result * wet


# ── Chord progression: Cmaj7 → Am7 → Fmaj7 → G ──
# Each entry: (pad_freqs, arp_freqs_low_to_high, bass_freq)
CHORDS = [
    (  # Cmaj7
        [hz('C',3), hz('E',3), hz('G',3), hz('B',3)],
        [hz('C',4), hz('E',4), hz('G',4), hz('B',4), hz('G',4), hz('E',4)],
        hz('C', 2),
    ),
    (  # Am7
        [hz('A',2), hz('C',3), hz('E',3), hz('G',3)],
        [hz('A',3), hz('C',4), hz('E',4), hz('G',4), hz('E',4), hz('C',4)],
        hz('A', 2),
    ),
    (  # Fmaj7
        [hz('F',2), hz('A',2), hz('C',3), hz('E',3)],
        [hz('F',3), hz('A',3), hz('C',4), hz('E',4), hz('C',4), hz('A',3)],
        hz('F', 2),
    ),
    (  # G  (Gsus2 color)
        [hz('G',2), hz('A',2), hz('D',3), hz('G',3)],
        [hz('G',3), hz('B',3), hz('D',4), hz('G',4), hz('D',4), hz('B',3)],
        hz('G', 2),
    ),
]

BEAT     = 60.0 / 60.0          # 1.0s — 60 BPM
CHORD_DUR = 6 * BEAT            # 6 beats per chord → spacious, unhurried
# Arp pattern: 6 notes per chord (up × 4 + down × 2), one per beat
ARP_PATTERN = [0, 1, 2, 3, 2, 1]   # indices into arp_freqs

output = np.zeros(int(SR * DUR), dtype=np.float64)


def mix_in(buf, start_s, signal):
    """Add signal into output buffer at start_s seconds."""
    s = int(start_s * SR)
    e = s + len(signal)
    if e > len(buf):
        signal = signal[:len(buf) - s]
        e = s + len(signal)
    if s >= len(buf) or len(signal) == 0:
        return
    buf[s:e] += signal


t = 0.0
chord_idx = 0
while t < DUR:
    pad_freqs, arp_freqs, bass_freq = CHORDS[chord_idx % len(CHORDS)]
    actual_dur = min(CHORD_DUR, DUR - t)

    # ── Pad layer ──
    p = string_pad(pad_freqs, actual_dur, amp=0.20)
    mix_in(output, t, p)

    # ── Bass note (root, stays for 2 beats) ──
    b = piano(bass_freq, min(2.0 * BEAT, actual_dur), amp=0.14)
    mix_in(output, t, b)

    # ── Piano arpeggio (one note per beat) ──
    for beat_i, arp_idx in enumerate(ARP_PATTERN):
        beat_t = t + beat_i * BEAT
        if beat_t >= DUR:
            break
        f = arp_freqs[arp_idx % len(arp_freqs)]
        note_dur = min(BEAT * 1.8, DUR - beat_t)   # let notes ring over next beat
        vol = 0.26 if beat_i == 0 else 0.20         # accent on beat 1
        n = piano(f, note_dur, amp=vol)
        mix_in(output, beat_t, n)

    t += CHORD_DUR
    chord_idx += 1

# ── Reverb ──
output = add_reverb(output, wet=0.40)

# ── Fade in / out ──
fi = int(4.0 * SR)
fo = int(6.0 * SR)
output[:fi]  *= np.linspace(0, 1, fi)
output[-fo:] *= np.linspace(1, 0, fo)

# ── Normalise to -3 dBFS ──
peak = np.max(np.abs(output))
if peak > 0:
    output = output / peak * 0.707

# ── Save ──
out_path = 'assets/relaxing-music.wav'
wavfile.write(out_path, SR, output.astype(np.float32))
print(f'Saved {out_path}  ({DUR}s, SR={SR})')
