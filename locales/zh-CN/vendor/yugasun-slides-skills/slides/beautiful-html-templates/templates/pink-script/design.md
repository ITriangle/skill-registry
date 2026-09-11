---
version: alpha
name: Pink Script (After Hours)
description: A nocturnal couture editorial system rendered in hot fuchsia ink on dim warm-black paper, with a soft film-grain overlay and a hairline interior frame. DM Serif Display carries every script and editorial moment at sizes up to 600px; Inter at weight 300 carries the body voice; JetBrains Mono carries the boutique-catalog metadata. The aesthetic borrows from glossy fashion magazine spreads, late-night perfume advertising, and the editorial pages of high-end zines — closer to a Maison's seasonal lookbook than a startup deck.

colors:
  ink-deep: "#060507"
  ink-violet: "#0F0D11"
  paper-blush: "#F5EDF1"
  pink: "#ED3D8C"
  pink-light: "#FF66A8"
  pink-deep: "#B81D67"
  line-pink: "rgba(237, 61, 140, 0.32)"
  mute-paper: "rgba(245, 237, 241, 0.55)"
  hair-paper: "rgba(245, 237, 241, 0.14)"

color-aliases:
  c-bg: ink-deep
  c-fg: paper-blush
  c-accent: pink
  c-line: line-pink

typography:
  script-huge:
    fontFamily: "DM Serif Display, serif"
    fontSize: 540px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -0.01em
    color: "{colors.pink}"
  script-section:
    fontFamily: "DM Serif Display, serif"
    fontSize: 600px
    fontWeight: 400
    lineHeight: 0.82
    letterSpacing: -0.02em
    color: "{colors.pink}"
  script-giant:
    fontFamily: "DM Serif Display, serif"
    fontSize: 360px
    fontWeight: 400
    lineHeight: 1.05
    color: "{colors.pink}"
  script-cover:
    fontFamily: "DM Serif Display, serif"
    fontSize: 280px
    fontWeight: 400
    lineHeight: 1.02
    letterSpacing: -0.015em
    color: "{colors.pink}"
  script-large:
    fontFamily: "DM Serif Display, serif"
    fontSize: 220px
    fontWeight: 400
    lineHeight: 1.04
    color: "{colors.pink}"
  script-med:
    fontFamily: "DM Serif Display, serif"
    fontSize: 156px
    fontWeight: 400
    lineHeight: 1.04
    color: "{colors.pink}"
  script-sm:
    fontFamily: "DM Serif Display, serif"
    fontSize: 132px
    fontWeight: 400
    lineHeight: 1.06
    color: "{colors.pink}"
  serif-cta:
    fontFamily: "DM Serif Display, serif"
    fontSize: 140px
    fontWeight: 400
    lineHeight: 1.04
    letterSpacing: -0.015em
    color: "{colors.paper-blush}"
  serif-h2:
    fontFamily: "DM Serif Display, serif"
    fontSize: 132px
    fontWeight: 400
    lineHeight: 1.06
    color: "{colors.paper-blush}"
  serif-quote:
    fontFamily: "DM Serif Display, serif"
    fontSize: 92px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -0.005em
    color: "{colors.paper-blush}"
  serif-chart-h:
    fontFamily: "DM Serif Display, serif"
    fontSize: 90px
    fontWeight: 400
    lineHeight: 1.06
    color: "{colors.paper-blush}"
  serif-section-h:
    fontFamily: "DM Serif Display, serif"
    fontSize: 88px
    fontWeight: 400
    lineHeight: 1.06
    color: "{colors.paper-blush}"
  serif-stat:
    fontFamily: "DM Serif Display, serif"
    fontSize: 116px
    fontWeight: 400
    lineHeight: 0.9
    color: "{colors.pink}"
  serif-toc-num:
    fontFamily: "DM Serif Display, serif"
    fontSize: 64px
    fontWeight: 400
    lineHeight: 1.0
    color: "{colors.pink}"
  serif-toc-title:
    fontFamily: "DM Serif Display, serif"
    fontSize: 56px
    fontWeight: 400
    lineHeight: 1.05
    color: "{colors.paper-blush}"
  serif-quote-attr:
    fontFamily: "DM Serif Display, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.05
    color: "{colors.paper-blush}"
  serif-process-h:
    fontFamily: "DM Serif Display, serif"
    fontSize: 38px
    fontWeight: 400
    lineHeight: 1.05
    color: "{colors.paper-blush}"
  serif-matrix-label:
    fontFamily: "DM Serif Display, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
    color: "{colors.paper-blush}"
  body:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 300
    lineHeight: 1.55
    color: "{colors.paper-blush}"
  body-muted:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 300
    lineHeight: 1.5
    color: "{colors.mute-paper}"
  body-toc-desc:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 300
    lineHeight: 1.4
    color: "{colors.mute-paper}"
  mono-runner:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 24px
    fontWeight: 400
    letterSpacing: 0.14em
    textTransform: uppercase
  mono-kicker:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 22px
    fontWeight: 400
    letterSpacing: 0.14em
    textTransform: uppercase
    color: "{colors.pink}"
  mono-label:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 22px
    fontWeight: 400
    letterSpacing: 0.14em
    textTransform: uppercase
    color: "{colors.paper-blush}"
  mono-cover-pre:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 28px
    fontWeight: 400
    letterSpacing: 0.42em
    textTransform: uppercase
    color: "{colors.paper-blush}"
  mono-pill:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 16px
    fontWeight: 400
    letterSpacing: 0.08em
    textTransform: uppercase

spacing:
  edge-x: 60px
  edge-top-chrome: 60px
  edge-bottom-chrome: 60px
  content-top: 140px
  content-bottom: 140px
  inner-frame-inset: 36px

