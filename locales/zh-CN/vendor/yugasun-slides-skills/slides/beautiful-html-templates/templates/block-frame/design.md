---
version: alpha
name: BlockFrame
description: "A maximalist neobrutalist presentation system built on 4px solid black borders, 8px hard offset shadows, and a high-key candy palette of five saturated pastels plus cream and off-white. Display type runs Inter at weight 800-900 in tight uppercase; secondary chrome uses Space Grotesk as a quasi-monospace label face. Tilted decorative shapes (rotated stars, rectangles, badges) puncture the borders and break the grid intentionally. Pastels are paired loudly: pink + blue + green + yellow + cream cycle through every region with deliberate juxtaposition. The aesthetic borrows from zine layout, 1990s-revival sticker books, and contemporary toy packaging — bold, joyful, slightly chaotic, never timid."

colors:
  black: "#000000"
  white: "#FFFFFF"
  offwhite: "#FFFDF5"
  pink: "#FE90E8"
  blue: "#C0F7FE"
  green: "#99E885"
  yellow: "#F7CB46"
  cream: "#FFDC8B"

borders:
  primary: "4px solid {colors.black}"
  thin: "3px solid {colors.black}"

shadows:
  default: "8px 8px 0px {colors.black}"
  small: "4px 4px 0px {colors.black}"
  hover: "6px 6px 0px {colors.black}"
  close-yellow: "12px 12px 0px {colors.yellow}"
  close-white: "6px 6px 0px {colors.white}"

typography:
  heading-xl:
    fontFamily: "'Inter', sans-serif"
    fontWeight: 900
    fontSize: "clamp(48px, 6vw, 96px)"
    lineHeight: 0.95
    letterSpacing: -0.03em
    textTransform: uppercase
  heading-lg:
    fontFamily: "'Inter', sans-serif"
    fontWeight: 800
    fontSize: "clamp(32px, 4vw, 64px)"
    lineHeight: 1
    letterSpacing: -0.02em
    textTransform: uppercase
  heading-md:
    fontFamily: "'Inter', sans-serif"
    fontWeight: 700
    fontSize: "clamp(24px, 2.5vw, 40px)"
    lineHeight: 1.1
    letterSpacing: -0.01em
  close-title:
    fontFamily: "'Inter', sans-serif"
    fontWeight: 900
    fontSize: "clamp(40px, 5vw, 80px)"
    lineHeight: 0.95
    letterSpacing: -0.03em
    textTransform: uppercase
  quote-text:
    fontFamily: "'Inter', sans-serif"
    fontWeight: 900
    fontSize: "clamp(28px, 3.5vw, 52px)"
    lineHeight: 1.15
    letterSpacing: -0.02em
    textTransform: uppercase
  stat-number:
    fontFamily: "'Inter', sans-serif"
    fontWeight: 900
    fontSize: "clamp(36px, 4vw, 64px)"
    lineHeight: 1
  card-title:
    fontFamily: "'Inter', sans-serif"
    fontWeight: 700
    fontSize: 22px
    lineHeight: 1.2
    textTransform: uppercase
  step-num:
    fontFamily: "'Inter', sans-serif"
    fontWeight: 900
    fontSize: 48px
    lineHeight: 1
  body:
    fontFamily: "'Inter', sans-serif"
    fontWeight: 500
    fontSize: "clamp(16px, 1.2vw, 20px)"
    lineHeight: 1.6
  body-card:
    fontFamily: "'Inter', sans-serif"
    fontWeight: 500
    fontSize: 15px
    lineHeight: 1.6
  list-body:
    fontFamily: "'Inter', sans-serif"
    fontWeight: 500
    fontSize: 16px
    lineHeight: 1.5
  label:
    fontFamily: "'Space Grotesk', monospace"
    fontWeight: 600
    fontSize: 13px
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  mono-tag:
    fontFamily: "'Space Grotesk', monospace"
    fontWeight: 600
    fontSize: 14px
    lineHeight: 1
    letterSpacing: 0.05em
    textTransform: uppercase
  mono-meta:
    fontFamily: "'Space Grotesk', monospace"
    fontWeight: 500
    fontSize: 15px
    letterSpacing: 0.02em
  subtitle-mono:
    fontFamily: "'Space Grotesk', monospace"
    fontWeight: 500
    fontSize: 18px
    lineHeight: 1.5
  counter:
    fontFamily: "'Space Grotesk', monospace"
    fontWeight: 700
    fontSize: 14px
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  legend-item:
    fontFamily: "'Space Grotesk', monospace"
    fontWeight: 600
    fontSize: 13px

spacing:
  slide-pad: 60px
  card-pad-lg: 60px
  card-pad-md: 36px
  card-pad-sm: 28px
  card-pad-xs: 22px
  gap-lg: 48px
  gap-md: 32px
  gap-sm: 24px
  gap-xs: 16px
  pad-bottom-clearance: 110px

canvas:
  width: 100vw
  height: 100vh
  default-background: "{colors.offwhite}"

