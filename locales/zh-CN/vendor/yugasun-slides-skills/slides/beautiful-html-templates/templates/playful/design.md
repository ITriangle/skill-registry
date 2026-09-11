---
version: alpha
name: Playful
description: "A warm, hand-crafted editorial system built on a peach-clay canvas with charcoal ink as the only \"color.\" Display type runs in Syne (weight 700–800, tight negative tracking); body type runs in Space Grotesk at weight 400–500. The aesthetic borrows from independent studio decks, risograph zines, and sketchbook spreads: organic blob frames, scribbled SVG doodles, slightly rotated cards, and double-stroke offset borders give every slide a hand-touched, unpolished warmth. The effect is creative-studio editorial, not corporate pitch — confident but human, structured but loose."

colors:
  bg: "#F0C8A0"
  bg-alt: "#E8B88E"
  light: "#F7DEC6"
  text: "#1A1A1A"

color-aliases:
  accent: text

typography:
  display-hero:
    fontFamily: "Syne, sans-serif"
    fontSize: "clamp(4rem, 10vw, 9rem)"
    fontWeight: 800
    lineHeight: 0.9
    letterSpacing: -0.03em
  display:
    fontFamily: "Syne, sans-serif"
    fontSize: "clamp(3rem, 8vw, 7rem)"
    fontWeight: 800
    lineHeight: 0.9
    letterSpacing: -0.02em
  headline:
    fontFamily: "Syne, sans-serif"
    fontSize: "clamp(2.5rem, 6vw, 5rem)"
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -0.01em
  statement:
    fontFamily: "Syne, sans-serif"
    fontSize: "clamp(2.5rem, 5vw, 4.5rem)"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.01em
  title:
    fontFamily: "Syne, sans-serif"
    fontSize: "clamp(2rem, 4vw, 3.5rem)"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.01em
  title-sm:
    fontFamily: "Syne, sans-serif"
    fontSize: "1.3rem"
    fontWeight: 700
    lineHeight: 1.2
  number-hero:
    fontFamily: "Syne, sans-serif"
    fontSize: "clamp(4rem, 8vw, 7rem)"
    fontWeight: 800
    lineHeight: 1.0
  number-md:
    fontFamily: "Syne, sans-serif"
    fontSize: "2.5rem"
    fontWeight: 800
    lineHeight: 1.0
  number-sm:
    fontFamily: "Syne, sans-serif"
    fontSize: "2rem"
    fontWeight: 800
    lineHeight: 1.0
  body:
    fontFamily: "Space Grotesk, sans-serif"
    fontSize: "clamp(1rem, 1.2vw, 1.1rem)"
    fontWeight: 400
    lineHeight: 1.7
  body-md:
    fontFamily: "Space Grotesk, sans-serif"
    fontSize: "1.2rem"
    fontWeight: 500
    lineHeight: 1.6
  label-eyebrow:
    fontFamily: "Space Grotesk, sans-serif"
    fontSize: "0.85rem"
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.15em
    textTransform: uppercase
  caption:
    fontFamily: "Space Grotesk, sans-serif"
    fontSize: "0.85rem"
    fontWeight: 500
    lineHeight: 1.4
  tag:
    fontFamily: "Space Grotesk, sans-serif"
    fontSize: "0.75rem"
    fontWeight: 600
    lineHeight: 1.2

spacing:
  pad-slide-lg: "4rem 5rem"
  pad-slide-md: "3rem 4rem"
  pad-card-lg: "2rem 3rem"
  pad-card-md: "1.5rem"
  gap-lg: "3rem"
  gap-md: "2rem"
  gap-sm: "1.5rem"

canvas:
  width: 100vw
  height: 100vh

