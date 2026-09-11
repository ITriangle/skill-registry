---
version: alpha
name: Sakura Chroma
description: "A cassette-package editorial system on warm cream paper with a six-color primary palette and warm-brown ink. Display type runs in Big Shoulders Display (condensed industrial display sans at weight 900); body in Albert Sans; tabular and tag content in JetBrains Mono; occasional Japanese accents in Noto Sans JP. The aesthetic borrows from 1970s consumer cassette packaging, Japanese print catalogues, and lo-fi product zines: petal-cluster blob clusters, diagonal multi-color ribbon bands, 12-point starburst seals, red rectangular stamps, and tracked uppercase micro-labels. The effect is hand-curated industrial editorial — warm but disciplined, playful but tightly typeset, with the cassette as its visual metaphor."

colors:
  paper: "#F1E6CB"
  paper-dk: "#E5D6B0"
  ink: "#3A2516"
  red: "#E5392A"
  pink: "#E54489"
  orange: "#F09131"
  green: "#3D9F47"
  blue: "#3F8BC4"
  yellow: "#F0BC2A"

color-aliases:
  line: ink

typography:
  disp-hero:
    fontFamily: "'Big Shoulders Display', sans-serif"
    fontSize: "clamp(120px, min(14vw, 22vh), 280px)"
    fontWeight: 900
    lineHeight: 0.84
    letterSpacing: -0.025em
  disp-statement:
    fontFamily: "'Big Shoulders Display', sans-serif"
    fontSize: "clamp(70px, min(8.4vw, 14vh), 168px)"
    fontWeight: 900
    lineHeight: 0.86
    letterSpacing: -0.022em
  disp-title:
    fontFamily: "'Big Shoulders Display', sans-serif"
    fontSize: "clamp(80px, min(9vw, 14vh), 180px)"
    fontWeight: 900
    lineHeight: 0.86
    letterSpacing: -0.022em
  disp-lockup:
    fontFamily: "'Big Shoulders Display', sans-serif"
    fontSize: "clamp(56px, min(7vw, 11vh), 130px)"
    fontWeight: 900
    lineHeight: 0.9
    letterSpacing: -0.015em
  disp-section:
    fontFamily: "'Big Shoulders Display', sans-serif"
    fontSize: "clamp(52px, min(5.6vw, 9vh), 100px)"
    fontWeight: 900
    lineHeight: 0.9
    letterSpacing: -0.018em
  disp-quote:
    fontFamily: "'Big Shoulders Display', sans-serif"
    fontSize: "clamp(48px, min(5.4vw, 9vh), 110px)"
    fontWeight: 900
    lineHeight: 0.92
    letterSpacing: -0.018em
  disp-quote-lg:
    fontFamily: "'Big Shoulders Display', sans-serif"
    fontSize: "clamp(56px, min(6.4vw, 10.5vh), 130px)"
    fontWeight: 900
    lineHeight: 0.9
    letterSpacing: -0.018em
  disp-brand:
    fontFamily: "'Big Shoulders Display', sans-serif"
    fontSize: "clamp(32px, min(3.4vw, 5.4vh), 56px)"
    fontWeight: 900
    lineHeight: 0.92
    letterSpacing: -0.02em
  disp-card-name:
    fontFamily: "'Big Shoulders Display', sans-serif"
    fontSize: "clamp(28px, min(2.6vw, 4.6vh), 48px)"
    fontWeight: 900
    lineHeight: 0.94
    letterSpacing: -0.012em
  num-hero:
    fontFamily: "'Big Shoulders Display', sans-serif"
    fontSize: "clamp(110px, min(11vw, 18vh), 240px)"
    fontWeight: 900
    lineHeight: 0.86
    letterSpacing: -0.025em
  num-md:
    fontFamily: "'Big Shoulders Display', sans-serif"
    fontSize: "clamp(70px, min(7vw, 11vh), 150px)"
    fontWeight: 900
    lineHeight: 0.86
    letterSpacing: -0.02em
  ttl-row:
    fontFamily: "'Big Shoulders Display', sans-serif"
    fontSize: "clamp(22px, 1.7vw, 30px)"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.005em
  body:
    fontFamily: "'Albert Sans', sans-serif"
    fontSize: "clamp(14px, 1vw, 17px)"
    fontWeight: 400
    lineHeight: 1.5
  body-md:
    fontFamily: "'Albert Sans', sans-serif"
    fontSize: "clamp(14px, 0.95vw, 15px)"
    fontWeight: 400
    lineHeight: 1.4
  body-emphasis:
    fontFamily: "'Albert Sans', sans-serif"
    fontSize: "clamp(15px, 1.1vw, 20px)"
    fontWeight: 600
    lineHeight: 1.4
  micro:
    fontFamily: "'Albert Sans', sans-serif"
    fontSize: "clamp(12px, 0.9vw, 14px)"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.16em
    textTransform: uppercase
  micro-lg:
    fontFamily: "'Albert Sans', sans-serif"
    fontSize: "clamp(12px, 0.9vw, 14px)"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.2em
    textTransform: uppercase
  micro-xl:
    fontFamily: "'Albert Sans', sans-serif"
    fontSize: "clamp(12px, 0.92vw, 14px)"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.32em
    textTransform: uppercase
  micro-spec:
    fontFamily: "'Albert Sans', sans-serif"
    fontSize: "clamp(14px, 1.1vw, 20px)"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.04em
  mono:
    fontFamily: "'JetBrains Mono', ui-monospace, monospace"
    fontSize: "clamp(11px, 0.78vw, 12px)"
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.02em
  mono-md:
    fontFamily: "'JetBrains Mono', ui-monospace, monospace"
    fontSize: "clamp(14px, 0.95vw, 16px)"
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.02em
  mono-tag:
    fontFamily: "'JetBrains Mono', ui-monospace, monospace"
    fontSize: "clamp(12px, 0.85vw, 14px)"
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.04em
  jp:
    fontFamily: "'Noto Sans JP', sans-serif"
    fontSize: "inherit"
    fontWeight: 500
    lineHeight: inherit
  stamp-text:
    fontFamily: "'Big Shoulders Display', sans-serif"
    fontSize: "clamp(20px, 1.6vw, 28px)"
    fontWeight: 900
    lineHeight: 1.0
    letterSpacing: 0.02em
  seal-text:
    fontFamily: "'Big Shoulders Display', sans-serif"
    fontSize: "clamp(22px, 2vw, 38px)"
    fontWeight: 900
    lineHeight: 0.9
    letterSpacing: -0.01em

