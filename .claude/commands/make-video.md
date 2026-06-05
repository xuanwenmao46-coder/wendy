# /make-video — Brutalist Documentary Video Generator

Generate a CONTROL FAILURE–style brutalist Swiss design short film.
User provides: topic, color scheme, photos. Output: MP4 ~78s with synthesized audio.

## Step 1 — Gather requirements

If `$ARGUMENTS` is empty, ask the user these questions (all in one message):

> **请告诉我以下信息：**
> 1. **主题**：你想科普什么？（例：气候变化、网络安全、食品安全…）用1-3句话描述故事弧：问题是什么 → 系统如何失败 → 后果是什么
> 2. **标志色调**：选择情绪基调
>    - 🔴 警报红系（rage/crimson） — 紧急、危险
>    - 🟡 酸黄系（acid/volt） — 警示、系统感
>    - 🔵 冷蓝系（volt/bone） — 科技、冷峻
>    - 或描述自定义颜色（如"深绿+荧光黄"）
> 3. **照片**：直接上传2-4张相关照片（会以duotone效果插入视频）
> 4. **章节关键词**（可选）：每章一个词，共7章。留空则自动生成。

Parse the user's reply into these variables:
- `TOPIC`: the subject matter (e.g. "climate change", "food safety")
- `NARRATIVE`: 3-act arc (problem → failure → consequence)
- `COLOR_PRIMARY`: main accent color hex (default #DEFF0A acid yellow)
- `COLOR_DANGER`: danger/alert color hex (default #FF3300 rage red)
- `COLOR_FIELD`: background field color for CH06 cards (default #0033FF volt blue)
- `COLOR_BG`: chapter background (default #080808 ink black)
- `CHAPTER_WORDS`: array of 7 chapter titles (auto-generate from topic if not provided)
- `PHOTOS`: list of uploaded photo filenames

## Step 2 — Generate chapter structure

From `TOPIC` and `NARRATIVE`, auto-generate a 7-chapter arc:

```
CH01 (0-8s):   PERFECT STATE — the ideal, the norm, before the problem
CH02 (8-16s):  THE ANOMALY — first signal, ignored or unnoticed
CH03 (16-25s): SYSTEM FIGHTS BACK — attempted correction, fails
CH04 (25-40s): SPREAD — problem grows, infection/cascade
CH05 (40-54s): ERASURE — what is lost (5 key nouns from topic)
CH06 (54-65s): COLLAPSE — full alarm, consequence realized
CH07 (65-75s): AFTERMATH — what remains, the lesson
```

Generate 5 "erasure words" for CH05 (things lost due to the problem).
Generate 5 "stamp messages" for CH06 (2-line narrative beats, e.g. "FIRST SIGN / IGNORED").
Generate the CH07 closing lines (2 lines of lesson/call-to-action).

## Step 3 — Extract/save photos

For each uploaded photo:
1. Save to `/home/user/wendy/cigarette-journey/` as `photo-{n}.jpg`
2. Assign duotone color:
   - photo-1: COLOR_DANGER tint (first reality intrusion during CH03)
   - photo-2: dark crimson tint (bridges CH05→CH06)
   - photo-3: near-black tint (CH06 climax)
   - photo-4 (if provided): bone white fade (CH07 aftermath)

If user uploaded inline images (not file attachments), extract them from the conversation
using Python base64 decode on the session JSONL at:
`/root/.claude/projects/-home-user-wendy/*.jsonl` (most recent file)

```bash
python3 - <<'EOF'
import json, base64, os, glob
# find most recent jsonl
files = sorted(glob.glob('/root/.claude/projects/-home-user-wendy/*.jsonl'))
jf = files[-1]
imgs = []
with open(jf) as f:
    for line in f:
        try:
            msg = json.loads(line)
            for block in (msg.get('message',{}).get('content') or []):
                if isinstance(block,dict) and block.get('type')=='image':
                    src = block.get('source',{})
                    if src.get('type')=='base64':
                        imgs.append(src['data'])
        except: pass
dest = '/home/user/wendy/cigarette-journey'
for n, data in enumerate(imgs[-4:], 1):
    path = f'{dest}/photo-{n}.jpg'
    with open(path,'wb') as out:
        out.write(base64.b64decode(data))
    print(f'Saved photo-{n}.jpg')
EOF
```

## Step 4 — Generate the HTML film

Create `/home/user/wendy/cigarette-journey/film.html` by adapting the CONTROL FAILURE v2 template.

Key substitutions from user input:
- Replace all color variables with user's chosen palette
- Replace chapter titles/labels with topic-specific text
- Replace CH05 erasure words with the 5 generated nouns
- Replace CH06 stamp messages with generated narrative beats
- Replace CH07 closing lines with the lesson/CTA
- Update photo src attributes to `photo-1.jpg`, `photo-2.jpg`, etc.
- Update photo caption text with topic-specific location/stats
- Update meme content to be topic-relevant (same brutalist style: ink bg, accent color text)
- Update the `DURATION` constant if needed (default 78s)

The HTML structure to follow exactly (copy from control-failure-v2.html and adapt):
- Same GSAP timeline structure and timing
- Same 7-chapter layer system
- Same infection canvas for CH04
- Same word erosion system for CH05
- Same clip-path transitions (diagonal slash CH02, iris open CH04/CH07)
- Same meme overlay system (6 memes at same timestamps)
- Same grain canvas + scanlines
- Same progress bar

Color variable substitution map:
```css
:root {
  --ink:   {COLOR_BG};
  --bone:  #F0EDE5;          /* keep neutral */
  --acid:  {COLOR_PRIMARY};  /* main accent */
  --volt:  {COLOR_FIELD};    /* secondary/field color */
  --rage:  {COLOR_DANGER};   /* danger/alert */
  --crim:  {derived darker variant of COLOR_DANGER};
  --gold:  #F5A800;          /* keep gold for metadata */
}
```

## Step 5 — Generate audio

Create `/home/user/wendy/cigarette-journey/audio-film.js` by adapting generate-audio.js:
- Keep the 128BPM industrial beat structure
- Adjust drone base frequency if needed for emotional tone:
  - Urgent/alarm topics: 38-55Hz (default)
  - Cold/tech topics: 55-80Hz (higher, more clinical)
  - Environmental topics: 28-42Hz (lower, more ominous)
- Keep all chapter rhythms and transitions
- Output to `audio-film.wav`

Run it:
```bash
cd /home/user/wendy/cigarette-journey && node audio-film.js
```

## Step 6 — Generate recorder

Create `/home/user/wendy/cigarette-journey/record-film.js` by copying record-cfv2.js and changing:
- `control-failure-v2.html` → `film.html`
- `control-failure-v2.mp4` → `film-output.mp4`
- `audio-cf.wav` → `audio-film.wav`
- `control-failure-v2-final.mp4` → `film-final.mp4`
- `frames_cfv2` → `frames_film`

## Step 7 — Render

```bash
cd /home/user/wendy/cigarette-journey
node record-film.js > /tmp/render-film.log 2>&1 &
```

Monitor with:
```bash
tail -f /tmp/render-film.log | grep -E --line-buffered "/2340|Final with audio|[Ee]rror"
```

Report progress every 300 frames (10s of video). Total: 2340 frames at 30fps.

## Step 8 — Deliver

When render completes (`✓ Final with audio:` appears in log):
1. Send `film-final.mp4` to user via SendUserFile
2. Commit all generated files to git and push:
   ```bash
   git add cigarette-journey/film.html cigarette-journey/audio-film.js \
           cigarette-journey/record-film.js cigarette-journey/film-final.mp4
   git commit -m "Generate {TOPIC} documentary film"
   git push
   ```

## Quality checklist before rendering

- [ ] All 7 chapter labels updated with topic-specific text
- [ ] CH05 has exactly 5 erasure words (single words, all-caps)
- [ ] CH06 has exactly 5 stamp messages (2 lines each, impactful)
- [ ] CH07 closing line is specific and memorable (not generic)
- [ ] At least 2 photos assigned (photo-1 and photo-2 minimum)
- [ ] Meme content is topic-relevant and uses brutalist visual style
- [ ] Color variables are consistent throughout CSS and JS
- [ ] `window.tl` is exposed for Puppeteer seek
- [ ] No play/reset buttons in HTML
- [ ] Audio file generated successfully before render starts

## Notes

- Render takes ~20 minutes. Keep user informed every 10s of video progress.
- If photos were uploaded as inline chat images (not file attachments), always extract from JSONL first.
- The meme overlays should use film's visual language: `background:var(--ink)`, accent color border, all-caps text. Never use white card backgrounds.
- CH07 is intentionally sparse — but fill the iris-open phase (t=65-67s) with background stats/data text that fades before the main message appears.
- The infection canvas (CH04) must call `drawGrid(t)` in the GSAP `onUpdate` callback.
