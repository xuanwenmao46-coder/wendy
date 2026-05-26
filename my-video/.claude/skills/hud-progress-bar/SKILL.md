---
name: hud-progress-bar
description: 创建半圆弧 HUD 进度条 Hyperframes 组合。包含入场、弧线填充+计数器主体、淡出出场三段动画，总时长可自定义（≥6s）。适用于数据可视化、加载动画、科技感 HUD 场景。
---

# HUD 半圆弧进度条 Skill

在 `compositions/` 下生成一个独立的 Hyperframes HTML 组合文件，实现 U 形弧线从左到右填充、中心百分比实时计数的 HUD 动画。

## 动画结构

| 阶段 | 默认时长 | 内容 |
|------|----------|------|
| 入场 | ~1.2s | 弧轨道淡入 → 上方标签飘入 → 百分比 + 下方标签显现 → 进度弧淡入 |
| 主体 | 总时长 − 2.7s | `stroke-dashoffset` 从满→0，同步 GSAP proxy 计数 0→100% |
| 出场 | ~1.5s | 全部元素 `power2.in` 淡出 |

## 关键几何参数

```
圆心:     (cx, cy) = (960, 620)   — 1920×1080 画布中偏下
半径:     r = 280
左端点:   (cx − r, cy) = (680, 620)
右端点:   (cx + r, cy) = (1240, 620)
SVG path: M {cx-r},{cy} A {r},{r} 0 0 1 {cx+r},{cy}
           sweep-flag=1 → 顺时针 → U 形底部半圆
半周长:   π × r ≈ 879.65  (即 stroke-dasharray 的值)
```

半径改变时重新计算：`dasharray = Math.PI * r`

