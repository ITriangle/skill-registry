---
version: alpha
name: People's Platform
description: "A WPA-poster-meets-political-campaign presentation system built on three typefaces and a five-color palette that reduces to three functional roles. Alfa Slab One — a compressed slab serif — does all the heavy lifting at extreme sizes in pure uppercase. Caveat Brush drops in as a handwritten human interrupt: lowercase, slightly rotated, emotionally warm. DM Mono carries all metadata at tight uppercase tracking. The palette is electric cobalt blue, amber orange, and hot red — with red functioning exclusively as a shadow/depth color, never as a surface fill. Every slide gets a paper grain overlay that makes the whole deck feel screen-printed. The aesthetic is loud, confident, and populist — the kind of visual language that belongs on a protest placard, a union newsletter, or a campaign bus."

colors:
  blue: "#2C2CDC"
  blue-deep: "#1B1BB0"
  orange: "#F2A03A"
  orange-deep: "#E89321"
  red: "#E83A2A"
  red-deep: "#B7281C"
  cream: "#F4E9D6"
  paper: "#F5F2EA"
  ink: "#0E0E14"

typography:
  display-jumbo:
    fontFamily: "Alfa Slab One, serif"
    fontSize: 540px
    fontWeight: 400
    lineHeight: 0.82
    letterSpacing: -0.02em
    textTransform: uppercase
  display-hero:
    fontFamily: "Alfa Slab One, serif"
    fontSize: 260px
    fontWeight: 400
    lineHeight: 0.86
    letterSpacing: 0.005em
    textTransform: uppercase
  display-title:
    fontFamily: "Alfa Slab One, serif"
    fontSize: 240px
    fontWeight: 400
    lineHeight: 0.86
    letterSpacing: 0.005em
    textTransform: uppercase
  display-xl:
    fontFamily: "Alfa Slab One, serif"
    fontSize: 180px
    fontWeight: 400
    lineHeight: 0.88
    letterSpacing: 0.005em
    textTransform: uppercase
  display-lg:
    fontFamily: "Alfa Slab One, serif"
    fontSize: 140px
    fontWeight: 400
    lineHeight: 0.88
    letterSpacing: 0.005em
    textTransform: uppercase
  display-md:
    fontFamily: "Alfa Slab One, serif"
    fontSize: 120px
    fontWeight: 400
    lineHeight: 0.88
    letterSpacing: 0.005em
    textTransform: uppercase
  display-sm:
    fontFamily: "Alfa Slab One, serif"
    fontSize: 108px
    fontWeight: 400
    lineHeight: 1.04
    letterSpacing: 0.005em
    textTransform: uppercase
  stat-unit:
    fontFamily: "Alfa Slab One, serif"
    fontSize: 130px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0
    textTransform: uppercase
  section-num:
    fontFamily: "Alfa Slab One, serif"
    fontSize: 54px
    fontWeight: 400
    lineHeight: 1.0
    textTransform: uppercase
  card-title:
    fontFamily: "Alfa Slab One, serif"
    fontSize: 54px
    fontWeight: 400
    lineHeight: 1.0
    textTransform: uppercase
  kpi-value:
    fontFamily: "Alfa Slab One, serif"
    fontSize: 88px
    fontWeight: 400
    lineHeight: 0.9
    textTransform: uppercase
  quote-mark:
    fontFamily: "Alfa Slab One, serif"
    fontSize: 300px
    fontWeight: 400
    lineHeight: 0.7
    textTransform: uppercase
  quote-body:
    fontFamily: "Alfa Slab One, serif"
    fontSize: 78px
    fontWeight: 400
    lineHeight: 1.08
    textTransform: uppercase
  item-title:
    fontFamily: "Alfa Slab One, serif"
    fontSize: 38px
    fontWeight: 400
    lineHeight: 1.0
    textTransform: uppercase
  item-title-sm:
    fontFamily: "Alfa Slab One, serif"
    fontSize: 30px
    fontWeight: 400
    lineHeight: 1.0
    textTransform: uppercase
  toc-entry:
    fontFamily: "Alfa Slab One, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.0
    textTransform: uppercase
  subtitle:
    fontFamily: "Alfa Slab One, serif"
    fontSize: 72px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.01em
    textTransform: uppercase
  cta:
    fontFamily: "Alfa Slab One, serif"
    fontSize: 48px
    fontWeight: 400
    letterSpacing: 0.02em
    textTransform: uppercase
  stamp:
    fontFamily: "Alfa Slab One, serif"
    fontSize: 28px
    fontWeight: 400
    letterSpacing: 0.04em
    textTransform: uppercase
  url:
    fontFamily: "Alfa Slab One, serif"
    fontSize: 46px
    fontWeight: 400
    letterSpacing: 0.02em
    textTransform: uppercase
  script-lg:
    fontFamily: "Caveat Brush, cursive"
    fontSize: 96px
    fontWeight: 400
    textTransform: lowercase
  script-md:
    fontFamily: "Caveat Brush, cursive"
    fontSize: 64px
    fontWeight: 400
    textTransform: lowercase
  body-lg:
    fontFamily: "Archivo Narrow, sans-serif"
    fontSize: 30px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Archivo Narrow, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-sm:
    fontFamily: "Archivo Narrow, sans-serif"
    fontSize: 26px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-xs:
    fontFamily: "Archivo Narrow, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label:
    fontFamily: "DM Mono, monospace"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.18em
    textTransform: uppercase
  label-wide:
    fontFamily: "DM Mono, monospace"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.22em
    textTransform: uppercase
  label-accent:
    fontFamily: "DM Mono, monospace"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0.16em
    textTransform: uppercase
  signoff:
    fontFamily: "DM Mono, monospace"
    fontSize: 26px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.20em
    textTransform: uppercase

