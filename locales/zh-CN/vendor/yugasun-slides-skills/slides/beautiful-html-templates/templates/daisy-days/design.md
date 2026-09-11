---
version: alpha
name: Daisy Days
description: A cheerful, childlike presentation system built around the chunky display face Fredoka One and the rounded humanist sans Quicksand. The palette is a sunny garden — cream canvas, turquoise, soft pink, butter yellow, mint, lavender, peach, sky blue, and a single coral accent — with charcoal-brown 2D outlines wrapping every shape. Hard offset shadows in dark charcoal, generous border-radius, and hand-drawn SVG decorations (daisies, stars, suns, clouds, rainbows) anchor the aesthetic somewhere between a children's storybook spread and a sticker-sheet kawaii zine.

colors:
  cream: "#F5F0E6"
  turquoise: "#7ECDC0"
  soft-pink: "#F7C8D4"
  butter: "#FDE68A"
  mint: "#A8E6CF"
  lavender: "#D4A5E8"
  peach: "#FFCBA4"
  sky: "#A8D8F0"
  coral: "#F8635F"
  text-dark: "#2D2D2D"
  text-muted: "#6B6B6B"
  white: "#FFFFFF"

borders:
  primary: "3px solid {colors.text-dark}"
  thin: "2px solid {colors.text-dark}"

shadows:
  default: "6px 6px 0 {colors.text-dark}"
  small: "4px 4px 0 {colors.text-dark}"
  text-headline: "3px 3px 0 {colors.text-dark}"
  text-headline-soft: "3px 3px 0 rgba(0,0,0,0.2)"

typography:
  display:
    fontFamily: "'Fredoka One', cursive"
    fontSize: "clamp(3.2rem, 7vw, 6.5rem)"
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 0.02em
  headline:
    fontFamily: "'Fredoka One', cursive"
    fontSize: "clamp(2.5rem, 5vw, 4.5rem)"
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 0.02em
  title:
    fontFamily: "'Fredoka One', cursive"
    fontSize: "clamp(1.8rem, 3.5vw, 3rem)"
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: 0.02em
  subtitle:
    fontFamily: "'Fredoka One', cursive"
    fontSize: "clamp(1.3rem, 2vw, 1.8rem)"
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.02em
  label-display:
    fontFamily: "'Fredoka One', cursive"
    fontSize: "clamp(1rem, 1.5vw, 1.3rem)"
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.02em
  quote:
    fontFamily: "'Fredoka One', cursive"
    fontSize: "clamp(1.3rem, 2.5vw, 2rem)"
    fontWeight: 400
    lineHeight: 1.35
  body:
    fontFamily: "'Quicksand', sans-serif"
    fontSize: "clamp(0.95rem, 1.3vw, 1.15rem)"
    fontWeight: 500
    lineHeight: 1.6
  body-strong:
    fontFamily: "'Quicksand', sans-serif"
    fontSize: "clamp(0.95rem, 1.4vw, 1.15rem)"
    fontWeight: 600
    lineHeight: 1.5
  meta:
    fontFamily: "'Quicksand', sans-serif"
    fontSize: "clamp(0.8rem, 1.1vw, 0.95rem)"
    fontWeight: 600
    lineHeight: 1.45
  badge:
    fontFamily: "'Fredoka One', cursive"
    fontSize: "0.85rem"
    fontWeight: 400
    letterSpacing: 0.02em

spacing:
  pad-slide: "40px 60px"
  pad-card-lg: "48px 56px"
  pad-card-md: "32px 40px"
  pad-card-sm: "16px 24px"
  gap-grid-lg: "28px"
  gap-grid-md: "24px"
  gap-grid-sm: "14px"
  radius: "20px"
  radius-lg: "28px"
  radius-pill: "50px"
  radius-round: "50%"

canvas:
  width: 100vw
  height: 100vh

