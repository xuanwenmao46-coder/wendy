#!/usr/bin/env node
/**
 * generate-tts.js
 * ─────────────────────────────────────────────────────────────
 * Generates per-beat TTS audio files for the Hyperframes project.
 * Supports three providers: openai | elevenlabs | google
 *
 * Usage:
 *   OPENAI_API_KEY=sk-xxx      node generate-tts.js --provider openai
 *   ELEVENLABS_API_KEY=xxx     node generate-tts.js --provider elevenlabs
 *   GOOGLE_API_KEY=xxx         node generate-tts.js --provider google
 *
 * Output: audio/beat-N.mp3 (or .wav for google)
 * ─────────────────────────────────────────────────────────────
 */

const fs   = require('fs');
const path = require('path');

// ── Narration segments — one per beat, timed to match index.html ──
const BEATS = [
  {
    id:       'beat-1-hook',
    file:     'audio/beat-1.mp3',
    start:    0,
    duration: 4.0,
    text:     'Nearly half of all adults now have three or fewer close friends. And that number is getting worse.'
  },
  {
    id:       'beat-2-cliff',
    file:     'audio/beat-2.mp3',
    start:    4.0,
    duration: 6.0,
    text:     'Research shows our social networks peak around age 25 — then shrink steadily with every decade. It\'s not personal. It\'s structural.'
  },
  {
    id:       'beat-3-walls',
    file:     'audio/beat-3.mp3',
    start:    10.0,
    duration: 8.0,
    text:     'Making friends as an adult is hard because friendship requires three things: proximity, openness, and repetition. Adult life systematically removes all three.'
  },
  {
    id:       'beat-4-cost',
    file:     'audio/beat-4.mp3',
    start:    18.0,
    duration: 6.0,
    text:     'And the cost isn\'t just loneliness. Social isolation carries the same mortality risk as smoking fifteen cigarettes a day. This is a health crisis hiding in plain sight.'
  },
  {
    id:       'beat-4b-pie',
    file:     'audio/beat-4b.mp3',
    start:    24.0,
    duration: 8.0,
    text:     'The data is just as stark when we look at the fashion industry. Thirty-eight percent of its entire carbon footprint comes from a single step — dyeing and treating the fabric we wear every day.'
  },
  {
    id:       'beat-4c-bar',
    file:     'audio/beat-4c.mp3',
    start:    32.0,
    duration: 8.0,
    text:     'And when that fabric reaches the end of its life? Polyester takes two hundred years to break down. Nylon, forty. While linen disappears in months. We are wearing plastic that will outlive our grandchildren.'
  },
  {
    id:       'beat-5-cta',
    file:     'audio/beat-5.mp3',
    start:    40.0,
    duration: 6.0,
    text:     'The good news? The biology never changed. Only the infrastructure did. Friendship in adulthood is an act of will — and it\'s possible for anyone willing to make the first move.'
  }
];

