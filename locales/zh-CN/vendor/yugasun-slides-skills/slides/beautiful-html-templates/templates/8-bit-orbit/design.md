---
version: alpha
name: 8-Bit Orbit
description: A retro-futuristic pixel-art presentation system that fuses 16-bit arcade nostalgia with editorial discipline. Display type runs in Tektur (a chunky geometric display face built on pixel-grid logic) paired with Chakra Petch for body and Space Mono for code-flavored labels and tabular data. The palette pivots on a deep cosmic navy (`#0F1B3D` / `#0A0E27`) lit by three saturated neons — cyan, hot pink, and a high-key yellow — with a soft lavender pastel for warm reprieves. Depth is built from stacked hard offset shadows in 4px increments (the pixel unit), CRT scanlines, atmospheric grain, vignettes, and animated starfields. The effect sits between an arcade cabinet and a Tron-era boardroom — unmistakably digital, intentionally lo-fi, and engineered to feel as if it just booted up.

colors:
  dark-void: "#0A0E27"
  deep-navy: "#0F1B3D"
  neon-cyan: "#5EDCF4"
  neon-pink: "#F0A6CA"
  neon-yellow: "#F4D03F"
  soft-lavender: "#E2D5F2"
  white: "#FFFFFF"

shadows:
  pixel-stack-cyan-yellow: "4px 0 0 0 {colors.deep-navy}, 0 4px 0 0 {colors.deep-navy}, 4px 4px 0 0 {colors.deep-navy}, 8px 4px 0 0 {colors.neon-yellow}, 4px 8px 0 0 {colors.neon-yellow}, 8px 8px 0 0 {colors.neon-yellow}"
  pixel-stack-pink-cyan: "4px 0 0 0 {colors.deep-navy}, 0 4px 0 0 {colors.deep-navy}, 4px 4px 0 0 {colors.deep-navy}, 8px 4px 0 0 {colors.neon-cyan}, 4px 8px 0 0 {colors.neon-cyan}, 8px 8px 0 0 {colors.neon-cyan}"
  pixel-l-shape: "4px 0 0 0 {colors.deep-navy}, 0 4px 0 0 {colors.deep-navy}, 4px 4px 0 0 {colors.deep-navy}"
  pixel-text-shadow: "4px 4px 0 {colors.neon-yellow}, 8px 8px 0 {colors.deep-navy}"
  pixel-text-shadow-small: "3px 3px 0 {colors.deep-navy}"
  card-offset: "6px 6px 0 rgba(15, 27, 61, 0.15)"
  card-featured: "8px 8px 0 {colors.neon-yellow}"

typography:
  pixel-hero:
    fontFamily: "'Tektur', cursive"
    fontSize: "clamp(48px, 10vw, 128px)"
    fontWeight: 900
    lineHeight: 1.05
    letterSpacing: 0.04em
  display:
    fontFamily: "'Tektur', cursive"
    fontSize: "clamp(32px, 5vw, 64px)"
    fontWeight: 700
    lineHeight: 1.15
  headline:
    fontFamily: "'Tektur', cursive"
    fontSize: "clamp(24px, 3.5vw, 45px)"
    fontWeight: 700
    lineHeight: 1.15
  subhead:
    fontFamily: "'Tektur', cursive"
    fontSize: "clamp(17.6px, 2vw, 24px)"
    fontWeight: 700
    lineHeight: 1.15
  stat-number:
    fontFamily: "'Tektur', cursive"
    fontSize: "clamp(32px, 4vw, 56px)"
    fontWeight: 900
    lineHeight: 1
  body:
    fontFamily: "'Chakra Petch', sans-serif"
    fontSize: "clamp(14.4px, 1.2vw, 18.4px)"
    fontWeight: 400
    lineHeight: 1.7
  hero-tagline:
    fontFamily: "'Chakra Petch', sans-serif"
    fontSize: "clamp(14.4px, 1.5vw, 19.2px)"
    fontWeight: 400
    lineHeight: 1.8
  quote-body:
    fontFamily: "'Chakra Petch', sans-serif"
    fontSize: "clamp(17.6px, 2.2vw, 25.6px)"
    fontWeight: 500
    lineHeight: 1.8
  label-pill:
    fontFamily: "'Space Mono', monospace"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.2em
    textTransform: uppercase
  label-eyebrow:
    fontFamily: "'Space Mono', monospace"
    fontSize: 13.6px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.3em
    textTransform: uppercase
  badge:
    fontFamily: "'Space Mono', monospace"
    fontSize: 11.2px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  chart-value:
    fontFamily: "'Space Mono', monospace"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1
  chart-label:
    fontFamily: "'Space Mono', monospace"
    fontSize: 11.2px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.05em
  date-chip:
    fontFamily: "'Space Mono', monospace"
    fontSize: 11.2px
    fontWeight: 400
    lineHeight: 1
  counter:
    fontFamily: "'Space Mono', monospace"
    fontSize: 12.8px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.15em

spacing:
  pixel-unit: 4px
  pad-slide-y: "3vh"
  pad-slide-x: "4vw"
  pad-card-lg: "32px 40px"
  pad-card-md: "28px"
  pad-card-sm: "16px 20px"
  gap-grid-lg: 32px
  gap-grid-md: 24px
  gap-grid-sm: 16px
  content-max-width: 1200px

canvas:
  width: 100vw
  height: 100vh

