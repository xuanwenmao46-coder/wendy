"""
Generate FORMA v3 audio assets.
BGM: Bicep-style hypnotic electronic — 130 BPM, 4-on-the-floor, driving, no climax.
"""
import numpy as np
import wave, struct, os

SR = 44100
OUT = os.path.join(os.path.dirname(__file__), "audio")
os.makedirs(OUT, exist_ok=True)

# ─── helpers ──────────────────────────────────────────────────────────────────
def write_mono(path, data):
    data = np.clip(data, -1, 1)
    pcm = (data * 32767).astype(np.int16)
    with wave.open(path, 'w') as f:
        f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR)
        f.writeframes(pcm.tobytes())

def write_stereo(path, L, R):
    L, R = np.clip(L, -1, 1), np.clip(R, -1, 1)
    buf = np.empty(2 * max(len(L), len(R)), dtype=np.int16)
    buf[0::2] = (L * 32767).astype(np.int16)
    buf[1::2] = (R * 32767).astype(np.int16)
    with wave.open(path, 'w') as f:
        f.setnchannels(2); f.setsampwidth(2); f.setframerate(SR)
        f.writeframes(buf.tobytes())

def t(dur): return np.linspace(0, dur, int(SR * dur), endpoint=False)

# simple first-order IIR lowpass  (fc in Hz)
def lpf(sig, fc):
    alpha = 1.0 / (1.0 + SR / (2 * np.pi * fc))
    out = np.zeros_like(sig)
    y = 0.0
    for i, x in enumerate(sig):
        y = alpha * x + (1 - alpha) * y
        out[i] = y
    return out

# fast IIR lpf with numpy cumsum trick (first-order only, stable)
def lpf_fast(sig, fc):
    alpha = 2 * np.pi * fc / SR
    alpha = min(alpha, 0.999)
    b = alpha
    a = 1 - alpha
    # Direct form I via cumsum approximation isn't exact but is fast & good enough
    out = np.zeros_like(sig, dtype=float)
    prev = 0.0
    # process in chunks of 4096
    chunk = 4096
    for start in range(0, len(sig), chunk):
        end = min(start + chunk, len(sig))
        for i in range(start, end):
            prev = b * sig[i] + a * prev
            out[i] = prev
    return out

# soft clip / saturation
def sat(sig, drive=1.2):
    return np.tanh(sig * drive) / np.tanh(drive)

# ADSR envelope
def adsr(n, A, D, S_level, R, sr=SR):
    a_n = int(A * sr); d_n = int(D * sr); r_n = int(R * sr)
    s_n = max(0, n - a_n - d_n - r_n)
    env = np.concatenate([
        np.linspace(0, 1, a_n),
        np.linspace(1, S_level, d_n),
        np.full(s_n, S_level),
        np.linspace(S_level, 0, r_n),
    ])
    return env[:n]

# ─── BGM synthesis ────────────────────────────────────────────────────────────
print("Generating bgm.wav (Bicep-style 130 BPM) ...")

BPM = 130
BEAT = 60.0 / BPM        # 0.4615s
BAR  = BEAT * 4           # 1.8462s
SXN  = BEAT / 4           # 16th note
EIGH = BEAT / 2           # 8th note
DUR  = 60.0
N    = int(SR * DUR)
T    = np.linspace(0, DUR, N, endpoint=False)

# ── Kick drum: pitch-swept sine, tight transient ──────────────────────────────
def make_kick(amp=0.88):
    dur_k = 0.45
    n_k = int(SR * dur_k)
    tk = np.linspace(0, dur_k, n_k, endpoint=False)
    freq = np.linspace(180, 38, n_k)
    freq_env = np.exp(-tk * 22)
    tone = np.sin(2 * np.pi * np.cumsum(freq / SR)) * freq_env
    # transient click
    click_env = np.exp(-tk * 90)
    click = np.sin(2 * np.pi * 900 * tk) * click_env * 0.35
    k = sat(tone + click, 1.6) * amp
    return k

