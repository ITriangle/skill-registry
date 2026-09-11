---
version: alpha
name: Cartesian
description: A quiet, museum-catalog editorial system built on Playfair Display serif headlines, Inter sans body, and a five-tone warm-stone palette. The aesthetic is "consulting deck meets architectural monograph" — minimal geometric line decorations (thin circles, dashed arcs, vertical and horizontal hairlines) drift behind content, suggesting drafting paper and compass work. Every divider is a single 1px line in a muted taupe; nothing is bold, nothing is loud. The cultural reference is Massimo Vignelli's editorial work, the Cooper Hewitt catalog, and pencil-and-tracing-paper urban planning documents.

colors:
  bg-primary: "#EDE8E0"
  bg-secondary: "#E2DBD1"
  text-primary: "#1A1A1A"
  text-secondary: "#5A5A5A"
  accent: "#8A8178"
  line: "#B8B0A4"
  white-overlay: "rgba(255, 255, 255, 0.3)"

typography:
  display:
    fontFamily: "Playfair Display, serif"
    fontSize: "clamp(3rem, 6vw, 5.5rem)"
    fontWeight: 400
    lineHeight: 1.1
  h1:
    fontFamily: "Playfair Display, serif"
    fontSize: "clamp(2.5rem, 5vw, 4.5rem)"
    fontWeight: 400
    lineHeight: 1.1
  h2:
    fontFamily: "Playfair Display, serif"
    fontSize: "clamp(1.8rem, 3.5vw, 3rem)"
    fontWeight: 400
    lineHeight: 1.1
  h3:
    fontFamily: "Playfair Display, serif"
    fontSize: "clamp(1.2rem, 2vw, 1.6rem)"
    fontWeight: 400
    lineHeight: 1.1
  stat-figure:
    fontFamily: "Playfair Display, serif"
    fontSize: "2rem"
    fontWeight: 400
    lineHeight: 1
  agenda-numeral:
    fontFamily: "Playfair Display, serif"
    fontSize: "1.5rem"
    fontWeight: 400
    lineHeight: 1
  team-initial:
    fontFamily: "Playfair Display, serif"
    fontSize: "2rem"
    fontWeight: 400
    lineHeight: 1
  quote-mark:
    fontFamily: "Playfair Display, serif"
    fontSize: "5rem"
    fontWeight: 400
    lineHeight: 1
  card-headline:
    fontFamily: "Playfair Display, serif"
    fontSize: "1.3rem"
    fontWeight: 400
    lineHeight: 1.1
  timeline-headline:
    fontFamily: "Playfair Display, serif"
    fontSize: "1.2rem"
    fontWeight: 400
    lineHeight: 1.1
  body:
    fontFamily: "Inter, sans-serif"
    fontSize: "clamp(0.9rem, 1.2vw, 1.1rem)"
    fontWeight: 400
    lineHeight: 1.6
  body-sm:
    fontFamily: "Inter, sans-serif"
    fontSize: "0.9rem"
    fontWeight: 400
    lineHeight: 1.6
  subtitle:
    fontFamily: "Inter, sans-serif"
    fontSize: "clamp(1rem, 1.5vw, 1.3rem)"
    fontWeight: 400
    lineHeight: 1.5
  attribution:
    fontFamily: "Inter, sans-serif"
    fontSize: "0.85rem"
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 2px
    textTransform: uppercase
  label:
    fontFamily: "Inter, sans-serif"
    fontSize: "0.75rem"
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 3px
    textTransform: uppercase
  micro:
    fontFamily: "Inter, sans-serif"
    fontSize: "0.7rem"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 2px
    textTransform: uppercase

spacing:
  pad-y: "4vh"
  pad-x: "4vw"
  gap-xl: "6vw"
  gap-lg: "5vw"
  gap-md: "3vw"
  gap-sm: "2vh"
  card-pad: "4vh 2vw"

canvas:
  width: 100vw
  height: 100vh

