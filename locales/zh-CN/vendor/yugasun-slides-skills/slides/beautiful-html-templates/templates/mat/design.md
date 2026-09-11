---
version: alpha
name: Mat
description: A warm, material-tactile presentation system inspired by a high-end product landing page. Dark forest green is the dominant environment, warmed by a low atmospheric wood-brown glow from the bottom-right corner of every dark slide. Cream type floats directly on the field; warm orange acts as the single accent. The typeface stack pairs Bricolage Grotesque (a heavy, rounded grotesque) for display with DM Sans for body and DM Mono for labels — the result reads as industrial-design portfolio meets boutique product launch, never tech demo.

colors:
  bg-dark: "#232E26"
  bg-dark-alt: "#2E3D30"
  bg-cream: "#EDE6D0"
  bg-cream-alt: "#E4DAC4"
  ink-cream: "#F0E8D2"
  ink-cream-2: "rgba(240, 232, 210, 0.58)"
  ink-cream-3: "rgba(240, 232, 210, 0.3)"
  ink-dark: "#1E2820"
  ink-dark-2: "rgba(30, 40, 32, 0.6)"
  ink-dark-3: "rgba(30, 40, 32, 0.3)"
  accent-orange: "#C07030"
  border-on-dark: "rgba(240, 232, 210, 0.12)"
  border-on-cream: "rgba(30, 40, 32, 0.14)"
  wood-glow: "#7A4E24"

color-aliases:
  c-fg: ink-cream
  c-fg-light: ink-dark
  c-bg: bg-dark
  c-bg-light: bg-cream
  c-accent: accent-orange

typography:
  display:
    fontFamily: "Bricolage Grotesque, Noto Sans SC, sans-serif"
    fontSize: 12vw
    fontWeight: 800
    lineHeight: 0.88
    letterSpacing: -0.03em
  h1:
    fontFamily: "Bricolage Grotesque, Noto Sans SC, sans-serif"
    fontSize: 7vw
    fontWeight: 800
    lineHeight: 0.92
    letterSpacing: -0.025em
  h2:
    fontFamily: "Bricolage Grotesque, Noto Sans SC, sans-serif"
    fontSize: 4vw
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -0.02em
  h3:
    fontFamily: "Bricolage Grotesque, Noto Sans SC, sans-serif"
    fontSize: 2.4vw
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.01em
  lead:
    fontFamily: "DM Sans, Noto Sans SC, sans-serif"
    fontSize: 1.5vw
    fontWeight: 400
    lineHeight: 1.55
  body:
    fontFamily: "DM Sans, Noto Sans SC, sans-serif"
    fontSize: 1.05vw
    fontWeight: 400
    lineHeight: 1.65
  caption:
    fontFamily: "DM Sans, Noto Sans SC, sans-serif"
    fontSize: 0.82vw
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "DM Mono, monospace"
    fontSize: 0.7vw
    fontWeight: 400
    letterSpacing: 0.12em
    textTransform: uppercase
  stat-value:
    fontFamily: "Bricolage Grotesque, Noto Sans SC, sans-serif"
    fontSize: 5.5vw
    fontWeight: 800
    lineHeight: 1.0
    letterSpacing: -0.025em
  quote-text:
    fontFamily: "Bricolage Grotesque, Noto Sans SC, sans-serif"
    fontSize: 3.4vw
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.02em
  quote-mark:
    fontFamily: "Bricolage Grotesque, Noto Sans SC, sans-serif"
    fontSize: 8vw
    fontWeight: 800
    lineHeight: 0.6

spacing:
  pad-x: 5.5vw
  pad-y: 5.5vh
  gap-lg: 4.5vh
  gap-md: 2.8vh
  gap-sm: 1.4vh

canvas:
  width: 100vw
  height: 100vh