kick_one = make_kick()
kick = np.zeros(N)
# 4-on-the-floor
for b in range(int(DUR / BEAT) + 1):
    s = int(b * BEAT * SR)
    e = s + len(kick_one)
    if e <= N:
        kick[s:e] += kick_one

# ── Clap / snare: filtered noise, on beats 2+4 ───────────────────────────────
rng = np.random.default_rng(17)
def make_clap():
    dur_c = 0.12
    n_c = int(SR * dur_c)
    noise = rng.normal(0, 1, n_c)
    # two-layer envelope (snap + body)
    env1 = np.exp(-np.linspace(0, 40, n_c))
    env2 = np.exp(-np.linspace(0, 18, n_c))
    c = noise * (env1 * 0.6 + env2 * 0.4)
    # bandpass ~2kHz
    c = lpf_fast(c, 4000) - lpf_fast(c, 800)
    return c * 0.48

clap_one = make_clap()
clap = np.zeros(N)
for b in range(int(DUR / BEAT) + 1):
    if b % 4 in (1, 3):   # beat 2 and 4
        s = int(b * BEAT * SR)
        e = s + len(clap_one)
        if e <= N:
            clap[s:e] += clap_one

# ── Closed hi-hat: 16th notes, slight velocity pattern ───────────────────────
def make_hat(amp):
    dur_h = 0.055
    n_h = int(SR * dur_h)
    noise = rng.normal(0, 1, n_h)
    env = np.exp(-np.linspace(0, 55, n_h))
    h = lpf_fast(noise, 12000) * env * amp
    return h

hat = np.zeros(N)
steps = int(DUR / SXN) + 1
for i in range(steps):
    # accent pattern: strong on 1, medium on 3, softer on 2/4
    pos = i % 4
    amp = [0.42, 0.22, 0.34, 0.22][pos]
    s = int(i * SXN * SR)
    hat_one = make_hat(amp)
    e = s + len(hat_one)
    if e <= N:
        hat[s:e] += hat_one

# ── Open hi-hat: offbeat 8th notes (Bicep "Glue" feel) ───────────────────────
def make_open_hat(amp):
    dur_oh = 0.22
    n_oh = int(SR * dur_oh)
    noise = rng.normal(0, 1, n_oh)
    env = np.exp(-np.linspace(0, 12, n_oh))
    oh = lpf_fast(noise, 14000) * env * amp
    return oh

oh = np.zeros(N)
for b in range(int(DUR / BEAT) + 1):
    # offbeat: halfway between beats
    s = int((b + 0.5) * BEAT * SR)
    oh_one = make_open_hat(0.18)
    e = s + len(oh_one)
    if e <= N:
        oh[s:e] += oh_one

# ── Deep bass: A minor feel, 2-bar pattern ────────────────────────────────────
# Pattern: A1(55) A1 E2(82) A1  G1(49) A1 F1(44) E2(82)
bass_notes = [55, 55, 82, 55, 49, 55, 44, 82]  # Hz, 8th note per step
bass_amps  = [1.0, 0.6, 0.9, 0.55, 0.85, 0.5, 0.8, 0.75]

def make_bass_note(freq, dur, amp):
    n_b = int(SR * dur)
    tb = np.linspace(0, dur, n_b, endpoint=False)
    # slightly detuned sines for warmth
    tone = (np.sin(2 * np.pi * freq * tb) * 0.65 +
            np.sin(2 * np.pi * freq * 1.003 * tb) * 0.25 +
            np.sin(2 * np.pi * freq * 2.0 * tb) * 0.12)
    env = adsr(n_b, 0.008, 0.12, 0.7, 0.06)
    return sat(tone * env, 1.4) * amp * 0.52

