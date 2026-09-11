---
version: alpha
name: Pin & Paper
description: A field-notebook editorial system rendered as yellow legal-pad paper with deep cobalt-blue ink. Every slide carries a fractalnoise paper-grain overlay, hand-drawn safety-pin SVG illustrations that "pin" cards to the page, and a hand-script Caveat face for personal annotations. Space Grotesk at heavy weights carries the printed headlines; DM Mono handles archival labels. The aesthetic borrows from analog field reports, vintage public-notice boards, and the diary pages of scientific notebooks — closer to a lab journal pinned to a corkboard than a polished deck.

colors:
  paper: "#EFE56A"
  paper-2: "#F5ECA0"
  paper-3: "#E8D85A"
  paper-extra: "#FBE6A4"
  cream: "#F8F1D6"
  kraft: "#C9A66B"
  ink: "#1F3A8A"
  ink-soft: "#2D4FB8"
  ink-line: "#3457C4"
  ink-deep: "#0E1430"
  red: "#C2342B"
  olive: "#6B7A2E"
  orange: "#D8702A"

color-aliases:
  c-bg: paper
  c-text: ink
  c-card: cream
  c-stamp: red

typography:
  display-mega:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 196px
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: -0.04em
  display-section:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 168px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.04em
  display-stat:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 168px
    fontWeight: 700
    lineHeight: 0.85
    letterSpacing: -0.04em
  h1-cta:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 130px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.035em
  h1-chart:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 110px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.035em
  h2:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 96px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.03em
  h2-md:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 84px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.03em
  h2-sm:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 50px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.02em
  quote-text:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 50px
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: -0.02em
  card-row:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 44px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: -0.02em
  card-h3:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 38px
    fontWeight: 700
    lineHeight: 1.02
    letterSpacing: -0.02em
  card-h3-sm:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.015em
  body:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.45
  body-md:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 21px
    fontWeight: 400
    lineHeight: 1.35
  body-sm:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 19px
    fontWeight: 400
    lineHeight: 1.45
  body-list:
    fontFamily: "Space Grotesk, Helvetica Neue, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.4
  scribble-mega:
    fontFamily: "Caveat, cursive"
    fontSize: 360px
    fontWeight: 700
    lineHeight: 0.8
  scribble-lg:
    fontFamily: "Caveat, cursive"
    fontSize: 70px
    fontWeight: 700
    lineHeight: 0.9
  scribble-md:
    fontFamily: "Caveat, cursive"
    fontSize: 60px
    fontWeight: 700
    lineHeight: 0.9
  scribble-sm:
    fontFamily: "Caveat, cursive"
    fontSize: 38px
    fontWeight: 600
    lineHeight: 1.05
  scribble-xs:
    fontFamily: "Caveat, cursive"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.05
  label-top:
    fontFamily: "DM Mono, ui-monospace, monospace"
    fontSize: 18px
    fontWeight: 500
    letterSpacing: 0.12em
    textTransform: uppercase
  label-meta:
    fontFamily: "DM Mono, ui-monospace, monospace"
    fontSize: 16px
    fontWeight: 500
    letterSpacing: 0.18em
    textTransform: uppercase
  label-footer:
    fontFamily: "DM Mono, ui-monospace, monospace"
    fontSize: 15px
    fontWeight: 500
    letterSpacing: 0.14em
    textTransform: uppercase
  stamp:
    fontFamily: "DM Mono, monospace"
    fontSize: 16px
    fontWeight: 500
    letterSpacing: 0.18em
    textTransform: uppercase

spacing:
  pad-edge: 64px
  pad-top: 110px
  pad-bottom: 90px
  card-pad-md: "28px 28px 24px"
  card-pad-lg: "32px 22px 22px"
  card-pad-xl: "36px 28px 28px"
  card-pad-quote: "60px 80px"
  grid-gap-sm: 22px
  grid-gap-md: 28px
  grid-gap-lg: 32px

canvas:
  width: 1920px
  height: 1080px

