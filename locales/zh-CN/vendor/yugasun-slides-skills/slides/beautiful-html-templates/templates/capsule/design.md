---
version: alpha
name: Capsule
description: A playful editorial system built on pill-shaped containers, a sun-bleached cream canvas, and a nine-color candy palette. Bodoni Moda serif headlines pair with Space Grotesk body to suggest a literary magazine that took a holiday at a 1970s ice-cream parlor. Every container that holds text is a pill (border-radius 9999px) outlined with a 2px ink stroke, casting a soft 6–12px offset shadow. The aesthetic is "Memphis-meets-editorial" — confident typography, generous bordered shapes, and decorative floating pills as atmospheric wallpaper.

colors:
  cream: "#F5F5F0"
  ink: "#1A1A1A"
  outline: "#1E1E1E"
  white: "#FFFFFF"
  coral: "#E85D4E"
  lime: "#C4D94E"
  lavender: "#C5B5E0"
  sky: "#8BB4F7"
  violet: "#A06CE8"
  yellow: "#F2D160"
  peach: "#F5B895"
  mint: "#A8E6CF"
  shadow: "rgba(26, 26, 26, 0.08)"

color-aliases:
  bg: cream
  fg: ink
  outline: outline                  # same hue family as ink; reserved for stroke role

typography:
  display:
    fontFamily: "Bodoni Moda, serif"
    fontSize: "clamp(3rem, 8vw, 7rem)"
    fontWeight: 800
    lineHeight: 0.9
    letterSpacing: -0.02em
  closing-display:
    fontFamily: "Bodoni Moda, serif"
    fontSize: "clamp(2.5rem, 6vw, 5rem)"
    fontWeight: 800
    lineHeight: 0.95
    letterSpacing: -0.03em
  headline:
    fontFamily: "Bodoni Moda, serif"
    fontSize: "clamp(2rem, 4vw, 3.5rem)"
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.02em
  section-headline:
    fontFamily: "Bodoni Moda, serif"
    fontSize: "clamp(1.8rem, 3.5vw, 3rem)"
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.01em
  quote-display:
    fontFamily: "Bodoni Moda, serif"
    fontSize: "clamp(1.6rem, 3.5vw, 3rem)"
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: -0.01em
  card-headline:
    fontFamily: "Bodoni Moda, serif"
    fontSize: "1.5rem"
    fontWeight: 700
    lineHeight: 1.1
  stat-number:
    fontFamily: "Bodoni Moda, serif"
    fontSize: "clamp(2rem, 3.5vw, 3rem)"
    fontWeight: 800
    lineHeight: 1
    letterSpacing: -0.03em
  orbit-numeral:
    fontFamily: "Bodoni Moda, serif"
    fontSize: "2.5rem"
    fontWeight: 700
    lineHeight: 1
  body:
    fontFamily: "Space Grotesk, sans-serif"
    fontSize: "clamp(0.95rem, 1.2vw, 1.15rem)"
    fontWeight: 400
    lineHeight: 1.6
  body-sm:
    fontFamily: "Space Grotesk, sans-serif"
    fontSize: "0.9rem"
    fontWeight: 400
    lineHeight: 1.55
  subtitle:
    fontFamily: "Space Grotesk, sans-serif"
    fontSize: "clamp(0.8rem, 1.5vw, 1.1rem)"
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.15em
    textTransform: uppercase
  pill-text-md:
    fontFamily: "Space Grotesk, sans-serif"
    fontSize: "0.85rem"
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.12em
    textTransform: uppercase
  pill-text-sm:
    fontFamily: "Space Grotesk, sans-serif"
    fontSize: "0.7rem"
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  label:
    fontFamily: "Space Grotesk, sans-serif"
    fontSize: "0.75rem"
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  mini-label:
    fontFamily: "Space Grotesk, sans-serif"
    fontSize: "0.65rem"
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase

spacing:
  pad-lg: "3rem 4rem"
  pad-md: "2rem"
  gap-xl: "4rem"
  gap-lg: "3rem"
  gap-md: "2rem"
  gap-sm: "1.5rem"
  gap-xs: "0.75rem"
  card-pad: "2.5rem 2rem"
  pill-pad-lg: "1.5rem 3.5rem"
  pill-pad-md: "1rem 2.5rem"
  pill-pad-sm: "0.4rem 1.2rem"
  pill-pad-xs: "0.35rem 1rem"

canvas:
  width: 100vw
  height: 100vh