spacing:
  frame-inset: "clamp(36px, 3.6vw, 72px)"
  frame-inset-bottom: "clamp(72px, 7vh, 110px)"
  topbar-gap: "clamp(12px, 1.4vh, 22px)"
  card-pad-x: "clamp(14px, 1.4vw, 20px)"
  card-pad-y: "clamp(16px, 1.7vw, 24px)"
  grid-gap: "clamp(16px, 1.6vw, 26px)"
  col-gap: "clamp(28px, 3vw, 56px)"
  pagenum-inset: "clamp(20px, 2.2vh, 36px) clamp(24px, 2.2vw, 44px)"

canvas:
  width: 100vw
  height: 100vh

components:
  paper-texture:
    backgroundImage: "radial-gradient(circle at 1px 1px, rgba(58,37,22,0.55) 1px, transparent 1.6px)"
    backgroundSize: "4px 4px"
    opacity: 0.16
    zIndex: 1
    description: "Subtle 4px-period halftone-dot paper texture sitting over every slide stage at 16% opacity. Drawn as a 1px-period radial-gradient. Required — it is the paper-grain that anchors every flat color block in the print register."
  petals-cluster:
    description: "A decorative cluster of 4–5 overlapping perfect circles (each `aspect-ratio: 1/1, border-radius: 50%`) in the primary palette colors. Circles overlap and tile within a bounded container. Used as a brand mark, decorative anchor in slide corners, or quote-page ornament."
  ribbon-band:
    height: "clamp(40px, 6vh, 96px)"
    width: "160% (oversize so rotation clears the frame)"
    transform: "rotate(-22deg) or rotate(22deg)"
    description: "A bundle of 5 stacked solid-color horizontal bars (pink, orange, yellow, green, blue) rotated -22° or +22° to sweep diagonally across a region. Echoes the cassette-label color-stripe motif. Anchored to one edge of the slide and bleeds off the opposite edge."
  ribbon-single:
    height: "16–18%"
    width: "160%"
    transform: "rotate(±22deg)"
    description: "A single solid-color ribbon in a multi-color stack; each ribbon is positioned with its own top/bottom percentage so the stack reads as parallel rays."
  rosette-seal:
    width: "clamp(60px, 6vw, 110px)"
    aspectRatio: "1 / 1"
    background: "{colors.ink}"
    color: "{colors.paper}"
    clipPath: "32-point starburst polygon"
    description: "12+ point starburst clip-path shape filled ink with cream text. Used as an authority seal or volume marker. Always carries a 1–4 character glyph (a number, two-letter abbreviation, or short word) in Big Shoulders 900."
  red-stamp:
    background: "{colors.red}"
    color: "{colors.paper}"
    padding: "clamp(8px, 1vh, 14px) clamp(12px, 1.4vw, 22px)"
    transform: "rotate(-3deg) or rotate(0)"
    fontFamily: "'Big Shoulders Display', sans-serif"
    fontWeight: 900
    description: "Red rectangular stamp with cream text, optionally rotated -3°. Used for status badges (COMPLETE, AS SEEN ON, LIMITED) and product callouts."
  card-product:
    border: "1.5px solid {colors.ink}"
    background: "{colors.paper}"
    overflow: hidden
    description: "Vertical product card with a 1.5px ink border, a colored topstrip header band, and a stacked body of name + description + extras + monospaced spec rows. The catalogue grid's primary unit."
  card-topstrip:
    height: "clamp(18px, 2vh, 32px)"
    description: "Colored horizontal band running the full width of a product card's top — fills in red, pink, orange, or blue depending on the card variant. Reads as a Pantone color tab."
  spec-checklist:
    description: "Vertical column of inline rows with a 14–20px square ink-bordered box (filled or empty) followed by a small caps label (COLOR, LO-FI, STEREO, LP). Echoes the cassette package's feature-spec checklist."
  bar-eq:
    bgUntint: "rgba(58, 37, 22, 0.10)"
    borderUntint: "rgba(58, 37, 22, 0.22)"
    description: "Equalizer-style bar chart. Each column is a stack of 6 equal-height tiles (segments). 'On' segments fill with one of the primary colors (red, pink, orange, yellow, green, blue) per column; 'off' segments fill with a translucent ink tint. column-reverse stacking means on-segments stack from the bottom up, like a VU meter."
  ledger-row:
    gridColumns: "96px 1.4fr 0.9fr 0.6fr 64px"
    paddingY: "clamp(10px, 1.2vh, 18px)"
    borderBottom: "1px solid rgba(58,37,22,0.22)"
    description: "5-column tabular row pattern: date | title | edition | chip | nr indicator. Header row uses a 1.5px ink border-bottom; body rows use 1px hairline ink-alpha dividers."
  chip:
    padding: "4px 10px"
    fontFamily: "'JetBrains Mono', ui-monospace, monospace"
    fontSize: "11–12px"
    color: "{colors.paper}"
    textTransform: uppercase
    letterSpacing: 0.06em
    description: "Mono-font color chip tagging a ledger row's category. Background pulls from red, pink, orange, blue, or green."
  topbar-rule:
    borderBottom: "1.5px solid {colors.ink}"
    paddingBottom: "clamp(12px, 1.4vh, 22px)"
    description: "Section header underline pattern. A title (Big Shoulders 900 with optional red em-emphasis) on the left aligned-end with a tracked-caps label on the right, separated from the body by a 1.5px ink rule."
  qbody-box:
    background: "{colors.paper}"
    border: "1.5px solid {colors.ink}"
    boxShadow: "8px 8px 0 {colors.ink}"
    padding: "clamp(20px, 2.4vh, 40px) clamp(28px, 2.6vw, 48px)"
    description: "Quote body container with a 1.5px ink border and a hard 8px ink offset shadow. Sits on top of diagonal ribbons as a paper-on-ribbons callout."
  petal:
    aspectRatio: "1 / 1"
    borderRadius: "50%"
    description: "A single perfect circle in one of the primary colors. The atomic unit of petal-clusters and scattered blobs. Always perfectly round — never an ellipse."
  pagenum:
    fontFamily: "'JetBrains Mono', ui-monospace, monospace"
    fontSize: "clamp(11px, 0.82vw, 13px)"
    color: "{colors.ink}"
    letterSpacing: 0.06em
    description: "Bottom-right page indicator — mono font, formatted NN / TT. Required on every content slide."
  nb-checkbox:
    width: "clamp(14px, 1.1vw, 20px)"
    aspectRatio: "1 / 1"
    border: "2px solid {colors.ink}"
    checkedFill: "{colors.ink}"
    checkedMarker: "× (cream-colored multiplication sign in Big Shoulders 900)"
    description: "Ink-bordered square checkbox used in spec-checklists and the cover footer. Checked state fills ink and centers a cream multiplication-sign glyph (not a checkmark)."
