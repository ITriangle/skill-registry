---
version: alpha
name: Signal
description: A literary editorial presentation system in the spirit of a long-form magazine — The Economist's restraint crossed with a private intelligence briefing. Source Serif 4 carries every headline with roman/italic mixing mid-sentence in antique gold, DM Sans steps back for body, and IBM Plex Mono runs all the timestamps, kickers, and chrome. The dual surface system is warm cream paper (#F0ECE3) and deep editorial navy (#1C2644), connected by a single hot accent — antique gold (#C8A870) — used only on rules, italic emphasis, and numerical figures. A near-invisible 80px grid texture overlays every dark slide as a fingerprint. The effect is sober, considered, and a little bit aristocratic.

colors:
  navy: "#1C2644"
  navy-alt: "#232F55"
  cream: "#F0ECE3"
  cream-alt: "#E6E0D4"
  text-warm: "#E2DCD0"
  text-muted-dark: "#8A96A8"
  text-hint-dark: "#4E5A6E"
  ink: "#1A2030"
  text-muted-light: "#5A6270"
  text-hint-light: "#9AA0A8"
  gold: "#C8A870"
  border-dark: "#2E3D5C"
  border-light: "#CAC4B4"

color-aliases:
  c-bg: navy
  c-bg-alt: navy-alt
  c-bg-light: cream
  c-bg-light-alt: cream-alt
  c-fg: text-warm
  c-fg-2: text-muted-dark
  c-fg-3: text-hint-dark
  c-fg-light: ink
  c-fg-light-2: text-muted-light
  c-fg-light-3: text-hint-light
  c-accent: gold
  c-border: border-dark
  c-border-light: border-light

typography:
  display:
    fontFamily: "Source Serif 4, Noto Serif SC, Georgia, serif"
    fontSize: 9.5vw
    fontWeight: 700
    lineHeight: 0.96
    letterSpacing: -0.02em
  h1:
    fontFamily: "Source Serif 4, Noto Serif SC, Georgia, serif"
    fontSize: 5.2vw
    fontWeight: 600
    lineHeight: 1.08
    letterSpacing: -0.01em
  h2:
    fontFamily: "Source Serif 4, Noto Serif SC, Georgia, serif"
    fontSize: 3vw
    fontWeight: 600
    lineHeight: 1.18
  h3:
    fontFamily: "Source Serif 4, Noto Serif SC, Georgia, serif"
    fontSize: 1.9vw
    fontWeight: 500
    lineHeight: 1.3
  lead:
    fontFamily: "DM Sans, Noto Sans SC, system-ui, sans-serif"
    fontSize: 1.4vw
    fontWeight: 400
    lineHeight: 1.58
  body:
    fontFamily: "DM Sans, Noto Sans SC, system-ui, sans-serif"
    fontSize: 1.05vw
    fontWeight: 400
    lineHeight: 1.65
  caption:
    fontFamily: "DM Sans, Noto Sans SC, system-ui, sans-serif"
    fontSize: 0.82vw
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "IBM Plex Mono, JetBrains Mono, monospace"
    fontSize: 0.7vw
    fontWeight: 500
    letterSpacing: 0.14em
    textTransform: uppercase
  stat-value:
    fontFamily: "Source Serif 4, Noto Serif SC, Georgia, serif"
    fontSize: 5.5vw
    fontWeight: 600
    lineHeight: 1
    letterSpacing: -0.02em
  quote-text:
    fontFamily: "Source Serif 4, Noto Serif SC, Georgia, serif"
    fontSize: 3.6vw
    fontWeight: 400
    lineHeight: 1.28
    letterSpacing: -0.01em
  quote-mark:
    fontFamily: "Source Serif 4, Noto Serif SC, Georgia, serif"
    fontSize: 8vw
    fontWeight: 300
    lineHeight: 0.6
  editorial-headline:
    fontFamily: "Source Serif 4, Noto Serif SC, Georgia, serif"
    fontSize: 2.75vw
    fontWeight: 600
    lineHeight: 1.2
  dense-headline:
    fontFamily: "Source Serif 4, Noto Serif SC, Georgia, serif"
    fontSize: 2.4vw
    fontWeight: 600
    lineHeight: 1.2

spacing:
  pad-x: 7.5vw
  pad-y: 5.5vh
  gap-lg: 4vh
  gap-md: 2.5vh
  gap-sm: 1.2vh
  grid-cell: 80px

canvas:
  width: 100vw
  height: 100vh

