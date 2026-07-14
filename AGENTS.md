# Repository Guide

This repo is a monorepo of three independent **HyperFrames** short-form video projects (HeyGen's code-based video framework — videos are authored as HTML/CSS/JS compositions and rendered to MP4):

- `my-video/`
- `why-adults-cant-make-friends/`
- `why-adults-cant-make-friends-v2/`

Each project is self-contained with its own `package.json` and (for the first two) `AGENTS.md`/`CLAUDE.md`. All commands are run **from within a project directory**, not the repo root.

## Cursor Cloud specific instructions

- **Standard commands are already documented.** Each project's `package.json` scripts (`dev`, `check`, `render`, `publish`) and the per-project `AGENTS.md`/`CLAUDE.md` are the source of truth. Run them from inside the relevant project directory.
- **The `hyperframes` CLI is fetched at runtime via `npx --yes hyperframes@0.6.20`** — it is intentionally NOT a declared dependency. The first invocation needs npm-registry network access; after that it is cached. The startup update script warms this cache, but a fresh/cold cache still requires network.
- **`npm run dev` is a long-running preview server ("Studio"), not a one-shot command.** It blocks until stopped and serves on `http://localhost:3002` (e.g. for `my-video`). Always start it backgrounded (e.g. in a `tmux` session); running it in the foreground will time out and kill the server.
- **Rendering uses system Chrome at `/usr/bin/google-chrome`.** `HeadlessExperimental.beginFrame` is unavailable in regular Chrome, so HyperFrames falls back to screenshot-capture mode. This works fine but is slower (~2 min to render a 20s / 600-frame clip). Optional speedup: `npx @puppeteer/browsers install chrome-headless-shell` (or set `HYPERFRAMES_BROWSER_PATH`). WebGL is also unavailable, so GPU mode auto-falls back to software.
- **`npm run check` runs `lint && validate && inspect` and exits non-zero on genuine composition issues.** As of setup, `why-adults-cant-make-friends-v2` has pre-existing `inspect` layout errors (`text_box_overflow`), so its `check` exits 1 — this is a content issue in that composition, not an environment problem. Contrast/lint warnings in the other projects are non-blocking.
- **Audio-regeneration scripts are optional and NOT needed for preview/render.** Committed audio and reference renders already exist. `why-adults-cant-make-friends/gen_music.py` needs Python `numpy`/`scipy` (not installed); `why-adults-cant-make-friends-v2/generate-tts.js` needs an external TTS API key (`OPENAI_API_KEY`/`ELEVENLABS_API_KEY`/`GOOGLE_API_KEY`) and network. Only install/configure these if you need to regenerate assets.
