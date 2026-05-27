---
name: hud-gprs
description: 生成战术/监控风格 HUD-GPRS 合成视频。包含双视频面板（上方真人画面 + 下方卫星地图）、左侧仪表盘、右侧仪表群+罗盘。当用户要求「生成 HUD 视频」「监控界面」「战术界面」「复刻 HUD GPRS 风格」时调用。提供完整的 1920×1080 HyperFrames HTML + GSAP 时间线模板。
---

# HUD-GPRS Composition Skill

生成 1920×1080 战术监控 HUD 视频，使用 HyperFrames + GSAP。

## 快速使用

直接复制 [templates/hud-gprs.html](./templates/hud-gprs.html) 作为起点，按需替换视频源和文字。

---

## 布局结构（像素精确）

```
┌─────────────────────────────── 1920px ───────────────────────────────┐
│  frame border (inset 12px)                                           │
│  topbar: 38px tall, center-aligned data text                         │
├──── 428px ────┬──────────── 1040px ────────────┬──── 428px ────┤  ↑  │
│   LEFT PANEL  │   CENTER SECTION               │  RIGHT PANEL  │     │
│               │  ┌──── crowd panel ────┐       │               │     │
│  UI-GPRS      │  │  top: 65px          │       │  -IH // HI-   │     │
│  (82px white) │  │  height: 408px      │       │  (62px white) │     │
│               │  │  crowd_v3_loop.mp4  │       │               │ 1018│
│  satellite    │  └─────────────────────┘       │  10 gauges    │  px │
│  dish box     │  separator: 122px gap          │  (2×5 rows)   │     │
│               │  ┌──── map panel ──────┐       │               │     │
│  status icons │  │  top: 595px         │       │  XDL code     │     │
│  crosshair    │  │  height: 217px      │       │  data bars    │     │
│  3× data grid │  │  map_v3_loop.mp4    │       │  compass      │     │
│               │  └─────────────────────┘       │  (220px dia)  │     │
│               │  progress bar (bottom: 22px)   │               │  ↓  │
└───────────────┴────────────────────────────────┴───────────────┘     │
```

---

## CSS 变量（设计系统）

```css
:root {
  --c:  #00d4e0;               /* 主色：青蓝 */
  --cd: rgba(0,180,190,0.38);  /* 暗版：边框/次要元素 */
  --cb: #50f0f0;               /* 亮版：高亮角落/进度条 */
  --pb: rgba(0,12,16,0.95);    /* 面板背景 */
  --rv: #ff2200;               /* 红色：目标十字 */
  --gn: #00cc44;               /* 绿色：罗盘 */
}
```

---

## 关键元素位置参考

### 整体框架

| 元素 | CSS 定位 |
|------|---------|
| 外框 `#frame` | `inset: 12px; border: 1px solid var(--c)` |
| 顶部数据条 `#topbar` | `top:12px; height:38px; border-bottom:1px solid var(--cd)` |
| 左面板 `#lp` | `top:50px; left:12px; width:428px; bottom:12px` |
| 中心区 `#cs` | `top:50px; left:440px; right:440px; bottom:12px` |
| 右面板 `#rp` | `top:50px; right:12px; width:428px; bottom:12px` |

### 中心视频面板（相对于 `#cs`）

| 元素 | top | height | 视频源 |
|------|-----|--------|-------|
| 人群画面 `#vp` | 65px | 408px | `crowd_v3_loop.mp4` |
| 分隔区 `#sep` | 473px | 122px | — |
| 卫星地图 `#mp` | 595px | 217px | `map_v3_loop.mp4` |
| 进度条 `#bpbar` | bottom: 22px | 6px | — |

### 视频裁剪参数（ffmpeg）

```bash
# 人群画面：从原视频 t=14.5s 取 2.9s
ffmpeg -ss 14.5 -i input.mp4 -vf "crop=1022:406:448:117" -t 2.9 crowd_v3.mp4

# 循环到 22s
ffmpeg -stream_loop 8 -i crowd_v3.mp4 -t 22 -c copy crowd_v3_loop.mp4

# 卫星地图：从原视频 t=14.5s 取 2.9s
ffmpeg -ss 14.5 -i input.mp4 -vf "crop=1022:215:448:645" -t 2.9 map_v3.mp4

# 循环到 22s
ffmpeg -stream_loop 8 -i map_v3.mp4 -t 22 -c copy map_v3_loop.mp4
```

---

## 左面板元素清单

