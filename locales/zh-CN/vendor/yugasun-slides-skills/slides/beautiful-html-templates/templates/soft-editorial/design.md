---
version: alpha
name: Soft Editorial
description: A warm magazine spread aesthetic — the kind of layout a small print quarterly with field-notes pretensions would commission. Cormorant Garamond carries every headline and ornamental moment with mixed roman and italic; Work Sans recedes into supporting body. The palette is cream paper with a quartet of pastel candy accents (dusty pink, chartreuse lemon, soft peach blush, sage green, lilac) used as colored card backgrounds. Generous rounded cards (24–36px radius) float on translucent white over the cream field. The mood is editorial calm with a sprinkling of riso-print color — closer to a literary research notebook than a corporate deck.

colors:
  paper: "#F2EEDF"
  paper-2: "#ECE6D2"
  ink: "#2A241B"
  ink-soft: "#5C5345"
  pink: "#E1A4C2"
  lemon: "#D6DD63"
  blush: "#E8C9B6"
  sage: "#B7C7A8"
  lilac: "#C9BEDC"
  card-fill: "rgba(255,255,255,0.55)"
  rule-soft: "rgba(42,36,27,0.18)"
  rule-medium: "rgba(42,36,27,0.35)"

color-aliases:
  background: paper
  text-primary: ink
  text-secondary: ink-soft

typography:
  display:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 232px
    fontWeight: 500
    lineHeight: 0.92
    letterSpacing: -0.02em
  title:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 188px
    fontWeight: 500
    lineHeight: 0.95
    letterSpacing: -0.015em
  closer:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 168px
    fontWeight: 500
    lineHeight: 0.95
    letterSpacing: -0.015em
  numeral-hero:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 320px
    fontWeight: 500
    lineHeight: 0.9
    letterSpacing: -0.02em
  numeral-lg:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 200px
    fontWeight: 500
    lineHeight: 0.9
    letterSpacing: -0.02em
  panel-headline:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 124px
    fontWeight: 500
    lineHeight: 0.98
    letterSpacing: -0.01em
  section-headline:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 96px
    fontWeight: 500
    lineHeight: 0.98
    letterSpacing: -0.01em
  page-headline:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 88px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: -0.01em
  quote-text:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 88px
    fontWeight: 500
    lineHeight: 1.05
    letterSpacing: -0.01em
  quote-mark:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 220px
    fontWeight: 500
    lineHeight: 0.7
    fontStyle: italic
  card-headline:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 72px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: -0.01em
  drop-cap:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 132px
    fontWeight: 500
    lineHeight: 0.85
  opener:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 56px
    fontWeight: 500
    fontStyle: italic
    lineHeight: 1.1
  numeral-step:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 92px
    fontWeight: 500
    fontStyle: italic
    lineHeight: 0.9
  numeral-card:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 64px
    fontWeight: 500
    fontStyle: italic
    lineHeight: 1
  subhead-lg:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 56px
    fontWeight: 500
    fontStyle: italic
    lineHeight: 1.1
  subhead-md:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 44px
    fontWeight: 500
    lineHeight: 1.05
  subhead-sm:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 38px
    fontWeight: 500
    lineHeight: 1.05
  kicker:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 38px
    fontWeight: 400
    fontStyle: italic
    lineHeight: 1.2
  marker:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 32px
    fontWeight: 400
    fontStyle: italic
    lineHeight: 1.3
  card-sub:
    fontFamily: "Work Sans, sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.1
  eyebrow:
    fontFamily: "Work Sans, sans-serif"
    fontSize: 28px
    fontWeight: 400
    letterSpacing: -0.005em
  page-marker:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 26px
    fontWeight: 400
    fontStyle: italic
  footer:
    fontFamily: "Cormorant Garamond, Garamond, serif"
    fontSize: 26px
    fontWeight: 400
    fontStyle: italic
  body:
    fontFamily: "Work Sans, sans-serif"
    fontSize: 26px
    fontWeight: 400
    lineHeight: 1.5
  body-md:
    fontFamily: "Work Sans, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.5
  attr:
    fontFamily: "Work Sans, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
  swatch-label:
    fontFamily: "Work Sans, sans-serif"
    fontSize: 11px
    fontWeight: 400
    letterSpacing: 0.06em
    textTransform: uppercase

spacing:
  pad-outer: 80px
  pad-top: 60px
  pad-bottom: 50px
  card-pad-lg: "64px 48px"
  card-pad-md: "48px 52px"
  card-pad-sm: "28px 30px"
  gap-cards: 28px
  gap-cards-lg: 36px
  gap-stack: 36px

canvas:
  width: 1920px
  height: 1080px