bass = np.zeros(N)
pattern_len = len(bass_notes) * EIGH  # 2 bars
for rep in range(int(DUR / pattern_len) + 2):
    for i, (freq, amp) in enumerate(zip(bass_notes, bass_amps)):
        t_start = rep * pattern_len + i * EIGH
        if t_start >= DUR:
            break
        s = int(t_start * SR)
        note = make_bass_note(freq, EIGH * 0.88, amp)
        e = s + len(note)
        if e <= N:
            bass[s:e] += note

# LP-filter bass to keep it sub/low-mid only
bass = lpf_fast(bass, 280)

# ── Chord pad: Am – F – C – G, warm detuned sines, 2-bar cycle ───────────────
# Am: A3(220) C4(262) E4(330)
# F:  F3(175) A3(220) C4(262)
# C:  C3(131) E3(165) G3(196)
# G:  G3(196) B3(247) D4(294)
chord_seq = [
    [220, 262, 330],   # Am
    [175, 220, 262],   # F
    [131, 165, 196],   # C
    [196, 247, 294],   # G
]

def make_pad_chord(freqs, dur, amp=0.11):
    n_p = int(SR * dur)
    tp = np.linspace(0, dur, n_p, endpoint=False)
    sig = np.zeros(n_p)
    for f in freqs:
        detune = [1.0, 1.004, 0.997]
        for d in detune:
            sig += np.sin(2 * np.pi * f * d * tp) * (amp / len(freqs) / len(detune))
    env = adsr(n_p, 0.15, 0.1, 0.85, 0.3)
    return sig * env

pad = np.zeros(N)
chord_dur = BAR  # each chord lasts one bar
for rep in range(int(DUR / (chord_dur * 4)) + 2):
    for i, chord_freqs in enumerate(chord_seq):
        t_start = rep * chord_dur * 4 + i * chord_dur
        if t_start >= DUR:
            break
        s = int(t_start * SR)
        p = make_pad_chord(chord_freqs, chord_dur * 1.05, 0.11)
        e = s + len(p)
        if e <= N:
            pad[s:e] += p

# LP filter pad for warmth (Bicep uses warm, not bright pads)
pad = lpf_fast(pad, 1800)

# ── Arpeggio: A minor pentatonic 16th notes (enters at bar 4 = ~7.4s) ────────
# A2=110, C3=131, D3=147, E3=165, G3=196 — repeating motif
arp_notes = [110, 165, 131, 196, 147, 196, 131, 165,
             110, 165, 147, 220, 165, 196, 147, 165]

def make_arp_note(freq, dur, amp=0.09):
    n_a = int(SR * dur)
    ta = np.linspace(0, dur, n_a, endpoint=False)
    # sawtooth-ish (sum of harmonics)
    sig = (np.sin(2 * np.pi * freq * ta) * 0.6 +
           np.sin(2 * np.pi * freq * 2 * ta) * 0.25 +
           np.sin(2 * np.pi * freq * 3 * ta) * 0.1)
    env = adsr(n_a, 0.005, 0.08, 0.5, 0.04)
    return sig * env * amp

arp = np.zeros(N)
arp_start = BAR * 4        # enters at bar 4
arp_pattern_dur = len(arp_notes) * SXN
for rep in range(int((DUR - arp_start) / arp_pattern_dur) + 2):
    for i, freq in enumerate(arp_notes):
        t_start = arp_start + rep * arp_pattern_dur + i * SXN
        if t_start >= DUR:
            break
        s = int(t_start * SR)
        note = make_arp_note(freq, SXN * 0.75)
        e = s + len(note)
        if e <= N:
            arp[s:e] += note

# Filter arp through animated LP (Bicep filter-sweep feel)
# cutoff sweeps: 400→1400 over bars 4-8, holds, sweeps down at end
arp_fc = np.interp(T, [arp_start, arp_start+BAR*4, arp_start+BAR*8, DUR-4, DUR],
                      [400, 1400, 1200, 900, 400])