components:
  kicker:
    fontFamily: "{typography.label.fontFamily}"
    fontSize: "{typography.label.fontSize}"
    letterSpacing: 0.12em
    textTransform: uppercase
    color: "{colors.accent-orange}"
  rule:
    width: 32px
    height: 1px
    background: "{colors.accent-orange}"
  bullet-marker:
    content: "—"
    color: "{colors.accent-orange}"
    fontFamily: "{typography.label.fontFamily}"
    description: "Em-dash prefix in warm orange; emerges in mono face. The system's standard list mark; never a bullet, never a checkmark."
  info-card:
    background: "{colors.bg-cream}"
    color: "{colors.ink-dark}"
    padding: "{spacing.gap-md} calc({spacing.pad-x} * 0.8)"
    maxWidth: 28vw
    description: "Cream inset box embedded on a dark green field. The signature material-contrast component; carries a heading and a body block, no border, no shadow."
  chrome-band:
    borderBottom: "1px solid {colors.border-on-dark}"
    paddingBottom: "{spacing.gap-sm}"
    description: "Label-pair on top of a 1px rule; suppressed on cover/quote/end slide types."
  foot-band:
    borderTop: "1px solid {colors.border-on-dark}"
    paddingTop: "{spacing.gap-sm}"
    description: "Label-pair under a 1px rule; mirrors the chrome band."
  stat-cell:
    borderRight: "1px solid {colors.border-on-dark}"
    padding: "{spacing.gap-md} {spacing.pad-x} {spacing.gap-md} 0"
    description: "A vertically-divided cell containing a large numerical value (with optional inline orange-emphasis em-span) and a one-line label. Last cell has no right border."
  bar-fill:
    width: "100%"
    background: "{colors.ink-cream-3}"
    description: "Vertical bar in muted cream; gets the orange accent (.accent variant) when it's the highlighted data point."
  compare-divider:
    width: 1px
    background: "{colors.border-on-dark}"
    description: "A 1px-wide vertical column (not a border) used to split a before/after comparison; subtle, not loud."
  image-placeholder:
    background: "rgba(240, 232, 210, 0.06)"
    border: "1px solid {colors.border-on-dark}"
    color: "{colors.ink-cream-3}"
    description: "Hairline-bordered void with centered mono label until photography is available."
  atmospheric-glow:
    selector: ".slide.dark::before"
    position: "bottom-right ellipse, 55% wide × 70% tall"
    gradient: "radial-gradient(ellipse at 70% 80%, rgba(122, 78, 36, 0.28) 0%, rgba(80, 50, 20, 0.14) 40%, transparent 70%)"
    description: "The wood-brown atmospheric glow that lives on every dark slide via ::before. Non-optional on dark surfaces; defines the warmth of the system."
---

## 概述

Mat 是一套**材质触感演示系统**，建立在单一环境前提上：深森林绿表面，从右下角被低位木棕色光晕烘暖。气氛做了重活——内容落地之前，这一页已经像午后光线下的工作台。奶油字直接浮在绿场上；没有卡片、没有面板、没有画框。系统需要打破绿色时，用一块奶油内嵌盒（info-card）来做，读成铺在深色表面上的暖纸。

字体栈是刻意的三声部配对。**Bricolage Grotesque** 字重 700 和 800 是展示主力——重、圆，带一点机械性格，适合产品文案而不像科技创业。**DM Sans** 字重 400 是正文声音，中性到足以让展示字呼吸。**DM Mono** 字重 400 处理所有标签、眉题、元信息和铬件——任何需要读成标签而不是句子的结构文字。本系统展示字**始终大小写混排**，从不全大写；全大写工作留给等宽标签。

色板刻意收窄。**深森林绿**是主导表面（`{colors.bg-dark}`），略浅的备用色可用于分层区域。**暖奶油**是深色上的主文本色，也是幻灯片翻浅时的次级表面色。**暖橙**（`{colors.accent-orange}`）是唯一强调色——只作为小的行内标记出现：眉题文字、项目符 em 破折号、数据数字里的 `<em>`、开引号字形、图表里那一根高亮柱。橙从不当背景，从不当大标题色；它是系统的结构强调点。

纵深极小、气氛性的，不是叠层。没有投影。任何结构元素都没有圆角。唯一的纵深信号是通过 `::before` 伪元素坐在每一页深色幻灯片后面的木棕径向光晕。区域分隔来自低不透明度奶油的**细 1px 发丝线**——用于铬件带、脚带、数据单元格分隔、对比面板分割和图表基线。这套系统没有任何地方大声。

**密度哲学：中等疏朗。** Mat 在幻灯片会呼吸时读起来优雅——左右内边距慷慨（`{spacing.pad-x}` 为 5.5vw），一个主要排印时刻，再加一块次级支撑文案。一页硬塞三列项目符会打破系统；暖绿场需要负空间来做气氛工作。例外是数据和对比页类型，那里干净的三栏或两栏克制单元格是正确的。一页一条标题加一段导语，正好在这套系统的车道里。一页用文字填满 80% 面积，是在跟设计打架。