components:
  card-soft:
    background: "{colors.card-fill}"
    borderRadius: "24px to 36px"
    padding: "{spacing.card-pad-sm} to {spacing.card-pad-lg}"
    description: "Translucent white card floating on the cream field. The system's default container — used for stats, columns, panels, content blocks."
  card-color:
    background: "any of pink, lemon, blush, sage, lilac"
    borderRadius: "22px to 36px"
    padding: "{spacing.card-pad-sm}"
    description: "Saturated pastel card containing numerals, step content, or featured items. Text stays ink/ink-soft on every accent fill — never inverted."
  pill:
    borderRadius: "999px"
    padding: "4px 14px"
    fontWeight: 500
    description: "Status pill in a pastel fill (lemon=yes, blush=partial, pink=no) or translucent white with a soft border for notes."
  swatch-dot:
    width: 56px
    height: 56px
    borderRadius: "50%"
    description: "Circular accent disc shown in a row at the top of cover slides — the visual signature of the system's color palette."
  swatch-tile:
    aspectRatio: "1/1.2"
    borderRadius: "16px"
    description: "Rounded rectangle paint chip used in palette displays and design-system layouts."
  rule-dashed:
    borderColor: "{colors.rule-soft}"
    borderStyle: "dashed"
    borderWidth: "1px"
    description: "1px dashed warm-ink hairline used inside matrix tables, panel dividers, and any subdivision that wants to read softer than a solid rule."
  rule-solid:
    borderColor: "{colors.rule-medium}"
    borderStyle: "solid"
    borderWidth: "1.5px"
    description: "Slightly heavier hairline for major dividers inside cards (head-row underlines, column rules)."
  drop-cap:
    typography: "{typography.drop-cap}"
    float: "left"
    description: "First letter of an opener paragraph floats left at ~132px, line-height 0.85, with 8px 14px 0 0 padding. The visible signature of editorial reads."
  legend-bar:
    width: 28px
    height: 12px
    borderRadius: "6px"
    description: "Rounded color bar used as a chart legend swatch."
  marker-rule:
    width: "auto"
    borderTop: "1px dashed {colors.rule-soft}"
    description: "Dashed top-rule used to mark source attributions or sign-offs beneath content."
  action-bar:
    background: "{colors.lemon}"
    borderRadius: "24px"
    padding: "24px 36px"
    description: "Lemon-yellow action band running near the top of a slide, containing a tag separator and a serif headline — used for important CTAs or callouts."
  chrome-eyebrow:
    position: "absolute top-left at 60px / 80px"
    typography: "{typography.eyebrow}"
    color: "{colors.ink}"
    description: "Section name in plain sans, sits at the top-left corner of standard slides."
  chrome-pagedot:
    position: "absolute top-right at 60px / 80px"
    typography: "{typography.page-marker}"
    color: "{colors.ink-soft}"
    description: "Roman or arabic page numeral in italic serif at the top-right corner."
  chrome-footer:
    position: "absolute bottom at 50px"
    typography: "{typography.footer}"
    color: "{colors.ink-soft}"
    description: "Two-column italic serif footer running across the bottom — date left, publication name right."
---

## 概览

Soft Editorial 是一套**温暖杂志跨页**演示系统，视觉线索来自小出版社文学季刊与设计研究笔记。前提是单一字体（Cormorant Garamond）几乎包办所有说话，只在衬线会显得累的地方，才用克制的人文无衬线（Work Sans）托底。奶油纸底是常量——每页都落在 `{colors.paper}`（#F2EEDF）上，这是温暖的陈年奶油色，读起来像实体纸，不是屏幕白。纸底之上，圆角卡片分两档漂浮：半透明白色柔软底用于默认内容，饱和的糖果粉彩用于强调瞬间。

字体系统是**单字族、混用样式**。标题用 Cormorant Garamond medium（字重 500），但罗马体标题句中常带一个 `<em>`，切到斜体且字重 400——斜体短语是同一字族更轻的一档，赋予系统标志性的「轻柔强调」语气。斜体也跑在小型装饰文字上（kicker、marker、页码、落款、开篇段落、步骤数字）。Work Sans 只在正文段落、eyebrow，以及一小套元标签里出场——那些地方衬线的个性会过满。

色彩哲学是**奶油底加五种粉彩**。粉彩——雾粉（`{colors.pink}`）、黄绿色柠檬（`{colors.lemon}`）、柔桃 blush（`{colors.blush}`）、鼠尾草绿（`{colors.sage}`）、丁香紫（`{colors.lilac}`）——可互换作为卡片填色。它们都不背固定语义角色（lemon 不是「警告」，pink 不是「错误」）。它们是色料——整套片子会轮换它们求变化，常常一页上同时看见三四种。每种粉彩表面上的文字都保持 `{colors.ink}`（偏暖的近黑，#2A241B）。系统从不在强调表面上反白文字。

层次来自**柔软圆角卡片**：默认卡片圆角很大（24–36px；pill 可到 999px），半透明白填色略高于奶油底。没有投影——层次靠半透明与圆角形态暗示。卡片内的发丝线是低不透明的暖墨水虚线，强化「笔记本」感。

**密度哲学：卡片内中高密度，卡片之间留足气口。** 卡片本身可以装大量内容——多列矩阵、密的步骤网格、较长引文。但画布在它们周围留出舒服的空气：80px 外边距、卡片间距 28–36px、奶油底大量露出来。这套系统里「坏掉」的一页，要么是 (a) 卡片挤在一起没有呼吸场，要么是 (b) 稀疏到纸底读成空，而不是刻意留白。目标是「慷慨排过的杂志页：卡片成组、呼吸、带路」。

