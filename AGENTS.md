# Repository Overview

This repo contains three independent **HyperFrames** video-composition projects (HeyGen's HTML-to-MP4 framework):

- `my-video/` — simple single-file composition
- `why-adults-cant-make-friends/` — composition with ElevenLabs TTS asset generation
- `why-adults-cant-make-friends-v2/` — composition built from sub-compositions in `compositions/` with audio in `audio/`

Each project is a standalone npm package. Per-project usage, key rules, and skills are documented in each project's `AGENTS.md` / `CLAUDE.md`.

## Cursor Cloud specific instructions

- **Runtime is already provisioned.** The VM has Node 22, npm, `ffmpeg`, and `google-chrome` preinstalled. The startup update script runs `npm install` in each project, so dependencies (`gsap`, etc.) are ready. `node_modules/` is gitignored.
- **The "application" is the HyperFrames CLI**, invoked per project via npm scripts that call `npx --yes hyperframes@0.6.20 ...` (downloaded/cached on first use; needs network). From inside a project directory:
  - `npm run dev` — preview studio (long-running server, default port 3002). It is a blocking server — start it in the background/tmux, never in the foreground, or it will be killed. Add `--no-open` in headless VMs since there is no auto-launchable desktop browser session.
  - `npm run check` — `lint` + `validate` + `inspect` (lint/inspect are static; validate/inspect launch headless Chrome).
  - `npm run render` — renders to `renders/*.mp4`.
  - `npm run publish` — uploads for a shareable link (needs network/account).
- **Headless Chrome note:** HyperFrames uses system `google-chrome`, which lacks `HeadlessExperimental.beginFrame`, so validate/inspect/render fall back to slower screenshot capture. This is expected and works; a `chrome-headless-shell` install only speeds things up. Renders are CPU-bound and can take a couple of minutes for a ~20s clip — do not assume a hang.
- **Pre-existing lint findings are not environment failures.** `inspect` may report content issues (e.g. `text_box_overflow` in `why-adults-cant-make-friends-v2`, WCAG contrast warnings) that make `npm run check` exit non-zero. These are composition-content issues, not setup problems; `lint` and `validate` pass.
- `why-adults-cant-make-friends-v2/index.html` loads GSAP from `./node_modules/gsap/...`, so that project must have its deps installed for the preview/render to work.
