---
version: alpha
name: Neo-Grid Bold
description: A heavy editorial poster system built on a strict 12-column × 8-row block grid with neon-yellow accents on putty-ecru. Space Grotesk at weight 700 in strict uppercase carries every display moment; JetBrains Mono carries every label and metadata tag. Each slide reads as a magazine spread divided into colored panels — paper-ecru, ink-black, and electric lemon-yellow trading roles across cells. The aesthetic borrows from contemporary editorial print, brutalist annual reports, and the populist-poster end of design week showcases.

colors:
  paper: "#F5F4EF"
  bg: "#ECECE8"
  ink: "#0A0A0A"
  accent-lemon: "#E6FF3D"
  muted: "#8A8A85"
  stage-bg: "#1A1A1A"

color-aliases:
  line: ink
  primary-bg: bg
  card-bg: paper

typography:
  display:
    fontFamily: "Space Grotesk, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 132px
    fontWeight: 700
    lineHeight: 0.92
    letterSpacing: -0.02em
    textTransform: uppercase
  title:
    fontFamily: "Space Grotesk, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 88px
    fontWeight: 700
    lineHeight: 0.95
    letterSpacing: -0.015em
    textTransform: uppercase
  subtitle:
    fontFamily: "Space Grotesk, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -0.01em
    textTransform: uppercase
  section-num:
    fontFamily: "Space Grotesk, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 320px
    fontWeight: 700
    lineHeight: 0.85
    letterSpacing: -0.05em
  stat-num:
    fontFamily: "Space Grotesk, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 156px
    fontWeight: 700
    lineHeight: 0.9
    letterSpacing: -0.03em
  stat-num-lg:
    fontFamily: "Space Grotesk, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 240px
    fontWeight: 700
    lineHeight: 0.85
    letterSpacing: -0.04em
  stat-num-sm:
    fontFamily: "Space Grotesk, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 96px
    fontWeight: 700
    lineHeight: 0.9
    letterSpacing: -0.03em
  card-headline:
    fontFamily: "Space Grotesk, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 44px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -0.01em
    textTransform: uppercase
  card-h3:
    fontFamily: "Space Grotesk, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 30px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.005em
    textTransform: uppercase
  body:
    fontFamily: "Space Grotesk, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.35
  body-sm:
    fontFamily: "Space Grotesk, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.45
  label:
    fontFamily: "JetBrains Mono, ui-monospace, monospace"
    fontSize: 24px
    fontWeight: 400
    letterSpacing: 0.08em
    textTransform: uppercase
  label-sm:
    fontFamily: "JetBrains Mono, ui-monospace, monospace"
    fontSize: 16px
    fontWeight: 400
    letterSpacing: 0.08em
    textTransform: uppercase
  label-xs:
    fontFamily: "JetBrains Mono, ui-monospace, monospace"
    fontSize: 14px
    fontWeight: 400
    letterSpacing: 0.12em
    textTransform: uppercase
  pagenum:
    fontFamily: "JetBrains Mono, ui-monospace, monospace"
    fontSize: 24px
    fontWeight: 400
    letterSpacing: 0.04em

spacing:
  frame-inset: 40px
  grid-gap: 12px
  grid-gap-lg: 18px
  card-pad-sm: "24px 28px"
  card-pad-md: "28px 32px"
  card-pad-lg: "36px 32px"
  card-pad-xl: "40px 44px"

canvas:
  width: 1920px
  height: 1080px

