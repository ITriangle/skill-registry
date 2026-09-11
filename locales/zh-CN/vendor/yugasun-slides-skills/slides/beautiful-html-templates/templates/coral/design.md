---
version: alpha
name: Coral
description: "A bold magazine-poster system that runs on three surface registers — coral fire, ink black, and warm cream — animated by Bebas Neue display caps and a constant 45° diagonal hatch pattern. Inter handles body copy; Bebas Neue handles every headline, stat, title, and meta-figure at heavy letter-spacing. The cultural reference is mid-century travel posters, Saul Bass film titles, and modern editorial sport magazines: solid color planes meeting at hard edges, oversized condensed caps as architectural elements, and a single coral hue used both as accent and as full-slide environment."

colors:
  coral: "#E85D5D"
  coral-dark: "#D44A4A"
  cream: "#F5F0E8"
  cream-dark: "#E8E0D4"
  black: "#1A1A1A"
  gray: "#6B6B6B"
  light-gray: "#B0B0B0"
  white: "#FFFFFF"

color-aliases:
  bg: cream
  ink: black

typography:
  hero-title:
    fontFamily: "Bebas Neue, sans-serif"
    fontSize: "min(120px, 9vw, 13vh)"
    fontWeight: 400
    lineHeight: 0.9
    letterSpacing: 4px
  jumbo-feature:
    fontFamily: "Bebas Neue, sans-serif"
    fontSize: "clamp(80px, 15vw, 200px)"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 12px
  display-statement:
    fontFamily: "Bebas Neue, sans-serif"
    fontSize: "clamp(42px, 7vw, 100px)"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 2px
  section-headline:
    fontFamily: "Bebas Neue, sans-serif"
    fontSize: "clamp(40px, 6vw, 80px)"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 2px
  column-title:
    fontFamily: "Bebas Neue, sans-serif"
    fontSize: "clamp(36px, 5vw, 72px)"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 2px
  stat-numeral:
    fontFamily: "Bebas Neue, sans-serif"
    fontSize: "clamp(48px, 7vw, 96px)"
    fontWeight: 400
    lineHeight: 1
  card-stat:
    fontFamily: "Bebas Neue, sans-serif"
    fontSize: "clamp(36px, 4vw, 56px)"
    fontWeight: 400
    lineHeight: 1
  sidebar-value:
    fontFamily: "Bebas Neue, sans-serif"
    fontSize: "clamp(28px, 3vw, 48px)"
    fontWeight: 400
    lineHeight: 1
  card-title:
    fontFamily: "Bebas Neue, sans-serif"
    fontSize: "clamp(24px, 2.5vw, 36px)"
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 1px
  bar-title:
    fontFamily: "Bebas Neue, sans-serif"
    fontSize: "clamp(28px, 4vw, 56px)"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 2px
  meta-figure:
    fontFamily: "Bebas Neue, sans-serif"
    fontSize: "min(44px, 3.5vw, 5.5vh)"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 2px
  meta-date:
    fontFamily: "Bebas Neue, sans-serif"
    fontSize: "min(38px, 3vw, 4.8vh)"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 2px
  background-numeral:
    fontFamily: "Bebas Neue, sans-serif"
    fontSize: "clamp(100px, 15vw, 200px)"
    fontWeight: 400
    lineHeight: 1
    description: "Decorative oversized numeral placed inside a coral region at rgba(0,0,0,0.12) — wallpaper opacity. Sits behind the actual column title at full opacity."
  giant-mark:
    fontFamily: "Bebas Neue, sans-serif"
    fontSize: "clamp(140px, 20vw, 280px)"
    fontWeight: 400
    lineHeight: 1
    description: "Oversized quote mark or single character placed inside a coral region at opacity 0.35 — half-decorative, half-content."
  body:
    fontFamily: "Inter, sans-serif"
    fontSize: "clamp(15px, 1.4vw, 20px)"
    fontWeight: 400
    lineHeight: 1.7
  body-sm:
    fontFamily: "Inter, sans-serif"
    fontSize: "clamp(13px, 1.1vw, 16px)"
    fontWeight: 400
    lineHeight: 1.6
  body-light:
    fontFamily: "Inter, sans-serif"
    fontSize: "clamp(20px, 2.5vw, 36px)"
    fontWeight: 300
    lineHeight: 1.5
    description: "Lighter-weight Inter for pull quotes — weight 300 to contrast against the Bebas Neue dominant voice."
  item-text:
    fontFamily: "Inter, sans-serif"
    fontSize: "clamp(14px, 1.2vw, 18px)"
    fontWeight: 400
    lineHeight: 1.6
  card-text:
    fontFamily: "Inter, sans-serif"
    fontSize: "clamp(13px, 1.1vw, 16px)"
    fontWeight: 400
    lineHeight: 1.6
  bar-meta:
    fontFamily: "Inter, sans-serif"
    fontSize: "12px"
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 2px
    textTransform: uppercase
  section-label:
    fontFamily: "Inter, sans-serif"
    fontSize: "12px"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 4px
    textTransform: uppercase
  item-label:
    fontFamily: "Inter, sans-serif"
    fontSize: "11px"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 3px
    textTransform: uppercase
  meta-label:
    fontFamily: "Inter, sans-serif"
    fontSize: "11px"
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 3px
    textTransform: uppercase
  sidebar-label:
    fontFamily: "Inter, sans-serif"
    fontSize: "12px"
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 1px
  quote-attribution:
    fontFamily: "Inter, sans-serif"
    fontSize: "14px"
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 3px
    textTransform: uppercase
  quote-role:
    fontFamily: "Inter, sans-serif"
    fontSize: "12px"
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 1px

