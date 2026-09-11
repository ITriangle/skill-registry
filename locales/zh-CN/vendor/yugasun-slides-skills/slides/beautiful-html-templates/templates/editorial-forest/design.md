---
version: alpha
name: Editorial Forest
description: A serif-led editorial presentation system in the register of a literary quarterly or art-book monograph. Display type runs in Source Serif 4 at weight 500 with optical-size axis engaged, scaling up to 220px for cover and stat moments. The palette pairs a deep forest green (#2e4a2a) with a dusty rose pink (#e89cb1) over an oat-cream paper ground (#efe7d4), with JetBrains Mono as the editorial chrome (labels, captions, axis ticks). The aesthetic is closer to a Penguin classic, Apartamento spread, or quiet annual report than a tech keynote — confident, paper-feeling, and committed to a small color vocabulary.

colors:
  green: "#2e4a2a"
  green-deep: "#243a21"
  green-lite: "#3a5a36"
  pink: "#e89cb1"
  pink-deep: "#d27e96"
  cream: "#efe7d4"
  cream-2: "#e6dcc4"
  ink: "#1a1a17"

typography:
  display-hero:
    fontFamily: "'Source Serif 4', 'Source Serif Pro', Georgia, serif"
    fontSize: 220
    fontWeight: 500
    lineHeight: 0.92
    letterSpacing: -0.02em
  display:
    fontFamily: "'Source Serif 4', 'Source Serif Pro', Georgia, serif"
    fontSize: 140
    fontWeight: 500
    lineHeight: 1.02
    letterSpacing: -0.02em
  headline-xl:
    fontFamily: "'Source Serif 4', 'Source Serif Pro', Georgia, serif"
    fontSize: 96
    fontWeight: 500
    lineHeight: 0.96
    letterSpacing: -0.02em
  headline:
    fontFamily: "'Source Serif 4', 'Source Serif Pro', Georgia, serif"
    fontSize: 84
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: -0.02em
  headline-sm:
    fontFamily: "'Source Serif 4', 'Source Serif Pro', Georgia, serif"
    fontSize: 80
    fontWeight: 500
    lineHeight: 0.98
    letterSpacing: -0.02em
  title-card-lg:
    fontFamily: "'Source Serif 4', 'Source Serif Pro', Georgia, serif"
    fontSize: 84
    fontWeight: 500
    lineHeight: 0.98
    letterSpacing: -0.01em
  title-card:
    fontFamily: "'Source Serif 4', 'Source Serif Pro', Georgia, serif"
    fontSize: 68
    fontWeight: 500
    lineHeight: 0.96
    letterSpacing: -0.01em
  title-card-sm:
    fontFamily: "'Source Serif 4', 'Source Serif Pro', Georgia, serif"
    fontSize: 56
    fontWeight: 500
    lineHeight: 0.98
    letterSpacing: -0.01em
  figure-caption-serif:
    fontFamily: "'Source Serif 4', 'Source Serif Pro', Georgia, serif"
    fontSize: 56
    fontWeight: 500
    lineHeight: 1.05
  name:
    fontFamily: "'Source Serif 4', 'Source Serif Pro', Georgia, serif"
    fontSize: 44
    fontWeight: 600
    lineHeight: 1.0
  meta-value:
    fontFamily: "'Source Serif 4', 'Source Serif Pro', Georgia, serif"
    fontSize: 32
    fontWeight: 500
  body-lg:
    fontFamily: "'Source Serif 4', 'Source Serif Pro', Georgia, serif"
    fontSize: 32
    fontWeight: 400
    lineHeight: 1.32
  body:
    fontFamily: "'Source Serif 4', 'Source Serif Pro', Georgia, serif"
    fontSize: 30
    fontWeight: 400
    lineHeight: 1.38
  body-card:
    fontFamily: "'Source Serif 4', 'Source Serif Pro', Georgia, serif"
    fontSize: 26
    fontWeight: 400
    lineHeight: 1.34
  label:
    fontFamily: "'JetBrains Mono', ui-monospace, Menlo, monospace"
    fontSize: 26
    fontWeight: 500
    letterSpacing: 0.18em
    textTransform: uppercase
  label-tight:
    fontFamily: "'JetBrains Mono', ui-monospace, Menlo, monospace"
    fontSize: 26
    fontWeight: 500
    letterSpacing: 0.14em
    textTransform: uppercase
  caption-mono:
    fontFamily: "'JetBrains Mono', ui-monospace, Menlo, monospace"
    fontSize: 24
    fontWeight: 500
    letterSpacing: 0.14em
    textTransform: uppercase
  axis-mono:
    fontFamily: "'JetBrains Mono', ui-monospace, Menlo, monospace"
    fontSize: 26
    fontWeight: 500
    letterSpacing: 0.08em
  stat-figure:
    fontFamily: "'Source Serif 4', 'Source Serif Pro', Georgia, serif"
    fontSize: 220
    fontWeight: 500
    lineHeight: 0.92
    letterSpacing: -0.03em
  stat-figure-unit:
    fontFamily: "'Source Serif 4', 'Source Serif Pro', Georgia, serif"
    fontSize: 110
    fontWeight: 500
    lineHeight: 0.92

spacing:
  slide-pad-default: "96px 120px"
  slide-pad-narrow: "100px 120px"
  slide-pad-wide: "100px 140px"
  slide-pad-statement: "130px 160px"
  grid-gap-cards: 28
  grid-gap-topics: 24
  grid-gap-kpi: 60
  rule-weight: "2px"
  rule-weight-card: "2.5px"
  radius-card: "6px"
  radius-card-step: "8px"
  radius-bar-top: "3px 3px 0 0"
  radius-mark-circle: "50%"

canvas:
  width: 1920px
  height: 1080px

components:
  topic-tile:
    description: "Bordered or filled rectangular region holding a mono ordinal, a serif title, optional body, and a mono foot. Background may be green / green-lite / pink / cream-2-with-green-border. Corner radius 6px."
    borderRadius: "{spacing.radius-card}"
    padding: "40px 40px 36px"
  step-tile:
    description: "Vertical card carrying a mono ordinal, a serif title, body paragraph, and a mono marker row separated by a top rule. Background fills: cream-with-green-border, solid green, or solid pink."
    borderRadius: "{spacing.radius-card-step}"
    padding: "40px 32px 32px"
    minHeight: "470px"
    border: "2.5px solid currentColor-region"
  monogram-circle:
    width: "130px"
    height: "130px"
    borderRadius: "{spacing.radius-mark-circle}"
    border: "2px solid {colors.pink}"
    fontFamily: "JetBrains Mono"
    fontSize: 28
    letterSpacing: 0.1em
    fontWeight: 500
    description: "Outlined round mark holding a short mono monogram. The system's signature identity stamp."
  topbar:
    placement: "top edge of slide"
    layout: "flex space-between, baseline-aligned"
    content: "{components.label} on the left, monogram-circle or counter on the right"
  footline:
    position: "absolute"
    placement: "bottom edge of slide, full-width between slide padding"
    layout: "flex space-between"
    typography: "{typography.caption-mono}"
  meta-dl:
    description: "Three-column definition list separated by a top rule (2px {colors.green}). Each entry has a mono dt label and a serif dd value."
    columns: 3
    gap: "36px"
    topBorder: "2px solid {colors.green}"
  bar:
    width: "56px"
    borderRadius: "{spacing.radius-bar-top}"
    description: "Vertical chart bar in pink, cream, or green. Value label printed above bar in mono."
  chart-axis:
    border: "2px solid currentColor"
    description: "Y-axis and x-axis use a single 2px rule on the inner edges of the plot region; no full axis box."
  rule-thin:
    description: "Hairline 2px rule, used as section separator above kpi rows, summary grids, meta dls. Color follows region (green on cream, pink on green)."
  legend-swatch:
    display: "inline-block"
    width: "26px"
    height: "26px"
    borderRadius: "2px"
    description: "Small filled square preceding a mono legend label. 2px corner radius is the smallest radius in the system."
---

## 概述

Editorial Forest 是一套**以衬线为主导的编辑风演示系统**，气质接近 Penguin 经典、安静的年报，或艺术书内页。系统的底层前提是单一、自信的字体声音——Source Serif 4——在极端字号（最高 220px）上承担标题与数据数字，JetBrains Mono 则扮演编辑「铬件」的配角（标签、图注、坐标刻度、页脚行）。

衬线几乎在每一个展示时刻都跑 **字重 500**——从不用更常见的 400 或 700。500 是本系统最鲜明的排印选择：够重，读起来像写过的；够轻，页面仍保持平静。启用了光学字号轴（`opsz` 8..60），意味着同一套 Source Serif 4 在 26px 图注与 220px 展示字号上会画出略有不同的字形——小字号会自动补上更高对比与更细的细节。JetBrains Mono 以 500、全大写、0.14em–0.18em 字距运行，用于每一个标签、标记、图注、坐标刻度与页脚行。系统从不混入第三套字体。

色板是一套收得很紧的五色编辑组合，围绕三块主表面：**深森林绿**（`{colors.green}` — #2e4a2a）、**灰玫瑰粉**（`{colors.pink}` — #e89cb1），以及**燕麦奶油纸色**（`{colors.cream}` — #efe7d4）。两对近重复色补齐整套：`{colors.green-deep}` 用于粉底上的绿字对比，`{colors.green-lite}` 用于需要第二档绿色的瓷砖填充，`{colors.pink-deep}` 用于粉上粉的描边，`{colors.cream-2}` 用于坐在主奶油表面上的瓷砖。正文到处都是 `{colors.ink}`（#1a1a17）——偏暖的近黑——除非坐在绿或粉表面上，那时改用该表面的互补色（绿底用奶油或粉；粉底用绿深或奶油）。

纵深是**扁平、纸感的**。没有投影、没有光晕、没有渐变、没有叠层。抬升完全靠色块对比、2px 发丝线，以及填色区域与描边区域的差别。6px 与 8px 的卡片圆角，是除花押圆章之外系统里仅有的圆意。页面读起来像印出来的，不像玻璃界面。

**密度哲学：疏朗而坚定。** 每一页只承载一个强主题——一条标题、一句引语、一张图、一行数据、一组卡片网格——四周是深的负空间。96–140px 的页边距很大；页顶是等宽顶栏（标签 + 花押或计数），页底是等宽脚线，中间把主主题放大。一页硬塞两块互相抢戏的内容会读成坏掉；一页一条展示标题 + 配套卡片 + 呼吸空间才读成权威。宁可少元素、大尺寸，也不要多元素、小尺寸。

**关键特征：**
- 三色编辑色板：深森林绿、灰玫瑰粉、燕麦奶油纸。一页典型用两种表面色；三种就偏吵。
- 每一个标题、正文与展示时刻都用 Source Serif 4、字重 500。启用光学字号轴，让字形随尺寸变化。
- 每一个标签、图注、坐标刻度与脚线都用 JetBrains Mono、字重 500、全大写、宽字距（0.14em–0.18em）。
- 封面与数据数字时刻展示字号到 220px；主标题 96px；卡片标题 56–84px。
- 2px 发丝线分隔叠放的区块——从不更粗，颜色也不超出所在区域语境。
- 主题瓷砖圆角 6px，步骤瓷砖 8px。花押圆章是唯一完全圆形的形状。
- 每一页都有顶栏（标签 + 花押或计数），大多数还有脚线（等宽图注行）。这套铬件锚定编辑感。
- 无阴影、无渐变、无光晕。抬升靠色块 + 线条。

## 色彩

### 色板
- **Green**（`{colors.green}` — #2e4a2a）：深森林主色。用作幻灯片表面、瓷砖填充、卡片描边、meta-dl 线条色，以及奶油表面上的主文本色。系统里最鲜明的表面。
- **Green Deep**（`{colors.green-deep}` — #243a21）：更深的绿，几乎只用于粉表面上的文本色——纯绿在那里对比不够。也用于粉色瓷砖上的文本。
- **Green Lite**（`{colors.green-lite}` — #3a5a36）：更浅的绿，当两块绿需要并排时用作瓷砖填充（例如同一网格里主绿瓷砖旁边的次绿-lite 瓷砖）。上面走粉色文本。
- **Pink**（`{colors.pink}` — #e89cb1）：灰玫瑰。用作幻灯片表面、瓷砖填充、绿底上的文本色、柱状图系列色，以及花押圆章描边色。系统的主强调色。
- **Pink Deep**（`{colors.pink-deep}` — #d27e96）：略深的玫瑰，只用作粉色填充瓷砖的描边，好让同色描边与填充分开。
- **Cream**（`{colors.cream}` — #efe7d4）：燕麦纸面。非封面页的默认幻灯片背景、绿底上的正文字色，以及奶油色柱状图系列色。
- **Cream 2**（`{colors.cream-2}` — #e6dcc4）：略深的奶油，用作奶油幻灯片表面上的瓷砖填充。配 2px 绿色描边，让瓷砖与页面底色分开。
- **Ink**（`{colors.ink}` — #1a1a17）：奶油表面上的正文字色。偏暖的近黑；从不用纯 #000。

### 默认值
- **默认幻灯片背景**：内容重的页用 `{colors.cream}`；封面、陈述数据、总结，以及任何需要分量的时刻用 `{colors.green}`。
- **`{colors.cream}` 表面上的默认标题色**：`{colors.green}`。
- **`{colors.green}` 表面上的默认标题色**：主标题用 `{colors.cream}`，hero / 封面级标题用 `{colors.pink}`。
- **`{colors.pink}` 表面上的默认标题色**：`{colors.green-deep}`。
- **`{colors.cream}` 表面上的默认正文字色**：`{colors.ink}`。
- **`{colors.green}` 表面上的默认正文字色**：`{colors.cream}`。
- **`{colors.pink}` 表面上的默认正文字色**：`{colors.green-deep}`。
- **默认标签 / 图注色**：跟区域强调色走（绿底标签为粉，奶油底为绿，粉底为绿深）。
- **奶油幻灯片上的默认瓷砖填充**：在轮换里选——实心绿（配粉色文本）、实心粉（配绿深文本）、green-lite（配粉色文本），或 cream-2 配 2px 绿色描边（配绿色文本）。同一网格通常混用这 4 种里的 3 种。
- **默认线条色**：奶油底用绿，绿底用粉，粉底用绿深。2px 发丝线总是拾取该区域的强调色。

色板刻意收紧。引入第四个色相家族（黄、蓝、再加一档玫瑰）会破坏编辑纪律。守住绿 / 粉 / 奶油三元组，把变化交给填色瓷砖与描边瓷砖之间的对比。

## 字体排印

### 字体家族
系统恰好加载两套网页字体：**Source Serif 4**（完整光学字号轴 8..60，字重 300–800）和 **JetBrains Mono**（字重 400、500、700）。Source Serif 4 承担每一个编辑时刻——标题、正文、衬线图注、姓名、数字。JetBrains Mono 承担每一件铬件——标签、标语、坐标刻度、脚线、瓷砖上的序号。

等宽 / 衬线配对就是系统的排印身份。等宽从不试图当标题；衬线从不试图当图注。角色与常见的「无衬线做铬件、衬线做正文」正好反过来——这里是「等宽做铬件，衬线做正文与展示」。

Source Serif 4 几乎在每一个时刻都跑 **字重 500**。字重 400 只出现在正文段落（小尺寸时更轻更好读）。字重 600 只出现一次，用于陈述页的署名姓名——略重一点，好把专有名从周围的等宽标签里分开。不用字重 700。

### 展示、正文与铬件字号阶梯

| Token | 字号 | 字体 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.display-hero}` | 220px | Source Serif 4 | 500 | 封面级或收场级标题 |
| `{typography.display}` | 140px | Source Serif 4 | 500 | 引语 / 大观点陈述 |
| `{typography.headline-xl}` | 96px | Source Serif 4 | 500 | 奶油表面上的主章节标题 |
| `{typography.headline}` | 84px | Source Serif 4 | 500 | 绿表面上的主章节标题 |
| `{typography.headline-sm}` | 80px | Source Serif 4 | 500 | 数据行的引导标题 |
| `{typography.title-card-lg}` | 84px | Source Serif 4 | 500 | hero 主题瓷砖内的标题（网格里最大的那块） |
| `{typography.title-card}` | 68px | Source Serif 4 | 500 | 步骤瓷砖内的标题 |
| `{typography.title-card-sm}` | 56px | Source Serif 4 | 500 | 标准主题瓷砖内的标题 |
| `{typography.figure-caption-serif}` | 56px | Source Serif 4 | 500 | 居中的图 / 图片占位图注 |
| `{typography.stat-figure}` | 220px | Source Serif 4 | 500 | KPI 数字 |
| `{typography.stat-figure-unit}` | 110px | Source Serif 4 | 500 | KPI 数字上的单位后缀（例如 "%"） |
| `{typography.name}` | 44px | Source Serif 4 | 600 | 署名行里的人名 |
| `{typography.meta-value}` | 32px | Source Serif 4 | 500 | 元信息行里的定义列表值 |
| `{typography.body-lg}` | 32px | Source Serif 4 | 400 | 总结或数据说明里的主正文段落 |
| `{typography.body}` | 30px | Source Serif 4 | 400 | 标准正文段落 |
| `{typography.body-card}` | 26px | Source Serif 4 | 400 | 卡片或瓷砖内的正文 |
| `{typography.label}` | 26px | JetBrains Mono | 500 / 0.18em | 顶栏里的眉题或章节标签 |
| `{typography.label-tight}` | 26px | JetBrains Mono | 500 / 0.14em | 图注行、脚线、署名行、瓷砖序号 |
| `{typography.caption-mono}` | 24px | JetBrains Mono | 500 / 0.12–0.16em | 瓷砖脚注、瓷砖标记、kpi 标签、meta-dl 术语 |
| `{typography.axis-mono}` | 26px | JetBrains Mono | 500 / 0.08em | 图表坐标刻度与标签 |

### 默认值
- **主章节标题的默认字号**：奶油表面用 `{typography.headline-xl}`（96px），绿表面用 `{typography.headline}`（84px）。
- **封面级或收场级时刻的默认字号**：`{typography.display-hero}`（220px）。
- **引语 / 大观点陈述的默认字号**：`{typography.display}`（140px）。
- **正文段落的默认字号**：`{typography.body}`（30px），衬线字重 400。
- **卡片 / 瓷砖内正文段落的默认字号**：`{typography.body-card}`（26px）。
- **元信息 dt 标签或瓷砖序号的默认字号**：`{typography.caption-mono}`（24px），JetBrains Mono 全大写。
- **顶栏标签 / 眉题的默认字号**：`{typography.label}`（26px），JetBrains Mono 全大写、0.18em 字距。
- **任何衬线时刻的默认字重**：500。（400 留给正文段落；600 只用于署名里的专有名。）
- **任何等宽时刻的默认字重**：500。

拿不准时，奶油页的主标题用 `{typography.headline-xl}`（96px），不要上更大的展示字号。140–220px 这一档留给陈述、数据数字，以及 hero/收场时刻——日常标题也用它，会把系统的层级压平。

### 标志性处理
只要用到对应元素类型，这些处理就**不可省略**：

- **每一个 JetBrains Mono 元素都是全大写，字距至少 0.08em。** 等宽用句首大写或不加字距，读起来像代码，不像编辑铬件。宽字距才让等宽像杂志里的图注行，而不像终端。
- **每一个 Source Serif 4 展示元素都用负字距（-0.01em 到 -0.03em）。** 更紧的字距把大号衬线字形收成一团，对 96–220px 至关重要。展示衬线用默认字距会显得松、没处理过。
- **展示标题的行高在 0.92 到 1.02 之间。** 紧行高是系统展示声音的一部分。更大的标题更紧（220px 时 0.92）；较小标题（84–96px）跑 0.96–1.0。
- **正文段落用衬线字重 400，不是 500。** 从标题到正文的字重下落，是系统的阅读节奏。正文用 500 会显得沉。
- **每一页都有顶栏（等宽标签 + 对侧的花押或计数）。** 顶栏是系统通用的铬件锚点。
- **区块之间的发丝线永远是 2px solid。** 从不用 1px（读成 Web 应用），从不用 3px+（读成海报）。

### 排印原则
字重 500 + 光学字号 + 紧字距的组合，就是系统的展示声音——改掉这三项里的任何一项（例如衬线字重 700，或默认字距，或关掉 opsz）都会读成另一套设计系统。衬线/等宽的角色划分很严：等宽从不以标题级出现，衬线从不以坐标刻度级出现。

系统里任何地方都不用斜体。不用下划线。强调靠尺寸与色彩对比，不靠字体变体。

## 版式

### 画布系统
系统面向固定的 **1920×1080** 画布。幻灯片是精确宽高的 `<section>` 元素；渲染依赖 `deck-stage.js` 把画布缩放到视口。画布是纸，不是视口——为投影、打印或导出 PDF 而设计。

### 幻灯片内边距阶梯
| Token | 取值 | 用途 |
|---|---|---|
| `{spacing.slide-pad-default}` | 96px 120px | 标准幻灯片内边距 |
| `{spacing.slide-pad-narrow}` | 100px 120px | 数据、框架、统计页——顶边略高 |
| `{spacing.slide-pad-wide}` | 100px 140px | 封面、总结页——给 hero 标题额外的侧边距 |
| `{spacing.slide-pad-statement}` | 130px 160px | 陈述页——展示引语时刻用最慷慨的内边距 |

按内容分量选内边距。陈述级时刻用最宽的内边距；日常内容页用默认的 96×120。

### 铬件解剖
每一页至少在顶边带一条 **topbar**——一行 flex，一侧是 JetBrains Mono `{typography.label}`，另一侧是 `{components.monogram-circle}` 或等宽计数 / 地点字符串。更重的页（封面、数据、总结）还带一条 **footline**，绝对定位在 `bottom: 60–80px`，等宽图注行在内边距之间横跨整页。

顶栏是系统的脊柱。没有它，一页读起来像没处理过。

### 卡片圆角
| 取值 | 用途 |
|---|---|
| 2px | 仅图例色块（系统里最小的圆角） |
| 3px 3px 0 0 | 柱状图柱子的顶角 |
| 6px | 主题瓷砖（议程式网格） |
| 8px | 步骤瓷砖（框架式网格） |
| 50% | 花押圆章 |

卡片是微圆的——既不是尖角，也不是大圆角。6–8px 圆角给系统纸感、而不是塑料感。

## 层次与纵深

### 扁平，无阴影
本系统**没有阴影**。卡片没有，瓷砖没有，文字没有，花押圆章也没有。抬升完全靠：

1. **色块对比**——奶油页上的绿色瓷砖之所以读成抬升，是因为深绿块从纸面里分出来。
2. **2px 发丝线**——区块分隔（kpi 行、总结网格、meta dl 上方）坐在一条 2px 线上，颜色跟区域强调色走。
3. **描边 vs 填色**——带 2px 绿色描边的 cream-2 瓷砖，与旁边的实心填充瓷砖读成不同的抬升。

没有阴影，本身就是抬升语言。加上 `box-shadow: 0 4px 12px rgba(0,0,0,0.1)` 会把编辑感打碎。

### 纸面规则
系统里每一块表面都读成纸，而不是数字窗格。奶油色调（`{colors.cream}`、`{colors.cream-2}`）把这种质感直接带出来。绿与粉表面通过联想继承它——全饱和使用、被奶油铬件围住、从无阴影或光晕，读成印在纸上的墨。

## 形状与处理

### 描边粗细与样式
- **2px solid** —— 通用发丝线。kpi 行 / 总结网格 / meta dl / 图表坐标上方的区块分隔线；cream-2 瓷砖描边；花押圆章描边。
- **2.5px solid** —— 步骤瓷砖描边。略重一点，好让瓷砖读成独立对象，而不是发丝线。

描边取区域强调色（奶油底用 `{colors.green}`，绿底用 `{colors.pink}`，粉底用 `{colors.green-deep}` 或 `{colors.pink-deep}`）。

### 装饰元素类型

**花押圆章**（`{components.monogram-circle}`）—— 130px 描边圆，2px 粉色描边，内放 2–3 个字符的 JetBrains Mono 花押，28px。出现在封面与总结页的右上。系统的身份戳。

**顶栏**（`{components.topbar}`）—— 横跨每一页顶部的 flex 行。一侧 JetBrains Mono 标签，另一侧花押、计数或地点字符串。顶栏标明这一页属于哪一族表面（标签颜色会告诉你）。

**脚线**（`{components.footline}`）—— 绝对定位的 flex 行，在 `bottom: 60–80px`，在内边距之间横跨整页。两条等宽图注字符串（例如左侧章节名，右侧页码）。用于封面、数据、总结，以及任何想读成印刷页的幻灯片。

**主题瓷砖**（`{components.topic-tile}`）—— 6px 圆角矩形区域，内放等宽序号、衬线标题、可选正文，以及等宽脚注字符串。背景填充在绿、green-lite、粉，或 cream-2-with-green-border 之间轮换。这些瓷砖组成的网格，就是议程 / 目录模式。

**步骤瓷砖**（`{components.step-tile}`）—— 8px 圆角竖向卡片，2.5px 描边，内放等宽序号、衬线标题（68px）、一段正文，以及被顶部分隔线隔开的等宽标记行。背景填充：cream-with-green-border、实心绿，或实心粉。3–4 块步骤瓷砖排成一行，就是框架 / 流程模式。

**KPI 块** —— 竖向堆叠：顶上等宽标签（24px），超大衬线数字（220px）加可选 110px 单位，然后一段衬线说明（30px）。坐在一行里，上方被绿表面上的 2px 粉色线隔开。

**柱（图表）** —— 56px 宽的矩形，顶角 3px 圆，填粉、奶油或绿。数值标签是等宽 24px，绝对定位在柱顶上方 38px。

**元信息定义列表**（`{components.meta-dl}`）—— 三列 dt/dd 网格，带 2px 顶边框。dt 是等宽 24px 全大写加字距，dd 是衬线 32px 字重 500。用作双栏页底部的致谢 / 规格 / 详情行。

**图例行** —— 水平 flex 的等宽全大写项，每项前面跟一个 26×26px、2px 圆角的填色色块。用于图表与数据语境。

## 应做与不应做

### 应做
- 每一条展示标题都用 Source Serif 4、字重 500、负字距（-0.01em 到 -0.03em）和紧行高（0.92–1.0）。这个组合就是系统的声音。
- 每一个标签、图注、标记、坐标刻度与脚线都用 JetBrains Mono、字重 500、全大写、0.08em–0.18em 字距。
- 每一页放一条顶栏（等宽标签 + 花押或计数）。顶栏是系统的脊柱。
- 每一页选一块主导表面（绿、粉或奶油），让它撑满整张画布。一页最多两种表面色。
- 网格里配对瓷砖填充：在绿 + 粉 + green-lite + cream-2-with-green-border 之间轮换，不要所有瓷砖复用同一种填充。
- 用 2px solid 发丝线分隔叠放的区块（kpi 行、总结网格、meta dl）。发丝线就是系统的分隔语言。
- 内容允许时把展示字号拉得很猛——陈述、hero 与收场时刻用 140–220px。有空间时，系统奖励大。
- 用慷慨的幻灯片内边距（96–160px）。负空间是编辑气质的一部分；挤的内边距读成坏掉。
- 把花押圆章留给封面与总结时刻。每一页都用，会稀释它作为身份戳的功能。

### 不应做
- 不要给任何元素加 box-shadow。系统无阴影；加阴影会打碎纸感。
- 不要引入第三套字体。只有 Source Serif 4 和 JetBrains Mono。不要 Inter，不要系统栈。
- 不要把衬线做成斜体或下划线。强调靠尺寸和颜色，不靠字体变体。
- 不要把 JetBrains Mono 做成句首大写或不加字距。等宽没有全大写 + 字距，读起来像代码，不像铬件。
- 不要引入第四个色相家族（黄、蓝、薰衣草）。绿 / 粉 / 奶油三元组就是全部色板。
- 不要用重描边（4px+）或细发丝线（1px）。系统只有 2px 和 2.5px——二选一。
- 不要在一页上堆两块互相抢戏的内容。一页一个主题；放大或拆开。
- 不要用 rgba 透明做表面色。每一块表面都是实心的纸上墨。
- 不要把衬线正文跑在字重 500——会显得沉。正文是字重 400；展示是字重 500。
- 不要省略顶栏。页顶没有等宽标签，编辑脊柱就没了。

## 响应行为

这是一套**固定 1920×1080 的演示系统**，通过 `deck-stage.js` 渲染。画布不是 Web 意义上的响应式——没有媒体查询、没有断点、没有流体尺寸。每一个度量都是 1920×1080 上的固定像素。

### 缩放行为
`deck-stage.js` 脚本包住每个 `<section>`，把 1920×1080 画布均匀缩放到浏览器视口，必要时加黑边。字号、内边距、间隙和线条粗细都是像素，随画布等比缩放。1920px 上读成 2px 的描边，在 960px 视口宽上会读成 1px——这在系统的容差之内可以接受。

### 演示行为
导航交给 `deck-stage.js` 提供的包装层——没有内联键盘处理。把每个 `<section>` 当作一页；运行时负责转场。

### 打印 / 导出
因为每一个度量都是 1920×1080 画布内的固定像素，系统可以干净地按同一宽高比（16:9）导出 PDF。带光学字号轴的 Source Serif 4 在印刷分辨率下表现很好，因为小字号变体自动拾取适合印刷的字形细节。

## 中日韩与国际内容

### 推荐中文搭配

| 角色 | 中文字体 | 字重 | 原因 |
|---|---|---|---|
| 展示标题（220 / 140 / 96 / 84px） | 霞鹜文楷 LXGW WenKai（Noto Serif SC 回退） | 400 | 文学、偏手写的笔触；对得上 Source Serif 4 的 Penguin 经典气质 |
| 正文段落（26 / 30 / 32px） | 思源宋体 Noto Serif SC | 400 | 读起来像文学季刊的印刷正文声音 |
| 数据数字（220px） | 思源宋体 Noto Serif SC | 700 | 明朝体字重 700 给出 Source Serif 4 字重 500 在拉丁文里提供的数字体量 |
| 等宽标签 / 图注 / 脚线（24–26px） | 思源等宽 Noto Sans Mono CJK SC | 500 | JetBrains Mono 没有中日韩字形；Noto Sans Mono CJK SC 保住打字机铬件的质感 |

### 中西混排策略

用 **策略 C** —— 拉丁文保持 Source Serif 4，中日韩字形回退到 LXGW WenKai（标题 / 展示）或 Noto Serif SC（正文 / 数据）。对 Editorial Forest 这是对的，因为 Source Serif 4 的光学字号轴是系统签名；整套换成明朝体会把定义这套 deck 的 Penguin 经典气质压平。font-family 栈把拉丁字体放在前面，然后是中日韩回退，再然后是通用 serif：

```css
font-family: 'Source Serif 4', 'Source Serif Pro', 'LXGW WenKai TC', 'Noto Serif SC', Georgia, serif;
```

浏览器按字形回退：拉丁字符以字重 500、启用 opsz 的 Source Serif 4 渲染，中文字符以 LXGW WenKai（展示）或 Noto Serif SC（正文）渲染。展示字号（96–220px）上的基线错位是主要要注意的——LXGW WenKai 的光学基线比 Source Serif 4 略高，所以像 "Designed in 北京" 这样的混排行可能出现 1–2px 的上下晃。幻灯片内容可以接受；印刷导出时，优先整行全中文或全拉丁。

### 加载

加到现有的 Google Fonts `<link>`（或作为第二条 link）：

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=LXGW+WenKai+TC&family=Noto+Serif+SC:wght@400;500;700&display=swap" rel="stylesheet">
```