components:
  card:
    background: "{colors.white}"
    border: "3px solid {colors.text-dark}"
    borderRadius: "{spacing.radius}"
    boxShadow: "{shadows.default}"
  card-lg:
    background: "{colors.white}"
    border: "3px solid {colors.text-dark}"
    borderRadius: "{spacing.radius-lg}"
    boxShadow: "{shadows.default}"
  badge-pill:
    display: "inline-block"
    padding: "8px 20px"
    borderRadius: "{spacing.radius-pill}"
    border: "3px solid {colors.text-dark}"
    fontFamily: "'Fredoka One', cursive"
    fontSize: "0.85rem"
    background: "{colors.butter}"
  framed-header:
    description: "A two-part stacked card: a colored header strip (any accent surface) with rounded top corners and no bottom border, sitting flush above a white body with rounded bottom corners. The pair reads as a single unit with a tonal cap."
    headerBackground: "any accent surface"
    headerBorderRadius: "{spacing.radius-lg} {spacing.radius-lg} 0 0"
    bodyBackground: "{colors.white}"
    bodyBorderRadius: "0 0 {spacing.radius-lg} {spacing.radius-lg}"
    border: "3px solid {colors.text-dark}"
    boxShadow: "{shadows.default}"
  circle-dot:
    width: "48px"
    height: "48px"
    borderRadius: "{spacing.radius-round}"
    border: "3px solid {colors.text-dark}"
    fontFamily: "'Fredoka One', cursive"
    color: "{colors.white}"
    description: "Outlined colored disc holding a numeral or single letter. Used as timeline node, step marker, or list bullet anchor."
  circle-icon:
    width: "44px"
    height: "44px"
    borderRadius: "{spacing.radius-round}"
    border: "3px solid {colors.text-dark}"
    fontFamily: "'Fredoka One', cursive"
    background: "any accent surface"
    description: "Smaller cousin of circle-dot used as a card icon at the top of an info card."
  step-circle-lg:
    width: "90px"
    height: "90px"
    borderRadius: "{spacing.radius-round}"
    border: "3px solid {colors.text-dark}"
    fontFamily: "'Fredoka One', cursive"
    color: "{colors.white}"
    boxShadow: "{shadows.small}"
    description: "Oversized outlined disc used as a process step marker. Carries a hard offset shadow."
  avatar-circle:
    width: "100px"
    height: "100px"
    borderRadius: "{spacing.radius-round}"
    border: "3px solid {colors.text-dark}"
    background: "{colors.white}"
    boxShadow: "{shadows.small}"
    overflow: "hidden"
  bullet-dot:
    width: "20px"
    height: "20px"
    borderRadius: "{spacing.radius-round}"
    border: "2px solid {colors.text-dark}"
    background: "{colors.butter}"
    description: "Small outlined disc used as a ::before bullet for body list items, anchored 4px from the top of the line."
  list-dash:
    description: "A simple muted-text dash character used as a ::before bullet for compact in-card lists (day-card body)."
  legend-swatch:
    width: "18px"
    height: "18px"
    border: "2px solid {colors.text-dark}"
    borderRadius: "4px"
  decoration:
    position: "absolute"
    pointerEvents: "none"
    zIndex: 1
    description: "Hand-drawn SVG sticker (daisy, star, sun, cloud, rainbow) placed at slide corners and edges as atmospheric ornament. Often crops past the slide edge."
  nav-dots:
    position: "fixed"
    placement: "right edge, vertically centered"
    dotSize: "12px"
    dotBorder: "2px solid {colors.text-dark}"
    activeBackground: "{colors.butter}"
    activeTransform: "scale(1.2)"
  slide-counter:
    position: "fixed"
    placement: "bottom center"
    background: "{colors.white}"
    border: "3px solid {colors.text-dark}"
    borderRadius: "{spacing.radius-pill}"
    padding: "6px 20px"
    fontFamily: "'Fredoka One', cursive"
    boxShadow: "{shadows.small}"
  chart-container:
    background: "{colors.white}"
    border: "3px solid {colors.text-dark}"
    borderRadius: "{spacing.radius-lg}"
    boxShadow: "{shadows.default}"
    padding: "{spacing.pad-card-md}"
---

## 概览

Daisy Days 是一套**欢快、孩子气的演示系统**，根植于单一字体搭配：胖圆展示脸 **Fredoka One** 用于每一个标题，友好人文无衬线 **Quicksand** 用于每一行正文和元信息。视觉语言来自图画书插画和贴纸表 kawaii：每个形状都带炭色 2D 描边，每个抬升元素都投下实心偏移阴影，每个表面都是阳光花园色板里的粉彩色。

色彩哲学是**多粉彩加一次暖色爆点**。背景画布在柔奶油（`{colors.cream}`）与饱和粉彩（`{colors.turquoise}`、`{colors.soft-pink}`、`{colors.butter}`、`{colors.mint}`、`{colors.lavender}`、`{colors.peach}`、`{colors.sky}`）之间轮换。唯一的高饱和强调色是 `{colors.coral}`——克制地用在小标记点和标题描边上，从不做整面。彩色表面上的标题加 3px 炭色文字阴影，让展示文字与周围形状同样带描边外观；奶油上的标题保持平面。正文从不离开 `{colors.text-dark}` 或 `{colors.text-muted}`。

纵深是**二维、图形的**，不是摄影的。每个抬升元素都拿到 `{shadows.default}` 或 `{shadows.small}`——一块实心炭色块向右下偏移，零模糊。厚炭色描边加硬偏移阴影，给系统贴纸贴在纸上的感觉。没有渐变、没有光晕、没有玻璃效果。

招牌处理是**手绘 SVG 装饰层**。每个区域带着 3–7 个绝对定位饰物——黄心雏菊、多色星星、微笑太阳、蓬松云、拱形彩虹——聚在边角，常常以 `top:-30px / right:-20px` 裁出幻灯片边界。这些装饰坐在内容（`z-index:2`）后面的 `z-index:1` 层上，带着与系统其余部分相同的约 2px 炭色描边，把饰物与结构统一起来。