components:
  card:
    border: "1px solid {colors.line}"
    padding: "{spacing.card-pad}"
    background: "{colors.white-overlay}"
    description: "Tracing-paper card — 1px taupe outline with semi-transparent white fill that lets the canvas tone bleed through. No radius, no shadow."
  card-icon:
    width: 40px
    height: 40px
    border: "1px solid {colors.line}"
    borderRadius: "50%"
    color: "{colors.accent}"
    fontSize: "1rem"
    description: "Small ringed circle (40px) containing a 1–3 character Roman numeral or letter in accent taupe."
  agenda-row:
    padding: "2vh 0"
    borderBottom: "1px solid {colors.line}"
    description: "List row separated only by a 1px taupe hairline. Numeral at left, label at right."
  timeline-rule:
    height: "1px"
    background: "{colors.line}"
    description: "Single horizontal 1px taupe line connecting timeline items. No nodes, no markers — just the line."
  vertical-line:
    width: "1px"
    height: "100%"
    background: "{colors.line}"
    opacity: 0.3
    description: "Optional decorative vertical hairline anchored at left edge (default 8vw from edge) at low opacity. Provides drafting-paper grid feel."
  horizontal-accent:
    width: "20vw"
    height: "1px"
    background: "{colors.text-primary}"
    description: "Single short ink-black 1px horizontal line used as a strong accent rule. Black, not taupe."
  geo-circle:
    border: "1px solid {colors.line}"
    borderRadius: "50%"
    opacity: 0.5
    description: "Thin solid taupe ring at low opacity, used as decorative geometry behind content."
  geo-arc:
    border: "1px dashed {colors.line}"
    borderRadius: "50%"
    opacity: 0.3
    description: "Thin dashed taupe ring at very low opacity, paired with geo-circle to suggest compass construction."
  geo-decoration:
    border: "1px solid {colors.line}"
    borderRadius: "50%"
    description: "Large decorative ring (30–50vw diameter) anchored to a corner or center. Always pairs with a ::before pseudo-element rendering a smaller dashed ring inside it, suggesting concentric drafting."
  geo-ring:
    width: "50vw"
    height: "50vw"
    border: "1px solid {colors.line}"
    borderRadius: "50%"
    opacity: 0.3
    description: "The largest geometric decoration variant — a 50vw centered ring with an inner ::before dashed ring at 70% diameter."
  image-placeholder:
    background: "{colors.bg-secondary}"
    border: "1px solid {colors.line}"
    description: "Solid taupe-tinted block with two crossed 1px diagonal hairlines via ::before/::after at +30° and -30°, suggesting an X over a blank frame. Holds a small uppercase label centered."
  team-photo:
    width: "12vw"
    height: "12vw"
    borderRadius: "50%"
    border: "1px solid {colors.line}"
    background: "{colors.bg-secondary}"
    description: "Circular portrait frame (12vw) in slightly darker stone, ringed in taupe, holding a single Playfair initial in accent taupe at center."
  nav-arrow:
    width: 40px
    height: 40px
    border: "1px solid {colors.line}"
    background: "transparent"
    description: "Square 40px button with 1px taupe border holding an arrow glyph. Hover state inverts to ink fill with cream text."
  nav-dot:
    width: 8px
    height: 8px
    borderRadius: "50%"
    background: "{colors.line}"
    description: "Small taupe dot at right edge as navigation indicator. Active state shifts to ink and scales 1.3."
  chart-stroke-primary: "{colors.text-primary}"
  chart-stroke-comparison: "{colors.line}"
  chart-comparison-dash: "5, 5"
  chart-grid-color: "{colors.bg-secondary}"
  chart-axis-tick-color: "{colors.accent}"
---

## 概述

Cartesian 是一套**安静的博物馆目录编辑系统**。其定义前提是**用 1px 线克制**。每一个结构元素——列表分隔、议程线、时间线连接、卡片边框、表格分割——都是一根闷灰褐 `{colors.line}` 的 1px 线。没有粗边框、没有填色块、没有阴影、没有圆角表面。层级靠字体对比和负空间建立；常规意义上的纵深并不存在。

字体栈是文学专著式配对。**Playfair Display**——高对比、带 Didone 影响的衬线——承担每一个标题、每一个统计数字、每一张卡片标题、每一个团队首字母、每一个引号。Playfair 几乎只用字重 400（regular）——系统里不用粗体或 700 字重的 Playfair。细笔画 Didone 美学依赖让字形在克制字重下呼吸。**Inter**——干净的现代 grotesque——承担每一段正文、每一个副标题、每一个标签、每一段落款。Inter 正文用 400，标签用 500。这对配对构成系统的编辑声线：衬线陈述 + 干净无衬线支撑结构。

色板是**五块暖石头加墨**。画布是 `{colors.bg-primary}`——温暖砂岩米白。略深一点的石头 `{colors.bg-secondary}` 提供细微区域区分（图片占位、团队照片框）。墨 `{colors.text-primary}` 是标题色；中灰 `{colors.text-secondary}` 是正文。更暖的灰褐 `{colors.accent}` 扛标签、落款和小数字。最浅的灰褐 `{colors.line}` 是通用 1px 线色。没有通俗意义上的强调色——没有红、没有橙、没有蓝。色板是石头、石头、石头、墨、墨。系统里唯一的「颜色」是字体对比。

