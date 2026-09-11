---
version: alpha
name: Editorial Tri-Tone
description: A literary magazine-meets-annual-report presentation system built on a strict three-color palette — blush pink, golden butter, and deep burgundy wine. Despite having eleven CSS variable names, only three hex values exist in the entire system; every alias is a semantic rename of one of those three. Headlines run Bricolage Grotesque (a variable grotesque with an optical-size axis) at extreme weights and negative letter-spacing. Instrument Serif (italic-cut only) appears as the expressive accent face for chapter numerals, pull-quotes, years, and signatures. JetBrains Mono carries all metadata, labels, and section markers at tight uppercase tracking. The aesthetic is "independent arts publication" — the kind with a colophon, hand-numbered editions, and an editorial desk.

colors:
  pink: "#F2B6C6"
  butter: "#F2D86A"
  burgundy: "#7A1F35"

color-aliases:
  pink-deep: pink
  sky: pink
  cream: butter
  lime: butter
  terracotta: butter
  navy: burgundy
  forest: burgundy
  ink: burgundy

typography:
  display-wordmark:
    fontFamily: "Bricolage Grotesque, sans-serif"
    fontSize: 300px
    fontWeight: 800
    lineHeight: 0.82
    letterSpacing: -0.04em
  display-closer:
    fontFamily: "Bricolage Grotesque, sans-serif"
    fontSize: 320px
    fontWeight: 700
    lineHeight: 0.82
    letterSpacing: -0.05em
  display-stat:
    fontFamily: "Bricolage Grotesque, sans-serif"
    fontSize: 540px
    fontWeight: 700
    lineHeight: 0.78
    letterSpacing: -0.06em
  display-stat-unit:
    fontFamily: "Instrument Serif, serif"
    fontSize: 220px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0
  chapter-num:
    fontFamily: "Instrument Serif, serif"
    fontSize: 240px
    fontWeight: 400
    lineHeight: 0.9
    letterSpacing: 0
  quote-mark:
    fontFamily: "Instrument Serif, serif"
    fontSize: 200px
    fontWeight: 400
    lineHeight: 0.6
    letterSpacing: 0
  display-xl:
    fontFamily: "Bricolage Grotesque, sans-serif"
    fontSize: 84px
    fontWeight: 700
    lineHeight: 0.95
    letterSpacing: -0.02em
  display-lg:
    fontFamily: "Bricolage Grotesque, sans-serif"
    fontSize: 76px
    fontWeight: 700
    lineHeight: 0.95
    letterSpacing: -0.02em
  signature:
    fontFamily: "Instrument Serif, serif"
    fontSize: 64px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0
  endorsement-num:
    fontFamily: "Instrument Serif, serif"
    fontSize: 56px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0
    color: pink
  timeline-year:
    fontFamily: "Instrument Serif, serif"
    fontSize: 56px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0
  subhead-serif:
    fontFamily: "Instrument Serif, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 0
  lede:
    fontFamily: "Bricolage Grotesque, sans-serif"
    fontSize: 56px
    fontWeight: 500
    lineHeight: 1.05
    letterSpacing: -0.02em
  cover-pill:
    fontFamily: "Bricolage Grotesque, sans-serif"
    fontSize: 44px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0
  chart-title:
    fontFamily: "Instrument Serif, serif"
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0
  card-title:
    fontFamily: "Bricolage Grotesque, sans-serif"
    fontSize: 40px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: -0.02em
  quote-heading:
    fontFamily: "Bricolage Grotesque, sans-serif"
    fontSize: 56px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: -0.02em
  body-lg:
    fontFamily: "Bricolage Grotesque, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  body-md:
    fontFamily: "Bricolage Grotesque, sans-serif"
    fontSize: 26px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  body-sm:
    fontFamily: "Bricolage Grotesque, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  label:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.15em
    textTransform: uppercase
  label-wide:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.18em
    textTransform: uppercase
  label-mid:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.12em
    textTransform: uppercase
  label-tight:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.10em
    textTransform: uppercase
  footer:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.12em
    textTransform: uppercase
    opacity: 0.75

spacing:
  slide-pad: 96px
  chrome-gutter: 64px
  section-gap: 48px
  card-pad: 28px 28px 30px
  chart-pad: 48px 48px 56px
  footer-bottom: 36px
  grid-gap: 24px
  endorsement-pad: 20px 0