components:
  paper-surface:
    background: "radial-gradient(120% 90% at 20% 10%, rgba(255,255,255,.18), transparent 60%), radial-gradient(140% 100% at 80% 95%, rgba(0,0,0,.05), transparent 55%), {colors.paper}"
    description: "Default slide surface — yellow paper with a soft upper-left highlight gradient and a soft lower-right shadow gradient layered over the base paper color."
  paper-grain-overlay:
    selector: ".slide::before"
    background: "fractalNoise SVG via data URI, baseFrequency=1.4, octaves=2"
    opacity: 0.35
    mixBlendMode: multiply
    description: "Non-optional fractal-noise paper grain overlay on every slide. Lives on the ::before pseudo-element; opacity 0.35, multiply blend. On ink slides, opacity drops to 0.25 with screen blend."
  pinned-card:
    background: "{colors.cream}"
    border: "1.5px solid {colors.ink}"
    borderRadius: 4px
    boxShadow: "5px 6px 0 0 {colors.ink}"
    padding: "{spacing.card-pad-md}"
    description: "Cream paper card with a 1.5px ink border, 4px micro-radius, and a hard 5px-6px ink-blue offset shadow. The system's universal card pattern — every card looks like a piece of paper pinned to the surface."
  pinned-card-alt:
    background: "{colors.paper-2}"
    description: "Card variant using the lighter paper-2 tone. Used to break up adjacent same-tone cards."
  pinned-card-alt2:
    background: "{colors.paper-extra}"
    transform: "rotate(0.6deg)"
    description: "Card variant with the deepest paper tone and a slight rotation (0.6 to 1.5 degrees) — gives the impression of being pinned slightly askew."
  pin-illustration:
    width: "varies (110–640px)"
    color: "currentColor"
    transform: "rotate(-14deg to +20deg)"
    description: "Hand-drawn safety-pin SVG illustration in ink-blue or paper (when on ink surface). Multiple variants: closed pin (#pin), open pin (#pin-open). Always rotated slightly off-axis. Acts as both decoration and the visual signal that a card is 'pinned' to the page."
  scribble:
    fontFamily: "Caveat, cursive"
    color: "{colors.ink}"
    lineHeight: 1.05
    description: "Caveat hand-script face used for handwritten notes, marginalia, and 'me' voice annotations. May be rotated slightly (-3 to -1.5 degrees) and underlined via 2px solid ink for emphasis."
  stamp:
    border: "3px solid {colors.red}"
    color: "{colors.red}"
    padding: "6px 16px"
    fontFamily: "DM Mono, monospace"
    fontSize: 16px
    letterSpacing: 0.18em
    textTransform: uppercase
    transform: "rotate(-4deg)"
    description: "Cinnabar-red rubber stamp — 3px solid red border, red mono text, rotated -4 degrees. Used for status marks like CONFIDENTIAL or RECEIVED."
  top-chrome:
    position: "absolute; top: 44px; left: 64px; right: 64px"
    fontFamily: "DM Mono, ui-monospace, monospace"
    fontSize: 18px
    fontWeight: 500
    letterSpacing: 0.12em
    textTransform: uppercase
    description: "Top metadata band — brand lockup on left (with inline #mark SVG glyph), meta tags on right. Mono uppercase, line-height 1."
  footer-chrome:
    position: "absolute; left: 64px; right: 64px; bottom: 36px"
    fontFamily: "DM Mono, ui-monospace, monospace"
    fontSize: 15px
    fontWeight: 500
    letterSpacing: 0.14em
    textTransform: uppercase
    opacity: 0.65
    description: "Bottom metadata band — typically left-source + right-page-position pair at 65% opacity."
  pin-glyph-closed:
    svgId: "#pin"
    viewBox: "0 0 360 110"
    description: "Closed safety-pin SVG glyph — coiled spring on the right, shaft sweeping left, oval clasp cap on the left."
  pin-glyph-open:
    svgId: "#pin-open"
    viewBox: "0 0 360 130"
    description: "Open safety-pin SVG glyph — clasp lifted, sharp point exposed pointing left."
  mark-glyph:
    svgId: "#mark"
    viewBox: "0 0 32 16"
    description: "Small inline mark glyph for the top-chrome brand lockup — circle on the right, arrow shaft pointing left."
  table-cell:
    padding: "18px 22px"
    borderBottom: "1.5px solid rgba(31,58,138,.5)"
    borderRight: "1.5px solid rgba(31,58,138,.5)"
    fontSize: 21px
    lineHeight: 1.35
    description: "Comparison table cell with semi-transparent ink-blue dividers. Sits inside the same cream + ink-border + offset-shadow card pattern."
  pill-yes:
    background: "{colors.ink}"
    color: "{colors.paper}"
    border: "1.5px solid {colors.ink}"
    borderRadius: 999px
    padding: "4px 14px"
    fontFamily: "Caveat, cursive"
    fontSize: 28px
    fontWeight: 600
    description: "Affirmative pill — solid ink fill with paper text, rounded 999px, Caveat script face. Unusual treatment: handwritten letterforms inside a UI pill shape."
  pill-no:
    background: transparent
    color: "{colors.red}"
    border: "1.5px solid {colors.red}"
    fontFamily: "DM Mono, monospace"
    fontSize: 16px
    letterSpacing: 0.14em
    textTransform: uppercase
    description: "Negative pill — red mono uppercase text in a red-bordered transparent pill. The only place red appears in regular use (outside the stamp component)."
  pill-part:
    background: "{colors.paper-2}"
    color: "{colors.ink}"
    fontFamily: "Caveat, cursive"
    description: "Partial-state pill — light paper fill with Caveat script ink text."
  number-script:
    fontFamily: "Caveat, cursive"
    fontWeight: 700
    fontSize: "60–70px"
    color: "{colors.ink}"
    description: "Hand-script numeral used as step numbers in process diagrams and ordered CTA steps. The script face makes ordering feel hand-counted, not algorithmic."
---

## 概览