components:
  frame:
    position: "absolute; inset: 40px"
    display: grid
    gridTemplateColumns: "repeat(12, 1fr)"
    gridTemplateRows: "repeat(8, 1fr)"
    gap: "{spacing.grid-gap}"
    description: "The universal slide frame — a 12-column × 8-row CSS grid inset 40px from each slide edge with 12px gaps between cells. Every slide composes its layout by spanning cells inside this frame."
  card:
    background: "{colors.paper}"
    position: relative
    overflow: hidden
    description: "Generic colored panel. Paper is the default fill; .ink switches to black with paper text; .lemon switches to yellow with ink text; .photo switches to deep-black with white text for image regions."
  card-ink:
    background: "{colors.ink}"
    color: "{colors.paper}"
    description: "Inverted card — black background, paper text. Used as a contrast block in any composition."
  card-lemon:
    background: "{colors.accent-lemon}"
    color: "{colors.ink}"
    description: "Yellow accent card — full neon-yellow fill with ink text. The system's loudest signal."
  pagenum:
    position: "absolute; left: 0; bottom: 0"
    background: "{colors.paper}"
    color: "{colors.ink}"
    padding: "14px 22px"
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 24px
    letterSpacing: 0.04em
    description: "Bottom-left page-number tag in the format '01 / 12'. Three variants: default (paper bg), .invert (ink bg), .lemon (yellow bg)."
  corner-mark:
    position: "absolute; top: 22px; right: 22px"
    width: 36px
    height: 36px
    display: "grid 2x2"
    gap: 4px
    description: "Top-right 2x2 block mark — three solid currentColor squares plus one transparent. A small structural identity stamp."
  blockmark:
    width: 56px
    height: 56px
    display: "grid 2x2"
    gap: 4px
    description: "Larger 2x2 block stamp with diagonal squares filled — used as a brand mark on covers and dividers. May be sized 56px, 96px, or larger."
  qr-tile:
    width: 90px
    height: 90px
    display: "grid 5x5"
    description: "Decorative QR-pattern tile composed of a 5x5 grid of black squares with some accent-lemon squares interspersed. Decorative, not a real scannable code."
  table-cell:
    padding: "18px 22px"
    borderBottom: "1.5px solid {colors.ink}"
    borderRight: "1.5px solid {colors.ink}"
    fontSize: 24px
    lineHeight: 1.35
    description: "Comparison-matrix cell. Solid hairline ink dividers on bottom and right; last column has no right border."
  table-head-row:
    background: "{colors.ink}"
    color: "{colors.paper}"
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 14px
    letterSpacing: 0.12em
    textTransform: uppercase
    description: "Inverted table header — black row with paper mono uppercase text."
  pill-yes:
    background: "{colors.accent-lemon}"
    color: "{colors.ink}"
    padding: "6px 14px"
    description: "Affirmative pill in a comparison cell — yellow fill, ink text, mono uppercase."
  pill-part:
    background: "{colors.paper}"
    color: "{colors.ink}"
    border: "1.5px solid {colors.ink}"
    description: "Partial-state pill — paper fill, ink border, ink text."
  pill-no:
    background: "{colors.ink}"
    color: "{colors.paper}"
    description: "Negative pill — black fill, paper text."
  arrow:
    width: 64px
    height: 64px
    description: "Inline SVG arrow glyph (right-pointing) at 64px square. Used as a flow indicator between process steps and as an out-of-cell pointer on stat cards."
  highlight-mark:
    background: "{colors.accent-lemon}"
    color: "{colors.ink}"
    padding: "0 6px"
    description: "Inline <mark> element — yellow background swatch wrapping one or more words inside a headline for emphasis."
  bar-fill-ink:
    background: "{colors.ink}"
    description: "Solid black vertical bar for chart series A."
  bar-fill-lemon:
    background: "{colors.accent-lemon}"
    border: "1.5px solid {colors.ink}"
    description: "Yellow vertical bar with ink border for chart series B."
  copyright:
    position: "absolute; left: 22px; bottom: 22px"
    fontFamily: "JetBrains Mono, ui-monospace, monospace"
    fontSize: 16px
    lineHeight: 1.4
    color: "{colors.ink}"
    opacity: 0.85
---

## 概览

Neo-Grid Bold 是一套**重量级编辑海报系统**，建立在单一结构前提上：每一页都是距幻灯片边缘内缩 40px 的 12 列 × 8 行 CSS 网格，单元格之间 12px 间隙。构图就是把彩色面板指派到网格跨度上——`grid-column: 4 / span 5` 和 `grid-row: 1 / span 5` 就是描述版式的方式。网格是刚性的；视觉变化来自 `{colors.paper}`、`{colors.ink}` 和 `{colors.accent-lemon}` 面板在单元格里怎么排布。

字体栈刻意收窄。**Space Grotesk** 字重 700 承担每一个展示瞬间，严格全大写并带负字距。正文跑字重 400、大小写混排。**JetBrains Mono** 字重 400 承担每一个标签、页码、坐标轴标记和元数据字符串——始终全大写，正字距 0.08–0.12em。没有第三张脸。粗重 Space Grotesk 全大写与 JetBrains Mono 全大写之间的对比，就是系统的主排印节奏。