components:
  label-pill:
    background: "{colors.deep-navy}"
    color: "{colors.neon-yellow}"
    padding: "6px 14px"
    fontSize: 12px
    fontWeight: 700
    letterSpacing: 0.2em
    textTransform: uppercase
    fontFamily: "'Space Mono', monospace"
    description: "Universal section tag. Default fill is deep-navy with neon-yellow text. Variant fills swap text color so the pill stays legible (e.g., navy bg with cyan text, navy bg with pink text)."
  pixel-button:
    background: "{colors.neon-cyan}"
    color: "{colors.deep-navy}"
    padding: "16px 36px"
    fontFamily: "'Tektur', cursive"
    fontWeight: 700
    letterSpacing: 0.08em
    textTransform: uppercase
    boxShadow: "{shadows.pixel-stack-cyan-yellow}"
    description: "The signature stacked-shadow CTA. The pink variant swaps cyan body for pink and yellow shadow halo for cyan halo."
  pixel-corner-bracket:
    width: 24px
    height: 24px
    borderWidth: 4px
    description: "Two outward-facing L-shapes (top-left + bottom-right) bracketing a region. Default color is neon-cyan; yellow and pink variants exist. Sits 8px outside the bracketed element."
  feature-card:
    background: "rgba(255, 255, 255, 0.15)"
    backdropFilter: "blur(8px)"
    padding: "32px 24px"
    border: "2px solid rgba(15, 27, 61, 0.2)"
    description: "Frosted-glass card with inset navy L-brackets (top-left + bottom-right) replacing rounded corners. Used on light-surface slides."
  stat-block:
    background: "rgba(94, 220, 244, 0.08)"
    border: "2px solid rgba(94, 220, 244, 0.2)"
    padding: "32px 16px"
    description: "Cyan-tinted glass stat tile with cyan L-bracket accents at opposite corners. Used on dark surfaces. Stat numeral uses the pixel-text-shadow-small treatment."
  bar-track-light:
    height: 32px
    background: "rgba(15, 27, 61, 0.1)"
    description: "Horizontal track for hbar charts on light surfaces. Fill is solid navy/cyan/pink with a yellow offset shadow."
  bar-vertical:
    background: "{colors.neon-cyan}"
    boxShadow: "{shadows.pixel-l-shape}"
    description: "Vertical chart bar with three-piece navy L-shadow. Color cycles cyan → pink → yellow."
  timeline-node:
    width: 24px
    height: 24px
    background: "{colors.neon-cyan}"
    border: "4px solid {colors.deep-navy}"
    description: "Square pixel node on timeline rails. Active state swaps fill to neon-yellow."
  timeline-rail:
    width: 4px
    background: "repeating-linear-gradient(to bottom, {colors.deep-navy} 0px, {colors.deep-navy} 16px, transparent 16px, transparent 24px)"
    description: "Dashed pixel rail running between timeline nodes."
  date-chip:
    background: "{colors.deep-navy}"
    color: "{colors.neon-cyan}"
    padding: "2px 10px"
    fontFamily: "'Space Mono', monospace"
    fontSize: 11.2px
    description: "Small inline date marker on timeline events."
  hero-badge:
    border: "2px solid {colors.neon-yellow}"
    color: "{colors.neon-yellow}"
    padding: "8px 16px"
    fontFamily: "'Space Mono', monospace"
    fontSize: 11.2px
    letterSpacing: 0.1em
    textTransform: uppercase
    description: "Outline-only chip used in clusters under hero headlines."
  bg-grid:
    backgroundColor: "{colors.dark-void}"
    backgroundImage: "linear-gradient(rgba(94, 220, 244, 0.07) 1px, transparent 1px), linear-gradient(90deg, rgba(94, 220, 244, 0.07) 1px, transparent 1px)"
    backgroundSize: "40px 40px"
    description: "40px cyan-on-navy grid wallpaper for dark surfaces. Pink, cyan, and lavender variants invert the relationship (colored ground with low-opacity navy grid lines)."
  scanlines:
    background: "repeating-linear-gradient(0deg, transparent 0px, transparent 2px, rgba(10, 14, 39, 0.04) 2px, rgba(10, 14, 39, 0.04) 4px)"
    mixBlendMode: multiply
    description: "Horizontal CRT scanline overlay applied via ::after at z-index 50. Always present on every slide."
  grain:
    opacity: 0.035
    description: "SVG fractal-noise grain layer applied via ::before at z-index 49. Always present on every slide."
  crt-glow:
    background: "radial-gradient(ellipse at center, transparent 50%, rgba(10, 14, 39, 0.25) 100%)"
    description: "Radial vignette that darkens the corners to mimic a CRT bulge. Applied to dark-surface slides via ::after at z-index 51."
  starfield:
    description: "Container of small 4-6px colored squares (cyan, yellow, pink) positioned absolutely with a 3s twinkle keyframe. Lives on dark surfaces only."
  pixel-particles:
    description: "Floating 8px colored squares with an 8s float keyframe. Decorative ambient layer on hero and CTA-type surfaces."
  nav-dot:
    width: 12px
    height: 12px
    border: "2px solid {colors.neon-cyan}"
    background: transparent
    description: "Hollow square pip with a 2px inset cyan fill on active state. Fixed vertical rail at right edge."
  quote-line:
    width: 60px
    height: 4px
    background: "{colors.neon-yellow}"
    boxShadow: "4px 4px 0 {colors.deep-navy}"
    description: "Short yellow rule with navy offset shadow, used as a separator under quote bodies."