spacing:
  slide-gutter: 90px
  content-gutter: 120px
  topbar-height: 90px
  section-border: 6px
  inner-border: 3px
  grid-gap-lg: 90px
  grid-gap-md: 30px
  frame-inset: 48px

canvas:
  width: 1920px
  height: 1080px

components:
  inset-frame:
    border: "6px solid {colors.cream}"
    position: absolute
    inset: 48px
  topbar:
    position: absolute
    top: 0
    left: 0
    right: 0
    height: 90px
    background: "{colors.blue}"
    color: "{colors.cream}"
    padding: 0 90px
    fontFamily: "DM Mono, monospace"
    fontSize: 24px
    letterSpacing: 0.18em
    borderBottom: "6px solid {colors.cream}"
  section-divider:
    borderBottom: "6px solid {colors.ink}"
    height: 6px
  toc-row:
    display: grid
    gridTemplateColumns: "90px 1fr 100px"
    gap: 24px
    padding: "20px 0"
    borderBottom: "3px solid {colors.ink}"
  toc-num:
    fontFamily: "Alfa Slab One, serif"
    fontSize: 54px
    color: "{colors.orange}"
    textShadow: "3px 3px 0 {colors.red}"
  pillar-col:
    padding: "60px 50px"
    borderRight: "6px solid {colors.ink}"
    background: "{colors.paper}"
  pillar-col-alt:
    background: "{colors.blue}"
    color: "{colors.cream}"
  pillar-tag:
    fontFamily: "DM Mono, monospace"
    fontSize: 24px
    letterSpacing: 0.18em
    borderTop: "3px solid {colors.ink}"
    paddingTop: 18px
    marginTop: 14px
    alignSelf: flex-start
  kpi-card:
    border: "5px solid {colors.ink}"
    padding: "28px 30px"
    background: "{colors.paper}"
  kpi-card-alt:
    background: "{colors.blue}"
    color: "{colors.cream}"
  timeline-dot:
    width: 60px
    height: 60px
    borderRadius: 50%
    background: "{colors.orange}"
    border: "6px solid {colors.ink}"
    boxShadow: "6px 6px 0 {colors.red}"
  timeline-dot-alt:
    background: "{colors.blue}"
  timeline-track:
    height: 14px
    background: "{colors.ink}"
  compare-side-left:
    background: "{colors.paper}"
    borderRight: "6px solid {colors.ink}"
    padding: "60px 70px"
  compare-side-right:
    background: "{colors.blue}"
    color: "{colors.cream}"
    padding: "60px 70px"
  compare-label:
    fontFamily: "DM Mono, monospace"
    fontSize: 24px
    letterSpacing: 0.22em
    paddingBottom: 14px
    borderBottom: "4px solid {colors.ink}"
    alignSelf: flex-start
  diamond-bullet:
    width: 24px
    height: 24px
    background: "{colors.red}"
    borderRadius: 4px
    transform: rotate(45deg)
  diamond-bullet-alt:
    background: "{colors.orange}"
  avatar:
    width: 120px
    height: 120px
    borderRadius: 50%
    background: "{colors.blue}"
    border: "6px solid {colors.blue}"
    boxShadow: "6px 6px 0 {colors.red}"
  quote-stamp:
    background: "{colors.blue}"
    color: "{colors.orange}"
    padding: "18px 32px"
    transform: rotate(-3deg)
    border: "5px solid {colors.cream}"
    fontFamily: "Alfa Slab One, serif"
    fontSize: 28px
    letterSpacing: 0.04em
    boxShadow: "6px 6px 0 {colors.red}"
    textTransform: uppercase
  circular-stamp:
    width: 200px
    height: 200px
    borderRadius: 50%
    background: "{colors.cream}"
    color: "{colors.blue}"
    border: "6px solid {colors.orange}"
    transform: rotate(-9deg)
    boxShadow: "8px 8px 0 {colors.red}"
  meta-pill:
    border: "3px solid {colors.cream}"
    padding: "8px 20px"
    borderRadius: 999px
  ribbon:
    position: absolute
    bottom: 0
    left: 0
    right: 0
    height: 60px
    background: "{colors.orange}"
    color: "{colors.blue}"
    borderTop: "6px solid {colors.ink}"
    fontFamily: "DM Mono, monospace"
    fontSize: 24px
    letterSpacing: 0.22em
    fontWeight: 600
  lede-block:
    fontFamily: "Archivo Narrow, sans-serif"
    fontWeight: 500
    fontSize: 28px
    lineHeight: 1.35
    borderLeft: "4px solid {colors.ink}"
    paddingLeft: 50px
  lede-block-top:
    borderTop: "6px solid {colors.ink}"
    paddingTop: 24px
  underline-rule:
    height: 14px
    background: "{colors.ink}"
    width: "30%"
    marginTop: 60px
  kicker:
    fontFamily: "DM Mono, monospace"
    letterSpacing: 0.22em
    fontSize: 26px
    color: "{colors.red}"
    marginBottom: 48px
  grain-overlay:
    position: absolute
    inset: 0
    pointerEvents: none
    backgroundImage: "radial-gradient(rgba(0,0,0,.06) 1px, transparent 1px), radial-gradient(rgba(255,255,255,.05) 1px, transparent 1px)"
    backgroundSize: "3px 3px, 5px 5px"
    backgroundPosition: "0 0, 1px 2px"
    mixBlendMode: multiply
    opacity: 0.5
  orange-dot:
    width: 10px
    height: 10px
    borderRadius: 50%
    background: "{colors.orange}"
