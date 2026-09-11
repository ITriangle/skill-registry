---
version: alpha
name: Scatterbrain
description: "A Post-it-note-and-cork-board presentation system. Every content block is a colored sticky note on a textured paper or cork surface, layered with red thumbtacks, masking tape, and decorative doodles. Display type runs in Shrikhand (a chunky decorative display serif) on every headline; body type runs in Zilla Slab (a friendly slab serif); handwritten emphasis runs in Caveat. The palette is pastel sticky-note colors (yellow, blue, pink, green, orange, purple) on cream paper / cork / warm gradient backgrounds. The aesthetic borrows from creative-workshop wall art, brainstorming boards, and indie-studio mood boards: scattered slight rotations, multiple background texture variants per slide, pin / tape / drop-shadow combinations. The effect is warmth, play, and tactile creative-process energy."

colors:
  yellow: "#ffe066"
  yellow-deep: "#ffd43b"
  blue: "#a5d8ff"
  blue-deep: "#74c0fc"
  pink: "#ffc9c9"
  pink-deep: "#ff9f9f"
  green: "#b2f2bb"
  green-deep: "#8ce99a"
  orange: "#ffcc80"
  purple: "#d0bfff"
  cream: "#faf8f3"
  paper: "#f7f5f0"
  ink: "#2d2a26"
  ink-light: "#5c5750"
  shadow: "rgba(45, 42, 38, 0.15)"
  shadow-deep: "rgba(45, 42, 38, 0.25)"

typography:
  display-hero:
    fontFamily: "'Shrikhand', cursive"
    fontSize: "clamp(2.5rem, 5vw, 4.5rem)"
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 0.02em
  statement:
    fontFamily: "'Shrikhand', cursive"
    fontSize: "clamp(2rem, 4vw, 3.5rem)"
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 0.02em
  headline:
    fontFamily: "'Shrikhand', cursive"
    fontSize: "clamp(1.8rem, 3.5vw, 3rem)"
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 0.02em
  title:
    fontFamily: "'Shrikhand', cursive"
    fontSize: "clamp(1.3rem, 2.5vw, 1.8rem)"
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 0.02em
  body:
    fontFamily: "'Zilla Slab', serif"
    fontSize: "clamp(1rem, 1.5vw, 1.25rem)"
    fontWeight: 400
    lineHeight: 1.7
  list-item:
    fontFamily: "'Zilla Slab', serif"
    fontSize: "1.1rem"
    fontWeight: 400
    lineHeight: 1.6
  handwritten:
    fontFamily: "'Caveat', cursive"
    fontSize: "clamp(1.2rem, 2vw, 1.6rem)"
    fontWeight: 400
    lineHeight: 1.4
  handwritten-lg:
    fontFamily: "'Caveat', cursive"
    fontSize: "clamp(1.4rem, 2.5vw, 2rem)"
    fontWeight: 600
    lineHeight: 1.3
  handwritten-sm:
    fontFamily: "'Caveat', cursive"
    fontSize: "clamp(1.2rem, 1.5vw, 1.4rem)"
    fontWeight: 500
    lineHeight: 1.3
  label-script:
    fontFamily: "'Caveat', cursive"
    fontSize: "0.9rem"
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.15em
    textTransform: uppercase
  stat-value:
    fontFamily: "'Shrikhand', cursive"
    fontSize: "1.8rem"
    fontWeight: 400
    lineHeight: 1.1
  caption-subtitle:
    fontFamily: "'Zilla Slab', serif"
    fontSize: "1.3rem"
    fontWeight: 400
    lineHeight: 1.6

spacing:
  slide-pad: 3rem
  post-it-pad-lg: "3rem 4rem"
  post-it-pad-md: "2.5rem"
  post-it-pad-sm: "1.5rem"
  post-it-pad-statement: "3.5rem 4rem"
  gap-lg: "3rem"
  gap-md: "2.5rem"
  gap-sm: "2rem"

canvas:
  width: 100vw
  height: 100vh