---

## 概览

8-Bit Orbit 是一套**复古未来像素风演示系统**。底层前提是 **4 像素单位**：每条阴影偏移、每条描边、每个角括号、每个标签高度，都落在 4px 的倍数上。版式读起来像是在旧 CRT 上栅格化后再拖进 HTML——而大气叠层（扫描线、颗粒、暗角光晕、动画星空）在每块表面上强化这种错觉。

字体栈是三套各司其职的面孔。**Tektur** 是展示字体——粗块、几何、半像素化的 grotesque，承担标题、hero 正文、统计数字，以及任何需要「画在像素网格上」的文字。**Chakra Petch** 是正文字体——带轻微几何切口的人文无衬线，小字号仍清晰，不会跟 Tektur 抢注意力。**Space Mono** 是系统字体——专用于标签、图注、徽章、图表数值、日期和计数器。等宽加上宽字距，让这些元素像 HUD 读数，而不是编辑图注。

色板以**深蓝海军为底**（`{colors.dark-void}` 与 `{colors.deep-navy}`），再用**三种高饱和霓虹**点亮——青、热粉、黄——外加柔薰衣草粉彩。表面交替：深蓝表面（青网格壁纸、白字、霓虹在前发光），再接彩色表面（粉、青或薰衣草底，海军蓝字，低不透明度的海军网格线刻进去）。霓虹从不做正文——它们留给标题、统计数字、强调线和标签填充。结果是高对比但不刺眼：霓虹像被点亮，而不是印上去。

纵深是这套系统的招牌手法：**按像素单位叠硬偏移阴影**。旗舰模式是按钮上的六段阴影——三段海军偏移以 4px 向右下迈步，再三段彩色光晕以 8px 再迈一步。Hero 文字用两层文字阴影（黄在 +4/+4，海军在 +8/+8）。卡片要么是 6px 海军 box-shadow，要么是 featured 档的 8px 黄 box-shadow。每条阴影都硬边、零模糊、锁在 4px 网格上。大气纵深来自始终开启的 **扫描线 + 颗粒 + CRT 光晕** 三件套，轻微调制每一块表面。

**密度哲学：中等偏密，大气层堆满。** 表面干净、没有陪衬时系统会「坏掉」——没有扫描线、颗粒、暗角、粒子或背后的彩色网格，字体就失去街机语境，看起来像普通网页排版。一定要叠气氛。但内容区里呼吸空间仍然重要：卡片间距宽（24–32px），统计砖内部 padding 很重，hero 文字被允许主导。典型一页承载一个展示瞬间 + 一小簇支撑元素（徽章、标签、一张图或一小格网格），全部坐在完全装饰过的大气背景上。

**关键特征：**
- 三字体栈：Tektur（展示）、Chakra Petch（正文）、Space Mono（HUD/标签）——绝不替换，绝不串角色。
- 海军底（`{colors.dark-void}` / `{colors.deep-navy}`）与彩色网格表面（粉、青、薰衣草）交替——两边都带着 40px 蚀刻网格。
- 三种霓虹（青、粉、黄）只用于展示、统计、线条和标签填充——绝不做正文。
- 所有尺寸咬合 4px 像素单位：描边 2–4px，阴影偏移 4px / 8px，角括号 24×24、4px 描边。
- 叠硬偏移阴影是纵深语言——永不模糊；文字阴影除了黄→海军级联外永不着色。
- 每一页都带着 z-index 49–51 的持续扫描线 + 颗粒 + CRT 暗角三件套。
- L 形角括号（`{components.pixel-corner-bracket}`）取代圆角，框住区域、卡片和统计砖。
- 等宽标签胶囊（`{components.label-pill}`）是每个区域的通用 eyebrow——海军填充、霓虹字、0.2em 字距、全大写。
- 动画星空与漂浮粒子方块铺在深色表面上——是氛围，不是装饰。

## 颜色

### 色板

- **Dark Void**（`{colors.dark-void}` — `#0A0E27`）：最深的底，用在 `<body>` 上，也是深色网格表面的基底。在 CRT 暗角下读起来像带蓝偏的黑。
- **Deep Navy**（`{colors.deep-navy}` — `#0F1B3D`）：结构色——所有阴影叠层、标签填充、深色卡片、霓虹表面上的按钮文字、图表柱文字。比 void 略暖；叠在一起时读作底与图。
- **Neon Cyan**（`{colors.neon-cyan}` — `#5EDCF4`）：系统的主发光。用于深色表面上的标题、主按钮填充、统计数字、主图表柱、时间线节点、导航点、角括号，以及深色表面上的网格线（7% 不透明度）。
- **Neon Pink**（`{colors.neon-pink}` — `#F0A6CA`）：暖强调。用作彩色表面底（40px 海军压粉网格）、次按钮填充、次图表柱、像素头像的嘴部细节、第三档角括号。
- **Neon Yellow**（`{colors.neon-yellow}` — `#F4D03F`）：高调警报色。用于按钮背后的阴影光晕和 featured 档卡片、活动时间线节点填充、hero 徽章、label-pill 文字变体、quote-line，以及 Tektur 文字阴影第 1 层。
- **Soft Lavender**（`{colors.soft-lavender}` — `#E2D5F2`）：冷静粉彩表面——给需要从霓虹压海军强度里喘口气的页面当底。带着与其他彩色表面相同的蚀刻海军网格壁纸。
- **White**（`{colors.white}` — `#FFFFFF`）：仅作深色/霓虹表面上的文字色。从不作幻灯片背景。