**密度哲学：满，但不挤。** 这套系统在每一页中央带一个聚焦内容区（一张卡、一个框、一个网格），边缘再加一圈慷慨的边角饰物时，读起来才有权威。空着的、没有装饰的边角读成坏了——饰物是结构构图的一部分，不是可选点缀。反过来，密集重叠的内容面板读成焦虑；系统要的是一个被框住、被环绕的主主体，不是三个互相抢的。目标是每页一个带描边/阴影的容器，边角装饰负责填满画布其余部分。

**关键特征：**
- 奶油（`{colors.cream}`）默认画布，粉彩表面轮换——每一页可以选不同的表面色。
- 全部标题 / 展示 / 引文文字用 Fredoka One；全部正文和元信息用 Quicksand 500/600。
- 每个形状和卡片都带 3px 实心炭色描边（`{colors.text-dark}`）加硬偏移阴影（`{shadows.default}` 或 `{shadows.small}`）。
- 慷慨圆角：标准卡 20px，特色卡 28px，徽章用胶囊（`{spacing.radius-pill}`），点和头像全圆。
- 手绘 SVG 饰物（雏菊、星星、太阳、云、彩虹）聚在边角并裁出幻灯片边缘，作为气氛层。
- 彩色表面上的标题永远带 3px 实心炭色文字阴影；奶油上的标题保持平面。
- 项目符号是彩色描边圆点（`{components.bullet-dot}`），不是字形。列表感觉像手排。
- 每页一个主内容容器，围着 3–7 个饰物。空边角是错的。

## 颜色

### 色板
- **Cream**（`{colors.cream}` — #F5F0E6）：默认画布。暖的灰白，读成纸料而不是数字白。用作 deck 的中性表面——标题开场、信息卡页、任何想感觉像图画书页的东西。
- **Turquoise**（`{colors.turquoise}` — #7ECDC0）：中饱和青绿。粉彩表面里最响的一种；响到上面的标题需要炭色文字阴影才能保持可读。
- **Soft Pink**（`{colors.soft-pink}` — #F7C8D4）：泡泡糖腮红。用作整面、页眉条颜色、日期标记填充，以及引语卡里的引号强调。
- **Butter**（`{colors.butter}` — #FDE68A）：黄油粉彩黄。导航点的激活态颜色、默认徽章填充、默认项目符号填充。当某物需要感觉被标出来时，它是系统的「高亮」色。
- **Mint**（`{colors.mint}` — #A8E6CF）：冷青瓷绿。表面色、页眉条颜色、圆形图标填充、时间线圆点颜色。
- **Lavender**（`{colors.lavender}` — #D4A5E8）：闷紫。表面、页眉条、标记点、日期标记——与 mint 和 soft-pink 同样灵活的角色。
- **Peach**（`{colors.peach}` — #FFCBA4）：暖粉彩橙。用作表面（通常在流程或序列页上）和强调。
- **Sky**（`{colors.sky}` — #A8D8F0）：粉彩蓝。表面和强调色，常与云装饰配对。
- **Coral**（`{colors.coral}` — #F8635F）：唯一的饱和强调色。只用做标记填充（编号点、时间线节点、步骤圆）和日期页眉——从不做整页表面。Coral 是系统的「看这里」色，用多了就失去冲击。
- **Text Dark**（`{colors.text-dark}` — #2D2D2D）：结构色。每条描边、浅表面上的每一段正文、每一道阴影、每一笔 SVG 描边。比纯黑略暖——读成炭，不是墨黑。
- **Text Muted**（`{colors.text-muted}` — #6B6B6B）：弱化文字色。副标题、标题下的描述、list-dash 项目符号、角色标签。
- **White**（`{colors.white}` — #FFFFFF）：默认卡片填充——每张卡、每个头像、每个图表容器内部。奶油画布上的卡片仍然拿白色内部，好让卡片边缘读得干净。

### 默认值
- **默认幻灯片背景**：`{colors.cream}`。当这一页想要一种色调性格时，用饱和粉彩表面（turquoise、soft-pink、mint、butter、lavender、peach、sky）；不想要时默认奶油。
- **默认卡片背景**：`{colors.white}`——在任何表面上，包括粉彩表面。白压粉彩是标准卡片处理。
- **默认标题颜色**：`{colors.text-dark}`——永远。
- **默认正文颜色**：主正文用 `{colors.text-dark}`，描述、角色标签、图注和副行用 `{colors.text-muted}`。
- **默认描边颜色**：`{colors.text-dark}`——永远。任何地方都没有彩色描边。
- **默认阴影颜色**：`{colors.text-dark}`——永远。阴影从不粉彩。
- **默认徽章填充**：`{colors.butter}`。
- **默认标记 / 强调填充**，当元素需要单一「注意」色时：`{colors.coral}`。需要一串标记时，在全套粉彩里轮换（coral → mint → sky → lavender → butter）做序列步骤和圆点。
- **framed-header 组件上的默认页眉条颜色**：任意粉彩表面——选与该页表面色最和谐的那种。

