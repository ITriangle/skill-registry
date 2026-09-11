---
version: alpha
name: Emerald Editorial
description: "A bold display-serif editorial system in the register of a fashion masthead or vintage magazine cover. Bodoni Moda runs at weight 900 across a wide scale (44–460px), set against a saturated emerald-green canvas with deep navy ink and oat-paper accents. The signature treatment is a stacked double-rule ornament that brackets centered display words like a 19th-century theatrical playbill. The aesthetic borrows from Harper's Bazaar / Vogue / Wallpaper covers: confident, theatrical, paper-and-ink committed, with a tight three-color palette and zero gradients or shadows."

colors:
  bg: "#3CD896"
  bg-2: "#2DC684"
  bg-3: "#25B377"
  ink: "#0F1A5C"
  ink-2: "#1B2774"
  ink-3: "#3A4593"
  paper: "#F1E9D6"
  rule: "rgba(15, 26, 92, 0.22)"
  rule-strong: "rgba(15, 26, 92, 0.85)"

typography:
  numeral-jumbo:
    fontFamily: "'Bodoni Moda', serif"
    fontSize: 460
    fontWeight: 900
    lineHeight: 0.9
    letterSpacing: -0.04em
  display-section:
    fontFamily: "'Bodoni Moda', serif"
    fontSize: 200
    fontWeight: 900
    lineHeight: 0.9
    letterSpacing: -0.015em
  display-cover:
    fontFamily: "'Bodoni Moda', serif"
    fontSize: 184
    fontWeight: 900
    lineHeight: 0.92
    letterSpacing: -0.01em
  display:
    fontFamily: "'Bodoni Moda', serif"
    fontSize: 130
    fontWeight: 900
    lineHeight: 0.96
    letterSpacing: -0.015em
  display-md:
    fontFamily: "'Bodoni Moda', serif"
    fontSize: 128
    fontWeight: 900
    lineHeight: 0.95
    letterSpacing: -0.015em
  display-sm:
    fontFamily: "'Bodoni Moda', serif"
    fontSize: 120
    fontWeight: 900
    lineHeight: 0.95
    letterSpacing: -0.015em
  headline-xl:
    fontFamily: "'Bodoni Moda', serif"
    fontSize: 104
    fontWeight: 900
    lineHeight: 0.95
    letterSpacing: -0.015em
  headline:
    fontFamily: "'Bodoni Moda', serif"
    fontSize: 92
    fontWeight: 900
    lineHeight: 1
    letterSpacing: -0.02em
  ornament-word-lg:
    fontFamily: "'Bodoni Moda', serif"
    fontSize: 84
    fontWeight: 800
    lineHeight: 1
  ornament-word:
    fontFamily: "'Bodoni Moda', serif"
    fontSize: 76
    fontWeight: 800
    lineHeight: 1
  ornament-word-sm:
    fontFamily: "'Bodoni Moda', serif"
    fontSize: 68
    fontWeight: 800
    lineHeight: 1
  title-card-lg:
    fontFamily: "'Bodoni Moda', serif"
    fontSize: 64
    fontWeight: 800
    lineHeight: 1
    letterSpacing: -0.005em
  title-card:
    fontFamily: "'Bodoni Moda', serif"
    fontSize: 48
    fontWeight: 800
    lineHeight: 1
    letterSpacing: -0.005em
  title-card-sm:
    fontFamily: "'Bodoni Moda', serif"
    fontSize: 44
    fontWeight: 800
    lineHeight: 1.05
    letterSpacing: -0.005em
  step-numeral:
    fontFamily: "'Bodoni Moda', serif"
    fontSize: 80
    fontWeight: 900
    lineHeight: 1
  step-title:
    fontFamily: "'Bodoni Moda', serif"
    fontSize: 40
    fontWeight: 800
    lineHeight: 1
    letterSpacing: -0.005em
  kpi-figure:
    fontFamily: "'Bodoni Moda', serif"
    fontSize: 144
    fontWeight: 900
    lineHeight: 0.9
    letterSpacing: -0.03em
  kpi-figure-unit:
    fontFamily: "'Bodoni Moda', serif"
    fontSize: 60
    fontWeight: 800
  stat-figure:
    fontFamily: "'Bodoni Moda', serif"
    fontSize: 92
    fontWeight: 900
    lineHeight: 1
    letterSpacing: -0.02em
  stat-figure-unit:
    fontFamily: "'Bodoni Moda', serif"
    fontSize: 48
    fontWeight: 900
  eyebrow:
    fontFamily: "'Manrope', sans-serif"
    fontSize: 28
    fontWeight: 800
    letterSpacing: 0.18em
    textTransform: uppercase
  label:
    fontFamily: "'Manrope', sans-serif"
    fontSize: 26
    fontWeight: 700
    letterSpacing: 0.08em
    textTransform: uppercase
  label-tight:
    fontFamily: "'Manrope', sans-serif"
    fontSize: 26
    fontWeight: 700
    letterSpacing: 0.05em
    textTransform: uppercase
  tag:
    fontFamily: "'Manrope', sans-serif"
    fontSize: 24
    fontWeight: 800
    letterSpacing: 0.12em
    textTransform: uppercase
  caption:
    fontFamily: "'Manrope', sans-serif"
    fontSize: 24
    fontWeight: 700
    letterSpacing: 0.1em
    textTransform: uppercase
  body-lg:
    fontFamily: "'Manrope', sans-serif"
    fontSize: 28
    fontWeight: 500
    lineHeight: 1.5
  body:
    fontFamily: "'Manrope', sans-serif"
    fontSize: 26
    fontWeight: 500
    lineHeight: 1.5
  body-sm:
    fontFamily: "'Manrope', sans-serif"
    fontSize: 24
    fontWeight: 500
    lineHeight: 1.45
  credit:
    fontFamily: "'Manrope', sans-serif"
    fontSize: 28
    fontWeight: 700
    letterSpacing: 0.18em
    textTransform: uppercase

