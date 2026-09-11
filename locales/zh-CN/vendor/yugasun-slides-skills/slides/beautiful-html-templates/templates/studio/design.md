---
version: alpha
name: Studio
description: "A \"Boring Studios\" agency presentation system — type-as-graphic-mass in the spirit of contemporary design-studio decks (Pentagram, Anti, Order). The entire system runs on Barlow at weight 900 uppercase, with type so heavy at display scale that it stops being type and starts being a shape. The palette is binary plus one: near-black field (#1C1C1C), acid yellow type (#F5D200), and the same yellow as a full slide background. IBM Plex Mono carries every footer metadata, slide counter, and three-column lockup. No drop shadows, no rounded corners, no accent colors — the headline IS the design, and the only chromatic decision per slide is dark-yellow-on-near-black or near-black-on-acid-yellow."

colors:
  near-black: "#1C1C1C"
  near-black-alt: "#242422"
  acid-yellow: "#F5D200"
  acid-yellow-alt: "#F0CC00"
  text-on-dark-2: "rgba(245,210,0,0.58)"
  text-on-dark-3: "rgba(245,210,0,0.32)"
  text-on-light-2: "rgba(28,28,28,0.62)"
  text-on-light-3: "rgba(28,28,28,0.35)"
  border-dark: "#2E2E2C"
  border-light: "rgba(28,28,28,0.18)"

color-aliases:
  c-bg: near-black
  c-bg-alt: near-black-alt
  c-bg-light: acid-yellow
  c-bg-light-alt: acid-yellow-alt
  c-fg: acid-yellow
  c-fg-light: near-black
  c-accent: acid-yellow
  c-fg-2: text-on-dark-2
  c-fg-3: text-on-dark-3
  c-fg-light-2: text-on-light-2
  c-fg-light-3: text-on-light-3

typography:
  display:
    fontFamily: "Barlow, Noto Sans SC, sans-serif"
    fontSize: 12vw
    fontWeight: 900
    lineHeight: 0.9
    letterSpacing: -0.02em
    textTransform: uppercase
  h1:
    fontFamily: "Barlow, Noto Sans SC, sans-serif"
    fontSize: 7.5vw
    fontWeight: 900
    lineHeight: 0.92
    letterSpacing: -0.02em
    textTransform: uppercase
  h2:
    fontFamily: "Barlow, Noto Sans SC, sans-serif"
    fontSize: 4.8vw
    fontWeight: 900
    lineHeight: 0.95
    letterSpacing: -0.01em
    textTransform: uppercase
  h3:
    fontFamily: "Barlow, Noto Sans SC, sans-serif"
    fontSize: 2.8vw
    fontWeight: 700
    lineHeight: 1.1
    textTransform: uppercase
  quote-text:
    fontFamily: "Barlow, Noto Sans SC, sans-serif"
    fontSize: 3.8vw
    fontWeight: 900
    lineHeight: 1.05
    letterSpacing: -0.02em
    textTransform: uppercase
  stat-value:
    fontFamily: "Barlow, Noto Sans SC, sans-serif"
    fontSize: 5.5vw
    fontWeight: 900
    lineHeight: 0.9
    letterSpacing: -0.03em
    textTransform: uppercase
  lead:
    fontFamily: "Barlow, Noto Sans SC, system-ui, sans-serif"
    fontSize: 1.6vw
    fontWeight: 500
    lineHeight: 1.45
  body:
    fontFamily: "Barlow, Noto Sans SC, system-ui, sans-serif"
    fontSize: 1.15vw
    fontWeight: 400
    lineHeight: 1.6
  caption:
    fontFamily: "Barlow, Noto Sans SC, system-ui, sans-serif"
    fontSize: 0.85vw
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "IBM Plex Mono, monospace"
    fontSize: 0.72vw
    fontWeight: 500
    letterSpacing: 0.06em

spacing:
  pad-x: 5vw
  pad-y: 5vh
  gap-lg: 3.5vh
  gap-md: 2vh
  gap-sm: 1vh

canvas:
  width: 100vw
  height: 100vh

