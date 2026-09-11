---
version: alpha
name: Broadside
description: A protest-poster editorial system built on massive Barlow type and a single fire-orange environment color. The aesthetic is "ink on fire" — dark slides for documentation, orange slides for declaration. Display type is enormous (13vw, roughly 187px at 1440 width) in weight 900 lowercase, treating words as graphic elements rather than reading copy. The cultural reference is broadside printing, SPACE10 reports, and Wim Crouwel grids reinterpreted with one loud color and zero decoration.

colors:
  ink-black: "#111111"
  ink-black-alt: "#1A1A18"
  fire-orange: "#E85D26"
  cream: "#F0ECE5"
  cream-muted: "#888880"
  cream-hint: "#505048"
  border-dark: "#282826"
  ink-on-orange-muted: "rgba(17, 17, 17, 0.75)"
  ink-on-orange-hint: "rgba(17, 17, 17, 0.55)"
  ink-on-orange-faint: "rgba(17, 17, 17, 0.40)"
  ink-on-orange-border: "rgba(17, 17, 17, 0.20)"

color-aliases:
  c-bg: ink-black
  c-bg-alt: ink-black-alt
  c-bg-light: ink-black            # Broadside collapses "light" → dark; there are no cream slides
  c-bg-orange: fire-orange
  c-fg: cream
  c-fg-2: cream-muted
  c-fg-3: cream-hint
  c-accent: fire-orange
  c-border: border-dark

typography:
  display:
    fontFamily: "Barlow, Noto Sans SC, sans-serif"
    fontSize: "13vw"
    fontWeight: 900
    lineHeight: 0.88
    letterSpacing: -0.04em
  h1:
    fontFamily: "Barlow, Noto Sans SC, sans-serif"
    fontSize: "7.5vw"
    fontWeight: 800
    lineHeight: 0.9
    letterSpacing: -0.03em
  h2:
    fontFamily: "Barlow, Noto Sans SC, sans-serif"
    fontSize: "4.5vw"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.02em
  h3:
    fontFamily: "Barlow, Noto Sans SC, sans-serif"
    fontSize: "2.8vw"
    fontWeight: 600
    lineHeight: 1.2
  lead:
    fontFamily: "Barlow, Noto Sans SC, sans-serif"
    fontSize: "1.6vw"
    fontWeight: 400
    lineHeight: 1.5
  body:
    fontFamily: "Barlow, Noto Sans SC, sans-serif"
    fontSize: "1.2vw"
    fontWeight: 400
    lineHeight: 1.6
  caption:
    fontFamily: "Barlow, Noto Sans SC, sans-serif"
    fontSize: "0.9vw"
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "IBM Plex Mono, monospace"
    fontSize: "0.72vw"
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.14em
    textTransform: uppercase
  stat-value:
    fontFamily: "Barlow, Noto Sans SC, sans-serif"
    fontSize: "5.5vw"
    fontWeight: 900
    lineHeight: 1
    letterSpacing: -0.04em
  quote-mark:
    fontFamily: "Barlow, Noto Sans SC, sans-serif"
    fontSize: "10vw"
    fontWeight: 900
    lineHeight: 0.6
  quote-text:
    fontFamily: "Barlow, Noto Sans SC, sans-serif"
    fontSize: "3.8vw"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.02em
  fadelist-item:
    fontFamily: "Barlow, Noto Sans SC, sans-serif"
    fontSize: "7.5vw"
    fontWeight: 900
    lineHeight: 1
    letterSpacing: -0.03em
  fadelist-title:
    fontFamily: "Barlow, Noto Sans SC, sans-serif"
    fontSize: "10.5vw"
    fontWeight: 900
    lineHeight: 0.9
    letterSpacing: -0.04em

spacing:
  pad-x: "5.5vw"
  pad-y: "5.5vh"
  gap-lg: "3.5vh"
  gap-md: "2vh"
  gap-sm: "1vh"

canvas:
  width: 100vw
  height: 100vh

motion:
  ease-slide: "cubic-bezier(0.77, 0, 0.175, 1)"
  dur-slide: "0.8s"
  ease-enter: "cubic-bezier(0.16, 1, 0.3, 1)"
  dur-enter: "0.5s"

