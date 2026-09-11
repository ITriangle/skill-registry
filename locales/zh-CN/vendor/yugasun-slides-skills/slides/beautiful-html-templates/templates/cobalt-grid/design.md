---
version: alpha
name: Cobalt Grid
description: "A Japanese-magazine trend-report system built on warm cream paper, electric cobalt ink, and a graph-paper grid that lives permanently behind every slide. Newsreader serif headlines tower at 18vh while DM Mono carries chrome and ticker text. The signature decoration is a pixel-glitch column — vertical scanlines stair-stepped down the right edge of declarative slides — paired with QR-style 8×8 grid patches. The cultural reference is WIRED Japan, Shift magazine, and architectural trend reports printed in two-color risograph: cream + one cobalt."

colors:
  paper: "#F0EBDE"
  paper-2: "#E6E0CE"
  ink: "#1F2BE0"
  ink-soft: "#5560E5"
  grid: "rgba(31, 43, 224, 0.10)"
  ink-faint: "rgba(31, 43, 224, 0.18)"

color-aliases:
  rule: ink
  bg: paper

typography:
  display-hero:
    fontFamily: "Newsreader, Georgia, serif"
    fontSize: "clamp(100px, min(11vw, 18vh), 200px)"
    fontWeight: 400
    lineHeight: 0.92
    letterSpacing: -0.008em
  display-closing:
    fontFamily: "Newsreader, Georgia, serif"
    fontSize: "clamp(72px, min(8.4vw, 14vh), 180px)"
    fontWeight: 400
    lineHeight: 0.96
    letterSpacing: -0.005em
  display-chapter:
    fontFamily: "Newsreader, Georgia, serif"
    fontSize: "clamp(56px, min(6vw, 10vh), 130px)"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: -0.005em
  display-quote:
    fontFamily: "Newsreader, Georgia, serif"
    fontSize: "clamp(50px, min(5.6vw, 9vh), 110px)"
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -0.005em
  display-manifesto:
    fontFamily: "Newsreader, Georgia, serif"
    fontSize: "clamp(56px, min(6.4vw, 11vh), 120px)"
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -0.005em
  headline:
    fontFamily: "Newsreader, Georgia, serif"
    fontSize: "clamp(46px, min(4.8vw, 8.2vh), 92px)"
    fontWeight: 400
    lineHeight: 0.95
  headline-index:
    fontFamily: "Newsreader, Georgia, serif"
    fontSize: "clamp(48px, min(5vw, 8.5vh), 100px)"
    fontWeight: 400
    lineHeight: 0.95
  vbig-numeral:
    fontFamily: "Newsreader, Georgia, serif"
    fontSize: "clamp(110px, min(11vw, 18vh), 240px)"
    fontWeight: 400
    lineHeight: 0.92
    letterSpacing: -0.015em
  ed-callout:
    fontFamily: "Newsreader, Georgia, serif"
    fontSize: "clamp(28px, min(2.8vw, 4.6vh), 50px)"
    fontWeight: 400
    lineHeight: 1.1
  row-headline:
    fontFamily: "Newsreader, Georgia, serif"
    fontSize: "clamp(26px, 2vw, 40px)"
    fontWeight: 400
    lineHeight: 1.05
  table-name:
    fontFamily: "Newsreader, Georgia, serif"
    fontSize: "clamp(20px, 1.6vw, 28px)"
    fontWeight: 400
    lineHeight: 1.15
  micro:
    fontFamily: "Hanken Grotesk, sans-serif"
    fontSize: "clamp(12px, 0.9vw, 14px)"
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.16em
    textTransform: uppercase
  micro-strong:
    fontFamily: "Hanken Grotesk, sans-serif"
    fontSize: "clamp(13px, 1vw, 16px)"
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.18em
    textTransform: uppercase
  micro-sm:
    fontFamily: "Hanken Grotesk, sans-serif"
    fontSize: "clamp(11px, 0.75vw, 12px)"
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.18em
    textTransform: uppercase
  body:
    fontFamily: "Hanken Grotesk, sans-serif"
    fontSize: "clamp(14px, 0.95vw, 15px)"
    fontWeight: 400
    lineHeight: 1.5
  body-lede:
    fontFamily: "Hanken Grotesk, sans-serif"
    fontSize: "clamp(15px, 1vw, 18px)"
    fontWeight: 400
    lineHeight: 1.5
  body-stat:
    fontFamily: "Hanken Grotesk, sans-serif"
    fontSize: "clamp(15px, 1vw, 17px)"
    fontWeight: 400
    lineHeight: 1.5
  mono-tag:
    fontFamily: "DM Mono, ui-monospace, monospace"
    fontSize: "clamp(13px, 0.9vw, 15px)"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.04em
  mono-chrome:
    fontFamily: "DM Mono, ui-monospace, monospace"
    fontSize: "clamp(11px, 0.82vw, 13px)"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.06em
  mono-tick:
    fontFamily: "DM Mono, ui-monospace, monospace"
    fontSize: "clamp(12px, 0.85vw, 14px)"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.04em

spacing:
  edge: "clamp(36px, 3.6vw, 80px)"
  edge-inner: "clamp(60px, 8vw, 160px)"
  pad-top: "clamp(76px, 8vh, 130px)"
  pad-bottom: "clamp(100px, 10vh, 150px)"
  gap-lg: "clamp(28px, 3vw, 56px)"
  gap-md: "clamp(20px, 2.2vh, 36px)"
  gap-sm: "clamp(14px, 1.6vh, 24px)"
  gap-xs: "clamp(10px, 1.2vh, 18px)"