components:
  rule-short:
    width: 36px
    height: 1px
    background: "{colors.gold}"
    description: "Short gold rule used as a kicker separator above headlines and as a chapter accent mark."
  rule-full:
    width: "100%"
    height: 1px
    background: "{colors.border-dark}"
    description: "Full-width hairline divider, color shifts to {colors.border-light} on cream surfaces."
  kicker:
    color: "{colors.gold}"
    typography: "{typography.label}"
    description: "Mono uppercase label in antique gold, sits above a headline."
  tag:
    border: "1px solid {colors.gold}"
    color: "{colors.gold}"
    padding: "0.3em 0.8em"
    typography: "{typography.label}"
    description: "Outlined gold pill containing a mono uppercase label."
  chrome-bar:
    borderBottom: "1px solid {colors.border-dark}"
    paddingBottom: "{spacing.gap-sm}"
    marginBottom: "{spacing.gap-md}"
    description: "Top chrome strip with mono label left, mono counter right, hairline rule beneath."
  foot-bar:
    borderTop: "1px solid {colors.border-dark}"
    paddingTop: "{spacing.gap-sm}"
    marginTop: "{spacing.gap-md}"
    description: "Bottom chrome strip, mirror of chrome-bar."
  stat-card:
    borderTop: "1px solid {colors.border-dark}"
    padding: "{spacing.gap-md} {spacing.gap-md} {spacing.gap-md} 0"
    description: "Stat tile with a top hairline rule, big gold serif numeral above a sans label and mono note."
  bullet-marker:
    content: "—"
    color: "{colors.gold}"
    fontFamily: "{typography.label.fontFamily}"
    description: "Em-dash bullet rendered in mono gold prefixes every list item."
  vt-spine:
    width: 1px
    background: "{colors.border-dark}"
    description: "Vertical hairline spine for timeline column, with a 9px gold dot marking each entry."
  vt-dot:
    width: 9px
    height: 9px
    borderRadius: 50%
    background: "{colors.gold}"
    description: "Gold node sitting on the timeline spine at each date."
  pie-donut:
    borderRadius: 50%
    innerCutout: "22% inset, painted to match slide background"
    description: "SVG/CSS donut chart, segments in palette colors with a 1px gold ring divider where used."
  bar-fill-default:
    background: "{colors.text-hint-dark}"
    description: "Default bar fill in muted slate; switches to gold for the highlighted bar."
  bar-fill-accent:
    background: "{colors.gold}"
  compare-divider:
    borderRight: "1px solid {colors.border-dark}"
    description: "Single vertical hairline separating two comparison panels."
  pyramid-band:
    borderLeft: "3px solid {colors.gold}"
    padding: "1.3vh 2.5vw"
    fillFunction: "color-mix(in srgb, {colors.gold} N%, {colors.navy})"
    description: "Horizontal band in pyramid layouts; opacity of gold mix decreases from top tier to bottom."
  grid-texture:
    background: "linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px)"
    backgroundSize: "80px 80px"
    description: "Near-invisible 80px grid overlay applied to every dark slide via ::before pseudo-element."
  cycle-step:
    borderTop: "2px solid {colors.gold}"
    padding: "{spacing.gap-md}"
    description: "Cycle/process step card with a 2px gold rule at top, gold numeral, serif title, sans body."
---

## 概述

Signal 是一套**文学编辑风**演示系统——长篇情报简报或严肃杂志季评如果做成幻灯片，就会是这副样子。视觉前提是两套字体的联姻：苏格兰烘焙感的编辑衬线（Source Serif 4）承担声线，精密 grotesk（DM Sans）承担实质，再加一套紧缩等宽（IBM Plex Mono）承担每一个时间戳、kicker 和铬件元数据。结果读起来像安静的权威——幻灯片不必喊，因为排印已经在发「认真」的电报。

系统跑在**双表面**模型上。深色表面是 `{colors.navy}`（#1C2644）——偏暖于海军蓝、偏冷于午夜的深编辑蓝。浅色表面是 `{colors.cream}`（#F0ECE3）——温暖的陈年纸调，从不是纯白。两套表面以相同字号阶梯承载同一套排印词汇；变的是前景色。深色表面上，主文本是 `{colors.text-warm}`（偏暖的灰白，从不是纯白）。奶油表面上，主文本是 `{colors.ink}`（带海军蓝偏向的近黑）。两套表面可以页与页互换——相邻页可以交替，无需解释，奶油表面在一段较长的深色运行里充当「重置」。

强调色恰好一种：**antique gold**（`{colors.gold}` — #C8A870）。金色只出现在三种语境：把 kicker 与标题分开的短线；混进正体衬线标题的 `<em>` 标签（「Signal 时刻」）；以及任何数字。金色从不承载正文段落，也从不填充背景。它是精密工具，用得克制，所以一旦出现就有分量。

纵深是**扁平加发丝线**。没有投影，没有圆角卡片铬件，没有抬升系统。区域靠 `{colors.border-dark}`（奶油面上则是 `{colors.border-light}`）的 1px 发丝线分开。系统里唯一的「纹理」是深色页上近乎看不见的 80px 网格叠层，白色 3% 透明度——只有刻意去看的眼睛才看得见。它是系统的指纹。

