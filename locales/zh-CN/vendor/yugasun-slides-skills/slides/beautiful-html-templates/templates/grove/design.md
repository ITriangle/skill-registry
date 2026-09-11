---
version: alpha
name: Grove
description: A quiet, editorial-serif presentation system in the register of a well-bound monograph or boutique brand book. Playfair Display at weight 400 (never bold) carries every headline, italicized in terracotta coral for accent emphasis as the signature move. Jost weight 300 carries every paragraph as the "good paper" body face. JetBrains Mono at weight 300 holds labels, kickers, and the thin chrome bars. The palette pairs a deep forest green canvas (#192b1b) with warm cream text (#d4cfbf) and a single terracotta coral accent (#c8524a). Generous negative space, hairline 1px borders, and a near-invisible serif watermark numeral give it the calm authority of a literary journal.

colors:
  bg: "#192b1b"
  bg-alt: "#1e3221"
  bg-light: "#e8e4d6"
  bg-light-alt: "#dedad0"
  fg: "#d4cfbf"
  fg-2: "rgba(212, 207, 191, 0.6)"
  fg-3: "rgba(212, 207, 191, 0.32)"
  fg-light: "#192b1b"
  fg-light-2: "rgba(25, 43, 27, 0.58)"
  fg-light-3: "rgba(25, 43, 27, 0.33)"
  accent: "#c8524a"
  border: "rgba(212, 207, 191, 0.12)"
  border-light: "rgba(25, 43, 27, 0.14)"
  watermark-dark: "rgba(212, 207, 191, 0.06)"
  watermark-light: "rgba(25, 43, 27, 0.06)"

color-aliases:
  fg-light: bg
  fg-light-canonical: "fg-light shares hex #192b1b with bg — the green is reused as both surface and primary text-on-light"

typography:
  display:
    fontFamily: "'Playfair Display', 'Noto Serif SC', Georgia, serif"
    fontSize: "10vw"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: -0.01em
  h1:
    fontFamily: "'Playfair Display', 'Noto Serif SC', Georgia, serif"
    fontSize: "5.5vw"
    fontWeight: 400
    lineHeight: 1.1
  h1-statement:
    fontFamily: "'Playfair Display', 'Noto Serif SC', Georgia, serif"
    fontSize: "min(4.5vw, 7.5vh, 88px)"
    fontWeight: 400
    lineHeight: 1.15
  h2:
    fontFamily: "'Playfair Display', 'Noto Serif SC', Georgia, serif"
    fontSize: "3.2vw"
    fontWeight: 400
    lineHeight: 1.2
  h3:
    fontFamily: "'Playfair Display', 'Noto Serif SC', Georgia, serif"
    fontSize: "2vw"
    fontWeight: 400
    lineHeight: 1.3
  quote-text:
    fontFamily: "'Playfair Display', 'Noto Serif SC', Georgia, serif"
    fontSize: "3.2vw"
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: -0.01em
    fontStyle: italic
  quote-mark:
    fontFamily: "'Playfair Display', 'Noto Serif SC', Georgia, serif"
    fontSize: "8vw"
    fontWeight: 400
    lineHeight: 0.6
  stat-value:
    fontFamily: "'Playfair Display', 'Noto Serif SC', Georgia, serif"
    fontSize: "4.5vw"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: -0.02em
  grove-num:
    fontFamily: "'Playfair Display', 'Noto Serif SC', Georgia, serif"
    fontSize: "18vw"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: -0.03em
  lead:
    fontFamily: "'Jost', 'Noto Sans SC', system-ui, sans-serif"
    fontSize: "1.45vw"
    fontWeight: 300
    lineHeight: 1.65
  body:
    fontFamily: "'Jost', 'Noto Sans SC', system-ui, sans-serif"
    fontSize: "1.05vw"
    fontWeight: 300
    lineHeight: 1.75
  body-list-emph:
    fontFamily: "'Jost', 'Noto Sans SC', system-ui, sans-serif"
    fontSize: "max(1.4vw, 17px)"
    fontWeight: 300
    lineHeight: 1.6
  caption:
    fontFamily: "'Jost', 'Noto Sans SC', system-ui, sans-serif"
    fontSize: "0.82vw"
    fontWeight: 300
    lineHeight: 1.55
  label:
    fontFamily: "'JetBrains Mono', monospace"
    fontSize: "0.7vw"
    fontWeight: 300
    letterSpacing: 0.12em
  kicker:
    fontFamily: "'JetBrains Mono', monospace"
    fontSize: "0.7vw"
    fontWeight: 300
    letterSpacing: 0.14em
    textTransform: uppercase
  chapter-num:
    fontFamily: "'JetBrains Mono', monospace"
    fontSize: "0.7vw"
    fontWeight: 300
    letterSpacing: 0.2em
    textTransform: uppercase
  stat-label:
    fontFamily: "'JetBrains Mono', monospace"
    fontSize: "0.7vw"
    fontWeight: 300
    letterSpacing: 0.12em
    textTransform: uppercase

spacing:
  pad-x: "8vw"
  pad-y: "6.5vh"
  pad-quote-x: "calc(8vw * 1.1)"
  pad-quote-y: "calc(6.5vh * 1.2)"
  gap-lg: "4.5vh"
  gap-md: "2.8vh"
  gap-sm: "1.4vh"
  rule-short: "36px"

motion:
  ease-slide: "cubic-bezier(0.77, 0, 0.175, 1)"
  dur-slide: "0.9s"
  ease-enter: "cubic-bezier(0.16, 1, 0.3, 1)"
  dur-enter: "0.7s"
  stagger-delays: "0 / 0.08s / 0.18s / 0.3s / 0.44s / 0.6s / 0.78s"

canvas:
  width: 100vw
  height: 100vh

components:
  slide-chrome:
    description: "Thin top bar separating slide content from the page edge. A flex space-between row holding mono label text on each side, separated below by a 1px hairline in {colors.border} (or {colors.border-light} on light slides). Pads with {spacing.gap-sm} above the rule, then {spacing.gap-md} below before content starts."
    border: "1px solid {colors.border}"
    typography: "{typography.label}"
  slide-foot:
    description: "Matching bottom bar. Flex space-between row holding section name and 'NN / TT' counter, with 1px hairline border-top. The chrome and foot together frame every content slide; cover, chapter, quote, and end slides hide both."
    border: "1px solid {colors.border}"
    typography: "{typography.label}"
  grove-num:
    description: "Massive serif digit placed in the background at very low opacity (6%) as compositional texture. Sits absolutely at right: {spacing.pad-x}, bottom: -0.15em, with pointer-events disabled. The system's signature wallpaper element on chapter and section moments."
    fontSize: "18vw"
    color: "{colors.watermark-dark} on dark / {colors.watermark-light} on light"
  grove-stat:
    description: "Stat card: large Playfair value in {colors.accent}, mono uppercase label beneath, 1px border-bottom hairline. No background fill — the card is defined by the rule and the type ratio alone."
    valueColor: "{colors.accent}"
    valueSize: "4.5vw"
    labelTypography: "{typography.stat-label}"
    borderBottom: "1px solid {colors.border}"
  bullet-list:
    description: "Two-column grid list (2em / 1fr) where the bullet is a coral em-dash glyph rendered in JetBrains Mono, not a CSS bullet. The em-dash is the system's bullet language."
    bulletGlyph: "—"
    bulletColor: "{colors.accent}"
    bulletFont: "'JetBrains Mono', monospace"
  rule-coral:
    width: "{spacing.rule-short}"
    height: "1px"
    background: "{colors.accent}"
    description: "A 36px-wide 1px-tall terracotta coral rule. The compositional beat between a kicker and the headline that follows."
  rule-full:
    width: "100%"
    height: "1px"
    background: "{colors.border} on dark / {colors.border-light} on light"
    description: "Full-width hairline divider. Used between stacked sections inside a slide."
  kicker:
    typography: "{typography.kicker}"
    color: "{colors.accent}"
    description: "Mono uppercase eyebrow in coral, placed above an h1/h2 headline."
  chapter-num:
    typography: "{typography.chapter-num}"
    color: "{colors.accent}"
    marginBottom: "{spacing.gap-md}"
  quote-mark:
    typography: "{typography.quote-mark}"
    color: "{colors.accent}"
    description: "Massive Playfair opening-quote glyph in coral, placed above the italic quote body."
  img-placeholder:
    background: "{colors.bg-alt} on dark / {colors.border-light} on light"
    color: "{colors.fg-3} on dark / {colors.fg-light-3} on light"
    typography: "{typography.label}"
    minHeight: "30vh"
    description: "Image-region marker — solid darker-than-background fill with a mono caption stating the placeholder text. Use this in place of <img> until a real image is available."
  nav-dots:
    position: "fixed"
    placement: "bottom: 24px, horizontally centered"
    dotSize: "5px"
    dotBackground: "rgba(255, 255, 255, 0.22)"
    activeBackground: "rgba(255, 255, 255, 0.8)"
    activeTransform: "scale(1.4)"
    description: "Small white dots at the bottom of the viewport indicating slide position. The fixed counter (#slide-counter) is intentionally disabled — the slide-foot already shows NN / TT."
---

## frontend-slides 固定舞台策略

当本设计系统由 `frontend-slides` skill 使用时，最终 deck 应生成为**固定 1920×1080 舞台**，并等比缩放到浏览器视口。deck 应在每一块屏幕上（包括手机）保持 16:9 幻灯片画布；可以加上下黑边或左右黑边，但不应为移动端重排幻灯片内容。

本策略的优先级高于本文件后文描述的任何源模板响应式行为。若后文说原模板是视口流体的，只把它当作源历史，不要当作 `frontend-slides` 的目标生成模型。

即使源模板最初用 `100vw`、`100vh`、`vw`、`vh` 或 `clamp()` 这类视口流体 CSS 实现，本策略仍然适用。把那些值当作设计比例，翻译成 1920×1080 舞台坐标，而不是生成 deck 里的实时响应规则。

最终输出使用 `deck-stage.js` 或等价的内联舞台缩放器：每页按 1920×1080 渲染，用一次 transform 缩放整块舞台，并核对渲染截图里是否有文字溢出和面板重叠。


## 概述

Grove 是一套**安静的编辑衬线演示系统**，气质接近文学专著或精品品牌手册。底层前提是克制：每一页只承载一个聚焦的内容时刻，四周是深的负空间，顶底各一条 1px 铬件细条锚定，并靠一小套构图节拍支撑（珊瑚眉题、36px 珊瑚线、斜体珊瑚强调、em 破折号项目符、近乎看不见的水印数字）。

排印栈跑四套字体，每套只用一个特定字重：

- **Playfair Display、字重 400** 承担每一条标题、每一条引语、每一个数据数字，以及每一个水印数字。**不允许加粗衬线**——禁止加粗是本系统最重要的排印承诺。斜体 Playfair 用 `{colors.accent}` 珊瑚色，是标志性强调动作：标题里的 `<em>` 会切成斜体珊瑚。
- **Jost、字重 300** 承担每一段正文和项目符正文。轻字重就是「好纸」的手感——它往后退，让衬线带头。
- **JetBrains Mono、字重 300** 承担每一个标签、眉题、脚线、页码计数和数据图注。始终全大写，始终至少 0.12em 字距。
- **Noto Serif SC / Noto Sans SC、字重 300–500** 作为每一个角色的中文回退加载。这套 deck 按双语意识搭建——内容里出现汉字时，通过 Noto 切面渲染。

色板是一套收得很紧的双表面系统，加一个强调色。深色页用 `{colors.bg}`（深森林绿）配 `{colors.fg}`（暖奶油——从不用纯白）做正文。浅色页翻成 `{colors.bg-light}`（暖羊皮纸）配 `{colors.fg-light}`（同一森林绿现在当文字）。唯一强调色是**陶土珊瑚**（`{colors.accent}` — #c8524a），只出现在小而刻意的地方：标题里的斜体强调、眉题下的 36px 线、em 破折号项目符、数据数字、章节序数，以及开引号。珊瑚是系统的强调声音；把它当表面填充或正文段落，会打碎编辑纪律。

纵深是**扁平、靠空气的**。没有投影、没有渐变、没有模糊、没有光晕。仅有的「纵深」手段是 1px 发丝线（铬件条、数据卡片分隔、对比面板分隔）以及 6% 不透明度的水印数字。整套系统读起来像印在亚麻纸上的墨，不像数字表面。

系统自带一套**动效词汇**：页与页之间用尖锐的 `cubic-bezier(0.77, 0, 0.175, 1)` 平移，时长 0.9s；元素入场通过 `[data-anim]` 和 `[data-delay]` 属性交错（fade-up / fade-in / reveal-right / reveal-left / scale-in），曲线是带弹性的 `cubic-bezier(0.16, 1, 0.3, 1)`，时长 0.7s，延迟为 0 / 0.08 / 0.18 / 0.3 / 0.44 / 0.6 / 0.78s。动画是系统身份的一部分；新幻灯片应使用这套动画属性栈，而不是自写自定义转场。

**密度哲学：疏朗、会呼吸。** Grove 在幻灯片安静时读起来优雅——一条标题、一段支撑段落、三个数据横排、两栏图文。8vw 水平、6.5vh 垂直内边距按设计就很慷慨。一页往画布里塞 6 个元素会打破系统；一页一条标题、一句导语、一条强调线才读成权威。宁可少元素、大尺寸。系统奖励字体周围的静，而不是内容密度。

**关键特征：**
- 每一个衬线时刻都用 Playfair Display、字重 400——从不加粗。`{colors.accent}` 斜体是标题强调。
- 每一段正文都用 Jost 字重 300。更轻的字重是系统的「好纸」声音。
- 每一个标签、眉题、脚线、计数和图注都用 JetBrains Mono 字重 300、全大写、0.12em–0.2em 字距。
- 深色页在 `{colors.bg}` 深森林绿上，文字用 `{colors.fg}` 暖奶油。浅色页在 `{colors.bg-light}` 羊皮纸上，文字用 `{colors.fg-light}` 绿色。
- 一个强调色：`{colors.accent}` 陶土珊瑚。只用于斜体标题强调、36px 珊瑚线、em 破折号项目符、数据数字、章节序数，以及引号。
- 只有 1px 发丝线（深色用 `{colors.border}`，浅色用 `{colors.border-light}`）。没有粗边框、没有阴影、没有渐变。
- JetBrains Mono 珊瑚色的 em 破折号字形，是系统通用的项目符。
- 巨大的衬线水印数字（`{components.grove-num}`，18vw，6% 不透明度）坐在章节与分节页的右下角，当作构图纹理。
- 内置交错淡入 / 揭示动画系统（`[data-anim]` + `[data-delay]`）；新内容应使用它，而不是无入场地出现。

## 色彩

### 色板
- **BG / 深森林**（`{colors.bg}` — #192b1b）：主导深色画布。深而克制的森林绿——落地、编辑感，Grove 的底色。默认幻灯片背景。
- **BG Alt**（`{colors.bg-alt}` — #1e3221）：略浅的森林绿，用于次级深色表面。用作深色页上 `{components.img-placeholder}` 的填充，读成从画布升一档的色调，同时不离开绿色家族。
- **BG Light / 羊皮纸**（`{colors.bg-light}` — #e8e4d6）：浅色页用的暖羊皮纸表面。读成好品质的纸张，不像数字白。
- **BG Light Alt**（`{colors.bg-light-alt}` — #dedad0）：略偏冷的羊皮纸，用于次级浅色表面。可供相邻浅色区域做色调分离。
- **FG / 暖奶油**（`{colors.fg}` — #d4cfbf）：深色表面上的主文本色。暖奶油——从不用纯白。偏白的色温对印刷墨感至关重要。
- **FG-2**（`{colors.fg-2}` — rgba(212,207,191,0.6)）：深色上的次级 / 弱化文本。用于导语、图注，以及需要从主文本后退的支撑文案。
- **FG-3**（`{colors.fg-3}` — rgba(212,207,191,0.32)）：深色上的三级 / 提示文本。近乎看不见——用于图片占位图注和最淡的元信息。
- **FG Light**（`{colors.fg-light}` — #192b1b）：浅色表面上的主文本。**与 `{colors.bg}` 共用 hex**——深森林绿既当深色画布，也当浅色上的深色文字。这是系统主要的表面-文字反转装置。
- **FG Light 2**（`{colors.fg-light-2}` — rgba(25,43,27,0.58)）：浅色上的次级弱化文本。
- **FG Light 3**（`{colors.fg-light-3}` — rgba(25,43,27,0.33)）：浅色上的三级文本。
- **Accent / 陶土珊瑚**（`{colors.accent}` — #c8524a）：唯一的暖音符。省着用：标题里的斜体强调、眉题下的 36px 珊瑚线、em 破折号项目符、数据数字、章节序数、开引号，以及导航点激活态。从不当表面填充，从不当正文段落。
- **Border**（`{colors.border}` — rgba(212,207,191,0.12)）：深色页上的发丝分隔。12% 奶油——作为结构线可见，但从不大声。
- **Border Light**（`{colors.border-light}` — rgba(25,43,27,0.14)）：浅色页上的发丝分隔。14% 森林绿。

### 默认值
- **默认幻灯片背景**：`{colors.bg}`（深森林绿），作为 deck 主导色调。当内容想要字面「纸页」感时再伸手去 `{colors.bg-light}`（羊皮纸）——通常是引语页、较轻的章节，或对比。
- **深色表面上的默认主文本色**：`{colors.fg}`（暖奶油）。
- **浅色表面上的默认主文本色**：`{colors.fg-light}`（深森林绿——与深色表面同一 hex）。
- **默认次级 / 弱化文本**：深色用 `{colors.fg-2}`，浅色用 `{colors.fg-light-2}`。使用 `.muted` 工具类。
- **默认标题颜色**：跟所在表面的主文本色走。标题从不整体用珊瑚，除非内部的斜体 `<em>` 强调。
- **默认正文颜色**：跟所在表面的主文本色走。
- **默认边框颜色**：深色用 `{colors.border}`，浅色用 `{colors.border-light}`——都是 1px solid 发丝线。
- **默认眉题 / 章节序号颜色**：`{colors.accent}`（陶土珊瑚）。等宽全大写眉题是唯一吃强调色的铬件元素。
- **眉题下那条 36px 构图短线的默认颜色**：`{colors.accent}`。全宽区块分隔线改用 `{colors.border}`。

色板刻意极简。深森林 / 浅羊皮纸 / 陶土珊瑚三元组就是全部色彩词汇。引入第四色（海军蓝、黄、第二个强调色）会打破系统的编辑克制。

## 字体排印

### 字体家族
系统从 Google Fonts 加载四套家族：

- **Playfair Display**，字重 400 和 500（斜体与正体）。**已发布幻灯片只用字重 400。** 字重 500 已加载但预留；系统规则明确不允许加粗衬线（字重 700）。
- **Jost**，字重 200、300、400、500。**只用字重 300。** 轻字重是系统的正文声音。
- **JetBrains Mono**，字重 300 和 400。**只用字重 300。** 轻等宽是铬件声音。
- **Noto Serif SC / Noto Sans SC**，字重 300–500，作为每一个角色的中文回退链加载。

四家族栈按角色很严：Playfair 承担每一个衬线时刻（展示、标题、引语、数据数字、水印），Jost 承担每一段正文和项目符，JetBrains Mono 承担每一个标签 / 眉题 / 脚线 / 计数 / 图注。

### 展示、正文与铬件字号阶梯

| Token | 字号 | 字体 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.grove-num}` | 18vw | Playfair | 400 | 水印序数数字，6% 不透明度，绝对定位右下 |
| `{typography.display}` | 10vw | Playfair | 400 | 封面 hero 标题 |
| `{typography.quote-mark}` | 8vw | Playfair | 400 | 开引号字形 |
| `{typography.h1}` | 5.5vw | Playfair | 400 | 章节标题、陈述标题 |
| `{typography.stat-value}` | 4.5vw | Playfair | 400 / 珊瑚 | 数据卡片数字值 |
| `{typography.h2}` | 3.2vw | Playfair | 400 | 日常幻灯片标题 |
| `{typography.quote-text}` | 3.2vw | Playfair | 400 斜体 | 引语正文 |
| `{typography.h3}` | 2vw | Playfair | 400 | 副标题、对比面板标题 |
| `{typography.lead}` | 1.45vw | Jost | 300 | 导语段落 |
| `{typography.body-list-emph}` | max(1.4vw, 17px) | Jost | 300 | 列表页正文 / 项目符——为易读而加重 |
| `{typography.body}` | 1.05vw | Jost | 300 | 标准正文段落 |
| `{typography.caption}` | 0.82vw | Jost | 300 | 图注、脚注、图表来源 |
| `{typography.label}` | 0.7vw | JetBrains Mono | 300 / 0.12em | 铬件标签、等宽元信息 |
| `{typography.kicker}` | 0.7vw | JetBrains Mono | 300 / 0.14em / 全大写 | 标题上方的眉题 |
| `{typography.chapter-num}` | 0.7vw | JetBrains Mono | 300 / 0.2em / 全大写 | 章节序数标签 |
| `{typography.stat-label}` | 0.7vw | JetBrains Mono | 300 / 0.12em / 全大写 | 数据数字下方的等宽标签 |

### 默认值
- **日常幻灯片标题的默认字号**：`{typography.h2}`（3.2vw）。
- **章节或陈述标题的默认字号**：`{typography.h1}`（5.5vw）。陈述级时刻专用 `{typography.h1-statement}`，上限 `min(4.5vw, 7.5vh, 88px)`，防止矮视口溢出。
- **封面 hero 标题的默认字号**：`{typography.display}`（10vw）。
- **正文段落的默认字号**：`{typography.body}`（1.05vw），Jost 字重 300。
- **导语 / 介绍段落的默认字号**：`{typography.lead}`（1.45vw）。
- **眉题 / 眉毛标签的默认字号**：`{typography.kicker}`（0.7vw），JetBrains Mono 全大写 0.14em，颜色 `{colors.accent}`。
- **数据卡片数字的默认字号**：`{typography.stat-value}`（4.5vw），Playfair 珊瑚。
- **每一个衬线元素的默认字重**：400。
- **每一个正文 / Jost 元素的默认字重**：300。
- **每一个等宽 / JetBrains 元素的默认字重**：300。

列表式幻灯片上的正文在典型笔记本视口上若 1.05vw 读得太小，系统会提到 `{typography.body-list-emph}`（1.4vw 或 17px 的较大者）。当一页的主内容时刻是正文段落或项目列表时，就用这个加重字号——默认 1.05vw 是按投影观看校准的，不是按笔记本阅读。

### 标志性处理
只要用到对应元素类型，这些处理就**不可省略**：

- **每一个 Playfair 元素都跑字重 400。** 加粗衬线（字重 700）在系统任何地方都不用。这是系统最重要的排印规则。
- **任何 Playfair 标题（h1、h2、h3 或引语）里的 `<em>` 标签，渲染为 `{colors.accent}` 珊瑚斜体。** 这是 Grove 的签名强调——给标题加强调的方式，就是把一个词做成珊瑚斜体。em 样式切换由 CSS 自动完成。
- **引语页上的开引号渲染为巨大的 Playfair 字形，8vw，`{colors.accent}` 珊瑚。** 没有超大珊瑚引号的引语是坏掉的。
- **引语正文始终斜体。** 正体引语文本不在系统里。
- **每一个眉题 / 章节序号 / 脚线 / 标签 / 图注都是 JetBrains Mono 全大写，字距至少 0.12em。** 等宽用句首大写或不加字距，读起来像代码，不像铬件。
- **项目符字形是 em 破折号（`—`），用 JetBrains Mono `{colors.accent}` 珊瑚渲染。** 从不用圆点（`•`），从不用连字符（`-`），从不用星号。em 破折号就是系统的项目符语言。
- **每一条铬件条（顶和底）都带 1px solid `{colors.border}` 线（浅色页用 `{colors.border-light}`）。** 发丝线让铬件读成「页周围的框」，而不是横幅。

### 排印原则
Playfair-400 / Jost-300 / JetBrains-Mono-300 的字重承诺就是系统的声音。改掉其中任何一个字重，都会打破编辑气质。没有字重阶梯——每套字体恰好一个字重。

斜体留给两个特定角色：标题里的珊瑚强调（通过 `<em>`），以及引语正文。不用斜体正文段落。不用下划线。正文里的强调靠 `.accent` 颜色工具（改成珊瑚色），不靠斜体或加粗。

## 版式

### 画布系统
系统面向流体视口——每个 `.slide` 是 `100vw × 100vh`，`padding: {spacing.pad-y} {spacing.pad-x}`（6.5vh / 8vw）。幻灯片并排坐在水平 `#deck` flex 条里，通过 `transform: translateX(...)` 平移，转场用 `{motion.dur-slide}` / `{motion.ease-slide}`。同一时间只有一页是 `is-active`；非活动页把内容保持不可见（`[data-anim]` 为 `opacity: 0`），直到活动类触发入场动画。

