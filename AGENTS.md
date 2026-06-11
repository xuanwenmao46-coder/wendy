# Repository Overview

This repo is a collection of three independent **HyperFrames** "video-as-code" projects (HeyGen). Each is a self-contained npm project at the repo root:

- `my-video/` — starter/demo composition
- `why-adults-cant-make-friends/` — explainer video (v1, single `index.html`)
- `why-adults-cant-make-friends-v2/` — same explainer reworked into modular sub-compositions under `compositions/`

There is no root-level workspace linking them; run all commands from inside a project directory. Each project's own `AGENTS.md`/`CLAUDE.md` documents the HyperFrames composition rules and the standard `npm run dev|check|render|publish` scripts.

## Cursor Cloud specific instructions

- **Per-project commands.** `cd` into one of the three project dirs first. The standard scripts (`dev`, `check`, `render`, `publish`) are defined in each `package.json` and described in that project's `AGENTS.md`/`CLAUDE.md`. There is no aggregate command that operates on all three at once.
- **CLI delivery.** Every script runs the pinned CLI via `npx --yes hyperframes@0.6.20 …`. The first invocation downloads it from the npm registry (needs network, ~15s); it is cached afterward, so later runs are offline-friendly.
- **`npm run dev` is a long-running Studio server.** It does not exit; run it in the background (e.g. a tmux session) and read its output for the chosen port (typically `http://localhost:3002`). Running it in the foreground will be killed and break the preview.
- **Rendering uses system Chrome in software mode.** `render`/`validate`/`inspect` use `/usr/bin/google-chrome`; `HeadlessExperimental.beginFrame` is unavailable so it falls back to screenshot capture and WebGL runs in software. This still works — a 20s composition renders to an MP4 in `renders/` in roughly 2 minutes.
- **Verify visual output via `npm run render`, not the interactive browser.** The Studio preview is WebGL-heavy; the in-VM interactive Chrome (computer-use) GPU/renderer process can crash ("Aw, Snap! Error code 4") and then show a permanently black preview that does not recover. The headless `render` path is unaffected and is the reliable way to confirm a composition produces correct visuals (extract frames from the output MP4 with `ffmpeg`).
- **`why-adults-cant-make-friends-v2` `npm run check` exits non-zero** due to 2 pre-existing `text_box_overflow` inspect errors (2–4px) in `compositions/beat-1-hook.html`. These are content-layout findings, not environment problems, and do not block `render`.
- **Optional asset-generation scripts are not required.** Generated audio/music is already committed. `why-adults-cant-make-friends/gen_music.py` needs Python `numpy`/`scipy`; `why-adults-cant-make-friends-v2/generate-tts.js` needs external TTS API keys. Skip unless regenerating media.