纵深在**常规意义上完全缺席**。没有阴影、没有抬起的卡片、没有圆角表面、没有渐变。气氛靠**几何线装饰**创造：`{colors.line}` 的细实线圆和虚线圆，以 20–50% 透明度漂在内容后面，像在描图纸上用圆规画出来。它们不创造层级——它们创造情绪。装饰几何信号是「起草过的、斟酌过的、精确的」。

**密度哲学：稀疏、会呼吸。** Cartesian 稀疏时读起来优雅，挤满时读起来坏掉。正确构图的一页，是一个 Playfair 标题配一段正文，或一张图配一句短图注，四周是宽裕的负空间。多数幻灯片构图用居中或不对称双栏，`5–6vw` 槽，垂直方向大量呼吸。装饰圆规弧强化稀疏——周围有空间时它们最有效。在这套系统里感觉坏掉的一页，是内容铺满边到边；正确密度是「一个清楚的想法，框得好，落在石头纸上」。

**关键特征：**
- 温暖砂岩画布 `{colors.bg-primary}`，通用结构元素是单根 1px 灰褐 `{colors.line}` 分割线。
- 每一个标题/数字/引号用字重 400 的 Playfair Display 衬线；每一段正文/标签/落款用 Inter 无衬线。
- 五调单色色板：两块石头、两档灰、一墨。任何地方都没有鲜艳强调色。
- 装饰几何环（细实线 + 虚线圆，20–50% 透明度）作为圆规起草的气氛漂在内容后面。
- 每一个标签、落款和微文字都是大写 Inter，字距 2–3px。
- 所有边框都是 1px 发丝；没有任何元素有更粗的边框、阴影或圆角填色。
- 右缘竖向 nav-dot 列，左下方形 nav-arrow 按钮，右下等宽页码计数。
- 图片占位带着招牌的一对交叉 1px 对角线（一个 X）盖在石头色块上。

## 色彩

### 石头与墨色板
- **Background Primary**（`{colors.bg-primary}` — #EDE8E0）：画布。温暖砂岩米白——更接近「马尼拉文件夹」而不是「白纸」。这是默认幻灯片背景。
- **Background Secondary**（`{colors.bg-secondary}` — #E2DBD1）：略深一点的石头，用于图片占位、团队照片框，以及任何需要与画布细微分开、又不想上色填或加边框的区域。
- **Text Primary**（`{colors.text-primary}` — #1A1A1A）：近黑墨。用于标题、统计数字，以及特殊的 `{components.horizontal-accent}` 线。系统里最强的对比色。
- **Text Secondary**（`{colors.text-secondary}` — #5A5A5A）：中暖灰。用于所有正文段落。比墨软——可读，但会退。
- **Accent**（`{colors.accent}` — #8A8178）：暖灰褐。用于标签、落款、议程数字、页码计数、card-icon 文字、团队成员角色文字。系统的「小文字」色。
- **Line**（`{colors.line}` — #B8B0A4）：浅灰褐。通用 1px 线色：卡片边框、议程线、时间线连接、团队照片环、nav-arrow 边框、geo-decoration 环。

### 默认值
- **默认表面背景**：`{colors.bg-primary}`。
- **默认标题色**：`{colors.text-primary}`——永远是墨，从不染色，从不用强调灰褐。Playfair 标题一律是墨。
- **默认正文字色**：`{colors.text-secondary}`（中暖灰）。
- **默认标签 / 落款 / 微文字色**：`{colors.accent}`（暖灰褐）。
- **默认边框色**：`{colors.line}`——每一根 1px 结构边框。除了稀有的 `horizontal-accent` 线，从不用墨黑做边框。
- **默认次级表面填色**：`{colors.bg-secondary}`。
- **默认图表主系列色**：`{colors.text-primary}`（墨）。
- **默认图表对比/次系列色**：`{colors.line}` 配 5px 虚线描边。
- **默认图表网格色**：`{colors.bg-secondary}`。
- **默认图表轴刻度色**：`{colors.accent}`。

Cartesian **没有通俗意义上的强调色。** 红色 callout、蓝色柱、绿色统计——这些都不存在。需要强调时，加大字号、从无衬线切到衬线，或加一根 1px 墨色 `horizontal-accent` 线。颜色不是这套系统的强调机制；克制才是。

## 字体排印

