---
name: progress-bar-hud
description: 进度条 HUD 合成参考 — 五种进度条类型（多步骤/Tooltip/文字百分比/步骤圆圈/倒计时）的 CSS 配方、两阶段填满动画、圆圈状态切换与 GSAP 时间轴。用于创建或改编进度条展示类视频合成。
---

# Progress Bar HUD — Skill

## Canvas

| 属性 | 值 |
|---|---|
| 尺寸 | 1920 × 1080 px |
| 时长 | 7.73 s（入场 1.2 s · Phase 1 填至 50% · Phase 2 填至 100% · Hold · 出场） |
| composition-id | `progress-bar-hud` |
| 背景色 | `#f0ebe3`（暖米色） |
| 字体 | `Inter, Arial, sans-serif` |

---

## 色彩系统

| Token | 值 | 用途 |
|---|---|---|
| `--bg` | `#f0ebe3` | 画布 / 数字圆圈背景 |
| `--card-bg` | `#ffffff` | 卡片背景 |
| `--fill` | `#2a2a2a` | 进度条填充色 / 完成圆圈 |
| `--track` | `#e2ddd6` | 进度条轨道 |
| `--text-dark` | `#252525` | 主要文字 |
| `--text-muted` | `#b0aba2` | 次要文字 / 未激活标签 |
| `--num-border` | `#cac5bc` | 数字圆圈边框 |
| `--circle-border` | `#d0cbc3` | 步骤圆圈默认边框 |

---

## 布局

```
left=300px, width=1320px, top=224px
┌──────────────────────────────────────────────────┐
│  ⓵  [card: multi-step bar]          margin-b:14px│
│  ⓶  [card: tooltip bar]                          │
│  ⓷  [card: text + % bar]                         │
│  ④  [card: step circles]                          │
│  ⑤  [card: timer bar]                            │
└──────────────────────────────────────────────────┘
```

- 每行 `.row`：`display:flex; align-items:center`
- `.num` 圆圈：`62×62px`，`margin-right:22px`
- `.card`：`flex:1`，`border-radius:14px`，`padding:20px 30px`，`box-shadow:0 2px 12px rgba(0,0,0,0.06)`

---

## 卡片 1 — 多步骤进度条

```html
<div class="c1-wrap">         <!-- position:relative; height:20px -->
  <div class="c1-track"></div> <!-- 全宽轨道 h=7px -->
  <div class="c1-fill" id="c1fill"></div>  <!-- width 从 0 动画 -->
  <div class="c1-dot filled" id="c1d1" style="left:0%"></div>
  <div class="c1-dot active"  id="c1d2" style="left:33.33%"></div>
  <div class="c1-dot"         id="c1d3" style="left:66.67%"></div>
  <div class="c1-dot"         id="c1d4" style="left:100%"></div>
</div>
```

```css
.c1-dot          { background:#e2ddd6; width:11px; height:11px; margin-left:-5.5px; }
.c1-dot.filled   { background:#2a2a2a; }
.c1-dot.active   { background:#fff; box-shadow:0 0 0 2.5px #2a2a2a; } /* 白心+深色环 */
```

**完成动画（dot ring → filled）**：
```javascript
tl.to('#c1d2', { backgroundColor: '#2a2a2a', boxShadow: '0 0 0 0px #2a2a2a', duration: 0.22 }, t);
```

---

## 卡片 2 — Tooltip 进度条

```html
<div class="prog-track" style="overflow:visible;">
  <div class="prog-fill" id="c2fill"></div>
  <div class="c2-tip" id="c2tip" style="left:50%;">50%</div>
</div>
```

```css
.c2-tip {
  position:absolute; top:-42px;
  background:#2a2a2a; color:#fff;
  font-size:15px; font-weight:700; padding:5px 11px; border-radius:7px;
  transform:translateX(-50%); opacity:0; white-space:nowrap;
}
.c2-tip::after {                       /* 下箭头 */
  content:''; position:absolute; top:100%; left:50%; transform:translateX(-50%);
  border:6px solid transparent; border-top-color:#2a2a2a;
}
```

**Tooltip 同步移动**（Phase 2，百分比从 50→100 时）：
```javascript
tl.to({ pct: 50 }, {
  pct: 100, duration: 1.0, ease: 'power2.inOut',
  onUpdate: function() {
    const v = Math.round(this.targets()[0].pct);
    const el = document.getElementById('c2tip');
    el.textContent = v + '%';
    el.style.left = v + '%';   /* 跟随填充位置移动 */
  }
}, 3.6);
```