spacing:
  pad-default: "110px 110px 70px"
  pad-cover: "56px 110px"
  pad-closing: "80px 110px"
  pad-statement: "110px 110px 70px"
  masthead-inset: "56px 80px"
  rule-thick: "4px"
  rule-thicker: "5px"
  rule-thin: "2px"

canvas:
  width: 1920px
  height: 1080px

components:
  ornament-double-rule:
    description: "The system's signature treatment. A centered serif word framed by two stacked 4px horizontal rules on each side. The rules sit 3px apart on top and 3px apart on bottom, giving a 19th-century playbill / theatrical-poster bracket effect. Configurable via :root[data-ornament] to switch between double (default), single, or none."
    ruleHeight: "4px"
    ruleGap: "3px"
    wordWeight: 800
    wordFamily: "'Bodoni Moda', serif"
  ornament-vertical:
    description: "An inline horizontal pair of stacked rules (each 4px tall, 8px apart) on either side of a small serif word. Used as a side bracket around connector words like prepositions."
    ruleHeight: "4px"
    ruleGap: "8px"
    barWidth: "64px"
  masthead:
    position: "absolute"
    placement: "top: 56px, full-width between 80px side padding"
    layout: "flex space-between"
    typography: "{typography.label-tight}"
    color: "{colors.ink}"
  footline:
    position: "absolute"
    placement: "bottom: 56px, full-width between 80px side padding"
    layout: "flex space-between"
    typography: "{typography.label-tight}"
    color: "{colors.ink}"
  rule-h-thick:
    height: "4px"
    background: "{colors.ink}"
    description: "Universal 4px horizontal rule used as section separator and tile/row border. The system's standard rule weight."
  agenda-row:
    description: "A three-column grid row (130px / 1fr / 320px) with 4px ink top borders. Holds a serif ordinal, serif name, and sans-serif kind label. The last row in a list also carries a 4px bottom border, sealing the list."
    rowPad: "26px 0"
    topBorder: "4px solid {colors.ink}"
  inverse-tile:
    description: "A solid {colors.ink} rectangle holding {colors.bg} text. Used for chart-card containers, kpi tiles, process steps, section-opener panels. Carries no corner radius and no shadow."
    background: "{colors.ink}"
    color: "{colors.bg}"
    padding: "32px to 36px"
  paper-tile:
    description: "A solid {colors.paper} rectangle holding {colors.ink} text. The alt variant of inverse-tile — used in rotation across a row of process steps or kpi tiles to break the monotony of ink fills."
    background: "{colors.paper}"
    color: "{colors.ink}"
  mark-pill:
    background: "{colors.ink}"
    color: "{colors.bg}"
    padding: "10px 22px"
    fontWeight: 700
    letterSpacing: 0.1em
    fontSize: 24
    textTransform: uppercase
    description: "A small ink-on-bg pill used as a category mark or section tag. No border-radius — strict rectangle."
  tag-pill:
    background: "{colors.ink}"
    color: "{colors.bg}"
    padding: "8px 20px"
    fontWeight: 700
    letterSpacing: 0.12em
    fontSize: 24
    textTransform: uppercase
  delta-pill:
    background: "{colors.bg}"
    color: "{colors.ink}"
    padding: "6px 16px"
    fontWeight: 800
    letterSpacing: 0.08em
    fontSize: 24
    textTransform: uppercase
    description: "A small bg-on-ink delta indicator placed inside an inverse kpi tile to show change direction. Inverted to ink-on-bg when inside a paper-tile."
  bar:
    description: "A vertical rectangular chart bar in bg (primary), paper (alt). Value label printed above bar in Bodoni 30px. No corner radius."
    background: "{colors.bg} or {colors.paper}"
  chart-card:
    background: "{colors.ink}"
    color: "{colors.bg}"
    padding: "36px 50px 30px"
    gridLineColor: "rgba(60, 216, 150, 0.22)"
    description: "An ink container framing a bar chart on bg. Y-axis labels are Bodoni 26px on the left; x-axis labels are Manrope 24px. Grid lines are 2px at 22% bg-on-ink."
  ornament-numeral-panel:
    description: "A full-bleed inverse panel (ink background) holding a single oversized Bodoni numeral (~460px weight 900) centered. Used as a section-opener device. Topbar / footline strings sit absolutely positioned in the panel corners."
---

## 概述

Emerald Editorial 是一套**大胆展示衬线编辑系统**，根植于时尚杂志和 19 世纪戏剧海报的视觉语言。底层前提是单一排印脸——**字重 900 的 Bodoni Moda**——以毫不道歉的尺度使用：日常标题 92px，陈述和章节开场 130–200px，hero 数字 460px。这张衬线响、戏剧、自信。每一页由字体带头，不是由图像带头。

色板是紧的三色编辑套：饱和祖母绿（`{colors.bg}` — #3CD896）做主导表面，深海军墨（`{colors.ink}` — #0F1A5C）既做主文字色也做反相面板表面，燕麦纸（`{colors.paper}` — #F1E9D6）做交替瓷砖的次级表面。海军 / 祖母绿对比是系统的色彩身份；每一段正文都是海军压祖母绿或祖母绿压海军。token 系统里存在祖母绿的两个近重复（`{colors.bg-2}`、`{colors.bg-3}`）和海军的两个（`{colors.ink-2}`、`{colors.ink-3}`），但它们是预留的——已发布幻灯片几乎完全提交给三种主色。