色板有三个工作色，外加一块腻子色表面。**Paper**（`{colors.paper}` —— 温暖本色偏白）是默认面板填色。**Ink**（`{colors.ink}` —— 近黑）是结构色：纸上的字、反相面板的填色、所有分割线、所有规则线。**Accent Lemon**（`{colors.accent-lemon}` —— 电霓虹黄 #E6FF3D）是大声信号——用作面板填色、标题里的高亮 `<mark>` 色块，以及图表的第二系列。**Putty BG**（`{colors.bg}`）是略冷一点的本色，坐在 40px 幻灯片内缩之外，像装裱卡纸（passe-partout）一样框住构图。**Muted graphite** 出现在 token 列表里，实务中很少用。

纵深完全靠**面板邻接与色彩对比**，不用阴影。卡片不带 box-shadow；卡片没有圆角；卡片没有描边（表格单元格和 pill 轮廓除外，它们用 1.5px solid ink）。一页的视觉重量，由填了 `{colors.ink}` vs `{colors.accent-lemon}` vs `{colors.paper}` 的单元格数量决定。三块黄面板的构图，读起来比只有一块黄面板激进得多。

**密度哲学：密。** 当 12×8 网格被不同跨度、不同颜色的面板填满时，Neo-Grid Bold 读起来才有权威。只有一两块面板、大片空网格的一页读起来像坏掉；系统设计成编辑海报，而海报就是密的。预期模式是每页 4–8 块面板，每块占不可忽略的单元格跨度，网格从角到角用满。例外是章节分隔页：单个 320px 章节数字占满网格的一整扇——但即便如此，画布其余部分仍由第二块对比色面板填满。

**关键特征：**
- 通用 12 列 × 8 行 CSS 网格（`{components.frame}`），距每边内缩 40px，单元格间隙 12px。
- 三色面板系统：纸本色（`{colors.paper}`）为默认，墨黑（`{colors.ink}`）做反相块，强调柠檬黄（`{colors.accent-lemon}`）做信号块。
- 每个展示元素都用 Space Grotesk 字重 700 全大写加负字距。
- 每个标签、页码、坐标轴标记都用 JetBrains Mono 全大写，字距 0.08–0.12em。
- 招牌 corner-mark 与 blockmark——小型 2×2 色块印章，充当装饰身份标签。
- 行内 `<mark>` 把标题里的词包进霓虹黄色块——系统的标题强调机制。
- 持续页码标签（`{components.pagenum}`）锚定在每一页左下。
- 无圆角、无投影、无渐变（照片区风格化噪点纹理除外）。
- 统计数字可放大到 240px 甚至 320px——允许字体主宰整块面板。

## 颜色

### 色板

- **Paper**（`{colors.paper}` — #F5F4EF）：温暖本色偏白。默认面板填色，反相时的默认文字色，以及任何「中性」卡片的画布。比纯白略奶油——选它是为了让霓虹黄强调不在上面振颤。
- **BG (Putty)**（`{colors.bg}` — #ECECE8）：略冷的本色，坐在 40px 幻灯片内缩之外，像装裱卡纸一样框住网格构图。每一页周围 40px 的腻子色边，就是系统的通用画框。
- **Ink**（`{colors.ink}` — #0A0A0A）：结构近黑。用于纸上所有文字、所有反相面板填色、所有分割线、所有表格单元格描边、所有 pill 轮廓。不是纯 #000——略软一点。
- **Accent Lemon**（`{colors.accent-lemon}` — #E6FF3D）：电霓虹黄。信号色。用作面板填色、标题里的行内 `<mark>` 高亮色块、第二图表系列、肯定态 pill 填色，以及页码变体背景。从不当文字色（这黄太浅，在任何表面上都不能当字来读）。
- **Muted**（`{colors.muted}` — #8A8A85）：预留的石墨调，出现在 token 列表里，但只在照片区标签上以低不透明度使用。可用于弱化文字，但很少部署。
- **Stage BG**（`{colors.stage-bg}` — #1A1A1A）：1920×1080 幻灯片画布之外的视口背景。这是 deck-stage 容器色，不属于幻灯片设计本身。

### 默认

