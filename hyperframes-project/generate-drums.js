#!/usr/bin/env node
/**
 * generate-drums.js
 * ─────────────────────────────────────────────────────────────
 * Synthesises a 46-second drum track for the Hyperframes project.
 * Zero npm dependencies — pure Node.js Buffer + fs.
 *
 * Usage:
 *   node generate-drums.js
 *
 * Output: audio/drums.wav
 *
 * Purpose: acts as a TIMING SKELETON for BGM producers.
 * Each kick/snare/hi-hat hit is placed to match the exact
 * scene transitions in index.html. Replace this file with
 * your real BGM once composed — same filename, same track-index.
 * ─────────────────────────────────────────────────────────────
 */

'use strict';

const fs   = require('fs');
const path = require('path');

const SR       = 44100;   // sample rate
const CHANNELS = 1;       // mono (BGM will be stereo — this is a guide track)
const DURATION = 46;      // seconds — matches index.html data-duration
const N        = SR * DURATION;

// ── Master mix buffer (float32 before clipping) ───────────────
const mix = new Float32Array(N);

// ─────────────────────────────────────────────────────────────
// SCENE TIMELINE (mirrors index.html exactly)
// ─────────────────────────────────────────────────────────────
// beat-1-hook    0  → 4s   : sparse, building tension
// beat-2-cliff   4  → 10s  : groove kicks in
// beat-3-walls   10 → 18s  : full pattern, energetic
// beat-4-cost    18 → 24s  : drops to half-time, heavy
// beat-4b-pie    24 → 32s  : groove returns, moderate
// beat-4c-bar    32 → 40s  : builds, adds hi-hats
// beat-5-cta     40 → 46s  : outro, sparse + final hit
//
// BPM STRATEGY:
//   Intro  0–4s  : no groove (silence + one impact at 0s)
//   Main  4–40s  : 86 BPM — calm, editorial documentary feel
//   Outro 40–46s : half-time, 43 BPM feel
//
// 86 BPM → beat = 60/86 = 0.6977s | bar (4 beats) = 2.791s
// ─────────────────────────────────────────────────────────────

const BPM  = 86;
const BEAT = 60 / BPM;         // 0.6977s per quarter-note
const BAR  = BEAT * 4;         // 2.791s per bar

// ─────────────────────────────────────────────────────────────
// SYNTHESIS HELPERS
// ─────────────────────────────────────────────────────────────

function addSine(buf, startSec, freq, decaySec, amp = 1.0) {
  const start = Math.floor(startSec * SR);
  const len   = Math.floor(decaySec * SR * 4); // render until inaudible
  for (let i = 0; i < len; i++) {
    const s = start + i;
    if (s >= N) break;
    const t   = i / SR;
    const env = Math.exp(-t / decaySec);
    if (env < 0.001) break;
    buf[s] += Math.sin(2 * Math.PI * freq * t) * env * amp;
  }
}

function addNoise(buf, startSec, decaySec, amp = 1.0, highpass = false) {
  const start = Math.floor(startSec * SR);
  const len   = Math.floor(decaySec * SR * 5);
  let hp = 0;
  for (let i = 0; i < len; i++) {
    const s = start + i;
    if (s >= N) break;
    const t   = i / SR;
    const env = Math.exp(-t / decaySec);
    if (env < 0.001) break;
    let n = (Math.random() * 2 - 1);
    if (highpass) { hp = hp * 0.92 + n * 0.08; n = n - hp; } // simple HPF
    buf[s] += n * env * amp;
  }
}

// ─────────────────────────────────────────────────────────────
// DRUM VOICES
// Each voice = addSine + addNoise combination
// ─────────────────────────────────────────────────────────────

function kick(t, amp = 1.0) {
  // Sub punch: freq sweeps 160→50Hz over 60ms
  const start = Math.floor(t * SR);
  const sweep = 0.06 * SR;
  for (let i = 0; i < sweep * 8; i++) {
    const s = start + i;
    if (s >= N) break;
    const ti  = i / SR;
    const env = Math.exp(-ti * 18) * amp;
    if (env < 0.0005) break;
    const freq = 160 * Math.exp(-ti * 22) + 45;
    mix[s] += Math.sin(2 * Math.PI * freq * ti) * env;
  }
  // Click transient
  addNoise(mix, t, 0.008, amp * 0.5, true);
}