辅助字体是 **Manrope**，人文几何无衬线，字重 500 跑正文段落，字重 700–800 全大写加宽字距跑每一个标签、标记、眉题、图注和脚线。Manrope 从不跨进展示领地——它停在 28px，留在铬件层。

招牌处理是**双线饰物**——居中衬线词，两侧各由两条叠放的 4px 水平线框住，线之间 3px。这种处理作为封面的中心件和反复出现的陈述括号出现。它读成 19 世纪戏剧海报或复古节目单——一种「The [word] of [word]」框住装置。双线饰物可通过 `:root[data-ornament]` 属性配置成单线或无线变体，但双线变体是系统身份。

纵深是**扁平、基于墨的**。没有投影、没有渐变、没有模糊、没有光晕。每个表面都是实心祖母绿、实心海军或实心纸。抬升通过色块反相发生（祖母绿画布上的海军瓷砖是「抬升」元素）以及分隔区块的 4px 墨线。整套系统读成印在纸上的墨，不是数字界面。

**密度哲学：中满、居中。** 大多数页带着一个尺度上的展示标题（92–200px）加 3–4 个支撑元素（统计行、kpi 网格、流程流、图表卡）。110px 的幻灯片内边距给出呼吸空间，顶底的刊头/脚线铬件锚定页面。塞六个小元素的页读成坏了；一个巨大标题加三块支撑瓷砖的页读成有权威。伸手去拿更少、更大的元素。例外：议程列表模式（由 4px 墨线分隔的大编号行垂直列表）天生密，垂直填满画布——该用时就该这样。

**关键特征：**
- 每一个展示时刻用字重 900 的 Bodoni Moda；每一个正文和标签时刻用字重 500/700/800 的 Manrope。
- 饱和祖母绿画布（`{colors.bg}`）加深海军墨（`{colors.ink}`）文字和反相面板。
- 带居中衬线词的双线饰物是招牌装饰装置。
- 4px 墨水平线分隔每一个叠放区块、每一个列表行、每一个图表边框。4px 粗细是系统的默认规则线。
- 任何地方都没有圆角。每个形状都是严格矩形，除了圆形 logo/排印字形本身。
- 没有阴影、没有渐变、没有模糊。纵深是色块反相 + 4px 规则线。
- 展示字体尺度激进——hero / 章节开场 / 收场时刻 184–460px。
- Manrope 铬件（标签、标记、图注）永远全大写，字距 0.05em–0.18em。

## 色彩

### 色板
- **BG / Emerald**（`{colors.bg}` — #3CD896）：主导幻灯片画布。饱和、略冷的祖母绿——饱和到感觉像印刷墨，不像 CSS 预设。默认幻灯片背景。
- **BG-2**（`{colors.bg-2}` — #2DC684）：略深的祖母绿，留给色调变化；在 token 系统里可用但克制使用。只在两块祖母绿表面相邻需要分开时伸手去拿。
- **BG-3**（`{colors.bg-3}` — #25B377）：最深的祖母绿变体；同样预留。
- **Ink / Navy**（`{colors.ink}` — #0F1A5C）：深海军主色。祖母绿和纸表面上的文字色；反相面板背景色；规则线颜色；描边颜色。系统的结构色。
- **Ink-2**（`{colors.ink-2}` — #1B2774）：略浅的海军变体——可用于墨压墨情境里的色调对比，但很少用。
- **Ink-3**（`{colors.ink-3}` — #3A4593）：最浅的海军变体；预留。
- **Paper**（`{colors.paper}` — #F1E9D6）：燕麦奶油次级表面。用作流程 / kpi 行里的交替瓷砖填充、交替柱状图系列，以及任何需要第三种「暖」表面来打破全海军反相瓷砖行的地方。带着 `{colors.ink}` 文字。
- **Rule**（`{colors.rule}` — `rgba(15, 26, 92, 0.22)`）：半透明海军，只用于细微内部网格线（例如深底上的图表网格线）。不是结构规则线颜色。
- **Rule Strong**（`{colors.rule-strong}` — `rgba(15, 26, 92, 0.85)`）：85% 不透明度海军，可用作近实心规则线替代。

### 默认值
- **默认幻灯片背景**：`{colors.bg}`（祖母绿）。当时刻想要重力时（章节开场、收场），伸手去拿 `{colors.ink}`（海军）做整页表面。
- **祖母绿上的默认标题颜色**：`{colors.ink}`。
- **海军上的默认标题颜色**：`{colors.bg}`——祖母绿压海军是系统用于展示字体的唯一颜色翻转。
- **祖母绿上的默认正文颜色**：`{colors.ink}`。
- **海军上的默认正文颜色**：`{colors.bg}`。
- **纸上的默认正文颜色**：`{colors.ink}`。
- **默认标签 / 眉题 / 标记颜色**：祖母绿和纸表面上 `{colors.ink}`，海军表面上 `{colors.bg}`。
- **默认规则线颜色**：`{colors.ink}`，4px solid。永远。
- **默认反相瓷砖填充**：`{colors.ink}` 配 `{colors.bg}` 文字。一行里的交替瓷砖用 `{colors.paper}` 配 `{colors.ink}` 文字。
- **墨瓷砖内的默认 delta / 胶囊填充**：`{colors.bg}` 背景配 `{colors.ink}` 文字。纸瓷砖内，反相成 `{colors.ink}` 背景配 `{colors.bg}` 文字。

色板故意紧。引入第四个色彩家族（红、黄、橙、薰衣草）会打碎编辑承诺。留在祖母绿 / 海军 / 纸里。bg-2/3 和 ink-2/3 变体为色调细微差别存在，但应该很少需要。