**关键特征：**
- 深森林绿画布（`{colors.bg-dark}`），暖木棕径向光晕（`{components.atmospheric-glow}`）锚定在每一页深色幻灯片的右下角。
- 奶油文字（`{colors.ink-cream}`）直接浮在绿场上，周围没有卡片、面板或画框。
- Bricolage Grotesque 展示字**始终大小写混排**——从不全大写。全大写留给 DM Mono 标签。
- 单一强调色，暖橙（`{colors.accent-orange}`），只作小的行内强调（眉题、项目符标记、行内 `<em>`、引号字形、一根图表柱）。
- 奶油 **info-card**（`{components.info-card}`）是签名材质对比组件——嵌在深色场上的暖纸矩形。
- 项目列表用 DM Mono 暖橙 em 破折号前缀——从不用圆点，从不用勾。
- 低不透明度奶油的细 1px 发丝线是唯一的分隔语言。没有重边框，没有阴影。
- 系统有一种浅色页变体（奶油背景配深绿文字），用作 deck 内的色调反转，从不当默认。

## 色彩

### 色板

- **深森林绿**（`{colors.bg-dark}` — #232E26）：主导环境。除非刻意选择浅色页变体，否则每一页的默认背景。绿色够闷，奶油字坐在上面不会振动。
- **略浅绿**（`{colors.bg-dark-alt}` — #2E3D30）：色调升一档，留给深色页内的分层或凹陷表面。可用，但用得省。
- **暖奶油**（`{colors.bg-cream}` — #EDE6D0）：浅色页背景，以及 info-card 内嵌的填充色。读成暖纸，不是白——暖意对系统的材质身份至关重要。
- **更深奶油**（`{colors.bg-cream-alt}` — #E4DAC4）：浅色页上图片占位用的次级奶油调。
- **奶油墨**（`{colors.ink-cream}` — #F0E8D2）：每一个深色表面上的主文本色。比背景奶油略暖——选它是为了让标题感觉像刻进绿色，而不是印在上面。
- **58% / 30% 奶油墨**（`{colors.ink-cream-2}`、`{colors.ink-cream-3}`）：深色上的次级和三级文本。分别用于弱化导语和几乎看不见的元信息。
- **深墨**（`{colors.ink-dark}` — #1E2820）：奶油表面上的主文本色（info-card 正文、浅色页）。非常深的森林绿，从不用纯黑。
- **60% / 30% 深墨**（`{colors.ink-dark-2}`、`{colors.ink-dark-3}`）：奶油上的弱化和三级文本。
- **暖橙**（`{colors.accent-orange}` — #C07030）：唯一强调色。烧过的铜橙，向木头、皮革和氧化金属点头。从不当背景，从不当大标题色。
- **木光**（`{colors.wood-glow}` — #7A4E24）：径向气氛光晕色，只在右下角渐变里以 0.28 和 0.14 alpha 施加。从不当平填充。

### 默认值

- **默认表面背景**：`{colors.bg-dark}`（森林绿）。系统是深色默认；奶油页是有意的色调断开，不是日常选择。
- **深色上的默认标题颜色**：`{colors.ink-cream}`。标题从不用橙。
- **奶油上的默认标题颜色**：`{colors.ink-dark}`。
- **深色上的默认正文颜色**：`{colors.ink-cream-2}`（58% 奶油——`.muted` 助手）。
- **奶油上的默认正文颜色**：`{colors.ink-dark-2}`。
- **默认边框 / 分隔颜色**：深色用 `{colors.border-on-dark}`；奶油用 `{colors.border-on-cream}`。始终 1px，从不超过。
- **默认眉题颜色**：`{colors.accent-orange}`。眉题是系统的眉毛标签，是橙色最稳定出现的地方。
- **默认行内强调颜色**：`{colors.accent-orange}`。数据值、引语署名或图表标签里的 `<em>` 解析为橙。
- **深色页的默认气氛处理**：木棕径向光晕（`{components.atmospheric-glow}`）始终开。它是深色表面本身的一部分。

橙的功能是标点色：它告诉眼睛结构强调住在哪里，却从不抢表面积。若同一页上两个橙色元素相邻，其中一个是错的。

## 字体排印

### 字体家族

系统跑在三套 Google Fonts 加中日韩回退上。**Bricolage Grotesque** 承担每一个展示、h1、h2、h3、数据数字和引语文字——字重 700–800 时圆而重的性格是定义声音。**DM Sans** 字重 400 承担每一段、导语、图注和项目项——中性、可读，让展示字带头。**DM Mono** 字重 400 承担每一个标签、眉题、铬件标签、页脚文字、项目符 em 破折号和图表标签——任何需要读成结构标记而不是散文的东西。**Noto Sans SC** 是所有无衬线角色的中日韩回退；**不用 Noto Serif SC**。