components:
  slide-chrome:
    layout: "flex row, justify space-between"
    paddingBottom: "{spacing.gap-sm}"
    borderBottom: "1px solid {colors.border-dark}"
    marginBottom: "{spacing.gap-md}"
    description: "Top chrome bar carrying section label on left, slide number/meta on right. Suppressed on cover, chapter, quote, and end slides."
  slide-foot:
    layout: "flex row, justify space-between"
    paddingTop: "{spacing.gap-sm}"
    borderTop: "1px solid {colors.border-dark}"
    marginTop: "{spacing.gap-md}"
    description: "Bottom chrome bar, mirrors top chrome. Same suppression rules."
  rule:
    width: 36px
    height: 2px
    background: "{colors.fire-orange}"
    description: "Stub accent rule. On orange slides this flips to {colors.ink-black}."
  rule-full:
    width: "100%"
    height: 2px
    background: "{colors.border-dark}"
  kicker:
    fontFamily: "{typography.label.fontFamily}"
    fontSize: "{typography.label.fontSize}"
    letterSpacing: 0.14em
    textTransform: uppercase
    color: "{colors.fire-orange}"
    description: "Eyebrow above headlines. Orange on dark; dark-ink-at-55%-opacity on orange."
  tag:
    fontFamily: "{typography.label.fontFamily}"
    fontSize: "{typography.label.fontSize}"
    letterSpacing: 0.14em
    textTransform: uppercase
    color: "{colors.fire-orange}"
    border: "1px solid {colors.fire-orange}"
    padding: "0.3em 0.8em"
    description: "Bordered mono tag. On orange slides flips to dark ink with 40%-opacity dark border."
  broadside-num:
    fontFamily: "IBM Plex Mono, monospace"
    fontSize: "1.1vw"
    fontWeight: 500
    letterSpacing: 0.1em
    color: "rgba(17, 17, 17, 0.45)"
    description: "Catalogue-style slide number, typically anchored top-left on orange slides. On dark slides, color shifts to {colors.cream-hint}."
  stat-card:
    borderTop: "1px solid {colors.border-dark}"
    padding: "{spacing.gap-md} {spacing.gap-md} {spacing.gap-md} 0"
    description: "Top-border-only data card. Big orange numeral above body label above mono note."
  bullet-marker:
    content: "/"
    color: "{colors.fire-orange}"
    fontFamily: "IBM Plex Mono, monospace"
    fontWeight: 700
    description: "Slash glyph rendered via ::before on every bullet item. Orange on dark, dark-at-45%-opacity on orange."
  compare-panel-left:
    paddingRight: "calc({spacing.pad-x} * 0.55)"
    borderRight: "1px solid {colors.border-dark}"
  compare-panel-right:
    paddingLeft: "calc({spacing.pad-x} * 0.55)"
  compare-panel-orange:
    background: "{colors.fire-orange}"
    description: "Right-half panel filled with fire orange — the 'after' or payoff side in compare layouts."
  bar-track:
    height: "30vh"
    borderLeft: "1px solid {colors.border-dark}"
    description: "Vertical bar chart container. Bars are cream-hint by default; one bar per chart gets the .accent class for fire orange."
  bar-fill:
    background: "{colors.cream-hint}"
  bar-fill-accent:
    background: "{colors.fire-orange}"
  img-placeholder:
    height: "55vh"
    background: "rgba(255, 255, 255, 0.04)"
    border: "1px dashed {colors.border-dark}"
    textTransform: uppercase
    letterSpacing: 0.12em
    description: "Dashed-border placeholder shown when no image is wired. Same 55vh footprint as a real img."
  fadelist-stack:
    description: "Vertical stack of three display-weight words, opacities 1.0 / 0.5 / 0.22 top-to-bottom. The SPACE10 'before/during/after' treatment."
---

## 概述

Broadside 是一套**抗议海报式编辑系统**。核心前提：字大到不再当正文读，而当成图形原件。展示字号 `13vw`（`{typography.display}`）让单个词在 1440 宽屏幕上大约 187px——宽到眼睛先扫字形，再才读字。这是系统的主表达工具。

字体栈是单体的。**Barlow** 从 `{typography.display}` 一路扛到 `{typography.body}`——没有衬线搭档，没有手写强调，没有第二套展示脸。表现力全靠字重（400 到 900）和字号，不靠面孔对比。**IBM Plex Mono** 是唯一的第二张脸，而且只出现在 chrome：页码、kicker、标签、tag、图注，以及列表斜杠标记。**Noto Sans SC** 坐在每个 font-family 栈里，作为匹配字重的 CJK 回退。声线统一、厚重、小写——*Broadside 不用大写标题。* 这是对野兽派常规的一次有意义反转。

色板分两套截然不同的色域。**暗色域**用近黑画布 `{colors.ink-black}`，奶油字 `{colors.cream}`，`{colors.fire-orange}` 作为唯一强调——橙色只用于重点（kicker、强调统计、列表标记、主柱）。**橙色域**把关系整个翻过来：`{colors.fire-orange}` 变成整页背景，同一套暗色 `#111111` 墨水用于标题和正文。没有浅色/奶油幻灯片变体——源码里 `.light` 类被故意别名到暗色。封面和章节页默认走橙色域；内容页默认走暗色。

