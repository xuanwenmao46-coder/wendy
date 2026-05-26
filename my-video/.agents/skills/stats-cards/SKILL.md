---
name: stats-cards
description: >
  Two dark stat cards on a muted purple-gray background.
  Top card: a line chart with a count-up number (e.g. portfolio balance).
  Bottom card: a full-screen canvas slot-machine counter that tumbles digits
  from 000,000,000 to a target value (e.g. YouTube views).
  Use when the user asks for a "stats card", "finance card", "counter animation",
  "slot machine number", "portfolio chart", or "YouTube views widget" scene in
  a HyperFrames composition.
---

# Stats Cards

Two stacked dark cards. Top card has a line chart + count-up dollar/number.
Bottom card slides in and runs a canvas slot-machine counter.

## Composition skeleton

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <script src="./node_modules/gsap/dist/gsap.min.js"></script>
    <style>
      /* ... see CSS section ... */
    </style>
  </head>
  <body>
    <div id="root"
      data-composition-id="main"
      data-start="0"
      data-duration="8"
      data-width="1920"
      data-height="1080"
    >
      <div class="cards-wrap" id="cardsWrap">
        <!-- Top card -->
        <div class="card pf-card">
          <div class="pf-left">
            <div class="pf-amount" id="pfAmount">$2,933</div>
            <div class="pf-label">Portfolio Balance</div>
          </div>
          <div class="pf-right">
            <svg class="pf-chart-svg" viewBox="0 0 1160 108"
                 preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
              <!-- line chart SVG — see SVG section -->
            </svg>
            <div class="pf-x-axis">
              <span>Mo</span><span>Tu</span><span>We</span>
              <span>Th</span><span>Fr</span><span>Sa</span><span>Su</span>
            </div>
          </div>
        </div>

        <!-- Bottom card -->
        <div class="card views-card" id="viewsCard">
          <div class="views-arrow">&#x2191;</div>
          <canvas id="slotCanvas" width="1536" height="148"></canvas>
          <div class="views-label">Views on Youtube</div>
          <div class="views-period">For 2024/2025</div>
        </div>
      </div>
    </div>
    <script>/* see Script section */</script>
  </body>
</html>
```

## CSS

```css
* { margin: 0; padding: 0; box-sizing: border-box; }
html, body {
  width: 1920px; height: 1080px;
  overflow: hidden;
  background: #292b3d;   /* muted purple-gray page bg */
}

.cards-wrap {
  position: absolute;
  left: 140px; top: 120px;
  width: 1640px;
  display: flex; flex-direction: column; gap: 32px;
  opacity: 0;            /* fades in via GSAP */
}

.card {
  background: #111116;   /* near-black card bg */
  border-radius: 22px;
  overflow: hidden;
}

/* ── Top card ── */
.pf-card {
  display: flex; align-items: stretch;
  height: 224px; padding: 38px 52px;
}
.pf-left {
  flex-shrink: 0; width: 340px;
  display: flex; flex-direction: column; justify-content: center;
}
.pf-amount {
  font-size: 86px; font-weight: 700; color: #fff;
  letter-spacing: -3px; line-height: 1;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}