LXGW WenKai TC 是 Google Fonts 上提供的版本（简体构建 `LXGW+WenKai+SC` 还不在 Google CDN 上——TC 同时带繁体和简体字形，两边都能用）。

### 通用中日韩调整

这些调整适用于本系统里的**每一个中日韩块**，不论尺寸或角色：

- **把行高放宽 0.05–0.08。** 中日韩字形是全宽方块，视觉重量比拉丁字母大；为拉丁调的行高（展示 0.92–1.0，正文 1.32–1.38）在中文里会读成挤。展示提到 1.0–1.1，正文提到 1.5–1.6。
- **去掉中文标题上的负字距。** Source Serif 4 展示用 -0.01em 到 -0.03em 字距，会把汉字挤在一起。中文段设 `letter-spacing: 0`——若标题看起来仍挤，可用极小的正值 `0.02em`。
- **从不要对中日韩文本使用 `text-transform: uppercase`。** 中文没有大小写；这条 CSS 对汉字什么也不做，却会悄悄弄坏混排行里本该大写的拉丁部分。
- **中文句子里用中文全角标点**（`，。：；！？「」『』（）`），不要用拉丁等价物（`,.:;!?""''()`）。同一句里混用两套标点系统，读起来像排版错误。
- **中文标题末尾不要句号（。）。** 中文标题遵循与拉丁相同的规则——标题式行去掉句末标点。正文段落保留 。
- **在中日韩与拉丁段的交界处应用盘古之白。** 汉字与相邻的拉丁词或数字之间要有空格（或 0.25em 边距），例如 `2026 年 5 月` 而不是 `2026年5月`。可以手打空格，或用 `pangu.js` 一类的自动加空。
- **一句只用一套字体。** 不要在同一句里在 LXGW WenKai 和 Noto Serif SC 之间切换——按尺寸档选字体（展示 = LXGW WenKai，正文 = Noto Serif SC），整段坚持用它。