---

## Frontend Slides 固定舞台策略

当这套设计系统被 `frontend-slides` skill 使用时，把最终片子生成成**固定 1920×1080 舞台**，再均匀缩放到浏览器视口。片子应在每块屏幕上（包括手机）保住 16:9 幻灯片画布；可以信箱或柱箱，但不应为移动端回流幻灯片内容。

这条策略优先于本文件后文描述的任何源模板响应式行为。如果后文说原模板是视口流体，只把它当成源历史，而不是 `frontend-slides` 的目标生成模型。

即便源模板原本用视口流体 CSS 实现，例如 `100vw`、`100vh`、`vw`、`vh` 或 `clamp()`，这条策略仍然适用。把那些值当成设计比例，翻译进 1920×1080 舞台坐标，而不是生成片子里的现场响应式规则。

最终输出用 `deck-stage.js` 或等效的内联舞台缩放器：每页渲在 1920×1080，用一次 transform 缩放整座舞台，并核对渲染截图里的文字溢出和面板重叠。


## 概览

Sakura Chroma 是一套**卡带包装编辑系统**，把每一页当成小型日文音频产品目录里的印刷产品页。视觉隐喻是彻底的：花瓣簇 blob 记号、对角多色丝带条、12 尖星爆章、红矩形印章、等宽规格行、颜色编码芯片，以及均衡器风格柱图。一切都读成从 1970 年代消费音频手册封底跨页抽出来的——暖、手策、工业排过。

字体栈配对四张脸，功能角色分明。**Big Shoulders Display** 是展示声线——压缩工业无衬线，字重 900，紧负字距（-0.012em 到 -0.025em）。它扛每个展示瞬间：hero 数字、宣言、品牌 lockup、卡片名、区块标题。压缩竖直性和重字重给系统响、目录封面的声线。**Albert Sans** 是正文声线——干净现代人文无衬线，字重 400–700，跑正文段落、微标签和规格图注。**JetBrains Mono** 是表格声线——用于规格行、页码、日期、芯片、均衡器刻度，以及任何需要读成「数据」而不是「编辑」的瞬间。**Noto Sans JP** 是文化强调——偶尔用于日文字符（限定版 "limited edition"），标出松本工坊声线。四张脸一起组成「工业展示 + 干净正文 + 等宽数据 + 日文香料」。

色彩哲学是**暖奶油纸 + 墨棕结构 + 六色主强调集**。纸（`{colors.paper}` — #F1E6CB）是暖奶油，比典型骨白略深，带着更深色调兄弟（`{colors.paper-dk}` — #E5D6B0）给分层表面。墨（`{colors.ink}` — #3A2516）是深暖棕而不是纯黑，给每种字和描边印刷压纸的温度。六种主色（`red`、`pink`、`orange`、`yellow`、`green`、`blue`）出现在花瓣簇填色、丝带条、卡片顶条、均衡器柱填色、芯片背景和红矩形印章上。红和粉作为强调色占主导；橙 / 黄 / 绿 / 蓝阶梯充当分类强调集。

层次来自**硬偏移阴影**（8px 8px 0 ink）、**纸纹纹理**和**色块分层**——不是模糊投影。招牌处理：qbody-box（引文呼出）带着 8px 硬墨色阴影、零模糊；每一页都带着 4px 周期的半色调点纸纹，16% 不透明度，把每块色块锚定在印刷档；对角多色丝带条扫过内容背后，是系统最有辨识度的大气层。

**密度哲学：中高。** 目录档依赖视觉丰富——产品卡片网格，4 张叠放卡片各自装着名称 + 描述 + 规格行、7+ 行的账本表、hero 统计 + 均衡器图组合的仪表盘、封面跨页叠品牌 lockup + 花瓣 + 丝带 + hero 数字 + 规格清单 + 页脚。一页只有一个居中标题读成宣言瞬间（为冲击力刻意稀疏）；其他每一页都应感觉像装满的目录页。正确密度是「每个区域都在同时干活」——顶栏带着标题 + 元标签，主体带着主视觉 + 次级面板，常常还有芯片 / 印章 / 章当装饰标点。

**关键特征：**
- 暖奶油纸画布（`{colors.paper}`）配暖棕墨（`{colors.ink}`）当结构，外加六种主强调色。
- 4px 周期的半色调点纸纹（`{components.paper-texture}`）以 16% 不透明度坐在每一页上。必需。
- 每个展示瞬间用 Big Shoulders Display 字重 900 加负字距；正文用 Albert Sans；表格 / 数据用 JetBrains Mono；日文强调用 Noto Sans JP。
- 花瓣簇 blob 记号（4–5 个重叠正圆）当招牌装饰元素。
- 对角多色丝带条（5 条叠放色条，-22° 或 +22°）当大气分层。
- 32 尖星爆章（`{components.rosette-seal}`）和红矩形印章（`{components.red-stamp}`）当权威记号。
- 硬偏移阴影：引文呼出上 8px 8px 0 ink；任何地方都没有模糊、没有柔软投影。
- 目录产品卡片：彩色顶条 + 名称 + 描述 + 虚线规则 + 等宽规格行。
- 均衡器柱图：每列叠 6 块砖，「开」段从下往上叠，像 VU 表。
- 每个内容页右下用 JetBrains Mono 页码。

## 颜色