components:
  card-elevated:
    border: "4px solid {colors.black}"
    background: "{colors.white}"
    boxShadow: "{shadows.default}"
    description: "Primary elevated card. 4px ink border + 8px ink offset shadow. Background is white by default; on darker surfaces background may shift to offwhite or to a colored fill."
  card-flat:
    border: "4px solid {colors.black}"
    background: "{colors.white}"
    description: "Bordered card without elevation shadow. Used for secondary content cells inside multi-card grids where the shadow would compound."
  card-small:
    border: "3px solid {colors.black}"
    background: "{colors.white}"
    boxShadow: "{shadows.small}"
    description: "Compact card with thinner border + smaller offset shadow. Used for intro-cards, stat-cards, team-cards, and timeline-steps."
  label-pill:
    border: "3px solid {colors.black}"
    padding: "6px 16px"
    fontFamily: "'Space Grotesk', monospace"
    fontSize: 13px
    fontWeight: 600
    letterSpacing: 0.08em
    textTransform: uppercase
    background: "{colors.white}"
    boxShadow: "{shadows.small}"
    description: "Universal section eyebrow. White base by default; pink, blue, green, yellow, cream variants swap background. Always sits on a 3px black border with a 4px hard offset shadow."
  button-primary:
    border: "3px solid {colors.black}"
    background: "{colors.yellow}"
    color: "{colors.black}"
    padding: "14px 32px"
    fontFamily: "'Inter', sans-serif"
    fontWeight: 700
    fontSize: 16px
    boxShadow: "{shadows.small}"
    description: "Primary CTA. Yellow fill with black text, 3px black border, 4px offset shadow. Hover lifts the button -2/-2 and grows shadow to 6px."
  corner-bracket:
    width: 24px
    height: 24px
    border: "3px solid {colors.black}"
    description: "Two L-shaped brackets at opposite corners of a card or frame (tl + br + tr + bl pattern available). Sits inside the card edge as a decorative frame-within-frame."
  icon-square:
    width: 64px
    height: 64px
    border: "3px solid {colors.black}"
    description: "Solid pastel square (pink/blue/green) holding a single uppercase letter glyph at weight 700 / 28px. Used as feature-card icons."
  feature-deco:
    width: 48px
    height: 48px
    border: "3px solid {colors.black}"
    background: "{colors.yellow}"
    position: "absolute top -12px right 24px"
    description: "Yellow square notch that protrudes from the top edge of a feature card, breaking the card's top border line."
  stat-deco-dot:
    width: 12px
    height: 12px
    borderRadius: 50%
    border: "2px solid {colors.black}"
    description: "Small black-bordered colored circle pinned to the top-right of a stat card. The only round shape used on cards. Fill cycles through the pastel palette."
  avatar-square:
    width: 72px
    height: 72px
    border: "3px solid {colors.black}"
    background: "{colors.pink}"
    fontFamily: "'Inter', sans-serif"
    fontWeight: 900
    fontSize: 28px
    textTransform: uppercase
    description: "Square avatar with two-letter initials, used in team grids. Fill cycles through the pastel palette."
  list-number:
    width: 36px
    height: 36px
    border: "3px solid {colors.black}"
    background: "{colors.yellow}"
    fontFamily: "'Space Grotesk', monospace"
    fontWeight: 700
    fontSize: 14px
    description: "Square numerical bullet pinned to the left of each list item. Black border, yellow fill, mono numeral."
  star-burst:
    clipPath: "polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%)"
    border: "3px solid"
    background: "{colors.pink}"
    description: "10-point star clipped via CSS clip-path with a 3px border. Decorative attention-grabber pinned to corners of close-frames and feature cards."
  stripe-block:
    background: "repeating-linear-gradient(45deg, {colors.black}, {colors.black} 4px, {colors.green} 4px, {colors.green} 12px)"
    border: "3px solid {colors.black}"
    description: "Black-and-color diagonal stripe panel used as decorative attention block on poster-class surfaces."
  bg-dot-grid:
    backgroundImage: "radial-gradient(circle, {colors.black} 1.2px, transparent 1.2px)"
    backgroundSize: "24px 24px"
    description: "Faint dot-grid background pattern used as an overlay on light surfaces or as decoration in corners of cards."
  tilt-card:
    transform: "rotate(±2deg) or rotate(±8deg)"
    description: "Card with intentional tilt. Stat cards alternate -2deg / +2deg; decorative rectangles tilt up to ±12deg. The tilt is the system's playful structural signature."
  nav-btn:
    width: 48px
    height: 48px
    border: "3px solid {colors.black}"
    background: "{colors.white}"
    boxShadow: "{shadows.small}"
    description: "Square nav arrow button. Hover translates -2/-2 and grows shadow; active translates 2/2 and shrinks shadow."
  slide-counter:
    border: "3px solid {colors.black}"
    background: "{colors.white}"
    padding: "10px 18px"
    boxShadow: "{shadows.small}"
    description: "Persistent slide counter pill at bottom-left. Space Grotesk uppercase NN / NN format."
---

## 概览

BlockFrame 是一套**极繁新粗野演示系统**，建立在五条结构法则上：每个区域都有 4px 黑描边，每个抬升元素都有 8px 硬偏移阴影，每个角都是方的，每种强调色都是饱和粉彩，每套布局都允许有一点歪。系统的乐趣来自这些法则的刻意碰撞——带框卡片碰上带框卡片，阴影叠上阴影，倾斜装饰故意刺穿网格。

字体系统以 **Inter**（字重 400–900）为轴，承担展示、正文和统计——标题用字重 800–900、紧全大写加负字距，正文用字重 500、句首大写，卡片标题用字重 700 全大写。**Space Grotesk**（字重 400–700）是第二面孔，当作准等宽标签声线，用于 eyebrow、幻灯片计数器、统计标签、等宽标签，以及任何应读成「系统」而不是「编辑」的 chrome。面孔组合故意普通——两套都是广泛可用的开放无衬线——但处理方式（重全大写 Inter + 宽字距 Space Grotesk）给它们鲜明的新粗野语域。

