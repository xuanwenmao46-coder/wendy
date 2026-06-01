"""Generate all audio assets for FORMA v3 composition."""
import numpy as np
import wave, struct, os

SR = 44100
OUT = os.path.join(os.path.dirname(__file__), "audio")
os.makedirs(OUT, exist_ok=True)

def write_wav(path, data, sr=SR):
    data = np.clip(data, -1, 1)
    pcm = (data * 32767).astype(np.int16)
    with wave.open(path, 'w') as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(sr)
        f.writeframes(pcm.tobytes())

def stereo_wav(path, L, R, sr=SR):
    L = np.clip(L, -1, 1)
    R = np.clip(R, -1, 1)
    interleaved = np.empty(len(L) + len(R), dtype=np.int16)
    interleaved[0::2] = (L * 32767).astype(np.int16)
    interleaved[1::2] = (R * 32767).astype(np.int16)
    with wave.open(path, 'w') as f:
        f.setnchannels(2)
        f.setsampwidth(2)
        f.setframerate(sr)
        f.writeframes(interleaved.tobytes())

t = lambda dur: np.linspace(0, dur, int(SR * dur), endpoint=False)

# ─── BGM: 60s minimal electronic beat ─────────────────────────────────────────
print("Generating bgm.wav ...")
dur = 60.0
n = int(SR * dur)
T = np.linspace(0, dur, n, endpoint=False)

# Deep kick — 40Hz boom with short decay, every beat (0.5s = 120bpm)
kick = np.zeros(n)
bpm = 120
beat_dur = 60 / bpm  # 0.5s
kick_sr = int(SR * beat_dur)
kick_env = np.exp(-np.linspace(0, 8, kick_sr))
kick_tone = np.sin(2*np.pi * np.linspace(0, 1, kick_sr) * 80) * kick_env * 0.5
# pitch drop: starts at 120hz, sweeps to 40hz
kick_pitch = np.sin(2*np.pi * np.cumsum(np.linspace(120, 40, kick_sr) / SR)) * kick_env * 0.55

for b in range(int(dur / beat_dur)):
    s = b * kick_sr
    e = s + kick_sr
    if e <= n:
        kick[s:e] += kick_pitch

# Hi-hat — every 8th note (0.25s), quiet
hat_period = int(SR * 0.25)
hat_env = np.exp(-np.linspace(0, 20, hat_period))
hat_noise = np.random.default_rng(42).normal(0, 1, hat_period) * hat_env * 0.08
hat = np.zeros(n)
for b in range(int(dur * 4)):
    s = b * hat_period
    e = s + hat_period
    if e <= n:
        hat[s:e] += hat_noise

# Bass synth — pulsed saw at 55Hz, every bar (2s)
bass = np.zeros(n)
bar_dur = 2.0
bar_n = int(SR * bar_dur)
saw_env = np.exp(-np.linspace(0, 3, bar_n))
t_bar = np.linspace(0, bar_dur, bar_n, endpoint=False)
saw_wave = (2 * (t_bar * 55 % 1) - 1) * saw_env * 0.22
# slight detune
saw_wave2 = (2 * (t_bar * 55.4 % 1) - 1) * saw_env * 0.1
for b in range(int(dur / bar_dur)):
    s = b * bar_n
    e = s + bar_n
    if e <= n:
        bass[s:e] += saw_wave + saw_wave2

# Acid green pad — slow evolving sine chord (A minor feel: A2=110, E3=165, A3=220)
pad = np.zeros(n)
for freq, amp in [(110, 0.06), (165, 0.04), (220, 0.05), (330, 0.03)]:
    lfo = 0.5 + 0.5 * np.sin(2*np.pi * 0.15 * T)
    pad += np.sin(2*np.pi * freq * T) * amp * lfo

# Pulse synth — stabs every bar, C#4=277Hz
stab = np.zeros(n)
stab_dur = 0.18
stab_n = int(SR * stab_dur)
stab_env = np.exp(-np.linspace(0, 12, stab_n))
t_stab = np.linspace(0, stab_dur, stab_n, endpoint=False)
stab_wave = (np.sin(2*np.pi * 277 * t_stab) + 0.3*np.sin(2*np.pi * 554 * t_stab)) * stab_env * 0.14
stab_beats = [4, 8, 10, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100, 104, 108, 112, 116]
for sb in stab_beats:
    s = sb * hat_period  # every 8th note position
    e = s + stab_n
    if e <= n:
        stab[s:e] += stab_wave

