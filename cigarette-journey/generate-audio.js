// CONTROL FAILURE — Film Score v3
// Fast industrial beat builds through 7 chapters, 78s stereo 44100Hz
const fs = require('fs'), path = require('path');

const SR = 44100;
const DUR = 78;
const N = SR * DUR;
const L = new Int16Array(N);
const R = new Int16Array(N);

// ── Deterministic LCG noise ──
let _seed = 12345;
function rng() { _seed = (_seed * 1664525 + 1013904223) & 0xFFFFFFFF; return (_seed >>> 0) / 0xFFFFFFFF - 0.5; }

// ── Envelope helpers ──
function fade(t, a, b)    { return Math.max(0, Math.min(1, (t - a) / (b - a))); }
function fadeOut(t, a, b) { return Math.max(0, Math.min(1, (b - t) / (b - a))); }
function sin(f, t)        { return Math.sin(2 * Math.PI * f * t); }

// ── BPM / grid ──
const BPM  = 128;
const BEAT = 60 / BPM;   // 0.46875s
const BAR  = BEAT * 4;   // 1.875s

// ── Kick drum (pitch-enveloped sine) ──
function kick(dt) {
  if (dt < 0 || dt > 0.42) return 0;
  const env = Math.exp(-dt * 18);
  const f0 = 150, fl = 42, k = 55;
  const phase = 2 * Math.PI * (-f0/k * (Math.exp(-k*dt) - 1) + fl * dt);
  return Math.sin(phase) * env * 0.88;
}

// ── Snare (noise + body tone) ──
function snare(dt) {
  if (dt < 0 || dt > 0.22) return 0;
  const env = Math.exp(-dt * 24);
  return (rng() * 0.72 + sin(195, dt) * 0.28) * env * 0.7;
}

// ── Closed hi-hat ──
function hihat(dt) {
  if (dt < 0 || dt > 0.055) return 0;
  return rng() * Math.exp(-dt * 75) * 0.32;
}

// ── Open hi-hat ──
function openHH(dt) {
  if (dt < 0 || dt > 0.16) return 0;
  return rng() * Math.exp(-dt * 20) * 0.28;
}

// ── Clap (CH05 snare layer) ──
function clap(dt) {
  if (dt < 0 || dt > 0.18) return 0;
  const env = Math.exp(-dt * 20) * 0.5 + Math.exp(-dt * 60) * 0.3;
  return rng() * env * 0.55;
}

// ── Bass synth (saturated sawtooth) ──
function bass(freq, dt, t) {
  if (dt < 0) return 0;
  const env = Math.exp(-dt * 4.5) * 0.55 + 0.22;
  const saw = 2 * ((t * freq) % 1) - 1;
  return Math.tanh(saw * 2.8) * env * 0.15;
}

