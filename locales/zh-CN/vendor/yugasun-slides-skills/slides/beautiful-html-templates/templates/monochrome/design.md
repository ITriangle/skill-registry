---
version: alpha
name: Monochrome (Ivory Ledger)
description: A literary editorial system rendered in black ink on cream paper. Ultra-light geometric sans (Jost at weight 200–300) carries every headline; Lora italic serif handles quote text and insight-card titles; JetBrains Mono provides the structural chrome. There are no chromatic accents — every color in the palette is a graphite or cream tone, and "accent" simply means "darker ink." The aesthetic borrows from independent research reports, scholarly monographs, and the quietest end of contemporary editorial design — closer to a printed journal than a tech presentation.

colors:
  cream-paper: "#FAFADF"
  cream-paper-2: "#F2F2D2"
  cream-paper-3: "#F0F0D4"
  cream-warm: "#F5F0E4"
  ink-black: "#1A1A16"
  ink-graphite: "#5E5E54"
  ink-graphite-light: "#8A8A80"

color-aliases:
  c-bg: cream-paper
  c-bg-light: cream-paper
  c-bg-cream: cream-warm
  c-fg: ink-black
  c-fg-light: ink-black
  c-fg-2: ink-graphite
  c-fg-3: ink-graphite-light
  c-accent: ink-black
  c-border: ink-black
  c-border-light: ink-black

typography:
  display:
    fontFamily: "Jost, Noto Sans SC, system-ui, sans-serif"
    fontSize: 8.5vw
    fontWeight: 200
    lineHeight: 0.96
    letterSpacing: -0.02em
  h1:
    fontFamily: "Jost, Noto Sans SC, system-ui, sans-serif"
    fontSize: 5vw
    fontWeight: 200
    lineHeight: 1.1
    letterSpacing: -0.01em
  h2:
    fontFamily: "Jost, Noto Sans SC, system-ui, sans-serif"
    fontSize: 3.2vw
    fontWeight: 300
    lineHeight: 1.2
  h3:
    fontFamily: "Jost, Noto Sans SC, system-ui, sans-serif"
    fontSize: 2vw
    fontWeight: 400
    lineHeight: 1.3
  lead:
    fontFamily: "Jost, Noto Sans SC, system-ui, sans-serif"
    fontSize: 1.5vw
    fontWeight: 300
    lineHeight: 1.65
  body:
    fontFamily: "Jost, Noto Sans SC, system-ui, sans-serif"
    fontSize: 1.1vw
    fontWeight: 300
    lineHeight: 1.7
  caption:
    fontFamily: "Jost, Noto Sans SC, system-ui, sans-serif"
    fontSize: 0.85vw
    fontWeight: 300
    lineHeight: 1.55
  label:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 0.72vw
    fontWeight: 400
    letterSpacing: 0.12em
    textTransform: uppercase
  quote-serif:
    fontFamily: "Lora, Noto Serif SC, Georgia, serif"
    fontSize: 3.2vw
    fontWeight: 400
    lineHeight: 1.35
  insight-serif:
    fontFamily: "Lora, Noto Serif SC, Georgia, serif"
    fontSize: 2.8vw
    fontWeight: 400
    lineHeight: 1.15
  stat-value:
    fontFamily: "Jost, Noto Sans SC, system-ui, sans-serif"
    fontSize: 5.5vw
    fontWeight: 200
    lineHeight: 1.0
    letterSpacing: -0.03em
  flow-num:
    fontFamily: "Jost, Noto Sans SC, system-ui, sans-serif"
    fontSize: 3.5vw
    fontWeight: 200
    lineHeight: 1.0
    letterSpacing: -0.02em

spacing:
  pad-x: 8vw
  pad-y: 6vh
  gap-lg: 5vh
  gap-md: 3vh
  gap-sm: 1.5vh

canvas:
  width: 100vw
  height: 100vh