## 字体排印

### 字族
系统从 Google Fonts 加载几套展示衬线字族（Bodoni Moda、Playfair Display、DM Serif Display、Rozha One、Yeseva One），外加 Manrope 做辅助无衬线。**实践中，展示只用 Bodoni Moda**——其他衬线字族加载了但休眠，留给未来变体。Bodoni Moda 是规范展示脸；其他的不是系统声线的一部分。

Bodoni Moda 几乎只用 **字重 900**——最重的切。字重 800 出现在小饰物词和瓷砖标题上（略轻，好让它们不与主标题抢）。字重 700 为一两处最小饰物介词出现。已发布系统里没有字重 500 的 Bodoni。字重 900 的承诺才给系统戏剧海报声线。

Manrope 承担其余一切：正文段落字重 500，标签 / 眉题 / 标记 / 图注字重 700 或 800 全大写、0.05em–0.18em 字距。Manrope 从不以展示尺度出现；Bodoni 从不以铬件尺度出现。

### 展示、正文与铬件字号阶梯

| Token | 字号 | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.numeral-jumbo}` | 460px | Bodoni Moda | 900 | 反相章节开场面板上的 hero 数字 |
| `{typography.display-section}` | 200px | Bodoni Moda | 900 | 议程 / 章节标题 hero |
| `{typography.display-cover}` | 184px | Bodoni Moda | 900 | 封面刊头标题 |
| `{typography.display}` | 130px | Bodoni Moda | 900 | 陈述 / 摘引尺度 |
| `{typography.display-md}` | 128px | Bodoni Moda | 900 | KPI 行开场标题 |
| `{typography.display-sm}` | 120px | Bodoni Moda | 900 | 流程流开场标题 |
| `{typography.headline-xl}` | 104px | Bodoni Moda | 900 | 图表 / 数据开场标题 |
| `{typography.headline}` | 92px | Bodoni Moda | 900 | 日常幻灯片标题 |
| `{typography.ornament-word-lg}` | 84px | Bodoni Moda | 800 | 大饰物括号词（陈述变体） |
| `{typography.ornament-word}` | 76px | Bodoni Moda | 800 | 标准饰物括号词（封面变体） |
| `{typography.ornament-word-sm}` | 68px | Bodoni Moda | 800 | 双线括号之间的封面介词 |
| `{typography.kpi-figure}` | 144px | Bodoni Moda | 900 | KPI 瓷砖数字 |
| `{typography.kpi-figure-unit}` | 60px | Bodoni Moda | 800 | KPI 数字上的单位后缀 |
| `{typography.stat-figure}` | 92px | Bodoni Moda | 900 | 次级统计数字（在侧面板里） |
| `{typography.stat-figure-unit}` | 48px | Bodoni Moda | 900 | 次级统计上的单位后缀 |
| `{typography.title-card-lg}` | 64px | Bodoni Moda | 800 | 大卡 / 议程行名称内的标题 |
| `{typography.title-card}` | 48px | Bodoni Moda | 800 | 图表卡 take-away 标题 |
| `{typography.title-card-sm}` | 44px | Bodoni Moda | 800 | 陈述支撑单元格标题 |
| `{typography.step-numeral}` | 80px | Bodoni Moda | 900 | 流程步骤序数 |
| `{typography.step-title}` | 40px | Bodoni Moda | 800 | 流程步骤标题（坐在顶规则线下方） |
| `{typography.body-lg}` | 28px | Manrope | 500 | 导语 / 副标题段落 |
| `{typography.body}` | 26px | Manrope | 500 | 标准正文段落 |
| `{typography.body-sm}` | 24px | Manrope | 500 | 瓷砖 / 图表侧面板里的紧凑正文 |
| `{typography.eyebrow}` | 28px | Manrope | 800 / 0.18em | 标题上方的章节眉题 |
| `{typography.label}` | 26px | Manrope | 700 / 0.08em | 刊头 / 脚线标签 |
| `{typography.label-tight}` | 26px | Manrope | 700 / 0.05em | 封面顶/底字符串 |
| `{typography.tag}` | 24px | Manrope | 800 / 0.12em | 反相胶囊 / 标记（mark、delta、侧标） |
| `{typography.caption}` | 24px | Manrope | 700 / 0.1em | 议程行类型标签、图表 x 轴、kpi 标签 |
| `{typography.credit}` | 28px | Manrope | 700 / 0.18em | 作者 / 机构署名行 |

### 默认值
- **日常幻灯片标题的默认字号**：`{typography.headline}`（92px）。
- **hero / 封面尺度时刻的默认字号**：`{typography.display-cover}`（184px）或 `{typography.display-section}`（200px）。
- **正文段落的默认字号**：`{typography.body}`（26px），Manrope 字重 500。
- **瓷砖内正文段落的默认字号**：`{typography.body-sm}`（24px）。
- **标题上方眉题的默认字号**：`{typography.eyebrow}`（28px），Manrope 800 全大写 0.18em。
- **标记 / 胶囊 / 芯片的默认字号**：`{typography.tag}`（24px），Manrope 800 全大写 0.12em。
- **KPI 数字的默认字号**：`{typography.kpi-figure}`（144px），可选 60px 单位。
- **任何 Bodoni 展示时刻的默认字重**：900。800 变体留给饰物词和瓷砖标题，从不用于主标题。
- **任何 Manrope 正文行的默认字重**：500。

拿不准时，这一页的主标题伸手去拿 `{typography.headline}`（92px）。120–200px 这一档留给章节开场、陈述和 KPI 行标题——日常标题也用它会把层级压平。

### 招牌处理
只要用到对应元素类型，这些处理就**不可省略**：

- **每一个主 Bodoni 标题以字重 900、负字距（-0.01em 到 -0.03em）和紧行高（0.9–0.95）跑。** 字重 700 或 800 的 Bodoni 标题读成副标题，不是主时刻。
- **每一个 Manrope 标签、眉题、标记、图注、脚线和署名元素都是全大写，字距至少 0.05em。** 句首大写或默认 tracking 的 Manrope 读成 web 应用正文，不是编辑铬件。
- **双线饰物一经使用就是双侧的——居中词两侧都有规则线。** 单侧饰物破坏括号对称。饰物可通过 `:root[data-ornament]` 降级为单线或无线变体，但默认和推荐形式是双线。
- **每一个区块分隔和瓷砖分隔都是 4px solid `{colors.ink}` 规则线。** 从不 1px，从不 2px，从不超出墨的着色。4px 粗细是系统的结构节奏。
- **反相瓷砖永远带 `{colors.ink}` 背景配 `{colors.bg}` 文字。** 交替纸瓷砖带 `{colors.paper}` 背景配 `{colors.ink}` 文字。这些配对之外的颜色组合破坏系统的印刷墨纪律。
- **jumbo 尺度（200px+）的 Bodoni 数字活在反相海军面板上。** 把 460px 数字放在祖母绿画布上技术上可行，但视觉上破坏面板锚定的戏剧海报声线；jumbo 数字属于墨面板内部。

### 排印原则
字重 900 + 负 tracking + 紧行距的组合就是系统的展示声线。改掉这三项里的任何一项（例如字重 700，或默认 tracking，或 1.2 行距）读成另一套设计系统。衬线/无衬线角色划分很严：Bodoni 从不以正文 / 标签尺度出现，Manrope 从不以展示尺度出现。

斜体在 Bodoni 字体请求里加载，但已发布系统里不用——除非刻意引入新模式，否则把它们留在外面。不用下划线。强调通过尺寸、颜色反相和饰物传达。

## 版式

### 画布系统
系统面向固定 **1920×1080** 画布。幻灯片是精确宽高的 `<section class="slide">` 元素。渲染依赖 `deck-stage.js` 把画布缩放到视口。画布是纸料，不是视口——为投影、打印机或 16:9 PDF 导出设计。

### 内边距阶梯
| Token | 取值 | 用途 |
|---|---|---|
| `{spacing.pad-default}` | 110px 110px 70px | 标准内容页（不对称——底边略少给脚线） |
| `{spacing.pad-cover}` | 56px 110px | 封面页（顶边距更少，给刊头空间） |
| `{spacing.pad-closing}` | 80px 110px | 收场页 |
| `{spacing.masthead-inset}` | 顶 56px，侧 80px | 封面和收场上绝对定位刊头 / 脚线内嵌 |

### 铬件解剖
封面和收场带着顶上的 **masthead**（一行 Manrope flex，两侧各一条标签字符串）和底下的 **footline**（匹配的一行）。内容页通常跳过刊头和脚线，靠 110px 顶内边距给标题空间。用刊头时，它活在 `top: 56px, left/right: 80px`。

### 卡片与瓷砖处理
系统**任何地方都没有圆角**。卡片、瓷砖、kpi 面板、饰物规则线、mark 胶囊、tag 胶囊——全是严格矩形。唯一的圆形状是 Bodoni 字形本身的自然曲线。视觉节奏完全来自矩形构图和 4px 墨线。

### 规则线粗细
| 粗细 | 用途 |
|---|---|
| 2px | 图表网格线（细微、半透明） |
| 4px | 通用结构规则线——区块分隔、列表行边框、瓷砖顶规则线 |
| 5px | 封面饰物规则线（略重，好在 184px 展示标题旁边站住重量） |
| 18px 高（顶 4px 规则线 + 底 4px 规则线） | 双线饰物跨度 |

4px 粗细是系统默认；除非时刻明确需要封面更重的 5px 规则线，否则伸手去拿它。

## 纵深与抬升

### 扁平，无阴影
本系统使用**零阴影**。没有 box-shadow，没有 text-shadow，没有 filter blur，没有渐变。抬升完全通过以下传达：

1. **色块反相** —— 祖母绿画布上的海军瓷砖是系统的「抬升」元素。反相就是纵深语言。
2. **4px 墨线** —— 区块由 4px 实心海军线分隔，读成区域之间的纸折痕。
3. **无圆角的实心面板** —— 严格矩形处理加上全反相填充，给瓷砖印刷墨块的重量。

没有软光晕、没有玻璃、没有新拟态。加 box-shadow 会打碎印刷墨纪律。

### 章节开场面板
一种招牌抬升装置：一页可以拆成通栏两列网格，左侧是实心 `{colors.ink}` 面板，装着超大 Bodoni 数字（`{typography.numeral-jumbo}` 460px），右侧是标准祖母绿画布，带标题 + 导语 + 类别标记。面板读成杂志扉页开场——重、锚定、仪式。把它当作开场模式，不是日常幻灯片版式。

## 形状与处理

### 圆角
**零。** 每个形状都是严格矩形。胶囊、标记、瓷砖、面板、柱、刊头、脚线、饰物词——全是方角。

### 描边 / 规则线样式
- **4px solid `{colors.ink}`** — 通用结构规则线。区块分隔、列表行边框、瓷砖内部规则线。
- **5px solid `{colors.ink}`** — 封面饰物略重的规则线。
- **4px solid `currentColor`** — 用在规则线应匹配瓷砖文字色的瓷砖内部（例如纸瓷砖的内部规则线是 `{colors.ink}`；墨瓷砖的内部规则线是 `{colors.bg}`）。

规则线从不虚线，从不断点，从不超出 ink / currentColor 模式着色。

### 装饰元素类型

**Double-Rule Ornament**（`{components.ornament-double-rule}`）— 系统招牌。居中衬线词，两侧各由两条叠放的 4px 水平线框住（线之间 3px）。用在封面上（「The [word] of [word]」框住）、陈述页上（绕着小连接词），以及任何排印时刻需要戏剧括号的地方。可通过 `:root[data-ornament]` 配置成单线或无线。

**Vertical Side-Bracket**（`{components.ornament-vertical}`）— 更小的行内变体：小衬线介词左侧一对叠放 4px 规则线，右侧一对匹配的。用在句子内部行内，而不是居中跨度。

**Masthead / Footline**（`{components.masthead}`、`{components.footline}`）— 封面和收场页顶/底绝对定位的 flex 行。两侧各一条 Manrope 全大写字符串（例如刊物名 + 日期；章节 + 页码）。确立杂志页身份。

**Inverse Tile**（`{components.inverse-tile}`）— 实心 `{colors.ink}` 矩形，装着 `{colors.bg}` 文字。用作图表卡容器、kpi 瓷砖、流程步骤、侧面板。无圆角，无阴影。

**Paper Tile**（`{components.paper-tile}`）— 交替变体：实心 `{colors.paper}` 配 `{colors.ink}` 文字。在一行反相瓷砖里轮换使用以打破单调（例如四步流程流交替 ink → paper → ink → paper）。

**Mark Pill**（`{components.mark-pill}`）— 小的墨压 bg 胶囊，用作章节开场底边距里的类别标记或章节标签。严格矩形。

**Tag Pill**（`{components.tag-pill}`）— 略小的胶囊变体，用在图表侧和 kpi 瓷砖内标记 takeaway 或统计类型。

**Delta Pill**（`{components.delta-pill}`）— bg 压墨（或在纸瓷砖内反相成墨压 bg）芯片，显示方向变化指示（例如 "↑ 12% YoY"）。活在 kpi 瓷砖的角落。

**Agenda Row**（`{components.agenda-row}`）— 三列网格行，上下由 4px 墨线分隔。左列衬线序数，中间衬线名称，右列 Manrope 类型标签。叠放的议程行构成系统的目录模式。

**Chart Card**（`{components.chart-card}`）— 海军反相面板，装着祖母绿 + 纸柱的柱状图。Y 轴标签用 Bodoni；x 轴标签用 Manrope。网格线是 2px、22% 不透明度的祖母绿压海军。面板读成杂志数据跨页。

**Ornament Numeral Panel**（`{components.ornament-numeral-panel}`）— 通栏反相半页，装着单一 460px 的 Bodoni 数字。顶栏 / 脚线字符串坐在角落。只用做章节开场装置。

## 该做与不该做

### 该做
- 每一个 Bodoni 展示标题以字重 900、负字距（-0.01em 到 -0.03em）和紧行高（0.9–0.95）跑。这个组合就是系统的声线。
- 每一个 Manrope 标签 / 眉题 / 标记 / 图注 / 脚线全大写，字距至少 0.05em。句首大写的 Manrope 失去编辑语域。
- 默认幻灯片背景到 `{colors.bg}`（祖母绿）。只在章节开场和收场时刻伸手去拿 `{colors.ink}` 做整页表面。
- 每一个区块分隔、列表边框、瓷砖分隔用 4px solid `{colors.ink}` 规则线。4px 粗细是系统的结构节奏。
- 当排印时刻需要戏剧框住时伸手去拿双线饰物——尤其在两个展示标题之间的小连接词（"of"、"in"、"for"）周围。
- 用反相瓷砖（`{colors.ink}` 底配 `{colors.bg}` 文字）做默认抬升元素。轮换进纸瓷砖以打破全反相填充行。
- 激进地放大展示字体——hero、章节开场和陈述时刻 130–460px。系统奖励尺度。
- 颜色翻转配对 ink-on-bg 与 bg-on-ink。没有清晰语义理由时不要引入第三种颜色翻转（paper-on-ink、ink-on-paper）。
- 保持每个形状是严格矩形。零圆角承诺与双线饰物并列，是系统招牌。

### 不该做
- 不要给任何元素加 box-shadow、text-shadow、渐变或模糊。系统只是扁平印刷墨。
- 不要在 Bodoni Moda 和 Manrope 之外引入第三套字体。Google Fonts 请求里的其他衬线字族（Playfair、DM Serif、Rozha、Yeseva）加载了但不是已发布声线的一部分——加上它们会打碎 Bodoni 承诺。
- 不要把 Bodoni 跑在字重 500 或更轻。系统提交给 900（默认）、800（饰物词、瓷砖标题）和 700（仅小介词）。
- 不要把 Manrope 渲成句首大写或不加字距。Manrope 永远是全大写铬件。
- 不要引入第四个色彩家族。祖母绿 / 海军 / 纸三件套就是全部色板。
- 不要给任何元素用圆角。零半径是系统招牌。
- 不要用 1px 或 2px 结构规则线。4px 粗细是结构默认；2px 留给细微图表网格线。
- 不要把 460px 数字放在没有墨面板锚点的祖母绿画布上。Jumbo 数字活在反相海军面板上。
- 不要用六个小元素挤一页。一个展示标题 + 3–4 块支撑瓷砖是节奏；更多元素需要更小尺度，并破坏编辑语域。
- 不要在封面和收场页上省略刊头 / 脚线。铬件才让它们读成杂志扉页。

## 响应式行为

这是一套通过 `deck-stage.js` 渲染的**固定 1920×1080 演示系统**。画布在 CSS 意义上不响应——没有媒体查询、没有断点、没有流体定尺寸。每一个度量都是 1920×1080 上的固定像素。

### 缩放行为
`deck-stage.js` 包裹每一个 `<section class="slide">`，把 1920×1080 画布均匀缩放到适合浏览器视口，需要时 letterbox。字体、内边距、间隙和规则线粗细都是固定像素，随画布按比例缩放。

### 演示行为
导航委托给 `deck-stage.js`。每一个 `<section class="slide">` 是一帧；运行时处理转场。

### 印刷 / 导出
1920×1080 画布内的固定像素度量干净导出到 16:9 PDF。Bodoni Moda 在印刷分辨率下渲染得好，因为重展示字重即使在大物理尺寸上也扛得住页面。

### 饰物变体切换
`:root[data-ornament]` 属性控制全局饰物风格：`"double"`（默认，两条叠放规则线）、`"single"`（一条居中规则线）或 `"none"`（无线，词单独浮着）。这是每套 deck 的演示级决定，不是每页。

## 中日韩与国际内容

### 推荐中文搭配

| 角色 | 中文字体 | 字重 | 原因 |
|---|---|---|---|
| 展示标题（92–460px） | 霞鹜文楷 LXGW WenKai（Noto Serif SC 900 回退） | 400 / 900 | LXGW WenKai 的手写暖意是最接近 Bodoni Moda 戏剧海报声线的中文对等；字重 900 的 Noto Serif SC 在 jumbo 尺寸上扛住结构体量 |
| 统计 / KPI 数字（144px+） | 思源宋体 Noto Serif SC | 900 | 明朝体字重 900 提供 Bodoni Moda 在 900 时达到的印刷墨体量 |
| 正文段落（24–28px） | 思源宋体 Noto Serif SC | 400 | 明朝体正文声线，用于暖杂志跨页阅读 |
| 眉题 / 标签 / 标记（24–28px） | 思源黑体 Noto Sans SC | 700–800 | 替换 Manrope 做铬件层中文；几何人文品质 |
| 瓷砖标记 / 胶囊 / 图注 | 思源黑体 Noto Sans SC | 700 | 为反相胶囊和标记保住全大写 tracking 的铬件感觉 |

### 混排策略

用 **策略 C** —— 拉丁展示脸保持 Bodoni Moda，让 CJK 字形落到 LXGW WenKai（展示）或 Noto Serif SC（正文）。字重 900 的 Bodoni Moda 承诺是 Emerald Editorial 的全部品牌身份；换成 CJK 字族会破坏定义这套 deck 的时尚杂志 / 19 世纪戏剧海报语域。栈：

```css
/* Bodoni Moda roles (every display moment) */
font-family: 'Bodoni Moda', 'LXGW WenKai TC', 'Noto Serif SC', Georgia, serif;
/* Manrope roles (every chrome / body moment) */
font-family: 'Manrope', 'Noto Sans SC', system-ui, sans-serif;
```

按字形回退策略让拉丁词以 Bodoni 900 渲染（带着给系统声线的戏剧压缩），中文字符以 LXGW WenKai 或 Noto Serif SC 渲染。jumbo 尺寸（200–460px）上的基线错位是最大要注意的点——Bodoni Moda 在 -0.03em tracking 上视觉上比 LXGW WenKai 更密，所以像 `第 3 期` 这样的混排数字面板可能晃。带 jumbo 数字的章节开场面板优先全数字（Bodoni）或全中文（LXGW WenKai）行。

### 加载

加到现有的 Google Fonts `<link>`（或作为第二条 link）：

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=LXGW+WenKai+TC&family=Noto+Serif+SC:wght@400;700;900&family=Noto+Sans+SC:wght@500;700;800&display=swap" rel="stylesheet">
```