**关键特征：**
- 每页同一块温暖奶油表面（`{colors.paper}`）；粉彩只作为卡片填色出现，从不做幻灯片背景（唯一例外是全出血 closer 页用 `{colors.pink}` 铺满）。
- Cormorant Garamond 承担所有 display、标题、kicker 与装饰瞬间；Work Sans 留给正文和 eyebrow。
- 标题内罗马体 + 斜体混排是系统的字体信号——斜体短语从标题的字重 500 降到 400。
- 饱和粉彩（`{colors.pink}`、`{colors.lemon}`、`{colors.blush}`、`{colors.sage}`、`{colors.lilac}`）是可互换的卡片填色，没有固定语义。
- 圆角卡片（半径 24–36px）是默认容器；pill 全圆（999px）；半透明白（`{colors.card-fill}`）是默认卡片填色。
- 没有投影。层次来自奶油底上的半透明，以及卡片的圆角 chrome。
- 页框是斜体衬线（页码与页脚）加纯无衬线（eyebrow）——从不用等宽，从不用全大写。
- 长文开篇段落开头有首字下沉，约 132px Cormorant Garamond medium。

## 颜色

### 色板

- **Paper**（`{colors.paper}` — #F2EEDF）：奶油纸页。默认幻灯片背景，整套片子的常量。温暖、陈年，从不刺亮。
- **Paper Alt**（`{colors.paper-2}` — #ECE6D2）：略冷一点的奶油色，留给相邻表面的分离。用得很少；许多片子根本用不到。
- **Ink**（`{colors.ink}` — #2A241B）：偏棕的暖近黑。每种表面上的主文字色——从不是纯黑。
- **Ink Soft**（`{colors.ink-soft}` — #5C5345）：闷的暖灰棕。次级文字——说明、导语、描述、页码、落款。
- **Pink**（`{colors.pink}` — #E1A4C2）：雾玫瑰色粉彩。用得最多的强调填色——封面色点、步骤卡片、全出血 closer 页、状态 pill（在矩阵里读成「否」）。
- **Lemon**（`{colors.lemon}` — #D6DD63）：黄绿色。最亮的强调——用于英雄数字卡片、行动条、「是」pill。
- **Blush**（`{colors.blush}` — #E8C9B6）：柔桃色。粉彩里最中性的——用于步骤卡片、「部分」pill，以及任何需要温暖中性的槽位。
- **Sage**（`{colors.sage}` — #B7C7A8）：闷绿。为变化而加入的「额外」强调——流程图、设计系统网格、次级步骤卡片。
- **Lilac**（`{colors.lilac}` — #C9BEDC）：柔紫灰。sage 的冷对位——多半出现在五种粉彩轮换的五步流程里。
- **Card Fill**（`{colors.card-fill}` — rgba(255,255,255,0.55)）：半透明白。默认卡片背景——坐在奶油底上，像「抬起」的表面，却不承诺饱和色。
- **Rule Soft**（`{colors.rule-soft}` — rgba(42,36,27,0.18)）：低不透明暖墨，用于内部虚线发丝。
- **Rule Medium**（`{colors.rule-medium}` — rgba(42,36,27,0.35)）：略重的发丝，用于卡片内主要分割。

### 默认值

- **默认幻灯片背景**：`{colors.paper}` —— 每一页标准页。
- **默认主文字色**：`{colors.ink}` —— 每种表面，包括所有粉彩卡片。文字从不在粉彩填色上反白。
- **默认次级文字色**：`{colors.ink-soft}` —— 用于描述、导语段落、说明、页码、落款。
- **默认卡片填色**：`{colors.card-fill}` —— 半透明白。内容容器不需要饱和色时，就用这个。
- **默认强调卡片填色（需要时）**：最暖的瞬间用 `{colors.pink}`，最亮用 `{colors.lemon}`，中性温暖用 `{colors.blush}`，冷静变化用 `{colors.sage}`，五宫格第五格用 `{colors.lilac}`。
- **默认标题色**：`{colors.ink}`。
- **默认 eyebrow 色**：`{colors.ink}`（eyebrow 是左上页框标签）。
- **默认页脚色**：`{colors.ink-soft}`。

粉彩不背语义。在矩阵版式里，惯例是 lemon = 正面 / 部分 / 是；blush = 部分；pink = 负面 / 否。矩阵之外，任何粉彩都可以填任何卡片，不传达状态。

## 字体

### 字族

Soft Editorial 用**两个字族**，角色仔细分开：

- **Cormorant Garamond**（`{typography.display.fontFamily}`）——精致的旧式衬线，斜体轴非常有表现力。承担每个尺度的标题（display、title、closer、page-headline、card-headline、所有副标题）、每个数字、每条引语、每个 kicker、每个装饰 marker、每个页码、每个页脚、每个首字下沉。这套字的斜体细腻、私人，系统用得很慷慨——斜体承担 kicker、marker、页码、页脚、步骤数字、落款，以及标题里的任何 `<em>`。
- **Work Sans**（`{typography.body.fontFamily}`）——人文 grotesk。留给正文段落、eyebrow、卡片副标签、署名，以及 Work Sans 专属标签（色板展示里小号全大写 swatch-label）。Work Sans 从不承担标题。

系统的字体信号是**同一标题内混用字重**：字重 500 的衬线标题带着一个降到字重 400（斜体）的 `<em>`。字重差是轻柔的——读成软化，不是加粗强调。这与杂志里「斜体当加粗」的惯例相反；这里斜体是更轻、更亲密的语气。

