---
version: alpha
name: Bold Poster
description: "A populist editorial poster system that mashes vintage Italian sports-magazine display lettering with classical serif body and tight monospace metadata. The display face is Shrikhand — a heavy slab/script hybrid with playful italic personality — rendered at poster scale (often 200-320px) and routinely tilted off-axis. Body runs Libre Baskerville for a literary editorial register; Space Grotesk handles tiny uppercase labels and chrome. The palette is uncompromising: white canvas, deep brown-black ink (#1C1410), single saturated tomato red (#D8000F), and a warm off-white (#F5F2EF) for alternating panels. Borders are bold 1.5-3px ink rules; the only shadow is a single stacked offset behind red display text. The aesthetic is loud, confident, and unmistakably print-poster — closer to a 1970s European brand annual report or a wine merchant's catalogue than a contemporary slide deck."

colors:
  bg: "#FFFFFF"
  dark: "#1C1410"
  red: "#D8000F"
  light: "#F5F2EF"

typography:
  hero-title:
    fontFamily: "'Shrikhand', cursive"
    fontWeight: 400
    fontSize: "clamp(72px, 16vw, 220px)"
    lineHeight: 0.88
    letterSpacing: 1px
    color: "{colors.dark}"
  hero-title-red:
    fontFamily: "'Shrikhand', cursive"
    fontWeight: 400
    fontSize: "clamp(84px, 18vw, 260px)"
    lineHeight: 0.85
    color: "{colors.red}"
    transform: "rotate(-4deg)"
  hero-title-bottom:
    fontFamily: "'Shrikhand', cursive"
    fontWeight: 400
    fontSize: "clamp(64px, 14vw, 200px)"
    lineHeight: 0.9
    color: "{colors.dark}"
    transform: "rotate(2deg)"
  close-big:
    fontFamily: "'Shrikhand', cursive"
    fontWeight: 400
    fontSize: "clamp(80px, 18vw, 260px)"
    lineHeight: 0.88
    color: "{colors.red}"
    transform: "rotate(-5deg)"
  stat-big:
    fontFamily: "'Shrikhand', cursive"
    fontWeight: 400
    fontSize: "clamp(120px, 26vw, 320px)"
    lineHeight: 0.82
    color: "{colors.red}"
    transform: "rotate(-6deg)"
  red-quote:
    fontFamily: "'Shrikhand', cursive"
    fontWeight: 400
    fontSize: "clamp(32px, 7vw, 90px)"
    lineHeight: 1.15
    color: "{colors.bg}"
    textShadow: "2px 2px 0 rgba(28,20,16,0.25), 4px 4px 0 rgba(28,20,16,0.2), 6px 6px 0 rgba(28,20,16,0.15)"
  section-header:
    fontFamily: "'Shrikhand', cursive"
    fontWeight: 400
    fontSize: "clamp(32px, 5vw, 64px)"
    lineHeight: 1
    color: "{colors.dark}"
  section-header-lg:
    fontFamily: "'Shrikhand', cursive"
    fontWeight: 400
    fontSize: "clamp(36px, 6vw, 72px)"
    lineHeight: 1
    color: "{colors.dark}"
  cell-number-lg:
    fontFamily: "'Shrikhand', cursive"
    fontWeight: 400
    fontSize: "clamp(28px, 3.5vw, 52px)"
    lineHeight: 1
    color: "{colors.red}"
  cell-number-md:
    fontFamily: "'Shrikhand', cursive"
    fontWeight: 400
    fontSize: "clamp(28px, 3.5vw, 48px)"
    lineHeight: 1
    color: "{colors.red}"
  card-title:
    fontFamily: "'Shrikhand', cursive"
    fontWeight: 400
    fontSize: "clamp(22px, 3vw, 36px)"
    lineHeight: 1.1
    color: "{colors.dark}"
  card-title-sm:
    fontFamily: "'Shrikhand', cursive"
    fontWeight: 400
    fontSize: "clamp(20px, 2.5vw, 32px)"
    lineHeight: 1.1
    color: "{colors.dark}"
  pillar-num:
    fontFamily: "'Shrikhand', cursive"
    fontWeight: 400
    fontSize: "clamp(36px, 5vw, 64px)"
    lineHeight: 1
    color: "{colors.red}"
  pillar-title:
    fontFamily: "'Shrikhand', cursive"
    fontWeight: 400
    fontSize: "clamp(18px, 2.2vw, 28px)"
    lineHeight: 1.15
    color: "{colors.dark}"
  stat-item-num:
    fontFamily: "'Shrikhand', cursive"
    fontWeight: 400
    fontSize: "clamp(28px, 4vw, 56px)"
    lineHeight: 1
    color: "{colors.dark}"
  roadmap-title:
    fontFamily: "'Shrikhand', cursive"
    fontWeight: 400
    fontSize: "clamp(18px, 2.5vw, 32px)"
    lineHeight: 1.1
  inline-stat:
    fontFamily: "'Shrikhand', cursive"
    fontWeight: 400
    fontSize: "clamp(18px, 2vw, 28px)"
    lineHeight: 1
    color: "{colors.red}"
  body:
    fontFamily: "'Libre Baskerville', serif"
    fontWeight: 400
    fontSize: "clamp(13px, 1.2vw, 16px)"
    lineHeight: 1.75
    color: "{colors.dark}"
  body-card:
    fontFamily: "'Libre Baskerville', serif"
    fontWeight: 400
    fontSize: "clamp(12px, 1.1vw, 14px)"
    lineHeight: 1.6
    color: "{colors.dark}"
  body-cell:
    fontFamily: "'Libre Baskerville', serif"
    fontWeight: 400
    fontSize: "clamp(11px, 1vw, 13px)"
    lineHeight: 1.55
    color: "{colors.dark}"
  body-small:
    fontFamily: "'Libre Baskerville', serif"
    fontWeight: 400
    fontSize: "clamp(11px, 1vw, 13px)"
    lineHeight: 1.5
    color: "{colors.dark}"
  hero-meta:
    fontFamily: "'Libre Baskerville', serif"
    fontWeight: 400
    fontSize: "clamp(11px, 1vw, 14px)"
    lineHeight: 1.5
    color: "{colors.dark}"
  tag-body:
    fontFamily: "'Libre Baskerville', serif"
    fontWeight: 400
    fontSize: "clamp(13px, 1.2vw, 16px)"
    lineHeight: 1.6
    color: "{colors.dark}"
  red-cite:
    fontFamily: "'Libre Baskerville', serif"
    fontWeight: 400
    fontSize: "clamp(13px, 1.3vw, 16px)"
    lineHeight: 1.5
    color: "{colors.bg}"
  close-sub:
    fontFamily: "'Libre Baskerville', serif"
    fontWeight: 400
    fontSize: "clamp(14px, 1.5vw, 18px)"
    lineHeight: 1.6
    color: "{colors.dark}"
  label:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 600
    fontSize: 10px
    letterSpacing: 2px
    textTransform: uppercase
    color: "{colors.dark}"
  label-red:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 600
    fontSize: 10px
    letterSpacing: 2px
    textTransform: uppercase
    color: "{colors.red}"
  rm-label:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 600
    fontSize: 9px
    letterSpacing: 3px
    textTransform: uppercase
    color: "{colors.red}"
  tag-label:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 600
    fontSize: "clamp(10px, 0.9vw, 12px)"
    letterSpacing: 3px
    textTransform: uppercase
    color: "{colors.red}"
  bullet-body:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 400
    fontSize: "clamp(10px, 0.9vw, 12px)"
    lineHeight: 1.45
    color: "{colors.dark}"
  counter:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 600
    fontSize: 11px
    lineHeight: 1
    letterSpacing: 2px
    textTransform: uppercase
    color: "{colors.dark}"
  link:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 600
    fontSize: "clamp(10px, 0.9vw, 12px)"
    letterSpacing: 2px
    textTransform: uppercase
    color: "{colors.dark}"
  fc-micro:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 400
    fontSize: 10px
    lineHeight: 1.4
    color: "{colors.dark}"

