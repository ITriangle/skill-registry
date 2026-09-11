---
version: alpha
name: Blue Professional
description: A restrained, consulting-grade presentation system on a warm cream canvas (#fdfae7) with a single saturated cobalt blue (#1e2bfa) as the only accent color. Display type runs Space Grotesk for headlines and numerical callouts; Inter handles body and chrome. Cards are soft-tinted cobalt at 4% opacity with 1.5px translucent borders and 10-14px rounded corners — quiet, never bordered in solid color. The aesthetic borrows from investment-research reports, McKinsey-grade quarterly briefings, and contemporary financial dashboards — measured, data-dense without feeling crowded, and unmistakably professional. The system is built for executive readability at distance, with strong typographic hierarchy and a single accent color carrying every emphasis moment.

colors:
  bg: "#fdfae7"
  primary: "#1e2bfa"
  text: "#111111"
  text-muted: "#6b6b6b"
  text-light: "#9a9a9a"
  accent-light: "rgba(30, 43, 250, 0.08)"
  accent-medium: "rgba(30, 43, 250, 0.15)"
  border: "rgba(30, 43, 250, 0.2)"
  card-bg: "rgba(30, 43, 250, 0.04)"
  positive: "#059669"
  negative: "#dc2626"

typography:
  h1:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 700
    fontSize: "clamp(44.8px, 5vw, 67.2px)"
    lineHeight: 1.1
    letterSpacing: -0.02em
  h2:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 600
    fontSize: "clamp(28.8px, 3vw, 41.6px)"
    lineHeight: 1.1
    letterSpacing: -0.02em
  h3:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 500
    fontSize: "clamp(17.6px, 1.8vw, 24px)"
    lineHeight: 1.3
    letterSpacing: -0.02em
  h4-eyebrow:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 600
    fontSize: "clamp(13.6px, 1.2vw, 16px)"
    lineHeight: 1.1
    letterSpacing: 0.08em
    textTransform: uppercase
    color: "{colors.primary}"
  body:
    fontFamily: "'Inter', sans-serif"
    fontWeight: 400
    fontSize: "clamp(13.6px, 1.1vw, 16.8px)"
    lineHeight: 1.6
    color: "{colors.text-muted}"
  metric-value:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 700
    fontSize: "clamp(35.2px, 3.4vw, 48px)"
    lineHeight: 1
    color: "{colors.primary}"
  metric-label:
    fontFamily: "'Inter', sans-serif"
    fontWeight: 600
    fontSize: "clamp(15.2px, 1.3vw, 17.6px)"
    lineHeight: 1.3
    color: "{colors.text}"
  metric-desc:
    fontFamily: "'Inter', sans-serif"
    fontWeight: 400
    fontSize: "clamp(12.5px, 0.95vw, 14.4px)"
    lineHeight: 1.5
    color: "{colors.text-muted}"
  metric-support:
    fontFamily: "'Inter', sans-serif"
    fontWeight: 400
    fontSize: "clamp(12px, 0.9vw, 13.6px)"
    lineHeight: 1.45
    color: "{colors.text-muted}"
  stat-num:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 700
    fontSize: "clamp(25.6px, 2.4vw, 33.6px)"
    lineHeight: 1
    color: "{colors.primary}"
  stat-name:
    fontFamily: "'Inter', sans-serif"
    fontWeight: 500
    fontSize: "clamp(13.6px, 1vw, 15.2px)"
    lineHeight: 1.35
    color: "{colors.text}"
  stat-context:
    fontFamily: "'Inter', sans-serif"
    fontWeight: 400
    fontSize: 12px
    lineHeight: 1.4
    color: "{colors.text-light}"
  agenda-num:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 700
    fontSize: 28.8px
    lineHeight: 1
    color: "{colors.primary}"
  insight-num:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 600
    fontSize: 12.5px
    lineHeight: 1.7
    letterSpacing: 0.05em
    color: "{colors.primary}"
  split-highlight:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 500
    fontSize: "clamp(18.4px, 1.55vw, 24px)"
    lineHeight: 1.4
    color: "{colors.text}"
  blockquote:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 500
    fontSize: "clamp(25.6px, 2.8vw, 38.4px)"
    lineHeight: 1.35
    color: "{colors.text}"
  quote-mark:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 700
    fontSize: "128px"
    lineHeight: 0.5
    color: "{colors.primary}"
    opacity: 0.15
  step-circle-text:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 700
    fontSize: 20.8px
    lineHeight: 1
  step-title:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 600
    fontSize: "clamp(15.2px, 1.4vw, 18.4px)"
    lineHeight: 1.2
  bar-label:
    fontFamily: "'Inter', sans-serif"
    fontWeight: 500
    fontSize: "clamp(12.8px, 1.1vw, 16px)"
    lineHeight: 1.3
    color: "{colors.text}"
  bar-pct:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 600
    fontSize: 15.2px
    color: "{colors.primary}"
  tag:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 500
    fontSize: 12px
    lineHeight: 1
    color: "{colors.primary}"
  counter:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 500
    fontSize: 12.8px
    lineHeight: 1
    letterSpacing: 0.05em
    color: "{colors.text-muted}"
  meta:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 400
    fontSize: 12.8px
    lineHeight: 1.4
    letterSpacing: 0.05em
    color: "{colors.text-light}"
  cite:
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 500
    fontSize: 12.5px
    lineHeight: 1.4
    letterSpacing: 0.04em
    textTransform: uppercase
    color: "{colors.text-muted}"

spacing:
  pad-slide-x: "4vw"
  pad-slide-y-top: "3.5vw"
  pad-slide-y-bottom: "8.5vh"
  pad-card-lg: "1.5rem 1.6rem"
  pad-card-md: "1.4rem 1.5rem"
  pad-card-sm: "1rem 1.2rem"
  pad-mini: "0.9rem 1rem"
  gap-grid-lg: "3.5rem"
  gap-grid-md: "2rem 3rem"
  gap-grid-sm: "1.5rem"
  gap-cards: "1.2rem"
  gap-mini: "1rem"
  header-margin: "2.5vh"
  accent-line-width: "60px"
  accent-line-height: "4px"

canvas:
  width: 100vw
  height: 100vh
  background: "{colors.bg}"

radii:
  pill: "100px"
  card-lg: "14px"
  card-md: "12px"
  card-sm: "10px"
  bar: "6px"
  circle: "50%"

components:
  card-tinted:
    background: "{colors.card-bg}"
    border: "1.5px solid {colors.border}"
    borderRadius: 14px
    padding: "1.5rem 1.6rem"
    description: "Primary content card. Cobalt tinted at 4% with a 20% cobalt 1.5px border. Soft 14px radius. Never solid-colored, never outlined in full primary."
  card-tinted-sm:
    background: "{colors.card-bg}"
    border: "1px solid {colors.border}"
    borderRadius: 12px
    padding: "1.4rem 1.5rem"
    description: "Compact tinted card with 1px border. Used for stat cells and small data blocks."
  card-tinted-xs:
    background: "{colors.card-bg}"
    border: "1px solid {colors.border}"
    borderRadius: 10px
    padding: "0.9rem 1rem"
    description: "Mini tinted card used for inline mini-stats."
  detail-block:
    background: "{colors.card-bg}"
    border: "1px solid {colors.border}"
    borderRadius: 10px
    padding: "1rem 1.2rem"
    description: "Detail block holding a small h3 + a bulleted ul. Used in detail-analysis grids."
  tag-pill:
    background: "{colors.accent-light}"
    color: "{colors.primary}"
    padding: "0.35rem 0.9rem"
    borderRadius: 100px
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 500
    fontSize: 12px
    description: "Pill-shaped tag sitting in the top-right of the slide-header. Fully rounded, soft cobalt tint background, cobalt text."
  cta-button:
    background: "{colors.primary}"
    color: "{colors.bg}"
    padding: "0.9rem 2.2rem"
    borderRadius: 100px
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 600
    fontSize: 15.2px
    description: "Primary CTA. Fully rounded solid cobalt pill with cream text. Hover lifts -2 with a soft cobalt drop shadow."
  nav-btn:
    width: 44px
    height: 44px
    borderRadius: 50%
    border: "1.5px solid {colors.border}"
    background: "{colors.bg}"
    color: "{colors.primary}"
    description: "Circular nav-arrow button. Hover inverts: cobalt fill, cream icon. Disabled state at 30% opacity."
  accent-line:
    width: 60px
    height: 4px
    background: "{colors.primary}"
    borderRadius: 2px
    description: "Short horizontal cobalt rule, 60×4px, slightly rounded. Used above cover titles and as eyebrow separators."
  accent-dot:
    width: 8px
    height: 8px
    background: "{colors.primary}"
    borderRadius: 50%
    description: "Small inline cobalt dot. Decorative inline marker."
  bar-track:
    height: 28px
    background: "{colors.accent-light}"
    borderRadius: 6px
    description: "Horizontal bar chart track. Soft cobalt tint with 6px rounded corners."
  bar-fill:
    height: "100%"
    background: "{colors.primary}"
    borderRadius: 6px
    description: "Solid cobalt fill inside bar-track. Width carries the data value. Animates from 0 to value on slide entry."
  step-circle:
    width: 56px
    height: 56px
    borderRadius: 50%
    background: "{colors.primary}"
    color: "{colors.bg}"
    description: "Circular numbered step marker in cobalt with cream numeral. Sequential steps reduce opacity (1.0 → 0.85 → 0.7 → 0.55) to suggest fade-into-future."
  metric-change-positive:
    color: "{colors.positive}"
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 600
    fontSize: 12.5px
    description: "Inline positive-change chip with up-arrow glyph and percentage. Green text inline; no border or fill."
  metric-change-negative:
    color: "{colors.negative}"
    fontFamily: "'Space Grotesk', sans-serif"
    fontWeight: 600
    fontSize: 12.5px
    description: "Inline negative-change chip with up/down-arrow glyph and percentage. Red text inline; no border or fill."
  insight-list-item:
    paddingLeft: "2.6rem"
    description: "Numbered insight list with a Space Grotesk 600 counter (decimal-leading-zero) at position absolute left. Numbers in cobalt, body in default text color."
  split-highlight-block:
    background: "{colors.accent-light}"
    borderLeft: "4px solid {colors.primary}"
    borderRadius: 12px
    padding: "1.3rem 1.5rem"
    description: "Highlighted callout block with cobalt left rule and tinted cobalt fill. Used for inline pull-quotes inside split-column layouts."
  progress-bar:
    position: "fixed bottom 0 left 0"
    height: 3px
    background: "{colors.primary}"
    description: "Thin cobalt progress bar at the bottom edge of the viewport, width grows linearly with slide index."
  cover-decoration:
    background: "{colors.accent-light}"
    clipPath: "polygon(30% 0, 100% 0, 100% 100%, 0% 100%)"
    description: "Diagonal accent panel filling the right ~35% of cover surfaces. Soft cobalt tint, clip-path angled cut on the left edge."
  cover-dots:
    layout: "3x3 grid of 6px cobalt dots at 12px gap, 25% opacity"
    description: "Small dotted decoration used on cover and other open-space surfaces."
  closing-circles:
    border: "1px solid {colors.border}"
    borderRadius: "50%"
    description: "Two concentric centered circles (500px outer, 360px inner) as atmospheric decoration on closing-class surfaces. Opacity 0.3-0.4."
---

## 概览

Blue Professional 是一套**咨询级演示系统**，为高管简报、研究交付物和季度复盘而设计。它的基础视觉前提是**克制，外加一项强硬承诺**：暖奶油画布（`{colors.bg}` — `#fdfae7`）和单一饱和钴蓝（`{colors.primary}` — `#1e2bfa`），承载每一种强调、每一个指标、每一个 CTA、每一条 eyebrow、每一根图表填充。没有第二品牌色，没有粉彩色板，没有暖冷配对——只有奶油、钴蓝，以及正文用的一阶收紧灰。

字体系统用两套开放 Google Fonts，角色定义得很紧。**Space Grotesk**（字重 300–700）是展示、标题、数字和 chrome 脸——用于 h1–h3 标题、所有指标/统计数字、eyebrow 标签（全大写加 0.08em 字距）、标签胶囊、CTA、幻灯片计数器、议程数字和步骤圆。略几何性格 + 柔和人文暖意，让它既现代（适合 AI/科技受众）又可信（适合金融受众）。**Inter**（字重 300–600）是正文字——用于段落文字、列表正文、指标说明和表格式内容。Space Grotesk / Inter 配对故意普通；让系统显得独特的是用法纪律，不是面孔的新奇。

色彩哲学是**一种强调，三阶文字灰**。钴蓝做全部强调工作：标题留在 `{colors.text}`（近黑 `#111111`），但每一个指标值、每一条 eyebrow、每一个 CTA、每一根图表柱、每一条呼出描边、每一个步骤圆、每一个进度指示都是钴蓝。正文用三阶灰阶梯——主正文用 `{colors.text}`，段落正文和指标说明用 `{colors.text-muted}`（`#6b6b6b`），第三级元数据用 `{colors.text-light}`（`#9a9a9a`）。只有两种非钴蓝强调色存在：`{colors.positive}`（压低的绿 `#059669`）和 `{colors.negative}`（压低的红 `#dc2626`），只用于方向变化指示（指标卡上的箭头和百分比）——而且这些是行内文字色，不是填充。

纵深是**柔软着色的**，从不偏移或投影。卡片是 4% 钴蓝着色（`{colors.card-bg}`），配 1.5px 半透明钴蓝描边（`{colors.border}` ——钴蓝 20% 不透明度）和 10–14px 圆角。除 CTA 悬停态上一条极淡的钴蓝着色阴影（`0 8px 24px rgba(30, 43, 250, 0.25)`）外没有投影。没有刺眼阴影，才给系统安静、高级的感觉——每一次抬升都由描边 + 着色暗示，不是由阴影。

**密度哲学：平衡，数据密但不挤。** 本系统为承载信息而建——六统计仪表盘、六细节块网格、七柱排名、带呼出和迷你统计的多列分割。填满实质性内容时系统读起来权威，稀疏时读起来怯。典型表面承载：一条 slide-header（h4 eyebrow + 标签胶囊）+ 一条章节 h2 标题 + 3–6 个信息单元格的网格或列表。卡片内部内边距适中（1.5rem），卡间距适中（1.2–1.5rem）——既不紧也不透气。系统既能支撑引文/封面级表面（空间里一句大胆陈述），也能支撑仪表盘级表面（六张密数据卡），而不感觉像两套系统。

**关键特征：**
- 每块表面都是暖奶油底（`{colors.bg}`）——从不纯白，从不灰。
- 单一饱和钴蓝（`{colors.primary}`）作为唯一强调——用于每一条 eyebrow、指标、CTA、图表填充和进度指示。
- Space Grotesk（展示 + chrome）+ Inter（正文）——绝不替换任何一套。
- 卡片是 4% 钴蓝着色，配 1.5px 钴蓝-20% 描边和 10–14px 圆角。
- 柔软胶囊形 chrome（`{components.tag-pill}`、`{components.cta-button}`），全 `100px` 圆角。
- 标题用 Space Grotesk 字重 600–700、-0.02em tracking，近黑文字色。
- 正文用 Inter 字重 400、13.6–16.8px、行高 1.6，压低灰。
- 每一页带着 slide-header（eyebrow + 标签胶囊）、单一 h2，以及灵活内容区——结构在整组幻灯片里有节奏。
- 持续 chrome：底边钴蓝进度条、左下幻灯片计数器、右下圆形导航箭头。
- 装饰大气元素（同心圆、点网格、对角强调面板）只出现在封面和收束级表面。

## 颜色

### 色板

- **Bg**（`{colors.bg}` — `#fdfae7`）：暖奶油画布。默认且通用的表面。略偏绿奶油的暖意，把系统与企业模板白区分开。每一页都落在这块底上。
- **Primary**（`{colors.primary}` — `#1e2bfa`）：签名钴蓝。高饱和电蓝，承载每一个强调瞬间。用于 h4 eyebrow、指标值、统计数字、图表柱填充、CTA 填充、步骤圆、进度条、强调线、议程数字，以及高亮块上的 cite 描边。不存在其他强调色。
- **Text**（`{colors.text}` — `#111111`）：主文字色。近黑，比 `#000000` 略暖。用于 h1–h3 标题、主内容文字、指标标签，以及任何应承载全重量的文字。
- **Text-muted**（`{colors.text-muted}` — `#6b6b6b`）：次级文字——正文段落、指标说明、图注。读起来比主文字舒适地更软，又不会消失。
- **Text-light**（`{colors.text-light}` — `#9a9a9a`）：第三级文字——幻灯片元信息、文字里的发丝分隔、统计语境行。最浅仍可读的灰；再往下，文字就变成环境噪声。
- **Accent-light**（`{colors.accent-light}` — `rgba(30, 43, 250, 0.08)`）：标签胶囊、柱轨道、高亮呼出和封面装饰面板的默认钴蓝着色。
- **Accent-medium**（`{colors.accent-medium}` — `rgba(30, 43, 250, 0.15)`）：略深一档的钴蓝着色，可用但很少用。
- **Border**（`{colors.border}` — `rgba(30, 43, 250, 0.2)`）：钴蓝 20% 不透明度。卡片、导航按钮、装饰圆和结构线的通用柔软描边色。
- **Card-bg**（`{colors.card-bg}` — `rgba(30, 43, 250, 0.04)`）：钴蓝 4% 不透明度。通用卡片填充——比 accent-light 更软，读起来是几乎不上色的表面，略微从奶油底抬起。
- **Positive**（`{colors.positive}` — `#059669`）：压低的绿。只作为正向变化指示的行内文字色（上箭头 + 百分比）。从不用作填充或描边。
- **Negative**（`{colors.negative}` — `#dc2626`）：压低的红。只作为负向变化指示的行内文字色。从不用作填充或描边。

### 默认

- **默认表面背景**：`{colors.bg}` ——每块表面从奶油开始。
- **默认标题色**：`{colors.text}`（`#111111`）——标题是近黑，从不是钴蓝。钴蓝留给强调瞬间（eyebrow、指标、CTA）。
- **默认正文字色**：`{colors.text-muted}`（`#6b6b6b`）——正文段落默认压低，不是全黑。
- **默认 eyebrow / h4 色**：`{colors.primary}` ——eyebrow 永远钴蓝，永远全大写，永远 0.08em 字距。
- **默认卡片填充**：`{colors.card-bg}`（钴蓝 4%）——通用柔软着色。
- **默认卡片描边**：`{colors.border}`（钴蓝 20%），1px 或 1.5px。从不用实心全钴蓝描边。
- **默认卡片圆角**：随卡片尺寸 10–14px（统计单元格用 `{radii.card-sm}`，统计卡和细节块用 `{radii.card-md}`，指标卡用 `{radii.card-lg}`）。
- **任何数值（指标、统计、议程数字、柱百分比）的默认强调**：`{colors.primary}`。
- **默认图表柱色**：`{colors.primary}` 实心填充，轨道用 `{colors.accent-light}`。
- **默认 CTA**：`{components.cta-button}` ——实心钴蓝胶囊，奶油字，100px 圆角。
- **默认标签胶囊**：`{components.tag-pill}` ——柔软钴蓝着色，钴蓝字，100px 圆角，与 slide-header 里的 h4 eyebrow 配对。

系统 **没有第二强调色**。不要伸手去拿橙、青绿或紫来区分类别——单一钴蓝纪律就是系统的身份。类别分化应通过位置、尺寸或标注完成，不是通过额外色相。

## 字体

### 字族
系统跑两套面孔，各司一职。

**Space Grotesk**（Google Fonts，字重 300–700）是展示 + 数字 + chrome 脸。用于每一个 h1、h2、h3、h4 标题；每一个数字呼出（指标值、统计数字、议程数字、柱百分比、步骤圆）；每一个 chrome 元素（标签胶囊、CTA、幻灯片计数器、提示文字）；以及每一条带 0.08em 字距的全大写 eyebrow。略几何性格 + 柔圆人文形态，读起来既当代又可信——适合 AI/科技和金融受众。

**Inter**（Google Fonts，字重 300–600）是正文字。用于段落文字、列表正文、指标说明、议程说明、细节块正文，以及任何更长内容。字重 400、行高 1.6、压低灰，Inter 读起来舒适、慷慨、编辑。

面孔角色不重叠：Space Grotesk 处理每一个数字和每一个标题；Inter 处理每一段和每一份列表正文。不要越界——Inter h1 读成另一个品牌；Space Grotesk 正文读成科技创业落地页。

### 字号阶梯

| Token | 字号 (clamp / px) | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.h1}` | 44.8–67.2px clamp | Space Grotesk | 700 | 封面或收束标题 |
| `{typography.h2}` | 28.8–41.6px clamp | Space Grotesk | 600 | 每页主章节标题 |
| `{typography.h3}` | 17.6–24px clamp | Space Grotesk | 500 | 议程项 / 区域标题 |
| `{typography.h4-eyebrow}` | 13.6–16px clamp | Space Grotesk | 600 | slide-header 里的全大写 eyebrow（永远钴蓝） |
| `{typography.body}` | 13.6–16.8px clamp | Inter | 400 | 标准正文段落 |
| `{typography.metric-value}` | 35.2–48px clamp | Space Grotesk | 700 | 呼出卡里的大指标数字 |
| `{typography.metric-label}` | 15.2–17.6px clamp | Inter | 600 | 数字下的指标标签行 |
| `{typography.metric-desc}` | 12.5–14.4px clamp | Inter | 400 | 指标支撑说明段 |
| `{typography.metric-support}` | 12–13.6px clamp | Inter | 400 | 指标支撑项目列表 |
| `{typography.stat-num}` | 25.6–33.6px clamp | Space Grotesk | 700 | 统计单元格数字（比 metric-value 小） |
| `{typography.stat-name}` | 13.6–15.2px clamp | Inter | 500 | 统计单元格描述名行 |
| `{typography.stat-context}` | 12px | Inter | 400 | 发丝分隔下的统计单元格第三级语境行 |
| `{typography.agenda-num}` | 28.8px | Space Grotesk | 700 | 议程项数字 |
| `{typography.insight-num}` | 12.5px | Space Grotesk | 600 | 洞察列表项上的计数器式数字前缀 |
| `{typography.split-highlight}` | 18.4–24px clamp | Space Grotesk | 500 | 分割高亮块内的行内拉引文字 |
| `{typography.blockquote}` | 25.6–38.4px clamp | Space Grotesk | 500 | 引文级标题正文 |
| `{typography.quote-mark}` | 128px | Space Grotesk | 700 | blockquote 上方 15% 不透明度的装饰超大引号字形 |
| `{typography.step-circle-text}` | 20.8px | Space Grotesk | 700 | 圆形步骤标记内的数字 |
| `{typography.step-title}` | 15.2–18.4px clamp | Space Grotesk | 600 | 步骤圆下的步骤标题 |
| `{typography.bar-label}` | 12.8–16px clamp | Inter | 500 | 柱状图行标签 |
| `{typography.bar-pct}` | 15.2px | Space Grotesk | 600 | 柱状图行百分比值 |
| `{typography.tag}` | 12px | Space Grotesk | 500 | slide-header 里的标签胶囊文字 |
| `{typography.counter}` | 12.8px | Space Grotesk | 500 | 持续幻灯片计数器 |
| `{typography.meta}` | 12.8px | Space Grotesk | 400 | 封面元信息行（例如日期 / 机密标记） |
| `{typography.cite}` | 12.5px | Space Grotesk | 500 | 拉引下的引用/署名，全大写加 0.04em 字距 |

### 默认

- **封面标题的默认字号**：`{typography.h1}`（44.8–67.2px）。永远 Space Grotesk 字重 700、-0.02em tracking。
- **每页主章节标题的默认字号**：`{typography.h2}`（28.8–41.6px）。Space Grotesk 字重 600。「章节 h2」是系统的结构主力——每一页内容都有一条。
- **区域或议程项标题的默认字号**：`{typography.h3}`（17.6–24px）。
- **h2 上方 eyebrow 的默认字号**：`{typography.h4-eyebrow}`（13.6–16px），钴蓝，全大写，0.08em 字距。
- **段落正文的默认字号**：`{typography.body}`（13.6–16.8px clamp）。Inter 字重 400，行高 1.6。
- **大指标数字的默认字号**：`{typography.metric-value}`（35.2–48px）。仪表盘统计单元格降到 `{typography.stat-num}`（25.6–33.6px）。
- **引文正文的默认字号**：`{typography.blockquote}`（25.6–38.4px）。永远 Space Grotesk 字重 500。
- **Space Grotesk 标题的默认字重**：500（h3）→ 600（h2 和 eyebrow）→ 700（h1 和数字呼出）。不要伸手去拿字重 400 或 800；字重阶梯是固定的。
- **Inter 正文的默认字重**：400。Inter 正文 500–600 太强硬；300 太细。
- **h1–h3 标题的默认字距**：-0.02em。没有负 tracking，Space Grotesk 展示读起来像没处理过。
- **h4 eyebrow 的默认字距**：0.08em 全大写。没有宽字距 + 全大写组合，eyebrow 读不成 eyebrow。

拿不准该用哪个标题 token 时，幻灯片的主文字瞬间默认 `{typography.h2}`（28.8–41.6px）。`{typography.h3}` 用于区域或议程项标题；`{typography.h1}` 留给封面和收束。

### 招牌处理

这些处理在**使用对应元素类型时不可省略**：

- **每一条 h4 eyebrow 都是 Space Grotesk 字重 600、`{colors.primary}` 钴蓝、全大写、0.08em 字距。** 没有例外。没有全大写 + 字距 + 钴蓝的 eyebrow，就不是系统的 eyebrow——只是一条散落的无衬线。
- **每一个标题（h1、h2、h3）都用 -0.02em 负字距。** 默认 tracking 的 Space Grotesk 展示读起来像没处理过，会打断编辑纪律。
- **每一个标题都用 `{colors.text}`（`#111111`），不是钴蓝。** 禁止钴蓝标题——钴蓝留给强调瞬间（eyebrow、指标、CTA、图表柱）。反转这一点会塌掉视觉层级。
- **每一个数字呼出（指标值、统计数字、议程数字、柱百分比、步骤圆）都是 Space Grotesk 字重 600–700、`{colors.primary}` 钴蓝。** 数值是系统的主强调瞬间。
- **每一段正文都是 Inter 字重 400、`{colors.text-muted}`（`#6b6b6b`）、行高 1.6。** 纯黑正文太重；text-light 正文太淡。
- **每一个 CTA 都是 `{components.cta-button}` 模式：实心钴蓝胶囊、奶油字、100px 圆角、0.9rem × 2.2rem 内边距。** 任何其他形状或颜色的 CTA 都不存在。
- **每一个标签胶囊都是 `{components.tag-pill}` 模式：柔软钴蓝着色、钴蓝字、100px 圆角、0.35rem × 0.9rem 内边距。** 实心背景或描边的标签胶囊会打断系统。
- **每一个 slide-header 把 h4 eyebrow 放左边、标签胶囊放右边。** 这是每一页内容的结构节奏。

