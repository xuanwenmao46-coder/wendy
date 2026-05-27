---
name: breaking-news-24
description: Layout, color, and animation reference for the "24 Breaking News" broadcast lower-third composition. Covers pixel measurements, SVG world map projection, banner entrance sequence, ticker scroll, LIVE badge blink, and GSAP timeline structure. Use when creating or modifying broadcast news-style HyperFrames compositions.
---

# Breaking News 24 — Composition Skill

## Canvas

- **Resolution**: 1920 × 1080 px
- **Duration**: 8 s (1.5 s intro · ~5.3 s hold · 1.2 s outro)
- **composition-id**: `breaking-news-24`
- **Background**: `#030810` (near-black navy)
- **Font stack**: `Impact, 'Franklin Gothic Heavy', 'Arial Narrow', Arial, sans-serif`

---

## Color Palette

| Token | Hex | Usage |
|---|---|---|
| `--bg` | `#030810` | Canvas, letterbox bars |
| `--ocean-center` | `#0d2e50` | World map ocean gradient center |
| `--ocean-mid` | `#0a2540` | World map ocean gradient mid |
| `--ocean-edge` | `#060f1f` | World map ocean gradient edge |
| `--continent` | `#1a688f` | SVG continent fill (teal-blue) |
| `--continent-stroke` | `rgba(40,120,165,0.35)` | Continent highlight rim stroke |
| `--grid-line` | `rgba(30,90,130,0.18)` | Lat/lon grid lines |
| `--red` | `#e5140a` | "24" box, LIVE badge, bot-box24 |
| `--banner-dark` | `rgba(6,15,28,0.97)` | "BREAKING NEWS" dark panel |
| `--banner-shadow` | `rgba(6,16,30,0.97)` | 3D face above banner |
| `--ticker-bg` | `rgba(3,8,16,0.82)` | Ticker bar backgrounds |
| `--ticker-text` | `rgba(200,220,235,0.38)` | Ticker text (dimmed monospace) |
| `--bot-stripe` | `rgba(6,15,28,0.92)` | Bottom "24 NEWS" stripe |

---

## Layout — Vertical Zones

```
y=0     ┌────────────────────────────────────────────────────┐
        │  lb-top  (letterbox, h=68px, #030810)             │
y=68    ├────────────────────────────────────────────────────┤
        │  tkbar-top  (ticker, h=26px)                       │
y=94    ├────────────────────────────────────────────────────┤
        │                                                    │
        │         world map SVG (full 1920×1080)             │
        │         visible area: y=94 – y=850                 │
        │                                                    │
y=850   ├────────────────────────────────────────────────────┤
        │  tkbar-bot  (ticker, h=26px, bottom=230)           │
y=876   ├────────────────────────────────────────────────────┤
        │  lb-bot  (letterbox, h=230px, #030810)             │
y=850   │  bot-stripe  (bottom=165, h=65px)                  │
y=915   │  tkbar-bot2  (bottom=130, h=26px)                  │
y=1080  └────────────────────────────────────────────────────┘
```

---

## Main Banner

```
left=462px, top=490px, height=142px
┌──────────────────────────────────────────────────────────────┐
│  #box24 (195×142, red #e5140a)   │  #banner-dark (638×142)  │
│  "24"  88px white Impact 900     │  "BREAKING NEWS" 65px     │
│                  4px dark divider│  italic white Impact 900  │
│                                  │  clip-path angled right   │
└──────────────────────────────────────────────────────────────┘
total width: 833px  (195 + 638)
```

- `#banner-shadow`: `left=498, top=365, width=312, height=128` — dark upper 3D face
  - `clip-path: polygon(22px 0%, 100% 0%, 100% 100%, 0% 100%)`
- `#box24::after`: 4px dark right-edge divider `rgba(0,0,0,0.35)`
- `#banner-dark` angled right: `clip-path: polygon(0 0, calc(100% - 18px) 0%, 100% 100%, 0% 100%)`
- `#bntxt .brk`: pure `#fff`; `.nws`: `rgba(180,210,230,0.88)` (slight blue tint)

### LIVE Badge

```
left=1200px, top=453px, width=136px, height=54px
background: #e5140a
"LIVE"  24px Impact 900 white  letter-spacing: 4px
transform-origin: center bottom
```

---

## World Map SVG

### Equirectangular Projection Formula

```
x = (lon + 180) / 360 * 1920
y = (90 - lat) / 180 * 1080
```