---

## 卡片 3 — 文字百分比进度条

```html
<div class="c3-header">
  <div class="c3-lbl">Your Progress...</div>
  <div class="c3-pct" id="c3pct">0%</div>
</div>
<div class="prog-track"><div class="prog-fill" id="c3fill"></div></div>
```

计数器 tween（需用 `function()` 而非箭头函数）：
```javascript
tl.to({ n: 0 }, {
  n: 50, duration: 0.9, ease: 'power2.out',
  onUpdate: function() {
    document.getElementById('c3pct').textContent = Math.round(this.targets()[0].n) + '%';
  }
}, 1.4);
```

---

## 卡片 4 — 步骤圆圈

### HTML 结构

每个圆圈包含 `.c4-inner-dot`（active 状态的实心点）和 `.c4-check`（done 状态的打勾 SVG）：

```html
<div class="c4-circle active" id="c4c3">
  <div class="c4-inner-dot" id="c4c3dot"></div>
  <svg class="c4-check" id="c4c3chk" width="22" height="22" viewBox="0 0 22 22" fill="none">
    <path d="M4.5 11.5l4.5 4.5 9-9" stroke="#fff" stroke-width="2.5"
          stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
</div>
```

### 三种状态

| 状态 | CSS | 视觉 |
|---|---|---|
| 默认（未来步骤） | `.c4-circle` | 白底，浅色边框 |
| 活跃（当前步骤） | `.c4-circle.active` | 白底，深色边框 + 实心点（`.c4-inner-dot` opacity:1） |
| 完成 | `.c4-circle.done` | 深色底，深色边框，打勾 SVG（`.c4-check` opacity:1） |

```css
.c4-circle      { border:2.5px solid #d0cbc3; background:#fff; }
.c4-circle.done { background:#2a2a2a; border-color:#2a2a2a; }
.c4-circle.active { border-color:#2a2a2a; }
.c4-inner-dot   { width:18px; height:18px; border-radius:50%; background:#2a2a2a; opacity:0; position:absolute; }
.c4-circle.active .c4-inner-dot { opacity:1; }
.c4-check       { opacity:0; position:absolute; }
.c4-circle.done .c4-check { opacity:1; }
```

### active → done 动画

```javascript
/* 1. 隐藏实心点 */
tl.to('#c4c3dot', { opacity: 0, duration: 0.15 }, 4.2);
/* 2. 圆圈变黑 */
tl.to('#c4c3', { backgroundColor: '#2a2a2a', borderColor: '#2a2a2a', duration: 0.25 }, 4.2);
/* 3. 打勾淡入 */
tl.to('#c4c3chk', { opacity: 1, duration: 0.22 }, 4.38);
```

### 连接线

```css
.c4-line {
  position:absolute; top:33px; left:30px; right:30px;
  height:3px; background:#e2ddd6; border-radius:2px;
}
.c4-line-fill {
  position:absolute; top:0; left:0; height:100%;
  background:#2a2a2a; border-radius:2px; width:0;
}
```

`width: '50%'` = 连线到第 3 步（5 步中的中点）。

---

## 卡片 5 — 倒计时进度条

```html
<div class="c5-timer">
  <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
    <circle cx="9" cy="9" r="7.5" stroke="#b0aba2" stroke-width="1.5"/>
    <path d="M9 5.5V9l2.5 1.5" stroke="#b0aba2" stroke-width="1.5" stroke-linecap="round"/>
  </svg>
  <span id="c5timer">60 sec left</span>
</div>
```

倒计时 tween：
```javascript
tl.to({ n: 30 }, {
  n: 0, duration: 1.0, ease: 'power2.inOut',
  onUpdate: function() {
    const s = Math.round(this.targets()[0].n);
    document.getElementById('c5timer').textContent = s > 0 ? s + ' sec left' : 'Complete!';
  }
}, 3.9);
```

---

## GSAP 两阶段填满时间轴