spacing:
  pad-y: "clamp(40px, 6vh, 80px)"
  pad-x: "clamp(40px, 8vw, 100px)"
  pad-y-tight: "clamp(28px, 4.5vh, 60px)"
  pad-col: "clamp(32px, 4vw, 60px)"
  gap-grid: "32px"
  gap-md: "40px"
  card-pad: "clamp(24px, 3vh, 40px)"
  bar-pad: "clamp(24px, 4vh, 40px)"

canvas:
  width: 100vw
  height: 100vh

components:
  diagonal-hatch:
    background: "repeating-linear-gradient(45deg, transparent, transparent 20px, rgba(0,0,0,0.06) 20px, rgba(0,0,0,0.06) 40px)"
    description: "Signature 45° diagonal hatch pattern in 6%-opacity black. Applied as a pseudo-element overlay on coral regions to provide texture without changing the surface color. Variant: -45° hatch on coral quote-left, with 30/60px stride. Variant: 90° vertical hatch in 10%-opacity black on coral gradient regions, with 60/62px stride. The hatch is a per-region atmospheric treatment, not a slide-level overlay."
  accent-line:
    width: "80px"
    height: "4px"
    background: "{colors.coral}"
    description: "Solid 80×4 coral rectangle used as a sub-headline accent rule. Closing or section-divider variant uses 60×4."
  quote-accent:
    width: "60px"
    height: "4px"
    background: "{colors.coral}"
    description: "60×4 coral rectangle placed above a quote attribution as a terminal accent."
  title-rule:
    width: "100%"
    height: "3px"
    background: "{colors.black}"
    opacity: 0.15
    description: "Full-width 3px ink rule at 15% opacity used as a subtle horizontal divider beneath the hero title on the cover composition."
  card:
    background: "{colors.white}"
    padding: "{spacing.card-pad}"
    borderTop: "5px solid {colors.coral}"
    description: "Column card — white surface with a 5px solid coral top border as the only border on the element. No shadow, no radius."
  sidebar-item:
    background: "{colors.white}"
    padding: "20px 24px"
    borderLeft: "4px solid {colors.coral}"
    description: "Compact data tile — white surface with a 4px solid coral left border. Holds a Bebas value and an Inter label."
  card-icon:
    width: "48px"
    height: "48px"
    background: "{colors.coral}"
    fontFamily: "Bebas Neue, sans-serif"
    fontSize: "24px"
    color: "{colors.white}"
    description: "48px solid coral square (no radius) containing a 1-character Bebas Neue glyph in white. Used as a card mark."
  timeline-line:
    height: "4px"
    background: "{colors.black}"
    description: "Horizontal 4px solid ink line spanning the timeline width. A ::after pseudo overlays a repeating linear-gradient (20px ink + 10px transparent) to create a dashed effect. The dashed pattern is rendered through the gradient, not the border-style."
  t-point-dot:
    width: "20px"
    height: "20px"
    borderRadius: "50%"
    background: "{colors.coral}"
    border: "4px solid {colors.cream}"
    description: "Timeline node — 20px coral circle with a 4px cream halo, sitting on the timeline-line."
  nav-dot:
    width: "10px"
    height: "10px"
    borderRadius: "50%"
    background: "rgba(255, 255, 255, 0.3)"
    border: "2px solid rgba(255, 255, 255, 0.5)"
    description: "Small 10px nav indicator. White-translucent default on dark/coral surfaces; ink-translucent .dark variant on cream surfaces. Active state fills with coral."
  nav-arrow:
    width: "44px"
    height: "44px"
    borderRadius: "50%"
    background: "rgba(255, 255, 255, 0.1)"
    border: "2px solid rgba(255, 255, 255, 0.3)"
    description: "44px circular nav button with translucent fill and 2px translucent border. .dark variant for cream surfaces. Hover state fills with coral."
  zigzag-layer:
    description: "SVG zigzag pattern overlay used decoratively on the cover's coral top-section. Renders as a thin black zigzag line at low opacity behind the title."
  pattern-overlay:
    description: "Decorative repeating-pattern overlay applied to feature regions — typically 90° vertical hatch in ink at 10% opacity on coral gradient backgrounds. Separate from the 45° diagonal-hatch which is the system's primary texture."
  bar-fill:
    description: "Chart.js horizontal bar fills use solid coral (#E85D5D) as the primary series color, with a darker coral (#D44A4A) for comparison or secondary series."
---

## 概述

Coral 是一套**大胆的杂志海报系统**，建在三套表面色域上——珊瑚火、墨黑和暖奶油——在硬边相接。定义性结构前提是**实色色块**：单页会拆成珊瑚一半 + 奶油一半 + 墨色顶区，每个区域都是一块平坦实色，装着自己自洽的构图。区域之间没有渐变过渡；两色相接处就是版式。这是更精致编辑系统的通俗对位——更接近体育杂志封面，而不是文学目录。

字体栈是**双脸层级**。**Bebas Neue**——高窄紧缩无衬线展示脸——承担每一个标题、每一个统计、每一个栏标题、每一个元数字、每一个区块名。Bebas 跑在它唯一可用的字重（400）上，被当成建筑——重字距（2–12px）、超大尺度（jumbo feature 到 200px），并且永远用它原生的大写。**Inter**——当代人文无衬线——承担每一段正文、每一个标签、每一个微文字、每一段落款。Inter 跨字重 300 到 700：引出式引文正文用 300，段落正文用 400，元标签用 600，区块 eyebrow 用 700。Bebas/Inter 配对构成系统的声线：Bebas 宣言，Inter 解释。