纵深是**平面**。没有投影，没有抬升 token，没有柔软表面。层级完全靠字重、字号和 1px 发丝分割线。`slide-chrome` 与 `slide-foot` 的边框、`stat-card` 的顶边、`compare-panel` 的分割线，是系统仅有的纵深信号。一切都坐在同一平面上。

**密度哲学：低到中。** Broadside 为负空间而建。正确构图的一页，是一个巨大的展示瞬间配 1–2 行图注，再别无他物。列表明确上限三条——系统看重冲击密度，不看信息密度。在这套系统里感觉坏掉的一页，是四栏正文抢注意力；正确密度是一句陈述、一根线、呼吸空间。封面、章节和引文页把这做到最远：彻底关掉 chrome，把字单独留在场上。

**关键特征：**
- 巨大的 Barlow 展示字，字重 900，**小写**——展示元素从不大写。
- 双色域：暗页配奶油字，或橙页配暗墨。不存在奶油/白页。
- `{colors.fire-orange}` 既是强调（暗页上）也是环境（橙页上）——从不是第二强调色，永远是*那一个*颜色。
- 单字体系统：Barlow + 仅用于 chrome 的 IBM Plex Mono。无衬线搭档，无手写，无第三张脸。
- 1px 发丝分割线（暗页用 `{colors.border-dark}`；橙页用 `rgba(17,17,17,0.2)`）提供全部层级结构。
- 等宽 kicker、等宽 tag、等宽目录编号——chrome 声线永远是 IBM Plex Mono 大写。
- 列表用等宽 `/` 字形作标记，每表上限三条。
- 平面——无阴影、无圆角表面、无渐变背景。
- `{spacing.pad-x}` 5.5vw + `{spacing.pad-y}` 5.5vh 造出宽裕的画框；字填满剩下的空间。

## 色彩

### 两套色域
Broadside 跑在二元表面系统上。每一页要么是**暗**（近黑底、奶油字、橙色作唯一强调），要么是**橙**（火橙底、暗墨字、暗墨作闷强调调）。没有奶油/纸色域——源码里 `.light` 类被别名到暗色。每页选一套色域并贯彻到底。

### 色板
- **Ink Black**（`{colors.ink-black}` — #111111）：暗色域的主画布，也是橙页上的主文字色。比纯黑略软，但读起来就是黑。这是系统的通用「墨」。
- **Ink Black Alt**（`{colors.ink-black-alt}` — #1A1A18）：暗色域的次级表面，用于某块区域需要相对基底画布略抬起、又不打破平面时。
- **Fire Orange**（`{colors.fire-orange}` — #E85D26）：招牌色。暗页上它是强调——kicker、强调统计值、列表标记、图表主柱、橙色开引号。橙页上它是整页环境。饱和度高，但色相偏暖而不是电光；读起来是抗议海报，不是安全背心。
- **Cream**（`{colors.cream}` — #F0ECE5）：暗页上的主文字色。暖米白，从不是纯白——暖意软化暗画布，并给出编辑色域信号。
- **Cream Muted**（`{colors.cream-muted}` — #888880）：暗页上的次级文字——支撑正文、副标题、对比里较闷的那一半。
- **Cream Hint**（`{colors.cream-hint}` — #505048）：暗页上的三级文字——图表轴标签、来源注、不在等宽语境时的页码。
- **Border Dark**（`{colors.border-dark}` — #282826）：暗页上的 1px 分割线色。相对画布几乎看不见；给结构，不抢注意。
- **Ink-on-orange 叠层**：暗墨四档透明度（75% / 55% / 40% / 20%），用于橙页上的正文、hint、标签和边框处理。它们是橙色域的「闷」对位。

### 默认值
- **内容页默认表面**：`{colors.ink-black}`（暗色域）。
- **封面、章节、statement-payoff、section-divider 页默认表面**：`{colors.fire-orange}`（橙色域）。
- **暗表面上的默认标题色**：`{colors.cream}`。
- **橙表面上的默认标题色**：`{colors.ink-black}`。
- **暗表面上的默认正文字色**：`{colors.cream}`。
- **橙表面上的默认正文字色**：`rgba(17, 17, 17, 0.75)`。
- **暗表面上的默认强调色**：`{colors.fire-orange}`——用于 kicker、强调统计值、列表标记、图表主柱，以及开引号。
- **橙表面上的默认强调色**：`{colors.ink-black}`——暗墨本身成为对比跳点。
- **默认 chrome 边框色**：暗页用 `{colors.border-dark}`；橙页用 `rgba(17, 17, 17, 0.2)`。

橙色域没有第三色。橙页需要强调时，用现有墨水的字重或透明度对比，不要加新色相。引入第二强调色会拆掉系统。

## 字体排印