```javascript
const tl = gsap.timeline({ paused: true });

/* ── INTRO ── */
tl.from('#hud-title', { y: -48, opacity: 0, duration: 0.65, ease: 'power2.out' }, 0);
tl.from(['#row1','#row2','#row3','#row4','#row5'], {
  y: 32, opacity: 0, duration: 0.5, ease: 'power2.out', stagger: 0.1
}, 0.3);

/* ── PHASE 1: 填至 50% (t=1.2–2.6) ── */
tl.to('#c1fill', { width: '37%',  duration: 0.8, ease: 'power2.out' }, 1.2); /* 到 Shipping */
tl.to('#c2fill', { width: '50%',  duration: 0.9, ease: 'power2.out' }, 1.3);
tl.to('#c2tip',  { opacity: 1,    duration: 0.28 }, 1.8);
tl.to('#c3fill', { width: '50%',  duration: 0.9, ease: 'power2.out' }, 1.4);
tl.to('#c4fill', { width: '50%',  duration: 1.0, ease: 'power2.out' }, 1.5);
tl.to('#c5fill', { width: '50%',  duration: 1.0, ease: 'power2.out' }, 1.6);
/* + 对应计数器 tween ... */

/* ── PHASE 2: 填至 100% (t=3.5–5.3) ── */
tl.to('#c1fill', { width: '100%', duration: 1.0, ease: 'power2.inOut' }, 3.5);
/* c1 dots 逐个点亮: t=3.88, 4.1, 4.42 */
tl.to('#c2fill', { width: '100%', duration: 1.0, ease: 'power2.inOut' }, 3.6);
/* c2 tooltip 滑动至 100%: onUpdate 更新 el.style.left */
tl.to('#c3fill', { width: '100%', duration: 1.0, ease: 'power2.inOut' }, 3.7);
tl.to('#c4fill', { width: '100%', duration: 1.0, ease: 'power2.inOut' }, 3.8);
/* c4 圆圈依次 active→done: t=4.2, 4.55, 4.9 */
tl.to('#c5fill', { width: '100%', duration: 1.0, ease: 'power2.inOut' }, 3.9);
/* c5 timer 30→0 → 'Complete!' */

/* ── HOLD 5.3–7.0 s ── */

/* ── OUTRO ── */
tl.to(['#row5','#row4','#row3','#row2','#row1'], {
  y: -28, opacity: 0, duration: 0.35, ease: 'power2.in', stagger: 0.07
}, 7.0);
tl.to('#hud-title', { y: -30, opacity: 0, duration: 0.38, ease: 'power2.in' }, 7.35);

window.__timelines = window.__timelines || {};
window.__timelines['progress-bar-hud'] = tl;
```

### 时序一览

| 时间 | 动效 |
|---|---|
| 0.0 | 标题从上滑入 |
| 0.3 | 5 行卡片交错上滑 |
| 1.2–2.6 | Phase 1：各进度条填至 50%，Tooltip 出现，倒计时 60→30 |
| 3.5–4.9 | Phase 2：全部填至 100%，步骤圆圈逐个打勾，倒计时 30→0 |
| 5.3–7.0 | Hold（完成状态稳定展示） |
| 7.0 | Outro：row5→1 逆序上飞淡出 |
| 7.35 | 标题淡出 |
| 7.73 | 结束 |

---

## 通用进度条 CSS

```css
/* 轨道 */
.prog-track {
  position: relative;
  height: 12px; background: #e2ddd6; border-radius: 6px; overflow: visible;
}
/* 填充（初始 width:0，由 GSAP 动画） */
.prog-fill {
  position: absolute; left: 0; top: 0; bottom: 0;
  background: #2a2a2a; border-radius: 6px; width: 0;
}
```

---

## 定制指南

### 修改进度条颜色

替换 `#2a2a2a`（填充）和 `#e2ddd6`（轨道）为目标色，同时更新 `.c4-circle.done` 背景色。

### 修改步骤数量

卡片 4 支持任意步骤数：
- 调整 HTML 中 `.c4-step` 数量
- Phase 1 线条 `width` = `(目标步骤-1) / (总步骤-1) * 100%`
- Phase 2 各圆圈按 `stagger * 0.35s` 间隔动画

### 修改 Phase 1 停留百分比

更改 Phase 1 各 tween 的 `width` 值，同时调整计数器的 `n` 终点。

### 移除 Phase 1（直接填满）

删除所有 `t=1.2–2.6` 的 tween，保留 Phase 2 直接从 `width:0` 填至 `100%`。

---

## HyperFrames 根元素

```html
<div id="root"
  data-composition-id="progress-bar-hud"
  data-width="1920"
  data-height="1080">
```

---

## 参考

- 渲染输出：`my-video/renders/progress-bar-hud.mp4`（1920×1080, 30fps, 7.73s）
- 模板：`templates/progress-bar-hud.html`
- 设计参考：Types Of Progress Bar（暖米色背景，炭黑填充，白卡片）
