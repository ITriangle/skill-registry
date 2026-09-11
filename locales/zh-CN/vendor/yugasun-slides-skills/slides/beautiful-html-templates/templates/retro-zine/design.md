---
version: alpha
name: Retro Zine
description: "A risograph-zine editorial system on warm khaki paper with a deep forest-green accent and ink-black structure. Display type runs in Bebas Neue (condensed industrial sans, uppercase, generously tracked); body type runs in Space Grotesk at weight 300–500; handwritten emphasis runs in Caveat. A subtle SVG grain overlay sits over every slide, reinforcing the printed-paper feel. The aesthetic borrows from independent press, mid-century activist posters, and DIY zine culture: slightly rotated stamp marks, masking-tape pieces in collage layouts, drop caps, and offset paper-on-paper shadows. The effect is hand-printed editorial — warm but disciplined, confident but tactile."

colors:
  bg: "#C8B99A"
  bg-dark: "#B8A98A"
  green: "#008F4D"
  green-light: "#00A85D"
  black: "#1A1A1A"
  white: "#F4EFE6"

color-aliases:
  line: black

typography:
  display-hero:
    fontFamily: "'Bebas Neue', sans-serif"
    fontSize: "clamp(56px, 10vw, 160px)"
    fontWeight: 400
    lineHeight: 0.85
    letterSpacing: 0.04em
    textTransform: uppercase
  display-cover:
    fontFamily: "'Bebas Neue', sans-serif"
    fontSize: "clamp(48px, 10vw, 140px)"
    fontWeight: 400
    lineHeight: 0.88
    letterSpacing: 0.04em
    textTransform: uppercase
  display:
    fontFamily: "'Bebas Neue', sans-serif"
    fontSize: "clamp(48px, 8vw, 120px)"
    fontWeight: 400
    lineHeight: 0.9
    letterSpacing: 0.04em
    textTransform: uppercase
  headline:
    fontFamily: "'Bebas Neue', sans-serif"
    fontSize: "clamp(42px, 6vw, 90px)"
    fontWeight: 400
    lineHeight: 0.95
    letterSpacing: 0.03em
    textTransform: uppercase
  headline-md:
    fontFamily: "'Bebas Neue', sans-serif"
    fontSize: "clamp(36px, 5vw, 72px)"
    fontWeight: 400
    lineHeight: 0.95
    letterSpacing: 0.03em
    textTransform: uppercase
  statement:
    fontFamily: "'Bebas Neue', sans-serif"
    fontSize: "clamp(36px, 6vw, 90px)"
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 0.02em
    textTransform: uppercase
  title:
    fontFamily: "'Bebas Neue', sans-serif"
    fontSize: "clamp(24px, 3vw, 42px)"
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 0.04em
    textTransform: uppercase
  number-hero:
    fontFamily: "'Bebas Neue', sans-serif"
    fontSize: "clamp(80px, 12vw, 160px)"
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.02em
  number-md:
    fontFamily: "'Bebas Neue', sans-serif"
    fontSize: "clamp(44px, 6vw, 80px)"
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.02em
  drop-cap:
    fontFamily: "'Bebas Neue', sans-serif"
    fontSize: "clamp(48px, 6vw, 80px)"
    fontWeight: 400
    lineHeight: 0.8
    letterSpacing: 0.02em
  body:
    fontFamily: "'Space Grotesk', sans-serif"
    fontSize: "clamp(13px, 1.2vw, 16px)"
    fontWeight: 400
    lineHeight: 1.7
  body-md:
    fontFamily: "'Space Grotesk', sans-serif"
    fontSize: "clamp(14px, 1.3vw, 18px)"
    fontWeight: 400
    lineHeight: 1.6
  label-eyebrow:
    fontFamily: "'Bebas Neue', sans-serif"
    fontSize: "14–18px"
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.2em
    textTransform: uppercase
  label-spaced:
    fontFamily: "'Space Grotesk', sans-serif"
    fontSize: "12–14px"
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.25em
    textTransform: uppercase
  caption-feature:
    fontFamily: "'Bebas Neue', sans-serif"
    fontSize: "13–15px"
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.2em
    textTransform: uppercase
  hand-script:
    fontFamily: "'Caveat', cursive"
    fontSize: "clamp(22px, 3vw, 36px)"
    fontWeight: 600
    lineHeight: 1.3
  hand-script-sm:
    fontFamily: "'Caveat', cursive"
    fontSize: "clamp(16px, 2vw, 22px)"
    fontWeight: 400
    lineHeight: 1.3
  hand-script-lg:
    fontFamily: "'Caveat', cursive"
    fontSize: "clamp(24px, 3vw, 36px)"
    fontWeight: 600
    lineHeight: 1.3

spacing:
  slide-pad: 60px
  slide-pad-wide: "60px 80px"
  card-pad-lg: 48px
  card-pad-md: 32px
  card-pad-sm: 24px
  gap-lg: 60px
  gap-md: 40px
  gap-sm: 24px

canvas:
  width: 100vw
  height: 100vh