---

## 概览

People's Platform 是一套 **WPA 海报遇见政治竞选的幻灯片系统** —— 信念的视觉语言，公共演说的图形声线。画布是暖纸（`{colors.paper}` — #F5F2EA），比白略暖一丝，每一页都通过 CSS 伪元素叠一层颗粒纹理，让整份文稿读起来像丝网印，而不是渲染出来的。

字体栈是三路分职系统。**Alfa Slab One** 在极端字号上占领舞台——压缩、厚板衬线、全大写，天生有权威。它是喊的声线。**Caveat Brush** 是人的打断——手写、小写、略旋转、情感在场。它是耳语的声线。**DM Mono** 是官僚记账员——等宽、宽字距全大写、始终 24px——把事情记账的声线。Archivo Narrow 是正文苦力：从不用在展示字号，始终压缩，字重 500 保可读。

色板有五个命名色，但三个功能角色。**Blue**（`{colors.blue}` — #2C2CDC）是主结构色：高强调表面的背景、内容分割的描边、非蓝底上的文字色。**Orange**（`{colors.orange}` — #F2A03A）是能量色：统计数字、列序号、蓝表面上的强调文字。**Red**（`{colors.red}` — #E83A2A）是纵深色——从不以表面填色出现，只作为叠层 text-shadow 或 box-shadow 的第一层。Blue-deep 和 red-deep 是双叠阴影系统里的外层阴影。

招牌纵深手法是**叠偏移 text-shadow**：橙字在 6–12px 处投下红影，红影再在 12–24px 处投下 red-deep 影。这做出三层准 3D 凸版效果，是系统最可辨认的特征。交互元素上的 box-shadow 镜像同一处理：`6px 6px 0 {colors.red}`。

**关键特征：**
- 纸色画布（`{colors.paper}` — #F5F2EA），每一页通过 CSS 伪元素叠颗粒。
- 双叠 text-shadow：`Npx Npx 0 {colors.red}, 2Npx 2Npx 0 {colors.red-deep}`。阴影尺寸随字号缩放。
- 所有展示与结构字体用 Alfa Slab One——全大写，行高 0.82–1.04，字距 0.005em。
- Red（`{colors.red}`）专门当阴影色——从不当表面背景。
- 所有主要结构分割（顶栏、章节头、列分隔、内缩画框）用粗 6px ink 描边。
- 所有页面上 DM Mono 标签精确 24px，字距 0.18–0.22em。
- Caveat Brush 出现在 64–96px，始终小写，始终旋转 2–5 度——刻意的粗糙信号。
- 橙色底丝带：锚定在数据密集页底部的横向跑马条。
- 内缩装饰画框（`inset: 48px` 处 6px solid cream），用在蓝底页上。