### 字号阶梯

| Token | 字号 | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.numeral-hero}` | 320px | Cormorant Garamond | 500 | 跨两栏统计卡片里的英雄数字 |
| `{typography.display}` | 232px | Cormorant Garamond | 500 | 封面尺度的 display 标题 |
| `{typography.numeral-lg}` | 200px | Cormorant Garamond | 500 | 独立的大号统计数字 |
| `{typography.title}` | 188px | Cormorant Garamond | 500 | 接近封面尺度的章节标题 |
| `{typography.closer}` | 168px | Cormorant Garamond | 500 | 全出血彩色页上的收束或「瞬间」标题 |
| `{typography.panel-headline}` | 124px | Cormorant Garamond | 500 | 填满两栏版式其中一栏的标题 |
| `{typography.section-headline}` | 96px | Cormorant Garamond | 500 | 图表、对照或分析区标题 |
| `{typography.numeral-step}` | 92px | Cormorant Garamond italic | 500 | 步骤卡片上的斜体序数（i.、ii.、iii.） |
| `{typography.page-headline}` | 88px | Cormorant Garamond | 500 | 流程图或一般页标题 |
| `{typography.quote-text}` | 88px | Cormorant Garamond | 500 | 引语正文 |
| `{typography.card-headline}` | 72px | Cormorant Garamond | 500 | 填满方形强调卡片头部的标题 |
| `{typography.numeral-card}` | 64px | Cormorant Garamond italic | 500 | 较小条目卡片上的斜体序数 |
| `{typography.opener}` | 56px | Cormorant Garamond italic | 500 | 序言 / 长文阅读的斜体开篇段落 |
| `{typography.subhead-lg}` | 56px | Cormorant Garamond italic | 500 | 用于成对栏开篇的斜体大副标题 |
| `{typography.subhead-md}` | 44px | Cormorant Garamond | 500 | 卡片或栏标题 |
| `{typography.subhead-sm}` | 38px | Cormorant Garamond | 500 | 面板内副标题；列表里的条目标题 |
| `{typography.kicker}` | 38px | Cormorant Garamond italic | 400 | 封面标题上方的斜体 kicker |
| `{typography.card-sub}` | 32px | Work Sans | 500 | 衬线卡片标题下方的副标签（唯一的无衬线副标题） |
| `{typography.marker}` | 32px | Cormorant Garamond italic | 400 | 斜体 marker 文字（落款、版本标签、「vol. iii」） |
| `{typography.eyebrow}` | 28px | Work Sans | 400 | 标准页左上的纯无衬线章节名 |
| `{typography.page-marker}` | 26px | Cormorant Garamond italic | 400 | 右上的罗马或阿拉伯页码 |
| `{typography.footer}` | 26px | Cormorant Garamond italic | 400 | 斜体衬线页脚行（日期、刊名） |
| `{typography.body}` | 26px | Work Sans | 400 | 默认段落正文 |
| `{typography.body-md}` | 24px | Work Sans | 400 | 卡片正文、列表条目正文、卡片内密段落 |
| `{typography.attr}` | 24px | Work Sans | 500 | 引语署名 |
| `{typography.drop-cap}` | 132px | Cormorant Garamond | 500 | 长文开篇段落开头的首字下沉 |
| `{typography.swatch-label}` | 11px | Work Sans uppercase | 400 | 色块磁贴内的小号全大写标签（色板展示） |

### 默认值

- **主章节标题默认字号**：标准页用 `{typography.section-headline}`（96px）；标题填满两栏之一时用 `{typography.panel-headline}`（124px）。
- **封面或章节标题默认字号**：`{typography.title}`（188px）到 `{typography.display}`（232px）。
- **段落正文默认字号**：开放页用 `{typography.body}`（26px）；卡片内或更密的栏用 `{typography.body-md}`（24px）。
- **kicker 或 marker 默认字号**：封面 kicker 用 `{typography.kicker}`（38px）；更小的装饰注记用 `{typography.marker}`（32px）。
- **主打统计数字默认字号**：`{typography.numeral-lg}`（200px）；只有一个数字主宰版式时才用 `{typography.numeral-hero}`（320px）。
- **步骤或条目数字默认字号**：完整步骤卡片用 `{typography.numeral-step}`（92px），较小条目用 `{typography.numeral-card}`（64px）。
- **默认标题字重**：500（medium）。内部斜体 `<em>` 降到 400。
- **默认标题色**：`{colors.ink}`。

一页的主瞬间拿不准字号时，用 `{typography.section-headline}`（96px）——这是编辑阅读的主力尺寸。

### 标志性处理

只要用到对应元素类型，这些处理就是**不可省略的**：

- **每个含强调短语的标题，把 `<em>` 渲染成斜体 Cormorant Garamond、字重 400**（周围标题跑字重 500）。斜体字重下降是系统的主字体信号。
- **所有页框（eyebrow、page-marker、footer）用绝对定位、固定偏移**（eyebrow 左上 60/80px；pagedot 右上 60/80px；footer 左右 80px / 底 50px）。标准页上页框位置不可商量。
- **Eyebrow 是纯 Work Sans、28px**，不斜体、不全大写。它们是唯一的无衬线页框元素。
- **页码与页脚是斜体衬线、26px，色为 `{colors.ink-soft}`。** 从不是无衬线，从不是全大写，从不是加粗。
- **步骤数字是斜体衬线小写罗马数字（i.、ii.、iii.、iv.、v.）**——从不是阿拉伯数字，从不是大写。罗马数字属于编辑语域。
- **开篇段落的首字下沉是 Cormorant Garamond、字重 500、约 132px，行高 0.85，内边距 `8px 14px 0 0`。** 规格不是这个，读成另一套系统。
- **卡片圆角始终在 22–36px 范围**（pill 为 999px）。这套系统里不存在方角卡片。

### 排印原则

衬线 / 无衬线分工是结构的：Cormorant Garamond 承担个性（每个标题、每个数字、每处装饰），Work Sans 承担实质（每个段落、每个 eyebrow、每个仅 Work Sans 的标签）。跨轨会打破编辑的平静。

斜体是慷慨的，不是珍藏的。斜体衬线出现在 kicker、marker、页码、页脚、步骤数字、开篇段落、标题 `<em>` 短语，以及任何小型装饰瞬间。无衬线从不斜体——Work Sans 应始终直立。

行高在 display 尺度收紧（0.9–0.98），在正文与卡片正文放开到 1.4–1.55。字距在最大号上略负（–0.01 到 –0.02em），正文为零或近零。11px 的 Work Sans swatch-label 是系统里唯一全大写元素——并带慷慨的 0.06em 字距，让 11px 仍可读。

## 版式

### 画布系统

Soft Editorial 目标是经由 `<deck-stage>` 元素的**固定 1920×1080 画布**。版式从幻灯片边缘做绝对定位——每个元素都用 `position: absolute`，相对幻灯片用 `top`/`left`/`right`/`bottom` 偏移。系统不用视口相对单位；靠 deck-stage 的缩放处理视口差异。

### 内边距与间距阶梯

| Token | 值 | 用途 |
|---|---|---|
| `{spacing.pad-outer}` | 80px | 内容块标准左右内缩 |
| `{spacing.pad-top}` | 60px | eyebrow / pagedot 页框的上内缩 |
| `{spacing.pad-bottom}` | 50px | 页脚页框的下内缩 |
| `{spacing.card-pad-lg}` | 64px 48px | 宽敞卡片的内边距（insights、closer） |
| `{spacing.card-pad-md}` | 48px 52px | 中等卡片的内边距（下一步面板） |
| `{spacing.card-pad-sm}` | 28px 30px | 紧凑卡片的内边距（栏、设计系统磁贴） |
| `{spacing.gap-cards}` | 28px | 行或网格中卡片的标准间距 |
| `{spacing.gap-cards-lg}` | 36px | 主要面板之间更大的间距 |
| `{spacing.gap-stack}` | 36px | 堆叠文字元素之间的垂直间距 |

### 页框

每页标准幻灯片在固定位置带三个页框元素：

- **Eyebrow** —— 左上章节名（距顶 60px、距左 80px），Work Sans 28px，色为 `{colors.ink}`。
- **Pagedot** —— 右上页码（距顶 60px、距右 80px），斜体 Cormorant Garamond 26px，色为 `{colors.ink-soft}`。
- **Footer** —— 底部两栏页脚（距底 50px、左右各 80px），斜体 Cormorant Garamond 26px，色为 `{colors.ink-soft}`（日期在左，刊名在右）。

封面页把 pagedot 换成右上三枚圆形粉彩色点（整套色板的视觉签名）。全出血强调页（closer）在彩色场上把页框改成深墨，位置保持不变。

## 层次与抬升

Soft Editorial **不用投影**。层次完全来自半透明与圆角形态：

- **半透明白卡片** —— `{colors.card-fill}`（rgba 255,255,255,0.55）——坐在奶油底上。半透明让暖纸透出来，卡片感觉「抬起」，却没有任何影子。
- **饱和粉彩卡片** —— pink、lemon、blush、sage、lilac 填色 —— 以全不透明坐在奶油底上。卡片与纸底的视觉差是颜色，不是抬升。
- **圆角** —— 每张卡片都有慷慨圆角（22–36px），软化形态，读成「实体卡片」而不是「屏幕矩形」。

没有第二层抬升。卡片不叠卡片。版式需要视觉层级时，用尺寸和颜色，不用 z 轴堆叠。

## 形状与处理

### 圆角

| 值 | 用途 |
|---|---|
| 999px（pill） | 状态 pill（是 / 部分 / 否 / 注） |
| 36px | 大 insight 卡片、closer 卡片 |
| 32px | 方法步骤卡片 |
| 28px | 条目卡片、流程节点、图表外框 |
| 24px | 默认面板卡片、咨询栏、设计系统磁贴、行动条 |
| 22px | 设计系统网格里较大的系统磁贴 |
| 18px | 装饰时间条 |
| 16px | 色板色块磁贴 |
| 14px | 设计系统网格里最小的装饰碎片 |
| 6px | 图例色条（扁平圆角条） |
| 50%（圆） | 封面色点 |

系统里**没有方角**。每个容器至少 14px 圆角；卡片 22–36px 圆角；pill 全圆。

### 描边粗细

- **标准卡片没有实线描边**。卡片的背景与圆角形态提供轮廓。
- **1px 虚线**，色为 `{colors.rule-soft}`（rgba 42,36,27,0.18）——表格单元格、矩阵分割、来源行标记、系统磁贴分隔的内部发丝。
- **1.5px 实线**，色为 `{colors.rule-medium}`（rgba 42,36,27,0.35）——矩阵表头下划线、栏标题线等更重的分割。
- **1px 实线**，类似低不透明墨水——用于图表绘图边缘和一小套「注」pill。

### 装饰元素类型

**软卡片** —— 默认内容容器。半透明白卡片，圆角 24–36px，内边距 28–64px。作为抬起区域坐在奶油底上。

**彩色卡片** —— 饱和粉彩卡片（pink、lemon、blush、sage、lilac），圆角 22–36px。用于统计、步骤卡片、insight 卡片，以及任何想要颜色的瞬间。内部文字保持 ink / ink-soft —— 从不反白。

**状态 pill** —— 全圆 999px 半径的 pill，衬线 / 无衬线内容混用。粉彩填色（lemon、blush、pink）表示肯定 / 部分 / 否定状态；半透明白加 1px 墨水描边表示「注」。

**行动条** —— 全宽柠檬填色圆角卡片（半径 24px）横贯幻灯片顶部，含标签分隔结构与衬线标题。用于 callout、CTA 或抢注意的元瞬间。

**封面色点行** —— 3–5 枚直径 56px 的圆形色点，按片子强调色板排列，放在封面右上。系统色彩哲学的视觉签名。

**首字下沉** —— 132px Cormorant Garamond medium 的首字母，在开篇段落开头向左浮动，内边距 8px 14px 0 0。系统里最编辑的字体瞬间。

**斜体步骤数字** —— 斜体 Cormorant Garamond 罗马数字（i.、ii.、iii.），64–92px，坐在步骤卡片顶部，下方是衬线标题与无衬线正文。步骤必须用罗马数字。

**引号** —— 单个斜体 Cormorant Garamond `"`，220px，色为 `{colors.blush}`，坐在居中引语上方。引号的颜色本身就是信号——柔桃，不是 ink。