粉彩在表面层级上可互换——它们不携带固定语义（mint 不是「成功」，coral 不是「警告」）。选最服务该页情绪语域的表面。唯一规则：coral 留给小的高对比强调，不是表面。

## 字体

### 字族
系统从 Google Fonts 精确加载两套 web 字体：**Fredoka One**（单字重圆展示脸）和 **Quicksand**（人文无衬线，提供 400/500/600/700）。这对搭配就是全部排印身份。

Fredoka One 是胖的单字重展示脸——没有斜体、没有更轻变体、没有窄切。规格上展示字重读成 400，但因为字形又圆又满，视觉上表现得像重字重。系统里每一个标题、每一个题名、每一个步骤数字、每一段引文都跑 Fredoka One。没有例外——用 Quicksand 做标题或用 Fredoka One 做正文段落会立刻破坏系统。

Quicksand 承担其余一切：段落、列表项、角色标签、图注、日期卡正文列表、图例文字。Quicksand 500 是正文默认；600 是「稍强」变体，用于强调正文（欢迎列表项、信息卡描述、图例标签）；700 克制地用于引文作者署名。

### 展示、正文与标记字号阶梯

| Token | 字号 | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.display}` | clamp(3.2rem, 7vw, 6.5rem) | Fredoka One | 400 | 封面 / 开场 hero 标题 |
| `{typography.headline}` | clamp(2.5rem, 5vw, 4.5rem) | Fredoka One | 400 | 主幻灯片标题 |
| `{typography.title}` | clamp(1.8rem, 3.5vw, 3rem) | Fredoka One | 400 | 章节标题或 framed-header 标题 |
| `{typography.quote}` | clamp(1.3rem, 2.5vw, 2rem) | Fredoka One | 400 | 摘引正文 |
| `{typography.subtitle}` | clamp(1.3rem, 2vw, 1.8rem) | Fredoka One | 400 | 副标题、卡内标题 |
| `{typography.label-display}` | clamp(1rem, 1.5vw, 1.3rem) | Fredoka One | 400 | 小 Fredoka 标签——日期卡页眉、步骤标题 |
| `{typography.body-strong}` | clamp(0.95rem, 1.4vw, 1.15rem) | Quicksand | 600 | 强调正文——欢迎列表、信息卡描述 |
| `{typography.body}` | clamp(0.95rem, 1.3vw, 1.15rem) | Quicksand | 500 | 标准段落正文 |
| `{typography.meta}` | clamp(0.8rem, 1.1vw, 0.95rem) | Quicksand | 600 | 紧凑次级文字——日期卡列表、步骤说明、图例行 |
| `{typography.badge}` | 0.85rem | Fredoka One | 400 | 胶囊徽章内的文字 |

### 默认值
- **主幻灯片标题的默认字号**：`{typography.headline}`（clamp 2.5–4.5rem）。
- **封面级标题时刻的默认字号**：`{typography.display}`（clamp 3.2–6.5rem）。
- **段落的默认字号**：`{typography.body}`（clamp 0.95–1.15rem），Quicksand 500。
- **强调列表项的默认字号**：`{typography.body-strong}`（Quicksand 600）。
- **卡片标题下的描述或元信息图注的默认字号**：`{typography.meta}`，颜色 `{colors.text-muted}`。
- **章节 / framed-header 标题的默认字号**：`{typography.title}`。
- **大于约 1.3rem 的任何文字的默认字族**：Fredoka One。小于该值的任何文字的默认字族：Quicksand。这条尺寸阈值大致跟 Fredoka / Quicksand 的角色边界对齐。

拿不准时，这一页的主文字时刻伸手去拿 `{typography.headline}`，不要拿 `{typography.subtitle}` 或 `{typography.title}`（那是内容内部的标题，不是这一页的主声线）。

### 招牌处理
只要用到对应元素类型，这些处理就**不可省略**：

- **放在饱和粉彩表面上的每一个 Fredoka One 标题都带 3px 炭色文字阴影**（turquoise / mint 这类大胆表面用 `{shadows.text-headline}`，pink / lavender 这类更软表面用 `{shadows.text-headline-soft}`）。奶油上的标题保持平面，不加阴影。文字阴影让标题读成与系统其余部分同一套「描边」词汇。在彩色表面上跳过它读成坏了。
- **放在饱和表面上的标题把文字颜色切到 `{colors.white}`**；奶油上和浅粉彩卡片上的标题保持 `{colors.text-dark}`。搭配是白压饱和、深压奶油或卡片。
- **每一个正文列表项用描边彩色圆盘做项目符号，不是字形。** 默认填充是 `{colors.butter}`。项目符号渲染为带 2px 炭色描边的 `::before` 20px 圆，定位在第一行顶部往下 4px。
- **每一段引文都用 Fredoka 引号处理**：一个超大的 `"` 字形，颜色 `{colors.soft-pink}`，坐在引文文字上方。引文从不在没有引号锚点的情况下出现。
- **Quicksand 正文永远不大写。** 正文上没有展示式 ALL-CAPS 处理。Fredoka 自有性格，不需要喊。

