# Motion Stability

Rules for text that moves, appears, or disappears in video. A typeface that works perfectly in a static frame can become completely unreadable at the wrong animation speed or with the wrong GSAP parameters.

---

## The Core Problem

Web typography assumes text is stationary. Video typography has three additional constraints:

1. **Motion blur**: Text moving fast enough creates blur. Dense strokes (CJK, bold sans) accumulate blur faster than open strokes (thin Latin serifs).

2. **Compression artifacts**: H.264 and HEVC encode motion as differences between frames. Animated text edges trigger block encoding. The smaller the text and the faster it moves, the more artifact noise appears.

3. **Freeze-frame readability**: Any viewer, screen recorder, or social media thumbnail will freeze the video at an arbitrary moment. Every frame must work as a still.

---

## Safety Classification

### ✅ Safe Animations (all text sizes, all scripts)

| Animation | Parameters | Notes |
|---|---|---|
| Opacity fade-in | `opacity: 0→1, duration: 0.3–0.6s` | Default safe pattern |
| Small Y offset + fade | `y: 20–36px, opacity: 0→1, duration: 0.3–0.5s` | The standard reveal |
| Scale 0.95→1 + fade | `scale: 0.95→1, opacity: 0→1, duration: 0.3–0.5s` | Subtle push |
| Clip reveal (mask wipe) | text appears from behind a clipping rect | Zero motion blur |
| Static hold → fade out | `opacity: 1→0, duration: 0.25–0.4s` | All exits are safer than entrances |

### ⚠️ Conditional Animations (safe only above minimum size)

| Animation | Safe above | Risky below | Fix if below |
|---|---|---|---|
| Y translate 40–80px | 36px (CJK), 28px (Latin) | Below threshold | Reduce to 20–36px offset |
| X translate, moderate | 48px (CJK), 36px (Latin) | Below threshold | Use clip reveal instead |
| Scale 0→1 | 64px (CJK), 48px (Latin) | Below threshold | Fade only, no scale |
| Stagger reveal (multiple items) | 28px per item (CJK) | Below 24px | Reduce stagger delay |

### ❌ Unsafe Animations (avoid at all sizes, all scripts)

| Animation | Problem |
|---|---|
| Fast X translate: `x: 200px, duration: 0.2s` | Creates motion blur stripe; text unreadable during motion |
| Rotation entrance: `rotation: 5deg` | Rasterization artifacts on diagonal strokes, especially CJK |
| Scale from 0 at body size: `scale: 0→1` on 24px text | Subpixel rendering at small scale collapses strokes |
| Skew/perspective: `skewX: 5` | Optical distortion; looks broken at any CJK size |
| Word-by-word fly-in at small size | Each word has too few frames to read during motion |
| `blur()` filter on CJK display text | Doubles the blur artifact problem |

---

## Stroke Density vs. Motion Blur Table

The denser the strokes, the faster legibility degrades under motion blur.

| Script / Weight | Stroke density | Max safe Y translate velocity | Max safe X translate velocity |
|---|---|---|---|
| Latin thin / 300 | Low | 120px/0.3s | 80px/0.3s |
| Latin regular / 400 | Medium | 80px/0.3s | 60px/0.3s |
| Latin bold / 700 | Medium-high | 60px/0.3s | 40px/0.3s |
| Latin black / 900 | High | 50px/0.3s | 30px/0.3s |
| CJK regular / 400 | High | 50px/0.3s | 30px/0.3s |
| CJK bold / 700 | Very high | 40px/0.3s | 24px/0.3s |
| CJK black / 900 | Extreme | 30px/0.3s | 16px/0.3s |

"Velocity" = total translate distance / animation duration. Example: `y: 36px, duration: 0.4s` = 90px/s — safe for all Latin weights, safe for CJK 400–700, marginal for CJK 900.

---

## Freeze-Frame Test (Poster Test)

Every section must pass this test: pause the video at any point during the content hold time and the frozen frame must work as a standalone poster or thumbnail.

**Mandatory for each section:**
1. At least **1.0 second** of "clean hold" — no active animation, all text fully opaque
2. The dominant text hierarchy is immediately clear in one glance
3. No text is mid-fade (opacity between 0.3 and 0.7 is the "ugly middle")
4. No element is partially translated (mid-move looks like a layout error, not animation)

**GSAP implementation for clean holds:**
```javascript
// After entrance animations complete, always add a hold tween:
.to({}, { duration: 1.2 })  // minimum 1.0s clean hold
// Then exit:
.to('#section', { opacity: 0, duration: 0.3 })
```