### 内边距阶梯
| Token | 取值 | 用途 |
|---|---|---|
| `{spacing.pad-x}` | 8vw | 幻灯片水平内边距 |
| `{spacing.pad-y}` | 6.5vh | 幻灯片垂直内边距 |
| `{spacing.pad-quote-x}` | 8.8vw | 引语页略宽的水平内边距 |
| `{spacing.pad-quote-y}` | 7.8vh | 引语页略高的垂直内边距 |
| `{spacing.gap-lg}` | 4.5vh | 主要内容区块之间 |
| `{spacing.gap-md}` | 2.8vh | 相关元素之间 |
| `{spacing.gap-sm}` | 1.4vh | 紧密耦合元素之间 |

### 铬件解剖
每一页内容页顶部都有一条 **slide-chrome**——一行薄的 flex space-between，两侧各一个等宽标签，下方用 1px 发丝边框隔开——底部有一条 **slide-foot**——匹配的一行，放章节名 + "NN / TT" 计数，上方用匹配的发丝线隔开。

封面、章节、引语和收场页隐藏铬件和脚条——那些是 deck 的无铬件情感时刻。其余每一页都带这个框。

### 圆角
**结构圆角为零。** 没有圆角卡片、没有圆角按钮、没有圆角图片占位。系统里仅有的圆形是视口底部 5px 的导航点（50% 半径——正圆）。