components:
  pill:
    borderRadius: 9999px
    border: "2px solid {colors.outline}"
    fontFamily: "Space Grotesk, sans-serif"
    fontWeight: 500
    letterSpacing: 0.02em
    whiteSpace: nowrap
    description: "The universal container shape. Any text container — chip, button, label, statement-highlight, stat tile, card, bar — is a pill with 2px outline. Background can be any palette accent or white."
  pill-card:
    background: "{colors.white}"
    border: "2px solid {colors.outline}"
    borderRadius: "2rem"
    padding: "{spacing.card-pad}"
    boxShadow: "8px 8px 0 {colors.shadow}"
    description: "Larger pill-shaped card (slightly squared corners at 2rem rather than full pill) for content blocks. Always white background, always shadowed."
  stat-pill:
    background: "{colors.white}"
    border: "2px solid {colors.outline}"
    borderRadius: "2rem"
    padding: "2rem 1.5rem"
    boxShadow: "6px 6px 0 {colors.shadow}"
    description: "Stat tile — pill-shaped white card containing a colored stat number, label, and a tiny accent bar."
  bar-track:
    height: 36px
    background: "{colors.cream}"
    border: "2px solid {colors.outline}"
    borderRadius: 9999px
    overflow: hidden
    description: "Horizontal bar chart track shaped as a pill. Fills use the candy palette."
  bar-fill:
    height: "100%"
    borderRadius: 9999px
    borderRight: "2px solid {colors.outline}"
    description: "Inner bar pill with the value label printed at right edge inside the fill."
  accent-line:
    width: 60px
    height: 4px
    background: "{colors.coral}"
    borderRadius: 9999px
    description: "Pill-shaped 60×4 accent rule. Default color coral; closing-context variant uses 80×4."
  card-icon:
    width: 60px
    height: 60px
    borderRadius: "50%"
    border: "2px solid {colors.outline}"
    fontFamily: "Bodoni Moda, serif"
    fontSize: "1.5rem"
    fontWeight: 700
    description: "Circular pill icon (60px) used as a card mark. Background is an accent color; contains a 1–3 character Roman numeral or letter."
  step-node:
    width: 56px
    height: 56px
    borderRadius: "50%"
    border: "2px solid {colors.outline}"
    background: "{colors.white}"
    fontFamily: "Bodoni Moda, serif"
    fontSize: "1.3rem"
    fontWeight: 700
    boxShadow: "4px 4px 0 {colors.shadow}"
    description: "Circular pill node (56px) used as a timeline step or sequence marker. Step accent color appears as filled-pill class on the node."
  orbit-center:
    width: 160px
    height: 160px
    borderRadius: "50%"
    background: "{colors.lime}"
    border: "2px solid {colors.outline}"
    fontFamily: "Bodoni Moda, serif"
    fontSize: "2.5rem"
    fontWeight: 700
    description: "Large circular pill (160px) used as the gravitational anchor of an orbit composition. Default fill lime; small satellite pills orbit around it."
  diagram-node:
    borderRadius: 9999px
    border: "2px solid {colors.outline}"
    padding: "1rem 2rem"
    boxShadow: "6px 6px 0 {colors.shadow}"
    background: "{colors.white}"
    description: "Flow-diagram node — pill-shaped container with shadow. Connected by 50×4 ink connectors with triangular arrowheads."
  diagram-connector:
    width: 50px
    height: 4px
    background: "{colors.outline}"
    description: "Solid 50×4 ink bar with a triangular arrowhead at the right end, connecting two diagram nodes inline."
  visual-frame:
    borderRadius: "2rem"
    border: "2px solid {colors.outline}"
    boxShadow: "12px 12px 0 {colors.shadow}"
    description: "Large image/illustration frame — slightly squared pill (2rem radius) with thicker 12px offset shadow. Often filled with a tri-stop linear gradient and a dot-pattern overlay."
  grain-overlay:
    position: fixed
    inset: 0
    pointerEvents: none
    zIndex: 9999
    opacity: 0.04
    mixBlendMode: multiply
    backgroundImage: "fractalNoise SVG"
    description: "Subtle film-grain noise overlay applied to the entire viewport at 4% opacity in multiply blend mode. Always present, never absent."
  radial-glow:
    description: "Soft radial gradient wash anchored to a corner or center of a slide background. Uses one of the candy palette colors at 6–15% opacity, blended into the cream canvas. Provides atmospheric warmth without changing the surface color."
---

## 概述

Capsule 是一套**玩味编辑系统**，其结构前提就是**胶囊（pill）**：每个文本容器都是胶囊，每个图标都是胶囊，每根条形都是胶囊，流程图里的每个节点都是胶囊。`border-radius: 9999px` 几乎套在所有 UI 元素上，较大面板则收成 2rem 圆角。再配上包裹每个形状的 2px 墨色描边，容器看起来鼓胀、友善、图形感强——向 Memphis 设计和 70 年代末冰淇淋店招牌点头，却不放弃编辑纪律。

字体栈是一场刻意的双面对谈。**Bodoni Moda**——高对比 Didone 衬线——承担每一次展示、每一个章节标题、每一个统计数字、每一张卡片标题、每一段引文。Bodoni 的高挑大写与粗细笔画对比，给标题编辑重量，也带一点时尚杂志的光泽。**Space Grotesk**——当代几何无衬线——承担每一段正文、每一个标签、每一段胶囊文字、每一个副标题。衬线 / grotesk 配对构成系统的主排印节奏：华美的衬线陈述 + 干净的 grotesk 支撑结构。