spacing:
  pad-slide: "48px 56px"
  pad-cell: "22px 20px"
  pad-cell-sm: "20px 24px"
  pad-pillar: "32px 24px"
  pad-card: "24px"
  pad-roadmap: "40px 48px"
  gap-grid-md: "24px 32px"
  gap-grid-roadmap: "28px 36px"
  gap-grid-stats: "48px"
  gap-stat-row: "20px"
  pad-bottom-clearance: "40px"
  max-width-content: 1100px
  max-width-services: 1000px

canvas:
  width: 100vw
  height: 100vh
  background: "{colors.bg}"

components:
  progress-bar:
    position: "fixed, bottom 0 left 0"
    height: 5px
    background: "{colors.red}"
    description: "Persistent thick red progress strip at the bottom of the viewport. Width grows linearly with slide index. The system's most prominent piece of chrome."
  counter:
    position: "fixed, bottom 18px right 24px"
    color: "{colors.dark}"
    opacity: 0.5
    fontFamily: "'Space Grotesk', sans-serif"
    fontSize: 11px
    letterSpacing: 2px
    description: "Persistent slide counter NN / NN at 50% opacity in Space Grotesk uppercase."
  hint-pill:
    position: "fixed, bottom 18px center"
    background: "{colors.light}"
    padding: "6px 14px"
    borderRadius: 4px
    fontSize: 10px
    opacity: 0
    description: "Bottom-center hint pill that fades to 50% opacity on body hover. Subtle wayfinding only."
  section-bordered-grid:
    border: "3px solid {colors.dark}"
    description: "Heavy 3px ink border enclosing a grid of cells. Each child cell carries a 1.5px ink inner border, producing a hairline-on-heavy double-border tabular grid. Used for financial-figure and summary-highlight grids."
  cell-bordered:
    border: "1.5px solid {colors.dark}"
    padding: "22px 20px"
    description: "Tabular cell with 1.5px ink border. Lives inside a 3px-bordered parent grid; the two border weights touch to produce the system's signature grid-with-double-edge."
  red-leftbar-card:
    borderLeft: "4px solid {colors.red}"
    paddingLeft: 18px
    description: "Service or content card marked by a 4px solid red left rule and 18px left padding. The system's editorial card pattern — no outline, just the red rule signaling the start of a block."
  red-leftbar-card-thin:
    borderLeft: "3px solid {colors.red}"
    paddingLeft: 16px
    description: "Thinner variant of the red-leftbar card used on dark surfaces (roadmap phases). Same pattern, scaled-down rule weight."
  bullet-em-dash:
    glyph: "—"
    color: "{colors.red}"
    fontWeight: 700
    paddingLeft: 14px
    description: "List bullet using a red em-dash (—) glyph in place of a disc. The dash sits at position absolute left and the body text indents to clear it."
  bullet-bullet:
    glyph: "•"
    color: "{colors.red}"
    paddingLeft: 12px
    description: "List bullet using a red round bullet (•) glyph. Same indent pattern as the em-dash variant."
  pillar-panel:
    flex: 1
    padding: "32px 24px"
    borderRight: "3px solid {colors.dark}"
    description: "Vertical column panel inside a multi-pillar layout. Each pillar separated by a 3px ink vertical rule. Alternating panels swap background from {colors.bg} to {colors.light} for striping."
  pillar-bullet-row:
    padding: "5px 0"
    borderBottom: "1px solid rgba(28, 20, 16, 0.08)"
    description: "Bullet row inside a pillar with a hairline-soft bottom border (ink at 8%) separating items. The last item drops the border."
  global-card:
    border: "2px solid {colors.dark}"
    padding: 24px
    description: "Bordered information card with 2px ink outline. Used on the global presence layout. Heavier than the leftbar pattern, more contained."
  stacked-text-shadow:
    textShadow: "2px 2px 0 rgba(28,20,16,0.25), 4px 4px 0 rgba(28,20,16,0.2), 6px 6px 0 rgba(28,20,16,0.15)"
    description: "Three-step decreasing-opacity stacked offset shadow in ink. Applied only to large red display text on red panels. The system's only shadow treatment."
  red-panel:
    background: "{colors.red}"
    color: "{colors.bg}"
    description: "Full-bleed saturated red panel surface. Carries white text with the stacked-text-shadow treatment on display."
  dark-panel:
    background: "{colors.dark}"
    color: "{colors.bg}"
    description: "Full-bleed deep brown-black panel surface. Carries white text and red accents (left bars, mono labels)."
  link-underline:
    color: "{colors.dark}"
    borderBottom: "2px solid {colors.red}"
    paddingBottom: 4px
    description: "Footer link style — Space Grotesk uppercase with a 2px red underline. Hover swaps text color to red."
  hero-title-stack:
    description: "A three-line stacked title where each line is a Shrikhand display element at a slightly different size. Two of the three lines carry rotation transforms (-4deg, +2deg) and one is set in red. The composition is the system's signature opener."
---

## frontend-slides 固定舞台策略

当 `frontend-slides` skill 使用本设计系统时，把最终幻灯片组生成为 **固定 1920×1080 舞台**，相对浏览器视口均匀缩放。幻灯片组应在每一块屏幕上（包括手机）保持 16:9 幻灯片画布；可以 letterbox 或 pillarbox，但不应为移动端重排幻灯片内容。

本策略优先于本文件后文描述的任何源模板响应式行为。如果后面某一节说原模板是视口流体的，只把它当作源历史，而不是 `frontend-slides` 的目标生成模型。