components:
  rough-box:
    border: "3px solid {colors.text}"
    background: "{colors.bg}"
    padding: "1.5rem"
    offsetShadowOffset: "6px 6px"
    offsetShadowBorder: "2–3px solid {colors.text}"
    description: "Generic content card with a double-stroke effect — the inner box has a 3px solid border, and an absolutely-positioned ::before pseudo-element offsets a second 2–3px border down-and-right by 6–8px to simulate a hand-drawn double outline. No fill on the offset; the canvas shows through."
  filled-block:
    background: "{colors.text}"
    color: "{colors.bg}"
    padding: "1.5rem"
    description: "Inverted card: dark charcoal background with peach text. Used as the visual counterpoint to outlined cards in a collage of mixed treatments."
  blob-frame-organic:
    border: "3px solid {colors.text}"
    borderRadius: "40% 60% 70% 30% / 40% 50% 60% 50%"
    description: "Organic outlined blob, asymmetric border-radius. Decorative wrapper that holds a smaller solid filled-blob inside it."
  blob-frame-pebble:
    border: "3px solid {colors.text}"
    borderRadius: "255px 15px 225px 15px / 15px 225px 15px 255px"
    description: "Pebble-shaped frame with extreme alternating border-radius — two opposing corners pulled long, the other two pinched short. Reads as a hand-drawn lozenge."
  blob-fill:
    background: "{colors.text}"
    borderRadius: "60% 40% 30% 70% / 60% 30% 70% 40%"
    description: "Solid dark blob with asymmetric organic radius. Used inside an outlined blob-frame or floating on its own as decorative mass."
  scribble-svg:
    stroke: "{colors.text}"
    strokeWidth: 2
    fill: none
    strokeLinecap: round
    description: "Inline SVG path drawn as a single hand-drawn line — wavy stub, scribbled circle, star outline, squiggle, arrow. Always 2px stroke, rounded caps. Placed absolutely in corners and edges as decorative breath."
  doodle-circle:
    border: "3px solid {colors.text}"
    borderRadius: "50%"
    description: "Plain round outlined circle used as a decorative anchor in slide corners."
  doodle-rect:
    border: "3px solid {colors.text}"
    rotation: "5–10deg"
    description: "Plain outlined rectangle, slightly rotated, used as a decorative anchor in slide corners."
  card-rotated:
    transform: "rotate(-3deg to 3deg)"
    description: "Any card or block can carry a small ±3deg rotation. Rotations stagger so adjacent cards rotate in opposite directions — never all in the same direction, never more than 3deg."
  step-node-circle:
    width: 64px
    height: 64px
    border: "3px solid {colors.text}"
    borderRadius: "50%"
    background: "{colors.bg}"
    fontFamily: "Syne, sans-serif"
    fontSize: 1.5rem
    fontWeight: 800
    description: "Round outlined node containing a single numeric digit at display weight. Used as a timeline or process marker; alternates between outlined (bg fill) and filled (charcoal fill, bg text)."
  avatar-placeholder:
    width: 60px
    height: 60px
    background: "{colors.text}"
    borderRadius: "50%"
    description: "Solid dark circle used as a portrait stand-in inside a team or people card."
  tag-pill:
    background: "{colors.text}"
    color: "{colors.bg}"
    padding: "0.4rem 0.8rem"
    fontFamily: "Space Grotesk, sans-serif"
    fontSize: "0.75rem"
    fontWeight: 600
    description: "Small charcoal pill with peach text, anchored to the bottom-left of an image frame as a category label."
  bar-chart:
    barFillSolid: "{colors.text}"
    barFillOutlined: "3px solid {colors.text} + transparent"
    axisStroke: "3px solid {colors.text}"
    description: "Custom HTML bar chart. Bars are either solid charcoal (primary series) or outlined transparent (secondary series). Axes are 3px solid charcoal lines, no grid."
  vertical-text:
    fontFamily: "Syne, sans-serif"
    fontWeight: 700
    letterSpacing: 0.1em
    transform: "rotate(90deg)"
    description: "Display-weight text rotated 90deg, anchored to a slide edge as a magazine-style spine label."
  ghost-blob:
    background: "{colors.text}"
    borderRadius: "40% 60% 70% 30% / 40% 50% 60% 50%"
    opacity: 0.08
    description: "Oversized organic blob at very low opacity placed behind content as atmospheric wallpaper. Functions like a watermark cloud."
---

## 概览

Playful 是一套**手作编辑系统**，锚定在单一温暖画布上——桃泥色 `{colors.bg}`（#F0C8A0）——炭墨 `{colors.text}`（#1A1A1A）是唯一有意义的「颜色」。一切都读成泥纸上的墨。没有第二品牌色，没有渐变，没有彩色强调。系统彻底押在单色纪律上，表现力来自形状、字重、旋转和手绘痕迹，而不是色板花样。

字体栈是 **Syne 做展示，Space Grotesk 做正文**。Syne 是性格——高对比展示无衬线，带着古怪的人文比例，读起来像当代独立工作室声线，不是企业无衬线。每个标题、宣言、统计数字和数字都用字重 700 和 800，配紧的负字距（-0.01em 到 -0.03em）。Space Grotesk 是干活的——稳、中性的几何无衬线，正文 400–500，标签 500–600。这对读起来像「建在可靠网格上的表现性编辑」。