## 颜色

### 主色板
- **Blue**（`{colors.blue}` — #2C2CDC）：电钴蓝。高强调页和结构元素的主导表面色。用作整页背景、列填色、顶栏背景、奶油/纸表面上的文字、头像填色，以及对照面板的暗侧。
- **Blue Deep**（`{colors.blue-deep}` — #1B1BB0）：更深的蓝。专门用作叠层 text-shadow 的最外层。从不当表面填色。
- **Orange**（`{colors.orange}` — #F2A03A）：暖琥珀。能量强调。用于超大统计数字、列序数、CTA 按钮填色、丝带背景、蓝表面内的强调文字，以及印章元素上 text-shadow 的内层。
- **Orange Deep**（`{colors.orange-deep}` — #E89321）：更深琥珀。留给橙色元素最深的阴影层。不当表面填色。
- **Red**（`{colors.red}` — #E83A2A）：热红。纵深色。专门用在 text-shadow 和 box-shadow 里——大多数展示文字和按钮的第一偏移层。从不以背景或主文字色出现。
- **Red Deep**（`{colors.red-deep}` — #B7281C）：暗红。最大展示元素上双叠 text-shadow 的最外层。从不当表面填色。

### 表面色板
- **Cream**（`{colors.cream}` — #F4E9D6）：暖奶油。用作蓝表面上的文字/描边色（反相模式）、内缩画框描边，以及奶油调页面的整页背景。
- **Paper**（`{colors.paper}` — #F5F2EA）：带暖偏的偏白。默认幻灯片背景——比 #fff 略暖、不那么刺。大多数内容页用这个。
- **Ink**（`{colors.ink}` — #0E0E14）：近黑，带着几乎察觉不到的蓝底。用于所有结构描边、正文、列分割、时间线轨道、KPI 卡片描边。

### 色彩角色摘要
- **蓝色表面** = 高强调、收束、权威瞬间
- **纸/奶油表面** = 内容优先、可读、从属瞬间
- **Orange** = 数字、能量、某一页上最要紧的那件事
- **Red** = 从不是你直接看见的颜色——只是你感觉到的阴影

## 字体

### 字族
三套字体；各自占完全不重叠的声线：

**Alfa Slab One** 是主声线。压缩、厚重的板衬线，竖画强、衬线块状。字重 400（唯一可用字重，天生就粗）严格全大写，覆盖从 28px 印章到 540px 统计数字的每一个展示瞬间。压缩字形意味着即便巨大字号也不觉得宽——它们觉得高、像柱子。略正的字距（0.005em）让大字号下字形不相撞。

**Caveat Brush** 是人的声线。粗糙手写脚本，只在大字号（64–96px）使用，始终小写，始终带小旋转（-2 到 -5 度）。它出现在温暖、过渡或不正式的瞬间——在其他方面结构刚性的文稿里的手写批注。从不用作正文或标签。

**DM Mono** 是记账声线。等宽、24px、宽字距（0.18–0.22em）、全大写。出现在顶栏、页脚、kicker 标签、元数据行、来源引用和丝带文字。它始终是支撑元素——海报底部印的技术规格，不是标题。

**Archivo Narrow** 是正文声线。压缩无衬线，承担所有跑文：柱说明、列表项段落、对照列表项、统计注释。大多数正文用字重 500；较小图注用 400。从不用在展示字号。

### 展示阶梯