components:
  chrome-bar:
    borderBottom: "1px solid {colors.border-dark} (or {colors.border-light} on yellow)"
    paddingBottom: "{spacing.gap-sm}"
    marginBottom: "{spacing.gap-md}"
    description: "Top chrome bar — mono label left, mono counter right, hairline rule beneath."
  foot-bar:
    borderTop: "1px solid {colors.border-dark} (or {colors.border-light} on yellow)"
    paddingTop: "{spacing.gap-sm}"
    marginTop: "{spacing.gap-md}"
    description: "Bottom chrome bar — mirror of chrome-bar."
  cover-meta:
    display: "grid 1fr 1fr 1fr"
    borderTop: "1px solid rgba(245,210,0,0.25)"
    description: "Three-column mono metadata footer over the cover image: studio × client + date, presentation title (center), studio name (right). The signature 'Boring Studios' lockup."
  stat-card:
    borderTop: "2px solid (acid-yellow on dark, near-black on yellow)"
    padding: "{spacing.gap-md} {spacing.gap-md} {spacing.gap-md} 0"
    description: "Stat tile with a 2px top rule. Value at 5.5vw weight 900 in the surface's foreground color; label and mono note beneath."
  bullet-marker:
    content: "—"
    color: "acid-yellow on dark, near-black on yellow"
    fontFamily: "{typography.body.fontFamily}"
    description: "Em-dash bullet prefix on every list item; color follows the surface accent."
  compare-divider:
    borderRight: "2px solid (near-black on yellow, dark-text-3 on dark)"
    description: "Single vertical 2px rule separating two compare panels."
  bar-fill-default:
    background: "muted text-on-surface (dark-text-3 or light-text-3)"
    description: "Default chart bar fill — muted version of the surface text color."
  bar-fill-accent:
    background: "acid-yellow on dark, near-black on yellow"
    description: "Highlighted chart bar — the surface's primary foreground color."
  chart-baseline:
    height: "2px"
    background: "muted accent (dark-text-3 or border-light)"
    description: "Heavier 2px baseline beneath chart bars — Studio uses thicker rules than Signal."
  cover-img-area:
    position: "absolute inset 0"
    background: "{colors.near-black-alt}"
    description: "Cover image placeholder filling the entire slide behind the cover-type and cover-meta. Image-or-placeholder occupies the whole canvas; type sits on top."
  img-placeholder:
    background: "near-black-alt on dark, acid-yellow-alt on yellow"
    description: "Warm-toned rectangular placeholder for images, centered mono label inside, no border on dark / hairline border on yellow."
---

## 概览

Studio 是一套**以字当图形块**的演示系统——视觉语域来自当代设计工作室幻灯片（Pentagram、Anti、Order、「Boring Studios」机构审美）。前提被压缩到近乎严厉：单一字体（Barlow），单一字重（900），严格大写，字号大到字体不再像字体，而开始像图形形状。标题就是设计——没有装饰元素，没有强调色，没有纹样。如果你从一张 Studio 幻灯片上拿掉其他一切，只留下标题，这一页仍然读作 Studio。

色板是**二元加一**。深色表面是 `{colors.near-black}`（#1C1C1C）——暖深色，不是冷中性。浅色表面是 `{colors.acid-yellow}`（#F5D200）——饱和镉黄，铺满整页，不是强调色而是环境。深色页上，文字是 `{colors.acid-yellow}`。黄底页上，文字是 `{colors.near-black}`。这就是整套颜色系统：深/黄，黄/深。没有次级色，没有灰，没有暖强调。甚至弱化文字也只是同一颜色降低不透明度（黄 58%，近黑 62%）。

字体栈是**功能导向而非表现导向**。Barlow 字重 900 承担每一个字号的每一个标题——从 1.15vw 正文一路到 12vw 封面展示。Barlow 500 承担正文和导语段落。IBM Plex Mono 承担元数据页脚、幻灯片计数器，以及三列封面 lockup——也是系统里第二套字体出现的唯一位置。等宽是系统的「规格表」声线；其他地方一律 Barlow 主导。

纵深是**扁平而严厉的**。没有投影。没有圆角。没有渐变。边框是 1px 或 2px 发丝线，颜色为 `{colors.border-dark}` 或 `{colors.border-light}`。2px 图表基线和 2px stat-card 顶线是系统里最重的线。系统读起来像建筑图或宣言海报——每条线都有意图，没有任何装饰。

**密度哲学：低而刻意。** Studio 天生稀疏。陈述页是一条标题填满大部分画布，上下留空。章节页是一个小等宽标签加一条标题。封面是 12vw 的一个词后面垫图片占位。内边距比 Signal 更紧（5vw / 5vh vs 7.5vw / 5.5vh），因为字体本身几乎跑到边缘——填满空间的是标题，不是页边。一张在 Studio 里读起来坏掉的幻灯片，是里面有多个互相抢戏的元素，或用正文段落填满画布。正确语域是「一件巨大的事，说一次，用 900 字重大写。」