canvas:
  width: 1920px
  height: 1080px

components:
  slide-surface:
    background: "radial-gradient(ellipse 90% 70% at 30% 30%, #1A1218 0%, #0A0709 55%, #050306 100%)"
    description: "Universal dark surface — radial ellipse from a slightly warmer #1A1218 in the upper-left fading to near-black in the lower-right. The off-center light source is part of the system's identity."
  film-grain:
    selector: ".slide::before"
    background: "fractalNoise SVG via data URI, baseFrequency=0.9, octaves=2"
    opacity: 0.08
    mixBlendMode: screen
    description: "Subtle film grain overlay on every slide via ::before. Opacity 0.08 with screen blend — barely visible but reads as photographic grain rather than digital flatness."
  hairline-frame:
    selector: ".slide::after"
    position: "absolute; inset: 36px"
    border: "1px solid {colors.hair-paper}"
    description: "1px paper-blush-at-14%-opacity interior frame inset 36px from each slide edge. Always present. Functions as the editorial border of the magazine page."
  runner:
    position: "absolute; top: 60px; left: 60px; right: 60px"
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 24px
    letterSpacing: 0.14em
    textTransform: uppercase
    description: "Top metadata runner — brand name on left (colored pink), section / chapter tag on right (muted paper-blush)."
  footer:
    position: "absolute; bottom: 60px; left: 60px; right: 60px"
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 24px
    letterSpacing: 0.14em
    textTransform: uppercase
    description: "Bottom metadata runner — source / confidentiality on left, page-position (e.g. '03 / 09') on right. Page-position has paper-blush base text with a pink ::em for the current number."
  pink-rule:
    height: 1px
    background: "{colors.pink}"
    opacity: 0.45
    description: "Hairline pink rule for soft section separators."
  hair-rule:
    height: 1px
    background: "{colors.paper-blush}"
    opacity: 0.25
    description: "Hairline paper rule for muted section separators."
  pink-glow:
    textShadow: "0 0 80px rgba(237, 61, 140, 0.18)"
    description: "Soft pink halo behind large script titles. Applied via text-shadow on hero serif text only."
  pink-glow-mega:
    textShadow: "0 0 120px rgba(237, 61, 140, 0.22)"
    description: "Stronger pink halo for section-divider mega numerals."
  callout-rail:
    borderLeft: "1px solid {colors.pink}"
    paddingLeft: 24px
    description: "Pink left rule with right-aligned content — used as a callout container beside a chart, beside a chapter explanation."
  matrix-cell:
    padding: "16px 24px"
    borderBottom: "1px solid {colors.line-pink}"
    fontFamily: "Inter, sans-serif"
    fontSize: 22px
    fontWeight: 300
    color: "{colors.paper-blush}"
    description: "Comparison matrix cell. Rows are separated by hairline pink-at-32% rules; columns are gap-separated, no vertical borders."
  matrix-cell-us:
    background: "rgba(237, 61, 140, 0.08)"
    description: "Highlighted matrix row variant — soft pink wash to mark the 'our' column."
  pill-outline:
    border: "1px solid {colors.pink}"
    color: "{colors.pink}"
    padding: "6px 14px"
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 16px
    letterSpacing: 0.08em
    textTransform: uppercase
    description: "Hollow pink pill — 1px pink border with pink mono text. The default pill state."
  pill-solid:
    background: "{colors.pink}"
    color: "{colors.ink-deep}"
    border: "1px solid {colors.pink}"
    fontWeight: 500
    description: "Solid pink pill — pink fill, deep-ink text. Affirmative / featured state."
  pill-dim:
    borderColor: "{colors.hair-paper}"
    color: "{colors.mute-paper}"
    description: "Dim pill — muted paper border, muted paper text. The de-emphasized state."
  qr-tile:
    width: 180px
    height: 180px
    background: "{colors.paper-blush}"
    padding: 12px
    description: "QR-code container — solid paper-blush square with 12px white padding around the SVG QR. The only large light-surface element in the system."
  stat-row:
    display: "grid; columns: 240px 1fr"
    borderBottom: "1px solid {colors.hair-paper}"
    paddingBottom: 16px
    description: "Stat row pattern — large pink serif figure on the left (with a paper-blush superscript unit) paired with a mono label and Inter description on the right. Rows are separated by 1px paper hairline."
  callout-num:
    fontFamily: "DM Serif Display, serif"
    fontSize: 120px
    lineHeight: 0.9
    color: "{colors.pink}"
    description: "Chart callout number — large pink serif numeral with smaller paper-colored unit suffix."
  arrow-glyph:
    width: 24px
    height: 24px
    color: "{colors.pink}"
    description: "Small pink right-arrow SVG used between process steps."
---

## Frontend Slides 固定舞台策略

当 `frontend-slides` skill 使用本设计系统时，把最终文稿生成为**固定 1920×1080 舞台**，均匀缩放到浏览器视口。文稿应在每一块屏幕上（包括手机）保住 16:9 幻灯片画布；可以 letterbox 或 pillarbox，但不应为移动端重排幻灯片内容。

本策略优先于本文后面描述的任何源模板响应式行为。如果后面某节说原模板是视口流体的，只把它当源历史，不要当成 `frontend-slides` 的目标生成模型。

即便源模板最初用视口流体 CSS 实现，例如 `100vw`、`100vh`、`vw`、`vh` 或 `clamp()`，本策略仍然适用。把那些值当设计比例，翻译进 1920×1080 舞台坐标，而不是生成文稿里的实时响应式规则。

最终输出用 `deck-stage.js` 或等效的行内舞台缩放器：每页按 1920×1080 渲染，用一次 transform 缩放整个舞台，并核对渲染截图里的文字溢出和面板重叠。