一条微妙但承重的规则：**每个列表项前的项目符 em 破折号用 DM Mono 暖橙渲染**，不用正文字体。等宽形状才让破折号感觉像刻意标记，而不是散落的标点字形。

本系统不用斜体做排印装饰。`<em>` 标签被改用作**橙色行内强调**——数据值或引语署名里的 `<em>` 切到 `{colors.accent-orange}` 并保持直立（font-style: normal）。任何地方都没有斜体字面。

### 字号阶梯

| Token | 字号 | 字体 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.display}` | 12vw | Bricolage Grotesque | 800 | 封面或开场 hero 展示——巨大，按每行 1–2 个词折行 |
| `{typography.h1}` | 7vw | Bricolage Grotesque | 800 | 章节开场或收场标题 |
| `{typography.h2}` | 4vw | Bricolage Grotesque | 700 | 主内容页标题 |
| `{typography.stat-value}` | 5.5vw | Bricolage Grotesque | 800 | 数据单元格里的大数字 |
| `{typography.quote-mark}` | 8vw | Bricolage Grotesque | 800 | 暖橙装饰开引号字形 |
| `{typography.quote-text}` | 3.4vw | Bricolage Grotesque | 600 | 引语正文 |
| `{typography.h3}` | 2.4vw | Bricolage Grotesque | 600 | 副标题或区域标题 |
| `{typography.lead}` | 1.5vw | DM Sans | 400 | 导语段落或大项目项 |
| `{typography.body}` | 1.05vw | DM Sans | 400 | 正文段落和 info-card 正文 |
| `{typography.caption}` | 0.82vw | DM Sans | 400 | 图片图注、标语、细字 |
| `{typography.label}` | 0.7vw | DM Mono | 400 | 眉题、铬件标签、页脚标签、元信息、图表标签 |

### 默认值

- **默认主章节标题**：`{typography.h2}`（4vw）。
- **默认开场或封面展示**：封面用 `{typography.display}`（12vw）；章节或收场时刻用 `{typography.h1}`（7vw）。
- **默认正文段落字号**：`{typography.body}`（1.05vw）。当段落是大标题下唯一的支撑块时，伸手去 `{typography.lead}`（1.5vw）。
- **默认标签 / 眉题字号**：`{typography.label}`（0.7vw）。
- **任何展示元素的默认字重**：700（h2）或 800（display、h1、stat-value）。
- **正文默认字重**：400。
- **默认标题字距**：负——display -0.03em，h1 -0.025em，h2 -0.02em。负字距至关重要。

拿不准时，默认用 `{typography.h2}` 做主文字时刻，配一段 `{typography.lead}` 作支撑文案——这对是系统最可靠的节奏。

### 标志性处理

只要用到对应元素类型，这些处理就**不可省略**：

- **所有 display、h1、h2、h3 文字都是大小写混排**——从不全大写。本系统不存在全大写展示字。若文字是 Bricolage Grotesque，它就是句首大写。
- **所有标签、眉题、铬件文字、页脚和元信息都是 DM Mono 全大写，正字距 0.12em。** 这里不存在句首大写的等宽。
- **眉题始终暖橙。** 当一页带眉题（标题上方的眉毛标签）时，不论表面，颜色都是 `{colors.accent-orange}`。
- **项目列表用 DM Mono 着色暖橙的 em 破折号前缀。** 从不用圆点，从不用勾，从不用数字。
- **数据数字里的 `<em>` 标签渲染为暖橙并保持直立。** 这是高亮数字里单位后缀或关键数位的机制。
- **深色表面上的标题是奶油；奶油表面上的标题是深墨。** 标题从不用橙。
- **所有 Bricolage 展示字都用负字距。** 展示字用默认字距读成没处理过；负字距才给字体压缩的精品产品性格。

### 排印原则

系统的节奏是**重的大小写混排展示 + 轻的大小写混排正文 + 小的全大写等宽标签**。改掉这三种模式里的任何一种（例如把展示做成全大写，或让正文与展示同字重）会打破编辑气质。Bricolage 700–800 挨着 DM Sans 400——字重落差是刻意且宽的。不要用中间 Bricolage 字重（400、500）做展示时刻；它们读成没拿定主意。

不用斜体。不用下划线。正文里唯一的强调机制是橙色 `<em>` 行内。唯一的结构强调是眉题和项目符 em 破折号。

## 版式

### 画布系统

Mat **按设计是视口流体的**。所有尺寸用 `vw` 和 `vh` 单位，让版式随视口线性缩放。幻灯片容器是 `100vw × 100vh`，deck 是水平 flex 条，按整视口宽度左右平移。没有固定画布尺寸；同一构图在任何接近 16:9 的视口上都能正确渲染。

### 内边距与间隙阶梯

| Token | 取值 | 用途 |
|---|---|---|
| `{spacing.pad-x}` | 5.5vw | 幻灯片水平内边距；左右边缘的呼吸空间 |
| `{spacing.pad-y}` | 5.5vh | 幻灯片垂直内边距 |
| `{spacing.gap-lg}` | 4.5vh | 主要内容区块之间 |
| `{spacing.gap-md}` | 2.8vh | 相关元素之间（标题 → 导语，数据 → 标签） |
| `{spacing.gap-sm}` | 1.4vh | 紧密相关元素之间（铬件带里的标签对） |

水平内边距很慷慨——内容大约占视口中间 89%。把内容推近边缘会打破系统的编辑疏朗。

### 铬件框

大多数幻灯片类型顶部带 **chrome-band**（`{components.chrome-band}`），底部带 **foot-band**（`{components.foot-band}`）。每一条都是两个 DM Mono 标签的 `flex space-between` 行（通常左侧章节名，右侧幻灯片位置或章节号），用 1px 发丝线与正文隔开。封面、引语和收场式幻灯片完全抑制两条带——那些时刻按惯例无铬件。

### 导航铬件

一行导航点固定在底部居中（低不透明度白的 5px 圆），页码计数坐在右下（10px DM Mono，`rgba(255,255,255,0.25)`，格式 `01 / 09`）。这些是演示铬件，不是设计语言本身的一部分——在本库所有模板家族里都一致。

## 层次与纵深

### 气氛光晕（主纵深机制）

系统唯一的纵深处理是通过 `::before` 住在每一页深色幻灯片上的**右下木棕径向光晕**。伪元素占 55% 宽 × 70% 高，锚定在右下角，径向渐变从 `rgba(122,78,36,0.28)` 到 `rgba(80,50,20,0.14)` 再到透明。光晕坐在 `z-index: 0`；所有幻灯片内容坐在 `z-index: 1`。这就是纵深——没有投影、没有抬升卡片、没有文字光晕效果。

### 发丝线（结构分隔）

系统需要分隔区域时，在深色表面上用低不透明度奶油的 **1px 发丝线**（`{colors.border-on-dark}`，12% 不透明度），在奶油上用低不透明度深墨（`{colors.border-on-cream}`，14% 不透明度）。这些线出现在铬件带下、脚带上、数据单元格之间、对比面板之间，以及图表基线。发丝线从不超过 1px，从不上色。

### 无阴影

任何结构元素上都没有 `box-shadow` 声明。info-card 坐在深色场上没有阴影——它的材质对比是奶油对绿的色调跳跃，不是抬升。给任何组件加阴影会打破系统的平面材质摄影审美。

## 形状与处理

### 圆角

| 取值 | 用途 |
|---|---|
| 0px | 每一个结构元素——info-card、图片占位、数据单元格、对比面板、柱 |
| 50% | 仅导航点圆 |

系统在任何组合内容上都**没有圆角**。卡片、面板和图片框全是严格矩形。仅有的圆形是导航 UI 点。

### 边框粗细

- **1px solid 发丝线** —— 通用结构边框。用于铬件带、脚带、数据单元格分隔、对比面板分割、图表基线和图片占位描边。颜色在深色表面上是 `{colors.border-on-dark}`，奶油上是 `{colors.border-on-cream}`。
- 不存在其他边框粗细。2px 边框会打破系统；3px 边框属于另一设计家族。

### 装饰元素类型

**眉题** —— 小的 DM Mono 全大写标签，暖橙，正字距 0.12em，作为眉毛标签放在标题上方。系统里橙色最稳定的出现。通常 0.7vw 字号。

**线** —— 32px 宽 × 1px 高的暖橙水平强调线。用作眉题与标题之间的小下划线式分隔，或章节号下方。装饰性的，不是结构的。

**项目符 em 破折号** —— 每一个项目列表的列表标记。渲染为 DM Mono 着色暖橙的 `—`，通过 CSS 网格标记列（`grid-template-columns: 1.4em 1fr`）前置到列表项。系统的项目符声音。

**Info-card** —— 放在深色页上的奶油内嵌矩形（`{components.info-card}`）。带标题（h3 级，深墨）和正文块（正文级，弱化深墨）。系统里最鲜明的组件——用来拿一块暖纸戳破绿场。没有边框、没有阴影、没有圆角；单靠色调跳跃定义边缘。

**数据单元格** —— 竖向分隔的单元格，内含大数字（`{typography.stat-value}`）和一行标签（`{typography.body}`，弱化奶油）。单元格三组并排，用 1px 右边框分隔（最后一格没有右边框）。数字值支持橙色行内 `<em>` 做单位后缀（例如 `4.7k` 里的后缀）。

**引号** —— `{typography.quote-mark}` 字号的超大开引号字形，暖橙。作为排印装饰坐在引语文字上方。只用于引语页类型。

**对比分隔** —— 两个并排面板之间 1px 宽的垂直 CSS 列（不是边框）。按设计很微妙——视觉工作由两块面板的对比来做，不是分隔本身。

**图片占位** —— 带 1px 发丝边框的空矩形，6% 奶油背景，居中 DM Mono 标签写占位名。直到放入真实摄影前使用。占位颜色刻意接近背景——图片区域不应自我宣告。

## 应做与不应做

### 应做
- 用深森林绿（`{colors.bg-dark}`）作默认幻灯片背景。系统是深色优先；奶油页是色调断开，不是默认。
- 每一页深色幻灯片都应用木棕气氛光晕。它是表面的一部分，不是可选花招。
- 把大小写混排的 Bricolage Grotesque 展示与全大写的 DM Mono 标签配对。两套字体之间的大小写对比就是系统的排印节奏。
- 深色上标题用奶油（`{colors.ink-cream}`），奶油上用深墨（`{colors.ink-dark}`）。标题从不带橙色强调。
- 用暖橙（`{colors.accent-orange}`）作眉题色、项目符 em 破折号色和行内 `<em>` 色。橙是标点，从不是表面。
- 当一页需要一块暖纸嵌在绿场上时，用奶油 info-card（`{components.info-card}`）——系统的签名材质对比动作。
- 保持幻灯片中等疏朗。一条主标题、一段支撑段落，可选 3–5 条短项目符，就是正确密度。
- 每一个结构分隔都用低不透明度奶油或深墨的 1px 发丝线。边框从不超过。
- 每一个项目列表都用 DM Mono 的 em 破折号前缀。从不用圆点、勾或数字替代。
- 把数字值里的 `<em>` 渲染为暖橙、font-style normal——这就是本系统单位后缀和强调数位的读法。

### 不应做
- 不要把任何 Bricolage display、h1、h2 或 h3 文字做成全大写。展示字始终大小写混排。全大写专属于 DM Mono 标签。
- 不要引入第二个强调色。系统有一个强调色（暖橙），不能分享那个角色。
- 不要给任何组件加投影、模糊阴影或抬升效果。纵深只有气氛光晕。
- 不要圆任何结构元素的角。卡片、面板、图片框、柱——全是严格矩形。只有导航点圆是圆的。
- 不要用三列项目符填满一页，或竖向叠五个区域。Mat 一挤就读成坏掉。
- 不要把橙当背景填充。橙只行内。
- 不要在任何地方用衬线字体。本系统没有衬线；圆无衬线承担每一个编辑时刻。
- 不要给 info-card 加边框。奶油与森林绿之间的色调跳跃定义边缘——边框会打破平面材质读法。
- 不要用斜体字形。`<em>` 标签被改用作橙色行内颜色切换，并保持直立。
- 不要把边框粗细加到 1px 以上。2px 边框会打破系统的发丝语言。

## 响应行为

Mat 面向流体 `100vw × 100vh` 视口，每一个排印尺寸、内边距和间隙都用 `vw`/`vh` 单位。同一构图在 1280×720、1920×1080 和 2560×1440 显示上无需断点即可正确渲染。因为所有尺寸都相对视口，内容线性缩放——更宽视口上文字和内边距都等比增长，所以视觉密度保持恒定。

### 演示行为
- 右箭头 / 下箭头 / 空格前进到下一页。
- 左箭头 / 上箭头后退。
- Home 跳到第一页；End 跳到最后一页。
- 触控滑动（水平）在移动端前进或后退。
- 鼠标滚轮前进，带 1000ms 防抖，防止意外连跳。
- 幻灯片作为单条 flex 条水平平移，转场 0s（deck 配置为即时导航，不是动画转场——`--dur-slide` token 设为 `0s`）。

### 打印行为
模板没有声明 `@media print` 规则。要出 PDF，用浏览器的截图或打印工具；多页 PDF 导出需要手工触发每一页。

## 中日韩与国际内容

### 推荐中文搭配

| 角色 | 中文字体 | 字重 | 原因 |
|---|---|---|---|
| Display / h1 / h2 / h3 / stat-value（Bricolage 角色，2.4–12vw） | 思源宋体 Noto Serif SC | 700 | 明朝体重字重提供 Bricolage 700–800 在拉丁文里提供的结构体量，同时保住暖材质气质 |
| 引语正文 / 引号（3.4vw / 8vw） | 思源宋体 Noto Serif SC | 600–700 | 编辑时刻用同一明朝体声音 |
| 导语 / 正文 / 图注（DM Sans 角色，0.82–1.5vw） | 思源宋体 Noto Serif SC | 400 | 明朝体正文声音——平静而有材质；与木光暖意配对 |
| Info-card 正文 / 标题 | 思源宋体 Noto Serif SC | 400 / 600 | 在中文里保持绿上暖纸的对比 |
| 标签 / 眉题 / 铬件 / 页脚（DM Mono 角色，0.7vw） | 思源宋体 Noto Serif SC | 500，0.05em 字距 | 替换 DM Mono——中文没有读成编辑铬件的等宽传统 |

### 中西混排策略

用 **策略 A** —— 所有角色整套换成 Noto Serif SC，替换 Bricolage Grotesque（展示）、DM Sans（正文）和 DM Mono（标签）。Mat 的身份不依赖特定拉丁字体；它依赖**带木棕气氛光晕的深森林绿画布**、**单一暖橙强调**、**奶油 info-card 内嵌**，以及 **1px 发丝分隔语言**。中文全明朝体能干净地保住每一个身份标记，而不会引入策略 C 在视口流体系统上会造成的基线晃动。栈：

```css
/* Bricolage roles (display, h1, h2, h3, stat-value, quote) */
font-family: 'Bricolage Grotesque', 'Noto Serif SC', sans-serif;
/* DM Sans roles (lead, body, caption) */
font-family: 'DM Sans', 'Noto Serif SC', sans-serif;
/* DM Mono roles (label, kicker, chrome, footer) */
font-family: 'DM Mono', 'Noto Serif SC', monospace;
```

系统源目前把 `'Noto Sans SC'` 列为中日韩回退——就 Mat 的材质触感气质，**换成 `'Noto Serif SC'`**。明朝体暖字形比几何的 Noto Sans SC 更匹配木光 / 森林绿气氛，后者对本系统读成过于现代临床。

### 加载

用 Noto Serif SC 替换现有的 Noto Sans SC 链接：

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;500;600;700&display=swap" rel="stylesheet">
```