canvas:
  width: 1920px
  height: 1080px

components:
  pill:
    borderRadius: 999px
    padding: 0.35em 0.9em
    fontFamily: "Bricolage Grotesque, sans-serif"
    fontWeight: 500
    lineHeight: 1.0
  cover-pill:
    borderRadius: 999px
    padding: 16px 38px
    fontSize: 44px
    fontWeight: 500
  closer-pill:
    borderRadius: 999px
    padding: 12px 28px
    fontSize: 22px
  value-card:
    borderRadius: 28px
    padding: 28px 28px 30px
    height: 340px
  value-card-dark:
    background: "{colors.burgundy}"
    color: "{colors.butter}"
  value-card-light:
    background: "{colors.butter}"
    color: "{colors.burgundy}"
  chart-card:
    background: "{colors.butter}"
    color: "{colors.burgundy}"
    borderRadius: 32px
    padding: 48px 48px 56px
  timeline-ribbon:
    background: "{colors.burgundy}"
    color: "{colors.butter}"
    borderRadius: 999px
    padding: 24px 44px
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 24px
    letterSpacing: 0.15em
    textTransform: uppercase
  timeline-ribbon-accent:
    fontFamily: "Instrument Serif, serif"
    fontSize: 30px
    fontWeight: 400
    letterSpacing: 0
    textTransform: none
    color: "{colors.pink}"
  footer-chrome:
    position: absolute
    left: 64px
    right: 64px
    bottom: 36px
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 16px
    letterSpacing: 0.12em
    textTransform: uppercase
    opacity: 0.75
  footer-dot:
    width: 8px
    height: 8px
    borderRadius: 999px
    background: currentColor
    opacity-inactive: 0.3
    opacity-active: 1.0
  swatch-circle:
    width: 36px
    height: 36px
    borderRadius: 999px
  stat-breakdown-bar:
    height: 10px
    borderRadius: 999px
    background: "rgba(246,237,220,0.15)"
  stat-breakdown-divider:
    borderTop: "1px solid rgba(246,237,220,0.25)"
  endorsement-divider:
    borderTop: "1px solid rgba(246,237,220,0.30)"
  avatar:
    width: 72px
    height: 72px
    borderRadius: 999px
    background: "{colors.burgundy}"
    border: "3px solid {colors.burgundy}"
  timeline-axis:
    height: 4px
    background: "{colors.burgundy}"
    opacity: 0.15
  timeline-dot:
    width: 28px
    height: 28px
    borderRadius: 999px
    border: "4px solid {colors.butter}"
    background: "{colors.burgundy}"
---

## frontend-slides 固定舞台策略

当 `frontend-slides` skill 使用这套设计系统时，把最终 deck 生成为**固定 1920×1080 舞台**，均匀缩放到浏览器视口。deck 应在每块屏幕上（包括手机）保住 16:9 幻灯片画布；可以 letterbox 或 pillarbox，但不应该为移动端回流幻灯片内容。

这条策略的优先级高于本文后面描述的任何源模板响应式行为。如果后面某节说原模板是视口流体，把它当作源历史，而不是 `frontend-slides` 的目标生成模型。

即使源模板最初用 `100vw`、`100vh`、`vw`、`vh` 或 `clamp()` 这类视口流体 CSS 实现，本策略仍然适用。把那些值当作设计比例，翻译成 1920×1080 舞台坐标，而不是生成 deck 里的活响应规则。

最终输出用 `deck-stage.js` 或等价的内联舞台缩放器：每页按 1920×1080 渲染，用一次 transform 缩放整个舞台，并核对渲染截图上的文字溢出和面板重叠。


## 概述

Editorial Tri-Tone 是一套**文学杂志演示系统**，建立在尽可能严格的色板上：三个 hex 值，十一个 CSS 变量名。命名系统揭示编辑意图——`--pink` 和 `--sky` 指向同一腮红；`--cream`、`--butter`、`--lime` 和 `--terracotta` 都落到同一金黄；`--burgundy`、`--navy`、`--forest` 和 `--ink` 都塌成同一深酒红。别名存在是为了在语境里传达颜色的角色，不是为了引入变化。