色板是**三块表面 + 墨 + 中性色**。珊瑚 `{colors.coral}` 既是*那一个*强调（侧栏砖上 4px 左边、卡片上 5px 顶边、48px 实心图标方），也是整页环境（一整块珊瑚面板、封面顶区、珊瑚渐变 feature 区）。奶油 `{colors.cream}` 是暖画布——杂志纸。墨 `{colors.black}` 是最强表面，用于引文和陈述版式的整页背景。白色只作为珊瑚或奶油区上的卡片填充出现。两档灰（`{colors.gray}`、`{colors.light-gray}`）扛正文和元文字。

纵深是**平面加硬色边**。没有投影、没有圆角表面、没有柔软抬升。层级来自：
- **实色区域分割** —— 珊瑚 / 墨 / 奶油区域在硬边相接。
- **强调边框** —— 4px 珊瑚左、5px 珊瑚顶、3px 墨顶、4px 墨水平。
- **45° 对角 hatch** —— 珊瑚区上招牌的 6% 透明度黑对角重复图案，提供纹理。
- **超大装饰排印** —— 12% 透明度的背景数字、35% 透明度的巨型引号，坐在主内容后面或旁边。

**密度哲学：中高，由区域结构化。** Coral 幻灯片是结构化的，而不是密的——每个色区装着自洽构图（一个栏标题配一块正文、一块统计砖配一个标签、一根时间线配五个点）。美学依赖区域在边界内感觉住满，而不是整页挤满。正确构图的一页配对 2–3 个实质区域，各自充分表达。感觉坏掉的一页，是珊瑚区只装着稀疏碎片，或奶油区试图扛太多互相竞争的元素。当内容本身填不满平面时，珊瑚区主标题后面 12% 透明度的装饰超大数字，是标准的「填满区域」动作。

**关键特征：**
- 三表面系统：`{colors.coral}`（火）、`{colors.black}`（墨）、`{colors.cream}`（纸）——作为实色区域在硬边相接。
- 每一个标题/统计/标题用 Bebas Neue 大写紧缩展示；每一段正文/标签/落款用 Inter 无衬线。
- 珊瑚区上 6% 透明度黑的 45° 对角 hatch 作为招牌气氛纹理。
- 珊瑚既是强调（4–5px 边框、48px 图标方、4 点时间线节点）也是环境（整区表面）。
- 珊瑚区栏标题后面 12% 透明度的装饰超大数字。
- 珊瑚区里 35% 透明度的超大引号作为半装饰内容。
- 矩形没有圆角；圆形只用于导航点、导航箭头和时间线节点。
- 每一个 Bebas 元素都有重字距：多数 1–4px，最大 feature 处理 12px。
- 硬边色分割（竖、横或 40/60 比例）定义幻灯片构图。

## 色彩

### 三表面系统
- **Coral**（`{colors.coral}` — #E85D5D）：招牌色——暖橙红，鲜艳但不霓虹。既作强调（4px sidebar-item 左边、5px 卡片顶边、48px card-icon 填充、80×4 强调线、60×4 引文强调、时间线节点、图表主系列、悬停填充、区块 eyebrow、奶油表面上的统计数字），也作整区表面（封面顶区、双栏左面板、全宽 feature 区、引文左面板）。定义系统。
- **Coral Dark**（`{colors.coral-dark}` — #D44A4A）：更深的珊瑚变体。用作线性渐变 feature 区的起点（135° 从 coral-dark 到 coral），以及图表次/对比系列色。
- **Cream**（`{colors.cream}` — #F5F0E8）：暖画布。用作默认幻灯片背景、封面底区、info-bar 表面、墨黑表面上的正文字色，以及时间线节点光晕。
- **Cream Dark**（`{colors.cream-dark}` — #E8E0D4）：略深一点的奶油。色板里可用于细微区域区分，但用得很少。
- **Black**（`{colors.black}` — #1A1A1A）：近黑墨。用作奶油表面上的标题色、引文和某些 feature 页的整背景墨色域、时间线色、title-rule 色、装饰背景数字色（珊瑚区里 12% 透明度），以及巨型标记色（珊瑚区里 35% 透明度）。
- **Gray**（`{colors.gray}` — #6B6B6B）：中性中灰。用于奶油表面上的正文段落、元标签、侧栏标签、卡片正文、引文角色。
- **Light Gray**（`{colors.light-gray}` — #B0B0B0）：浅中性。定义在色板里但用得很少——灰太强时可用于三级文字。
- **White**（`{colors.white}` — #FFFFFF）：真白。用作卡片填充（sidebar-item、card、column-card）、墨表面上的 item-text 色、nav-dot/nav-arrow 半透明填充。