### 默认

- **默认表面背景**：`{colors.dark-void}` 配 40px 青网格（`{components.bg-grid}`）。始终在上面叠扫描线 + 颗粒 + crt-glow。
- **深色表面上的默认标题色**：`{colors.neon-cyan}`，hero 级文字用 `{shadows.pixel-text-shadow-small}` 或 `{shadows.pixel-text-shadow}`。
- **彩色网格（粉/青/薰衣草）上的默认标题色**：`{colors.deep-navy}`——霓虹字在霓虹底上会看不清。
- **深色表面上的默认正文字色**：`rgba(255, 255, 255, 0.7)`——柔化白，不是纯白。
- **彩色网格上的默认正文字色**：`rgba(15, 27, 61, 0.75)`——柔化海军。
- **默认 label-pill 填充**：`{colors.deep-navy}` 配 `{colors.neon-yellow}` 文字。彩色网格上文字可换成青或粉，只要对海军的对比仍成立。
- **标注与统计数字的默认强调色**：`{colors.neon-cyan}`。
- **默认图表色序**：青 → 粉 → 黄（按系列这个顺序）。
- **默认角括号颜色**：`{colors.neon-cyan}`。黄、粉变体用于主题强调。

当一页需要更软或更暖时，把彩色网格从青压海军（默认）换成海军压粉、海军压青或海军压薰衣草——结构关系倒置（网格线变成低不透明度海军），但排版规则不变。

## 字体

### 字族
系统跑三套面孔，各自锁死角色。

**Tektur** 是展示字体——宽体、半几何 grotesque，带轻微像素网格切口。用于每个 hero 标题、headline、统计数字、引号标记和大数字。Tektur 的粗块性格让系统像原生街机；换成 Inter 或 Space Grotesk 会整套美学崩掉。

**Chakra Petch** 是正文字体——人文无衬线，带轻微几何/方切口，14–22px 仍清晰，性格刚好能挨着 Tektur 而不消失。用于段落、hero 标语、引文正文和任何较长散文。

**Space Mono** 是 HUD 字体——等宽，专用于标签、徽章、图表数值/坐标轴、页码计数器、日期芯片，以及任何应像系统读数的元素。等宽 + 宽字距全大写，是系统的「界面」声线。

绝不用 Tektur 做正文，绝不用 Chakra Petch 做 chrome/HUD，绝不用 Space Mono 做标题。三角色分离就是排版结构。

### 字号阶梯