LXGW WenKai TC 是 Google Fonts 上的版本（同时带繁体和简体字形）。

### 通用中日韩调整

这些调整适用于本系统里的**每一个中日韩块**，不论尺寸或角色：

- **把行高放宽 0.05–0.08。** 中日韩字形是全宽方块，视觉重量比拉丁字母大；为拉丁调的行高（展示 0.9–0.95，正文 1.45–1.5）在中文里会读成挤。展示提到 1.0–1.1，正文提到 1.55–1.65。
- **去掉中文标题上的负字距。** Bodoni Moda 展示用 -0.01em 到 -0.03em tracking，会把汉字撞到一起。中文跑句设 `letter-spacing: 0`——若标题看起来仍挤，可用极小的正值 `0.02em`。
- **永远不要对中日韩文本使用 `text-transform: uppercase`。** 中文没有大小写；这条 CSS 对汉字什么也不做，却会悄悄弄坏混排行里本该大写的 Manrope 部分。（这里要紧——每一个 Manrope 标签、眉题、标记、图注都用 `text-transform: uppercase`。）
- **中文句子里用中文全角标点**（`，。：；！？「」『』（）`），不要用拉丁等价物（`,.:;!?""''()`）。同一句里混用两套标点系统，读起来像排版错误。
- **中文标题末尾不要句号（。）。** 中文标题遵循与拉丁相同的规则——标题式行去掉句末标点。正文段落保留 。
- **在中日韩与拉丁段的交界处应用盘古之白。** 汉字与相邻的拉丁词或数字之间要有空格（或 0.25em 边距），例如 `2026 年 5 月` 而不是 `2026年5月`。可以手打空格，或用 `pangu.js` 一类的自动加空。
- **一句只用一套字体。** 不要在同一句里在 LXGW WenKai 和 Noto Serif SC 之间切换——按尺寸档选字体（展示 = LXGW WenKai，正文 = Noto Serif SC），整段坚持用它。