### 默认值
- **默认幻灯片表面**：`{colors.cream}`。（封面和 feature 页用混表面构图；陈述、引文和三栏页默认奶油或墨。）
- **奶油表面上的默认标题色**：`{colors.black}` —— Bebas Neue 标题是墨，不是珊瑚。
- **珊瑚表面上的默认标题色**：`{colors.black}` —— 火上落墨。珊瑚上的 Bebas 永远是墨，从不是白。
- **墨表面上的默认标题色**：`{colors.cream}`。
- **奶油表面上的默认正文字色**：`{colors.gray}`。
- **墨表面上的默认正文字色**：`{colors.cream}`。
- **珊瑚表面上的默认正文字色**：`{colors.black}` —— 墨，不是白。
- **默认 eyebrow / 区块标签色**：奶油和墨表面上 `{colors.coral}`；珊瑚表面上 `{colors.black}`。
- **默认强调边框色**：`{colors.coral}` —— 4px 左（侧栏砖）、5px 顶（卡片）、48px 实心（图标方）。
- **珊瑚区内默认装饰数字色**：`rgba(0, 0, 0, 0.12)`（墨 12% 透明度）。
- **珊瑚区内默认巨型标记色**：`rgba(0, 0, 0, 0.35)`（墨 35% 透明度）。
- **默认图表主系列色**：`{colors.coral}`。
- **默认图表对比系列色**：`{colors.coral-dark}`。

三块表面按构图混用：一页可以拆成珊瑚/奶油、珊瑚/墨、墨/奶油，或守在单一表面。表面之间没有语义映射；每一块都为构图平衡和对比而选。

## 字体排印

### 字体家族
系统跑在**双脸层级**上：`Bebas Neue`（展示，单字重 400）承担每一个标题、统计数字、栏标题、元数字、bar 标题、卡片统计、侧栏值和装饰数字；`Inter`（无衬线，字重 300 / 400 / 600 / 700）承担每一段正文、标签、eyebrow、元标签、落款、角色和图表图例。没有第三张脸。

Bebas Neue 是高窄紧缩无衬线展示脸——窄字形允许大字号而不压满幻灯片宽度，它唯一可用的字重（400）被当成系统唯一字重。Bebas 永远用它原生的大写。系统的展示性格来自重字距（标准标题 1–4px，最大 jumbo feature 处理 12px）和超大尺度（jumbo / giant-mark 瞬间到 200–280px）。

Inter 以字重对比扛支撑声线：引出式引文正文用 300（相对 Bebas 主导的更轻色域），段落正文用 400，元标签用 600，区块 eyebrow 用 700。不用斜体和下划线。

### 字号阶梯

