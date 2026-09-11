---
version: alpha
name: Biennale Yellow
description: "A literary-editorial presentation system in the visual register of an art biennale catalogue or quiet exhibition poster. The aesthetic is built on warm parchment grounds (`#E9E5DB`) flooded with soft solar yellow (`#F1EE2E`) radial blooms, set against a single deep indigo navy ink color. Display type is Instrument Serif — a contemporary high-contrast serif with tall ascenders and elegant italics — paired with Archivo for sans-serif chrome and JetBrains Mono for numerical and metadata callouts. No drop shadows, no rounded corners, no bordered cards: the only structural lines are hairline 1px rules in ink. The mood sits between a folded museum brochure, a slow-reading literary quarterly, and a Mediterranean exhibition poster — confident, atmospheric, and deeply restrained."

colors:
  paper: "#E9E5DB"
  paper-deep: "#DCD6C4"
  sun: "#F1EE2E"
  sun-soft: "#F8F39B"
  haze: "#F0DA7C"
  ink: "#1B2566"
  ember: "#E26B4A"

color-aliases:
  line: ink

typography:
  display:
    fontFamily: "'Instrument Serif', Georgia, serif"
    fontWeight: 400
    fontSize: "clamp(120px, min(14.6vw, 22vh), 240px)"
    lineHeight: 0.86
    letterSpacing: -0.018em
  display-md:
    fontFamily: "'Instrument Serif', Georgia, serif"
    fontWeight: 400
    fontSize: "clamp(80px, min(10vw, 16vh), 200px)"
    lineHeight: 0.86
    letterSpacing: -0.018em
  display-sm:
    fontFamily: "'Instrument Serif', Georgia, serif"
    fontWeight: 400
    fontSize: "clamp(110px, min(11vw, 18vh), 200px)"
    lineHeight: 0.86
    letterSpacing: -0.018em
  display-it:
    fontFamily: "'Instrument Serif', Georgia, serif"
    fontWeight: 400
    fontStyle: italic
    fontSize: "clamp(56px, min(7vw, 11vh), 120px)"
    lineHeight: 1.04
    letterSpacing: -0.005em
  numeral-jumbo:
    fontFamily: "'Instrument Serif', Georgia, serif"
    fontWeight: 400
    fontSize: "clamp(220px, min(28vw, 64vh), 720px)"
    lineHeight: 0.84
    letterSpacing: -0.04em
  numeral-lg:
    fontFamily: "'Instrument Serif', Georgia, serif"
    fontWeight: 400
    fontSize: "clamp(120px, min(15vw, 22vh), 280px)"
    lineHeight: 0.9
    letterSpacing: -0.04em
  numeral-md:
    fontFamily: "'Instrument Serif', Georgia, serif"
    fontWeight: 400
    fontSize: "clamp(72px, min(7vw, 12vh), 144px)"
    lineHeight: 0.92
    letterSpacing: -0.01em
  headline:
    fontFamily: "'Instrument Serif', Georgia, serif"
    fontWeight: 400
    fontSize: "clamp(40px, min(4.6vw, 7vh), 88px)"
    lineHeight: 1.06
    letterSpacing: -0.005em
  headline-sm:
    fontFamily: "'Instrument Serif', Georgia, serif"
    fontWeight: 400
    fontSize: "clamp(32px, min(3.6vw, 6vh), 56px)"
    lineHeight: 1
  date-rail:
    fontFamily: "'Instrument Serif', Georgia, serif"
    fontWeight: 400
    fontSize: "clamp(48px, min(5.2vw, 9vh), 96px)"
    lineHeight: 0.96
    letterSpacing: -0.005em
  ledger-title:
    fontFamily: "'Instrument Serif', Georgia, serif"
    fontWeight: 400
    fontSize: "clamp(20px, 1.6vw, 30px)"
    lineHeight: 1.15
  strand-title:
    fontFamily: "'Instrument Serif', Georgia, serif"
    fontWeight: 400
    fontSize: "clamp(22px, 1.7vw, 32px)"
    lineHeight: 1.1
  strand-num:
    fontFamily: "'Instrument Serif', Georgia, serif"
    fontWeight: 400
    fontSize: "clamp(28px, 2vw, 38px)"
    lineHeight: 1
  body-lede:
    fontFamily: "'Archivo', sans-serif"
    fontWeight: 400
    fontSize: "clamp(15px, 1.05vw, 18px)"
    lineHeight: 1.55
  body:
    fontFamily: "'Archivo', sans-serif"
    fontWeight: 400
    fontSize: "clamp(14px, 0.95vw, 16px)"
    lineHeight: 1.5
  body-sm:
    fontFamily: "'Archivo', sans-serif"
    fontWeight: 400
    fontSize: "clamp(11px, 0.78vw, 13px)"
    lineHeight: 1.5
  micro-label:
    fontFamily: "'Archivo', sans-serif"
    fontWeight: 600
    fontSize: "clamp(11px, 0.85vw, 14px)"
    lineHeight: 1.2
    letterSpacing: 0.18em
    textTransform: uppercase
  micro-label-tight:
    fontFamily: "'Archivo', sans-serif"
    fontWeight: 600
    fontSize: "clamp(10px, 0.72vw, 12px)"
    lineHeight: 1.2
    letterSpacing: 0.16em
    textTransform: uppercase
  rail-label:
    fontFamily: "'Archivo', sans-serif"
    fontWeight: 600
    fontSize: "clamp(11px, 0.85vw, 13px)"
    lineHeight: 1
    letterSpacing: 0.32em
    textTransform: uppercase
  mono-data:
    fontFamily: "'JetBrains Mono', ui-monospace, monospace"
    fontWeight: 400
    fontSize: "clamp(12px, 0.85vw, 14px)"
    lineHeight: 1.4
    letterSpacing: 0.04em
  mono-date:
    fontFamily: "'JetBrains Mono', ui-monospace, monospace"
    fontWeight: 400
    fontSize: "clamp(13px, 0.95vw, 16px)"
    lineHeight: 1.4
    letterSpacing: 0.02em
  pagenum:
    fontFamily: "'JetBrains Mono', ui-monospace, monospace"
    fontWeight: 400
    fontSize: "clamp(11px, 0.85vw, 13px)"
    lineHeight: 1
    letterSpacing: 0.08em