### 色板
- **Paper**（`{colors.paper}` — #F1E6CB）：暖奶油画布。每页的默认表面。比典型灰白略深、略暖，给片子印刷纸的温度。
- **Paper Dark**（`{colors.paper-dk}` — #E5D6B0）：画布略深的色调兄弟。用于分层表面、半区域背景，以及一块纸区域需要读成坐在另一块下面时。
- **Ink**（`{colors.ink}` — #3A2516）：深暖棕墨。结构色——全部正文、全部描边、全部分隔、全部硬偏移阴影色、全部章填色、全部顶栏规则。略冷的棕而不是纯黑，好当暖纸上的暖墨。
- **Red**（`{colors.red}` — #E5392A）：主强调色和印章色。用于 Big Shoulders 展示标题里的行内 `em` 强调、红矩形印章、第一张目录卡片顶条、数据页上的 hero 数字，以及第一条丝带条色。
- **Pink**（`{colors.pink}` — #E54489）：亮品红粉。用作封面 hero lockup 上的 lockup 条背景、丝带条色、第二变体的卡片顶条色，以及芯片背景。
- **Orange**（`{colors.orange}` — #F09131）：暖日落橙。用作花瓣色、丝带条色、第三变体的卡片顶条色，以及芯片背景。
- **Yellow**（`{colors.yellow}` — #F0BC2A）：芥末暖黄。用作花瓣色、丝带条色。留给分类强调。
- **Green**（`{colors.green}` — #3D9F47）：中等草绿。用作花瓣色、丝带条色、芯片背景和均衡器柱色。
- **Blue**（`{colors.blue}` — #3F8BC4）：暖中蓝。用作花瓣色、丝带条色、第四变体的卡片顶条色、芯片背景，以及主红统计需要配对对位时的第二 hero 统计色。

### 默认值
- **默认表面背景**：`{colors.paper}` ——每页都从暖奶油纸打开。
- **默认标题色**：`{colors.ink}` ——展示标题是暖棕墨，不是红或其他强调。红只作为墨标题里的行内 `em` 强调出现。
- **默认正文字色**：`{colors.ink}`。
- **默认描边色**：`{colors.ink}` ——每条结构描边都是暖棕墨，没有例外。
- **默认表格 / 等宽文字色**：`{colors.ink}`。等宽行偶尔在关键标签上用 `opacity: 0.7` 做视觉层级。
- **默认强调色（展示标题里的行内 `em`）**：正文和目录跨页用 `{colors.red}`；引文跨页在主体色故事已经含红时用 `{colors.blue}`。
- **默认 hero 数字色**：`{colors.red}` ——大数据页统计是红。两个统计一起出现时，配对 `{colors.blue}` 做第二统计。
- **默认印章色**：每个红矩形印章 `{colors.red}` 背景配 `{colors.paper}` 文字。
- **默认章色**：每个星爆章 `{colors.ink}` 背景配 `{colors.paper}` 文字。
- **`{colors.red}`、`{colors.pink}`、`{colors.orange}`、`{colors.green}`、`{colors.blue}` 表面上的默认文字色**：`{colors.paper}`（奶油）——系统里唯一的颜色反转。
- **`{colors.ink}` 表面上的默认文字色**：反转用 `{colors.paper}`（奶油）。
- **默认芯片色板顺序**（账本 / 表里的分类芯片）：红 → 粉 → 橙 → 蓝 → 绿。

六种主色**没有固定语义**（红不是「危险」，绿不是「成功」）。它们充当分类强调集——选哪种颜色适合构图。例外是强调用的 `{colors.red}`：它带着冷色没有的「注意力」档，所以留给行内 `em` 和最强调的 hero 数字。

## 字体

### 字族
系统有四款 Google Fonts，各自功能角色分明：

- **Big Shoulders Display**（展示）：压缩工业无衬线，字重 700 和 900。用于每个展示瞬间——标题、宣言、hero 数字、品牌 lockup、卡片名、章文字、印章文字、账本行标题。始终带负字距（-0.012em 到 -0.025em）。它又高又窄的压缩形态是整套系统的视觉身份。
- **Albert Sans**（正文）：干净现代人文无衬线，字重 400、500、600、700。用于正文段落（字重 400）、描述（字重 400）、加字距全大写微标签（字重 700），以及强调正文（字重 600–700）。给 Big Shoulders 的表现力提供中性对位。
- **JetBrains Mono**（数据）：等宽，字重 400、500。用于产品卡片里的规格行、账本里的日期标签、页码、均衡器刻度标签、芯片文字、导航提示、元标签。任何读成「数据」而不是「编辑」的瞬间。
- **Noto Sans JP**（文化强调）：日文无衬线，字重 500、700。省着用在封面页脚和品牌记号里嵌入的日文字符（限定版、漢字、平仮名）。提供松本工坊文化档。

不存在斜体。不存在下划线。强调靠行内 `<em>`（切到红或蓝，没有斜体样式）、靠字重（Albert Sans 400 → 700），或靠换脸（Albert Sans 正文 → Big Shoulders 展示）。

### 字号阶梯