components:
  rule:
    width: 36px
    height: 1px
    background: "{colors.ink-black}"
    description: "A 36-pixel hairline accent rule. The system's signature small punctuation mark — appears under chapter labels, beside kickers, above stat values."
  rule-full:
    width: "100%"
    height: 1px
    background: "{colors.ink-black}"
    description: "Full-width 1px hairline rule for chrome bands, foot bands, and section dividers."
  kicker:
    fontFamily: "{typography.label.fontFamily}"
    fontSize: "{typography.label.fontSize}"
    letterSpacing: 0.14em
    textTransform: uppercase
    color: "{colors.ink-graphite-light}"
    description: "Muted mono uppercase eyebrow label above a headline."
  tag:
    border: "1px solid {colors.ink-black}"
    padding: "0.3em 0.8em"
    fontFamily: "{typography.label.fontFamily}"
    fontSize: "{typography.label.fontSize}"
    letterSpacing: 0.12em
    textTransform: uppercase
    description: "Bordered inline tag for version numbers, status labels."
  bullet-marker:
    content: "—"
    color: "{colors.ink-graphite-light}"
    fontFamily: "{typography.label.fontFamily}"
    description: "Em-dash in muted graphite via JetBrains Mono. The standard list mark; never a dot, never a check."
  insight-card:
    background: "{colors.cream-warm}"
    borderRadius: 16px
    padding: "3vh 2.5vw"
    description: "Tall rounded-rectangle card in cream tone (one of three near-identical creams). Holds a large Lora serif title and a Jost body block at the bottom."
  stat-cell:
    borderTop: "1px solid {colors.ink-black}"
    padding: "{spacing.gap-md} {spacing.gap-md} {spacing.gap-md} 0"
    description: "Rule-topped vertical cell with a 5.5vw weight-200 numeral, a Jost label, and a mono source note."
  timeline-dot:
    width: 8px
    height: 8px
    borderRadius: 50%
    background: "{colors.ink-black}"
    border: "2px solid {colors.cream-warm}"
    description: "Solid black dot with a cream border ring that punches through a horizontal connector rule."
  vtimeline-spine:
    width: 1px
    background: "{colors.ink-black}"
    description: "1px vertical rule that anchors a vertical timeline. Carries a 9px solid black dot at the top of each entry."
  pie-donut:
    width: "min(26vw, 42vh)"
    height: "min(26vw, 42vh)"
    borderRadius: 50%
    description: "Donut ring rendered by overlaying a same-color circular ::after pseudo on a conic-gradient or similar. Center cutout is the slide background."
  pyramid-bar:
    borderLeft: "2px solid {colors.ink-black}"
    background: "color-mix(in srgb, {colors.ink-black} N%, {colors.cream-paper})"
    description: "Horizontal pyramid level. Width grows down each level (36% → 100%); fill darkens up the pyramid via color-mix at increasing percentages."
  bar-fill:
    width: "100%"
    background: "{colors.ink-graphite-light}"
    opacity: 0.5
    description: "Vertical bar in muted graphite at half opacity. Accented variant uses solid ink-black at full opacity."
  img-placeholder:
    border: "1px solid {colors.ink-black}"
    background: "{colors.cream-paper-3}"
    color: "{colors.ink-graphite}"
    description: "Hairline-bordered cream void with a centered mono label. Used until photography is dropped in."
---

## 概述

Monochrome（Ivory Ledger）是一套**文学编辑系统**，建立在单一材质约束上：奶油纸上的黑墨，别无其他。色板有八个 token，但其中七个是奶油或石墨的色调变体。没有色相强调——「强调」色只是更深的墨。结果是一套读成仔细排版的研究报告或安静当代专著的系统，不像演示文稿。

字体栈是三声部编辑配对。**Jost** 字重 200、300 和 400 承担每一个展示、标题、正文和标签——它的几何无衬线在超轻字重上保持平静，字重 200（展示）与字重 300（正文）之间的对比是系统的主排印节奏。**Lora** 斜体衬线留给两个特定时刻：引语正文和洞察卡片标题。斜体衬线提供系统里唯一的排印暖意——它出现的地方，就在发信号「这是人的声音」。**JetBrains Mono** 字重 400 承担每一个结构标记：铬件标签、侧栏标签、版本号、页脚文字、项目符破折号、坐标标签、日期。等宽是全大写，字距 0.12em 或更宽。

色板承担三种角色。**奶油纸**（`{colors.cream-paper}` 及其三个近乎相同的兄弟调）是画布——幻灯片从不是白，始终是暖偏黄奶油。**黑墨**（`{colors.ink-black}` —— 实际是 #1A1A16，非常深的橄榄黑）是每一个文字时刻、每一条边框、每一条分隔、每一个不是装饰奶油的形状填充。两种调的 **石墨**（`{colors.ink-graphite}` 做次级文本，`{colors.ink-graphite-light}` 做三级）处理弱化文案。那就是全部色彩系统。