canvas:
  width: 100vw
  height: 100vh

components:
  graph-paper-grid:
    backgroundImage: "linear-gradient(to right, {colors.grid} 1px, transparent 1px), linear-gradient(to bottom, {colors.grid} 1px, transparent 1px)"
    backgroundSize: "clamp(28px, 2.2vw, 44px) clamp(28px, 2.2vw, 44px)"
    description: "Permanent ::before pseudo on every stage. 28–44px squared graph paper grid in 10%-opacity cobalt that sits behind every slide at z-index 1. Cannot be turned off — it is the canvas tone."
  hairlines:
    height: "1.5px"
    background: "{colors.ink}"
    description: "Two persistent slim cobalt rules — one at the top of every slide (≈2.6vh from top) and one near the bottom (≈2vh from bottom) — both inset from edges by {spacing.edge}. They frame the slide composition."
  pagenum:
    position: absolute
    right: "{spacing.edge}"
    bottom: "clamp(48px, 4.8vh, 76px)"
    fontFamily: "DM Mono, ui-monospace, monospace"
    fontSize: "clamp(11px, 0.82vw, 13px)"
    color: "{colors.ink}"
    letterSpacing: 0.06em
    description: "Mono cobalt page number anchored bottom-right above the bottom hairline. One per slide."
  nav-hint:
    position: fixed
    left: "{spacing.edge}"
    bottom: "clamp(48px, 4.8vh, 76px)"
    fontFamily: "DM Mono, ui-monospace, monospace"
    fontSize: "clamp(10px, 0.75vw, 12px)"
    color: "{colors.ink}"
    letterSpacing: 0.08em
    opacity: 0.4
    description: "Mono cobalt navigation hint anchored bottom-left, mirrors pagenum."
  pixel-glitch:
    description: "Stair-stepped column of vertical scanlines, rendered as inline SVG. Each stepped rectangle contains evenly-spaced cobalt vertical lines on cream. Sits absolutely positioned (typically right edge) at z-index 3, decorative only. Size ranges from 16vw × full-height (compact decoration) to 32vw × full-height (signature cover decoration)."
  qr-block:
    display: grid
    gridTemplateColumns: "repeat(8, 1fr)"
    gridTemplateRows: "repeat(8, 1fr)"
    gap: 1.5px
    background: "{colors.paper}"
    padding: 4px
    boxShadow: "0 0 0 1.5px {colors.paper}"
    description: "8×8 QR-style mosaic of cobalt cells on cream background. Paper-fill ensures it reads as a discrete patch when overlapping the pixel-glitch column. Typical size 58–100px square."
  topbar-rule:
    borderBottom: "1.5px solid {colors.ink}"
    paddingBottom: "clamp(12px, 1.4vh, 22px)"
    description: "1.5px cobalt rule under the topbar of an index, data, or table layout. Below the rule sits a Newsreader headline (left) and a mono lab-tag (right)."
  row-divider:
    borderBottom: "1px solid {colors.ink-faint}"
    description: "Faint 18%-opacity cobalt rule between rows of an index list, table, or ledger."
  attribution-rule:
    borderTop: "1px solid {colors.ink}"
    paddingTop: "clamp(10px, 1.2vh, 18px)"
    description: "Solid cobalt rule above a quote attribution or manifesto byline."
  pixel-stack-bars:
    description: "Vertical bar chart rendered as a column of stacked 'cells' — flex column-reverse with 3px gaps, each cell a small horizontal block. Cells default to 10%-opacity cobalt (the grid color); .on cells fill solid cobalt to represent the value. Reads as a pixelated bar made of grid units."
  ledger-row:
    display: grid
    gridTemplateColumns: "76px 0.6fr 1.4fr 0.7fr 0.5fr"
    gap: "clamp(14px, 1.4vw, 28px)"
    borderBottom: "1px solid {colors.ink-faint}"
    description: "Dense table row carrying a num-tag, name (Newsreader), description (Hanken Grotesk), mood-tag, and delta-tag (mono with up/down arrow prefix). Header row uses 1.5px solid cobalt bottom border."
  vstack-label:
    fontFamily: "DM Mono, ui-monospace, monospace"
    writingMode: "vertical-rl"
    textOrientation: "mixed"
    letterSpacing: 0.04em
    description: "Vertical-orientation mono label column anchored to the right edge of a slide. Replaces the Korean vertical column of the reference with mono catalogue text rotated 90°."
  delta-up:
    content: "↑ "
    description: "Up arrow prefix via ::before on a mono delta tag in the ledger table."
  delta-down:
    content: "↓ "
    opacity: 0.6
    description: "Down arrow prefix via ::before, dimmed 40% to read as decline."
  delta-flat:
    content: "— "
    opacity: 0.6
    description: "Em-dash prefix via ::before, dimmed 40% to read as neutral."
---

## 概述

Cobalt Grid 是一套**双色趋势报告编辑系统**，建在三块不可移动的地基上：温暖奶油纸画布（`{colors.paper}`）、电光钴蓝墨（`{colors.ink}`），以及**永久坐在每一页后面的方格纸网格**。网格不是可选装饰——它经每个 `.stage` 上的 `::before` 伪元素渲染，关不掉。美学是「双色油印专著」：只有奶油 + 钴蓝，网格让整套片子读起来像建筑描图纸或日式趋势报告。