### 本系统的审美说明

Editorial Forest 的整体声音是「Penguin 经典 / 安静年报」——字重 500 的衬线，由光学字号轴做随尺寸变化的字形工作。对应这种气质的中文是**展示时刻用 LXGW WenKai**（它有与 Source Serif 4 在 500 时相同的手排、略不正式的暖意）和**正文用 Noto Serif SC 400**（平静的明朝体声音，读起来像文学期刊）。正文不要用 Noto Sans SC——无衬线会把系统翻成「技术报告」而不是「专著内页」。

系统的等宽 / 衬线角色划分（JetBrains Mono 做铬件，Source Serif 4 做其余一切）可以干净地映射到中文。顶栏标签、脚线字符串、瓷砖序号和坐标刻度用 Noto Sans Mono CJK SC——保持全大写等价（即拉丁标签用 0.14em–0.18em 字距；中文则用 Mono CJK 字重 500 提供同样的铬件质感）。不要把中文标签跑在 LXGW WenKai 或 Noto Serif SC 上；编辑铬件会失去打字机感。

### 已知中日韩缺口

LXGW WenKai 的笔触暖意是它在大展示字号上的长处，但在正文字号（26–32px）上，同样的笔触会略显噪。系统把正文提到 Noto Serif SC（更干净的明朝体）来避开这一点，但 96px 的 LXGW WenKai 标题与下方 30px 的 Noto Serif SC 段落之间的视觉交接，是系统最大的中日韩接缝——两套字体的笔画对比曲线不同。若接缝读得太响，展示与正文都用 Noto Serif SC（牺牲暖意换一致性），或都用 LXGW WenKai（牺牲正文易读换一致性）。默认拆分对大多数 deck 是对的折中，但封面与陈述页值得人工检查。