色板是九个彩色加上三个中性色。画布是 `{colors.cream}`——温暖的日晒米白，信号是「杂志纸」而不是「屏幕白」。墨色是 `{colors.ink}`，用于正文、标题和通用描边。七个糖果强调色——`{colors.coral}`、`{colors.lime}`、`{colors.lavender}`、`{colors.sky}`、`{colors.violet}`、`{colors.yellow}`、`{colors.peach}`，再加上 `{colors.mint}`——可以互换。它们填充胶囊、给统计数字上色、填满条形图，并作为装饰氛围漂浮。没有语义映射：没有任何颜色表示「警告」，也没有任何颜色表示「成功」。每个强调色都为构图平衡而选，不为含义而选。

纵深来自 **柔软的硬偏移阴影**，偏移 4px、6px、8px、12px，用低透明度墨色（`{colors.shadow}` = `rgba(26, 26, 26, 0.08)`）。与真正的野兽派阴影不同，它们略微透明——读起来是「抬起」而不是「盖章」。配上 2px 描边，每个胶囊都像浮在奶油画布上方一点点。不用模糊投影；偏移永远是实色，永远朝右下。

**密度哲学：中高氛围。** Capsule 的幻灯片感觉是住满了的。系统围绕这个想法：装饰性漂浮胶囊应作为壁纸环绕实际内容——小彩色胶囊在背景上倾斜 5–25°，每个只装一个大写单词。这些氛围胶囊没有功能；它们是排印五彩纸屑。正确构图的幻灯片会把一到两块实质内容（一张 pill-card、一个统计网格、一张图）与边缘 5–8 个漂浮装饰胶囊配对。在 Capsule 里感觉坏掉的幻灯片，是角落空着或奶油色铺满、没有缓解——糖果色板即使在内容并不严格需要的地方，也想参与进来。

**关键特征：**
- 通用胶囊几何——小容器用 `border-radius: 9999px`，较大卡片 / 画框用 2rem。
- 2px 实线 `{colors.outline}` 描边包裹每个胶囊、图标和卡片。
- 每次展示 / 标题 / 统计都用 Bodoni Moda 衬线；每段正文 / 标签 / 胶囊文字都用 Space Grotesk 无衬线。
- 日晒奶油画布 `{colors.cream}`，背景氛围用糖果强调色 6–15% 透明度的柔和径向辉光。
- 低透明度墨色（`{colors.shadow}`）的硬偏移阴影，偏移 4/6/8/12px，永远实色，永远右下。
- 九色糖果强调色板可互换——没有语义映射。
- 倾斜 5–25° 的装饰漂浮胶囊作为氛围壁纸填充幻灯片背景。
- 持久的分形噪声颗粒叠层（4% 透明度，multiply 混合）始终覆盖整个视口。
- 全屏右侧竖向 nav-dot 列，右下角等宽页码计数。

## 色彩

### 画布与墨色
- **Cream**（`{colors.cream}` — #F5F5F0）：画布。温暖的日晒米白。用作默认幻灯片背景、默认 bar-track 内部，以及任何想要纸张温度、又不想纯白的中性区域。
- **Ink**（`{colors.ink}` — #1A1A1A）：主文本色。用于标题、正文，以及（在别名 `outline` 下）通用描边。
- **Outline**（`{colors.outline}` — #1E1E1E）：功能上与墨色相同；保留为每个胶囊、卡片、图标和画框的描边色，以便语义清晰。
- **White**（`{colors.white}` — #FFFFFF）：真白。用作 pill-card、stat-pill、图节点，以及任何需要在奶油画布上最高对比的胶囊的默认填充。白色胶囊始终带 2px 墨色描边。

### 糖果强调色
- **Coral**（`{colors.coral}` — #E85D4E）：温暖橙红。强调色里最「有声音」的一个；用作默认 accent-line 颜色、序列中第一张卡片的默认 pill-card 图标填充，以及最常见的统计数字色。
- **Lime**（`{colors.lime}` — #C4D94E）：鲜艳黄绿。与 coral 搭配很好；orbit-center 锚点的默认填充，也是常见统计数字色。
- **Lavender**（`{colors.lavender}` — #C5B5E0）：柔和丁香紫。用作页眉里平静的胶囊填充，以及常见的引文高亮色。
- **Sky**（`{colors.sky}` — #8BB4F7）：中饱和矢车菊蓝。默认的「第三强调」——在 3 卡片网格里舒适地挨着 coral 和 lime。
- **Violet**（`{colors.violet}` — #A06CE8）：更深的紫。当幻灯片已经有 lavender 作一个强调、还需要第二个紫系跳点时使用。
- **Yellow**（`{colors.yellow}` — #F2D160）：温暖万寿菊黄。标题胶囊、收束胶囊，以及任何应读作「重要 / 主打」的胶囊的默认填充。
- **Peach**（`{colors.peach}` — #F5B895）：浅杏色。最柔的强调；用于漂浮装饰胶囊和圆形装饰斑点。
- **Mint**（`{colors.mint}` — #A8E6CF）：浅水绿。最常出现在线性渐变 visual-frame 内部，以及较低强调的装饰胶囊里。
- **Shadow**（`{colors.shadow}` — `rgba(26, 26, 26, 0.08)`）：通用柔软硬偏移阴影色。永远不要用别的阴影色。