spacing:
  pad-edge: "clamp(40px, 4vw, 76px)"
  pad-region: "clamp(40px, 4.2vw, 80px)"
  pad-foot: "clamp(56px, 5vh, 88px)"
  pad-strand-y: "clamp(12px, 1.6vh, 22px)"
  gap-region: "clamp(20px, 2.5vw, 48px)"
  gap-strand: "clamp(14px, 1.8vh, 22px)"
  gap-footer-col: "clamp(20px, 2.4vw, 44px)"
  pagenum-bottom: "clamp(22px, 2.4vh, 42px)"
  pagenum-right: "clamp(24px, 2.4vw, 48px)"

canvas:
  width: 100vw
  height: 100vh
  background: "{colors.paper}"

components:
  pagenum:
    position: "absolute, right + bottom"
    color: "{colors.ink}"
    opacity: 0.75
    fontFamily: "'JetBrains Mono', ui-monospace, monospace"
    fontSize: "clamp(11px, 0.85vw, 13px)"
    letterSpacing: 0.08em
    description: "Single mono pagenum NN / NN pinned to bottom-right of every slide at 75% opacity. The only persistent chrome on every surface."
  hairline-rule:
    border: "1px solid {colors.ink}"
    description: "1px solid ink horizontal or vertical rule. The system's only border treatment — separates header bands from content, footer columns from each other, ledger rows from each other. No thicker rule exists."
  hairline-rule-soft:
    border: "1px solid rgba(27, 37, 102, 0.18-0.2)"
    description: "1px ink at 18-20% opacity. Used for between-row separators inside dense ledger or strand lists where a full-weight rule would feel oppressive."
  sun-bloom:
    background: "radial-gradient using {colors.sun} {colors.sun-soft} {colors.haze} blending to transparent on {colors.paper}"
    description: "Large soft radial bloom of solar yellow placed off-center or behind a focal element. The system's primary atmospheric layer. Sized 42-70% of viewport in the larger axis."
  ember-bloom:
    background: "radial-gradient using {colors.ember} at 15-22% opacity blending to transparent"
    description: "Small warm peach bloom used as a counter-temperature accent in a corner opposite the sun bloom. Always subordinate; never dominant."
  block-tile:
    background: "{colors.sun} at 40-70% opacity"
    description: "Geometric blocks of translucent solar yellow placed on an 8-row × 4-column grid behind cover or colophon surfaces. Suggests a layered poster underprint."
  yellow-panel:
    background: "{colors.sun}"
    color: "{colors.ink}"
    description: "Full-bleed yellow panel covering a column or third of the slide. The strongest possible color statement — used when a region needs to read as poster-fill, not paper."
  bar-ink:
    background: "{colors.ink}"
    height: "clamp(14px, 1.6vh, 22px)"
    description: "Solid ink horizontal bar for data charts. Width carries the data value."
  bar-lit:
    background: "{colors.sun}"
    border: "1px solid {colors.ink}"
    height: "clamp(14px, 1.6vh, 22px)"
    description: "Highlighted variant of bar-ink — yellow fill with 1px ink stroke. Used to mark the current or featured row in a series."
  strand-row:
    layout: "grid 56px 1fr, gap clamp(14px, 1.4vw, 24px), border-bottom hairline-soft, padding-bottom clamp(12px, 1.6vh, 22px)"
    description: "Numbered editorial list row — numeral cell + content cell separated by hairline-soft. Used for programmes, agendas, and curated lists."
  ledger-row:
    layout: "grid 92px 1.6fr 0.9fr 80px, gap clamp(14px, 1.4vw, 28px), border-bottom hairline-soft, padding clamp(10px, 1.3vh, 18px) 0"
    description: "Four-column tabular row for calendars and itineraries. Date column is mono, title is serif, venue is sans, duration is mono right-aligned."
  footer-band:
    layout: "grid 4-column with hairline-rule top border on each cell, gap clamp(20px, 2.4vw, 44px)"
    description: "Four-column metadata strip pinned to the bottom of cover and colophon surfaces. Each cell has a tiny uppercase tag + a brief plain-English statement."
  vertical-rail:
    transform: "rotate(-90deg) translateY(-50%) at left edge"
    fontFamily: "'Archivo', sans-serif"
    fontSize: "clamp(11px, 0.85vw, 13px)"
    letterSpacing: 0.32em
    textTransform: uppercase
    description: "Rotated vertical text label running up the left edge. Used on chapter/divider surfaces as a section marker."
  date-rail-stack:
    fontFamily: "'Instrument Serif', Georgia, serif"
    fontSize: "clamp(48px, min(5.2vw, 9vh), 96px)"
    lineHeight: 0.96
    textAlign: right
    description: "Large serif date or date-range stacked at top-right of cover surfaces. Uses an en-dash to indicate spans."
---

## 概览

Biennale Yellow 是一套**文学编辑风演示系统**，视觉语言取自欧洲艺术双年展图录、慢节奏展览海报，以及季刊文学出版物。没有卡片、没有按钮、没有阴影、没有圆角。结构词汇只有三样：纸、墨、黄。

