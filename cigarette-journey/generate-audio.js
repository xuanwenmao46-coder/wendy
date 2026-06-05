// CONTROL FAILURE — Full Film Score
// 7 chapters, 75 seconds, stereo 44100Hz
const fs = require('fs'), path = require('path');

const SR = 44100;
const DUR = 78;
const N = SR * DUR;
const L = new Int16Array(N);
const R = new Int16Array(N);

// ── Deterministic noise (LCG) ──
let _seed = 12345;
function rng() { _seed = (_seed * 1664525 + 1013904223) & 0xFFFFFFFF; return (_seed >>> 0) / 0xFFFFFFFF - 0.5; }

// ── Envelope helpers ──
function fade(t, start, end) { return Math.max(0, Math.min(1, (t - start) / (end - start))); }
function fadeOut(t, start, end) { return Math.max(0, Math.min(1, (end - t) / (end - start))); }
function window(t, a, b, ramp=0.3) { return Math.min(fade(t,a,a+ramp), fadeOut(t,b-ramp,b)); }
function sin(freq, t) { return Math.sin(2 * Math.PI * freq * t); }
function tri(freq, t) { const p = (t * freq) % 1; return p < 0.5 ? 4*p-1 : 3-4*p; }

for (let i = 0; i < N; i++) {
  const t = i / SR;
  let mixL = 0, mixR = 0;

  // ════ LAYER 1: MASTER DRONE — evolves through all chapters ════
  // Frequency rises with tension: 38Hz(CH01) → 42Hz(CH03) → 48Hz(CH04) → 55Hz(CH06)
  const droneFreq = t < 8  ? 38 :
                    t < 16 ? 38 + (t-8)/8 * 2 :
                    t < 25 ? 40 + (t-16)/9 * 4 :
                    t < 40 ? 44 + (t-25)/15 * 8 :
                    t < 54 ? 52 + (t-40)/14 * 3 :
                    t < 65 ? 55 :
                             50 - (t-65)/10 * 45; // dies down in silence
  const droneVol  = t < 4  ? fade(t,0,4) * 0.06 :       // builds up in CH01
                    t < 65  ? 0.10 + Math.sin(t * 0.15) * 0.02 : // breathes
                              fadeOut(t,65,75) * 0.06;            // fades in CH07
  const droneBody = sin(droneFreq, t) * 0.55 +
                    sin(droneFreq * 2.01, t) * 0.28 +
                    sin(droneFreq * 3.00, t) * 0.12 +
                    sin(droneFreq * 0.50, t) * 0.18;
  const d = droneBody * droneVol;
  // stereo spread — slight width
  const spread = sin(0.11, t) * 0.015;
  mixL += d + spread; mixR += d - spread;

  // ════ LAYER 2: CHAPTER PULSE RHYTHMS ════
  // CH01 (0-8s): slow heartbeat — 0.5Hz
  if (t >= 1.5 && t < 8) {
    const env = window(t, 1.5, 8, 1.0);
    const beat = Math.max(0, sin(0.5, t));
    const pulse = Math.pow(beat, 4) * 0.04 * env * sin(droneFreq * 1.5, t);
    mixL += pulse; mixR += pulse;
  }

  // CH02 (8-16s): irregular glitch ticks — system noticing error
  if (t >= 9.3 && t < 16) {
    const ticks = [9.3, 10.2, 11.0, 12.4, 13.1, 14.0, 14.8];
    for (const tk of ticks) {
      const dt = Math.abs(t - tk);
      if (dt < 0.012) {
        const env2 = (1 - dt/0.012);
        const click = env2 * 0.14 * sin(880 + rng()*200, t);
        mixL += click * 0.7; mixR += click * 0.9; // off-center
      }
    }
  }

  // CH03 (16-25s): correction attempts — rhythmic buzzing
  if (t >= 16.5 && t < 25) {
    const corrEnv = window(t, 16.5, 25, 1.5);
    // 3Hz buzz that becomes more erratic
    const bfreq = 3.0 + (t - 16.5) * 0.2;
    const buzz = Math.pow(Math.max(0, sin(bfreq, t)), 2) * corrEnv * 0.035 * tri(440, t);
    mixL += buzz; mixR += buzz;
    // distortion rising
    const distEnv = fade(t, 20, 25) * 0.025;
    const dist = Math.tanh(sin(220, t) * 8) * distEnv;
    mixL += dist; mixR += dist;
  }

  // CH04 (25-40s): infection grid spread — granular texture building
  if (t >= 25 && t < 40) {
    const infEnv = window(t, 25, 40, 2.0);
    // Rumble deepens
    const rumble = sin(28, t) * 0.08 * infEnv + sin(21, t) * 0.05 * infEnv;
    mixL += rumble; mixR += rumble;
    // Sporadic high crackle (infection spreading sound)
    const crackRate = 1.5 + (t - 25) / 15 * 4; // accelerates
    const crackPhase = (t * crackRate) % 1;
    if (crackPhase < 0.04) {
      const c = (1 - crackPhase/0.04) * 0.06 * infEnv * rng() * 2;
      const pan = sin(0.7, t) * 0.3;
      mixL += c * (1 + pan); mixR += c * (1 - pan);
    }
  }

  // CH05 (40-54s): erasure — each word deletion has a low "delete" thud
  if (t >= 40 && t < 54) {
    // Sustained heavy pressure
    const pressEnv = window(t, 40, 54, 1.0) * 0.06;
    const press = sin(33, t) * pressEnv + sin(29, t) * pressEnv * 0.7;
    mixL += press; mixR += press;

    // Word deletion thuds at specific times (matching timeline)
    const deletions = [43.0, 45.2, 47.8, 50.5, 52.4];
    for (const dt_time of deletions) {
      const dt = t - dt_time;
      if (dt >= 0 && dt < 0.18) {
        const env5 = (1 - dt/0.18) * Math.exp(-dt * 12);
        const thud = env5 * 0.22 * sin(55 + dt*200, t);
        mixL += thud * 0.85; mixR += thud * 1.0;
      }
    }

    // Hiss rising toward end of CH05
    const hissEnv = fade(t, 50, 54) * 0.03;
    mixL += rng() * hissEnv; mixR += rng() * hissEnv;
  }

  // CH06 (54-65s): COLLAPSE — full alarm chaos
  if (t >= 54 && t < 65) {
    const ch6t = t - 54;

    // Alarm evolution: single → dual → triple frequency
    const alarmFreqs = [660, 880, 1100];
    for (let ai = 0; ai < alarmFreqs.length; ai++) {
      if (ch6t < ai * 2.5) continue; // each new tone enters later
      const aEnv = fade(t, 54 + ai * 2.5, 56 + ai * 2.5) * fadeOut(t, 63, 65);
      const aPhase = ((t - 54) % 0.38);
      if (aPhase < 0.18) {
        const aGate = Math.min(aPhase/0.015, 1) * Math.min((0.18-aPhase)/0.015, 1);
        const aTone = aGate * aEnv * 0.14 * sin(alarmFreqs[ai], t);
        const aPan = (ai - 1) * 0.25;
        mixL += aTone * (1 - aPan); mixR += aTone * (1 + aPan);
      }
    }

    // Distortion crunch — grows with time
    const crunchEnv = fade(t, 54, 62) * fadeOut(t, 63, 65) * 0.08;
    const crunch = Math.tanh(sin(110, t) * (2 + ch6t * 0.5)) * crunchEnv;
    mixL += crunch; mixR += crunch;

    // White noise burst at stamp moments (matching CF color card stamps)
    const stamps = [54.0, 55.3, 56.3, 57.1, 57.9];
    for (const st of stamps) {
      const dt = t - st;
      if (dt >= 0 && dt < 0.08) {
        const stEnv = (1 - dt/0.08) * 0.15;
        mixL += rng() * stEnv * 2; mixR += rng() * stEnv * 2;
      }
    }

    // Sub-bass impact at headline flashes
    const headlines = [61.0, 61.35, 61.7, 62.05, 62.4];
    for (const hl of headlines) {
      const dt = t - hl;
      if (dt >= 0 && dt < 0.15) {
        const hlEnv = Math.exp(-dt * 20) * 0.25;
        mixL += hlEnv * sin(40, t); mixR += hlEnv * sin(40, t);
      }
    }
  }

  // ════ LAYER 3: PHOTO MOMENT AMBIANCE ════
  // Photo 1 (20.5-23s): fire crackle + low roar
  if (t >= 20.5 && t < 23.0) {
    const pEnv = window(t, 20.5, 23.0, 0.4);
    mixL += sin(48, t) * 0.10 * pEnv + sin(38, t) * 0.06 * pEnv;
    mixR += sin(51, t) * 0.10 * pEnv + sin(35, t) * 0.06 * pEnv;
    // Crackle texture
    const cr = rng() * 0.04 * pEnv * (1 + sin(7, t));
    mixL += cr; mixR += cr * 0.85;
  }

  // Photo 2 (53.8-56.8s): heavy, documentary silence breaking
  if (t >= 53.8 && t < 56.8) {
    const pEnv = window(t, 53.8, 56.8, 0.5);
    const deep = sin(35, t) * 0.15 + sin(28, t) * 0.08;
    mixL += deep * pEnv * 0.9; mixR += deep * pEnv * 1.1;
  }

  // Photo 3 (62.4-63.1s): explosion thud
  if (t >= 62.4 && t < 63.1) {
    const dt = t - 62.4;
    const pEnv = Math.exp(-dt * 6) * 0.3;
    mixL += sin(40 + dt*50, t) * pEnv + rng() * 0.08 * pEnv;
    mixR += sin(40 + dt*50, t) * pEnv + rng() * 0.08 * pEnv;
  }

  // ════ LAYER 4: CH07 SILENCE — single sustained tone, very quiet ════
  if (t >= 65 && t < 75.4) {
    // Long slow tone — like an aftermath bell
    const sEnv = fade(t, 67, 70) * fadeOut(t, 73, 75.4);
    const bell = sin(220, t) * 0.018 * sEnv +
                 sin(440, t) * 0.009 * sEnv * Math.exp(-(t-67)*0.15);
    mixL += bell; mixR += bell;
    // Barely audible breath texture
    const breathEnv = window(t, 67, 75, 2.0) * 0.008;
    mixL += rng() * breathEnv; mixR += rng() * breathEnv;
  }

  // ════ LAYER 5: CHAPTER TRANSITION IMPACTS ════
  const transitions = [8.0, 16.0, 25.0, 40.0, 54.0, 65.0];
  for (const tr of transitions) {
    const dt = t - tr;
    if (dt >= 0 && dt < 0.06) {
      const impEnv = Math.exp(-dt * 40) * 0.20;
      // Low thud
      mixL += sin(55, t) * impEnv;
      mixR += sin(55, t) * impEnv;
      // High click
      if (dt < 0.02) {
        const cl = (1 - dt/0.02) * 0.12 * rng() * 2;
        mixL += cl; mixR += cl;
      }
    }
  }

  // ════ MASTER LIMITER + FINAL MIX ════
  const outL = Math.tanh(mixL * 1.15) * 0.88;
  const outR = Math.tanh(mixR * 1.15) * 0.88;
  L[i] = Math.max(-32767, Math.min(32767, Math.round(outL * 32767)));
  R[i] = Math.max(-32767, Math.min(32767, Math.round(outR * 32767)));
}

// Write stereo WAV
function writeWAV(fpath, left, right, sr) {
  const n = left.length;
  const dataSize = n * 4;
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