**密度哲学：中低且不对称。** Signal 是编辑系统；它要呼吸。典型一页只用一小部分面积——一个 kicker、一条标题、一句话、一条页脚。封面和章节页最疏（一条展示标题对着大片奶油或海军蓝）。密集编辑版式是例外而不是规则，即便那些也留着宽裕的内边距。在 Signal 里感觉坏掉的页，是把画布从边到边填满内容；正确音域是「我有一件事要说，我会小心地说」。

**关键特征：**
- Source Serif 4 承担每一个标题，句中混用正体 / 斜体；标题里的斜体永远是金色。
- 正文用 DM Sans；每一个时间戳、kicker、标签和铬件元素用 IBM Plex Mono。
- 双表面——`{colors.navy}`（深）和 `{colors.cream}`（浅）——可互换使用，除特殊对剖版式外从不在同一页混合。
- Antique gold（`{colors.gold}`）是唯一强调色。它标记线条、斜体强调和数字，别处不出现。
- `{colors.border-dark}` / `{colors.border-light}` 的 1px 发丝边框分隔每一个区域。没有卡片铬件，没有圆角面板。
- 近乎看不见的 80px 网格纹理叠在每一张深色页上，作为几乎感知不到的指纹。
- 金色等宽的破折号项目标记替换标准列表圆点。
- 每一张标准页顶部的等宽全大写铬件携带章节标签和页码计数。
- 无投影、无渐变（全出血图片页自下而上的 scrim 除外）、无圆角（环形图除外）。

## 色彩

### 色板

- **Navy**（`{colors.navy}` — #1C2644）：深色表面。深编辑蓝，暖于午夜，冷于靛蓝。「情报」色——权威而不攻击。
- **Navy Alt**（`{colors.navy-alt}` — #232F55）：略抬起的海军蓝，留给次级深色表面（占位面板、图片回退）。视觉上几乎与 navy 相同；只在紧挨着时才有差别。
- **Cream**（`{colors.cream}` — #F0ECE3）：浅色表面。温暖的陈年纸调，从不是中性，也从不是明亮。读作「宽报」或「手稿」，不是「屏幕白」。
- **Cream Alt**（`{colors.cream-alt}` — #E6E0D4）：略冷一点的奶油，用于次级浅色表面。角色与 navy alt 相同，只是在浅色一侧。
- **Text Warm**（`{colors.text-warm}` — #E2DCD0）：偏暖灰白。海军蓝表面上的主文本色。从不用 `#FFFFFF`——纯白会与系统的暖纸逻辑冲突。
- **Text Muted Dark**（`{colors.text-muted-dark}` — #8A96A8）：闷青灰。海军蓝上的次级文本——描述、想要退后的导语段落。
- **Text Hint Dark**（`{colors.text-hint-dark}` — #4E5A6E）：海军蓝上的第三档文本。用于统计注释、等宽图注，以及应可读但安静的元素。
- **Ink**（`{colors.ink}` — #1A2030）：带海军蓝偏向的近黑。奶油上的主文本。拾取深色表面色，而不是与它对抗。
- **Text Muted Light**（`{colors.text-muted-light}` — #5A6270）：奶油上的次级文本。
- **Text Hint Light**（`{colors.text-hint-light}` — #9AA0A8）：奶油上的第三档文本。
- **Gold**（`{colors.gold}` — #C8A870）：Antique gold。系统的单一强调色。出现在线条、标题内斜体强调、统计数字、kicker 标签和项目标记上。从不用作填充，从不用在正文上。
- **Border Dark**（`{colors.border-dark}` — #2E3D5C）：海军蓝表面上的发丝分隔。看得见但安静。
- **Border Light**（`{colors.border-light}` — #CAC4B4）：奶油表面上的发丝分隔。偏暖灰褐。

### 默认值

- **默认表面**：整套在 `{colors.navy}`（深）和 `{colors.cream}`（浅）之间交替。没有「主」表面——两者都是一等公民。拿不准时，章节开场和陈述页用海军蓝，密集编辑阅读用奶油。
- **海军蓝上的默认主文本**：`{colors.text-warm}`。
- **奶油上的默认主文本**：`{colors.ink}`。
- **海军蓝上的默认次级文本**：`{colors.text-muted-dark}`。
- **奶油上的默认次级文本**：`{colors.text-muted-light}`。
- **默认第三档 / hint 文本**：海军蓝上 `{colors.text-hint-dark}`，奶油上 `{colors.text-hint-light}`——用于等宽图注、统计注释、脚注。
- **默认强调**：`{colors.gold}`——应用到线条、标题内斜体强调、统计数字、kicker 标签。
- **默认边框**：海军蓝上 `{colors.border-dark}`，奶油上 `{colors.border-light}`。
- **默认 kicker 色**：`{colors.gold}`。