- **默认幻灯片画布背景**：`{colors.bg}` —— 作为每个网格构图周围 40px 腻子色画框可见。
- **默认面板填色**：`{colors.paper}`。拿不准时，面板就是纸色。
- **默认主标题色**：纸或柠檬面板上用 `{colors.ink}`；墨色面板上用 `{colors.paper}`。
- **默认正文字色**：纸/柠檬上用 `{colors.ink}`；墨色上用 `{colors.paper}`。
- **默认标签 / 元数据色**：纸上用 `{colors.ink}`，不透明度 0.7–0.85 以闷住；墨上用 `{colors.paper}`，不透明度 0.7–0.85。
- **默认图表系列色**：系列 A 用 `{colors.ink}`；系列 B 用 `{colors.accent-lemon}`（带 1.5px ink 描边）。
- **标题内的默认强调机制**：用 `<mark>` 包起来，在墨字上铺霓虹黄色块。这是系统的主标题级强调。
- **默认肯定态**：`{colors.accent-lemon}` 填色。默认否定态：`{colors.ink}` 填色。默认中性态：`{colors.paper}` 填色加 `{colors.ink}` 描边。

霓虹黄是系统唯一的彩色强调——绝不要换成红、蓝或任何第三色。黄的角色是拉眼睛，不是传达语义（它不是语义上的「警告」或「高亮」；它只是信号）。

## 字体

### 字族

系统用两套 web 字体：**Space Grotesk**（字重 400、500、700）承担所有展示与正文，**JetBrains Mono**（字重 400、500）承担所有标签与元数据。没有第三张脸——没有衬线、没有斜体、没有展示手写。系统性格活在 Space Grotesk 700 全大写与 Space Grotesk 400 大小写混排的字重对比里，再加上 JetBrains Mono 的结构等宽标签。

一条具体的行内混用规则：**Space Grotesk 标题里的 `<em>` 标签把颜色切到 `{colors.accent-lemon}` 并保持直立**（font-style 归一成非斜体）。Em 被改造成黄色行内换色，像 `<mark>` 色块但不带背景填色。

第二条行内混用规则：**`<mark>` 元素把 Space Grotesk 标题里的词包进霓虹黄色块，左右 padding 0 6px**，做出反复出现的荧光笔强调——这是系统的招牌。

### 字号阶梯