### 默认值
- **默认幻灯片表面**：`{colors.cream}`。
- **默认标题色**：`{colors.ink}`——Bodoni 衬线标题永远是墨色，从不染色。颜色只出现在统计数字和强调胶囊内部。
- **默认正文色**：`{colors.ink}` 以 0.6–0.7 透明度渲染，相对奶油画布软一点。
- **默认描边色**：`{colors.outline}`（≈ 墨色）——每个胶囊 / 卡片 / 图标都是 2px，没有例外。
- **默认卡片填充**：`{colors.white}`。
- **默认 accent-line 颜色**：`{colors.coral}`。
- **默认标题胶囊填充**：`{colors.yellow}`。
- **默认收束胶囊填充**：`{colors.yellow}`。
- **默认 orbit-center 填充**：`{colors.lime}`。
- **3 色或 4 色序列的默认第一强调**：coral → lime → sky → violet（需要更多颜色时轮转）。这个序列是系统的「Roy G. Biv」；给 agent 一个确定的伸手顺序，糖果色板才不会显得随机。
- **默认装饰胶囊背景透明度**：全饱和（不淡化）。漂浮胶囊故意很响。

强调色没有语义角色。按冷暖平衡和邻接来选，不按含义。三个强调色一起出现时，把暖色（coral/yellow/peach）与冷色（sky/lavender/violet/mint）与中性亮色（lime）配对。避免两个同族强调色相邻（两个紫、两个绿、两个暖色）。

## 字体排印

### 字体家族
系统跑在一场**双面对谈**上：`Bodoni Moda`（衬线，字重 400–900，opsz 轴）承担每一次展示和标题；`Space Grotesk`（无衬线，字重 300–700）承担每一段正文、标签和胶囊文字。没有第三张脸。两套字体都从 Google Fonts 以可变轴字重加载。

Bodoni Moda 的高对比与 Didone 调制给系统编辑-华美的音域；粗细笔画对比在大字号最明显，所以展示字重应始终 700+，以保持笔画存在感。Space Grotesk 的几何 grotesk 承担干净、现代的正文——它从不试图与 Bodoni 标题竞争。

Bodoni 标题里的行内 `<em>` 仍用 Bodoni，只切到斜体。Bodoni 引文正文里的 `quote-highlight` 把包住的词换成胶囊（Space Grotesk 大写胶囊文字，糖果填充），作为视觉强调。

### 字号阶梯