### 字体家族
系统在 **Barlow** 上是单语的（Noto Sans SC 作为 CJK 回退，覆盖相同角色）。每个 display、标题、导语、正文和图注 token 都用 Barlow。唯一的第二张脸是 **IBM Plex Mono**，完全留给 chrome：页码、kicker、tag、标签、图表轴图注、列表标记、图片图注和来源注。Barlow 紧凑 grotesque 密度与 IBM Plex Mono 均匀等宽之间的对比，是系统的次级排印节奏；主节奏是 Barlow 自己的字重与字号轴。

不用斜体。不用下划线。唯一的强调机制是字重、字号和颜色（暗页上的橙色强调，或橙页上仅靠字重）。

### 展示、标题与正文阶梯

| Token | 字号 | 字体 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.display}` | 13vw | Barlow | 900 | 封面级展示——字*就是*构图的那一页上的单一主导元素 |
| `{typography.fadelist-title}` | 10.5vw | Barlow | 900 | fadelist 构图里舞台一侧的超大展示 |
| `{typography.quote-mark}` | 10vw | Barlow | 900 | 引出式引文页上的开引号字形 |
| `{typography.h1}` | 7.5vw | Barlow | 800 | 章节或章节开场标题 |
| `{typography.fadelist-item}` | 7.5vw | Barlow | 900 | 三阶段 fadelist 处理里每一个叠放的词 |
| `{typography.stat-value}` | 5.5vw | Barlow | 900 | 统计卡里的大号数据数字 |
| `{typography.h2}` | 4.5vw | Barlow | 700 | 主幻灯片标题 |
| `{typography.quote-text}` | 3.8vw | Barlow | 700 | 引出式引文正文 |
| `{typography.h3}` | 2.8vw | Barlow | 600 | 副标题，或对比里的面板标题 |
| `{typography.lead}` | 1.6vw | Barlow | 400 | 导语段、列表项、突出的支撑文案 |
| `{typography.body}` | 1.2vw | Barlow | 400 | 标准正文段落 |
| `{typography.caption}` | 0.9vw | Barlow | 400 | 图片图注、脚注、来源行 |
| `{typography.label}` | 0.72vw | IBM Plex Mono | 500 | chrome 标签、kicker、tag、等宽注 |

### 默认值
- **主内容页标题默认字号**：`{typography.h2}`（4.5vw）。
- **封面或章节标题默认字号**：`{typography.h1}`（7.5vw）。
- **陈述页上单一宣言式展示瞬间的默认字号**：`{typography.display}`（13vw）。
- **段落正文默认字号**：`{typography.body}`（1.2vw）；紧跟标题的导语段用 `{typography.lead}`（1.6vw）。
- **任何行内 chrome 元素（标签、kicker、tag、页码、轴标签）的默认字号**：`{typography.label}`（0.72vw）。
- **统计卡里英雄数字的默认字号**：`{typography.stat-value}`（5.5vw）。
- **任何 Barlow 展示瞬间（h2 及以上）的默认字重**：700+；最大展示用 900。
- **正文默认字重**：400。

拿不准时，伸手去拿 `{typography.h2}` 做这一页的主文字瞬间。`{typography.h1}` 留给章节/区块开场；`{typography.display}` 留给字就是整幅构图的稀有瞬间。

### 招牌处理
这些处理在**对应元素类型一旦使用时就是必选项**：

- **所有 Barlow 展示、标题、导语和正文都用句首大写（专有名词用真正的标题大小写）。** 本系统不存在展示字重的大写 Barlow——那读起来完全是另一套设计语言。小写展示是 Broadside 最鲜明的单一决定。
- **所有 IBM Plex Mono chrome 文字都是大写，字距至少 0.1em。** 等宽标签、kicker、tag、页码、轴标签、来源注和列表标记永远大写。Barlow 正文小写与等宽 chrome 大写之间的大小写分裂，是系统的主大小写节奏。
- **所有展示 token 都带负字距。** `{typography.display}` 和 `{typography.stat-value}` 为 -0.04em；`{typography.h1}` 和 `{typography.fadelist-title}` 为 -0.03em 或 -0.04em；`{typography.h2}` 和 `{typography.quote-text}` 为 -0.02em。展示字重的 Barlow 没有负 tracking，读起来像没处理过。
- **所有 Barlow 展示元素跑在字重 700、800 或 900——从不更轻。** 展示字号上更轻的 Barlow 会丢掉大幅传单的密度。
- **橙页上，每一个 Barlow display/h1/h2/h3 元素都强制为 `{colors.ink-black}`。** 这就是「火上落墨」规则——橙页上不存在奶油色标题。
- **每一条列表项都通过 `::before` 带上橙色 `/` 等宽标记。** 本系统不存在圆点、破折号或数字列表标记。
- **每一个 kicker 都是大写 IBM Plex Mono，字号 `{typography.label}`，颜色 `{colors.fire-orange}`**（橙页上则是 55% 透明度的暗墨）。

### 排印原则
字重 900 + 小写 + 负 tracking + Barlow 的组合就是系统的声线。换成大写、切到字重 600、或拿掉负 tracking，每一项都读成另一套系统。chrome 的 IBM Plex Mono 大写 + 0.14em tracking 同样不可拆。

行高在大字号处收紧：`{typography.display}` 跑 0.88，`{typography.h1}` 跑 0.9，`{typography.h2}` 跑 1.1，直到 `{typography.lead}` 才开到 1.5+。阶梯顶部的压缩，才让展示读起来像一块整体。

## 版式

### 画布系统
画布是 `100vw × 100vh`——全视口，溢出隐藏。幻灯片在水平 `#deck` flexbox 里并排；导航水平平移 deck 容器，而不是切换 `display`。所有尺寸都相对视口（`vw` / `vh`）——没有固定的 1920×1080 网格。