**图例条** —— 28px × 12px、端头圆角（半径 6px）的水平条，用图表强调色，配标签。

**来源行** —— 栏或面板底部的虚线上规则斜体衬线行，标记来源署名或落款。

## 该做与不该做

### 该做

- 每个标题用 Cormorant Garamond 字重 500，内部斜体 `<em>` 短语降到字重 400。字重下降是系统的声音。
- 每页标准幻灯片背景设为 `{colors.paper}` —— 温暖奶油底是常量。
- 默认卡片用半透明白（`{colors.card-fill}`），圆角 24–36px。需要颜色或状态时再拿粉彩填色，不是默认。
- 每种表面上的文字保持 `{colors.ink}`，包括所有粉彩卡片。系统从不在粉彩上反白。
- 用斜体衬线（Cormorant Garamond italic）做 kicker、marker、页码、页脚、步骤数字、落款，以及任何小型装饰瞬间。
- 长文阅读的开篇段落加首字下沉 —— 132px Cormorant Garamond medium，行高 0.85，内边距 8px 14px 0 0。
- 步骤序数用罗马数字（小写斜体：i.、ii.、iii.）。阿拉伯步骤数字会打破编辑语域。
- 每个页码渲染成斜体 Cormorant Garamond、26px，色为 `{colors.ink-soft}`，绝对定位在右上。
- Work Sans 只用于正文、eyebrow、署名和小号全大写 swatch-label。Work Sans 从不承担标题。
- 幻灯片用 80px 外内缩，卡片之间留 28–36px 间距。卡片周围呼吸的奶油底是设计的一部分。