字体栈是一场刻意的三面对谈。**Newsreader**——当代文学衬线，低调制罗马字形——承担每一个展示瞬间、每一个区块标题、每一个统计数字。Newsreader 只用字重 400；字体靠字号立层级，不靠字重。**Hanken Grotesk**——人文无衬线——承担每一段正文、每一个大写标签、每一个微文字。Hanken 正文用 400，标签用 600。**DM Mono**——等宽——承担每一个 chrome 元素：页码、等宽 tag、轴刻度、竖排标签、表格里的 delta 箭头。三脸系统构成系统身份：衬线陈述 + 无衬线正文 + 等宽 chrome。

色板**严格双色**：奶油和钴蓝，外加一档更软的钴蓝 `{colors.ink-soft}` 和两档透明度（`{colors.grid}` 10%、`{colors.ink-faint}` 18%）用于气氛和结构。没有强调色。钴蓝是*唯一*墨色——标题、正文、边框、页码、方格纸、pixel-glitch 装饰、QR 补丁全用它。奶油纸是*唯一*表面。连 pixel-stack 柱状图也用两档透明度的钴蓝（10% 关、100% 开）来画数据。

纵深是**平面加结构线**。没有投影、没有抬起的卡片、没有圆角表面。层级来自：
- 每一页顶底的 1.5px 钴蓝**发丝框**。
- 区块标题下的 1.5px 钴蓝 **topbar 线**。
- 表格或索引条目之间的 1px 淡钴蓝 **行分割线**。
- 一切后面 10% 透明度的**方格纸网格**。
- 作为构图强调的 pixel-glitch 和 QR-block **装饰 SVG 补丁**。

**密度哲学：中到密，由网格结构化。** Cobalt Grid 为编辑密度而建——杂志跨页、趋势索引、数据账本。正确构图的一页，是一个大号 Newsreader 标题配多行结构化信息（六条趋势的索引、八条账本、八根 pixel-stack 柱的图）。底下的方格纸主动想被填满；稀疏页露出太多网格，读起来像线框。例外是 manifesto、quote 和 colophon 版式，刻意留空，让方格纸呼吸。按页类型选密度：chapter / manifesto / quote / colophon 稀疏；index / data / table 密。

**关键特征：**
- 奶油纸画布 `{colors.paper}`，电光钴蓝 `{colors.ink}` 作为唯一墨——严格双色。
- 每一页后面永久的 28–44px 方格纸网格，10% 透明度钴蓝。
- 顶底 1.5px 钴蓝发丝以 `{spacing.edge}` 内缩框住每一页。
- 每一次展示/标题用字重 400 的 Newsreader 衬线；正文/标签用 Hanken Grotesk 无衬线；所有 chrome 用 DM Mono。
- 竖向扫描线 pixel-glitch 柱和 QR 式 8×8 马赛克，是系统的招牌装饰补丁。
- 展示字可以非常大——`{typography.display-hero}` 到 18vh（1080 高显示器上约 194px），`{typography.vbig-numeral}` 到 240px。
- Hanken 标签大写，字距 0.16–0.18em；等宽 tag 带 0.04–0.06em tracking。
- Pixel-stack 柱状图把数据画成网格单元叠柱（钴蓝开 / 钴蓝 10% 关）。
- 页码在右下，等宽导航提示在左下，都锚在底发丝上方。

## 色彩

### 双色系统
- **Paper**（`{colors.paper}` — #F0EBDE）：画布。温暖奶油米白，带明确的黄暖偏——更接近「新闻纸」而不是「空白白」。用作通用幻灯片背景，也作 QR-block 后面的填充，让它们在 pixel-glitch 柱上读成独立补丁。
- **Paper-2**（`{colors.paper-2}` — #E6E0CE）：略深一点的奶油。定义在色板里但用得很少——需要细微区域区分时可用。
- **Ink**（`{colors.ink}` — #1F2BE0）：电光钴蓝 / 宝蓝。系统里*唯一*的墨色。用于所有标题、所有正文、所有边框、所有 chrome、方格纸网格、pixel-glitch 装饰和 QR 补丁。高饱和是刻意的——全力时读起来像油印钴蓝，不是海军蓝。
- **Ink Soft**（`{colors.ink-soft}` — #5560E5）：更浅的钴蓝，用于次级标记。定义在色板里但用得很少——系统里大多数软化钴蓝来自墨上的透明度，而不是这档专用调。
- **Grid**（`{colors.grid}` — rgba(31, 43, 224, 0.10)）：10% 透明度钴蓝。专用于每一页后面永久的方格纸网格，以及 pixel-stack 柱状图里的「关」格。
- **Ink Faint**（`{colors.ink-faint}` — rgba(31, 43, 224, 0.18)）：18% 透明度钴蓝。专用于索引列表、表格和账本里的淡行分割线——夹在共享同一密信息层的行之间。

### 默认值
- **默认幻灯片表面**：`{colors.paper}`。
- **默认标题色**：`{colors.ink}`——每一个 Newsreader 衬线标题都是钴蓝。没有其他标题色。
- **默认正文字色**：`{colors.ink}`——正文也是钴蓝，只是更小。奶油上的钴蓝是系统唯一的文字关系。
- **默认标签 / 等宽 / 微文字色**：`{colors.ink}`。
- **默认边框色（结构线）**：`{colors.ink}` 1.5px solid。
- **默认边框色（密列表内的行分割）**：`{colors.ink-faint}` 1px solid。
- **默认网格色**：`{colors.grid}`——从不以全力可见；从不断开。
- **默认图表数据色（开）**：`{colors.ink}`。
- **默认图表数据色（关）**：`{colors.grid}`。