字体系统以 **Instrument Serif** 为轴——当代高对比衬线，升部修长，斜体优雅，字脚略微外展。所有展示瞬间、所有数字、所有引文都由它承担，字号从 headline-small（40px）一直到超过 700px 的巨型数字。排得紧（行高 0.86，字距 −0.018em）时，读起来是自信的编辑展示；斜体排得稍松（行高 1.04，字距 −0.005em）时，就变成慢读引文脸。**Archivo** 是无衬线搭档——用于正文段落，以及小字号、宽字距的全大写标签（「micro-label」处理）。**JetBrains Mono** 负责所有数字与元数据呼出：日期、账本数字、页码。三字体系统刻板而克制；它们之间的对比就是全部排印故事。

色彩世界建在**暖羊皮纸**（`{colors.paper}` — `#E9E5DB`）上，作为通用底色，再以单一**墨色**（`{colors.ink}` — `#1B2566`，深靛蓝海军）画出每一行字、每一条线。系统的签名色是 **sun**（`{colors.sun}` — `#F1EE2E`），高饱和日黄，可作铺满面板、柔软绽放的径向渐变，或几何色块底印。**柔余烬桃**（`{colors.ember}` — `#E26B4A`）只作为从属的对温度点缀，永远以 15–22% 不透明度出现在角落径向晕里。不用反色处理；系统承诺暖底上的海军墨。

纵深是**大气的，不是结构的**。系统里没有任何投影。纵深来自叠层的黄色径向渐变（sun-bloom 与 ember-bloom 组件），以及封面级表面上可选的 block-tile 底印。卡片没有描边；区域只靠 1px 墨色发丝线分开。没有描边重量本身就是美学——设计读起来像印出来的，而不是工程出来的。

**密度哲学：编辑克制。** 稀疏时系统读起来优雅，挤满时就会坏掉。典型表面承载一个大型展示瞬间 + 少量支撑元素（一条 micro-label、一段正文、一份有序列表，或一朵径向晕）。用卡片、按钮、面板或叠组件把画布塞满，会把系统变成另一种美学。即使是密的表面（日历或节目单），密度也来自表格重复，而不是视觉丰富——许多安静的、发丝线隔开的元数据行，而不是许多带框单元格。慷慨的边缘内边距（40–76px）和宽页脚/页头带让画布呼吸。

**关键特征：**
- 每块表面都是暖羊皮纸底（`{colors.paper}`）；从不纯白，从不灰。
- 单一墨色（`{colors.ink}`）用于全部文字和全部线——没有第二套文字色。
- 日黄（`{colors.sun}`）有三种用法：铺满面板、柔软径向晕、半透明几何色块底印。
- Instrument Serif 承担每一个展示瞬间，字号从 40px 到 720px+。
- Archivo Bold 全大写 + 0.16–0.32em 字距是通用标签声线。
- JetBrains Mono 专用于日期、账本数字和页码。
- `{colors.ink}` 的 1px 发丝线是唯一描边处理——用于页头带、账本行、页脚列和 strand 分隔。
- 无投影、无圆角、无卡片轮廓、无按钮。装饰要么是大气的（径向晕），要么是几何的（半透明色块）。
- 每块表面右下角持续出现 `01 / NN` 的 JetBrains Mono 页码，75% 不透明度。
- 章节/分隔表面左缘可选旋转的 vertical rail-label。

## 颜色

### 色板

- **Paper**（`{colors.paper}` — `#E9E5DB`）：暖羊皮纸画布。默认且近乎通用的背景。读起来是带强暖意的柔化灰白——从不中性，从不冷。
- **Paper-deep**（`{colors.paper-deep}` — `#DCD6C4`）：略深一档的羊皮纸调，可用作次级表面，或在不用真实阴影的情况下暗示阴影带。留给需要表面分化、但仍待在暖纸家族里的瞬间。
- **Ink**（`{colors.ink}` — `#1B2566`）：整套系统唯一的文字与线条色。深靛蓝海军，读起来像带蓝偏的自信编辑黑。用于标题、正文、micro-label、等宽、发丝线，以及 ink-bar 填充。`--line` CSS 变量解析到同一颜色。
- **Sun**（`{colors.sun}` — `#F1EE2E`）：系统的签名日黄。高饱和，略偏绿。三种用法：铺满全出血或列出血面板、柔软径向晕的核心，以及 40–70% 不透明度的几何色块。
- **Sun-soft**（`{colors.sun-soft}` — `#F8F39B`）：更淡的奶油黄，用在 sun-bloom 渐变的中间色标，柔化从饱和日黄到纸的过渡。
- **Haze**（`{colors.haze}` — `#F0DA7C`）：更暖、偏芥末的黄，用在 sun-bloom 渐变最外圈色标，把晕延进纸里而不出现硬边。
- **Ember**（`{colors.ember}` — `#E26B4A`）：暖桃橙，只作为从属对温度点缀，出现在 15–22% 不透明度的径向晕里。从不用作填充色，从不用作文字色。它的工作是在画布对面平衡一朵 sun-bloom。

### 默认

- **默认表面背景**：`{colors.paper}`。每块表面从这里开始。
- **默认标题色**：`{colors.ink}`。永远如此。标题从不出现在黄、余烬或 paper-deep 上——只有墨。
- **默认正文字色**：`{colors.ink}`。正文与展示用同一色；对比靠字号和字重，不靠颜色。
- **默认线条色**：`{colors.ink}`（1px solid）用于主分隔；次级行分隔用 18–20% 不透明度的墨。
- **海报瞬间的默认强调表面**：`{colors.sun}`——铺满日黄的面板，上面是 `{colors.ink}` 文字。
- **默认大气层**：表面上偏心放置一朵 `{components.sun-bloom}`，对面角落可选 `{components.ember-bloom}`。
- **默认图表柱色**：`{colors.ink}`。当前/精选柱用 `{components.bar-lit}`（黄填充、墨描边）。
- **默认标签色**：文字用 `{colors.ink}`，无填充。标签靠字距 + 全大写 + 字重 600，不是填色胶囊。