纵深完全通过 **1px 发丝线** 和 **慷慨留白** 达成。没有投影、没有渐变、没有抬升、没有气氛效果。两块区域需要分隔时，一条 1px 黑线分开它们。一块区域需要视觉重量时，它得到更多内边距，而不是填充变化。洞察卡片表面与页面本身几乎无法区分——卡片由圆角和内边距定义，不是由对比跳跃定义。

**密度哲学：疏朗。** Ivory Ledger 在慷慨留白主导、单个排印时刻锚定这一页时读起来优雅。水平内边距设为 8vw（库里最慷慨的），内容通常只用画布中间 60–70%。一页用文字填满 80% 面积读成挤，并打破编辑阅读。系统在请代理留空间——让一条 Jost-200 标题撑起否则几乎空的一页。当需要密度时（研究时间线、两栏密文跨页、12 行表），系统仍能撑住，只因为字体如此轻、线条如此细，即使密内容也读成透气。

**关键特征：**
- 每一页奶油纸背景（`{colors.cream-paper}`）——从不是白，默认从不是深色。奶油是表面，不是风格选择。
- 超轻 Jost（展示字重 200，正文字重 300）是主导排印声音。
- Lora 斜体衬线出现在两个特定时刻：引语正文和洞察卡片标题。别无其他。
- JetBrains Mono 全大写、0.12em+ 字距处理每一个结构标签、铬件标记、坐标和项目符标记。
- 系统没有色相强调。强调色是 `{colors.ink-black}` —— 略深的墨。
- 所有结构分隔都是 1px 黑发丝线，加上用作小标点的签名 36px 短线（`{components.rule}`）。
- 项目列表标记是 JetBrains Mono 弱化石墨的 em 破折号。
- 慷慨的 8vw 水平内边距——模板库里最疏朗的。

## 色彩

### 色板

- **奶油纸**（`{colors.cream-paper}` — #FAFADF）：默认表面。暖偏黄，从不用纯白。每一页背景都是此色或近乎相同的变体。
- **奶油纸备用**（`{colors.cream-paper-2}` — #F2F2D2）：略深的奶油，用于内嵌表面。用得省——与默认奶油的差别几乎察觉不到。
- **深奶油纸**（`{colors.cream-paper-3}` — #F0F0D4）：图片占位填充。略更饱和的奶油，把空矩形与幻灯片表面区分开。
- **暖奶油**（`{colors.cream-warm}` — #F5F0E4）：洞察 / 时间线页背景，更暖的调，把这些页标成 deck 内相关的子审美时刻。
- **黑墨**（`{colors.ink-black}` — #1A1A16）：每一个文字时刻、每一条线、每一条分隔、每一条边框。非常深的橄榄黑，不是纯黑——为了在奶油纸上的暖意而选。
- **石墨墨**（`{colors.ink-graphite}` — #5E5E54）：次级文本色。用于弱化导语、密页上的正文段落，以及需要从标题重量后退的标签。
- **浅石墨墨**（`{colors.ink-graphite-light}` — #8A8A80）：三级文本。用于眉题、坐标标签、来源注、项目符标记、页脚铬件——任何应读成几乎不在场的结构元信息。

### 默认值

- **默认表面背景**：`{colors.cream-paper}`。系统默认单一表面。
- **默认主标题颜色**：`{colors.ink-black}`。标题从不用石墨或任何其他调。
- **默认正文颜色**：浅色页上的主文案用 `{colors.ink-black}`；弱化导语段落用 `{colors.ink-graphite}`。
- **默认眉题 / 标签颜色**：`{colors.ink-graphite-light}` —— 最弱的石墨。标签应往后退，不要带头。
- **默认边框 / 分隔颜色**：`{colors.ink-black}` —— 每一条分隔都是实心黑。没有弱化边框调。
- **默认线条粗细**：1px。系统从不用更粗的线。
- **默认「强调」色**：`{colors.ink-black}` —— 与主文本色相同。本系统的强调意味着更深的强调墨，不是色相切换。
- **洞察或时间线组的默认更暖表面处理**：`{colors.cream-warm}` —— 用来在色调上识别一组幻灯片，而不打破单色色板。

系统没有暖/冷配对，没有语义色（没有警告红、没有成功绿），没有色相强调。每一个强调都来自排印（尺寸、字重、斜体切换）或来自一条线，从不是来自颜色。