# Apply time-varying filter: process in blocks
arp_filt = np.zeros_like(arp)
block = 2048
prev_y = 0.0
for start in range(0, N, block):
    end = min(start + block, N)
    fc_block = float(arp_fc[start])
    alpha = 2 * np.pi * fc_block / SR
    alpha = min(alpha, 0.999)
    b, a = alpha, 1 - alpha
    for i in range(start, end):
        prev_y = b * arp[i] + a * prev_y
        arp_filt[i] = prev_y
arp = arp_filt

# ── Master filter sweep (LPF): mimics Bicep's subtle freq rolling ─────────────
# The whole mix is gently filtered — opens up over first 16 bars, stays open,
# then softly closes in the last 4 bars.
master_fc = np.interp(T,
    [0,  BAR*2, BAR*8, BAR*16, DUR-6, DUR],
    [600, 1200, 3500, 8000,   8000,  4000])

def apply_lp_sweep(sig, fc_array):
    out = np.zeros_like(sig)
    prev = 0.0
    block = 1024
    for start in range(0, len(sig), block):
        end = min(start + block, len(sig))
        fc = float(fc_array[start])
        alpha = min(2 * np.pi * fc / SR, 0.9999)
        for i in range(start, end):
            prev = alpha * sig[i] + (1 - alpha) * prev
            out[i] = prev
    return out

# ── Mix ───────────────────────────────────────────────────────────────────────
mix = (kick * 1.0 +
       clap * 0.9 +
       hat  * 0.85 +
       oh   * 0.75 +
       bass * 1.1 +
       pad  * 1.0 +
       arp  * 0.95)

mix = apply_lp_sweep(mix, master_fc)

# Master soft-clip limiter
mix = sat(mix, 1.5)

# Volume envelope: fade in 1.5s, fade out 3s
vol = np.minimum(T / 1.5, 1.0) * np.minimum((DUR - T) / 3.0, 1.0)
mix *= vol

# ── Stereo width: comb-filter stereo spread ───────────────────────────────────
delay_ms = 14
delay_smp = int(SR * delay_ms / 1000)
L = mix * 0.82 + np.concatenate([np.zeros(delay_smp), mix[:-delay_smp]]) * 0.18
R = mix * 0.82 - np.concatenate([np.zeros(delay_smp * 2), mix[:-delay_smp * 2]]) * 0.12
L = L[:N]; R = R[:N]

write_stereo(f"{OUT}/bgm.wav", L, R)
print(f"  → {OUT}/bgm.wav  ({DUR}s, {BPM}BPM Bicep-style)")

# ─── SFX: Impact ──────────────────────────────────────────────────────────────
print("Generating SFX ...")

dur_i = 0.6
ti = t(dur_i)
boom_env = np.exp(-ti * 8)
boom = np.sin(2 * np.pi * np.cumsum(np.linspace(200, 38, len(ti)) / SR)) * boom_env * 0.7
click_env = np.exp(-ti * 65)
click = np.sin(2 * np.pi * 900 * ti) * click_env * 0.45
noise_i = rng.normal(0, 1, len(ti)) * np.exp(-ti * 28) * 0.18
impact = sat(boom + click + noise_i, 1.4)
write_mono(f"{OUT}/sfx-impact.wav", impact)

dur_w = 0.32
tw = t(dur_w)
noise_w = rng.normal(0, 1, len(tw))
center = np.linspace(180, 3400, len(tw))
sweep_w = np.sin(2 * np.pi * np.cumsum(center / SR))
env_w = np.sin(np.pi * tw / dur_w) ** 0.5
whoosh = (noise_w * 0.38 + sweep_w * 0.32) * env_w * 0.58
write_mono(f"{OUT}/sfx-whoosh.wav", whoosh)

dur_t = 0.06
tt = t(dur_t)
tick = np.sin(2 * np.pi * 1800 * tt) * np.exp(-tt * 80) * 0.35
write_mono(f"{OUT}/sfx-tick.wav", tick)