系统从不反色：黄面板上的墨字是正确的（也是关键签名处理），但墨底上的黄字不存在。文字永远是墨；变化活在文字背后，而不是文字色本身。

## 字体

### 字族
系统跑三套面孔，每套角色定义得很紧。

**Instrument Serif**（Google Fonts，斜体 + 正体）是展示与编辑脸。高对比、修长升部、略微外展的字脚，给出当代文学语域——更接近杂志报头，而不是传统书籍衬线。正体用于标题、数字、账本标题和 date rail。斜体用于宣言引文和某些强调瞬间。排得紧（行高 ≤ 1.06，负字距 −0.005 到 −0.04em）。

**Archivo**（Google Fonts）是无衬线搭档。字重 400 用于正文段落（行高 1.5），字重 600 用于通用 micro-label 处理（全大写、0.16–0.32em 字距、10–14px）。从不用中间字重，从不用来做标题。

**JetBrains Mono**（Google Fonts）是数字/元数据脸。专用于账本日期、数据页的等宽数字呼出、页码和 nav-hint。它的 slab 气质给数字内容编辑重量，而不靠粗体造型。

### 字号阶梯

| Token | 字号 (clamp) | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.display}` | 120–240px | Instrument Serif | 400 | 封面级展示标题 |
| `{typography.display-sm}` | 110–200px | Instrument Serif | 400 | 面板语境中的编辑展示 |
| `{typography.display-md}` | 80–200px | Instrument Serif | 400 | 收束陈述的展示 |
| `{typography.display-it}` | 56–120px | Instrument Serif italic | 400 | 宣言级斜体引文正文 |
| `{typography.numeral-jumbo}` | 220–720px | Instrument Serif | 400 | 章节分隔的序数数字 |
| `{typography.numeral-lg}` | 120–280px | Instrument Serif | 400 | 装饰性引号、超大标点 |
| `{typography.numeral-md}` | 72–144px | Instrument Serif | 400 | Hero 统计数字 |
| `{typography.headline}` | 40–88px | Instrument Serif | 400 | 主章节标题、大引文正文 |
| `{typography.headline-sm}` | 32–56px | Instrument Serif | 400 | 区域标题、账本/日历顶栏 |
| `{typography.date-rail}` | 48–96px | Instrument Serif | 400 | 叠在表面顶部的日期或日期区间 |
| `{typography.ledger-title}` | 20–30px | Instrument Serif | 400 | 日历/账本行内的标题单元格 |
| `{typography.strand-title}` | 22–32px | Instrument Serif | 400 | 编号 strand/列表行内的标题 |
| `{typography.strand-num}` | 28–38px | Instrument Serif | 400 | strand 行内的数字单元格 |
| `{typography.body-lede}` | 15–18px | Archivo | 400 | 章节标题后的导语段 |
| `{typography.body}` | 14–16px | Archivo | 400 | 标准正文段落 |
| `{typography.body-sm}` | 11–13px | Archivo | 400 | 页脚带正文、密元数据 |
| `{typography.micro-label}` | 11–14px | Archivo | 600 | 通用全大写 eyebrow 标签 |
| `{typography.micro-label-tight}` | 10–12px | Archivo | 600 | 页脚单元格内更小的全大写标签 |
| `{typography.rail-label}` | 11–13px | Archivo | 600 | 垂直旋转的 rail 标签 |
| `{typography.mono-data}` | 12–14px | JetBrains Mono | 400 | 图表年/值标签、等宽行内数据 |
| `{typography.mono-date}` | 13–16px | JetBrains Mono | 400 | 日历账本中的日期列 |
| `{typography.pagenum}` | 11–13px | JetBrains Mono | 400 | 持续页码 |

### 默认

- **封面级展示标题的默认字号**：`{typography.display}`（120–240px clamp）。再小就读成章节级，不是封面级。
- **主章节标题的默认字号**：`{typography.headline}`（40–88px clamp）。
- **章节分隔数字的默认字号**：`{typography.numeral-jumbo}`（220–720px clamp）。不要缩小——巨型数字就是分隔表面的意义。
- **Hero 统计的默认字号**：`{typography.numeral-md}`（72–144px clamp）。统计数字与标题共用同一衬线——它们是展示瞬间，不是数据 chrome。
- **段落正文的默认字号**：`{typography.body}`（14–16px）。章节标题后的导语用 `{typography.body-lede}`（15–18px）。
- **任何 eyebrow 标签的默认字号**：`{typography.micro-label}`（11–14px），字重 600，全大写，0.18em 字距。
- **任何 Archivo 正文的默认字重**：400。Archivo 正文用任何其他字重都会打断节奏。
- **任何 micro-label 的默认字重**：600。标签用 400 或 700 会读成要么怯，要么过大。
- **任何全大写标签的默认字距**：最低 0.16em，最高 0.32em。没有宽字距的标签读起来像代码，不像编辑。

拿不准该用哪个展示 token 时，主瞬间默认 `{typography.headline}`（40–88px），单个 hero 统计默认 `{typography.numeral-md}`（72–144px）。display、display-sm 和 display-md token 留给封面/版权页/海报级瞬间。

### 招牌处理

这些处理在**使用对应元素类型时不可省略**：

- **每一个 display、numeral、headline 和 ledger-title 元素都是 Instrument Serif、字重 400。** 本系统不存在粗衬线展示——面孔的对比就是它的字重信号。把 Instrument Serif 设成字重 700，整套优雅会塌掉。
- **每一个 Instrument Serif 展示元素都用紧行高（0.84–1.06）。** 展示用宽松行高会毁掉编辑海报感——大衬线标题必须叠得紧，不能透气。
- **每一个 Instrument Serif 展示元素都用负字距。** display、headline、巨型数字用 −0.018 到 −0.04em；斜体展示用 −0.005em。没有负 tracking，宽体字形读起来像没处理过。
- **每一个 micro-label 都是全大写 Archivo、字重 600、字距 ≥ 0.16em。** 没有例外。没有全大写 + 字距的标签，在本系统里就不是标签；只是一条散落的无衬线。
- **每一个数字元数据元素（日期、页码、图表值、日历日期）都是 JetBrains Mono。** 衬线数字留给展示瞬间；等宽数字留给数据 chrome。不要越线。
- **每一条斜体宣言级引文都用 `{typography.display-it}`。** 把斜体引文设成 headline 级（40–88px）会读成更小的瞬间；斜体本意是主导。
- **每一段正文都是 Archivo 字重 400、行高 ≥ 1.45。** 不存在 Instrument Serif 正文——Instrument 只做展示。

### 排版原则

声线对比是 **慢而优雅的衬线 ↔ 宽字距全大写无衬线 ↔ 表格等宽**。斜体 Instrument 是系统的「感觉」声线（留给引文和宣言瞬间）；正体 Instrument 是「陈述」声线；Archivo 全大写宽字距是「标签」声线；等宽是「数据」声线。各司一职。

混用规则很紧：Instrument Serif 标题里的 `<em>` 仍是斜体 Instrument Serif（不换脸）。Archivo 正文里的 `<em>` 变成斜体 Archivo，不是衬线。不要在行内混脸。

颜色锁在每一个元素的墨上。本系统没有「强调色文字」处理——强调通过大气晕和面板填充送达，不是通过文字色。

## 版式

### 画布系统
系统以每页 `100vw × 100vh` 为目标。幻灯片绝对定位，通过不透明度过渡交叉淡入（280ms ease）。同一时间只有一页是 `.active`。所有度量都用带 vw 和 vh 项的 CSS `clamp()`——字体 clamp 包含 `min(...vw, ...vh)` 模式，让展示字按更短的视口轴缩放。

### 内边距与间距阶梯

| Token | 范围 | 用途 |
|---|---|---|
| `{spacing.pad-edge}` | 40–76px | 从任何幻灯片边缘到内容的标准边缘内边距 |
| `{spacing.pad-region}` | 40–80px | 铺满黄面板或主区域内的内部内边距 |
| `{spacing.pad-foot}` | 56–88px | 有页脚带时的底部内边距 |
| `{spacing.gap-region}` | 20–48px | 两个主内容列/区域之间的间距 |
| `{spacing.gap-strand}` | 14–22px | 编号列表中 strand 行之间的间距 |
| `{spacing.gap-footer-col}` | 20–44px | 页脚带元数据条各列之间的间距 |
| `{spacing.pagenum-bottom}` | 22–42px | 持续页码的底部内缩 |
| `{spacing.pagenum-right}` | 24–48px | 持续页码的右侧内缩 |

### 持续 Chrome
**pagenum** 是唯一持续的画布内元素。它出现在每一页的 `bottom-right`，JetBrains Mono 11–13px，墨色，不透明度 0.75。**nav-hint**（`← / → · space`）出现一次，固定在视口左下，JetBrains Mono 10–12px / 不透明度 0.4。nav-hint 不是幻灯片构图的一部分——它活在 `.stage` 外面。

### 边缘纪律
每一个有意义的元素都遵守最低 40px（移动端）到 76px（桌面）的边缘内缩。系统的优雅依赖边缘负空间——把内容推到出血（全出血面板、晕和色块除外）会打断图录感。

### 大气叠层
每一页都可以在内容后面带一层或两层大气：
- 一朵 **sun-bloom**（`{components.sun-bloom}`）——大而软的日黄径向渐变，尺寸为视口的 42–70%，偏心放置或放在焦点元素后面。
- 一朵 **ember-bloom**（`{components.ember-bloom}`）——小而暖的桃径向渐变，15–22% 不透明度，放在日晕对面的角落。

这些层不是可选装饰——它们是系统的主纵深机制。没有晕的表面读起来是平的羊皮纸。

## 纵深与抬升

### 无投影
系统有 **零投影**。没有 `box-shadow`，没有 `text-shadow`，没有 `filter: drop-shadow(...)`。纵深以大气方式送达。

### 大气纵深（日晕）
主纵深机制是 **sun-bloom**——从画布上某一点绽放的大而软的日黄径向渐变。晕的解剖是三到四个色标的叠层径向渐变：
- 0%：`{colors.sun}` 在 70–95% 不透明度（热核）
- ~30–40%：`{colors.sun}` 在 40–65% 不透明度（绽放）
- ~55–65%：`{colors.haze}` 在 18–22% 不透明度（柔软延伸）
- 80–90%：`{colors.paper}` 在 0%（平滑淡入底）

晕的尺寸和位置随表面需要变化：封面表面用居中或略偏心、视口 42% × 38% 的晕；章节表面用角落锚定、半径 720px 的晕；收束表面用底部锚定、55% × 50%、从下方升起的晕。

### 对温度点缀（余烬晕）
可选的 **ember-bloom** 放在日晕对面的角落，提供暖冷色张力，而不抬高画布饱和度。永远 15–22% 不透明度，永远比日晕小，永远从属。

### 几何底印（色块砖）
在封面和版权页表面上，内容后面可以再出现一层 **block-tile**——半透明日黄矩形，按 8 行 × 4 列网格系统放置，不透明度 40–70%。这一层暗示分层海报底印，而不承诺实心面板。色块是装饰几何，不是活动内容区域。

### 黄面板（结构色）
需要最强色彩陈述的表面，用 **yellow-panel** 铺满（`{components.yellow-panel}`），覆盖画布的一列、一半或三分之一，颜色是饱和的 `{colors.sun}`。这是系统里唯一的「硬」色彩处理——用面板时，墨字以全不透明度坐在上面。面板没有描边或阴影；它们直接碰到纸边或另一块面板边。

### 发丝线
内部结构纵深由 **1px solid 墨发丝线** 送达，分隔页头带与内容、账本行彼此、页脚列彼此。线从不粗过 1px。次级列表行之间（例如 strand 分隔），线降到 `rgba(27, 37, 102, 0.18-0.2)`——同一色，更低不透明度。

## 形状与处理

### 圆角
**一切都是零。** 每个形状都是严格矩形。径向晕在技术上是圆，但没有可见边缘——它们淡进纸里。

### 描边粗细
- **1px solid `{colors.ink}`** ——通用线。用于页头带下划线、账本行分隔、页脚列顶，以及点亮行上带描边的图表柱强调。
- **1px solid `rgba(27, 37, 102, 0.18-0.2)`** ——同一条线的柔软变体。用于密列表里的次级行分隔，全重量墨会显得沉。

系统 **没有更粗的描边**。任何地方都没有 2px、3px 或 4px 轮廓。视觉结构依赖发丝的轻。

### 装饰元素类型

**Sun-bloom** ——大而软的日黄径向渐变，偏心放置或放在焦点元素后面。系统的主纵深机制。每块表面永远一朵，有时配一朵对晕。

**Ember-bloom** ——小而暖的桃径向渐变，15–22% 不透明度，放在日晕对面的角落。从属的大气平衡。

**Block-tile 底印** ——半透明日黄矩形，放在 8×4 网格系统上。装饰几何，暗示分层海报，用在封面和版权页类表面。

**Yellow panel** ——画布的全出血列、一半或三分之一，用 `{colors.sun}` 铺满。系统最强的色彩陈述。上面承载墨字。

**Hairline rule** ——1px solid 墨。用于页头带下划线、账本分隔、页脚列顶。系统唯一的描边。

**Footer band** ——封面/版权页表面底部的四列元数据条。每个单元格有 `{components.hairline-rule}` 顶边、一条 Archivo micro-label，以及一句短正文陈述。

**Strand row** ——编号编辑列表行，衬线数字单元格 + 衬线标题 + 无衬线正文，与下一行用 hairline-soft 线分开。

**Ledger row** ——四列表格式日历/行程行：等宽日期 + 衬线标题 + 无衬线场地 + 等宽时长（右对齐），用 hairline-soft 线分开。

**Vertical rail label** ——旋转的 Archivo 全大写文字，沿章节分隔表面左缘向上跑，0.32em 字距。

**Date rail** ——大衬线日期或日期区间，叠在封面表面右上，常用 en-dash 表示跨年或跨月。

**Jumbo numeral** ——单个巨大的 Instrument Serif 数字（220–720px）主导分隔表面。永远衬线，永远字重 400，永远紧行高。

**Chart bar** ——实心墨矩形，宽度承载数据值。精选/当前柱换成黄填充加 1px 墨描边（`{components.bar-lit}`）。图表布局用网格行模式：等宽年标签 + 柱 + 等宽值，用间距分开。

## 该做与不该做

### 该做

- 把 `{colors.paper}` 当作通用背景。每块表面从羊皮纸开始。
- 每一行字都设成 `{colors.ink}`——展示、正文、micro-label、等宽，全部。单一文字色不可商量。
- 每一个展示瞬间都用 Instrument Serif、字重 400、紧行高（0.84–1.06）和负字距（-0.018 到 -0.04em）。衬线的优雅活在这个配置里。
- 每块表面至少加一朵 `{components.sun-bloom}`。大气纵深是系统的纵深机制；平的羊皮纸表面读起来是坏的。
- 想要暖冷张力又不抬整体饱和度时，在对面角落配一朵 `{components.ember-bloom}`。
- 每一个结构分隔都用 `{components.hairline-rule}`（1px solid 墨）：页头带下划线、账本行、页脚列、strand 分隔。
- 每一个全大写标签都设成 Archivo 字重 600、0.16–0.32em 字距。没有宽字距，标签读起来像代码，不像编辑。
- 表面需要最强色彩承诺时用 `{components.yellow-panel}`（全出血日黄列或面板）——墨字以全不透明度坐在上面。
- 把持续 `{components.pagenum}`（JetBrains Mono，75% 不透明度墨）放在每块表面右下。
- 把 JetBrains Mono 专留给数字与元数据呼出：日期、账本数字、图表值、页码、nav-hint。从不用等宽做展示或正文。

### 不该做

- 不要加投影。系统有零 box-shadow 和零 text-shadow。加上任何模糊或偏移阴影，印刷纸感立刻坏掉。
- 不要圆任何角。每个形状都是严格矩形。禁止 border-radius。
- 不要用粗过 1px 的描边。发丝线是唯一的描边词汇；不存在 2px、3px 或 4px 轮廓。
- 不要把 Instrument Serif 设成字重 700 或任何粗体。衬线的性格活在字重 400；粗衬线展示会压扁系统。
- 不要引入第二种文字色。纸上的黄字、任何地方的余烬字，或压低的墨色次级文字——都不存在。文字永远是全不透明度墨。
- 不要用卡片或面板把画布挤满。系统稀疏时读起来优雅。带框卡片、按钮堆或容器的多区域网格会打断编辑克制。
- 不要反色：带黄或纸色文字的墨面板不是系统的一部分。墨底只留给图表柱和小线条元素。
- 不要用 Inter、Helvetica 或 system-ui 替换 Archivo，也不要用 Times 替换 Instrument Serif。字体选择就是视觉身份；替换会塌掉美学。
- 不要用等宽做正文或标题。JetBrains Mono 专用于数字/元数据 chrome。
- 不要省略表面上的晕层。平的羊皮纸幻灯片读起来像 CMS 模板；晕才是发出「双年展」信号的气氛。

## 响应式行为

本系统建成 **视口流体的 100vw × 100vh 幻灯片组**，没有响应式断点。每个字号、内边距值和间距都用带 vw 和 vh 项的 CSS `clamp()`——`clamp(40px, min(4.4vw, 7vh), 88px)` 是典型模式。展示字按更短的视口轴缩放，所以竖屏方向不会把标题撑爆。

### 缩放行为
- 封面级展示从 120px → 240px。
- 章节分隔巨型数字从 220px → 720px。
- Headline 从 40px → 88px。
- 正文从 14px → 16px。
- 边缘内边距从 40px → 76px。
- 发丝线（1px）和页码尺寸（11–13px）基本固定。

### 演示行为
- 用 `ArrowRight`、`PageDown` 或 `Space` 前进。
- 用 `ArrowLeft` 或 `PageUp` 后退。
- `Home` 跳到第一页，`End` 跳到最后一页。
- 水平触摸滑动，阈值 40px，前进/后退。
- 幻灯片以 280ms ease 交叉淡入，通过 `.active` 类上的 `opacity` 切换。只有活动页是 `pointer-events: auto`。

### 打印行为
系统没有 `@media print` 规则。交叉淡入过渡只用于屏幕。静态导出时，逐页截图可保留全部大气层（径向晕是纯 CSS 渐变，不是资源）。

### 移动端行为
展示 clamp 里的 `min(vw, vh)` 模式意味着窄竖屏视口会自动缩小展示字以适配。strand 和账本行用固定 px 的第一列（56px、92px），在窄宽度上可能显得紧——系统设计给横屏演示语境，在低于 768px 的竖屏上能用，但没有优化。

## CJK 与国际内容

用本模板承载中文（或其他 CJK）内容时，把拉丁字体栈换成对等的中文搭配，并套用通用 CJK 调整。所有推荐中文字体经 CDN 加载——无需安装。

### 推荐中文搭配

| 角色 | 拉丁（默认） | 中文对应 |
|---|---|---|
| 展示 / 数字 / 标题 / date rail | Instrument Serif 400 | 得意黑 Smiley Sans（oblique）——展示瞬间；长篇衬线标题回退到 思源宋体 Noto Serif SC 400 |
| 正文 / 导语 / micro-label | Archivo 400–600 | 正文用 思源宋体 Noto Serif SC 400；micro-label 用 思源黑体 Noto Sans SC 600 |
| 等宽数据 / 日期 / 页码 | JetBrains Mono 400 | 思源黑体 Noto Sans SC 500，带表格感对齐——见下方已知 CJK 缺口 |

### 混排策略

**策略 A** ——每个角色单一 CJK 字族，拉丁字形由同一 CJK 字族处理。思源宋体和思源黑体都带能与汉字干净并排的拉丁字形，所以混排句子以一致面孔渲染。得意黑外科式使用——只用于最大展示瞬间，其轻微斜切匹配拉丁原作里 Instrument Serif 提供的意大利海报语域。其余一切（正文、micro-label、等宽）由 Noto Serif SC / Noto Sans SC 同时承载两种文字。

### 加载

加到模板的 `<head>`：

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;600;700&family=Noto+Serif+SC:wght@400;500;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/cn-fontsource-smiley-sans-oblique/font.min.css">
```