| Token | 字号 | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.section-num}` | 320px | Space Grotesk | 700 | 章节分隔面板里的英雄章节序数 |
| `{typography.stat-num-lg}` | 240px | Space Grotesk | 700 | 主打大型数值统计 |
| `{typography.stat-num}` | 156px | Space Grotesk | 700 | 标准统计数字 |
| `{typography.display}` | 132px | Space Grotesk | 700 | 封面、章节或英雄展示标题 |
| `{typography.stat-num-sm}` | 96px | Space Grotesk | 700 | 小卡片里的紧凑统计数字 |
| `{typography.title}` | 88px | Space Grotesk | 700 | 主内容页标题 |
| `{typography.subtitle}` | 56px | Space Grotesk | 700 | 次级标题、区域标题 |
| `{typography.card-headline}` | 44px | Space Grotesk | 700 | 面板填满尺度的卡片标题 |
| `{typography.card-h3}` | 30px | Space Grotesk | 700 | 较小卡片里的副标题 |
| `{typography.body}` | 28px | Space Grotesk | 400 | 功能卡片里的正文段落 |
| `{typography.label}` | 24px | JetBrains Mono | 400 | 标准等宽标签或 kicker |
| `{typography.body-sm}` | 22px | Space Grotesk | 400 | 密卡片里的紧凑正文 |
| `{typography.pagenum}` | 24px | JetBrains Mono | 400 | 页码标签（例如 "01 / 12"） |
| `{typography.label-sm}` | 16px | JetBrains Mono | 400 | 次级元数据标签、版权文字 |
| `{typography.label-xs}` | 14px | JetBrains Mono | 400 | 坐标轴标签、表头文字、小字 |

### 默认

- **默认主章节标题**：`{typography.title}`（88px）——内容页的主力标题。
- **默认封面或章节开场展示**：封面用 `{typography.display}`（132px）；章节分隔序数用 `{typography.section-num}`（320px）。
- **默认正文段落字号**：`{typography.body}`（28px）。密的多卡片页降到 `{typography.body-sm}`（22px）。
- **默认标签 / 元数据字号**：独立等宽标签用 `{typography.label}`（24px）；行内元数据用 `{typography.label-sm}`（16px）。
- **默认统计数字**：`{typography.stat-num}`（156px）。只有统计占满整块主打面板时，才伸手去拿 `{typography.stat-num-lg}`（240px）。
- **任何展示元素的默认字重**：700。本系统不存在其他字重的展示。
- **正文默认字重**：400。

拿不准时，用 `{typography.title}` 做这一页的主文字瞬间，再配 `{typography.body}` 做支撑文案。

### 招牌处理

对应元素类型一旦用上，这些处理**不可省略**：

- **每一个 Space Grotesk display、title、subtitle、card-headline 和统计数字都是全大写**，并带负字距（按尺度从 -0.005 到 -0.05em）。本系统不存在大小写混排的展示。
- **正文是字重 400 的大小写混排。** 正文从不全大写。
- **每一个 JetBrains Mono 元素都是全大写**，正字距至少 0.08em。
- **标题里的 `<mark>` 元素始终用 `{colors.accent-lemon}` 背景、`{colors.ink}` 文字、左右 padding 0 6px。** 黄色荧光笔色块是系统的标题强调信号。
- **标题里的 `<em>` 元素切到 `{colors.accent-lemon}` 颜色并保持直立（font-style: normal）。** 不用斜体字形。
- **负字距随字号缩放**：较小标题用 -0.005em 到 -0.015em；较大展示用 -0.02 到 -0.05em。字距越紧，标题读起来越压缩、越粗野主义——320px 时 -0.05em 是对的。
- **页码始终是 JetBrains Mono 24px、字距 0.04em**，格式 `01 / 12`，个位数补零，斜杠分隔。

### 排印原则

节奏是**粗重全大写展示 + 轻量大小写混排正文 + 小号全大写等宽标签**。三个模式里换掉任何一个，编辑声线就断。正文全大写读成在喊的段落。展示用大小写混排读成另一套设计系统。等宽用大小写混排读成代码，不是编辑元数据。

不用斜体字形。`<em>` 和 `<mark>` 标签被改造成颜色/高亮开关，不是斜体强调。不用下划线。正文里不用粗体——强调靠把标题隔离在自己的单元格里完成。

## 布局

### 画布系统

系统瞄准**固定 1920×1080 画布**，渲染在负责缩放到视口的 `<deck-stage>` web component 里。所有尺寸都是 `px`（不是 vw/vh）——字号、padding、网格间隙、内缩值全部像素固定。构图按 1920×1080 设计，舞台把整份文稿按比例缩放。

deck stage 之外的视口背景是 `{colors.stage-bg}`（#1A1A1A）——深灰画框，把明亮幻灯片在浏览器 chrome 里视觉锚定住。

### 通用框架

每一页带着一个 `.frame` div，定位 `absolute; inset: 40px`，并设 `display: grid; grid-template-columns: repeat(12, 1fr); grid-template-rows: repeat(8, 1fr); gap: 12px`。这是系统的结构常量：12 列 × 8 行网格、间隙 12px，距幻灯片边缘内缩 40px。有些页面变体会把网格间隙加到 16–18px 换呼吸，但列/行数和 40px 内缩永不改。

构图完全靠在这个网格里跨单元格完成。占 `grid-column: 1 / span 4; grid-row: 1 / span 3` 的面板，就是左上角 4 格宽 × 3 行高的卡片。网格是唯一的版式语言——flexbox 只用于单个单元格内部对齐。

### 单元格内边距

单元格内部 padding 随单元格尺寸和用途变化：
- 紧凑卡片（小统计砖）：24px × 28px
- 标准卡片（功能面板）：28px × 32px
- 大卡片（章节面板）：36px × 32px
- 英雄卡片（章节分隔）：40px × 44px

这些不是刚性 token——是实用阶梯。选能让卡片内部字体喘气、又不丢掉面板身份的 padding。

### 持续 Chrome

每一页左下带着 `{components.pagenum}` 标签，格式 `01 / 12`。三种变体：
- 默认：纸色背景，墨色文字。
- `.invert`：墨色背景，纸色文字。
- `.lemon`：黄色背景，墨色文字。

有些页面还带着右上的 `{components.corner-mark}`（小型 2×2 色块）、左下的 `{components.copyright}`，或作为品牌标识的 `{components.blockmark}`（更大的 2×2 印章）。

## 纵深与抬升

### 无阴影，仅靠色块邻接

系统在任何结构面板上使用**零条 box-shadow 声明**。纵深完全是色彩邻接的函数：纸面板挨着墨面板读作抬起（纸朝向观者）；黄面板挨着墨面板读作构图里最响的信号。面板之间 12px 网格间隙露出腻子色 `{colors.bg}`，充当统一画框色。

### 无渐变（照片区除外）

系统里仅有的渐变在照片区占位纹理里：`radial-gradient` 加 `repeating-linear-gradient` 做出风格化黑白颗粒纹理，充当摄影替身。这些纹理活在 class 为 `.photo` 或 `.ph` 的单元格里，从不出现在结构面板上。

### 表格与 pill 的描边

- 表格单元格（`{components.table-cell}`）在底边和右边用 1.5px solid ink 分割线，做出线框网格。
- 对照 pill（`{components.pill-part}`）用 1.5px solid ink 描边作为部分态轮廓。
- 图表坐标轴用 2px solid ink 做左下线框。
- 柱状图里的黄柱（`{components.bar-fill-lemon}`）带着 1.5px solid ink 描边，防止亮填色在纸底上振颤。

其他元素不带描边。卡片无边框，靠填色对比。

## 形状与处理

### 圆角

| 值 | 用途 |
|---|---|
| 0px | 每一个元素——卡片、pill、标签、页码、表格单元格、图表柱、blockmark |

系统在任何元素上**圆角为零**。每个形状都是严格矩形或正方形。block-stamp 和 corner-mark 字形由直角方块组成。

### 描边粗细

- **1.5px solid `{colors.ink}`** —— 用于表格单元格分割线、pill 轮廓，以及黄柱的描边。最常见的描边粗细。
- **2px solid `{colors.ink}`** —— 用于图表坐标轴（绘图区左边和底边），线框略强。

不存在其他描边粗细。没有闷色描边，没有虚线描边（内部用的非常特定的 `1px dashed rgba(0,0,0,.18)` 图表网格线除外）。

### 装饰元素类型

**Block stamp（`{components.blockmark}`）** —— 2×2 小方格网格，左上和右下填实（另两格透明）。对角填色印章，充当品牌身份标记。尺寸从 36px（corner-mark）到 96px（引文页上的 block stamp）。可用 ink 或 accent-lemon 渲染。

**Corner mark（`{components.corner-mark}`）** —— 36px × 36px 版 block stamp，锚定在面板右上。充当小型结构身份标签。

**QR tile（`{components.qr-tile}`）** —— 5×5 小方格网格，ink 与 accent-lemon 填色呈棋盘状。装饰性 QR 图案视觉，不是真正可扫的码。用作封面页点缀。

**Arrow（`{components.arrow}`）** —— 行内 SVG 右指箭头，64px × 64px（小流程指示可用 24px × 24px）。用作流程步骤之间的流向信号，以及统计面板上的外指指示。

**Highlight mark（`{components.highlight-mark}`）** —— 通过 `<mark>` 元素把标题里一个或多个词包进霓虹黄色块。系统的标题强调机制。Padding 是 `0 6px`（更大字号可用 `0 8px`）。

**Page number（`{components.pagenum}`）** —— 左下位置标签，格式 `01 / 12`，带彩色背景。三种背景变体（paper、ink、lemon）让页码能对照当前页主导面板，选最看得见的颜色。

**照片区** —— class 为 `.photo` 的单元格，深黑背景（#111），内含 `.ph` 子元素，渲染风格化黑白噪点纹理（径向 + 对角条纹）。单元格里一个小号等宽标签给区域命名（例如 "PORTRAIT / B&W"）。在真实摄影到位之前当占位。

**Pills（`{components.pill-yes}`、`{components.pill-part}`、`{components.pill-no}`）** —— 对照单元格里的行内等宽全大写标签，三种颜色状态：黄填（肯定）、纸色加 ink 描边（部分）、墨填加纸色字（否定）。三者都是 0 圆角矩形，尽管名叫 pill，并不圆。

**章节序数面板** —— 整块内容就是一个 320px Space Grotesk 字重 700 数字。用作章节分隔页的视觉身份；页面其余部分带着互补的墨色标题面板。

**图表柱对** —— 成组的两根竖柱（系列 A 实心 ink，系列 B 黄色加 ink 描边）。柱在列内等宽，列间隙由父网格设定。

## 该做与不该做

### 该做
- 每一页都在 12 列 × 8 行网格（`{components.frame}`）上构图，内缩 40px，间隙 12px（要呼吸可用 18px）。网格就是系统身份。
- 把网格从角到角填满。网格被不同跨度的面板密密填住时，系统才读作权威。
- 用 `{colors.paper}` 做默认面板填色，`{colors.ink}` 做对比块，`{colors.accent-lemon}` 做每页一到三块信号面板。
- 每一个 display、title、subtitle 和统计数字都设成 Space Grotesk 700 全大写加负字距。这个组合就是系统的排印声线。
- 在标题里用 `<mark>` 把一个或多个词包进黄色荧光笔色块——系统的主标题强调。
- 在标题里用 `<em>` 把一个词切到 accent-lemon 颜色（保持直立，无斜体）。
- 每一页左下放 `{components.pagenum}` 标签。选与左下面板对比的背景变体（paper / ink / lemon）。
- 每一个标签、页码、坐标轴标记和元数据字符串都用 JetBrains Mono 全大写，字距至少 0.08em。
- 在对照表里按规范三色处理渲染 pills（yes / part / no）。
- 当统计数字占主打面板时，允许它们放到 156–320px。大数字是编辑海报身份的一部分。

### 不该做
- 不要给任何面板加 box-shadow。纵深只来自色彩邻接。
- 不要给任何元素圆任何角。系统严格矩形。
- 不要把展示标题做成大小写混排。Space Grotesk 展示始终全大写。
- 不要把正文做成全大写。字重 400 的大小写混排才是正文声线。
- 不要引入第二强调色。霓虹黄是唯一的彩色强调——加红、蓝或绿会拆掉系统。
- 不要把黄当文字色。强调色太浅，不能当字来读；它只是填色。
- 不要在 12×8 网格之外构图。绝对定位、打破网格的元素（页码、corner mark、版权）明确是仅有的例外。
- 不要用斜体字形。`<em>` 标签被改造成换色开关——这里不存在斜体视觉样式。
- 不要用圆角「pill」形状，尽管组件名叫 pill。Pills 是 0 圆角矩形。
- 不要稀疏填充网格。一页只有一块面板、七个空单元格读起来像坏掉——系统需要密度才能作为编辑海报运作。

## 响应式行为

系统瞄准**固定 1920×1080 画布**，渲染在 `<deck-stage>` web component 里（经由 `deck-stage.js` 加载）。舞台把整个 1920×1080 构图按比例缩放到浏览器视口——字号、面板位置、网格间隙、内缩值全部在画布内像素固定，舞台负责响应式变换。

这意味着：系统里每一个排印和版式决定都按 1920×1080 分辨率做出。尺寸不按断点缩放；整张画布作为单一单元缩放。幻灯片样式里没有 media queries。

### 演示行为
- `<deck-stage>` web component 管理页到页导航、视口缩放和演示 chrome。
- 键盘导航、触摸滑动和鼠标滚轮由舞台组件处理，不靠行内脚本。
- 无论浏览器视口如何，幻灯片画布恒为 1920×1080；舞台按比例缩放它。

### 打印行为
模板用 deck-stage 组件渲染。打印导出取决于组件的打印处理，可能一页一页渲染，也可能只捕获当前页。

## CJK 与国际内容

### 推荐中文搭配

| 角色 | 拉丁字体 | 中文字体 | 字重 |
|---|---|---|---|
| Display / title / stat（Space Grotesk 700 UPPERCASE） | Space Grotesk | Noto Sans SC（思源黑体） | 900 |
| Body（Space Grotesk 400） | Space Grotesk | Noto Sans SC | 400 |
| Label / page number（JetBrains Mono UPPERCASE） | JetBrains Mono | Noto Sans SC | 400（不要对 CJK 强制等宽） |

### 中英混排策略

策略 A —— 单一 `font-family` 栈，拉丁优先回退。把每个 token 的 `fontFamily` 从 `"Space Grotesk, Helvetica Neue, Helvetica, Arial, sans-serif"` 改成 `"Space Grotesk, Noto Sans SC, Helvetica Neue, Helvetica, Arial, sans-serif"`。拉丁字形用 Space Grotesk 700 渲染；CJK 字符自动落到 Noto Sans SC 900。混排字符串如 `THE CLAUDE 模型` 能正确行内渲染。

### 加载

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=JetBrains+Mono:wght@400;500&family=Noto+Sans+SC:wght@400;500;700;900&display=swap" rel="stylesheet">
```