色板围绕**五种饱和粉彩**（粉 `#FE90E8`、蓝 `#C0F7FE`、绿 `#99E885`、黄 `#F7CB46`、奶油 `#FFDC8B`），外加用于描边和文字的**纯黑**（`#000000`）、用于干净卡片填充的**白**（`#FFFFFF`），以及用于暖画布的**灰白**（`#FFFDF5`）。粉彩不是细微点缀——它们是全出血表面填充。典型幻灯片组让每一页循环不同色底（灰白封面 → 蓝 intro → 灰白内容 → 绿图表 → 粉引文 → 黄分割 → 灰白时间线 → 蓝统计 → 奶油团队 → 黑收束）。这种色彩循环是系统的主节奏。

纵深是 **4px 和 8px 的硬偏移阴影**，永远实心黑，永远零模糊，永远落在右下。更大元素用 8px，更小 chrome 用 4px。close-frame 用单一 12px **黄**偏移（系统里唯一的彩色阴影）作为最响的纵深陈述，反色 close-frame 在黑表面上配 6px **白**阴影。主卡片描边是 4px solid 黑，次级 chrome 是 3px solid 黑。描边重量和阴影尺寸紧耦合——4px 描边配 8px 阴影；3px 描边配 4px 阴影。

**密度哲学：舒适地密。** 塞满时系统读起来权威，稀疏时读起来怯。典型表面承载：一条 label-pill eyebrow + 一个大标题 + 一张多卡片网格（3–6 张卡）+ 至少一个装饰元素（倾斜矩形、星爆、条纹块、角括号、装饰点）。区域内的空空间读起来像「坏掉」——每张卡都应填满，每张网格都应完整。系统的乐趣依赖同一画框里许多带框物件的视觉嘈杂。

**关键特征：**
- 主卡片 4px solid 黑描边，次级 chrome 3px——从不能更细。
- 主卡片 8px 硬偏移阴影，次级 chrome 4px——实心黑，零模糊。
- 五粉彩色板（粉、蓝、绿、黄、奶油）加黑、白、灰白——在表面间循环。
- Inter 字重 800–900 全大写加负 tracking 是展示声线；Space Grotesk 字重 600 全大写加 0.08em 字距是标签声线。
- 到处都是方角，除了统计卡上一个圆形强调点。
- 倾斜装饰元素（旋转矩形、星、徽章）故意刺穿网格。
- Label pills（`{components.label-pill}`）带 3px 描边、4px 偏移阴影和粉彩填充变体——通用章节 eyebrow。
- 彩色填充大胆而饱和；粉彩用作面板底，不是浅点缀。
- 黄是默认 CTA 色；黑是默认收束表面色。
- 星爆、条纹块和点网格是可复用的装饰注意力单元。

## 颜色

### 色板

- **Black**（`{colors.black}` — `#000000`）：结构色。每条描边、每一个主文字瞬间、每一条阴影。纯黑，无暖偏。系统的对比锚。
- **White**（`{colors.white}` — `#FFFFFF`）：默认卡片填充。用在每一张主卡片上，也作为 label-pill 和 nav-button 的背景。纯白，无暖意。
- **Off-white**（`{colors.offwhite}` — `#FFFDF5`）：暖画布调。没有粉彩底时的默认正文/幻灯片背景。比纯白略暖，好让上面的白卡片仍有分层感。
- **Pink**（`{colors.pink}` — `#FE90E8`）：高调糖果品红。用作全表面底、label-pill 填充、icon-square 填充、star-burst 填充，以及粉彩图表系列之一。五种粉彩里最饱和的。
- **Blue**（`{colors.blue}` — `#C0F7FE`）：浅青冰蓝。用作全表面底（「intro」和「stats」感觉）、label-pill 填充、icon-square 填充，以及图表系列。
- **Green**（`{colors.green}` — `#99E885`）：明亮春绿。用作全表面底、label-pill 填充、icon-square 填充、stripe-block 对角图案，以及图表系列。
- **Yellow**（`{colors.yellow}` — `#F7CB46`）：CTA 色。用作默认按钮填充、close-frame 阴影色、list-number 方块、feature-deco 缺口，以及 label-pill 填充。最亮、最抓注意力的粉彩。
- **Cream**（`{colors.cream}` — `#FFDC8B`）：暖黄奶油。比黄更软，比 offwhite 更饱和。用作全表面底（「团队」或「封面」感觉）、label-pill 填充，以及第三图表强调。

### 默认

- **默认表面背景**：内容重的表面用 `{colors.offwhite}`；需要更强底的表面在 `{colors.cream}`、`{colors.blue}`、`{colors.pink}`、`{colors.green}`、`{colors.yellow}` 间循环。循环就是节奏；许多页停在同一底上会压扁系统。
- **默认标题色**：所有浅/粉彩表面上用 `{colors.black}`；黑收束表面上用 `{colors.white}`。
- **默认正文字色**：所有浅/粉彩表面上用 `{colors.black}`；深色表面上用 `{colors.white}` 或 `{colors.cream}`。
- **默认描边色**：`{colors.black}` ——永远。除了反色 close-frame 上的 4px 白描边，任何地方都没有彩色描边。
- **默认卡片填充**：`{colors.white}`。只有卡片属于多卡行、每张卡需要鲜明色彩身份时才用粉彩填充（例如时间线步骤行，每一步不同粉彩）。
- **默认按钮填充**：`{colors.yellow}`。其他粉彩也能用，但黄是系统的主「点这里」信号。
- **默认 label-pill 底**：`{colors.white}`；粉彩变体（`{colors.pink}`、`{colors.blue}`、`{colors.green}`、`{colors.yellow}`、`{colors.cream}`）发出章节类型信号或装饰 eyebrow。
- **统计卡上的默认装饰强调**：12px 圆（`{components.stat-deco-dot}`），粉彩填充——在卡片间循环粉、蓝、绿、黄。
- **默认图表色板顺序**：粉 → 蓝 → 绿（三系列），黄和奶油留给额外系列。