## 色彩（续）

三个「洞察卡片表面」（`--c-card-a`、`--c-card-b`、`--c-card-c`）都是近乎相同的奶油调（#FAFADF、#F5F0E4、#FAFADF）。它们是刻意塌掉的——卡片区分意在来自内边距和衬线标题，不是表面色。把三个卡片表面 token 当作实际上同一表面。

## 字体排印

### 字体家族

系统加载五套字体：**Jost**（字重 200、300、400、500、600）承担所有无衬线展示和正文；**Lora**（斜体和正体，字重 400、500、600）只承担引语文字和洞察卡片标题；**JetBrains Mono**（字重 300、400、500）承担每一个结构标签；**Noto Serif SC** 是 Lora 的中日韩回退；**Noto Sans SC** 是 Jost 的中日韩回退。

情感气质是刻意的：
- Jost 在字重 200 上读成**安静、几何、几乎数学**。它是系统的编辑声音。
- Lora 斜体读成**文学、个人、手排**。它发信号「这是人或引语的声音」——它出现的地方，语气从分析转到抒情。
- JetBrains Mono 读成**档案、索引、结构**。它是系统的目录卡声音——版本号、日期、坐标标签，任何是元信息而不是信息的东西。

### 字号阶梯

| Token | 字号 | 字体 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.display}` | 8.5vw | Jost | 200 | 封面或开场 hero 展示——慷慨而透气 |
| `{typography.h1}` | 5vw | Jost | 200 | 章节开场或分节标题 |
| `{typography.h2}` | 3.2vw | Jost | 300 | 主内容页标题 |
| `{typography.stat-value}` | 5.5vw | Jost | 200 | 数据单元格里的大数字 |
| `{typography.quote-serif}` | 3.2vw | Lora 斜体 | 400 | 引语正文 |
| `{typography.insight-serif}` | 2.8vw | Lora | 400 | 洞察卡片标题 |
| `{typography.h3}` | 2vw | Jost | 400 | 副标题、区域标题、流程步骤标题 |
| `{typography.lead}` | 1.5vw | Jost | 300 | 导语段落或大项目项 |
| `{typography.body}` | 1.1vw | Jost | 300 | 正文段落 |
| `{typography.caption}` | 0.85vw | Jost | 300 | 图片图注、来源注、细字 |
| `{typography.label}` | 0.72vw | JetBrains Mono | 400 | 眉题、铬件标签、坐标标签、版本标签 |
| `{typography.flow-num}` | 3.5vw | Jost | 200 | 流程图里的大步骤数字 |

### 默认值

- **默认主章节标题**：`{typography.h2}`（3.2vw，字重 300）。标准内容页不要伸手去 `{typography.h1}` —— 那个尺寸用于章节断开。
- **默认开场或封面展示**：`{typography.display}`（8.5vw，字重 200）。
- **默认正文段落字号**：`{typography.body}`（1.1vw，字重 300）。
- **默认导语段落字号**：当段落是标题下唯一的支撑块时，用 `{typography.lead}`（1.5vw，字重 300）。
- **默认标签 / 眉题字号**：`{typography.label}`（0.72vw）。
- **任何展示元素的默认字重**：200。Jost 200 是系统的展示声音。
- **正文默认字重**：300。

拿不准时，典范配对是标题用 `{typography.h2}`（字重 300）+ 支撑块用一段 `{typography.lead}`（字重 300）。窄字重落差（300 对 300，只靠尺寸区分）是正确的——Ivory Ledger 不靠重字重对比。

### 标志性处理

只要用到对应元素类型，这些处理就**不可省略**：

- **每一个 Jost display、h1、h2、h3 元素都是大小写混排**——从不全大写。全大写专属于 JetBrains Mono 标签。
- **每一个标签、眉题、铬件标记、页脚、坐标标签和来源注都用 JetBrains Mono 全大写，正字距至少 0.12em**（大多数是 0.14–0.18em）。这里不存在句首大写的等宽。
- **引语正文始终是 Lora 斜体。** Jost 里的引语读成另一套设计系统。
- **洞察卡片标题始终是 Lora 正体（不是斜体）。** 衬线字体是卡片的定义视觉信号。
- **项目列表标记始终是 JetBrains Mono 着色 `{colors.ink-graphite-light}` 的 em 破折号。** 从不用圆点，从不用勾，从不用数字。
- **数据值、展示标题和流程数字都用 Jost 字重 200、负字距。** 超轻字重加紧字距的组合是系统的展示签名。
- **标题和正文着色 `{colors.ink-black}`；弱化导语是 `{colors.ink-graphite}`；标签是 `{colors.ink-graphite-light}`。** 标题从不用石墨调。

### 排印原则

Ivory Ledger 的节奏是 **超轻 Jost + 两个特定时刻的 Lora 斜体 + 带字距的等宽标签**。把标题的 Jost 换成更重字重（500+）读成另一套系统。把正文设成 Lora 读成另一套系统。把标签设成 Jost 而不是 JetBrains Mono 读成另一套系统。每套字体的角色又窄又不动。

斜体只用于 Lora（引语正文），不用于 Jost。任何地方都不用下划线。不用加粗来强调正文——段落内强调要么靠 Lora 斜体切换（少见），要么靠留白隔离。

## 版式

### 画布系统

系统面向流体 `100vw × 100vh` 视口，所有尺寸用 `vw`/`vh`。deck 是水平 flex 条，页间转场 0.9s，平滑缓动曲线。动画 token（`fade-up`、`fade-in`、`reveal-right`、`reveal-left`、`scale-in`）可通过 `data-delay` 属性做交错延迟——这些在每一页入场时运行。

### 内边距与间隙阶梯

| Token | 取值 | 用途 |
|---|---|---|
| `{spacing.pad-x}` | 8vw | 幻灯片水平内边距（库里最慷慨的） |
| `{spacing.pad-y}` | 6vh | 幻灯片垂直内边距 |
| `{spacing.gap-lg}` | 5vh | 主要内容区块之间 |
| `{spacing.gap-md}` | 3vh | 相关元素之间 |
| `{spacing.gap-sm}` | 1.5vh | 紧密相关元素之间 |

幻灯片容器在左侧额外预留 3.5vw 给垂直侧栏元素（源里目前禁用——见已知缺口），所以总左内边距约 11.5vw。内容坐在这套慷慨的槽系统里。

### 铬件框

大多数内容页带 **chrome header** 和 **chrome foot**：每一条都是两个 JetBrains Mono 标签的 `flex space-between` 行，用 1px 实心黑线与幻灯片正文隔开。封面式、章节断开、引语和收场页类型完全抑制铬件和脚条。

### 已禁用的侧栏

CSS 定义了 `.slide-sidebar` 元素——左槽里一条细的 1px 黑垂直线，旋转等宽标签从下往上读。源明确用 `display: none !important` 禁用它，注释说它读成「视觉噪音」。样式仍作为休眠产物留在 CSS 里；没有有意的设计理由不要重新启用。

## 层次与纵深

### 无阴影，只有发丝线

系统在任何结构元素上都使用 **零 box-shadow 声明**。纵深通过三种机制创造：

1. **实心 `{colors.ink-black}` 的 1px 发丝线** —— 铬件带下、脚带上、对比面板之间、数据单元格上、时间线轨道上、图表基线上。线就是分隔、分隔器、结构标记。
2. **36px 短线**（`{components.rule}`）—— 用在章节标签下、眉题旁，或作精致强调断开的小标点。
3. **慷慨留白** —— 主纵深信号是 8vw 水平槽和每个排印时刻周围的空间。

### 无气氛效果

没有渐变、没有光晕、没有纹理、没有颗粒叠加。即使甜甜圈图中心挖空也只是铺在圆锥环上的同色圆——没有对比跳跃。

## 形状与处理

### 圆角

| 取值 | 用途 |
|---|---|
| 0px | 每一个结构元素——图片占位、数据单元格、对比面板、表格、图表区域 |
| 16px | 仅洞察卡片 |
| 50%（圆） | 饼/甜甜圈图形状、时间线点小圆、vt-spine 点 |
| 999px（胶囊） | 无——不用胶囊 |

系统以方角为主。洞察卡片上的 16px 圆角是唯一的结构软边，是把卡片与区域区分开的视觉信号。

### 边框粗细

- **1px solid `{colors.ink-black}`** —— 通用结构线粗细。用于每一条分隔、每一条铬件线、每一条图表坐标、每一个单元格边框。
- **2px solid `{colors.ink-black}`** —— 只用于金字塔柱左边缘（`{components.pyramid-bar}`），作为该特定图表类型略强的左锚。

没有更粗的边框重量，没有虚线边框（密图表内 `1px dashed` 石墨提示除外），没有上色边框。

### 装饰元素类型

**36px 短线** —— 小的 36px 宽 × 1px 高实心黑水平强调线。系统的签名标点。用在章节号下、眉题旁，或作精致区块断开。

**眉题 / 等宽眉毛** —— `{colors.ink-graphite-light}` 的弱化 JetBrains Mono 全大写标签，放在标题上方。眉毛按设计几乎不在场。

**描边标签** —— 带 1px 黑边框和 0.3em × 0.8em 内边距的小行内元素，内含等宽全大写字符串。用于版本标签或状态标签。

**项目符 em 破折号** —— JetBrains Mono 着色 `{colors.ink-graphite-light}` 的 `—` 字形，通过 CSS 网格标记列（`grid-template-columns: 1.2em 1fr`）前置到每个列表项。

**洞察卡片** —— 略暖奶油表面上的 16px 圆角矩形（`{components.insight-card}`）。带 Lora 正体标题（2.8vw 字重 400）和推到卡片底部的 Jost 正文块（字重 300）。卡片靠圆角和衬线标题识别，不是靠颜色对比。

**数据单元格** —— 带 1px 实心黑顶线的竖向区域（`{components.stat-cell}`），内含 5.5vw Jost-200 数字、Jost 标签，以及小等宽来源注。三格数据并排是典范排布。

**时间线点** —— 8px 实心黑圆，带 2px 暖奶油边框环（`{components.timeline-dot}`），穿过水平连接线。环色匹配暖奶油幻灯片表面，让点读成浮在线上，而不是穿过它。

**垂直时间线脊柱** —— 1px 宽垂直实心黑线（`{components.vtimeline-spine}`），每条条目顶部有 9px 实心黑点。用于长编年列表。

**饼 / 甜甜圈图** —— `min(26vw, 42vh)` 尺寸的圆（`{components.pie-donut}`），通过 `::after` 同色圆形挖空做成甜甜圈环。图表坐在图例列旁边。

**金字塔柱** —— 水平柱（`{components.pyramid-bar}`），2px 实心黑左边缘，通过 `color-mix(in srgb, ink-black N%, cream-paper)` 计算的奶油到石墨色调填充，N 在五层上从 4% 到 55%。宽度从 36%（顶，最深）步进到 100%（底，最浅）。

**垂直柱状图** —— 默认柱是 50% 不透明度的弱化石墨（`{colors.ink-graphite-light}`）；高亮柱是全不透明度实心黑柱。图表有 1px 黑左轴和 1px 黑基线。

**图片占位** —— 带 1px 边框的 cream-paper-3 矩形，居中等宽标签。直到摄影到达前使用。

**无箭头的流程** —— 本系统的流程图明确不在步骤之间用箭头。步骤之间的留白暗示顺序；系统用 CSS 里的注释声明这一点。

## 应做与不应做

### 应做
- 每一页都用奶油纸背景（`{colors.cream-paper}`）。单一表面画布是系统的地基。
- 每一条标题都设成 `{colors.ink-black}`，让字重（Jost 200）和尺寸做工作。标题从不需要色相切换。
- 任何展示时刻都用 Jost 字重 200。超轻字重是系统的定义排印声音。
- 只有当文字是引语正文时才伸手去 Lora 斜体；只有当它是洞察卡片标题时才伸手去 Lora 正体。衬线的两个角色不重叠。
- 每一个结构标签、坐标标记、页脚和项目符标记都用 JetBrains Mono 全大写、至少 0.12em 字距。等宽是目录卡声音。
- 每一个结构分隔都渲染为 1px 实心黑线。系统里没有更粗、没有弱化、没有虚线边框。
- 每一个项目列表都用 JetBrains Mono 弱化石墨的 em 破折号标记。
- 留下慷慨留白。内容应舒适地坐在画布中间 60–70%；把内容挤到边缘会打破编辑阅读。

### 不应做
- 不要引入色相颜色。红、蓝、绿、黄在本系统里不存在。强调是更深的墨。
- 不要用重字重（Jost 500、600、700）做标题。展示字重超过 300，系统读成坏掉。
- 不要把引语放进 Jost。Lora 斜体正文是引语的身份——换成无衬线会塌掉排印区分。
- 不要在任何元素上用 box-shadow。系统没有抬升。
- 不要用带色相对比的卡片表面。洞察卡片靠圆角和衬线标题识别；彩色填充会打破单色阅读。
- 不要挤一页。水平内边距是 8vw 是有原因的——内容需要呼吸。
- 不要用加粗来强调正文。行内强调很少；用时切到 Lora 斜体，不要加字重。
- 不要用圆点、勾、箭头或数字替代 em 破折号项目符标记。em 破折号是系统唯一的列表标记。
- 不要启用已禁用的侧栏（`.slide-sidebar`）。它是有意隐藏的——重新启用会加上系统被调校去掉的视觉噪音。
- 不要圆任何元素，洞察卡片（16px）或真正的圆（点、甜甜圈）除外。方角是结构默认。

## 响应行为

系统按设计是视口流体的。所有尺寸用 `vw`/`vh`，让同一构图在任何 16:9 视口上无需断点即可正确渲染。较小视口上，排印和内边距都线性缩放，所以视觉密度和负空间比保持恒定。

### 演示行为
- 标准键盘导航：箭头、空格、Home、End。
- 移动端触控滑动。
- 鼠标滚轮带防抖，防止连跳。
- 页间转场以 0.9s 平滑缓动曲线动画。
- 每一页可通过 `data-anim`（fade-up、fade-in、reveal-right、reveal-left、scale-in）在单个元素上声明入场动画，通过 `data-delay="N"` 做交错延迟，其中 N 映射到离散延迟步（0s、0.08s、0.18s、0.3s、0.44s、0.6s、0.78s、0.96s）。
- 带 `[data-anim]` 的元素开始时不可见（opacity:0），在 `.is-active` 上动画——再访问一页会重放入场。

### 打印行为
模板没有声明 `@media print` 规则。浏览器驱动的 PDF 导出只会捕捉活动页；多页导出需要逐页手工导航。

## 中日韩与国际内容

### 推荐中文搭配

| 角色 | 拉丁字体 | 中文字体 | 字重 |
|---|---|---|---|
| Display / headline（Jost 200） | Jost | Noto Sans SC（思源黑体） | 700（可用最重；中日韩 200 读成坏掉——见审美说明） |
| 正文 / 导语（Jost 300） | Jost | Noto Sans SC（思源黑体） | 400 |
| 引语 / 洞察标题（Lora 斜体 / 正体） | Lora | Noto Serif SC（思源宋体） | 400 |
| 标签 / 等宽铬件（JetBrains Mono） | JetBrains Mono | Noto Sans SC | 400（不要强迫中日韩用等宽；见审美说明） |

### 中西混排策略

策略 A —— 同一 `font-family` 栈，拉丁优先回退。每一个排印 token 已经列出 `"Jost, Noto Sans SC, system-ui, sans-serif"`（或 Lora 等价）。拉丁字形以 Jost / Lora 渲染；中日韩字形自动落到 Noto Sans SC / Noto Serif SC。不需要按语言的类。像 `使用 Claude 思考` 这样的混排句在一次逻辑运行里按文字系统用正确字体渲染。

### 加载

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Jost:wght@200;300;400;500;600&family=Lora:ital,wght@0,400;0,500;0,600;1,400;1,500&family=JetBrains+Mono:wght@300;400;500&family=Noto+Sans+SC:wght@300;400;500;700;900&family=Noto+Serif+SC:wght@400;500;700&display=swap" rel="stylesheet">
```

