# Why Adults Can't Make Friends — Hyperframes Project

## File Structure

```
hyperframes-project/
├── index.html                        ← Root composition (46s, no BGM)
├── generate-tts.js                   ← TTS generator script ★
├── audio/                            ← Generated per-beat TTS files (auto-created)
│   ├── beat-1.mp3
│   ├── beat-2.mp3
│   ├── beat-3.mp3
│   ├── beat-4.mp3
│   ├── beat-4b.mp3
│   ├── beat-4c.mp3
│   └── beat-5.mp3
├── README.md
└── compositions/
    ├── beat-1-hook.html              ←  0–4s  : Shocking stat (49%)
    ├── beat-2-cliff.html             ←  4–10s : Bar chart + "peak at 25"
    ├── beat-3-walls.html             ← 10–18s : Three blocker cards
    ├── beat-4-cost.html              ← 18–24s : Surgeon General quote
    ├── beat-4b-pie.html              ← 24–32s : ECharts donut (carbon %)
    ├── beat-4c-bar.html              ← 32–40s : ECharts bar (fabric decay)
    └── beat-5-cta.html              ← 40–46s : Way forward + end card
```

---

## Step 1 — Generate TTS audio

Run ONE of the following (pick your provider):

### Option A — OpenAI TTS (recommended, best quality)
Voice: `onyx` (deep, authoritative). Model: `tts-1-hd`.
```bash
OPENAI_API_KEY=sk-xxxxxxxx node generate-tts.js --provider openai
```

### Option B — ElevenLabs
Voice: `Bella` by default (edit `voiceId` in generate-tts.js to change).
```bash
ELEVENLABS_API_KEY=xxxxxxxx node generate-tts.js --provider elevenlabs
```

### Option C — Google Cloud TTS
Voice: `en-US-Studio-O` (Studio tier, male).
```bash
GOOGLE_API_KEY=xxxxxxxx node generate-tts.js --provider google
```

Output files land in `./audio/` automatically.

---

## Step 2 — Open in Hyperframes

No further config needed. `index.html` already references:
```
audio/beat-1.mp3 → beat-1-hook  (0–4s)
audio/beat-2.mp3 → beat-2-cliff (4–10s)
audio/beat-3.mp3 → beat-3-walls (10–18s)
audio/beat-4.mp3 → beat-4-cost  (18–24s)
audio/beat-4b.mp3→ beat-4b-pie  (24–32s)
audio/beat-4c.mp3→ beat-4c-bar  (32–40s)
audio/beat-5.mp3 → beat-5-cta   (40–46s)
```

**BGM has been removed.** Only TTS narration plays. Each audio track is on `data-track-index="0"` and precisely timed to its beat.

---

## Narration Script

| Beat | Time | Script |
|------|------|--------|
| 1 | 0–4s | "Nearly half of all adults now have three or fewer close friends. And that number is getting worse." |
| 2 | 4–10s | "Research shows our social networks peak around age 25 — then shrink steadily with every decade. It's not personal. It's structural." |
| 3 | 10–18s | "Making friends as an adult is hard because friendship requires three things: proximity, openness, and repetition. Adult life systematically removes all three." |
| 4 | 18–24s | "And the cost isn't just loneliness. Social isolation carries the same mortality risk as smoking fifteen cigarettes a day." |
| 4b | 24–32s | "38% of fashion's carbon footprint comes from a single step — dyeing and treating the fabric we wear every day." |
| 4c | 32–40s | "Polyester takes 200 years to break down. Nylon, 40. While linen disappears in months. We are wearing plastic that will outlive our grandchildren." |
| 5 | 40–46s | "The good news? The biology never changed. Only the infrastructure did. Friendship is an act of will — and it's possible for anyone willing to make the first move." |

---

## Customising the voice

Edit `generate-tts.js` — the relevant lines:

```js
// OpenAI — change voice:
voice: 'onyx'   // options: alloy | echo | fable | onyx | nova | shimmer

// ElevenLabs — change voiceId:
voiceId: 'EXAVITQu4vr4xnSDxMaL'   // replace with any ElevenLabs voice ID

// All providers — change speed:
speed: 0.95    // 0.5 (very slow) → 1.5 (fast). 0.9–1.0 works best on-screen.
```

---

## Dependencies

- GSAP 3.14.2 (CDN)
- ECharts 5.4.3 (CDN)
- Google Fonts: DM Serif Display + DM Sans
- Node.js ≥ 18 (for generate-tts.js — uses built-in fetch)

Total runtime: **46 seconds**