Pin & Paper 是一套**野外笔记本编辑系统**，建立在单一材料前提上：每一页都是黄色 legal-pad 纸。纸通过基色（`{colors.paper}` —— 饱和镉黄）、两道柔径向渐变高光（左上亮、右下影），以及 `::before` 伪元素上不可省略的分形噪点颗粒叠层（multiply 混合）来渲染。这套叠层做出在斜光下读作实体纸的表面。没有颗粒，系统塌成扁平卡通黄；纹理是根基，不是装饰。

字体栈是刻意的三声线编辑配对。**Space Grotesk** 字重 600–700 承担每一个印刷标题和展示瞬间——重字重下紧的几何性格读起来像海报或布告栏打印件。**Caveat**（手写字体）承担每一个手写瞬间：页边批注、「我」的声线注释、步骤数字、pill 标签、超大手写序数。Caveat 是系统的私人声线机制——手写一出现，语气就从「正式布告」切到「页边手写便条」。**DM Mono** 字重 500 承担每一个档案元数据标签：顶栏品牌 lockup、页脚 meta、来源归属、坐标轴标签。三声线——印刷标题、手写便条、档案编目标签——互不重叠，系统的编辑节奏取决于它们各守其道。

色板锚定在黄蓝互补对上。**Paper yellow**（`{colors.paper}` 及其三个近变体）是每一块表面。**Ink blue**（`{colors.ink}` —— 深钴蓝 #1F3A8A）是每一个文字瞬间、每一条描边、每一条分割、每一个别针插图。**Cream**（`{colors.cream}`）是卡片背景——更冷静的偏白象牙调，让卡片从大声黄页上视觉后退。**Cinnabar red**（`{colors.red}` — #C2342B）只用于两个特定角色：旋转橡皮章组件和否定态 pill。红从不以这两个角色之外的文字、填色或描边出现。第三档颜色（olive、orange、kraft）存在于 token 列表，但源里没有积极部署。

纵深通过单一招牌机制做出：**硬偏移阴影**。每张卡片带着 `5px 6px 0 0 {colors.ink}`（或 `4px 5px 0 0`，最大引文面板用 `8px 9px 0 0`）——实心墨蓝矩形向右下偏移，零模糊。这层阴影加上 4px 微圆角再加 1.5px ink 描边，定义了通用卡片模式。卡片看起来被别住、从页面略抬起；硬偏移是系统唯一的纵深语言。

**密度哲学：中密、填满。** 当卡片以清楚的排布别满一页时，Pin & Paper 读起来才有权威——通常每页 3 到 6 张卡片，每张带着标题、正文块，常常还有手写页边批注。一页只有居中标题、其余空着读起来像坏掉——系统设计成填满的野外笔记本页，大半空白的笔记本页读起来不完整。卡片应填满；别针应出现；手写层应至少在一半页面上加一条页边便条。例外是封面和章节分隔页，惯例上更疏，但用超大展示字体（196px）和大别针插图补偿。

**关键特征：**
- 黄纸背景（`{components.paper-surface}`）带两层径向渐变，以及每一页不可省略的分形噪点颗粒叠层（`{components.paper-grain-overlay}`）。
- 深钴蓝墨水（`{colors.ink}`）作为通用文字、描边、分割和别针插图色。
- 奶油卡片表面（`{colors.cream}`）配 1.5px ink 描边、4px 微圆角，以及**硬墨蓝偏移阴影**（5px–6px，零模糊）。
- 手绘安全别针 SVG 插图（`{components.pin-illustration}`）——闭合与打开变体——以略旋转角度别在卡片上。
- 三声线排印：Space Grotesk 做印刷标题，Caveat 手写做私人声线，DM Mono 做档案标签。
- 招牌朱砂红旋转橡皮章（`{components.stamp}`）做状态标记（CONFIDENTIAL、RECEIVED 等）。
- 每张卡片 4px 微圆角；pills 走全 999px。
- 交替卡片上轻微面板旋转（0.6 到 1.5 度），做出「别歪了」的效果。

## 颜色

### 色板

- **Paper Yellow**（`{colors.paper}` — #EFE56A）：主导表面色。饱和镉黄。叠上径向渐变和颗粒后，这就是让幻灯片读作实体纸的东西。
- **Paper Light**（`{colors.paper-2}` — #F5ECA0）：更浅、饱和度更低的黄。用作交替卡片填色，打破相邻同调卡片。
- **Paper Deep**（`{colors.paper-3}` — #E8D85A）：更深、更饱和的黄。用在 `.deep` 幻灯片变体上，做更高对比瞬间。
- **Paper Extra**（`{colors.paper-extra}` — #FBE6A4）：带一丝奶油的暖黄，用作最能区分的卡片变体——常配轻微旋转。
- **Cream**（`{colors.cream}` — #F8F1D6）：卡片背景。柔偏白象牙，让卡片从大声黄页上后退。用在每一张标准卡片表面上。
- **Kraft**（`{colors.kraft}` — #C9A66B）：暖棕/牛皮纸调。在 token 系统里已定义，但源里没有积极使用。
- **Ink Blue**（`{colors.ink}` — #1F3A8A）：深钴蓝海军。通用文字、描边、分割、别针插图和阴影色。系统的结构身份。
- **Ink Soft**（`{colors.ink-soft}` — #2D4FB8）：略浅的钴蓝变体；可用但很少用。
- **Ink Line**（`{colors.ink-line}` — #3457C4）：略亮的钴蓝，用于线条装饰；很少用。
- **Ink Deep**（`{colors.ink-deep}` — #0E1430）：近黑带轻微蓝偏。用于 `.ink` 幻灯片变体背景。
- **Cinnabar Red**（`{colors.red}` — #C2342B）：印章色以及否定 pill 的描边/文字色。只用于两个角色——从不当通用强调。
- **Olive**（`{colors.olive}`）和 **Orange**（`{colors.orange}`）：已定义但未启用。作为预留第三档色可用。