components:
  bg-cork:
    backgroundLayers: "radial-gradient ellipse + linear-gradient (warm browns) + SVG plus-sign pattern at 15% opacity"
    description: "Cork-board background variant. Warm tan/brown tonal gradient with a faint pattern of small plus-sign marks suggesting cork texture. Used on slides that feel like 'a wall of pinned notes.'"
  bg-paper:
    backgroundLayers: "linear-gradient (cream) + 40px grid lines at 8% opacity"
    description: "Desk-paper background variant. Cream gradient with a faint 40px grid overlay suggesting graph or notebook paper. Used on slides that feel like 'notes arranged on a desk.'"
  bg-warm:
    backgroundLayers: "multiple radial-gradients (yellow/blue/pink soft glows) + linear-gradient cream base"
    description: "Warm gradient background variant. Cream base with soft-glow ellipses of yellow, blue, and pink suggesting morning light. Used on slides that need a softer, less-textured atmosphere."
  grain-overlay:
    backgroundImage: "SVG fractal-noise filter, 256×256 tile"
    opacity: 0.04
    zIndex: 9999
    description: "Fixed full-viewport SVG grain texture above all content at 4% opacity. Reinforces the paper-and-cork tactile register. Always present."
  post-it:
    padding: "2rem"
    boxShadow: "2px 3px 15px {colors.shadow}, 0 1px 3px {colors.shadow-deep}"
    description: "Generic colored sticky-note base. Soft drop-shadow simulates the note's slight lift off the surface. Always carries a background color from the post-it palette (yellow, blue, pink, green, orange, purple, or white)."
  post-it-yellow:
    background: "linear-gradient(135deg, {colors.yellow} 0%, {colors.yellow-deep} 100%)"
    description: "Yellow sticky variant. Soft 135° gradient from light to deep yellow."
  post-it-blue:
    background: "linear-gradient(135deg, {colors.blue} 0%, {colors.blue-deep} 100%)"
    description: "Blue sticky variant."
  post-it-pink:
    background: "linear-gradient(135deg, {colors.pink} 0%, {colors.pink-deep} 100%)"
    description: "Pink sticky variant."
  post-it-green:
    background: "linear-gradient(135deg, {colors.green} 0%, {colors.green-deep} 100%)"
    description: "Green sticky variant."
  post-it-orange:
    background: "{colors.orange}"
    description: "Orange sticky variant. Flat fill (no gradient) — the only post-it that ships flat."
  post-it-purple:
    background: "{colors.purple}"
    description: "Purple sticky variant. Flat fill."
  post-it-white:
    background: "#fff"
    border: "2px solid {colors.ink}"
    description: "White note variant. Carries a 2px ink border (because pure white otherwise disappears into cream/paper backgrounds). Used as a 'plain note' in timelines or comparisons."
  pin:
    width: 16px
    height: 16px
    position: "::before, top: -12px, centered"
    background: "radial-gradient(circle at 30% 30%, #ff6b6b, #c92a2a)"
    boxShadow: "0 2px 4px {colors.shadow-deep}, inset -2px -2px 4px rgba(0,0,0,0.2)"
    description: "Red thumbtack mark sitting at the top-center of a post-it via ::before. Radial-gradient gives it a 3D bead-shaped highlight; inset shadow adds dimension. The default pin color."
  pin-blue:
    background: "radial-gradient(circle at 30% 30%, #4dabf7, #1864ab)"
    description: "Blue thumbtack variant."
  pin-green:
    background: "radial-gradient(circle at 30% 30%, #69db7c, #2f9e44)"
    description: "Green thumbtack variant."
  pin-gold:
    background: "radial-gradient(circle at 30% 30%, #ffd43b, #f59f00)"
    description: "Gold thumbtack variant."
  tape:
    width: 80px
    height: 25px
    position: "::after, top: -15px, centered, rotate(-2deg)"
    background: "rgba(255, 255, 255, 0.4)"
    border: "1px solid rgba(255, 255, 255, 0.3)"
    description: "Masking-tape mark across the top-center of a post-it via ::after. Translucent white, slightly rotated. Often combined with .pin so a single note has both tape and a tack."
  card-rotation:
    rotation: "±1° to ±15°"
    description: "Every post-it carries a small rotation. Statement and feature cards: ±1° to ±3°. Accent / floating notes: ±5° to ±15° (more dramatic to read as 'casually applied'). Rotations alternate direction across adjacent notes."
  feature-icon:
    width: 60px
    height: 60px
    border: "3px solid {colors.ink}"
    borderRadius: "50%"
    fontFamily: "'Shrikhand', cursive"
    fontSize: 1.5rem
    description: "Round ink-bordered icon containing a single character (letter, number, or symbol) in Shrikhand display. Used as a category marker at the top of feature post-its."
  versus-circle:
    width: 60px
    height: 60px
    background: "{colors.ink}"
    color: "{colors.paper}"
    borderRadius: "50%"
    fontFamily: "'Shrikhand', cursive"
    fontSize: 1.2rem
    boxShadow: "0 2px 8px {colors.shadow-deep}"
    description: "Ink-filled circle with cream text used between two compare-cards. Centered between the two cards with absolute positioning; reads as a 'vs' / 'and' connector."
  photo-frame:
    background: "#fff"
    padding: "1rem"
    boxShadow: "2px 3px 15px {colors.shadow}"
    rotation: "±1° to ±2°"
    description: "Polaroid-style image frame. White paper with 1rem padding around the inner image area; same drop shadow as post-its; small rotation. The inner image area has a 4:3 aspect ratio."
  chart-canvas:
    background: "#fff"
    padding: "2.5rem"
    boxShadow: "2px 3px 15px {colors.shadow}"
    rotation: "±1°"
    description: "White paper card hosting an inline SVG chart. Same drop shadow as post-its and photo-frames; small rotation. Charts use the post-it color palette for fills."
  stat-row:
    borderBottom: "1px dashed rgba(45, 42, 38, 0.2)"
    padding: "1rem 0"
    description: "A label-and-value row inside a stat post-it. Label in Zilla Slab body color; value in Shrikhand stat-value. Bottom-divider is a dashed ink-alpha hairline."
  doodle:
    opacity: 0.15
    stroke: "{colors.ink}"
    strokeWidth: 3
    description: "Decorative SVG mark placed absolutely in slide corners — a circle, squiggle, triangle, line, or X+ pair. All at 0.15 opacity, all in 3px ink stroke. Slides have 0–2 doodles each."
  timeline-connector:
    height: 60px
    pathStyle: "Q (quadratic) bezier curve at 0.3 opacity, stroke-dasharray '8 4', polygon arrowhead at end"
    description: "Dashed quadratic-bezier line between timeline nodes. Curve direction alternates row to row (concave up, concave down). Always ends with a triangle arrowhead."
  custom-cursor:
    cursor: "URL data-svg red-and-white thumbtack, 24×24, hotspot 12×12"
    description: "Browser cursor replaced with a tiny SVG thumbtack circle (red outer, white center) when hovering over any slide. Reinforces the 'pinning ideas to a board' metaphor."
---

## 概述

Scatterbrain 是一套**便利贴 + 软木板演示系统**。每一个内容块都是一张彩色便利贴（`{components.post-it}`），叠在三种纹理背景变体之一上——软木板、桌面纸，或暖色渐变——再用红 / 蓝 / 绿 / 金色图钉钉住，有时再盖一层半透明美纹纸胶带。视觉隐喻是完整的：整套幻灯片就是一面创意工坊墙、一块头脑风暴板，或一张思考者的书桌，内容就是钉在上面的那一簇便利贴。