字体栈是一场刻意的三方对话：
1. **Bricolage Grotesque** — 带光学字号轴的可变 grotesque。字重 500、600、700 和 800，用于全部展示和正文无衬线文字。
2. **Instrument Serif** — 只用字重 400，常常是它的斜体面貌。留给章节数字、摘引引号、时间线年份、签名、背书序数和统计百分号。
3. **JetBrains Mono** — 全部元信息、标签、章节标记、脚注、页脚铬件。

编辑声线是带版权页的独立杂志——deck 的最后一页字面就叫 "Colophon。" 章节标记用章节符号（§）后跟数字和标题。语气克制、文学、暖，而不是企业或高能量。

**关键特征：**
- 三色色板加语义别名：腮红粉（#F2B6C6）、金黄油（#F2D86A）、深酒红（#7A1F35）。
- 混排字体：Bricolage Grotesque grotesque 做展示和正文；Instrument Serif 做表现性强调数字、引语和年份；JetBrains Mono 做全部标签。
- Bricolage Grotesque 标题里的 `em` 标签永远触发切到 Instrument Serif 斜体——系统的主排印混搭。
- 胶囊（border-radius 999px）是通用标签组件；在封面、图表图例和收场上用三种不同尺寸。
- 价值卡有慷慨的 28px 圆角——软、圆，不是粗野。
- 深表面上的分隔线用低不透明度 rgba（0.25–0.30）而不是实色——低声分隔。
- 页脚圆点行：用 8px 圆做进度指示，未激活 30% 不透明度，激活 100% 不透明度。
- 唯一的 SVG 图表在同一画布上组合四种系列类型：填充面积、垂直柱、相连圆、点线。

## 色彩

### 三种实际颜色
尽管有许多 CSS 变量名，色板是：

| 名称 | Hex | 角色 |
|---|---|---|
| Blush Pink | #F2B6C6 | 深表面上的强调 / 高亮；统计数字颜色；引号光晕 |
| Golden Butter | #F2D86A | 暖中调；浅色页背景；深表面上的强调文字 |
| Deep Burgundy | #7A1F35 | 主深表面；墨色；结构调 |

### 别名映射
全部别名落到上面三个值之一。别名名信号语境：

| 别名 | 指向 | 使用语境 |
|---|---|---|
| `--pink` | #F2B6C6 | 默认强调标签 |
| `--pink-deep` | #F2B6C6 | （未使用的独立值——与 pink 相同） |
| `--sky` | #F2B6C6 | 分解图里的 Segment D 柱 |
| `--cream` | #F2D86A | 浅表面背景 |
| `--butter` | #F2D86A | 深色上的强调文字；卡片背景 |
| `--lime` | #F2D86A | 缎带强调文字；深表面上的 kicker 标签 |
| `--terracotta` | #F2D86A | 导语或正文里的斜体 em 高亮 |
| `--navy` | #7A1F35 | 深表面语境的交替标签 |
| `--forest` | #7A1F35 | 深面板或列背景 |
| `--burgundy` | #7A1F35 | 结构背景色 |
| `--ink` | #7A1F35 | 全部文字颜色 |


## 字体排印

### 字族
- **Bricolage Grotesque**：主字体。可变，带光学字号轴（opsz 12..96）和 400 到 800 的字重。字重范围是表现工具——400 做正文，500 做导语，600 做卡片标题和引语页眉，700 做章节标题，800 做 wordmark。
- **Instrument Serif**：仅字重 400，加载斜体变体。作为 Bricolage Grotesque 的表现对位。从不用于正文；永远用于大数字、引号、签名、年份、背书序数和统计百分号。关键洞察是系统从不把 Instrument Serif 用于「正常」跑文——只用于人的表现性时刻。
- **JetBrains Mono**：字重 400 和 500。全部标签全大写，字距 0.10–0.18em。永远是次级信息：章节标记、元信息、脚注、图例类别、kicker、页脚铬件。

### `em` 规则
在任何 Bricolage Grotesque 标题里，`<em>` 标签触发切到字重 400 的 Instrument Serif。这是系统的主行内排印混搭——grotesque 标题被衬线旁白打断。例如："A short trajectory, told in *five stops*." em 部分读成更安静、更反思的对位。