| Token | 字号 | 字体 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.giant-mark}` | clamp(140px, 20vw, 280px) | Bebas Neue | 400 | 珊瑚区内超大装饰引号或 feature 字符 |
| `{typography.jumbo-feature}` | clamp(80px, 15vw, 200px) | Bebas Neue | 400 | 填满 feature 区的单一主导词 |
| `{typography.background-numeral}` | clamp(100px, 15vw, 200px) | Bebas Neue | 400 | 珊瑚区内 12% 透明度的装饰壁纸数字 |
| `{typography.hero-title}` | min(120px, 9vw, 13vh) | Bebas Neue | 400 | 最大封面标题——三行标题断行 |
| `{typography.display-statement}` | clamp(42px, 7vw, 100px) | Bebas Neue | 400 | 奶油表面上的大宣言陈述 |
| `{typography.stat-numeral}` | clamp(48px, 7vw, 96px) | Bebas Neue | 400 | 英雄统计数字 |
| `{typography.section-headline}` | clamp(40px, 6vw, 80px) | Bebas Neue | 400 | 主区块标题 |
| `{typography.column-title}` | clamp(36px, 5vw, 72px) | Bebas Neue | 400 | 区域内的栏或面板标题 |
| `{typography.card-stat}` | clamp(36px, 4vw, 56px) | Bebas Neue | 400 | 每张卡片的统计数字 |
| `{typography.bar-title}` | clamp(28px, 4vw, 56px) | Bebas Neue | 400 | Info-bar 标题 |
| `{typography.sidebar-value}` | clamp(28px, 3vw, 48px) | Bebas Neue | 400 | 侧栏砖数值 |
| `{typography.card-title}` | clamp(24px, 2.5vw, 36px) | Bebas Neue | 400 | 卡片或栏卡片标题 |
| `{typography.meta-figure}` | min(44px, 3.5vw, 5.5vh) | Bebas Neue | 400 | 封面元数值（地点、日期、品牌） |
| `{typography.meta-date}` | min(38px, 3vw, 4.8vh) | Bebas Neue | 400 | 封面日期变体 |
| `{typography.body-light}` | clamp(20px, 2.5vw, 36px) | Inter | 300 | 引出式引文正文（更轻字重对抗 Bebas 主导） |
| `{typography.body}` | clamp(15px, 1.4vw, 20px) | Inter | 400 | 标准段落正文 |
| `{typography.item-text}` | clamp(14px, 1.2vw, 18px) | Inter | 400 | 墨表面上的条目正文 |
| `{typography.card-text}` | clamp(13px, 1.1vw, 16px) | Inter | 400 | 卡片正文 |
| `{typography.body-sm}` | clamp(13px, 1.1vw, 16px) | Inter | 400 | 紧凑正文 |
| `{typography.section-label}` | 12px | Inter | 700 | 标题上方的区块 eyebrow，4px 字距 |
| `{typography.item-label}` | 11px | Inter | 700 | 列表里的条目 eyebrow，3px 字距 |
| `{typography.meta-label}` | 11px | Inter | 600 | 封面元标签，3px 字距 |
| `{typography.quote-attribution}` | 14px | Inter | 600 | 引出式引文下方的作者名，3px 字距 |
| `{typography.bar-meta}` | 12px | Inter | 400 | Info-bar 元文字，2px 字距 |
| `{typography.sidebar-label}` | 12px | Inter | 400 | 侧栏砖标签，1px 字距 |
| `{typography.quote-role}` | 12px | Inter | 400 | 引文落款下方的作者角色，1px 字距 |

### 默认值
- **主区块标题默认字号**：`{typography.section-headline}`（clamp 40–80px）。
- **封面/英雄标题默认字号**：`{typography.hero-title}`（min(120px, 9vw, 13vh)）。
- **feature 主导词默认字号**：`{typography.jumbo-feature}`（clamp 80–200px），字距 12px。
- **段落正文默认字号**：`{typography.body}`（clamp 15–20px）。
- **任何大写 eyebrow / 标签默认字号**：`{typography.section-label}`（12px），字重 700，4px 字距；列表语境用 `{typography.item-label}`（11px），字重 700，3px 字距。
- **任何 Bebas Neue 元素的默认字重**：400（唯一可用字重）。
- **正文默认字重**：400；引出式引文用 300。
- **标签默认字重**：600 或 700。
- **英雄统计数字默认字号**：`{typography.stat-numeral}`（clamp 48–96px）。
- **卡片内统计数字默认字号**：`{typography.card-stat}`（clamp 36–56px）。

拿不准时，伸手去拿 `{typography.section-headline}` 做这一页的主文字瞬间。

### 招牌处理
这些处理在**对应元素类型一旦使用时就是必选项**：

- **每一个 Bebas Neue 元素都用它原生的大写。** 不存在句首大写的 Bebas Neue——字体本身不支持。这是系统最根基的排印规则。
- **每一个 Bebas Neue 元素都带至少 1px 字距。** 标准标题 2px，hero-title 4px，jumbo-feature 12px。没有 tracking 的 Bebas 读起来像没处理过。
- **每一个 Inter 标签、eyebrow 和元文字都是大写，字距 1–4px。** 区块标签 4px，条目标签 3px，bar-meta 2px，侧栏标签 1px。没有 tracking 的 Inter 大写会拆掉编辑色域。
- **每一个 Bebas 标题都按表面对比渲染成 `{colors.black}`、`{colors.cream}` 或 `{colors.coral}`** —— 从不是灰。颜色选择：奶油/珊瑚上用墨，墨上用奶油，奶油上需要强调时用珊瑚。
- **每一个区块 eyebrow 在奶油或墨上渲染成 `{colors.coral}`**，在珊瑚上渲染成 `{colors.black}`。不存在珊瑚压珊瑚。
- **珊瑚区内每一个装饰超大数字都渲染成 `rgba(0, 0, 0, 0.12)`** —— 壁纸数字招牌。坐在全力透明度的主内容后面。
- **珊瑚区内每一个巨型装饰标记（引号、单字符）都渲染成 `rgba(0, 0, 0, 0.35)`** —— 半装饰、半内容。
- **引出式引文正文用 Inter 字重 300，不用 Bebas。** 这是系统主「声线断裂」——内容需要感觉个人而不是宣言时，Inter Light 接手。

### 排印原则
Bebas-大写-tracking + Inter-混字重的组合就是系统的声线。换掉任何一张脸——用另一套展示无衬线做标题，或用 Bebas 做正文——会彻底拆掉系统。斜体不出现。下划线不出现。唯一的强调机制是字重（Bebas 主导）、大小写（Bebas + 标签永远大写）、颜色（奶油表面上的珊瑚）和表面翻转（把元素放进另一块区域）。

行高在阶梯顶部一律收紧：Bebas 元素 0.9–1.0；Inter 正文 1.6–1.7。展示压缩 + 开放正文，才给出系统的杂志海报节奏。

## 版式

### 画布系统
画布是 `100vw × 100vh`——全视口，溢出隐藏。每一张 `.slide` 绝对定位填满视口；同一时间一张幻灯片带着 `.active`（opacity 1，visibility visible）。过渡是 0.6s 透明度 + visibility 淡入淡出。

系统**没有通用 chrome 条**。每一页都是自洽构图，有自己的内边距、区域结构和颜色处理。导航是逐页的（导航箭头 + 导航点 + 页码计数），浮在活动表面上方，奶油表面用 `.dark` 变体。

### 内边距与间距阶梯
| Token | 值 | 用途 |
|---|---|---|
| `{spacing.pad-y}` | clamp(40px, 6vh, 80px) | 标准垂直幻灯片内边距 |
| `{spacing.pad-x}` | clamp(40px, 8vw, 100px) | 标准水平幻灯片内边距 |
| `{spacing.pad-y-tight}` | clamp(28px, 4.5vh, 60px) | 紧凑垂直内边距（封面底区） |
| `{spacing.pad-col}` | clamp(32px, 4vw, 60px) | 区域内的栏内边距 |
| `{spacing.gap-grid}` | 32px | 栏网格间距 |
| `{spacing.gap-md}` | 40px | 图表容器内部间距 |
| `{spacing.card-pad}` | clamp(24px, 3vh, 40px) | 卡片内部内边距 |
| `{spacing.bar-pad}` | clamp(24px, 4vh, 40px) | Info-bar 内部内边距 |

### 区域构图
Coral 的主版式动作是**多表面构图**。幻灯片拆成实色区域，区域边界定义版式。标准分割包括：
- `grid-template-rows: 32% 68%` —— 顶强调条 + 主体（封面构图）。
- `grid-template-rows: 1fr auto` —— 大 feature 区 + 底 info-bar。
- `grid-template-columns: 1fr 1fr` —— 等分竖拆（常常左珊瑚 + 右墨）。
- `grid-template-columns: 40% 60%` —— 窄强调栏 + 更宽内容栏（引文版式）。
- 单表面页 —— 整块画布是奶油或墨（陈述、三栏、时间线版式）。

区域之间的边界永远是**硬色边**——没有柔过渡、没有跨边界渐变、交界没有圆角。两块实色相接就是版式结构。

## 纵深与层次

### 平面加硬色边
Coral 没有投影、没有柔软抬升、没有圆角表面。每个元素都坐在同一平面上。

纵深信号完全是结构的：
- **硬色区域边界** —— 主结构信号。
- **强调边框** —— 卡片上 5px 珊瑚顶、侧栏砖上 4px 珊瑚左、4px 墨水平时间线、15% 透明度 3px 墨 title-rule。
- **45° 对角 hatch** —— 珊瑚区上 6% 透明度黑对角 repeating-linear-gradient 叠层创造纹理，没有纵深。
- **装饰壁纸排印** —— 12% 透明度的超大数字和 35% 透明度的巨型标记坐在主内容后面当壁纸，创造分层效果，不用 z-index 花招。

引入 box-shadow、抬起的卡片或柔渐变，会拆掉定义这套系统的通俗海报美学。

### 气氛 hatch 变体
45° 对角 hatch 是系统的主气氛处理，但出现几种步幅/角度变体：
- **45°、20/40px 步幅**，6% 透明度黑 —— 标准珊瑚区叠层。
- **-45°、30/60px 步幅**，6% 透明度黑 —— 珊瑚引文左面板变体。
- **90° 竖向、60/62px 步幅**，10% 透明度黑 —— 珊瑚渐变 feature 区叠层。

所有 hatch 都克制（6–10% 透明度黑）。它们提供纹理，不跟内容抢。

## 形状与处理

### 圆角
| 值 | 用途 |
|---|---|
| 50%（圆） | 仅圆形元素：`nav-dot`（10px）、`nav-arrow`（44px）、`t-point-dot`（20px 时间线节点） |
| 0 | 其余一切：每一个区域、每一张卡片、每一块侧栏砖、每一个图标方、每一张图、每一根强调线、每一根强调边 |

系统只用**两个半径值**：50%（真圆）或 0（尖角矩形）。不存在软圆角。卡片、图标方、info-bar 和 feature 区都是严格矩形。

### 描边粗细
- **5px solid `{colors.coral}`（顶）** —— 用于卡片顶边（栏卡片模式）。
- **4px solid `{colors.coral}`（左）** —— 用于 sidebar-item 左边。
- **4px solid `{colors.black}`（水平）** —— 用于时间线。
- **4px solid `{colors.cream}`（环）** —— 用作 20px 珊瑚时间线节点周围的光晕。
- **3px solid `{colors.black}` 15% 透明度** —— 用于封面英雄标题下方的 title-rule。
- **2px solid 半透明** —— 用于 nav-dot 和 nav-arrow 边框（深色表面上 rgba(255,255,255,0.3–0.5)；奶油表面上 rgba(26,26,26,0.2–0.4)）。

所有边框要么是珊瑚、黑、奶油，要么是半透明。带边矩形没有圆角。

### 装饰元素类型

**45° 对角 hatch** —— `repeating-linear-gradient(45deg, transparent, transparent 20px, rgba(0,0,0,0.06) 20px, rgba(0,0,0,0.06) 40px)` 作为 `::before` 伪元素叠在珊瑚区上。招牌气氛纹理。变体：-45°、90° 竖向、不同步幅。

**背景数字** —— 超大 Bebas Neue 数字（clamp 100–200px），`rgba(0, 0, 0, 0.12)`，放在珊瑚区内。坐在区域全力透明度的主栏标题后面，创造分层「序数壁纸」效果。

**巨型标记** —— 超大 Bebas Neue 字符（clamp 140–280px），`rgba(0, 0, 0, 0.35)`，放在珊瑚区内。用作半装饰半内容元素，通常是引文版式珊瑚左面板上的引号。

**卡片（栏卡片）** —— 白填充矩形，5px 珊瑚顶边作为唯一边框。顶部含 48px 实心珊瑚图标方、Bebas 卡片标题、Inter 卡片正文，底部珊瑚卡片统计。5px 顶边是唯一 chrome——没有其他边框、没有阴影、没有圆角。

**侧栏条目** —— 白填充矩形，4px 珊瑚左边作为唯一边框。含 Bebas 侧栏值和 Inter 侧栏标签。4px 左边是唯一 chrome。

**图标方** —— 48px 实心珊瑚矩形（无圆角），含一个白色 Bebas 单字符字形。用作卡片标记。

**Info bar** —— 横跨区域全宽的 flex 行，左 Bebas bar-title，右大写 Inter bar-meta。奶油背景；用作 feature 区下方的页脚带。

**时间线** —— 横跨时间线宽度的 4px 实线墨水平线，`::after` repeating-linear-gradient 叠层（20px 墨 + 10px 透明）造出虚线效果。时间线点是 20px 珊瑚圆配 4px 奶油光晕，沿线条均匀分布。

**强调线** —— 80×4 实心珊瑚矩形，用作副标题强调线，收束/引文语境用 60×4。永远珊瑚，永远实心，无圆角。

**Title rule** —— 全宽 3px 实线墨线，15% 透明度，用作封面英雄标题下方的细微水平分割。

**Zigzag 层** —— SVG 折线图案，渲染为低透明度细墨折线，装饰叠在封面珊瑚顶区上。

**图案叠层** —— 单独的重复图案叠层（通常 90° 竖向 hatch，10% 透明度墨）用在珊瑚渐变 feature 区。与标准 45° 对角 hatch 不同。

## 宜与忌

### 宜
- 把幻灯片构图成多表面区域分割——珊瑚、墨和奶油在硬色边相接。区域边界就是版式结构。
- 每一个 Bebas Neue 元素都用它原生的大写，至少 1px 字距——标准标题 2px，英雄标题 4px，jumbo feature 处理 12px。
- 每一个区块 eyebrow 在奶油和墨表面上用 `{colors.coral}` 大写 Inter 字重 700，字距 3–4px。
- 把 45° 对角 hatch（6% 透明度黑，20/40px 步幅）作为 `::before` 叠层用在珊瑚区上，作气氛纹理。
- 用卡片上 5px 珊瑚顶边和侧栏砖上 4px 珊瑚左边作为那些元素仅有的 chrome——没有其他边框、没有阴影、没有圆角。
- 当区域需要比标题本身更多的视觉重量时，在珊瑚区栏标题后面放 12% 透明度的超大装饰 Bebas 数字。
- 墨表面引文版式上用 Inter 字重 300（light）做引出式引文正文——更轻字重对抗 Bebas 主导。
- 珊瑚表面上的 Bebas 标题渲染成 `{colors.black}`（火上落墨）。本系统不存在珊瑚上的白标题。
- 任何图表数据都用珊瑚系列 + coral-dark 对比系列惯例。
- 用 48px 实心珊瑚图标方（无圆角、单个白色 Bebas 字形）作为标准卡片标记。

### 忌
- 不要把 Bebas Neue 渲染成句首大写。字体只有大写——那就是全部身份。
- 不要渲染没有字距的 Bebas。没有 tracking 的 Bebas 即使大字号也读起来像没处理过。
- 不要引入第四表面色。三块表面（珊瑚 / 墨 / 奶油）就是系统——加黄或蓝区会拆掉杂志海报身份。
- 不要把标题渲染成 `{colors.gray}`。标题是墨、奶油或珊瑚；灰只留给正文和元文字。
- 不要加投影、抬起的卡片或圆角表面。系统是平面的——纵深来自色区分割和强调边框。
- 不要圆任何矩形元素。卡片、侧栏砖、info bar、图标方、强调线——全是尖角矩形。
- 不要给 Bebas 配另一套无衬线正文字体。Bebas + Inter 配对是固定的。
- 不要把 Inter 标签渲染成句首大写。小号 Inter 文字永远是大写，字距 1–4px。
- 不要用渐变软化区域边界（稀有的 135° coral-dark → coral feature 渐变除外）。区域边缘是硬色相接。
- 不要用稀疏内容填一块珊瑚区。珊瑚要重量——要么把区域构图填满，要么用装饰超大数字 / 巨型标记当壁纸。

## 响应式行为

Coral 是一套视口流体的 1920×1080 演示系统，全程用 `clamp()`、`min()` 和相对视口单位。源码里没有显式响应断点——每个尺寸都在最小和最大边界之间缩放。

### 缩放行为
- 英雄标题经 `min(120px, 9vw, 13vh)` 缩放——同时被宽度和高度封顶，让三行标题不会溢出矮笔记本屏。
- Jumbo feature 从最小视口 80px 缩放到最大 200px。
- 正文从 15px 到 20px。
- 内边距经每区 `clamp` 缩放。
- 边框、图标方（48px）、导航点（10px）、导航箭头（44px）和时间线点（20px）是固定的，不缩放。

### 演示行为
- 前进：`ArrowRight` 或 `Space`。
- 后退：`ArrowLeft`。
- 导航点浮在右缘；导航箭头在左下；页码计数在右下。三者都带着奶油表面的 `.dark` 变体（墨半透明填充）和珊瑚/墨表面的标准变体（白半透明填充）。
- 活动导航点无论表面都填 `{colors.coral}`。

### 图表
图表用 Chart.js 渲染（经 CDN 加载）。主系列用 `{colors.coral}`；对比系列用 `{colors.coral-dark}`。图表样式在 JS 里行内配置；重设样式要改 JS，不是 CSS。

### 打印 / 导出
没有显式处理。每一页是 100vw × 100vh 块；导出工作流应对每页在 1920×1080 截图。45° hatch 叠层应在 PDF 捕获里正确渲染。

## 中日韩与国际内容

### 推荐中文配对

| 角色 | 拉丁字体 | 推荐中文配对 | 来源 |
|---|---|---|---|
| Display / Headline（Bebas Neue 大写 400） | Bebas Neue | 站酷小薇体 ZCOOL XiaoWei | Google Fonts |
| Body / Label（Inter 300–700） | Inter | 悠哉字体 Yozai | cn-fontsource CDN |

### 中英混排策略

用 **策略 A —— 单字体栈带回退**：在同一 `font-family` 栈里把 ZCOOL XiaoWei 声明在 Bebas Neue *之后*，Yozai 声明在 Inter *之后*，这样拉丁字形用 Bebas / Inter 渲染，CJK 字形自动落到中文面孔。每个角色一条 CSS 规则，不用手动切类。

### 加载

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@300..700&family=ZCOOL+XiaoWei&display=swap" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/cn-fontsource-yozai-regular/font.css" rel="stylesheet">
```