色彩哲学是**单色温暖**：单一墨色落在单一温暖表面上，外加画布的两个色调兄弟（`{colors.bg-alt}` 略深，给图片占位；`{colors.light}` 略浅，给轻分层）。桃色饱和到足以读成刻意的审美选择，而不是中性底。墨从纯黑略软成 #1A1A1A，好坐在暖纸上。系统的情绪档是「工作室速写本」——自信但暖，有结构但不抛光。

层次来自**双描边偏移边框**和**手绘痕迹**，不是模糊阴影。招牌处理：卡片上 3px 炭描边，再加一个 `::before` 伪元素向右下偏移 6–8px，带着第二道 2–3px 描边——视觉效果是手绘双轮廓，像描边没描齐。配上卡片的小旋转（±0.5deg 到 ±3deg）和角落里的涂鸦 SVG 路径，系统读成手作，而不是软件渲出来的。

**密度哲学：中低。** 每一页锚定在单一主导元素上——一句宣言、一张图、一份名单——周围是刻意留白，再加一两笔装饰涂鸦。卡片、涂鸦和文案同时挤满画布，会把手作感压成杂乱。正确密度是每页一个实质瞬间，用一两道 SVG 涂鸦或有机 blob 在负空间里当标点。

**关键特征：**
- 桃泥画布（`{colors.bg}`）配炭墨（`{colors.text}`）作为唯一颜色。没有第二品牌色板。
- 每个展示和数字瞬间用 Syne 字重 700–800 加负字距；正文用 Space Grotesk 400–500。
- 卡片上的双描边偏移边框——3px 外轮廓，再加 `::before` 偏移 6–8px 的幽灵描边。
- 卡片、色块和统计数字带小幅 ±0.5deg 到 ±3deg 旋转，做出手摆上去的感觉。
- 不对称 border-radius 的有机 blob 形状，充当装饰框和填色。
- 内联 2px 描边的 SVG 涂鸦（波浪线、星星、圆、箭头）住在幻灯片角落，当手绘标点。
- 没有网页阴影。层次来自双描边、旋转和墨密度对比。
- 每页一个主导元素，负空间要慷慨——绝不满铺内容。

## 颜色

### 色板
- **Background**（`{colors.bg}` — #F0C8A0）：桃泥画布。每页的默认表面。饱和到足以当系统签名；暖到炭墨读起来柔，而不是刺。
- **Background Alt**（`{colors.bg-alt}` — #E8B88E）：画布略深的色调兄弟。用作图片占位区域的填色，以及一张卡片需要读成「在另一张后面」却又不承诺新颜色时的轻微表面分化。
- **Light**（`{colors.light}` — #F7DEC6）：画布略浅的色调兄弟。区域需要只抬升一个色阶、又不引入白色时，给轻分层用。
- **Text/Ink**（`{colors.text}` — #1A1A1A）：炭墨——系统里唯一的非画布色。从纯黑软下来，好当暖纸上的暖墨。用于全部正文、全部展示字、全部描边、全部 SVG 描边、全部实心底块、全部深色填色。

`accent` 别名解析到 `{colors.text}` ——系统没有单独的强调色。Playful 里的「强调」是相对画布的对比，不是第三色相。

### 默认值
- **默认表面背景**：`{colors.bg}` ——每页都从桃泥打开。
- **默认标题色**：`{colors.text}` ——始终如此。标题从不染色或换色。
- **默认正文字色**：`{colors.text}` ——有时用不透明度 0.7–0.9 来弱化，但底层颜色仍是炭。
- **默认描边色**：`{colors.text}` ——每个描边卡片、blob、涂鸦和图表坐标轴都是炭。
- **实心炭块上的默认文字色**：`{colors.bg}` ——深色表面上的桃色文字是唯一的颜色反转。
- **默认图片占位填色**：`{colors.bg-alt}` ——比画布略深，让占位读成独立区域，却不用白色。
- **默认装饰 blob 填色**：`{colors.text}` 全不透明（前景），或 0.08 不透明（内容背后的大气 ghost-blob）。

系统没有「主色 vs 次色」的概念。每个视觉决定都是画布（桃）和墨（炭）的二元选择，用不透明度、尺度和形状来调制。

## 字体