**关键特征：**
- 二元色板——`{colors.near-black}` 底配 `{colors.acid-yellow}` 字，或 `{colors.acid-yellow}` 底配 `{colors.near-black}` 字。没有第三色。
- 每一个字号的每一个标题都用 Barlow 字重 900 大写；正文用 Barlow 400/500；IBM Plex Mono 只用于元数据铬件。
- 标题跑得巨大——封面展示 12vw（1920px 视口约 230px），陈述 7.5vw，章节头 4.8vw。
- 所有展示字使用紧凑负字距（-0.01 到 -0.03em）；大写不可商量。
- 扁平：无投影、无圆角、无渐变，除黄/深二元之外无强调色。
- 铬件用 1px 发丝边框；stat-card 顶线、图表基线和对比例面板分隔用 2px。
- 封面页的三列等宽元数据页脚是系统的签名 lockup（studio × client / 演示标题 / 工作室名）。
- 列表标记用表面强调色的破折号（深底用黄，黄底用近黑）。
- 正文与铬件用同一颜色的不透明度变体（黄 58%/32%，近黑 62%/35%）——从不单独用灰色。

## 颜色

### 色板

- **Near-Black**（`{colors.near-black}` — #1C1C1C）：深色表面。暖深色，略偏棕，不是冷中性。系统的「墨」。
- **Near-Black Alt**（`{colors.near-black-alt}` — #242422）：略微抬起的近黑，用于图片占位和次级深色表面。视觉上与 near-black 几乎相同。
- **Acid Yellow**（`{colors.acid-yellow}` — #F5D200）：浅色表面，同时也是深色表面上的主文字色。镉黄，饱和、略暖。深色页上这是字体色。浅色页上这是背景。同一颜色，两种角色。
- **Acid Yellow Alt**（`{colors.acid-yellow-alt}` — #F0CC00）：略冷一点的黄，用于浅色页上相邻表面的区分。使用克制。
- **Text on Dark 2**（`{colors.text-on-dark-2}` — rgba(245,210,0,0.58)）：深底上的次级文字——黄 58% 不透明度。系统从不单独用「灰」；弱化只靠不透明度。
- **Text on Dark 3**（`{colors.text-on-dark-3}` — rgba(245,210,0,0.32)）：深底上的三级文字——黄 32%。
- **Text on Light 2**（`{colors.text-on-light-2}` — rgba(28,28,28,0.62)）：黄底上的次级文字——近黑 62%。
- **Text on Light 3**（`{colors.text-on-light-3}` — rgba(28,28,28,0.35)）：黄底上的三级文字——近黑 35%。
- **Border Dark**（`{colors.border-dark}` — #2E2E2C）：深色表面上的发丝边框色。比 near-black 略抬，好让它读作一条线，而不是空洞。
- **Border Light**（`{colors.border-light}` — rgba(28,28,28,0.18)）：黄表面上的发丝边框色。低不透明度近黑，做轻微分隔。

### 默认值

- **默认表面**：在整套幻灯片里交替使用 `{colors.near-black}`（深）和 `{colors.acid-yellow}`（浅）。两种表面都是一等公民。拿不准时，封面/引语/陈述页用 near-black，章节页和结尾页用 acid-yellow。
- **深底默认主文字**：`{colors.acid-yellow}`。
- **黄底默认主文字**：`{colors.near-black}`。
- **深底默认次级文字**：`{colors.text-on-dark-2}`（黄 58% 不透明度）。
- **黄底默认次级文字**：`{colors.text-on-light-2}`（近黑 62%）。
- **默认三级文字**（等宽图注、图表坐标标签、统计注释）：表面强调色的第三档不透明度。
- **深底默认边框**：`{colors.border-dark}`。
- **黄底默认边框**：`{colors.border-light}`。
- **默认标题色**：表面强调色——深底用黄，黄底用近黑。从不用其他颜色。
- **默认图表强调填充**：表面强调色（深底用黄，黄底用近黑）。「高亮」柱就是主文字色；「默认」柱是第三档弱化。

没有语义色角色。黄不表示「警告」；近黑不表示「主色」。它们只是两块表面。在两者之间选择是节奏性的——交替以变化视觉节拍，或连续几张深色页形成安静段落，再用一张黄页当标点时刻。

## 字体

### 字族

Studio 跑**两套字族**，角色严格分开：

- **Barlow**（`{typography.display.fontFamily}`）——当代 grotesque，字重轴很宽。承担每一个字号的每一个标题（display 到 h3）、每一个数字（stat-value）、每一条引语、全部正文和全部导语段落。系统对所有展示和标题 token 用字重 900；h3 用字重 700；导语和列表标记用字重 500；正文和图注用字重 400。
- **IBM Plex Mono**（`{typography.label.fontFamily}`）——精密等宽。**只**用于元数据标签——铬件条、幻灯片计数器、章节编号、三列封面 lockup、统计注释、cover-meta 内的等宽图注。等宽是系统的「元数据声线」；其他地方一律 Barlow 主导。

情绪划分是二元的：Barlow 承担内容（响、大写、主导）；IBM Plex Mono 承担规格表元数据（小、精确、辅助）。没有第三套字体。