| Token | 字号 | 字体 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.display}` | clamp(3rem, 8vw, 7rem) | Bodoni Moda | 800 | 最大封面 / 标题展示 |
| `{typography.closing-display}` | clamp(2.5rem, 6vw, 5rem) | Bodoni Moda | 800 | 收束性陈述标题 |
| `{typography.headline}` | clamp(2rem, 4vw, 3.5rem) | Bodoni Moda | 700 | 分栏或双栏版式上的主幻灯片标题 |
| `{typography.section-headline}` | clamp(1.8rem, 3.5vw, 3rem) | Bodoni Moda | 700 | 章节开场或卡片 / 图表上方的居中标题 |
| `{typography.quote-display}` | clamp(1.6rem, 3.5vw, 3rem) | Bodoni Moda | 600 | 引出式引文正文 |
| `{typography.card-headline}` | 1.5rem | Bodoni Moda | 700 | 卡片或支柱块标题 |
| `{typography.stat-number}` | clamp(2rem, 3.5vw, 3rem) | Bodoni Moda | 800 | 大号数值统计 |
| `{typography.orbit-numeral}` | 2.5rem | Bodoni Moda | 700 | orbit-center 圆里的居中序数 |
| `{typography.body}` | clamp(0.95rem, 1.2vw, 1.15rem) | Space Grotesk | 400 | 段落正文 |
| `{typography.body-sm}` | 0.9rem | Space Grotesk | 400 | 卡片内紧凑正文 |
| `{typography.subtitle}` | clamp(0.8rem, 1.5vw, 1.1rem) | Space Grotesk | 400 | 展示标题下方的大写、加字距副标题 |
| `{typography.pill-text-md}` | 0.85rem | Space Grotesk | 600 | 标题 / 收束胶囊内文字 |
| `{typography.pill-text-sm}` | 0.7rem | Space Grotesk | 600 | 小漂浮装饰胶囊内文字 |
| `{typography.label}` | 0.75rem | Space Grotesk | 500 | 页眉标签胶囊、署名行 |
| `{typography.mini-label}` | 0.65rem | Space Grotesk | 500 | 标签簇里的 mini-pill 碎片 |

### 默认值
- **主章节标题的默认字号**：`{typography.section-headline}`（clamp 1.8–3rem）。双栏或分栏版式用 `{typography.headline}`（clamp 2–3.5rem）。
- **封面或开场展示时刻的默认字号**：`{typography.display}`（clamp 3–7rem）。
- **段落正文的默认字号**：`{typography.body}`（clamp 0.95–1.15rem）。
- **任何行内标签或碎片的默认字号**：`{typography.label}`（0.75rem）。
- **任何 Bodoni 展示元素的默认字重**：最低 700；最大展示用 800。
- **任何 Space Grotesk 正文元素的默认字重**：400。
- **英雄统计数字的默认字号**：`{typography.stat-number}`（clamp 2–3rem）。

拿不准时，伸手去拿 `{typography.section-headline}` 作为幻灯片的主文本时刻，而不是 `{typography.card-headline}`（那是卡片内块级标题）。

### 标志性处理
对应元素类型一旦使用，这些处理就是**不可省略的**：

- **每个 display、headline、stat-number、card-headline 和 quote-display 元素都用 Bodoni Moda。** Space Grotesk 不出现在任何展示角色。
- **每个 body、subtitle、pill-text、label 和 chip 元素都用 Space Grotesk。** Bodoni 不出现在正文或碎片角色。
- **每个 Bodoni 展示元素都用负字距**（-0.01em 到 -0.03em）。Bodoni 在大字号用默认 tracking 会显得松。
- **每个 Space Grotesk 副标题、标签、胶囊文字和碎片元素都是大写，且 0.08em+ tracking。** 大写 + tracking 是小字身份信号。
- **Bodoni 标题始终渲染为 `{colors.ink}`，从不用糖果色。** 颜色出现在统计数字上（例如 `color: {colors.coral}`），但不出现在衬线标题上。例外是 orbit-center 数字：它坐在彩色圆形胶囊里，但数字本身仍是墨色。
- **每个胶囊元素都带 2px 实线描边。** 没有 2px 墨色描边的胶囊会打破系统。
- **每个 `border-radius: 9999px` 或 `2rem` 的容器，要么自带 2px 描边，要么坐在已经描边的父级里。** 不存在未描边的圆角容器。
- **每张卡片或抬起的胶囊都带硬偏移阴影**，偏移 4/6/8/12px，用 `{colors.shadow}`。较小胶囊用 4–6px；卡片用 8px；visual-frame 用 12px。

### 排印原则
Bodoni 标题 + Space Grotesk 正文的配对是主节奏；换掉任何一张脸都会打破系统。斜体只出现在引出式引文正文里，通过 `<em>` 标签（Bodoni italic）。不用下划线。胶囊封装是系统的主强调机制：把短语包进糖果填充的胶囊，等于传统编辑系统里的粗斜体。

行高随尺度收紧：`{typography.display}` 为 0.9，`{typography.headline}` 为 1.05，正文为 1.6。紧展示 + 开正文的对比，就是系统的编辑呼吸节奏。

## 版式

### 画布系统
画布是 `100vw × 100vh`——满视口，溢出隐藏。每个 `.slide` 绝对定位铺满视口，同一时间只有一页带 `.active`（opacity 1）。过渡是 0.6s 透明度淡入淡出，缓动 `cubic-bezier(0.4, 0, 0.2, 1)`。所有尺寸在 CSS `clamp()` 里用 rem，版式可流畅缩放。

### 内边距与间距阶梯
| Token | 取值 | 用途 |
|---|---|---|
| `{spacing.pad-lg}` | 3rem 4rem | 默认幻灯片外边距 |
| `{spacing.gap-xl}` | 4rem | 主双栏槽宽 |
| `{spacing.gap-lg}` | 3rem | 章节块间距 |
| `{spacing.gap-md}` | 2rem | 标准元素间距 |
| `{spacing.gap-sm}` | 1.5rem | 紧卡片内部间距 |
| `{spacing.gap-xs}` | 0.75rem | mini-pill 之间的行内间距 |
| `{spacing.card-pad}` | 2.5rem 2rem | 默认支柱卡片内边距 |
| `{spacing.pill-pad-lg}` | 1.5rem 3.5rem | 标题胶囊 / 收束胶囊内边距 |
| `{spacing.pill-pad-md}` | 1rem 2.5rem | 主打胶囊内边距 |
| `{spacing.pill-pad-sm}` | 0.4rem 1.2rem | 页眉标签胶囊内边距 |
| `{spacing.pill-pad-xs}` | 0.35rem 1rem | mini-pill 碎片内边距 |

### 氛围背景层
每张幻灯片在奶油画布上叠两层氛围处理：
1. **径向辉光**——一到三道柔和的 `radial-gradient(ellipse at X% Y%, rgba(accent, 0.06–0.15), transparent)` 洗色，锚在角落或中心。它们给画布温暖染色，却不改变表面色。
2. **颗粒叠层**——分形噪声 SVG 固定在 `inset: 0`，opacity 0.04，mix-blend-mode multiply，z-index 9999。始终存在，始终相同，从不移除。

这些不是装饰选项；它们是每张幻灯片都应出现的基线画布处理。

### 装饰胶囊壁纸
一个签名：小装饰胶囊（宽 60–160px，高 35–90px）倾斜 -20° 到 +25°，绝对定位在幻灯片背景上，作为氛围排印五彩纸屑。每个装一个大写 Space Grotesk 单词和糖果填充。有些是圆形（border-radius 50%）而不是胶囊形。它们没有信息角色——它们是视觉氛围。典型数量：封面 / 收束 / 引文版式每页 5–8 个；稠密数据版式为 0。

## 纵深与层次

### 柔软硬偏移阴影
系统唯一的纵深手法是低透明度墨色的**实色硬偏移阴影**：
- **4px 4px 0**——小抬起节点（step node、小胶囊）。
- **6px 6px 0**——orbit 胶囊、stat-pill、图节点。
- **8px 8px 0**——支柱卡片、图表容器。
- **12px 12px 0**——大 visual-frame（系统里抬得最高的元素）。

所有阴影都用 `{colors.shadow}`（`rgba(26, 26, 26, 0.08)`）。透明度是相对野兽派硬阴影的关键区别：8% 时阴影读作柔和抬起，而不是盖章偏移。偏移方向永远是右下。

### 基于描边的纵深
大部分可见纵深来自包裹每个胶囊、相对奶油画布的 2px 墨色描边。描边做了大量抬起工作；阴影给卡片和抬起胶囊加抬升。

### 扁平装饰层
装饰漂浮胶囊和径向辉光是扁平的——它们不投影。阴影留给承载内容的容器（卡片、统计砖、图节点、visual-frame）。这条视觉规则一眼就把「内容」和「氛围」分开。

## 形状与处理

### 圆角
| 取值 | 用途 |
|---|---|
| 9999px（全胶囊） | 所有小胶囊：标题胶囊、收束胶囊、装饰胶囊、页眉标签、mini 碎片、bar track、bar fill、accent line、orbit 胶囊、漂浮胶囊、引文高亮、图节点 |
| 2rem（32px） | 较大卡片：支柱卡片、stat-pill、图表容器、visual-frame |
| 1.5rem（24px） | visual-frame 内部的虚线内框 |
| 50%（圆） | 圆形胶囊：card-icon（60px）、step-node（56px）、orbit-center（160px）、nav dots（10px） |
| 0 | 颗粒叠层；幻灯片本身；visual-frame 内的糖果色渐变区域 |

系统**没有尖角文本容器**。每个装文本或图标内容的容器都是圆的。

### 边框粗细
- **2px solid `{colors.outline}`**——通用描边。用在每个胶囊、卡片、图标、画框、bar track、nav dot。
- **2px dashed `{colors.outline}`**——只用于 visual-frame 组件内的内框（装饰性内边框，表示「图片占位」）。
- **4px solid 墨色**——只用于水平连接序列 step node 的 timeline-line。

所有边框都是 `{colors.outline}`。系统里不存在彩色边框。

### 装饰元素类型

**装饰漂浮胶囊**——小（宽 60–160px × 高 35–90px）胶囊或圆，糖果填充，倾斜 -20° 到 +25°，绝对定位在幻灯片背景上。内含一个 0.55–0.85rem 的大写 Space Grotesk 单词。功能是排印五彩纸屑 / 氛围壁纸。陈述性幻灯片每页五到八个。

**页眉标签胶囊**——小（≈0.7rem 文字）胶囊，糖果填充（通常 lavender），`pill-pad-sm` 内边距，居中放在章节标题上方。系统的章节标签碎片。

**标题胶囊 / 收束胶囊**——中等胶囊（`pill-pad-lg`），`{colors.yellow}` 填充，承载大写 Space Grotesk 文字。放在封面和收束页最大展示标题上方。

**支柱卡片**——2rem 圆角白卡片，2px 描边和 8px 偏移阴影，顶部有圆形 `card-icon`、Bodoni `card-headline` 和 Space Grotesk 正文段落。用于 3 卡片和 4 卡片网格。

**Stat-pill**——2rem 圆角白卡片，内含彩色 Bodoni 统计数字、小号大写标签，底部一根细 40×4 强调条。坐在 3 列或 4 列统计网格里。

**Bar-track**——36px 高的水平胶囊（9999px 圆角），2px 描边，奶油内部。填充是糖果色的子胶囊，数值标签印在填充内部的右缘。

**轨道构图**——中心 160px 圆形胶囊，`{colors.lime}` 填充，承载 Bodoni 序数，周围 4–6 个小 `orbit-pill` 卫星，糖果填充，各自倾斜，定位在 8–45% / 8–45% 偏移，带 6px 阴影。

**图节点 + 连接器**——胶囊形流程节点（`diagram-node`）带 6px 阴影，用 50×4 墨色条加三角箭头连到下一个节点。节点可以带糖果填充；箭头永远是墨色。

**Visual-frame**——2rem 圆角大画框，12px 偏移阴影，填三段线性渐变（通常 lavender → sky → mint），叠加 0.15 透明度的点阵，内虚线边框表示「图片占位」。用于英雄视觉时刻。

**Quote-highlight**——lime 或 sky 的行内胶囊，2px 描边，包住 Bodoni 引文正文里的单个短语。系统的主行内强调机制。

**Accent line**——60×4（收束页用 80×4）水平胶囊，`{colors.coral}`，用作副标题强调线。

## 宜与忌

### 宜
- 让每个文本容器都成为胶囊——小胶囊 9999px 圆角，较大卡片 2rem 圆角。胶囊几何是系统最鲜明的单一特征。
- 给每个胶囊、卡片、图标和画框加上 2px `{colors.outline}` 描边。描边让糖果色板读作图形，而不是糖果。
- 把每个 Bodoni 展示元素设为 `{colors.ink}`，从不用糖果色。颜色属于统计数字和胶囊填充，不属于衬线标题。
- 每个标题 / 统计 / 卡片标题用 Bodoni Moda；每段正文 / 标签 / 胶囊用 Space Grotesk。双面拆分不可商量。
- 把阴影渲染成 4/6/8/12px 的实色硬偏移，用 `{colors.shadow}`（`rgba(26,26,26,0.08)`）。从不模糊；从不改色。
- 在封面、收束、引文和其他陈述性版式上，用 5–8 个倾斜 -20° 到 +25° 的漂浮装饰胶囊填充幻灯片背景。壁纸胶囊处理是系统签名。
- 每张幻灯片都把径向渐变强调辉光（6–15% 透明度）叠进奶油画布，给氛围温度。
- 让颗粒叠层（4% 透明度，multiply 混合）在每张幻灯片上都激活——它是基线层，不是可选装饰。
- 在 Bodoni 引文正文里，把行内强调短语包进 `quote-highlight` 胶囊（lime、sky 或其他糖果色），而不是加粗或斜体。
- 把暖 + 冷强调色相邻配对：coral 配 sky，yellow 配 lavender，peach 配 mint。避免两个同族强调色挨在一起。

### 忌
- 不要用尖角渲染任何文本容器。Capsule 里不存在方形文本容器。
- 不要渲染没有 2px 墨色描边的胶囊、卡片或图标。描边就是系统身份。
- 不要用糖果色渲染 Bodoni 标题。标题永远是 `{colors.ink}`；颜色活在统计数字和胶囊填充上。
- 不要用模糊投影。阴影永远是 4/6/8/12px 的实色偏移，用 `{colors.shadow}`。
- 不要把 Bodoni 配另一套无衬线伴侣。Bodoni Moda + Space Grotesk 配对是固定的。
- 不要在 Bodoni 标题上用全大写。这个系统里的 Bodoni 是句首大写（专有名词才用真正的标题大小写）。
- 不要在 Space Grotesk 副标题、标签或胶囊文字上用句首大写。小的 Space Grotesk 文字永远是大写 + 0.08em tracking。
- 不要引入第十个强调色。九个糖果强调色是封闭色板。
- 不要给装饰漂浮胶囊加阴影。阴影留给承载内容的容器。
- 不要在陈述性版式上把角落留空。奶油画布想要氛围胶囊或径向辉光；光秃角落读作坏掉。

## 响应式行为

Capsule 是视口流体的 1920×1080 演示系统，全程使用 `clamp()` 和视口相对单位。有一个 `@media (max-width: 900px)` 断点，把网格列收成单列堆叠并隐藏 nav-dot 列；低于 600px 时统计网格再从 2 列收到 1 列。除此之外系统无断点也可响应。

### 缩放行为
- 展示标题从最小视口 3rem 缩放到最大 7rem。
- 正文从 0.95rem 缩放到 1.15rem。
- 内边距通过各版式选择器里的 `clamp` 缩放。
- 边框、胶囊描边、阴影偏移和颗粒叠层是固定的，不缩放。

### 演示操作
- 用 `ArrowRight`、`ArrowDown` 或 `Space` 前进。
- 用 `ArrowLeft` 或 `ArrowUp` 后退。
- `Home` 跳到第一页；`End` 跳到最后一页。
- 触摸横滑：滑动距离 >50px 则前进或后退。
- 活动页带 `.active`（opacity 1）；非活动页 opacity 0 + pointer-events none。
- Nav dots 是右缘竖列；页码在右下；键盘提示在左下。

### 打印 / 导出
没有显式处理；透明度切换意味着朴素打印只捕获活动页。导出工作流应按 1920×1080 逐页快照。

## 中日韩与多语言内容

### 推荐中文搭配

| 角色 | 西文字体 | 推荐中文搭配 | 来源 |
|---|---|---|---|
| Display / Headline（Bodoni Moda 700–800） | Bodoni Moda | 站酷小薇体 ZCOOL XiaoWei | Google Fonts |
| Body / Pill text（Space Grotesk 400–600） | Space Grotesk | 悠哉字体 Yozai | cn-fontsource CDN |

### 中西混排策略

用 **策略 A——单字体栈带回退**：在同一 `font-family` 栈里把中文字体声明在西文字体 *之后*，这样西文字形用 Bodoni Moda / Space Grotesk 渲染，中日韩字形自动落到中文字体。每个角色一条 CSS 规则，不用手工切 class。

### 加载

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400..900;1,6..96,400..900&family=Space+Grotesk:wght@300..700&family=ZCOOL+XiaoWei&display=swap" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/cn-fontsource-yozai-regular/font.css" rel="stylesheet">
```