### `b` 规则（仅引语页）
在 Instrument Serif 块引里，`<b>` 标签触发切回字重 600 的酒红色 Bricolage Grotesque。em 规则的反向——衬线引语被 grotesk 强调点破。

### 展示字号阶梯

| Token | 字号 | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.display-stat}` | 540px | Bricolage Grotesque | 700 | 通栏超大统计或数字图形 |
| `{typography.display-closer}` | 320px | Bricolage Grotesque | 700 | 超大标题或收场 wordmark |
| `{typography.display-wordmark}` | 300px | Bricolage Grotesque | 800 | 主 wordmark 或 deck 标题 |
| `{typography.display-stat-unit}` | 220px | Instrument Serif | 400 | 统计图形旁的强调符号 |
| `{typography.chapter-num}` | 240px | Instrument Serif | 400 | 大章节或分节数字 |
| `{typography.quote-mark}` | 200px | Instrument Serif | 400 | 装饰大引号 |
| `{typography.display-xl}` | 84px | Bricolage Grotesque | 700 | 数据或图表版式的章节标题 |
| `{typography.display-lg}` | 76px | Bricolage Grotesque | 700 | 章节标题 |
| `{typography.signature}` | 64px | Instrument Serif | 400 | 签名或收束元素 |
| `{typography.lede}` | 56px | Bricolage Grotesque | 500 | 导语或开场陈述 |
| `{typography.quote-heading}` | 56px | Bricolage Grotesque | 600 | 面板标题或编辑副题 |
| `{typography.endorsement-num}` | 56px | Instrument Serif | 400 | 背书或列表序数 |
| `{typography.timeline-year}` | 56px | Instrument Serif | 400 | 年份戳或大序数强调 |
| `{typography.subhead-serif}` | 48px | Instrument Serif | 400 | 深表面上的次级副题 |
| `{typography.cover-pill}` | 44px | Bricolage Grotesque | 500 | 大标签云或关键词胶囊 |
| `{typography.chart-title}` | 40px | Instrument Serif | 400 | 卡片或面板标题 |
| `{typography.card-title}` | 40px | Bricolage Grotesque | 600 | 卡片或价值标题 |

### 正文与标签字号阶梯

| Token | 字号 | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.body-lg}` | 28px | Bricolage Grotesque | 400 | 宣言右栏正文 |
| `{typography.body-md}` | 26px | Bricolage Grotesque | 600/400 | 署名名、背书正文 |
| `{typography.body-sm}` | 24px | Bricolage Grotesque | 400 | 卡片描述、统计注释、收场索引 |
| `{typography.label}` | 24px | JetBrains Mono | 400 | 标准章节标签（0.15em tracking） |
| `{typography.label-wide}` | 24px | JetBrains Mono | 400 | 深色页上的 kicker（0.18em tracking） |
| `{typography.label-mid}` | 24px | JetBrains Mono | 400 | 宣言底部元信息（0.12em） |
| `{typography.label-tight}` | 24px | JetBrains Mono | 400 | 图例类别、分解标签（0.10em） |
| `{typography.footer}` | 16px | JetBrains Mono | 400 | 页脚铬件（0.12em，不透明度 0.75） |

### 原则
Bricolage Grotesque 的光学字号轴让这张脸在大尺寸上显著更有表现力，在小尺寸上更易读，而不改字重。在 540px 和 300px（统计和 wordmark）上，展示以宽、开的字形渲染；在 24px（正文）上它压缩。展示都是字重 700 或 800；正文都是字重 400。这张脸从不用于中间尺寸（48–72px）——那一区属于 Instrument Serif。

Bricolage Grotesque 在展示上的字距永远是负的：300px 时 -0.04em，320px 时 -0.05em，540px 时 -0.06em。正文字号（24–28px）不加字距。

JetBrains Mono 标签 tracking 永远是正的，并按用途变化：密集数据语境 0.10em，次级元信息 0.12em，标准章节标签 0.15em，深色页上的标题 kicker 0.18em。

## 版式

### 画布系统
每一页都精确 1920×1080px。`deck-stage` 自定义元素负责居中和缩放。

