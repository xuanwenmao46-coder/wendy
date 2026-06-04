# Editorial Motion Documentary — Complete Generation Skill

---

```yaml
name: editorial-motion-documentary
description: >
  Complete pipeline for generating a premium editorial investigative video from a user's topic
  description. VOX × Bloomberg × NYT × Pentagram visual language. When a user describes any
  topic they want turned into a documentary short, invoke this skill to collect their brief,
  then execute all steps to produce a final MP4 with audio. Trigger phrases: "帮我做一个关于X的视频",
  "做一个调查类视频", "editorial motion video", "editorial documentary", "investigative short".
  Do NOT use for brand ads, product demos, or TTS explainer podcasts.
category: Editorial Video Design
version: 2.0.0
effort: high
```

---

## Step 0 — User Intake (Always Run First)

When the user describes a topic, collect these answers before writing any code.
Ask ALL in one message, clearly formatted. User may skip optional items.

```
EDITORIAL VIDEO BRIEF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

① 主题 / Topic
   你的视频要调查什么？用一句话描述。
   e.g. "手机每天偷走了多少时间" / "外卖平台如何控制餐厅" / "年轻人为何不买房"

② 核心关键词 / Central Keyword
   这个调查的核心概念词（将贯穿全片）
   e.g. ATTENTION · CONTROL · PRICE · SILENCE · DEBT

③ 目标观众 / Target Audience
   谁在看这个视频？
   e.g. 25–40岁城市白领 / 在校大学生 / 投资者

④ 关键数据 / Key Facts (可选, optional)
   你已有哪些具体数字或事实？每行一条。
   e.g. 平均每天看手机4.2小时 / 中国外卖市场规模9000亿

⑤ 结尾基调 / Ending Tone
   你希望观众离开时的感受：
   a) 愤怒并想行动
   b) 沉默与自我反思
   c) 信息已获取，去做自己的判断

⑥ 视频时长 / Duration (可选, default=72s)
   建议范围: 60–90s

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Once all answers are received, proceed directly to Step 1. Do not wait for further approval.

---

## Step 1 — Narrative Architecture (Generate Before Any Code)

Using the user's brief, generate the following document **in full** before writing HTML:

### 1A. Investigative Arc

Fill this template:

```
TOPIC:          [from brief]
CENTRAL KEYWORD:[from brief — ALL CAPS, one word]
ONE QUESTION:   [the question the film raises, never answers directly]
ONE TRUTH:      [what is revealed in CH06 — one number or fact]
AUDIENCE FEELING AT END: [from brief option a/b/c]

EMOTIONAL CURVE:
  0–8s   CURIOSITY   — [specific suspicion raised for this topic]
  8–18s  INVESTIGATION — [what evidence is assembled]
  18–28s DISCOVERY   — [which human story / person type]
  28–38s SUSPICION   — [what data is found inside a document]
  38–50s CONFIRMATION — [what converges, what becomes undeniable]
  50–60s SHOCK       — [the single number / the cost]
  60–67s COMPRESSION  — [what is stripped away, what remains]
  67–72s REFLECTION  — [the single question left in silence]
```

### 1B. Chapter Blueprint (8 chapters)

For each chapter generate:

```
CH01 · THE INVESTIGATION (0–8s)
  Primary content:   [7 flash keywords from the topic, e.g. SCREEN · TIME · HABIT · COST]
  Title line 1-3:    [3-line title matching the topic]
  Series label:      [e.g. "A SCREEN TIME INVESTIGATION"]
  Dark bg: yes

CH02 · EVIDENCE BOARD (8–18s)
  6 document cards:
    Card 1: [document type + title + one stat]
    Card 2: [document type + title + one stat]
    Card 3: [document type + title + one stat]
    Card 4: [document type + title + one stat]
    Card 5: [document type + title + one stat]
    Card 6: [document type + title + one stat]
  Thread intersection keyword: [CENTRAL KEYWORD]
  Stamp labels: [3 × small stamps e.g. "VERIFIED" "SOURCE: 2024" "CROSS-REF"]

CH03 · ONE PERSON (18–28s)
  Portrait label:    [e.g. "SUBJECT: CHEN WEI, 31"]
  Log title:         "THE DAILY LOG — [TOPIC CODE]"
  Log rows (5):      [time / activity / duration, e.g. "07:12 / OPENS PHONE / 00:08:47"]
  Highlighted row:   [row 3 or 4 — the revealing one]
  Pull quote:        [a real or plausible quote about the topic, 12 words max]

CH04 · THE DISCOVERY (28–38s)
  Report institution: [e.g. "DIGITAL WELLNESS INSTITUTE · STANFORD"]
  3 FINDING blocks:
    FINDING 01: [FIG code] / [value] / [quote] / [source]
    FINDING 02: [FIG code] / [value] / [quote] / [source]
    FINDING 03: [FIG code] / [value] / [quote] / [source]
  Stamp: CONFIRMED

CH05 · ESCALATION (38–50s)
  5 media zones (tile layout):
    Zone 1: [headline type] — [content]
    Zone 2: [ad copy type] — [content]
    Zone 3: [academic type] — [content]
    Zone 4: [news ticker type] — [content]
    Zone 5: [chart-in-document type] — [content]
  CENTRAL KEYWORD pulse: 8× appearances across zones

CH06 · THE COST (50–60s)
  The single number: [e.g. "9 YEARS"] — [what it represents]
  Unit label:        [e.g. "OF YOUR LIFE / SPENT ON A SCREEN"]
  Supporting text:   [one sentence below the number]
  SFX: single_thump — ONE hit only

CH07 · COLLAPSE (60–67s)
  CENTRAL KEYWORD flood: 62 instances in 3 waves
  Wave sizes: 12 → 20 → 30
  At t=66.0: all → #c00
  At t=67.0: all disappear

CH08 · ENDING (67–72s)
  Line 1 (t=68.7): [e.g. "Your [noun]"]
  Line 2 (t=69.8): [e.g. "is your life."]
  Line 3 (t=71.0): [e.g. "What will you spend it on?"] — gray
  Audio: piano_note D4 (timed to black screen onset)
```

---

## Step 2 — Project Setup

```bash
# Create or use existing project directory
mkdir -p my-video && cd my-video

# Init if no package.json yet
npx hyperframes init

# Verify structure
ls index.html package.json
```

---

## Step 3 — Write index.html

Use this **complete structural template**. Fill ALL `[PLACEHOLDER]` values from Step 1B.

### 3A. Full HTML Template

```html
<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=1920, height=1080"/>
<title>[TOPIC TITLE]</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<style>
/* ── Reset ───────────────────────────────────────────────────── */
*{margin:0;padding:0;box-sizing:border-box}
body{
  width:1920px;height:1080px;overflow:hidden;
  background:#fff;
  font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.75' numOctaves='4' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='300' height='300' filter='url(%23n)' opacity='0.025'/%3E%3C/svg%3E");
}

/* ── Clip visibility ─────────────────────────────────────────── */
.clip{opacity:0;position:absolute}
.scene{width:1920px;height:1080px;top:0;left:0}