加载后，在应承载最强海报语域的展示 token 上，把得意黑引用为 `font-family: 'Smiley Sans Oblique', 'Noto Serif SC', serif`。

### 通用 CJK 调整

- **行高**：相对拉丁规格增加约 15–25%。正文 1.75–1.85（从 1.5–1.55 上调），展示 1.05–1.15（从 Instrument Serif 上非常紧的 0.84–0.96 上调）。这里的拉丁展示 token 行高低到 0.84——那种压缩下 CJK 字符会垂直碰撞。中文展示至少开到 1.0，多行标题用 1.15+。
- **字距**：每一段 CJK 都设为 0。拉丁展示 token 用 −0.005em 到 −0.04em 的负 tracking；在方形 CJK 字形上会重叠笔画，读起来是坏的。0.16–0.32em 宽字距的 micro-label 也降到 0。
- **文本变换**：不要对中文应用 `uppercase`——CJK 没有大小写。本系统每一个 micro-label 和 rail-label 都用 `text-transform: uppercase`；CJK 段要去掉。
- **标点**：用全角中文标点（，。：；！？「」（））。日期区间的 en-dash 分隔换成中文「至」或全角「—」连字符。
- **展示标题不加句号**：中文排印惯例在展示级标题上省略末尾的 。
- **中西文之间的空格（盘古之白）**：每个汉字与相邻拉丁字符或数字之间插入 ASCII 空格。写 `2024 春季双年展`，不要写 `2024春季双年展`。
- **一句一面孔**：思源宋体以统一衬线风格覆盖 CJK 和拉丁字形——让它处理混排编辑句。不要让浏览器在段中切到 Archivo。