### 本系统的审美说明

Emerald Editorial 的整体声线是「时尚刊头 / 19 世纪戏剧海报」——极端尺度上字重 900 的 Bodoni Moda，双线饰物框住居中词。那种戏剧重量的中文对等是**大展示尺寸上的 LXGW WenKai**（它的笔触暖意复现 Bodoni 的手排性格）配** jumbo 数字用字重 900 的 Noto Serif SC**（那里纯体量比暖意更要紧）。展示不要用 Noto Sans SC——几何 grotesque 会把戏剧海报声线压平成「现代企业」。

双线饰物在中文里成立——在 4px 叠放规则线之间框住一个中文词（例如「春」），让 LXGW WenKai 的暖意扛住戏剧括号。对「The X of Y」封面惯例，中文自然读成 `「X」之「Y」` 或 `X 与 Y`，用连接介词（之 / 与 / 的）替换小介词槽里的拉丁 "of"。连接词应该用字重 400 的 LXGW WenKai（匹配拉丁里的 ornament-word-sm 角色）。

Manrope 作为铬件层的角色（全大写 + 0.08em–0.18em tracking）转到中文是**思源黑体 Noto Sans SC 字重 700–800 加 0.05em 正 tracking**。不要试图伪造全大写——在 CJK 跑句上丢掉 `text-transform: uppercase` 规则，让 Noto Sans SC 的几何人文品质只通过字重和 tracking 扛住铬件感觉。