### 内边距与间距阶梯
| Token | 值 | 用途 |
|---|---|---|
| `{spacing.pad-x}` | 5.5vw | 每一页的外侧水平内边距 |
| `{spacing.pad-y}` | 5.5vh | 每一页的外侧垂直内边距 |
| `{spacing.gap-lg}` | 3.5vh | 主要块之间的大垂直间距 |
| `{spacing.gap-md}` | 2vh | 兄弟元素之间的标准间距 |
| `{spacing.gap-sm}` | 1vh | 紧间距——kicker 到标题、chrome 条内部间隙 |

内边距刻意比通用编辑系统更紧。Broadside 的巨大字体需要幻灯片边缘感觉近，而不是远——字本该挤满画框。

### 页框
系统有可选页框，由两根水平发丝条组成：顶部 `slide-chrome` 条（左标签、右页码）和底部 `slide-foot` 条（镜像）。两者都是 1px 实线边框，暗页用 `{colors.border-dark}`，橙页用 `rgba(17, 17, 17, 0.2)`。内部 padding/margin 用 `{spacing.gap-sm}` 和 `{spacing.gap-md}`。

chrome 在系统的「宣言」页类型上**彻底关掉**——cover、chapter、statement、quote 和 end。那些页拿掉全部 chrome，让字占满整块场。内容页（split、stats、list、compare、chart、diagram）保留 chrome。

独立的 `broadside-num` 元素（等宽，约 1.1vw，低透明度）也可以不靠 chrome 条单独放置，作为目录式页码锚在橙色封面/章节页的左上。

## 纵深与层次

### 平面（唯一手法）
Broadside 完全平面。没有投影、没有内阴影、没有模糊抬升、没有圆角表面渐变。每个元素都坐在同一平面上。

层级由以下构成：
- **字重 + 字号对比**——主导信号。
- **1px 发丝分割线**——`slide-chrome`/`slide-foot` 边框、`stat-card` 顶边、`compare-panel` 分割线、`bar-track` 左边、`chart-baseline` 基线。
- **颜色位移**——橙对墨、墨对奶油、cream-muted 对 cream。
- **负空间**——宽裕的内边距和刻意的空区。

引入 `box-shadow`、带抬升的卡片或柔渐变会拆掉系统。平面就是编辑信号。

## 形状与处理

### 圆角
圆角**处处 0px**，除了 `nav-dot`（50%——底部那些小导航圆点）。卡片、面板、tag、图片占位、统计卡、图表柱——全是尖角矩形。

### 描边粗细
- **1px solid**——唯一的结构粗细。用于 `slide-chrome`、`slide-foot`、`stat-card` 顶边、`compare-panel` 分割线、`bar-track` 左缘、`chart-baseline`、图片图注、`rule.full` 分割线。
- **1px dashed**——只用于 `img-placeholder`，信号是「还没接上图」。
- **2px solid**——只用于小的 `rule` 强调短棒（36px 宽）和 `chapter-rule` 标记。

所有边框要么是 `{colors.border-dark}`（暗页），要么是 `rgba(17, 17, 17, 0.2)`（橙页），要么是 `{colors.fire-orange}`（暗页上的 tag 边框）。

### 装饰元素类型

**短强调线** —— 36×2px 实心条，暗页用 `{colors.fire-orange}`，橙页用 `{colors.ink-black}`。用作章节标题上方、统计上方或 kicker 旁边的视觉「分段」标记。是 Broadside 唯一的装饰。

**等宽目录编号** —— 小号 IBM Plex Mono 数字，锚在封面/章节页左上，低透明度（橙页 `rgba(17, 17, 17, 0.45)`，暗页 `{colors.cream-hint}`）。读起来像出版物目录标记。