### 字体家族
系统跑在一场**双面对谈**上：`Playfair Display`（衬线，字重 400/600/700，有斜体）承担每一个标题、统计数字、引号、卡片标题和团队首字母；`Inter`（无衬线，字重 300/400/500/600）承担每一段正文、副标题、标签、落款和微文字。没有第三张脸。

Playfair Display 几乎只用 **字重 400（regular）**。系统故意避开粗体 Playfair——Didone 美学依赖细笔画调制，更重字重会让它消失。斜体 Playfair 已加载但默认模板没有用；留给正文里的行内强调。

Inter 正文用字重 400，标签和微文字用 500，稀有的行内强调用 600。Playfair 高调制衬线与 Inter 均匀无衬线之间的对比，是系统的主排印节奏。

### 字号阶梯

| Token | 字号 | 字体 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.display}` | clamp(3rem, 6vw, 5.5rem) | Playfair Display | 400 | 封面或大开场标题 |
| `{typography.h1}` | clamp(2.5rem, 5vw, 4.5rem) | Playfair Display | 400 | 章节开场或大收束标题 |
| `{typography.h2}` | clamp(1.8rem, 3.5vw, 3rem) | Playfair Display | 400 | 主幻灯片标题 |
| `{typography.h3}` | clamp(1.2rem, 2vw, 1.6rem) | Playfair Display | 400 | 区域内的副标题 |
| `{typography.card-headline}` | 1.3rem | Playfair Display | 400 | 卡片或支柱块标题 |
| `{typography.timeline-headline}` | 1.2rem | Playfair Display | 400 | 时间线步骤或阶段标题 |
| `{typography.stat-figure}` | 2rem | Playfair Display | 400 | 数值统计（通常嵌在统计簇里） |
| `{typography.team-initial}` | 2rem | Playfair Display | 400 | 团队照片圆里居中的首字母 |
| `{typography.agenda-numeral}` | 1.5rem | Playfair Display | 400 | 议程行前面的序数 |
| `{typography.quote-mark}` | 5rem | Playfair Display | 400 | 引出式引文的开引号字形 |
| `{typography.subtitle}` | clamp(1rem, 1.5vw, 1.3rem) | Inter | 400 | 展示标题下方的副标题段 |
| `{typography.body}` | clamp(0.9rem, 1.2vw, 1.1rem) | Inter | 400 | 标准段落正文 |
| `{typography.body-sm}` | 0.9rem | Inter | 400 | 卡片或时间线项里的紧凑正文 |
| `{typography.attribution}` | 0.85rem | Inter | 400 | 引文下方的落款行，2px tracking + 大写 |
| `{typography.label}` | 0.75rem | Inter | 500 | 标题上方的区块标签 / eyebrow，3px tracking + 大写 |
| `{typography.micro}` | 0.7rem | Inter | 400 | 图片标签、页码计数、最小 chrome 文字 |

### 默认值
- **主幻灯片标题默认字号**：`{typography.h2}`（clamp 1.8–3rem）。
- **封面或大开场标题默认字号**：`{typography.h1}`（clamp 2.5–4.5rem）；最开阔的封面用 `{typography.display}`（clamp 3–5.5rem）。
- **段落正文默认字号**：`{typography.body}`（clamp 0.9–1.1rem）。
- **任何行内标签或 eyebrow 的默认字号**：`{typography.label}`（0.75rem）——永远 3px tracking + 大写。
- **任何 Playfair 标题的默认字重**：400。不要伸手去拿 600 或 700。
- **正文默认字重**：400。
- **标签/微文字默认字重**：500。
- **统计簇里统计数字的默认字号**：`{typography.stat-figure}`（2rem）。Cartesian 没有英雄统计数字模式（没有 5–7rem 展示统计）；统计以克制尺度作为行内档位呈现。

拿不准时，伸手去拿 `{typography.h2}` 做这一页的主文字瞬间，不要拿 `{typography.h3}`（那是区域内的副标题）。

### 招牌处理
这些处理在**对应元素类型一旦使用时就是必选项**：

- **每一个 Playfair 标题、统计、引文、卡片标题和首字母都设为字重 400。** 本系统不存在粗体 Playfair。细笔画 Didone 美学就是身份。
- **每一个 Playfair 元素都用句首大写（专有名词用真正的标题大小写）。** 不用大写 Playfair。
- **每一个 Inter 标签、落款和微文字元素都是大写，字距 2–3px。** 标签 3px tracking；落款和微文字 2px。没有 tracking 的 Inter 大写读起来像没处理过。
- **每一个 Playfair 元素都渲染成 `{colors.text-primary}`（墨）。** 标题从不是强调灰褐，从不是灰。例外是圆形 `card-icon` 或 `team-photo` 里的装饰首字母，字形渲染成 `{colors.accent}`。
- **每一根 1px 结构边框都用 `{colors.line}`。** 除了稀有的墨色 `horizontal-accent` 线，不存在其他边框色。
- **每一张卡片、image-placeholder、team-photo 和 nav-arrow 边框都是 1px solid。** 本系统不存在更粗的边框。
- **图表主系列用墨黑，对比系列用虚线灰褐（5px, 5px）。** 这对是唯一的图表颜色规则。

### 排印原则
Playfair-400 + Inter-400 的组合就是系统的声线。换掉任何一套家族，或把 Playfair 跳到字重 700，都读成另一套设计系统。允许通过正文里的行内 `<em>` 做斜体强调（Inter 斜体）——斜体 Playfair 已加载但留给稀有用途。不用下划线。

行高保持开放：标题 1.1，正文 1.6。宽的正文字行高是呼吸空间美学的一部分。

## 版式

### 画布系统
画布是 `100vw × 100vh`——全视口，溢出隐藏。每一张 `.slide` 绝对定位填满视口；同一时间一张幻灯片带着 `.active`（opacity 1，visibility visible）。过渡是 0.6s 透明度 + visibility 淡入淡出。

### 内边距与间距阶梯
| Token | 值 | 用途 |
|---|---|---|
| `{spacing.pad-y}` | 4vh | 默认垂直幻灯片内边距 |
| `{spacing.pad-x}` | 4vw | 默认水平幻灯片内边距 |
| `{spacing.gap-xl}` | 6vw | 主要双栏槽（最宽裕） |
| `{spacing.gap-lg}` | 5vw | 标准双栏或网格槽 |
| `{spacing.gap-md}` | 3vw | 卡片网格槽 |
| `{spacing.gap-sm}` | 2vh | 议程行垂直内边距、落款间距 |
| `{spacing.card-pad}` | 4vh 2vw | 内容卡片内部内边距 |

标题通常相对上方标签有 2–3vh margin-bottom，相对下方正文有 2vh margin-bottom。3 卡片或 4 人团队网格上方的区块标题相对网格有 6vh margin-bottom（显著的呼吸空间）。

### 装饰几何层
Cartesian 的招牌是**描图纸几何装饰**。每一页可以叠一层或多层：
- 锚在角落的大环 `geo-decoration`（通常直径 30–50vw），内圈虚线环约 80% 直径（`::before` 伪元素）。
- 距左缘约 8vw 的 `vertical-line`，从地到顶，30% 透明度。
- 锚在距左下 15vh 的 `horizontal-accent`（一根短的黑色 1px 线）。
- 收束或沉思页上居中的 `geo-ring`（50vw 圆）。

这些元素**没有信息角色**——它们创造气氛。没有任何几何装饰的幻灯片也成立；过度装饰（每页超过两个 geo 元素）会拆掉克制。

### 页框
系统的 chrome 很少：
- 右缘竖列小 `nav-dot` 指示器（8px 灰褐圆）。
- 左下一对方形 `nav-arrow` 按钮（40×40，1px 灰褐边框，透明填充）。
- 右下 `slide-counter` 文字，Inter 0.75rem、2px tracking、`{colors.accent}`。

没有顶部 chrome 条，没有持久页眉，没有页脚线。

## 纵深与层次

### 平面（唯一手法）
Cartesian 没有阴影、没有抬起的卡片、没有圆角表面、没有渐变。每个元素都坐在同一平面上。

层级由以下构成：
- **字体对比**——Playfair 衬线对 Inter 无衬线；字号从 5rem 下到 0.7rem。
- **1px 发丝分割线**——议程行、时间线、卡片轮廓、image-placeholder 轮廓、统计顶边、团队照片环、nav-arrow 边框。
- **色调**——墨对灰对灰褐。
- **负空间**——每个元素周围宽裕的内边距。
- **几何气氛**——内容后面圆规起草的环暗示纵深，而不创造它。

引入 `box-shadow`、抬起的卡片或柔渐变，会拆掉定义这套系统的克制。

## 形状与处理

### 圆角
| 值 | 用途 |
|---|---|
| 50%（圆） | 每一个圆形元素：`card-icon`（40px）、`team-photo`（12vw）、`nav-dot`（8px）、`geo-circle`、`geo-arc`、`geo-decoration`、`geo-ring` |
| 0 | 其余一切：卡片、image-placeholder、nav-arrow、议程行、时间线、统计块、图表容器 |

系统只用**两个半径值**：50%（真圆）或 0（尖角矩形）。不存在软圆角。

### 描边粗细
- **1px solid `{colors.line}`** —— 通用结构边框。用于每一张卡片、image-placeholder、团队照片环、nav-arrow、议程行底、时间线、统计顶、geo-circle、geo-decoration。
- **1px dashed `{colors.line}`** —— 用于 `geo-arc` 以及 `geo-decoration` / `geo-ring` 里的内圈 `::before` 环。虚线信号是「构造线 / 弧」。
- **1px solid `{colors.text-primary}`** —— 只用于稀有的 `horizontal-accent` 装饰线。系统唯一的墨黑线。
- **图表柱/线描边宽度** —— Chart.js 系列 1px（柱边框）、2px（线系列）。对比系列 2px 虚线（5px 虚、5px 空）。

所有结构边框都是 `{colors.line}`。不存在更粗的边框、彩色边框，以及（geo-arc 以外的）虚线结构边框。

### 装饰元素类型

**几何环（geo-circle / geo-decoration / geo-ring）** —— 各种尺寸（10vw、30vw、50vw）的细 1px 灰褐圆，20–50% 透明度。通常配一个内圈虚线 `::before` 环，为外径的 70–80%，暗示圆规构造既有主弧也有偏移弧。锚在角落或中心；坐在内容后面，`z-index: 0` 且 `pointer-events: none`。

**竖线** —— 单根 1px 灰褐柱，锚在距幻灯片左缘约 8vw，从地到顶，30% 透明度。暗示描图纸对齐导轨。每页可选。

**水平强调线** —— 单根 20vw × 1px 黑线，锚在距幻灯片左下 15vh。系统唯一的墨黑线——用作封面或收束版式上的强终端强调线。少用。

**图片占位** —— 实心 `{colors.bg-secondary}` 块，两根 150% 对角线 1px 灰褐线经 `::before` / `::after` 以 +30° 和 -30° 交叉，形成一个 X。居中一个小号大写 Inter 标签（「Visual Reference」或类似）。X 图案是招牌的「图还没接上」处理。

**团队照片框** —— 12vw 圆形块，`{colors.bg-secondary}`，1px 灰褐环，居中一个 2rem 的 Playfair-400 首字母，颜色 `{colors.accent}`。用作肖像占位。

**卡片** —— 1px 灰褐边框块，半透明白内部填充（`{colors.white-overlay}`），让画布色调细微渗过来。淡白填充把卡片和裸区域区分开；拿掉填充，卡片就消失。

**议程行** —— flex 行，左边 Playfair `{typography.agenda-numeral}` 用 `{colors.accent}`，右边标签，2vh padding，1px 灰褐底边。叠起来的行形成议程列表。

**时间线** —— 一根 1px 灰褐顶边横跨均匀分布的时间线项 flex 行；每一项带着小号 Inter `year` 标签（灰褐）、Playfair `{typography.timeline-headline}`，以及一段 Inter 正文。发丝线是唯一的时间线结构——没有节点、没有标记、没有圆点。

**统计簇** —— 统计项 flex 行，用 `gap-md` 分开，1px 灰褐顶边框住，行内 `{typography.stat-figure}` Playfair 数字，下方小号大写 Inter 标签（灰褐）。

**引号** —— 5rem Playfair 引号字形，50% 透明度灰褐，放在 Playfair `{typography.h2}` 标题上方 + 下方小号大写灰褐落款。

**图表** —— Chart.js 柱图或折线图，主系列墨黑，对比系列虚线灰褐。网格线用 `{colors.bg-secondary}`。轴刻度用 `{colors.accent}`。主系列永远不填色（或折线图上用 5% 墨色淡填）。

## 宜与忌

### 宜
- 每一个结构分隔都用 `{colors.line}` 的单根 1px 线——议程线、时间线连接、卡片边框、统计顶、团队照片环。1px 发丝就是 Cartesian 的身份。
- 每一个 Playfair 标题、统计、引号和卡片标题都设为字重 400。不要伸手去拿粗体；细笔画 Didone 美学依赖它。
- 每一个标题都渲染成 `{colors.text-primary}`（墨）。Playfair 从不以灰褐或彩色出现。
- 每一个标签、落款、议程数字和微文字都渲染成 `{colors.accent}`（灰褐），大写 + 2–3px 字距。
- 在内容后面叠装饰几何环（实线 + 虚线），20–50% 透明度，作气氛。每页一到两个 geo 元素；从不超过。
- 用 Playfair Display（衬线标题）配 Inter（无衬线正文）。双面对位是固定的。
- 在图片占位里用交叉对角线 X 图案。它是系统的招牌占位处理。
- 让幻灯片呼吸——稀疏版式配宽裕负空间才是正确密度。
- 用 `{colors.bg-secondary}` 作图片占位和团队照片框的填充——一块细微的石头，不是白，不是灰。
- 少用一根 `horizontal-accent`（20vw × 1px 墨线）作为封面或收束构图上的强终端线。

### 忌
- 不要引入通俗强调色。不要红、不要橙、不要蓝、不要绿。色板是石头压石头，标题用墨。
- 不要把 Playfair 标题渲染成 `{colors.accent}`（灰褐）。标题是墨；灰褐留给小文字。
- 不要把任何 Playfair 元素加粗。字重 400 是常设规则；粗体会拆掉 Didone 美学。
- 不要加阴影、抬起的卡片或渐变填充。Cartesian 是平面的；纵深来自几何和字体，不是 z 轴。
- 不要给卡片或矩形用圆角。唯一的圆形状是真圆（半径 50%）。
- 不要用粗边框（2px+）。每一根结构边框都是 1px。
- 不要把幻灯片挤满。稀疏呼吸的版式读起来优雅；塞满的版式读起来坏掉。
- 不要给 Playfair 配另一套无衬线搭档。Inter 配对是固定的。
- 不要把标签或微文字渲染成句首大写。小号 Inter 文字永远是大写 + 2–3px tracking。
- 不要每页加超过两个 geo 装饰——克制是规则；过度装饰读起来杂。

## 响应式行为

Cartesian 是一套视口流体的 1920×1080 演示系统，全程用 `vw` / `vh` 和 `clamp()`。有一个 `@media (max-aspect-ratio: 4/3)` 断点，把双栏网格收成单栏，藏掉时间线（叠起来会失去意义），并把团队和卡片网格竖向堆叠。除此之外系统无需断点即可响应。

### 缩放行为
- 展示标题经 `clamp()` 从最小视口 2.5rem 缩放到最大 5.5rem。
- 正文从 0.9rem 到 1.1rem。
- 内边距用随视口线性缩放的 `vh` / `vw`。
- 1px 边框、8px 导航点、40px 导航箭头是固定的，不缩放。

### 演示行为
- 前进：`ArrowRight` 或 `Space`。
- 后退：`ArrowLeft`。
- 右缘导航点可点击跳到指定页。
- 左下导航箭头可点击；悬停状态把背景反成墨、文字变成奶油。
- 右下页码计数显示当前 / 总数，两位零填充。

### 图表
图表用 Chart.js 渲染（经 CDN 加载）。源码里两种图表类型是柱和线；都遵循墨主色 / 虚线灰褐对比的惯例。自定义字体设置把 Inter 注入 Chart.js 标签渲染。

### 打印 / 导出
没有显式处理。每一页是 100vw × 100vh 块；导出工作流应对每页在 1920×1080 截图。

## 中日韩与国际内容

### 推荐中文配对

| 角色 | 拉丁字体 | 推荐中文配对 | 来源 |
|---|---|---|---|
| Display / Headline（Playfair Display 400） | Playfair Display | 思源宋体 Noto Serif SC 700 | Google Fonts |
| Body / Label（Inter 400–500） | Inter | 思源宋体 Noto Serif SC 400 | Google Fonts |

### 中英混排策略

用 **策略 A —— 单字体栈带回退**：在同一 `font-family` 栈里把 Noto Serif SC 声明在拉丁字体*之后*，这样拉丁字形用 Playfair / Inter 渲染，CJK 字形自动落到 Noto Serif SC。每个角色一条 CSS 规则，不用手动切类。

### 加载

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..700;1,400..700&family=Inter:wght@300..600&family=Noto+Serif+SC:wght@400;700&display=swap" rel="stylesheet">
```