## 概览

Pink Script 是一套**夜间高定编辑系统**，建立在单一气氛前提上：深暖黑表面，被左上略暖的 #1A1218 椭圆从左上照亮，向右下淡到近黑。偏心光源读作摄影棚柔光箱扫到杂志跨页的一角。之上，8% 不透明度、screen 混合的微妙胶片颗粒叠层，加上深夜编辑摄影的颗粒感。这层表面里坐着 1px 发丝内框（paper-blush 14% 不透明度，距每边内缩 36px）——每一页的编辑边框。没有点亮的渐变、胶片颗粒和内框，系统塌成扁平深色 UI。

字体栈是刻意的三声线编辑配对。**DM Serif Display** 承担每一个编辑瞬间——手写标题（当作系统的「粉红 script」）、衬线标题、统计数字、引文。它只跑字重 400；这张脸只有一个字重，那就是系统的展示声线。衬线从 32px（表格标签）自由缩放到 600px（章节分隔数字）。**Inter** 字重 300 承担每一个正文段落、导语、描述和图注——超细几何无衬线是系统冷静的散文声线。**JetBrains Mono** 字重 400 承担每一个标签、kicker、页码、坐标轴标记、runner 和页脚字符串——始终全大写，正字距至少 0.08em。

色板锚定在单一招牌上：**热粉 fuchsia**（`{colors.pink}` — #ED3D8C）对照深暖黑（`{colors.ink-deep}` — #060507）。粉是整套编辑强调系统；它作为 script 标题色、kicker 色、图表线条色、pill 描边、paper-blush 标题里的行内 `<em>` 开关、callout 数字、规则线色，以及英雄 script 标题背后的柔光晕（text-shadow glow）出现。**Paper-blush**（`{colors.paper-blush}` — #F5EDF1）是次文字色——用于编辑无衬线标题、段落文案，以及任何应读作墨水而不是高亮的瞬间。55% 不透明度的闷 paper 处理次文字；14% 的发丝 paper 处理分隔和内框。

纵深通过三层机制做出：**偏心径向渐变表面**（从左上点亮）、**微妙胶片颗粒叠层**（8% 不透明度，screen 混合，加摄影纹理），以及英雄 script 标题上的**粉光晕 text-shadow**（柔 80–120px 光晕，模拟大号霓虹饱和字体在相纸上的漏光）。任何元素都没有投影；纵深是气氛和摄影的，不是结构的。

**密度哲学：疏到中等，带一个英雄瞬间。** 当单个超大 script 锚定一页、其余是慷慨负空间、再点缀 2–4 个小编辑碎片（一条 runner、一个 kicker、一段、一个页脚）时，Pink Script 读起来才优雅。英雄 script 占画布 60–70%、支撑文案安静绕着剩余边距转，是对的。把画布塞满多个等权区域，会打破深夜杂志感。例外是统计页（5 行统计并排）、对照矩阵（满网格表）和系统页（多面板）——这些页按设计更密，因为编辑目的是查阅，不是诗。流程和 TOC 页是填满的，但始终分层：巨大 script 页头主宰，较小卡片行在下面绕转。

**关键特征：**
- 深暖黑表面（`{components.slide-surface}`），由径向渐变椭圆从左上点亮。
- 每一页微妙胶片颗粒叠层（`{components.film-grain}`）——不透明度 0.08，screen 混合。
- 1px paper-blush 内框（`{components.hairline-frame}`）距每边内缩 36px，出现在每一页。
- 热 fuchsia 粉（`{colors.pink}`）是单一彩色强调——用作 script 色、kicker 色、线条色、pill 轮廓、行内强调，以及英雄 script 背后的柔光晕。
- DM Serif Display 承担每一个编辑瞬间，从 32px 缩放到 600px。没有第二张展示脸。
- Inter 字重 300 承担每一个正文段落——超细无衬线是系统的散文声线。
- JetBrains Mono 全大写、字距 0.08em+ 承担每一个标签、页码和 runner 字符串。
- 顶栏 runner 和底栏页脚 chrome 出现在每一页；runner 品牌文字是粉，chrome 其余都是闷 paper-blush。
- 行内 `<em>` 元素把 paper-blush 衬线标题切到粉——系统的编辑强调机制。

## 颜色

### 色板

- **Ink Deep**（`{colors.ink-deep}` — #060507）：基础表面色。近黑带微暖偏。叠上径向渐变后，锚定深色编辑表面。
- **Ink Violet**（`{colors.ink-violet}` — #0F0D11）：略抬起的深色带紫偏。预留交替深色——可用，但当前幻灯片类型里很少用。
- **Paper Blush**（`{colors.paper-blush}` — #F5EDF1）：暖偏白带微粉底。主编辑文字色、QR-tile 背景，以及次高亮表面。读作纸而不是纯白。
- **Pink**（`{colors.pink}` — #ED3D8C）：热 fuchsia。系统单一彩色强调。用作 script 标题色、kicker 色、行内 `<em>` 色、callout 数字色、规则线色、图表线条色、pill 轮廓色，以及光晕 text-shadow 的源色。
- **Pink Light**（`{colors.pink-light}` — #FF66A8）：更亮的粉。已定义但当前幻灯片类型未用。
- **Pink Deep**（`{colors.pink-deep}` — #B81D67）：更深的粉。已定义但当前幻灯片类型未用。
- **Line Pink**（`{colors.line-pink}` — rgba(237,61,140,0.32)）：32% 不透明度的粉，用于表格行分割和图表坐标轴线。
- **Mute Paper**（`{colors.mute-paper}` — rgba(245,237,241,0.55)）：55% 的 paper-blush，用于闷正文和元数据。
- **Hair Paper**（`{colors.hair-paper}` — rgba(245,237,241,0.14)）：14% 的 paper-blush，用于内发丝框、闷 pill 描边和 toc-row 分割。