function snare(t, amp = 1.0) {
  // Tone body (180Hz)
  addSine(mix, t, 180, 0.06, amp * 0.7);
  addSine(mix, t, 320, 0.04, amp * 0.3);
  // Snare noise (white, HPF)
  addNoise(mix, t, 0.09, amp * 0.9, true);
  // Crack transient
  addNoise(mix, t, 0.012, amp * 0.6, false);
}

function hihat(t, amp = 0.4, open = false) {
  // Very short HPF noise
  addNoise(mix, t, open ? 0.12 : 0.025, amp, true);
}

function rimshot(t, amp = 0.6) {
  addSine(mix, t, 900,  0.03, amp * 0.8);
  addSine(mix, t, 1700, 0.02, amp * 0.5);
  addNoise(mix, t, 0.018, amp * 0.4, true);
}

function impact(t, amp = 1.0) {
  // Big cinematic boom — low sine + noise burst
  addSine(mix, t, 55, 0.5, amp);
  addSine(mix, t, 90, 0.3, amp * 0.6);
  addNoise(mix, t, 0.15, amp * 0.8, false);
  addNoise(mix, t, 0.04, amp * 0.5, true);
}

function riser(startSec, endSec, amp = 0.3) {
  // White noise swell — tension builder
  const len = Math.floor((endSec - startSec) * SR);
  for (let i = 0; i < len; i++) {
    const s = Math.floor(startSec * SR) + i;
    if (s >= N) break;
    const t   = i / len;
    const env = t * t * amp; // quadratic swell
    mix[s] += (Math.random() * 2 - 1) * env;
  }
}

// ─────────────────────────────────────────────────────────────
// PATTERN BUILDER — places hits on a grid
// grid = array of 16 steps per bar (16th-note resolution)
// ─────────────────────────────────────────────────────────────

function pattern(startSec, bars, {
  kickGrid  = [],   // 16 steps, 1=hit
  snareGrid = [],
  hatGrid   = [],
  rimGrid   = [],
  kickAmp   = 1.0,
  snareAmp  = 1.0,
  hatAmp    = 0.4
} = {}) {
  const step = BEAT / 4; // 16th-note = beat/4

  for (let bar = 0; bar < bars; bar++) {
    const barStart = startSec + bar * BAR;
    for (let s = 0; s < 16; s++) {
      const t = barStart + s * step;
      if (kickGrid[s])  kick(t, kickAmp);
      if (snareGrid[s]) snare(t, snareAmp);
      if (hatGrid[s])   hihat(t, hatAmp);
      if (rimGrid[s])   rimshot(t);
    }
  }
}

// ─────────────────────────────────────────────────────────────
// SCENE PATTERNS
// ─────────────────────────────────────────────────────────────

// ── BEAT 1: Hook (0 – 4s) ─────────────────────────────────
// Silence + one massive impact at t=0, riser into beat 2
impact(0.0, 1.2);
riser(2.0, 4.0, 0.25);

// ── BEAT 2: Cliff (4 – 10s) ─────────────────────────────
// Groove kicks in at scene change — 86 BPM, 4-on-floor kick
// bar grid starts at t=4.0, each bar = 2.791s → ~2 bars fit
// K = kick, S = snare, H = hihat  (16th-note slots)
//  1 . . . 2 . . . 3 . . . 4 . . .
//  0 1 2 3 4 5 6 7 8 9 A B C D E F
pattern(4.0, 2, {
  kickGrid:  [1,0,0,0, 1,0,0,0, 1,0,0,0, 1,0,0,0],  // 4-on-floor
  snareGrid: [0,0,0,0, 1,0,0,0, 0,0,0,0, 1,0,0,0],  // beats 2 & 4
  hatGrid:   [1,0,1,0, 1,0,1,0, 1,0,1,0, 1,0,1,0],  // 8th-note hats
  hatAmp: 0.3
});
// bar 3 partial (10.0 - 4.0 = 6s / 2.791 = 2.15 bars)
pattern(4.0 + BAR * 2, 1, {
  kickGrid:  [1,0,0,0, 1,0,0,0, 0,0,0,0, 0,0,0,0],
  snareGrid: [0,0,0,0, 1,0,0,0, 0,0,0,0, 0,0,0,0],
  hatGrid:   [1,0,1,0, 1,0,1,0, 0,0,0,0, 0,0,0,0],
  hatAmp: 0.3
});