components:
  grain-overlay:
    backgroundImage: "SVG fractal-noise filter, base 200×200 tile"
    opacity: 0.07
    zIndex: 9999
    description: "Fixed, full-viewport SVG grain overlay sitting above all content. Imitates the print-grain texture of a risograph or letterpress page. Pointer-events disabled. Required on every slide."
  line-box:
    border: "3px solid {colors.black}"
    description: "Generic outlined card with 3px solid black border on khaki background. The system's default content container."
  line-divider:
    border: "3px solid {colors.black}"
    description: "Strict 3px black rule used as a region divider. May be top, bottom, left, or right of a region; meets adjacent borders without gap."
  line-thin:
    border: "2px solid {colors.black}"
    description: "2px black rule used inside a section for sub-region division (editorial column rule, ed-header bottom rule)."
  line-fine:
    border: "1.5px solid {colors.black}"
    description: "1.5px black rule used inside grid containers for cell separation (sub-cells inside a 3px-bordered grid)."
  stamp:
    transform: "rotate(-8deg) or rotate(6deg)"
    display: inline-block
    description: "Any element may be rotated -8deg (stamp) or 6deg (stamp-alt) to read as a hand-pressed ink stamp or applied label. Reserve for badges, callouts, and decorative overlays."
  stamp-mark:
    background: "{colors.black}"
    color: "{colors.green}"
    fontFamily: "'Bebas Neue', sans-serif"
    padding: "10px 24px"
    border: "2px solid {colors.green}"
    transform: "rotate(-8deg)"
    fontSize: 18px
    letterSpacing: 0.1em
    description: "Approval / status stamp — black background, green text, green 2px border, rotated -8deg. Used as a 'stamp of authenticity' callout."
  ribbon-bar:
    background: "{colors.green}"
    color: "{colors.white}"
    padding: "4–8px 12–20px"
    description: "Solid green color-block that contains light cream text — used as section labels, accent strips, and inline highlight bars."
  inline-highlight:
    background: "{colors.black}"
    color: "{colors.bg}"
    padding: "2px 8px"
    fontWeight: 600
    description: "Black-on-khaki marker highlight applied inline inside body paragraphs to lift a phrase. The print equivalent of a marker pen swipe."
  drop-cap:
    float: left
    fontSize: "clamp(48px, 6vw, 80px)"
    fontFamily: "'Bebas Neue', sans-serif"
    color: "{colors.green}"
    lineHeight: 0.8
    marginRight: 12px
    description: "Oversized green initial cap at the start of an editorial paragraph. Bebas Neue, line-height 0.8, floated left so body text wraps around."
  card-offset:
    background: "{colors.white}"
    border: "3px solid {colors.black}"
    positionBefore:
      offset: "12px down, 12px right"
      background: "{colors.green}"
      zIndex: -1
    description: "Card with a paper-on-paper offset effect — a solid green slab sits 12px behind the card, offset down-and-right. Reads as a colored shadow without using box-shadow."
  collage-piece:
    border: "3px solid {colors.black}"
    padding: 24px
    position: absolute
    transform: "rotate(-5deg to 5deg)"
    description: "Free-positioned collage panel with a 3px black border and small rotation. Backgrounds vary across pieces — white, khaki-dark, green, or black-with-inversion. Used in scatter-on-page compositions."
  tape:
    width: 80px
    height: 24px
    background: "rgba(255,255,255,0.4)"
    border: "1px solid rgba(0,0,0,0.1)"
    transform: "rotate(-40deg to 35deg)"
    description: "Translucent masking-tape rectangle layered at random angles over a collage to suggest physically taped-down pieces. Positioned absolutely; 1px hairline border. Always semi-transparent white."
  divider-stub:
    width: 60–80px
    height: 4px
    background: "{colors.white} or {colors.green}"
    description: "Short solid horizontal rule used as a centered visual breath above/below a statement or closing title. 4px tall."
  rsvp-field:
    borderBottom: "2px solid {colors.black}"
    paddingBottom: 8px
    description: "Form-field row pattern: small Bebas Neue green label, hand-script value drawn over a 2px black underline. Mimics a written form."
  ledger-row:
    borderBottom: "1.5px solid {colors.black} (header) or 1px solid rgba(black, 0.22) (body)"
    padding: "10–18px 0"
    description: "Horizontal data row pattern: date | title | edition | track | nr. Header row has stronger bottom border; body rows have hairline dividers."
  chip:
    padding: "4px 10px"
    fontFamily: "'JetBrains Mono', ui-monospace, monospace"
    fontSize: "11–12px"
    color: "{colors.white}"
    textTransform: uppercase
    letterSpacing: 0.06em
    description: "Mono-font color chip used inline in tabular ledger rows to tag a row's category. Fill pulls from green / red-stamp / orange / pink / blue as a categorical palette extension."
---

## 概览

Retro Zine 是一套**孔版印刷 zine 编辑系统**，落在温暖卡其纸上（`{colors.bg}` — #C8B99A），深绿森林色（`{colors.green}` — #008F4D）当有意义的强调，墨黑（`{colors.black}` — #1A1A1A）当结构色。审美借自立独立出版社文化、世纪中叶行动派海报和 DIY zine 版式：压缩工业展示字、手写强调、略旋转的印章、美纹纸胶带拼贴痕迹、首字下沉，以及把每块表面绑到印刷纸档的印纹颗粒叠层。