### 默认

- **默认幻灯片表面**：`{components.slide-surface}` —— 点亮的暖黑径向渐变。始终如此。
- **默认胶片颗粒**：`{components.film-grain}`，不透明度 0.08，screen 混合。不可省略。
- **默认内框**：`{components.hairline-frame}`，1px paper-blush 14%。不可省略。
- **默认主标题色**：英雄 script 瞬间用 `{colors.pink}`。应读作墨水（不是高亮）的编辑标题用 `{colors.paper-blush}`。
- **默认正文字色**：主文案用 `{colors.paper-blush}`；闷导语和描述用 `{colors.mute-paper}`。
- **默认 kicker 色**：`{colors.pink}`。eyebrow 标签始终是粉。
- **默认标签 / 元数据色**：runner、页脚和元数据用 `{colors.mute-paper}`。
- **默认线条 / 分割色**：柔粉规则线用 `{colors.pink}` 45% 不透明度；闷发丝用 `{colors.hair-paper}`。
- **paper-blush 标题内的默认强调机制**：用 `<em>` 包起来，把那个词切到 `{colors.pink}`（font-style 保持直立）。
- **默认 pill 状态**：outline（`{components.pill-outline}`）——粉描边、粉文字。
- **默认图表系列**：主系列粉线；次系列闷 paper-blush 虚线。

粉是常规使用里唯一的彩色；其他粉变体（Pink Light、Pink Deep）是预留的。不要引入第二彩色强调——Pink Script 的身份就是单色地粉。

## 字体

### 字族

系统加载三套 web 字体：**DM Serif Display**（字重 400，仅 italic 0）承担从 32px 到 600px 的每一个编辑 / 展示瞬间；**Inter**（字重 300、400、500、600）承担每一个正文段落和导语；**JetBrains Mono**（字重 400、500）承担每一个标签、runner、页脚和元数据字符串。

每张脸的情感声线都不同：
- DM Serif Display 读作**编辑的、香水杂志的、深夜高定** —— 这张脸有优雅高对比笔画，系统用它承担每一个应觉得文学或杂志排印的瞬间。
- Inter 字重 300 读作**冷静、当代、中性优雅** —— 超细字重匹配编辑语气，又不跟衬线抢。
- JetBrains Mono 读作**档案的、精品目录的、版次编号的** —— 等宽全大写声线处理版次号、页码位置、runner 品牌文字和章节标签。

一条关键行内混用规则：**DM Serif Display 标题里的 `<em>` 元素把颜色切到 `{colors.pink}`**（font-style 归一成直立）。这是系统的主标题强调——paper-blush 衬线文字里的粉墨。

第二条行内混用规则：**统计数字里的 `<sup>` 元素按 ~36px、`{colors.paper-blush}` 渲染**，带轻微顶 padding 偏移——用于单位后缀（%、×、M）。

### 字号阶梯