| Token | 字号 (clamp) | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.pixel-hero}` | 48–128px | Tektur | 900 | Hero 或封面展示标题——始终带两层文字阴影 |
| `{typography.display}` | 32–64px | Tektur | 700 | 大段开场 |
| `{typography.headline}` | 24–45px | Tektur | 700 | 主区块标题 |
| `{typography.subhead}` | 17.6–24px | Tektur | 700 | 区域级副标题或卡片标题 |
| `{typography.stat-number}` | 32–56px | Tektur | 900 | 统计砖数字——配小文字阴影 |
| `{typography.body}` | 14.4–18.4px | Chakra Petch | 400 | 段落正文 |
| `{typography.hero-tagline}` | 14.4–19.2px | Chakra Petch | 400 | Hero 副标题 / pixel-hero 下方的导语段 |
| `{typography.quote-body}` | 17.6–25.6px | Chakra Petch | 500 | 引文文字 |
| `{typography.label-pill}` | 12px | Space Mono | 700 | 海军标签胶囊内的文字 |
| `{typography.label-eyebrow}` | 13.6px | Space Mono | 400 | 标题上方独立的全大写 eyebrow（字距比胶囊更宽） |
| `{typography.badge}` | 11.2px | Space Mono | 400 | 仅描边的 hero 徽章文字 |
| `{typography.chart-value}` | 12px | Space Mono | 700 | 图表柱数值 |
| `{typography.chart-label}` | 11.2px | Space Mono | 400 | 图表坐标轴或类别标签 |
| `{typography.date-chip}` | 11.2px | Space Mono | 400 | 时间线事件上的日期标记 |
| `{typography.counter}` | 12.8px | Space Mono | 400 | 持续页码计数器（NN / NN） |

### 默认

- **Hero 或封面标题的默认字号**：`{typography.pixel-hero}`（48–128px clamp）——始终 Tektur 字重 900，带两层文字阴影。
- **主区块标题的默认字号**：`{typography.headline}`（24–45px clamp）——Tektur 字重 700。
- **段落正文的默认字号**：`{typography.body}`（14.4–18.4px clamp）——Chakra Petch 字重 400。
- **统计数字的默认字号**：`{typography.stat-number}`（32–56px clamp）——Tektur 字重 900，始终带 3px 海军文字阴影。
- **Eyebrow 标签的默认字号**：`{typography.label-pill}`（12px）装在海军胶囊里——或独立 eyebrow 时用 `{typography.label-eyebrow}`（13.6px）。
- **任何 Space Mono 标签的默认字距**：0.1em（徽章）到 0.3em（eyebrow 标签）。没有宽字距的等宽读起来像代码，不像 HUD。
- **默认正文字重**：Chakra Petch 用 400，引文正文用 500。
- **默认展示字重**：标题用 700，hero 级和统计数字用 900。

拿不准该用哪个展示 token 时，默认 `{typography.headline}`——它是区块级主力。把 `{typography.pixel-hero}` 只留给封面和 CTA 瞬间。

### 招牌处理

对应元素类型一旦用上，这些处理**不可省略**：

- **每个 pixel-hero 元素都带着叠文字阴影。** 模式是青字上的 `4px 4px 0 {colors.neon-yellow}, 8px 8px 0 {colors.deep-navy}`。没有这层两级级联的 pixel-hero 读起来像未处理的展示字体，街机声线会断。
- **每个统计数字都带着小文字阴影。** 模式是青字上的 `3px 3px 0 {colors.deep-navy}`。深色表面上的统计数字需要这层阴影才像被点亮；没有它会发扁。
- **每个 Space Mono 元素都是全大写加宽字距**——图表标签最少 0.05em，胶囊和徽章 0.08–0.2em，独立 eyebrow 标签 0.3em。本系统不存在句首大写的等宽。
- **每个 Tektur 展示元素保持原生字距或略正（hero 级 +0.04em）。** Tektur 天生宽体——负字距会把它压成另一张脸。
- **每个 Chakra Petch 正文块用 line-height ≥ 1.6。** 这张脸本身密；正文行高再紧就会糊。
- **每个标签胶囊用 Space Mono 12px、0.2em 字距。** 没有例外——胶囊是系统最可辨认的小 chrome，字号或字距一偏就坏。
- **每个图表柱数值 / 坐标轴标签都用 Space Mono。** 数字 chrome 是等宽，从不 Tektur 或 Chakra Petch。

### 排版原则

声线对比是 **粗块展示 ↔ 人文正文 ↔ 宽字距等宽 chrome**。三个角色里换任何一个脸，系统就会扁成通用深色模式。展示和正文从不斜体——唯一出现的斜意，是像素装饰元素上那点隐式倾斜。

Tektur 应始终感觉**钉住**——左对齐、行高宽裕，正文长度的跑句绝不居中（居中只允许用在 hero 和 CTA 标题上）。Chakra Petch 应始终感觉**冷静**——默认左对齐，不全大写，不加字距。

## 版式

### 画布系统
系统按每页 `100vw × 100vh` 来做。幻灯片在 `slides-container` 里纵向堆叠，用 `transform: translateY(...)` 导航。同一时刻只有一页占满视口，过渡用 cubic-bezier `(0.22, 1, 0.36, 1)`、800ms。

默认页边距是 `3vh 4vw`。内部 `slide-content` 上限 `max-width: 1200px` 并居中，所以宽屏上内容仍保持编辑栏宽，彩色背景则铺满视口。

### 像素单位
系统里每个尺寸都咬合 **4px 网格**。描边宽度 2px 或 4px。阴影偏移 4px 或 8px。角括号 24×24、4px 描边。背景网格 40px（10 × 像素单位）。卡片 padding 通常落在 8 的倍数（16、24、32、48）。这套纪律让系统像栅格化，而不是矢量。

### 持续 Chrome
三件东西出现在每一页：
- **导航点轨** — 12×12 青描边方块的纵向堆，固定在 `right: 24px`，垂直居中。活动态把内部 8×8 填成青。
- **页码计数器** — Space Mono `01 / 10` 格式，固定在 `bottom: 24px`，水平居中，深蓝半透明胶囊底。
- **导航提示** — `USE KEYS ↑ ↓`，Space Mono 11px、50% 不透明度，固定在 `bottom: 24px right: 24px`。

整份文稿光标是 `crosshair`——又一个街机信号。

### 大气叠层
每一页按 z 序带着：
1. 表面背景 — 要么 `{components.bg-grid}`（青压海军），要么某种彩色网格变体。
2. 颗粒层，z-index 49，不透明度 0.035。
3. 扫描线，z-index 50，multiply 混合。
4. CRT 暗角光晕，z-index 51（仅深色表面）。
5. 可选星空 / 像素粒子，表面内 z-index 1。
6. `.slide-content` 在 z-index 10，压在大气层之上。

这套叠层就是系统身份。没有它的一页看起来像线框。

## 纵深与抬升

### 叠硬偏移阴影（招牌）
系统用 **按 4px 像素单位叠、多步硬偏移阴影**。每条阴影值落在三种模式之一：

- **三步海军 L 形**（`{shadows.pixel-l-shape}`）—— `4px 0`、`0 4px`、`4px 4px` 三段深蓝偏移，零模糊。用在图表柱和小件抬升 chrome 上，暗示单层下落。
- **六步按钮级联**（`{shadows.pixel-stack-cyan-yellow}` / `{shadows.pixel-stack-pink-cyan}`）——三段 4px 海军迈步，再三段 8px 彩色光晕跟在后面。做出两层像素斜切。专用于 `{components.pixel-button}`。
- **两层文字阴影**（`{shadows.pixel-text-shadow}` / `{shadows.pixel-text-shadow-small}`）——黄层在 +4/+4，再海军层在 +8/+8（或统计级数字只用海军 +3/+3）。用在每个 Tektur 展示元素上。

所有阴影都是零模糊、硬边、锁在像素单位上。系统里不存在模糊 drop shadow。

### 卡片阴影
卡片用两种更简单的模式：
- `{shadows.card-offset}` = `6px 6px 0 rgba(15, 27, 61, 0.15)` — 浅色表面上非 featured 档卡片的柔海军偏移。
- `{shadows.card-featured}` = `8px 8px 0 {colors.neon-yellow}` — featured 档卡片的霓虹黄偏移，配 `-12px` translateY 抬升。

### 角括号当纵深
L 形角括号（`{components.pixel-corner-bracket}`）取代区域和卡片上的传统描边。对角两个括号暗示一个框，却不围死——眼睛会补上缺的边。统计块和功能卡片上，括号内嵌在 `top: -2px / left: -2px` 与 `bottom: -2px / right: -2px`，略微打断单元格边缘，强化像素斜切感。

### 大气纵深
扫描线 + 颗粒 + CRT 暗角叠层给每块表面提供环境纵深，不必给单个元素加阴影。动画星空和漂浮粒子在内容背后再叠空间线索。这些都不是装饰插件——它们是系统纵深感知的核心。

## 形状与处理

### 圆角
实质上为零。唯一出现的圆形状是甜甜圈式导航点内填（本系统里仍是方——导航点是方 pip，不是圆）。圆角按钮、圆角卡片或圆角胶囊芯片会立刻打断像素美学。

像素脸头像区用方形眼睛和矩形嘴——解剖画成像素，不是曲线。

### 描边粗细
- **2px solid** — 用于功能卡片轮廓、hero 徽章、导航点、统计块边框、图表柱（内边）。
- **3px stroke** — 用于 SVG 图表内的坐标轴（深蓝）。
- **4px solid** — 用于角括号、时间线节点边框、quote-line，以及按钮的内侧像素斜切。

描边始终实线，始终海军或霓虹，除时间线轨（`{components.timeline-rail}`）外从不虚线——那条轨刻意用 16px 开、8px 关的 repeating linear gradient，模仿像素虚线。

### 装饰元素类型

**像素角括号** — 两个朝外的 L 形（左上 + 右下）框住一块区域。24×24、4px 描边。默认青色；有黄、粉变体。括号图案是系统最鲜明的非字体标记。

**标签胶囊** — 海军矩形，霓虹黄 Space Mono 文字，12px / 0.2em。通用区块 eyebrow。变体把文字换成青或粉，海军填充不变。

**Hero 徽章** — 仅描边 2px 黄边配黄 Space Mono 文字。成簇出现在 hero 标题下，当功能标签。

**统计块** — 青调玻璃砖（8% 青填充、20% 青边）配左上和右下的青角括号。放大统计数字压在 Space Mono 粉标签上。

**功能卡片** — 磨砂白卡片（15% 白填充、blur）配对角海军角括号。用在彩色网格表面上。

**像素按钮** — 青矩形配六步叠阴影级联。悬停时按钮平移 +2/+2，阴影收成 4 步级联——模拟像素风按键。

**Quote-line** — 60×4 黄矩形配 4×4 海军偏移阴影。用在引文正文下方当分隔。

**时间线节点** — 24×24 青方块配 4px 海军边，落在虚线海军轨上。活动态填充换成黄。

**日期芯片** — 行内 2px padding 的海军胶囊配青 Space Mono 文字，用来标时间线事件。

**像素脸** — 120×120 一组方形「五官」（青眼、粉嘴），在海军头像区里绝对定位的 div。既是友好吉祥物，也是系统招牌装饰模块。

**档位卡片** — 白矩形，6px 海军偏移阴影。Featured 档把填充换成深蓝、阴影换成 8px 黄，并 `-12px` translateY 抬升。档位特性用青的 `+` ::before 字形，而不是标准项目符号。

**像素地貌** — CTA 类表面底部一排高低不等的海军山，不透明度 0.3。纯装饰，暗示街机地平线。

## 该做与不该做

### 该做

- 每一页都叠扫描线 + 颗粒 + CRT 暗角。气氛就是设计系统；没有它的表面看起来像线框。
- 深色表面上默认标题用 `{colors.neon-cyan}`，彩色网格（粉/青/薰衣草）上默认标题用 `{colors.deep-navy}`。
- 每个 pixel-hero 元素用 `{shadows.pixel-text-shadow}`，每个统计数字用 `{shadows.pixel-text-shadow-small}`。没有文字阴影的 Tektur 展示字会发扁。
- 每个尺寸咬合 4px 像素单位——描边、阴影偏移、padding、角括号尺寸。偏网格的值会打断栅格化手感。
- 展示用 Tektur，正文用 Chakra Petch，chrome 用 Space Mono——专属。三声线串味会把系统压扁。
- 把 eyebrow 包进 `{components.label-pill}`（海军底、黄 Space Mono 字、0.2em 字距、全大写），当通用区块标签。
- 海军底上每个区域至少配一处霓虹发光——文字、图表柱、角括号或按钮阴影光晕。纯海军没有霓虹强调读起来像死屏。
- 在深色 hero 和 CTA 表面上叠动画星空和像素粒子漂浮物。动是气氛的一部分。
- 图表按青 → 粉 → 黄系列顺序渲染，数字/标签用 Space Mono。霓虹三色就是图表色板。
- 用对角 L 形角括号框卡片和统计砖，而不是整圈描边。暗示框是系统的招牌卡片处理。

### 不该做

- 不要换字体。Tektur、Chakra Petch 和 Space Mono 是三声线——换成 Inter、Roboto 或 Space Grotesk 系统会塌。
- 不要圆任何角。像素美学依赖方边。Border-radius 只留给 SVG 甜甜圈图几何。
- 不要模糊任何阴影。每条阴影都硬边、零模糊。`0 4px 12px rgba(0,0,0,0.1)` 这里不存在。
- 不要把霓虹字放在霓虹表面上。青标题压粉网格会看不清——彩色底上改用深蓝。
- 不要用 Tektur 跑句首大写正文，也不要用 Chakra Petch 做 chrome/标签。每张脸只有一个角色。
- 不要引入第四种霓虹。色板是青 + 粉 + 黄 + 薰衣草粉彩。加绿或橙会打断精选霓虹三色。
- 不要在任何一页省略大气叠层，即使是图表重或表格重的页。叠层不可谈判。
- 不要用全大写 Chakra Petch 正文。正文始终句首大写；全大写留给 Space Mono 和 Tektur 展示。
- 不要丢掉海军标签胶囊改用纯文字 eyebrow。胶囊是系统里最可辨认的小 chrome。
- 不要用偏轴偏移给文字或 chrome 加阴影。每条阴影都按 4px 增量向右下迈步——左或上偏移不存在。

## 响应式行为

8-Bit Orbit 是围绕 `vw/vh` 尺寸和 CSS `clamp()` 区间建的**视口流体系统**。文稿本身没有硬断点——每个字号、padding 和间距都按视口宽度在最小与最大之间插值。

### 缩放行为
- Hero 文字随视口宽度从 48px → 128px。
- 统计数字 32px → 56px。
- 正文 14.4px → 18.4px。
- 4px 像素单位、40px 网格尺寸、扫描线 4px 条纹和角括号尺寸是固定的——不缩放，意味着更大视口上像素 chrome 会成比例更细（有意为之——画布越大，像素读起来越小、越精致）。

### 组件断点
三个组件级断点：
- `max-width: 1024px` — 功能网格从 4 列收成 2，两栏拆分布局改叠放。
- `max-width: 900px` — 功能网格再收，hbar 图表标签列变窄。
- `max-width: 500px` — 功能网格变单列，统计网格叠放。

### 演示行为
- 前进：`ArrowDown`、`ArrowRight` 或 `Space`。
- 后退：`ArrowUp` 或 `ArrowLeft`。
- `Home` 跳到第一页，`End` 跳到最后一页。
- 触控设备上纵向滑动，阈值 50px 前进/后退。
- 鼠标滚轮前进/后退，带 800ms debounce 锁。
- 页面过渡用 800ms cubic-bezier `(0.22, 1, 0.36, 1)` 的 translateY transform。

### 动画触发
图表柱和统计计数器在进入页面时用 `setTimeout` 交错动画（项目间隔 100–150ms）。离开页面时柱/计数器重置为 0，再进入会重放。`prefers-reduced-motion` 媒体查询会关掉过渡以及星空/粒子闪烁 keyframe。

### 打印行为
系统没有 `@media print` 规则。文稿以屏幕为先；打印只出当前活动页。静态导出时，逐页截图会保留所有大气叠层（扫描线和颗粒是 CSS 渲染，不是素材）。

## CJK 与国际内容

用这套模板做中文（或其他 CJK）内容时，把拉丁字体栈换成对等的中文搭配，并套用通用 CJK 调整。推荐中文字体全部走 CDN——无需安装。

### 推荐中文搭配

| 角色 | 拉丁（默认） | 中文对应 |
|---|---|---|
| 展示 / hero / 统计数字 | Tektur 700–900 | 思源黑体 Noto Sans SC 900 |
| 正文 / hero 标语 / 引文正文 | Chakra Petch 400–500 | 思源黑体 Noto Sans SC 400 |
| HUD 标签 / 徽章 / 图表数值 / 计数器 | Space Mono 400–700（全大写 + 宽字距） | 思源黑体 Noto Sans SC 500（无 transform、无字距）——见下方已知 CJK 缺口 |

### 混排策略

**策略 A** — 单一 CJK 字族，自带拉丁字形覆盖。把每个文字元素设为 `font-family: 'Noto Sans SC', sans-serif`。思源黑体自带的拉丁字形能干净地挨着汉字，所以像 `使用 Tektur 字体` 这样的句子会用同一张脸，而不是词中换字体。本系统通常跑三张脸（展示 / 正文 / HUD）；收成一张 CJK 脸是对的取舍，因为三张拉丁脸都没有可信的中文对应，视觉层级仍可通过字重（900 / 700 / 500 / 400）加上系统招牌阴影叠层成立。

### 加载

加到模板的 `<head>`：

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700;900&display=swap" rel="stylesheet">
```