### 排印原则
字号阶梯就是节奏。Fredoka One 不加斜体、不下划线、不以交替字重渲染——Fredoka 只有一个字重，句号。Quicksand 留在 500 / 600 / 700 阶梯里；即使有 400 或 800 也不要引入。Fredoka 的字距保持规格默认 `0.02em`。Quicksand 的字距保持 0。

把 Quicksand 混进标题（例如为了斜体短语）在本系统里不受支持——标题跑一张脸。如果标题需要不同的情绪语域，尺寸和颜色干活，不是换字体。

## 布局

### 画布系统
系统面向全视口——每一个 `.slide` 是 `100vw × 100vh`，`padding: 40px 60px`（默认幻灯片内边距）。幻灯片在使用 CSS scroll-snap（`scroll-snap-type: y mandatory`）的 `.slides-container` 里垂直叠放，把每一页锁到视口。导航由固定右缘导航点、固定底中计数胶囊、键盘方向键 / 空格，以及 intersection-observer 驱动的圆点状态处理。

### 内边距与间隙阶梯
| Token | 取值 | 用途 |
|---|---|---|
| `{spacing.pad-slide}` | 40px 60px | 外层幻灯片内边距 |
| `{spacing.pad-card-lg}` | 48px 56px | 大特色卡（引语框、欢迎正文） |
| `{spacing.pad-card-md}` | 32px 40px | 标准卡（图表容器、framed-header 正文） |
| `{spacing.pad-card-sm}` | 16px 24px | 紧凑卡（时间线卡、日期卡正文） |
| `{spacing.gap-grid-lg}` | 28px | 主网格间隙（团队网格、信息卡网格） |
| `{spacing.gap-grid-md}` | 24px | 标准网格间隙 |
| `{spacing.gap-grid-sm}` | 14px | 紧网格间隙（每周日期卡网格） |

### 圆角阶梯
| Token | 取值 | 用途 |
|---|---|---|
| `{spacing.radius}` | 20px | 标准卡、日期卡、时间线卡 |
| `{spacing.radius-lg}` | 28px | 特色卡（图表容器、欢迎框、引语框） |
| `{spacing.radius-pill}` | 50px | 徽章、幻灯片计数器 |
| `{spacing.radius-round}` | 50% | 全部圆（头像、项目符号点、标记点、步骤圆、图标） |

每个可见区域都带某种圆角。本系统除了 SVG 装饰本身，零直角。

### 内容居中
幻灯片内容在幻灯片内边距内垂直和水平 flex 居中。主内容容器的 max-width 随构图变化（通常 700–1100px），从不横跨整页宽度——内容和幻灯片边缘之间永远有边距给装饰占用。

## 纵深与抬升

### 硬偏移阴影（唯一手法）
每个抬升元素使用两个阴影取值之一：
- **`{shadows.default}`** = `6px 6px 0 {colors.text-dark}` — 卡片、框、图表容器、徽章、幻灯片计数器的标准偏移。
- **`{shadows.small}`** = `4px 4px 0 {colors.text-dark}` — 更小抬升元素的较轻偏移（日期卡、时间线卡、信息卡、步骤圆、头像）。

阴影是**实心炭色、零模糊、固定右下偏移**。没有 rgba 阴影，没有模糊，没有软抬升。一个元素要么投下 `{colors.text-dark}` 的硬偏移阴影，要么不投阴影。

### 展示字体的文字阴影
单独的文字阴影处理只活在放在饱和粉彩表面上的展示标题上：
- **`{shadows.text-headline}`** = `3px 3px 0 {colors.text-dark}`，用于大胆粉彩表面（turquoise、butter、peach）。
- **`{shadows.text-headline-soft}`** = `3px 3px 0 rgba(0,0,0,0.2)`，用于更软的粉彩表面（soft-pink、mint），全炭在那里会太重。

奶油上的标题不加文字阴影。

### 装饰 z-index 层
气氛 SVG 装饰活在 `z-index: 1` 上，带 `pointer-events: none`。内容坐在 `z-index: 2`。这意味着装饰可以在视觉上叠过内容矩形，但从不挡住交互。装饰经常以 `top:-30px / left:-30px` 这类负偏移裁出幻灯片边缘，给版式「贴纸伸到页外」的感觉。

## 形状与处理

### 描边粗细与样式
- **3px solid `{colors.text-dark}`** — 通用结构描边。卡片、framed header、徽章、标记圆、步骤圆、头像、图表容器、幻灯片计数器。
- **2px solid `{colors.text-dark}`** — 较轻描边，只用于项目符号 / 导航点 / 图例色块 / 日期页眉分隔线这一尺度的小元素。
- **约 2.1px solid `#232323` 或 `#000`** — 雏菊 / 星星 / 云 / 太阳装饰内部使用的 SVG 描边粗细。在 SVG 的自然尺度上，这匹配 3px 结构描边的感知重量。