## 层次与纵深

### 扁平，无阴影
系统使用**零 box-shadow、零 text-shadow、零模糊、零渐变**。纵深完全通过以下传达：

1. **1px 发丝线**——顶底铬件条、数据卡片分隔、对比面板分隔、区块分隔线。
2. **文本颜色的不透明度分层**——主（`{colors.fg}`）、弱化（`{colors.fg-2}`）、提示（`{colors.fg-3}`）。三级不透明度阶梯是系统的文本抬升装置。
3. **6% 不透明度的水印数字**——巨大的 Playfair 数字坐在章节与分节页右下角，当作构图纹理，不是 UI。

没有阴影，本身就是抬升语言。加上 `box-shadow: 0 4px 12px rgba(0,0,0,0.1)` 会打碎印刷墨感。

### 水印数字
`{components.grove-num}` 元素是 18vw / 6% 不透明度的 Playfair 数字，绝对定位在 `right: {spacing.pad-x}, bottom: -0.15em`。它读成淡背景纹理，从不当内容。用在章节 / 分节 / 陈述页上，否则空着的右下角会显得没锚。它是纵深语言的一部分，尽管看起来像装饰元素。

## 形状与处理

### 描边粗细与样式
- **1px solid `{colors.border}`** —— 深色页上的通用发丝线。铬件条边框、数据卡片底边、对比面板分隔、全宽区块分隔。
- **1px solid `{colors.border-light}`** —— 浅色页上匹配的发丝线。
- **1px solid `{colors.accent}`** —— 36px 宽的珊瑚线（`{components.rule-coral}`），用作眉题与随后标题之间的构图节拍。