系统**没有通俗意义上的强调色**。第二色不存在——加红色 callout、绿色统计或黄色高亮会拆掉油印双色身份。需要强调时，加大字号、从 Hanken 切到 Newsreader、加等宽 delta 箭头，或用透明度变暗而不是上色来高亮。

## 字体排印

### 字体家族
系统跑在一场**三面对谈**上：`Newsreader`（衬线，字重 400 / 500 斜体）承担每一次展示和标题；`Hanken Grotesk`（无衬线，字重 400–700）承担每一段正文、标签和微文字；`DM Mono`（等宽，400–500）承担每一个 chrome 元素。没有第四张脸。

Newsreader 的罗马字形几乎只用字重 400——字体靠字号立层级，不靠字重。斜体 Newsreader 已加载（300/400/500 斜体轴），用在 manifesto 的 `.roman` 修饰符里（它*不是斜体*——这个修饰符把斜体正文翻回罗马体，做行内引出瞬间），也可用于行内 `<em>` 强调。Hanken Grotesk 正文用 400，标签用 600。DM Mono 以 400 提供 chrome。

衬线/grotesk/等宽三向配对是系统的主排印节奏。每张脸角色锁死：衬线 = 陈述，grotesk = 支撑文案，等宽 = 目录 chrome。

### 字号阶梯