字体栈配对三张脸，情绪角色分明。**Bebas Neue** 是展示声线——压缩、全大写的工业无衬线，宽字距（0.02–0.04em），用于每个标题、宣言、统计、数字和标签。它的压缩竖直性是系统的视觉身份；换成任何其他展示无衬线都会丢掉 zine 声线。**Space Grotesk** 是正文声线——干净的人文几何无衬线，字重 300–500 跑段落，用小字号（13–18px）保住杂志栏文密度。**Caveat** 是手写声线——随意圆珠笔草书，用于作者署名、旁注、展示元素上的图注，以及 RSVP 式版式里表单栏的「书写」。三张脸一起读成「小出版社排过的编辑跨页」。

色彩哲学是**土地 + 森林**：温暖卡其纸画布、更深卡其色调兄弟给分层表面、深绿森林色给强调和强调表面、墨黑给结构和正文，以及灰白奶油（`{colors.white}` — #F4EFE6）给卡片和反转文字填色。白色故意不是纯白——是柔软奶油，坐成纸里的纸，而不是硬矩形。绿扛着系统的情绪声线：它激活区块、盖批准章、标记品牌。同一个 hex（#008F4D）出现在首字下沉、丝带条、行内标签、宣言背景和进度条上。

层次来自**纸压纸偏移色块**和**小旋转**，不是模糊阴影。招牌处理：`{components.card-offset}` 带着一块实心绿板，通过绝对定位的 `::before` 伪元素坐在后面偏右下 12px。视觉效果是分层纸或凸版垫印，而不是柔软投影。印章上的旋转（`-8deg` 或 `6deg`）和拼贴片上的旋转（`-5deg` 到 `5deg`）加上手摆上去的感觉。

**密度哲学：中高。** Zine 档依赖视觉丰富——拼贴构图、多栏编辑版式、正文里的首字下沉、带芯片分类的表格账本、斜角盖上的丝带条页眉。一页只撑一个居中标题读成设计不足；zine 声线期待版式装满编辑动作。正确密度是一个主导文字瞬间，由多个从属组件支撑（装饰印章、eyebrow 标签、分隔 stub、手写署名、首字下沉）。真正的稀疏留给宣言 / 陈述瞬间，那里一句大引文主导整块实心绿场。

**关键特征：**
- 温暖卡其纸画布（`{colors.bg}`）+ 深绿森林强调（`{colors.green}`）+ 墨黑结构（`{colors.black}`）。
- SVG 颗粒叠层（`{components.grain-overlay}`）以 0.07 不透明度坐在每一页上，强化印刷纸档。
- 每个展示瞬间用 Bebas Neue 全大写 + 字距；正文用小字号 Space Grotesk；手写强调用 Caveat。
- 3px 实心黑结构描边划分区域；2px 和 1.5px 描边再细分。
- 纸压纸偏移卡片：绿板通过 `::before` 坐在白卡片后面 12px。
- 印章和拼贴片带着小旋转（-8°、+6°、-5° 到 +5°）。
- 半透明美纹纸胶带片（`{components.tape}`）叠在拼贴构图上。
- 绿首字下沉、绿丝带条和绿行内高光标记编辑强调。

## 颜色

### 色板
- **Background**（`{colors.bg}` — #C8B99A）：温暖卡其纸画布。每页的默认表面。饱和到足以读成带历史的纸，而不是中性底；暖到能与森林绿强调和谐。
- **Background Dark**（`{colors.bg-dark}` — #B8A98A）：画布略深的色调兄弟。分屏一半需要在视觉上坐在另一半后面时用于分层表面区域，以及想读成「卡其纸上的纸」的拼贴片。
- **Green**（`{colors.green}` — #008F4D）：深绿森林。系统的强调色——hero 数字、首字下沉、丝带条、宣言页背景、进度条、行内高光、RSVP 标签、卡片后的偏移板、收束页上的分隔 stub。最有辨识度的非画布色。
- **Green Light**（`{colors.green-light}` — #00A85D）：绿略亮的兄弟。深绿需要抬一档时，可用作悬停状态或次级绿；基线静态页里很少用。
- **Black**（`{colors.black}` — #1A1A1A）：墨黑。结构色——全部描边、全部正文、全部分隔、全部收束页背景、全部标签填色（反转时）。比纯黑（#000000）略软，好当暖纸上的暖墨。
- **White / Cream**（`{colors.white}` — #F4EFE6）：柔软奶油。用作卡片填色（纸压纸）、黑表面上的文字，以及宣言页上的分隔 stub 色。关键是，这不是纯白——是纸奶油，即便当「白」表面用也保住暖纸档。