两套表面可互换，并携带同一金色强调——海军蓝上的金线与奶油上的金线读起来相同。正文从不以金色出现。金色从不充当区域填充。

## 字体排印

### 字体家族

Signal 以小心分开的角色运行四套字体家族：

- **Source Serif 4**（`{typography.display.fontFamily}`）——苏格兰烘焙感的编辑衬线。以每一种尺度承担每一个标题（display、h1、h2、h3、editorial-headline、dense-headline、quote-text、stat-value）。这套字有完整斜体轴，系统最鲜明的排印动作是**句中混用正体与斜体**：正体承担句子，内部一个 `<em>` 标签切到 `{colors.gold}` 的斜体。这就是「Signal 时刻」。
- **DM Sans**（`{typography.body.fontFamily}`）——人文主义 grotesk，用于正文、导语段落、项目符号项和统计标签。DM Sans 是结构替补——它从不领衔，永远支撑。当 `<em>` 出现在无衬线 `.lead` 段落里，强调切到**金色斜体衬线**（换 font-family），而不是斜体无衬线。
- **IBM Plex Mono**（`{typography.label.fontFamily}`）——紧缩编辑等宽。承担每一个标签、每一个 kicker、每一个铬件元素（顶栏、页脚、页码）、每一个章节号、每一个等宽图注、每一个统计注释、每一个时间线日期。等宽是系统的「元数据声线」。
- **Noto Serif SC / Noto Sans SC** —— 衬线与无衬线角色的中文回退。接到每一条 font-family 栈里，让系统用中文内容时渲染相同。

情绪对比是：衬线 = 声线，无衬线 = 实质，等宽 = 时间戳。在一句话里混用它们（无衬线导语内部嵌金色斜体衬线 `<em>`）是系统的小编舞。

### 字号阶梯