Barlow 字重 900 在展示字号上不再像字体，而开始像图形形状——字形重到字怀（字母内部的孔）变成结构性负空间，标题先读成黑或黄的几何块，然后才读成词。这就是系统的身份。

### 字号阶梯

| Token | 尺寸 | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.display}` | 12vw | Barlow | 900 | 封面 hero，最大字号 |
| `{typography.h1}` | 7.5vw | Barlow | 900 | 章节标题、整页陈述标题 |
| `{typography.stat-value}` | 5.5vw | Barlow | 900 | 统计卡片内的数据数字 |
| `{typography.h2}` | 4.8vw | Barlow | 900 | 幻灯片主标题 |
| `{typography.quote-text}` | 3.8vw | Barlow | 900 | 引文正文（大写，无引号） |
| `{typography.h3}` | 2.8vw | Barlow | 700 | 副标题、面板标题 |
| `{typography.lead}` | 1.6vw | Barlow | 500 | 导语段落、开场句 |
| `{typography.body}` | 1.15vw | Barlow | 400 | 默认正文段落、列表正文 |
| `{typography.caption}` | 0.85vw | Barlow | 400 | 图注、来源署名 |
| `{typography.label}` | 0.72vw | IBM Plex Mono | 500 | 等宽铬件、幻灯片计数、章节编号、统计注释、cover-meta |

### 默认值

- **主章节标题默认尺寸**：`{typography.h2}`（4.8vw）。
- **章节或陈述标题默认尺寸**：`{typography.h1}`（7.5vw）。
- **封面 hero 默认尺寸**：`{typography.display}`（12vw）。
- **段落正文默认尺寸**：`{typography.body}`（1.15vw）。
- **导语句默认尺寸**：`{typography.lead}`（1.6vw）。
- **任何铬件标签、计数器或等宽图注默认尺寸**：`{typography.label}`（0.72vw）。
- **数据数字默认尺寸**：`{typography.stat-value}`（5.5vw），表面强调色。
- **任何标题默认字重**：900。
- **任何正文元素默认字重**：400（导语 = 500）。

拿不准尺寸时，偏大。Studio 的身份依赖字体跑得巨大——4.8vw 的 h2 读作本系统；把 2.8vw 的 h3 当主标题会读成另一套系统。

### 标志性处理

只要用到对应元素类型，这些处理就是**不可省略的**：

- **每一个 display、h1、h2、h3、quote-text 和 stat-value 都是大写。** 不存在句首大写的展示字。即使 h3（2.8vw）字重 700 也跑大写。
- **每一个展示标题都用字重 900。** display、h1、h2、quote-text 和 stat-value 全是字重 900——没有例外。展示字号用字重 800 或 700 会破坏以字当图形块的效果。
- **每一个展示元素都使用负字距。** display –0.02em，h1 –0.02em，h2 –0.01em，stat-value –0.03em。没有负字距的 Barlow 900 展示字读起来像没处理过；负字距才给字体带来压缩密度。
- **所有铬件、标签、计数器和元数据都是 IBM Plex Mono，字距 0.06em。** 没有例外。用 Barlow 写等宽标签会破坏元数据/内容分离。
- **标题始终用表面强调色渲染**——深底用黄，黄底用近黑。从不用弱化不透明度，从不用别的颜色。
- **正文列表用表面强调色的破折号**，从不用圆点，从不用别的字形。破折号带表面感知色（深底用黄，黄底用近黑）。
- **统计卡片有 2px（不是 1px）顶线**，颜色为表面强调色（深色一侧可用弱化强调）。2px 线比铬件发丝线更重，因为统计是锚点。
- **三列 cover-meta lockup 使用 IBM Plex Mono，第 1 列左对齐，第 2 列居中，第 3 列右对齐。** 这是「Boring Studios」签名；列结构不可商量。

### 排版原则

字族阶梯是固定的：除元数据外一律 Barlow；元数据只用 IBM Plex Mono。等宽出现在元数据角色之外，或 Barlow 出现在元数据角色之内，都会破坏排版分离。

字重阶梯也是固定的：900 / 700 / 500 / 400。不用中间字重（600、800）。四档字重就是排版的全部表达语域。

行高在展示字号上收紧（display 0.9，h1 0.92），正文放到 1.5–1.6。字距在展示上统一为负（–0.01 到 –0.03em），正文为零，等宽标签为正 0.06em。

不使用斜体。不使用下划线。系统没有 font-style 变化；强调纯粹靠字重对比（900 标题对 400 正文）。

## 布局

### 画布系统

Studio 目标是 `100vw × 100vh`——铺满视口。每个 `.slide` 弹性填满视口，幻灯片并排成水平条带，导航时左右平移。所有尺寸使用视口相对单位（`vw`、`vh`），布局流体缩放。

### 内边距与间距层级

| Token | 值 | 用途 |
|---|---|---|
| `{spacing.pad-x}` | 5vw | 幻灯片水平内边距 |
| `{spacing.pad-y}` | 5vh | 幻灯片垂直内边距 |
| `{spacing.gap-lg}` | 3.5vh | 主要内容区块之间 |
| `{spacing.gap-md}` | 2vh | 相关元素之间 |
| `{spacing.gap-sm}` | 1vh | 紧密耦合元素之间 |

陈述页和章节页把底内边距加大到 1.5× pad-y，让标题落到幻灯片下半，上方刻意留空。封面页外边距为零，因为图片区域填满整块画布。

### 铬件框架

标准幻灯片带顶铬件条和底脚条：

- **铬件条**——左对齐等宽标签，右对齐等宽计数器，下方 1px 发丝线。padding-bottom 是 `{spacing.gap-sm}`，margin-bottom 是 `{spacing.gap-md}`。
- **脚条**——左对齐等宽标签，右对齐等宽计数器，上方 1px 发丝线。铬件条的镜像。

封面、章节、陈述、引语和结尾页省略标准铬件——这些版式要么用 cover-meta lockup（封面），要么什么都不用（章节、陈述、引语、结尾）。

### 封面组合

封面页是系统的签名版式：
- 图片占位填满整块画布，垫在所有内容后面。
- 一条展示标题（通常是 12vw 的一个词）坐在上方区域，作为 `cover-type`。
- 三列等宽元数据页脚坐在底部——第 1 列左（"studio × client" + 日期），第 2 列中（演示标题），第 3 列右（工作室名）——与图片区域之间用 1px 发丝线分隔，黄色 25% 不透明度。

## 纵深与抬升

Studio **设计上就是扁平的**。没有投影。没有圆角卡片抬升。没有渐变。每个元素都与表面齐平。

表观纵深来自：
- **表面对比**——near-black 对 acid-yellow，当两者同时出现时（对比例面板、图片占位）。
- **发丝分隔**——1px 和 2px 边框划分区域。
- **重字体**——字重 900 的展示标题形成视觉块，在扁平表面上读作前景。

系统故意严厉。如果一个版式需要抬升才能读对，这个版式就不适合 Studio——减少内容或重组，让扁平表面 + 重字体 + 发丝线提供足够层级。

## 形状与处理

### 圆角

| 值 | 用途 |
|---|---|
| 0 | 系统里的一切 |
| 50%（圆形） | 仅导航点和幻灯片计数 UI（不属于幻灯片内容） |

Studio **没有圆角铬件**。卡片、面板、统计砖、图表框、图片占位、对比例面板——全部是直角严格矩形。唯一的圆形是导航点和底层幻灯片计数 UI，那是 deck-stage 铬件，不是幻灯片内容。

### 边框粗细

- **1px solid**，颜色 `{colors.border-dark}`（near-black 上）或 `{colors.border-light}`（黄上）——通用发丝线。用于铬件条、脚条、cover-meta 分隔。
- **2px solid**，颜色为表面强调色（深底用黄，黄底用近黑）——更重的线。用于 stat-card 顶线、对比例面板竖分隔、图表基线、图表柱轨道左线。
- **没有虚线边框。** 系统里每条边框都是实线。

### 装饰元素类型

**展示标题当图形块**——Barlow 字重 900 在展示字号（4.8vw 及以上）上坐成黑或黄的几何块。标题是每一页的主装饰元素；没有额外纹样。

**发丝线**——表面边框色的 1px 实线。用于分隔铬件与正文、正文与脚，以及对比例面板内部。这条线是系统唯一的结构分隔。

**重线**——表面强调色（或弱化强调）的 2px 实线。用于 stat-card 顶、图表基线、对比例面板竖分隔。比铬件发丝线更重；读作「锚点」而不是「分隔」。

**统计卡片**——扁平区域，带 2px 顶线、表面强调色的统计数字（5.5vw Barlow 900）、统计标签（1.15vw Barlow 500），以及可选的等宽统计注释（0.85vw IBM Plex Mono，第三档不透明度）。右和底有内边距；左内边距为零（线与卡片左缘齐平）。

**Cover-meta lockup**——封面页底部的三列等宽页脚。第 1 列：第 1 行 studio × client 名，第 2 行日期。第 2 列：演示标题（居中）。第 3 列：工作室名（右对齐）。与 cover-type 之间用 1px 发丝线分隔，黄色 25% 不透明度。

**图片占位**——扁平矩形，填充 `{colors.near-black-alt}`（深底）或带发丝边框的 `{colors.acid-yellow-alt}`（黄底），内含居中 IBM Plex Mono 文字，第三档不透明度。用于尚未填入的图片槽。

**图表柱**——扁平竖矩形，默认用弱化的 text-on-surface 色，高亮用表面强调色。没有圆端，没有渐变。"hi" 变体使用完整强调色，数值标签字重 900。

**图表基线**——弱化表面强调色（深底用黄第三档，黄底用 border-light）的 2px 实线，横贯图表容器全宽，位于柱顶下方。

**破折号列表标记**——每个列表项前缀 `—`，表面强调色，右边距 0.5em。颜色随表面翻转。

## 该做与不该做

### 该做

- 每一个字号的每一个标题都用 Barlow 字重 900 大写，负字距至少 -0.01em。以字当图形块的效果就是系统身份。
- 自由交替 `{colors.near-black}` 和 `{colors.acid-yellow}` 表面。两者都是一等公民；深/黄交替的节奏就是系统的节拍。
- 每条标题都用表面强调色——深底用黄，黄底用近黑。从不用弱化版本，从不用第三色。
- IBM Plex Mono 只用于元数据（铬件标签、幻灯片计数器、章节编号、cover-meta lockup、统计注释、等宽图注）。等宽是规格表声线；从不用于内容。
- 把 cover-meta 页脚渲染成三列等宽 lockup（左/中/右）。这是系统的签名模式。
- 用不透明度弱化次级文字（黄上 .58，近黑上 .62），不要用单独的灰色。系统没有灰——只有黄和近黑的不透明度变体。
- 对 stat-card 顶、图表基线和对比例面板分隔用 2px 线。2px 粗细把「锚点」元素与铬件发丝线区分开。
- 用表面强调色的破折号当列表标记——从不用圆点，从不用圆圈。
- 把幻灯片内边距收紧（5vw / 5vh），让展示字靠近边缘。Studio 依赖字体填满画布；宽松内边距会破坏字号效果。
- 让陈述页和章节页刻意稀疏。一条巨大标题对着空表面，才是这些页型的正确语域。

### 不该做

- 不要把标题改成小写。每一个 Barlow 900 元素都跑大写，没有例外。
- 不要在展示字号用字重 800 或 700。Display = 始终字重 900。
- 不要给色板加第三色。系统是二元加不透明度变体——加入红、蓝或任何强调色都会破坏二元逻辑。
- 不要给任何角加圆。到处都是严格矩形；只有导航点是圆。
- 不要加投影或渐变。系统极度扁平——纵深来自对比和字重，不是抬升。
- 不要用 Barlow 写铬件元数据。等宽是元数据声线；用 Barlow 写铬件会读成内容而不是规格。
- 不要用 Mono 写标题或正文。等宽只活在元数据角色里。
- 不要为强调加入斜体、下划线或颜色变体。唯一的强调机制是字重对比（900 vs 400）。
- 不要引入虚线边框。系统里每条线都是实线。
- 不要让典型幻灯片的内容超过约 60%。空表面是结构性的——挤满时 Studio 读起来像坏掉。

## 响应式行为

Studio 目标是 1920×1080 视口，全程使用视口相对单位（`vw`、`vh`），因此布局在 1280×720 到 2560×1440 之间流体缩放，无需断点。除 deck-chrome 点和幻灯片计数器外，没有固定像素尺寸。

### 缩放行为

- 展示标题缩放：12vw → 1920px 视口约 230px，1280px 约 154px。
- 正文缩放：1.15vw → 1920px 约 22px，1280px 约 15px。
- 内边距缩放：pad-x 5vw → 1920px 约 96px，1280px 约 64px。

2px 和 1px 边框粗细是固定像素，不缩放；在大视口上边框会显得比例更细。

### 演示行为

幻灯片由 JS 驱动，并排成水平条带，导航时左右平移。当前幻灯片带 `is-active`，会触发任何 `[data-anim]` 元素入场。动画比 Signal 更锐、更短（时长 0.5s vs 0.65s；幻灯片 0.75s vs 0.85s）——按源码注释是「机构的紧迫，不是编辑的从容」。动画关键帧包括 fade-up、fade-in、reveal-right、reveal-left、scale-in，带交错 `data-delay`（0–6）。

导航点和幻灯片计数器固定在视口底部——小巧的白字深底 UI，刻意克制。

### 打印行为

没有内嵌打印样式表。水平条带布局需要拆开才能做静态导出。

## CJK 与国际内容

### 推荐中文搭配

| 角色 | 拉丁字体（默认） | 中文字体 | 字重 | 说明 |
|---|---|---|---|---|
| Display / h1 / h2 / quote-text / stat-value | Barlow 900 大写 | 思源宋体 / Noto Serif SC | 700 | Studio 赖以成立的「以字当图形块」效果，依赖单一字体跑到最大字重。NSC 700 是 CDN 上最重的宋体衬线，能在 12vw / 7.5vw / 4.8vw 展示字号上保住视觉块。 |
| h3 | Barlow 700 大写 | 思源宋体 / Noto Serif SC | 700 | 副标题字重对齐。 |
| Lead / Body / Caption | Barlow 500 / 400 | 思源宋体 / Noto Serif SC | 400 | 极简编辑正文——NSC 400 在系统稀疏版式里读得干净。 |
| Metadata / chrome / label / stat-note | IBM Plex Mono 500 | IBM Plex Mono + Noto Sans Mono CJK fallback | 400–500 | 等宽 CJK 很少需要（多数元数据仍是拉丁：日期、计数器、工作室名），但若铬件出现中文，用 Noto Sans Mono CJK SC。 |

### 混排策略

本模板使用 **Strategy A**：任何渲染汉字的元素，整套拉丁字体替换为 CJK 字体。Studio 的身份是以字当图形块——而 Barlow 900 无法渲染 CJK 字形（没有字形覆盖）。同一行里通过栈回退把 Barlow 拉丁与 NSC CJK 混在一起，会在展示字号上产生度量不匹配，破坏「单一字体、单一字重」的语域。任何中文内容元素，把整个 `font-family` 换成 NSC。

```css
font-family: 'Noto Serif SC', 'Barlow', sans-serif;  /* display / headlines — CJK first */
font-family: 'Noto Serif SC', 'Barlow', sans-serif;  /* body — CJK first */
font-family: 'IBM Plex Mono', 'Noto Sans Mono CJK SC', monospace;  /* mono — Latin first, CJK only if needed */
```

纯中文幻灯片里，系统的「大写」身份会脱落（中文没有大小写），所以 Studio 的性格会从「工业机构宣言」转向「中文报纸标题的编辑感」。这是真实的语域变化——中文 Studio 读起来严肃而严厉，但不再读作 Pentagram/Anti。接受这种取舍，或把中文限定在特定页，封面和章节分隔仍用拉丁 Barlow。

### 加载

加到 `<head>`（Google Fonts 托管 Noto Serif SC 和 Noto Sans SC）：

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;700;900&family=IBM+Plex+Mono:wght@400;500&family=Noto+Serif+SC:wght@400;500;700;900&family=Noto+Sans+SC:wght@400;500;700&display=swap" rel="stylesheet">
```