### 排版原则

声线对比是 **近黑展示标题 ↔ 钴蓝 eyebrow + 数字 ↔ 压低灰正文**。不用斜体和下划线。唯一的强调机制是：在 Space Grotesk 阶梯内切换字重，从 text-muted 切到 text 或钴蓝，以及标签上的全大写 + 字距。

数字内容 **永远是 Space Grotesk**，即使是小数字标签（柱百分比、幻灯片计数器、迷你统计值）。Space Grotesk 在数字尺寸上的准等宽性格模仿表列数字，而不需要真正的等宽脸。

## 版式

### 画布系统
系统以每页 `100vw × 100vh` 为目标。幻灯片绝对定位，通过不透明度 + translateX（40px → 0px）、500ms ease 动画进入。只有 `.active` 页是 `opacity: 1`；上一页拿到 `.prev` 类并向外平移 -40px。

默认幻灯片内边距不对称：左、上、右 `3.5vw`；底 `8.5vh`。额外底部空间预留给固定的幻灯片计数器（左）和导航控件（右），它们坐在 `bottom: 2.5vh`，叠在视口底边上。

### 内边距与间距阶梯

| Token | 值 | 用途 |
|---|---|---|
| `{spacing.pad-slide-x}` | 4vw | 幻灯片水平内边距 |
| `{spacing.pad-slide-y-top}` | 3.5vw | 幻灯片顶部内边距 |
| `{spacing.pad-slide-y-bottom}` | 8.5vh | 幻灯片底部内边距（额外以避开导航 chrome） |
| `{spacing.pad-card-lg}` | 1.5rem 1.6rem | 大卡内部内边距（指标卡） |
| `{spacing.pad-card-md}` | 1.4rem 1.5rem | 中卡内部内边距（统计单元格） |
| `{spacing.pad-card-sm}` | 1rem 1.2rem | 小卡内部内边距（细节块） |
| `{spacing.pad-mini}` | 0.9rem 1rem | 迷你卡内部内边距（迷你统计单元格） |
| `{spacing.gap-grid-lg}` | 3.5rem | 分割列之间的大间距 |
| `{spacing.gap-grid-md}` | 2rem 3rem | 两列网格中的中间距（行 × 列） |
| `{spacing.gap-grid-sm}` | 1.5rem | 三列指标网格中的标准间距 |
| `{spacing.gap-cards}` | 1.2rem | 仪表盘统计单元格之间的间距 |
| `{spacing.gap-mini}` | 1rem | 迷你统计之间的间距 |
| `{spacing.header-margin}` | 2.5vh | slide-header 下方的外边距 |