/* ── Persistent layer ────────────────────────────────────────── */
#persist{
  position:absolute;top:0;left:0;
  width:1920px;height:1080px;
  z-index:100;pointer-events:none
}
.top-rule{position:absolute;top:0;left:0;width:1920px;height:2px;background:#000}
.bottom-rule{position:absolute;top:1070px;left:0;width:1920px;height:1px;background:#000}
.left-margin{position:absolute;top:0;left:60px;width:1px;height:1080px;background:#000}
.right-margin{position:absolute;top:0;left:1860px;width:1px;height:1080px;background:#000}
.masthead{
  position:absolute;top:10px;left:80px;
  font-size:10px;font-weight:400;letter-spacing:0.2em;color:#000;
  text-transform:uppercase
}
.ch-label{
  position:absolute;top:1052px;left:80px;
  font-size:11px;font-weight:400;letter-spacing:0.15em;color:#555
}
.archive-code{
  position:absolute;top:1052px;left:1720px;
  font-size:11px;color:#888;font-family:'Courier New',monospace
}

/* ── Shared document styles ──────────────────────────────────── */
.doc-card{
  background:#fff;border:1px solid #000;
  padding:16px 20px;position:absolute
}
.doc-label{font-size:9px;letter-spacing:0.2em;color:#888;text-transform:uppercase;margin-bottom:8px;font-family:'Courier New',monospace}
.doc-title{font-size:13px;font-weight:800;color:#000;margin-bottom:6px;line-height:1.3}
.doc-stat{font-size:28px;font-weight:800;color:#000;margin:8px 0}
.doc-source{font-size:9px;color:#888;letter-spacing:0.1em;border-top:1px solid #ddd;padding-top:6px;margin-top:8px}

/* ── Red accent ──────────────────────────────────────────────── */
.red{color:#c00}
.red-border{border-color:#c00}
.annotation-svg{position:absolute;pointer-events:none}
.annotation-svg path,.annotation-svg circle,.annotation-svg line{
  fill:none;stroke:#c00;stroke-width:2
}

/* ── CH01 dark ───────────────────────────────────────────────── */
#ch01{background:#0a0a0a}
.flash-word{
  position:absolute;font-size:96px;font-weight:800;
  color:#fff;text-align:center;
  left:50%;top:50%;transform:translate(-50%,-50%)
}
.ch01-title{
  position:absolute;left:50%;top:50%;
  transform:translate(-50%,-50%);text-align:center
}
.ch01-title .t1{font-size:120px;font-weight:800;color:#fff;display:block;letter-spacing:-0.01em}
.ch01-title .t2{font-size:120px;font-weight:800;color:#fff;display:block;letter-spacing:-0.01em}
.ch01-title .t3{font-size:120px;font-weight:800;color:#fff;display:block;letter-spacing:-0.01em}
.ch01-title .series{font-size:13px;color:#c00;letter-spacing:0.25em;margin-top:16px;display:block}

/* ── CH02 evidence cards ─────────────────────────────────────── */
.ev-card{width:260px;background:#fff;border:1px solid #000;padding:14px 16px;position:absolute}
.ev-card .ev-label{font-size:8px;letter-spacing:0.2em;color:#888;text-transform:uppercase;margin-bottom:6px;font-family:'Courier New',monospace}
.ev-card .ev-title{font-size:12px;font-weight:800;line-height:1.35;color:#000;margin-bottom:8px}
.ev-card .ev-num{font-size:32px;font-weight:800;color:#000}
.ev-card .ev-src{font-size:8px;color:#aaa;border-top:1px solid #eee;padding-top:5px;margin-top:8px}

/* ── CH03 log ────────────────────────────────────────────────── */
.log-row{
  display:flex;align-items:center;
  padding:12px 0;border-bottom:1px solid #eee;
  position:relative
}
.log-time{font-size:13px;font-family:'Courier New',monospace;color:#555;width:70px}
.log-act{font-size:14px;font-weight:700;color:#000;flex:1}
.log-dur{font-size:13px;font-family:'Courier New',monospace;color:#c00;width:90px;text-align:right}

/* ── CH04 findings ───────────────────────────────────────────── */
.finding-block{
  width:800px;background:#fff;border-left:4px solid #000;
  padding:20px 28px;position:absolute
}
.finding-block .fig{font-size:9px;color:#888;letter-spacing:0.2em;font-family:'Courier New',monospace;margin-bottom:6px}
.finding-block .fval{font-size:48px;font-weight:800;color:#000;margin-bottom:6px}
.finding-block .fquote{font-size:13px;color:#333;font-style:italic;line-height:1.5;margin-bottom:8px}
.finding-block .fsrc{font-size:10px;color:#999}

/* ── CH05 zones ──────────────────────────────────────────────── */
.media-zone{position:absolute;background:#fff;border:1px solid #000;overflow:hidden}
.zone-type{font-size:8px;letter-spacing:0.2em;color:#888;text-transform:uppercase;padding:8px 10px 4px;font-family:'Courier New',monospace}
.zone-content{padding:8px 10px 10px;font-size:12px;font-weight:800;line-height:1.4;color:#000}

/* ── CH06 the number ─────────────────────────────────────────── */
#ch06{background:#fff}
.the-number{
  position:absolute;left:50%;top:50%;
  transform:translate(-50%,-60%);text-align:center
}
.the-number .num{font-size:280px;font-weight:800;color:#000;line-height:0.9;letter-spacing:-0.03em}
.the-number .unit{font-size:32px;font-weight:400;color:#555;letter-spacing:0.2em;margin-top:20px;text-transform:uppercase}
.the-number .sub{font-size:14px;color:#888;margin-top:16px;letter-spacing:0.1em}

/* ── CH07 flood ──────────────────────────────────────────────── */
#ch07{background:#fff}
.flood-word{position:absolute;font-weight:800;color:#000;text-transform:uppercase;letter-spacing:0.05em}

/* ── CH08 ending ─────────────────────────────────────────────── */
#ch08{background:#000}
.end-line{
  position:absolute;left:50%;
  transform:translateX(-50%);
  font-size:52px;font-weight:800;color:#fff;
  text-align:center;letter-spacing:-0.01em
}
.end-sub{
  position:absolute;left:50%;transform:translateX(-50%);
  font-size:28px;font-weight:400;color:#888;
  text-align:center;letter-spacing:0.05em
}
</style>
</head>
<body>

<div id="root" data-composition-id="root" data-start="0" data-duration="72"
     data-width="1920" data-height="1080">

  <!-- ══ PERSISTENT ═══════════════════════════════════════════════ -->
  <div id="persist">
    <div class="top-rule"></div>
    <div class="bottom-rule"></div>
    <div class="left-margin"></div>
    <div class="right-margin"></div>
    <div class="masthead">THE [TOPIC] — AN EDITORIAL INVESTIGATION</div>
    <div class="ch-label" id="ch-label-persist">CH.01 / THE INVESTIGATION</div>
    <div class="archive-code">REF-2024-001</div>
  </div>

  <!-- ══ CH01: THE INVESTIGATION (0–8s) ════════════════════════════ -->
  <div id="ch01" class="scene clip" data-start="0" data-duration="8" data-track-index="10">

    <!-- Background newspaper fragments -->
    <div class="clip" data-start="0" data-duration="8" data-track-index="11"
         style="position:absolute;top:120px;left:80px;width:400px;opacity:0.15;
                font-size:11px;color:#fff;line-height:1.8;font-style:italic;
                transform:rotate(-2deg)">
      [TOPIC EXCERPT LINE 1]<br>[TOPIC EXCERPT LINE 2]<br>[TOPIC EXCERPT LINE 3]
    </div>
    <div class="clip" data-start="0" data-duration="8" data-track-index="12"
         style="position:absolute;top:600px;right:120px;width:360px;opacity:0.10;
                font-size:10px;color:#fff;line-height:1.9;transform:rotate(1.5deg)">
      [TOPIC EXCERPT LINE 4]<br>[TOPIC EXCERPT LINE 5]
    </div>

    <!-- Flash words: 7 × 0.4s each, t=0.3–3.1s -->
    <div id="fw1" class="flash-word clip" data-start="0.3" data-duration="0.4" data-track-index="13">[FLASH1]</div>
    <div id="fw2" class="flash-word clip" data-start="0.7" data-duration="0.4" data-track-index="14">[FLASH2]</div>
    <div id="fw3" class="flash-word clip" data-start="1.1" data-duration="0.4" data-track-index="15">[FLASH3]</div>
    <div id="fw4" class="flash-word clip" data-start="1.5" data-duration="0.4" data-track-index="16">[FLASH4]</div>
    <div id="fw5" class="flash-word clip" data-start="1.9" data-duration="0.4" data-track-index="17">[FLASH5]</div>
    <div id="fw6" class="flash-word clip" data-start="2.3" data-duration="0.4" data-track-index="18">[FLASH6]</div>
    <div id="fw7" class="flash-word clip" data-start="2.7" data-duration="0.4" data-track-index="19">[FLASH7]</div>

    <!-- Main title (t=3.5–8s) -->
    <div id="ch01-title" class="ch01-title clip" data-start="3.5" data-duration="4.5" data-track-index="20">
      <span class="t1">[TITLE LINE 1]</span>
      <span class="t2">[TITLE LINE 2]</span>
      <span class="t3">[TITLE LINE 3]</span>
      <span class="series">[SERIES LABEL]</span>
    </div>

  </div><!-- /ch01 -->

  <!-- ══ CH02: EVIDENCE BOARD (8–18s) ══════════════════════════════ -->
  <div id="ch02" class="scene clip" data-start="8" data-duration="10" data-track-index="30">

    <!-- 6 evidence cards — positions set by GSAP chaos/settle -->
    <div id="ev1" class="ev-card clip" data-start="8" data-duration="10" data-track-index="31"
         style="top:140px;left:180px">
      <div class="ev-label">[CARD1-TYPE] · 2024</div>
      <div class="ev-title">[CARD1-TITLE]</div>
      <div class="ev-num">[CARD1-STAT]</div>
      <div class="ev-src">[CARD1-SOURCE]</div>
    </div>
    <div id="ev2" class="ev-card clip" data-start="8" data-duration="10" data-track-index="32"
         style="top:140px;left:520px">
      <div class="ev-label">[CARD2-TYPE] · 2024</div>
      <div class="ev-title">[CARD2-TITLE]</div>
      <div class="ev-num">[CARD2-STAT]</div>
      <div class="ev-src">[CARD2-SOURCE]</div>
    </div>
    <div id="ev3" class="ev-card clip" data-start="8" data-duration="10" data-track-index="33"
         style="top:140px;left:860px">
      <div class="ev-label">[CARD3-TYPE] · 2024</div>
      <div class="ev-title">[CARD3-TITLE]</div>
      <div class="ev-num">[CARD3-STAT]</div>
      <div class="ev-src">[CARD3-SOURCE]</div>
    </div>
    <div id="ev4" class="ev-card clip" data-start="8" data-duration="10" data-track-index="34"
         style="top:460px;left:180px">
      <div class="ev-label">[CARD4-TYPE] · 2024</div>
      <div class="ev-title">[CARD4-TITLE]</div>
      <div class="ev-num">[CARD4-STAT]</div>
      <div class="ev-src">[CARD4-SOURCE]</div>
    </div>
    <div id="ev5" class="ev-card clip" data-start="8" data-duration="10" data-track-index="35"
         style="top:460px;left:520px">
      <div class="ev-label">[CARD5-TYPE] · 2024</div>
      <div class="ev-title">[CARD5-TITLE]</div>
      <div class="ev-num">[CARD5-STAT]</div>
      <div class="ev-src">[CARD5-SOURCE]</div>
    </div>
    <div id="ev6" class="ev-card clip" data-start="8" data-duration="10" data-track-index="36"
         style="top:460px;left:860px">
      <div class="ev-label">[CARD6-TYPE] · 2024</div>
      <div class="ev-title">[CARD6-TITLE]</div>
      <div class="ev-num">[CARD6-STAT]</div>
      <div class="ev-src">[CARD6-SOURCE]</div>
    </div>

    <!-- Red thread SVG (draws on at t=10.5s) -->
    <svg id="ch02-threads" class="annotation-svg clip" data-start="10.5" data-duration="7.5" data-track-index="37"
         style="top:0;left:0" width="1920" height="1080">
      <path id="thread1" d="M 440 220 Q 680 180 860 220" stroke-dasharray="300" stroke-dashoffset="300"/>
      <path id="thread2" d="M 780 490 Q 920 400 860 490" stroke-dasharray="200" stroke-dashoffset="200"/>
      <circle id="thread-node" cx="970" cy="350" r="28" stroke-dasharray="180" stroke-dashoffset="180"/>
    </svg>

    <!-- Node keyword -->
    <div class="clip" data-start="11" data-duration="7" data-track-index="38"
         style="position:absolute;top:323px;left:940px;
                font-size:9px;font-weight:800;color:#c00;letter-spacing:0.15em;
                text-align:center;width:60px">[KEYWORD]</div>

    <!-- Stamp labels -->
    <div class="clip" data-start="11.5" data-duration="6.5" data-track-index="39"
         style="position:absolute;top:320px;left:360px;
                font-size:8px;letter-spacing:0.2em;color:#c00;text-transform:uppercase;
                transform:rotate(-8deg);border:1px solid #c00;padding:3px 6px">VERIFIED</div>
    <div class="clip" data-start="12" data-duration="6" data-track-index="40"
         style="position:absolute;top:500px;left:700px;
                font-size:8px;letter-spacing:0.2em;color:#555;
                transform:rotate(5deg);border:1px solid #999;padding:3px 6px">SOURCE: 2024</div>
    <div class="clip" data-start="12.5" data-duration="5.5" data-track-index="41"
         style="position:absolute;top:280px;left:800px;
                font-size:8px;letter-spacing:0.2em;color:#555;
                transform:rotate(-3deg);border:1px solid #999;padding:3px 6px">CROSS-REF</div>

  </div><!-- /ch02 -->

  <!-- ══ CH03: ONE PERSON (18–28s) ══════════════════════════════════ -->
  <div id="ch03" class="scene clip" data-start="18" data-duration="10" data-track-index="50">

    <!-- Left: halftone portrait -->
    <div class="clip" data-start="18" data-duration="10" data-track-index="51"
         style="position:absolute;top:80px;left:100px;width:680px">
      <div style="width:640px;height:640px;
                  background:repeating-linear-gradient(0deg,#000 0,#000 1px,transparent 1px,transparent 5px),
                  repeating-linear-gradient(90deg,#000 0,#000 1px,transparent 1px,transparent 5px);
                  background-color:#bbb;filter:contrast(1.4)"></div>
      <div style="margin-top:10px;font-size:10px;letter-spacing:0.2em;color:#555;font-family:'Courier New',monospace">
        SUBJECT: [SUBJECT-NAME] · [SUBJECT-AGE] · [SUBJECT-CITY]</div>
      <div style="margin-top:4px;font-size:9px;color:#aaa;letter-spacing:0.1em">
        [CAPTION LINE]</div>
    </div>

    <!-- Right: The Daily Log -->
    <div class="clip" data-start="18" data-duration="10" data-track-index="52"
         style="position:absolute;top:80px;left:820px;width:900px">
      <div style="font-size:10px;letter-spacing:0.25em;color:#c00;font-weight:800;
                  border-bottom:2px solid #c00;padding-bottom:10px;margin-bottom:20px;text-transform:uppercase">
        THE DAILY LOG — [LOG-CODE]</div>
      <div style="font-size:9px;letter-spacing:0.2em;color:#888;margin-bottom:16px;
                  font-family:'Courier New',monospace">
        PARTICIPANT TRACKING / 24-HOUR AUDIT · REF-003</div>

      <!-- Log rows — stagger t=19.2, 20.4, 21.6, 22.8, 24.0 -->
      <div id="log1" class="log-row clip" data-start="19.2" data-duration="8.8" data-track-index="53">
        <span class="log-time">[TIME1]</span>
        <span class="log-act">[ACT1]</span>
        <span class="log-dur">[DUR1]</span>
      </div>
      <div id="log2" class="log-row clip" data-start="20.4" data-duration="7.6" data-track-index="54">
        <span class="log-time">[TIME2]</span>
        <span class="log-act">[ACT2]</span>
        <span class="log-dur">[DUR2]</span>
      </div>
      <div id="log3" class="log-row clip" data-start="21.6" data-duration="6.4" data-track-index="55" style="background:#fff7f7">
        <span class="log-time">[TIME3]</span>
        <span class="log-act" style="color:#c00">[ACT3 — THE REVEALING ONE]</span>
        <span class="log-dur">[DUR3]</span>
      </div>
      <div id="log4" class="log-row clip" data-start="22.8" data-duration="5.2" data-track-index="56">
        <span class="log-time">[TIME4]</span>
        <span class="log-act">[ACT4]</span>
        <span class="log-dur">[DUR4]</span>
      </div>
      <div id="log5" class="log-row clip" data-start="24.0" data-duration="4" data-track-index="57">
        <span class="log-time">[TIME5]</span>
        <span class="log-act">[ACT5]</span>
        <span class="log-dur">[DUR5]</span>
      </div>

      <!-- Red highlight line (draws over log3) -->
      <svg id="log-highlight" class="annotation-svg clip" data-start="22" data-duration="6" data-track-index="58"
           style="top:0;left:-10px" width="900" height="400">
        <line id="hl-line" x1="0" y1="145" x2="890" y2="145"
              stroke="#c00" stroke-width="1.5" stroke-dasharray="900" stroke-dashoffset="900"/>
      </svg>

      <!-- Pull quote -->
      <div id="ch03-quote" class="clip" data-start="25" data-duration="3" data-track-index="59"
           style="margin-top:40px;font-size:20px;font-style:italic;color:#333;line-height:1.6;
                  border-left:3px solid #c00;padding-left:20px">
        "[PULL QUOTE]"
      </div>
    </div>

  </div><!-- /ch03 -->

  <!-- ══ CH04: THE DISCOVERY (28–38s) ══════════════════════════════ -->
  <div id="ch04" class="scene clip" data-start="28" data-duration="10" data-track-index="70">

    <!-- Report header -->
    <div class="clip" data-start="28" data-duration="10" data-track-index="71"
         style="position:absolute;top:60px;left:160px;width:1600px;
                border-bottom:2px solid #000;padding-bottom:12px;
                display:flex;justify-content:space-between;align-items:baseline">
      <span style="font-size:11px;font-weight:800;letter-spacing:0.2em;color:#000">[INSTITUTION]</span>
      <span style="font-size:11px;letter-spacing:0.2em;color:#888;font-family:'Courier New',monospace">DRAFT — NOT FOR DISTRIBUTION · PAGE 14</span>
    </div>
    <div class="clip" data-start="28" data-duration="10" data-track-index="72"
         style="position:absolute;top:90px;left:160px;
                font-size:28px;font-weight:800;color:#000;letter-spacing:-0.01em">
      [KEYWORD] RESEARCH QUARTERLY — Vol. 8, Issue 3
    </div>

    <!-- 3 Finding blocks — stagger t=29.5, 31.5, 33.5 -->
    <div id="f1" class="finding-block clip" data-start="29.5" data-duration="8.5" data-track-index="73"
         style="top:150px;left:160px">
      <div class="fig">[FIG1-CODE] · PRIMARY FINDING</div>
      <div class="fval">[FINDING1-VALUE]</div>
      <div class="fquote">"[FINDING1-QUOTE]"</div>
      <div class="fsrc">[FINDING1-SOURCE]</div>
    </div>
    <div id="f2" class="finding-block clip" data-start="31.5" data-duration="6.5" data-track-index="74"
         style="top:370px;left:160px">
      <div class="fig">[FIG2-CODE] · SECONDARY FINDING</div>
      <div class="fval">[FINDING2-VALUE]</div>
      <div class="fquote">"[FINDING2-QUOTE]"</div>
      <div class="fsrc">[FINDING2-SOURCE]</div>
    </div>
    <div id="f3" class="finding-block clip" data-start="33.5" data-duration="4.5" data-track-index="75"
         style="top:590px;left:160px">
      <div class="fig">[FIG3-CODE] · CRITICAL FINDING</div>
      <div class="fval">[FINDING3-VALUE]</div>
      <div class="fquote">"[FINDING3-QUOTE]"</div>
      <div class="fsrc">[FINDING3-SOURCE]</div>
    </div>

    <!-- Annotation circles -->
    <svg class="annotation-svg clip" data-start="30.5" data-duration="7.5" data-track-index="76"
         style="top:0;left:0" width="1920" height="1080">
      <circle id="ann1" cx="290" cy="190" r="52" stroke-dasharray="330" stroke-dashoffset="330"/>
    </svg>
    <svg class="annotation-svg clip" data-start="32.5" data-duration="5.5" data-track-index="77"
         style="top:0;left:0" width="1920" height="1080">
      <circle id="ann2" cx="290" cy="412" r="52" stroke-dasharray="330" stroke-dashoffset="330"/>
    </svg>

    <!-- CONFIRMED stamp -->
    <div id="confirmed-stamp" class="clip" data-start="35" data-duration="3" data-track-index="78"
         style="position:absolute;top:620px;left:1000px;
                font-size:36px;font-weight:800;color:#c00;
                border:3px solid #c00;padding:8px 20px;
                letter-spacing:0.2em;transform:rotate(-5deg)">CONFIRMED</div>

  </div><!-- /ch04 -->

  <!-- ══ CH05: ESCALATION (38–50s) ══════════════════════════════════ -->
  <div id="ch05" class="scene clip" data-start="38" data-duration="12" data-track-index="80">

    <!-- Chapter header -->
    <div class="clip" data-start="38" data-duration="12" data-track-index="81"
         style="position:absolute;top:40px;left:100px;
                font-size:18px;font-weight:800;letter-spacing:0.15em;color:#000;
                text-transform:uppercase">
      THE [KEYWORD] COMPLEX — FIVE DOMAINS OF IMPACT</div>

    <!-- Zone 1 (top-left) -->
    <div id="z1" class="media-zone clip" data-start="39" data-duration="11" data-track-index="82"
         style="top:90px;left:100px;width:360px;height:200px">
      <div class="zone-type">[ZONE1-TYPE]</div>
      <div class="zone-content">[ZONE1-HEADLINE]<br>
        <span style="font-size:9px;color:#888;font-weight:400">[ZONE1-SUBTEXT]</span>
      </div>
    </div>

    <!-- Zone 2 (top-center) -->
    <div id="z2" class="media-zone clip" data-start="39.6" data-duration="10.4" data-track-index="83"
         style="top:90px;left:480px;width:400px;height:200px">
      <div class="zone-type">[ZONE2-TYPE]</div>
      <div class="zone-content">[ZONE2-HEADLINE]<br>
        <span style="font-size:9px;color:#888;font-weight:400">[ZONE2-SUBTEXT]</span>
      </div>
    </div>

    <!-- Zone 3 (top-right) -->
    <div id="z3" class="media-zone clip" data-start="40.2" data-duration="9.8" data-track-index="84"
         style="top:90px;left:900px;width:380px;height:200px">
      <div class="zone-type">[ZONE3-TYPE]</div>
      <div class="zone-content">[ZONE3-HEADLINE]<br>
        <span style="font-size:9px;color:#888;font-weight:400">[ZONE3-SUBTEXT]</span>
      </div>
    </div>

    <!-- Zone 4 (bottom-left) -->
    <div id="z4" class="media-zone clip" data-start="40.8" data-duration="9.2" data-track-index="85"
         style="top:320px;left:100px;width:500px;height:200px">
      <div class="zone-type">[ZONE4-TYPE]</div>
      <div class="zone-content">[ZONE4-HEADLINE]<br>
        <span style="font-size:9px;color:#888;font-weight:400">[ZONE4-SUBTEXT]</span>
      </div>
    </div>

    <!-- Zone 5 (bottom-right) -->
    <div id="z5" class="media-zone clip" data-start="41.4" data-duration="8.6" data-track-index="86"
         style="top:320px;left:620px;width:660px;height:200px">
      <div class="zone-type">[ZONE5-TYPE]</div>
      <div class="zone-content">[ZONE5-HEADLINE]<br>
        <span style="font-size:9px;color:#888;font-weight:400">[ZONE5-SUBTEXT]</span>
      </div>
    </div>

    <!-- KEYWORD pulse (8×) -->
    <div id="kw-pulse" class="clip" data-start="42" data-duration="8" data-track-index="87"
         style="position:absolute;top:580px;left:100px;right:100px;
                font-size:80px;font-weight:800;color:#000;letter-spacing:0.05em;
                text-align:center;text-transform:uppercase">
      [KEYWORD] [KEYWORD COMPOUND 1]
    </div>

  </div><!-- /ch05 -->

  <!-- ══ CH06: THE COST (50–60s) ════════════════════════════════════ -->
  <div id="ch06" class="scene clip" data-start="50" data-duration="10" data-track-index="100">

    <!-- Context block (appears first) -->
    <div id="ch06-ctx" class="clip" data-start="50" data-duration="10" data-track-index="101"
         style="position:absolute;top:80px;left:200px;width:1520px;
                border-bottom:1px solid #000;padding-bottom:14px;
                display:flex;justify-content:space-between">
      <span style="font-size:10px;letter-spacing:0.2em;color:#555;text-transform:uppercase">[KEYWORD] LOSS STUDY — TOTAL LIFETIME COST</span>
      <span style="font-size:10px;color:#aaa;font-family:'Courier New',monospace">CALCULATION REF-007 · PEER REVIEWED</span>
    </div>

    <!-- The big number -->
    <div id="the-number" class="the-number clip" data-start="51.5" data-duration="8.5" data-track-index="102">
      <div class="num">[THE-BIG-NUMBER]</div>
      <div class="unit">[UNIT-LABEL]</div>
      <div class="sub">[SUPPORTING-SENTENCE]</div>
    </div>

    <!-- Calculation details -->
    <div class="clip" data-start="53" data-duration="7" data-track-index="103"
         style="position:absolute;top:860px;left:200px;
                font-size:11px;color:#aaa;letter-spacing:0.1em;
                font-family:'Courier New',monospace">
      [CALCULATION: e.g. 4.2 hours/day × 365 × 75 years = 9.25 years]
    </div>

  </div><!-- /ch06 -->

  <!-- ══ CH07: THE COLLAPSE (60–67s) ════════════════════════════════ -->
  <div id="ch07" class="scene clip" data-start="60" data-duration="7" data-track-index="120">

    <!-- Wave 1: 12 instances, t=60 -->
    <!-- Wave 2: 20 instances, t=63 -->
    <!-- Wave 3: 30 instances, t=65 -->
    <!-- Generated by GSAP in the script below using hardcoded positions -->

  </div><!-- /ch07 -->

  <!-- ══ CH08: THE ENDING (67–72s) ══════════════════════════════════ -->
  <div id="ch08" class="scene clip" data-start="67" data-duration="5" data-track-index="180">

    <div id="end1" class="end-line clip" data-start="68.7" data-duration="3.3" data-track-index="181"
         style="top:360px">[END LINE 1]</div>
    <div id="end2" class="end-line clip" data-start="69.8" data-duration="2.2" data-track-index="182"
         style="top:430px">[END LINE 2]</div>
    <div id="end3" class="end-sub clip" data-start="71.0" data-duration="1" data-track-index="183"
         style="top:510px">[END LINE 3 — gray question]</div>

  </div><!-- /ch08 -->

</div><!-- /root -->

<script>
// ══ GSAP TIMELINE ═══════════════════════════════════════════════════
const tl = gsap.timeline({ paused: true });
window.__timelines = window.__timelines || {};
window.__timelines.root = tl;

// ── Hard chapter kills ───────────────────────────────────────────────
tl.set('#ch01', { opacity: 0 }, 8.0);
tl.set('#ch02', { opacity: 0 }, 18.0);
tl.set('#ch03', { opacity: 0 }, 28.0);
tl.set('#ch04', { opacity: 0 }, 38.0);
tl.set('#ch05', { opacity: 0 }, 50.0);
tl.set('#ch06', { opacity: 0 }, 60.0);
tl.set('#ch07', { opacity: 0 }, 67.0);

// ── CH01: Flash words ────────────────────────────────────────────────
['#fw1','#fw2','#fw3','#fw4','#fw5','#fw6','#fw7'].forEach(function(id, i) {
  tl.set(id, { opacity: 1 }, 0.3 + i * 0.4);
  tl.set(id, { opacity: 0 }, 0.65 + i * 0.4);
});
// Title entrance: 3-line stagger skewX
tl.set('#ch01-title', { opacity: 1 }, 3.5);
['.t1','.t2','.t3'].forEach(function(cls, i) {
  tl.fromTo('#ch01-title ' + cls,
    { x: -40, skewX: -4, opacity: 0 },
    { x: 0, skewX: 0, opacity: 1, duration: 0.55, ease: 'power3.out' },
    3.6 + i * 0.18);
});
tl.fromTo('#ch01-title .series',
  { opacity: 0, y: 10 },
  { opacity: 1, y: 0, duration: 0.4, ease: 'power2.out' }, 4.3);

// ── CH02: Chaos → Order ──────────────────────────────────────────────
var c2cards = [
  { id: '#ev1', finalRot: -2,   chaosX:  320, chaosY:  180, chaosR:  22 },
  { id: '#ev2', finalRot:  1.5, chaosX: -260, chaosY:  240, chaosR: -18 },
  { id: '#ev3', finalRot:  3,   chaosX: -420, chaosY:  160, chaosR:  28 },
  { id: '#ev4', finalRot: -1.5, chaosX:  380, chaosY: -140, chaosR: -24 },
  { id: '#ev5', finalRot:  2,   chaosX: -200, chaosY: -180, chaosR:  16 },
  { id: '#ev6', finalRot: -2.5, chaosX:  240, chaosY: -120, chaosR: -20 }
];
c2cards.forEach(function(c) {
  tl.set(c.id, { x: c.chaosX, y: c.chaosY, rotation: c.chaosR, opacity: 1 }, 8.0);
});
c2cards.forEach(function(c, i) {
  tl.to(c.id, { x: 0, y: 0, rotation: c.finalRot, duration: 0.7, ease: 'back.out(1.6)' }, 8.4 + i * 0.3);
});
// Thread draw-ons
tl.to('#thread1', { strokeDashoffset: 0, duration: 0.8, ease: 'power2.inOut' }, 10.5);
tl.to('#thread2', { strokeDashoffset: 0, duration: 0.7, ease: 'power2.inOut' }, 11.2);
tl.to('#thread-node', { strokeDashoffset: 0, duration: 0.6, ease: 'power2.inOut' }, 12.0);
// Card micro-breathing
c2cards.forEach(function(c, i) {
  tl.to(c.id, { rotation: (c.finalRot + 0.4), duration: 1.8, ease: 'sine.inOut', yoyo: true, repeat: 3 }, 9.5 + i * 0.1);
});

// ── CH03: Log stagger + highlight ────────────────────────────────────
['#log1','#log2','#log3','#log4','#log5'].forEach(function(id, i) {
  tl.fromTo(id, { x: 30, opacity: 0 }, { x: 0, opacity: 1, duration: 0.4, ease: 'power2.out' }, 19.2 + i * 1.2);
});
tl.to('#hl-line', { strokeDashoffset: 0, duration: 1.2, ease: 'power2.inOut' }, 22.0);
tl.fromTo('#ch03-quote', { y: 20, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6, ease: 'power2.out' }, 25.0);

// ── CH04: Finding slides + annotation circles ─────────────────────────
['#f1','#f2','#f3'].forEach(function(id, i) {
  tl.fromTo(id, { x: 120, rotationY: 8, opacity: 0 }, { x: 0, rotationY: 0, opacity: 1, duration: 0.6, ease: 'power3.out' }, 29.5 + i * 2.0);
});
tl.to('#ann1', { strokeDashoffset: 0, duration: 0.7, ease: 'power2.inOut' }, 30.5);
tl.to('#ann2', { strokeDashoffset: 0, duration: 0.7, ease: 'power2.inOut' }, 32.5);
tl.fromTo('#confirmed-stamp', { scale: 1.4, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.3, ease: 'back.out(1.4)' }, 35.0);

// ── CH05: Zone drop-ins ──────────────────────────────────────────────
['#z1','#z2','#z3','#z4','#z5'].forEach(function(id, i) {
  tl.fromTo(id, { y: -25, rotation: (i % 2 === 0 ? 3 : -3), opacity: 0 },
    { y: 0, rotation: 0, opacity: 1, duration: 0.45, ease: 'back.out(1.4)' }, 39.0 + i * 0.6);
});
tl.fromTo('#kw-pulse', { opacity: 0, scale: 0.95 }, { opacity: 1, scale: 1, duration: 0.4, ease: 'power2.out' }, 42.0);
// Pulse 4×
[42.0, 44.0, 46.0, 48.0].forEach(function(t) {
  tl.to('#kw-pulse', { scaleX: 1.02, duration: 0.15, ease: 'power2.out', yoyo: true, repeat: 1 }, t);
});

// ── CH06: The number ────────────────────────────────────────────────
tl.fromTo('#the-number', { scale: 0.92, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.5, ease: 'power2.out' }, 51.5);

// ── CH07: Flood ──────────────────────────────────────────────────────
// Hardcoded positions for 62 KEYWORD instances (3 waves)
// Replace [KEYWORD] with actual keyword below
var floodKeyword = '[KEYWORD]';
var floodCompounds = [
  floodKeyword + ' ECONOMY', floodKeyword + ' CRISIS',
  floodKeyword + ' CAPTURE', floodKeyword + ' DRAIN',
  floodKeyword + ' MARKET', floodKeyword + ' RESEARCH',
  floodKeyword + ' LOSS',   floodKeyword + ' STUDY',
  floodKeyword + ' DESIGN', floodKeyword + ' REPORT',
  floodKeyword + ' SYSTEM', floodKeyword
];
// Wave 1: 12 items at t=60
var wave1Pos = [
  [120,80,28],[420,200,22],[780,120,32],[1100,80,26],[1400,160,20],[1680,100,30],
  [220,420,24],[560,520,28],[920,480,20],[1240,400,26],[1540,500,22],[1820,440,18]
];
var wave2Pos = [
  [80,300,14],[300,160,18],[600,320,16],[850,280,20],[1080,320,14],[1320,260,18],
  [1600,300,16],[1760,200,12],[140,660,18],[380,700,14],[650,720,16],[900,660,20],
  [1150,700,14],[1400,680,18],[1620,660,14],[160,900,12],[440,860,16],[700,880,14],
  [960,900,18],[1200,860,12]
];
var wave3Pos = [];
var lcg3 = 77777;
for (var wi = 0; wi < 30; wi++) {
  lcg3 = (lcg3 * 1664525 + 1013904223) & 0x7FFFFFFF;
  var wx = 60 + (lcg3 % 1800);
  lcg3 = (lcg3 * 1664525 + 1013904223) & 0x7FFFFFFF;
  var wy = 60 + (lcg3 % 960);
  wave3Pos.push([wx, wy, 8 + (wi % 7)]);
}

function createFloodWord(x, y, size, text, wave) {
  var el = document.createElement('div');
  el.className = 'flood-word';
  el.style.left = x + 'px';
  el.style.top = y + 'px';
  el.style.fontSize = size + 'px';
  el.textContent = text;
  el.dataset.wave = wave;
  document.getElementById('ch07').appendChild(el);
  return el;
}

wave1Pos.forEach(function(pos, i) {
  var el = createFloodWord(pos[0], pos[1], pos[2], floodCompounds[i % floodCompounds.length], 1);
  tl.fromTo(el, { opacity: 0, y: -8 }, { opacity: 1, y: 0, duration: 0.25, ease: 'power2.out' }, 60.0 + i * 0.06);
});
wave2Pos.forEach(function(pos, i) {
  var el = createFloodWord(pos[0], pos[1], pos[2], floodCompounds[i % floodCompounds.length], 2);
  tl.fromTo(el, { opacity: 0 }, { opacity: 1, duration: 0.2, ease: 'none' }, 63.0 + i * 0.04);
});
wave3Pos.forEach(function(pos, i) {
  var el = createFloodWord(pos[0], pos[1], pos[2], floodKeyword, 3);
  tl.fromTo(el, { opacity: 0 }, { opacity: 1, duration: 0.15, ease: 'none' }, 65.0 + i * 0.03);
});
// All red at t=66
tl.to('.flood-word', { color: '#c00', duration: 0.1, ease: 'none' }, 66.0);
// All disappear at t=67
tl.to('.flood-word', { opacity: 0, duration: 0.2, ease: 'none' }, 66.8);

// ── CH08: Ending lines ───────────────────────────────────────────────
tl.fromTo('#end1', { opacity: 0 }, { opacity: 1, duration: 0.6, ease: 'power2.out' }, 68.7);
tl.fromTo('#end2', { opacity: 0 }, { opacity: 1, duration: 0.6, ease: 'power2.out' }, 69.8);
tl.fromTo('#end3', { opacity: 0 }, { opacity: 1, duration: 0.6, ease: 'power2.out' }, 71.0);

// ── Chapter label updates ────────────────────────────────────────────
var chLabels = [
  [0,  'CH.01 / THE INVESTIGATION'],
  [8,  'CH.02 / EVIDENCE BOARD'],
  [18, 'CH.03 / ONE PERSON'],
  [28, 'CH.04 / THE DISCOVERY'],
  [38, 'CH.05 / ESCALATION'],
  [50, 'CH.06 / THE COST'],
  [60, 'CH.07 / COLLAPSE'],
  [67, 'CH.08 / ENDING']
];
chLabels.forEach(function(entry) {
  tl.call(function(lbl) {
    var el = document.getElementById('ch-label-persist');
    if (el) el.textContent = lbl;
  }, [entry[1]], entry[0]);
});
</script>
</body>
</html>
```

**After writing index.html, always run:**
```bash
cd my-video && npm run check
```
Fix ALL errors before proceeding.

---

## Step 4 — Audio Generation Script

Generate `/tmp/gen_audio.py` with this template. Fill placeholders from Step 1B.

```python
"""
Audio track for [TOPIC] editorial documentary.
Three-layer system: BGM + SFX + Ambience
Total: [DURATION]s
Output: /tmp/audio_track.wav
"""
import wave, struct, math, array, os

SR = 44100
DURATION = 72.0  # adjust to match data-duration in root div
N = int(SR * DURATION)
buf_L = [0.0] * N
buf_R = [0.0] * N

# ── LCG noise (deterministic, no Math.random equivalent) ──────────────
def lcg(n, seed=12345):
    s = seed & 0xFFFFFFFF
    out = []
    for _ in range(n):
        s = (s * 1664525 + 1013904223) & 0xFFFFFFFF
        out.append(((s >> 16) / 32768.0) - 1.0)
    return out

def mix(buf, samples, t, vol=1.0, pan=0.0):
    off = int(t * SR)
    lvol = vol * (1.0 - max(0, pan)) 
    rvol = vol * (1.0 + min(0, pan))
    for i, v in enumerate(samples):
        idx = off + i
        if 0 <= idx < N:
            buf_L[idx] = max(-1.0, min(1.0, buf_L[idx] + v * lvol))
            buf_R[idx] = max(-1.0, min(1.0, buf_R[idx] + v * rvol))

def env(s, atk, dec):
    n = len(s); a = int(atk*SR); d = int(dec*SR)
    return [v * (i/max(1,a) if i<a else math.exp(-5*(i-a)/max(1,d)) if i<a+d else 0.0)
            for i,v in enumerate(s)]

def lp1(s, fc):
    alpha = fc/(fc + SR/(2*math.pi)); prev = 0.0; out = []
    for v in s:
        prev = prev + alpha*(v - prev); out.append(prev)
    return out

def hp1(s, fc):
    alpha = 1.0/(1.0 + 2*math.pi*fc/SR); px = py = 0.0; out = []
    for x in s:
        y = alpha*(py + x - px); out.append(y); px,py = x,y
    return out

def sine(freq, dur): n=int(dur*SR); return [math.sin(2*math.pi*freq*i/SR) for i in range(n)]
def sweep(f0,f1,dur): n=int(dur*SR); return [math.sin(2*math.pi*f0*((f1/f0)**(i/SR/dur))*i/SR) for i in range(n)]

# ── SFX definitions ───────────────────────────────────────────────────
def soft_click():
    n = int(0.018*SR)
    return lp1(env([math.sin(2*math.pi*820*i/SR)*math.exp(-160*i/SR) for i in range(n)], 0.001, 0.017), 1800), 0.12

def paper_slide(seed=9999):
    n = int(0.07*SR); noise = lcg(n, seed)
    # sweep bandpass 1200→3000
    out=[0.0]*n; x1=x2=y1=y2=0.0
    for i,x0 in enumerate(noise):
        fc=1200*((3000/1200)**(i/n)); R=1-math.pi*1500/SR; K=-math.cos(2*math.pi*fc/SR)
        b0=(1-R)/2; b2=-(1-R)/2; a1=2*R*K; a2=-(R*R)
        y0=b0*x0+b2*x2+a1*y1+a2*y2; x2,x1,y2,y1=x1,x0,y1,y0; out[i]=y0
    return env(out, 0.005, 0.065), 0.16

def ui_tap():
    n=int(0.022*SR)
    return lp1(env([math.sin(2*math.pi*600*i/SR) for i in range(n)], 0.001, 0.021), 1200), 0.09

def clock_tick():
    n=int(0.025*SR)
    return env([math.sin(2*math.pi*1150*i/SR) for i in range(n)], 0.001, 0.024), 0.07

def digital_pulse():
    n=int(0.2*SR); tone=sine(68, 0.2)
    return lp1(env(tone, 0.003, 0.197), 200), 0.22

def tok():
    n=int(0.085*SR)
    return env(lp1(lcg(n, 33333), 800), 0.002, 0.083), 0.14

def single_thump():
    # ONE hit. Weight, not drama. Sine sweep 90→30Hz, 350ms.
    s = sweep(90, 30, 0.35)
    return env(s, 0.002, 0.348), 0.85

def heartbeat():
    # Two-hit pattern: lub-dub
    dur=0.35; n=int(dur*SR)
    s1=sweep(60,25,0.12); s2=sweep(55,22,0.10)
    out=[0.0]*n
    for i,v in enumerate(env(s1,0.002,0.118)): out[i]+=v*0.6
    off=int(0.16*SR)
    for i,v in enumerate(env(s2,0.002,0.098)):
        if off+i<n: out[off+i]+=v*0.45
    return out, 0.35

def piano_note(freq=293.66):  # D4 — reflective
    dur=2.8; n=int(dur*SR)
    harmonics=[(1,1.0),(2,0.5),(3,0.25),(4,0.12)]
    out=[]
    for i in range(n):
        t=i/SR; v=sum(a*math.sin(2*math.pi*freq*h*t) for h,a in harmonics)
        env_v=math.exp(-t/1.1) if t<0.01 else math.exp(-t/1.1)
        out.append(v*env_v)
    return lp1(out, 2000), 0.45

# ── BGM: minimal tech pulse ───────────────────────────────────────────
print("Generating BGM...")
bpm = 84; beat = 60.0 / bpm
pulse_dur = beat * 0.18
for beat_n in range(int(DURATION / beat)):
    t = beat_n * beat
    if t > DURATION - 2: break
    # Cutoff closes 34–55s
    if t < 34: fc = 900
    elif t < 55: fc = 900 - 700 * ((t-34)/21)
    else: fc = 200
    s = lp1(env(sine(52, pulse_dur), 0.004, pulse_dur-0.004), fc)
    vol = 0.14
    if t > 55 and t < 60: vol = 0.14 * (1 - (t-55)/5)
    elif t > 60 and t < 67: vol = 0.06
    elif t >= 67: vol = 0.0
    mix(buf_L, s, t, vol); mix(buf_R, s, t, vol)

# Low drone
print("Generating drone...")
drone_n = int(DURATION * SR)
for i in range(drone_n):
    t = i / SR
    if t < 34: v = 0.04
    elif t < 55: v = 0.04 + 0.08 * ((t-34)/21)
    elif t < 60: v = 0.12
    elif t < 62: v = 0.12 * (1-(t-60)/2)
    else: v = 0.0
    sample = math.sin(2*math.pi*42*i/SR) * v
    buf_L[i] = max(-1,min(1,buf_L[i]+sample))
    buf_R[i] = max(-1,min(1,buf_R[i]+sample))

# ── Ambience ──────────────────────────────────────────────────────────
print("Generating ambience...")
amb_n = int(60 * SR); amb = lcg(amb_n, 54321)
# BP filter 200–800Hz
R=1-math.pi*600/SR; K=-math.cos(2*math.pi*400/SR)
b0=(1-R)/2; b2=-(1-R)/2; a1=2*R*K; a2=-(R*R)
out=[0.0]*amb_n; x1=x2=y1=y2=0.0
for i,x0 in enumerate(amb):
    y0=b0*x0+b2*x2+a1*y1+a2*y2; x2,x1,y2,y1=x1,x0,y1,y0; out[i]=y0
for i,v in enumerate(out):
    fade = 1.0 - max(0,(i/SR - 55)/7)
    mix(buf_L, [v*0.04*fade], i/SR); mix(buf_R, [v*0.04*fade], i/SR)

# ── SFX CUE MAP ───────────────────────────────────────────────────────
# Adjust timestamps to match your chapter layout
print("Generating SFX cues...")
cues = [
    # CH01 flash words
    (0.3,  soft_click, ()),  (0.7,  soft_click, ()),
    (1.1,  soft_click, ()),  (1.5,  soft_click, ()),
    (1.9,  soft_click, ()),  (2.3,  soft_click, ()),
    (2.7,  soft_click, ()),
    (3.5,  tok,        ()),  (3.7,  tok,        ()),  (3.9,  tok,        ()),
    # CH02 chaos+settle
    (8.0,  paper_slide, (9999,)),
    (8.4,  ui_tap,  ()), (8.7, ui_tap, ()), (9.0, ui_tap, ()),
    (9.3,  ui_tap,  ()), (9.6, ui_tap, ()), (9.9, ui_tap, ()),
    (10.5, paper_slide, (11111,)), (11.2, paper_slide, (22222,)),
    (11.5, ui_tap, ()), (12.0, ui_tap, ()), (12.5, ui_tap, ()),
    # CH03 log rows
    (19.2, clock_tick, ()), (20.4, clock_tick, ()),
    (21.6, clock_tick, ()), (22.8, clock_tick, ()), (24.0, clock_tick, ()),
    (22.0, paper_slide, (33333,)),
    # CH04 findings
    (29.5, tok, ()), (31.5, tok, ()), (33.5, tok, ()),
    (30.5, ui_tap, ()), (32.5, ui_tap, ()),
    (35.0, single_thump, ()),  # CONFIRMED stamp
    # CH05 zones
    (39.0, tok, ()), (39.6, tok, ()), (40.2, tok, ()), (40.8, tok, ()), (41.4, tok, ()),
    (42.0, digital_pulse, ()), (44.0, digital_pulse, ()),
    (46.0, digital_pulse, ()), (48.0, digital_pulse, ()),
    # CH06 THE NUMBER
    (51.5, single_thump, ()),  # ONE thump only
    # CH07 flood
    (60.0, paper_slide, (44444,)),
    (61.0, heartbeat, ()), (62.5, heartbeat, ()), (64.0, heartbeat, ()),
    # CH08 piano
    (63.0, piano_note, ()),  # timed to black screen onset in master video
]

for t, fn, args in cues:
    s, v = fn(*args)
    mix(buf_L, s, t, v)
    mix(buf_R, s, t, v)
    print(f"  {t:5.1f}s  {fn.__name__}  vol={v:.2f}")

# ── Master tanh limiter ───────────────────────────────────────────────
limit = 0.92
int_samples = []
for L, R in zip(buf_L, buf_R):
    int_samples.append(max(-32767, min(32767, int(math.tanh(L/limit)*limit * 32767))))
    int_samples.append(max(-32767, min(32767, int(math.tanh(R/limit)*limit * 32767))))

# ── Write WAV ─────────────────────────────────────────────────────────
out_path = '/tmp/audio_track.wav'
arr = array.array('h', int_samples)
with wave.open(out_path, 'w') as wf:
    wf.setnchannels(2)
    wf.setsampwidth(2)
    wf.setframerate(SR)
    wf.writeframes(arr.tobytes())

print(f"\nDone. {os.path.getsize(out_path)//1024} KB, {DURATION}s stereo @ {SR}Hz")
```

Run it:
```bash
python3 /tmp/gen_audio.py
```

---

## Step 5 — Render and Mix

```bash
# Static ffmpeg (use if system ffmpeg is broken)
FFMPEG=/opt/node22/lib/node_modules/ffmpeg-static/ffmpeg

# Render video (no audio — Web Audio not captured)
cd my-video && npm run render
# Output: renders/my-video_[timestamp].mp4

# Mix audio into video
RENDER=$(ls -t my-video/renders/*.mp4 | head -1)
$FFMPEG -i "$RENDER" -i /tmp/audio_track.wav \
  -map 0:v -map 1:a \
  -c:v libx264 -crf 16 \
  -c:a aac -b:a 256k \
  -shortest \
  my-video/renders/final_with_audio.mp4

echo "Done: my-video/renders/final_with_audio.mp4"
```

---

## Step 6 — Quality Check

Before delivering, verify:

```
□ npm run check → 0 errors
□ Video opens and plays from 0s without black flash
□ CH02 chaos→order animation visible
□ CH06 single number renders large and centered
□ CH07 flood covers screen, turns red, disappears instantly
□ CH08 text appears on black background
□ Audio present: SFX click on each flash word, single thump at THE NUMBER
□ No audio continues past CH08 black screen (except piano tail)
□ Print Test: pause at t=5s, 15s, 25s, 35s, 45s → all look like magazine spreads
```

---

## Design System Reference

### Palette (locked)
```
#ffffff — paper background
#000000 — ink (primary text)
#555555 — gray (captions, metadata)
#c00000 — red (annotations, stamps, accents ONLY)
#0a0a0a — near-black (CH01 only)
```

### Typography
```
Font:    'Helvetica Neue', Helvetica, Arial, sans-serif
Mono:    'Courier New' (timestamps, codes, archive refs)
Weight contrast is the ONLY decorative tool — no color, no size inflation
```

### Motion Rules
```
✅ Paper physics: back.out(1.6) settle, power3.out entrance, sine.inOut breathing
✅ SVG draw-on: strokeDashoffset for annotations
✅ Text: skewX entrance, y:20→0 fade-up
❌ Forbidden: scale pop, glitch, RGB split, neon glow, bounce, elastic, linear on text
```

### Frame Density Minimum
Every frame must contain **4 layers**:
1. Primary content
2. Document/publication wrapper  
3. Source annotation / FIG reference
4. Background texture / watermark

### KEYWORD Escalation Pattern
```
CH01: 1× hidden   CH02: 3×   CH03: 4×   CH04: 5×
CH05: 8×          CH06: bg   CH07: 62×  CH08: 0×
```

### Audio Mix Levels
```
BGM        -16 dBFS   Pulse 80–90 BPM, no drops
SFX        -8 dBFS    Every information event has a sound
Transitions -10 dBFS  Paper physics sounds
Ambience   -20 dBFS   Room texture, barely perceptible
```

---

## Anti-Pattern Checklist

```
❌ Any number floating alone on empty background (must live inside a document)
❌ Any chart not inside a publication frame
❌ KEYWORD as decoration — must be embedded in compound phrases
❌ More than ONE thump at the data revelation
❌ Music continuing over final black screen text
❌ Glitch, RGB split, neon, HUD elements
❌ Hard aspect ratio mismatch if splicing clips
❌ Math.random() or Date.now() anywhere in HTML
```

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `npm run check` clip errors | Every element with `data-start` needs `class="clip"` |
| Chaos cards don't appear | Check `tl.set(id, { opacity:1 }, 8.0)` runs before settle tweens |
| Audio track too long | Add `-shortest` to ffmpeg mix command |
| System ffmpeg missing libcaca | Use `/opt/node22/lib/node_modules/ffmpeg-static/ffmpeg` |
| Piano note too late | Calculate: `piano_t = part1_end + (black_screen_t_in_source - source_splice_start)` |
| Flood words persist after CH07 | Ensure `tl.set('#ch07', {opacity:0}, 67.0)` is present |
| 25fps in final output | Add `fps=30` filter: `[0:v]fps=30[v0]` in filter_complex |