### 通用中日韩调整

- 行高：正文 1.75–1.85，展示 1.15–1.25
- 字距：中日韩为 0
- Text-transform：中日韩不要全大写
- 全角标点 （，。：；！？「」（））
- 展示标题不要句号（中文排印惯例）
- 盘古之白（中日韩与拉丁之间空格：`使用 Claude` 不是 `使用Claude`）
- 一句只用一套字体

### 本系统的审美说明

Ivory Ledger 的定义特质是字重 200 的 Jost——奶油上纸薄的几何笔画。**Noto Sans SC 没有可用的字重 200。** 它最轻的字重（300）仍比 Jost 200 读得更重，因为汉字每个字符笔画多得多。把中文展示设成 **Noto Sans SC 700**，以匹配 Jost 200 在奶油纸上的*视觉存在*（反直觉，但中文读者在大尺寸上会觉得更轻字重贫血）。正文用 Noto Sans SC 400 对 Jost 300 是正确匹配——奶油纸加石墨墨的时刻跨文字系统带过去。

Lora 斜体是系统在引语正文里的「人的声音」。**Noto Serif SC 没有斜体。** 中文引语完全丢掉斜体；衬线字体本身承担编辑暖意。不要用 `font-style: italic` 假装斜体——Noto Serif SC 会渲染自动倾斜的字形，看起来坏掉。