| Token | 字号 | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.script-section}` | 600px | DM Serif Display | 400 | 章节分隔 mega 数字 |
| `{typography.script-huge}` | 540px | DM Serif Display | 400 | 功能展示位置上的英雄 script |
| `{typography.script-giant}` | 360px | DM Serif Display | 400 | 大号编辑 script 标题 |
| `{typography.script-cover}` | 280px | DM Serif Display | 400 | 封面 script 标题 |
| `{typography.script-large}` | 220px | DM Serif Display | 400 | TOC 主 script |
| `{typography.script-med}` | 156px | DM Serif Display | 400 | 流程页主标题 |
| `{typography.serif-cta}` | 140px | DM Serif Display | 400 | 收束 CTA 标题（paper-blush 色） |
| `{typography.script-sm}` | 132px | DM Serif Display | 400 | 统计页标题、矩阵标题 |
| `{typography.serif-stat}` | 116px | DM Serif Display | 400 | 统计行数字 |
| `{typography.callout-num}` | 120px | DM Serif Display | 400 | 图表 callout 数字 |
| `{typography.serif-quote}` | 92px | DM Serif Display | 400 | 引文页正文 |
| `{typography.serif-chart-h}` | 90px | DM Serif Display | 400 | 图表页标题 |
| `{typography.serif-section-h}` | 88px | DM Serif Display | 400 | 章节分隔支撑标题 |
| `{typography.serif-toc-num}` | 64px | DM Serif Display | 400 | TOC 行数字 |
| `{typography.serif-toc-title}` | 56px | DM Serif Display | 400 | TOC 行标题 |
| `{typography.serif-quote-attr}` | 48px | DM Serif Display | 400 | 引文归属名 |
| `{typography.serif-process-h}` | 38px | DM Serif Display | 400 | 流程步骤标题 |
| `{typography.serif-matrix-label}` | 32px | DM Serif Display | 400 | 矩阵行标签 |
| `{typography.body}` | 24px | Inter | 300 | 标准正文段落 |
| `{typography.body-muted}` | 22px | Inter | 300 | 闷导语和描述 |
| `{typography.body-toc-desc}` | 24px | Inter | 300 | TOC 行描述 |
| `{typography.mono-runner}` | 24px | JetBrains Mono | 400 | 顶栏 runner 和底栏页脚 |
| `{typography.mono-kicker}` | 22px | JetBrains Mono | 400 | 粉 kicker eyebrow |
| `{typography.mono-label}` | 22px | JetBrains Mono | 400 | 标准 paper-blush 标签 |
| `{typography.mono-cover-pre}` | 28px | JetBrains Mono | 400 | 封面前导行（宽字距 0.42em） |
| `{typography.mono-pill}` | 16px | JetBrains Mono | 400 | Pill 文字 |

### 默认

- **默认主内容标题**：`{typography.script-sm}`（132px）——当这一页是带强标题的内容瞬间。
- **默认封面 / 开场标题**：`{typography.script-cover}`（280px）——封面 script lockup。
- **默认章节分隔 mega 数字**：`{typography.script-section}`（600px）。
- **默认正文段落**：`{typography.body}`（24px Inter 300）。
- **默认闷导语 / 描述**：`{typography.body-muted}`（22px Inter 300，mute-paper 色）。
- **默认标签 / kicker**：`{typography.mono-kicker}`（22px JetBrains Mono，粉）。
- **默认页脚 / runner**：`{typography.mono-runner}`（24px JetBrains Mono）。
- **默认统计数字**：`{typography.serif-stat}`（116px）配 36px paper-blush `<sup>` 做单位。
- **任何展示元素的默认字重**：400（DM Serif Display 只有一个字重）。
- **正文默认字重**：300。

拿不准时，规范模式是：22px 粉 kicker + 132–156px DM Serif Display 标题（若需额外强调，用 `<em>` 包一个词成粉）+ 22–24px Inter 300 段落，闷 paper-blush。那三元素模式是系统最可靠的节奏。

### 招牌处理

对应元素类型一旦用上，这些处理**不可省略**：

- **每一页都带着径向渐变表面、胶片颗粒叠层，以及 1px paper-blush 内框。** 三者一起。拿掉任何一个，编辑杂志读法就塌。
- **每一个英雄 script 元素（280px 及以上）都带着粉光晕 text-shadow。** 英雄 script 用 `{components.pink-glow}`（80px 模糊）；章节分隔 mega 数字用 `{components.pink-glow-mega}`（120px 模糊）。光晕模拟霓虹饱和印刷的漏光。
- **每一个 script 颜色都是 `{colors.pink}`。** 其他颜色的 DM Serif Display 不是「script」——它变成「衬线标题」。粉颜色就是本系统里定义 script vs. 标题的东西。
- **Paper-blush 衬线标题可以通过 `<em>` 把一个词切到粉** —— 这是系统的标题强调机制。`<em>` 保持直立（font-style: normal）。
- **DM Serif Display 标题始终有 `padding-bottom: .1em`（最大 script 用 `.12em`）。** 这补偿衬线下伸，让视觉基线对齐读得正确。
- **所有 JetBrains Mono 都是全大写，正字距至少 0.08em**（大多数 chrome 和标签用 0.12–0.18em；封面前导用 0.42em）。
- **正文始终是 Inter 字重 300。** 其他字重的 Inter 不是正文——切到 400 读成另一种语气。
- **Kicker 始终是粉**，用 `{colors.pink}`。eyebrow 颜色不可商量。
- **左边 runner 品牌文字始终是粉；右边 meta 始终是闷 paper-blush。** 粉品牌文字是系统持续的身份信号。
- **页码位置页脚用 paper-blush 底字，当前数字用粉 `<em>`。** 格式：`<span>03 / 09</span>`，其中 `03` 包在 `<em>` 里渲染成粉。

### 排印原则

Pink Script 的节奏是**超大粉 script + paper-blush 衬线段落标题 + 闷 Inter 散文 + 小号等宽编辑标签**。换任何一声线（例如 script 用 Inter，或正文用 DM Serif）都会塌掉系统的编辑声线。衬线从 32px 自由缩放到 600px；按这一页的英雄瞬间选字号，不要按固定阶梯。

不用斜体字形（DM Serif Display 确实有斜体，但模板没加载）。`<em>` 标签被改造成粉换色开关。不用下划线。DM Serif Display 没有粗体字重，用粗 Inter 做正文会打破冷静散文声线。

## 布局

### 画布系统

系统瞄准**固定 1920×1080 画布**，渲染在 `<deck-stage>` web component 里。所有尺寸像素固定；舞台负责按比例缩放。

大多数页面用**绝对定位**和边缘锚定元素。标准内容区是 `inset: 140px 60px 140px 60px` —— 顶部 140px 留给 runner + 标题区，底部 140px 留给页脚，左右 60px 边缘边距。

### 内边距与锚定

| 锚点 | 值 | 用途 |
|---|---|---|
| `edge-x` | 60px | 内容左右边缘边距 |
| `edge-top-chrome` | 60px | runner chrome 的顶内缩 |
| `edge-bottom-chrome` | 60px | 页脚 chrome 的底内缩 |
| `content-top` | 140px | 幻灯片正文内容顶内缩（runner 之下） |
| `content-bottom` | 140px | 幻灯片正文内容底内缩（页脚之上） |
| `inner-frame-inset` | 36px | 发丝内框内缩 |

### Chrome 画框

每一页带着 **顶栏 runner**，上 60px / 左右 60px —— 左边品牌名（始终粉），右边章节 / chapter 标签（闷 paper-blush）。Runner 是 JetBrains Mono 全大写 24px，字距 0.14em。

每一页还带着 **底栏页脚**，下 60px / 左右 60px —— 通常左边来源或机密字符串，右边页码位置标记。页码位置用 paper-blush 底加粉 `<em>` 标当前数字（例如 `01 / 09`）。

**发丝内框** 1px paper-blush 14%，每一页坐在 `inset: 36px`。它是杂志页的编辑边框，无条件出现。

## 纵深与抬升

### 无 Box Shadow，仅气氛纵深

系统在任何结构元素上使用**零条 box-shadow 声明**。纵深来自三层气氛：

1. **径向渐变表面**（`{components.slide-surface}`）——从左上被暖深椭圆点亮，向右下淡到近黑。这做出摄影棚柔光箱扫到页面一角的印象。
2. **胶片颗粒叠层**（`{components.film-grain}`）——8% 不透明度，screen 混合，给表面加摄影颗粒。
3. **英雄 script 标题上的粉光晕 text-shadow** —— 低 alpha 粉的柔 80–120px 模糊，模拟大号霓虹饱和字体在相纸上的漏光。

### 卡片或面板上无投影

卡片、表格和面板不带阴影。系统的「卡片」模式是结构的而不是抬起的：由描边或左边线定义的区域，平坐在表面上。

### 发丝线作为结构纵深

系统需要分隔区域时，用：
- 1px 粉 45% 不透明度（`{components.pink-rule}`）做柔粉规则线。
- 1px paper-blush 14%（`{components.hair-paper}`）做闷发丝分隔。
- 1px 粉 32%（`{colors.line-pink}`）做表格行分割和图表坐标轴线。

从不要 2px 或更粗的线。从不要粉和 paper 之外的彩色线。

## 形状与处理

### 圆角

| 值 | 用途 |
|---|---|
| 0px | 卡片、面板、表格单元格、QR tiles、runner / 页脚文字 |
| 999px | 无——这里的 pills 明确是矩形 |

系统在任何结构元素上**圆角为零**。Pills 是 0 圆角矩形（尽管命名惯例叫「pill」）。唯一的圆元素是小号图表 callout 圆标记（标记拐点的 SVG `<circle>` 元素）。

### 描边粗细

- **1px solid paper-blush 14%** —— 通用内发丝框。
- **1px solid 粉**（`{colors.pink}`）—— pill 轮廓。
- **1px solid 粉 32%**（`{colors.line-pink}`）—— 表格分割、图表坐标轴。
- **1px solid paper-blush 14%** —— TOC 行分割、页脚分隔。
- **1px solid 粉** 全不透明度 —— 左 callout-rail 描边、流程页步骤顶边。
- **1px dashed 粉 18%** —— 图表网格线。

不存在其他描边粗细。系统里任何地方都没有 2px、3px 或更粗的描边。

### 装饰元素类型

**英雄 script 标题** —— 220–600px 的 DM Serif Display 标题，粉色，带光晕 text-shadow。任何用到它的页面的定义性瞬间。始终粉，始终带 glow，始终带着 `padding-bottom: .1em` 补偿下伸。

**Paper-blush 衬线标题** —— 88–140px 的 DM Serif Display 标题，paper-blush。用于瞬间应读作墨水而不是高亮时。可含 `<em>` 把一个词切到粉。

**粉 kicker** —— 22px JetBrains Mono 全大写 eyebrow，`{colors.pink}`，放在标题上方。系统里粉与英雄 script 最一致的共同出场。

**等宽 runner / 页脚** —— 标准 JetBrains Mono chrome，24px / 字距 0.14em。Runner 上的品牌始终粉；其余是闷 paper-blush。

**粉规则线（`{components.pink-rule}`）** —— 1px 粉 45% 不透明度。用作柔分隔。

**发丝规则线（`{components.hair-rule}`）** —— 1px paper-blush 14% 不透明度。用作闷分隔以及 TOC 行分割。

**Callout rail（`{components.callout-rail}`）** —— 1px 粉左边配右对齐内容，padding-left 24px。用作图表旁或章节说明旁的纵向 callout 容器。

**统计行（`{components.stat-row}`）** —— 240px 衬线数字配对等宽标签 + Inter 描述，与下一行用 1px paper 发丝分隔。统计数字是粉；描述是闷 paper-blush。

**Pills（`{components.pill-outline}`、`{components.pill-solid}`、`{components.pill-dim}`）** —— 三种 pill 状态：空心粉（默认）、实心粉配深墨文字（肯定 / 主打），以及闷发丝（弱化）。全部是 0 圆角矩形。

**QR tile（`{components.qr-tile}`）** —— 180×180 paper-blush 方，12px 白 padding，里面 SVG QR。系统里唯一的大浅色表面元素；在 CTA 页上充当「票」物件。

**图表 callout** —— 120px 粉衬线数字配 0.5em 纸色单位后缀，再加小号等宽标签和 22px 闷 Inter 描述，用 1px 粉 callout rail 锚在图表右边。

**图表线** —— 主系列 3px solid 粉线；次系列 2px paper-blush 虚线。主线上的拐点带着 9px 实心粉圆、18px 空心环 50% 不透明度，以及落到坐标轴的纵向虚线。

**流程步骤** —— 纵向列，用 1px solid 粉顶边锚定，96px 粉衬线数字、38px paper-blush 衬线标题和 Inter 描述。步骤间隙 24px，用小号粉箭头字形连接。

**矩阵表** —— 4 列网格，第一列是 32px paper-blush 衬线标签，列表头行着色为粉，「our column」行用 `rgba(237, 61, 140, 0.08)` 着色以标记它。

## 该做与不该做

### 该做
- 每一页叠径向渐变表面、胶片颗粒叠层和 1px paper-blush 内框。三者都不可省略。
- 英雄 script 标题设成 `{colors.pink}` 并带光晕 text-shadow。Glow 是 script 身份的一部分。
- 每一个编辑 / 展示瞬间用 DM Serif Display。衬线是系统唯一的编辑脸——不要换成第二张脸。
- 正文段落设成 Inter 字重 300。超细字重是系统冷静的散文声线。
- 每一个标签、页码、runner 和页脚字符串用 JetBrains Mono 全大写，字距至少 0.08em。
- 在 paper-blush 衬线标题里用 `<em>` 把一个词切到粉——系统的主标题强调。
- 每一个主标题上方放粉 kicker。粉 eyebrow 是系统的编辑信号。
- 用粉左边 callout（`{components.callout-rail}`）把统计、callout 或章节说明锚在图表或内容区右边。
- 给每一个 DM Serif Display 标题加 `padding-bottom: .1em`。衬线下伸需要补偿。
- 用页码位置页脚模式，当前数字用粉 `<em>`：`<em>03</em> / 09`。

### 不该做
- 不要省略胶片颗粒或内发丝框。系统的编辑气氛依赖两者。
- 不要给任何面板或卡片用 box-shadow。纵深是气氛的，不是结构的。
- 不要引入第二彩色强调。粉是唯一强调。加红、蓝或绿会拆掉系统。
- 不要把热 fuchsia 粉当文字渲染在 paper-blush 表面上——对比会反相，看起来像打错字。
- 不要把正文放进 DM Serif Display。衬线给编辑瞬间，不当段落。
- 不要把展示标题放进 Inter。无衬线是正文声线，不是标题声线。
- 不要圆任何元素。卡片、pills、表格、QR tiles——全部严格矩形。
- 不要给任何元素用模糊阴影。系统里唯一的「阴影」是英雄 script 上的粉光晕 text-shadow，而且那是 glow，不是投影。
- 不要用斜体字形。`<em>` 标签被改造成粉换色开关。
- 不要用多个等权区域挤满一页。一个英雄瞬间主宰时，系统才读作优雅。

## 响应式行为

系统瞄准**固定 1920×1080 画布**，渲染在 `<deck-stage>` web component 里。舞台负责按比例缩放到浏览器视口——画布内所有像素固定尺寸均匀缩放。

### 演示行为
- 导航、缩放和演示 chrome 由 `<deck-stage>` 组件处理。
- 键盘、触摸和鼠标滚轮导航由舞台管理。
- 无论视口如何，画布恒为 1920×1080。

### 打印行为
打印导出取决于 deck-stage 组件的打印处理。粉光晕 text-shadow 和胶片颗粒叠层在 PDF 导出里可能渲染不一致——假设视觉对等之前先测试。

## CJK 与国际内容

### 推荐中文搭配

| 角色 | 拉丁字体 | 中文字体（推荐） | 字重 | 说明 |
|---|---|---|---|---|
| Script / display（DM Serif Display） | DM Serif Display | **思源宋体 Noto Serif SC** | **900** | 厚衬线，在深底上保住视觉质量。默认选择。 |
| Display 交替（纤细瞬间） | DM Serif Display | 站酷小薇体 ZCOOL XiaoWei | 400 | 高定细展示脸——只在极大字号（400px+）使用，纤细才读作刻意。典型标题字号（40–200px）在深底上太细。 |
| Body（Inter 300） | Inter | Noto Serif SC（思源宋体） | 400 | 衬线正文让编辑声线与厚展示保持一体。 |
| Label / runner（JetBrains Mono UPPERCASE tracked） | JetBrains Mono | Noto Sans SC | 400（不要对 CJK 强制等宽） | |

### 中英混排策略

策略 A —— 把每个 token 的 `fontFamily` 扩展为拉丁字体后面跟中文字体。DM Serif Display token 变成 `"DM Serif Display, 'Noto Serif SC', serif"`，中文 run 上 `font-weight: 900`；Inter 正文 token 变成 `"Inter, 'Noto Serif SC', system-ui, sans-serif"`；JetBrains Mono token 变成 `"JetBrains Mono, 'Noto Sans SC', monospace"`。拉丁字形用原字体渲染；CJK 自动落下。

**关键**：中文文字走展示角色时，显式设 `font-weight: 900`。DM Serif Display 的「单字重」因为是高对比展示衬线，视觉上已经重——对等的 CJK 重量在 Noto Serif SC 的字重 900，不是 400。

### 加载

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&family=Noto+Serif+SC:wght@400;500;700;900&family=Noto+Sans+SC:wght@400;500;700&family=ZCOOL+XiaoWei&display=swap" rel="stylesheet">
```