### 通用中日韩调整

这些调整适用于本系统里的**每一个中日韩块**，不论尺寸或角色：

- **把行高放宽 0.05–0.08。** 中日韩字形是全宽方块，视觉重量比拉丁字母大；为拉丁调的行高（展示 0.88–1.1，正文 1.5–1.65）在中文里会读成挤。展示提到 1.0–1.2，正文提到 1.7–1.85。
- **去掉中文标题上的负字距。** Bricolage 展示用 -0.025em 到 -0.03em 字距，会把汉字挤在一起。中文段设 `letter-spacing: 0`——若标题看起来仍挤，可用极小的正值 `0.02em`。
- **从不要对中日韩文本使用 `text-transform: uppercase`。** 中文没有大小写；这条 CSS 对汉字什么也不做，却会悄悄弄坏混排行里本该大写的 DM Mono 标签部分。（这里很要紧——每一个 DM Mono 标签、眉题、铬件带和页脚都是 `text-transform: uppercase`。）
- **中文句子里用中文全角标点**（`，。：；！？「」『』（）`），不要用拉丁等价物（`,.:;!?""''()`）。同一句里混用两套标点系统，读起来像排版错误。
- **中文标题末尾不要句号（。）。** 中文标题遵循与拉丁相同的规则——标题式行去掉句末标点。正文段落保留 。
- **在中日韩与拉丁段的交界处应用盘古之白。** 汉字与相邻的拉丁词或数字之间要有空格（或 0.25em 边距），例如 `2026 年 5 月` 而不是 `2026年5月`。可以手打空格，或用 `pangu.js` 一类的自动加空。
- **一句只用一套字体。** 不要在同一句里在 Noto Serif SC 字重 400、500 和 700 之间切换——按角色选字重（标题 = 700，正文 = 400，标签 = 500），整段坚持用它。