边框从不超过 1px。从不用虚线，从不用点线。1px 发丝线就是系统的结构节奏。

### 装饰元素类型

**幻灯片铬件条**（`{components.slide-chrome}`）—— 薄顶条，两侧等宽标签，下方 1px 发丝线隔开。系统通用的「你在读一页纸」的框。

**幻灯片脚条**（`{components.slide-foot}`）—— 匹配的底条，章节名 + 计数，上方 1px 发丝线隔开。

**珊瑚线**（`{components.rule-coral}`）—— 36px 宽、1px 高的陶土珊瑚水平线。坐在眉题（上）与标题（下）之间的构图节拍。眉题导入主标题时每页用一次——不要叠多条珊瑚线。

**全宽线**（`{components.rule-full}`）—— `{colors.border}` / `{colors.border-light}` 的全宽 1px 发丝分隔。用作幻灯片正文内部的区块断开。

**眉题**（`{components.kicker}`）—— 珊瑚色等宽全大写眉毛，放在 h1 或 h2 标题上方。常与下方的珊瑚线成对。

**章节序号** —— 章节标题上方珊瑚色的等宽全大写序数（`{typography.chapter-num}`）。在章节开场页设定章节身份。

**Em 破折号项目符**（`{components.bullet-list}`）—— 两列网格列表（2em / 1fr），项目符是 JetBrains Mono 渲染的珊瑚 em 破折号字形。从不用真正的圆点（`•`）；始终用 em 破折号。