### 本系统的美学备注

系统的编辑身份建立在 Instrument Serif 的高对比、修长升部性格上——这张脸发出「艺术双年展图录」和「慢文学季刊」的信号。语域上最接近的中文对等是正文与编辑展示用 **思源宋体 Noto Serif SC**，把 **得意黑 Smiley Sans Oblique** 留给海报级展示瞬间——拉丁原作里 Instrument Serif 在 120–240px 做最重的身份工作。得意黑轻微斜切和 slab 气质匹配意大利展览海报语域；巨型数字上纯用 Noto Serif SC 读起来是克制的学术中文，而不是双年展的响亮。

本系统「单一文字色、单一强调」的纪律干净地转到 CJK——纸上的墨、日晕气氛、发丝线、无阴影。micro-label 处理（Archivo 字重 600、全大写、0.16–0.32em 字距）是翻译时最脆弱的元素：CJK micro-label 同时失去全大写信号和宽字距。补偿方式：中文 micro-label 用思源黑体字重 600、字距 0，并靠 **略重的字重对比**（正文降到思源宋体字重 400，标签保持思源黑体 600），以及 **永远在标签下配一条 hairline-soft 线**——这条线做拉丁宽字距全大写所做的 chrome 识别工作。

### 已知 CJK 缺口

- **没有可 CDN 加载的中文等宽面孔来做表格数据。** JetBrains Mono 在这里的角色（日历账本日期、图表年/值标签、页码）依赖 CJK 不提供的等宽数字节奏。思源黑体字重 500 加 `font-feature-settings: "tnum"` 能给出表格拉丁数字，但汉字仍是比例宽。对齐具有结构性的账本行，把日期和值列留在拉丁数字（阿拉伯数字 + 拉丁日期缩写），标题/场地单元格才用思源黑体。
- **Instrument Serif 斜体没有直接的中文对应。** 斜体展示 token（宣言级引文正文）在 CJK 里会完全失去慢读性格。用思源宋体 400，配更松的行高（1.4）和略大的字号来补偿；考虑用「」引号框来发出「这是引文」的信号。
- **得意黑在受限网络上可能加载失败。** cn-fontsource CDN 在中国大陆可靠，国际场景验证较少。栈里永远包含 `'Noto Serif SC', serif` 作为回退，这样即使得意黑失败，展示标题仍保持编辑感。