```
UI-GPRS          font-size:82px; font-weight:900; color:#fff
EARTH GPRS/01256 font-size:17px; color:var(--c)
天气图标+时钟     font-size:18px; margin-top:10px

卫星链接盒 #satbox:
  - 青色标题条: background:var(--c); color:#000; letter-spacing:3px
  - 迷你雷达圆: 56px 圆形 + 旋转扫描线 (GSAP: rotation:2880, 22s)
  - 大数字 "83": font-size:54px; color:var(--c); blink-slow
  - 卫星天线 SVG: 碟形 + 支撑臂 + 信号弧
  - 3行数据条: UPLINK FREQ / SIG STRENGTH / DATA RATE

状态图标行:
  [!](red,blink-fast)  [✕](red)  [▲](yellow,blink-slow)  [●](fill)

十字像素图标: 6×6 grid, 中间十字 = on，其余 = transparent
迷你方块: 38×38px, border:2px solid var(--c)

数据网格（3行，每行6格）:
  每格: border:1px solid var(--cd); font-size:9px; color:var(--c)
  内容示例: ZX1/JX2/TO2/LdE/VX1/HG8 (带 6px 副标签)
```

---

## 右面板元素清单

```
-IH // HI-       font-size:62px; font-weight:900; color:#fff; text-align:right
XX 1256//CGSTW 012  font-size:14px; color:var(--c)

仪表群（2行×5个 = 10个）:
  每个: width:50px; height:50px; border-radius:50%; border:1px solid var(--c)
  内圈: inset:6px; border:1px solid var(--cd)
  指针: width:1px; height:14px; transform-origin:bottom center

数据网格（1行6格）: 同左面板样式

综合信息盒 #rp-infobox: height:90px; 左半+右半(世界地图SVG)
  左半: "XX63152 1.172" (14px cyan bold) + 3条进度条
  右半: 简单世界地图 SVG + 发光定位点

XDL.XXJZ.C20203  font-size:26px; font-weight:900; color:var(--cb)
                 border-top:1px solid var(--cd); text-align:right

数据条盒 #rp-databox: border:1px solid var(--cd)
  SPEED / LOCK / SIGNAL 各一行 (label + bar)

计时器:
  "CALCULATING SPEED ON..."  font-size:8px; color:var(--cd)
  "00:00:00.000"             font-size:22px; color:var(--cb)
  (由 tl.eventCallback('onUpdate') 驱动)

罗盘 #compass: 220×220px; position:absolute; bottom:8px; right:8px
  外圈: stroke:#00cc44; width:1.5px
  刻度: N/E/S/W 主刻度 + 次刻度 + 点缀
  活跃弧: 第一象限高亮 stroke-width:3
  指针: 2px×42px; transform-origin:top center; GSAP rotation:1080 in 22s
  发光点: 12px; background:#00cc44; box-shadow:0 0 10px #00cc44
```

---

## GSAP 时间线模板

```js
const tl = gsap.timeline({ paused: true });
const SCAN_START = 5.5;

/* 片头 (0-2.7s) */
tl.to('#intro-text', { opacity:1, duration:0.7 }, 0.4);
tl.to('#intro-sub',  { opacity:1, duration:0.5 }, 0.9);
tl.to('#intro-text', { opacity:0, duration:0.4 }, 1.7);
tl.to('#intro-sub',  { opacity:0, duration:0.4 }, 1.8);
tl.to('#intro',      { opacity:0, duration:0.5 }, 2.1);
tl.set('#intro', { visibility:'hidden' }, 2.7);

/* HUD 入场 (2.1-5.0s) */
tl.to('#hud', { opacity:1, duration:0.7 }, 2.1);
tl.from('#frame',  { scaleX:0, transformOrigin:'left center', duration:0.35 }, 2.3);
tl.from('#topbar', { opacity:0, duration:0.3 }, 2.55);
// 左面板 stagger: 2.8s 起
// 右面板 stagger: 2.85s 起
// 中心面板: 4.5s / 5.2s / 5.65s

/* 持续动画 (全程 22s) */
tl.to('#c-needle',       { rotation:1080, duration:22, ease:'none' }, 0); // 罗盘
tl.to('#sat-radar-line', { rotation:2880, duration:22, ease:'none' }, 0); // 雷达扫描

/* 扫描线 (SCAN_START 起，每 3s 一次，7次) */
for (var i = 0; i < 7; i++) {
  tl.fromTo('#scanline', { y:0 }, { y:408, duration:3.0, ease:'none' },
    SCAN_START + i * 3.0);
}

/* 进度条 */
tl.to('#bpfill', { width:'100%', duration:15, ease:'none' }, SCAN_START);
tl.to('#bpdot',  { left:'100%', duration:15, ease:'none' }, SCAN_START);

/* 地图十字漂移 */
tl.to('#mapxhair', { x:40,  duration:9, ease:'power1.inOut', yoyo:true, repeat:2 }, SCAN_START);
tl.to('#mapxhair', { y:-20, duration:7, ease:'power1.inOut', yoyo:true, repeat:2 }, SCAN_START+1);

/* 计时器文字更新 */
tl.eventCallback('onUpdate', function() {
  var t = tl.time();
  if (t < SCAN_START) return;
  var e = t - SCAN_START;
  var mm = String(Math.floor(e / 60)).padStart(2,'0');
  var ss = String(Math.floor(e % 60)).padStart(2,'0');
  var ms = String(Math.floor((e % 1) * 1000)).padStart(3,'0');
  document.getElementById('rtimer-val').textContent = '00:'+mm+':'+ss+'.'+ms;
  document.getElementById('lp-clock').textContent   = '00:'+mm+':'+ss+' P60';
});

window.__timelines = window.__timelines || {};
window.__timelines['hud-gprs-v3'] = tl;
```