### 通用 CJK 调整

- **行高**：相对拉丁规格提高约 15–25%。正文 1.75–1.85（从 1.7–1.8 上调），展示 1.15–1.25（从 1.05–1.15 上调）。CJK 字形方且视觉饱满——纵向比拉丁更挤。
- **字距**：每段 CJK 跑句都设为 0。模板里 Tektur 展示的正字距（+0.04em）以及 Space Mono 标签 0.1–0.3em 等宽字距，在方形 CJK 字形上会坏——它们设计上已经均匀。
- **文字变换**：不要对中文施加 `uppercase`——CJK 没有大小写。本系统每个 Space Mono 标签都用 `text-transform: uppercase`；CJK 跑句请去掉。
- **标点**：用全角中文标点 （，。：；！？「」（））。
- **展示标题不加句号**：中文排版惯例在展示级标题末尾不加 。
- **中西文之间的空格（盘古之白）**：每个汉字与相邻拉丁字母或数字之间插入 ASCII 空格。写 `8 位赛博 / 1989 模式`，不要写 `8位赛博/1989模式`。
- **一句一字体**：思源黑体以统一风格覆盖 CJK 和拉丁字形——让它处理混排句子。不要让浏览器在句中为 ASCII 回退到 Tektur 或 Space Mono。