描边从不上色。描边从不虚线。系统里唯一的线型是实心炭色。

### 装饰元素类型

**Daisy** — 六瓣白瓣 / 黄心雏菊，两个成对的茎位置。系统的招牌饰物。放在边角（通常 `top-left`、`top-right`、`bottom-left`、`bottom-right`），常常以 `top:-30px` 或 `right:-20px` 裁出边缘。两朵雏菊加 2–3 颗星星是最常见的装饰簇。

**Star** — 蓬松五角贴纸星，实心粉彩填充（粉、黄、mint、lavender、白）加炭色描边。用作较大雏菊 / 太阳 / 云饰物之间的散落强调。同一页上各实例要换填充色；不要全白或全黄星星。

**Sun** — 黄油黄的微笑圆太阳，带光芒。用作单一特色饰物，通常在左上或右下。

**Cloud** — 蓬松白蓝云，可选更小云变体。用于序列（对角边角两朵云）或作为想要天空气氛的页上的单一饰物。

**Rainbow** — 拱形四带彩虹（coral / yellow / mint / sky），带标准炭色描边。用作单一特色饰物，通常在右上或右下。

**Framed Header**（`{components.framed-header}`）— 两部分叠卡：彩色页眉条（任意粉彩）齐平坐在白色正文上方。这一对共享一个圆的外圆角半径和一条连续 3px 描边，整个单元投下单一偏移阴影。用作特色信息容器。

**Badge Pill**（`{components.badge-pill}`）— 短圆胶囊芯片，3px 描边，黄油（默认）填充。用作章节标签或小标签。胶囊文字是 0.85rem 的 Fredoka One。

**Marker Circle Set** — 三种尺寸（`{components.bullet-dot}` 20px、`{components.circle-dot}` 48px、`{components.circle-icon}` 44px、`{components.step-circle-lg}` 90px）。全是粉彩填充的描边圆，全带炭色描边。较大标记圆内的数字或单字母永远是白色 Fredoka One（黄油黄上除外，那里文字回到深色）。

**Avatar Circle** — 100px 描边白圆，装着小角色 SVG 肖像或首字母。带 `{shadows.small}`。

**Quote Mark** — 超大 `"` 字形，Fredoka One 约 4rem，颜色 `{colors.soft-pink}`，放在引语卡内引文正文上方。

**Process Arrow** — 简单 `→` 字形，Fredoka One 约 2rem，颜色 `{colors.text-dark}`，坐在流程步骤之间。

**Legend Swatch** — 18px 方块，4px 圆角，2px 描边。装着与对应数据系列匹配的填充色。

## 该做与不该做

### 该做
- 按角色严格搭配 Fredoka One 与 Quicksand——每一个标题和展示时刻用 Fredoka，每一段和元信息行用 Quicksand。两脸对比就是系统的声线。
- 把默认画布设为 `{colors.cream}`。当这一页想要色调情绪时伸手去拿饱和粉彩表面（turquoise、soft-pink、mint 等），但内容重的时刻奶油是安全默认。
- 给每个抬升容器加 3px 实心炭色描边，再加 `{shadows.default}` 或 `{shadows.small}` 硬偏移阴影。描边 + 偏移阴影组合是系统的招牌抬升。
- 给放在饱和粉彩表面上的每一个 Fredoka One 标题加 `{shadows.text-headline}` 文字阴影。只在奶油上跳过。
- 在每一页边缘簇拥 3–7 个手绘 SVG 装饰（雏菊、星星、太阳、云、彩虹），常常裁出边界。空边角在这套系统里看起来是坏的。
- 用描边彩色圆盘做列表项目符号——永远不要裸连字符或星号。带 `{colors.butter}` 填充的 `{components.bullet-dot}` 是默认。
- 把 `{colors.coral}` 留给小的高注意标记（步骤数字、时间线点、日期页眉）。Coral 做整页表面会破坏温暖平衡，读成攻击性。
- 把主内容容器居中，max-width 好好落在幻灯片内边距之内。装饰需要边缘空间；通栏内容会挡住饰物层。
- 当序列需要可区分步骤时，在粉彩集里轮换标记 / 圆点颜色（coral → mint → sky → lavender → butter）。不要所有步骤用单一颜色。