粉彩在角色上可互换——没有一种带固定语义（绿不是「成功」，色板里根本没有红）。靠视觉并置配对：粉 + 蓝 + 绿是最常见的三人组；奶油 + 黄是暖对；蓝 + 粉是冷暖对比。

## 字体

### 字族
系统跑两套面孔。

**Inter**（字重 400–900）是展示、正文、标题和统计脸。Hero/收束标题和引文用字重 900，主标题用字重 800，中标题和卡片标题用字重 700，正文用字重 500。展示字重永远全大写加负字距（-0.02 到 -0.03em）；正文字重永远句首大写、默认 tracking。重全大写展示与字重 500 句正文之间的对比，就是系统的排印节奏。

**Space Grotesk**（字重 400–700）是标签和 chrome 脸。label-pill 用字重 600（13px，0.08em 字距，全大写），等宽元数据呼出用字重 500。这张脸技术上不是等宽，但其略几何性格 + 宽字距处理让它读成系统的「代码」声线。

不要引入第三张脸。Inter + Space Grotesk 配对就是全部排印色板。

### 字号阶梯

| Token | 字号 (clamp / px) | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.heading-xl}` | 48–96px clamp | Inter | 900 | Hero 或封面级标题 |
| `{typography.heading-lg}` | 32–64px clamp | Inter | 800 | 主章节标题 |
| `{typography.heading-md}` | 24–40px clamp | Inter | 700 | 区域标题、图表标题 |
| `{typography.close-title}` | 40–80px clamp | Inter | 900 | 收束陈述标题（反色表面） |
| `{typography.quote-text}` | 28–52px clamp | Inter | 900 | 引文正文——永远全大写 |
| `{typography.stat-number}` | 36–64px clamp | Inter | 900 | 统计数字 |
| `{typography.card-title}` | 22px | Inter | 700 | 功能卡标题——全大写 |
| `{typography.step-num}` | 48px | Inter | 900 | 时间线步骤内的数字（不透明度 0.6） |
| `{typography.body}` | 16–20px clamp | Inter | 500 | 标准正文段落 |
| `{typography.body-card}` | 15px | Inter | 500 | 紧凑卡内正文 |
| `{typography.list-body}` | 16px | Inter | 500 | 编号列表正文 |
| `{typography.label}` | 13px | Space Grotesk | 600 | label-pill 内文字 |
| `{typography.mono-tag}` | 14px | Space Grotesk | 600 | 等宽标签/徽章、幻灯片计数器 |
| `{typography.mono-meta}` | 15px | Space Grotesk | 500 | 行内等宽元数据 |
| `{typography.subtitle-mono}` | 18px | Space Grotesk | 500 | Hero 副标题 / 收束副标题 |
| `{typography.counter}` | 14px | Space Grotesk | 700 | 持续幻灯片计数器（NN / NN） |
| `{typography.legend-item}` | 13px | Space Grotesk | 600 | 图表图例标签 |

### 默认

- **Hero 或封面标题的默认字号**：`{typography.heading-xl}`（48–96px）。永远全大写，永远字重 900，永远 -0.03em tracking。
- **主章节标题的默认字号**：`{typography.heading-lg}`（32–64px）。全大写，字重 800，-0.02em。
- **区域或图表标题的默认字号**：`{typography.heading-md}`（24–40px）。默认唯一不加全大写的 Inter 标题——不过允许全大写。
- **统计数字的默认字号**：`{typography.stat-number}`（36–64px）。字重 900，行高 1。
- **正文段落的默认字号**：`{typography.body}`（16–20px clamp）。字重 500，句首大写，行高 1.6。
- **eyebrow 标签的默认字号**：`{typography.label}`（13px），放在 `{components.label-pill}` 里。
- **任何 Inter 展示的默认字重**：800 或 900。Inter 展示用字重 700 读起来「差不多了」；只在 `{typography.heading-md}` 或卡片标题上用 700。
- **任何 Inter 正文的默认字重**：500。正文 400 太轻，正文 700 过大。
- **任何 Space Grotesk 标签/chrome 的默认字距**：0.05–0.10em。宽字距是这张脸的「chrome」信号。
- **任何 Inter 展示的默认字距**：-0.01em（heading-md）到 -0.03em（heading-xl）。没有负 tracking 的展示读起来像没处理过。

拿不准该用哪个标题 token 时，幻灯片的主文字瞬间默认 `{typography.heading-lg}`（32–64px）。`{typography.heading-md}` 用于页内区域或图表标题。

### 招牌处理

这些处理在**使用对应元素类型时不可省略**：

- **每一个 Inter 展示元素（heading-xl、heading-lg、quote-text、close-title）都是全大写。** 本系统不存在字重 800+ 的句首大写 Inter 展示。全大写 + 重字重 + 负 tracking 的组合就是视觉身份。
- **每一个 Inter 展示元素都用负字距**（-0.01 到 -0.03em）。没有负 tracking 的展示读起来像默认 Inter，那是完全不同的美学。
- **每一个 label-pill 都带着 3px 描边 + 4px 阴影 + 全大写 Space Grotesk 文字** 的组合。缺少这三样的标签不是 label-pill——只是散落的文字元素。
- **每一个 card-title 都是全大写 Inter 字重 700。** 句首大写的卡片标题会打断粗野节奏。
- **每一个 Space Grotesk 标签/chrome/计数器都是全大写、0.05–0.1em 字距。** 本系统除贴近正文的元数据（mono-meta、行内等宽）外，不存在句首大写 Space Grotesk。
- **每一个统计数字都是 Inter 字重 900、行高 1。** 统计数字是展示瞬间，不是数据 chrome。
- **每一个 Inter 正文块都是句首大写、行高 1.6（紧凑卡正文用 1.5）。** 全大写或紧行高的正文读起来是坏的。
- **时间线步骤卡内的步骤数字是 48px、字重 900、不透明度 0.6。** 降低不透明度是强制的——全不透明度步骤数字会压过步骤标题。

### 排版原则

声线对比是 **粗全大写展示 ↔ 句正文 ↔ 宽字距标签**。从不用斜体。从不用下划线。唯一的强调机制是 Inter 阶梯内的字重对比，以及全大写/句首大写切换。

展示元素应被允许**主导画布**。系统为海报级排印而建；把 heading-xl 读成小字号会塌掉它的性格。靠向每一个 clamp 的上界。

## 版式

### 画布系统
系统以每页 `100vw × 100vh` 为目标。幻灯片绝对定位，通过 `.active` 类上的 `display: none` / `display: flex` 切换。默认幻灯片内边距四面都是 60px。含底部锚定网格的幻灯片（时间线、团队网格、带统计列的图表）额外带 `padding-bottom: 110px`，以避开固定的幻灯片计数器和导航 chrome。

默认幻灯片 flex 方向是 column，`justify-content: center`。两列分割（intro 页、图+文分割）时，flex 方向切到 row。

### 内边距与间距阶梯

| Token | 值 | 用途 |
|---|---|---|
| `{spacing.slide-pad}` | 60px | 从边缘到内容的默认幻灯片内边距 |
| `{spacing.card-pad-lg}` | 60px | Hero-frame 和 quote-frame 内部内边距 |
| `{spacing.card-pad-md}` | 36px | 功能卡内部内边距 |
| `{spacing.card-pad-sm}` | 28px | intro-card 内部内边距 |
| `{spacing.card-pad-xs}` | 22px | 团队卡和小单元格内边距 |
| `{spacing.gap-lg}` | 48px | 主区块之间的间距（页头到网格） |
| `{spacing.gap-md}` | 32px | 功能卡之间的间距 |
| `{spacing.gap-sm}` | 24px | intro 卡、统计卡之间的间距 |
| `{spacing.gap-xs}` | 16px | 列表项内部、卡内内容间距 |
| `{spacing.pad-bottom-clearance}` | 110px | 底部内边距预留，以避开固定导航 chrome |

### 持续 Chrome
每一页出现三个元素：
- **幻灯片计数器** 在左下 —— 3px 黑描边、白填充、4px 阴影，Space Grotesk 14px 字重 700 全大写，NN / NN 格式。
- **导航控件** 在右下 —— 两个 48px 方形导航按钮，3px 描边、白填充、4px 阴影。
- 幻灯片计数器和导航控件不是幻灯片构图的一部分——它们活在 `.slides-container` 外面，叠在底边上。

### 卡叠卡结构
系统的主布局模式是 **底上叠底上的卡**。典型一页放一块色底表面，上面坐一张白卡，4px 黑描边 + 8px 阴影，里面可能再含更小的卡或 icon-square。每一层嵌套带着自己的描边重量：外卡 4px，内 chrome 3px。这种嵌套带框结构给系统密、塞满的感觉。

### 装饰扰乱
倾斜装饰元素（旋转矩形、星、徽章、点网格）绝对定位在幻灯片和卡表面上，故意刺穿网格。它们不是「背景装饰」——它们是构图的一部分。没有任何装饰元素的表面读起来太干净。

## 纵深与抬升

### 硬偏移阴影栈
系统使用三个主阴影值：
- **`{shadows.default}`** = `8px 8px 0px {colors.black}` ——主卡阴影。用于 hero-frame、功能卡、quote-frame、chart-frame，以及任何抬升卡。
- **`{shadows.small}`** = `4px 4px 0px {colors.black}` ——次级 chrome 阴影。用于 intro-card、stat-card、team-card、timeline-step、label-pill、button-primary、nav-btn、slide-counter。
- **`{shadows.hover}`** = `6px 6px 0px {colors.black}` ——按钮和导航的悬停态。配合 -2/-2 变换触发。

所有阴影都是实心黑、零模糊、固定右下偏移。悬停上的阴影 + 变换配对创造「从纸上掀起」的交互签名——元素平移 -2/-2，同时阴影长到 6/6，模拟掀起。

### 反色阴影
在深色收束表面上，阴影反转颜色但保持偏移逻辑：
- **`{shadows.close-yellow}`** = `12px 12px 0px {colors.yellow}` ——系统最响的纵深陈述。用在 close-frame 上，让反色表面尽管深底仍读成「抬升」。
- **`{shadows.close-white}`** = `6px 6px 0px {colors.white}` ——用在 close-btn 上，在黑底上维持抬升。

这些彩色阴影是「阴影永远是黑」规则的唯一例外，且只出现在深色表面上。

### 基于描边的纵深
系统大部分表观分层来自 4px 或 3px 墨描边，而不是阴影。有描边没有阴影的卡仍读成「表面上的物件」——阴影才让它读成「掀起」。抬升卡用阴影；多卡网格里的次级卡只用描边，叠阴影会合成噪声。

### 倾斜元素当纵深
系统好玩的纵深签名是 **倾斜**。统计卡交替 -2deg / +2deg 旋转。装饰粉矩形倾斜到 ±12deg。Hero frame 上的黄按钮页签倾斜 -3deg。这些倾斜故意打断网格对齐，在不用真实透视或阴影的情况下创造感知维度。

## 形状与处理

### 圆角
- **结构上一切都是 0px** ——卡、label-pill、按钮、icon-square、list-number、头像、徽章。方角不可商量。
- **50%（圆）** 只用于 stat-deco 点（钉在统计卡上的 12×12 圆形强调）。这是系统里唯一的圆形状。

方角纪律是系统的结构身份。给任何卡或芯片加圆角，立刻读成另一种美学。

### 描边粗细
- **4px solid `{colors.black}`** ——用于主卡片（hero-frame、功能卡、quote-frame、chart-frame、团队卡描边、timeline-step 描边、stat-card 描边）以及 close-frame 反色（黑底上 4px solid 白）。
- **3px solid `{colors.black}`** ——用于次级 chrome（label-pill、按钮、intro-card、icon-square、list-number、头像、corner-bracket、nav-btn、slide-counter、stripe-block、star-burst）。3px 重量发出「次级结构」信号，相对 4px「主结构」。
- **2px solid `{colors.black}`** ——只用于图例色块（16×16 图表色块）和 stat-deco 点。最细的描边重量，留给原子 chrome。
- **4px solid `{colors.white}`** ——只用于反色 close-frame、visual-box，以及深色 split-visual 表面上的 ::after 偏移框。

描边重量阶梯（2 / 3 / 4）是固定的。没有 1px 描边，没有 5px+ 描边。

### 装饰元素类型

**Label-pill** ——方形带框胶囊（3px 黑描边，4px 阴影），粉彩或白填充，Space Grotesk 13px 字重 600 全大写文字，0.08em 字距。通用章节 eyebrow。

**Corner-bracket** ——卡角上的两个 L 形括号（或四个做全包围），3px 黑描边。创造框中框装饰母题。

**Star-burst** ——经 CSS clip-path 裁出的 10 角星，3px 描边，粉彩填充。装饰注意力抓手，钉在 close-frame 和功能卡的角上。

**Stripe-block** ——对角 4px 开、8px 关的条纹图案，黑 + 一种粉彩色，外框 3px 黑描边。用在海报级表面上的装饰注意力块。

**Dot-grid** ——1.2px radial-gradient 点图案，24×24 间距。用作幻灯片角落的淡装饰叠层，不透明度 30–40%。

**Feature-deco notch** ——48×48 黄方块，3px 黑描边，绝对定位从功能卡顶边凸出。缺口打断卡的顶描边，暗示它被「钉上去」。

**Icon-square** ——64×64 粉彩方块，3px 黑描边，内含单个全大写字母字形，Inter 字重 700 / 28px。用作功能卡图标。

**Stat-deco dot** ——12×12 圆，2px 黑描边，粉彩填充，钉在统计卡右上。系统唯一的圆形状。

**List-number** ——36×36 黄方块，3px 黑描边，内含 Space Grotesk 14px 字重 700 数字。用作编号列表的项目符号。

**Avatar-square** ——72×72 粉彩方块，3px 黑描边，内含两个全大写缩写，Inter 字重 900 / 28px。用在团队网格里；填充在粉彩间循环。

**Step-connector** ——28×4 水平黑条，钉在时间线步骤卡右缘中高。在视觉上把相邻步骤连成水平流。

**Tilted decoration** ——任何带 rotate(±2deg 到 ±12deg) 变换的矩形、徽章或星。倾斜是对网格的故意扰乱；没有它，系统读起来太整齐。

## 该做与不该做

### 该做

- 给主卡片（`{components.card-elevated}`、hero-frame、quote-frame）加 4px solid 黑描边，次级 chrome 用 3px。描边重量阶梯是系统的结构脊梁。
- 每条 4px 描边配 8px 偏移阴影，每条 3px 描边配 4px 偏移阴影。描边/阴影耦合不可商量。
- 让幻灯片背景在粉彩色板间循环——offwhite、cream、blue、pink、green、yellow——保持幻灯片组视觉有节奏。许多页停在一色上会压扁系统。
- 每一个 Inter 展示元素都设成全大写、负字距（-0.01 到 -0.03em）、字重 800+。这个组合就是排印身份。
- 把 `{components.label-pill}`（3px 描边、4px 阴影、粉彩填充、Space Grotesk 全大写 0.08em）当作每个区域的通用章节 eyebrow。
- 给装饰矩形、统计卡、星和徽章加倾斜（±2deg 到 ±12deg）。故意错位是系统好玩的签名。
- 用 `{colors.yellow}` 作为默认按钮色。黄配 3px 黑描边和 4px 黑阴影，是系统的「点这里」声线。
- 把阴影渲染成实心黑、零模糊，永远右下偏移。硬边阴影就是纵深语言。
- 每块表面加一个装饰元素（star-burst、stripe-block、dot-grid、corner-bracket、倾斜矩形）。视觉嘈杂是系统能量的一部分。
- 收束表面用纯黑 `{colors.black}`，白字，close-frame 上 12px 黄偏移阴影。反色深表面是系统最响的对比瞬间。

### 不该做

- 不要给卡、按钮、label-pill、icon-square 或头像圆任何角。除 stat-deco 点（12px 圆）外禁止 border-radius。
- 不要模糊任何阴影。每条阴影都是零模糊硬边。本系统不存在 `box-shadow: 0 4px 12px rgba(0,0,0,0.1)`。
- 不要用彩色描边。描边永远纯黑，除了 close-frame 上反色的 4px 白描边。
- 不要用句首大写的 Inter 展示字重。heading-xl、heading-lg、quote-text、close-title 和 card-title 必须全大写。
- 不要在没有负字距的情况下设 Inter 展示。默认 tracking 的重字重 Inter 读起来像另一套系统。
- 不要引入第六种粉彩。色板锁在粉、蓝、绿、黄、奶油。加紫、橙或红会打断策划过的糖果色板。
- 不要省略区域上的 label-pill。从背景直接跳到标题、没有 eyebrow 标签，会打断系统的编辑节奏。
- 不要把 label-pill 渲染成纯文字。3px 描边 + 4px 阴影 + 粉彩填充的组合才定义这颗胶囊。
- 不要用模糊或彩色正文。正文在浅表面上是实心黑，在深表面上是实心白或奶油。
- 不要让每张卡都完美对齐。统计卡、装饰和徽章上的倾斜，才给系统手作能量。

## 响应式行为

BlockFrame 设计成 **1920×1080 演示系统**（有效 100vw × 100vh）。尺寸对字体用 CSS `clamp()`，对描边、阴影和结构内边距用固定 px。系统为窄视口提供三个组件级断点。

### 缩放行为
- Heading-xl 随视口宽度从 48px → 96px。
- Heading-lg 从 32px → 64px。
- 正文从 16px → 20px。
- 描边（3px、4px）、阴影（4px、8px）和结构内边距（60px slide-pad）固定，不缩放。

### 组件断点
- `max-width: 1024px` ——幻灯片内边距从 60px → 40px，两列分割垂直堆叠，功能卡行垂直堆叠，时间线轨道垂直堆叠并隐藏 step-connector，统计网格塌成 2 列，团队网格塌成 2 列。Split visual 失去左边框，改得顶边框。
- `max-width: 640px` ——统计网格塌成 1 列，团队网格塌成 1 列，hero-frame 内边距缩到 32px，quote-frame 内边距缩到 32px。

### 演示行为
- 用 `ArrowRight` 或 `Space` 前进。
- 用 `ArrowLeft` 后退。
- 水平触摸滑动，阈值 50px，前进/后退。
- 幻灯片过渡是即时的（`.active` 类上 `display: none` ↔ `display: flex`），没有交叉淡入。

### 打印行为
系统没有 `@media print` 规则。幻灯片绝对定位且同一时间只有一页可见——打印只产出活动页。静态导出时，逐页截图可保留全部描边、阴影和装饰（全是 CSS，不是图像资源）。

### 交互状态
- 按钮和导航按钮悬停时平移 -2/-2，阴影长到 6px（`{shadows.hover}`）；按下时平移 2/2，阴影缩到 2px。这种悬停按压行为对演示系统不寻常；它反映 BlockFrame 作为幻灯片组与交互产品模型的混合身份。

## CJK 与国际内容

用本模板承载中文（或其他 CJK）内容时，把拉丁字体栈换成对等的中文搭配，并套用通用 CJK 调整。所有推荐中文字体经 CDN 加载——无需安装。

### 推荐中文搭配

| 角色 | 拉丁（默认） | 中文对应 |
|---|---|---|
| 展示 / hero / 引文 / 收束标题 / 统计数字 | Inter 800–900（全大写，负 tracking） | 思源黑体 Noto Sans SC 900（句首大写，字距 0） |
| 卡片标题 | Inter 700（全大写） | 思源黑体 Noto Sans SC 700（无变换） |
| 正文 / 列表正文 | Inter 500 | 思源黑体 Noto Sans SC 400 |
| 标签 / 等宽标签 / 计数器 / 图例 | Space Grotesk 600–700（全大写，0.05–0.1em 字距） | 思源黑体 Noto Sans SC 600（无变换，无字距） |

### 混排策略

**策略 A** ——单一 CJK 字族，自带拉丁字形覆盖。把每个文字元素设成 `font-family: 'Noto Sans SC', sans-serif`。思源黑体带能与汉字干净配对的拉丁字形，所以混排句子以一张一致面孔渲染。拉丁原作里 Inter / Space Grotesk 的区分通过字重对比保留：字重 900 承担粗野展示角色，字重 600 承担标签角色，字重 400–500 承担正文。即使面孔对比没了，视觉层级仍在。

### 加载

加到模板的 `<head>`：

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;600;700;900&display=swap" rel="stylesheet">
```