### 通用 CJK 调整

- 行高：正文 1.75–1.85，展示 1.15–1.25
- 字距：CJK 为 0
- Text-transform：CJK 不强制全大写
- 全角标点 （，。：；！？「」（））
- 展示标题不加句号（中文排印惯例）
- 盘古之白（CJK 与拉丁之间加空格：`使用 Claude` 而不是 `使用Claude`）
- 一句一字体

### 本系统的审美说明

Neo-Grid Bold 是粗重全大写 Space Grotesk 700，负字距，字号可到 320px。**中文没有大写概念**，所以系统的主排印招牌（全大写粗野主义标题）必须改由*字重和密度*来转译。每一个中文展示瞬间都设成 **Noto Sans SC 900** —— 能拿到的最重字重 —— 以匹配大字号 Space Grotesk 700 ALL CAPS 的视觉重量。中文标题还应完全丢掉负字距；CJK 字形设计在方形 em 盒上，收紧会造成撞字。

标题里用 `<mark>` 霓虹黄色块高亮一个词，转到中文是完美迁移——用 `<mark>` 包一个汉字或一个短语，柠檬色块读感相同。**在 CJK 里继续把荧光笔机制作为系统的主标题强调。** `<em>` 换色（行内黄）也干净迁移。

JetBrains Mono 全大写标签（`01 / 12` 格式的页码）是纯拉丁 / 数字——保持 JetBrains Mono。不要试图用等宽渲染中文；CJK 字形设计上已经是等宽的，强制 JetBrains Mono 会产生缺字。含 CJK 的混排等宽标签，落到同字号的 Noto Sans SC 400。