**Grove 数据**（`{components.grove-stat}`）—— 竖向堆叠：顶部大号 Playfair 珊瑚值（4.5vw），下方等宽全大写标签，1px 底边发丝线。无背景填充——卡片由线和字号比定义，不是由容器盒子定义。

**引号**（`{components.quote-mark}`）—— 巨大的 Playfair 开引号字形，8vw，珊瑚，放在斜体引语正文上方。引语页上始终存在。

**水印数字**（`{components.grove-num}`）—— 右下角 18vw / 6% 不透明度的 Playfair 数字。只作构图纹理，从不当 UI。

**图片占位**（`{components.img-placeholder}`）—— 实心 `{colors.bg-alt}`（深色）或 `{colors.border-light}`（浅色）填充，标记真实 `<img>` 将出现的位置。放一条等宽图注，如 `{colors.fg-3}` 的 "[ image ]"。

**导航点**（`{components.nav-dots}`）—— 视口底部固定的 5px 圆点，指示幻灯片位置。未激活：22% 白。激活：80% 白，1.4× 缩放。

## 应做与不应做

### 应做
- 每一个衬线时刻都跑 Playfair Display 字重 400。从不加粗。
- 在任何 Playfair 标题里用 `<em>` 把一个词切成斜体陶土珊瑚——这是系统的签名强调动作。
- 每一段都跑 Jost 字重 300。更轻的字重是系统的正文声音。
- 每一个标签、眉题、章节序号、脚线、计数和数据图注都跑 JetBrains Mono 字重 300、全大写、至少 0.12em 字距。
- 默认幻灯片背景用 `{colors.bg}`（深森林绿）。引语页以及任何想要字面「纸页」感的时刻，用 `{colors.bg-light}`（羊皮纸）。
- 把眉题与 36px 珊瑚线当作主标题上方的一个构图单元。
- 用珊瑚色 em 破折号字形（`—`）作通用项目符。从不用圆点或连字符。
- 在章节和分节开场页上应用 `{components.grove-num}` 水印数字——右下角需要那个锚。
- 每一个新内容元素都用内置的 `[data-anim]` + `[data-delay]` 动画栈（fade-up / fade-in / reveal-right / reveal-left / scale-in，延迟 0–6）。动画是系统身份的一部分，不是可选抛光。
- 保持幻灯片疏朗——一条标题 + 一段支撑段落 + 一条强调线就是节奏。宁可少元素、大尺寸。