### 持续 Chrome
每一页出现三个元素：
- **幻灯片计数器** 在左下 —— Space Grotesk 12.8px 字重 500，text-muted 灰，固定在 `bottom: 2.5vh; left: 3vw`。
- **导航控件** 在右下 —— 两个圆形 44px 导航按钮，1.5px 钴蓝-20% 描边，固定在 `bottom: 2.5vh; right: 3vw`。禁用态 30% 不透明度（第一页 / 最后一页）。
- **进度条** 在底边 —— 3px solid 钴蓝条，宽度 = `(currentSlide + 1) / total * 100%`。换页时动画。

一条 **键盘提示**（"Use arrow keys to navigate"）出现在底中，text-light 灰。

### Slide-Header 结构
每一页内容顶部带着 `.slide-header` 带：左边 h4 eyebrow，右边标签胶囊。slide-header 下面是章节 h2，然后是内容区（网格、列表、图表或分割）。封面、引文和收束页跳过 slide-header，改用居中内容。

### 内容网格
系统用重复网格模式做内容布局：2×3 议程网格、三列指标行、三列统计网格（仪表盘上变成 2 行）、1.05fr/1fr 分割正文、4 步时间线行、两列细节网格。这些是内容密度容器；网格选择取决于内容量，不是固定布局词汇。