章节数字（320px Space Grotesk 700）和统计数字（156–240px）是纯数字——原样迁移。霓虹黄强调面板系统与脚本无关；只要字重停在 900，粗野主义海报美学就能熬过脚本切换。

### 已知 CJK 缺口

负字距（-0.005 到 -0.05em）在本系统里随展示字号缩放，是「粗野主义压缩」招牌的一部分。**给中文字符去掉它，会在中英混排文稿里打破与纯拉丁页的视觉对等。** 接受这一点：纯 CJK 页会读起来比纯拉丁页略少压缩。不要靠收紧中文来补偿——撞字比调性不匹配更糟。

## 迭代指南

1. 每一张新页都通过 `grid-column` 和 `grid-row` span 声明在 12×8 网格上构图。除页码标签、corner-mark 和版权印章外，绝不用绝对定位打破网格。
2. 每一块新面板只用三种填色之一：paper（默认）、ink（反相）或 accent-lemon（信号）。不要引入第四种面板色。
3. 每一个新展示标题都是 Space Grotesk 字重 700 全大写，负字距随标题字号缩放（30px 时 -0.005em，到 320px 时 -0.05em）。
4. 每一个新正文元素都是 Space Grotesk 字重 400 大小写混排，三种正文字号之一（28px、24px、22px）。
5. 每一个新标签或元数据标记都是 JetBrains Mono 全大写，字距至少 0.08em。
6. 每一个新图表系列色要么是 `{colors.ink}`（系列 A），要么是带 ink 描边的 `{colors.accent-lemon}`（系列 B）。不要加第三系列色。
7. 每一张新卡片圆角为 0。方角不可商量。
8. 要强调标题里的一个词，用 `<mark>` 包黄色块，或用 `<em>` 做黄色换色。不用粗体、斜体或下划线。
9. 每一个新对照单元格用三态 pill 系统：黄填（yes）、纸色加 ink 描边（partial）、墨填（no）。
10. 密密填满网格。如果构图让一行里空出超过两个单元格，重新考虑是不是缺了一张卡片。