.pf-label { font-size: 19px; color: #585a70; margin-top: 14px; }

.pf-right {
  flex: 1;
  display: flex; flex-direction: column; justify-content: space-between;
  padding-top: 2px;
}
.pf-chart-svg { flex: 1; width: 100%; overflow: visible; }
.pf-x-axis {
  display: flex; justify-content: space-between;
  padding: 0 1px; margin-top: 8px;
}
.pf-x-axis span { font-size: 19px; color: #44465a; }

/* ── Bottom card ── */
.views-card {
  height: 224px; padding: 36px 52px;
  position: relative;
  display: flex; align-items: center; justify-content: center;
  opacity: 0;
  transform: translateY(62px); /* animated in */
}
.views-arrow {
  position: absolute; top: 36px; left: 52px;
  font-size: 30px; color: #fff; font-weight: 300;
}
.views-label {
  position: absolute; bottom: 36px; left: 52px;
  font-size: 18px; color: #8082a0;
}
.views-period {
  position: absolute; bottom: 36px; right: 52px;
  font-size: 18px; color: #585a70;
}

/* Canvas self-clips — no DOM overflow errors */
#slotCanvas { display: block; width: 1536px; height: 148px; }
```

## SVG Line Chart

The chart spans `viewBox="0 0 1160 108"` with `preserveAspectRatio="none"`.
Use a `linearGradient` fill under the line and a stroked `<path>` on top.
The path below is a 7-day wavy upward-trend. Adjust control points for
different shapes.

```svg
<defs>
  <linearGradient id="areaGrad" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%"   stop-color="#4ade80" stop-opacity="0.16"/>
    <stop offset="100%" stop-color="#4ade80" stop-opacity="0.00"/>
  </linearGradient>
</defs>

<!-- area fill: same path + close to bottom -->
<path d="M 0,72 C 22,76 46,88 72,86 C 96,84 115,80 138,70
         C 158,60 172,96 194,94 C 214,92 235,60 258,52
         C 278,46 298,62 320,72 C 340,82 358,68 378,48
         C 398,30 418,36 440,54 C 460,70 474,62 492,52
         C 510,42 526,44 550,58 C 572,70 585,74 606,68
         C 626,62 640,52 662,48 C 682,44 698,36 722,44
         C 744,52 756,58 778,48 C 798,40 812,32 834,30
         C 856,28 868,36 890,42 C 912,48 928,40 950,34
         C 970,28 986,20 1010,18 C 1042,15 1075,11 1160,8
         L 1160,108 L 0,108 Z"
  fill="url(#areaGrad)"/>

<!-- line stroke -->
<path d="M 0,72 C 22,76 46,88 72,86 C 96,84 115,80 138,70
         C 158,60 172,96 194,94 C 214,92 235,60 258,52
         C 278,46 298,62 320,72 C 340,82 358,68 378,48
         C 398,30 418,36 440,54 C 460,70 474,62 492,52
         C 510,42 526,44 550,58 C 572,70 585,74 606,68
         C 626,62 640,52 662,48 C 682,44 698,36 722,44
         C 744,52 756,58 778,48 C 798,40 812,32 834,30
         C 856,28 868,36 890,42 C 912,48 928,40 950,34
         C 970,28 986,20 1010,18 C 1042,15 1075,11 1160,8"
  fill="none" stroke="#4ade80" stroke-width="3"
  stroke-linecap="round" stroke-linejoin="round"/>
```

## Script — GSAP Timeline + Canvas Slot Machine

### Key rules
- Timeline **must** be `paused: true` and registered on `window.__timelines["main"]`.
- Portfolio counter uses a plain object tweened by GSAP; `onUpdate` writes to the DOM.
- Slot machine uses **`<canvas>`** to avoid `text_box_overflow` inspector errors
  (a tall DOM reel would overflow its `overflow:hidden` clip at the layout level).
- All number formatting is deterministic (no `toLocaleString`).

```javascript
window.__timelines = window.__timelines || {};

/* ── Helpers ── */
function fmtDollar(n) {
  return '$' + Math.round(n).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
}
// Always 9 digits zero-padded: 000,000,000 → 750,000,000
function fmtCounter(n) {
  var s = Math.max(0, Math.round(n)).toString().padStart(9, '0');
  return s.slice(0,3) + ',' + s.slice(3,6) + ',' + s.slice(6,9);
}

/* ── Canvas slot machine ── */
var TARGET = 750000000;  // ← change this
var STEPS  = 80;
var stepSz = TARGET / STEPS;
var ROW_H  = 148;
var canvas = document.getElementById('slotCanvas');
var ctx    = canvas.getContext('2d');
var CW = 1536, CH = ROW_H;

// drawSlot: draws current + incoming row on the canvas.
// rawVal  — current animated value (0 → TARGET)
// progress — 0→1 normalised progress of the counter tween
function drawSlot(rawVal, progress) {
  ctx.clearRect(0, 0, CW, CH);

  var v       = Math.max(0, Math.min(TARGET, rawVal));
  var stepF   = v / stepSz;
  var stepIdx = Math.floor(stepF);
  var subFrac = stepF - stepIdx;                     // 0–1 within current step
  var speed   = Math.pow(Math.max(0, 1 - progress), 0.6); // 1=fast, 0=stopped

  var currVal = Math.round(Math.min(TARGET, stepIdx       * stepSz));
  var nextVal = Math.round(Math.min(TARGET, (stepIdx + 1) * stepSz));

  // current row scrolls upward; next row enters from below
  var currY = CH / 2 - subFrac * ROW_H * speed;
  var nextY = CH / 2 + ROW_H   - subFrac * ROW_H * speed;

  ctx.font         = 'bold 112px system-ui, -apple-system, sans-serif';
  ctx.textAlign    = 'center';
  ctx.textBaseline = 'middle';

  if (speed > 0.02 && subFrac > 0) {
    ctx.globalAlpha = subFrac * speed;
    ctx.fillStyle   = '#4ade80';
    ctx.fillText(fmtCounter(nextVal), CW / 2, nextY);
  }
  ctx.globalAlpha = 1;
  ctx.fillStyle   = '#4ade80';
  ctx.fillText(fmtCounter(currVal), CW / 2, currY);
}

drawSlot(0, 0); // initial frame

/* ── Portfolio counter ── */
var pfObj = { val: 2933 };  // ← change start/end
var pfEl  = document.getElementById('pfAmount');

/* ── Timeline ── */
var tl = gsap.timeline({ paused: true });

// 0.0s — wrap fades in
tl.to('#cardsWrap', { opacity: 1, duration: 0.45, ease: 'power2.out' }, 0);

// 0.0–2.5s — portfolio count-up
tl.to(pfObj, {
  val: 7980,               // ← change end value
  duration: 2.5,
  ease: 'power2.out',
  onUpdate: function () { pfEl.textContent = fmtDollar(pfObj.val); }
}, 0);

// 1.2s — bottom card slides up
tl.to('#viewsCard', { opacity: 1, y: 0, duration: 0.5, ease: 'power2.out' }, 1.2);

// 1.8–4.6s — slot machine (power2.out: fast start → slow finish)
var cntObj = { val: 0 };
tl.to(cntObj, {
  val: TARGET,
  duration: 2.8,
  ease: 'power2.out',
  onUpdate:  function () { drawSlot(cntObj.val, cntObj.val / TARGET); },
  onComplete: function () { drawSlot(TARGET, 1); }
}, 1.8);

window.__timelines['main'] = tl;
```

## Customisation guide

| What to change         | Where                                      |
|------------------------|--------------------------------------------|
| Page background        | `background: #292b3d` on `html, body`      |
| Card background        | `background: #111116` on `.card`           |
| Portfolio start/end    | `pfObj.val` initial + tween `val:`         |
| Portfolio label        | `.pf-label` text                           |
| Line chart shape       | SVG `<path>` control points               |
| X-axis day labels      | `<span>` contents in `.pf-x-axis`         |
| Counter target         | `var TARGET = 750000000`                   |
| Counter speed          | `duration: 2.8` + ease (`power2.out`)      |
| Counter color          | `ctx.fillStyle = '#4ade80'`                |
| Bottom labels          | `.views-label` / `.views-period` text      |
| Card enter timing      | `}, 1.2)` (second arg to last `tl.to`)     |
| Total duration         | `data-duration="8"` on `#root`             |

## Inspector notes

- `text_box_overflow` errors: **always use `<canvas>` for the slot counter**, never
  a tall DOM reel. The reel approach creates thousands of `text_box_overflow` errors
  because layout positions are checked before `overflow:hidden` is applied visually.
- Contrast warnings on `.pf-label`, `.pf-x-axis span`, `.views-period` are expected;
  they match the intentionally dim UI style of the reference design.
- Run `npm run check` after every edit; 0 errors and 0 layout issues is the bar.