### 边距系统
- **铬件边距**（左右 64px）：页脚铬件和大多数内容边缘使用。
- **慷慨幻灯片内边距**（96px）：大多数页用 `padding: 96px 64px`——上下内边距比两侧大，即使在横版幻灯片上也给出肖像出版物的感觉。
- **宽幻灯片内边距**（图表页顶 88px）：略减以容纳两栏版式。


### 幻灯片内部间距模式
每一页遵循自上而下的阅读顺序：
1. 章节标记（`§ XX — Title`，JetBrains Mono，24px，标签 tracking）
2. 标题或主要内容
3. 正文 / 网格内容
4. 页脚元信息（绝对定位，距底 36px）

## 抬升与纵深

本系统**完全不用 box-shadow**。纵深完全来自：

### 色表面对比
酒红/黄油/粉三件套自己造出纵深层级：
- 黄油表面感觉「向前」（暖、浅）
- 粉感觉「被强调」（暖、中）
- 酒红感觉「凹进」（深、锚定）

分栏页内交替表面色（宣言页奶油左 / 酒红右；引语页 lime 左 / 酒红右）通过边缘对比而不是阴影造出纵深。

### 不透明度分隔线
在深（酒红）表面上，全部分隔线和结构线用 rgba 而不是实色：
- 统计分解里的行分隔：`rgba(246,237,220,0.25)`
- 引语页里的背书行：`rgba(246,237,220,0.30)`
- 时间线轴：实心酒红上 `opacity: 0.15`

那些 rgba 字符串里的奶油值（246,237,220）在全不透明度下近似黄油色——分隔线感觉像凹进蚀刻，而不是画出来的线。

### 图表卡抬升
图表卡（第 6 页）通过酒红背景上黄油卡的 32px 圆角获得「抬起」感。没有阴影——对比表面上的圆角信号抬升。

## 形状与处理

### 圆角阶梯
| 取值 | 用途 |
|---|---|
| 999px | 全部胶囊、时间线缎带、色块圆、头像、分解条、时间线点、页脚点、图表数据圆 |
| 32px | 图表卡（第 6 页） |
| 28px | 价值卡（第 3 页） |
| 4px | SVG 图表柱（rx="4"） |
| 0px | 章节标题、网格单元格（不圆） |

系统有强烈的二元：要么全圆（胶囊、圆），要么方（内容块）。例外是图表卡（32px）和价值卡（28px）——圆角大到感觉「软」，但是几何的而不是圆形的。

### 胶囊系统
胶囊是通用标签/标记组件。三种尺寸变体：
- **封面胶囊**：44px 字体，16px 38px 内边距——大到在标签云里读成标题元素
- **标准胶囊**（章节标签、图例项）：22–24px 字体，10–12px 24–28px 内边距
- **颜色分配**交替：封面上酒红底/粉字和黄油底/酒红字；收场上酒红/奶油或 lime/ink

### SVG 图表（第 6 页）
720×380 viewBox 的内联 SVG 图表故意组合四种系列类型，以展示单一图表表面的范围：
- **面积系列**（Series A）：填充路径，粉填充 0.85 不透明度，酒红描边字重 3
- **柱系列**（Series C）：酒红矩形，rx="4"
- **相连圆系列**（Series B）：黄油圆（r=8），酒红描边/填充，坐在字重 3 的酒红线上
- **点线**（Series D）：酒红虚线描边（stroke-dasharray="2 10"，stroke-linecap="round"），60% 不透明度

Y 轴标签是 60% 不透明度的 JetBrains Mono 24px，左对齐到 x=0。

## 该做与不该做

### 该做
- 把三个 hex 值当作封闭系统。每个元素用粉、黄油或酒红——没有中性色、没有灰、没有白。
- Instrument Serif 只用于人的表现性时刻：数字、年份、签名、引号、背书序数。从不用于跑文正文。
- 在 Bricolage Grotesque 标题里用 `em` 标签触发衬线切换。这是系统的主行内混搭，也是它最清晰的编辑声线。
- 给全部标签文字（JetBrains Mono）0.10em 到 0.18em 的正字距。没有 tracking 的等宽读成代码，不是编辑。
- 在两栏分栏页上交替表面色。一侧永远是黄油，另一侧永远是酒红。
- 正文留在 Bricolage Grotesque，字重 400（文字）和 500–600（强调标签）。字重轴是调性旋钮。
- 在多种尺寸上用胶囊——胶囊是通用标签，尺寸信号语境：44px 做标题级分类，22–24px 做工具标签。
- 章节标记遵循 JetBrains Mono 的 `§ NN — Title` 模式——每一页都以这个惯例开场。