## 迭代指南

1. 任何新标题都是 Source Serif 4 字重 500、负字距。从展示阶梯里选字号（220 / 140 / 96 / 84 / 80 / 68 / 56）——不要发明新字号。
2. 任何新标签、图注或标记都是 JetBrains Mono 字重 500、全大写、0.08em–0.18em 字距。从等宽阶梯里选字号（26 / 24）。
3. 任何新幻灯片顶部都带顶栏。等宽标签颜色跟表面走（绿底粉、奶油底绿、粉底绿深）。
4. 任何新卡片用 6px（主题瓷砖）或 8px（步骤瓷砖）圆角。花押圆章是唯一完全圆形的形状；不要引入第四档圆角。
5. 任何新区块分隔都是区域强调色的 2px 发丝线。不要 1px，不要 3px。
6. 任何新填充色必须来自现有色板（`{colors.green}`、`{colors.green-lite}`、`{colors.pink}`、`{colors.cream}`、`{colors.cream-2}`）。不要引入黄、蓝或第三档粉。
7. 任何新正文段落都是衬线字重 400、26–32px。不要把正文跑在字重 500。
8. 任何新 KPI 数字都是 `{typography.stat-figure}`（220px）。更小的 KPI 字号不在系统里——若版式装不下 220px，就重组这一页。
9. 任何新图表都用柱处理（粉 / 奶油 / 绿填充、等宽坐标、2px 轴线），放在绿表面上。数据构图是系统身份的一部分。
10. 拿不准时，少元素、大尺寸。系统的编辑气质一挤就会塌。