JetBrains Mono 的全大写带字距标签（0.12–0.18em）无法转到中日韩。**把中文标签设成 Noto Sans SC 400、大小写混排、字距重置为 0。** 中文里的「目录卡」声音通过小尺寸和奶油纸浅色达成，不是通过等宽 + 字距。若标签是纯拉丁（版本号、日期），按原设计保持 JetBrains Mono 全大写。

em 破折号项目符标记（`—`）在中文里完美工作——中文 em 破折号也是 `—`，渲染同样宽度。保持标记原样。

### 已知中日韩缺口

8vw 水平内边距（库里最慷慨的）是按拉丁更窄的字形宽度调的。汉字大致是方的，同一点尺寸下消耗更多水平空间。英文能一行放下的长中文标题可能折成两行。标题是纯中文时，把展示标题字号减约 15%（Jost 8.5vw → Noto Sans SC 7.2vw），或把折行当作编辑节奏的一部分接受。

## 迭代指南

1. 任何新幻灯片背景都是 `{colors.cream-paper}`（洞察/时间线子审美用 `{colors.cream-warm}`）。不要引入深色或色相背景。
2. 任何新标题都用大小写混排的 Jost，字重 200（display、h1）或 300（h2）。从不要伸手去更重字重。
3. 任何新标签、眉毛、标记或元信息文字都用 JetBrains Mono 全大写、至少 0.12em 字距，着色 `{colors.ink-graphite-light}`。
4. 任何新结构分隔都是 1px 实心黑线。装饰强调用 `{components.rule}`（36px 短），区域分隔用 `{components.rule-full}`。
5. 任何新引语都用 `{typography.quote-serif}` 字号的 Lora 斜体。引语从不以无衬线出现。
6. 任何新卡片时刻都用 16px 圆角和 Lora 正体标题。不要引入方角卡片或无衬线标题的卡片。
7. 任何新项目列表都用 JetBrains Mono 弱化石墨的 em 破折号。
8. 慷慨留白是功能，不是缺版式。不要因为空间在就填满它。
9. 若需要强调一个时刻，加大尺寸或用 Lora 斜体包一层 span。不要引入颜色。
10. 看起来像色相的颜色 token（例如 `--c-accent`）都别名到 `{colors.ink-black}` —— 它们为 token 兼容存在，但解析为黑。不要给它们加色相值。