### 通用 CJK 调整

- **行高**：相对拉丁规格增加约 15–25%。正文 1.75–1.85（从 1.6 上调），展示 1.15–1.25（从 0.95–1 上调）。拉丁展示压缩到 0.95 行高；CJK 在那种压缩下会垂直碰撞。
- **字距**：每一段 CJK 都设为 0。模板里 Inter 展示的负 tracking（−0.02 到 −0.03em）会重叠 CJK 笔画，读起来是坏的；Space Grotesk 标签上 0.05–0.1em 的正字距在方形字形上读起来发空。
- **文本变换**：不要对中文应用 `uppercase`——CJK 没有大小写。拉丁原作里每一个 Inter 展示标题（heading-xl、heading-lg、quote-text、close-title、card-title）都用 `text-transform: uppercase`；CJK 段要去掉。每一个 label-pill、计数器和 chrome 元素也用全大写；也要去掉。
- **标点**：用全角中文标点（，。：；！？「」（））。
- **展示标题不加句号**：中文排印惯例在展示级标题上省略末尾的 。
- **中西文之间的空格（盘古之白）**：每个汉字与相邻拉丁字符或数字之间插入 ASCII 空格。写 `BlockFrame 设计系统`，不要写 `BlockFrame设计系统`。
- **一句一面孔**：思源黑体以统一风格覆盖 CJK 和拉丁字形——让它处理混排句。不要让浏览器在词中切到 Inter 或 Space Grotesk。