字体栈把三套 Google Fonts 配上各自的情绪角色。**Shrikhand** 是展示声线——粗壮装饰展示衬线，曲线玩味、对比高。字重只用 400（仅有的字重），承担每一个标题、陈述、功能图标字形、统计数字和超大提引。它响亮、友善的个性是系统的主信号：读起来像手写马克笔，而不是排好的出版物。**Zilla Slab** 是正文书写——友善的现代粗衬线，人文主义比例。字重 300–700，用于正文段落、列表项和标签。它的 slab 衬线贴合 Shrikhand 的温暖手绘音域，却不抢注意力。**Caveat** 是手写脚本声线——随性草书。用于私人便条、旁注、label-script 眉题、统计分隔行里的俏皮话，以及任何应读作「用笔随手写在便利贴上」的时刻。

色彩哲学是**粉彩色便利贴色板，铺在有触感的纸面背景上**。七种便利贴颜色（`yellow`、`blue`、`pink`、`green`、`orange`、`purple`，外加描边的 `white`）提供分类变化；每种都有更深的兄弟色驱动 135° 渐变填充。墨色（`{colors.ink}` — #2d2a26）是偏暖的软炭黑，而不是纯黑，坐在暖粉彩上很舒服。三种背景变体——软木（`bg-cork`）、纸面（`bg-paper`）、暖色渐变（`bg-warm`）——让各页有触感变化，整套不会读成单调。粉彩够淡，墨色文字在每一种便利贴颜色上都可读，无需反相。

纵深来自**柔和投影 + 小幅旋转 + 分层触感元素**（图钉、胶带、涂鸦）。签名处理：每张便利贴都带一层柔和模糊投影（`2px 3px 15px {colors.shadow}`），暗示它略微离开表面，再加一个小旋转（±1° 到 ±15°），读起来像手贴上去的，而不是对齐到网格。可选图钉（红色图钉，经 `::before`）和胶带（半透明白，经 `::after`）增加触感层次，而不靠 box-shadow 花招。

**密度哲学：中等。** 每一页锚定 1–4 张便利贴，外加 1–2 个强调装饰（漂浮侧贴、涂鸦、装饰形状）。一页一张居中大便利贴读作宣言时刻；三张功能卡读作版式页；一张主便利贴加 2–4 张小漂浮强调贴读作 hero 铺陈。同时堆满互相重叠的便利贴，会把玩味能量压成混乱。正确密度是：便利贴够多，感觉像一次创意过程铺陈，又留够负空间把每张贴读清楚。

**关键特征：**
- 三种纹理背景变体：软木（`{components.bg-cork}`）、纸面（`{components.bg-paper}`）、暖色渐变（`{components.bg-warm}`）。每页选一种。
- 固定 SVG 颗粒叠层，4% 透明度，盖在全部内容之上，强化纸面音域。
- 七种便利贴颜色：黄、蓝、粉、绿、橙、紫、白描边。各自渐变填充（橙 / 紫 / 白除外）。
- 每张便利贴都带柔和投影 + 小幅旋转。相邻便利贴旋转方向交替。
- 红色图钉（以及蓝 / 绿 / 金变体）经 `::before`。美纹纸胶带经 `::after`。经常叠在同一张贴上。
- 展示标题用 Shrikhand（粗壮展示衬线）。正文用 Zilla Slab（友善 slab）。私人批注用 Caveat（随性脚本）。
- 装饰 SVG 涂鸦（圆、波浪线、三角、X 标记）住在幻灯片角落，透明度 0.15。
- 自定义图钉光标强化「把想法钉到板上」的隐喻。

## 色彩

### 色板

**便利贴颜色**（渐变填充或平涂）：
- **Yellow**（`{colors.yellow}` — #ffe066 → `{colors.yellow-deep}` — #ffd43b）：经典便利贴黄。最常见的贴色。系统的「默认」便利贴。
- **Blue**（`{colors.blue}` — #a5d8ff → `{colors.blue-deep}` — #74c0fc）：柔和天蓝。系统的「次级」便利贴。
- **Pink**（`{colors.pink}` — #ffc9c9 → `{colors.pink-deep}` — #ff9f9f）：柔和玫瑰粉。系统的「暖强调」便利贴。
- **Green**（`{colors.green}` — #b2f2bb → `{colors.green-deep}` — #8ce99a）：薄荷绿。系统的「冷强调」便利贴。
- **Orange**（`{colors.orange}` — #ffcc80）：暖桃橙。平涂，无渐变。用作第三档强调，增加变化。
- **Purple**（`{colors.purple}` — #d0bfff）：薰衣草紫。平涂，无渐变。用作第三档强调，增加变化。

**特殊贴色**：
- **White**（`#fff`）：描边白色便利贴，用于时间线和对比，需要「素」或「中性」贴时。永远带 2px 墨色描边，因为纯白否则会消失进奶油 / 纸面背景。

**纸面 / 表面色**：
- **Cream**（`{colors.cream}` — #faf8f3）：最浅的纸面变体。用在 `bg-paper` 和 `bg-warm` 背景渐变内部。
- **Paper**（`{colors.paper}` — #f7f5f0）：正文字面背景——坐在每一页后面，作为透过 bg 叠层可见的页面色。也用作深墨色表面上的反相文字色。