### 已知中日韩缺口

系统对反相海军面板上 460px 字重 900 的 Bodoni Moda（jumbo 数字）的承诺最难翻译——Google Fonts CDN 上没有中文脸能在那个尺度上交出 Bodoni 900 的光学重量。字重 900 的 Noto Serif SC 最接近，但 460px 上汉字的对比曲线视觉上比 Bodoni 数字更重，可能压过海军面板。中文 jumbo 数字章节开场考虑：（1）用中文数字字符（一二三四五六七八九十），视觉上比西方数字更轻，或（2）数字保持 Bodoni（拉丁），让它下面的面板标签扛中文语境。本系统上纯中文 jumbo 数字是最冒险的时刻，值得逐页人工检查。

## 迭代指南

1. 任何新展示标题都是字重 900 的 Bodoni Moda，负字距、紧行距。从展示阶梯里选字号（92 / 104 / 120 / 128 / 130 / 184 / 200）——不要发明新字号。
2. 任何新铬件行（标签、眉题、标记、图注）都是字重 700 或 800 的 Manrope 全大写，0.05em–0.18em 字距。从铬件阶梯里选字号（24 / 26 / 28）。
3. 任何新区块分隔或列表行边框都是 4px solid `{colors.ink}` 规则线。不要 1px / 2px / 3px 结构规则线。
4. 任何新瓷砖用反相填充模式（`{colors.ink}` 底配 `{colors.bg}` 文字）或纸填充模式（`{colors.paper}` 底配 `{colors.ink}` 文字）。在一行瓷砖里轮换混用两者。
5. 任何新胶囊 / 标记 / 芯片都是严格矩形（无圆角），用 `{components.tag-pill}` / `{components.delta-pill}` 的反相填充或 bg 填充颜色组合。
6. 任何新 KPI 数字都是 `{typography.kpi-figure}`（144px），可选 `{typography.kpi-figure-unit}`（60px）后缀。更小的 KPI 字号不在系统里。
7. 任何新饰物时刻默认用双线处理。只通过 `:root[data-ornament]` 全局切到 single 或 none，不要按元素切。
8. 任何新章节开场用半通栏反相面板 + jumbo 数字模式。数字活在海军面板上；右半边装着眉题 + 标题 + 导语 + 标记。
9. 任何新颜色必须来自 `{colors.bg}` / `{colors.ink}` / `{colors.paper}`（若需要色调细微差别，或预留的 bg-2/3 / ink-2/3 变体）。不要引入黄、红或第三强调色。
10. 当版式感觉挤时，加大展示标题字号，而不是加更多元素。系统奖励更大的字，不是更多件。