### 本系统的美学备注

系统身份立在三声线上——Tektur（粗块街机展示）、Chakra Petch（人文正文）、Space Mono（HUD 读数）——CJK 构建无法保住这三脸对比。补偿办法是更用力压在**非字体**招牌元素上：叠文字阴影（黄在 +4/+4，海军在 +8/+8）在思源黑体 900 标题上仍然成立，字体本身变通用时，是它在扛街机声线。保留所有大气叠层（扫描线、颗粒、CRT 暗角、星空、网格壁纸）——它们在 CJK 构建里比拉丁原版做更多身份工作。

系统的 Space Mono 标签胶囊（海军填充、霓虹黄字、0.2em 字距、全大写）是最可辨认的小 chrome，翻译效果差：CJK 字符吃不下宽字距或全大写变换。中文 label-pill 用思源黑体字重 500、0 字距、无 transform，字号略紧（10–11px 而不是 12px），以保住芯片的紧凑轮廓。彩色胶囊底和角括号框承担辨认负荷。

### 已知 CJK 缺口

- **没有可 CDN 加载的中文像素字体。** 系统的街机美学依赖 Tektur 的半像素 grotesque 性格——Google Fonts 或主流 CDN 上没有既读得像「像素风」又保持可读的对等中文脸。思源黑体字重 900 有分量，但像素网格信号完全丢掉。大气叠层（扫描线、颗粒、暗角、星空）和像素斜切阴影叠层必须自己扛街机声线。
- **没有 CDN 中文等宽脸做 HUD 标签。** Space Mono 的「系统读数」声线依赖等宽节奏 + 全大写 + 0.1–0.3em 字距——没有一项能转到 CJK。label-pill 失去等宽性格；靠海军填充 + 霓虹字 + 角括号框让 chrome 仍可辨认。