```css
:root {
  --font-display: "Bodoni Moda", "ZCOOL XiaoWei", serif;
  --font-body: "Space Grotesk", "Yozai", sans-serif;
}
```

### 通用中日韩调整

- **行高**：把中日韩正文行高从 1.6 提到约 1.7——汉字比西文小写需要更多纵向呼吸。
- **字距**：汉字片段把 `letter-spacing` 清零（讨好 Bodoni 大写的负 tracking 会把汉字笔画挤在一起）。只在西文片段上保持紧 tracking。
- **大小写变换**：内容是汉字时，去掉任何胶囊 / 标签 / 副标题上的 `text-transform: uppercase`——中文没有大小写；强迫 uppercase 对汉字无效，却会破坏内部混排的西文缩写渲染。
- **标点**：中文句子用中文全角标点（，。：；「」），西文用半角（`,.:;""`）。永远不要把半角标点混进中文句子。
- **标题不加句号**：中文标题惯例省略句末 。——从展示字符串里去掉它。
- **盘古间距**：相邻汉字与西文 / 数字片段之间插入细空格（或普通空格）（例如 `2026 年`、`AI 产品`）。改善混排可读性。
- **一句一字体**：不要在句子中途切换中日韩字体家族。按角色为一段文字选 ZCOOL XiaoWei *或* Yozai，永远不要在一个短语里两个都用。