```css
:root {
  --font-display: "Bebas Neue", "ZCOOL XiaoWei", sans-serif;
  --font-body: "Inter", "Yozai", sans-serif;
}
```

### 通用 CJK 调整

- **行高**：把 CJK 正文字行高提到约 1.8（从 1.7）——汉字比拉丁小写需要更多垂直呼吸，而 Coral 的正文本就偏爱宽裕行距。
- **字距**：汉字跑段把 `letter-spacing` 清零（1–12px 的 Bebas tracking 和 1–4px 的 Inter tracking 会打碎汉字节奏）。只在拉丁 span 上保留重 tracking。
- **大小写变换**：内容是汉字时，任何标签/eyebrow/元文字都去掉 `text-transform: uppercase`——中文没有大小写；强制大写对汉字无效，但会弄坏里面混排的拉丁缩写。
- **标点**：中文句子用中文全角标点（，。：；「」），拉丁用半角（`,.:;""`）。永远不要把半角标点混进中文句子。
- **标题不加句号**：中文标题惯例省略末尾 。——从展示字符串里拿掉。
- **盘古之白**：相邻汉字与拉丁/数字跑段之间插入细空格（或普通空格）（例如 `2026 年`、`AI 产品`）。改善混排可读性。
- **一句一句一种字体**：不要在句子中间切换 CJK 家族。给定一段文字跑段按角色选 ZCOOL XiaoWei *或* Yozai，永远不要在一个短语里两套都用。