| Token | 字号 | 字体 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.vbig-numeral}` | clamp(110px, min(11vw, 18vh), 240px) | Newsreader | 400 | 最大数字展示——英雄统计数字 |
| `{typography.display-hero}` | clamp(100px, min(11vw, 18vh), 200px) | Newsreader | 400 | 最大标题——封面或英雄展示 |
| `{typography.display-closing}` | clamp(72px, min(8.4vw, 14vh), 180px) | Newsreader | 400 | colophon/收束版式上的收束标题 |
| `{typography.display-chapter}` | clamp(56px, min(6vw, 10vh), 130px) | Newsreader | 400 | 章节开场或章节标题 |
| `{typography.display-manifesto}` | clamp(56px, min(6.4vw, 11vh), 120px) | Newsreader | 400 | manifesto 陈述展示 |
| `{typography.display-quote}` | clamp(50px, min(5.6vw, 9vh), 110px) | Newsreader | 400 | 引出式引文正文 |
| `{typography.headline-index}` | clamp(48px, min(5vw, 8.5vh), 100px) | Newsreader | 400 | 索引或趋势列表区块标题 |
| `{typography.headline}` | clamp(46px, min(4.8vw, 8.2vh), 92px) | Newsreader | 400 | 数据、表格或图表区块标题 |
| `{typography.ed-callout}` | clamp(28px, min(2.8vw, 4.6vh), 50px) | Newsreader | 400 | 英雄标题下方的编辑副标题 |
| `{typography.row-headline}` | clamp(26px, 2vw, 40px) | Newsreader | 400 | 索引列表里每行的标题 |
| `{typography.table-name}` | clamp(20px, 1.6vw, 28px) | Newsreader | 400 | 账本表格里每行的姓名格 |
| `{typography.body-lede}` | clamp(15px, 1vw, 18px) | Hanken Grotesk | 400 | 章节标题下方的导语段 |
| `{typography.body-stat}` | clamp(15px, 1vw, 17px) | Hanken Grotesk | 400 | 统计数字旁边的描述段 |
| `{typography.body}` | clamp(14px, 0.95vw, 15px) | Hanken Grotesk | 400 | 标准段落正文 |
| `{typography.micro-strong}` | clamp(13px, 1vw, 16px) | Hanken Grotesk | 600 | 最大大写标签 / kicker |
| `{typography.micro}` | clamp(12px, 0.9vw, 14px) | Hanken Grotesk | 600 | 标准大写标签 / lab-tag |
| `{typography.micro-sm}` | clamp(11px, 0.75vw, 12px) | Hanken Grotesk | 600 | 最小大写标签 / 表头 |
| `{typography.mono-tag}` | clamp(13px, 0.9vw, 15px) | DM Mono | 400 | 等宽目录 tag、索引行里的 num-tag |
| `{typography.mono-tick}` | clamp(12px, 0.85vw, 14px) | DM Mono | 400 | 等宽图表刻度标签、竖排标签条目 |
| `{typography.mono-chrome}` | clamp(11px, 0.82vw, 13px) | DM Mono | 400 | 等宽页码、导航提示、次级元数据 |

### 默认值
- **主区块标题（index、data、table）默认字号**：`{typography.headline}`（clamp 46–92px），索引版式用 `{typography.headline-index}`。
- **封面或英雄展示默认字号**：`{typography.display-hero}`（clamp 100–200px）。
- **章节或章节开场标题默认字号**：`{typography.display-chapter}`（clamp 56–130px）。
- **段落正文默认字号**：`{typography.body}`（clamp 14–15px）。
- **任何行内大写标签默认字号**：`{typography.micro}`（clamp 12–14px），字重 600，0.16em tracking。
- **任何等宽 chrome（页码、tag、刻度）默认字号**：`{typography.mono-tag}`（clamp 13–15px）。
- **Newsreader 默认字重**：400。不用 Newsreader 粗体。
- **Hanken 正文默认字重**：400。
- **Hanken 标签默认字重**：600。

拿不准时，伸手去拿 `{typography.headline}`（clamp 46–92px）做这一页的主区块标题，不要拿 `{typography.display-chapter}`（那只留给章节开场瞬间）。

### 招牌处理
这些处理在**对应元素类型一旦使用时就是必选项**：

- **每一个 Newsreader 元素都设为字重 400。** 本系统不用 600/700 的 Newsreader。文学衬线美学依赖克制字重下开放的罗马字形。
- **每一个 Newsreader 元素都渲染成 `{colors.ink}`（钴蓝）。** 不存在奶油衬线标题。
- **每一个 Hanken 标签、kicker、lab-tag 和微文字都是大写，字距至少 0.16em**，字重 600。没有 tracking 的 Hanken 大写读起来像没处理过。
- **每一个 DM Mono 元素都渲染成 `{colors.ink}`，字距 0.04–0.08em。** tracking 更紧的等宽读起来像代码，不是编辑。
- **每一个展示元素都带负字距。** display-hero 为 -0.008em，vbig-numeral 为 -0.015em，chapter / closing / manifesto / quote 为 -0.005em。
- **方格纸网格在每一页上都是永久的。** `.stage::before` 规则不能逐页覆盖——每幅构图都坐在它上面。
- **顶底发丝框住每一页。** `.hairlines::before` 和 `.hairlines::after` 规则默认生效；不应关掉。
- **页码坐在底发丝上方，留出清楚的垂直空间。** 底发丝锚在 `bottom: clamp(20px, 2vh, 32px)`；页码锚在 `bottom: clamp(48px, 4.8vh, 76px)`——它们不能撞上。

### 排印原则
Newsreader-400 + Hanken-600-大写-tracking + DM-Mono-tracking 的组合就是系统的声线。换掉这三条面孔/字重/大小写规则中的任何一条，都读成另一套设计系统。允许通过已加载的 Newsreader 斜体做行内 `<em>`，以及 manifesto 的编辑斜体配 `.roman` 翻转处理。不用下划线。

行高在顶部收紧：display-hero / vbig-numeral 为 0.92，display-chapter 为 1.0，正文为 1.5。紧展示 + 开放正文的对比，才给出系统的趋势报告节奏。

## 版式

### 画布系统
画布是 `100vw × 100vh`——全视口，溢出隐藏。每一张 `.slide` 绝对定位填满视口；同一时间一张幻灯片带着 `.active`（opacity 1，pointer-events auto）。过渡是 280ms 透明度淡入淡出。

`.stage` 包装器坐在 `.deck` 里面（`position: fixed; inset: 0`），提供奶油背景加上永久的 `::before` 方格纸网格。

### 边距与内边距阶梯
| Token | 值 | 用途 |
|---|---|---|
| `{spacing.edge}` | clamp(36px, 3.6vw, 80px) | 内容、页码、发丝的标准幻灯片边内缩 |
| `{spacing.edge-inner}` | clamp(60px, 8vw, 160px) | manifesto 式居中陈述用的更紧内缩 |
| `{spacing.pad-top}` | clamp(76px, 8vh, 130px) | 索引/数据/表格框内部的顶内边距，在顶发丝下方 |
| `{spacing.pad-bottom}` | clamp(100px, 10vh, 150px) | 索引/数据/表格框内部的底内边距，在底发丝上方 |
| `{spacing.gap-lg}` | clamp(28px, 3vw, 56px) | 一页内主要区域之间的大间距 |
| `{spacing.gap-md}` | clamp(20px, 2.2vh, 36px) | 标准元素间距 |
| `{spacing.gap-sm}` | clamp(14px, 1.6vh, 24px) | 紧间距——chrome 条内部间隙、落款到引文间隙 |
| `{spacing.gap-xs}` | clamp(10px, 1.2vh, 18px) | 竖排行间距、最小元素间距 |

### 通用页框
每一页带着四件套 chrome 框：
1. **顶发丝** —— 1.5px 实线钴蓝，距顶约 2.6vh，左右以内缩 `{spacing.edge}`。
2. **底发丝** —— 1.5px 实线钴蓝，距底约 2vh，左右以内缩 `{spacing.edge}`。
3. **页码** —— DM Mono 钴蓝锚在右下，距底约 4.8vh（底发丝上方）。
4. **导航提示** —— DM Mono 钴蓝 40% 透明度锚在左下，与页码同一垂直高度。

这个框由 `.hairlines` 和 `.pagenum` / `.nav-hint` 规则自动渲染——每一张新页都继承它。

嵌套的 **`.frame` 内容矩形** 坐在索引、数据、表格和章节版式的 chrome 里面。它绝对定位，`inset: {spacing.pad-top} {spacing.edge} {spacing.pad-bottom}`，作为真正的内容容器。

### 构图模式
在页框里，内容通常走这些构图动作之一（不是枚举可用版式——这些是描述性的，不是规定性的）：
- 一个 `topbar` 块（左 Newsreader 标题、右等宽 lab-tag、底下 1.5px 钴蓝线）在主内容区上方。
- 一根 pixel-glitch 柱锚在内容区右缘（偶尔在左，如 colophon）。
- 一块 QR-block 补丁作为小标点（通常右上角）。
- 一列竖排等宽标签锚在一条边上。
- 一份密账本或索引，等 flex 行用淡钴蓝分割线分开。

## 纵深与层次

### 平面加结构线
Cobalt Grid 没有投影、没有抬起的卡片、没有圆角表面、没有渐变。每个元素都坐在同一平面上。

纵深信号完全是结构的：
- **1.5px 钴蓝线** —— 顶/底幻灯片发丝、topbar 线、落款线。
- **1px 淡钴蓝分割线** —— 索引列表、表格和账本里的行分隔。
- **方格纸网格** —— 10% 透明度钴蓝背景创造被量度过的平面感。
- **Pixel-glitch 装饰** —— 竖向扫描线柱加视觉纹理，没有 z 轴抬升。
- **QR-block 补丁** —— 因纸填充和 1.5px 纸色外扩阴影，在网格+glitch 背景上读成独立图形对象（功能上是「反阴影」——把网格推开，让 QR 马赛克保持可读）。

QR-block 的 1.5px 纸色外扩是系统里*唯一*像阴影的效果，目的是在 pixel-glitch 柱上保住可读性，不是创造抬升。没有 z 轴纵深。

## 形状与处理

### 圆角
| 值 | 用途 |
|---|---|
| 0 | 每一个结构元素——框、卡片、账本行、QR 格、pixel-glitch 矩形、图表、表格 |
| 50%（圆） | 无——Cobalt Grid 没有圆形元素 |

系统用**零圆角**。每一种形状都是严格矩形。这对编辑系统不寻常，是趋势报告身份的一部分。

### 描边粗细
- **1.5px solid `{colors.ink}`** —— 主结构线：顶/底幻灯片发丝、topbar 底线、表头行底边、图表基线。
- **1px solid `{colors.ink}`** —— 引文 byline 上方的落款线、manifesto 落款顶边。
- **1px solid `{colors.ink-faint}`**（18% 透明度）—— 密列表 / 表格 / 账本条目之间的淡行分割线。
- **1px solid `{colors.grid}`**（10% 透明度）—— 每一页后面永久的方格纸网格。
- **`{colors.paper}` 的 1.5px box-shadow** —— QR-block 可读性外扩（功能性的，不是装饰）。

所有结构边框都是钴蓝。不存在彩色边框（没有「彩色」——只有不同透明度的钴蓝）。

### 装饰元素类型

**Pixel-glitch 柱** —— 阶梯状竖柱，渲染为行内 SVG。每一步是一块矩形，奶油底上均匀间隔的钴蓝竖扫描线。柱往下走时台阶宽度递减（或反过来），造出「故障」像素化效果。锚在幻灯片一条边上（通常右侧），绝对定位，z-index 3，pointer-events 关闭。仅装饰——尺寸从紧凑的 16vw × 全高次级用途，到 32vw × 全高招牌封面装饰。透明度 0.6–1.0 视语境而定（当背景用时更低，当主装饰用时全力）。

**QR-block 补丁** —— 8×8 格网格（有的 `.on` = 实心钴蓝，有的默认 = 纸）形成 QR 码式马赛克。坐在纸填充背景上，4px 内部内边距和 1.5px 纸色外扩（叠在 pixel-glitch 柱上时保住可读性）。典型尺寸 58–100px 方。用作构图标点——通常右上角。

**竖排标签列** —— 一列 DM Mono 标签，用 `writing-mode: vertical-rl` 和 `text-orientation: mixed` 写，把拉丁文字顺时针转 90°。锚在右缘，垂直居中，均匀间隔。读起来像沿幻灯片边叠放的目录式元数据。

**Topbar（带线）** —— 一行 flex，左 Newsreader 标题、右小号等宽 lab-tag，用 1.5px 实线钴蓝底边与下方内容分开。通用区块标题模式。

**Frame** —— 绝对定位的内容容器，`inset: {spacing.pad-top} {spacing.edge} {spacing.pad-bottom}`。装这一页真正的内容，同时让它离开发丝框、页码和导航提示。

**索引列表** —— 2×3 等 flex 行网格，每行一列 56px num-tag + 一列内容（Newsreader row-headline 和 Hanken 正文段），用 1px 淡钴蓝底边分开。

**Pixel-stack 柱状图** —— 一行 8 根竖「叠」，每根是 flex column-reverse 的小水平格（默认 10% 钴蓝关，.on 实心钴蓝）。格数代表数值。柱下方一根 1.5px 钴蓝顶边配等宽刻度标签作轴。把数据画成由网格单元组成的像素化柱——直接呼应 pixel-glitch 装饰。

**账本表格** —— 密行 flex 列，每行 5 列网格（76px num-tag / 0.6fr 姓名 / 1.4fr 描述 / 0.7fr mood-tag / 0.5fr delta-tag），用 1px 淡钴蓝底边分开。表头行用 1.5px 实线钴蓝。Delta tag 经 `::before` 用 `↑` / `↓` / `—` 前缀。

**Manifesto** —— 居中陈述，`{typography.display-manifesto}` Newsreader，斜体 `<em>` 正文里带行内 `.roman`（非斜体）强调瞬间。下方：1px 钴蓝顶边，Hanken who-tag 和等宽 meta-tag 并排。

**Quote** —— Hanken kicker 在 `{typography.display-quote}` Newsreader 引出上方，底下 1px 钴蓝顶边落款行。右缘配一根紧凑 pixel-glitch 柱。

**Colophon** —— 右对齐收束版式。大号 `{typography.display-closing}` Newsreader 标题右对齐，上方 kicker。Pixel-glitch 柱锚在左缘（镜像封面）。页脚 3–4 栏网格的段落致谢。

## 宜与忌

### 宜
- 每一个 Newsreader 元素都设为字重 400，颜色 `{colors.ink}`。克制字重的细罗马衬线就是文学色域的身份。
- 每一个标签、kicker 和微文字都用 Hanken Grotesk 字重 600 大写，字距 0.16em+，颜色 `{colors.ink}`。
- 每一个 chrome 元素（页码、等宽 tag、刻度标签、竖排）都用 DM Mono，tracking 0.04–0.08em，颜色 `{colors.ink}`。
- 让永久方格纸网格留在每一页后面。网格就是系统——关掉它会拆掉身份。
- 每一页都维持顶底 1.5px 钴蓝发丝，页码和导航提示坐在底发丝上方。
- 在宣言页（cover、chapter、quote、colophon）上把 pixel-glitch 柱当系统的主装饰动作。
- 构图需要独立图形锚点时，把 pixel-glitch 与 QR-block 补丁配对——QR 的纸填充让它在故障线前保持可读。
- 在 index、data 和 table 版式上用 `topbar + 1.5px 钴蓝线` 模式作为标准区块标题处理。
- 密列表、表格和账本的行之间用 1px 淡钴蓝分割线。
- 把图表画成网格单元的 pixel-stack 柱（钴蓝开 / 钴蓝 10% 关）。Pixel-stack 柱处理呼应装饰故障，统一视觉语言。

### 忌
- 不要引入第二墨色。系统严格双色：奶油纸 + 钴蓝墨。第二色相会拆掉油印身份。
- 不要把 Newsreader 标题渲染成字重 600 或 700。只用 400 是招牌。
- 不要关掉或藏起方格纸网格。它是画布色调，不是可选装饰。
- 不要在一页上关掉顶/底发丝。它们是框——每一页都带着它们。
- 不要圆任何角。每一种形状都是严格矩形；系统没有圆形元素。
- 不要加投影、抬起的卡片或渐变填充。纵深是结构的（线 + 网格 + glitch），不是 z 轴。
- 不要用不带 0.16em+ tracking 的 Hanken 大写。没 tracking 的 Hanken 大写读起来像没处理过。
- 不要把页码直接放在底发丝上。它坐在 `bottom: clamp(48px, 4.8vh, 76px)`，发丝上方留出清楚空间。
- 不要渲染没有纸填充和 1.5px 纸外扩的 QR-block。填充才是在 pixel-glitch 柱上保住 QR 可读性的东西。
- 不要把 manifesto、quote 或 colophon 版式挤满。那些版式刻意露出网格——塞满会拆掉沉思色域。

## 响应式行为

Cobalt Grid 是一套视口流体的 1920×1080 演示系统，全程用 `clamp()` 和相对视口单位。源码里没有显式响应断点——每个尺寸都在最小和最大之间缩放。

### 缩放行为
- Display-hero 从最小视口约 100px 缩放到最大约 200px。
- 正文从 14px 到 15px（刻意窄区间——正文保持紧凑）。
- 方格纸网格从 28px 格（较小视口）缩放到 44px 格（较大视口），大致维持幻灯片宽度上 50–80 格。
- 边内缩从 36px 到 80px。
- 1.5px 发丝和 1px 行分割线是固定的，不缩放。

### 演示行为
- 幻灯片以 280ms 透明度过渡交叉淡入。
- 导航由 JS 驱动（源码包含 `.deck` / `.slide.active` 模式）；适用典型键盘箭头 / 空格惯例。
- 左下导航提示以 40% 透明度等宽钴蓝显示交互指引。

### 打印 / 导出
没有显式处理。每一页是 100vw × 100vh 块；导出工作流应对每页在 1920×1080 截图。网格和发丝叠层应在 PDF 捕获里正确渲染（没有混合模式或滤镜）。

## 中日韩与国际内容

### 推荐中文配对

| 角色 | 拉丁字体 | 推荐中文配对 | 来源 |
|---|---|---|---|
| Display / Headline（Newsreader 400） | Newsreader | 思源宋体 Noto Serif SC 700 | Google Fonts |
| Body / Label（Hanken Grotesk 400–600） | Hanken Grotesk | 思源宋体 Noto Serif SC 400 | Google Fonts |
| Chrome / Mono（DM Mono） | DM Mono | DM Mono（仅拉丁/数字——等宽 chrome 保持拉丁） | Google Fonts |

### 中英混排策略

用 **策略 A —— 单字体栈带回退**：在同一 `font-family` 栈里把 Noto Serif SC 声明在拉丁字体*之后*，这样拉丁字形用 Newsreader / Hanken Grotesk 渲染，CJK 字形自动落到 NSC。等宽 chrome 保持仅拉丁/数字——页码、刻度和竖排 tag 不需要 CJK 回退（DM Mono 按设计没有 CJK 字形）。

### 加载

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400..500;1,6..72,400..500&family=Hanken+Grotesk:wght@400..700&family=DM+Mono:wght@400..500&family=Noto+Serif+SC:wght@400;700&display=swap" rel="stylesheet">
```