### 审美说明

ZCOOL XiaoWei 是高对比、偏文学衬线的汉字面孔，粗细笔画调制呼应 Bodoni Moda 的 Didone 音域——它给展示标题与西文原作同样的编辑-华美重量。Yozai 是友善圆润的汉字无衬线，开阔字怀和克制笔画对比镜像 Space Grotesk 的几何 grotesk，所以胶囊文字、标签和正文段落仍保留「干净现代无衬线」的感觉，而不是退回僵硬的系统汉字。两者都干净地配糖果色板：`{colors.ink}` 的 ZCOOL XiaoWei 保住「Bodoni 标题从不染色」的规则，Yozai 坐在 coral / lime / yellow 胶囊里，对着 2px 墨色描边仍可读。装饰漂浮胶囊壁纸在中文里仍然成立——用单字或双字氛围词（愿景、未来、下一步）替换英文大写五彩纸屑。

### 已知中日韩缺口

ZCOOL XiaoWei 是展示字体，字重轴有限（单字重），字形集也小于 Noto 家族——生僻或技术汉字（罕见姓氏、文言字、GB2312 之外的仅简体变体）可能回退到系统字体。繁体中文文稿把 Yozai 换成 `LXGW WenKai TC`（Google Fonts），覆盖更全，友善人文主义音域也相近。Bodoni 通过 opsz 轴做到的斜体 / 粗重时刻，中文字体没有等价物——西文会靠斜体 Bodoni 时，用尺度和颜色来补偿。