**关键——不要把字体拆到多个 CDN**：四套中文字体（Noto Serif SC、Noto Sans SC、ZCOOL XiaoWei）都在 Google Fonts。把它们留在上面这一条 Google Fonts URL 里。**不要把 ZCOOL XiaoWei 挪进 `cn-fontsource-zcool-xiaowei` 包** —— 那个 npm 包不存在，CDN 返回 404，浏览器会静默落到系统衬线（macOS 上是 PingFang），标题就会渲染成通用细衬线而不是 XiaoWei。这是上一代已经确认的真实失败。

### 通用 CJK 调整

- 行高：正文 1.75–1.85，展示 1.15–1.25
- 字距：CJK 为 0
- Text-transform：CJK 不强制全大写
- 全角标点 （，。：；！？「」（））
- 展示标题不加句号（中文排印惯例）
- 盘古之白（CJK 与拉丁之间加空格：`使用 Claude` 而不是 `使用Claude`）
- 一句一字体

### 本系统的审美说明

Pink Script (After Hours) 是夜间高定系统，整套编辑身份压在深暖黑纸上、热 fuchsia 粉、可到 600px 的 DM Serif Display 上。任何字号下 DM Serif Display 的视觉重量都可观——高对比笔画、衬线端点，以及在深底上站得住的排印质量。