If a section has no clean hold (e.g., entrance animations run until exit starts), it will produce no usable freeze-frames for thumbnails or reposts. Add the hold.

---

## Minimum Animation Duration Table

Each animation type has a minimum duration below which it becomes imperceptible or looks like a glitch rather than an intentional motion.

| Animation | Minimum duration | Optimal range |
|---|---|---|
| Fade-in | 0.15s | 0.3–0.5s |
| Fade-out / exit | 0.20s | 0.25–0.4s |
| Y translate entrance | 0.25s | 0.3–0.5s |
| Scale entrance | 0.20s | 0.3–0.4s |
| Clip wipe (horizontal) | 0.15s | 0.2–0.4s |
| Progress bar / width tween | 0.5s | 0.8–1.5s |
| Stagger delay between items | 0.06s | 0.08–0.15s |
| Timeline node assembly | 0.20s per node | 0.25–0.4s per node |

Below the minimum: the animation registers as a flash or a cut, not a motion. It wastes the GPU and confuses the viewer.

---

## Hold Time Recommendations by Section Type

| Section type | Minimum hold | Reason |
|---|---|---|
| Title / pain point | 1.5s | Viewer needs time to read emotional claim |
| Product demo / feature reveal | 1.0s | Must register what was revealed |
| Data / task list | 0.8s per item | Each item needs to land individually |
| CTA (call to action) | 2.0s | Most important frame; must be readable |
| Transition between sections | 0.0s | Transitions are not hold time |

---

## The GSAP Ease Guide for Legibility

Not all eases produce equal legibility during animation. Some eases are fast at the start and slow at the end (text lingers in the readable state); others decelerate quickly and leave a blur tail.

| Ease | Legibility profile | Recommended for |
|---|---|---|
| `power3.out` | Fast initial move → slow settle → fully readable quickly | Standard entrance — use by default |
| `power4.out` | Very fast initial → abrupt settle | Impact entrances for display text; CJK 900 weight |
| `power2.out` | Moderate — text readable for more of its travel | Support text, subtle reveals |
| `sine.inOut` | Equal ease in and out | Exit animations (text leaving frame) |
| `power2.in` | Accelerates through the exit | Clean exits; text is already read |
| `expo.out` | Extreme fast → very soft land | Show-off entrances; use sparingly |
| `linear` | Uniform velocity — constant motion blur throughout | Use only for progress bars, not text |
| `steps(N)` | Jump cuts | Typing/counter animations only |
| `bounce`, `elastic` | Overshoot | Never for video text. Always wrong. |

**Rule**: use `power3.out` or `power4.out` for entrances. Use `power2.in` or `sine.inOut` for exits. Never use `linear` on text.

---

## Subtitle Zone Rules

The subtitle-safe zone is the bottom 80–140px of the 720p frame (bottom 10–19%). Text in this zone is:
- Closest to video player controls (will be covered on mobile)
- Subject to letterboxing crop on some platforms
- Often rendered over dark gradient overlays (add if background is light)

Subtitle zone typography for video:
```css
.subtitle {
  position: absolute;
  bottom: 80px;        /* safe zone inset */
  left: 96px;
  right: 96px;
  font-size: 22px;     /* CJK minimum for subtitle */
  font-weight: 400;
  line-height: 1.35;
  letter-spacing: 0;   /* do not open-track subtitles */
  color: #EDEBE6;
  text-shadow: 0 1px 8px rgba(0,0,0,0.7); /* lift from dark backgrounds */
}
```

Subtitle text should not animate. It should appear and disappear with a simple opacity fade (0.15–0.2s). Translated subtitles moving across the frame are a broadcast convention only — not appropriate for promotional video.

---

## Pre-Render Audit Checklist

Before encoding MP4, verify:

- [ ] Every animated text element is within velocity limits in the Stroke Density table
- [ ] No text element animates below its minimum size threshold
- [ ] No `rotation`, `skewX`, or perspective transforms on text
- [ ] Every section has a clean hold of ≥ 1.0s (≥ 2.0s for CTA)
- [ ] All text entrances use `power3.out` or `power4.out`
- [ ] All exits use `power2.in` or `sine.inOut`
- [ ] No `linear` ease on any text tween
- [ ] CJK display text animation offset ≤ 36px Y / ≤ 16px X
- [ ] Subtitle zone text is opacity-only (no translate)
- [ ] `bounce` and `elastic` eases are absent from the codebase