## 迭代指南

1. 任何新的装文本的容器都用胶囊几何——小的 9999px 圆角，卡片 2rem 圆角。不要引入尖角文本容器。
2. 任何新胶囊都带 2px 实线 `{colors.outline}` 描边。不要渲染未描边的胶囊。
3. 任何新标题都用 `{colors.ink}` 的 Bodoni Moda。不要给衬线标题上色；不要把展示换成 Space Grotesk。
4. 任何新卡片都带 `8px 8px 0 {colors.shadow}` 偏移阴影（小节点 4px，visual-frame 12px）。不要模糊；不要改色。
5. 任何新强调都用九色糖果色板，默认顺序 coral → lime → sky → violet → yellow → lavender → peach → mint。不要引入第十色。
6. 任何新的陈述性幻灯片（封面、收束、引文、陈述）都加 5–8 个漂浮装饰胶囊作氛围壁纸。
7. 任何新数据页都在画布背景加一到两道径向强调辉光。不要让奶油表面扁平空着。
8. Bodoni 引文正文里的任何行内强调都用 `quote-highlight` 胶囊。不要加粗；除了 `<em>` 里的 Bodoni italic 轴，不要斜体。
9. 新组件继承胶囊几何 + 2px 描边 + 4–12px 阴影模式。如果新组件打破这三条里的任何一条，先重新设计再加入。

## 已知缺口

- 加载了两个 Bodoni 字体轴（italic 和 opsz 6..96），但模板只在固定字号上使用正体轴；展示字号之间的光学尺寸变化没有显式启用。
- 条形图数值通过 `style="width: NN%"` 行内样式设定——没有数据绑定层。
- 装饰漂浮胶囊的位置和旋转都靠每个实例的行内样式手调；没有生成式摆放系统。
- visual-frame 的三段渐变（lavender → sky → mint）是硬编码「默认」——其他渐变组合有效，但需要按实例撰写。
- 颗粒叠层使用行内 SVG data URL；替换或移除它需要改标记，而不是 CSS 变量。
- 图表 bar-fill 右侧 2px 实线描边，才让条形有胶囊端帽定义；去掉它，条形就失去胶囊美感。
- 系统继承全部 9 个糖果强调 CSS 变量，但源里大约只用了 ~6 个——peach 和 mint 在色板里，但用得很少。它们可供新构图使用。
- 装饰漂浮胶囊把文字内容当作视觉身份的一部分（单个大写 Space Grotesk 单词）。这些词不是信息；新构图应选中性单词语氛围（"VISION"、"FUTURE"、"NEXT" 等），而不是内容特定文本。