## 纵深与抬升

### 着色卡片（主纵深机制）
系统用 **柔软钴蓝着色背景 + 柔软钴蓝描边 + 圆角** 在不用阴影的情况下创造抬升印象。一张 `background: {colors.card-bg}`（钴蓝 4%）和 `border: 1.5px solid {colors.border}`（钴蓝 20%）的卡，在视觉上坐在奶油底之上，没有任何实际偏移。这种处理就是系统的纵深语言。

### 卡片上无投影
卡片、统计单元格、细节块或任何内容容器上都没有 `box-shadow` 声明。系统里唯一的阴影是 CTA 按钮上单一柔软钴蓝着色悬停态：`0 8px 24px rgba(30, 43, 250, 0.25)`，悬停出现 200ms，移出消失。这是系统里唯一的彩色、模糊阴影。

### 左边强调（高亮块）
`{components.split-highlight-block}` 用 4px solid 钴蓝左边框发出「这是引用呼出，有别于周围正文」的信号。这是系统的结构强调机制——它不是阴影，但携带同样的抬升线索（彩色线把块在视觉上往前拉）。

### 圆角当柔软
卡片上 10–14px 的 border-radius 是纵深语言的一部分。没有圆角，钴蓝着色卡会读成平板；柔软半径把它们柔成「掀起」的表面。