## 已知缺口

- 系统依赖经由 `deck-stage.js` 加载的 `<deck-stage>` web component。没有这支脚本，1920×1080 画布不会缩放到视口，幻灯片会按原生像素尺寸渲染。
- 照片区用风格化 CSS 生成的噪点纹理（径向 + 对角条纹渐变）当占位。真实摄影必须替换 `.photo` 单元格内容为 `<img>`，并确保周围面板颜色补足照片的负空间。
- QR 图案砖是装饰性的——5×5 方格网格并不编码真正可扫的码。真 QR 码需要另外在外部生成 SVG。
- 柱状图高度通过每根柱填色上的行内 `style="height: XX%"` 声明设定。没有数据绑定层。
- 流程步骤之间用的箭头 SVG 在每个幻灯片模板里手绘路径；如果一页增加或删掉流程节点，箭头位置必须手工重算。
- `<deck-stage>` 组件不是由本模板的 script 标签直接加载的——期望它通过 `deck-stage.js` 全局可用。缺脚本会静默把幻灯片渲染成扁平绝对定位 div。
- 系统全程用固定像素尺寸（不用 `vw`/`vh`）。在异常视口宽高比下，deck-stage 比例缩放可能用腻子色条给画布加 letterbox。
- `{colors.muted}`（#8A8A85）token 已定义，但只用于照片区标签上的低不透明度叠层——在主字体或面板系统里没有角色。