### 不应做
- 不要用加粗衬线。Playfair 字重 700 不在这套系统里。加粗衬线会打破编辑声音。
- 不要在 Playfair、Jost、JetBrains Mono 和 Noto SC 之外引入第四套字体。四家族栈就是全部排印身份。
- 不要把珊瑚当表面填充或正文段落。珊瑚是强调声音：斜体强调、眉题、线、em 破折号项目符、数据数字、引号、章节序数。那就是全部珊瑚词汇。
- 不要用 box-shadow、渐变、模糊或任何 rgba 阴影。系统是扁平的。
- 不要用粗边框（2px+）。1px 发丝线就是系统的结构节奏。
- 不要圆任何角。仅有的圆形是 5px 导航点。
- 不要用圆点、连字符或星号做列表项。珊瑚色 em 破折号是唯一的项目符字形。
- 不要放没有下方珊瑚线的眉题。眉题 → 线 → 标题三元组是一个单元。
- 不要把等宽文本做成句首大写或不加字距。等宽始终是全大写铬件，字距 0.12em+。
- 不要在内容页上省略 slide-chrome 和 slide-foot。顶底细框才让幻灯片读成一页纸。
- 不要挤满画布。Grove 奖励字体周围的静。若一页觉得满，去掉一个支撑元素，而不是缩小字号。

## 响应行为

系统**全程使用 vw / vh 单位**——每一个尺寸、内边距、间隙和线条都与视口成比例。同一构图在 1280×720 笔记本、1920×1080 显示器和 2560×1440 显示上无需断点即可正确渲染。

### 缩放行为
- 展示标题随视口宽度线性缩放（10vw → 1920 时 192px，1280 时 128px）。
- 正文类似缩放（1.05vw → 1920 时 20.16px，1280 时 13.44px）——列表页正文除外，那里 `max(1.4vw, 17px)` 的下限防止较小视口上文字不可读。
- 内边距、间隙和 grove-num 都随 vw/vh 等比缩放。
- 1px 发丝边框是固定像素、不缩放，这意味着更大视口上它们会显得比例更细。这是设计如此。

### 演示行为
- 幻灯片前进：右/下箭头 / 空格 / page-down（由 deck JavaScript 处理）。
- 幻灯片后退：左/上箭头 / page-up。
- 水平 `#deck` 条通过 `transform: translateX(-N * 100vw)` 在页间平移，用 `{motion.dur-slide}` 尖锐减速曲线，时长 0.9s。
- 每一页带 `is-active` 类，触发其上 `[data-anim]` 元素的交错入场动画。
- 底部导航点反映当前幻灯片位置；点击一个点跳到那一页。

### 动画
`[data-anim]` + `[data-delay]` 系统是内置的：
- `fade-up`：opacity 0 → 1，translateY 28px → 0
- `fade-in`：opacity 0 → 1
- `reveal-right`：clip-path inset(0 100% 0 0) → inset(0 0 0 0)
- `reveal-left`：clip-path inset(0 0 0 100%) → inset(0 0 0 0)
- `scale-in`：opacity 0 → 1，scale 0.94 → 1