### 大气装饰
装饰元素（cover-decoration 对角面板、同心 closing-circles、cover-dots 网格、引文装饰圆）只出现在封面、引文和收束级表面。它们是大气的，不是结构的——用来柔化开放空间表面，而不用内容填满它们。

## 形状与处理

### 圆角
- **`{radii.pill}` = 100px** ——全圆。用于 `{components.tag-pill}`、`{components.cta-button}`，以及任何胶囊形 chrome。
- **`{radii.card-lg}` = 14px** ——用于大指标卡。
- **`{radii.card-md}` = 12px** ——用于标准统计单元格、分割高亮块。
- **`{radii.card-sm}` = 10px** ——用于细节块和迷你统计。
- **`{radii.bar}` = 6px** ——用于柱轨道和柱填充。
- **`{radii.circle}` = 50%** ——用于步骤圆、导航按钮圆、强调点、收束装饰圆、封面点、引文装饰圆。

半径阶梯是分级的：更小 chrome 上更紧的半径，更大卡上更大的半径，胶囊上全圆，chrome 上正圆。系统除进度条外 **任何地方都没有方（0px）角**。

### 描边粗细
- **1px solid `{colors.border}`** ——通用柔软描边。用于统计单元格、迷你统计、细节块、议程项（仅底边）、stat-context 分隔（仅顶边）。
- **1.5px solid `{colors.border}`** ——略重的柔软描边。用于指标卡、导航按钮。
- **2px solid `{colors.border}`** ——用于分割列分隔（分割布局右列的 border-left）。
- **4px solid `{colors.primary}`** ——只作为 `{components.split-highlight-block}` 上的左边线，发出引用呼出信号。