### 本系统的美学备注

拉丁原作的排印身份完全建立在 Inter 展示上的 **重全大写 + 负 tracking** 组合。CJK 没有大小写，所以这个信号消失。系统能活下来，是因为身份是 **80% 结构、20% 排印**：4px 黑描边、8px 硬偏移阴影、五粉彩色板、倾斜装饰、label-pill、星爆、条纹块和点网格做粗野工作。把思源黑体 900 设成句首大写、同样大的字号；块状黑压粉彩 + 硬阴影取景，无论字体是否大写都读成粗野。

label-pill（Space Grotesk 600 全大写、0.08em 字距、3px 描边 + 4px 阴影、粉彩填充）会失去全大写 + tracking 等宽性格。中文 label-pill 用思源黑体字重 600、字距 0、略紧的 fontSize（11–12px 而不是 13px）——带框胶囊形状和阴影做 chrome 识别工作。保持粉彩填充轮换（粉 / 蓝 / 绿 / 黄 / 奶油）完整；这是描边本身之后系统最可识别的信号。

### 已知 CJK 缺口

- **没有 CDN 中文等宽面孔来做「系统读数」声线。** Space Grotesk 的准等宽角色（label-pill、计数器、mono-tag、幻灯片计数器 NN / NN）依赖其略几何性格加上宽字距全大写处理。两者在 CJK 翻译里都不存活。幻灯片计数器和图表图例可以保留拉丁数字 + 拉丁标签；纯中文 chrome 则靠胶囊描边 + 阴影 + 粉彩填充发出「标签」信号，而不是靠排印处理。
- **「全大写粗野」身份变弱。** 系统最鲜明的排印决定是「重全大写 Inter 加负 tracking」——这个信号在 CJK 里无法替代。补偿方式是更用力靠结构元素：更多装饰扰乱（额外倾斜矩形、星爆、条纹块），幻灯片间更饱和的粉彩底轮换，以及略紧的阴影偏移，以补偿更平静的排印基线。