### 字族
系统配对两款精心挑选的 Google Fonts：

- **Syne**（展示）：当代人文展示无衬线，字形古怪，开口窄，比例略压缩。每个展示瞬间——标题、宣言、标题、数字、竖排标签——都用字重 700 和 800。它的性格是 Playful 区别于普通暖色调片子的地方：Syne 读成独立工作室声线，不是企业页眉。
- **Space Grotesk**（正文）：干净、略几何的无衬线，带着友好的人文温度。正文段落用字重 400–500，标签和图注用 500–600。给 Syne 的表现力提供稳、可读的对位。

没有第三张脸。不用斜体，不用下划线。强调来自字重（700 → 800）、字号，以及 Syne vs Space Grotesk 的对比本身。

### 字号阶梯

| Token | 字号 (clamp) | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.display-hero}` | 4–9rem | Syne | 800 | 超大封面或开场日期/标题 |
| `{typography.display}` | 3–7rem | Syne | 800 | 收束或重大宣言标题 |
| `{typography.headline}` | 2.5–5rem | Syne | 700 | 主区块标题 |
| `{typography.statement}` | 2.5–4.5rem | Syne | 700 | 长引文宣言或宣言句 |
| `{typography.title}` | 2–3.5rem | Syne | 700 | 区域或章节标题 |
| `{typography.number-hero}` | 4–7rem | Syne | 800 | Hero 统计数字 |
| `{typography.number-md}` | 2.5rem | Syne | 800 | 中等序数或统计数字 |
| `{typography.number-sm}` | 2rem | Syne | 800 | 行内序数或步骤数字 |
| `{typography.title-sm}` | 1.3rem | Syne | 700 | 小块内的卡片标题 |
| `{typography.body-md}` | 1.2rem | Space Grotesk | 500 | 副标题或强调正文 |
| `{typography.body}` | 1–1.1rem | Space Grotesk | 400 | 段落正文 |
| `{typography.label-eyebrow}` | 0.85rem | Space Grotesk | 600 | 标题上方的区块 eyebrow，全大写加字距 |
| `{typography.caption}` | 0.85rem | Space Grotesk | 500 | 副标题、细字、脚注 |
| `{typography.tag}` | 0.75rem | Space Grotesk | 600 | 炭标签胶囊内的 pill 文字 |

### 默认值
- **主区块标题的默认字号**：`{typography.headline}`（2.5–5rem clamp）。
- **封面或重大开场瞬间的默认字号**：`{typography.display-hero}`（4–9rem clamp）。
- **段落正文的默认字号**：`{typography.body}`（1–1.1rem clamp）。
- **副标题或强调导语正文的默认字号**：`{typography.body-md}`（1.2rem）。
- **任何行内图注、脚注或细字的默认字号**：`{typography.caption}`（0.85rem）。
- **Hero 数字的默认字号**：`{typography.number-hero}`（4–7rem clamp）。
- **统计砖或序数数字的默认字号**：`{typography.number-md}`（2.5rem）。
- **任何展示元素（标题、宣言、标题、数字）的默认字重**：700 或 800 ——从不更低。
- **任何正文元素的默认字重**：400 或 500。

一页上的主文字在 `{typography.title}` 和 `{typography.headline}` 之间拿不准时，伸手去拿 `{typography.headline}` —— `{typography.title}` 留给页内子区域。

### 标志性处理
这些处理在**对应元素类型被使用时不可省略**：

- **每个展示元素都设成 Syne。** 标题、宣言、标题、数字、竖排标签、装饰单字符记号——全部 Syne。大字号用 Space Grotesk 是错误的系统信号。
- **每个 Syne 元素都用负字距**：按字号 -0.01em 到 -0.03em。默认字距的 Syne 读成没处理过；负字距才给展示字紧、压缩的性格。
- **每个正文和标签元素都设成 Space Grotesk。** 用 Syne 跑正文段落读成用力过猛。
- **Eyebrow 标签是全大写加 0.15em 字距。** 没有全大写 + 字距的标签读成正文碎片，不是标签。
- **统计和数字始终字重 800。** 即便中等数字（2rem）也跟展示字重约定。字重 500 的数字读成库存清单，不是炫耀。
- **数字和统计作为独立统计项、而不是图表或表格内时，可以带小旋转（±0.5deg 到 ±1deg）**。旋转强化手摆上去的感觉。

### 排印原则
系统的排印节奏来自 **Syne vs Space Grotesk 的对比**，不是同一张脸里混字重。一页只用不同字重的 Syne 读成单调；一页只用 Space Grotesk 读成克制到企业风。正确节奏是 Syne 标题 + Space Grotesk 正文，有纪律地重复。

行高：展示紧（0.85–1.1），正文松（1.5–1.7）。绝不要在正文上用紧行高，也绝不要在展示上用松行高——两种倒置都会打断节奏。

这套系统里不存在斜体。不存在下划线。强调靠换脸（正文 → 展示）或换字重（400 → 700），从不靠斜体。

## 版式

### 画布系统
系统目标是 `100vw × 100vh` ——满视口。每个 `.slide` 绝对定位铺满视口，只有 `.active` 页可见（不透明度 1，其余 0）。幻灯片导航由 JS 驱动：方向键、空格、点下一步/上一步按钮、触控滑动。视口底部有一条 4px 高的炭进度条，随页码增长。所有尺寸用 `clamp()`，所以版式在 768px 的移动回流之前无需断点就能流体缩放。

### 内边距阶梯
| Token | 值 | 用途 |
|---|---|---|
| `{spacing.pad-slide-lg}` | 4rem 5rem | 封面、宣言和收束页——慷慨外边距 |
| `{spacing.pad-slide-md}` | 3rem 4rem | 标准内容页——外边距 |
| `{spacing.pad-card-lg}` | 2rem 3rem | 大卡片或联系色块的内部 padding |
| `{spacing.pad-card-md}` | 1.5rem | 标准卡片内部 padding |
| `{spacing.gap-lg}` | 3rem | 主区域之间的大网格/flex 间距 |
| `{spacing.gap-md}` | 2rem | 单元格之间的标准网格/flex 间距 |
| `{spacing.gap-sm}` | 1.5rem | 紧的行内间距 |

### 页框
右下角固定一组 48px×48px 导航簇（上一页箭头、页码计数、下一页箭头——全部 2px 炭描边）。一条 4px 高的炭进度条贴着视口底边跑。两者都不是幻灯片构图的一部分；它们是片子持续的演示页框，不该被拿去对着做样式。

进度条和导航按钮是仅有的持续 UI 元素。幻灯片本身没有顶栏、没有页脚 chrome、画布内也没有页码。

## 层次与抬升

### 双描边偏移边框（主手法）
招牌层次处理是**双描边偏移边框**。卡片带着 3px 实心炭描边，一个绝对定位在卡片上的 `::before` 伪元素带着第二道 2–3px 描边，向右下偏移 6–8px。偏移描边没有填色——画布透出来。视觉效果是手绘双轮廓，像笔沿着边缘拉了两遍。这是系统的抬升装置；它取代大多数系统会用的 `box-shadow`。

### 旋转（次手法）
卡片、色块、统计和装饰形状上的小旋转（±0.5deg 到 ±3deg）提供手摆上去的感觉。相邻元素的旋转方向交替——绝不要两张卡片朝同一方向转挨在一起——暗示有人一片片用手放下，而不是对齐到吸附网格。

### 大气 Ghost-Blob
招牌处理：一个超大有机 blob（`{components.ghost-blob}`）用 0.08 不透明度的炭填色，绝对定位在幻灯片角落当大气壁纸。blob 读成内容背后柔软的水印云。省着用——每页最多一个 ghost-blob，锚定在主内容不占用的角落。

### 没有网页阴影
系统使用**没有 `box-shadow` 模糊值、没有 `drop-shadow`、没有 rgba 阴影**。所有表观层次来自双描边偏移边框、旋转和墨密度对比。任何元素上的模糊阴影都会打断手作审美——痕迹应看起来是画的，不是渲的。

## 形状与处理

### 圆角阶梯
| 值 | 用途 |
|---|---|
| 0px | 卡片、色块、标签、图片框、表格单元格 |
| 50% | 圆形头像占位、步骤节点圆、涂鸦圆 |
| 不对称有机（例如 `40% 60% 70% 30% / 40% 50% 60% 50%`） | 仅 blob 框和 blob 填色 |
| 卵石不对称（例如 `255px 15px 225px 15px / 15px 225px 15px 255px`） | 仅卵石形框 |

系统避开平滑的中等圆角（4px、8px、12px）——角要么尖、要么正圆、要么有机 blob。中间地带读成通用 web app，是错误信号。

### 描边粗细
- **3px solid `{colors.text}`** ——标准描边卡片和 blob 框的描边粗细。
- **2–3px solid `{colors.text}`** —— `::before` 伪元素上的偏移幽灵描边粗细（比主描边略细）。
- **3px solid `{colors.text}`** ——图表坐标轴粗细（柱状图的 X、Y 轴）。
- **2px solid `{colors.text}`** ——导航按钮描边粗细和时间线轨道水平线。
- **2px stroke** ——标准 SVG 涂鸦描边粗细，圆线帽。

### 装饰元素类型

**Rough-box 卡片** — 矩形内容卡片，带着招牌双描边偏移边框。背景可以是画布桃色（默认），或实心炭（反转卡片）。Padding 来自 `{spacing.pad-card-*}` 阶梯。可选小旋转（±0.5–3deg）。

**有机 blob 框** — 不对称 border-radius 的装饰描边包裹。用作肖像框或装饰锚点；常常在里面再放一个更小的实心 blob-fill。两种特征形状：波浪有机 blob（`{components.blob-frame-organic}`）和卵石形（`{components.blob-frame-pebble}`）。

**实心 blob 填色** — 不对称有机圆角的炭有机形状。要么放在描边 blob 框里（做成框与体量配对），要么独自漂浮当装饰体量。

**涂鸦 SVG** — 内联 SVG 路径，画成单条 2px 描边的炭线，圆线帽。词汇：波浪短 stub、星形轮廓、涂鸦圆、波形 squiggle、箭头、同心圆。绝对定位在幻灯片角落或边缘当装饰呼吸。每页至少一道涂鸦；最满的页带两三道。

**涂鸦圆 / 涂鸦矩形** — 普通描边圆或矩形，略旋转，绝对定位在幻灯片角落当最小装饰锚。blob 形状更简单的对位——当一页需要视觉标点、但 blob 会显得太有机时用。

**步骤节点圆** — 64px 圆形描边节点，里面一个 Syne 800 的单位数字。在描边（画布填色、炭数字）和实心（炭填色、画布数字）之间交替——奇数步实心、偶数步描边，或任何一致模式。

**Tag pill** — 小炭矩形，桃色文字，0.75rem 字重 600。锚定在图片框左下当类别标签。唯一不是完整卡片的反转「字压炭」元素。

**竖排书脊标签** — Syne 700 文字，1.5rem，旋转 90deg，锚定在幻灯片右缘，字距 0.1em。读成杂志书脊路标。

**Ghost-blob 壁纸** — 0.08 不透明度的超大有机 blob，绝对定位在幻灯片角落当大气壁纸。

**连接箭头涂鸦** — 小 SVG 速写箭头（单条 2px 线加 chevron 箭头头），用于在页的负空间里暗示「下一步」或「另见」。

## 该做与不该做

### 该做
- 每个展示瞬间（标题、宣言、标题、数字、竖排标签）用 Syne，每个正文和标签用 Space Grotesk。两张脸的对比是系统的排印节奏。
- 每个 Syne 元素施加负字距（-0.01em 到 -0.03em）。默认字距的 Syne 读成没处理过。
- 每个主内容卡片施加双描边偏移边框——3px 主轮廓，再加 `::before` 偏移 6–8px 的幽灵描边。这是系统的招牌抬升装置。
- 每页至少一个角落放一道涂鸦 SVG 记号（波浪线、星星、圆、箭头）当手绘呼吸。记号是标点，不是内容。
- 给卡片、色块和统计数字小幅 ±0.5–3deg 旋转。相邻元素交替旋转方向，这样没有任何东西读成吸附到网格。
- 只用 `{colors.text}`（炭）当墨色。标题、正文、描边、涂鸦、填色——全是同一颜色。
- 区域需要读成独立表面、又不引入白色或新颜色时，伸手去拿 `{colors.bg-alt}`。
- 让负空间呼吸。每页一个主导元素加一两道涂鸦是正确密度。
- 需要肖像式装饰锚时，把描边 blob 框和一个更小的实心 blob 填色配对放进去。
- 负空间显得空、但涂鸦又太小时，在幻灯片角落放一个超大 ghost-blob（炭，0.08 不透明度）。

### 不该做
- 不要引入第三色。系统只有桃画布 + 炭墨。没有蓝、没有红、没有图表分段色板——图表柱是实心炭或描边炭，从不着色。
- 不要用模糊 `box-shadow`。所有层次来自双描边和旋转。模糊阴影立刻打断手绘审美。
- 不要施加中等圆角值（4px、8px、12px）。角要么尖、要么全圆、要么有机 blob——没有中间。
- 不要用 Space Grotesk 做标题或展示瞬间。Syne 是性格脸；换成 Space Grotesk 会丢掉工作室声线。
- 不要用 Syne 跑正文段落。小字号、低字重时读成用力过猛。
- 不要把元素旋转超过 3deg。超过 ±3deg，手摆感会滑成歪和业余。
- 不要让每个元素朝同一方向转。相邻元素交替 ±方向；一律同向读成整张画布歪了，不是手摆。
- 不要用同时出现的卡片、统计和涂鸦挤满一页。稀疏时系统读成贵，密时读成坏掉。
- 不要用斜体或下划线做强调。改换脸或换字重。
- 不要把展示字重文字放在默认字距上。始终用负字距收紧 Syne。

## 响应式行为

系统目标是 `100vw × 100vh`，全程用 `clamp()`，所以字号和 padding 在视口尺寸之间流体缩放，无需媒体查询。唯一一条媒体查询在 `max-width: 768px`：多列网格回流成单列，水平时间线轨道收成竖直，幻灯片 padding 减到 2rem。

### 演示行为
- 前进：`ArrowRight`、`Space` 或 `Enter`。
- 后退：`ArrowLeft`。
- 活动页带着 `.active` 类；非活动页 visibility-hidden，不透明度 0。
- 页面过渡用 0.6s 不透明度淡入淡出。
- 视口底部有一条 4px 高的炭进度条，随片子前进增长。
- 右下导航簇显示上一步/下一步按钮（48px 描边方块）和当前/总页计数。
- 移动端水平触控滑动前进/后退。

### 打印行为
没有定义 `@media print` 规则。片子以网页/视口为先；没有自定义打印样式时，打印不会正确渲染。

## 中日韩与国际内容

### 推荐中文搭配

| 角色 | 拉丁字体 | 中文字体 | 字重 |
|---|---|---|---|
| 展示 / 标题 / 数字（Syne 700–800） | Syne | 站酷快乐体 ZCOOL KuaiLe | 400（仅有这一档字重） |
| 正文 / 标签（Space Grotesk 400–600） | Space Grotesk | 悠哉字体 Yozai | 400 |

### 混排策略

策略 A ——把每个 token 的 `fontFamily` 扩到拉丁字体后面跟上中文字体。Syne token 变成 `"Syne, ZCOOL KuaiLe, sans-serif"`；Space Grotesk token 变成 `"Space Grotesk, Yozai, sans-serif"`。拉丁字形走原字体；CJK 字符自动下落。

### 加载

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=Space+Grotesk:wght@400;500;600;700&family=ZCOOL+KuaiLe&display=swap" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/cn-fontsource-yozai-regular/font.css" rel="stylesheet">
```