即使源模板原本用视口流体 CSS 实现，例如 `100vw`、`100vh`、`vw`、`vh` 或 `clamp()`，本策略仍然适用。把那些值当作要翻译进 1920×1080 舞台坐标的设计比例，而不是生成幻灯片组里的实时响应式规则。

最终输出使用 `deck-stage.js` 或等效的行内舞台缩放器：每页渲染为 1920×1080，用一次 transform 缩放整座舞台，并核验渲染截图是否同时存在文字溢出和面板重叠。


## 概览

Bold Poster 是一套**民粹编辑海报系统**，视觉词汇取自复古意大利体育杂志、世纪中欧洲品牌年报，以及酒商图录。前提是每一页都应感觉印出来的——设在重展示字体上，锁在一种强红强调上，白或灰白纸上，网格用墨画线，装饰严格最少。

字体系统是三套面孔、角色很紧。**Shrikhand**（Google Fonts）是展示脸——重 slab/手写混合，带好玩的斜体性格、窄开口，鲜明的意大利体育手写个性。用在海报级（常常 100–320px），几乎总带好玩的旋转（-6° 到 +2°），Shrikhand 承担每一个 hero 标题、每一个章节页头、每一个统计数字、每一个卡片标题。**Libre Baskerville**（Google Fonts）是正文字——古典文学衬线，笔画对比强，把系统锚定在编辑语域。11–16px、行高 1.5–1.75、深墨，Libre Baskerville 才让系统感觉印出来而不是数字的。**Space Grotesk**（Google Fonts）是 chrome 脸——专用于小全大写标签（9–12px，2–3px 字距）、卡内项目正文、幻灯片计数器和页脚链接。Space Grotesk 处理是系统的「元数据」声线。

色彩哲学是**毫不妥协的克制**：白画布、深棕黑墨（`{colors.dark}` — `#1C1410`）、单一饱和番茄红（`{colors.red}` — `#D8000F`），以及用于交替面板的暖灰白（`{colors.light}` — `#F5F2EF`）。没有第二品牌色，没有渐变（叠文字阴影内部除外），没有着色，没有语义状态色。每一个数字呼出、每一条活动线、每一个 CTA、每一个强调瞬间都是红——红只留给这些瞬间（从不用作正文，从不用作没有字压在上面的卡填充，从不用作着色）。

纵深是**结构的，不是大气的**。除红面板上红展示文字上的单一叠文字阴影（三步 2/2、4/4、6/6，递减不透明度墨）外，系统没有投影。其余纵深来自重描边：表格式网格上 3px 墨轮廓、单元格上 1.5–2px 墨描边、编辑卡上 4px 红左边线、项目之间 1px 发丝线。双描边处理（外 3px + 内 1.5px）是系统的签名表格式模式——它产出定义外观的印刷新闻纸质感。

**密度哲学：高——民粹而塞满。** 幻灯片密时系统读起来权威，稀时读起来怯。路线图、支柱和财务页常常承载 3–6 个不同单元格，内含正文段、项目列表和表格式数据——读起来有能量，不挤。反过来，hero、收束和陈述页故意降到一两个巨大展示元素加大量负空间——极低和极高密度两极都是有意的。典型内容页承载一条章节页头 + 3–6 个单元格的网格，每个单元格装着红数字/标题 + 一段 Libre Baskerville 正文 + 3–6 条 Space Grotesk 等宽项目。典型陈述页承载一个旋转红 Shrikhand 元素占画布一半，下面一句标语。

**关键特征：**
- 白（`{colors.bg}`）画布与灰白（`{colors.light}`）面板交替做条纹，外加深色（`{colors.dark}`）和红（`{colors.red}`）全出血面板表面做陈述瞬间。
- 单一番茄红（`{colors.red}`）作为唯一强调——用于每一个数字、每一条章节线、每一个标签、每一条左边标记。
- 三字体栈：Shrikhand（展示 + 数字）、Libre Baskerville（正文）、Space Grotesk（等宽标签 + 项目 + chrome）。
- 展示 Shrikhand 常常倾斜（-6° 到 +2°）——旋转是系统的签名动作。
- 重墨描边：表格式网格容器 3px，单元格 1.5–2px，编辑 leftbar 卡 4px 红，项目行之间 1px 发丝。
- 叠文字阴影（三步 2/2、4/4、6/6，递减墨不透明度）用在红展示元素上——系统里唯一的阴影。
- 每一页底边持续红进度条（5px 厚）。
- 列表标记用红 em-dash 和项目符号字形——从不用默认圆点。
- Hero 构图叠三行不同尺寸的 Shrikhand，至少一行红、至少一行倾斜。
- 页脚链接用 Space Grotesk 全大写加 2px 红下划线。

## 颜色

### 色板

- **Bg**（`{colors.bg}` — `#FFFFFF`）：纯白画布。多数表面的默认底。读起来像新鲜新闻纸。
- **Dark**（`{colors.dark}` — `#1C1410`）：带暖偏的深棕黑——不是纯黑。用于每一行正文、每一条描边、每一个 Space Grotesk 标签、每一段 Libre Baskerville，以及路线图级表面上的全出血面板底。暖意把它与通用编辑黑区分开。
- **Red**（`{colors.red}` — `#D8000F`）：饱和番茄红。系统的单一强调。用于每一个数字（红 Shrikhand 数字是最常见元素）、每一条章节 eyebrow 标签、编辑卡上的每一条 leftbar 线、每一个列表项目字形、每一条页脚下划线、持续进度条，以及陈述级表面上的全出血面板底。从不用作正文字色，从不用作着色，从不用作没有叠字的卡填充。
- **Light**（`{colors.light}` — `#F5F2EF`）：暖灰白。用于支柱布局内交替面板背景（每隔一根支柱换成灰白做垂直条纹），以及 hint-pill chrome 的背景。比白画布略暖——在不打断印刷纸语域的情况下创造表面分化。

### 默认

- **默认表面背景**：`{colors.bg}`（白）。陈述瞬间切到 `{colors.red}`（全出血红面板）。路线图级瞬间切到 `{colors.dark}`。支柱布局内条纹则交替 `{colors.bg}` 和 `{colors.light}`。
- **白表面上的默认标题 / 展示色**：主标题用 `{colors.dark}`，数字和统计级展示元素用 `{colors.red}`。
- **红面板上的默认标题色**：`{colors.bg}`（白），配叠文字阴影处理。
- **深色面板上的默认标题色**：`{colors.bg}`（白）。数字强调仍是 `{colors.red}`。
- **默认正文字色**：白/浅表面上 `{colors.dark}`，深/红表面上 `{colors.bg}`（白），第三级内容不透明度 0.5–0.8。
- **默认 eyebrow / 标签色**：白表面上 `{colors.red}`（红 Space Grotesk 全大写，2–3px 字距），网格内更小单元格标签用 `{colors.dark}`。
- **默认 leftbar 线色**：`{colors.red}`。4px（深色表面上 3px）红左边线是编辑卡签名。
- **单元格和网格的默认描边色**：`{colors.dark}`。没有彩色单元格描边。
- **默认项目字形色**：`{colors.red}`。本系统不存在默认圆点项目；每一份列表都用红 em-dash 或红圆点字形。