**墨色 / 文本色**：
- **Ink**（`{colors.ink}` — #2d2a26）：结构色。所有标题、所有正文、所有描边、所有涂鸦描边。比纯黑略软，换来温度。
- **Ink Light**（`{colors.ink-light}` — #5c5750）：次级文本色，用于正文段落、图注和弱化文字。

**阴影 token**：
- `{colors.shadow}`（rgba(45, 42, 38, 0.15)）：柔和投影——用在每一张便利贴上。
- `{colors.shadow-deep}`（rgba(45, 42, 38, 0.25)）：更强的接触阴影——用作便利贴投影的第二层。

### 默认值
- **默认表面背景**：每页在 `{components.bg-cork}` / `{components.bg-paper}` / `{components.bg-warm}` 中选一。软木是触感 / 「满墙便利贴」时刻的默认；纸面用于桌面 / 聚焦内容时刻；暖色渐变用于 hero / 氛围时刻。
- **默认便利贴颜色**：`{components.post-it-yellow}`——黄色是最常见的便利贴，读作系统基线。
- **默认标题色**：`{colors.ink}`（#2d2a26）——每张便利贴上的 Shrikhand 展示都用偏暖软炭黑。
- **默认正文字色**：段落正文用 `{colors.ink-light}`（#5c5750）；列表项和强调正文用 `{colors.ink}`。
- **默认描边色**：白色便利贴的 2px 描边和功能图标圆形描边用 `{colors.ink}`。大多数便利贴没有描边（渐变填充定义它们）。
- **默认图钉色**：`{components.pin}`（红）——系统的「默认」图钉。需要视觉变化时，用蓝 / 绿 / 金变体去贴合底下的便利贴颜色。
- **默认胶带**：用得克制——通常在 hero / 陈述便利贴上，让那张贴感觉「正式钉上去了」，图钉和一条胶带都有。
- **墨色表面上的默认文字色**：`{colors.paper}`（#f7f5f0）。
- **默认装饰涂鸦色**：`{colors.ink}`，透明度 0.15，3px 描边。

七种便利贴颜色**没有固定语义**——黄不是「警告」，绿不是「成功」。它们是分类色板，选择只信号「这簇里是哪一张」。为视觉变化循环颜色；把渐变填充贴（黄、蓝、粉、绿）和平涂贴（橙、紫）配对，换纹理变化。

## 字体排印

### 字体家族
系统有三套 Google Fonts，各自角色分明：

- **Shrikhand**（展示）：粗壮装饰展示衬线，笔画对比高，曲线玩味，手写马克笔感。单字重（400）。用于每一个展示时刻——标题、陈述、标题行、功能图标字形、统计数字、versus-circle 文字。它响亮的个性是系统的主身份；换成另一套展示衬线就会丢掉工坊声线。
- **Zilla Slab**（正文）：友善的现代粗衬线，人文主义温度。多字重（300–700，斜体变体 300 和 400）。正文段落默认字重 400，最轻图注 300，强调 500–700。slab 读起来像温暖的手，而不是机械。
- **Caveat**（手写脚本）：随性草书，多字重（400–700）。用于私人便条、旁注、label-script 眉题（全大写、0.15em tracking）、收场页署名，以及统计分隔行里的装饰俏皮话。

Zilla Slab 有斜体（300 和 400 italic），但很少用——强调来自换字重或换字体，不是斜体。不用下划线。

### 字号阶梯