### 不该做

- 不要用粉彩铺满幻灯片背景——粉彩是卡片填色（一个例外：全出血 closer 页可以整场粉红，做一个「瞬间」）。默认页留在奶油底上。
- 不要在粉彩卡片上把文字反白。文字始终是墨在色上。
- 不要给任何卡片或容器用方角。可接受的最小半径是 14px；卡片活在 22–36px。
- 不要加投影。系统的层次来自半透明与形态，不是抬升。
- 不要用第三套字体。Cormorant Garamond 与 Work Sans 是仅有的字族。加 display 字体或等宽会打破编辑语域。
- 不要在正文里加粗。正文需要强调时，切到斜体衬线，或在 Work Sans 里用字重 500 的 strong 标签（少见）。
- 不要用罗马体衬线渲染 kicker、marker 或页脚。装饰性小字始终是斜体。
- 不要在 11px swatch-label 之外用全大写。系统通篇是句首大写。
- 不要用等宽。这套系统没有等宽——每个标签是无衬线或斜体衬线。
- 不要把卡片挤到边贴边。28–36px 间距和卡片周围的奶油底是承重的。

## 响应式行为

Soft Editorial 是在 `<deck-stage>` web component 里渲染的**固定 1920×1080** 系统。deck-stage 负责缩放：幻灯片内容按精确 1920×1080 像素排好，组件把整座舞台缩放到视口（按 stage 配置做 letterbox 或适配）。幻灯片内所有 `top`/`left`/`right`/`bottom`/`width`/`height` 值都是像素，并假定固定 1920×1080 画布。