系统 **硬** 承诺四色色板。不要引入第五色（正向绿、信息蓝、高亮黄）。全部强调靠红，全部正文是浅底深字，全部反色是红上白或深上白。类别分化来自位置、标签和倾斜——从不来自颜色。

## 字体

### 字族
系统跑三套面孔，每套紧绑角色。

**Shrikhand**（Google Fonts）是展示 + 数字脸。单字重（400）重 slab-手写，带好玩的斜切形态和窄开口——读起来既旧世界（明信片手写）又当代（可变字重数字展示）。从 18px（行内统计）到 320px（hero 统计）每一个尺度都用。永远字重 400（这张脸没有其他字重）。旋转是这张脸声线的一部分——每页多个 Shrikhand 元素带着从 -6° 到 +2° 的变换。

**Libre Baskerville**（Google Fonts，400 / 700 + 斜体）是正文字。古典文学衬线，高笔画对比——用于每一段、每一个正文单元格、每一条元数据行、每一条 cite、每一条 close-sub。11–16px、行高 1.5–1.75，这张脸读起来舒适地编辑。斜体和粗体字重已加载但很少用——斜体存在于行内强调，粗体字重 700 很少需要，因为 Shrikhand 已经承担全部重展示工作。

**Space Grotesk**（Google Fonts，字重 400–700）是元数据 + chrome 脸。9–12px 全大写、2–3px 字距，用于标签、eyebrow、幻灯片计数器、链接文字、卡片项目正文（不用 Libre Baskerville 时），以及进度 chrome。宽字距全大写处理是系统的「盖章元数据」声线。

角色不重叠：Shrikhand 处理每一个展示瞬间和每一个数字；Libre Baskerville 处理每一段正文和编辑文字；Space Grotesk 处理每一个全大写标签、项目和 chrome 元素。不要越界——Shrikhand 正文会不可读；Libre Baskerville 标签会像书脚注；Space Grotesk 标题会感觉像科技创业。

### 字号阶梯