bgm = kick + hat + bass + pad + stab

# Master envelope — fade in 2s, fade out 3s
fade_in = np.minimum(T / 2.0, 1.0)
fade_out = np.minimum((dur - T) / 3.0, 1.0)
bgm *= fade_in * fade_out

# Stereo spread
rng = np.random.default_rng(7)
delay = int(SR * 0.012)
L = bgm * 0.85 + np.concatenate([np.zeros(delay), bgm[:-delay]]) * 0.15
R = bgm * 0.85 + np.concatenate([np.zeros(delay*2), bgm[:-delay*2]]) * 0.15
stereo_wav(f"{OUT}/bgm.wav", L, R)
print(f"  → {OUT}/bgm.wav ({dur}s)")

# ─── SFX: Impact (S01 letters slam) ───────────────────────────────────────────
print("Generating sfx-impact.wav ...")
dur_i = 0.6
ti = t(dur_i)
# Sub boom
boom_env = np.exp(-ti * 8)
boom = np.sin(2*np.pi * np.cumsum(np.linspace(200, 40, len(ti)) / SR)) * boom_env * 0.7
# Transient click
click_env = np.exp(-ti * 60)
click = np.sin(2*np.pi * 800 * ti) * click_env * 0.5
# Noise burst
rng2 = np.random.default_rng(12)
noise_env = np.exp(-ti * 25)
noise = rng2.normal(0, 1, len(ti)) * noise_env * 0.2
impact = boom + click + noise
write_wav(f"{OUT}/sfx-impact.wav", impact)
print(f"  → {OUT}/sfx-impact.wav")

# ─── SFX: Whoosh (transitions) ────────────────────────────────────────────────
print("Generating sfx-whoosh.wav ...")
dur_w = 0.35
tw = t(dur_w)
rng3 = np.random.default_rng(33)
noise_w = rng3.normal(0, 1, len(tw))
# Band-pass sweep: center freq 200→3000
center = np.linspace(200, 3000, len(tw))
# Simple FIR approximation using convolution in chunks is too slow; use modulated sine
sweep = np.sin(2*np.pi * np.cumsum(center / SR))
env_w = np.sin(np.pi * tw / dur_w) ** 0.5
whoosh = (noise_w * 0.4 + sweep * 0.35) * env_w * 0.6
write_wav(f"{OUT}/sfx-whoosh.wav", whoosh)
print(f"  → {OUT}/sfx-whoosh.wav")

# ─── SFX: Tick (grid build, chart reveal) ─────────────────────────────────────
print("Generating sfx-tick.wav ...")
dur_t = 0.06
tt = t(dur_t)
tick_env = np.exp(-tt * 80)
tick = np.sin(2*np.pi * 1800 * tt) * tick_env * 0.35
write_wav(f"{OUT}/sfx-tick.wav", tick)
print(f"  → {OUT}/sfx-tick.wav")

# ─── SFX: Matrix flash burst (S08) ────────────────────────────────────────────
print("Generating sfx-matrix.wav ...")
dur_m = 8.0
tm = t(dur_m)
rng4 = np.random.default_rng(77)
# Rapid electronic stutter
matrix = np.zeros(len(tm))
# Clicks at 8th-note intervals, pitch rising then falling
click_positions = np.arange(0, dur_m, 0.08)
click_freqs = np.interp(click_positions, [0, 4, 8], [600, 2400, 300])
click_n = int(SR * 0.04)
click_env_m = np.exp(-np.linspace(0, 20, click_n))
for i, (cp, cf) in enumerate(zip(click_positions, click_freqs)):
    s = int(cp * SR)
    e = s + click_n
    if e <= len(tm):
        tc = np.linspace(0, 0.04, click_n, endpoint=False)
        c = np.sin(2*np.pi * cf * tc) * click_env_m
        # alternate channels for interest
        matrix[s:e] += c * (0.12 if i % 2 == 0 else 0.09)