## 迭代指南

1. 任何新表面从 `{colors.paper}` 开始，至少放一朵 `{components.sun-bloom}` 做气氛，并把持续 `{components.pagenum}` 钉在右下。
2. 任何新标题用 Instrument Serif 字重 400，紧行高和负 tracking。主瞬间用 `{typography.headline}`，只有封面级才用 `{typography.display}`。
3. 任何新正文段落用 Archivo 字重 400、行高 1.5。标题后的导语段用略大的 `{typography.body-lede}` 来透气。
4. 任何新 eyebrow 或章节标签用 micro-label 处理：Archivo 字重 600、全大写、0.16–0.32em 字距、墨色、无填充。不要换成胶囊或芯片。
5. 任何新结构分隔都是 1px `{components.hairline-rule}` 墨线，或次级列表行用其柔软变体。从不要更粗的描边。
6. 任何新数字或元数据内容（日期、页码、图表值、账本数字）用 JetBrains Mono。衬线数字只留给展示瞬间。
7. 任何新「海报级」色彩陈述用 `{components.yellow-panel}`——画布上一列或一份铺满的 `{colors.sun}`，上面是墨字。
8. 任何新的节目有序列表用 `{components.strand-row}` 模式：衬线数字单元格 + 衬线标题 + 无衬线正文，用 hairline-soft 线分开。
9. 任何新表格式行程用 `{components.ledger-row}` 模式：等宽日期 + 衬线标题 + 无衬线场地 + 等宽时长右对齐，用 hairline-soft 线分开。
10. 如果表面显得平，在日晕对面角落加一朵 `{components.ember-bloom}`——永远不要加卡片描边或阴影。