| Token | 字号 (clamp / px) | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.stat-big}` | 120–320px clamp | Shrikhand | 400 | Hero 级统计数字（永远旋转 -6°，永远红） |
| `{typography.hero-title-red}` | 84–260px clamp | Shrikhand | 400 | 多行 hero 栈里的红词（永远旋转 -4°） |
| `{typography.close-big}` | 80–260px clamp | Shrikhand | 400 | 收束陈述标题（永远旋转 -5°，永远红） |
| `{typography.hero-title}` | 72–220px clamp | Shrikhand | 400 | Hero 栈顶行（默认不旋转） |
| `{typography.hero-title-bottom}` | 64–200px clamp | Shrikhand | 400 | Hero 栈底行（永远旋转 +2°） |
| `{typography.section-header-lg}` | 36–72px clamp | Shrikhand | 400 | 财务 / 密数据页的大章节页头 |
| `{typography.section-header}` | 32–64px clamp | Shrikhand | 400 | 标准章节页头（摘要、服务、全球、收束） |
| `{typography.pillar-num}` | 36–64px clamp | Shrikhand | 400 | 支柱面板顶上的数字（红） |
| `{typography.cell-number-lg}` / `{typography.cell-number-md}` | 28–52px clamp | Shrikhand | 400 | 表格式单元格数字（永远红） |
| `{typography.stat-item-num}` | 28–56px clamp | Shrikhand | 400 | 行内补充统计数字（深色） |
| `{typography.card-title}` | 22–36px clamp | Shrikhand | 400 | 服务卡标题或全球卡标题 |
| `{typography.card-title-sm}` | 20–32px clamp | Shrikhand | 400 | 更小卡片标题（全球卡） |
| `{typography.pillar-title}` | 18–28px clamp | Shrikhand | 400 | 支柱面板标题 |
| `{typography.roadmap-title}` | 18–32px clamp | Shrikhand | 400 | 路线图阶段标题（深色表面上的白） |
| `{typography.red-quote}` | 32–90px clamp | Shrikhand | 400 | 红面板上的引文正文（白字 + 叠阴影） |
| `{typography.inline-stat}` | 18–28px clamp | Shrikhand | 400 | 正文块内的行内迷你统计数字（红） |
| `{typography.body}` | 13–16px clamp | Libre Baskerville | 400 | 标准正文段落 |
| `{typography.body-card}` | 12–14px clamp | Libre Baskerville | 400 | 服务/全球卡内正文 |
| `{typography.body-cell}` | 11–13px clamp | Libre Baskerville | 400 | 网格内表格式单元格正文 |
| `{typography.body-small}` | 11–13px clamp | Libre Baskerville | 400 | 摘要高亮的小正文 |
| `{typography.hero-meta}` | 11–14px clamp | Libre Baskerville | 400 | 标题栈上方的 hero 元信息行 |
| `{typography.red-cite}` | 13–16px clamp | Libre Baskerville | 400 | 红面板引文下的引用（白字） |
| `{typography.close-sub}` | 14–18px clamp | Libre Baskerville | 400 | 收束标题下的副标题 / 联系行 |
| `{typography.label-red}` / `{typography.tag-label}` | 10–12px | Space Grotesk | 600 | 章节标签（全大写，2–3px 字距，红） |
| `{typography.label}` | 10px | Space Grotesk | 600 | 网格内单元格标签（全大写，2px 字距，深） |
| `{typography.rm-label}` | 9px | Space Grotesk | 600 | 路线图阶段标签（全大写，3px 字距，红） |
| `{typography.bullet-body}` | 10–12px clamp | Space Grotesk | 400 | 卡和支柱内的列表项目正文 |
| `{typography.counter}` | 11px | Space Grotesk | 600 | 持续幻灯片计数器 |
| `{typography.link}` | 10–12px clamp | Space Grotesk | 600 | 页脚 / 收束链接文字（全大写，2px 字距） |
| `{typography.fc-micro}` | 10px | Space Grotesk | 400 | 表格式单元格底部的微小语境行 |

### 默认

- **Hero 或封面标题的默认字号**：栈顶用 `{typography.hero-title}`（72–220px），第二行配 `{typography.hero-title-red}`（84–260px，红，旋转 -4°），第三行配 `{typography.hero-title-bottom}`（64–200px，旋转 +2°）。三行叠构图是系统的标准 hero 模式。
- **主章节标题的默认字号**：`{typography.section-header}`（32–64px）。永远 Shrikhand。
- **Hero 级统计的默认字号**：`{typography.stat-big}`（120–320px）旋转 -6°，永远红。
- **表格式单元格数字的默认字号**：`{typography.cell-number-md}`（28–52px），红。
- **正文的默认字号**：`{typography.body}`（13–16px）Libre Baskerville，行高 1.75。
- **卡片正文的默认字号**：`{typography.body-card}`（12–14px），行高 1.6。
- **章节 eyebrow 标签的默认字号**：`{typography.tag-label}`（10–12px）Space Grotesk 字重 600，红，全大写，2–3px 字距。
- **列表项目正文的默认字号**：`{typography.bullet-body}`（10–12px）Space Grotesk 字重 400。
- **Shrikhand 的默认字重**：400 ——这张脸没有其他字重。
- **Libre Baskerville 正文的默认字重**：400。粗体（700）只用于正文段落内的行内强调。
- **Space Grotesk 标签的默认字重**：600。宽字距是系统的标签声线；字重 400 只用于项目正文。

拿不准该用哪个展示 token 时，主幻灯片章节开场默认 `{typography.section-header}`（32–64px）。把 `{typography.stat-big}` 留给 hero 统计瞬间，把 `{typography.hero-title}` 三件套留给封面级表面。

### 招牌处理

这些处理在**使用对应元素类型时不可省略**：

- **每一个 hero 级 Shrikhand 元素都是多行叠构图的一部分，至少一行旋转、至少一行红。** 没有旋转或色彩对比的单行 Shrikhand hero 标题会塌成通用展示瞬间。
- **每一个表格式数字单元格数字都是 cell-number 级（28–52px）的 Shrikhand，`{colors.red}`。** 深色文字的数字单元格会打断系统层级——红才是数据信号。
- **每一条章节 eyebrow 都是 Space Grotesk 字重 600、`{colors.red}`、全大写、2–3px 字距。** 没有例外。任何其他字距、字重、颜色或大小写的 eyebrow 都不是系统的 eyebrow。
- **每一个陈述级 Shrikhand 元素（stat-big、close-big）都旋转 -5° 到 -6°，`{colors.red}`。** Hero 级不倾斜的红 Shrikhand 看起来像放错位置的词——倾斜是系统的「动作」信号。
- **每一个红面板展示元素都带着叠文字阴影**（`2px 2px 0 rgba(28,20,16,0.25), 4px 4px 0 rgba(28,20,16,0.2), 6px 6px 0 rgba(28,20,16,0.15)`）。没有阴影，红上的白 Shrikhand 读起来像漂着；有了它，文字感觉印进、压进面板。
- **每一个列表项目都用 `{colors.red}` em-dash（—）或圆点（•）字形**，绝对定位在左，正文 12–14px padding-left。不存在默认圆点项目；红标记是系统的列表信号。
- **每一段 Libre Baskerville 正文行高 ≥ 1.5（最好 1.6–1.75）。** 更紧的行高会塌掉编辑语域。
- **Libre Baskerville 段落里每一个正文 strong（`<strong>`）都把脸切到 Space Grotesk 字重 600。** 行内换脸是系统的主行内强调机制——衬线 strong 标签不会产生同样效果。

### 排版原则

声线对比是 **块状倾斜展示 Shrikhand ↔ 文学衬线正文 ↔ 宽字距等宽标签**。斜体很少（Libre Baskerville 斜体存在，但只用于正文内行内强调）；下划线留给红下划线页脚链接处理。Libre Baskerville 正文内的粗体换成行内切到 Space Grotesk 字重 600——换脸就是强调信号。

数字内容（统计数字、财务值、百分比呼出、迷你统计）永远是红 Shrikhand。即使是正文单元格里的小行内统计也变成红 Shrikhand。数字当展示的模式，才给系统体育杂志语域。

## 版式

### 画布系统
系统以每页 `100vw × 100vh` 为目标。幻灯片绝对定位，通过不透明度 + translateY（30px）+ scale（0.98 → 1）、550ms ease 动画进入。同一时间只有一页是 `.active`。默认幻灯片内边距是 `48px 56px`，有几处大变化：
- Hero 页：`5vh 7vw` 顶内边距，对齐改到左上。
- 路线图页：`40px 48px` 以容纳密两列网格。
- 支柱页：`0`（支柱列提供自己的内部内边距）。

### 内边距与间距阶梯

| Token | 值 | 用途 |
|---|---|---|
| `{spacing.pad-slide}` | 48px 56px | 默认幻灯片内边距 |
| `{spacing.pad-cell}` | 22px 20px | 表格式单元格内部内边距（财务网格） |
| `{spacing.pad-cell-sm}` | 20px 24px | 摘要高亮单元格内边距 |
| `{spacing.pad-pillar}` | 32px 24px | 支柱列内边距 |
| `{spacing.pad-card}` | 24px | 全球卡内边距 |
| `{spacing.pad-roadmap}` | 40px 48px | 路线图表面内边距 |
| `{spacing.gap-grid-md}` | 24px 32px | 标准服务/全球网格间距（行 × 列） |
| `{spacing.gap-grid-roadmap}` | 28px 36px | 路线图两列网格间距 |
| `{spacing.gap-grid-stats}` | 48px | 大统计行间距 |
| `{spacing.gap-stat-row}` | 20px | 统计项栈内的垂直间距 |

### 持续 Chrome
每一页出现三个元素：
- **进度条** 在底边 —— 5px 厚 `{colors.red}` 条，宽度随页索引增长。最厚、最可见的 chrome；既当进度指示，也当底边海报裁边。
- **幻灯片计数器** 在右下（`bottom: 18px right: 24px`）—— Space Grotesk 字重 600 全大写 NN / NN，50% 不透明度。
- **提示胶囊** 在底中 —— 灰白胶囊里的 Space Grotesk 全大写文字，默认不透明度 0，`body:hover` 时淡到 50%。

### 表面变体
幻灯片组在五种表面处理间循环：
- **白内容表面** ——默认，多数页。
- **灰白条纹面板** ——支柱布局内，交替列拿到 `{colors.light}` 背景做垂直条纹。
- **全出血红面板** ——陈述 / 引文页用 `{colors.red}` 铺满画布，白展示文字加叠文字阴影。
- **全出血深色面板** ——路线图级表面用 `{colors.dark}` 底，白字和红强调。
- **带框表格式网格** ——财务数字和摘要高亮网格带着 3px 墨外描边 + 1.5px 墨内单元格描边，产出系统签名的双描边表格式构图。

### Hero 栈构图
标准封面/hero 模式是 **三行 Shrikhand 栈**，每行不同尺寸，至少一行带旋转，至少一行红。栈从左上读到右下，最小行在底，最响的红旋转在中。这套构图是系统最鲜明的开场。

## 纵深与抬升

### 无卡片，无阴影（大体如此）
系统 **几乎不用 box-shadow**。卡片不靠阴影从表面浮起。纵深来自：
- **重描边**（表格式网格上外 3px + 内 1.5px 双描边；全球卡上 2px solid 描边；编辑 leftbar 卡上 4px 红左边线）。
- **表面反色**（全出血红或深面板切换整块表面）。
- **倾斜展示元素** 打断网格对齐。

### 单一阴影模式（叠文字阴影）
整套系统里唯一的阴影是 **红面板上红展示文字上的叠文字阴影**：三步 2/2、4/4、6/6，递减不透明度墨填充（0.25、0.20、0.15）。阴影通过 `text-shadow:` 应用，不是 `box-shadow:`。效果是印刷机感——文字读起来像稍微套印偏了三次。这种处理只出现在 red-quote 和红面板上某些旋转 Shrikhand 展示瞬间。

### 描边当纵深（表格式网格签名）
财务网格和摘要高亮网格模式用 **3px solid 墨外描边** 配 **1.5px solid 墨内单元格描边** ——两种描边重量在每个单元格交叉处相触，产出印刷新闻纸质感。这是数据重表面上系统的主结构纵深机制。

### Leftbar 线
编辑卡（服务卡、路线图阶段、全球卡）由 **4px（深色表面上 3px）红实心左边框** 标记，16–18px padding-left。leftbar 线发出「这是一张卡」的信号而不围住它——卡读起来像从红线悬臂伸出。这是系统最常见的卡模式。

### 倾斜当纵深
旋转 Shrikhand 展示元素打断水平基线，在不用透视的情况下创造感知维度。标准旋转是 -6°（stat-big）、-5°（close-big）、-4°（hero-title-red）、+2°（hero-title-bottom）。这些倾斜是系统空间语言的一部分。

## 形状与处理

### 圆角
- **除 hint-pill（4px）和柱轨道元素（本模板没有，但若使用应为 0px）外，一切都是 0px。** 每一张卡、每一个单元格、每一块面板、每一个呼出都是严格矩形。
- **4px** 只在 hint-pill 上——给浮动 chrome 的小小让步。

方角纪律是必要的。圆角卡立刻把印刷海报感塌成通用网页美学。

### 描边粗细
- **5px solid `{colors.red}`** ——只用于持续进度条。
- **4px solid `{colors.red}`** ——用于编辑 leftbar 卡（白表面上的服务卡）。
- **3px solid `{colors.dark}`** ——用于表格式网格的外描边（财务网格、摘要高亮）以及垂直支柱分隔。
- **3px solid `{colors.red}`** ——用于路线图阶段卡的 leftbar（深色表面上）。
- **2px solid `{colors.red}`** ——用作页脚链接上的下划线。
- **2px solid `{colors.dark}`** ——用作全球卡上的轮廓描边。
- **1.5px solid `{colors.dark}`** ——用于表格式网格的内单元格。
- **1px solid `rgba(28, 20, 16, 0.08)`** ——支柱面板内项目行之间的发丝软分隔。

描边阶梯（1px-软 / 1.5px / 2px / 3px / 4px / 5px）是固定的。每条描边都是实线；不存在虚线和点线描边。

### 装饰元素类型

**Hero 标题栈** ——三行不同尺寸的 Shrikhand 构图，带旋转和色彩对比。系统的签名开场。

**红面板** ——全出血 `{colors.red}` 底，白展示文字带着叠文字阴影。用于陈述 / 引文瞬间。

**深色面板** ——全出血 `{colors.dark}` 底，白字和红强调。用于路线图级密数据表面。

**表格式带框网格** ——3px 墨外描边 + 1.5px 墨内单元格描边，产出双描边表格式构图。每个单元格装着 Shrikhand 红数字 + Space Grotesk 全大写标签 + Libre Baskerville 正文段 + 可选底部 Space Grotesk 微行。

**红 leftbar 卡** ——4px 实心红左边线，18px 左内边距，装着 Shrikhand 卡标题 + Libre Baskerville 正文 + Space Grotesk 红项目列表。系统的主编辑卡模式。

**支柱面板** ——多支柱布局内的垂直列，用 3px 墨垂直线分开，白与灰白背景交替。每个支柱装着 Shrikhand 红数字、Shrikhand 标题、Libre Baskerville 导语，以及用 1px 发丝软线分开的 Space Grotesk 项目。

**全球卡** ——2px solid 墨描边卡，24px 内边距，装着 Space Grotesk 红标签 + Shrikhand 标题 + Libre Baskerville 正文 + 行内 gc-stats 行。用在全球存在表面上。

**Em-dash 项目** ——红 em-dash 字形，绝对定位在左，正文 14px padding-left。系统的主列表标记。

**圆点项目** ——红圆点字形，绝对定位在左，正文 12px padding-left。次级列表标记，用在卡和支柱项目里。

**页脚链接** ——Space Grotesk 全大写文字，2px 红下划线，4px padding-bottom。悬停把文字色换成红。

**叠文字阴影** ——三步递减不透明度墨阴影，用在红面板上的红展示文字。系统唯一的阴影处理。

**倾斜展示** ——旋转 -6° 到 +2° 的 Shrikhand 元素。用于 hero-title-red、stat-big、close-big 和 hero-title-bottom。

## 该做与不该做

### 该做

- 把 `{colors.bg}`（白）当作多数表面的默认画布。陈述页切到 `{colors.red}`，密数据页切到 `{colors.dark}`，垂直支柱条纹交替 `{colors.bg}` / `{colors.light}`。
- 把每一个 hero 级标题设成多行 Shrikhand 栈，至少一行旋转、至少一行红。组合栈是系统的开场签名。
- 每一个数字呼出瞬间都用 `{colors.red}` 的 Shrikhand ——表格式单元格、摘要高亮、支柱数字、行内迷你统计。红 Shrikhand 数字是系统的数据声线。
- 把每一条章节 eyebrow 设成 Space Grotesk 字重 600 全大写、2–3px 字距、`{colors.red}`。宽字距红标签是通用章节开场。
- 把叠文字阴影用在红面板上的红展示文字。三步递减不透明度墨阴影是系统唯一的阴影，创造印刷机感。
- 编辑卡用 4px 红 leftbar 模式（`{components.red-leftbar-card}`）。从线上悬臂伸出的处理是系统的主卡模式。
- 用双描边处理建表格式网格：3px 墨外描边 + 1.5px 墨内单元格描边在交叉处相触。
- 每一个列表项目都用红 em-dash（`{components.bullet-em-dash}`）或红圆点（`{components.bullet-bullet}`），绝对定位在左。禁止默认圆点项目。
- 倾斜 Shrikhand 陈述元素（-5° 到 -6°）以创造系统的签名动作。不倾斜的红陈述展示读起来像放错位置。
- 每一段正文都用 Libre Baskerville、行高 1.5–1.75、`{colors.dark}`。文学编辑正文才让系统感觉印出来。

### 不该做

- 不要引入第二强调色。红是唯一强调——正向绿、信息蓝、高亮黄都会打断单一强调纪律。
- 不要给卡、面板、单元格或呼出圆任何角。方角不可商量；唯一例外是 4px hint-pill chrome。
- 不要加投影或模糊阴影。系统有零 box-shadow；唯一阴影是红展示文字上的叠文字阴影。
- 不要替换字体。Shrikhand + Libre Baskerville + Space Grotesk 就是三人组。用任何其他展示脸替换 Shrikhand 会塌掉整套身份。
- 不要用 Shrikhand 做正文或 Libre Baskerville 做标签。三字体角色纪律不可商量。
- 不要用默认项目符号或圆点列表标记。列表永远用红 em-dash 或红圆点字形，绝对定位在左。
- 不要省略 hero 级红 Shrikhand 元素上的倾斜。旋转是系统的签名动作；不倾斜的红展示读起来平。
- 不要在白表面上把标题渲染成红（stat-big、close-big、hero-title-red 这些旋转陈述元素除外）。多数章节页头是 `{colors.dark}` Shrikhand，不是红。
- 不要把 Libre Baskerville 正文行高压到 1.5 以下。紧正文行高会把文学语域塌成局促。
- 不要用卡片或结构内容挤满陈述页。陈述表面（红面板、统计页、收束页）故意在单个旋转红展示元素周围预留大量负空间。

## 响应式行为

Bold Poster 设计成 **1920×1080 演示系统**。尺寸对展示字用带 `vw` 中间值的 CSS `clamp()`，对描边和 chrome 用固定 `px`，对单元格内边距用贴近 rem 的固定值。系统为窄视口提供单一 768px 响应式断点。

### 缩放行为
- Hero 统计随视口宽度从 120px → 320px。
- Hero 标题从 64px → 260px。
- 章节页头从 32px → 72px。
- 正文从 11px → 16px。
- 描边（1px-软 / 1.5px / 2px / 3px / 4px / 5px）和旋转变换固定，不缩放。

### 移动端断点（max-width: 768px）
单一 `@media (max-width: 768px)` 块为窄视口重组密布局：
- 幻灯片内边距从 48px × 56px 缩到 32px × 24px。
- 摘要列从 2 → 1 塌缩。
- 摘要高亮网格从 3 → 1 塌缩。
- 财务网格从 3 → 2 塌缩。
- 服务网格从 2 → 1 塌缩。
- 路线图网格从 2 → 1 塌缩。
- 支柱从水平 flex-row 切到垂直 flex-column；垂直分隔变成水平底边。
- 全球网格从 2 → 1 塌缩。
- 统计行垂直堆叠。
- Hero 标语从绝对定位右下改成相对定位在 hero 标题栈下方。

系统能用，但没有为低于 768px 的竖屏优化——为横屏演示语境而设计。

### 演示行为
- 用 `ArrowRight`、`ArrowDown`、`Space`、`Enter` 或 `PageDown` 前进。
- 用 `ArrowLeft`、`ArrowUp` 或 `PageUp` 后退。
- 点击视口右半前进；点击左半后退。
- 水平触摸滑动，阈值 50px，前进/后退。
- 幻灯片过渡是 550ms cubic-bezier `(0.22, 1, 0.36, 1)`，组合不透明度、translateY（30px）和 scale（0.98 → 1）。
- 底边进度条以 500ms cubic-bezier ease 动画到当前页百分比。

### 打印行为
系统没有 `@media print` 规则。过渡只用于屏幕。静态导出时，逐页截图可保留全部旋转变换和叠文字阴影（两者都是纯 CSS）。

### 交互状态
- 页脚链接悬停时文字色从 `{colors.dark}` 换成 `{colors.red}`。
- hint-pill 在 `body:hover` 上从不透明度 0 淡到 0.5，400ms ease。

## CJK 与国际内容

用本模板承载中文（或其他 CJK）内容时，把拉丁字体栈换成对等的中文搭配，并套用通用 CJK 调整。所有推荐中文字体经 CDN 加载——无需安装。

### 推荐中文搭配

| 角色 | 拉丁（默认） | 中文对应 |
|---|---|---|
| 展示 / hero / 统计 / 章节页头 / 数字 / 卡片标题 | Shrikhand 400（重 slab-手写，旋转） | 思源宋体 Noto Serif SC 900 |
| 正文 / body-card / body-cell / hero-meta / cite / close-sub | Libre Baskerville 400（文学衬线） | 思源宋体 Noto Serif SC 400 |
| 标签 / 项目正文 / 计数器 / 链接 / 微 chrome | Space Grotesk 400–600（全大写，2–3px 字距） | 思源黑体 Noto Sans SC 500（无变换，无字距） |

### 混排策略

**策略 A** ——每个角色单一 CJK 字族，自带拉丁字形覆盖。展示和正文都用 **思源宋体 Noto Serif SC**（展示字重 900，正文字重 400——视觉层级来自字重、尺寸、颜色和旋转，不是面孔对比）。小全大写 chrome（标签、项目正文、计数器、链接）用 **思源黑体 Noto Sans SC** 字重 500。思源宋体带能与汉字干净配对的拉丁字形；混排展示瞬间里，思源宋体字重 900 会以同一重衬线声线渲染中文和拉丁。

### 加载

加到模板的 `<head>`：

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;500;700;900&family=Noto+Sans+SC:wght@400;500;600&display=swap" rel="stylesheet">
```