## 迭代指南

1. 任何新页都拿到完整大气叠层三件套（深色表面上扫描线 + 颗粒 + crt-glow，彩色表面上扫描线 + 颗粒）以及 40px 蚀刻网格表面。不要跳过叠层。
2. 任何新展示元素用 Tektur。任何新正文元素用 Chakra Petch。任何新标签、徽章、计数器或图表数值用 Space Mono。绝不跨角色边界。
3. 任何新标题在深色表面上用 `{colors.neon-cyan}`，在彩色网格上用 `{colors.deep-navy}`——两者都带对应 Tektur 字重，hero 级还要叠文字阴影。
4. 任何新 eyebrow 用 `{components.label-pill}`——海军填充、霓虹黄 Space Mono 字，12px / 0.2em / 全大写。不要换成普通 h 标签。
5. 任何新卡片或区域用对角 L 形角括号（左上 + 右下），而不是整圈描边。暗示框是系统招牌。
6. 任何新尺寸咬合 4px 像素单位。描边 2–4px，阴影偏移 4px / 8px，角括号 24px，网格 40px。偏网格的值会不对。
7. 任何新阴影都硬边、零模糊。按钮用六步级联；卡片用 6px 海军或 8px 黄；文字用两层级联。
8. 任何新图表按青 → 粉 → 黄系列循环。数字标签和坐标轴标签始终 Space Mono。
9. 表面需要更暖或更软时，换成粉、青或薰衣草蚀刻网格变体——但排版规则原封不动（海军标题、柔化海军正文）。
10. 动画元素（星空、粒子、图表柱生长、计数器上卷）应尊重 `prefers-reduced-motion`。大气叠层（扫描线、颗粒、暗角）不是动画，始终开着。

## 已知缺口

- **Tektur、Chakra Petch 和 Space Mono 是 Google Fonts**，通过 preconnect + `<link>` 加载。系统除了 `cursive` / `sans-serif` / `monospace` 没有回退策略——Google Fonts 失败的环境里（离线、受限网络），美学会塌成系统默认，丢掉性格。
- **星空和像素粒子元素由内联 JS 生成**，创建固定数量的绝对定位 div，带随机位置和动画延迟。动画 keyframe 在 CSS 里，但元素只有 JS 成功跑起来才会被创建。
- **图表系统是写死的**：柱高、hbar 宽度和统计计数器目标存在 `data-*` 属性里，用匹配 slide-index 触发的 `setTimeout` 交错来动画。没有数据绑定层——加新图表需要复制 HTML 模式并更新 JS 的 slide-index 匹配器。
- **CTA 表面上的像素地貌由 JS 从写死的高度数组生成** `[30, 50, 70, ...]`。每座山宽度变化（60 + (i % 3) * 20px）。替换地貌需要改 JS 高度数组。
- **CRT 暗角光晕用固定深蓝径向渐变。** 调整需要改 CSS 渐变 stop；没有 token 化的暗角强度。
- **光标整份文稿设为 `crosshair`**，出于气氛。文稿被嵌入时，可能与文本选择预期冲突。
- **滚轮/触控回退没有键盘导航提示。** nav-hint 写着 `USE KEYS ↑ ↓`，尽管滚轮和触控也接好了。
- **页码计数器格式固定为 `NN / NN` 零填充。** 超过 99 页的文稿，计数器会发生布局跳动。
- **pixel-corner-bracket 尺寸固定 24×24、4px 描边**，不随视口缩放。极大或极小视口上括号可能成比例失调。