### 不该做
- 不要引入第四种颜色。三色约束就是设计前提。
- 不要在小尺寸或正文段落里用 Instrument Serif。它纯粹是强调脸。
- 不要打破 em 规则——用 Bricolage Grotesque 斜体而不是 Instrument Serif 做行内强调，会丢掉排印混搭。
- 不要在展示尺寸上给 Bricolage Grotesque 加字距——只通过 `letter-spacing: -0.02em` 到 `-0.06em`（随尺寸）做负 tracking。
- 不要在深（酒红）表面上加实色分隔线。深背景上的全部结构线必须用低不透明度 rgba。
- 不要加 box-shadow。系统一个都没有。纵深来自表面对比和对比背景上的圆角。
- 不要给大内容容器（章节面板、网格背景）圆角。圆角只用于胶囊尺度和卡片尺度元素（价值卡、图表卡）。
- 除 wordmark 外不要用 Bricolage Grotesque 字重 800。字重 800 留给单一最大排印时刻。

## 响应式行为

本模板**专为 1920x1080 演示显示设计**。`deck-stage` web 组件通过 CSS transform 处理视口缩放；1920x1080 画布按比例缩放到任意屏幕，版式不变。

### 演示行为
- 通过键盘或演示翻页器前进幻灯片（由 `deck-stage.js` 处理）。
- 没有定义悬停状态。
- 没有交互元素。

### 印刷 / 导出
- 在 96dpi 下，1920x1080 对应 20x11.25 英寸画幅。
- 540px 的统计数字渲染约 ~405pt——适合大幅面印刷。
- 三色色板可安全印刷；酒红是深 PMS 范围的酒红调，黄油是暖黄，粉是闷腮红——在 CMYK 胶印里都再现得好。

## 中日韩与国际内容

### 推荐中文搭配

| 角色 | 中文字体 | 字重 | 原因 |
|---|---|---|---|
| 展示 wordmark / 收场 / 统计（300–540px） | 站酷小薇体 ZCOOL XiaoWei | 400 | 文学装饰衬线，与极端尺度上的 Bricolage Grotesque + Instrument Serif 斜体有同样的表现性格 |
| 章节标题（76–84px） | 思源黑体 Noto Sans SC | 700 | CJK 里的 grotesque 对等——扛住 Bricolage Grotesque 的结构重量 |
| 章节数字 / 引号 / 年份（200–240px） | 霞鹜文楷 LXGW WenKai | 400 | 手排暖意，匹配 Instrument Serif 的表现强调角色 |
| 正文段落（24–28px） | 思源宋体 Noto Serif SC | 400 | 明朝体正文声线；文学语域 |
| 导语 / quote-heading（56px） | 思源黑体 Noto Sans SC | 500–600 | 匹配 Bricolage Grotesque 字重 500/600 |
| 等宽标签 / 章节标记 / 页脚 | 思源等宽 Noto Sans Mono CJK SC | 400–500 | 为 `§ NN — Title` 标记保住 JetBrains Mono 铬件品质 |

### 混排策略

用 **策略 C** —— 拉丁脸保持 Bricolage Grotesque（展示、正文）和 Instrument Serif（斜体强调），只对 CJK 字形回退到中文栈。Editorial Tri-Tone 的文学杂志身份依赖 Bricolage Grotesque 的光学字号轴和 Instrument Serif 的斜体切作为品牌声线的一部分；整套换成 CJK 字族会把系统压平成「通用中文编辑」。栈：

```css
/* Bricolage Grotesque roles (display, body) */
font-family: 'Bricolage Grotesque', 'Noto Sans SC', sans-serif;
/* Instrument Serif roles (chapter-num, quote-mark, year, signature) */
font-family: 'Instrument Serif', 'LXGW WenKai TC', serif;
/* JetBrains Mono roles (labels, section markers) */
font-family: 'JetBrains Mono', 'Noto Sans Mono CJK SC', monospace;
```