| Token | 字号 (clamp) | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.disp-hero}` | 120–280px | Big Shoulders Display | 900 | 封面跨页上的 hero 数字 |
| `{typography.disp-title}` | 80–180px | Big Shoulders Display | 900 | 版权页 / 收束跨页上的超大标题 |
| `{typography.disp-statement}` | 70–168px | Big Shoulders Display | 900 | 宣言 / 单句跨页 |
| `{typography.disp-lockup}` | 56–130px | Big Shoulders Display | 900 | 封面上的品牌 lockup 条 |
| `{typography.disp-quote-lg}` | 56–130px | Big Shoulders Display | 900 | 大抽引 |
| `{typography.disp-section}` | 52–100px | Big Shoulders Display | 900 | 区块顶栏标题 |
| `{typography.disp-quote}` | 48–110px | Big Shoulders Display | 900 | 标准抽引 |
| `{typography.disp-brand}` | 32–56px | Big Shoulders Display | 900 | 品牌子记号或 wordmark |
| `{typography.disp-card-name}` | 28–48px | Big Shoulders Display | 900 | 产品卡片名 |
| `{typography.num-hero}` | 110–240px | Big Shoulders Display | 900 | 主 hero 统计 |
| `{typography.num-md}` | 70–150px | Big Shoulders Display | 900 | 次级统计 |
| `{typography.ttl-row}` | 22–30px | Big Shoulders Display | 700 | 账本行标题 |
| `{typography.body-emphasis}` | 15–20px | Albert Sans | 600 | 导语段落或强调正文 |
| `{typography.body}` | 14–17px | Albert Sans | 400 | 标准段落正文 |
| `{typography.body-md}` | 14–15px | Albert Sans | 400 | 卡片内紧凑正文 |
| `{typography.micro-spec}` | 14–20px | Albert Sans | 700 | 规格清单标签（轻字距） |
| `{typography.micro-xl}` | 12–14px | Albert Sans | 700 | 最松的加字距全大写微标签（0.32em） |
| `{typography.micro-lg}` | 12–14px | Albert Sans | 700 | 加字距全大写 eyebrow 标签（0.2em） |
| `{typography.micro}` | 12–14px | Albert Sans | 700 | 标准加字距全大写微标签（0.16em） |
| `{typography.mono-md}` | 14–16px | JetBrains Mono | 400 | 表格日期或值 |
| `{typography.mono}` | 11–12px | JetBrains Mono | 400 | 规格行、页码、均衡器刻度 |
| `{typography.mono-tag}` | 12–14px | JetBrains Mono | 400 | 芯片标签文字 |
| `{typography.stamp-text}` | 20–28px | Big Shoulders Display | 900 | 红矩形印章文字 |
| `{typography.seal-text}` | 22–38px | Big Shoulders Display | 900 | 星爆章文字 |
| `{typography.jp}` | inherit | Noto Sans JP | 500 | 日文字符强调 |

### 默认值
- **主区块标题（顶栏语境）的默认字号**：`{typography.disp-section}`（52–100px clamp），`{colors.ink}`。
- **宣言 / 居中陈述跨页的默认字号**：`{typography.disp-statement}`（70–168px clamp），`{colors.ink}`，可选 `<em>` 换色。
- **段落正文的默认字号**：`{typography.body}`（14–17px clamp）。
- **加字距全大写微标签或 eyebrow 的默认字号**：`{typography.micro}`（12–14px Albert Sans 字重 700，0.16em 字距，全大写），`{colors.ink}`。
- **Hero 统计的默认字号**：`{typography.num-hero}`（110–240px clamp），`{colors.red}`。
- **表格日期或等宽值的默认字号**：`{typography.mono-md}`（14–16px），`{colors.ink}`。
- **页码的默认字号**：`{typography.mono}`（11–12px），`{colors.ink}`。
- **任何 Big Shoulders Display 元素的默认字重**：900。（700 留给 `{typography.ttl-row}` ——账本行标题，系统里唯一的次展示瞬间。）
- **正文的默认字重**：400；微标签：700；强调正文：600–700。

主导文字瞬间在 `{typography.disp-section}` 和 `{typography.disp-statement}` 之间拿不准时：页带着顶栏/主体网格就选 `{typography.disp-section}`；页专给一句居中陈述就选 `{typography.disp-statement}`。

### 标志性处理
这些处理在**对应元素类型被使用时不可省略**：

- **每个 Big Shoulders Display 元素都带着负字距**（-0.012em 到 -0.025em）。默认字距的 Big Shoulders 读成没处理过；负字距才给展示字压缩、目录封面的密度。
- **每个微标签都是全大写加显著字距**（按语境 0.16em、0.18em、0.2em 或 0.32em）。没有全大写 + 字距的微标签读成正文碎片，不是标签。
- **每个页码都用 JetBrains Mono**，`NN / TT` 格式。页码在每个内容页上不可省略，住在右下。
- **Big Shoulders 展示标题里的每个行内 `<em>` 都换色**到 `{colors.red}`（默认）或 `{colors.blue}`（红过载的引文跨页）。从不用斜体样式；换色是全部强调装置。
- **每个规格行都用 JetBrains Mono。** Albert Sans 的规格行读成正文句子，不是目录数据。
- **每个星爆章都用 32 尖 clip-path 多边形**，`{colors.ink}` 填色配 `{colors.paper}` 文字。改尖数或简化（例如 8 尖爆、16 尖）会打断章识别信号。
- **每个红印章都用 `{colors.red}` 背景配 `{colors.paper}` 文字**和 Big Shoulders 900。印章文字始终全大写，始终正字距（0.02em）。

### 排印原则
系统的排印节奏来自**脸对脸对比**：Big Shoulders 展示（响、压缩、墨）→ Albert Sans 正文（静、中性、句首大写）→ JetBrains Mono 数据（机械、表格、定宽）→ Noto Sans JP（文化标点）。只用一张脸的页读成扁；Big Shoulders + Albert Sans + JetBrains Mono 一起用的页读成目录正确。

行高：展示紧（0.84–0.94），正文松（1.4–1.5），微标签和等宽紧（1.0–1.3）。倒置会打断节奏。

## 版式

### 画布系统
系统目标是 `100vw × 100vh`。片子包在 `.deck` 网格里，居中 `.stage` 填满视口。每个 `.slide` 绝对定位 inset 0，不透明度 0；只有 `.active` 页不透明度 1。过渡是 280ms ease 不透明度淡入淡出。导航由 JS 驱动：方向键、空格、PageUp/Down、Home/End、触控滑动。

### 画框内缩模式
多数内容页遵循画框内缩模式：`.frame` div 从幻灯片边缘内缩，上/左/右 `clamp(36px, 3.6vw, 72px)`，底 `clamp(72px, 7vh, 110px)`（清开页码）。画框内，顶栏模式（标题 + 元标签 + 1.5px 墨规则）坐在主体区域之上。

封面、宣言和引文跨页打破画框模式——它们把花瓣、丝带、hero 数字和 lockup 自由铺在画布上，没有顶栏/主体网格。

### 内边距阶梯
| Token | 值 | 用途 |
|---|---|---|
| `{spacing.frame-inset}` | 36–72px | 从幻灯片边缘的画框内缩 |
| `{spacing.frame-inset-bottom}` | 72–110px | 画框底内缩（清开页码） |
| `{spacing.topbar-gap}` | 12–22px | 顶栏底 padding 和区块间距 |
| `{spacing.grid-gap}` | 16–26px | 卡片网格格间间距 |
| `{spacing.col-gap}` | 28–56px | 双栏主体间距 |
| `{spacing.card-pad-x}` / `{spacing.card-pad-y}` | 14–20px / 16–24px | 产品卡片主体 padding |
| `{spacing.pagenum-inset}` | 20–36px / 24–44px | 页码从右下的内缩 |

### 持续页框
两个持续元素：
- **页码**在每个内容页右下——JetBrains Mono 11–13px `NN / TT` 格式。
- **导航提示**固定在左下——JetBrains Mono 10–12px 文字，读成 `← / → · space`，不透明度 0.36。

页码是每页构图的一部分（不是全局叠层）；导航提示是单个全局元素。

## 层次与抬升

### 硬偏移阴影（主手法）
系统用**墨色硬偏移阴影**，恰好一个值：`8px 8px 0 {colors.ink}`（零模糊，实心墨）。施加在 qbody-box（引文呼出）和其他需要从忙碌底层构图上抬起的抬升纸压丝带元素上。阴影很少见——多数卡片和面板只靠描边定义，8px 墨阴影留给配得上它的瞬间。

### 纸纹纹理（大气层）
`{components.paper-texture}` 半色调点图案以 16% 不透明度坐在每一页上。它不是严格意义上的层次，但提供根基纹理地面，让每块平色块读成纸上的墨。拿掉它立刻打断印刷档。每一页都必需。

### 色块分层
层次主要来自**分层彩色区域**：hero 数字后的丝带条；品牌 lockup 后的花瓣；纸卡片顶上的顶条色签；对角丝带上的红印章。高对比强调对着暖奶油背景向前凸，是系统的主层次语法。

### 描边定义
多数卡片和面板靠 1.5px 墨描边定义，不靠阴影。同一纸背景上纸卡片周围的 1.5px 墨描边，单靠边界就读成抬升。

### 没有柔软阴影
系统使用**没有模糊 `box-shadow`**（qbody-box 上那条 8px 硬偏移除外）、没有 `drop-shadow` 滤镜、没有 rgba 阴影着色。任何元素上的柔软现代阴影都会打断印刷目录审美。

## 形状与处理

### 圆角
| 值 | 用途 |
|---|---|
| 0px | 全部卡片、全部印章、全部顶栏、全部主体、全部芯片、全部账本行 |
| 50% | 花瓣（正圆）——仅用在花瓣簇和散落 blob 里 |
| 多边形 clip-path（32 尖星爆） | 玫瑰章——唯一复杂形状原语 |

系统**没有圆角半径**，除了正圆（花瓣）和多边形裁切的星爆（章）。其他每个形状都是严格矩形或正方形。

### 描边粗细
- **1.5px solid `{colors.ink}`** ——卡片、顶栏规则、账本表头规则、qbody-box、封面画框底规则、封面页脚顶规则上的标准描边粗细。
- **2px solid `{colors.ink}`** ——用在规格清单复选框描边上。
- **1px solid `{colors.ink}`** ——用在均衡器内刻度/标签分隔上。
- **1px solid rgba(58,37,22, 0.22)** ——用作发丝账本行正文分隔，以及均衡器段关状态描边。
- **1px dashed `{colors.ink}`** ——用作分隔产品卡片描述与等宽规格行的虚线规则。

描边始终是墨（暖棕）。这套系统里不存在彩色描边，除了芯片隐含的背景边。

### 装饰元素类型

**花瓣簇**（`{components.petals-cluster}`）— 有界容器，装着 4–5 个重叠的正圆彩色 blob。每个花瓣在容器内按百分比偏移绝对定位。颜色在主色板间轮换（红、粉、橙、黄、绿、蓝）——绝不要全是同一色。用作幻灯片角落的品牌记号锚，以及引文跨页上的装饰纹样。招牌装饰元素。

**丝带条**（`{components.ribbon-band}`）— 5 条实心彩色水平条叠成一束，旋转 -22° 或 +22°，对角扫过一个区域。条竖直叠放，每条丝带不同 `top` 百分比，做成平行射线效果。锚定在幻灯片一边，超大到从对边出血。系统的大气分层签名。

**玫瑰章**（`{components.rosette-seal}`）— 32 尖星爆 clip-path 形状，填 `{colors.ink}` 配奶油字。带着 1–4 字符字形：年份数字（"26"）、卷号（"VOL 26"），或 2-3 字母缩写。用作封面和收束版权页上的权威记号。

**红矩形印章**（`{components.red-stamp}`）— 红矩形配奶油字，可选 -3° 旋转。用于状态徽章（COMPLETE、AS SEEN ON）和产品呼出。始终 Big Shoulders 900 全大写。

**产品卡片**（`{components.card-product}`）— 竖直卡片，1.5px 墨描边、彩色顶条（红 / 粉 / 橙 / 蓝变体），以及叠放主体：Big Shoulders 900 卡片名 → Albert Sans 400 描述 → 虚线规则 → 等宽规格行。目录网格的主单元。

**卡片顶条**（`{components.card-topstrip}`）— 18–32px 高的实心色带，跑满产品卡片顶部宽度。读成 Pantone 色签；在网格内识别卡片变体。

**规格清单**（`{components.spec-checklist}`）— `nb-checkbox` + 加字距全大写标签行的竖列。每行有 14–20px 墨描边方框（实心或空，实心状态显示奶油 `×` 字形），后面跟上全大写加字距标签。

**账本行**（`{components.ledger-row}`）— 5 列表格行模式：日期（等宽）| 标题（Big Shoulders 700）| 版次（Albert Sans）| 芯片 | nr 指示器（方框）。表头行用 1.5px 墨 border-bottom；正文行用 1px 发丝墨 alpha 分隔。

**芯片**（`{components.chip}`）— 等宽字体色块，标记账本行类别。背景从主色板拉（红、粉、橙、蓝、绿）。始终奶油字。

**顶栏规则**（`{components.topbar-rule}`）— 区块页眉下划线模式：左标题（展示）与右加字距全大写元标签 aligned-end，用 1.5px 墨规则与主体分开。

**均衡器柱图**（`{components.bar-eq}`）— 8 列网格，每列叠 6 块等高砖（段）。`column-reverse` flex 方向意味着源顺序里第一段坐在底部；「开」段从下往上叠，像 VU 表。开段颜色按列设置（红、粉、橙、黄、绿或蓝）；关段是半透明墨着色。

**Qbody-box**（`{components.qbody-box}`）— 引文呼出容器，1.5px 墨描边加 8px 硬墨阴影。坐在对角丝带之上。

**品牌 lockup** — Big Shoulders 900 wordmark 压在 Albert Sans 600 子记号上，绝对定位在封面花瓣附近。

## 该做与不该做

### 该做
- 每一页都保留纸纹半色调点纹理（`{components.paper-texture}`），16% 不透明度。它是根基印刷档；拿掉它片子看起来像扁平网页模板。
- 每个展示瞬间用 Big Shoulders Display 字重 900 加负字距（-0.012em 到 -0.025em）。
- 每个微标签施加加字距全大写——标准 0.16em，eyebrow 0.2em，最松宣言 kicker 0.32em。默认字距读成正文句子。
- Hero 统计设成 `{colors.red}`，Big Shoulders 900。第二统计配对 `{colors.blue}`。
- 展示标题里用行内 `<em>` 换色（默认红，引文跨页蓝）。从不要斜体。
- 构图花瓣簇 blob 记号（4–5 个重叠正圆，主色）当幻灯片角落的装饰锚。
- 在封面和收束跨页上，对角多色丝带条（-22° 或 +22°）扫过 hero 内容背后当大气分层。
- 每个内容页右下放 JetBrains Mono 页码（`NN / TT` 格式）。
- 规格行、日期、芯片和任何表格数据用 JetBrains Mono——任何应读成「数据」而不是「编辑」的东西。
- 把 32 尖星爆章和红矩形印章留给权威瞬间（封面、版权页、产品呼出）。它们是招牌记号；滥用会降解它们。

### 不该做
- 不要圆任何角。卡片、印章、芯片、顶栏——全部严格矩形。花瓣（圆）和星爆章（多边形 clip-path）是仅有的非矩形形状。
- 不要用模糊 `box-shadow`。系统里唯一的阴影是引文呼出上的 8px 硬墨偏移。柔软现代阴影会打断印刷档。
- 不要用另一张展示脸替换 Big Shoulders Display。压缩工业 900 声线是整套系统身份。
- 不要用另一张等宽脸替换 JetBrains Mono。表格声线是目录伪装的一部分。
- 不要用 Big Shoulders Display 跑正文段落。小正文字号时读成用力过猛。
- 不要用 Albert Sans 做展示瞬间。Albert Sans 是中性正文字；展示瞬间需要 Big Shoulders。
- 不要用斜体做强调。用行内 `<em>` 加红或蓝色，或换字重（Albert 400 → 700）。
- 不要引入第七种主色。色板锁在红 / 粉 / 橙 / 黄 / 绿 / 蓝。加紫、青或其他色相会打断目录色故事。
- 不要用饱和强调色填卡片描边（红描边、蓝描边）。描边始终是墨。
- 不要在内容页上省略页码。它是不可省略的编辑信号。

## 响应式行为

系统目标是 `100vw × 100vh`，全程用 `clamp()`，带 `min(Xvw, Yvh)` 模式，把视口宽度和视口高度约束合在一起。这在桌面尺寸间产生流体缩放，无需响应式断点。没有定义移动断点——片子以演示为先。

### 缩放行为
- 展示标题通过 `min(Xvw, Yvh)` 缩放，所以视口变矮时也会缩小，不只是变窄时。
- 正文、等宽和微标签在 clamp 区间内按视口宽度缩放。
- 花瓣、丝带、章和印章用 `vw`/`vmin` 单位，所以它们与画布成比例缩放。
- 4px 纸纹周期不论视口都固定。

### 演示行为
- 前进：`ArrowRight`、`PageDown` 或 `Space`。
- 后退：`ArrowLeft` 或 `PageUp`。
- `Home` 跳到第一页，`End` 跳到最后一页。
- 水平触控滑动前进/后退。
- 活动页带着 `.active` 类；非活动页不透明度 0。

### 打印行为
没有定义 `@media print` 规则。

## 中日韩与国际内容

### 推荐中文搭配

| 角色 | 拉丁 | 中文 | 字重映射 |
|---|---|---|---|
| 展示 / 标题 / 宣言 / Hero 数字 / 卡片名 / 章 / 印章 / Lockup | Big Shoulders Display (900) | **站酷小薇体 ZCOOL XiaoWei** | regular（单字重） |
| 正文 / Body-md / Body-emphasis / 微标签 | Albert Sans (400 / 600 / 700) | **霞鹜文楷 LXGW WenKai** | regular |
| 表格 / 规格行 / 芯片 / 页码 / 等宽标签 | JetBrains Mono (400 / 500) | **霞鹜文楷 LXGW WenKai**（或规格行保持仅拉丁等宽） | regular |
| 日文强调 | Noto Sans JP | *（不变）* | 500 / 700 |

### 混排策略

**策略 A ——展示 CJK + 正文 CJK，各自带着自己的性格。** 卡带包装审美是女性花卉加工业纪律，中文搭配应两边都尊重。**ZCOOL XiaoWei（站酷小薇体）** 是优雅压缩展示脸，高对比笔画——它呼应 Big Shoulders Display 的压缩竖直性，同时带着更软、分明女性的声线，匹配花瓣簇装饰系统。**LXGW WenKai（霞鹜文楷）** 是温暖楷体风格正文字，基于 Fontworks Klee——它有友好的手策品质，匹配 Albert Sans 作为正文声线的角色，小字号压在暖奶油纸上读起来漂亮。两张 CJK 脸一起保住拉丁系统的「工业展示 + 温暖正文」节奏，同时把中文片子落到分明手策、略女性的档，契合 Sakura Chroma 的名字和花卉母题。

### 加载

两款字体都在 Google Fonts 上——用标准 Google Fonts URL 加载，跟模板已有的拉丁脸并列：

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=ZCOOL+XiaoWei&family=LXGW+WenKai+TC&display=swap" rel="stylesheet">
```