### 默认值
- **默认表面背景**：`{colors.bg}` ——每页都从温暖卡其纸打开。
- **默认标题色**：主区块标题和 hero 标题用 `{colors.green}`；双栏或分屏里与正文配对的标题用 `{colors.black}`。拿不准时伸手去拿 `{colors.green}` ——绿标题是系统最响的编辑信号。
- **默认正文字色**：`{colors.black}`。
- **默认描边色**：`{colors.black}` ——每条结构描边都是黑，没有例外。
- **强调用的默认强调表面（宣言、hero 呼出）**：`{colors.green}` 配 `{colors.white}` 文字。
- **`{colors.green}` 表面上的默认文字色**：`{colors.white}`（奶油）。
- **`{colors.black}` 表面上的默认文字色**：`{colors.bg}`（卡其画布），这样即便反转，字仍读成「纸上的墨」。黑表面上的绿强调（收束页 eyebrow + 手写）抬起反转。
- **默认 eyebrow / 标签色**：Bebas Neue 标签用 `{colors.green}`；加字距的 Space Grotesk 标签用 `{colors.black}`。
- **默认首字下沉色**：`{colors.green}`。首字下沉是编辑指纹，始终是绿。
- **默认手写色**：卡其/奶油表面上 `{colors.black}`；黑表面上 `{colors.green}`（收束）。
- **默认行内高光**：黑压卡其（`{components.inline-highlight}`）——用来在正文段落里抬起短语，像马克笔划过。

绿和黑强调不可互换：**绿 = 强调**（这是我们想让你注意到的），**黑 = 结构**（这是把页撑住的）。反过来——用黑做强调、用绿做结构——会翻掉系统声线。

## 字体

### 字族
系统配对三款 Google Fonts：

- **Bebas Neue**（展示）：压缩全大写工业无衬线。单字重（400），但靠密的竖笔画读成粗。每个展示瞬间——标题、宣言、统计、序数、eyebrow 标签——都全大写，字距 0.02–0.04em。窄、加字距的 Bebas 声线是让系统一眼就是「zine」的东西。
- **Space Grotesk**（正文）：干净的人文几何无衬线，比例略古怪。小字号（13–18px）正文段落用字重 300–500，加字距的 Space Grotesk 全大写标签用字重 600。给 Bebas 的表现密度提供可读对位。
- **Caveat**（手写）：随意手写草书。字重 400–700，用于作者署名（"— Our founding principle since day one"）、旁注、展示元素上的装饰图注、RSVP 式表单版式里的值填空。在否则都是排过的系统里提供温度和人手声线。

没有第四张脸。不存在斜体（Caveat 是手写脸，不是斜体）。不存在下划线。强调靠换脸（Space Grotesk 正文 → Caveat 手写做私人便条，Bebas Neue 展示做呼出）或换色（`{colors.black}` → `{colors.green}`）。

### 字号阶梯