```css
:root {
  --font-display: "Playfair Display", "Noto Serif SC", serif;
  --font-body: "Inter", "Noto Serif SC", sans-serif;
}
/* Headlines use Noto Serif SC 700; body uses Noto Serif SC 400. */
```

### 通用 CJK 调整

- **行高**：把 CJK 正文字行高提到约 1.75（从 1.6）——汉字比拉丁小写需要更多垂直呼吸，而 Cartesian 本就偏爱宽裕行距。
- **字距**：汉字跑段把 `letter-spacing` 清零。只在大写拉丁标签上保留 2–3px tracking。
- **大小写变换**：内容是汉字时，任何标签/落款/微文字都去掉 `text-transform: uppercase`——中文没有大小写；强制大写对汉字无效，但会弄坏里面混排的拉丁缩写。
- **标点**：中文句子用中文全角标点（，。：；「」），拉丁用半角（`,.:;""`）。永远不要把半角标点混进中文句子。
- **标题不加句号**：中文标题惯例省略末尾 。——从展示字符串里拿掉。
- **盘古之白**：相邻汉字与拉丁/数字跑段之间插入细空格（或普通空格）（例如 `2026 年`、`AI 产品`）。改善混排可读性。
- **一句一句一种字体**：不要在句子中间切换 CJK 家族。给定一段文字跑段只选一个字重的 Noto Serif SC，永远不要在一个短语里用两个。