描边 **从不是不透明钴蓝** ——它们永远是 20% 不透明度（`{colors.border}`）。这才给系统安静、掀起的质感。

### 装饰元素类型

**着色卡片**（`{components.card-tinted}`）——钴蓝-4% 背景，1.5px 钴蓝-20% 描边，14px 半径。主内容卡。

**标签胶囊**（`{components.tag-pill}`）——全圆钴蓝-8% 胶囊，钴蓝字。坐在 slide-header 右上。

**Eyebrow**（`{typography.h4-eyebrow}`）——全大写钴蓝标签，0.08em 字距。坐在 slide-header 左上。

**CTA 按钮**（`{components.cta-button}`）——实心钴蓝胶囊，奶油字。系统唯一的实心色元素。每个收束表面用一次。

**强调线**（`{components.accent-line}`）——短 60×4 水平钴蓝线，2px 半径。用在封面标题上方，以及开放空间表面上的 eyebrow 分隔。

**步骤圆**（`{components.step-circle}`）——56×56 实心钴蓝圆，内含奶油 Space Grotesk 数字。顺序时间线步骤降低不透明度（1.0 → 0.85 → 0.7 → 0.55），暗示淡入未来。

**柱轨道 + 填充**（`{components.bar-track}` + `{components.bar-fill}`）——28px 高轨道，钴蓝-8%，实心钴蓝填充宽度承载数据。两者都是 6px 圆角。

**洞察列表项**（`{components.insight-list-item}`）——用 CSS counter() 渲染带前导零的十进制前缀（"01"、"02"）的计数编号列表，钴蓝 Space Grotesk 600 / 12.5px，绝对定位在左。

**分割高亮块**（`{components.split-highlight-block}`）——钴蓝-8% 着色块，4px 钴蓝左边线，下面一条 cite 行。用于分割列布局里的行内拉引。

**封面装饰**（`{components.cover-decoration}`）——裁切的对角钴蓝着色面板，填满封面表面右侧约 35%。读起来像印刷强调，而不围住布局。

**封面点**（`{components.cover-dots}`）——3×3 网格的 6px 钴蓝点，12px 间距，25% 不透明度。开放空间表面上的装饰气氛。

**收束圆**（`{components.closing-circles}`）——两个同心居中圆（外 500px，内 360px），1px 钴蓝-20% 描边，不透明度 0.3–0.4。收束级表面上的大气装饰。

**指标变化芯片**（`{components.metric-change-positive}` / `{components.metric-change-negative}`）——行内方向指示：小箭头字形 + `{colors.positive}` 或 `{colors.negative}` 的百分比值。无填充、无描边——纯行内文字色。

## 该做与不该做

### 该做

- 把 `{colors.bg}`（奶油）当作通用画布。每块表面从暖奶油开始，从不是纯白。
- 把 `{colors.primary}` 钴蓝当作整组幻灯片唯一强调色——用于 eyebrow、指标、CTA、图表填充、步骤圆和进度指示。
- 把标题（h1、h2、h3）设成 `{colors.text}`（`#111111`）近黑、-0.02em tracking。禁止钴蓝标题；钴蓝只用于强调瞬间。
- 把每一条 h4 eyebrow 设成钴蓝 Space Grotesk 字重 600、全大写 + 0.08em 字距。eyebrow 是通用章节开场。
- 把 `{components.card-tinted}`（钴蓝-4% 填充 + 钴蓝-20% 1.5px 描边 + 14px 半径）当作通用内容卡模式。
- 每一个 slide-header 左边配 h4 eyebrow，右边配 `{components.tag-pill}`。这个节奏就是系统的结构身份。
- 正文用 Inter 字重 400、13.6–16.8px、`{colors.text-muted}`（`#6b6b6b`）、行高 1.6。压低灰正文才让系统感觉高级。
- 每一个数字呼出（指标、统计、柱百分比、议程数字）都用 Space Grotesk 字重 600–700、钴蓝。钴蓝数字强调是系统的数据声线。
- 所有 chrome（标签胶囊、CTA、导航按钮）用全 100px 圆角。胶囊形状是系统的 chrome 签名。
- 用方向变化芯片（`{components.metric-change-positive}` / `{components.metric-change-negative}`）行内、无填充——正向绿、负向红，两者都压低。

