---
name: kinetic-typography
description: >
  Kinetic typography promo video with two scenes separated by a color wipe.
  Scene 1: warm off-white background, bold condensed words build up one-by-one
  sliding in from below. Scatter transition: words fly off in different
  directions while scaling up (one word scales to 14× for a letter close-up).
  Horizontal color-wipe reveals Scene 2: solid color background with large
  words sliding in from opposite sides. Ends with fade-to-black.
  Use when the user asks for "kinetic typography", "word reveal", "text promo",
  "typography animation", "scatter transition", or "word build" in HyperFrames.
---

# Kinetic Typography

Two-scene kinetic typography composition with a full-screen color wipe
transition between scenes. Total duration: ~9 seconds.

## Full HTML template

Copy, rename IDs/text, and run `npm run check` before rendering.

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <style>
      /* ── Self-hosted font (download TTF from Google Fonts first) ── */
      @font-face {
        font-family: 'Barlow Condensed';
        font-style: normal;
        font-weight: 900;
        src: url('./assets/fonts/barlow-condensed-900.ttf') format('truetype');
      }
      @font-face {
        font-family: 'Barlow Condensed';
        font-style: italic;
        font-weight: 900;
        src: url('./assets/fonts/barlow-condensed-900-italic.ttf') format('truetype');
      }
    </style>
    <script src="./node_modules/gsap/dist/gsap.min.js"></script>
    <style>
      * { margin: 0; padding: 0; box-sizing: border-box; }
      html, body {
        width: 1920px; height: 1080px;
        overflow: hidden;
        background: #000;
      }

      /* Scene 1 bg */
      #bgCream {
        position: absolute; inset: 0;
        background: #e7e2da;   /* warm off-white */
        opacity: 0;
      }

      /* Word stack — left-aligned, starts ~140px from top */
      .word-block {
        position: absolute;
        left: 115px;
        top: 138px;
      }
      .word {
        display: block;
        font-family: 'Barlow Condensed', 'Arial Black', sans-serif;
        font-weight: 900;
        font-size: 192px;
        line-height: 0.955;
        letter-spacing: -2px;
        color: #231f20;
        opacity: 0;
        will-change: transform, opacity, filter;
      }
      .word-italic { font-style: italic; }

      /* Scene 2 wipe bg */
      #bgCoral {
        position: absolute; inset: 0;
        background: #d4706b;   /* coral/salmon — change freely */
        transform: scaleY(0);
        transform-origin: 50% 50%;
        will-change: transform;
      }

      /* Scene 2 words — centered */
      .coral-block {
        position: absolute; inset: 0;
        display: flex; flex-direction: column;
        align-items: center; justify-content: center;
        line-height: 0.92;
      }
      .coral-word {
        display: block;
        font-family: 'Barlow Condensed', 'Arial Black', sans-serif;
        font-weight: 900;
        font-size: 258px;
        color: #f0ece5;          /* cream on coral */
        letter-spacing: -1px;
        opacity: 0;
        will-change: transform, opacity;
      }

      /* Fade-to-black overlay */
      #fadeOut {
        position: absolute; inset: 0;
        background: #000;
        opacity: 0;
        pointer-events: none;
      }
    </style>
  </head>
  <body>
    <div id="root"
      data-composition-id="main"
      data-start="0"
      data-duration="9"
      data-width="1920"
      data-height="1080"
    >
      <div id="bgCream"></div>

      <!-- Scene 1 words — add data-layout-allow-overflow; they fly off canvas -->
      <div class="word-block" data-layout-allow-overflow="true">
        <span class="word"             id="w1" data-layout-allow-overflow="true">KINETIC</span>
        <span class="word"             id="w2" data-layout-allow-overflow="true">TYPOGRAPHY</span>
        <span class="word word-italic" id="w3" data-layout-allow-overflow="true">PROMO</span>
        <span class="word"             id="w4" data-layout-allow-overflow="true">SLIDESHOW</span>
      </div>

      <div id="bgCoral"></div>

      <!-- Scene 2 words -->
      <div class="coral-block" data-layout-allow-overflow="true">
        <span class="coral-word" id="cw1" data-layout-allow-overflow="true">UNIVERSAL</span>
        <span class="coral-word" id="cw2" data-layout-allow-overflow="true">EXPRSSIONS</span>
      </div>

      <div id="fadeOut"></div>
    </div>

    <script>
      window.__timelines = window.__timelines || {};
      var tl = gsap.timeline({ paused: true });

      /* 0 — Fade in cream bg */
      tl.to('#bgCream', { opacity: 1, duration: 0.4, ease: 'power2.out' }, 0);

      /* 1 — Words enter from bottom, staggered 0.4s */
      var entries = [
        { id: '#w1', t: 0.30 },
        { id: '#w2', t: 0.72 },
        { id: '#w3', t: 1.10 },
        { id: '#w4', t: 1.50 }
      ];
      entries.forEach(function(e) {
        tl.fromTo(e.id,
          { opacity: 0, y: 270 },
          { opacity: 1, y: 0, duration: 0.46, ease: 'power3.out' },
          e.t
        );
      });

      /* 2 — Scatter (t=2.82): each word flies in a different direction + scales up */
      var ST = 2.82;

      tl.to('#w1', { x:  820, y: -560, scale:  6,  opacity: 0, filter: 'blur(5px)',  duration: 0.58, ease: 'power3.in' }, ST);
      tl.to('#w2', { x: -1350, y:  60, scale:  4.5, opacity: 0, filter: 'blur(10px)', duration: 0.60, ease: 'power3.in' }, ST + 0.04);
      tl.to('#w4', { x: -720, y: -350, scale:  5,  opacity: 0, filter: 'blur(8px)',  duration: 0.58, ease: 'power3.in' }, ST + 0.06);

      /* PROMO: scale to 14× without blur → M letter close-up fills frame,
         then fade before the wipe arrives. overwrite:true prevents tween conflict. */
      tl.to('#w3', { x: -480, y: 160, scale: 14, opacity: 1, filter: 'blur(0px)', duration: 0.55, ease: 'power2.in' }, ST + 0.02);
      tl.to('#w3', { opacity: 0, duration: 0.18, ease: 'power1.in', overwrite: true }, ST + 0.57);

      /* 3 — Coral horizontal wipe from vertical center */
      tl.to('#bgCoral', { scaleY: 1, duration: 0.48, ease: 'power2.inOut' }, 3.50);
      tl.to('#bgCream', { opacity: 0, duration: 0.25 }, 3.72);

      /* 4 — Scene 2 words: opposite-side slide-in */
      tl.fromTo('#cw1', { opacity: 0, x:  380 }, { opacity: 1, x: 0, duration: 0.52, ease: 'power3.out' }, 4.12);
      tl.fromTo('#cw2', { opacity: 0, x: -380 }, { opacity: 1, x: 0, duration: 0.52, ease: 'power3.out' }, 4.55);

      /* 5 — Fade to black */
      tl.to('#fadeOut', { opacity: 1, duration: 0.7, ease: 'power2.in' }, 8.2);

      window.__timelines['main'] = tl;
    </script>
  </body>
