---
name: texture-hud
description: 质感 HUD 合成参考 — 三种材质面板（玻璃态/金属/新拟态）的 CSS 配方、色彩系统、SVG 圆环、光晕 Blob 背景、金属光扫动画与 GSAP 时间轴。用于创建或改编高质感深色 HUD / 数据看板视频合成。
---

# Texture HUD — 质感合成 Skill

## Canvas

| 属性 | 值 |
|---|---|
| 尺寸 | 1920 × 1080 px |
| 时长 | 9.05 s（0.45 s 入场 · ~5 s 展示 · 1.2 s 结尾） |
| composition-id | `texture-hud` |
| 背景色 | `#07091a`（极深海军蓝） |
| 字体 | `Inter, 'Helvetica Neue', Arial, sans-serif` |

---

## 色彩系统

| Token | 值 | 用途 |
|---|---|---|
| `--bg` | `#07091a` | 画布底色 |
| `--blue-blob` | `rgba(40,80,230,0.30)` | 背景光晕 1（左上） |
| `--purple-blob` | `rgba(130,28,195,0.24)` | 背景光晕 2（右） |
| `--teal-blob` | `rgba(0,155,145,0.22)` | 背景光晕 3（下中） |
| `--gold-blob` | `rgba(200,140,18,0.14)` | 背景光晕 4（右上） |
| `--accent-blue` | `#2260d8 → #6ba8ff` | 渐变蓝（进度环、CPU 条） |
| `--accent-gold` | `#a07418 → #e8c060` | 渐变金（内存条、金属边框） |
| `--accent-teal` | `#007d72 → #00d4b4` | 渐变青绿（网络条） |
| `--glass-bg` | `rgba(255,255,255,0.065)` | 玻璃面板底色 |
| `--glass-border` | `rgba(255,255,255,0.11)` | 玻璃面板边框 |
| `--metal-bg-from` | `#141929` | 金属面板渐变起始 |
| `--metal-bg-to` | `#0c1018` | 金属面板渐变结束 |
| `--metal-gold` | `rgba(190,160,68,0.22)` | 金属面板金色边框 |
| `--neu-bg` | `#0b1020` | 新拟态面板底色 |

---

## 布局 — 三栏结构

```
left=110   left=538          left=1422
┌────────┐ ┌──────────────┐  ┌────────┐
│ GLASS  │ │   METALLIC   │  │  NEU   │
│ 388×730│ │   844 × 730  │  │388×730 │
│        │ │              │  │        │
│ 3×metric│ │ ring + stats │  │4 status│
└────────┘ └──────────────┘  └────────┘
   top=176                      top=176
```

- 左右面板各 388px；中间面板 844px
- 间距：538 - (110+388) = 40px；1422 - (538+844) = 40px
- 面板顶部均 top=176px；title 区域 top=52px

---

## 材质 1 — 玻璃态（Glassmorphism）

```css
.glass-panel {
  background: rgba(255,255,255,0.065);
  backdrop-filter: blur(22px);
  -webkit-backdrop-filter: blur(22px);
  border: 1px solid rgba(255,255,255,0.11);
  box-shadow:
    0 8px 52px rgba(0,0,0,0.42),
    inset 0 1px 0 rgba(255,255,255,0.09),   /* 顶部高光线 */
    inset 0 -1px 0 rgba(0,0,0,0.15);         /* 底部暗线 */
  border-radius: 22px;
}
```

**关键点**：
- `backdrop-filter: blur(22px)` 需要面板后面有丰富内容（彩色 blob）才有效果
- 内嵌卡片再加一层 `rgba(255,255,255,0.045)` + `border: 1px solid rgba(255,255,255,0.07)` 制造深度
- 顶部高亮条：`inset 0 1px 0 rgba(255,255,255,0.09)` 模拟玻璃上边缘折射
- 每张子卡底部色条（`height:2px`）区分数据类型

```css
/* 子卡顶部高光线 (::before) */
.gcard::before {
  content: '';
  position: absolute; top: 0; left: 0; right: 0; height: 1px;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.13), transparent);
}
```

---

## 材质 2 — 金属质感（Metallic）

```css
.metal-panel {
  background: linear-gradient(158deg, #141929 0%, #0c1018 55%, #111826 100%);
  border: 1px solid rgba(190,160,68,0.22);
  box-shadow:
    0 0 90px rgba(190,160,68,0.07),          /* 外发光（极弱） */
    0 24px 80px rgba(0,0,0,0.6),
    inset 0 1px 0 rgba(190,160,68,0.18),     /* 金色顶光 */
    inset 0 -1px 0 rgba(0,0,0,0.3);
  border-radius: 22px;
}
```

**金色分割线**：
```css
.gold-rule {
  height: 1px;
  background: linear-gradient(90deg,
    transparent,
    rgba(190,160,68,0.45),
    rgba(190,160,68,0.2),
    transparent
  );
}
```

### 光扫动画（Shimmer）

在面板内叠一个绝对定位 div，用 GSAP 平移：