### 美学说明

Noto Serif SC（思源宋体）是主流汉字衬线里唯一能给出 Cartesian 所需克制编辑色域的——它调制过的横细竖粗笔画呼应 Playfair 的 Didone 美学，均匀节奏也匹配 Cartesian 的「博物馆目录」声线。标题用 NSC 字重 700 保住拉丁展示的视觉质量，NSC 400 以 Inter 同样安静的暖意扛正文。五石头色板干净吸收汉字，因为每个字形都停在墨或灰褐——没有糖果填色要谈判。装饰圆规弧几何层与内容无关，任何语言都一样工作。不要给汉字加粗（这是 Cartesian「Playfair 不加粗」规则的中文排印对位）；靠字号和 1px 线分割做层级。

### 已知 CJK 缺口

只加载了 Noto Serif SC 这一套汉字衬线——没有斜体轴（中文活字历史上没有斜体），所以正文落到 NSC 时，稀有的斜体 Playfair `<em>` 瞬间会丢掉强调。用 `{colors.accent}`（灰褐）给单字符 span 上色，或把强调短语包进淡括号 「」，来找回强调。NSC 的 700 字重是能拿到的最重——系统通过 400 字重克制的规则自然延伸到中文，所以实践中这很少是缺口。

## 迭代指南

1. 每一个新结构分隔都用 1px solid `{colors.line}` 边框。没有例外。
2. 每一个新标题都用字重 400 的 Playfair Display，颜色 `{colors.text-primary}`。不加粗；不上色。
3. 每一个新的小文字元素（标签、落款、微文字）都用大写 Inter，字距 2–3px，颜色 `{colors.accent}`。
4. 每一个新正文段落都用 Inter 字重 400，颜色 `{colors.text-secondary}`，行高 1.6。
5. 每一张新卡片都用 1px 灰褐边框 + 半透明白叠层填充。无阴影，无圆角。
6. 新的圆形元素（图标、照片、装饰环）用 border-radius 50% 配 1px 灰褐环。
7. 新的几何装饰保持克制：每页 1 或 2 个，20–50% 透明度，在内容后面（z-index 0，pointer-events none）。
8. 新图表系列遵循墨主色 / 虚线灰褐对比惯例。不要引入彩色图表系列。
9. 新版式遵守呼吸空间密度规则——在 Cartesian 里稀疏胜过密。
10. `horizontal-accent` 20vw 墨线是系统唯一的「墨线」——少用作终端强调，从不当常规分割线。