### 不该做

- 不要引入第二强调色。钴蓝是唯一强调——橙、青绿、紫或任何额外品牌色都会打断单一强调纪律。
- 不要把标题设成钴蓝。标题是近黑；钴蓝留给 eyebrow、指标、CTA 和图表填充。
- 不要在卡片或内容上用投影。系统除单一柔软钴蓝 CTA 悬停外有零 box-shadow。
- 不要在任何地方用方角（0px 半径）。系统围绕柔软圆角而建——方角立刻读成另一种美学。
- 不要在卡片上用不透明钴蓝描边。描边永远是钴蓝-20%（`{colors.border}`）。全不透明度描边会打断安静、掀起的感觉。
- 不要替换字体。Space Grotesk + Inter 就是配对。换成 Arial、Helvetica、Roboto 或 Open Sans 会塌掉排印身份。
- 不要用带硬边框的元素把画布挤满。系统依赖柔软着色和轻描边；加上重轮廓会让它感觉像另一套系统。
- 不要在内容页上省略 slide-header（h4 eyebrow + 标签胶囊）。页头就是编辑节奏。
- 不要用全大写正文。全大写留给 h4 eyebrow 和高亮块下的 cite 行。
- 不要把方向芯片用于非方向强调。绿/红变化芯片留给真正的正/负比较（例如「较上季 +11 pts」）。它们不是通用强调色。

## 响应式行为

Blue Professional 设计成 **1920×1080 演示系统**（有效 100vw × 100vh）。尺寸对字体用 CSS `clamp()`，对间距用 `vw / vh / rem`。系统响应式行为极少——为横屏演示语境而建。

### 缩放行为
- h1 随视口宽度从 44.8px → 67.2px。
- h2 从 28.8px → 41.6px。
- 正文从 13.6px → 16.8px。
- 指标值从 35.2px → 48px。
- 卡片内边距（基于 rem）随用户字号设置缩放；默认卡片内部内边距大约 24–26px。
- 描边（1px、1.5px、2px）、圆角（10–14px）和胶囊半径（100px）固定，不缩放。

### 低视口高度下的组件调整
单一 `@media (max-height: 700px)` 块在密页上收紧间距：
- 幻灯片内边距从 3.5vw / 8.5vh 减到 2.5vh / 3vw。
- 议程网格间距减小。
- 指标和细节卡内边距减到 1rem。
- 柱项内边距减小。

这确保系统能装进更矮的笔记本屏幕，而不打断结构布局。

### 演示行为
- 用 `ArrowRight`、`Space` 或 `PageDown` 前进。
- 用 `ArrowLeft` 或 `PageUp` 后退。
- `Home` 跳到第一页，`End` 跳到最后一页。
- 水平触摸滑动，阈值 50px，前进/后退。
- 幻灯片过渡是 500ms ease，不透明度淡入 + 40px translateX 滑入/滑出。
- 导航按钮在第一/最后一页禁用（不透明度 0.3）。
- 底边进度条以 400ms ease 动画到当前页百分比。

### 打印行为
系统没有 `@media print` 规则。幻灯片过渡只用于屏幕；打印只产出活动页。静态导出时，逐页截图可保留全部大气元素（封面装饰、点、同心圆全是 CSS）。

### 交互状态
- 导航按钮悬停时反色（钴蓝填充，奶油图标）。
- 议程项悬停时得到微妙的 `{colors.card-bg}` 背景（200ms 过渡）。
- CTA 按钮悬停时掀起 -2px，带柔软钴蓝投影（系统里唯一的阴影）。
- 柱填充以 0.8s ease 过渡从 0 动画到数据值——在进入页时最明显。

## CJK 与国际内容

用本模板承载中文（或其他 CJK）内容时，把拉丁字体栈换成对等的中文搭配，并套用通用 CJK 调整。所有推荐中文字体经 CDN 加载——无需安装。

### 推荐中文搭配

| 角色 | 拉丁（默认） | 中文对应 |
|---|---|---|
| h1 / h2 / h3 / h4-eyebrow / 指标数字 / 图表百分比 | Space Grotesk 500–700（负 tracking，h4 全大写） | 思源黑体 Noto Sans SC 700（字距 0，无变换） |
| 正文 / 指标说明 / 列表正文 | Inter 400 | 思源宋体 Noto Serif SC 400 |
| 等宽 / 计数器 / 标签胶囊 / cite | Space Grotesk 500–600（常全大写） | 思源黑体 Noto Sans SC 500（无变换） |

### 混排策略

**策略 A** ——每个角色单一 CJK 字族，自带拉丁字形覆盖。Space Grotesk 的每一个角色（展示、eyebrow、数字、chrome）用思源黑体 Noto Sans SC，Inter 正文角色用思源宋体 Noto Serif SC。两套面孔都带能与汉字干净并排的拉丁字形。衬线正文配对强化本模板所建的咨询级编辑语域——投资者报告和麦肯锡式简报在中文里常常无衬线展示配衬线正文。

### 加载