原始 design.md 里的 Barlow 栈已经把 Noto Sans SC 接成 CJK 回退。我们把标题和正文升级到 Noto Serif SC，因为宋体衬线在 900 字重上能带出与 Barlow 900 相当的图形块，而同等字重的 Noto Sans SC 读起来太光滑/太圆，会丢掉「图形块」性格。把 Noto Sans SC 留给只要更干净无衬线的纯正文幻灯片。

### 通用 CJK 调整

应用到任何渲染中文内容的元素（通常通过 `:lang(zh)` 或 `<span lang="zh">` 限定范围）：

- **行高**：正文 1.75–1.85（Studio 默认的 1.5–1.6 Barlow 行高对拉丁合适，对 CJK 笔画偏紧）；展示 1.15–1.25（比拉丁 0.9–0.95 更松，因为 12vw 的 CJK 字形需要垂直呼吸）。
- **字距**：CJK 上为 0。Studio 在拉丁展示上的负字距（-0.01 到 -0.03em）对中文是错的——CJK 字形已预留间距；负字距会在展示字号上让字形相碰或重叠。
- **文本变换**：CJK 不大写。Studio 在展示 token 上的 `text-transform: uppercase` 对汉字是空操作，但要确保没有父级规则触发意外行为。系统的「大写」身份在中文里脱落。
- **全角标点**：用 `，。：；！？`（全角），不用 `,.:;!?`（半角）。全角形式自带周围空白，并对齐 CJK em-box。
- **展示标题不加句号**：中文标题去掉句末 `。`——Studio 拉丁标题从不带句号，这条规则延伸到 CJK。
- **盘古之白（Pangu spacing）**：在 CJK 与相邻拉丁/数字之间插入细空格。写 `使用 Claude` 而不是 `使用Claude`；写 `2024 年` 而不是 `2024年`。Studio 的等宽元数据经常挨着中文标签——那里盘古之白必不可少。
- **一句一字体**：不要在同一行里混用 NSC 和 Noto Sans SC。衬线/无衬线切换应发生在元素边界。