---

## 视频面板必须属性

```html
<!-- 每个 video 元素必须有以下属性，否则 HyperFrames lint 报错 -->
<video id="crowd-video"
       class="panel-video"
       src="../crowd_v3_loop.mp4"
       muted
       playsinline
       data-start="0"
       data-duration="22">
</video>
```

---

## 常用装饰 SVG 片段

### 面板角标

```html
<div class="pcorner tl"></div>
<div class="pcorner tr"></div>
<div class="pcorner bl"></div>
<div class="pcorner br"></div>
```

```css
.pcorner { position:absolute; width:24px; height:24px; z-index:10; }
.pcorner.tl { top:-2px;left:-2px; border-top:3px solid var(--cb); border-left:3px solid var(--cb); }
.pcorner.tr { top:-2px;right:-2px; border-top:3px solid var(--cb); border-right:3px solid var(--cb); }
.pcorner.bl { bottom:-2px;left:-2px; border-bottom:3px solid var(--cb); border-left:3px solid var(--cb); }
.pcorner.br { bottom:-2px;right:-2px; border-bottom:3px solid var(--cb); border-right:3px solid var(--cb); }
```

### 红色目标十字

```html
<svg width="80" height="80" viewBox="-40 -40 80 80">
  <g stroke="#ff2200" stroke-width="2" fill="none">
    <line x1="-34" y1="-34" x2="-19" y2="-34"/><line x1="-34" y1="-34" x2="-34" y2="-19"/>
    <line x1="34"  y1="-34" x2="19"  y2="-34"/><line x1="34"  y1="-34" x2="34"  y2="-19"/>
    <line x1="-34" y1="34"  x2="-19" y2="34"/><line x1="-34" y1="34"  x2="-34" y2="19"/>
    <line x1="34"  y1="34"  x2="19"  y2="34"/><line x1="34"  y1="34"  x2="34"  y2="19"/>
  </g>
  <g stroke="#ff2200" stroke-width="1.5">
    <line x1="-28" y1="0" x2="-9" y2="0"/><line x1="9" y1="0" x2="28" y2="0"/>
    <line x1="0" y1="-28" x2="0" y2="-9"/><line x1="0" y1="9"  x2="0" y2="28"/>
  </g>
  <rect x="-8" y="-8" width="16" height="16" fill="none" stroke="#ff2200" stroke-width="1.5"/>
  <circle cx="0" cy="0" r="2.5" fill="#ff2200"/>
</svg>
```

### 卫星天线 SVG（缩小版）

```html
<svg width="200" height="130" viewBox="0 0 200 130">
  <ellipse cx="100" cy="78" rx="62" ry="34" fill="none" stroke="rgba(255,255,255,0.65)" stroke-width="1.5"/>
  <ellipse cx="100" cy="78" rx="50" ry="27" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.3)" stroke-width="0.8"/>
  <line x1="100" y1="78" x2="130" y2="46" stroke="rgba(255,255,255,0.7)" stroke-width="1.5"/>
  <circle cx="130" cy="46" r="4.5" fill="none" stroke="rgba(255,255,255,0.8)" stroke-width="1.5"/>
  <circle cx="130" cy="46" r="2"   fill="rgba(0,212,224,0.9)"/>
  <line x1="100" y1="112" x2="100" y2="126" stroke="rgba(255,255,255,0.55)" stroke-width="2"/>
  <line x1="82"  y1="126" x2="118" y2="126" stroke="rgba(255,255,255,0.55)" stroke-width="2"/>
  <path d="M138,34 A22,22 0 0,1 138,58" fill="none" stroke="rgba(0,212,224,0.5)" stroke-width="1.2" stroke-dasharray="3 3"/>
</svg>
```

---

## 检查清单

渲染前必须通过：

```bash
npm run check   # 0 errors
```

常见 lint 错误：
- `media_missing_id` → video 元素缺少 `id`
- `media_missing_data_start` → video 元素缺少 `data-start` / `data-duration`
- `timeline_not_registered` → 缺少 `window.__timelines['hud-gprs-v3'] = tl`

---

## 渲染命令

```bash
npx hyperframes@0.6.20 render . \
  -c compositions/hud-gprs-v3.html \
  -o renders/hud-gprs-v3.mp4
```

输出：1920×1080, 30fps, ~32s, ~8-10MB MP4