| Token | 字号 | 字体 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.display}` | 9.5vw | Source Serif 4 | 700 | 最大尺度的封面 hero 标题 |
| `{typography.h1}` | 5.2vw | Source Serif 4 | 600 | 章节标题或单句陈述标题 |
| `{typography.stat-value}` | 5.5vw | Source Serif 4 | 600 | 金色大号统计数字 |
| `{typography.quote-mark}` | 8vw | Source Serif 4 | 300 | 金色装饰开引号字形 |
| `{typography.quote-text}` | 3.6vw | Source Serif 4 | 400 | 抽引正文 |
| `{typography.h2}` | 3vw | Source Serif 4 | 600 | 主幻灯片标题 |
| `{typography.editorial-headline}` | 2.75vw | Source Serif 4 | 600 | 编辑 / 通讯版式的标题 |
| `{typography.dense-headline}` | 2.4vw | Source Serif 4 | 600 | 双列密文版式的标题 |
| `{typography.h3}` | 1.9vw | Source Serif 4 | 500 | 副标题、面板标题、区域内标题 |
| `{typography.lead}` | 1.4vw | DM Sans | 400 | 导语段落、引入句、列表项正文 |
| `{typography.body}` | 1.05vw | DM Sans | 400 | 段落正文、项目符号正文 |
| `{typography.caption}` | 0.82vw | DM Sans | 400 | 图注、脚注、来源署名 |
| `{typography.label}` | 0.7vw | IBM Plex Mono | 500 | 等宽全大写铬件标签、kicker、tag、等宽元数据 |

### 默认值

- **主章节标题的默认字号**：`{typography.h2}`（3vw）。
- **章节开场的默认字号**：`{typography.h1}`（5.2vw）。
- **封面 hero 的默认字号**：`{typography.display}`（9.5vw）。
- **段落的默认字号**：`{typography.body}`（1.05vw）。
- **标题下导语句的默认字号**：`{typography.lead}`（1.4vw）。
- **任何铬件、kicker 或元数据标签的默认字号**：`{typography.label}`（0.7vw）。
- **统计数字的默认字号**：`{typography.stat-value}`（5.5vw），用 `{colors.gold}`。
- **默认标题色**：该表面的主文本色（海军蓝上 `{colors.text-warm}`，奶油上 `{colors.ink}`）。从不是金色。

拿不准主时刻该用 `{typography.h2}` 还是 `{typography.h3}` 时，用 `{typography.h2}`——`h3` 用于区域内副标题，不是该页的主陈述。

### 签名处理

这些处理在**使用对应元素类型时不可省略**：

- **任何衬线标题（`display`、`h1`、`h2`、`h3`、`editorial-headline`、`dense-headline`）内的 `<em>` 标签必须以斜体 Source Serif 4、`{colors.gold}` 渲染。** 这是系统最鲜明的排印时刻——句中混用正体与斜体并换色。带强调短语却没有这套处理的标题，读起来像另一套设计系统。
- **无衬线 `.lead` 或正文段落内的 `<em>` 标签必须把 font-family 切到 Source Serif 4、斜体、`{colors.gold}`。** 正文里的强调从不留在 DM Sans 斜体——换字体才是强调。
- **每一个 kicker 都是 `{colors.gold}` 的等宽全大写，字距至少 0.14em。** 无衬线、小写或不是金色的 kicker 就不是 kicker。
- **每一个统计数字都是 Source Serif 4 600、`{colors.gold}`、字距 -0.02em。** 无衬线的统计，或主文本色的统计，会破坏系统。
- **每一条铬件栏下方都带 `{colors.border-dark}` / `{colors.border-light}` 的 1px 发丝线。** 发丝线让铬件读作铬件，而不是漂浮文字。
- **每一张章节页在章节号与章节标题之间带 36px 金线。** 这条线就是章节分隔——没有线，就没有章节。
- **项目列表用金色等宽破折号作标记。** 本系统不存在标准圆点项目符号。

### 排印原则

字体阶梯是固定的：衬线管声线（display 到 h3），无衬线管实质（lead 到 caption），等宽管元数据（仅 label）。从不用衬线做正文，从不用无衬线做标题，从不用等宽超出元数据角色。越过这些轨道会破坏编辑分离。

斜体是结构，不是装饰——它是标题内和导语段落内的强调载体。不存在下划线。正文内不存在加粗；正文需要强调时，切到斜体衬线金色 `<em>` 模式。

行高在展示尺度紧（display 0.96，h1 1.08），随字号减小而打开（caption 和 body 1.5–1.72）。展示和 h1 的字距为负（–0.01 到 –0.02em），正文为零。等宽标签带 0.14em 到 0.22em tracking——宽字距是等宽读作编辑而不是代码的方式。

## 版式

### 画布系统

系统目标是 `100vw × 100vh`——满视口。每个 `.slide` flex 精确铺满视口，幻灯片并排坐在一条水平带上，导航时左右平移。所有尺寸用视口相对单位（`vw`、`vh`），版式随窗口缩放——除铬件圆点 / 计数尺寸外，没有固定像素度量。

### 内边距与间距阶梯

| Token | 值 | 用途 |
|---|---|---|
| `{spacing.pad-x}` | 7.5vw | 幻灯片水平内边距 |
| `{spacing.pad-y}` | 5.5vh | 幻灯片垂直内边距 |
| `{spacing.gap-lg}` | 4vh | 主要内容区块之间 |
| `{spacing.gap-md}` | 2.5vh | 相关元素之间 |
| `{spacing.gap-sm}` | 1.2vh | 紧耦合元素之间 |

引语页把 pad-x 提到 1.1×、pad-y 提到 1.2×，给抽引额外呼吸空间。对比版式用 `pad-x * 0.55` 作为每个面板的内缩内边距。

### 铬件框架

标准页带顶栏铬件和底栏脚条——都是 flex 行，左侧等宽标签、右侧等宽计数，用 1px 发丝线与正文分开。封面、章节、陈述、引语和结束页上铬件和脚条消失——那些版式无铬件，让字体从边到边呼吸。

每一页是 CSS grid，`grid-template-rows: auto 1fr auto`——铬件和脚条是 auto 行，正文是填满的 1fr 行。

### 网格纹理

每一张深色页带近乎看不见的 80px × 80px 网格叠层，用两道 linear-gradient 背景、白色 3% 透明度画出。网格是系统的视觉指纹——本意不是被有意识感知，只被感觉成「这一页有结构」。奶油页不带这层叠层。

## 纵深与层次

Signal **设计上就是扁平的**。没有投影。没有圆角卡片抬升。完全没有抬升系统——每个元素都与表面齐平。

看起来像纵深的其实是**发丝线分离**。区域靠 `{colors.border-dark}`（海军蓝上）或 `{colors.border-light}`（奶油上）的 1px 实线边框分开。统计瓷砖、铬件栏、编辑栏——全靠发丝线分开，不靠阴影或背景。

唯一例外是**全出血渐变 scrim**：全出血图片页上，一道从透明到 `rgba(15, 20, 36, 0.9)` 的线性渐变自下而上铺过页的下半，让底下的字对着图片仍可读。这是系统里唯一的渐变；别处表面都是实色。

## 形状与处理

### 圆角

| 值 | 用途 |
|---|---|
| 0 | 系统里除环形图和环形中心井之外的每一种形状 |
| 50%（圆） | 环形图形状、9px 时间线圆点、色板 2px 圆端描边 |
| 2px | 饼图图例色块（仅轻微软化） |

Signal 实际上**没有圆角铬件**。统计瓷砖、铬件栏、对比面板、图片框——全是尖角矩形。

### 边框粗细

- **1px solid** —— 通用发丝边框。用于每一条铬件栏、每一块统计瓷砖顶线、每一道栏分隔、每一道对比面板分隔、每一道编辑栏边界。颜色跟随表面（`{colors.border-dark}` 或 `{colors.border-light}`）。
- **1px dashed** —— 仅用于图表绘图区内部的网格线（rgba 透明，透明度很低）。
- **2px solid `{colors.gold}`** —— 用于循环 / 流程步骤的顶线。
- **3px solid `{colors.gold}`** —— 用作金字塔条带的左边框。

### 装饰元素类型

**短金线** —— 36px × 1px 实心金色水平条。坐在 kicker 与标题之间，或作为章节强调标记。系统里最小的原子装饰元素。

**全宽发丝线** —— `{colors.border-dark}` / `{colors.border-light}` 的 100% × 1px 水平线。用作区块分隔、铬件分隔、统计瓷砖顶边、栏边界。

**描边金色 tag** —— 小型 inline-block，1px 金色边框围着等宽全大写金色文字。kicker 的「胶囊」版——同一套排印规格，外加描边。

**编辑栏分隔** —— 编辑版式里两栏之间从地板到天花板的 1px 发丝线。栏内内边距是 `pad-x * 0.38`。

**竖向时间线脊柱** —— 竖向时间线高度上的 1px 竖向发丝线，沿脊柱在每一条目处置 9px 圆形金色圆点。

**金字塔条带** —— 带 3px 实心金色左边框的水平条带，填充 `color-mix(in srgb, gold N%, navy)`，N 从顶层 70% 降到底层 8%。每一层也逐步更宽（38% → 100%）。这通过饱和度与宽度做出视觉金字塔，没有任何真正的三角形几何。

**环形中心井** —— 饼环内 22% inset 用幻灯片背景色（海军蓝或奶油）填充，做出环心。

**连接箭头** —— 在循环和 diagram 版式里，低对比箭头字形用 `{colors.border-dark}`（或 `{colors.border-light}`）坐在顺序步骤之间。箭头刻意闷掉——步骤领衔，连接退后。

**等宽破折号项目符号** —— 每一个列表项带金色等宽破折号（`—`）作项目标记，标记占 1.2em 列，间隙 0.5em。

## 宜与忌

### 宜

- 在同一条标题里混用正体与斜体 Source Serif 4，斜体用 `{colors.gold}`——这就是 Signal 时刻，系统依赖它贯穿整套出现。
- 每一个 kicker、标签、tag、铬件元素、页码、章节号和统计注释都用 IBM Plex Mono。等宽是元数据声线。
- 把每一个 kicker 渲染成等宽全大写金色，字距至少 0.14em——tracking 才让等宽读作编辑。
- 让每一条铬件栏下方带该表面对应边框色的 1px 发丝线。发丝线不可商量；没有线的铬件读作漂浮文字。
- 在一套里自由交替海军蓝与奶油表面。哪一个都不是「那个」背景——两者都是一等公民。
- 用 Source Serif 4 600、字距 -0.02em，把每一个统计数字上成 `{colors.gold}`。统计是斜体金色标题强调之后第二可识别的元素。
- 用金色等宽破折号替换标准项目圆点。标准圆点会破坏编辑音域。
- 用 36px 金线作章节分隔和 kicker 分隔。它是系统的小标点。
- 经 `::before` 把 80px 网格纹理叠层应用到每一张深色页。它是系统的指纹，永远不该去掉。
- 用 `{spacing.pad-x}` 7.5vw / `{spacing.pad-y}` 5.5vh 做内边距——Signal 需要呼吸空间；紧内边距会破坏编辑克制。

### 忌

- 不要把金色用在正文上，也不要用金色填背景。金色只出现在线条、斜体强调和数字上。
- 不要用纯白（`#FFFFFF`）在海军蓝上做文字。永远用 `{colors.text-warm}`——偏暖灰白才把系统钉在纸面音域上。
- 不要加投影或圆角卡片铬件。系统是扁平加发丝线；抬升会破坏编辑框架。
- 不要把衬线用在正文或段落文字上。衬线 / 无衬线分离是结构的——衬线领衔，无衬线支撑。
- 不要在正文里加粗做强调。改用斜体衬线金色 `<em>` 模式——换字体才是强调。
- 不要给铬件、面板、统计瓷砖或图片框圆角。系统里仅有的圆形状是环形图和 9px 时间线圆点。
- 不要引入第二种强调色。Antique gold 是唯一热色；加第二种强调会稀释它的分量。
- 不要用内容填满典型一页的一半以上。挤满时系统读作坏掉——克制才是音域。
- 不要把等宽用在元数据角色之外（标签、kicker、铬件、计数、图注注释）。正文或标题里的等宽会破坏排印阶梯。
- 不要省略铬件下方或统计瓷砖上方的 1px 发丝线。发丝线是系统的纵深替代；没有它们元素就会漂。