### 通用 CJK 调整

- **行高**：相对拉丁规格增加约 15–25%。正文 1.75–1.85（已接近 Libre Baskerville 1.75；CJK 保持 1.8），展示 1.1–1.25（从 Shrikhand 上非常紧的 0.82–0.9 上调）。展示 0.82 在 CJK 里会垂直碰撞；至少开到 1.0。
- **字距**：每一段 CJK 都设为 0。模板里 hero-title 上 1px 正 tracking 和 Space Grotesk 标签上 2–3px 字距，在方形 CJK 字形上都读起来发空。
- **文本变换**：不要对中文应用 `uppercase`——CJK 没有大小写。拉丁原作里每一个 Space Grotesk 标签、tag-label、rm-label、计数器和链接都用 `text-transform: uppercase`；CJK 段要去掉。
- **标点**：用全角中文标点（，。：；！？「」（））。
- **展示标题不加句号**：中文排印惯例在展示级标题上省略末尾的 。
- **中西文之间的空格（盘古之白）**：每个汉字与相邻拉丁字符或数字之间插入 ASCII 空格。写 `1970 米兰式海报`，不要写 `1970米兰式海报`。
- **一句一面孔**：思源宋体以统一衬线风格覆盖 CJK 和拉丁字形——让它处理展示和正文里的混排句。不要让浏览器在词中把 ASCII 字符回退到 Shrikhand 或 Libre Baskerville。