### 通用中日韩调整

- 行高：正文 1.75–1.85，展示 1.15–1.25
- 字距：CJK 上为 0
- 文字变换：CJK 上不要全大写
- 全角标点 （，。：；！？「」（））
- 展示标题不加句号（中文排版惯例）
- 盘古之白（CJK 与拉丁之间空格：`使用 Claude` 而不是 `使用Claude`）
- 一句一字体

### 本系统的审美说明

Playful 是一套手作编辑系统，建在 Syne（古怪人文展示）加 Space Grotesk（温暖几何正文）上，落在桃泥画布上。中文迁移特别强，因为这里选的两张中文脸，都带着与拉丁配对相同的「暖、手作、独立工作室」档。

**站酷快乐体 ZCOOL KuaiLe** 是圆润、友好的中文展示脸，带着古怪人文比例——CDN 上最接近 Syne 表现性工作室声线的对等。在展示字重（4–9rem）下，KuaiLe 读成当代独立中文工作室声线，不是企业或正式。它自然配上桃画布和炭墨。**中文展示请丢掉负字距（-0.01em 到 -0.03em）** ——KuaiLe 设计在方形 em 盒上，收紧会造成字形碰撞。这张脸内在的温度，取代负字距给 Syne 做的事。

**悠哉字体 Yozai** 是为放松正文阅读设计的中文无衬线——终端略圆，人文比例友好，用来匹配 Space Grotesk 给拉丁带来的温度。每个中文正文段落和标签都设成 Yozai 400。Eyebrow 标签处理（0.15em 字距 + 拉丁全大写）转不到 CJK；中文 eyebrow 用同一 0.85rem 字号的 Yozai，字距 0、无全大写——单靠小字号就读成标签。