| Token | 字号（clamp） | 字体 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.display-hero}` | 2.5–4.5rem | Shrikhand | 400 | 封面或收场超大标题 |
| `{typography.statement}` | 2–3.5rem | Shrikhand | 400 | 居中陈述或抽引 |
| `{typography.headline}` | 1.8–3rem | Shrikhand | 400 | 主幻灯片标题 / 章节标题 |
| `{typography.title}` | 1.3–1.8rem | Shrikhand | 400 | 子区域或卡片标题 |
| `{typography.caption-subtitle}` | 1.3rem | Zilla Slab | 400 | hero 标题下的幻灯片副标题 |
| `{typography.body}` | 1–1.25rem | Zilla Slab | 400 | 标准正文段落 |
| `{typography.list-item}` | 1.1rem | Zilla Slab | 400 | 项目符号 / 勾选列表行 |
| `{typography.handwritten}` | 1.2–1.6rem | Caveat | 400 | 装饰俏皮话、私人便条 |
| `{typography.handwritten-lg}` | 1.4–2rem | Caveat | 600 | 更大的手写副标题 |
| `{typography.handwritten-sm}` | 1.2–1.4rem | Caveat | 500 | 小强调标签 |
| `{typography.label-script}` | 0.9rem | Caveat | 400 | 加字距的全大写眉题标签 |
| `{typography.stat-value}` | 1.8rem | Shrikhand | 400 | 统计行里的数字值 |

### 默认值
- **主章节标题（便利贴内部）的默认字号**：`{typography.headline}`（1.8–3rem clamp），Shrikhand。
- **封面或收场超大标题的默认字号**：`{typography.display-hero}`（2.5–4.5rem clamp）。
- **居中宣言 / 抽引陈述的默认字号**：`{typography.statement}`（2–3.5rem clamp）。
- **正文段落的默认字号**：`{typography.body}`（1–1.25rem clamp），Zilla Slab 400。
- **列表行（项目符号、勾选或对比列表）的默认字号**：`{typography.list-item}`（1.1rem），Zilla Slab 400。
- **侧贴或俏皮话的默认字号**：`{typography.handwritten}`（1.2–1.6rem clamp），Caveat 400。
- **卡片标题上方眉题标签的默认字号**：`{typography.label-script}`（0.9rem），Caveat，全大写，0.15em tracking。
- **统计数字的默认字号**：`{typography.stat-value}`（1.8rem），Shrikhand。
- **Shrikhand 的默认字重**：400（仅有的字重）。
- **Zilla Slab 正文的默认字重**：400。强调正文：500–700。轻图注：300。
- **Caveat 的默认字重**：随性便条 400；强调 500–700。

拿不准卡片主文字该用 `{typography.headline}` 还是 `{typography.title}` 时：卡片是该页主导元素就用 `{typography.headline}`；它只是若干较小卡片之一就用 `{typography.title}`。

### 签名处理
这些处理在**使用对应元素类型时不可省略**：

- **每一个展示标题都用 Shrikhand。** 换成 Zilla Slab 或另一套展示面会丢掉工坊声线。即使功能卡里 1.3rem 的小标题也用 Shrikhand。
- **每一段正文和每一个列表项都用 Zilla Slab。** 用 Shrikhand 排正文会读成过度制作且不可读。
- **每一条随性 / 私人便条都用 Caveat。** 包括侧贴、装饰俏皮话（"Jot it down before you forget!"、"OK"、":)"），以及统计分隔行里的个人观察。换成斜体 Zilla 会丢掉手绘声线。
- **每一个 label-script 眉题都是全大写 + 0.15em tracking。** 正常 tracking 的 Caveat 读作正文草书；全大写 + tracking 才把它变成分类标签。
- **每一个功能图标圆形描边都是 3px 墨色，里面一个 Shrikhand 字形。** 变体（2px 描边、无衬线字形）会破坏图标的视觉签名。
- **每一张承载主标题的便利贴都经 `::before` 加一枚图钉。** 没有图钉的标题便利贴读起来像漂着、未定义。
- **每一张 hero / 陈述便利贴同时带图钉和一条胶带**（`.pin .tape` 类一起用）。这是系统对最强调那张贴的「正式钉贴」处理。

### 排印原则
系统的排印节奏来自**三面对比**：Shrikhand 展示（响亮、装饰、友善衬线）→ Zilla Slab 正文（稳定、可读、粗衬线）→ Caveat 手写脚本（私人、随性、草书）。只用一面的幻灯片读成单调；三面都用的幻灯片读成工坊正确。

行高：展示紧（1.1），正文宽（1.6–1.7），手写脚本中等（1.3–1.4）。展示字距略正（0.02em），给 Shrikhand 比默认多一点开阔；正文无 tracking；手写脚本标签带 0.15em 全大写 tracking。

## 版式

### 画布系统
系统目标是 `100vw × 100vh`。每个 `.slide` 绝对定位铺满视口，默认 `display: none`；`.active` 页是 `display: flex` 居中。导航由 JS 驱动：方向键、空格、PageUp/Down、Home/End、触摸滑动、鼠标滚轮（700ms 锁，防止连跳）。

### 幻灯片构图模式
系统支持若干构图模式，但不规定死版式：
- **居中单卡**：一张大便利贴（陈述、收场、RSVP 风格）。
- **2 列或 3 列网格**：对齐的便利贴网格，带小幅旋转。
- **图表 + 图例**：一侧白色图表卡，另一侧彩色便利贴图例。
- **图 + 文**：一侧拍立得风格相框，另一侧文字便利贴簇。
- **自由簇**：一张 hero 便利贴，周围 2–4 张小强调便利贴，旋转和位置各异。
- **时间线行**：交替左右节点 + 虚线曲线连接 + 每行一张内容卡。
- **对比**：两张便利贴并排，中间一枚居中墨色 versus-circle。

每一种模式里，单张便利贴都坐在三种背景纹理之一上，带小幅旋转，空角落有装饰涂鸦标记。

### 内边距阶梯
| Token | 值 | 用途 |
|---|---|---|
| `{spacing.slide-pad}` | 3rem | 幻灯片外边距 |
| `{spacing.post-it-pad-lg}` | 3rem 4rem | Hero / 标题便利贴内边距 |
| `{spacing.post-it-pad-statement}` | 3.5rem 4rem | 陈述便利贴内边距 |
| `{spacing.post-it-pad-md}` | 2.5rem | 标准便利贴内边距 |
| `{spacing.post-it-pad-sm}` | 1.5rem | 小强调便利贴内边距 |
| `{spacing.gap-lg}` | 3rem | 多列网格间距 |
| `{spacing.gap-md}` | 2.5rem | 功能网格间距 |
| `{spacing.gap-sm}` | 2rem | 时间线行间距 |

### 持久铬件
系统没有持久幻灯片铬件——没有进度条、没有页码、没有导航提示。自定义图钉光标是唯一持久视觉信号。导航纯靠键盘 / 滑动 / 滚轮。

## 纵深与层次

### 柔和投影（主手法）
系统定义纵深的处理是每张便利贴、相框、图表卡和 diagram-canvas 上的**柔和投影**：`2px 3px 15px {colors.shadow}, 0 1px 3px {colors.shadow-deep}`。15px 模糊的外阴影，水平 2px、垂直 3px 偏移，暗示便利贴略微悬在软木或纸面之上。1px 模糊、1px 垂直偏移的内层阴影补上底边接触阴影。合在一起读作「钉在板上、略微抬起的纸贴」。

这是**本库里唯一用柔和模糊阴影定义纵深的系统**——大多数其他模板禁止它们。Scatterbrain 拥抱它们，因为视觉隐喻依赖纸贴离开纹理表面的触感抬升。

### 旋转（次手法）
每张便利贴都带小幅旋转（±1° 到 ±15°）。Hero / 陈述 / 功能便利贴用小旋转（±1° 到 ±3°）；强调 / 漂浮 / 收场簇便利贴用更大旋转（±5° 到 ±15°）。相邻便利贴旋转方向交替，让这一簇读作随手贴上，而不是对齐到网格。

### 触感叠层（图钉 + 胶带）
单张便利贴上的可选分层标记提供额外纵深：
- **Pin**（`{components.pin}`）——16px 圆形红色图钉，经 `::before` 坐在贴的顶中。径向渐变高光 + 内阴影 + 投影让它读作 3D 珠。
- **Tape**（`{components.tape}`）——80×25px 半透明白胶带条，经 `::after` 坐在顶中，略旋转。

图钉和胶带可以叠在同一张贴上（`.pin.tape` 类对）。图钉颜色变体（`pin-blue`、`pin-green`、`pin-gold`）贴合底下贴色，保持视觉凝聚。

### 背景纹理（氛围层）
三种背景变体（`bg-cork`、`bg-paper`、`bg-warm`）和全视口颗粒叠层（`{components.grain-overlay}`，4% 透明度）提供基础纹理地面。没有背景变体，整套读成白底上漂浮的便利贴；有了它们，整套读成物理落在软木、桌面纸或晨光上。

## 形状与处理

### 圆角
| 值 | 用途 |
|---|---|
| 0px | 所有便利贴、图表卡、相框、diagram-canvas、对比卡 |
| 50%（圆） | 功能图标圆形描边、versus-circle、图钉 |
| 3px | 图表条形 `<rect>` 圆角（行内 SVG） |
| 自定义（无固定 token） | 相框内图区域跟随拍立得 4:3 画幅 |

大多数表面是严格矩形。圆形留给图标、图钉和 versus 标记。图表条形带轻微 3px 圆角（在 SVG 内），换友善感。

### 边框粗细
- **2px solid `{colors.ink}`** —— 用于白色便利贴描边和图表 SVG `<rect>` 描边。
- **3px solid `{colors.ink}`** —— 用于功能图标圆形描边和涂鸦 SVG 路径。
- **1px dashed rgba(ink, 0.2)** —— 用作统计行发丝分隔。
- **1px solid rgba(ink, 0.1)** —— 用作对比列表行分隔。

描边一律是墨色（暖炭黑）。不出现彩色描边。

### 装饰元素类型

**Post-it**（`{components.post-it}`）——七种变体之一的彩色便利贴（黄、蓝、粉、绿、橙、紫、描边白）。内边距来自 `{spacing.post-it-pad-*}` 阶梯。永远带柔和投影。几乎永远带小幅旋转。通常带图钉，有时带胶带。

**Pin**（`{components.pin}`）——红色图钉，经 `::before`。默认红色；变体蓝、绿、金。坐在贴的顶中。

**Tape**（`{components.tape}`）——半透明白美纹纸胶带标记，经 `::after` 坐在贴的顶中，略旋转。

**Feature icon**（`{components.feature-icon}`）——60px 圆形墨色描边圆，里面一个 Shrikhand 字形（单字符）。用在功能便利贴顶部作为分类标记。

**Versus circle**（`{components.versus-circle}`）——墨色填充圆，奶油色 Shrikhand 文字，绝对定位居中在两张对比便利贴之间。自带投影。

**Photo frame**（`{components.photo-frame}`）——拍立得风格白卡，内图区域四周 1rem 内边距，内图 4:3。投影与便利贴相同；小幅旋转。

**Chart canvas**（`{components.chart-canvas}`）——承载行内 SVG 图表的白卡。投影与便利贴相同；小幅旋转。SVG 图表用便利贴色板填色。坐标标签用 Zilla Slab；数值标签用 Caveat。

**Diagram canvas** —— 承载环形 / 饼图 SVG 的白卡。处理与 chart canvas 相同。SVG 扇区用便利贴色板；图例行用墨色文字。

**Stat row**（`{components.stat-row}`）——统计便利贴内的标签-值行。Zilla Slab 标签 + Shrikhand stat-value，用虚线墨色 alpha 底边分隔。

**Timeline node + connector** —— 每一时间线行：左侧便利贴（时间线节点，带 phase-label Caveat 图注）+ 中间虚线贝塞尔 SVG 连接 + 右侧白描边便利贴（时间线内容正文）。行方向交替（左/右），偶数行经 `flex-direction: row-reverse`。

**Doodle SVG**（`{components.doodle}`）——装饰 SVG 标记，绝对放在幻灯片角落：圆、波浪线、三角、线、X+ 对。3px 墨色描边，透明度 0.15。每页 0–2 个涂鸦。

**Custom cursor** —— SVG 图钉光标（外红圆心白）在悬停幻灯片时替换默认光标。

## 宜与忌

### 宜
- 每页选一种背景变体：`{components.bg-cork}` 给「满墙便利贴」能量，`{components.bg-paper}` 给「桌面」聚焦，`{components.bg-warm}` 给「晨光」氛围。各页变化，换触感多样性。
- 每页都保留 SVG 颗粒叠层（`{components.grain-overlay}`）在 4% 透明度。它是把整套钉在纸面音域上的纹理。
- 每一个展示时刻（标题、标题行、功能图标、统计数字）用 Shrikhand；每一段正文和每一个列表项用 Zilla Slab。
- 随性 / 私人便条用 Caveat——旁注、装饰俏皮话（"Jot it down before you forget!"、":)"），以及 label-script 眉题。手写脚本是系统最鲜明的声线。
- 给每张便利贴一个小旋转（±1° 到 ±15°）。相邻便利贴交替旋转方向；任何东西都不应对齐到网格。
- 把标准柔和投影（`2px 3px 15px shadow, 0 1px 3px shadow-deep`）应用到每一张便利贴、相框、图表卡和 diagram-canvas。
- 用红色图钉经 `::before` 钉住每一张主便利贴。便利贴颜色提示时，用颜色匹配的图钉变体（蓝 / 绿 / 金）。
- 在 hero / 陈述便利贴上组合图钉 + 胶带，做「正式钉贴」处理。
- 在幻灯片角落放小 SVG 涂鸦（圆、波浪线、三角），透明度 0.15，作为装饰标点。每页 1–2 个涂鸦就够。
- 多卡网格里循环便利贴颜色（黄 → 蓝 → 粉 → 绿 → 橙 → 紫）换视觉变化。不要所有卡片重复同一色。

### 忌
- 不要省略背景纹理，让便利贴漂在纯白视口上。纹理背景是系统的基础视觉地面。
- 不要用另一套展示面替换 Shrikhand。粗壮装饰衬线是系统身份；换成无衬线或另一套衬线会丢掉工坊声线。
- 不要用另一套脚本面替换 Caveat。随性草书声线锚定「手写涂鸦」音域。
- 不要用 Zilla Slab 做标题，或用 Shrikhand 做正文段落。配对是锁死的：Shrikhand 展示 + Zilla Slab 正文 + Caveat 脚本。
- 不要给便利贴颜色赋语义（黄 = 警告，绿 = 好）。颜色只是分类。
- 不要把便利贴旋转超过 ±15°。超过那个，手贴就变成歪了。
- 不要让每张便利贴朝同一方向旋转。相邻便利贴交替 ± 方向；整齐划一会读成整块画布歪了，而不是手贴。
- 不要用纯白做便利贴填充却不加 2px 墨色描边。白贴在奶油背景上会看不见。
- 不要省略标题便利贴上的图钉。没有图钉的标题读起来像漂着、未定义。
- 不要用互相重叠的便利贴挤满一页。便利贴堆起来，玩味能量就会塌掉；正确密度是 1–4 张主贴加 1–2 张小强调 / 漂浮贴。

## 响应式行为

系统目标是 `100vw × 100vh`，全程用 `clamp()` 做流体缩放。单一媒体查询在 `max-width: 900px` 把多列网格和时间线收到单列，中和部分旋转（versus-circle 变成行内而不是绝对定位），并把对比卡竖向堆叠。

### 缩放行为
- 展示标题经 `clamp(2.5rem, 5vw, 4.5rem)` 模式缩放——在最小与最大之间流体。
- 正文从最小 1rem 缩放到最大 1.25rem。
- 便利贴内边距不随视口缩放——固定在内边距阶梯的值。
- 投影、图钉尺寸、胶带尺寸和装饰 SVG 尺寸无论视口都固定。

### 演示操作
- 用 `ArrowRight`、`ArrowDown`、`Space` 或 `PageDown` 前进。
- 用 `ArrowLeft`、`ArrowUp` 或 `PageUp` 后退。
- `Home` 跳到第一页，`End` 跳到最后一页。
- 移动端触摸横滑前进 / 后退。
- 鼠标滚轮前进 / 后退，滚动之间锁 700ms，防止触控板上连跳。
- 自定义图钉光标在每一次悬停上强化隐喻。

### 打印行为
一条 `@media print` 规则给每页设 `page-break-after: always`，并设 `min-height: 100vh`。打印产出按页顺序的一页一幻灯片输出。

## 中日韩与多语言内容

### 推荐中文搭配

| 角色 | 西文 | 中文 | 字重映射 |
|---|---|---|---|
| Display / Headline / Statement / Title / Stat-value / Feature-icon glyph | Shrikhand (400) | **站酷快乐体 ZCOOL KuaiLe** | regular（单字重） |
| Body / List-item / Caption-subtitle | Zilla Slab (400) | **悠哉字体 Yozai** | regular |
| Hand-script (Caveat) — 仅西文 | Caveat (400 / 500 / 600) | *（无中日韩替代）* | n/a |

### 中西混排策略

**策略 A——展示用中日韩 + 正文用中日韩，各自有个性。** Scatterbrain 的整套音域是玩味-触感-温暖，中文搭配应落在同一情绪音域。**ZCOOL KuaiLe（站酷快乐体）** 是粗壮装饰展示面，圆润曲线、手绘马克笔感——它是最接近 Shrikhand 粗壮装饰衬线声线的中日韩匹配。两面都共享定义工坊板美学的「响亮而友善」个性。**Yozai（悠哉字体）** 是温暖圆润正文面，源自 M+ Rounded——它带着与 Zilla Slab 粗衬线相同的友善人文主义气质，软字端读起来像手写便条，而不是排好的文字。两套中日韩字体一起保住玩味-粗壮-展示 + 温暖-友善-正文的节奏，而这正是 Scatterbrain 声线成立的原因。

### 加载

```html
<link href="https://chinese-fonts-cdn.deno.dev/packages/zcool-kuaile/dist/ZCOOLKuaiLe-Regular/result.css" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/cn-fontsource-yozai-regular/font.css" rel="stylesheet">
```

然后把中日韩家族追加到相应字体栈：
```css
/* Display roles */
font-family: 'Shrikhand', 'ZCOOL KuaiLe', cursive;
/* Body roles */
font-family: 'Zilla Slab', 'Yozai', serif;
```

### 通用中日韩调整

- 行高：正文 1.75–1.85，展示 1.15–1.25
- 字距：中日韩为 0
- 大小写变换：中日韩不用 uppercase
- 全角标点
- 展示标题不加句号
- 盘古之白：写 `使用 Claude` 而不是 `使用Claude`
- 一句一字体

### 本系统审美说明

- **Shrikhand 展示上 0.02em 正 tracking，在 ZCOOL KuaiLe 上必须降到 0。** 加了 tracking 的中文展示字看起来是坏的。
- **展示行高应从 1.1 开到 1.2–1.3** 给 ZCOOL KuaiLe——圆润粗壮笔画需要更多纵向呼吸。
- **功能图标圆形描边配单个汉字**（新、巧、趣）放在 60px 圆里、用 ZCOOL KuaiLe，效果极好。粗壮展示字重让单字读作盖章式分类标记。
- **Versus circle 配短中文词**（对比、与）用较小展示字重也成立；奶油色压墨色的对比会带过去。
- **label-script Caveat 眉题（全大写、0.15em tracking）是最难翻译的。** 选项：（1）眉题保持西文（`CHAPTER ONE`、`THE SETUP`），保住手写脚本签名；（2）换成 0.9rem 的 Yozai 眉题，无 tracking、无 uppercase——这会丢掉分类标签的示能。选项（1）保住系统最鲜明的小声线，并且当西文眉题坐在中文标题上方时效果很好（整套读作中文文章配英文 kicker，这是常见编辑惯例）。
- **Caveat 里的私人便条 / 装饰俏皮话（`Jot it down before you forget!`、`:)`）应保持西文**——随性圆珠笔脚本没有可接受的中文替代。以中文为主的页上，把手写脚本时刻当作西文页边注；这实际上可以加深工坊声线（整套读作中文头脑风暴配英文旁白，对任何当代中文创意团队都说得通）。
- **便利贴图钉、胶带、投影、旋转、自定义光标、涂鸦 SVG、背景纹理** 都与字形无关——它们在中文内容后面同样好地承载玩味-触感系统。
- **统计行标签-值模式** 与中文标签（用户数量、转化率）用 Yozai、西文数字值用 ZCOOL KuaiLe 干净地成立。

### 已知中日韩缺口

Caveat——系统最鲜明的声线（锚定每一条私人便条的随性圆珠笔手写脚本）——没有中日韩等价物。有手写风格的中文网页字体（悠果手写体、站酷庆科黄油体），但随性草书手写的文化音域在西文与中日韩传统之间差得很远，没有任何中文字面会读作「和 Caveat 同一条声线」。推荐变通是：即使在其余都是中文的页上，也保留 Caveat 做西文页边批注——中文正文配英文手写的模式在当代中文编辑设计里很常见，读作地道，而不是翻译缺口。

## 迭代指南

1. 每一张新幻灯片选三种背景变体之一（`{components.bg-cork}`、`{components.bg-paper}`、`{components.bg-warm}`）。各页变化，换触感多样性。
2. 每一个新内容块都是七色之一的便利贴（黄、蓝、粉、绿、橙、紫、描边白）。黄色是默认；多卡变化时循环颜色。
3. 每一张新便利贴都带小幅旋转。Hero / 陈述便利贴：±1–3°。强调 / 漂浮便利贴：±5–15°。相邻交替方向。
4. 每一张新便利贴都带标准柔和投影（`2px 3px 15px shadow, 0 1px 3px shadow-deep`）。
5. 每一张新的主便利贴都经 `::before` 带图钉（默认红；蓝 / 绿 / 金变体做颜色凝聚）。
6. Hero / 陈述 / 收场便利贴经 `::after` 加一条胶带，做「正式钉贴」处理。
7. 标题用 Shrikhand，字号从 `{typography.title}`（1.3rem）的小卡片标题到 `{typography.display-hero}`（4.5rem）的封面 / 收场。正文用 Zilla Slab。私人便条用 Caveat。
8. 功能便利贴以 60px 圆形墨色描边功能图标开场，里面一个 Shrikhand 字符（A/B/C、1/2/3、!/✓/✗）。
9. 装饰 SVG 涂鸦（圆、波浪线、三角、X 标记）住在每页 1–2 个空角落，透明度 0.15，3px 墨色描边。
10. 图表和 diagram 坐在白色 chart-canvas（`{components.chart-canvas}`）里，投影 + 小幅旋转与便利贴相同。SVG 填充用便利贴色板（黄、蓝、粉、绿）。

## 已知缺口

- 系统加载三套 Google Fonts（Shrikhand、Zilla Slab、Caveat）。Shrikhand 是单字重（仅 400）；试图用更重字重会回退。生产环境建议自托管。
- 自定义 SVG 图钉光标（`{components.custom-cursor}`）在各浏览器上渲染并不完全相同——Safari 和 Firefox 可能比 Chrome 缩放或定位光标热点不同。纯触摸设备上光标无关。
- 背景纹理（`bg-cork`、`bg-paper`、`bg-warm`）用 CSS 渐变与行内 SVG data-URI 图案的组合。现代浏览器渲染一致，但色调温度会随屏幕色彩配置略有变化。
- 图钉（`::before`）和胶带（`::after`）占满一张便利贴的两个伪元素槽。如果还需要额外装饰标记（卷角、污渍等），就得用真正的子元素，而不是伪元素。
- 每张便利贴上的柔和投影增加渲染开销。10+ 张便利贴的页在低端设备上可能出现轻微阴影渲染延迟。
- 自定义光标和绝对定位的图钉 / 胶带不会按预期与屏幕阅读器交互。装饰元素应对辅助技术保持隐藏。
- 行内 SVG 图表（柱、环、饼）是硬编码的——柱高、扇区路径和标签烤进 SVG。没有数据绑定层；新图表数值需要手工重算 SVG 路径 / 位置。
- 自定义光标（红色图钉）出现在每一页，包括文字很重的页，用户读正文段落时可能视觉嘈杂。把光标当作整套强调，而不是按页交互提示。
- 鼠标滚轮导航锁（700ms）不寻常，可能让期待平滑滚动的用户吃惊。尤其触控板用户可能觉得滚轮步进行为反直觉。