```html
<div id="shimmer" style="position:absolute;inset:0;pointer-events:none;z-index:3;
  border-radius:22px;
  background:linear-gradient(108deg,transparent 32%,rgba(255,255,255,0.055) 50%,transparent 68%);">
</div>
```

```javascript
tl.set('#shimmer', { x: '-120%' }, 0);
tl.to('#shimmer', { x: '220%', duration: 1.6, ease: 'power1.inOut' }, 2.0);  /* 第一次扫 */
tl.set('#shimmer', { x: '-120%' }, 5.8);
tl.to('#shimmer', { x: '220%', duration: 1.6, ease: 'power1.inOut' }, 5.8);  /* 第二次扫 */
```

---

## 材质 3 — 新拟态（Neumorphism）

深色背景上的凸起效果：

```css
.neu-panel {
  background: #0b1020;
  box-shadow:
    12px 12px 36px rgba(0,0,0,0.68),        /* 右下深阴影 */
    -6px -6px 22px rgba(32,58,110,0.13),    /* 左上蓝白阴影 */
    inset 0 1px 0 rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.035);
  border-radius: 22px;
}

/* 凸起子元素 */
.neu-item {
  background: #0b1020;
  box-shadow:
    6px 6px 18px rgba(0,0,0,0.55),
    -3px -3px 12px rgba(34,60,112,0.11);
  border-radius: 14px;
}

/* 凹陷子元素（inset） */
.neu-inset {
  background: #0b1020;
  box-shadow:
    inset 4px 4px 12px rgba(0,0,0,0.45),
    inset -2px -2px 8px rgba(34,60,112,0.1);
  border-radius: 12px;
}

/* 小图标块 */
.neu-icon {
  background: #0b1020;
  box-shadow:
    4px 4px 12px rgba(0,0,0,0.52),
    -2px -2px 8px rgba(34,60,112,0.1);
  border-radius: 12px;
}
```

**状态指示灯**（默认暗，GSAP 点亮）：
```css
.n-pip {
  width: 9px; height: 9px; border-radius: 50%;
  background: rgba(40,60,100,0.7);
  box-shadow: inset 2px 2px 4px rgba(0,0,0,0.4); /* 凹陷暗灯 */
}
```

```javascript
/* 点亮 */
tl.to('#np1', {
  backgroundColor: 'rgba(0,200,140,0.95)',
  boxShadow: '0 0 10px rgba(0,200,140,0.85)',
  duration: 0.3
}, 1.7);
```

---

## 背景光晕 Blob

大圆形 + `filter: blur(110px)` → 为玻璃面板提供丰富底色：

```html
<div style="position:absolute;width:720px;height:720px;border-radius:50%;
  filter:blur(110px);pointer-events:none;
  background:rgba(40,80,230,0.30);left:-60px;top:-100px;"></div>
```

4 个 blob 覆盖画面不同区域，配合玻璃面板背景模糊制造彩色折射感。

---

## SVG 圆环进度（Ring Gauge）

```
r = 118px, cx = cy = 150 (300×300 viewBox)
circumference = 2π × 118 ≈ 741
```

```html
<svg width="300" height="300" viewBox="0 0 300 300">
  <defs>
    <linearGradient id="rg" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#2260d8"/>
      <stop offset="100%" stop-color="#6ba8ff"/>
    </linearGradient>
    <filter id="rglow">
      <feGaussianBlur stdDeviation="3.5" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <!-- 底轨 -->
  <circle cx="150" cy="150" r="118" fill="none"
    stroke="rgba(255,255,255,0.055)" stroke-width="18"/>
  <!-- 活跃填充（从 -90° 起始，顺时针） -->
  <circle cx="150" cy="150" r="118" id="ring-fill" fill="none"
    stroke="url(#rg)" stroke-width="18"
    stroke-dasharray="741" stroke-dashoffset="741"
    stroke-linecap="round" filter="url(#rglow)"
    transform="rotate(-90 150 150)"/>
</svg>
```

**填充公式**：
```javascript
const CIRC = 741; /* 2π × 118 */
const target = 0.87; /* 87% */
tl.to('#ring-fill', {
  strokeDashoffset: CIRC * (1 - target), /* = 741 × 0.13 = 96.3 */
  duration: 2.1, ease: 'power2.out'
}, 1.1);
```

**不同半径速查**：

| r | circumference |
|---|---|
| 100 | 628 |
| 118 | 741 |
| 128 | 804 |
| 140 | 880 |
| 160 | 1005 |

---

## GSAP 时间轴（9.05 s）