## 响应式行为

Signal 以 1920×1080 视口为目标，但完全用视口相对单位（`vw`、`vh`）实现，所以在 1280×720 到 2560×1440 之间无断点流体缩放。80px 网格纹理是唯一跨视口变化仍保持的固定像素度量——在更大视口上会按比例更细。

### 缩放行为

- 展示标题随视口缩放：1920px 时，9.5vw 渲染约 ~182px。1280px 时约 ~122px。
- 正文缩放：1.05vw → 1920px 时约 ~20px，1280px 时约 ~13px。
- 内边距缩放：pad-x 7.5vw → 1920px 时约 ~144px，1280px 时约 ~96px。

### 演示操作

整套由 JS 驱动。幻灯片经导航带前进（deck 容器上的 translateX），导航圆点和页码固定在底部。当前页带 `is-active`；带 `[data-anim]` 属性的元素经 fade-up、fade-in、reveal-right、reveal-left 或 scale-in 关键帧入场，错开 `data-delay`（0–6）。动画短（0.5–0.85s），用锐利的 `cubic-bezier(0.77, 0, 0.175, 1)` 滑动缓动和带弹性的 `cubic-bezier(0.16, 1, 0.3, 1)` 入场缓动。

### 打印行为

没有专用打印样式表。静态导出应把每一页渲染成顺序页面；为了打印保真，需要把 deck 容器的水平版式拆开。