## HTML 模板

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <script src="../node_modules/gsap/dist/gsap.min.js"></script>
    <style>
      * { margin: 0; padding: 0; box-sizing: border-box; }
      html, body {
        width: 1920px; height: 1080px; overflow: hidden;
        background: radial-gradient(ellipse 120% 100% at 50% 30%,
          #6e8fa8 0%, #3d5a70 40%, #1c2e3d 100%);
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
      }
      .hud-text {
        position: absolute; left: 50%; transform: translateX(-50%);
        color: white; font-weight: 300; letter-spacing: 0.35em;
        text-transform: uppercase; white-space: nowrap; text-align: center;
      }
    </style>
  </head>
  <body>
    <div
      id="root"
      data-composition-id="hud-progress-bar"
      data-start="0"
      data-duration="8"
      data-width="1920"
      data-height="1080"
    >
      <svg style="position:absolute;inset:0;width:1920px;height:1080px;overflow:visible;"
           viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg">

        <!-- 轨道：半透明底弧 -->
        <path id="arc-track"
          d="M 680,620 A 280,280 0 0 1 1240,620"
          fill="none" stroke="rgba(255,255,255,0.22)"
          stroke-width="2.5" stroke-linecap="round" style="opacity:0"/>

        <!-- 进度弧：填充动画主角 -->
        <path id="arc-progress"
          d="M 680,620 A 280,280 0 0 1 1240,620"
          fill="none" stroke="white"
          stroke-width="4.5" stroke-linecap="round"
          stroke-dasharray="879.65" stroke-dashoffset="879.65"
          style="opacity:0"/>
      </svg>

      <!-- 上方标签（弧顶区域，top ≈ cy − r − margin） -->
      <div id="label-top" class="clip hud-text"
        style="top:228px; font-size:26px; opacity:0;"
        data-start="0" data-duration="8" data-track-index="1">
        LORE
      </div>

      <!-- 百分比计数器（弧内居中） -->
      <div id="pct-display" class="clip"
        style="position:absolute; top:390px; left:50%; transform:translateX(-50%);
               text-align:center; color:white;
               font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;
               font-weight:200; white-space:nowrap; opacity:0;"
        data-start="0" data-duration="8" data-track-index="2">
        <span id="pct-num"
          style="font-size:144px; line-height:1; letter-spacing:-4px;">0</span><span
          style="font-size:68px; vertical-align:top; padding-top:18px;
                 display:inline-block;">%</span>
      </div>

      <!-- 下方标签（弧端点附近，top ≈ cy − 46） -->
      <div id="label-bottom" class="clip hud-text"
        style="top:574px; font-size:22px; opacity:0;"
        data-start="0" data-duration="8" data-track-index="3">
        PROFIT
      </div>
    </div>

    <script>
      window.__timelines = window.__timelines || {};
      const tl = gsap.timeline({ paused: true });
      const TOTAL = 8;          // 与 data-duration 保持一致
      const INTRO  = 1.2;
      const OUTRO  = 1.5;
      const FILL   = TOTAL - INTRO - OUTRO;   // 5.3s

      // ── 入场 ──────────────────────────────────────────────────────────
      tl.fromTo("#arc-track",    { opacity:0 }, { opacity:1, duration:0.9, ease:"power2.out" }, 0.1);
      tl.fromTo("#label-top",    { opacity:0, y:-14 }, { opacity:1, y:0, duration:0.8, ease:"power2.out" }, 0.2);
      tl.fromTo("#pct-display",  { opacity:0 }, { opacity:1, duration:0.6, ease:"power2.out" }, 0.45);
      tl.fromTo("#label-bottom", { opacity:0 }, { opacity:1, duration:0.6, ease:"power2.out" }, 0.55);
      tl.fromTo("#arc-progress", { opacity:0 }, { opacity:1, duration:0.35, ease:"none" }, 0.9);

      // ── 主体：弧填充 + 计数器 ─────────────────────────────────────────
      tl.fromTo("#arc-progress",
        { strokeDashoffset: 879.65 },
        { strokeDashoffset: 0, duration: FILL, ease: "power1.inOut" },
        INTRO
      );
      const proxy = { pct: 0 };
      tl.fromTo(proxy, { pct: 0 }, {
        pct: 100, duration: FILL, ease: "power1.inOut",
        onUpdate() {
          const el = document.getElementById("pct-num");
          if (el) el.textContent = Math.round(proxy.pct);
        }
      }, INTRO);

      // ── 出场：直接淡出 ────────────────────────────────────────────────
      tl.to(
        "#arc-track, #arc-progress, #label-top, #pct-display, #label-bottom",
        { opacity:0, duration:1.2, ease:"power2.in" },
        INTRO + FILL
      );

      window.__timelines["hud-progress-bar"] = tl;
    </script>
  </body>
</html>
```

## 自定义要点

### 修改文字标签
- `#label-top`（弧顶）：改 `LORE` 为任意文字
- `#label-bottom`（弧端）：改 `PROFIT` 为任意文字

### 修改总时长
1. 改 `data-duration="8"` 为目标秒数（≥6）
2. 同步修改脚本中 `const TOTAL = 8`
3. `FILL` 自动重算：`TOTAL − INTRO(1.2) − OUTRO(1.5)`

### 修改弧半径
设新半径为 `R`：
```
新 path: M {960-R},{620} A {R},{R} 0 0 1 {960+R},{620}
新 dasharray = Math.PI * R
```
同时更新 `stroke-dasharray` 属性和 JS 中的 `strokeDashoffset` 起止值。

### 修改颜色
- 弧轨道：`stroke="rgba(255,255,255,0.22)"`
- 进度弧：`stroke="white"`
- 文字：CSS `color:white`
- 背景：`body { background: ... }`

### 修改字号
- 数字：`font-size:144px`
- `%` 符号：`font-size:68px`
- 上标签：`font-size:26px`
- 下标签：`font-size:22px`

## Hyperframes 必须遵守的规则

1. 每个 `class="clip"` 元素必须有 `data-start`、`data-duration`、`data-track-index`
2. 同一 `data-track-index` 的 clip 不得时间重叠（本 skill 用了 track 1/2/3）
3. SVG 元素无需 `class="clip"`，直接用 GSAP 控制 opacity
4. timeline 必须 `paused:true` 并注册到 `window.__timelines["composition-id"]`
5. 禁止 `Date.now()`、`Math.random()`、网络请求
6. 改动后必须运行 `npm run check`，0 errors 才算完成

## 验证步骤

```bash
npm run check
# 预期：0 error(s)
# 可忽略：index.html 的 timeline_track_too_dense 警告（已有问题，非本 skill 引入）
```