加到模板的 `<head>`：

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;600;700&family=Noto+Serif+SC:wght@400;500;700&display=swap" rel="stylesheet">
```

### 通用 CJK 调整

- **行高**：相对拉丁规格增加约 15–25%。正文 1.75–1.85（从 1.6 上调），展示 1.2–1.3（从 1.1 上调）。CJK 字符视觉上更满，垂直上比拉丁更挤。
- **字距**：每一段 CJK 都设为 0。模板里 h1–h3 的 −0.02em 负 tracking 会重叠 CJK 笔画；h4 eyebrow 上 +0.08em 正字距在方形字形上读起来发空。
- **文本变换**：不要对中文应用 `uppercase`——CJK 没有大小写。拉丁原作里 h4-eyebrow 和 cite token 用 `text-transform: uppercase`；CJK 段要去掉。
- **标点**：用全角中文标点（，。：；！？「」（））。
- **展示标题不加句号**：中文排印惯例在展示级标题上省略末尾的 。
- **中西文之间的空格（盘古之白）**：每个汉字与相邻拉丁字符或数字之间插入 ASCII 空格。写 `2024 Q3 业绩复盘`，不要写 `2024Q3业绩复盘`。
- **一句一面孔**：思源黑体 / 思源宋体覆盖 CJK 和拉丁字形——让一张脸处理每一句。不要让浏览器在句中把 ASCII 字符回退到 Space Grotesk 或 Inter。

### 本系统的美学备注

系统身份建立在 **克制，外加一项强硬承诺** ——奶油底、钴蓝强调、柔软着色卡、无阴影。这些都不依赖拉丁排印；干净地转到中文。h4-eyebrow 在 CJK 里失去「全大写 + 0.08em tracking + 钴蓝」性格，因为全大写和宽字距都去掉了。补偿方式是 **永远把 eyebrow 与标题上方的钴蓝 accent-line 组件配对** ——60×4 钴蓝线做拉丁 tracking 全大写所做的 chrome 识别工作。保持 eyebrow 的钴蓝和相对压低灰正文的字重-600 对比。

钴蓝纪律（`#1e2bfa` 作为唯一强调，数字和 CTA 全不透明度，描边 20% 不透明度，卡片填充 4% 不透明度）才是系统真正的身份，完整转到 CJK 构建。按惯例，中文咨询幻灯片组里数字呼出仍用拉丁阿拉伯数字（业绩 $24.3M，同比 +18%），所以钴蓝 Space Grotesk → 思源黑体的替换主要影响标签和标题，而不是抓眼球的数字。数字渲染保持思源黑体字重 700。

### 已知 CJK 缺口

- **没有 CDN 中文面孔精确匹配 Space Grotesk 的「可信咨询」语域。** 思源黑体读起来更机构、比 Space Grotesk 略少当代。模板会比拉丁原作略更「官方报告」、略少「AI 创业」。这对中文高管简报语境通常是可取的。
- **h4-eyebrow 信号变弱。** 「全大写 Space Grotesk 600 钴蓝加 0.08em 字距」组合是系统最可识别的小 chrome，在 CJK 里同时失去全大写和字距信号。建议在 eyebrow 上或下加 `{components.accent-line}` 作补偿；没有它，eyebrow 可能并进正文字重对比。
- **思源宋体正文改变语域。** Inter 正文读起来中性现代；思源宋体读起来编辑严肃。系统的「高级咨询」感觉会略更「政策文件」——适合国企或政府受众，对创业路演受众略重。创业语境把正文换成思源黑体 Noto Sans SC 400。

## 迭代指南

1. 任何新幻灯片从 `{colors.bg}` 奶油底开始。不要按页切换背景；恒定底就是系统的身份。
2. 任何新内容页顶部带着 slide-header：左边 h4 eyebrow（钴蓝、全大写、0.08em）+ 右边 tag-pill。
3. 任何新标题用 Space Grotesk 字重 600–700、`{colors.text}` 近黑、-0.02em tracking。主瞬间用 h2（28.8–41.6px）。
4. 任何新卡用着色模式：`{colors.card-bg}`（钴蓝 4%）+ 1–1.5px `{colors.border}`（钴蓝 20%）+ 10–14px 半径。从不用实心色填充或不透明描边。
5. 任何新数字呼出（指标值、统计数字、议程数字、柱百分比、步骤圆）都是 Space Grotesk 字重 600–700、`{colors.primary}` 钴蓝。数字就是强调瞬间。
6. 任何新强调线、分隔或方向线用钴蓝——主线用实心，描边用柔软钴蓝（20% 不透明度）。
7. 任何新 CTA 用 `{components.cta-button}` 模式：实心钴蓝胶囊、奶油字、100px 半径，不存在其他 CTA 形状。
8. 任何新图表柱用 `{components.bar-fill}`（实心钴蓝）坐在 `{components.bar-track}`（钴蓝 8%）上，6px 半径。
9. 任何新步骤或顺序指示用 `{components.step-circle}`，未来步骤递减不透明度（1.0 → 0.85 → 0.7 → 0.55）。
10. 如果表面太稀，加信息（更多统计、更多细节块）——不要加第二强调色或更重描边来填空间。系统填满实质时读起来优雅，不是噪声。

## 已知缺口

- **Space Grotesk 和 Inter 从 Google Fonts 加载**，经由 preconnect + `<link>`。除 `sans-serif` 外没有系统回退——Google Fonts 失败的环境里，系统塌成系统默认，失去性格。
- **方向变化色（`{colors.positive}` 和 `{colors.negative}`）只用于行内。** 除这两种行内文字色外，没有 token 级支持做状态填充、成功/错误徽章或告警。
- **单一强调纪律限制类别颜色编码。** 多系列图表必须通过位置或标注区分——没有「用不同颜色展示 4 个类别系列」的设计系统答案。这是有意的，但限制图表表现力。
- **议程项悬停态把背景改成 `{colors.card-bg}`** ——悬停时交互。在静态屏幕共享语境里可能不如预期工作。
- **柱填充进入时从 0 动画到值**，但只有活动页的柱可见。再次进入一页会重放动画；系统不保留动画状态。
- **进度条在第 1 页读起来像装饰**（10 页幻灯片组上大约 10%），直到组后段才很有信息量。与幻灯片计数器结合以给出明确位置线索。
- **幻灯片过渡用 translateX（40px 进/出）** 配不透明度淡入。在非常宽的显示器上 40px 位移几乎察觉不到；在小显示器上可能感觉突兀。
- **系统加载 Inter 字重 300–600**，但实践中只用字重 400。更轻或更重的 Inter 字重不是视觉词汇的一部分；加载它们技术上浪费。
- **指标变化指示器用 HTML 实体（`&uarr;`、`&darr;`）** 做箭头字形。多数浏览器渲染正确，但可能因系统字体而渲染成小/不一致的字形；换成 SVG 或 Unicode 字符会标准化渲染。
- **收束装饰同心圆绝对定位，固定 500px / 360px 尺寸。** 在非常小的视口上可能超出视口边界；在非常大的视口上可能显得偏小。
- **封面装饰使用 clip-path**，支持广泛但不普遍。没有 clip-path 支持的浏览器会把面板渲染成完整右列矩形。