| Token | 字号 | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.display-jumbo}` | 540px | Alfa Slab One | 400 | 全出血超大统计数字 |
| `{typography.display-hero}` | 260px | Alfa Slab One | 400 | 主导收束或开场标题 |
| `{typography.display-title}` | 240px | Alfa Slab One | 400 | 主文稿标题 |
| `{typography.display-xl}` | 180px | Alfa Slab One | 400 | 大号列序数 |
| `{typography.display-lg}` | 140px | Alfa Slab One | 400 | 章节标题，主 |
| `{typography.display-md}` | 120px | Alfa Slab One | 400 | 章节标题，次 |
| `{typography.display-sm}` | 108px | Alfa Slab One | 400 | 挨着正文的宣言标题 |
| `{typography.stat-unit}` | 130px | Alfa Slab One | 400 | 统计旁边的上标单位符号 |
| `{typography.quote-mark}` | 300px | Alfa Slab One | 400 | 装饰性超大引号 |
| `{typography.quote-body}` | 78px | Alfa Slab One | 400 | 拉引文正文 |
| `{typography.kpi-value}` | 88px | Alfa Slab One | 400 | KPI 或指标卡片数值 |
| `{typography.subtitle}` | 72px | Alfa Slab One | 400 | 主标题旁的副标题或次标题 |
| `{typography.card-title}` | 54px | Alfa Slab One | 400 | 卡片或列标题 |
| `{typography.section-num}` | 54px | Alfa Slab One | 400 | 章节或条目序数 |
| `{typography.cta}` | 48px | Alfa Slab One | 400 | CTA 按钮标签 |
| `{typography.url}` | 46px | Alfa Slab One | 400 | URL 或联系地址 |
| `{typography.item-title}` | 38px | Alfa Slab One | 400 | 列表项或节点标题 |
| `{typography.toc-entry}` | 36px | Alfa Slab One | 400 | 目录条目标题 |
| `{typography.item-title-sm}` | 30px | Alfa Slab One | 400 | 密列表项标题 |
| `{typography.stamp}` | 28px | Alfa Slab One | 400 | 印章或徽章标签 |

### 手写阶梯

| Token | 字号 | 用途 |
|---|---|---|
| `{typography.script-lg}` | 96px | 醒目手写强调——过渡词、情感开场 |
| `{typography.script-md}` | 64px | 较小手写批注——副标题 callout、次标签 |

两个 script token 始终小写，始终带 -2deg 到 -5deg 的旋转。从不要用不带旋转的 Caveat Brush。

### 正文与标签阶梯

| Token | 字号 | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.body-lg}` | 30px | Archivo Narrow | 500 | 统计注释、主正文段落 |
| `{typography.body-md}` | 28px | Archivo Narrow | 500 | 列正文、导语段落、对照列表 |
| `{typography.body-sm}` | 26px | Archivo Narrow | 500 | 支撑正文段落 |
| `{typography.body-xs}` | 24px | Archivo Narrow | 400 | 密列表项、图注 |
| `{typography.label}` | 24px | DM Mono | 400 | 标准元数据标签（字距 0.18em） |
| `{typography.label-wide}` | 24px | DM Mono | 400 | 页脚线和丝带文字（字距 0.22em） |
| `{typography.label-accent}` | 32px | DM Mono | 600 | 高亮元数据（例如章节计数） |
| `{typography.signoff}` | 26px | DM Mono | 400 | 页脚落款块（字距 0.20em） |

### 排印原则
Alfa Slab One 始终全大写——从不要用句首大写或小写。展示字号下行高很紧：大标题 0.82–0.88，只有多行、挨着正文、会发生行碰撞的文字才用 1.04。0.005em 字距几乎看不见，但能防止 100px+ 时撞字。

叠层 text-shadow 是展示文字的行内样式规则：橙色展示字体始终把 `{colors.red}` 投为第一层阴影。200px 以上，加第二层 `{colors.red-deep}`，偏移加倍。100px 以下，单层 3px–6px `{colors.red}` 偏移就够。

DM Mono 标签无论语境始终 24px。字距随位置变化：顶栏/页脚 0.18em，丝带和页脚线 0.22em，分栏侧标签 0.16em。从不要收紧 DM Mono 的字距——24px 没有字距时读起来像实用字体，不像编辑。

Archivo Narrow 始终字重 400 或 500。从不要用在展示字号。它是支撑声线，不是标题声线。

## 布局

### 画布系统
每一页 1920×1080px。`deck-stage` 自定义元素负责缩放。所有内容绝对定位或用 CSS grid——不滚动。

### 边距系统
- **Slide gutter**（左右 90px）：大多数内容区的标准边缘 padding。
- **Content gutter**（左右 120px）：用于已有结构页头的页内正文——给阅读文字额外呼吸。
- **Topbar height**（90px）：坐在页面绝对顶部的固定高度蓝色顶栏带。
- **Frame inset**（48px）：幻灯片边缘到蓝底页上装饰内缩画框描边的距离。

### 通用 Chrome
系统并不强制每一页都有通用顶栏。存在两种 chrome 模式：

**Topbar 模式** —— 全宽 90px 蓝条锚定在顶部（`position:absolute; top:0; left:0; right:0`）。内含 DM Mono 24px 标签文字，字距 0.18em。带着 6px solid cream 底边。用在高强调蓝底页上。

**章节分隔模式** —— 页头块与下方内容区之间 6px solid ink 水平线。页头块左右 padding 90px；下方内容用 90px padding。没有顶栏——这条线就是分割元素。

两种模式可以在同一页共存，也可以各自独立使用。

## 纵深与抬升

### 叠层 Text-Shadow（主手法）
系统的招牌。展示文字向同一方向（右下）投分层偏移阴影，做出准 3D 凸版效果。按元素尺寸分三档：