## 中日韩与多语言内容

### 推荐中文搭配

| 角色 | 西文 | 中文 | 字重映射 |
|---|---|---|---|
| Display / Headlines (h1, h2, h3) / Stat-value / Quote-text / Editorial-headline / Dense-headline | Source Serif 4 (500–700) | **思源黑体 Noto Sans SC** | 700 |
| Lead / Body / Caption | DM Sans (400) | **思源黑体 Noto Sans SC** | 400 |
| Label / Kicker / Chrome / Slide counter | IBM Plex Mono (500) | **思源黑体 Noto Sans SC** | 500（去掉 uppercase + tracking） |

### 中西混排策略

**策略 A——全角色单一中日韩家族（思源黑体 Noto Sans SC）。** Signal 的西文系统已经把 Noto Serif SC 和 Noto Sans SC 接到每一条 font-family 栈作回退——系统设计时就考虑了中日韩。推荐的收拢是**每个角色都用 Noto Sans SC**，而不是混用 Noto Serif SC（展示）+ Noto Sans SC（正文）——原因是系统最鲜明的处理：标题内金色斜体 `<em>` 强调。Noto Serif SC 不提供斜体轴，意味着 Signal 时刻（句中正体到斜体的换色）无法在中文里复现。把整个系统收拢到 Noto Sans SC，并把中日韩 `<em>` 留给仅换色的强调（金色、不斜体），比硬扛一套没有斜体的衬线更干净。定义西文阶梯的衬线 vs 无衬线对比在中日韩里会丢掉，但系统的编辑克制——发丝线、等宽 kicker、antique gold 强调、双表面——不受影响地带过去。

### 加载

系统已经经现有 font-family 栈加载 Noto Sans SC。若使用 CDN preconnect 模式：

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&display=swap" rel="stylesheet">
```

现有 CSS 变量已经在每一条字体栈里包含 Noto Sans SC 和 Noto Serif SC。对以中日韩为主的套件，把衬线栈换成以 Noto Sans SC 为活动中日韩面（而不是 Noto Serif SC），让整个系统收拢到一套中文字体：
```css
/* Display / headline roles (CJK-primary) */
font-family: 'Source Serif 4', 'Noto Sans SC', Georgia, serif;
/* Body roles */
font-family: 'DM Sans', 'Noto Sans SC', system-ui, sans-serif;
/* Mono roles */
font-family: 'IBM Plex Mono', 'Noto Sans SC', monospace;
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