**不要通过 cn-fontsource、chinese-fonts-cdn 或其他 CDN 加载** ——那些包要么不存在（`cn-fontsource-zcool-xiaowei` 返回 404），要么在企业代理后不可靠。ZCOOL XiaoWei 和 LXGW WenKai 都由 Google 托管；那是它们唯一可靠的 CDN。

然后把 CJK 字族接到对应字体栈：
```css
/* Display roles */
font-family: 'Big Shoulders Display', 'ZCOOL XiaoWei', sans-serif;
/* Body / micro roles */
font-family: 'Albert Sans', 'LXGW WenKai', sans-serif;
/* Mono roles (if used for CJK content) */
font-family: 'JetBrains Mono', 'LXGW WenKai', ui-monospace, monospace;
```

### 通用中日韩调整

- 行高：正文 1.75–1.85，展示 1.15–1.25
- 字距：CJK 上为 0
- 文字变换：CJK 上不要全大写
- 全角标点
- 展示标题不加句号
- 盘古之白：`使用 Claude` 而不是 `使用Claude`
- 一句一字体

### 本系统的审美说明

- **Big Shoulders 展示上的负字距（-0.012em 到 -0.025em）在 CJK 上必须降到 0。** ZCOOL XiaoWei 已经是压缩脸；负字距会造成字形碰撞。
- **加字距全大写微标签（0.16em、0.2em、0.32em）没有 CJK 对等。** CJK 微标签把字距降到 0，让暖棕墨色 + 粗字重扛分类标签信号。「限定版 LIMITED EDITION」eyebrow 可以在同一标签里混 CJK + 拉丁——CJK 字符保持字距 0，拉丁保持 0.16em+。
- **行内 `<em>` 换色（到红或蓝）在 CJK 里同样成立** ——颜色强调与字形无关，落在 ZCOOL XiaoWei 展示标题上漂亮。
- **花瓣簇、丝带条、星爆章和红矩形印章都与字形无关** ——它们在中文内容背后同样扛着系统的工业目录声线。
- **带着 2–4 字符字形的 32 尖星爆章** 配单个汉字（限、新、季）用 ZCOOL XiaoWei、`{colors.paper}` 奶油，效果特别好。粗展示字重让中心字形读成制作者记号。
- **JetBrains Mono 规格行** 是最棘手的决定：纯拉丁规格行（`44.1 KHZ`、`LP / 33⅓`）保住目录伪装；LXGW WenKai 本地化规格行（`立体声`、`限定版`）读成中国市场目录，但丢掉技术规格声线。正确做法是**混语言规格行：拉丁值保持等宽，中文描述符行内切到 LXGW WenKai。**
- **Noto Sans JP 强调（限定版）保持不变** ——日文字符在许多情况下与简体中文共享字形，但 Noto Sans JP 渲染是故意的（日文版情调）。以中文为主的片子上，把这些字符换成 LXGW WenKai，让它们读成中文而不是日文借词。