| 档 | 第 1 偏移层 | 第 2 偏移层 | 用途 |
|---|---|---|---|
| Small | `3px 3px 0 {colors.red}` | — | 72px 以下的条目 |
| Medium | `5px–6px 5px–6px 0 {colors.red}` | — | 72px–140px 展示 |
| Large | `10px 10px 0 {colors.red}, 20px 20px 0 {colors.red-deep}` | | 140px–260px 展示 |
| Jumbo | `12px 12px 0 {colors.red}, 24px 24px 0 {colors.red-deep}` | | 260px+ 统计数字 |

橙色展示文字是「脸」层；红是「身」；red-deep 是「脚」。错觉是带物理厚度的字形。

### Box-Shadow（次手法）
交互和装饰元素（印章、头像、CTA 按钮、KPI 卡片）用同一偏移逻辑的 box-shadow 形式：`6px 6px 0 {colors.red}` 或 `8px 8px 0 {colors.red}`。这把纵深系统统一起来：文稿里所有元素以同一表观光角、同一方向投阴影。

### 颗粒纹理（气氛纵深）
每一页带着 `.grain::before` 伪元素：两套重叠的径向渐变点网格，间距 3px 和 5px，`mix-blend-mode: multiply`，不透明度 50%。这模拟丝网印半色调纹理，给扁平数字表面一层物理、印刷质感。它不是抬升而是气氛——整份文稿读起来像制作出来的，而不是渲染出来的。

### 扁平元素
DM Mono 标签、ink 章节线、正文和网格线完全扁平。结构分割上没有阴影。

## 形状与处理

### 圆角阶梯
| 值 | 用途 |
|---|---|
| 999px（pill） | 顶栏/页头区的元标签 pills |
| 50%（圆） | 头像元素、时间线里程碑点、圆形印章 |
| 4px | 菱形项目符号伪元素（旋转 45deg 成菱形） |
| 0px | 所有结构元素：列、卡片、顶栏、画框、丝带、KPI 卡片、印章 |

系统几乎全是方的。仅有的软形状是 pill（元数据芯片）、圆（头像、点、收束印章）和菱形项目符号。结构元素的方正强化印刷/构造美学。

### 描边粗细
- **6px solid `{colors.ink}`** —— 主结构描边：章节分割、列分隔、顶栏底边、内缩画框、KPI 卡片描边、CTA 按钮描边。
- **6px solid `{colors.cream}`** —— 蓝表面上的反相结构描边：内缩画框、cream-on-blue 模式下的顶栏分割。
- **5px solid** —— 次结构描边：引文印章、对照列表项处理。
- **4px solid** —— 第三档分割：对照面板侧标签、导语左边。
- **3px solid `{colors.ink}`** —— 细结构线：TOC 行分隔、列标签、统计来源分割、内部时间线。

### 装饰元素

**内缩画框** —— `inset: 48px` 处 6px solid cream 描边，在蓝底页上做出第二道内矩形。强化海报/标语牌美学——设计中的设计。

**橙色丝带** —— `{colors.orange}` 的 60px 底锚条，6px ink 顶边，重复 DM Mono 文字、字距 0.22em。在数据页上充当跑马页脚。

**菱形项目符号** —— 列表项标记，用 `::before` 伪元素：24px × 24px，`background: {colors.red}`，`border-radius: 4px`，`transform: rotate(45deg)`。蓝底列表改用 `{colors.orange}`。形状绝对定位在文字左边 48px。

**圆形印章** —— 200px 圆（`{components.circular-stamp}`），旋转 -9deg，6px 橙描边加 8px 红 box-shadow。充当印章——官僚文件上的物理世界批准标记。

**旋转矩形印章** —— 矩形块旋转 -3deg，5px cream 描边加 6px 红 box-shadow。内含 Alfa Slab One 28px 文字、字距 0.04em。旋转比圆形印章更轻——像略斜贴上的地址标签。

**手写批注** —— Caveat Brush 64–96px，小写，旋转 2–5 度。始终出现在它限定或打断的 Alfa Slab One 标题旁边——从不单独出现。

**列序数** —— 180px Alfa Slab One 橙色数字配 5px 红 text-shadow，下面跟 3px ink 顶边的 DM Mono 标签。这对（大橙数字 + 小等宽标签）是系统标注列或章节的标准方式。

**下划线规则条** —— 14px 高的实心 ink 矩形，宽为容器的 30%，用在宣言标题后面当句号。它比发丝线重——更接近涂黑条。

**颗粒叠层** —— `.grain` class 给每一页加上 `::before` 伪元素纹理。本系统里不能从一页上拿掉它——它对美学是结构性的。

## 该做与不该做