# Noise underlayer
noise_m = rng4.normal(0, 1, len(tm))
noise_env_m = np.interp(tm, [0, 2, 5, 6.5, 8], [0, 0.06, 0.1, 0.06, 0])
matrix += noise_m * noise_env_m
# Strobe collapse at end (6.5-7.5s): rapid noise bursts
for i in range(30):
    s = int((6.5 + i * 0.033) * SR)
    burst_n = int(0.02 * SR)
    e = s + burst_n
    if e <= len(tm):
        matrix[s:e] += rng4.normal(0, 1, burst_n) * 0.18 * (1 - i/30)
write_wav(f"{OUT}/sfx-matrix.wav", matrix)
print(f"  → {OUT}/sfx-matrix.wav")

# ─── SFX: Collapse + logo reveal (S09) ─────────────────────────────────────────
print("Generating sfx-collapse.wav ...")
dur_c = 7.0
tc = t(dur_c)
rng5 = np.random.default_rng(99)
col = np.zeros(len(tc))
# Phase 1 (0-2.5s): fragments appear — quick pops
for i in range(8):
    s = int((0.1 + i*0.1) * SR)
    p_n = int(0.05 * SR)
    tp = np.linspace(0, 0.05, p_n, endpoint=False)
    penv = np.exp(-tp * 40)
    col[s:s+p_n] += np.sin(2*np.pi * (400 + i*100) * tp) * penv * 0.15
# Phase 2 (1.8-3.2s): converge whoosh — descending pitch sweep
conv_s = int(1.8 * SR)
conv_n = int(1.4 * SR)
conv_t = np.linspace(0, 1.4, conv_n, endpoint=False)
conv_freq = np.linspace(1200, 60, conv_n)
conv_env = np.sin(np.pi * conv_t / 1.4) ** 0.4
conv_noise = rng5.normal(0, 1, conv_n)
conv_sweep = np.sin(2*np.pi * np.cumsum(conv_freq / SR))
col[conv_s:conv_s+conv_n] += (conv_sweep * 0.3 + conv_noise * 0.15) * conv_env
# Phase 3 (3.0s): logo impact — massive boom
logo_s = int(3.0 * SR)
logo_n = int(1.5 * SR)
logo_t = np.linspace(0, 1.5, logo_n, endpoint=False)
logo_env = np.exp(-logo_t * 4)
logo_boom = np.sin(2*np.pi * np.cumsum(np.linspace(300, 50, logo_n) / SR)) * logo_env * 0.65
logo_air = rng5.normal(0, 1, logo_n) * np.exp(-logo_t * 8) * 0.15
col[logo_s:logo_s+logo_n] += logo_boom + logo_air
# Phase 4 (3.6-5s): acid tone ring — C6 sine resonance
ring_s = int(3.65 * SR)
ring_n = int(1.4 * SR)
ring_t = np.linspace(0, 1.4, ring_n, endpoint=False)
ring_env = np.exp(-ring_t * 2.5)
col[ring_s:ring_s+ring_n] += np.sin(2*np.pi * 1047 * ring_t) * ring_env * 0.18
col[ring_s:ring_s+ring_n] += np.sin(2*np.pi * 523 * ring_t) * ring_env * 0.12
write_wav(f"{OUT}/sfx-collapse.wav", col)
print(f"  → {OUT}/sfx-collapse.wav")

# ─── SFX: Acid sweep (acid-green wipe transitions) ────────────────────────────
print("Generating sfx-acid-sweep.wav ...")
dur_a = 0.25
ta = t(dur_a)
rng6 = np.random.default_rng(55)
acid_freq = np.linspace(80, 3200, len(ta))
acid_sweep = np.sin(2*np.pi * np.cumsum(acid_freq / SR))
acid_noise = rng6.normal(0, 1, len(ta))
acid_env = np.sin(np.pi * ta / dur_a) ** 0.3
acid = (acid_sweep * 0.4 + acid_noise * 0.25) * acid_env * 0.55
write_wav(f"{OUT}/sfx-acid-sweep.wav", acid)
print(f"  → {OUT}/sfx-acid-sweep.wav")

# ─── SFX: Type blip (S03 word reveal) ─────────────────────────────────────────
print("Generating sfx-type.wav ...")
dur_ty = 0.12
tty = t(dur_ty)
type_env = np.exp(-tty * 35)
tyblip = np.sin(2*np.pi * 1200 * tty) * type_env * 0.22
write_wav(f"{OUT}/sfx-type.wav", tyblip)
print(f"  → {OUT}/sfx-type.wav")

print("\nAll audio assets generated.")