### 默认

- **默认幻灯片表面**：`{components.paper-surface}` —— 带分层渐变的黄纸。始终如此。
- **默认表面颗粒**：`{components.paper-grain-overlay}`，不透明度 0.35，multiply 混合。不可省略。
- **默认主标题色**：黄表面上 `{colors.ink}`；墨表面上 `{colors.paper}`。
- **默认正文字色**：黄/奶油上 `{colors.ink}`；墨上 `{colors.paper}`（闷导语用 `opacity: 0.85`）。
- **默认卡片表面**：`{colors.cream}`。伸手去拿 `{colors.paper-2}` 或 `{colors.paper-extra}` 来打破相邻同调卡片。
- **默认描边色**：`{colors.ink}` 1.5px。始终如此。
- **默认阴影**：`5px 6px 0 0 {colors.ink}`（硬偏移，零模糊）。较小卡片可用 `4px 5px 0 0`；最大引文面板用 `8px 9px 0 0`。
- **默认标签 / 元数据色**：chrome 和页脚用 `{colors.ink}`，不透明度 0.65–0.75。
- **默认 scribble / 手写色**：`{colors.ink}`。Caveat 在黄上始终是墨蓝。
- **默认印章色**：`{colors.red}` —— 红的唯一常规用途。

奶油是卡片填色；黄是页面填色。混用会打破视觉层级：黄卡片在黄页上消失；奶油卡片在奶油页上塌掉分层纸的读法。

## 字体

### 字族

系统加载三套 web 字体：**Space Grotesk**（字重 400、500、600、700）承担所有印刷展示和正文；**Caveat**（字重 500、600、700）承担所有手写 / 私人声线瞬间；**DM Mono**（字重 400、500）承担所有档案元数据。

每张脸的情感声线都不同，而且承重：
- Space Grotesk 读作**印刷的、正式的、排好的** —— 文件本身的声线。
- Caveat 读作**手写的、私人的、页边便条** —— 读这份文件的人的声线。
- DM Mono 读作**档案的、目录卡的、索引的** —— 把文件归档的系统的声线。

一条关键行内混用规则：**嵌在 Caveat 数字里的 `<small>` 元素切到较小的 60px Caveat**，用于单位后缀（如 `M`、`×`、`%`）。手写后缀保住父数字那种手点过的感觉。

第二条行内混用规则：**Caveat scribble 文字里的 `.underline` span 得到 2px solid 墨蓝下划线** —— 用来模仿手画强调下划线。

### 字号阶梯