| Token | 字号 (clamp) | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.display-hero}` | 56–160px | Bebas Neue | 400 | 收束或超大封面标题 |
| `{typography.display-cover}` | 48–140px | Bebas Neue | 400 | 封面 / 开场展示标题 |
| `{typography.display}` | 48–120px | Bebas Neue | 400 | 重大宣言或呼出展示 |
| `{typography.headline}` | 42–90px | Bebas Neue | 400 | 主区块标题 |
| `{typography.statement}` | 36–90px | Bebas Neue | 400 | 长引文宣言 |
| `{typography.headline-md}` | 36–72px | Bebas Neue | 400 | 编辑区块页眉 |
| `{typography.title}` | 24–42px | Bebas Neue | 400 | 区域或拼贴片标题 |
| `{typography.number-hero}` | 80–160px | Bebas Neue | 400 | Hero 统计数字 |
| `{typography.number-md}` | 44–80px | Bebas Neue | 400 | 砖或次级统计数字 |
| `{typography.drop-cap}` | 48–80px | Bebas Neue | 400 | 编辑段落开头的首字 |
| `{typography.body-md}` | 14–18px | Space Grotesk | 400 | 导语段落或强调正文 |
| `{typography.body}` | 13–16px | Space Grotesk | 400 | 标准段落正文 |
| `{typography.label-eyebrow}` | 14–18px | Bebas Neue | 400 | 标题上方的 eyebrow 标签，字距 0.2em |
| `{typography.label-spaced}` | 12–14px | Space Grotesk | 600 | 加字距全大写小标签 |
| `{typography.caption-feature}` | 13–15px | Bebas Neue | 400 | 加字距全大写图注或特性呼出标签 |
| `{typography.hand-script}` | 22–36px | Caveat | 600 | 作者署名、装饰便条、宣言落款 |
| `{typography.hand-script-sm}` | 16–22px | Caveat | 400 | 小手写标签或描述 |
| `{typography.hand-script-lg}` | 24–36px | Caveat | 600 | 更大的手写副标题 |

### 默认值
- **主区块标题的默认字号**：`{typography.headline}`（42–90px clamp），`{colors.green}`。
- **封面或超大开场标题的默认字号**：`{typography.display-cover}`（48–140px clamp），`{colors.green}`。
- **段落正文的默认字号**：`{typography.body}`（13–16px clamp）——zine 档期待小正文字，不是现代 18px+ 段落。
- **导语段落或强调正文的默认字号**：`{typography.body-md}`（14–18px）。
- **标题上方 eyebrow 标签的默认字号**：`{typography.label-eyebrow}`（14–18px），`{colors.green}`，字距 0.2em 全大写。
- **Hero 数字的默认字号**：`{typography.number-hero}`（80–160px clamp），`{colors.green}`。
- **任何手写署名 / 旁注的默认字号**：`{typography.hand-script}`（22–36px clamp）。
- **任何 Bebas 展示元素的默认字重**：400（Bebas Neue 以 400 出货；改字重不是系统的一部分）。
- **正文的默认字重**：400；加字距全大写小标签：600。

一页上主导文字瞬间在 `{typography.headline}` 和 `{typography.title}` 之间拿不准时，伸手去拿 `{typography.headline}` —— `{typography.title}` 留给页内拼贴片或区域级副标题。

### 标志性处理
这些处理在**对应元素类型被使用时不可省略**：

- **每个 Bebas Neue 元素都是全大写。** 字体有小写字形，但这套系统不用。句首大写 Bebas 不是词汇的一部分。
- **每个 Bebas Neue 元素都带着至少 0.02em 的正字距。** 默认字距的 Bebas 读成挤；0.02–0.04em 把它打开。标签和 eyebrow 字距更宽（0.2–0.25em）。
- **每个主区块标题都设成 `{colors.green}`。** 黑标题存在（给与正文配对的栏），但系统最响的编辑声线是绿压卡其。
- **每个打开一栏的编辑段落都可以带首字下沉。** 首字下沉始终是 `{components.drop-cap}` ——绿、Bebas Neue、行高 0.8、左浮动。用作特写长度正文栏的开场花饰。
- **每个手写元素都用 Caveat。** 换成另一张手写脸会丢掉私人便条声线。
- **手写署名跟在引文 / 宣言版式的展示标题后面。** 没有手写落款的宣言读成不完整；落款把引文锚定成人声。
- **正文内的行内高光用黑压卡其模式**（`{components.inline-highlight}`），不是绿压卡其。行内绿读成笔误；行内黑读成马克笔条。

### 排印原则
系统的排印节奏来自**三脸对比**：压缩工业 Bebas 展示（响、加字距、全大写）→ 干净 Space Grotesk 正文（静、小、句首大写）→ 表现性 Caveat 手写（私人、更松、签名式）。只用一张脸的页读成单调；在单一构图里混三张脸的页读成 zine 正确。

行高：展示紧（0.85–1.1），正文松（1.6–1.7），手写松（1.3）。绝不要倒置——紧正文和松展示都会打断节奏。

## 版式

### 画布系统
系统目标是 `100vw × 100vh` ——满视口。每个 `.slide` 绝对定位铺满视口；只有 `.active` 页可见（不透明度 1，其余 0）。页面过渡用 0.6s 不透明度 + translateY(20px) ease，做出柔软翻纸感。导航由 JS 驱动：方向键、空格、点击、触控滑动。一条 4px 高的 `{colors.green}` 进度条贴着底边跑。

### 内边距阶梯
| Token | 值 | 用途 |
|---|---|---|
| `{spacing.slide-pad}` | 60px | 标准幻灯片外边距 |
| `{spacing.slide-pad-wide}` | 60px 80px | 编辑栏跨页外边距 |
| `{spacing.card-pad-lg}` | 48px | Hero 卡片内部（RSVP、大呼出） |
| `{spacing.card-pad-md}` | 32px | 网格盒单元格内部 |
| `{spacing.card-pad-sm}` | 24px | 拼贴片、较小卡片单元格内部 |
| `{spacing.gap-lg}` | 60px | 编辑栏间距 |
| `{spacing.gap-md}` | 40px | 标准区域间距 |
| `{spacing.gap-sm}` | 24px | 紧的行内间距 |

### 持续页框
三个持续元素活在幻灯片构图之外：
- **进度条**贴着左下，4px 高，填色 `{colors.green}`。随片子前进增长。
- **页码计数**在右下——Bebas Neue 14px，2px 描边的奶油芯片，卡其墨。
- **导航提示**在底部居中——黑填胶囊配奶油字，只在 `body:hover` 时淡入（0.4s 不透明度过渡）。

### 区域描边 vs 内部 padding
系统对网格容器遵循**描边当分隔**原则——父容器有 3px 实心黑外描边，每个子单元格有 1.5px 实心黑描边，做成发丝格到格分隔。区域在幻灯片边缘相接时（分屏版式），分隔线是 3px 实心黑，两个区域直接碰上——没有缝。

自由构图（拼贴、hero、宣言）里，区域绝对定位带旋转和重叠；描边坐在单片上，不坐在幻灯片网格上。

## 层次与抬升

### 纸压纸偏移色块（主手法）
招牌层次处理是**偏移色块**：卡片带着绝对定位的 `::before` 伪元素，向右下偏移 12px，填 `{colors.green}`（或其他强调），z-index 在卡片后面。视觉效果是分层纸垫印——卡片看起来坐在略大的绿纸上，绿从右下边缘透出来。用在 hero RSVP 卡片和主呼出容器上。

### 旋转（次手法）
印章记号、RSVP 标签、视觉叠层呼出和拼贴片上的小旋转（`-8deg` stamp、`+6deg` stamp-alt、`-5deg` 到 `+5deg` 拼贴）给系统手摆上去的能量。旋转是故意的——绝不是意外歪——留给应读成实物的元素（印章、胶带片、贴上的标签）。

### 颗粒叠层（大气纹理）
微妙的 SVG 分形噪点叠层以 0.07 不透明度坐在每一页上，给所有表面染上印纹。这不是严格意义上的层次——是把每块平色块锚定在印刷纸档上的表面纹理。拿掉颗粒立刻打断 zine 声线。

### 没有网页阴影
系统使用**没有模糊 `box-shadow`、没有 `drop-shadow`、没有 rgba 阴影着色**做层次。偏移色块、旋转和颗粒叠层是全部层次语法。任何元素上的现代柔软阴影都会打断印刷审美。

### 色块对比
阴影和旋转之外，**绿压卡其和黑压卡其对比**提供区域层次。卡其区域里的绿丝带条在视觉上向前凸；白卡片后的黑区域在视觉上后退。色板的高对比是次级层次信号。

## 形状与处理

### 圆角
系统**没有圆角**。每个形状——卡片、丝带条、印章、RSVP 卡片、表格单元格、首字下沉、芯片、分隔 stub——都是严格矩形或正方形。Border-radius 全系统 `0`。

### 描边粗细
- **3px solid `{colors.black}`** ——卡片、区域分隔、网格容器外描边、拼贴片、RSVP 卡片、hero 呼出上的通用结构描边。
- **2px solid `{colors.black}`** ——用于编辑栏线、RSVP 栏下划线、ed-header 底边，以及 stamp-mark 的绿描边。
- **1.5px solid `{colors.black}`** ——用于 3px 外描边容器内的网格单元格子描边，以及账本表头下划线。
- **1px solid rgba(black, 0.22)** ——用于账本行分隔和发丝表格分隔。

描边始终是黑。彩色描边不存在，除了 `{components.stamp-mark}` 批准章上的绿描边。

### 装饰元素类型

**Line box**（`{components.line-box}`）— 卡其背景上通用 3px 描边卡片。系统的默认内容容器。Padding 来自 `{spacing.card-pad-*}` 阶梯。

**带偏移的卡片**（`{components.card-offset}`）— 白奶油卡片，3px 黑描边，12px 偏移的绿板通过 `::before` 坐在后面。招牌纸压纸卡片。

**印章**（`{components.stamp}` / `{components.stamp-mark}`）— 任何元素都可以旋转 -8°（stamp）或 +6°（stamp-alt），读成手盖上去的记号。`stamp-mark` 变体是黑矩形配绿字和绿描边。用作批准章、「CONTACT US」徽章和编辑印章。

**拼贴片**（`{components.collage-piece}`）— 自由定位面板，3px 黑描边加小旋转。背景在片之间轮换：绿、白奶油、卡其深、黑反转。用在多片带重叠散落在页上的拼贴构图。

**胶带**（`{components.tape}`）— 半透明白矩形，随机角度叠在拼贴片上，暗示物理贴住的纸。始终半透明，始终锐角（-40° 到 +35°）。

**丝带条**（`{components.ribbon-bar}`）— 实心绿色块配奶油字——用作 eyebrow 条、强调条和行内区块标签。读成粘在页上的印刷丝带。

**首字下沉**（`{components.drop-cap}`）— 超大绿 Bebas Neue 首字，打开编辑段落。左浮动，行高 0.8，正文绕过去。

**行内高光**（`{components.inline-highlight}`）— 正文段落里行内施加的黑压卡其马克笔划，用来抬起短语。马克笔的印刷对等。

**RSVP 栏**（`{components.rsvp-field}`）— 表单栏行模式：Bebas Neue 绿标签配对 2px 黑下划线上的手写 Caveat「书写」。系统的「手填」表单模式。

**账本行**（`{components.ledger-row}`）— 水平数据行模式，date | title | edition | track | nr 列。表头行有 1.5px 黑下划线；正文行有 1px 发丝分隔。每行可以含一个颜色编码芯片（`{components.chip}`）标记其类别。

**芯片**（`{components.chip}`）— 等宽字体色块（用了则 JetBrains Mono，否则默认等宽）标记行类别。填色：绿，加上从更宽印章色板拉来的分类色板扩展（出现在那些页上）。

**分隔 stub**（`{components.divider-stub}`）— 短 4px 实心水平线（宽 60–80px），居中，用作 hero 标题或宣言上/下的视觉呼吸。绿表面上白，黑表面上绿。

**手写元素** — 任何 Caveat 文字。系统给「人声」的信号——署名、旁注、图注、RSVP 栏填空、收束页落款。

## 该做与不该做

### 该做
- 每一页都保留 SVG 颗粒叠层（`{components.grain-overlay}`），0.07 不透明度。它是把整套片子锚定到印刷纸档的纹理。
- 每个展示、标题、宣言、统计、数字和 eyebrow 标签都用 Bebas Neue 全大写加 0.02–0.04em 字距。
- 主区块标题默认伸手去拿 `{colors.green}`。绿压卡其是系统最响的编辑信号。
- Hero 呼出和 RSVP 式卡片用纸压纸偏移模式（`{components.card-offset}`）——绿板通过 `::before` 坐在白卡片后面。
- 对应读成实物的元素施加小旋转（-8° 印章、-5° 到 +5° 拼贴片）。旋转应始终感觉是故意的。
- 用首字下沉（`{components.drop-cap}`）打开编辑正文栏。它们是系统的编辑指纹。
- 在单一构图里混三张脸——Bebas Neue 展示 + Space Grotesk 正文 + Caveat 手写。三脸对比是排印节奏。
- 正文段落里的行内高光设成黑压卡其（`{components.inline-highlight}`），模仿马克笔划。
- 每句引文 / 宣言下面配对 Caveat 手写落款。手写署名把引文锚定成人声。
- 在拼贴构图上以锐角叠半透明胶带片（`{components.tape}`），暗示物理贴住的纸。

### 不该做
- 不要圆任何角。每个元素的 border-radius 全系统 0。
- 不要用模糊 `box-shadow`。所有层次来自偏移色块、旋转和颗粒叠层。
- 不要用另一张展示脸替换 Bebas Neue。压缩工业加字距全大写声线是整套系统身份。
- 不要用句首大写的 Bebas Neue。这套系统里 Bebas 始终渲成全大写；小写 Bebas 读成错。
- 不要用另一张手写脸替换 Caveat。随意圆珠笔声线是系统的一部分；Lobster、Pacifico 等会落到别处。
- 不要引入第三品牌色。卡其 + 绿 + 黑 + 奶油是系统。加蓝或红会打断土地与森林色板。芯片色板扩展（橙 / 粉 / 蓝 / 红）留给表格账本里的分类芯片标签——不是通用强调。
- 不要用绿压卡其做行内高光。行内马克笔划是黑压卡其；行内绿读成笔误。
- 不要把元素歪超过 ±8°。超过那个，手摆就变成坏掉。
- 不要把正文放到大于 18px。Zine 栏密度档依赖小正文字（13–16px）。现代 20px+ 正文读成过大。
- 不要用纯白（#FFFFFF）做卡片。奶油（`{colors.white}` #F4EFE6）保住纸压纸档；纯白读成数字的。

## 响应式行为

系统目标是 `100vw × 100vh`，全程用 `clamp()` 做流体缩放。唯一一条媒体查询在 `max-width: 768px`：多栏版式回流成单栏，去掉栏间描边规则改成底边框，幻灯片 padding 减到 32px。

### 缩放行为
- 展示标题从最小 48px 缩放到最大 140–160px。
- 正文从 13px 缩放到 16–18px。
- Padding 从 32px（移动）缩放到 60–80px（桌面）。
- 描边、胶带尺寸和印章旋转是固定的——不随视口缩放。

### 演示行为
- 前进：`ArrowRight`、`ArrowDown`、`Space`、`Enter`、`PageDown`，或点视口右半。
- 后退：`ArrowLeft`、`ArrowUp`、`PageUp`，或点左半。
- 活动页带着 `.active` 类；非活动页不透明度 0 并带 `translateY(20px)`。
- 移动端水平触控滑动前进/后退。
- 底部居中的导航提示在 `body:hover` 时淡入（0.4s 不透明度）。

### 打印行为
没有定义 `@media print` 规则。片子以网页/视口为先。

## 中日韩与国际内容

### 推荐中文搭配

| 角色 | 拉丁 | 中文 | 字重映射 |
|---|---|---|---|
| 展示 / 标题 / 宣言 / 标题 / 数字 / 首字下沉 / Label-eyebrow | Bebas Neue (400) | **思源宋体 Noto Serif SC** | 900 |
| 正文 / Body-md / Label-spaced | Space Grotesk (400 / 600) | **思源宋体 Noto Serif SC** | 400（正文），600（标签） |
| 手写（Caveat）——仅拉丁 | Caveat (400 / 600) | *（无 CJK 替代）* | n/a |

### 混排策略

**策略 A ——单一 CJK 字族（思源宋体 Noto Serif SC）扛每个排过的角色。** Bebas Neue 的压缩工业全大写声线没有能保住重海报字重、又不读成陈词滥调汉字风展示的中文无衬线对等。不过 Noto Serif SC 字重 900 带着真正的印刷机分量，映射到 zine 档：深衬线笔画呼应凸版和木刻印刷，这比任何中文无衬线都*更接近*系统的世纪中叶行动派海报审美。拉丁 Bebas + 中文 Noto Serif SC 读成「同一本 zine 的译本」，不是两套互相竞争的系统。正文用同一字族字重 400，在小字号（13–16px）上坐得舒服，保住杂志栏密度。

### 加载

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;600;700;900&display=swap" rel="stylesheet">
```

