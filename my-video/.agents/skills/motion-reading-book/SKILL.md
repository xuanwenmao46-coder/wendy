---
name: motion-reading-book
description: >
  根据书名、作者、简介、角色图片等输入，生成一段完整的「Motion Reading」风格书影视频 HTML 合成文件。
  适用于书单推荐、读书博主、知识分享等场景。输出为 HyperFrames 兼容的 index.html，可直接渲染为 MP4。
  Use when: user provides a book title, author, key quote, character images, and wants a motion book-review video.
---

# Motion Reading Book Skill

## 工作流

### Step 1 — 收集参数

从用户输入中提取以下信息：

| 参数 | 说明 | 示例 |
|---|---|---|
| `book_title` | 书名（拆分为两行，每行最多6字符） | `HARRY / POTTER` |
| `author` | 作者全名 | `J.K. Rowling` |
| `year` | 出版年份 | `1997` |
| `series_name` | 系列名（可选） | `Harry Potter Series` |
| `series_no` | 系列编号（可选） | `02` |
| `genre` | 体裁，用于选色 | `fantasy` / `scifi` / `thriller` / `romance` / `literary` |
| `key_quote` | 全书最具代表性的引句（≤30字） | `"You're a wizard, Harry."` |
| `quote_speaker` | 引句来源 | `Rubeus Hagrid · Year One` |
| `protagonist` | 主角名（全大写，≤8字符） | `HARRY` |
| `protagonist_trait` | 主角特质描述（4组，每组2行） | `BORN TO\nTWO WORLDS` |
| `antagonist` | 反派/张力词（全大写，分3行） | `LORD / VOLDE / MORT` |
| `antagonist_bio` | 反派简介 | `Tom Marvolo Riddle · Half-Blood` |
| `closing_word` | 情感收尾词（1-2个词，全书灵魂） | `Always.` |
| `closing_quote` | 收尾词前的小问句 | `"After all this time?"` |
| `closing_speaker` | 收尾引言来源 | `Severus Snape · Ch. 33` |
| `stats_number` | 核心统计数字（大字显示） | `4,195` |
| `stats_label` | 统计数字说明 | `SEVEN BOOKS · TOTAL PAGES` |
| `book_bars` | 各册页数列表（7个值，用于柱状图） | `[223,251,317,636,870,607,759]` |
| `book_labels` | 各册缩写 | `["PS","CoS","PoA","GoF","OotP","HBP","DH"]` |
| `endcard_quote` | 尾卡引言（核心主题） | `"Not talent. Not destiny. Love is the only magic."` |
| `img_protagonist` | 主角图片路径 | `assets/harry-nobg.png` |
| `img_antagonist` | 反派图片路径 | `assets/tomriddle-nobg.png` |
| `img_emotional` | 情感场景图片路径 | `assets/snape-nobg.png` |

### Step 2 — 选择色彩方案

根据 `genre` 自动选择预设色板，也可用户手动指定：

| Genre | 背景 bg | 亮面板 panel | 强调色 accent | 金色 gold |
|---|---|---|---|---|
| `fantasy` | `#0D1427` | `#E8DFC8` | `#9B1515` | `#C9A050` |
| `scifi` | `#080E1C` | `#D0DFF0` | `#0D4FA0` | `#40C4C4` |
| `thriller` | `#0D0D0D` | `#F0F0F0` | `#C41A1A` | `#AAAAAA` |
| `romance` | `#1A0A12` | `#F5E4E8` | `#8B1A3A` | `#D4967A` |
| `literary` | `#0F1208` | `#F0EDE0` | `#1A4A20` | `#C8A456` |

### Step 3 — 生成 HTML

运行脚本：

```bash
skill_dir=""
for base in "${AGENTS_HOME:-$HOME/.agents}" "${CLAUDE_HOME:-$HOME/.claude}" "${CODEX_HOME:-$HOME/.codex}"; do
  if [ -d "$base/skills/motion-reading-book" ]; then
    skill_dir="$base/skills/motion-reading-book"
    break
  fi
done
[ -n "$skill_dir" ] || { echo "motion-reading-book skill not found"; exit 1; }

python3 "$skill_dir/scripts/generate_motion_reading.py" \
  --book-title "HARRY POTTER" \
  --title-line1 "HARRY" \
  --title-line2 "POTTER" \
  --author "J.K. Rowling" \
  --year "1997" \
  --series-name "Harry Potter Series" \
  --series-no "02" \
  --genre "fantasy" \
  --key-quote "\"You're a wizard, Harry.\"" \
  --quote-speaker "Rubeus Hagrid · Year One" \
  --protagonist "HARRY" \
  --protagonist-traits "BORN TO|TWO WORLDS,MARKED|BY EVIL,RAISED|AS HUMAN,RETURNED|TO DESTINY,YOU ARE|THE ONE" \
  --antagonist-lines "LORD,VOLDE,MORT" \
  --antagonist-bio "Tom Marvolo Riddle · anagram|Slytherin · Class of 1945 · Half-Blood" \
  --closing-word "Always." \
  --closing-quote "\"After all this time?\"" \
  --closing-speaker "Severus Snape · Deathly Hallows · Ch. 33" \
  --stats-number "4,195" \
  --stats-label "SEVEN BOOKS · TOTAL PAGES · NARRATIVE ARC" \
  --book-bars "223,251,317,636,870,607,759" \
  --book-labels "PS,CoS,PoA,GoF,OotP,HBP,DH" \
  --peak-bar 4 \
  --peak-label "PEAK · 870P" \
  --endcard-quote "\"Not talent. Not destiny. Love is the only magic that endures.\"" \
  --img-protagonist "assets/harry-nobg.png" \
  --img-antagonist "assets/tomriddle-nobg.png" \
  --img-emotional "assets/snape-nobg.png" \
  --output "index.html"
```

### Step 4 — 输出

脚本打印生成的 HTML 文件路径。告诉用户在浏览器中预览，或直接运行 `npm run render` 渲染为 MP4。

## 图片处理建议

- 上传的图片推荐使用 `hyperframes-media` skill 的 `remove-background` 命令预处理去背景
- 处理后的图片放入 `assets/` 目录，路径传给 `--img-*` 参数
- 若无去背图片，可直接使用原图，滤镜会自动做高对比度黑白处理

## 时长说明

- 默认生成 46 秒视频（与原 HP 视频一致）
- Acts 时间轴：0-3s 标题 | 3-9s 引句 | 9-14s 主角 | 14-22s 统计 | 22-28s 反派 | 28-37s 情感 | 37-46s 尾卡
- 如需调整时长，直接编辑生成的 HTML 中的 `data-duration` 和对应 GSAP 时间点

## 关联资源

- **HTML 模板**：`assets/motion_reading_template.html`
- **生成脚本**：`scripts/generate_motion_reading.py`