推荐的中文对等是 **思源宋体 Noto Serif SC 字重 900**。它带着与 DM Serif Display 相同的视觉质量：粗衬线端点、足够的笔画密度在深表面上清楚可读，以及定义系统的编辑声线。展示瞬间字重 900 不可商量——任何更轻（400、500，甚至 700）都会在粉光晕 + 深纸组合里视觉消失，拆掉整套高定声线。

**站酷小薇体 ZCOOL XiaoWei** 是可行的第二选项，用于极端纤细读作刻意的瞬间——单条 400px+ 拉引文、发丝章节分隔标题、封面页最顶上的品牌 wordmark。它单字重 400 加极端笔画对比带着不同感觉：更盛装、更耳语细、更 vintage-Vogue 而不是现代时尚编辑。大多数展示工作选 Noto Serif SC 900；只有瞬间真正是极大字号的纤细强调时，才伸手去拿 XiaoWei。

粉光晕 text-shadow（`{components.pink-glow}`，80–120px 模糊）无论选哪张展示脸，都完美迁到中文字。**给每一个粉色中文展示瞬间加上同样的 glow** —— 霓虹漏光效果与脚本无关，深夜杂志气氛能完整熬过脚本切换。

粉颜色（`{colors.pink}` — #ED3D8C）作为唯一彩色强调原样工作。行内 `<em>` 换色（paper-blush 标题里一个词变粉）干净迁到中文——用 `<em>` 包一个汉字或一个短语，粉墨开关读感完全相同。