所有入场动画使用 `{motion.ease-enter}`，时长 `{motion.dur-enter}`（0.7s）。交错延迟：0 / 0.08s / 0.18s / 0.3s / 0.44s / 0.6s / 0.78s。

### 打印 / 导出
系统没有 `@media print` 规则。打印导出会继承水平条布局，不太可能干净分页。把 Grove 当作屏幕优先系统；PDF 导出需要专用打印样式表。

## 中日韩与国际内容

### 推荐中文搭配

| 角色 | 中文字体 | 字重 | 原因 |
|---|---|---|---|
| Display / h1 / h2 / h3（Playfair 角色，2–10vw） | 霞鹜文楷 LXGW WenKai | 400 | 文学、手排的暖意，镜像 Playfair Display 字重 400——从不加粗，恰好是 Grove 规则 |
| 引语正文 / 引号（8vw 引号，3.2vw 正文） | 霞鹜文楷 LXGW WenKai | 400 | 同样的文学暖意承担斜体引语时刻；中文没有斜体，所以由字体做表达工作 |
| 数据数字（4.5vw，珊瑚） | 霞鹜文楷 LXGW WenKai | 400 | 把数据数字留在 Playfair 气质里；珊瑚色承担强调 |
| 水印数字（18vw） | 霞鹜文楷 LXGW WenKai | 400 | 6% 不透明度的水印在这个尺度上，配合 LXGW WenKai 开放的字形效果好 |
| 正文 / 导语（Jost 角色，1.05–1.45vw） | 思源宋体 Noto Serif SC | 300–400 | 明朝体正文声音——平静、文学，像 Jost 字重 300 一样往后退 |
| 标签 / 眉题 / 章节序号（JetBrains Mono 角色） | 思源等宽 Noto Sans Mono CJK SC | 300–400 | 为眉题和脚线保住打字机铬件质感 |

### 中西混排策略

用 **策略 C** —— 拉丁衬线保持 Playfair Display，让中日韩字形落到 LXGW WenKai。Playfair Display 字重 400（从不加粗）是系统最重要的排印承诺；整套换成中日韩衬线会打破定义 Grove 的专著 / 精品品牌手册气质。系统已经按现有字体栈加载 Noto Serif SC / Noto Sans SC 作为回退——改动是把 LXGW WenKai 作为首选中日韩展示字体加在 Noto Serif SC 前面：

```css
/* Playfair roles (display, h1, h2, h3, quote, stat, watermark) */
font-family: 'Playfair Display', 'LXGW WenKai TC', 'Noto Serif SC', Georgia, serif;
/* Jost roles (lead, body, caption) */
font-family: 'Jost', 'Noto Serif SC', system-ui, sans-serif;
/* JetBrains Mono roles (label, kicker, chapter-num, stat-label) */
font-family: 'JetBrains Mono', 'Noto Sans Mono CJK SC', monospace;
```

（注意：系统目前在 Jost 栈里列的是 `'Noto Sans SC'`——就 Grove 的文学气质，改成 `'Noto Serif SC'`。明朝体正文声音比黑体无衬线更接近 Jost 字重 300 的「好纸」手感。）

展示字号（5.5–10vw）上的基线错位很轻——LXGW WenKai 和 Playfair Display 光学基线相近，所以像 `A Quiet 山林` 这样的混排标题读得干净。`<em>` 斜体珊瑚强调规则是更精细的一块（见下方已知中日韩缺口）。


### 加载