### 该做
- 每一页都叠颗粒（`.grain::before`）。它不是装饰——它是其他一切印上去的表面。
- 所有橙色和奶油展示文字用叠层 text-shadow。没有阴影的 Alfa Slab One 读起来扁，丢掉凸版性格。
- 阴影偏移按字号比例缩放：小字小号偏移，jumbo 字 jumbo 偏移。
- 红专门当阴影色。红一旦以文字色或背景填色出现，纵深系统就塌。
- Caveat Brush 只在大字号（64px+）使用，始终小写，始终略旋转。从不当正文。
- DM Mono 标签精确 24px，字距至少 0.16em。正文字号、正常字距的等宽读起来像代码，不像编辑。
- 主要结构分割用 6px 描边粗细。更细读成 SaaS；更粗看起来像设计失误。
- 蓝底页用内缩画框——把蓝底页区分为「被框住」而不仅仅是填满。
- 在蓝表面上用 `{colors.orange}` 做数字、数值和强调文字。蓝底上仅允许的其他文字组合是 blue-on-orange 或 cream-on-blue。

### 不该做
- 不要把红当背景或主文字色。它是阴影材料，不是表面材料。
- 不要在正文字号或不带旋转时用 Caveat Brush。扁、小的手写读起来凌乱，不是刻意。
- 不要用大小写混排的 Alfa Slab One。全大写锁定对板衬线的权威必不可少。
- 不要软化描边粗细。结构元素上 1px 或 2px 描边会打破印刷品美学。
- 不要圆卡片或容器角。内缩画框和 KPI 卡片严格方形。
- 不要用 Archivo Narrow 做标题。它只是正文和导语脸——没有展示用的视觉重量。
- 不要把 blue-deep 或 red-deep 当表面色。它们是仅阴影值——角色是纵深，不是填色。
- 不要省略列表项上的菱形项目符号旋转。旋转 45deg 的方是菱形；直立的方是盒子——形状信号是手作，不是通用。
- 不要改 DM Mono 字号。24px 是所有等宽标签文字的唯一固定尺寸——为强调加大它会拆系统；唯一例外是 `{typography.label-accent}`（32px，字重 600）。

## 响应式行为

本模板专为 1920×1080 演示显示设计。`deck-stage` 自定义元素通过 CSS transforms 处理视口缩放——1920×1080 画布按比例缩放到任何屏幕尺寸，版式不变。

幻灯片通过 `deck-stage.js` 用键盘或演示翻页器前进。没有 hover 状态，没有交互表单元素，没有响应式断点。

打印和 PDF 导出：96dpi 下，1920×1080 画布映射到 20×11.25 英寸画框。颗粒叠层用 `mix-blend-mode: multiply` —— PDF 导出时混合模式可能被压平；测试打印输出，并考虑为印刷格式关掉颗粒。

## CJK 与国际内容

### 推荐中文搭配

| 角色 | 拉丁字体 | 中文字体 | 字重 |
|---|---|---|---|
| Display / title / quote（Alfa Slab One UPPERCASE） | Alfa Slab One | Noto Serif SC（思源宋体） | 900 |
| Script interrupt（Caveat Brush lowercase rotated） | Caveat Brush | —（没有好对等；见审美说明） | — |
| Body（Archivo Narrow 500） | Archivo Narrow | Noto Sans SC（思源黑体） | 500 |
| Label / mono（DM Mono UPPERCASE tracked） | DM Mono | Noto Sans SC | 400（不要对 CJK 强制等宽） |

### 中英混排策略

策略 A —— 把每个 token 的 `fontFamily` 扩展为拉丁字体后面跟中文字体。Alfa Slab token 变成 `"Alfa Slab One, Noto Serif SC, serif"`；Archivo Narrow token 变成 `"Archivo Narrow, Noto Sans SC, sans-serif"`；DM Mono token 变成 `"DM Mono, Noto Sans SC, monospace"`。拉丁字形用原字体渲染；CJK 自动落到 SC 回退。

### 加载

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Alfa+Slab+One&family=Caveat+Brush&family=Archivo+Narrow:wght@400;500;600;700&family=DM+Mono:wght@300;400;500&family=Noto+Serif+SC:wght@400;500;700;900&family=Noto+Sans+SC:wght@400;500;700;900&display=swap" rel="stylesheet">
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

People's Platform 是建立在三套承重字体上的 WPA 海报系统，**三套都没有干净的中文迁移**。