### 本系统的审美说明

Mat 的整体声音是「工业设计作品集遇见精品产品发布」——深森林绿配木棕光晕，奶油字浮在场上，暖橙作唯一强调。在中文里，系统身份不依赖 Bricolage / DM Sans / DM Mono 三件套；它依赖**环境气氛**（每一页深色幻灯片上的径向木光）、**单一强调纪律**（橙只作眉题、em 破折号项目符、行内强调），以及作为签名材质对比动作的**奶油 info-card**。这些全部无需修改即可翻译。

橙色 em 破折号项目符在中文里同样工作——em 破折号字符（—）在任何文字系统里都是同一字形，前置到中文列表项上的橙色 Noto Serif SC 字重 500 读成刻意标记，与拉丁完全一样。项目符列保持 Noto Serif SC 字重 500（替换 DM Mono）；明朝体的暖意比无衬线铬件字体更匹配系统的材质触感气质。

Bricolage 规则「始终大小写混排，从不全大写」在中文里很有意思——中文没有大小写，规则自动满足。但系统对标签的全大写规则（DM Mono、0.12em 字距）无法翻译；在中文里，标签应是 **Noto Serif SC 字重 500、正字距 0.05em**，不要 `text-transform`。正字距单靠字重和间距把铬件质感带过去。