## 已知缺口

- CSS 定义了 `.slide-sidebar` 元素（左槽里旋转的等宽标签），有意通过 `display: none !important` 隐藏。休眠样式仍留在源里；未经设计审查重新启用，会加上系统被调校去掉的视觉噪音。
- 三个洞察卡片表面 token（`--c-card-a`、`--c-card-b`、`--c-card-c`）解析为两个近乎相同的值（#FAFADF、#F5F0E4）。卡片「颜色变化」实际上是表面的——卡片靠衬线标题和内边距区分，不是表面调。
- 饼/甜甜圈图用 `::after` 伪挖空，要求图表背景匹配幻灯片表面。背景不同的幻灯片（例如暖奶油变体）需要调整 `--c-bg-light` token，挖空才能正确消失。
- 金字塔图使用 `color-mix(in srgb, ...)`，需要现代浏览器。较旧浏览器会把柱渲染成实心 `{colors.cream-paper}`。
- 动画系统需要给幻灯片加上 `.is-active` 类，入场动画才会播放。没有正确的导航引擎接线，`[data-anim]` 元素会保持 opacity 0。
- 大尺寸 Lora 斜体（3.2vw 引语正文）的笔画对比明显比周围 Jost 宽——这是刻意的，但会造成感知字重跳跃。不要通过把周围文字加重来补偿。
- 柱状图 `bar-fill` 使用内联 `style="height: XX%"` 声明——没有数据绑定层。高度是手工计算的。
- 系统在源注释里原名 "Ivory Ledger"。模板在库里以 "Monochrome" 暴露；两个名字指同一套设计系统。