然后把 `'Noto Serif SC'` 接到对应字体栈：
```css
/* Display roles */
font-family: 'Bebas Neue', 'Noto Serif SC', sans-serif;
/* Body roles */
font-family: 'Space Grotesk', 'Noto Serif SC', sans-serif;
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

- **定义 Bebas 展示的 0.02–0.04em 正字距在 CJK 上必须降到 0。** 加字距的中文字看起来坏掉——间距在视觉上把每个字分成单独的词。Bebas 的压缩加字距签名转不过去；单靠字重 900 扛展示声线。
- **展示行高必须从 0.85–0.95 打开到 1.15–1.25。** Bebas 的紧行高是拉丁展示惯例；CJK 字符完全占满 em 盒，需要纵向呼吸空间。
- **首字下沉需要再想。** Bebas 首字下沉浮动在正文左边；同样字号（`clamp(48px, 6vw, 80px)`）的 Noto Serif SC 首字下沉，`{colors.green}`，视觉上成立，但缺少编辑传统共鸣——中文排版历史上不用首字下沉。要么把处理当成西式编辑点头留下，要么换成绿竖侧栏（3px 宽，绿填色）沿着开场段落跑。
- **行内高光、丝带条和印章记号都干净地翻译** ——它们是色块处理，不依赖字形。
- **手写 Caveat 是系统的「人声」——没有保住圆珠笔草书性格的中文对等。** 把 Caveat 瞬间当成仅拉丁：署名单用拉丁，即便在否则是中文的页上也用拉丁旁注，RSVP 表单填空用拉丁。中文排过的正文与拉丁手写边注的对比，反而能加深 zine 声线（读成「译者批注」，契合小出版社档）。
- **编辑正文字号（13–16px）仍然适用** ——这个字号的 Noto Serif SC 读成密的杂志栏文，对 zine 档是对的。

### 已知中日韩缺口

系统的三脸对比（Bebas 展示 + Space Grotesk 正文 + Caveat 手写）是拉丁排印论证；收成单一 CJK 衬线丢掉一种节奏、换上另一种。决定用衬线（Noto Serif SC）而不是无衬线（Noto Sans SC）是故意的——zine 的世纪中叶印刷机谱系，映射到中文衬线传统比映射到中文几何无衬线更好。混中英文的片子需要接受：英文 Bebas 声线和中文衬线声线是不同档；这在任何重海报 CJK 改编里都不可避免。

## 迭代指南

1. 每一页新页都带着 0.07 不透明度的 SVG 颗粒叠层。拿掉颗粒立刻打断 zine 声线。
2. 任何新标题用 Bebas Neue 全大写，字重 400，字距 0.02–0.04em。页上的主瞬间伸手去拿 `{typography.headline}`，`{colors.green}`；分屏或栏里标题与正文配对时，用 `{colors.black}`。
3. 任何新正文用 Space Grotesk 13–16px（导语正文 14–18px）。行高 1.6–1.7。不要把正文放大超过 18px。
4. 任何新 eyebrow 标签：最强调的 eyebrow 用 `{typography.label-eyebrow}`（Bebas Neue，14–18px，0.2em 字距），`{colors.green}`；次级标签切到 `{typography.label-spaced}`（Space Grotesk 字重 600，0.25em 字距）。
5. 任何新卡片用 3px 实心黑描边，白奶油或卡其背景。Hero 呼出加上通过 `::before` 的 12px 偏移绿板（`{components.card-offset}`）。
6. 任何新编辑栏可以带首字下沉——绿 Bebas Neue，左浮动，行高 0.8。首字下沉是编辑指纹。
7. 任何新宣言 / 引文页把 Bebas Neue 全大写引文和 Caveat 手写落款配对。落款不是可选的。
8. 任何拼贴构图用 3px 描边拼贴片加小旋转（-5° 到 +5°），锐角半透明胶带片叠在接缝上。循环背景：绿、白奶油、卡其深、黑反转。
9. 任何表格账本用 `{components.ledger-row}` 模式，表头下划线 1.5px，正文行分隔 1px 发丝。分类标签用等宽 `{components.chip}`，绿或分类芯片色板。
10. 状态 / 批准章用 `{components.stamp-mark}` ——黑背景、绿字、绿 2px 描边，旋转 -8°。留给配得上盖章的瞬间；滥用会降解信号。

## 已知缺口

- 系统从 CDN 加载三款 Google Fonts（Bebas Neue、Caveat、Space Grotesk）。Bebas Neue 是单字重（仅 400）；尝试用更重字重会回退。生产环境建议自托管。
- 颗粒叠层是带 `feTurbulence` 的内联 SVG data URI——渲染会在浏览器之间略有差异，尤其是较旧的 Safari 和 Firefox 版本。
- 纸压纸偏移色块依赖 `z-index: -1` 的 `::before` 伪元素。卡片必须有 `position: relative`，父级不得裁切 overflow，否则偏移板会被切掉。
- 账本行上的芯片颜色扩展用红 / 粉 / 橙 / 蓝 / 绿——只为表内分类标记拉进来。这些颜色不是通用系统色板的一部分，不应出现在幻灯片构图的别处。
- Caveat 手写脸有很强的文化档（随意美式手写）。它配不好非拉丁文字；CJK 或西里尔片子需要不同的手写替代。
- 导航提示上的 `body:hover` 淡入在触控设备上不触发，意味着移动用户可能永远看不到导航提示。把提示当成仅桌面 chrome。
- 收束页用 `{colors.black}` 背景配 `{colors.bg}`（卡其）文字。颗粒叠层仍施加，但 0.07 不透明度压在黑上可见得多——收束页上的印刷档比卡其背景页弱。
- 表单栏 RSVP 卡片用手画下划线（`_________`）当「空白行」——这些是基于字符的，不是渲成真正的 `<input>` 下划线，跨系统字体不会完美对齐。