### 已知中日韩缺口

ZCOOL XiaoWei 是单字重脸——没有 900 对等。定义拉丁展示声线的 Big Shoulders 900 字重响度无法精确匹配。补偿办法是把 CJK 展示留给柔软优雅受欢迎的瞬间（封面跨页、引文页），而不是需要纯粹野兽派字重的地方（hero 统计）。Hero 数字把数字保持在拉丁数字、Big Shoulders 900——中文数字（一二三四）反正扛不起目录封面的统计声线。

## 迭代指南

1. 每个新内容页都带着纸纹半色调点纹理、画框内缩区域（边缘 36–72px，底部 72–110px），以及右下页码。
2. 任何遵循画框模式的新内容页以顶栏打开：左 display-section 标题，右加字距全大写元标签，用 1.5px 墨规则与主体分开。
3. 任何新标题用 Big Shoulders Display 字重 900 加负字距。区块顶栏用 `{typography.disp-section}`；单句跨页用 `{typography.disp-statement}`；hero 数字用 `{typography.num-hero}` 红色。
4. 任何新正文用 Albert Sans 400；加字距全大写标签用 Albert Sans 700 全大写加 0.16–0.32em 字距；表格内容用 JetBrains Mono 400。
5. 任何新卡片用 1.5px 墨描边、可选彩色顶条（红 / 粉 / 橙 / 蓝），以及展示名 → Albert 正文 → 虚线规则 → 等宽规格行的主体模式。
6. 任何新账本 / 表格模式用 5 列 ledger-row 网格，表头下划线（1.5px 墨）和发丝正文分隔（1px 墨 alpha）。分类标签用主色板背景的等宽芯片。
7. 任何新装饰锚用花瓣簇（4–5 个重叠正圆花瓣，混主色）。避开椭圆——花瓣始终正圆。
8. 任何新权威记号用 32 尖星爆章（墨填、奶油字）或红矩形印章。章是正式的；印章是冲的。
9. 展示标题里的任何行内强调用 `<em>` 换色到 `{colors.red}`（默认）或 `{colors.blue}`（红过载时）。从不要斜体。
10. 大气分层——hero 内容后 -22° 或 +22° 的对角丝带条——出现在封面、收束和条纹跨页瞬间。它不是常规页元素；留给配得上大气野心的跨页。