```css
:root {
  --font-display: "Newsreader", "Noto Serif SC", Georgia, serif;
  --font-body: "Hanken Grotesk", "Noto Serif SC", sans-serif;
  --font-mono: "DM Mono", ui-monospace, monospace;
}
/* Headlines use Noto Serif SC 700; body uses Noto Serif SC 400. */
```

### 通用 CJK 调整

- **行高**：把 CJK 正文字行高提到约 1.7（从 1.5）——汉字比拉丁小写需要更多垂直呼吸。
- **字距**：汉字跑段把 `letter-spacing` 清零（0.16em+ 的 Hanken 大写 tracking 会打碎汉字节奏）。只在拉丁 span 上保留紧 tracking。
- **大小写变换**：内容是汉字时，任何 micro/标签/kicker 都去掉 `text-transform: uppercase`——中文没有大小写；强制大写对汉字无效，但会弄坏里面混排的拉丁缩写。
- **标点**：中文句子用中文全角标点（，。：；「」），拉丁用半角（`,.:;""`）。永远不要把半角标点混进中文句子。
- **标题不加句号**：中文标题惯例省略末尾 。——从展示字符串里拿掉。
- **盘古之白**：相邻汉字与拉丁/数字跑段之间插入细空格（或普通空格）（例如 `2026 年`、`AI 产品`）。改善混排可读性。
- **一句一句一种字体**：不要在句子中间切换 CJK 家族。给定一段文字跑段只选一个字重的 Noto Serif SC，永远不要在一个短语里用两个。