### 本系统的美学备注

系统身份建立在 **Shrikhand 的块状 slab-手写性格 + 旋转 + 饱和红** 上。Shrikhand 是本模板最鲜明的单一决定——它没有中文对等。思源宋体字重 900 承载重量和编辑语域，但完全失去好玩的斜切 slab 性格。补偿方式是 **更用力靠非排印签名**：保持全部旋转完整（stat-big -6°、close-big -5°、hero-title-red -4°、hero-title-bottom +2°），保持红面板展示上的叠文字阴影，保持饱和番茄红作为唯一强调，保持 3px + 1.5px 双描边表格式网格，保持红 leftbar 卡，保持红 em-dash 项目标记。旋转、红和印刷新闻纸结构语言在换脸后仍存活。

系统的三字体角色纪律（Shrikhand 展示 / Libre Baskerville 正文 / Space Grotesk chrome）在 CJK 里塌成两字体系统：拉丁衬线的一切用思源宋体，拉丁等宽的一切用思源黑体。正文对展示的对比变成纯字重（400 vs 900）加颜色（深 vs 红）。**不要在 CJK 内容里句中换脸** ——即使是 `<strong>` 强调。句中换脸在中文排印里读起来是坏的（解析成不一致，不是编辑对比）。中文正文里的行内 `<strong>` 强调，留在思源宋体里用字重对比（400 → 700）或颜色对比（深 → 红强调）。把换脸信号留给角色边界（标题对正文、正文对标签），在那里读成层级而不是噪声。