用 LXGW WenKai + Noto Serif SC + Noto Sans Mono CJK 配对，替换现有的仅 Noto 回退：

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=LXGW+WenKai+TC&family=Noto+Serif+SC:wght@300;400;500&family=Noto+Sans+Mono+CJK+SC:wght@300;400&display=swap" rel="stylesheet">
```

LXGW WenKai TC 是 Google Fonts 上托管的版本（同时覆盖繁体和简体字形）。

### 通用中日韩调整

这些调整适用于本系统里的**每一个中日韩块**，不论尺寸或角色：

- **把行高放宽 0.05–0.08。** 中日韩字形是全宽方块，视觉重量比拉丁字母大；为拉丁调的行高（展示 1.0–1.1，正文 1.65–1.75）在中文里会读成挤。展示提到 1.15–1.25，正文提到 1.7–1.85。
- **去掉中文标题上的负字距。** Playfair Display 用 -0.01em 到 -0.03em 字距，会把汉字挤在一起。中文段设 `letter-spacing: 0`——若标题看起来仍挤，可用极小的正值 `0.02em`。
- **从不要对中日韩文本使用 `text-transform: uppercase`。** 中文没有大小写；这条 CSS 对汉字什么也不做，却会悄悄弄坏混排行里本该大写的 JetBrains Mono 部分。
- **中文句子里用中文全角标点**（`，。：；！？「」『』（）`），不要用拉丁等价物（`,.:;!?""''()`）。同一句里混用两套标点系统，读起来像排版错误。
- **中文标题末尾不要句号（。）。** 中文标题遵循与拉丁相同的规则——标题式行去掉句末标点。正文段落保留 。
- **在中日韩与拉丁段的交界处应用盘古之白。** 汉字与相邻的拉丁词或数字之间要有空格（或 0.25em 边距），例如 `2026 年 5 月` 而不是 `2026年5月`。可以手打空格，或用 `pangu.js` 一类的自动加空。
- **一句只用一套字体。** 不要在同一句里在 LXGW WenKai 和 Noto Serif SC 之间切换——按角色选字体（展示 = LXGW WenKai，正文 = Noto Serif SC），整段坚持用它。

### 本系统的审美说明

Grove 的整体声音是「文学专著 / 精品品牌手册」，加一个陶土珊瑚强调。对应这种安静权威的中文是**每一个衬线时刻用 LXGW WenKai**（它手排的暖意是最接近 Playfair Display 字重 400 的中文类比）和**正文用 Noto Serif SC 字重 300–400**（匹配 Jost 字重 300 克制的明朝体平静）。避免把中文正文跑在 Noto Sans SC 上——几何无衬线会把系统从「好纸」翻成「现代应用」。

DM Mono 珊瑚色的 em 破折号项目符字形在中文里无需修改即可工作——em 破折号字符本身是同一个 Unicode 字形（—），读成中文列表项前面的刻意标记。项目符列保持 Noto Sans Mono CJK SC 字重 300 珊瑚，恰好镜像拉丁模式。

水印数字（18vw，6% 不透明度）在中文里特别有效——用中文序数字符（例如「三」或「五」）代替西文数字。6% 不透明度时读成淡构图纹理，汉字在该尺度上更密的视觉重量，比纤细的西文数字更能平衡这一页。

### 已知中日韩缺口

系统签名的 `<em>` 斜体珊瑚处理是最难翻译的一块：**中文没有斜体概念**——倾斜的汉字读成坏掉，不像强调。当前 Grove CSS 依赖浏览器默认的 `<em>` 样式（斜体）加上珊瑚色的 CSS 颜色规则。在中文里斜体视觉上什么也不做，所以强调塌成「标题里只是珊瑚色文字」。这并不糟——LXGW WenKai 标题里的珊瑚仍读成刻意强调——但系统失去两个强调维度之一（颜色 + 倾斜），只剩颜色。

**中文标题只用颜色强调**——让珊瑚自己承担重量。句中切换字体不是中文排印惯例；即便觉得少了倾斜对比，在同一标题里把中日韩字形换成另一套字体，读成不一致，而不是有意的编辑强调。正确规则：

```css
.h1 em, .h2 em, .h3 em, .quote-text em {
  color: var(--c-accent);  /* coral — works in Latin and CJK */
  font-style: italic;       /* renders italic in Latin; ignored by CJK glyphs */
  /* deliberately no font-family switch — preserves "one font per sentence" in CJK */
}
```

拉丁部分得到斜体珊瑚；中日韩部分只得到珊瑚。实践中，以中文为主的标题，珊瑚单独就够——若想给中文第二个强调维度，伸手去字重（400 → 700），而不是换字体。

## 迭代指南

1. 任何新标题都是 Playfair Display 字重 400。从标题阶梯里选字号（10vw display / 5.5vw h1 / 3.2vw h2 / 2vw h3）——不要发明新字号。
2. 任何标题里的新强调都用 `<em>`，自动渲染为斜体珊瑚。不要手写颜色/斜体样式。
3. 任何新正文段落都是 Jost 字重 300、1.05vw（导语用 1.45vw，列表式幻灯片用 `max(1.4vw, 17px)`）。
4. 任何新标签 / 眉题 / 脚线 / 计数 / 图注都是 JetBrains Mono 字重 300、全大写、至少 0.12em 字距。
5. 任何新铬件线（顶条、底条、区块分隔、数据卡片边框）都是 1px solid 发丝线，深色用 `{colors.border}`，浅色用 `{colors.border-light}`。不要更粗的边框。
6. 任何新项目列表都用 `{components.bullet-list}` 模式（两列网格，珊瑚色等宽 em 破折号）。不要写另一种项目符样式。
7. 任何新强调时刻都用 `{colors.accent}` 陶土珊瑚。强调用于斜体标题强调、36px 线、em 破折号、数据数字、引号、章节序数，以及眉题文字。别无其他。
8. 任何新章节或分节开场页都在右下角带 `{components.grove-num}` 水印数字。
9. 任何新内容元素都拿 `[data-anim]` 属性（fade-up、fade-in、reveal-right、reveal-left 或 scale-in）加上 `[data-delay]`（0–6）做交错入场。不要写自定义转场。
10. 拿不准时，加空间而不是加内容。Grove 的编辑气质是静，不是密。

## 已知缺口

- 四套 Google Fonts（Playfair Display、Jost、JetBrains Mono、Noto Serif SC / Noto Sans SC）通过 `<link>` 加载。离线渲染会回退到 Georgia、system-ui、monospace，以及 Noto 角色的系统衬线/无衬线——能保住大致性格，但会失去排印身份。离线 / 印刷可靠性建议自托管。
- 系统加载 Playfair 字重 500 和 Jost 字重 200/400/500——已发布 CSS 里不用这些，但它们是可用的。用它们会打破系统的单字重承诺。
- `<em>` 斜体珊瑚处理依赖 CSS 规则 `.h1 em, .h2 em, .h3 em { color: var(--c-accent); }`——注意规则里**没有**设置 italic 属性（注释块是空的）。斜体来自浏览器默认的 `<em>` 样式。若样式表覆盖去掉了默认斜体，珊瑚强调就会失去斜体性格。
- grove-num 水印用 18vw 字号——在极宽视口（3000px+）上会变得很大，可能顶到 slide-foot 区域。CSS 把它放在 `bottom: -0.15em` 以吸收部分溢出，但极宽视口上很高的数字可能需要调整。
- 垂直侧栏组件（`.grove-sidebar`）已加载进 CSS，但明确禁用（`display: none !important`）。它曾是章节标签装饰，读成杂乱；slide-chrome 条已经提供章节名。
- 固定页码计数（`#slide-counter`）也被禁用——slide-foot 条已经显示 "NN / TT"，固定计数是重复。
- CSS 有几处空规则块（`.h1 em { }`、`.grove-stat-val em { }`、`.quote-text { ... }`），看起来是早期迭代留下的残桩。它们是惰性的，删掉没有影响。
- deck 按双语意识搭建（通过 Noto Serif SC / Noto Sans SC 做中文回退），但已发布源里没有实际中文内容——双语支持是结构上的，不是启用中的。
- 图片占位组件是版式预留，不是真图。用 `<img>` 替换占位 div，需要手工匹配父级的 flex 行为和背景。