## 已知缺口

- **Instrument Serif、Archivo 和 JetBrains Mono 从 Google Fonts 加载**，经由 preconnect + `<link>`。回退（`Georgia`、`Helvetica Neue`、`ui-monospace`）已定义，但渲染差很多——Google Fonts 失败的环境里，系统塌成通用编辑默认，失去身份。
- **Instrument Serif 斜体轴已加载**，但只用于宣言级引文处理。其他斜体瞬间（例如正文段落里的 `<em>`）在风格上不会发出与专用斜体展示相同的信号。
- **系统没有图表引擎**——数据页用柱 div 上的行内 `style="width: XX%"`。做动态图表需要在 JS 里计算宽度，或在服务端模板化标记。
- **block-tile 底印使用硬编码网格位置**（每个色块 `grid-column: 1 / 3; grid-row: 6 / 9;`）。色块是装饰性的，放置按表面调过；没有参数化色块放置系统。
- **vertical rail-label 使用旋转变换**，在某些浏览器上可能产生细微的亚像素渲染伪影。标签是装饰性的；如果渲染看起来不对，可以安全去掉。
- **幻灯片导航除了页码没有其他指示器。** 没有点轨、没有进度条、没有缩略图栏。页码文字是唯一的位置线索。
- **交叉淡入过渡只用于屏幕**，不会退化成合理的打印/静态状态。为 PDF 导出捕获幻灯片需要逐表面手动截图。
- **封面和版权页页脚带列使用分数宽度**（`1.1fr 1fr 1.4fr 2fr` 和 `1.2fr 1.1fr 1fr 1.4fr`）。这些比例按演示内容调过，如果页脚单元格文字长度差很多，可能需要调整。
- **系统为 Instrument Serif 加载带 `ital` 轴的 Google Fonts**，但 Archivo 和 JetBrains Mono 只有 `wght` 轴。要加斜体正文或斜体等宽瞬间，需要更新字体加载请求。