### 本系统审美说明

Studio 的二元色板（近黑上的酸黄，酸黄上的近黑）在 CJK 里完整保留——颜色决策不变。NSC 700 用 `{colors.acid-yellow}` 对着 `{colors.near-black}` 底，在 12vw 展示字号上，能带出与同角色 Barlow 900 相同的视觉冲击；饱和黄对着暖深表面，让汉字读出同样的海报权威。

「以字当图形块」效果在 CJK 里确实被改写，但方式很有意思：Barlow 900 大写块读作西方招牌 / 工业宣言，而 NSC 700 在展示字号上读作**中文木刻或活字海报**——同样严厉，同样图形，但是另一种文化语域。对中文读者这读作权威、设计到位；对混合受众，感知语气会略向「编辑出版物」偏移，离开「设计机构」。

破折号列表标记直接平移——保持表面强调色的 `—`。三列等宽 cover-meta lockup 也不必改——studio × client / 演示标题 / 工作室名用中文或拉丁都行，IBM Plex Mono 都能干净渲染（若 lockup 出现中文，CJK 回退到 Noto Sans Mono CJK SC）。

统计卡片在 CJK 里效果很好——5.5vw 斜体风格的统计数字若是中文数字（`三百万`）可用 NSC 700，若是阿拉伯数字（`3M`）可留在 Barlow。2px 顶线和统计注释（等宽）不受影响。