### 美学说明

ZCOOL XiaoWei 扛起 Bebas Neue 给拉丁提供的杂志海报声线——它高窄的汉字形态有类似的建筑展示色域，在 Coral 用于 jumbo feature 的 80–200px 字号上，ZCOOL XiaoWei 能站住形，不会像系统汉字脸那样碎掉。关键是，Bebas Neue「只有大写加重 tracking」的规则对汉字没有意义（没有大小写，没有 tracking），所以系统最根基的排印规则对 CJK 根本不适用——拿掉 tracking，拿掉大写，让 ZCOOL XiaoWei 只靠字号站住。Yozai 与 Inter 配对做正文和标签：它圆润的人文形态匹配 Inter 的暖意，在珊瑚 / 奶油 / 墨表面里仍清晰。三表面区域分割、45° 对角 hatch、装饰超大数字（可以保持拉丁——01、02、03 作为中文栏标题后面的壁纸完全成立）和 5px 珊瑚顶边都与内容无关，任何语言都一样工作。

### 已知 CJK 缺口

ZCOOL XiaoWei 是单字重展示脸，字形覆盖比 Noto 家族有限——生僻或技术汉字（罕见姓、古典字、GB2312 以外的简体变体）可能回退到系统字体。繁体中文片子把 Yozai 换成 `LXGW WenKai TC`（Google Fonts），TC 覆盖更全。Bebas Neue 的窄紧缩比例没有精确的中文对等——ZCOOL XiaoWei 充其量是中等紧缩，所以中文英雄标题会比拉丁对等大约多占 20% 水平空间。调整断行（通常两行中文标题填满与三行英文 hero-title 相同的面积），中文标题偏长时考虑提高 hero-title 的 `min()` 封顶。