| Token | 字号 | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.scribble-mega}` | 360px | Caveat | 700 | 装饰性超大引号字形 |
| `{typography.display-mega}` | 196px | Space Grotesk | 700 | 封面标题 |
| `{typography.display-section}` | 168px | Space Grotesk | 700 | 章节分隔标题（在 ink 页上） |
| `{typography.display-stat}` | 168px | Space Grotesk | 700 | 英雄统计数字 |
| `{typography.h1-cta}` | 130px | Space Grotesk | 700 | 收束 CTA 标题 |
| `{typography.h1-chart}` | 110px | Space Grotesk | 700 | 图表页标题 |
| `{typography.h2}` | 96px | Space Grotesk | 700 | 标准议程或统计标题 |
| `{typography.h2-md}` | 84px | Space Grotesk | 700 | 密页里的章节标题 |
| `{typography.scribble-lg}` | 70px | Caveat | 700 | 流程步骤数字 |
| `{typography.scribble-md}` | 60px | Caveat | 700 | CTA 步骤数字、大手写强调 |
| `{typography.quote-text}` | 50px | Space Grotesk | 500 | 拉引文正文 |
| `{typography.h2-sm}` | 50px | Space Grotesk | 700 | 布告页标题 |
| `{typography.card-row}` | 44px | Space Grotesk | 600 | 议程行标签 |
| `{typography.card-h3}` | 38px | Space Grotesk | 700 | 卡片标题 |
| `{typography.scribble-sm}` | 38px | Caveat | 600 | 封面上的手写页边便条、布告卡 meta |
| `{typography.scribble-xs}` | 32px | Caveat | 600 | 卡片内小号手写批注 |
| `{typography.card-h3-sm}` | 28px | Space Grotesk | 700 | 子卡片标题 |
| `{typography.body}` | 22px | Space Grotesk | 400 | 标准正文段落 |
| `{typography.body-md}` | 21px | Space Grotesk | 400 | 表格内正文 |
| `{typography.body-sm}` | 19px | Space Grotesk | 400 | 密卡片里的紧凑正文 |
| `{typography.body-list}` | 18px | Space Grotesk | 400 | 卡片内列表项 |
| `{typography.label-top}` | 18px | DM Mono | 500 | 顶栏品牌 lockup 与 meta |
| `{typography.label-meta}` | 16px | DM Mono | 500 | 日期条、归属 |
| `{typography.stamp}` | 16px | DM Mono | 500 | 印章文字 |
| `{typography.label-footer}` | 15px | DM Mono | 500 | 页脚 chrome |

### 默认

- **默认主内容标题**：`{typography.h2}`（96px Space Grotesk 700）。
- **默认封面 / 开场标题**：`{typography.display-mega}`（196px）。
- **默认章节分隔标题**：`{typography.display-section}`（168px），用在墨蓝页变体上。
- **默认正文段落字号**：`{typography.body}`（22px）。密的多卡片页降到 `{typography.body-sm}`（19px）。
- **默认卡片标题**：标准卡片用 `{typography.card-h3}`（38px）；子卡片用 `{typography.card-h3-sm}`（28px）。
- **默认统计数字**：`{typography.display-stat}`（168px）——配 Caveat `<small>` 后缀做单位（M、%、×）。
- **默认标签 / chrome 字号**：顶栏用 `{typography.label-top}`（18px）；底部用 `{typography.label-footer}`（15px）。
- **默认手写批注字号**：页边便条用 `{typography.scribble-sm}`（38px）；步骤数字用 `{typography.scribble-lg}`（70px）。
- **任何展示元素的默认字重**：700。
- **正文默认字重**：400。

拿不准时，规范卡片构图是：38px Space Grotesk 卡片标题 + 22px Space Grotesk 正文段落 + 底部 32px Caveat 手写便条。那三层排印节奏（印刷标题、印刷正文、手写页边便条）是系统最可辨认的内部模式。

### 招牌处理

对应元素类型一旦用上，这些处理**不可省略**：

- **每一页都带着纸颗粒叠层（`{components.paper-grain-overlay}`）。** 没有它，纸美学就塌。颗粒是表面的一部分，不是装饰点缀。
- **每张卡片都带着 1.5px solid ink 描边、4px border-radius，以及硬墨蓝偏移阴影（偏移 5–8px，零模糊）。** 三者一起——缺阴影让卡片觉得没被别住；缺描边让它觉得没印过。
- **Caveat 始终是墨蓝**（`{colors.ink}`）在黄/奶油表面上，在墨表面上始终是纸黄。其他颜色的 Caveat 不存在。
- **别针插图（`{components.pin-illustration}`）始终离轴旋转**（典型范围：-14° 到 +20°）。0° 旋转渲染的别针打破手别美学。
- **印章组件（`{components.stamp}`）始终旋转 -4°**，3px solid 红描边、红等宽文字、零圆角。印章文字始终是 DM Mono 全大写。
- **每一个 Space Grotesk 展示标题用负字距**，范围 -0.02 到 -0.04em。越大越紧。
- **手写数字（Caveat 60–70px）是流程图和有序 CTA 列表里唯一的步骤编号机制。** 不要换成 Space Grotesk 数字。
- **顶栏 lockup 在品牌文字旁包含行内 `#mark` SVG 字形。** 这个字形是品牌身份的一部分，不可省略。

### 排印原则

Pin & Paper 的节奏是**印刷标题 + 印刷正文 + 手写页边便条 + 等宽档案标签** —— 四声线，各自在指定的脸上。换任何一声线（例如页边便条用 Space Grotesk，或正文段落用 Caveat）都会塌掉系统的编辑声线。

不用斜体字形。下划线只用于 Caveat scribble 文字里的 `.underline` span（2px solid ink）。正文里粗体很少；强调要么切到更重、更大的 Space Grotesk，要么在下面加一条 Caveat 手写批注。

## 布局

### 画布系统

系统瞄准**固定 1920×1080 画布**，渲染在 `<deck-stage>` web component 里。所有尺寸像素固定；舞台负责按比例缩放到浏览器视口。

大多数页面用**绝对定位**，内容舞台用边缘锚定元素（`left: 64px`、`right: 64px`、`top: 110px`、`bottom: 100px`），卡片行再用定向网格布局。别针插图是叠在卡片堆上的绝对定位覆盖。

### 内边距与锚定

| 锚点 | 值 | 用途 |
|---|---|---|
| `pad-edge` | 64px | 每一页的左右边缘内缩 |
| `pad-top` | 110px | 内容顶内缩（在 44px 顶栏之下） |
| `pad-bottom` | 90px | 内容底内缩（在 36px 页脚 chrome 之上） |
| `grid-gap-sm` | 22px | 流程卡片间隙 |
| `grid-gap-md` | 28px | 布告 / 统计卡片间隙 |
| `grid-gap-lg` | 32px | 便条网格间隙 |

卡片内部通常顶部 padding `28px–36px`，两侧 `22px–28px`，底部 `22px–28px`。