</html>
```

## Font setup

Google Fonts blocks in headless Chromium. Always download TTF locally:

```bash
# Fetch URLs from Google Fonts CSS
curl -sA "Mozilla/5.0" "https://fonts.googleapis.com/css2?family=Barlow+Condensed:ital,wght@0,900;1,900&display=swap"

# Download the .ttf files from the src: url() lines, e.g.:
mkdir -p assets/fonts
curl -sL "<ttf-url-regular>" -o assets/fonts/barlow-condensed-900.ttf
curl -sL "<ttf-url-italic>"  -o assets/fonts/barlow-condensed-900-italic.ttf
```

Then use `@font-face` with `url('./assets/fonts/...')` — never `<link>` to Google Fonts.

## Customisation guide

| What to change            | Where                                           |
|---------------------------|-------------------------------------------------|
| Scene 1 bg color          | `background:` on `#bgCream`                     |
| Scene 1 text color        | `color:` on `.word`                             |
| Scene 1 words             | Text content of `#w1`–`#w4`                     |
| Word font size            | `font-size:` on `.word` (192px default)         |
| Stagger speed             | Change `t:` values in `entries` array           |
| Scatter directions        | `x`, `y` values in scatter tweens              |
| Letter close-up word      | Change which word gets `scale: 14` (currently `#w3`) |
| Wipe color                | `background:` on `#bgCoral`                     |
| Wipe timing               | `3.50` position arg on `#bgCoral` tween         |
| Scene 2 bg color          | Same `background:` on `#bgCoral`               |
| Scene 2 text color        | `color:` on `.coral-word`                       |
| Scene 2 words             | Text content of `#cw1`, `#cw2`                  |
| Scene 2 font size         | `font-size:` on `.coral-word` (258px default)   |
| Fade-out timing           | `8.2` position arg on `#fadeOut` tween          |
| Total duration            | `data-duration="9"` on `#root`                  |

## Inspector rules

- **Always** add `data-layout-allow-overflow="true"` to `.word-block`, every
  `.word`, `.coral-block`, and every `.coral-word`. The scatter and scale
  animations move text far outside canvas bounds; without this attribute the
  inspector throws `text_box_overflow` errors and exits with code 1.
- `overwrite: true` on the PROMO fade-out tween prevents
  `overlapping_gsap_tweens` lint warnings when two tweens target the same
  `opacity` property on the same element.
- Contrast warnings on dark text over off-white are expected and intentional
  (design matches the reference). They do not fail `npm run check`.
- Run `npm run check` after every edit; gate: 0 errors, 0 layout issues.