**统计卡** —— 只带顶边的数据块：顶上 1px 实线，没有其他边框，padded 正文里是 `{typography.stat-value}`（暗页上大号橙色数字；橙页上暗墨）在 `{typography.body}`（标签）之上，再在 `{typography.caption}`（等宽注，`{colors.cream-hint}` 或暗淡墨）之上。

**对比面板对** —— 两块等宽面板，中间一根 1px 竖边。右面板可选填满 `{colors.fire-orange}`（`compare-panel-orange`）作为「之后」/ payoff 一侧；左面板在暗画布上保持透明。

**竖向柱状图** —— `bar-track` 容器只带 `border-left`（没有其他轴），柱从顶部落下，默认 `cream-hint` 填充，每张图一根柱带 `.accent` 类变成火橙。轴标签在基线下方，等宽大写。

**Fadelist** —— SPACE10 式构图：三个叠放的 Barlow-900 词，透明度递减（1.0 / 0.5 / 0.22），对面配一个超大展示标题。用于「之前 / 之中 / 之后」或「过去 / 现在 / 未来」叙事。

**引出式引文** —— 超大火橙 `{typography.quote-mark}` 字形（行高 0.6，让它坐在基线上而不是沉下去），后面是 `{typography.quote-text}`，宽度封顶约栏宽的 78%，再跟两行 `quote-attr`，姓名在上、等宽角色/机构在下。

**带边等宽 tag** —— 小号行内 pill，IBM Plex Mono 大写，1px 实线边框，padding 垂直 0.3em × 水平 0.8em。暗页上边框和文字都是 `{colors.fire-orange}`；橙页上是 40% 透明度的暗墨。

## 宜与忌

### 宜
- 每一个 Barlow 展示、标题、导语和正文元素都用句首大写。小写展示是 Broadside 最鲜明的单一选择。
- 每一个 chrome 元素都用 IBM Plex Mono 大写，tracking 0.1em+：页码、kicker、标签、tag、轴标签、来源注、列表标记。
- 让 `{colors.fire-orange}` 成为暗页上的唯一强调——kicker、强调统计值、列表 `/` 标记、图表主柱、开引号、`rule` 短棒。
- 在封面、章节和宣言式 payoff 页上让橙色成为*整页背景*。那些页类型上把它当环境，不只当强调。
- 列表上限三条。Broadside 看重冲击密度，不看信息密度。
- 每一个 Barlow 展示瞬间都加负字距——最大号 -0.04em，h2 上 -0.02em。
- 所有结构分割用 1px 发丝边框（暗页 `{colors.border-dark}`，橙页 `rgba(17,17,17,0.2)`）。它们是系统仅有的层级 chrome。
- 在 cover、chapter、statement、quote 和 end 页上关掉 slide-chrome 和 slide-foot——让字从边到边呼吸。
- 在橙色封面/章节页左上放 `broadside-num` 目录编号，作为出版物式标记。
- 每一条列表项都用火橙等宽 `/` 字形作标记。

### 忌
- 不要把展示或标题字重的 Barlow 改成大写。13vw 的大写 Barlow 读起来完全是另一套设计系统。
- 不要引入第二强调色。橙色是*那一个*颜色——加蓝、黄或绿强调会拆掉抗议海报身份。
- 不要加投影、模糊抬升或圆角表面。Broadside 严格平面——纵深来自字和 1px 线。
- 不要在橙页上用奶油色文字。「火上落墨」规则是绝对的：橙页标题和正文用 `{colors.ink-black}`。
- 不要给 Barlow 配衬线搭档。单字体单体是身份的一部分。
- 不要给卡片、tag、面板或统计块加圆角。系统里唯一的圆形状是小导航点。
- 不要在一页里塞进超过一个展示瞬间。Broadside 是一句陈述、一根线、呼吸空间——不是杂志式层层构图。
- 不要用 Barlow 渲染 chrome 元素。chrome 专属 IBM Plex Mono 大写。
- 不要引入第三套表面色域。只有两套：暗和橙。奶油/纸页不存在。
- 不要用斜体或下划线。强调只通过字重、字号或橙色达成。

## 响应式行为

这是一套视口流体的 1920×1080 演示系统，全程用 `vw`/`vh`。没有固定像素断点。每个排印 token、内边距值和组件尺寸都随视口线性缩放。

### 缩放行为
- 展示标题（`{typography.display}`）从约 1066 宽视口的 ~138px 缩放到 1920 宽的 ~250px。
- 正文（`{typography.body}`）在同一区间从 ~13px 到 ~23px。
- 外侧内边距（`{spacing.pad-x}` 5.5vw）从 ~59px 到 ~106px。
- 所有边框固定在 1px 或 2px，不缩放。