## 迭代指南

1. 任何新卡都用 4px 或 3px solid 黑描边 + 匹配重量的偏移阴影（8px 或 4px）。永远不要用缺其中一样的卡。
2. 任何新区域以粉彩填充的 `{components.label-pill}` eyebrow 开头，然后是全大写 Inter 字重 800+ 的标题，然后是内容。标签-标题-内容序列是系统的编辑节奏。
3. 任何新标题用全大写 Inter、负字距、字重 800–900。主瞬间用 `{typography.heading-lg}`（32–64px），封面/hero 级用 `{typography.heading-xl}`（48–96px）。
4. 任何新强调或表面填充从五粉彩色板里挑（粉、蓝、绿、黄、奶油）——永远不要引入第六种粉彩。
5. 任何新 CTA 用 `{components.button-primary}` 模式：3px 黑描边、黄填充、4px 黑阴影、Inter 字重 700 / 16px。悬停掀起 -2/-2，阴影长到 6px。
6. 任何新图表按粉 → 蓝 → 绿循环系列顺序，黄/奶油留给额外系列。图例色块用 2px 黑描边。
7. 任何新统计或指标用 Inter 字重 900 + 行高 1 做数字，下面配 Space Grotesk 全大写标签。用粉彩色的 `{components.stat-deco-dot}` 装饰卡片。
8. 任何新幻灯片至少加一处装饰扰乱（倾斜矩形、star-burst、stripe-block、dot-grid 角、corner-bracket 框）——空表面显得怯。
9. 任何新收束风格表面用纯 `{colors.black}` 底配白字、4px 白描边 close-frame，以及 12px 黄偏移阴影。这是唯一允许的彩色阴影。
10. 如果表面太吵，丢掉一件装饰——不要丢掉描边或阴影。描边和阴影是结构；装饰是可调的。