### 缩放行为

因为 deck-stage 均匀缩放，所有元素在任何输出视口都保持相对位置和尺寸。232px 的 display 标题在 deck-stage 内部画布上仍是 232px；舞台把整块画布缩放到浏览器视口。

### 演示行为

导航由 `deck-stage.js` 脚本处理（外部依赖，不内嵌）。每页带 `data-label` 属性，在演示 UI 里标识自己。翻页走 deck-stage 自己的控件。

### 打印行为

没有内嵌打印样式表。静态导出取决于 deck-stage 组件的打印 / 导出行为；生成 PDF 时，deck-stage 应把每页渲染成一张 1920×1080 画布尺寸的单页。

## 中日韩与国际内容

### 推荐中文字体搭配

| 角色 | 拉丁字体（默认） | 中文字体 | 字重 | 说明 |
|---|---|---|---|---|
| Display / 标题 | Cormorant Garamond 500 | 霞鹜文楷 LXGW WenKai（LXGW WenKai TC） | 400 | LXGW WenKai 是带手写感的楷体，镜像 Cormorant 的文学语域。单一 regular 字重对上 Cormorant 的轻柔 medium。 |
| 斜体强调（`<em>`） | Cormorant Garamond italic 400 | 霞鹜文楷 LXGW WenKai | 400 | LXGW WenKai 没有真正斜体——强调改为降到 `{colors.ink-soft}` 或淡下划线。不要合成斜体。 |
| 正文 | Work Sans 400 | 思源宋体 / Noto Serif SC | 400 | 中日韩正文从无衬线切到衬线，以保住文学语域；Work Sans 挨着楷体标题会丢掉编辑的平静。 |
| 正文 — 备选无衬线（可选） | Work Sans 400 | Noto Sans SC | 400 | 仅当片子数据极密时使用；默认用 Noto Serif SC。 |
| Kicker / marker / 页码 | Cormorant Garamond italic 400 | 霞鹜文楷 LXGW WenKai 400 | 400 | 斜体装饰变成直立楷体；靠 `{colors.ink-soft}` 的颜色偏移代替斜体，保留同样的「软装饰」感。 |

### 混排策略

本模板用 **Strategy C（文学）**：英文字形保留拉丁字体，中文字符出现时才经层叠 `font-family` 落入中日韩回退。Cormorant Garamond 是 Soft Editorial 品牌身份的一部分——每个标题都换成楷体会剥掉旧式衬线个性。拉丁留在 Cormorant、中文落入 LXGW WenKai，两边语域都保住。

```css
font-family: 'Cormorant Garamond', 'LXGW WenKai TC', 'Noto Serif SC', serif;  /* headlines */
font-family: 'Work Sans', 'Noto Serif SC', sans-serif;                          /* body */
```

**警告——display 尺寸上的基线错位。** Cormorant Garamond 的 x-height 明显低于 LXGW WenKai 的视觉中心。在 96px+ 标题上，像 `Soft Editorial 软编辑` 这样的短语会让中文字略浮在拉丁基线之上。缓解办法：
- 在中文片段上加 `font-feature-settings: "palt"` 收紧度量。
- 用 `<span lang="zh">` 包住中日韩，并在 display token（display、title、closer、numeral-hero、panel-headline）上做小幅 `vertical-align: -0.04em` 调整。
- 纯中文标题（无拉丁）时问题消失——错位只出现在混排行。

### 加载