### Chrome 画框

每一页带着 **顶栏 chrome 带**，上 44px / 左右 64px —— 左边品牌 lockup（带行内 #mark SVG 字形），右边一对 meta 标签。Chrome 是 DM Mono 全大写 18px，字距 0.12em。

每一页还带着 **页脚 chrome**，下 36px / 左右 64px —— 通常左边来源归属，右边页码位置标记。页脚是 DM Mono 全大写 15px，字距 0.14em，不透明度 65%。

在墨蓝页上，两道 chrome 都翻成 `{colors.paper}`，颗粒叠层改成不透明度 0.25、screen 混合模式。

## 纵深与抬升

### 硬偏移阴影（主纵深）

系统唯一的纵深处理是每张卡片上的**硬墨蓝偏移阴影**：`5px 6px 0 0 {colors.ink}`（标准），`4px 5px 0 0`（紧凑），`6px 7px 0 0 rgba(239,229,106,.25)`（带黄调阴影的图表卡），或 `8px 9px 0 0`（最大引文面板）。阴影始终实心、始终右下偏移、始终零模糊。系统里任何地方都没有模糊投影。

### 纸纹理纵深

分形噪点颗粒（`{components.paper-grain-overlay}`）不透明度 0.35、multiply 混合，加上一层微妙的感知纵深——纹理做出读作纸纤维的微变化。这是表面级纵深，不是元素级。

### 别针插图作为纵深信号

手绘安全别针 SVG 放在卡片顶边（通常 `position: absolute; top: -14 to -22px; left: 28–90px; transform: rotate(-6 to -12deg)`），做出卡片被别在页面上的视觉错觉。别针是纵深叙事：卡片顶上出现别针，解释了为什么卡片有阴影和旋转。

### 交替卡片上的轻微旋转

有些卡片变体（`{components.pinned-card-alt2}`）带着轻微旋转（`transform: rotate(0.6deg)` 到 `rotate(1.5deg)`），读作一张别得略歪的纸。这是刻意的不完美——惜用（每页一两张卡片），不是每张都转。

## 形状与处理

### 圆角

| 值 | 用途 |
|---|---|
| 0px | 印章、别针字形、页码 |
| 4px | 卡片、面板、表格容器、图片包裹——系统的微圆角 |
| 999px | 仅 pills |

系统在每张卡片上用 **4px 微圆角** —— 小到读作「印刷边角略洇」，而不是圆角 UI。Pills 是唯一的圆形状；pills 用不寻常的处理：里面是 Caveat 手写字形。

### 描边粗细

- **1.5px solid `{colors.ink}`** —— 通用卡片描边。用于每一张奶油卡、每一个表格容器、每一块面板。
- **1.5px dashed rgba(31,58,138,.45)** —— 用作议程行之间、CTA 步骤之间，以及卡片内来源注释顶部的点状分隔。加上「方格纸换行」感。
- **3px solid `{colors.red}`** —— 只用于印章组件（`{components.stamp}`）。
- **2px solid `{colors.ink}`** —— 只用于 Caveat `.underline` span 处理。

### 装饰元素类型

**别针插图（`{components.pin-illustration}`）** —— 定义性视觉招牌。手绘安全别针 SVG（两种变体：闭合与打开），以 `currentColor` 渲染并略角旋转。别针出现在卡片顶上、封面上的装饰覆盖、章节分隔上的超大强调插图（宽可到 640px），以及别在议程行上。别针是系统的声线——别针一出现，页面就读作被别住的文件。

**印章（`{components.stamp}`）** —— 朱砂红旋转橡皮章标签，3px solid 红描边、红等宽全大写文字、-4° 旋转。用于状态标记（CONFIDENTIAL、RECEIVED）。印章是本系统使用红色的两个角色之一。

**Scribble（`{components.scribble}`）** —— Caveat 手写文字块，常旋转 -1.5° 到 -3° 做出「手写」感。用于页边便条、「我」的声线注释、大手写强调。可含 `.underline` span 做手写强调。

**被别住的卡片（`{components.pinned-card}`）** —— 通用卡片模式：奶油填色、1.5px ink 描边、4px 微圆角、5–6px 硬 ink 偏移阴影。常带着重叠顶边的别针插图。三种交替填色打破相邻同调卡片。

**顶栏 lockup** —— 品牌文字配行内 #mark SVG 字形（右边一个圆，箭头杆指向左）。这个字形是品牌身份的一部分。

**虚线描边分隔** —— 用作议程列表、CTA 步骤列表的行间分割，以及卡片内来源归属分隔。始终是 `1.5px dashed rgba(31,58,138,.45)`。

**Caveat pills（`{components.pill-yes}`、`{components.pill-part}`）** —— 里面是手写字形的 pills（Caveat 28px），实心或纸调填色。圆角 UI 形状与手写文字的错配是刻意的。

**流程 / CTA 手写数字** —— 卡片或列表行里的 Caveat 60–70px 序数。手写数字信号「用手点过的步骤，不是算法点的」。

**超大手写引号** —— 引文页上 360px Caveat 作为开场字形。手写尺寸推进到装饰领域；字形大到充当构图，不是标点。