- **Signal 时刻（句中斜体金色 `<em>`）在中日韩上变成仅换色。** Noto Sans SC 没有斜体变体；即便 Noto Serif SC 也不带斜体。对中文标题，把 `<em>` 渲染成切到 `{colors.gold}` *而不*斜体——强调仍然成立，因为金色是系统负载最重的颜色。把这当作 Signal 时刻在中日韩里刻意翻译成仅换色的本质。
- **展示上的负字距（display -0.02em，h1/h2 -0.01em）在中日韩上必须降到 0。** 系统的紧 tracking 是西文展示惯例，会破坏中日韩渲染。
- **IBM Plex Mono 全大写、0.14–0.22em tracking 的等宽 kicker 仅限西文。** 对中日韩 kicker，把 tracking 降到 0，靠金色 + 小字号信号「这是 kicker」。中日韩 + 西文混合 kicker（`第一章 / CHAPTER ONE`）可以让西文一半保留 tracking、中日韩一半 tracking 为 0——不对称的等宽声线读作编辑双语。
- **Source Serif 4 600 金色的统计数字**保持西文数字（现代编辑设计里统计用阿拉伯数字是通用惯例）。不要换成中文数字（一二三四）——它们会丢掉目录-统计声线。
- **破折号项目符号（金色等宽的 `—`）翻译得完美**——破折号项目符号在中文排印里同样地道。
- **80px 网格纹理、发丝边框、双表面（海军蓝 + 奶油）、金线、章节页、全出血图片 scrim、无铬件陈述版式** 都与字形无关。编辑克制和情报简报音域不受影响地带过去。
- **中日韩正文行高应从 1.58–1.72 开到 1.75–1.85**——汉字填满 em-box，在系统正文字号（1.05vw、1.4vw）上需要额外纵向呼吸才可读。
- **引号字形（8vw 装饰开引号）应换成中文开引号（「）或弯引号（"）**——西文开引号字形在中文抽引上读作异物。

### 已知中日韩缺口

系统最鲜明的排印处理（Source Serif 4 标题里正体 + 斜体金色句中混排）本质上是西文排印动作，翻译不过去。Noto Serif SC 和 Noto Sans SC 都不提供斜体轴，用 CSS `font-style: italic` 发明一套会产出斜切 / 倾斜字形，读作坏掉而不是强调。把中日韩 `<em>` 收拢到仅换色（金色、不斜体）是最干净的变通；强调短语是西文（因此可以吃斜体金色）、周围句子是中文的混排标题，会落成 Signal 时刻最强的中日韩执行。

## 迭代指南

1. 任何新标题都用 Source Serif 4，并且有资格在句中用斜体金色 `<em>`。如果标题没有强调短语，考虑它应不应该有——Signal 声线依赖金色斜体时刻出现。
2. 任何新区域分隔都是 `{colors.border-dark}` / `{colors.border-light}` 的 1px 发丝线。从不是更粗的边框，从不是彩色边框，从不是阴影。
3. 任何新标签、kicker 或铬件元素都是 `{colors.gold}` 的等宽全大写（kicker）或该表面对应的闷色（铬件）。字距至少 0.14em。
4. 任何新统计数字都用 Source Serif 4 600、`{colors.gold}`、字距 -0.02em。无论表面，统计永远是金色衬线。
5. 任何新强调处理都用 `{colors.gold}`——没有第二种强调。如果一页需要更多视觉区分，变表面（海军蓝 vs. 奶油），而不是加颜色。
6. 任何新项目列表都用金色等宽破折号标记。加另一种项目符号风格会破坏系统。
7. 封面、章节、陈述、引语和结束版式无铬件。标准版式带铬件和脚条。不要混——无铬件陈述是正确的；带铬件的陈述读作另一套系统。
8. 80px 网格叠层是深色表面身份的一部分。任何新深色页应继承 `.slide.dark`，好让 `::before` 叠层自动应用。
9. 新版式应保住编辑呼吸空间。如果版式要求内容边到边，重新考虑——Signal 是克制系统。
10. 正文里的斜体永远意味着 font-family 切到 Source Serif 4 斜体、`{colors.gold}`。斜体 DM Sans 不是系统原语。

## 已知缺口

- 四套字体家族运行时从 Google Fonts 加载。如果字体加载失败（网络问题、广告拦截），回退是 Georgia（衬线）、system-ui（无衬线）和 Courier 风格等宽——结果渲染会丢掉大量编辑性格，但仍可读。
- 中文回退（Noto Serif SC、Noto Sans SC）接到每一条 font-family 栈，但度量与西文面略有不同；纯中文套件会读得略紧。
- 80px 网格纹理是绑在视口尺度上的魔术数字；在非常大的视口（>2560px）上，网格可能开始感觉粗糙，而不是难以察觉。
- 幻灯片导航由 JavaScript 驱动，deck 容器上硬编码 `transform: translateX(...)`。系统依赖这套引擎；替换它需要保住 `is-active` 类行为，动画才会触发。
- `--c-bg-alt`、`--c-bg-light-alt` 和若干闷色 token 已定义但用得克制——它们作为相邻表面区分的储备存在，源模板只偶尔使用。
- 金字塔版式用 `color-mix(in srgb, ...)`，需要现代浏览器支持；较旧浏览器可能把条带渲染成平涂而不是分层。
- 全出血页渐变硬编码为 `rgba(15, 20, 36, 0.9)`（接近海军蓝，但没有经 token 参数化）。改海军蓝色需要并行更新这道渐变。