## 已知缺口

- 系统依赖 `deck-stage.js` 做画布缩放与幻灯片导航。这份 design.md 没有描述该脚本——把它当作运行时依赖。
- Source Serif 4 和 JetBrains Mono 通过 `<link>` 从 Google Fonts 加载。离线渲染会分别回退到 Georgia 衬线和 Menlo 等宽，能保住大致性格，但会失去光学字号轴和 JetBrains Mono 的身份。离线 / 印刷可靠性建议自托管。
- Source Serif 4 的光学字号轴（`opsz` 8..60）对系统品质至关重要——用无 opsz 的回退字体会压平随尺寸变化的字形对比。
- 柱状图用手设柱高（固定 520px 绘图区的 `%`）。没有数据绑定——扩展图表需要手工算高度。
- 花押圆章、脚线字符串和瓷砖计数在源码里是写死的文本。每套 deck 都要用实际身份替换。
- 系统没有 `@media print` 规则，也没有响应断点——它是固定 1920×1080，任何视口适配都靠 `deck-stage.js`。
- 绿上粉与粉上绿的文本对比在所用的展示字号（84px+）上足够，但在正文字号会通不过 WCAG AA。不要把 26px 正文做成粉上绿或绿上粉——小字保持绿上奶油或奶油上墨。