**Alfa Slab One** 是极端字号（可到 540px）的压缩板衬线全大写。CDN 上没有同等重量和权威的中文板衬线。**Noto Serif SC 字重 900** 是最接近的匹配——它带着板状厚重和结构权威——但读起来更像「文学纪念碑」而不是「抗议标语牌」。接受这种声线偏移：这套系统的中文版更接近遗产时代的公示板（想 大字报 或博物馆导视），而不是 1930 年代 WPA 海报。叠层红 text-shadow 仍然适用，仍然带着系统的凸版纵深招牌。

**Caveat Brush** 是「人的打断」声线——小写、旋转、情感温暖。**这迁不到中文。** 中文毛笔书法（Ma Shan Zheng / 马善政）带着文化和传统重量——读起来仪式、正式，甚至官僚，**不是**拉丁 Caveat 那种随意私人声线。**推荐做法：纯 CJK 页上完全拿掉毛笔瞬间。** 第二选项：即使在中文内容里，也用一个短拉丁词做 Caveat Brush 打断（例如中文标题旁手写 `yes!` 批注）——这保住随意打断的能量，并信号「声线断裂」，而不调用中文书法传统。

**DM Mono** 全大写宽字距标签迁不到 CJK。中文元数据设成 **Noto Sans SC 400**，字距重置为 0，不全大写。纯拉丁标签（URL、日期、版次号）保持 DM Mono。

**Archivo Narrow** 是字重 500 的压缩体。**Noto Sans SC 没有压缩变体。** 用 Noto Sans SC 500 配原来的 Archivo 字号，接受中文正文会比拉丁正文略宽。单色纸画布和颗粒叠层会吸收宽度差。

叠层 text-shadow（橙 → 红 → red-deep）是系统最可辨认的特征。**它完美迁到中文。** 给每一个橙色中文展示标题都加上它，凸版纵深就能熬过脚本切换。蓝-橙-红色板也完全与脚本无关。

菱形项目符号、旋转橡皮章、内缩奶油画框、6px ink 描边——在中文里全部原样工作。

### 已知 CJK 缺口

**Caveat Brush 没有可接受的中文对等。** 在纯 CJK 的 People's Platform 文稿里，「人的打断」声线结构上缺席。两种变通（完全丢掉打断；用手写瞬间的中文里夹拉丁）都是看得见的审美妥协——民粹海报系统被迫进入纯中文时，丢掉三声线之一。中英混排文稿（英文主导带中文点缀，或反过来）是本模板最强的适配。

## 迭代指南

1. 叠阴影是硬不变量——任何橙色或奶油的新展示元素都必须带着它。偏移大致用字号除以 20 得到第一层阴影距离，第二层加倍。
2. 任何蓝底新页都得到内缩画框（6px cream，`inset: 48px`）；如果有页头条，那条用顶栏模式，6px cream 底边。
3. 新列或并排面板遵循 6px ink 分隔惯例。不对称布局（例如 60/40 分割）可以，只要分隔描边仍是 6px。
4. 新 KPI 或数据卡片用 `{components.kpi-card}` 模式：5px ink 描边、纸背景，可选蓝底 alt 变体。里面的数字用 Alfa Slab One 加标准 text-shadow。
5. 新列表项始终用菱形项目符号（24px × 24px，4px 半径，旋转 45deg）。ink 底条目用红，蓝底条目用橙。
6. 如果需要新的装饰印章或徽章，用 Alfa Slab One、`letter-spacing: 0.04em`、`6px 6px 0 {colors.red}` 的 box-shadow，以及轻微旋转（–3 到 –9deg）。圆形印章 round 50%；矩形保持方形。
7. 颗粒叠层是 `section` 元素上的 CSS 伪元素——每一张新页都必须通过 `.grain` class 带上它。
8. 手写（Caveat Brush）文字是打断，不是默认。每页最多用一次，且只在 64px+。

## 已知缺口

- `deck-stage.js` 是此处未文档化的外部脚本依赖。幻灯片导航和缩放完全由它处理。
- 数据页上的橙色丝带用静态重复文字实现——没有 JavaScript 跑马动画。1920px 宽时文字自然折行；更长的字符串请手工复制文字。
- 颗粒叠层用 `mix-blend-mode: multiply`。这需要半透明背景或带可见填色的父级才能做出纹理效果——在纯白或纯黑表面上效果可能看不见。
- 演讲者备注作为模板里的 `<script type="application/json">` 块嵌入——这些数据是呈现性的，不是设计系统的一部分，也没有被捕获进这些 token。
- Archivo Narrow 作为 web 字体加载。它有宽的系统回退（`system-ui, sans-serif`），但系统字体栈回退的压缩宽度会与 Archivo Narrow 差很多，可能在紧网格配置下撑破版式。
- 引文上的 `text-wrap: pretty` 属性是现代 CSS 特性，浏览器支持有限——在较旧的导出环境里可能不生效。