### 不该做
- 不要用 Fredoka One 和 Quicksand 以外的任何字体。系统只从 Google Fonts 加载这两张脸。加第三张脸会破坏图画书声线。
- 不要把 Quicksand 放进标题，或把 Fredoka One 放进段落。角色 / 脸映射是严格的。
- 不要用直角。每张卡、每个徽章、每个标记都有某种圆角——系统里最小的圆角是 4px（图例色块），大多数是 20px 或更大。
- 不要用模糊或 rgba 阴影。系统只用实心炭色偏移。`0 4px 12px rgba(0,0,0,0.1)` 这里不存在。
- 不要用彩色描边。全部描边都是炭色 `{colors.text-dark}`。
- 不要把 coral 当整页表面。Coral 是系统的高注意专色；盖住一整块区域就会失去力量。
- 不要把 Fredoka One 渲成斜体、下划线或拉伸字重。Fredoka 只有一个字重——那就是设计。
- 不要省略坐在饱和粉彩表面上的 Fredoka 标题的文字阴影。阴影才把标题重量与描边形状词汇统一起来。
- 不要让一页的边角空着没有装饰。饰物层是构图的一部分，不是可选打扮。
- 不要把两张卡叠在一起而不分开。系统读成每页一个主内容区，被饰物环绕——不是一叠互相抢的面板。

## 响应式行为

系统面向视口流体版式（一切以 `clamp()` 或 `vw` 定尺寸），但为大约 1280–1920 宽的桌面 / 投影调校。两个响应断点适配网格：

- **`@media (max-width: 768px)`**：幻灯片内边距收紧到 `24px 20px`。多列网格折叠：5 列每周网格降到 3，4 列团队网格降到 2，2 列信息卡网格降到 1，水平流程流垂直叠放并旋转箭头，水平甜甜圈版式叠放。右缘导航点隐藏。装饰不透明度降到 0.6，以免在局促版式里压过内容。
- **`@media (max-width: 480px)`**：3 列每周网格再降到 2。装饰不透明度降到 0.4。

### 演示行为
- Scroll-snap-y mandatory 在垂直滚动时把每一页锁到视口。
- 键盘：ArrowDown / ArrowRight / Space / PageDown 前进；ArrowUp / ArrowLeft / PageUp 后退；Home 跳到第一页；End 跳到最后一页。
- 右缘导航点显示当前页，并接受点击跳转。
- 底中计数胶囊显示 `N / total`，经 IntersectionObserver 更新。

### 印刷 / 导出
没有定义 `@media print` 规则。打印导出会继承滚动容器版式，可能分页不干净。把这套当作屏幕优先系统；PDF 导出需要单独的打印样式表。

## CJK 与国际内容

### 推荐中文搭配

| 角色 | 拉丁字体 | 推荐中文搭配 | 来源 |
|---|---|---|---|
| 展示 / 标题（Fredoka One 400） | Fredoka One | 站酷小薇体 ZCOOL XiaoWei | Google Fonts |
| 正文（Quicksand 500–600） | Quicksand | 悠哉字体 Yozai | cn-fontsource CDN |

### 混排策略

用 **策略 A——单一字体栈加回退**：在同一 `font-family` 栈里把 ZCOOL XiaoWei 声明在 Fredoka One *之后*，把 Yozai 声明在 Quicksand *之后*，这样拉丁字形以拉丁脸渲染，CJK 字形自动落到中文脸上。每个角色一条 CSS 规则，不用手工切 class。