// ── Main loop ──
for (let i = 0; i < N; i++) {
  const t = i / SR;
  let mixL = 0, mixR = 0;

  // ════ MASTER DRONE ════
  const droneFreq = t < 8  ? 38 :
                    t < 25 ? 38 + (t - 8) / 17 * 6 :
                    t < 54 ? 44 + (t - 25) / 29 * 12 :
                    t < 65 ? 56 :
                             50 - (t - 65) / 13 * 45;
  const droneVol = t < 4  ? fade(t, 0, 4) * 0.055 :
                   t < 65 ? 0.06 + Math.sin(t * 0.14) * 0.012 :
                             fadeOut(t, 65, 75) * 0.05;
  const droneBody = sin(droneFreq, t) * 0.52 +
                    sin(droneFreq * 2.01, t) * 0.26 +
                    sin(droneFreq * 3.00, t) * 0.10 +
                    sin(droneFreq * 0.50, t) * 0.16;
  const d = droneBody * droneVol;
  const spread = sin(0.11, t) * 0.013;
  mixL += d + spread; mixR += d - spread;

  // ════ BEAT ENGINE ════
  const beatEnv = t < 10  ? 0 :
                  t < 13  ? fade(t, 10, 13) * 0.55 :
                  t < 16  ? 0.55 :
                  t < 19  ? 0.55 + fade(t, 16, 19) * 0.3 :
                  t < 40  ? 0.85 :
                  t < 42  ? 0.85 + fade(t, 40, 42) * 0.15 :
                  t < 54  ? 1.0 :
                  t < 57  ? 1.0 :
                  t < 63  ? 1.0 - fade(t, 57, 63) * 0.6 :
                  t < 65  ? fadeOut(t, 63, 65) * 0.4 :
                             0;

  if (beatEnv > 0) {
    const barPos = ((t - 10) % BAR + BAR) % BAR;
    const beatFrac = barPos % BEAT;

    // Kick on beats 0 and 2
    const kdt = barPos < 2 * BEAT ? barPos : barPos - 2 * BEAT;
    const kv = kick(kdt) * beatEnv;
    mixL += kv * 0.85; mixR += kv;

    // Snare on beats 1 and 3
    let sdt;
    if      (barPos < BEAT)       sdt = barPos + BEAT;
    else if (barPos < 3 * BEAT)   sdt = barPos - BEAT;
    else                          sdt = barPos - 3 * BEAT;

    const snaresOn = t < 57 || (Math.floor((t - 57) / (BAR * 2)) % 2 === 0);
    if (snaresOn) {
      const sv = snare(sdt) * beatEnv;
      mixL += sv * (1 + rng() * 0.06); mixR += sv * (1 - rng() * 0.06);
      if (t >= 40 && t < 54) {
        mixL += clap(sdt) * beatEnv * 0.85;
        mixR += clap(sdt) * beatEnv * 0.85;
      }
    }

    // Hi-hat: 8th notes
    const hhdt = beatFrac < BEAT / 2 ? beatFrac : beatFrac - BEAT / 2;
    const hv = hihat(hhdt) * beatEnv * 0.85;
    const hhPan = sin(0.33, t) * 0.2;
    mixL += hv * (1 + hhPan); mixR += hv * (1 - hhPan);

    // Open hi-hat on beat 2.5 (CH03+)
    if (t >= 16) {
      const beat25 = barPos - (2 * BEAT + BEAT / 2);
      const ohv = openHH(beat25 >= 0 ? beat25 : 999) * beatEnv * 0.75;
      mixL += ohv; mixR += ohv;
    }

    // Bass synth with kick
    const bassNote = t < 20 ? 41 : t < 30 ? 36.7 : t < 46 ? 30.9 : 27.5;
    const bassEnvT = t < 16 ? 0 : t < 20 ? fade(t, 16, 20) : t < 63 ? 1 : fadeOut(t, 63, 65);
    if (kdt < BEAT) {
      const bv = bass(bassNote, kdt, t) * beatEnv * bassEnvT;
      mixL += bv; mixR += bv;
      const sub = kick(kdt) * beatEnv * bassEnvT * 0.22 * sin(bassNote, t);
      mixL += sub; mixR += sub;
    }
  }

  // ════ CH01: Heartbeat pulse ════
  if (t >= 1.5 && t < 8) {
    const env = fade(t, 1.5, 4) * fadeOut(t, 6, 8);
    const beat = Math.max(0, sin(0.5, t));
    mixL += Math.pow(beat, 4) * 0.045 * env * sin(droneFreq * 1.5, t);
    mixR += Math.pow(beat, 4) * 0.045 * env * sin(droneFreq * 1.5, t);
  }

  // ════ CH02: Glitch clicks ════
  if (t >= 9.3 && t < 16) {
    const ticks = [9.3, 10.2, 11.0, 12.4, 13.1, 14.0, 14.8];
    for (const tk of ticks) {
      const dt = Math.abs(t - tk);
      if (dt < 0.011) {
        const e = (1 - dt / 0.011) * 0.13 * sin(880 + rng() * 200, t);
        mixL += e * 0.7; mixR += e * 0.95;
      }
    }
  }

  // ════ CH03: Correction buzz ════
  if (t >= 16.5 && t < 25) {
    const bfreq = 3.0 + (t - 16.5) * 0.25;
    const body = 2 * ((t * 440) % 1) - 1;
    const buzz = Math.pow(Math.max(0, sin(bfreq, t)), 2) *
                 fade(t, 16.5, 20) * fadeOut(t, 23, 25) * 0.025 * body;
    mixL += buzz; mixR += buzz;
    const distEnv = fade(t, 21, 25) * 0.022;
    mixL += Math.tanh(sin(220, t) * 9) * distEnv;
    mixR += Math.tanh(sin(220, t) * 9) * distEnv;
  }

  // ════ CH04: Infection rumble + crackle ════
  if (t >= 25 && t < 40) {
    const infEnv = fade(t, 25, 28) * fadeOut(t, 38, 40);
    mixL += sin(28, t) * 0.06 * infEnv + sin(21, t) * 0.04 * infEnv;
    mixR += sin(28, t) * 0.06 * infEnv + sin(21, t) * 0.04 * infEnv;
    const crackRate = 1.8 + (t - 25) / 15 * 3.5;
    const crackPhase = (t * crackRate) % 1;
    if (crackPhase < 0.035) {
      const c = (1 - crackPhase / 0.035) * 0.05 * infEnv * rng() * 2;
      const pan = sin(0.7, t) * 0.25;
      mixL += c * (1 + pan); mixR += c * (1 - pan);
    }
  }

  // ════ CH05: Deletion thuds + hiss ════
  if (t >= 40 && t < 54) {
    const pressEnv = fade(t, 40, 42) * 0.055;
    mixL += sin(33, t) * pressEnv + sin(29, t) * pressEnv * 0.6;
    mixR += sin(33, t) * pressEnv + sin(29, t) * pressEnv * 0.6;
    const deletions = [43.0, 45.3, 47.9, 50.6, 52.5];
    for (const dt_time of deletions) {
      const dt = t - dt_time;
      if (dt >= 0 && dt < 0.20) {
        const env5 = (1 - dt / 0.20) * Math.exp(-dt * 10);
        const thud = env5 * 0.24 * sin(55 + dt * 180, t);
        mixL += thud * 0.82; mixR += thud * 1.0;
      }
    }
    const hissEnv = fade(t, 50, 54) * 0.025;
    mixL += rng() * hissEnv; mixR += rng() * hissEnv;
  }

  // ════ CH06: Alarm + crunch + stamp noise + sub hits ════
  if (t >= 54 && t < 65) {
    const ch6t = t - 54;
    const alarmFreqs = [660, 880, 1100];
    for (let ai = 0; ai < alarmFreqs.length; ai++) {
      if (ch6t < ai * 2.5) continue;
      const aEnv = fade(t, 54 + ai * 2.5, 56 + ai * 2.5) * fadeOut(t, 63, 65);
      const aPhase = ch6t % 0.38;
      if (aPhase < 0.18) {
        const aGate = Math.min(aPhase / 0.015, 1) * Math.min((0.18 - aPhase) / 0.015, 1);
        const aTone = aGate * aEnv * 0.13 * sin(alarmFreqs[ai], t);
        const aPan = (ai - 1) * 0.25;
        mixL += aTone * (1 - aPan); mixR += aTone * (1 + aPan);
      }
    }
    const crunchEnv = fade(t, 54, 62) * fadeOut(t, 63, 65) * 0.07;
    mixL += Math.tanh(sin(110, t) * (2 + ch6t * 0.45)) * crunchEnv;
    mixR += Math.tanh(sin(110, t) * (2 + ch6t * 0.45)) * crunchEnv;
    const stamps = [54.0, 55.3, 56.3, 57.1, 57.9];
    for (const st of stamps) {
      const dt = t - st;
      if (dt >= 0 && dt < 0.09) {
        const stEnv = (1 - dt / 0.09) * 0.14;
        mixL += rng() * stEnv * 2; mixR += rng() * stEnv * 2;
      }
    }
    const headlines = [61.0, 61.35, 61.7, 62.05, 62.4];
    for (const hl of headlines) {
      const dt = t - hl;
      if (dt >= 0 && dt < 0.16) {
        const hlEnv = Math.exp(-dt * 18) * 0.28;
        mixL += hlEnv * sin(40, t); mixR += hlEnv * sin(40, t);
      }
    }
  }

  // ════ PHOTO AMBIANCES ════
  if (t >= 20.5 && t < 23.0) {
    const pEnv = fade(t, 20.5, 21.2) * fadeOut(t, 22.5, 23.0);
    mixL += sin(48, t) * 0.08 * pEnv + rng() * 0.03 * pEnv;
    mixR += sin(51, t) * 0.08 * pEnv + rng() * 0.03 * pEnv;
  }
  if (t >= 53.8 && t < 56.8) {
    const pEnv = fade(t, 53.8, 54.5) * fadeOut(t, 56.0, 56.8);
    mixL += (sin(35, t) * 0.12 + sin(28, t) * 0.07) * pEnv * 0.9;
    mixR += (sin(35, t) * 0.12 + sin(28, t) * 0.07) * pEnv * 1.1;
  }
  if (t >= 62.4 && t < 63.1) {
    const dt = t - 62.4;
    const pEnv = Math.exp(-dt * 6) * 0.28;
    mixL += sin(40 + dt * 45, t) * pEnv + rng() * 0.07 * pEnv;
    mixR += sin(40 + dt * 45, t) * pEnv + rng() * 0.07 * pEnv;
  }

  // ════ CH07: Aftermath bell ════
  if (t >= 65 && t < 75.4) {
    const sEnv = fade(t, 67, 70) * fadeOut(t, 73, 75.4);
    const bell = sin(220, t) * 0.018 * sEnv +
                 sin(440, t) * 0.009 * sEnv * Math.exp(-(t - 67) * 0.14);
    mixL += bell; mixR += bell;
    mixL += rng() * fade(t, 67, 70) * fadeOut(t, 73, 75) * 0.007;
    mixR += rng() * fade(t, 67, 70) * fadeOut(t, 73, 75) * 0.007;
  }

  // ════ CHAPTER TRANSITION IMPACTS ════
  for (const tr of [8.0, 16.0, 25.0, 40.0, 54.0, 65.0]) {
    const dt = t - tr;
    if (dt >= 0 && dt < 0.07) {
      const impEnv = Math.exp(-dt * 38) * 0.22;
      mixL += sin(55, t) * impEnv; mixR += sin(55, t) * impEnv;
      if (dt < 0.022) {
        const cl = (1 - dt / 0.022) * 0.14 * rng() * 2;
        mixL += cl; mixR += cl;
      }
    }
  }

  // ════ MASTER LIMITER ════
  const outL = Math.tanh(mixL * 1.2) * 0.86;
  const outR = Math.tanh(mixR * 1.2) * 0.86;
  L[i] = Math.max(-32767, Math.min(32767, Math.round(outL * 32767)));
  R[i] = Math.max(-32767, Math.min(32767, Math.round(outR * 32767)));
}

function writeWAV(fpath, left, right, sr) {
  const n = left.length, dataSize = n * 4;
  const buf = Buffer.alloc(44 + dataSize);
  buf.write('RIFF', 0); buf.writeUInt32LE(36 + dataSize, 4);
  buf.write('WAVE', 8); buf.write('fmt ', 12);
  buf.writeUInt32LE(16, 16); buf.writeUInt16LE(1, 20);
  buf.writeUInt16LE(2, 22); buf.writeUInt32LE(sr, 24);
  buf.writeUInt32LE(sr * 4, 28); buf.writeUInt16LE(4, 32);
  buf.writeUInt16LE(16, 34); buf.write('data', 36);
  buf.writeUInt32LE(dataSize, 40);
  for (let i = 0; i < n; i++) {
    buf.writeInt16LE(left[i],  44 + i * 4);
    buf.writeInt16LE(right[i], 44 + i * 4 + 2);
  }
  fs.writeFileSync(fpath, buf);
}

const outPath = path.join(__dirname, 'audio-cf.wav');
writeWAV(outPath, L, R, SR);
console.log('✓ Audio written:', outPath);