### 已知 CJK 缺口

- **没有精确在线 CJK 匹配 Shrikhand 的 slab-手写性格。** 这张脸是意大利体育杂志展示手写，带块状字脚和好玩斜切形态——Google Fonts、Adobe Fonts 或 cn-fontsource 上都没有中文对等。思源宋体字重 900 给出重量和编辑语域，但读起来严肃而不是好玩。旋转变换和饱和红自己就能承载好玩体育杂志声线；译成 CJK 时不要丢掉倾斜。
- **没有 CDN 中文等宽面孔做 chrome 声线。** Space Grotesk 的角色（全大写 tracking 标签、幻灯片计数器、带红下划线的页脚链接）依赖全大写 + 2–3px 字距处理。思源黑体字重 500–600、字距 0 是最接近的匹配，但失去「盖章元数据」信号。CJK 构建里，标签/链接上的红色和 1–2px 描边处理做大部分 chrome 识别工作。
- **Libre Baskerville 的古典文学语域没有精确中文对应。** 思源宋体读起来机构现代，而不是 19 世纪文学。需要专门文学季刊声线的项目（随笔或宣言里的长正文），考虑用霞鹜文楷 LXGW WenKai 替代思源宋体——它带着更接近 Baskerville 编辑个性的手写/书法暖意。

## 迭代指南

1. 任何新内容页以 `{typography.section-header}`（32–64px）、`{colors.dark}` 的 Shrikhand 章节页头开头，可选前面加一条 Space Grotesk 红 eyebrow 标签。
2. 任何新数字呼出（单元格数字、支柱数字、行内统计、摘要高亮）都是适当 cell-number 级的 `{colors.red}` Shrikhand。
3. 任何新正文段落都是 Libre Baskerville 字重 400、`{colors.dark}`、行高 1.5–1.75。
4. 任何新编辑卡用 `{components.red-leftbar-card}` 模式（4px 红左边线 + 18px padding-left），装着 Shrikhand 标题 + Libre Baskerville 正文 + Space Grotesk 红项目列表。
5. 任何新数据网格包在 3px 墨外描边里，内单元格 1.5px 墨描边。每个单元格装着：Shrikhand 红数字 + Space Grotesk 全大写标签 + Libre Baskerville 正文 + 可选底部 Space Grotesk 微语境行。
6. 任何新陈述页用全出血 `{colors.red}` 面板，白 Shrikhand 展示文字带着叠文字阴影，下面白 Libre Baskerville cite。
7. 任何新密数据页用全出血 `{colors.dark}` 面板，白字、红 Space Grotesk 标签、阶段卡上红 3px leftbar 线，列表上红圆点字形。
8. 任何新列表用红 em-dash 或红圆点字形，绝对定位在左——从不用默认圆点项目。
9. 任何新 hero 构图都是多行 Shrikhand 栈：至少三行，至少一行旋转，至少一行红。不要塌成单一水平标题。
10. 如果表面太单调，切换表面底（白 → 红 / 深 / 灰白面板）——不要加第二强调色或第三字体。

## 已知缺口

- **Shrikhand 是单字重（400）展示脸** ——没有更粗或更轻的字重。每一个 Shrikhand 元素都是同一字重；视觉层级只来自尺寸、颜色和旋转。
- **Shrikhand、Libre Baskerville 和 Space Grotesk 从 Google Fonts 加载**，经由单一 `<link>` 请求。除 `cursive` / `serif` / `sans-serif` 外没有系统回退——Google Fonts 失败的环境里，系统塌成通用系统字体，完全失去身份。
- **叠文字阴影为墨压红语境硬编码。** 把它用到不同色彩组合（例如浅底上的红字）不会产出同样效果；三步阴影专门为红面板表面调过。
- **旋转变换按元素类型固定**（stat-big -6°、close-big -5°、hero-title-red -4°、hero-title-bottom +2°）。调整个别旋转需要逐实例样式覆盖。
- **财务网格和摘要高亮网格使用重叠描边**（外 3px + 内 1.5px，因 box-sizing 在物理上重叠半像素）。浏览器对这种重叠的渲染通常干净，但在某些缩放级别可能产生细微 1 像素伪影。
- **支柱布局在每根支柱列上使用 `overflow-y: auto`。** 内容长的表面上，这会在某些操作系统上引入可见滚动条——系统设计给装进视口的内容。
- **slide-hero 上的 hero 标语绝对定位在 `bottom: 8vh; right: 7vw`**，最大宽度 300px。在非常宽或非常窄的宽高比上，可能与 hero 标题栈错位。
- **进度条是 5px 高条**，在底边有文字的页上可能在视觉上叠到内容——尤其是 slide-close 表面把 close-links 放在 `bottom: 5vh`，能避开进度条但余量很小。
- **点击前进交互在 50% 宽度处分割视口** 做下一页/上一页。这可能与页内链接的点击交互行为冲突（收束页页脚链接）。系统依赖链接点击事件 stopPropagation，而它们默认不会。
- **bullet-list 类全局定义** 了 em-dash 字形，但演示模板里没用——支柱项目、服务项目和路线图项目都在行内重定义自己的项目样式。已定义工具和实际用法模式之间有些不一致。