## 已知缺口

- Chart.js 库经 CDN 加载；柱和线以外的新图表类型需要手工配置，以匹配墨主色 / 虚线灰褐对比美学。
- 装饰 `geo-decoration` 和 `geo-ring` 的 `::before` 内环图案硬编码在 CSS 里；超出源码练习的尺寸变体需要新样式规则。
- 团队照片占位显示一个灰褐 Playfair 首字母；插入真正肖像需要把首字母换成 `<img>` 并调整圆形裁切。
- 图表轴标签色和网格色硬编码在 Chart.js options 块的行内（而不是从 CSS 变量读）——重设样式要改 JS，不是 CSS。
- 图片占位 X 图案（交叉 +30°/-30° 对角线）经 `::before` / `::after` 以固定 150% 宽度渲染；把占位缩放到超出源码尺寸时，可能需要重算旋转角以保持贴边。
- 斜体 Playfair 已加载但没有任何默认规则用到；可用于正文里的行内 `<em>` 强调，但系统本身不写任何斜体文字。
- `vertical-line` 和 `horizontal-accent` 装饰元素有硬编码位置值（距左 8vw，距底 15vh）；偏离默认位置使用时需要逐实例样式覆盖。
- 页码计数的 `currentSlide` / `totalSlides` ID 在 JS 里被引用，但系统没有内部幻灯片名称注册表；新幻灯片只按 DOM 顺序递增。