双描边偏移边框、小幅 ±3deg 旋转、有机 blob 形状、SVG 涂鸦、ghost-blob 壁纸——全部与文字无关。单色纪律（桃 + 炭）和手作审美在换文字后完整存活。

系统的排印节奏（Syne vs Space Grotesk 对比）在纯中文里变成（KuaiLe vs Yozai 对比）——两对都带着同一套「建在可靠网格上的表现性编辑」节奏。统计和数字是纯数字，仍走 Syne 800 不变；只有当统计带着中文单位后缀（`亿`、`万`）时，后缀字形才落到 KuaiLe。

### 已知中日韩缺口

ZCOOL KuaiLe 和 Yozai 都是单字重脸（400）。系统对字重对比的依赖（Syne 700 vs 800 做次展示层级；Space Grotesk 400 vs 500 vs 600 做标签层级）在纯中文里塌成只靠字号的层级。这不是有意义的损失——Playful 的层级本来就主要靠字号驱动，缺掉的字重台阶不足以改变视觉节奏。旋转、涂鸦和双描边处理无论有没有字重可用，都扛着系统性格。

## 迭代指南

1. 任何新卡片都用 rough-box 模式：3px 炭描边，桃色背景（反转则为炭），padding 来自 `{spacing.pad-card-*}`，以及 `::before` 幽灵描边向右下偏移 6–8px、粗细 2–3px。
2. 任何新卡片带小旋转（±0.5–3deg）。与相邻卡片交替旋转方向；绝不要让所有卡片对齐到同一角度。
3. 任何新标题用 Syne 字重 700–800 加负字距。如果标题是页上的主瞬间，伸手去拿 `{typography.headline}` 或 `{typography.display}` ——不要用 `{typography.title}`（那是子区域尺度）。
4. 任何新正文或标签用 Space Grotesk 字重 400–600。标题上方的小标签用 `{typography.label-eyebrow}`（0.85rem，字重 600，全大写，0.15em 字距）。
5. 任何新统计或数字用 Syne 字重 800 加负字距。即便小数字（2rem）也跟展示字重约定。
6. 任何新页至少一个角落有一道涂鸦 SVG 记号——波浪线、星星、圆、箭头。描边 2px，圆线帽，颜色 `{colors.text}`。
7. 任何装饰形状用不对称有机 border-radius（blob），或尖 0px（矩形），或 50%（圆）。避开中等圆角。
8. 如果页的负空间显得沉，加一个 ghost-blob（炭，0.08 不透明度，超大有机形状），锚定在内容不占用的角落。
9. 图表（柱、甜甜圈、线）只用 `{colors.text}` 和 `{colors.bg-alt}` 当填色。不要引入彩色图表色板。
10. 卡片可以是描边（默认——画布填色、炭描边、炭字）或反转（炭填色、桃色字）。反转卡片是系统的强调装置；留给你想锚定页注意力的那一格。