系统招牌的 `<em>` 规则（Bricolage Grotesque → Instrument Serif 斜体行内）在拉丁里扛着编辑调性**但不能移植到中文**。句中换脸在 CJK 排印里读成坏了——中文读者把它解析成排版错误，而不是拉丁读者解析的那种刻意编辑对比。当周围句子是中文时，**抑制 em 规则里换脸的那一部分**，改用颜色或字重对比：

```css
/* Latin sentences — original em rule applies */
:lang(en) h1 em, :lang(en) h2 em, :lang(en) .lede em, :lang(en) .quote-heading em {
  font-family: 'Instrument Serif', serif;
  font-style: italic;
}
/* Chinese sentences — emphasize via color or weight, not face */
:lang(zh) h1 em, :lang(zh) h2 em, :lang(zh) .lede em, :lang(zh) .quote-heading em {
  font-family: inherit;
  font-style: normal;
  color: var(--terracotta); /* or another palette accent */
  /* optional alternative: font-weight: 700; */
}
```

如果 deck 没有语言标记的元素，更安全的规则是：**根本不要用 `<em>` 包中文短语**。章节符号 + 标题 + 正文的层级已经给中文提供了足够的强调结构；行内斜体强调是拉丁编辑习惯，中文没有对等。中文句子从头到尾活在一张脸上时读得干净。

注意展示尺寸（300–540px）上的基线错位：Bricolage Grotesque 在 -0.04em 到 -0.06em tracking 上视觉上比 Noto Sans SC 更紧，所以像 `INTO 中国` 这样的混排 wordmark 可能感觉不均。hero / wordmark 时刻优先单文种行，让第二种文种自己活在下面一行。

### 加载