## 该做与不该做

### 该做
- 每一页叠纸颗粒（`{components.paper-grain-overlay}`）。纹理是纸读法的根基。
- 每张卡片用通用模式：1.5px ink 描边 + 4px 圆角 + 硬 ink 偏移阴影。三者一起定义卡片。
- 每一个印刷标题用 Space Grotesk 字重 700 大小写混排（加负字距）。
- 每一个手写或私人声线瞬间用 Caveat——页边便条、步骤数字、pill 文字。手写是系统的「我」声线。
- 每一个档案标签、chrome 标签和页脚字符串用 DM Mono 全大写，字距 0.12–0.18em。
- 每一个别针插图离轴旋转（典型范围 -14° 到 +20°）。0° 旋转的别针打破手别美学。
- 填满卡片。3–6 张卡片别满一页、各带标题 + 正文 + 页边便条时，系统才读作权威。
- 用旋转印章组件（`{components.stamp}`）做状态标记。-4° 旋转就是它的身份。
- 在流程和 CTA 列表里，把 Caveat 步骤数字与 Space Grotesk 卡片标题配对。手写数字是系统的排序声线。
- 每页在一张卡片上用轻微旋转（0.6° 到 1.5°）做「别歪了」效果。不要每张都转。

### 不该做
- 不要省略纸颗粒叠层。没有它，表面塌成扁平卡通黄。
- 不要用别的列表标记替换 Caveat 手写数字。步骤号始终是手写。
- 不要在印章和否定 pill 之外用红。红只是双角色强调。
- 不要以 0° 旋转渲染别针插图。离轴倾斜才让它们读作物理别针。
- 不要用模糊阴影。卡片只用硬墨蓝偏移阴影。
- 不要在黄页表面上用黄填卡片。卡片是奶油；奶油卡与黄页的对比才是分层纸信号。
- 不要把正文放进 Caveat。手写给页边便条和强调，从不当段落。
- 不要把标题文案放进 DM Mono。等宽是档案声线，不是编辑声线。
- 不要在卡片上用大于 4px 的圆角。微圆角是印刷边角信号；更大圆角塌成通用 UI。
- 不要构图近乎空白的一页。系统设计成填满的笔记本页；稀疏读起来像坏掉。

## 响应式行为

系统瞄准**固定 1920×1080 画布**，渲染在 `<deck-stage>` web component 里（经由 `deck-stage.js` 加载）。舞台负责按比例缩放到浏览器视口——画布内所有像素固定尺寸均匀缩放。

### 演示行为
- `<deck-stage>` 组件管理导航、缩放和演示 chrome。
- 键盘、触摸和鼠标滚轮导航由舞台组件处理。
- 无论视口大小，幻灯片画布恒为 1920×1080。

### 打印行为
打印导出取决于 deck-stage 组件的打印处理。分形噪点颗粒叠层可能不会在所有 PDF 导出里渲染——假设纹理能迁过去之前先测试。

## CJK 与国际内容

### 推荐中文搭配

| 角色 | 拉丁字体 | 中文字体 | 字重 |
|---|---|---|---|
| Display / headline（Space Grotesk 700） | Space Grotesk | 龙藏体 Long Cang | 400（仅有的字重） |
| Body（Space Grotesk 400） | Space Grotesk | 霞鹜文楷 LXGW WenKai | 400 |
| Handwritten / scribble（Caveat） | Caveat | 龙藏体 Long Cang | 400 |
| Label / mono（DM Mono UPPERCASE tracked） | DM Mono | 霞鹜文楷 LXGW WenKai | 400（不要对 CJK 强制等宽） |

### 中英混排策略

策略 A —— 把每个 token 的 `fontFamily` 扩展为拉丁字体后面跟中文字体。Space Grotesk 展示 token 变成 `"Space Grotesk, Long Cang, Helvetica Neue, Arial, sans-serif"`；Space Grotesk 正文 token 变成 `"Space Grotesk, LXGW WenKai, Helvetica Neue, Arial, sans-serif"`；Caveat token 变成 `"Caveat, Long Cang, cursive"`。拉丁字形用原字体渲染；CJK 自动落下。