## 已知缺口

- **Inter 和 Space Grotesk 从 Google Fonts 加载**，经由行内 `@import`。除 `sans-serif` 和 `monospace` 外没有系统回退——Google Fonts 失败的环境里，系统塌成系统默认，失去身份。
- **系统在 `<style>` 块内使用 `@import`**，而不是 `<link>` preconnect。这比标准 `<link>` 做法更慢，可能推迟排印的首次绘制。
- **图表渲染为行内 SVG，坐标硬编码**（`viewBox="0 0 800 360"`，每个 `<rect>` 硬编码 `x/y/width/height`）。加新图表页需要手动坐标运算；没有数据绑定层。
- **按钮上的悬停/按下态假定有指针设备。** 在触摸设备上，掀起-按下反馈只在点按时触发，可能感觉不一致。
- **统计卡上的倾斜用 `:nth-child(odd)` -2deg 和 `:nth-child(even)` +2deg 硬编码。** 重排卡片会改变哪张往哪边倾——除了排序外没有逐卡倾斜控制。
- **装饰星使用带 10 个点的 CSS clip-path 多边形。** 不支持 clip-path 的浏览器（非常老的 IE/Edge）会把星渲染成彩色矩形。
- **幻灯片计数器和导航控件在底边叠在幻灯片内容区上。** 某些页（slide-4、slide-9）上的 110px 底部内边距预留了空间，但其他页的内容可能挤到左下计数器胶囊。
- **黑收束表面用纯 `#000000` 底配白字** ——无障碍上这是高对比、没问题，但这块表面上的彩色装饰（黄阴影、白描边）在小尺寸下过不了 WCAG 颜色对比检查。
- **点网格背景是 CSS radial-gradient。** 在非常大的视口上，点可能小到读不成网格；在非常小的尺寸上，它们可能在视觉上并成实心噪声。
- **幻灯片之间没有过渡**，只有二元 display 切换。要加淡入或滑动动画，需要改 JS 并加过渡 CSS。