### 已知 CJK 缺口

- 定义系统的「大写 + 负字距 + 字重 900」公式无法在 CJK 里复现。中文拿到字重 700（最重的 NSC 字重）、无大小写变换、零字距。纯中文模式下系统会丢掉约 30% 的拉丁性格。
- IBM Plex Mono 的完整特性集只覆盖拉丁。若元数据出现汉字（Studio 幻灯片里很少见），会回退到 Noto Sans Mono CJK SC 或系统等宽，比例可能与周围的 Plex Mono 在视觉上不同。
- NSC 900 字重（会更贴近 Barlow 900）在 Google Fonts 上存在，但大尺寸时够重，字怀开始闭合——12vw 展示上，NSC 900 可能把某些字渲成近乎实心块。NSC 700 是建议上限；极端展示时刻逐案测试 NSC 900。
- 系统「交替深/黄表面」的节奏不受 CJK 影响，但中文读者可能以不同于西方读者的方式解析节奏（颜色的文化阅读惯例会影响节拍感知）。

## 迭代指南

1. 任何新标题都用 Barlow 字重 900 大写加负字距。缺了这三项（字重、大小写、字距）中的任何一项，字体就会丢掉图形块性格。
2. 任何新幻灯片都与上一张交替表面——一般不要连续超过 2–3 张深色页才插入一张黄页打断，反之亦然。节奏是设计的一部分。
3. 任何新铬件、元数据、标签或计数器都用 IBM Plex Mono。等宽出现在其他角色会破坏元数据分离。
4. 任何新颜色都会给二元色板引入第三选项——不要。守住黄和近黑，弱化只用不透明度变体。
5. 任何新列表都用表面强调色的破折号标记。圆点列表会破坏系统。
6. 统计卡片用 2px 顶线加 5.5vw 字重 900 数字。更小的统计、句首大写统计或圆角统计砖都会破坏模式。
7. 封面页底部用三列等宽 lockup。不要省略；它是系统最可识别的模式。
8. 章节、陈述、引语和结尾页无铬件。标准页带铬件和脚。不要混用——无铬件的引语是对的；带铬件的引语读成另一套系统。
9. 新版式应瞄准一个主导元素（标题）加最少支撑元素。多元素版式（超过 4–5 个独立区域）会挤满设计。
10. 2px 线粗细留给锚点（统计顶、基线、对比例分隔）。铬件和结构分隔保持 1px。