## 迭代指南

1. 每一张新页是一到三块表面区域（珊瑚、墨、奶油）在硬边相接的构图。按内容强调选表面分割。
2. 每一个新标题都用大写 Bebas Neue，至少 1–2px 字距。不要句首大写；不要没 tracking。
3. 每一个新区块 eyebrow 用 Inter 字重 700 大写、4px tracking，奶油/墨上 `{colors.coral}`，珊瑚上 `{colors.black}`。
4. 每一张新卡片用 5px 珊瑚顶边 + 白填充 + 无阴影 + 无圆角模式。
5. 每一块新侧栏砖用 4px 珊瑚左边 + 白填充 + 无圆角模式。
6. 每一块新珊瑚区带着 6% 透明度的 45° 对角 hatch 叠层作纹理。
7. 感觉分量不够的新珊瑚区，在主标题后面加 12% 透明度的装饰超大 Bebas 数字当壁纸。
8. 新图表系列用珊瑚 + coral-dark；不要引入额外系列色。
9. 新引文版式把珊瑚左面板（35% 透明度巨型标记）与墨或奶油右面板（Inter 字重 300 的引文正文）配对。
10. 系统有三块表面和一个强调（珊瑚）。不要引入第四表面色或第二强调。

## 已知缺口

- Chart.js 库经 CDN 加载；图表样式在 JS 里行内配置，而不是从 CSS 变量读——重设样式要改 JS。
- 45° 对角 hatch 步幅值（标准 20px/40px；变体 30px/60px；竖向 60px/62px）按用途硬编码；没有参数化 hatch 组件。
- 装饰超大数字作为行内内容放置，数值硬编码；没有生成序数系统。
- 封面构图的 SVG zigzag-layer 是源码里嵌入的行内 SVG——调整折线图案需要改 SVG 标记。
- 时间线的虚线效果经 `::after` repeating-linear-gradient 叠层渲染，而不是 `border-style: dashed`——这给出对虚线尺寸的精确控制，但不寻常。
- 封面构图用 `min(120px, 9vw, 13vh)` 三轴封顶尺寸，防止三行标题在矮笔记本上溢出；新封面变体应遵循同样的多轴封顶模式。
- 引出式引文版式用 Inter 字重 300；Inter 字重 300 显式加载但别处不用——这是系统唯一的 Inter Light 部署。
- `cream-dark` 和 `light-gray` 色板 token 已定义，但源码里用得很少；它们可用于需要额外中性档的新构图。
- 导航点和导航箭头的 `.dark` 变体必须在奶油表面页上手工应用以维持可见性——没有自动表面检测。
- 线性渐变 feature 区（135° coral-dark → coral）是系统唯一刻意的渐变；所有其他表面都是平色。别处用渐变会拆掉平面表面美学。