Key reference points:
| Location | lon, lat | SVG x, y |
|---|---|---|
| Prime meridian (0°) | 0, 0 | 960, 540 |
| Date line (180°) | 180, 0 | 1920, 540 |
| New York (−74°, 41°) | — | 565, 294 |
| London (0°, 51°) | — | 960, 235 |
| Tokyo (140°, 36°) | — | 1707, 324 |
| Sydney (151°, −34°) | — | 1727, 722 |

### Map Layers (in z-order)

1. **Ocean radial gradient** — `<rect fill="url(#oceangrd)"/>` — `cx=52%, cy=48%`
2. **Grid lines** — horizontal (equator, tropics ±23.5°, polar circles ±66.5°) + vertical every 45°
3. **Continent fills** — `fill="#1a688f"`, `filter="url(#mapblur)"` (stdDeviation=0.8), `opacity=0.88`
4. **Continent highlight strokes** — `stroke="rgba(40,120,165,0.35)"`, `stroke-width=0.8`

### Continent Paths Included

North America, Alaska peninsula, Greenland, South America, Europe (mainland + Scandinavia), British Isles, Africa, Madagascar, Asia (main mass), India subcontinent, Sri Lanka, Japan, Taiwan, Indonesia (4 islands), Australia, New Zealand, Philippines.

---

## Bottom Elements

### `#bot-stripe`

```css
position: absolute;
left: 0; right: 0; bottom: 165px; height: 65px;
background: rgba(6,15,28,0.92);
display: flex; align-items: center;
```

- `#bot-box24`: `72×65px`, `#e5140a`, "24" 34px white
- `#bot-text`: Courier New 16px, letter-spacing 3px, `rgba(200,220,235,0.75)`, repeating "BREAKING NEWS * " text

### `#tkbar-bot2`

```css
bottom: 130px; height: 26px;
background: rgba(3,8,16,0.82);
```

---

## Ticker Bands

All three tickers share:
- Font: `'Courier New', monospace`, 13px, letter-spacing 2px
- Text color: `rgba(200,220,235,0.38)`
- Content: `"24 NEWS &nbsp;*&nbsp; "` repeated 30×

GSAP scroll: `{ x: -1800, duration: 7.4, ease: 'none' }` — start at t=0.2s

---

## GSAP Animation Timeline (8 s)

```javascript
const tl = gsap.timeline({ paused: true });
const DUR = 8;

// t=0: map fade + slow scale-down (cinematic zoom-out)
tl.from('#mapsvg',  { opacity: 0, duration: 0.8 }, 0);
tl.from('#glow',    { opacity: 0, duration: 1.0 }, 0.1);
tl.fromTo('#mapsvg',
  { scale: 1.06, transformOrigin: '50% 48%' },
  { scale: 1.00, duration: DUR, ease: 'power1.out' }, 0);

// t=0.2: tickers fade in + start scrolling
tl.from('#tkbar-top', { opacity: 0, duration: 0.4 }, 0.2);
tl.from('#tkbar-bot', { opacity: 0, duration: 0.4 }, 0.2);
tl.to('#tk-top',  { x: -1800, duration: 7.4, ease: 'none' }, 0.2);
tl.to('#tk-bot',  { x: -1800, duration: 7.4, ease: 'none' }, 0.2);

// t=0.48: reveal banner wrapper
tl.to('#banner-wrap', { opacity: 1, duration: 0.05 }, 0.48);

// t=0.5: red "24" box slides from left
tl.from('#box24',        { x: -280, opacity: 0, duration: 0.45, ease: 'power2.out' }, 0.5);
// t=0.55: 3D shadow follows
tl.from('#banner-shadow',{ x: -280, opacity: 0, duration: 0.45, ease: 'power2.out' }, 0.55);
// t=0.72: dark panel wipes in (scaleX from left)
tl.from('#banner-dark',  { scaleX: 0, transformOrigin: 'left center', duration: 0.5, ease: 'power2.out' }, 0.72);
// t=1.05: text fades in after bar arrives
tl.from('#bntxt',        { opacity: 0, x: 30, duration: 0.4, ease: 'power2.out' }, 1.05);
// t=1.15: LIVE badge drops from above
tl.from('#live-badge',   { y: -60, opacity: 0, duration: 0.4, ease: 'back.out(1.4)' }, 1.15);

// t=0.7-0.8: bottom elements
tl.to('#bot-stripe',  { opacity: 1, duration: 0.4 }, 0.7);
tl.to('#tkbar-bot2',  { opacity: 1, duration: 0.4 }, 0.8);
tl.to('#tk-bot2',     { x: -1800, duration: 7.0, ease: 'none' }, 0.8);

// t=2.5 & t=5.0: LIVE blink (2 pulses)
tl.to('#live-txt', { opacity: 0.3, duration: 0.18, yoyo: true, repeat: 5, ease: 'none' }, 2.5);
tl.to('#live-txt', { opacity: 0.3, duration: 0.18, yoyo: true, repeat: 5, ease: 'none' }, 5.0);

// t=6.8: outro — staggered fade
tl.to('#banner-wrap', { opacity: 0, y: -8, duration: 0.5, ease: 'power2.in' }, 6.8);
tl.to('#bot-stripe',  { opacity: 0, duration: 0.4, ease: 'power2.in' }, 6.9);
tl.to('#tkbar-bot2',  { opacity: 0, duration: 0.4 }, 7.0);
tl.to(['#tkbar-top','#tkbar-bot'], { opacity: 0, duration: 0.4 }, 7.1);
tl.to('#mapsvg',      { opacity: 0, duration: 0.5 }, 7.3);
tl.to('#glow',        { opacity: 0, duration: 0.4 }, 7.3);

window.__timelines = window.__timelines || {};
window.__timelines['breaking-news-24'] = tl;
```