**正文用 Inter 字重 300** 不能直接迁移。推荐正文字是 Noto Serif SC 字重 400——它的高对比衬线笔画匹配系统整体的高定声线。正文字色保持 paper-blush（`{colors.paper-blush}`）；超细声线通过字号、paper-blush 颜色和闷 55% 不透明度导语达成，不通过字重。

JetBrains Mono 全大写宽字距标签（runner 品牌、页码、页脚 chrome）迁不到 CJK。纯拉丁 chrome 字符串（品牌名本身、`01 / 09` 这类版次号）保持 JetBrains Mono。中文 chrome 文字（右上章节 / chapter 标签）用同 24px 字号的 Noto Sans SC 400，字距重置为 0，不全大写。

径向渐变表面、胶片颗粒叠层、1px paper-blush 内框——全部与脚本无关。粉光晕、kicker、callout rail、stat-row 模式、matrix-cell——全部原样迁移。

### 已知 CJK 缺口

DM Serif Display 的「单字重」有误导：它是高对比展示衬线，任何字号都读作视觉上重。中文对等重量在 Noto Serif SC 的 **字重 900**，不是 400——展示用字重 400 会让中文标题发软，跟粗粉 callout 脱节。系统靠字号做层级在中文里仍成立，但必须把展示字重锁在 900 才能保住视觉质量。

ZCOOL XiaoWei 是唯一能在 CDN 加载、比例上抓住「高对比高定衬线」性格的中文字，但它单字重 400 对这套模板深表面上的大多数展示字号太细。把 XiaoWei 当小众选项，不当默认。

## 迭代指南

1. 每一张新页背景都是点亮的径向渐变（`{components.slide-surface}`），带胶片颗粒和内发丝框。三层都不要跳。
2. 每一个新英雄 script 标题是 `{colors.pink}` 的 DM Serif Display，光晕 text-shadow 模糊 80–120px。
3. 每一个应读作墨水（不是高亮）的新编辑标题是 `{colors.paper-blush}` 的 DM Serif Display。里面用 `<em>` 把一个词切到粉。
4. 每一个新正文段落是 Inter 字重 300，paper-blush（全）或 mute-paper（闷）。
5. 每一个新标签、runner、页脚或元数据标记是 JetBrains Mono 全大写，字距 0.08em+。
6. 每一个新 kicker eyebrow 是粉。不要用其他颜色渲染 kicker。
7. 每一个新 pill 是 0 圆角矩形。选 outline（默认）、solid（肯定）或 dim（弱化）状态。
8. 每一个新表格或矩阵用 1px 粉 32% 行分割，没有竖向描边。
9. 每一个图表主系列用 3px solid 粉线，次系列用 2px paper-blush 虚线。不要引入第三色。
10. Runner 品牌文字始终粉；右边 meta 始终闷 paper-blush。不要对调。

## 已知缺口

- 系统依赖经由 `deck-stage.js` 加载的 `<deck-stage>` web component。没有它，1920×1080 画布不会缩放，幻灯片会按原生像素尺寸渲染。
- 胶片颗粒叠层用带 `feTurbulence` 的 data-URI SVG。有些浏览器（较旧 Safari）噪点渲染不一致，或在 PDF 导出时跳过。
- DM Serif Display 只有字重 400。没有粗体或斜体变体可用——系统没有回退字重阶梯，层级只靠字号。
- 粉光晕 text-shadow 用固定 80px 和 120px 模糊值。在很小的视口缩放下，glow 可能盖过字体；在很大缩放下，glow 可能显得弱。
- `{colors.pink-light}`、`{colors.pink-deep}` 和 `{colors.ink-violet}` token 已定义，但在当前幻灯片类型里未启用。它们预留给未来变化。
- CTA 页里 QR-tile 的 SVG 是手工编码的 `<rect>` 元素图案，并不编码真正可扫的码。真 QR 码需要在外部生成。
- 图表线点和拐点标记是必须手工计算的 SVG `<polyline>` 坐标。没有数据绑定层。
- 封面 script lockup 在第二行用 `padding-left: 180px` 做缩进悬挂效果。这是硬编码的版式决定，不能推广到其他词长——第二行太长可能打破居中。
- Runner 和页脚依赖 `white-space: nowrap` 防止折行。极长品牌名或页码位置字符串可能溢出 60px 边缘边距。
- 矩阵 `cell.us` 列高亮是硬编码的 `rgba(237, 61, 140, 0.08)` 薄涂。给其他列着色需要逐列加 class。
