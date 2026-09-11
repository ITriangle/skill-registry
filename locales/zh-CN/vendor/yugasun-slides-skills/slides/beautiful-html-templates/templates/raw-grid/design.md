---
version: alpha
name: Raw Grid
description: A neobrutalist presentation system where 3px solid black borders ARE the layout. Display type runs in the native system sans-serif stack (Segoe UI / system-ui) at weight 900 in strict uppercase — no web fonts loaded. The palette is white canvas + black structure + two muted pastel accents (blush pink #F2D4CF and sage green #E5EDD6) + a neutral gray. Depth comes from hard offset shadows in solid black at 4px and 6px — never blurred, never colored. The aesthetic borrows from brutalist editorial web design and zine layout: borders meet without gaps, contrast is high but warmed by the pastel accents, and large numerals sit at very low opacity behind content as decorative wallpaper. The effect is sharp, system-native, and unmistakably digital — closer to a Notion-meets-protest-poster than a polished pitch deck.

colors:
  black: "#0A0A0A"
  white: "#FFFFFF"
  pink: "#F2D4CF"
  green: "#E5EDD6"
  gray: "#F5F5F5"
  darkgray: "#333333"

borders:
  primary: "3px solid {colors.black}"

shadows:
  default: "6px 6px 0 {colors.black}"
  small: "4px 4px 0 {colors.black}"

typography:
  display:
    fontFamily: "Segoe UI, system-ui, -apple-system, Helvetica, Arial, sans-serif"
    fontSize: "clamp(48px, 7vw, 96px)"
    fontWeight: 900
    lineHeight: 1.05
    letterSpacing: -0.02em
    textTransform: uppercase
  headline:
    fontFamily: "Segoe UI, system-ui, -apple-system, Helvetica, Arial, sans-serif"
    fontSize: "clamp(32px, 4.5vw, 64px)"
    fontWeight: 900
    lineHeight: 1.1
    letterSpacing: -0.01em
    textTransform: uppercase
  title:
    fontFamily: "Segoe UI, system-ui, -apple-system, Helvetica, Arial, sans-serif"
    fontSize: "clamp(24px, 2.5vw, 36px)"
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: 0.01em
    textTransform: uppercase
  subtitle:
    fontFamily: "Segoe UI, system-ui, -apple-system, Helvetica, Arial, sans-serif"
    fontSize: "clamp(16px, 1.4vw, 22px)"
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.04em
    textTransform: uppercase
  body:
    fontFamily: "Segoe UI, system-ui, -apple-system, Helvetica, Arial, sans-serif"
    fontSize: "clamp(16px, 1.3vw, 20px)"
    fontWeight: 500
    lineHeight: 1.6
    letterSpacing: 0
  caption:
    fontFamily: "Segoe UI, system-ui, -apple-system, Helvetica, Arial, sans-serif"
    fontSize: "clamp(11px, 1vw, 13px)"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  number:
    fontFamily: "Segoe UI, system-ui, -apple-system, Helvetica, Arial, sans-serif"
    fontSize: "clamp(64px, 8vw, 120px)"
    fontWeight: 900
    lineHeight: 1.0
    letterSpacing: -0.04em
  number-md:
    fontFamily: "Segoe UI, system-ui, -apple-system, Helvetica, Arial, sans-serif"
    fontSize: "clamp(36px, 4vw, 56px)"
    fontWeight: 900
    lineHeight: 1.0
    letterSpacing: -0.02em
  number-lg:
    fontFamily: "Segoe UI, system-ui, -apple-system, Helvetica, Arial, sans-serif"
    fontSize: "clamp(48px, 6vw, 80px)"
    fontWeight: 900
    lineHeight: 1.0
    letterSpacing: -0.02em
  label-text:
    fontFamily: "Segoe UI, system-ui, -apple-system, Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 800
    lineHeight: 1.0
    letterSpacing: 0.08em
    textTransform: uppercase

spacing:
  pad-lg: "clamp(32px, 4vw, 64px)"
  pad-md: "clamp(20px, 2.5vw, 40px)"
  pad-sm: "clamp(12px, 1.5vw, 20px)"
  gap-lg: "clamp(24px, 3vw, 48px)"
  gap-md: "clamp(16px, 2vw, 32px)"
  gap-sm: "clamp(8px, 1vw, 16px)"

canvas:
  width: 100vw
  height: 100vh

components:
  label:
    background: "{colors.black}"
    color: "{colors.white}"
    padding: "6px 14px"
    fontSize: 11px
    fontWeight: 800
    letterSpacing: 0.08em
    textTransform: uppercase
  line-h:
    width: 60px
    height: 4px
    background: "{colors.black}"
  line-v:
    width: 4px
    height: 60px
    background: "{colors.black}"
  line-full:
    width: "100%"
    height: 4px
    background: "{colors.black}"
  arrow-prefix:
    content: "→\\00a0"
    description: "Inline right-arrow glyph (U+2192) followed by a non-breaking space. Prepended via ::before on CTAs and interactive list items."
  icon-box:
    width: 48px
    height: 48px
    border: "3px solid {colors.black}"
    background: "{colors.white}"
    fontSize: "18px–20px"
    fontWeight: 900
    description: "Square white box with 3px black border, used for logos and feature icons. Contains 1–3 character glyph or Roman numeral."
  bar-track:
    width: "100%"
    height: 32px
    border: "3px solid {colors.black}"
    background: "{colors.white}"
  bar-fill-pink:
    background: "{colors.pink}"
  bar-fill-green:
    background: "{colors.green}"
  bar-fill-black:
    background: "{colors.black}"
    color: "{colors.white}"
  stat-box:
    border: "3px solid {colors.black}"
    padding: "clamp(16px, 2vw, 28px)"
    background: "{colors.white}"
  card:
    padding: "clamp(24px, 3vw, 48px)"
    border: "3px solid {colors.black}"
    description: "Generic content card. Background may be white, pink, green, or gray."
  decorative-numeral:
    fontWeight: 900
    fontSize: "clamp(40px, 5vw, 72px)"
    lineHeight: 1.0
    opacity: 0.2–0.35
    description: "Oversized numeral placed inside a card at very low opacity as decorative wallpaper behind the actual content."
  decorative-quote-mark:
    fontSize: "clamp(80px, 12vw, 160px)"
    fontWeight: 900
    opacity: 0.15
    description: "Oversized opening quotation mark placed absolutely at the top-left of a quote region at very low opacity."
  connector-node:
    width: 32px
    height: 32px
    border: "3px solid {colors.black}"
    background: "{colors.black}"
    color: "{colors.white}"
    fontSize: 16px
    fontWeight: 900
    description: "Small black square with white arrow glyph, used as a connector between sequential items in a horizontal flow."
  legend-swatch:
    width: 16px
    height: 16px
    border: "3px solid {colors.black}"
  donut-stroke-width: 24
  donut-track-stroke-width: 1.5
  table-cell:
    border: "3px solid {colors.black}"
    padding: "clamp(12px, 1.5vw, 20px)"
    fontWeight: 600
  table-header:
    background: "{colors.black}"
    color: "{colors.white}"
    fontWeight: 800
    letterSpacing: 0.06em
    textTransform: uppercase
  table-zebra-row:
    background: "{colors.gray}"
  hover-highlight:
    background: "{colors.green}"
    transition: "background 0.15s"
---

## 概览

Raw Grid 是一套**新粗野主义演示系统**，建立在单一结构前提上：**3px 实心黑边框就是版式**。区域之间没有外边距，单元格之间没有间隙，没有圆角，没有渐变。两个区域相遇时，一条 3px 黑线把它们分开——这条线就是整套网格系统。

字体选择刻意不做装饰。系统使用**原生系统无衬线栈**（`Segoe UI, system-ui, -apple-system, Helvetica, Arial, sans-serif`）——不加载 Google Fonts，不加载网页字体，没有授权问题。展示级文字用字重 900、严格大写，并带紧凑的负字距。正文字重 500、句首大写。粗重大写展示字与轻量句首大写正文之间的对比，就是这套系统的排版节奏。选用系统字体本身就是审美表态：读起来像「这是软件，不是印刷品」——对应大多数粗野主义系统的印刷 zine 审美，它是数字原生的对位。

色板有六个 token，实际承担四种角色。**白**（`{colors.white}`）是画布。**黑**（`{colors.black}`）是结构：边框、标题、正文、标签填充、阴影颜色。**粉**（`{colors.pink}`——低饱和腮红粉 #F2D4CF）和**绿**（`{colors.green}`——鼠尾草绿 #E5EDD6）是强调色块——暖与冷的对位，从不用于文字，始终用作区域填充。**灰**（`{colors.gray}`——#F5F5F5）是中性填充，用于表格斑马纹和第三层表面。这些粉彩色足够浅，黑字叠在上面仍完全可读，这一点很关键：系统从不在强调色块上反转文字颜色。

纵深完全来自**硬偏移阴影**，偏移 6px 与 4px，纯黑、零模糊。不用 `rgba(...)`，不用 `0 4px 12px`。要么是硬边纯黑阴影，要么完全没有阴影。

**密度哲学：中等。** 系统用边框把区域干净地隔开，但每个区域内的内容克制——通常是一个展示元素配一段正文，或一个数据配一条说明。边框很响（3px 实心黑，毫不妥协）；区域内的内容很静。这套系统里「坏掉」的幻灯片，是某个区域*空着*或*塞得过满*；正确密度是每个带边框区域放一个实质元素。

**关键特征：**
- 白（`{colors.white}`）画布，3px 实心黑（`{colors.black}`）边框划分每个区域。单元格之间无间隙——边框边对边相接。
- 系统无衬线，展示级一律字重 900 大写；正文一律字重 500、句首大写。
- 硬偏移阴影 6px 与 4px，纯黑，永不模糊。
- 两种低饱和粉彩色强调表面——腮红粉与鼠尾草绿——用作区域填充，从不作为文字色。
- 标志性的黑胶囊 `label` 组件（`{components.label}`）——小黑矩形里的白色大写文字——作为通用章节标签出现。
- 超大装饰数字以 0.15–0.35 不透明度垫在内容后面当墙纸。
- CTA 与可交互列表项通过 `::before` 前置箭头字形（→ 加不换行空格）。
- 系统中任何地方都没有圆角。每种形状都是严格的矩形、正方形或圆形。
- 系统不加载任何外部字体；只要浏览器有默认字体，渲染就一致。

## 颜色

### 色板
- **黑**（`{colors.black}` — #0A0A0A）：结构色。所有边框、所有标题文字、所有正文、所有标签填充、所有阴影值。比纯 #000000 略软，但在任何合理尺寸下都读作黑色。
- **白**（`{colors.white}` — #FFFFFF）：画布。用作默认幻灯片背景、默认卡片背景，以及黑色表面上的文字色（标签、表头、深色数据块）。
- **粉**（`{colors.pink}` — #F2D4CF）：低饱和腮红。暖强调表面——区域背景、条形填充、数据块填充。粉彩饱和度让黑字无需反转即可完全可读。
- **绿**（`{colors.green}` — #E5EDD6）：鼠尾草绿。冷强调表面——区域背景、条形填充、悬停高亮、交替卡片。始终与粉作为强调系统的两半成对出现；同一构图里很少单独出现。
- **灰**（`{colors.gray}` — #F5F5F5）：偏白中性色。用于表格斑马纹行，以及需要与白面分离、又不想用彩色强调的第三层卡片背景。
- **深灰**（`{colors.darkgray}` — #333333）：预留的第三层文字色，存在于 token 系统中但使用很少。可用于需要比纯黑更柔的弱化文字。

### 默认值
- **默认表面背景**：`{colors.white}`。
- **默认标题颜色**：`{colors.black}`——始终如此。标题从不出现粉、绿或灰；只在浅色表面上用黑，或在黑色表面上用白。
- **默认正文颜色**：`{colors.black}`。
- **默认边框颜色**：`{colors.black}`——始终如此。
- **暖色区域默认强调表面**：`{colors.pink}`。
- **冷色区域默认强调表面**：`{colors.green}`。
- **第三层区域默认中性填充**：`{colors.gray}`。
- **`{colors.black}` 表面上的默认文字色**：`{colors.white}`——系统中唯一的颜色反转。

强调表面（粉、绿）可以互换——两者都没有固定语义角色（例如粉不是「警告」，绿不是「成功」）。用哪种颜色对比更服务构图就用哪种。两个强调区域相邻时，用粉配绿做暖/冷平衡，而不是同色加倍。

## 字体

### 字族
整套系统跑在**原生系统无衬线栈**上：`Segoe UI, system-ui, -apple-system, Helvetica, Arial, sans-serif`。不加载网页字体。这是刻意的——数字原生审美依赖于在用户实际系统字体里渲染，而不是下载来的展示字体。结果只在气质上一致，字母形状并不完全相同：macOS 渲染会与 Windows 略有不同，这种差异在系统容差之内可以接受。

字重轴是全部表达工具。展示字用字重 900（最重），标题用 800，副标题用 700，正文用 500，没有斜体变体，没有替代字面。字重 900 大写与字重 500 句首大写之间的对比，是系统的主要排版节奏。

### 展示与数字层级

| Token | 尺寸（clamp） | 字重 | 字距 | 用途 |
|---|---|---|---|---|
| `{typography.number}` | 64–120px | 900 | -0.04em | 主视觉数字指标 |
| `{typography.display}` | 48–96px | 900 | -0.02em | 章节开场或封面展示 |
| `{typography.number-lg}` | 48–80px | 900 | -0.02em | 大型装饰或突出数字 |
| `{typography.headline}` | 32–64px | 900 | -0.01em | 主章节标题 |
| `{typography.number-md}` | 36–56px | 900 | -0.02em | 数据块或指标数字 |
| `{typography.title}` | 24–36px | 800 | 0.01em | 区域或章节小标题 |
| `{typography.subtitle}` | 16–22px | 700 | 0.04em | 副标题、区域内标题 |
| `{typography.body}` | 16–20px | 500 | 0 | 段落正文 |
| `{typography.caption}` | 11–13px | 700 | 0.08em | 说明、细字、脚注 |
| `{typography.label-text}` | 11px | 800 | 0.08em | 黑色标签胶囊内的文字 |

### 默认值
- **主章节标题默认尺寸**：`{typography.headline}`（32–64px clamp）。
- **封面或开场展示默认尺寸**：`{typography.display}`（48–96px clamp）。
- **段落正文默认尺寸**：`{typography.body}`（16–20px clamp）。
- **行内标签或说明默认尺寸**：`{typography.caption}`（11–13px clamp）。
- **任何展示元素默认字重**：900。
- **任何正文元素默认字重**：500。
- **主视觉数字默认尺寸**：`{typography.number}`（64–120px clamp）。

拿不准时，幻灯片的主文字时刻用 `{typography.headline}`，不要用 `{typography.title}`（后者是幻灯片内部区域级标题）。

### 标志性处理
只要用到对应元素类型，这些处理就是**不可省略的**：

- **每一个 display、headline、title、subtitle 元素都是大写。** 本系统不存在句首大写的展示字。只要文字是 `{typography.display}`、`{typography.headline}`、`{typography.title}` 或 `{typography.subtitle}`，就必须大写。
- **每一个正文元素都是句首大写。** 永远不要把 `{typography.body}` 设成全大写——展示字与正文之间的大写/句首大写对比，就是系统的排版信号。
- **每一个展示元素都使用负字距。** Display（–0.02em）、headline（–0.01em）、number（–0.04em）。默认字距的展示字读起来像没处理过；负字距才给字体带来压缩的粗野主义密度。
- **每一个 caption 和 label 至少使用 0.06em 正字距。** 没有字距的 caption 和 label 字形读起来像代码，而不是编辑设计。
- **所有数字都用字重 900 加负字距。** 即使是较小的指标数字（36–56px）也遵循展示级字重惯例。

### 排版原则
字重 900 + 大写 + 负字距的组合是系统的主要「声音」。改动这三项中的任何一项（例如字重 700 大写，或字重 900 句首大写）都会读成另一套设计系统。字重 800 留给 `{typography.title}` 和标签；字重 700 给 `{typography.subtitle}` 和 `{typography.caption}`；字重 500 给正文。不要用中间字重（400、600）——字重阶梯是固定的。

系统中任何地方都不使用斜体。不使用下划线。唯一的强调机制是字重对比。

## 布局

### 画布系统
系统目标是 `100vw × 100vh`——铺满视口。每个 `.slide` 绝对定位填满视口，同一时间只有一张幻灯片是 `display: flex`（幻灯片导航由 JS 驱动：键盘方向键、空格、触摸滑动）。所有尺寸使用 CSS `clamp()`，布局在最小与最大值之间流体缩放，无需断点。

### 内边距与间距层级
| Token | 范围 | 用途 |
|---|---|---|
| `{spacing.pad-lg}` | 32–64px | 幻灯片区域外边距、整区单元格 |
| `{spacing.pad-md}` | 20–40px | 页头条带、次级区域 |
| `{spacing.pad-sm}` | 12–20px | 紧凑区域、表格单元格 |
| `{spacing.gap-lg}` | 24–48px | 大 flex/grid 间距 |
| `{spacing.gap-md}` | 16–32px | 标准 flex/grid 间距 |
| `{spacing.gap-sm}` | 8–16px | 紧凑行内间距 |

### 边框即布局原则
决定性的结构模式：**区域用 3px 实心黑边框分隔，而不是用间隙。** 当幻灯片分成两列网格时，两列共享一条 3px 黑色竖边框，单元格直接贴上这条边框——没有 `gap` 属性，没有 margin。当页头条带位于内容区上方时，一条 3px 黑色横线把它们分开，两侧区域都贴着这条线。这是系统最鲜明的结构选择。

区域内的内边距（`{spacing.pad-lg}` 等）提供单元格内部的呼吸空间。单元格之间不存在间隙。

## 纵深与层级

### 硬偏移阴影（唯一手法）
系统恰好使用两个阴影值：
- **`{shadows.default}`** = `6px 6px 0 {colors.black}`——抬升元素的标准硬偏移阴影（大卡片、主 callout）。
- **`{shadows.small}`** = `4px 4px 0 {colors.black}`——较小抬升元素的轻偏移。

两种阴影都是**纯黑、零模糊、固定右下偏移**。没有按颜色变化的阴影，没有模糊投影，没有柔和抬升。元素要么投下硬偏移阴影，要么完全没有阴影。

### 边框纵深
系统大部分表面上的「纵深」其实来自边框，而不是阴影。彩色背景上带 3px 实心黑边框的卡片，无论是否带阴影都读作被抬起。只有当元素需要感觉「从下方表面掀起来」时才用阴影——通常是叠在或浮在所属区域之上的卡片。

### 装饰墙纸（氛围纵深）
标志性处理：超大数字放在卡片内、极低不透明度（最大引号 0.15，步骤数字 0.20，卡片序数 0.35），垫在实际内容后面当装饰墙纸。数字填满区域左上或上半，真正的标题以全不透明度叠在前面。这形成「内容叠在装饰上」的分层效果，而不用任何 z-index 花招。

## 形状与处理

### 圆角
| 值 | 用途 |
|---|---|
| 0px | 除圆形以外的一切 |
| 50%（圆形） | 仅甜甜圈图形状 |

系统**没有圆角**。卡片、按钮、标签、图标盒、数据块、表格单元格、图片框——全部是严格矩形或正方形。唯一的圆形是 SVG 甜甜圈图，几何上必须是圆。

### 边框粗细
- **3px solid `{colors.black}`**——通用边框。用于每一处结构划分：区域分隔、卡片轮廓、表格单元格、图标盒、连接节点、色标、条形轨道、数据块边框。从不更细，从不更粗，从不上色，从不虚线。
- **4px solid `{colors.black}`**——仅用于 `{components.line-h}` 和 `{components.line-v}` 装饰短线元素（60px 短线）。
- **4px solid `{colors.white}`**——仅用于黑色图片区域内的图片占位框（白底黑面语境下的反转边框处理）。
- **1.5px stroke**——仅用于 SVG 甜甜圈图内圈描边，不透明度 0.1（几乎看不见的内环）。

### 装饰元素类型

**黑色标签胶囊**——小黑矩形，内含白色大写文字，11px / 字重 800 / 0.08em 字距，内边距 6px × 14px。系统的通用章节标签、财年标记或状态芯片。CTA 变体可前置 `{components.arrow-prefix}`。

**水平短线**——60px × 4px 实心黑矩形（`{components.line-h}`），用作行内视觉分隔，或标签旁的强调。在编辑版式里充当「章节断点」标记。

**图标盒**——48px × 48px 白方块，3px 黑边框，内含 1–3 个字符的字形（首字母、罗马数字、单字母），18–20px、字重 900。用作标志标记和功能图标。

**装饰超大数字**——大数字字符（通常是步骤号或章节序数），字重 900，放在卡片内，不透明度 0.15–0.35。作为墙纸坐在卡片实际内容后面或上面。

**连接节点**——32px × 32px 实心黑方块，内含白色箭头字形，字重 900。绝对定位在水平流程的连续项目之间（例如时间线步骤之间）。充当阶段之间的视觉「→」。

**条形轨道**——32px 高的水平矩形，3px 黑边框、白色内部。填充（粉、绿或黑）是子 `div`，其 `width` 百分比代表数据值，数值标签印在填充内，12px、字重 800。黑色条形反转文字颜色（白）。

**数据块**——带边框的卡片（`{components.stat-box}`），内含大数字（`{typography.number-md}`）和其下小说明（`{typography.caption}`）。背景可以是白、粉、绿、灰或黑（配合相应文字反转）。

**带箭头前缀的文字**——文字元素（CTA、可交互列表行）通过 `::before` 前置 `→`（U+2192）加不换行空格，表示动作或导航。这是系统的交互信号。

**甜甜圈图**——多段 SVG 环，描边宽 24px，内部分隔环 1.5px、不透明度 0.1。分段使用色板颜色（黑、粉、绿），中心放数值 + 标签对。

## 该做与不该做

### 该做
- 每一处结构划分都用 3px 实心黑边框。边框粗细就是系统身份——更细读起来像普通 web 应用，更粗读起来像坏了。
- 标题颜色默认设为 `{colors.black}`。本系统不存在粉、绿或灰的标题。
- 两个强调表面一起出现时，把粉和绿当对立面配对——暖配冷，从不两块粉或两块绿相邻。
- 每一个展示元素同时使用大写 + 负字距 + 字重 900。这三项特质不可拆分——单独使用会丢掉粗野主义性格。
- 用黑色标签胶囊（`{components.label}`）作为通用章节标签。它是系统最鲜明的小组件，应当慷慨出现。
- 每个 CTA 和可交互列表行都用箭头前缀（`→ + nbsp`）。它是系统的交互信号。
- 阴影渲染为 `6px 6px 0 {colors.black}` 或 `4px 4px 0 {colors.black}`。只有两个阴影值——选一个。
- 在有数字身份的卡片（步骤号、序数、引号）里，把超大装饰数字以 0.15–0.35 不透明度垫在内容后面。墙纸数字模式是系统签名。
- 让边框直接相接。两个区域在 3px 黑线处相遇是正确的；它们之间有间隙是错的。
- 正文用字重 500、句首大写；展示字用字重 900、大写。两者之间的对比就是排版节奏。

### 不该做
- 不要加载任何网页字体。系统跑在原生无衬线栈上——Segoe UI / system-ui / Helvetica。加入 Google Fonts 会破坏数字原生审美。
- 不要给任何角加圆。卡片、按钮、标签、图标盒——全部是严格矩形。圆角只允许用于圆形（甜甜圈图）。
- 不要使用模糊阴影。`0 4px 12px rgba(0,0,0,0.1)` 在这里不存在。要么是 4px/6px 硬纯黑偏移，要么没有。
- 不要给边框上色。所有结构边框都是黑。彩色边框会破坏系统。
- 不要使用中间字重（400、600）。字重阶梯固定为 500 / 700 / 800 / 900。
- 不要使用斜体或下划线。唯一的强调机制是字重对比。
- 不要把展示级字重的文字设成句首大写。display、headline、title、subtitle 和 caption token 上的大写不可商量。
- 不要引入第三种强调表面颜色。粉和绿是仅有的强调表面。加一张黄或蓝卡片会破坏暖/冷配对系统。
- 不要在边框分隔的区域之间使用 gap 属性。区域在边框处相遇；它们之间没有外边距。
- 不要在粉、绿或灰表面上反转文字颜色。这些粉彩色就是为黑字叠在上面设计的——反转处理只适用于 `{colors.black}` 表面。

## 响应式行为

与本库大多数模板不同，Raw Grid **从设计上就是视口流体的**。整套系统用 CSS `clamp()` 控制尺寸，没有固定画布尺寸。每一个 `font-size`、`padding`、`gap` 和 `width` 值都根据视口宽度在最小与最大值之间线性缩放。同一构图在 1280×720 笔记本、1920×1080 显示器和 2560×1440 屏幕上无需媒体查询即可正确渲染。

### 缩放行为
- 展示标题从最小视口的 48px 缩放到最大视口的 96px。
- 正文从 16px 缩放到 20px。
- `{spacing.pad-lg}` 上的内边距从 32px 缩放到 64px。
- 边框、标签胶囊内边距和阴影偏移是固定的（3px、6px 14px、6px 6px）——它们不缩放，因此在更大视口上边框会显得比例更细。

### 演示行为
- 用 `ArrowDown`、`ArrowRight` 或 `Space` 前进。
- 用 `ArrowUp` 或 `ArrowLeft` 后退。
- `Home` 跳到第一张，`End` 跳到最后一张。
- 移动端触摸滑动（垂直）前进/后退。
- 当前幻灯片带 `.active` 类；非当前幻灯片是 `display: none`。

### 打印行为
`@media print` 规则把所有幻灯片设为 `display: flex`，并带 `page-break-after: always`——打印整套幻灯片会得到按页一张的 PDF。

### 悬停状态
系统独特地把交互悬停状态写进设计——列表项和表格行悬停时通过 0.15s 过渡高亮为 `{colors.green}`。这对演示系统来说不寻常；它反映了 Raw Grid 作为演示与产品 mockup 的双重身份。

## CJK 与国际内容

### 推荐中文搭配

| 角色 | 拉丁 | 中文 | 字重映射 |
|---|---|---|---|
| Display / Headline / Title / Subtitle | Segoe UI / system-ui（900） | **思源黑体 Noto Sans SC** | 900 |
| Body / Caption / Label | Segoe UI / system-ui（500–800） | **思源黑体 Noto Sans SC** | 500（正文），700–800（说明 / 标签） |

### 混排策略

**策略 A——整套系统只用一个 CJK 字族。** Raw Grid 刻意是单字族系统：每个字重（900 / 800 / 700 / 500）都来自同一套拉丁栈。用单一 CJK 字族——Noto Sans SC——镜像这一点，能保住系统最核心的属性：排版均一。因为拉丁栈是 `system-ui`（Windows 上是 Segoe UI，macOS 上是 San Francisco），配一套高质量 CJK 网页字体，能让渲染尽量贴近数字原生审美所要求的「系统原生」。用两套 CJK 字族会撕裂新粗野主义的单一种族。

### 加载

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@500;700;800;900&display=swap" rel="stylesheet">
```

然后在每个 font-family token 的拉丁栈后面追加 `'Noto Sans SC'`：
```css
font-family: 'Segoe UI', system-ui, -apple-system, Helvetica, Arial, 'Noto Sans SC', sans-serif;
```

### 通用 CJK 调整

- 行高：正文 1.75–1.85，展示级 1.15–1.25
- 字距：CJK 上为 0
- 文本变换：CJK 不大写
- 全角标点
- 展示级标题不加句号
- 盘古之白：`使用 Claude` 而不是 `使用Claude`
- 一句一字体

### 本系统审美说明

- **定义拉丁展示声音的负字距不能平移。** 每个 CJK 展示元素都设 `letter-spacing: 0`。Noto Sans SC 字重 900 已经读作密实粗野；负字距会把字形挤在一起，读起来像渲染 bug，而不是设计选择。
- **大写就是整个拉丁展示声音——中文里不存在。** 补偿方式是更用力地依靠字重对比（展示 900 vs 正文 500），以及标签胶囊的白底黑面反转。粗野主义密度来自字重阶梯，而不是大小写。
- **黑色标签胶囊（`{components.label}`）翻译后效果很好。** 2–4 个汉字的标签（品牌、信号源、第四季度）用 Noto Sans SC 800，读起来更紧凑，甚至可能比英文对应物更醒目。
- **0.15–0.35 不透明度的装饰超大数字应保持拉丁数字**（阿拉伯数字在这套系统里看起来正确；全角中文数字零一二三带不出同样的墙纸数字信号）。
- **箭头前缀（`→`）在 CJK 语境下渲染相同**，对两种语言都是正确的交互信号。

### 已知 CJK 缺口

Raw Grid 的全部审美论点是「这是用户实际的系统字体，不是下载来的展示字体。」加载 Noto Sans SC 从技术上违反了这种纯粹——但没有可接受的替代。macOS 自带 PingFang SC，Windows 自带微软雅黑，但两者在「900」字重上渲染明显不同，而数字原生审美依赖于字重 900 读起来一致。Noto Sans SC 是对网页字体最小可接受的让步；把它当作「不加载网页字体」规则的唯一例外，且仅用于 CJK 内容。

## 迭代指南

1. 任何新结构区域都用 3px 实心黑边框与相邻区域分开。永远不要在区域之间用 gap 或 margin——边框就是分隔。
2. 任何新卡片或面板继承带边框矩形模式：3px 实心黑边框、直角、内边距来自 `{spacing.pad-*}` 层级、背景来自色板（白、粉、绿、灰或黑）。
3. 任何新标题使用 `{typography.headline}`（封面级时刻用 `{typography.display}`），颜色 `{colors.black}`，大写。主时刻不要伸手去拿 `{typography.title}`——那是副标题。
4. 任何新标签或芯片使用 `{components.label}` 模式：黑背景、白色大写文字 11px / 字重 800 / 0.08em。
5. 任何新数字遵循字重 900 + 负字距惯例。数据块用 `{typography.number-md}`；主视觉指标用 `{typography.number}`。
6. 任何新强调表面按暖/冷需要选粉或绿。不要引入第三种颜色。
7. 任何新 CTA 或交互元素加上 `→` 箭头前缀；若被抬升，再加 `6px 6px 0 {colors.black}` 阴影。
8. 如果卡片需要「性格」元素，加一个 0.15–0.35 不透明度的超大装饰数字，而不是图形或图标。墙纸数字处理是系统的签名装饰动作。
9. 表格遵循带边框单元格 + 斑马纹 + 黑表头模式。不要改样式——粗野主义表格审美是系统身份的一部分。

## 已知缺口

- `--darkgray`（#333333）CSS 变量已定义，但没有任何规则真正使用。它可作为预留的第三层文字色，但源码中未部署。
- 系统不加载外部字体——渲染出的字母形状会因操作系统而异。macOS 把 system-ui 渲染成 San Francisco，Windows 渲染成 Segoe UI，Linux 渲染成配置好的无衬线字体。这种视觉不一致是设计如此，但值得注明。
- 悬停状态（列表项 → 绿，表格行 → 绿）是交互式网页行为，在打印或静态导出中没有对应物。把它们当额外交互，而不是核心设计系统。
- 幻灯片导航 JavaScript 内嵌在页面里——处理键盘、触摸和 active-class 系统。任何新幻灯片必须遵循 `<div class="slide sN">` 模式，并尊重 `current` 索引。
- SVG 甜甜圈图使用硬编码的 `stroke-dasharray` 值，必须根据分段百分比和图表 80px 半径周长（约 502.4）手动计算。没有数据绑定层。
- 图文配对区域上的图片占位只是一个 4px 白边框 div，文字是「[ Image Placeholder ]」——真正插入图片需要把占位 div 换成 `<img>`，并把父级背景对齐到图片的负空间。
- `.s5-image-placeholder` 包含单词 "Cohots"（原文如此），源码里似乎是 "Cohorts" 的拼写错误。复用内容时请标出。