### 加载

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Caveat:wght@500;600;700&family=DM+Mono:wght@400;500&family=Long+Cang&display=swap" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/cn-fontsource-lxgw-wen-kai-regular/font.css" rel="stylesheet">
```

### 通用 CJK 调整

- 行高：正文 1.75–1.85，展示 1.15–1.25
- 字距：CJK 为 0
- Text-transform：CJK 不强制全大写
- 全角标点 （，。：；！？「」（））
- 展示标题不加句号（中文排印惯例）
- 盘古之白（CJK 与拉丁之间加空格：`使用 Claude` 而不是 `使用Claude`）
- 一句一字体

### 本系统的审美说明

Pin & Paper 是整座库里对中文适配最强的一套。黄 legal-pad 表面、钴蓝墨、安全别针插图和野外笔记本声线，都自然迁进中文——系统在两种脚本里都读作笔记本 / 手账页。

**龙藏体 Long Cang** 是硬笔手写中文字——无毛笔、圆珠笔写在纸上的中文手写对等。它是本系统里 Space Grotesk + Caveat 双重标题-与-scribble 声线的完美中文替身。大字号 Long Cang（96–168px）读作自信的手写野外笔记标题——正是 Pin & Paper 想唤起的。用它同时承担展示标题和 Caveat 对等的 scribble 层。纯中文里叠两套视觉不同的手写没有必要；Long Cang 两角都扛。

**霞鹜文楷 LXGW WenKai** 是为屏幕阅读设计的楷书派生正文字——带着手写楷书的温度和轻微不规则，但在正文字号（18–22px）仍清晰。它是 Long Cang 手写展示最强的对位，并精确匹配系统「野外笔记本私人声线」的声线。每一个中文正文段落设成 LXGW WenKai 400。

别针插图、旋转红章、带硬 ink 偏移阴影的奶油卡片——全部原样迁移。Caveat pill 组件（圆角 pill 里的手写字母）迁成同一 pill 形状里的 Long Cang，在中文里读作迷人的手点过。

系统最可辨认的节奏（印刷标题 + 印刷正文 + 手写页边便条）变成（Long Cang 标题 + LXGW WenKai 正文 + 略不同字号的 Long Cang 页边便条）。纯中文里的声线区分来自字号、旋转和颜色，而不是换脸——页边里旋转 -3° 的 38px Long Cang，对照标题里直立 96px Long Cang，清楚读作「页边批注」。

DM Mono 全大写宽字距标签迁不到 CJK。顶栏里的中文元数据应用 LXGW WenKai 400 大小写混排、字距 0。纯拉丁元数据（日期字符串、来源 URL）留在 DM Mono。

### 已知 CJK 缺口

Long Cang 和 LXGW WenKai 视觉相邻——都带着手写楷书 DNA。三声线编辑配对（印刷 / 手写 / 档案）在纯中文里塌成两声线配对（手写展示 / 手写正文 / 仅拉丁档案）。这不是 bug——Pin & Paper 的纯中文文稿读起来比拉丁对应更均匀地被手碰过，这实际上更接近系统瞄准的野外笔记本美学。

## 迭代指南

1. 每一张新页背景都是 paper-surface（`{components.paper-surface}`），颗粒叠在 `::before` 上。不要跳过纹理。
2. 每一张新卡片用通用模式：奶油填色、1.5px ink 描边、4px 圆角、硬 ink 偏移阴影。不要自定义。
3. 每一个新标题是 Space Grotesk 字重 700 大小写混排加负字距。不要伸手去拿别的字重。
4. 每一个新步骤数字或有序列表标记是 Caveat 手写 60–70px。不要换成数字字体。
5. 每一个新标签或元数据标记是 DM Mono 全大写，字距 0.12–0.18em。
6. 每一个新别针插图离轴旋转。要「别牢」感选闭合（#pin）；要「掀起」感选打开（#pin-open）。
7. 要给卡片加私人声线，在底部追加 Caveat 页边便条——通常带 `.underline` span 做手写强调。
8. 要给卡片标状态，把印章组件（`{components.stamp}`）以轻微旋转放在卡片上部。
9. 要打破相邻同调卡片，在 cream、paper-2 和 paper-extra 填色之间交替。给一张卡片加轻微旋转求变化。
10. 要用墨蓝表面变体（例如章节分隔），把文字色翻成 `{colors.paper}`，并把颗粒不透明度降到 0.25、screen 混合模式。

## 已知缺口

- 系统依赖经由 `deck-stage.js` 加载的 `<deck-stage>` web component。没有它，1920×1080 画布不会缩放，幻灯片会按原生像素尺寸渲染。
- 别针插图作为文档顶部的行内 SVG symbol 定义嵌入。需要别针插图的新页必须通过 `<use href="#pin">` 或 `<use href="#pin-open">` 引用它们——并且文档里必须有这些 symbol 定义。
- 分形噪点颗粒叠层用带 `feTurbulence` 的 data-URI SVG。有些浏览器（尤其较旧的 Safari 版本）可能不一致地渲染噪点，或在 PDF 导出时跳过它。
- Caveat 字体带着手写连字，操作系统之间渲染可能不一致。默认回退是 `cursive`，跨系统差异极大。
- `kraft`、`olive` 和 `orange` 颜色 token 已定义但在源里未启用。它们预留给未来扩展，目前没有角色。
- pill-yes 组件在圆角 pill 形状里用 Caveat 字形——这是刻意不寻常的，但对不熟悉系统的观者可能读成 UI bug。
- 纸颗粒叠层在标准页上用 `mix-blend-mode: multiply`，在 ink 页上用 `mix-blend-mode: screen`。混合模式翻转是必要的——在深 ink 页上用 multiply 会把页面弄脏。
- 柱状图和折线图组件用带手工定位点的 SVG。没有数据绑定层。
- 手绘别针 SVG 是固定路径插图。通过 `currentColor` 可以重上色，但别针比例不改 SVG 路径数据就调不了。