```javascript
const tl = gsap.timeline({ paused: true });
const CIRC = 741;

/* 0.0 — Blobs 渐入 */
tl.from(['#b1','#b2','#b3','#b4'], { opacity: 0, duration: 1.4, stagger: 0.12 }, 0);

/* 0.15 — 标题从上滑入 */
tl.from('#title-wrap', { y: -44, opacity: 0, duration: 0.7, ease: 'power2.out' }, 0.15);

/* 0.45 — 三块面板交错上滑 */
tl.from(['#pl','#pc','#pr'], { y: 44, opacity: 0, duration: 0.7, ease: 'power2.out', stagger: 0.13 }, 0.45);

/* 设置 shimmer 初始位置（不进入 Timeline 之前先 set） */
tl.set('#shimmer', { x: '-120%' }, 0);

/* 1.0–2.4 — 数字计数器 */
tl.to({ n: 0 }, { n: 2.4, duration: 1.5, ease: 'power2.out',
  onUpdate: function() { document.getElementById('gv1').textContent = this.targets()[0].n.toFixed(1); }
}, 1.0);

/* 1.1 — 进度环填充到 87% */
tl.to('#ring-fill', { strokeDashoffset: CIRC * 0.13, duration: 2.1, ease: 'power2.out' }, 1.1);

/* 1.3–1.66 — 侧边数据条 */
tl.to('#sf1', { width: '64%', duration: 1.3, ease: 'power2.out' }, 1.3);
tl.to('#sf2', { width: '48%', duration: 1.3, ease: 'power2.out' }, 1.48);
tl.to('#sf3', { width: '78%', duration: 1.3, ease: 'power2.out' }, 1.66);

/* 1.7–2.3 — 状态灯逐个点亮 (stagger 0.2s) */
/* ... 见模板 ... */

/* 2.0 — 金属面板第一次光扫 */
tl.to('#shimmer', { x: '220%', duration: 1.6, ease: 'power1.inOut' }, 2.0);
/* 5.8 — 第二次光扫 */
tl.set('#shimmer', { x: '-120%' }, 5.8);
tl.to('#shimmer', { x: '220%', duration: 1.6, ease: 'power1.inOut' }, 5.8);

/* 8.2 — Outro: 面板逆序飞出 */
tl.to(['#pr','#pc','#pl'], { y: -36, opacity: 0, duration: 0.42, ease: 'power2.in', stagger: 0.1 }, 8.2);
tl.to('#title-wrap', { y: -36, opacity: 0, duration: 0.4, ease: 'power2.in' }, 8.5);
tl.to(['#b1','#b2','#b3','#b4'], { opacity: 0, duration: 0.5 }, 8.55);

window.__timelines = window.__timelines || {};
window.__timelines['texture-hud'] = tl;
```

### 动画序列一览

| 时间 | 动效 |
|---|---|
| 0.0 | 背景光晕渐入 |
| 0.15 | 标题从上滑入 |
| 0.45 | 三面板交错上滑 |
| 1.0–2.6 | 玻璃面板数字计数 (2.4M / 124K / 99.9%) |
| 1.1–3.2 | 进度环 0→87%，数字同步 |
| 1.3–2.96 | 侧边进度条填充（蓝/金/青） |
| 1.7–2.5 | 新拟态状态灯逐个点亮 |
| 2.0 | 金属面板第一次光扫 |
| 2.1–3.5 | Sessions 计数 0→1247 |
| 5.8 | 金属面板第二次光扫 |
| 8.2 | Outro — 面板右→中→左逆序飞出 |
| 8.5 | 标题淡出 |
| 8.55 | Blobs 淡出 |

---

## 定制指南

### 更换主题色（蓝→紫）

替换所有 `#2260d8 / #6ba8ff` 为紫色 `#6620d8 / #b06bff`，同步调整 blob 色与面板边框色。

### 修改进度环目标值

```javascript
const target = 0.78; /* 改为 78% */
tl.to('#ring-fill', { strokeDashoffset: CIRC * (1 - target), ... }, 1.1);
```

### 增加面板

三栏布局固定于 `left: 110 / 538 / 1422`。增加第四栏前需要调整总宽度：
- 四栏各 282px + 间距 40px × 3 = 1128 + 120 = 1248px，左边距 (1920-1248)/2 = 336px

### 更换状态灯颜色

修改 `pipC` 数组中对应索引的 `rgba(...)` 值。

### 关闭 Shimmer（光扫）

删除 `#shimmer` 元素及相关 GSAP 语句。

---

## HyperFrames 根元素

```html
<div id="root"
  data-composition-id="texture-hud"
  data-width="1920"
  data-height="1080">
```

---

## 技术注意事项

- `backdrop-filter: blur(22px)` 需要加 `-webkit-backdrop-filter` 前缀确保 Chrome 兼容
- 光晕 Blob 必须在玻璃面板之前渲染（DOM 顺序在前），blur 才能采样到颜色
- Shimmer 用 `z-index:3` 确保在面板内容之上；`pointer-events:none` 避免遮挡交互
- 新拟态在**深色**背景上最佳；浅色背景下阴影比例需要重新调整
- GSAP `onUpdate` 中用 `this.targets()[0].n` 读取中间值；必须使用 `function()` 而非箭头函数

---

## 参考

- 渲染输出：`my-video/renders/texture-hud.mp4`（1920×1080, 30fps, 9.05s, 1.2MB）
- 模板：`templates/texture-hud.html`
- 相关技术：Glassmorphism CSS, Neumorphism dark, SVG stroke-dasharray animation