加到现有的 Google Fonts `<link>`（或作为第二条 link）：

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&family=Noto+Serif+SC:wght@400;500;700&family=LXGW+WenKai+TC&family=ZCOOL+XiaoWei&display=swap" rel="stylesheet">
```

ZCOOL XiaoWei 是用于 em 切换角色的装饰终端衬线；它在 Google Fonts 上只以字重 400 托管。

### 通用中日韩调整

这些调整适用于本系统里的**每一个中日韩块**，不论尺寸或角色：

- **把行高放宽 0.05–0.08。** 中日韩字形是全宽方块，视觉重量比拉丁字母大；为拉丁调的行高（展示 0.78–0.92，正文 1.4–1.45）在中文里会读成挤。展示提到 0.95–1.05，正文提到 1.5–1.6。
- **去掉中文标题上的负字距。** Bricolage Grotesque 展示用 -0.04em 到 -0.06em tracking，会把汉字撞到一起。中文跑句设 `letter-spacing: 0`——若标题看起来仍挤，可用极小的正值 `0.02em`。
- **永远不要对中日韩文本使用 `text-transform: uppercase`。** 中文没有大小写；这条 CSS 对汉字什么也不做，却会悄悄弄坏混排行里本该大写的拉丁部分。
- **中文句子里用中文全角标点**（`，。：；！？「」『』（）`），不要用拉丁等价物（`,.:;!?""''()`）。同一句里混用两套标点系统，读起来像排版错误。
- **中文标题末尾不要句号（。）。** 中文标题遵循与拉丁相同的规则——标题式行去掉句末标点。正文段落保留 。
- **在中日韩与拉丁段的交界处应用盘古之白。** 汉字与相邻的拉丁词或数字之间要有空格（或 0.25em 边距），例如 `2026 年 5 月` 而不是 `2026年5月`。可以手打空格，或用 `pangu.js` 一类的自动加空。
- **一句只用一套字体。** 不要在同一句里在 Noto Sans SC、Noto Serif SC 和 ZCOOL XiaoWei 之间切换——选匹配角色的脸（标题 = Noto Sans SC，正文 = Noto Serif SC），整段坚持用它。**这条规则覆盖中文内容的 em 规则**：即使同一个 `<em>` 在拉丁里换脸，也不要在中文的 `<em>` 上句中换脸。中文的行内强调用颜色（例如 `var(--terracotta)`）或字重（400 → 700），永远不要换脸。

### 本系统的审美说明

Editorial Tri-Tone 的文学杂志声线依赖 Bricolage Grotesque（结构）与 Instrument Serif 斜体（表现）之间的排印对比。**这种对比不能干净转到中文**，因为句中换脸不是中文排印惯例——它读成不一致，而不是刻意的编辑强调。正确的适配是在**角色层级**保住脸对比（标题 = 思源黑体，正文 = 思源宋体，标签 = 等宽），而不是行内。任何单一中文跑句里，留在一张脸上。拉丁会用 `<em>` 翻进 Instrument Serif 斜体的地方，中文应该用色板的强调色（黄油上的 terracotta，酒红上的粉，等等）或字重上提（400 → 700）来强调。

对系统招牌展示时刻——300px wordmark、540px 统计数字、240px 章节数字——中文处在最响的位置。时刻是装饰性时伸手去拿**站酷小薇体**（文学衬线渲染的章节序数「第一章」），时刻是结构性时伸手去拿**思源黑体字重 700**（像「我们的方法」这样的章节标题）。200px 引号字形在中文里更难——中文引号（「」）没有拉丁「弯引号」同样的装饰重量，所以考虑把整个引语时刻的标点字符本身用拉丁字形渲染（用 `Instrument Serif` 脸），让下面的正文切到思源宋体。

章节标记惯例 `§ NN — Title` 在中文里成立：`§ 02 — 我们的承诺`。章节符号和数字保持 JetBrains Mono / Noto Sans Mono CJK SC；标题文字可以切到思源黑体字重 400，带 0.05em tracking，以保住铬件品质。

### 已知中日韩缺口

ZCOOL XiaoWei 是 em 切换角色的正确审美匹配，但它以**仅字重 400、没有斜体切**出货。中文没有斜体概念（倾斜汉字读成坏了，不是强调），所以缺斜体没问题——但 Instrument Serif 斜体在拉丁里提供的视觉柔软对比（更斜、更流动的字形）无法在中文里精确复现。ZCOOL XiaoWei 的装饰终端衬线品质提供最接近的对等，但相对思源黑体的对比是**基于脸的，不是基于倾斜的**。重度依赖 em 规则的 deck 应在中文里测试视觉节奏再提交——若对比感觉闷，把 em 部分字号加大 4–8px 来补偿。

## 迭代指南

1. 章节标签永远用 JetBrains Mono 的 `§ NN — Title` 惯例，带 `{typography.label}` tracking。
2. 每一个带 em/斜体时刻的标题用 `<em>` 触发 Instrument Serif。永远不要直接在 Bricolage Grotesque 上用 `font-style: italic`。
3. 价值卡交替：奇数卡（c1、c3、c5、c7）是深（酒红/黄油）；偶数卡（c2、c4、c6、c8）是浅（黄油/酒红）。
4. 新的深表面区块用 `rgba(246,237,220,0.25)` 做分隔线——不要全不透明度的 `{colors.butter}`。
5. 新胶囊遵循现有交替：簇里用酒红底/粉字和黄油底/酒红字求变化。
6. 加图表系列：在发明新编码之前，先用四种既有视觉编码（面积、柱、圆、点线）。
7. 全部章节背景必须是三色色板之一——永远不要混（不要半粉半黄油）。
8. 页脚铬件在所有幻灯片上共享：`position:absolute; left:64px; right:64px; bottom:36px; font-family:JetBrains Mono; font-size:16px; opacity:0.75`。

## 已知缺口

- `deck-stage.js` 脚本是此处未文档化的外部依赖。
- 页脚圆点行进度指示（`.footer .dotrow`）在 HTML 里渲染，但圆点全部用 class "on" 样式化或留作未激活——演示者需要动态更新幻灯片状态。
- SVG 图表使用写死的路径、坐标和占位值——不存在数据绑定层。
- 第 4 页的分解条用内联 `width: XX%` 作为样式——百分比必须手工设置。
- 时间线站点圆点（`.stop .dot`）有 `display: none`——它们有样式但不可见。填充这一页的演示者会通过 CSS 启用它们。
- Instrument Serif 斜体作为字体变体加载，但并非在每个语境里都用 `font-style: italic` 显式调用——有些情况下浏览器根据周围语境从可变字体的斜体轴自动选择它。
- 第 4 页的色块圆引用 `--terracotta` 和 `--sky`，它们分别与 `--butter` 和 `--pink` 相同解析——视觉区分只在源码里语义存在，视觉上不存在。