## 已知缺口

- 两套字族（Barlow、IBM Plex Mono）从 Google Fonts 加载。若字体失败，回退是 Noto Sans SC / system-ui（Barlow）和 monospace（IBM Plex Mono）；没有 Barlow 900 时系统会明显降级，因为以字当图形块的效果依赖特定字形。
- 中文回退（Noto Sans SC）已接到 Barlow 栈，但只随 400、500、700、900 字重出货——中文内容用 h3（700）和 lead（500）渲染干净；中间字重会落到最近可用档。
- `--c-bg-alt`、`--c-bg-light-alt` 和若干弱化颜色 token 已定义但使用很少——它们作为相邻表面区分的储备存在。
- 幻灯片导航 JS 内嵌；系统依赖它做幻灯片条带变换行为和 `is-active` 类管理。
- 封面图片占位使用硬编码的 `IMAGE PLACEHOLDER` 标签和扁平 near-black-alt 填充；真正插入图片需要把占位 div 换成匹配父级画布的 background-image 样式元素。
- 5vw / 5vh 内边距刻意收紧，意味着在很小的视口上标题可能不舒服地靠近边缘；系统针对 1280px 及以上的 16:9 显示器调校。
- 对比例面板只在左面板用 2px 右边框（右面板没有左边框），两块面板不对称——这是刻意的，但若把对比例版式扩展到 3 列，值得注意。