// ── Provider configs ──────────────────────────────────────────
const PROVIDERS = {
  openai: {
    endpoint: 'https://api.openai.com/v1/audio/speech',
    envKey:   'OPENAI_API_KEY',
    ext:      'mp3',
    buildBody: (text) => JSON.stringify({
      model:          'tts-1-hd',
      voice:          'onyx',       // deep, authoritative: alloy|echo|fable|onyx|nova|shimmer
      input:          text,
      response_format:'mp3',
      speed:          0.95          // slightly slower for clarity on-screen
    }),
    headers: (key) => ({
      'Authorization': `Bearer ${key}`,
      'Content-Type':  'application/json'
    })
  },

  elevenlabs: {
    endpoint: (voiceId) => `https://api.elevenlabs.io/v1/text-to-speech/${voiceId}`,
    envKey:   'ELEVENLABS_API_KEY',
    ext:      'mp3',
    voiceId:  'EXAVITQu4vr4xnSDxMaL',  // "Bella" — swap to your preferred voice ID
    buildBody: (text) => JSON.stringify({
      text,
      model_id: 'eleven_multilingual_v2',
      voice_settings: { stability: 0.55, similarity_boost: 0.80, style: 0.2 }
    }),
    headers: (key) => ({
      'xi-api-key':  key,
      'Content-Type':'application/json',
      'Accept':      'audio/mpeg'
    })
  },

  google: {
    endpoint: (key) => `https://texttospeech.googleapis.com/v1/text:synthesize?key=${key}`,
    envKey:   'GOOGLE_API_KEY',
    ext:      'wav',
    buildBody: (text) => JSON.stringify({
      input: { text },
      voice: { languageCode: 'en-US', name: 'en-US-Studio-O', ssmlGender: 'MALE' },
      audioConfig: { audioEncoding: 'LINEAR16', speakingRate: 0.95, pitch: -1.0 }
    }),
    headers: () => ({ 'Content-Type': 'application/json' }),
    extractAudio: (json) => Buffer.from(JSON.parse(json).audioContent, 'base64')
  }
};

// ── CLI args ──────────────────────────────────────────────────
const args     = process.argv.slice(2);
const provider = (args[args.indexOf('--provider') + 1] || 'openai').toLowerCase();
const cfg      = PROVIDERS[provider];

if (!cfg) {
  console.error(`Unknown provider: ${provider}. Use: openai | elevenlabs | google`);
  process.exit(1);
}

const apiKey = process.env[cfg.envKey];
if (!apiKey) {
  console.error(`Missing env var: ${cfg.envKey}`);
  process.exit(1);
}

// ── Ensure audio output dir ───────────────────────────────────
const audioDir = path.join(__dirname, 'audio');
if (!fs.existsSync(audioDir)) fs.mkdirSync(audioDir);

// ── Generator ─────────────────────────────────────────────────
async function generateBeat(beat) {
  const outFile = path.join(__dirname, beat.file.replace('mp3', cfg.ext));
  console.log(`[${beat.id}] Generating: "${beat.text.slice(0, 60)}..."`);

  const endpoint =
    provider === 'elevenlabs' ? cfg.endpoint(cfg.voiceId) :
    provider === 'google'     ? cfg.endpoint(apiKey) :
    cfg.endpoint;

  const headers = cfg.headers(apiKey);
  const body    = cfg.buildBody(beat.text);

  const response = await fetch(endpoint, { method: 'POST', headers, body });

  if (!response.ok) {
    const errText = await response.text();
    throw new Error(`[${beat.id}] HTTP ${response.status}: ${errText}`);
  }

  let audioBuffer;
  if (provider === 'google') {
    const json = await response.text();
    audioBuffer = cfg.extractAudio(json);
  } else {
    const arrayBuf = await response.arrayBuffer();
    audioBuffer = Buffer.from(arrayBuf);
  }

  fs.writeFileSync(outFile, audioBuffer);
  const kb = (audioBuffer.length / 1024).toFixed(1);
  console.log(`  ✓ Saved ${outFile} (${kb} KB)`);
  return outFile;
}

// ── Main ──────────────────────────────────────────────────────
(async () => {
  console.log(`\n🎙  TTS Generator — provider: ${provider.toUpperCase()}\n`);
  const errors = [];

  for (const beat of BEATS) {
    try {
      await generateBeat(beat);
      // Small delay between requests to avoid rate limiting
      await new Promise(r => setTimeout(r, 300));
    } catch (e) {
      console.error(`  ✗ Failed: ${e.message}`);
      errors.push(beat.id);
    }
  }

  console.log('\n─────────────────────────────────────');
  if (errors.length === 0) {
    console.log('✅ All beats generated successfully.');
    console.log('\nNext: open index.html in Hyperframes — audio files are in ./audio/');
  } else {
    console.log(`⚠️  Failed beats: ${errors.join(', ')}`);
  }
})();
