// Audio synthesizer for CONTROL FAILURE
// Generates: industrial drone + impact hits + alarm beeps + photo ambiance
const fs = require('fs');

const SR = 44100;
const DUR = 80;
const N = SR * DUR;

const L = new Int16Array(N);
const R = new Int16Array(N);

for (let i = 0; i < N; i++) {
  const t = i / SR;

  // ── Layer 1: Industrial drone (38Hz+41Hz beating, builds first 8s, fades at 65s) ──
  const droneUp  = Math.min(1, t / 8);
  const droneOut = t > 65 ? Math.max(0, 1 - (t - 65) / 4) : 1;
  const drone =
    0.10 * Math.sin(2 * Math.PI * 38 * t) +
    0.07 * Math.sin(2 * Math.PI * 41 * t) +
    0.025 * Math.sin(2 * Math.PI * 19 * t);
  const droneV = drone * droneUp * droneOut;

  // ── Layer 2: Impact transients at title slams / chapter cuts ──
  const impacts = [0.95, 8.0, 16.0, 25.0, 40.0, 54.0];
  let impact = 0;
  for (const h of impacts) {
    const dt = Math.abs(t - h);
    if (dt < 0.04) {
      // Pseudo-random using sine for determinism
      const n = Math.sin(i * 127.1 + h * 311.7) * Math.sin(i * 269.5 + h * 93.3);
      impact += (1 - dt / 0.04) * 0.22 * n;
    }
  }

  // ── Layer 3: Alarm beeps during CH06 collapse (54–65s) ──
  let alarm = 0;
  if (t > 54 && t < 65) {
    const phase = (t - 54) % 0.38;
    if (phase < 0.16) {
      const env = Math.min(phase / 0.015, 1) * Math.min((0.16 - phase) / 0.015, 1);
      alarm = 0.30 * env * Math.sin(2 * Math.PI * 660 * t);
      alarm += 0.12 * env * Math.sin(2 * Math.PI * 1320 * t); // harmonic
    }
  }

  // ── Layer 4: Photo-moment low rumble / fire texture ──
  let photo = 0;
  // Photo 1 (houses): 20.5–23s
  if (t > 20.5 && t < 23.0) {
    const env = Math.min((t - 20.5) / 0.3, 1) * Math.min((23.0 - t) / 0.3, 1);
    photo += env * 0.09 * Math.sin(2 * Math.PI * 52 * t);
    photo += env * 0.04 * Math.sin(2 * Math.PI * 43 * t);
  }
  // Photo 2 (firefighter): 53.7–56.5s
  if (t > 53.7 && t < 56.5) {
    const env = Math.min((t - 53.7) / 0.35, 1) * Math.min((56.5 - t) / 0.35, 1);
    photo += env * 0.13 * Math.sin(2 * Math.PI * 44 * t);
    photo += env * 0.06 * Math.sin(2 * Math.PI * 33 * t);
  }
  // Photo 3 (truck): 60–61.5s
  if (t > 60.0 && t < 61.5) {
    const env = Math.min((t - 60.0) / 0.1, 1) * Math.min((61.5 - t) / 0.2, 1);
    photo += env * 0.18 * Math.sin(2 * Math.PI * 48 * t);
  }

  // ── Layer 5: Final silence breath (65–75s, single very low tone fades in/out) ──
  let silence = 0;
  if (t > 67 && t < 75) {
    const env = Math.min((t - 67) / 2.5, 1) * Math.min((75 - t) / 2.5, 1);
    silence = env * 0.04 * Math.sin(2 * Math.PI * 80 * t);
  }

  // Mix + soft clip
  const mix = droneV + impact + alarm + photo + silence;
  const clipped = Math.tanh(mix * 1.1) * 0.9;
  const s = Math.floor(clipped * 32000);

  // Slight stereo spread on drone
  const spread = 0.025 * Math.sin(2 * Math.PI * 0.13 * t + 1.0);
  L[i] = Math.max(-32767, Math.min(32767, s + Math.floor(spread * 32000)));
  R[i] = Math.max(-32767, Math.min(32767, s - Math.floor(spread * 32000)));
}

// Write stereo WAV
function writeWAV(path, left, right, sr) {
  const numSamples = left.length;
  const dataSize = numSamples * 4; // 2 channels × 2 bytes
  const buf = Buffer.alloc(44 + dataSize);
  buf.write('RIFF', 0);
  buf.writeUInt32LE(36 + dataSize, 4);
  buf.write('WAVE', 8);
  buf.write('fmt ', 12);
  buf.writeUInt32LE(16, 16);
  buf.writeUInt16LE(1, 20);   // PCM
  buf.writeUInt16LE(2, 22);   // stereo
  buf.writeUInt32LE(sr, 24);
  buf.writeUInt32LE(sr * 4, 28);
  buf.writeUInt16LE(4, 32);
  buf.writeUInt16LE(16, 34);
  buf.write('data', 36);
  buf.writeUInt32LE(dataSize, 40);
  for (let i = 0; i < numSamples; i++) {
    buf.writeInt16LE(left[i],  44 + i * 4);
    buf.writeInt16LE(right[i], 44 + i * 4 + 2);
  }
  fs.writeFileSync(path, buf);
}

const out = require('path').join(__dirname, 'audio-cf.wav');
writeWAV(out, L, R, SR);
console.log('✓ Audio written:', out);