## 已知缺口

- Google Fonts 请求加载 Bodoni Moda、Playfair Display、DM Serif Display、Rozha One、Yeseva One 和 Manrope。**实践中只用 Bodoni Moda 和 Manrope。** 其他四套衬线字族休眠——加载了但 CSS 里未引用。它们可作为交替展示声线，但必须显式接入。
- 系统依赖 `deck-stage.js` 做画布缩放和幻灯片导航。这份 design.md 没有描述该脚本——把它当作运行时依赖。
- `:root[data-ornament]` 切换（`double` / `single` / `none`）是全局演示设置。不能按页或按饰物应用——切换变体作用于整套 deck。
- ink-2 / ink-3 和 bg-2 / bg-3 颜色 token 已定义，但已发布 CSS 里未积极使用。它们留给色调变化，目前休眠。
- 柱状图用手设柱高（CSS `%`）。没有数据绑定层——扩展图表需要手工算百分比。
- 离线渲染会把 Bodoni 回退到系统衬线（很可能 Georgia），把 Manrope 回退到系统无衬线（很可能 SF/Segoe）。Bodoni 回退会显著压平展示声线；离线 / 印刷可靠性建议自托管。
- 92px Bodoni 标题在海军压祖母绿和祖母绿压海军上维持 WCAG AA 对比，但更小文字（24–28px Manrope）在同一颜色配对上接近对比下限。可能时把小字保持海军压祖母绿（对比更足的方向）。
- 刊头和脚线字符串在源码里是写死的占位（刊物名、日期、页码）。必须按 deck 编辑。
- 系统没有 `@media print` 规则，也没有响应断点。它是固定 1920×1080，任何视口适配都靠 `deck-stage.js`。