### 美学说明

Noto Serif SC（思源宋体）是 Newsreader 自然的汉字搭档——两者都是安静的文学衬线，粗细调制在非常大的展示字号上仍站得住（vbig-numeral 到 18vh / 240px）。奶油上的钴蓝双色规则吸收中文无需谈判，因为只有一种墨色可分配。NSC 700 扛 Newsreader 400 会在 100–200px 出现的展示瞬间；NSC 400 扛正文和标签。DM Mono chrome 层（页码、竖排 tag、刻度）故意保持仅拉丁/数字——`编号 001` 渲染成 DM Mono 的拉丁 "001"，汉字前缀用 Hanken/NSC，保住等宽目录 chrome 的「技术规格」声线。方格纸网格、pixel-glitch 柱和 QR-block 装饰与内容无关，任何语言都同样读。用 `writing-mode: vertical-rl` 写的竖排标签对汉字也成立——中文才是原来的竖写脚本——但同一竖向跑段里混拉丁和汉字会把汉字转正、拉丁仍转 90°；按语言隔离跑段。

### 已知 CJK 缺口

Noto Serif SC 没有斜体轴（中文活字历史上没有斜体），所以内容是汉字时，manifesto 版式的斜体-Newsreader-配-`.roman`-翻转强调模式会塌掉。用字重对比（NSC 700 对 NSC 400）或淡钴蓝调（`{colors.ink-faint}`）来找回强调色域。Newsreader 的光学尺寸轴（6..72）没有 NSC 对等——文学「这是小号图注」的光学细化对汉字不可用，但以 NSC 的品质这很少被注意到。