### 演示行为
- 前进：`ArrowRight`、`ArrowDown`、`Space` 或 `PageDown`。
- 后退：`ArrowLeft`、`ArrowUp` 或 `PageUp`。
- 导航以 `cubic-bezier(0.77, 0, 0.175, 1)` 缓动、0.8s，水平平移 deck 容器。
- 元素入场动画（`data-anim="fade-up"`、`fade-in`、`reveal-right`、`reveal-left`、`scale-in`）每次幻灯片变成 `.is-active` 都会重放，按 `data-delay`（0 到 6）错开。
- 导航点在底部居中，等宽页码计数在右下。

### 打印 / 导出
源码没有显式处理。每一页是 `100vw × 100vh` 块；导出工作流应对每页出 1920×1080 PNG/PDF。

## 中日韩与国际内容

用这套模板做中文（或其他 CJK）内容时，把拉丁字体栈换成对等的中文配对，并套用通用 CJK 调整。所有推荐中文字体经 CDN 加载——无需安装。

### 推荐中文配对

| 角色 | 拉丁（默认） | 中文对位 |
|---|---|---|
| Display / h1 / h2 / h3 / stat-value / quote / fadelist | Barlow 700–900（小写，负 tracking） | 思源宋体 Noto Serif SC 900 |
| Lead / body / caption | Barlow 400 | 霞鹜文楷 LXGW WenKai 400 |
| Label / kicker / tag / 页码 / 列表标记 | IBM Plex Mono 500（大写，0.14em tracking） | 思源黑体 Noto Sans SC 500（无 transform，无 tracking） |

### 中英混排策略

**策略 A** —— 每个角色一套 CJK 家族，自带拉丁字形覆盖。每一次展示和标题角色用 **思源宋体 Noto Serif SC** 字重 900；正文和导语用 **霞鹜文楷 LXGW WenKai** 字重 400；chrome（kicker、标签、页码、列表标记）用 **思源黑体 Noto Sans SC** 字重 500。三套面孔都带拉丁字形，能干净地挨着汉字。衬线/手写/无衬线对比松散呼应 Broadside 的 display/正文/等宽区分，尽管源码全程用 Barlow。

### 加载

