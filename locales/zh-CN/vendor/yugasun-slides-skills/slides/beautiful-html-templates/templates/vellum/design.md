---
version: alpha
name: Vellum
description: An essay-pinned-to-a-wall presentation system — a single monochromatic field of deep periwinkle (#2A3870) with warm chartreuse-yellow type (#E8D85C) floating centered on it, every slide. Italic Cormorant Garamond carries every headline at all sizes — the italic serif is the personality, against the bold colorfield. DM Sans handles body in a quiet supporting role. Courier Prime mono provides the typed annotation voice — appearing as a "pin-note" attribution sitting in the bottom-left corner of every slide. The mood is gallery exhibition wall meets archive folder — quiet, monochromatic, deeply still. One color, two warm typefaces, zero motion.

colors:
  navy: "#2A3870"
  navy-alt: "#343F80"
  navy-deep: "#1F2858"
  navy-mid: "#34407A"
  yellow: "#E8D85C"
  yellow-2: "rgba(232,216,92,0.62)"
  yellow-3: "rgba(232,216,92,0.32)"
  emphasis-yellow: "#F5E168"
  teal: "#3A7878"
  border: "rgba(232,216,92,0.20)"

color-aliases:
  c-bg: navy
  c-bg-alt: navy-alt
  c-bg-light: navy
  c-fg: yellow
  c-fg-2: yellow-2
  c-fg-3: yellow-3
  c-fg-light: yellow
  c-emphasis: emphasis-yellow
  c-accent: teal
  c-border: border

typography:
  display:
    fontFamily: "Cormorant Garamond, Noto Serif SC, Georgia, serif"
    fontSize: 11vw
    fontWeight: 400
    fontStyle: italic
    lineHeight: 0.92
    letterSpacing: -0.01em
  h1:
    fontFamily: "Cormorant Garamond, Noto Serif SC, Georgia, serif"
    fontSize: 7vw
    fontWeight: 400
    fontStyle: italic
    lineHeight: 0.95
    letterSpacing: -0.01em
  h2:
    fontFamily: "Cormorant Garamond, Noto Serif SC, Georgia, serif"
    fontSize: 4vw
    fontWeight: 400
    fontStyle: italic
    lineHeight: 1.05
  h3:
    fontFamily: "Cormorant Garamond, Noto Serif SC, Georgia, serif"
    fontSize: 2.4vw
    fontWeight: 500
    fontStyle: italic
    lineHeight: 1.15
  quote-text:
    fontFamily: "Cormorant Garamond, Noto Serif SC, Georgia, serif"
    fontSize: 3.2vw
    fontWeight: 400
    fontStyle: italic
    lineHeight: 1.25
  quote-mark:
    fontFamily: "Cormorant Garamond, Noto Serif SC, Georgia, serif"
    fontSize: 7vw
    fontWeight: 400
    fontStyle: italic
    lineHeight: 0.6
    color: "{colors.teal}"
  stat-value:
    fontFamily: "Cormorant Garamond, Noto Serif SC, Georgia, serif"
    fontSize: 5.5vw
    fontWeight: 400
    fontStyle: italic
    lineHeight: 1
    letterSpacing: -0.02em
  lead:
    fontFamily: "DM Sans, Noto Sans SC, system-ui, sans-serif"
    fontSize: 1.5vw
    fontWeight: 400
    lineHeight: 1.6
  body:
    fontFamily: "DM Sans, Noto Sans SC, system-ui, sans-serif"
    fontSize: 1.05vw
    fontWeight: 400
    lineHeight: 1.65
  caption:
    fontFamily: "DM Sans, Noto Sans SC, system-ui, sans-serif"
    fontSize: 0.85vw
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "Courier Prime, Courier New, monospace"
    fontSize: 0.72vw
    fontWeight: 400
    letterSpacing: 0.06em
  pin-note:
    fontFamily: "Courier Prime, Courier New, monospace"
    fontSize: 1.15vw
    fontWeight: 500
    lineHeight: 1.5
    color: "{colors.teal}"
    letterSpacing: 0.01em
  bar-val:
    fontFamily: "Courier Prime, Courier New, monospace"
    fontSize: 1.1vw
    fontWeight: 400
    lineHeight: 1

spacing:
  pad-x: 6vw
  pad-y: 6vh
  gap-lg: 5vh
  gap-md: 3vh
  gap-sm: 1.5vh

canvas:
  width: 100vw
  height: 100vh

components:
  pin-annotation:
    position: "absolute bottom-left, padding ~0.9 * pad-y from bottom and 1 * pad-x from left"
    typography: "{typography.pin-note}"
    color: "{colors.teal}"
    maxWidth: "22vw"
    description: "The system's signature element — a small stack of Courier Prime mono lines in dusty teal, sitting in the bottom-left of every slide. Holds slide counter (e.g., '03 / 09'), a short pinned label, and an optional second pin note. Functions as the 'tag stuck to the wall.'"
  kicker:
    typography: "{typography.label}"
    color: "{colors.teal}"
    description: "Small Courier Prime mono label in dusty teal, sits above a headline as a section marker."
  rule:
    width: 28px
    height: 1px
    background: "{colors.teal}"
    description: "A 28px hairline accent rule in dusty teal, used as a small kicker separator."
  chrome-bar:
    borderBottom: "1px solid {colors.border}"
    paddingBottom: "{spacing.gap-sm}"
    marginBottom: "{spacing.gap-md}"
    description: "Top chrome bar — mono label left, mono counter right, low-opacity hairline rule beneath."
  foot-bar:
    borderTop: "1px solid {colors.border}"
    paddingTop: "{spacing.gap-sm}"
    marginTop: "{spacing.gap-md}"
    description: "Bottom chrome bar — mirror of chrome-bar."
  bullet-list-numbered:
    listStyle: "none"
    counter: "list-counter"
    markerFontFamily: "{typography.label.fontFamily}"
    markerColor: "{colors.teal}"
    markerSize: "{typography.label.fontSize}"
    description: "Numbered list using CSS counters — the counter renders in Courier Prime mono at label size in dusty teal, with a 2em column for the number and 0.5em gap to the body."
  pin-stat:
    borderRight: "1px solid {colors.border}"
    padding: "{spacing.gap-md}"
    description: "Vertically-arranged centered stat (italic serif numeral above mono label), separated from neighbors by a single 1px low-opacity hairline. Last stat in row drops the border."
  pin-stat-val:
    typography: "{typography.stat-value}"
    color: "{colors.yellow}"
    description: "Large italic serif stat numeral (5.5vw italic Cormorant Garamond), centered in a pin-stat tile."
  pin-stat-label:
    typography: "{typography.caption}"
    fontFamily: "{typography.label.fontFamily}"
    color: "{colors.yellow-2}"
    description: "Small mono caption beneath a pin-stat numeral."
  compare-panel-dark:
    background: "{colors.navy-deep}"
    description: "Left compare panel — a slightly deeper navy to create internal contrast against the standard navy field."
  compare-panel-light:
    background: "{colors.navy-mid}"
    borderLeft: "1px solid {colors.border}"
    description: "Right compare panel — a slightly lighter navy with a hairline left-border, creating the two-shade panel pair."
  bar-fill-default:
    background: "{colors.yellow-3}"
    description: "Default chart bar fill — yellow at 32% opacity (the tier-3 muted color)."
  bar-fill-accent:
    background: "{colors.yellow}"
    description: "Highlighted chart bar — full yellow."
  chart-baseline:
    height: 1px
    background: "{colors.border}"
    description: "1px hairline baseline beneath chart bars."
  img-placeholder:
    background: "rgba(42,56,112,0.12)"
    border: "1px dashed {colors.border}"
    description: "Image slot — translucent navy fill with a dashed yellow-low-opacity border, centered mono label inside."
  quote-mark:
    typography: "{typography.quote-mark}"
    color: "{colors.teal}"
    description: "A 7vw italic Cormorant Garamond opening quote glyph in dusty teal, sitting centered above a centered pull-quote. The teal color is the system's only large-graphic accent."
---

## 概览

Vellum 是一套**单色墙上随笔**演示系统。视觉前提既严厉又温柔：每一页都是同一块深 periwinkle 海军蓝底（`{colors.navy}` — #2A3870），暖黄绿字（`{colors.yellow}` — #E8D85C）居中浮在上面。没有交替表面。没有浅/深主题。没有第二背景色。底是常量；字体，再加上左下角一条小注释，就是其余的一切。

排印前提是**斜体衬线即性格**。Cormorant Garamond 承担每一个字号的每一个标题——display 到 h3、quote-text、stat-value——斜体、字重 400。大字号斜体衬线对着大胆的 periwinkle 底，读作画廊墙文字：个人、经过考量、略带亲密。DM Sans 以安静配角承担正文和导语段落；正文应当退后，让斜体衬线标题带路。Courier Prime 等宽扮演最鲜明的角色：它承担「pin-note」——一小叠打字机式署名行，坐在每一页左下角。尘青 pin-note 看起来像钉在装裱随笔旁墙上的打字机标签；这就是系统的签名。

颜色哲学是**一块底，两种强调**。底是 `{colors.navy}`。文字主色是全不透明度的 `{colors.yellow}`，次级 62%，三级 32%。第一种强调是 `{colors.emphasis-yellow}`（#F5E168）——更亮的黄，只用于斜体标题里的 `<em>` 强调，以及小强调文字。第二种强调是 `{colors.teal}`（#3A7878）——低饱和尘青，只用于：大引号字形、pin-note 文字、kicker、28px 强调短线，以及列表计数标记。尘青是系统里唯一非黄的可见色，出现在精心限定的语境里。

纵深是**扁平而居中的**。没有投影。没有圆角。没有渐变。边框是黄 20% 不透明度的 1px 发丝线——几乎看不见，更多是淡结构痕迹而不是分隔。对比例版式是唯一例外：它用两种略有差别的海军蓝（`{colors.navy-deep}` 和 `{colors.navy-mid}`）做出可见的分栏，但即便如此差别也很克制。动画时长设为零——幻灯片不做过渡。系统设计上完全静止。

**密度哲学：稀疏而居中。** Vellum 幻灯片是钉在墙上的随笔——每页只承载少量内容，居中放在画布里，上下左右都有显著呼吸空间。陈述页是底上居中的一条短标题。封面是一个 kicker、一条展示标题、一句导语，加上角落里的 pin-note——仅此而已。列表页是居中 60% 宽栏里的四条编号规则。挤满时系统读起来像坏掉；内容周围的空海军蓝底是结构，不是负空间。它是墙。

**关键特征：**
- 单一单色底——`{colors.navy}`（深 periwinkle）——每一页都是。没有浅色主题，没有反转。
- 每一个标题、每一个数字、每一个衬线高光时刻都用斜体 Cormorant Garamond、字重 400。
- 正文和导语段落用 DM Sans；铬件标签和 pin-note 签名用 Courier Prime 等宽。
- 黄字（`{colors.yellow}`）是主色；更亮的 `{colors.emphasis-yellow}` 是标题里唯一的 `<em>` 色。
- 尘青（`{colors.teal}`）是第二种强调——只用于大引号字形、pin-note 文字、kicker、28px 短线，以及列表计数标记。
- pin-annotation（每一页左下角尘青 Courier Prime 等宽行）是系统的签名元素。
- 每一页内容居中——多数版式 `text-align: center`，内容占画布宽度的 55–80%。
- 铬件分隔用黄 20% 不透明度的 1px 发丝边框；除此之外无边框、无阴影、无抬升。
- 零动效——幻灯片过渡和入场动画时长都设为 0。系统设计为静止。
- 斜体是结构，不是装饰：展示字号的衬线斜体是系统身份，从不用正体罗马体做默认。

## 颜色

### 色板

- **Navy**（`{colors.navy}` — #2A3870）：深 periwinkle 底。每一页的单一表面。比 midnight 略暖，比 ultramarine 略冷——坐在沉思的蓝色语域里。
- **Navy Alt**（`{colors.navy-alt}` — #343F80）：略抬起的海军蓝，用于相邻表面区分。实际很少用。
- **Navy Deep**（`{colors.navy-deep}` — #1F2858）：更深的对比例面板色。只用于对比例版式左侧，做内部面板对比。
- **Navy Mid**（`{colors.navy-mid}` — #34407A）：更浅的对比例面板色。只用于对比例版式右侧。
- **Yellow**（`{colors.yellow}` — #E8D85C）：暖黄绿主文字色。暖，略偏绿——对着海军蓝底读作陈年羊皮纸或黄绿丝绸。
- **Yellow 2**（`{colors.yellow-2}` — rgba(232,216,92,0.62)）：次级文字——黄 62% 不透明度。用于导语段落和说明。
- **Yellow 3**（`{colors.yellow-3}` — rgba(232,216,92,0.32)）：三级文字——黄 32%。用于弱化图注、图表坐标标签、默认图表柱。
- **Emphasis Yellow**（`{colors.emphasis-yellow}` — #F5E168）：更亮的黄。只用于斜体标题里的 `<em>` 强调（此处 `<em>` 渲成这种更亮色的正体非斜体——见标志性处理），以及小强调文字标签。
- **Teal**（`{colors.teal}` — #3A7878）：低饱和尘青。系统的第二种强调。只用于：大引号字形、pin-note 文字、kicker 标签、28px 强调短线、列表计数标记，以及 bullet-list 标记。尘青是黄/海军蓝二元之外系统的颜色签名。
- **Border**（`{colors.border}` — rgba(232,216,92,0.20)）：发丝边框色——黄 20% 不透明度。用于铬件条、统计分隔、图片占位。

### 默认值

- **默认表面**：`{colors.navy}`——每一页。
- **默认主文字色**：`{colors.yellow}`。
- **默认次级文字色**：`{colors.yellow-2}`（黄 62% 不透明度）。
- **默认三级文字色**：`{colors.yellow-3}`（黄 32%）。
- **默认强调色（标题内）**：`{colors.emphasis-yellow}`——应用到 `display`、`h1`、`h2` 内的 `<em>` 标签（强调渲成这种更亮黄的正体非斜体，提供系统的 `<em>` 机制）。
- **默认 kicker / pin-note / 强调短线色**：`{colors.teal}`。
- **默认大图形强调色**：`{colors.teal}`——专用于引号字形。
- **默认边框**：`{colors.border}`——黄 20% 不透明度。仅发丝线。

颜色之间没有语义映射。尘青不是「警告」，黄不是「高亮」。黄只是字体；尘青是注释声线；emphasis-yellow 只是强调旗标。色板足够小，不需要语义角色。

## 字体

### 字族

Vellum 跑**三套字族**，角色仔细分开：

- **Cormorant Garamond**（`{typography.display.fontFamily}`）——老式衬线，斜体轴极富表现力。承担每一个标题（display 到 h3）、每一个数字（stat-value）、每一个衬线高光时刻、quote-text，以及引号字形。标题 token 指定 `fontStyle: italic`——斜体是默认呈现，不是强调变体。display/h1/h2/quote-text 字重 400（regular）；h3 字重 500。展示字号的斜体 Cormorant Garamond 对着 periwinkle 底，是系统的定义性视觉时刻。
- **DM Sans**（`{typography.body.fontFamily}`）——干净的人文 grotesque。承担正文、导语段落和列表正文。DM Sans 退到性格字体后面——它是实质，不是声线。
- **Courier Prime**（`{typography.label.fontFamily}`）——打字机风格等宽。承担每一个铬件标签、每一个幻灯片计数器、每一页左下角的 pin-note、列表计数标记，以及统计标签。等宽是「打字注释声线」——给系统带来档案/展览语域。

情绪划分：斜体衬线承担个人随笔声线（标题、引语）；无衬线承担支撑实质（正文）；等宽承担打字注释（pin-note、铬件）。斜体衬线 + 打字机等宽的混合不寻常，是系统最鲜明的排印组合。

### 字号阶梯

| Token | 尺寸 | 字族 | 字重 | 样式 | 用途 |
|---|---|---|---|---|---|
| `{typography.display}` | 11vw | Cormorant Garamond | 400 | 斜体 | 封面 hero，最大字号 |
| `{typography.h1}` | 7vw | Cormorant Garamond | 400 | 斜体 | 章节或陈述标题 |
| `{typography.quote-mark}` | 7vw | Cormorant Garamond | 400 | 斜体 | 装饰性开引号字形（尘青色） |
| `{typography.stat-value}` | 5.5vw | Cormorant Garamond | 400 | 斜体 | 大号斜体衬线统计数字 |
| `{typography.h2}` | 4vw | Cormorant Garamond | 400 | 斜体 | 幻灯片主标题 |
| `{typography.quote-text}` | 3.2vw | Cormorant Garamond | 400 | 斜体 | 引文正文 |
| `{typography.h3}` | 2.4vw | Cormorant Garamond | 500 | 斜体 | 副标题、对比例面板标题 |
| `{typography.lead}` | 1.5vw | DM Sans | 400 | 正体 | 导语段落、开场句 |
| `{typography.pin-note}` | 1.15vw | Courier Prime | 500 | 正体 | Pin-annotation 文字（尘青色），bar-val 强调 |
| `{typography.bar-val}` | 1.1vw | Courier Prime | 400 | 正体 | 图表柱数值标签 |
| `{typography.body}` | 1.05vw | DM Sans | 400 | 正体 | 默认正文段落 |
| `{typography.caption}` | 0.85vw | DM Sans | 400 | 正体 | 图注、次级文字 |
| `{typography.label}` | 0.72vw | Courier Prime | 400 | 正体 | 铬件标签、幻灯片计数、kicker、stat-label |

### 默认值

- **主章节标题默认尺寸**：`{typography.h2}`（4vw）。
- **章节或陈述标题默认尺寸**：`{typography.h1}`（7vw）。
- **封面 hero 默认尺寸**：`{typography.display}`（11vw）。
- **正文段落默认尺寸**：`{typography.body}`（1.05vw）。
- **导语句默认尺寸**：`{typography.lead}`（1.5vw）。
- **任何铬件标签、kicker 或等宽元数据默认尺寸**：`{typography.label}`（0.72vw）。
- **pin-note 默认尺寸**：`{typography.pin-note}`（1.15vw）。
- **数据数字默认尺寸**：`{typography.stat-value}`（5.5vw 斜体）。
- **默认标题字重**：400 斜体。
- **默认标题色**：`{colors.yellow}`。

拿不准尺寸时，偏大。Vellum 稀疏——标题常常就是这一页，所以应当大到能锚定周围的空底。

### 标志性处理

只要用到对应元素类型，这些处理就是**不可省略的**：

- **每一个标题都是斜体 Cormorant Garamond、字重 400**（h3 例外为字重 500，仍是斜体）。本系统不存在展示字号的正体（非斜体）衬线，除非作为 `<em>` 强调。
- **斜体标题（`display`、`h1`、`h2`）内的 `<em>` 标签渲成正体罗马 Cormorant Garamond，字重 600，颜色 `{colors.emphasis-yellow}`。** 这是系统的强调机制——斜体翻成正体，再加颜色切换，不可商量。它与常规「斜体表强调」相反；这里斜体是默认，正体才是强调。
- **每一页左下角都带 pin-annotation。** pin-annotation 是 `{colors.teal}` 的一叠 Courier Prime 等宽行——通常是幻灯片计数（例如 "03 / 09"）加 1–2 条短 pin note（标签、署名或短语）。pin-annotation 绝对定位在 `bottom: ~0.9 * pad-y`、`left: pad-x`，max-width 22vw。没有 pin-annotation 的幻灯片读成另一套系统。
- **pin-note 排印使用 Courier Prime 字重 500、颜色 `{colors.teal}`**，字距 0.01em。换成任何其他字体或颜色都会破坏注释语域。
- **Kicker 使用标签尺寸的 Courier Prime 等宽，颜色 `{colors.teal}`。** 无衬线 kicker、斜体 kicker 或黄色 kicker 会破坏 kicker 惯例。
- **大引号字形（7vw 斜体 Cormorant Garamond）渲成 `{colors.teal}`，不是黄。** 尘青引号是大尺度图形唯一上尘青色的地方；其他地方尘青只出现在小文字（标签尺寸）。
- **列表使用标签尺寸、`{colors.teal}` 的 Courier Prime 等宽编号计数**——从不用圆点，从不用破折号。编号惯例是系统的列表签名。
- **每一页版式内容居中**（text-align: center，flex 列 items 居中对齐）。左对齐标题会破坏画廊墙钉随笔语域。

### 排版原则

字族阶梯是固定的：斜体衬线（Cormorant Garamond italic）用于标题、数字、引语和任何性格时刻；无衬线（DM Sans）用于正文和导语；等宽（Courier Prime）用于铬件、pin-note、kicker 和列表计数。串轨（例如用斜体衬线写正文，或用无衬线写标题）会破坏画廊墙语域。

斜体是结构，不是强调。标题默认斜体；强调靠切到字重 600 的正体，颜色 `{colors.emphasis-yellow}`。这种倒置模式是系统最鲜明的排印动作。

行高在展示字号上收紧（display 0.92，h1 0.95），正文放到 1.5–1.65。展示字距略负（–0.01em）；正文和标签近中性。等宽标签带 0.06em 字距；pin-note 带 0.01em（比铬件标签更紧）。

正文内不用粗体。不用下划线。正文内的强调与标题内相同：罗马体 + emphasis-yellow——从斜体切到更重字重的正体，用更亮的黄。

## 布局

### 画布系统

Vellum 目标是 `100vw × 100vh`——铺满视口。每个 `.slide` 弹性填满视口，幻灯片并排成水平条带。所有尺寸使用视口相对单位（`vw`、`vh`），布局流体缩放。

### 内边距与间距层级

| Token | 值 | 用途 |
|---|---|---|
| `{spacing.pad-x}` | 6vw | 幻灯片水平内边距 |
| `{spacing.pad-y}` | 6vh | 幻灯片垂直内边距 |
| `{spacing.gap-lg}` | 5vh | 主要内容区块之间 |
| `{spacing.gap-md}` | 3vh | 相关元素之间 |
| `{spacing.gap-sm}` | 1.5vh | 紧密耦合元素之间 |

引语页使用 1.2× pad-y 和 1.4× pad-x，给居中引语额外呼吸空间。对比例版式把幻灯片内边距覆盖为 0，因为每个面板自带内部内边距。

### 铬件框架

标准幻灯片带铬件和脚条（黄 20% 不透明度的 1px 发丝线，配等宽标签）。无铬件版式包括封面、陈述、引语、结尾，以及任何内容应无结构框浮着的页——整套幻灯片的大多数。

系统的通用铬件元素是**左下角的 pin-annotation**，无论该页是否带铬件/脚条，每一页都有。pin-annotation 是系统的持续识别标记。

### 内容居中

每一种幻灯片版式都把内容居中。封面、陈述、引语、结尾使用 `align-items: center; justify-content: center` 加 `text-align: center`。列表、统计、图表使用 60–80% 宽的居中正文容器。对比例拆成两块等宽面板，每块面板内容垂直居中。

内容很少填满超过画布宽度的 70% 或高度的 60%。剩下的海军蓝底就是钉墙语境。

## 纵深与抬升

Vellum **完全扁平**。没有投影。没有圆角。没有渐变。完全没有抬升系统。

看起来像区分的东西来自：
- **海军蓝家族内的颜色推移**——对比例面板上的 `{colors.navy-deep}` 和 `{colors.navy-mid}` 做出克制的双色配对。
- **黄 20% 不透明度的发丝边框**——可见但安静的结构痕迹。
- **黄的不透明度档**——三档不透明度（全、62%、32%）提供足够文字色对比来建立层级，而不引入额外颜色。

系统故意静止。没有动效（幻灯片和入场动画时长都设为 0）。没有阴影抬升。幻灯片应像对开本里的一页那样读——一次一页，没有过渡。

## 形状与处理

### 圆角

| 值 | 用途 |
|---|---|
| 0 | 除导航点外的一切 |
| 50%（圆形） | 导航点（仅 deck-stage 铬件，不是幻灯片内容） |

Vellum **没有圆角铬件**。卡片、面板、统计砖、图片占位、对比例面板——全部是严格矩形。唯一的圆形是幻灯片导航点，属于 deck-stage UI 而不是幻灯片内容。

### 边框粗细

- **1px solid**，颜色 `{colors.border}`（黄 20% 不透明度）——通用发丝线。用于铬件条、脚条、统计分隔、图表基线、对比例面板左缘。
- **1px dashed**，颜色 `{colors.border}`——用于图片占位框（虚线边框标记「这是一个槽」）。
- **1px solid**，略高不透明度（rgba(232,216,92,0.18)）——用于对比例面板左/右分隔。

系统里没有更重的边框。每条线都是 1px。

### 装饰元素类型

**斜体展示标题**——Cormorant Garamond italic、字重 400、4–11vw，居中放在幻灯片上，颜色 `{colors.yellow}`。标题是每一张内容页的主导视觉元素。

**Pin-annotation**——1–3 行 Courier Prime 等宽，颜色 `{colors.teal}`，绝对定位在每一页左下角。行通常包括幻灯片计数（例如 "04 / 09"）、一条短打字标签，以及可选的第二条 pin 短语。行以 0.3vh 间距叠放，max-width 22vw。这是系统的签名。

**尘青引号字形**——7vw 斜体 Cormorant Garamond `"`，颜色 `{colors.teal}`，居中放在居中引文上方。系统里唯一的大尺度尘青元素。

**Kicker**——标签尺寸（0.72vw）的 Courier Prime 等宽，颜色 `{colors.teal}`，字距 0.1em。坐在标题上方。

**28px 强调短线**——28px × 1px 水平条，颜色 `{colors.teal}`。用作小 kicker 分隔或章节强调。

**编号列表**——使用 CSS `counter-reset: list-counter; counter-increment: list-counter`，以标签尺寸、`{colors.teal}` 的 Courier Prime 等宽渲染数字，数字占 2em 列，与正文（DM Sans lead）间隔 0.5em。

**Pin-stat**——居中列，上方是斜体衬线统计数字（5.5vw），下方是弱化黄的等宽图注。成行时，pin-stat 之间用黄 20% 不透明度的单条 1px 发丝线分隔；行末统计去掉边框。

**对比例面板对**——并排两块面板填满幻灯片。左面板：`{colors.navy-deep}` 背景。右面板：`{colors.navy-mid}` 背景加 1px 左边框。每块面板含 `{colors.yellow-2}` 的小等宽 compare-label、斜体 h3、斜体导语，以及编号列表。

**图片占位**——`{colors.border}` 的 1px 虚线矩形，淡海军蓝内部，居中 Courier Prime 等宽标签，最小高度 28vh。虚线边框是「槽」指示。

**图表柱**——扁平竖矩形，默认 `{colors.yellow-3}`，强调 `{colors.yellow}`。柱值用 Courier Prime 等宽渲染（`{typography.bar-val}`）。

## 该做与不该做

### 该做

- 每一页都填 `{colors.navy}`——单色底是常量。没有浅色交替。
- 每一个标题都用斜体 Cormorant Garamond、字重 400、颜色 `{colors.yellow}`。展示字号的斜体衬线就是系统身份。
- 每一页左下角放 pin-annotation——`{colors.teal}` 的 Courier Prime 等宽，1.15vw，max-width 22vw。pin-annotation 是系统的持续签名。
- 标题内的 `<em>` 用正体罗马（非斜体）、字重 600、颜色 `{colors.emphasis-yellow}`。这种斜体翻正体的强调模式不可商量。
- kicker、列表计数标记、28px 短线和大引号字形用 `{colors.teal}`。尘青是第二种强调，只出现在这些特定语境。
- 每一页内容居中。Text-align center，items 居中对齐。左对齐标题会破坏钉随笔语域。
- 铬件标签、幻灯片计数器、pin-note、列表计数标记和柱值用 Courier Prime 等宽。等宽是打字注释声线。
- 列表用 `{colors.teal}` 的 Courier Prime 等宽计数编号。本系统不存在圆点列表和破折号列表。
- 在每个内容块周围留下充裕的空海军蓝底。稀疏才是正确语域。
- 幻灯片内边距用 `{spacing.pad-x}` 6vw 和 `{spacing.pad-y}` 6vh，引语页加大到 1.2–1.4×。

### 不该做

- 不要引入第二背景色。海军蓝底是单一表面。即便对比例版式也用两种近乎相同的海军蓝，而不是对比背景。
- 不要用正体罗马渲染标题。展示字号斜体是默认；正体只作为 `<em>` 强调机制出现。
- 不要加投影、圆角或渐变。系统极度扁平。
- 不要给引号字形或 kicker 上黄色。那些时刻是尘青；换成黄会压扁尘青作为强调的角色。
- 不要用圆点或破折号。列表用尘青 Courier Prime 等宽计数编号。
- 不要给幻灯片加动效。整套刻意静止——幻灯片过渡和入场动画时长都是 0。
- 不要省略 pin-annotation。它在每一页上——无论有无铬件——拿掉它会破坏系统签名。
- 不要引入第三套字体。三套字族（Cormorant Garamond italic、DM Sans、Courier Prime）就是整栈。
- 不要用斜体衬线渲染小字。斜体只用于展示字号；正文和图注保持正体无衬线。
- 不要把幻灯片挤到边对边。空海军蓝底是结构性的——稀疏内容居中，上下留呼吸空间，才是语域。

## 响应式行为

Vellum 目标是 1920×1080 视口，全程使用视口相对单位（`vw`、`vh`），因此布局在 1280×720 到 2560×1440 之间流体缩放。没有媒体查询，除 deck-chrome 点和 pin-annotation 定位偏移外没有固定像素尺寸（偏移相对 pad，随幻灯片内边距缩放）。

### 缩放行为

- 展示标题缩放：11vw → 1920px 视口约 211px，1280px 约 141px。
- 正文缩放：1.05vw → 1920px 约 20px，1280px 约 13px。
- Pin-annotation 定位相对 `pad-y` 和 `pad-x`，因此随幻灯片内边距缩放。

### 演示行为

幻灯片由 JS 驱动，但过渡时长为零（系统刻意静止）。幻灯片并排，通过 deck-stage 的 translateX 导航，但用户感知为即时切页而不是动画过渡。没有入场动画系统——`[data-anim]` 属性没有对应关键帧，因为动画时长为 0。

导航点和幻灯片计数器固定在视口底部。

### 打印行为

没有内嵌打印样式表。静态导出依赖把 deck 容器拆开做顺序分页渲染。

## CJK 与国际内容

### 推荐中文搭配

| 角色 | 拉丁字体（默认） | 中文字体 | 字重 | 说明 |
|---|---|---|---|---|
| Display / h1 / h2 / quote-text / stat-value | Cormorant Garamond 斜体 400 | 霞鹜文楷 LXGW WenKai（LXGW WenKai TC） | 400 | LXGW WenKai 手写楷体的温度镜像 Cormorant 的斜体性格——CDN 上唯一带斜体式个人语域的 CJK 字体。 |
| h3 | Cormorant Garamond 斜体 500 | 霞鹜文楷 LXGW WenKai | 400 | 单字重楷体；从 h2 到 h3 的视觉台阶必须来自尺寸，不是字重。 |
| 引号字形（7vw，尘青） | Cormorant Garamond 斜体 400 | LXGW WenKai 400 或 NSC 里的 `「`/`『` | 400 | 中文引号把 `"` 换成 `「`（全角直角引号），用 LXGW WenKai 或 NSC，同一尘青色。 |
| Body / lead | DM Sans 400 | 思源宋体 / Noto Serif SC | 400 | 系统正文在 CJK 里从无衬线切到衬线，以保住文学语域——DM Sans 挨着楷体会在中文里读成教科书。 |
| Pin-note / kicker / chrome label / list counter | Courier Prime 400–500 | Courier Prime + Noto Sans Mono CJK SC fallback | 400–500 | Pin-note 通常是拉丁；若出现中文，回退到 Noto Sans Mono CJK SC。尘青色保留。 |

### 混排策略

本模板使用 **Strategy C（literary）**：拉丁字形保留拉丁字体，汉字出现时才通过堆叠 `font-family` 落入 CJK 回退。Cormorant Garamond italic 是 Vellum 的定义性品牌身份——每个标题都换成楷体会剥掉系统「斜体衬线对着 periwinkle」的时刻。让拉丁留在 Cormorant italic，中文落入 LXGW WenKai，两种语域都保住。

```css
font-family: 'Cormorant Garamond', 'LXGW WenKai TC', 'Noto Serif SC', Georgia, serif;  /* headlines */
font-family: 'DM Sans', 'Noto Serif SC', system-ui, sans-serif;                         /* body */
font-family: 'Courier Prime', 'Noto Sans Mono CJK SC', 'Courier New', monospace;        /* pin-note / chrome */
```

**警告——展示字号上的基线不匹配。** Cormorant Garamond italic 的光学中心低于 LXGW WenKai 的光学中心，尤其在 11vw display 和 7vw h1。像 `Vellum 羊皮纸` 这样的短语会让汉字相对斜体拉丁基线略微上浮。缓解办法：
- 在中文片段上加 `font-feature-settings: "palt"` 收紧度量。
- 把 CJK 包进 `<span lang="zh">`，在展示 token（display、h1、h2、quote-text、stat-value）上用 `vertical-align: -0.05em` 调整。斜体拉丁的倾斜让基线不匹配比正体配对更明显，所以偏移可能需要比非斜体系统略大。
- 纯 CJK 标题（无拉丁）时，问题完全消失。

### 加载

加到 `<head>`（Google Fonts 托管 LXGW WenKai TC、Noto Serif SC 和 Courier Prime）：

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=DM+Sans:wght@400;500&family=Courier+Prime:wght@400;700&family=LXGW+WenKai+TC&family=Noto+Serif+SC:wght@400;500;700&display=swap" rel="stylesheet">
```

LXGW WenKai TC 是 Google Fonts 上的繁体切片；它包含完整 CJK Unified Ideographs 范围，简体中文也能干净渲染。Noto Serif SC 用正确 hinting 承担简体中文正文。Cormorant 斜体轴对拉丁保持原样。

### 通用 CJK 调整

应用到任何渲染中文内容的元素（通常通过 `:lang(zh)` 或 `<span lang="zh">` 限定范围）：

- **行高**：正文 1.75–1.85（Vellum 默认的 1.65 DM Sans 行高接近，但 CJK 笔画需要再抬）；展示 1.15–1.25（比拉丁 0.92–1.05 更松，因为 7–11vw 的 CJK 字形需要垂直呼吸）。
- **字距**：CJK 上为 0。Vellum 在拉丁展示上的负字距（-0.01 到 -0.02em）对中文是错的——CJK 字形已预留间距；负字距会造成重叠。
- **文本变换**：CJK 不大写。Vellum 拉丁也不用大写（斜体衬线全程句首大写），所以这里只是确认没有父级规则试图做这件事。
- **全角标点**：用 `，。：；！？`（全角），不用 `,.:;!?`（半角）。中文引号把 `"…"` 换成 `「…」` 或 `『…』`（全角直角引号）——这是常规中文引号字形，并匹配系统的尘青引号处理。
- **展示标题不加句号**：中文标题去掉句末 `。`——标题的视觉收束已经足够。
- **盘古之白（Pangu spacing）**：在 CJK 与相邻拉丁/数字之间插入细空格。写 `使用 Claude` 而不是 `使用Claude`；写 `2024 年` 而不是 `2024年`。这是好中文排印的编辑惯例，也匹配 Vellum 考究的画廊墙语域。
- **一句一字体**：不要在同一行里混用 LXGW WenKai 和 Noto Serif SC。整段只用其中一套；句中切换会造成度量顿挫，在这套稀疏居中版式里尤其显眼。

### 本系统审美说明

LXGW WenKai 与 Vellum 的画廊随笔语域匹配极好。楷体的手写温度与 Cormorant Garamond italic 亲密的个人声线密切相关——两套字体都读作个人、经过考量、略带亲密。对着深 periwinkle 底、暖黄绿字，LXGW WenKai 在 7–11vw 展示上读作**画廊墙上的手写黄绿**——在中文里可以说比英文原版 Cormorant 处理更有诗意。楷体的笔画调制与黄的温度自然配对。

`<em>` 强调机制（斜体 → `{colors.emphasis-yellow}` 字重 600 的正体罗马）无法平移到 CJK，因为 LXGW WenKai 没有独立的斜体/正体对。CJK 等价强调是切到 **`{colors.emphasis-yellow}` 的 NSC 700**——更重字重 + 更亮颜色给出同样的「这就是此刻」信号。靠确保强调字重与楷体 regular 有明显差别，来保住正体非斜体的倒置逻辑。

pin-annotation（左下角尘青 Courier Prime 等宽）是系统签名，在混排幻灯片里无需修改即可工作。纯中文 pin-note 回退到 Noto Sans Mono CJK SC——等宽间距部分保住打字机质感，但打字机性格丢失。即使在中文幻灯片上也考虑把 pin-note 留在拉丁（日期、幻灯片计数、工作室名）；这在中文画廊展览设计里是惯例，读起来像刻意，而不是不完整。

编号列表惯例（尘青 Courier Prime 计数）直接平移——用 Courier Prime 的 `01.` `02.` `03.` 数字，而不是中文数字（`一、` `二、`），以保住打字注释语域。尘青色和 2em 列宽不变。

### 已知 CJK 缺口

- LXGW WenKai 只有单一字重（regular）。系统的 h3（字重 500 italic）无法在 CJK 里抬字重——视觉层级台阶必须只来自尺寸（h2 4vw → h3 2.4vw）。需要更强副标题强调的幻灯片，可考虑 NSC 500 作为 h3 替代。
- LXGW WenKai 没有斜体轴。Vellum 定义性的「斜体即默认」惯例无法在 CJK 里复现——正体楷体是最接近的类比，牺牲系统的斜体语域，换成另一种「手写温度」语域。这是 CJK 适配里最大的审美损失。
- 斜体翻正体的 `<em>` 强调机制在 CJK 里不存在。用 `{colors.emphasis-yellow}` 的 NSC 700 替代，给出等价的「强调旗标」效果。
- LXGW WenKai TC 的繁体切片字形可能把少量字渲成繁体形式（例如 設 而不是 设）。纯简体中文幻灯片优先用 `font-family: 'Noto Serif SC'` 作为主 CJK 字体，把 LXGW WenKai 留给强调时刻（封面标题、章节标题）。
- 尘青引号字形（`{colors.teal}` 上 7vw 的 `"`）在 CJK 惯例里不存在。用同一 7vw 尺寸、尘青色的 `「` 或 `『`（全角直角引号）——这是正确的中文等价，并保住系统的「尘青引号时刻」信号。
- 展示字号上的基线不匹配（见混排策略）在斜体拉丁 + 正体 CJK 配对里比正体-正体配对更明显。混排封面需要按套调校。

## 迭代指南

1. 任何新标题都用斜体 Cormorant Garamond、字重 400、颜色 `{colors.yellow}`。斜体是默认，不是强调。
2. 标题内任何被强调的短语切到字重 600 的正体罗马，颜色 `{colors.emphasis-yellow}`。斜体翻正体是系统的 `<em>` 机制。
3. 每一张新幻灯片都必须在左下角包含 pin-annotation。pin-annotation 含 1–3 行 `{colors.teal}` 的 Courier Prime 等宽：通常是幻灯片计数加一两条短打字短语。
4. 任何新 kicker、列表计数标记或 28px 强调短线都用 `{colors.teal}`。尘青是第二种强调，留给这些特定元素。
5. 任何新列表都用尘青 Courier Prime 等宽计数编号。本系统不存在圆点和短划列表。
6. 任何新版式都把内容居中。Text-align center，items 居中对齐。左对齐版式会破坏画廊语域。
7. 任何新背景都是系统断裂——只有一种表面色，`{colors.navy}`。对比例版式用轻微海军蓝变体，但不引入不同色相。
8. 任何新字体都禁止。Cormorant Garamond、DM Sans、Courier Prime 就是整栈。
9. 任何新图表、表格或数据展示都用黄 20% 不透明度的 1px 发丝线。没有更重边框，没有阴影，没有圆角铬件。
10. 内容密度应低而居中。如果一页觉得挤，删内容，而不是调内边距或缩小文字。

## 已知缺口

- 三套字族（Cormorant Garamond、DM Sans、Courier Prime）从 Google Fonts 加载。若字体失败，回退是 Georgia（斜体衬线）、system-ui（无衬线）和 Courier New（等宽）。没有 Cormorant italic 时系统会丢掉大量性格——Georgia italic 替代可接受，但比例不同。
- 中文回退（Noto Serif SC、Noto Sans SC）已接到栈里，但 Noto Serif SC 没有真正斜体——中文斜体标题会落到正体 Noto Serif SC，丢掉系统定义性的斜体时刻。
- `.light` 类为向后兼容而保留，但渲染与 `.dark` 相同（两者都用海军蓝底）。`.light` token 别名（`--c-bg-light`、`--c-fg-light`）指向深色 token。
- 动画时长设为 0——系统刻意静止。动画关键帧和 `[data-anim]` 基础设施存在于引擎中，但在 Vellum 里是空操作。重新启用动效需要改 token 块里的 `--dur-slide` 和 `--dur-enter`。
- pin-annotation 定位使用 `bottom: calc(var(--pad-y) * 0.9)`，刚好略在 pad-y 边界内侧；在很小的视口上 pin-note 可能靠近幻灯片边缘。
- 对比例面板使用两种近乎相同的海军蓝（`{colors.navy-deep}` 和 `{colors.navy-mid}`）——在低对比显示器或强环境光下，面板分界可能难以察觉。
- 尘青强调色（`{colors.teal}` — #3A7878）饱和度低，在某些显示器上可能读作弱化蓝而不是青。
- 系统没有浅色主题、没有反转、没有交替表面。需要「重置」页（用不同颜色背景打断长序列）的幻灯片，必须要么接受单色限制，要么走出设计系统。