## 迭代指南

1. 每一张新页继承永久方格纸网格、顶底 1.5px 钴蓝发丝、右下页码和左下导航提示。不要逐页写这些——它们活在 `.stage` 和 `.hairlines` 上。
2. 每一个新标题都用字重 400 的 Newsreader，颜色 `{colors.ink}`。不加粗；不上色。
3. 每一个新标签都用 Hanken Grotesk 字重 600 大写，字距 0.16em+，颜色 `{colors.ink}`。
4. 每一个新 chrome 元素都用 DM Mono，颜色 `{colors.ink}`，tracking 0.04–0.08em。
5. index / data / table 版式上的新内容页用 topbar（左 Newsreader 标题 + 右 Hanken lab-tag）配 1.5px 钴蓝底线。
6. 新图表页用 pixel-stack 处理——column-reverse 叠里钴蓝开 / 钴蓝 10% 关的格。不要引入单块实心填充柱状图。
7. 新宣言页（cover、chapter、quote、colophon）用 pixel-glitch 柱作主装饰。构图需要独立图形锚点时配 QR-block。
8. 密列表里的新行分割线用 1px solid `{colors.ink-faint}`（18% 透明度），不要全力钴蓝。全力钴蓝留给主要结构线。
9. 新组件继承零圆角、无阴影、无渐变的平面。如果一个组件打破其中任何一条，先重设计再加入。
10. 系统有一种墨色（`{colors.ink}`）和一种表面（`{colors.paper}`）。新构图永远不要引入第三色或第三表面调（paper-2 可用但很少需要）。

## 已知缺口

- Pixel-glitch 柱渲染为按用途手写的行内 SVG；没有生成组件——调整阶梯图案需要直接改 SVG 标记。
- QR-block 8×8 格图案按用途手写；每个实例手工放 `.on` 格。没有 QR 码生成逻辑。
- Pixel-stack 柱状图的格数硬编码在标记里；没有把数值翻译成开格数的数据绑定层。
- 竖排标签列用 `writing-mode: vertical-rl`；这在现代浏览器里成立，但这种朝向上混排拉丁/CJK 的渲染可能因渲染引擎而异。
- Manifesto 版式的斜体配 `.roman` 翻转模式（斜体 Newsreader 正文里含行内非斜体 `.roman` span 做强调）是典型斜体强调的反转——规则活在 manifesto 专用 CSS 里，没有泛化。
- QR-block 上 1.5px 纸色外扩是当反阴影用的 `box-shadow`（它把纸填充往外延，清掉 QR 格后面的网格）。这是系统里唯一的 `box-shadow`，不应被挪用做抬升。
- Colophon 的 pixel-glitch 柱锚在左缘（镜像封面）；其他页锚在右缘——方向性是逐页的，写新宣言版式时应考虑。
- 方格纸网格格尺寸经 `clamp` 在 28–44px 之间缩放——极端宽高比下，幻灯片宽度上的网格数可能感觉不均匀。
- 系统加载三套 Google Fonts 家族（Newsreader、Hanken Grotesk、DM Mono）及多个字重——初次渲染需要字体加载成功，以免回退到 Georgia/Helvetica 改变视觉节奏。