## 已知缺口

- 系统加载四款 Google Fonts（Big Shoulders Display、Albert Sans、JetBrains Mono、Noto Sans JP）。Big Shoulders 是多字重（500、700、800、900）；系统用 700 和 900。生产环境建议自托管。
- 纸纹纹理是 CSS radial-gradient（不是 SVG 噪点滤镜），所以它在浏览器间确定性平铺且性能好。点周期（4px）固定，不随视口缩放。
- 32 尖星爆 clip-path 多边形是写死的；改章形状需要重写多边形点列表。系统只因为到处复用同一多边形才一致——换成不同星爆多边形会打断视觉内聚。
- 对角丝带条用 `transform: rotate(-22deg)` 和超大宽度（160%）从幻灯片边缘出血。很高视口上，丝带覆盖可能看起来比标准 16:9 视口更薄。
- 均衡器柱图用 `display: flex; flex-direction: column-reverse;` 从下往上叠开段。这是微妙的版式模式，在激进覆盖下可能脆弱——改 eq 段需要保住 column-reverse 行为。
- Hero 统计用行内 `<sub>` 和行内样式 `font-size` 覆盖做子单位（`26K`、`61%`），绕过了排印 token 系统。新统计应跟同一模式：超大数字 + 更小的行内单位，约数字字号的 ~34%，墨色。
- Noto Sans JP 已加载但只用一次（封面页脚里的限定版 "limited edition"）。如果片子没有日文内容，字体加载是未用重量；非日文片子考虑去掉导入。
- 左下导航提示不透明度很低（0.36），默认演示亮度下可能难看清。它意在当氛围 chrome，不是显著可供性。