加入 `<head>`（Google Fonts 托管 LXGW WenKai TC 与 Noto Serif SC）：

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400;1,500&family=Work+Sans:wght@400;500&family=LXGW+WenKai+TC&family=Noto+Serif+SC:wght@400;500;700&display=swap" rel="stylesheet">
```

LXGW WenKai TC 是 Google Fonts 上的繁体切割；它覆盖完整 CJK Unified Ideographs 范围，简体也干净。Noto Serif SC 用正确 hinting 承载简体正文。

### 通用中日韩调整

凡渲染中文内容的元素都要应用（通常用 `:lang(zh)` 或 `<span lang="zh">` 限定范围）：

- **行高**：正文 1.75–1.85（Soft Editorial 的 1.5 无衬线默认对中日韩笔画需要更多气口）；display 1.15–1.25（比拉丁 0.92–1 更松，因为中日韩字形已含固有间距）。
- **字距**：中日韩为 0。系统在 display 拉丁上的负 tracking（-0.01 到 -0.02em）对中文是错的——中日韩字形预留了间距；负 tracking 会造成重叠。
- **text-transform**：中日韩不要全大写。中文没有大小写，CSS `text-transform: uppercase` 对汉字也是空操作，但要确保没有父规则去尝试它。
- **全角标点**：用 `，。：；！？`（全角），不用 `,.:;!?`（半角）。全角形态自带周围空白，并对齐中日韩 em 盒。
- **display 标题不加句号**：中文标题去掉句末 `。`——标题的视觉收束已经够了。（本系统拉丁标题本就不加句号；规则延伸到中日韩。）
- **盘古之白**：中日韩与相邻拉丁 / 数字之间插入细空格。写 `使用 Claude` 而不是 `使用Claude`；`2024 年` 而不是 `2024年`。这是好中文排印的编辑惯例，也匹配 Soft Editorial 的文学用心。
- **一句只用一种字体**：同一行里不要混 LXGW WenKai 与 Noto Serif SC。整段只用其一；句中切换会造成度量颠簸。

### 本系统的审美说明

LXGW WenKai 与 Soft Editorial 的语域匹配得异常好。楷体略带手写的温暖，从 Cormorant Garamond 旧式斜体停下的地方接上——两套字在奶油纸底上都读成私人、斟酌、略亲密。在粉彩卡片（pink、lemon、blush、sage、lilac）上，标题尺度的 LXGW WenKai 读成书法瞬间，加强而不是削弱编辑的平静。首字下沉处理（132px Cormorant Garamond medium）不能平移到中日韩——楷体首字下沉看起来像被切断，而不是装饰；中文开篇段落请完全去掉首字下沉，靠段落上方的斜体 kicker 给出「随笔开头」的提示。

衬线正文切换（Work Sans → Noto Serif SC）是最有后果的改动。Work Sans 的人文 grotesk 在拉丁里与 Cormorant 成对，但楷体标题旁边的无衬线正文在中文里读成廉价课本。Noto Serif SC 的宋体笔画与奶油底、文学标题字体都共鸣，把小出版社文学季刊的气质跨语言保住。若希望从正文做一点语域偏移，eyebrow（28px）可留在 Noto Sans SC，镜像拉丁的无衬线 vs 衬线区分。

### 已知中日韩缺口

- LXGW WenKai 只有单一字重（regular）。系统标志性的标题内「字重下降」（Cormorant 500 → 斜体 400）无法在中日韩复现。强调改为颜色偏移到 `{colors.ink-soft}`，或接受中文标题读成一贯字重。
- LXGW WenKai TC 的繁体切割字形，少数字符可能出繁体形态（例如 設 而不是 设）。纯简体片子优先把 `'Noto Serif SC'` 作主中日韩字体，LXGW WenKai 留给强调瞬间（封面标题、章节标题）。
- 斜体装饰瞬间（kicker、页码、页脚、落款）在中日韩会丢掉斜体，因为没有中日韩字体带真正斜体。用 `{colors.ink-soft}` 和略小字号补偿，保住「装饰低语」语域。
- display 尺寸上的基线错位（见混排策略）在封面带混排标题时需要按套片子微调。

## 迭代指南

1. 任何新标题用 Cormorant Garamond 字重 500，斜体 `<em>` 短语降到字重 400。字重下降是编辑信号。
2. 任何新卡片默认半透明白（`{colors.card-fill}`），圆角 24–36px。粉彩填色给需要颜色的瞬间，不是每张卡片。
3. 任何新步骤序数是斜体小写罗马数字（i.、ii.、iii.），Cormorant Garamond italic，64–92px。
4. 任何新 kicker、marker、页码、页脚或落款是斜体 Cormorant Garamond，26–38px，色为 `{colors.ink-soft}` 或 `{colors.ink}`。
5. 任何新粉彩引入（第六色）会打破系统。五色粉彩板（pink、lemon、blush、sage、lilac）是封闭的。
6. 任何新 pill 用 999px 圆角，粉彩填色或半透明白。Pill 是副标题强调单元，不是页框。
7. 封面色点行（右上三枚圆形色点）是系统的身份标记。封面上要保住。
8. 页框（eyebrow、pagedot、footer）在每页标准幻灯片上坐在固定绝对位置。不要漂移位置。
9. 长文段落阅读应以首字下沉开篇（132px Cormorant Garamond medium）——这是系统最鲜明的编辑瞬间。
10. 卡片周围与之间的奶油底是承重的。版式需要更密时，增加卡片内容，而不是缩小纸底。

## 已知缺口

- 系统依赖外部 `deck-stage.js` 做幻灯片缩放与导航。脚本被引用但未内嵌；没有它，幻灯片会按固有 1920×1080 渲染，没有视口缩放。
- Cormorant Garamond 与 Work Sans 都从 Google Fonts 加载。字体失败时，衬线回退到 Garamond/serif，无衬线回退到 Helvetica/sans-serif；没有 Cormorant，编辑性格会显著退化。
- 全出血 closer 页是粉彩铺满整块画布的唯一位置。这个模式是刻意的，但应少用——每个 closer 都全粉红会削弱「奶油为默认」的身份。
- 五种粉彩（`{colors.pink}`、`{colors.lemon}`、`{colors.blush}`、`{colors.sage}`、`{colors.lilac}`）被列为语义可互换，但源模板在矩阵版式里用 lemon = 是 / blush = 部分 / pink = 否。新片子可以遵循或忽略这个惯例。
- 首字下沉处理依赖 CSS `:first-letter` 渲染，跨浏览器在度量处理上略有差异。内边距与行高为 Cormorant Garamond 调过，字体加载失败时可能需要调整。
- 半透明白卡片填色（`rgba(255,255,255,0.55)`）依赖奶油纸透出来。在不同背景色上，卡片会读成另一回事——规格假定表面是 `{colors.paper}`。
- 卡片内边距在各版式间变化（28/30、48/52、64/48），没有严格阶梯；规则是「紧凑、中等、宽敞」，而不是固定 token 系统。