`<em>` 行内橙规则（数据数字里的单位后缀）在中文里工作——像「万」或「亿」这样的中文单位字符放进 `<em>` 会渲染为暖橙并保持直立，恰好镜像拉丁模式。用法相同：`4.7<em>万</em>` 表示 `4.7 万 (47k)`。

### 已知中日韩缺口

Bricolage Grotesque「重、圆、带机械性格的无衬线」是 Mat 在拉丁文里最鲜明的排印动作之一——正是它给系统工业产品页声音。中文没有精确等价物：Noto Serif SC 字重 700 提供结构体量，但读成比 Bricolage 的圆现代更传统 / 文学。中文渲染失去一些工业设计品质，部分由木光气氛和暖橙强调承担更多性格工作来补偿。对工业气质至关重要的 deck（例如专门关于硬件或材质设计的产品发布 deck），可考虑只在最大展示时刻（封面、hero）用 **思源黑体 Noto Sans SC 字重 800** 补充 Noto Serif SC——Noto Sans SC 800 的几何重量比 Noto Serif SC 更接近 Bricolage Grotesque 800。省着用，好在其余地方保住文学-材质气质。

## 迭代指南

1. 任何新组件都作为奶油文字坐在深色表面上；除非是 info-card 动作（奶油对绿的色调对比），否则不要用卡片、面板或画框包它。
2. 任何新标题都用大小写混排的 Bricolage Grotesque，字重 700（h2）或 800（display/h1）。展示从不要伸手去字重 500。
3. 任何新结构分隔都是低不透明度奶油或深墨的 1px 发丝线。从不要用更粗或上色的边框。
4. 任何新标签、眉毛、标记或元信息文字都用 DM Mono 全大写、0.12em 字距。这里不存在大小写混排的等宽。
5. 任何新项目列表都用 DM Mono 着色暖橙的 em 破折号前缀。标记字体和颜色不可商量。
6. 任何新强调时刻（高亮数字、强调词、眉题）都用暖橙。不要引入第二个强调色。
7. 任何新深色页都在 `::before` 上带气氛光晕。若你做自定义幻灯片布局，复制这个伪元素，否则这一页会读成平。
8. 若一页需要一块暖纸来锚定（CTA、摘要、署名块），用 info-card。不要发明平行的卡片模式。
9. 色调断开页（奶油背景）每套 deck 用一次作强调，不是深色的日常替代。系统读成深色默认。

## 已知缺口

- `--c-bg-dark-alt`（#2E3D30）变量定义为略浅的绿色表面，但没有任何选择器主动使用。留给未来的分层区域工作。
- 气氛光晕通过 `::before` 伪元素硬编码到右下角。重新定位需要直接改 CSS 规则；没有光晕位置或强度的 token。
- 系统加载四套 Google Fonts（Bricolage Grotesque、DM Sans、DM Mono、Noto Sans SC）——渲染一致性依赖这些字体加载。中日韩回退栈覆盖中文，但日文和韩文字形回退到系统衬线/无衬线。
- 幻灯片转场时长设为 `0s`（即时）。`--ease-slide` 和 `--dur-slide` token 为动画存在但是惰性的；若一套 deck 需要动画转场，必须提高时长值。
- 垂直柱状图在每个柱填充上使用内联 `style="height: XX%"` 声明。没有数据绑定层；柱高必须手工计算。
- `.split-center` 图片区域固定 52vh 高。高的竖构图影像可能需要版式级覆盖。
- 导航点和页码计数使用硬编码的 `rgba(255,255,255,...)` 值，不会适配奶油页变体——奶油页上白点读成洗掉了。