// ── BEAT 3: Three Walls (10 – 18s) ──────────────────────
// Full energy — adds rim on 16ths, offbeat kick, open hat on 4&
// 8s / 2.791 = 2.86 bars → 2 full + partial
pattern(10.0, 2, {
  kickGrid:  [1,0,0,0, 0,0,1,0, 1,0,0,0, 0,1,0,0],  // syncopated
  snareGrid: [0,0,0,0, 1,0,0,0, 0,0,0,0, 1,0,0,0],
  hatGrid:   [1,1,1,1, 1,1,1,1, 1,1,1,1, 1,1,1,0],  // 16th hats
  rimGrid:   [0,0,1,0, 0,0,0,0, 0,0,1,0, 0,0,0,0],
  kickAmp: 1.1, snareAmp: 1.0, hatAmp: 0.28
});
// Open hat accent on bar transition
hihat(10.0 + BAR * 2, 0.5, true);
pattern(10.0 + BAR * 2, 1, {
  kickGrid:  [1,0,0,0, 0,0,1,0, 1,0,0,0, 0,0,0,0],
  snareGrid: [0,0,0,0, 1,0,0,0, 0,0,0,0, 1,0,0,0],
  hatGrid:   [1,1,1,1, 1,1,1,1, 1,1,0,0, 0,0,0,0],
  hatAmp: 0.28
});

// ── BEAT 4: The Cost (18 – 24s) ──────────────────────────
// Half-time feel — heavy, slow, emotional weight
// Kick only on beat 1 and 3, snare on beat 3 (half-time snare)
pattern(18.0, 2, {
  kickGrid:  [1,0,0,0, 0,0,0,0, 1,0,0,0, 0,0,0,0],
  snareGrid: [0,0,0,0, 0,0,0,0, 1,0,0,0, 0,0,0,0],
  hatGrid:   [0,0,1,0, 0,0,1,0, 0,0,1,0, 0,0,1,0],  // sparse 8ths
  kickAmp: 1.2, snareAmp: 1.1, hatAmp: 0.2
});
// drop-hit at scene entry
impact(18.0, 0.7);
// fill before pie
rimshot(22.0);
rimshot(22.0 + BEAT * 0.5);
kick(23.5, 0.9);
snare(23.5 + BEAT * 0.25, 0.9);

// ── BEAT 4b: Pie Chart (24 – 32s) ───────────────────────
// Groove returns — medium energy, 8th-note hats
pattern(24.0, 2, {
  kickGrid:  [1,0,0,0, 1,0,0,0, 0,0,1,0, 1,0,0,0],
  snareGrid: [0,0,0,0, 1,0,0,0, 0,0,0,0, 1,0,0,0],
  hatGrid:   [1,0,1,0, 1,0,1,0, 1,0,1,0, 1,0,1,0],
  hatAmp: 0.32
});
hihat(24.0 + BAR * 2, 0.5, true); // open hat flourish
pattern(24.0 + BAR * 2, 1, {
  kickGrid:  [1,0,0,0, 1,0,0,0, 1,0,0,0, 0,0,0,0],
  snareGrid: [0,0,0,0, 1,0,0,0, 0,0,0,0, 1,0,0,0],
  hatGrid:   [1,0,1,0, 1,0,1,0, 0,0,0,0, 0,0,0,0],
  hatAmp: 0.32
});

// ── BEAT 4c: Bar Chart (32 – 40s) ───────────────────────
// Building — adds 16th hats + ghost snares for energy
pattern(32.0, 2, {
  kickGrid:  [1,0,0,0, 0,0,1,0, 1,0,0,0, 0,1,0,0],
  snareGrid: [0,0,0,0, 1,0,0,0, 0,0,0,0, 1,0,0,0],
  hatGrid:   [1,1,1,1, 1,1,1,1, 1,1,1,1, 1,1,1,1],  // full 16ths
  rimGrid:   [0,0,0,0, 0,0,0,0, 0,1,0,0, 0,0,0,0],  // ghost rim
  kickAmp: 1.1, snareAmp: 1.05, hatAmp: 0.26
});
// snare roll fill into outro
for (let i = 0; i < 8; i++) {
  snare(38.0 + i * (BEAT / 8), 0.4 + i * 0.07);
}
impact(40.0 - 0.05, 0.5); // pre-hit just before CTA