## 已知缺口

- 系统通过网络加载两款 Google Fonts（Syne、Space Grotesk）。如果字体加载失败，回退无衬线仍会渲染，但系统的声线会丢掉。生产环境建议自托管。
- 双描边偏移边框（带 6–8px 偏移的 `::before`）要求父卡片有 `position: relative`，伪元素在视觉上要落在卡片包围盒加上偏移之内。靠近幻灯片边缘的卡片，偏移描边可能被裁切。
- 768px 的移动响应断点会回流网格，但不会调整绝对定位的装饰 SVG 和 blob——它们仍停在桌面坐标，小视口上可能重叠或掉出屏幕。把响应式行为当成基础档，不是打磨过的。
- 桃画布（#F0C8A0）有很强的文化档（泥土、温暖、略乡土）。它配不好冷色调品牌色板，也不能跟中性奶油或白色互换——温暖是根基。
- 图片占位（`{colors.bg-alt}` 填色加居中的 "IMG 01" 标签）只是桩。生产片子需要尊重暖色板的真实图片；冷色调照片会跟画布打架。
- 没有定义暗色模式变体。系统是单模式（只有暖桃画布）。
- 导航按钮的悬停状态（背景填成炭，文字反转到桃）是交互式演示页框行为，不是片子幻灯片构图的一部分。