加到模板的 `<head>`：

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;500;700;900&family=Noto+Sans+SC:wght@400;500&family=LXGW+WenKai+TC&display=swap" rel="stylesheet">
```

### 通用 CJK 调整

- **行高**：相对拉丁规格提高约 15–25%。正文 1.75–1.85（从 1.6 上调），展示 1.15–1.25（从 Barlow 展示非常紧的 0.88–0.9 上调）。拉丁模板把 quote-mark token 的展示压到 0.6；那种压缩下 CJK 字符会完全重叠。展示至少开到 1.0。
- **字距**：每一段 CJK 跑段设为 0。模板在 Barlow 展示上 −0.02 到 −0.04em 的负 tracking 会让 CJK 笔画重叠；IBM Plex Mono chrome 上 +0.14em 的正 tracking 在方块字形上读起来像裂缝。
- **大小写变换**：不要对中文套 `uppercase`——CJK 没有大小写。拉丁原版里每一个 IBM Plex Mono 标签、kicker、tag、页码和列表标记都用 `text-transform: uppercase`；CJK 跑段要去掉。
- **标点**：用全角中文标点 （，。：；！？「」（））。
- **展示标题不加句号**：中文排印惯例在展示级标题省略末尾 。。对 Broadside 的巨大展示瞬间尤其重要——13vw 的拖尾 。 在视觉上很扰。
- **CJK 与拉丁之间的空格（盘古之白）**：每个汉字与相邻拉丁字符或数字之间插入一个 ASCII 空格。写 `2024 大字海报`，不要写 `2024大字海报`。
- **一句一句一种字体**：思源宋体以统一衬线风格覆盖 CJK 和拉丁字形做展示；霞鹜文楷覆盖正文两边。不要让浏览器在中文句子中间把 ASCII 字符回退到 Barlow。

### 本系统的美学说明

Broadside 最鲜明的单一决定是 **13vw 展示字号、字重 900 的小写 Barlow**。小写展示把这套系统从通用野兽派片子里分开。在 CJK 里那个信号彻底消失——中文没有大小写。系统能补偿，因为它的身份 **80% 是结构 + 颜色**：双色域表面系统（暗 / 橙）、唯一的火橙强调、平面、1px 发丝分割线、`/` 等宽列表标记、宣言页关掉 chrome，以及负空间即构图的哲学，都能干净迁移。

最接近 Barlow「单体厚重 grotesque」色域的中文面孔是 **思源宋体字重 900**——但是厚重衬线展示，而不是厚重无衬线展示。这是一次刻意的色域位移：抗议海报尺度上的厚重中文衬线，读起来更像「大幅传单印刷海报」（系统真正的文化参照），比厚重中文无衬线更可信，后者更像「企业标牌」。正文字体上，**霞鹜文楷 LXGW WenKai** 带来手写/书法暖意，配得上编辑-抗议色域；如果需要更体制化的正文，换成思源宋体 400。

用小号字（等价 0.72vw）和 kicker/标签上的橙色，保住 chrome 的「盖章元数据」声线。IBM Plex Mono 大写 + tracking 处理在 CJK 里两个信号都会丢，但橙色本身已经足够做 chrome 识别。`/` 列表标记即使在中文语境里也可以留作拉丁斜杠字符——它是图形标记，不是语言元素。

### 已知 CJK 缺口

- **没有 CDN 中文面孔能匹配 Barlow 的单体 grotesque + 小写身份。** Barlow 在这套系统里的鲜明选择是重字重的小写展示——CJK 没有对等的表达杠杆。系统的「抗议海报小写呐喊」性格会软成「厚重衬线宣言」。双色域颜色系统（暗 / 橙）和唯一的火橙强调，自己就能扛起抗议海报身份。
- **没有 CDN 中文等宽面孔来扛 chrome 声线。** IBM Plex Mono 的角色（kicker、标签、页码、`/` 列表标记）依赖等宽节奏 + 大写 + 0.14em tracking。思源黑体字重 500、tracking 0 是最接近的匹配，但丢掉「目录标记」信号。保住橙色和小字号；颜色和尺度做 chrome 识别工作。
- **霞鹜文楷在受限网络上可能加载失败。** Google Fonts CDN 对繁体变体（LXGW WenKai TC）服务可靠；简体变体也可经 cn-fontsource 获得。正文栈里始终带上 `'Noto Serif SC', serif` 作回退。
- **10vw、行高 0.6 的 quote-mark 字形是拉丁引号惯例。** 中文排印用 「」 或 『』 框，而不是超大开引号字形。中文引出式引文可考虑把超大火橙 quote-mark 换成 8vw 的全角 「 字符，或干脆丢掉装饰引号字形，靠橙色 + 更大字号来信号「这是引文」。

## 迭代指南

1. 每一张新内容页以等宽大写火橙 `kicker` 开场，后面接 Barlow 小写 `{typography.h2}` 标题。不要跳过 kicker——它是系统内容页的 chrome 信号。
2. 每一张封面、章节、statement-payoff 或收束页走橙色域。不要把橙色用在内容/数据页上——橙色留给宣言瞬间。
3. 新统计卡用 `stat-card` 只带顶边的模式，`{typography.stat-value}` 在暗页上橙色、橙页上墨色。不要给统计卡加底边或全边框。
4. 新列表用火橙等宽 `/` 标记。上限三条。
5. 新图表用 `bar-track` 竖柱模式，每张图一根火橙强调柱；其余柱用 `{colors.cream-hint}`。
6. 新引文用超大火橙 `{typography.quote-mark}` 开字形，后面接最多 78% 宽的 `{typography.quote-text}`。
7. 橙页上的标题永远是 `{colors.ink-black}`。橙页上没有奶油标题。
8. 新 tag 用 `tag` 样式：暗页上 1px 火橙边框 + 火橙等宽大写文字；橙页上 40% 透明度暗墨。
9. 系统有九种经典版式——cover、chapter、statement、split、stats、quote、list、compare、end——外加 fadelist、chart 和 diagram 扩展。新版式应按这一页是宣言还是承载内容，遵守 chrome/无 chrome 规则。

## 已知缺口

- Broadside 的 `.light` 幻灯片类被故意覆盖成暗色——源码注释确认「没有奶油/白页」。任何使用 `.light` 的尝试都会回退到暗色域。
- Noto Sans SC 在每个字体栈里作为 CJK 回退，但系统并不是为混排拉丁/CJK 标题设计的；CJK 展示字号上的行高行为可能需要逐页调整。
- 列表标记字形（`/`）通过 `::before` 设成 IBM Plex Mono——换成别的字形要改 CSS，不是改标记。
- 柱状图 `bar-fill` 高度在源码里用 `style="height: NN%"` 行内样式；没有数据绑定层。
- fadelist 和柱状图版式不在经典「9 种版式」注释块里；它们是文档系统之外追加的扩展。
- 图片占位用虚线 `{colors.border-dark}` 边框和等宽大写标签——换成真正的 `<img src>` 时保持同样的 55vh 高度以维持版式。
- 色板里存在 `c-fg-light` token（`#111111`）用于「浅色主题主文字」，但浅色主题被关掉，这个 token 在渲染输出里实际上没用。
- 系统加载三套 Google Fonts 家族（Barlow、IBM Plex Mono、Noto Sans SC）及多个字重——初次渲染需要字体加载成功，以免回退到 Times New Roman。