// ── BEAT 5: CTA / Outro (40 – 46s) ──────────────────────
// Sparse, resolving — kick + snare only, no hats
pattern(40.0, 2, {
  kickGrid:  [1,0,0,0, 0,0,0,0, 0,0,1,0, 0,0,0,0],
  snareGrid: [0,0,0,0, 0,0,0,0, 1,0,0,0, 0,0,0,0],
  hatAmp: 0
});
// Final impact + reverb tail (simulated by long sine decay)
kick(45.0, 1.3);
snare(45.0 + BEAT * 0.5, 1.1);
addSine(mix, 45.5, 55, 1.2, 0.5); // sub rumble tail

// ─────────────────────────────────────────────────────────────
// MIX & CLIP — normalise then hard limit to 16-bit range
// ─────────────────────────────────────────────────────────────
let peak = 0;
for (let i = 0; i < N; i++) peak = Math.max(peak, Math.abs(mix[i]));
const gain = peak > 0 ? 0.9 / peak : 1;
console.log(`Peak: ${peak.toFixed(3)}, normalisation gain: ${gain.toFixed(3)}`);

// ─────────────────────────────────────────────────────────────
// WRITE WAV
// ─────────────────────────────────────────────────────────────
const audioDir = path.join(__dirname, 'audio');
if (!fs.existsSync(audioDir)) fs.mkdirSync(audioDir);

const outPath  = path.join(audioDir, 'drums.wav');
const dataSize = N * 2;                      // 16-bit mono
const wavBuf   = Buffer.alloc(44 + dataSize);

wavBuf.write('RIFF', 0);
wavBuf.writeUInt32LE(36 + dataSize, 4);
wavBuf.write('WAVE', 8);
wavBuf.write('fmt ', 12);
wavBuf.writeUInt32LE(16, 16);
wavBuf.writeUInt16LE(1, 20);                 // PCM
wavBuf.writeUInt16LE(CHANNELS, 22);
wavBuf.writeUInt32LE(SR, 24);
wavBuf.writeUInt32LE(SR * CHANNELS * 2, 28);
wavBuf.writeUInt16LE(CHANNELS * 2, 32);
wavBuf.writeUInt16LE(16, 34);
wavBuf.write('data', 36);
wavBuf.writeUInt32LE(dataSize, 40);

for (let i = 0; i < N; i++) {
  const s   = Math.max(-1, Math.min(1, mix[i] * gain));
  const val = s < 0 ? s * 32768 : s * 32767;
  wavBuf.writeInt16LE(Math.round(val), 44 + i * 2);
}

fs.writeFileSync(outPath, wavBuf);
const kb = (wavBuf.length / 1024).toFixed(0);
const mb = (wavBuf.length / 1024 / 1024).toFixed(1);
console.log(`\n✅  Written: ${outPath}`);
console.log(`    Size: ${kb} KB (${mb} MB)`);
console.log(`    Duration: ${DURATION}s @ ${SR}Hz, 16-bit mono`);
console.log(`    BPM: ${BPM} | Beat: ${BEAT.toFixed(4)}s | Bar: ${BAR.toFixed(4)}s`);
console.log(`\n📋  Beat map (for BGM composer):`);

const beatMap = [
  { t: '0.000', label: 'IMPACT — scene open, hook' },
  { t: '2.000', label: 'RISER starts → tension build' },
  { t: '4.000', label: '▶ GROOVE IN — beat-2 scene cut (86 BPM)' },
  { t: '10.000', label: '▶ FULL PATTERN — beat-3 scene cut (16th hats)' },
  { t: '18.000', label: '▶ HALF-TIME DROP — beat-4 scene cut (heavy)' },
  { t: '24.000', label: '▶ GROOVE RETURN — beat-4b scene cut' },
  { t: '32.000', label: '▶ BUILD — beat-4c scene cut (add 16ths)' },
  { t: '38.000', label: 'SNARE ROLL — pre-outro fill' },
  { t: '40.000', label: '▶ OUTRO SPARSE — beat-5 scene cut' },
  { t: '45.000', label: 'FINAL HIT — end' },
];
beatMap.forEach(b => console.log(`    ${b.t}s  →  ${b.label}`));
console.log('\nReplace audio/drums.wav with your real BGM when ready.');
console.log('Keep the same filename — index.html loads it as track-index="2".');