dur_m = 8.0
tm = t(dur_m)
matrix = np.zeros(len(tm))
click_positions = np.arange(0, dur_m, 0.08)
click_freqs = np.interp(click_positions, [0, 4, 8], [600, 2400, 300])
click_n_m = int(SR * 0.04)
click_env_m = np.exp(-np.linspace(0, 20, click_n_m))
for i, (cp, cf) in enumerate(zip(click_positions, click_freqs)):
    s = int(cp * SR); e = s + click_n_m
    if e <= len(tm):
        tc = np.linspace(0, 0.04, click_n_m, endpoint=False)
        matrix[s:e] += np.sin(2 * np.pi * cf * tc) * click_env_m * (0.12 if i % 2 == 0 else 0.09)
noise_env_m = np.interp(tm, [0, 2, 5, 6.5, 8], [0, 0.06, 0.1, 0.06, 0])
matrix += rng.normal(0, 1, len(tm)) * noise_env_m
for i in range(30):
    s = int((6.5 + i * 0.033) * SR); bn = int(0.02 * SR); e = s + bn
    if e <= len(tm):
        matrix[s:e] += rng.normal(0, 1, bn) * 0.18 * (1 - i / 30)
write_mono(f"{OUT}/sfx-matrix.wav", matrix)

dur_c = 7.0
tc2 = t(dur_c)
col = np.zeros(len(tc2))
for i in range(8):
    s = int((0.1 + i * 0.1) * SR); p_n = int(0.05 * SR)
    tp2 = np.linspace(0, 0.05, p_n, endpoint=False)
    col[s:s+p_n] += np.sin(2 * np.pi * (400 + i * 100) * tp2) * np.exp(-tp2 * 40) * 0.15
conv_s = int(1.8 * SR); conv_n = int(1.4 * SR)
conv_t = np.linspace(0, 1.4, conv_n, endpoint=False)
conv_env2 = np.sin(np.pi * conv_t / 1.4) ** 0.4
col[conv_s:conv_s+conv_n] += (
    np.sin(2*np.pi*np.cumsum(np.linspace(1200, 60, conv_n)/SR)) * 0.3 +
    rng.normal(0, 1, conv_n) * 0.15) * conv_env2
logo_s = int(3.0 * SR); logo_n = int(1.5 * SR)
logo_t2 = np.linspace(0, 1.5, logo_n, endpoint=False)
col[logo_s:logo_s+logo_n] += (
    np.sin(2*np.pi*np.cumsum(np.linspace(300, 50, logo_n)/SR)) * np.exp(-logo_t2*4) * 0.65 +
    rng.normal(0, 1, logo_n) * np.exp(-logo_t2*8) * 0.15)
ring_s = int(3.65 * SR); ring_n = int(1.4 * SR)
ring_t2 = np.linspace(0, 1.4, ring_n, endpoint=False)
ring_env2 = np.exp(-ring_t2 * 2.5)
col[ring_s:ring_s+ring_n] += (np.sin(2*np.pi*1047*ring_t2)*0.18 + np.sin(2*np.pi*523*ring_t2)*0.12) * ring_env2
write_mono(f"{OUT}/sfx-collapse.wav", col)

dur_a = 0.25
ta2 = t(dur_a)
acid_freq = np.linspace(80, 3200, len(ta2))
acid = (np.sin(2*np.pi*np.cumsum(acid_freq/SR))*0.4 + rng.normal(0,1,len(ta2))*0.25) * \
       np.sin(np.pi*ta2/dur_a)**0.3 * 0.55
write_mono(f"{OUT}/sfx-acid-sweep.wav", acid)

dur_ty = 0.12
tty = t(dur_ty)
write_mono(f"{OUT}/sfx-type.wav", np.sin(2*np.pi*1200*tty) * np.exp(-tty*35) * 0.22)

print("\nAll audio assets generated.")
print(f"BGM: {BPM} BPM, {DUR}s — kick/clap/hat/bass/pad/arp, master LPF sweep")