### Animation Sequence Summary

| Time | Event |
|---|---|
| 0.0 | Map fades in, begins slow scale 1.06→1.00 over 8 s |
| 0.2 | Tickers appear and start scrolling left |
| 0.48 | Banner wrapper becomes visible |
| 0.5 | Red "24" box slides in from left (−280px) |
| 0.55 | 3D shadow slides in |
| 0.7 | Bottom stripe fades in |
| 0.72 | Dark "BREAKING NEWS" panel wipes in (scaleX 0→1) |
| 0.8 | Second bottom ticker appears and starts scrolling |
| 1.05 | "BREAKING NEWS" text fades in with +30px slide |
| 1.15 | LIVE badge drops from above (back.out bounce) |
| 2.5 | First LIVE blink pulse (5 cycles × 0.18 s) |
| 5.0 | Second LIVE blink pulse |
| 6.8 | Banner fades out (y: −8 drift) |
| 6.9–7.1 | Bottom stripe and tickers fade out staggered |
| 7.3 | Map and glow fade to black |

---

## HyperFrames Root Element

```html
<div id="root"
  data-composition-id="breaking-news-24"
  data-width="1920"
  data-height="1080">
```

---

## Customization Guide

### Change headline text

Edit `#bntxt` span content. Keep "BREAKING" in `.brk` (white), "NEWS" in `.nws` (blue-tinted).

### Change accent color (red → another color)

Replace `#e5140a` in `#box24`, `#live-badge`, `#bot-box24` CSS rules.

### Adjust banner vertical position

Change `top:490px` on `#banner-bar` and `top:365px` / `top:453px` on `#banner-shadow` and `#live-badge` proportionally.

### Adjust banner width

- `#box24` width: controls the number box (default 195px)
- `#banner-dark` width: controls the text panel (default 638px)
- Total: 195 + 638 = 833px starting at left=462px → right edge at 1295px

### Extend duration

Change `const DUR = 8` and push outro start times forward. Recompute LIVE blink repeat counts if needed (keep finite: `repeat: N` never `-1`).

### Add headline ticker (scrolling news text)

Replace the static `#bntxt` text with a longer string and add a GSAP x-scroll tween inside `#banner-dark` overflow.

---

## Template

Full working composition at `templates/breaking-news-24.html`.

```bash
cp .agents/skills/breaking-news-24/templates/breaking-news-24.html \
   my-video/compositions/my-breaking-news.html
```

---

## References

- Source video: `9ff5eddf-12.mp4` (3840×2160, 25fps, 3.92s, H.264)
- Rendered output: `my-video/renders/breaking-news-24.mp4` (1920×1080, 30fps, 8s)
- Pixel analysis method: `ffmpeg -ss N -i video.mp4 -update 1 -vframes 1 frame.png` then Python/PIL coordinate scan
- Equirectangular SVG formula: `x = (lon+180)/360*1920`, `y = (90-lat)/180*1080`