### 加载

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fredoka+One&family=Quicksand:wght@400..700&family=ZCOOL+XiaoWei&display=swap" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/cn-fontsource-yozai-regular/font.css" rel="stylesheet">
```

```css
:root {
  --font-display: "Fredoka One", "ZCOOL XiaoWei", cursive;
  --font-body: "Quicksand", "Yozai", sans-serif;
}
```

### 通用 CJK 调整

- **行高**：把 CJK 正文行高提到约 1.75（从 1.6）——汉字比拉丁小写需要更多纵向呼吸。
- **字距**：汉字跑句上把 `letter-spacing` 归零（Fredoka 的 0.02em tracking 会把汉字笔画挤在一起）。拉丁 tracking 只留在拉丁跨度上。
- **文字变换**：内容是汉字时，去掉任何徽章/标签上的 `text-transform: uppercase`——中文没有大小写；强制大写对汉字无用，却会弄坏里面夹着的拉丁缩写渲染。
- **标点**：中文句子用中文全角标点（，。：；「」），拉丁用半角（`,.:;""`）。永远不要把半角标点混进中文句子。
- **标题不加句号**：中文标题惯例省略句末 。——从展示字符串里去掉。
- **盘古之白**：相邻汉字与拉丁/数字跑句之间插入细空格（或普通空格）（例如 `2026 年`、`AI 产品`）。改善混排可读性。
- **一句一字体**：不要在句中切换 CJK 字族。按角色给给定文本跑句选 ZCOOL XiaoWei *或* Yozai，永远不要在一个短语里两个都用。

### 审美说明

ZCOOL XiaoWei 的圆软展示语域是最接近 Fredoka One 胖图画书声线的汉字对等——它在标题尺度上带着同样的「友好儿童书」情绪，又不会甜到发腻。Yozai 开阔的字怀和克制的笔画对比匹配 Quicksand 的人文暖意，所以正文段落和元信息行与粉彩花园审美连续。坐在饱和粉彩表面上的标题的 3px 炭色文字阴影在 ZCOOL XiaoWei 上同样成立——turquoise / butter / peach 表面上的中文标题用 `{shadows.text-headline}`，soft-pink / mint 上用 `{shadows.text-headline-soft}`，与拉丁规则完全一致。彩色项目符号点、手绘 SVG 装饰（雏菊、星星、太阳、云、彩虹）、framed-header 帽加身模式，以及粉彩标记轮换都与内容无关。Fredoka One 的单字重约束干净映射到 ZCOOL XiaoWei 的单字重约束——两张脸都不支持斜体、下划线或字重轴变化，这保住了系统「一个角色一个字重、一张脸」的纪律。

### 已知 CJK 缺口

ZCOOL XiaoWei 是单字重展示脸，字形覆盖比 Noto 家族有限——生僻或技术汉字（罕见姓氏、古典字、GB2312 以外的仅简体变体）可能回退到系统字体。繁体中文 deck 把 Yozai 换成 `LXGW WenKai TC`（Google Fonts），它有更全的繁体覆盖和相似的友好人文语域。ZCOOL XiaoWei 读起来比 Fredoka One 的胖块性格略更文学正式——用 Daisy Days 做的中文 deck 会比拉丁原版多约 20%「平静粉彩」、少约 20%「贴纸表 kawaii」。手绘 SVG 饰物（雏菊、星星、太阳、云、彩虹）扛着字体略微丢掉的图画书情绪，所以中文 deck 上考虑每页簇拥 5–7 个饰物（3–7 范围的上端）来找回俏皮重量。

## 迭代指南

1. 任何新容器都是圆的（20px / 28px / 胶囊 / 圆），3px 炭色描边，并用 `{shadows.default}` 或 `{shadows.small}` 加阴影。永远不要交出带直角的扁平矩形。
2. 任何新标题都是 Fredoka One。如果它坐在饱和粉彩表面上，就拿到 3px 炭色文字阴影并把颜色切到 `{colors.white}`。如果它坐在奶油上或白色卡片上，保持 `{colors.text-dark}` 并跳过阴影。
3. 任何新段落默认 Quicksand 500；段落需要强调时 Quicksand 600。
4. 任何新项目符号都是描边彩色圆盘（`{components.bullet-dot}`），不是字形。默认填充是黄油，但圆形项目符号可以在粉彩集里轮换。
5. 任何新的标记序列（步骤、时间线节点、日期标签）在粉彩集里轮换（`coral → mint → sky → lavender → butter`），而不是复用一种颜色。
6. 任何新幻灯片需要 3–7 个 SVG 装饰簇在边角。从既有饰物类型里画（daisy、star、sun、cloud、rainbow）——不要引入新饰物风格（例如线描箭头、照片剪贴）。
7. 任何新强调表面从八种粉彩里选一种。不要引入第九种颜色。
8. Coral 只保持小标记色。不要做 coral 表面、coral 卡片或 coral 标题。
9. 任何列表项目符号坐在第一行文字顶部往下 4px，与 x-height 垂直对齐，不是行基线。
10. 当新组件需要「两部分框」感觉时，伸手去拿 `{components.framed-header}` 模式（彩色帽 + 白色身），而不是嵌两张分开的卡。

## 已知缺口

- 两套 Google Fonts（Fredoka One、Quicksand）经 `<link>` 从 Google Fonts CDN 加载。离线渲染会回退到 `cursive` 和 `sans-serif` 系统默认，整套排印身份会塌。离线 / 印刷可靠性需要自托管字体。
- 手绘 SVG 装饰（daisy、star、sun、cloud、rainbow）是内联 SVG，描边颜色写死为 `#232323` 或 `#2D2D2D`。没有程序化方式把它们重着色去匹配新色板——扩展装饰库需要编写新的 SVG 源。
- 系统使用 scroll-snap 导航（不是绝对定位幻灯片）。没有专用打印样式表；deck 的 PDF 导出不会开箱即一页一幻灯片分页。
- nav-dots / slide-counter / 键盘 / observer 的 JavaScript 内联嵌入，并通过 `<div class="nav-dot">` 数组写死幻灯片数量。加新幻灯片需要手工加对应的 nav-dot div。
- 粉彩表面（turquoise、mint、peach）的感知亮度不同；标题的文字阴影处理必须按表面调校（系统已经这样做——大胆表面用全炭，软表面用 20% 不透明度炭）。新表面色会需要类似的调校决定。
- `--text-muted` 颜色（#6B6B6B）用于副标题和图注，但相对粉彩表面对比有限。把闷文字留给奶油或白色卡片上用，不要直接用在粉彩表面上。
- 装饰 SVG 包含占位注释字符串 `SVG created with Arrow, by QuiverAI (https://quiver.ai)`——这是原始创作工具署名，去掉不影响渲染。
