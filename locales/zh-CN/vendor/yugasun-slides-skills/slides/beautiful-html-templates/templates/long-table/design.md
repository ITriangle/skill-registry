---
version: alpha
name: Long Table
description: A warm, single-ink editorial system in the register of a supper-club poster, a small-batch zine, or a Risograph-printed program. The entire system runs in one ink color — a warm rust terracotta (#B53D2A) — on a buttery cream paper ground (#FAF1E2), with a subtle 4px radial-dot texture overlay giving the surface its "printed paper" quality. Display type runs in Bricolage Grotesque at weight 700–800 in uppercase; body and metadata run in Fraunces serif at weight 400–600 with optical-size axis engaged. Pill buttons, outlined edition badges, italic-edition numerals, and dashed/solid 1.5px borders complete the printed-program vocabulary.

colors:
  paper: "#FAF1E2"
  paper-d: "#F2E5CF"
  paper-vd: "#E8D7B6"
  ink: "#B53D2A"
  ink-dp: "#8E2D1F"
  rule: "#B53D2A"
  ink-32: "rgba(181, 61, 42, 0.32)"
  ink-78: "rgba(181, 61, 42, 0.78)"
  ink-50: "rgba(181, 61, 42, 0.5)"

color-aliases:
  rule: ink
  ink-32-canonical: "Same ink #B53D2A at 32% opacity, used for dashed dividers and subtle internal rules"
  ink-78-canonical: "Same ink #B53D2A at 78% opacity, used for de-emphasized metadata"

typography:
  display-jumbo-numeral:
    fontFamily: "'Fraunces', Georgia, serif"
    fontSize: "clamp(180px, min(22vw, 38vh), 480px)"
    fontWeight: 400
    lineHeight: 0.86
    letterSpacing: -0.02em
    fontStyle: italic
  display-cover:
    fontFamily: "'Bricolage Grotesque', sans-serif"
    fontSize: "clamp(82px, min(8.8vw, 15vh), 180px)"
    fontWeight: 800
    lineHeight: 0.92
    letterSpacing: -0.012em
    textTransform: uppercase
  display:
    fontFamily: "'Bricolage Grotesque', sans-serif"
    fontSize: "clamp(72px, min(7.6vw, 13vh), 160px)"
    fontWeight: 800
    lineHeight: 0.9
    letterSpacing: -0.012em
    textTransform: uppercase
  headline-xl:
    fontFamily: "'Bricolage Grotesque', sans-serif"
    fontSize: "clamp(60px, min(6.4vw, 10.5vh), 140px)"
    fontWeight: 800
    lineHeight: 0.9
    letterSpacing: -0.012em
    textTransform: uppercase
  headline:
    fontFamily: "'Bricolage Grotesque', sans-serif"
    fontSize: "clamp(56px, min(6vw, 10vh), 120px)"
    fontWeight: 800
    lineHeight: 0.9
    letterSpacing: -0.012em
    textTransform: uppercase
  headline-md:
    fontFamily: "'Bricolage Grotesque', sans-serif"
    fontSize: "clamp(48px, min(5vw, 8.4vh), 100px)"
    fontWeight: 800
    lineHeight: 0.92
    letterSpacing: -0.012em
    textTransform: uppercase
  quote:
    fontFamily: "'Bricolage Grotesque', sans-serif"
    fontSize: "clamp(40px, min(4.4vw, 7.4vh), 96px)"
    fontWeight: 700
    lineHeight: 0.95
    letterSpacing: -0.012em
    textTransform: uppercase
  card-title:
    fontFamily: "'Bricolage Grotesque', sans-serif"
    fontSize: "clamp(28px, 2.4vw, 44px)"
    fontWeight: 800
    lineHeight: 0.95
    letterSpacing: -0.008em
    textTransform: uppercase
  course-name:
    fontFamily: "'Bricolage Grotesque', sans-serif"
    fontSize: "clamp(20px, 1.5vw, 28px)"
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.005em
    textTransform: uppercase
  info-value:
    fontFamily: "'Bricolage Grotesque', sans-serif"
    fontSize: "clamp(20px, 1.6vw, 28px)"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.005em
    textTransform: uppercase
  edition-label-tracked:
    fontFamily: "'Bricolage Grotesque', sans-serif"
    fontSize: "clamp(15px, 1.1vw, 18px)"
    fontWeight: 700
    letterSpacing: 0.18em
    textTransform: uppercase
  who-tag:
    fontFamily: "'Bricolage Grotesque', sans-serif"
    fontSize: "clamp(15px, 1.05vw, 18px)"
    fontWeight: 700
    letterSpacing: -0.005em
    textTransform: uppercase
  body-serif-italic-lg:
    fontFamily: "'Fraunces', Georgia, serif"
    fontSize: "clamp(20px, 1.5vw, 28px)"
    fontWeight: 400
    lineHeight: 1.45
    fontStyle: italic
  body-serif-italic:
    fontFamily: "'Fraunces', Georgia, serif"
    fontSize: "clamp(17px, 1.2vw, 22px)"
    fontWeight: 400
    lineHeight: 1.5
    fontStyle: italic
  body-roman:
    fontFamily: "'Fraunces', Georgia, serif"
    fontSize: "clamp(15px, 1vw, 17px)"
    fontWeight: 400
    lineHeight: 1.45
  edition-label:
    fontFamily: "'Fraunces', Georgia, serif"
    fontSize: "clamp(20px, 1.6vw, 30px)"
    fontWeight: 400
    lineHeight: 1
    fontStyle: italic
  tagline:
    fontFamily: "'Fraunces', Georgia, serif"
    fontSize: "clamp(18px, 1.4vw, 26px)"
    fontWeight: 400
    lineHeight: 1.35
    fontStyle: italic
  stats:
    fontFamily: "'Fraunces', Georgia, serif"
    fontSize: "clamp(17px, 1.2vw, 22px)"
    fontWeight: 400
    lineHeight: 1.4
    fontStyle: italic
  pill-text:
    fontFamily: "'Fraunces', Georgia, serif"
    fontSize: "clamp(15px, 1.1vw, 20px)"
    fontWeight: 400
    lineHeight: 1
    fontStyle: italic
  meta-tag:
    fontFamily: "'Fraunces', Georgia, serif"
    fontSize: "clamp(14px, 0.95vw, 16px)"
    fontWeight: 400
    lineHeight: 1.4
    fontStyle: italic
  info-key:
    fontFamily: "'Fraunces', Georgia, serif"
    fontSize: "clamp(14px, 0.95vw, 16px)"
    fontWeight: 400
    letterSpacing: 0.16em
    textTransform: uppercase
    fontStyle: italic
  pagenum:
    fontFamily: "'Fraunces', Georgia, serif"
    fontSize: "clamp(14px, 0.95vw, 16px)"
    fontWeight: 400
    letterSpacing: 0.02em
    fontStyle: italic
  nav-hint:
    fontFamily: "'Fraunces', Georgia, serif"
    fontSize: "clamp(11px, 0.78vw, 13px)"
    fontWeight: 400
    letterSpacing: 0.02em
    fontStyle: italic

spacing:
  slide-pad-h-default: "clamp(60px, 5vw, 110px)"
  slide-pad-h-wide: "clamp(80px, 7vw, 160px)"
  slide-pad-h-narrow: "clamp(120px, 12vw, 280px)"
  slide-pad-top-default: "clamp(96px, 10vh, 160px)"
  slide-pad-top-cover: "clamp(60px, 6vh, 100px)"
  slide-pad-bottom-default: "clamp(110px, 11vh, 170px)"
  slide-pad-bottom-wide: "clamp(150px, 14vh, 220px)"
  gap-section: "clamp(28px, 3vh, 50px)"
  gap-content: "clamp(18px, 2vh, 32px)"
  gap-row: "clamp(14px, 1.6vh, 24px)"
  gap-tight: "clamp(10px, 1.2vh, 18px)"
  border-weight: "1.5px"
  rule-dashed-color: "{colors.ink-32}"

canvas:
  width: 100vw
  height: 100vh

components:
  pill:
    description: "Outlined rounded-rectangle (border-radius 999px → fully pill) holding short italic Fraunces text. The system's CTA / action button. Border is 1.5px solid {colors.ink}; padding is generous (~12px / 28px); text-color is {colors.ink}."
    border: "1.5px solid {colors.ink}"
    borderRadius: "999px"
    padding: "clamp(8px, 1vh, 14px) clamp(20px, 2vw, 32px)"
    typography: "{typography.pill-text}"
  pill-divider:
    typography: "{typography.pill-text}"
    opacity: 0.7
    description: "A small italic Fraunces divider character (typically · or /) used inline between adjacent pills."
  ed-badge:
    description: "A small circular outlined badge (~38px) holding a single italic Fraunces digit. The edition / chapter ordinal marker. Border is 1.5px solid {colors.ink}; background is transparent."
    width: "clamp(34px, 2.6vw, 44px)"
    height: "clamp(34px, 2.6vw, 44px)"
    border: "1.5px solid {colors.ink}"
    borderRadius: "50%"
  rect-tag:
    description: "Outlined rectangular tag — like the pill but with sharp corners. Holds short italic Fraunces text. Used as a category / status / metadata chip when the pill's roundness isn't appropriate."
    border: "1.5px solid {colors.ink}"
    padding: "clamp(7px, 0.9vh, 12px) clamp(14px, 1.4vw, 22px)"
    typography: "{typography.pill-text}"
  card-outlined:
    description: "A 1.5px ink-outlined rectangular content card. Holds a card-top metadata row (separated below by a 1px @ 32%-opacity rule), a Bricolage card-name, a Fraunces body description, and a meta-row at the bottom (separated above by a 1px dashed @ 32%-opacity rule). The system's primary content card pattern."
    border: "1.5px solid {colors.ink}"
    padding: "clamp(20px, 2vh, 32px) clamp(20px, 1.8vw, 30px)"
    internalDivider-solid: "1px solid {colors.ink-32}"
    internalDivider-dashed: "1px dashed {colors.ink-32}"
  paper-texture:
    description: "Subtle radial-dot texture overlay on the stage. A 4px-tile background-image of 0.5px radial-gradient dots in {colors.ink-50} at 10% opacity. Sits absolutely on the stage with pointer-events disabled, giving the paper its Risograph / printed-stock quality. This is on every slide."
    backgroundImage: "radial-gradient(circle at 1px 1px, {colors.ink-50} 0.5px, transparent 1px)"
    backgroundSize: "4px 4px"
    opacity: 0.1
  topbar-divider:
    description: "A 1.5px ink solid border-bottom under a slide topbar (where a Bricolage headline sits beside a small Fraunces label). The horizontal rule beneath the topbar is the system's universal page-divider device."
    borderBottom: "1.5px solid {colors.ink}"
  pagenum:
    position: "absolute"
    placement: "right: clamp(36px, 3.6vw, 80px); bottom: clamp(40px, 4vh, 64px)"
    typography: "{typography.pagenum}"
    color: "{colors.ink}"
    description: "Italic Fraunces page number at the bottom-right of every slide."
  nav-hint:
    position: "fixed"
    placement: "left: clamp(36px, 3.6vw, 80px); bottom: clamp(40px, 4vh, 64px)"
    typography: "{typography.nav-hint}"
    color: "{colors.ink}"
    opacity: 0.45
    description: "A faint italic Fraunces hint string at the bottom-left of the viewport (e.g. '← → to navigate'). Bonus interactivity affordance."
  ledger-row:
    description: "A horizontal ledger-style row in a calendar/schedule context. Multi-column grid (typical: 80px / 130px / 1.6fr / 0.9fr / auto) with a 1px @ 32%-opacity ink border-bottom. Each cell is a tag, label, or pill. Reads as a guestbook / restaurant-reservation log."
    rowPad: "clamp(11px, 1.3vh, 18px) 0"
    borderBottom: "1px solid {colors.ink-32}"
---

## 概述

Long Table 是一套**单色油墨编辑系统**，气质接近晚餐会海报、Risograph zine，或小出版社晚宴节目单。底层前提是单色：系统里每一个可见标记——每一条标题、每一段、每一条边框、每一条线、每一个胶囊、每一个页码——都用同一种暖锈陶土墨（`{colors.ink}` — #B53D2A）印在黄油奶油纸地上（`{colors.paper}` — #FAF1E2）。唯一的色彩变化是不透明度：同一墨色 100% 做主标记，78% 做弱化元信息，32% 做虚线内部分隔，10% 做纸纹点。

单墨约束就是系统的身份。审美借自单色丝网印刷、凸版海报和 Risograph 信笺——那些格式里每多一色就是一次独立印次，因此是刻意决定。承诺只用一色墨，系统得到印刷物的平静权威，而不是数字表面的抛光。

每一页上都有签名的**纸纹叠加**：4px 瓷砖径向点图案，50% 不透明度墨再乘 10% 不透明度，通过 `.stage::before` 伪元素施加。日常观看距离上看不见这些点，凑近才可见——它们给奶油表面「印刷纸」的手感，是设计系统的必要部分，不是可选装饰。

排印栈是两套字体配对：

- **Bricolage Grotesque** 字重 700 和 800、**严格全大写**，承担每一个展示时刻——封面、标题、卡片标题、菜品名、引语正文、信息值、who-tag。Bricolage 是略收的宽无衬线，性格强；全大写套装有手写海报的冲击力。启用了光学字号轴（`opsz` 12..96）。
- **Fraunces** 字重 400–600 承担每一段正文、每一个元信息字段、每一个胶囊、每一个页码、每一个版次标签。**斜体 Fraunces 是默认正文样式**——斜衬线是系统的正文声音，带来暖意和编辑性格。正体 Fraunces 只出现在特定紧场合（信息键、索引卡片里的说明正文）。两种样式都启用光学字号轴（`opsz` 9..144）。

巨大的**斜体 Fraunces 版次数字**，最大到 480px，是系统的签名展示锚——它替换传统上会填满封面/精选页右半的手绘插图，给这一页一个与其余页面同色墨的排印中心。

纵深是**扁平、印刷的**。没有阴影、没有渐变、没有模糊、没有光晕。抬升完全通过卡片、徽章、胶囊和标签上的 1.5px 实心墨边框；32% 不透明度的 1px 实线或 1px 虚线内部分隔；以及纹理叠加的气氛质感来传达。整套系统读起来像渗进纸里的墨。

**密度哲学：丰富但经过策展。** Long Table 在幻灯片承载实质内容时读成权威——封面带 hero 标题加标语加动作胶囊加数据加一个大版次数字；索引页带顶栏标题加三张丰富卡片；菜单页带五行菜品，每行有名称 + 说明 + 配酒。页是满的，但从不挤——每个区域承载一个聚焦元素，四周有呼吸空间。一页只放一条标题读成缺了节目单；一页放 8 块互相抢戏的内容读成坏掉。每页伸手去一个主要排印时刻（Bricolage 展示），再锚上 2–4 组支撑（卡片、胶囊、账本行、信息值对）。

**关键特征：**
- 一种墨色（`{colors.ink}` — 暖锈陶土）印在奶油纸（`{colors.paper}`）上。不透明度变体是唯一的色彩变化。
- 每一个展示时刻用 Bricolage Grotesque 字重 700–800 全大写；每一个正文和元信息时刻用 Fraunces 400–600、默认斜体。
- 每一页通过 `.stage::before` 有微妙的 4px 径向点纸纹——远看不见，近处在场。
- 胶囊按钮（圆角 999px）、版次徽章（圆形）、矩形标签（尖角）、描边卡片（1.5px 实线）——全是单重量墨描边，无填充。
- 巨大的斜体 Fraunces 版次数字（最大 480px）是封面级幻灯片上系统的 hero 排印锚。
- 1.5px 结构边框，1px @ 32% 不透明度实线或虚线内部分隔。没有更粗边框，没有阴影。
- 每一页右下角有页码（斜体 Fraunces）；左下角有导航提示（斜体 Fraunces，45% 不透明度）。
- 系统设计为单墨——加上任何第二色（海军蓝、绿、黄）会打碎印刷节目单气质。

## 色彩

### 色板
- **Paper / 奶油**（`{colors.paper}` — #FAF1E2）：主导的暖黄油奶油表面。读成好品质纸张——不是白，不是米色，介于两者之间。默认幻灯片背景，也是系统使用的唯一背景填充。
- **Paper Dark**（`{colors.paper-d}` — #F2E5CF）：略深的奶油，用于次级表面或色调分离。在 token 系统里可用，但用得省。
- **Paper Very Dark**（`{colors.paper-vd}` — #E8D7B6）：更深的奶油，用于强调表面。预留。
- **Ink / 暖锈陶土**（`{colors.ink}` — #B53D2A）：唯一墨色。每一段文字、每一条边框、每一条线、每一个胶囊描边、每一个页码——全是这一色。系统的结构色与表达色。
- **Ink Deep**（`{colors.ink-dp}` — #8E2D1F）：更深的锈色，留给强调。在 token 系统里可用，已发布幻灯片里用得省。
- **Rule**（`{colors.rule}` — #B53D2A）：`{colors.ink}` 的别名——同一 hex，语义上指线条时使用。
- **Ink @ 78%**（`{colors.ink-78}` — rgba(181,61,42,0.78)）：78% 不透明度的墨。用于需要略低对比的弱化元信息文字（例如菜单行里的配酒注、引语下的元标签）。
- **Ink @ 50%**（`{colors.ink-50}` — rgba(181,61,42,0.5)）：50% 不透明度的墨。用于纸纹径向点渐变内部。
- **Ink @ 32%**（`{colors.ink-32}` — rgba(181,61,42,0.32)）：32% 不透明度的墨。用于内部分隔——卡片内、账本行之间、菜品行之间的 1px 实线和 1px 虚线。

### 默认值
- **默认幻灯片背景**：`{colors.paper}`。每一页。本系统没有备用表面。
- **默认文本颜色**：`{colors.ink}`。每一段文字。
- **默认边框颜色**：结构边框用 `{colors.ink}`、1.5px solid；内部分隔用 `{colors.ink-32}`、1px solid 或 dashed。
- **默认标题颜色**：`{colors.ink}`。
- **默认正文颜色**：`{colors.ink}`。
- **默认页码 / 导航提示颜色**：`{colors.ink}`（页码全不透明度；导航提示 45% 不透明度）。
- **默认弱化元信息颜色**：`{colors.ink-78}`——当一小块支撑文字需要从主行后退时。

色板刻意单墨。没有可以伸手去的「强调色」——设计语言依赖单墨约束。若某个时刻需要突出，放大字号（Bricolage 800 到 180px）或伸手去斜体 Fraunces 版次数字；不要引入第二色。

## 字体排印

### 字体家族
系统恰好从 Google Fonts 加载两套网页字体，都带光学字号轴：

- **Bricolage Grotesque**，`opsz` 12..96，字重 400、600、700、800。**已发布幻灯片只用 700 和 800。**
- **Fraunces**，`opsz` 9..144，正体与斜体，字重 400、500、600。**已发布幻灯片使用斜体的全部三个字重，以及正体的 400/600。**

两字体角色划分很严：**Bricolage 全大写承担每一个展示时刻**（封面、标题、卡片标题、菜品名、引语正文、信息值、who-tag、带字距的版次标签）。**Fraunces 斜体承担每一个正文时刻**（段落、导语、元信息、标语、胶囊、页码、信息键、不带字距的版次标签）。**Fraunces 正体**留给特定紧角色（信息行里斜体字距会显得不合的信息键，以及索引卡片里正体更好读的说明正文）。

光学字号轴至关重要：同一套 Fraunces 在 14px 元信息与 480px hero 数字上会画出略有不同的字形——小尺寸拾取更结实的笔画；大尺寸拾取更细的细节。没有 `opsz` 的自托管回退会失去这种品质。

### 展示、正文与铬件字号阶梯

| Token | 字号 | 字体 | 字重 / 样式 | 用途 |
|---|---|---|---|---|
| `{typography.display-jumbo-numeral}` | 最大 480px | Fraunces | 400 斜体 | Hero 版次数字（封面级排印锚） |
| `{typography.display-cover}` | 最大 180px | Bricolage | 800 全大写 | 封面级 Bricolage 标题 |
| `{typography.display}` | 最大 160px | Bricolage | 800 全大写 | 章节开场 / 宣言标题 |
| `{typography.headline-xl}` | 最大 140px | Bricolage | 800 全大写 | 精选版次标题 |
| `{typography.headline}` | 最大 120px | Bricolage | 800 全大写 | 索引 / 日历页上的顶栏标题 |
| `{typography.headline-md}` | 最大 100px | Bricolage | 800 全大写 | 菜单 / 节目单标题 |
| `{typography.quote}` | 最大 96px | Bricolage | 700 全大写 | 引语 / 证言正文 |
| `{typography.card-title}` | 最大 44px | Bricolage | 800 全大写 | 描边卡片内的标题 |
| `{typography.course-name}` | 最大 28px | Bricolage | 700 全大写 | 账本行里的菜品 / 项目名 |
| `{typography.info-value}` | 最大 28px | Bricolage | 700 全大写 | 键/值信息行里的值 |
| `{typography.edition-label-tracked}` | 最大 18px | Bricolage | 700 全大写 / 0.18em | Hero 数字下方的大版次标签 |
| `{typography.who-tag}` | 最大 18px | Bricolage | 700 全大写 | 引语行里的署名名 |
| `{typography.body-serif-italic-lg}` | 最大 28px | Fraunces | 400 斜体 | 宣言 / 书信里的导语段落 |
| `{typography.body-serif-italic}` | 最大 22px | Fraunces | 400 斜体 | 标准正文段落 / 导语 |
| `{typography.body-roman}` | 最大 17px | Fraunces | 400 正体 | 卡片说明正文（小尺寸为易读而更紧） |
| `{typography.edition-label}` | 最大 30px | Fraunces | 400 斜体 | 版次徽章旁的 "EDITION N." 斜体标签 |
| `{typography.tagline}` | 最大 26px | Fraunces | 400 斜体 | 封面标题下的标语 / 副标题 |
| `{typography.stats}` | 最大 22px | Fraunces | 400 斜体 | 数据行（"N seats · M cities · L hours"） |
| `{typography.pill-text}` | 最大 20px | Fraunces | 400 斜体 | 胶囊按钮或矩形标签内的文字 |
| `{typography.meta-tag}` | 最大 16px | Fraunces | 400 斜体 | 卡片元信息（城市标签、编号标签、座位标签、日期标签） |
| `{typography.info-key}` | 最大 16px | Fraunces | 400 斜体 / 0.16em / 全大写 | 键/值信息行里的键 |
| `{typography.pagenum}` | 最大 16px | Fraunces | 400 斜体 | 每一页右下角的页码 |
| `{typography.nav-hint}` | 最大 13px | Fraunces | 400 斜体 / 45% 不透明度 | 视口左下角的导航提示 |

### 默认值
- **主幻灯片标题的默认字号**：`{typography.headline}`（最大 120px），Bricolage 800 全大写。
- **封面级标题的默认字号**：`{typography.display-cover}`（最大 180px）。
- **封面级幻灯片上 hero 排印锚的默认字号**：`{typography.display-jumbo-numeral}`（斜体 Fraunces，最大 480px）——系统的签名 hero 元素。
- **正文段落的默认字号**：`{typography.body-serif-italic}`（最大 22px），斜体 Fraunces。
- **导语段落的默认字号**：`{typography.body-serif-italic-lg}`（最大 28px）。
- **卡片内正文的默认字号**：`{typography.body-roman}`（最大 17px），**正体** Fraunces——小尺寸时正体比斜体更好读。
- **"EDITION N." 标签的默认字号**：`{typography.edition-label}`（最大 30px），斜体 Fraunces，与 `{components.ed-badge}` 圆形序数成对。
- **任何 Bricolage 展示时刻的默认字重**：800。（字重 700 留给引语正文和菜品/who-tag 元素；字重 800 是主展示字重。）
- **任何 Fraunces 正文时刻的默认字重**：400。

拿不准时，日常幻灯片标题伸手去 `{typography.headline}`（最大 120px）。140–180px 这一档用于精选版次标题和封面；160px 这一档用于章节开场。当幻灯片是封面级时刻、需要 hero 锚时，用超大版次数字。

### 标志性处理
只要用到对应元素类型，这些处理就**不可省略**：

- **每一个 Bricolage 展示元素都是全大写，带负字距（-0.005em 到 -0.012em）。** 本系统不存在句首大写的 Bricolage 标题。全大写 + 负字距 + 字重 800 的组合就是系统的展示声音。
- **每一个 Fraunces 正文元素默认斜体。** 正体 Fraunces 只出现在特定紧场合（信息行里的 info-key、索引卡片内正文）。拿不准时用斜体。
- **版次徽章（`{components.ed-badge}`）始终与斜体版次标签成对**——圆形序数和 "EDITION N." 文字是一个单元。只用其中一个读成坏掉。
- **每一张卡片 / 胶囊 / 矩形标签 / 徽章都带 1.5px 实心墨边框、无填充。** 单重量描边形状词汇就是系统的结构语言。不存在填色形状。
- **纸纹叠加（`{components.paper-texture}`）在每一页上。** 去掉它（或在没有纹理的纯平奶油上跑系统）会失去印刷纸质感。
- **每一页右下角都带页码标记**，斜体 Fraunces。页码是系统的脊柱——没有它，幻灯片会显得没锚。
- **卡片内部分隔在内容上方用 1px solid @ 32% 不透明度，内容下方用 1px dashed @ 32% 不透明度。** 实线/虚线配对是系统的卡片节奏装置。

### 排印原则
字重 800 + 全大写 + 负字距的组合就是系统的 Bricolage 声音。改掉这三项里的任何一项（例如字重 700 全大写，或字重 800 句首大写，或默认字距）都会读成另一套设计系统。Fraunces 默认斜体 + opsz 轴的组合就是系统的正文声音——用无 opsz 的回退字面会压平小尺寸上的品质。

不用下划线。正文段落里的加粗用 Fraunces 字重 600（不是 700/800）。不存在颜色强调，因为只有一色。系统仅有的强调机制是：尺度（更大的 Bricolage）、正文内字重切换（Fraunces 400 → 600）、斜体 ↔ 正体切换，以及不透明度（全 → 78%）。

## 版式

### 画布系统
系统面向流体视口——每个 `.slide` 是 `100vw × 100vh`，绝对定位。幻灯片叠在带纸纹叠加的 `.stage` 容器里，纹理绝对坐在舞台上。同一时间只有一个 `.slide.active` 可见；页间不透明度转场 280ms。

### 内边距阶梯（使用 `clamp()` 范围）
| Token | 范围 | 用途 |
|---|---|---|
| `{spacing.slide-pad-h-default}` | clamp(60px, 5vw, 110px) | 默认水平幻灯片内边距 |
| `{spacing.slide-pad-h-wide}` | clamp(80px, 7vw, 160px) | 精选 / 日历页更宽的水平内边距 |
| `{spacing.slide-pad-h-narrow}` | clamp(120px, 12vw, 280px) | 菜单 / 引语页更窄的水平内边距（把内容逼进一栏） |
| `{spacing.slide-pad-top-default}` | clamp(96px, 10vh, 160px) | 默认顶内边距 |
| `{spacing.slide-pad-top-cover}` | clamp(60px, 6vh, 100px) | 封面顶内边距（更少，给标题空间） |
| `{spacing.slide-pad-bottom-default}` | clamp(110px, 11vh, 170px) | 默认底内边距（给页码铬件留空间） |
| `{spacing.slide-pad-bottom-wide}` | clamp(150px, 14vh, 220px) | 精选 / 引语页更宽的底内边距 |
| `{spacing.gap-section}` | clamp(28px, 3vh, 50px) | 主要内容区块之间 |
| `{spacing.gap-content}` | clamp(18px, 2vh, 32px) | 相关内容块之间 |
| `{spacing.gap-row}` | clamp(14px, 1.6vh, 24px) | 行级元素之间（菜品行、账本行） |
| `{spacing.gap-tight}` | clamp(10px, 1.2vh, 18px) | 紧密耦合元素之间 |

### 铬件解剖
每一页右下角都带**页码标记**（斜体 Fraunces，最大约 16px）。视口左下角还带**导航提示**（斜体 Fraunces，45% 不透明度），提示键盘导航。这两个铬件元素是系统通用的幻灯片锚。

带顶栏的幻灯片（索引、日历）左侧是 Bricolage 标题 + 右侧一个小斜体 Fraunces 标签，下方用 1.5px 实心墨水平线隔开。顶栏分隔线是系统通用的页分隔装置。

### 圆角
- **999px** —— 胶囊按钮（完全胶囊形）
- **50%** —— 圆形版次徽章
- **0** —— 其余每一种形状（卡片、矩形标签、信息卡、账本行、内部分隔）

系统对内容容器用尖角，对动作和序数标记用胶囊/圆。不存在中等圆角值（4px、8px、12px）。

## 层次与纵深

### 扁平，无阴影
系统使用**零阴影**。没有 box-shadow、没有 text-shadow、没有 filter、没有渐变。抬升完全通过以下传达：

1. **1.5px 实心墨边框** 在卡片、胶囊、徽章、矩形标签上——描边形状词汇就是系统的结构纵深。
2. **32% 不透明度的 1px 实线或虚线内部分隔** 在卡片内和行之间——微妙的水平线给卡片内部节奏。
3. **每一页 10% 不透明度的纸纹叠加**——点状纹理气氛性地坐在所有内容下面，给页面印刷纸质感。
4. **文本上的不透明度分层**——主文字 100%，弱化元信息 78%，近乎看不见的分隔 32%。

没有阴影，本身就是纵深语言。加上 `box-shadow: 0 4px 12px rgba(0,0,0,0.1)` 会打碎印刷纸感。

### 纸纹作为气氛纵深
`.stage::before` 上的径向点纹理是纵深系统的一部分——不是可选装饰。纹理给奶油表面一种平坦 #FAF1E2 所缺的品质：表面是带纹理的纸张，不是 CSS 背景填充。4px 瓷砖、0.5px 径向点、50% 不透明度墨、整体 10% 不透明度，校准成日常观看距离上看不见，凑近检查时刚好可见。

## 形状与处理

### 描边粗细与样式
- **1.5px solid `{colors.ink}`** —— 通用结构边框。卡片、胶囊、版次徽章、矩形标签、顶栏分隔、who-row 顶边、信息卡描边。
- **1px solid `{colors.ink-32}`** —— 卡片内的实心内部分隔（卡片顶元信息与卡片标题之间），账本行之间，菜品行之间。
- **1px dashed `{colors.ink-32}`** —— 卡片内的虚线内部分隔（卡片正文与底部元信息行之间），信息卡里信息行之间。

边框从不超过 1.5px。颜色从不超过墨（全或不透明度 32%）。从不用点线（点线留给纸纹图案）。卡片内的实线/虚线配对是系统的签名节奏装置。

### 装饰元素类型

**纸纹叠加**（`{components.paper-texture}`）—— `.stage::before` 上 4px 瓷砖径向点图案，50% 不透明度墨、整体 10% 不透明度。系统的气氛底；每一页都有。

**胶囊按钮**（`{components.pill}`）—— 描边的全圆角矩形（圆角 999px），内放短斜体 Fraunces 文字。系统的 CTA / 动作按钮。胶囊在动作行里成组（例如封面动作行）。

**胶囊分隔**（`{components.pill-divider}`）—— 行内胶囊之间放置的小斜体 Fraunces 字符（通常是 `·` 或 `/`），70% 不透明度。

**版次徽章**（`{components.ed-badge}`）—— 约 38px 圆形描边徽章，内放单个斜体 Fraunces 数字。系统的版次 / 章节序数标记；始终与斜体 "EDITION N." 标签成对。

**矩形标签**（`{components.rect-tag}`）—— 描边尖角矩形标签，内放短斜体 Fraunces 文字。胶囊的尖角表亲；用在圆意不合适的地方。

**描边卡片**（`{components.card-outlined}`）—— 1.5px 墨描边矩形卡片。内放卡片顶元信息行（下方用 1px @ 32% 实线分隔）、Bricolage 卡片标题、Fraunces 正文说明，以及底部元信息行（上方用 1px @ 32% 虚线分隔）。系统的主内容卡片。

**带分隔的顶栏** —— 左侧 Bricolage 标题 + 右侧小斜体 Fraunces 标签，下方 1.5px 实心墨水平线隔开。系统通用的章节开场。

**信息卡** —— 更宽的描边卡片，内含信息行（键 / 值对，用 1px @ 32% 虚线分隔）。用作精选版次的支撑面板。

**账本行**（`{components.ledger-row}`）—— 多列网格行，1px @ 32% 实心底边框。列对齐地放标签、标签文字和胶囊。系统的日历 / 日程 / 索引模式。

**菜品行** —— 64px / 1fr / auto 网格行，1px @ 32% 实心底边框。放 Fraunces 编号标签、一个项目（Bricolage 名 + Fraunces 说明），以及 Fraunces 配酒标签。菜单 / 节目单模式。

**斜体超大版次数字** —— 巨大的斜体 Fraunces 数字，最大 480px。封面级幻灯片上系统的签名 hero 排印锚，下方配小字距 Bricolage 标签和一条斜体 Fraunces 元信息行。

**页码**（`{components.pagenum}`）—— 每一页右下角的斜体 Fraunces。

**导航提示**（`{components.nav-hint}`）—— 视口左下角 45% 不透明度的斜体 Fraunces，提示键盘导航。

## 应做与不应做

### 应做
- 承诺单墨渲染。每一段文字、边框、线、徽章和胶囊都是 `{colors.ink}` —— 暖锈陶土。用变化用不透明度（78%、32%、10%），从不用不同色相。
- 每一页都应用纸纹叠加。10% 不透明度的 4px 径向点图案是设计系统的一部分，不是可选抛光。
- 每一个 Bricolage 展示元素都跑字重 800（引语 / 菜品名 / who-tag 用 700）、严格全大写、负字距。
- 每一个 Fraunces 正文元素默认斜体。正体只用于信息键（斜体字距会显得不合）和卡片正文说明（小尺寸斜体较差读）。
- 封面级幻灯片把斜体 Fraunces 超大数字（最大 480px）当作 hero 排印锚。这是系统的签名。
- 每一个版次徽章都配斜体 "EDITION N." Fraunces 标签——圆形序数和文字标签是一个单元。
- 主内容卡片用描边卡片模式（1.5px 墨边框 + 内容上方 1px @ 32% 实线分隔 + 内容下方 1px @ 32% 虚线分隔）。实线/虚线配对是系统的节奏。
- 有意地用胶囊（圆角 999px）和矩形标签（尖角）——胶囊做动作，矩形做元信息 / 状态。不要把它们混为一谈。
- 每一页放置页码标记（斜体 Fraunces，右下）。标记是系统的脊柱。
- 保持幻灯片丰富但经过策展：一个主要 Bricolage 展示时刻 + 2–4 组支撑（卡片、胶囊、账本行、信息对）。单元素页显得过轻；8 元素页显得坏掉。

### 不应做
- 不要引入第二墨色。系统是单墨的——加上海军蓝、绿、黄或任何第二色相会打碎印刷节目单气质。
- 不要填充任何形状。卡片、胶囊、徽章、矩形标签只描边。不存在墨色填充矩形。
- 不要在任何元素上用 box-shadow、渐变、模糊或 filter。系统是扁平印刷纸。
- 不要省略纸纹叠加。没有点图案的平坦 #FAF1E2 背景读成数字，不像纸。
- 不要把 Bricolage 跑成句首大写。Bricolage 始终全大写、负字距、字重 700 或 800。
- 不要默认把 Fraunces 渲染成正体。斜体是正文声音；正体是特定紧场合的例外。
- 不要用更粗的边框（2px+）。1.5px 结构边框重量是系统的承诺。
- 不要用中等圆角（4px、8px、12px）。系统用 999px（胶囊）、50%（徽章）或 0（其余一切）。
- 不要把版次徽章配非 Fraunces 标签，或完全跳过标签。徽章加标签单元是系统的版次标记。
- 不要用 8 个小元素挤满一页。宁可少而大的组，带呼吸空间。

## 响应行为

系统**全程使用 `clamp()` 单位**——每一个尺寸、内边距、间隙和线条都根据视口宽高在最小值和最大值之间流体缩放。同一构图在 1280×720 笔记本、1920×1080 显示器和 2560×1440 显示上无需媒体查询即可正确渲染。

### 缩放行为
- Bricolage 展示字号在最小值（例如 60px）、基于 vw/vh 的中间值和最大值（例如 140px）之间 clamp。内部的 `min()` 函数组合基于宽度和基于高度的上限，让标题在矮视口上从不溢出。
- Fraunces 正文字号遵循同一模式，但范围更小。
- 内边距和间隙随 vw/vh 线性缩放。
- 1.5px 结构边框和 1px @ 32% 内部分隔是固定像素、不缩放，这意味着更大视口上边框会显得比例更细。这是设计如此。

### 演示行为
- 幻灯片通过键盘导航前进（由 deck JavaScript 处理）。
- 同一时间只有一个 `.slide.active` 可见；非活动页是 `opacity: 0; pointer-events: none`。
- 页间转场是 280ms 不透明度淡入淡出。
- 左下角的导航提示（"← → to navigate"）告诉观看者如何前进。

### 打印 / 导出
系统没有 `@media print` 规则。打印导出只会渲染活动页；多页打印需要逐页渲染或专用打印样式表。

## 中日韩与国际内容

### 推荐中文搭配

| 角色 | 中文字体 | 字重 | 原因 |
|---|---|---|---|
| Display / cover / headline（Bricolage 角色，96–180px） | 思源宋体 Noto Serif SC | 700 | 明朝体重字重承担 Bricolage 800 在拉丁文里提供的印刷节目单体量 |
| 卡片标题 / 菜品名 / 信息值（28–44px） | 思源宋体 Noto Serif SC | 700 | 较小尺寸用同一明朝体声音，保持一致 |
| Hero 版次数字（480px 斜体 Fraunces） | 思源宋体 Noto Serif SC | 400 | 用中文序数字符（一二三 / 春夏秋）做 hero 锚，代替西文数字 |
| 正文 / 导语 / 标语（Fraunces 斜体角色） | 思源宋体 Noto Serif SC | 400 | 明朝体正文声音——没有斜体也有暖意，因为中文没有斜体 |
| 胶囊文字 / 元标签 / 页码 | 思源宋体 Noto Serif SC | 400 | 所有铬件保持明朝体 400；系统的单墨纪律贯穿始终 |
| 信息键 / 带字距版次标签（全大写字距角色） | 思源宋体 Noto Serif SC | 400，0.16em 字距 | 保持带字距铬件的手感 |

### 中西混排策略

用 **策略 A** —— 所有角色整套换成 Noto Serif SC，替换 Bricolage Grotesque（展示）和 Fraunces（正文）。Long Table 是极简单墨数据 / 节目单系统，排印性格更多由**单墨锈陶土**、**描边形状词汇**和**纸纹叠加**承担，而不是由特定拉丁字体承担。中文全明朝体能干净地保住印刷节目单气质，而不会引入策略 C 在排印如此密的系统上会造成的逐字形基线晃动。栈：

```css
/* Bricolage roles (display, headline, card-title, course-name, info-value) */
font-family: 'Bricolage Grotesque', 'Noto Serif SC', sans-serif;
/* Fraunces roles (body, lede, tagline, pill, pagenum, edition-label) */
font-family: 'Fraunces', 'Noto Serif SC', Georgia, serif;
```

当 deck 内容是纯中文时，把两套字体栈都覆盖成以 Noto Serif SC 打头。Bricolage 角色用字重 700（匹配明朝体里 800 的体量），Fraunces 角色用字重 400。

### 加载

加到现有的 Google Fonts `<link>`：

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;500;700&display=swap" rel="stylesheet">
```

### 通用中日韩调整

这些调整适用于本系统里的**每一个中日韩块**，不论尺寸或角色：

- **把行高放宽 0.05–0.08。** 中日韩字形是全宽方块，视觉重量比拉丁字母大；为拉丁调的行高（展示 0.86–0.95，正文 1.45–1.5）在中文里会读成挤。展示提到 1.0–1.1，正文提到 1.55–1.65。
- **去掉中文标题上的负字距。** Bricolage 展示用 -0.005em 到 -0.012em 字距，会把汉字挤在一起。中文段设 `letter-spacing: 0`——若标题看起来仍挤，可用极小的正值 `0.02em`。
- **从不要对中日韩文本使用 `text-transform: uppercase`。** 中文没有大小写；这条 CSS 对汉字什么也不做，却会悄悄弄坏混排行里本该大写的 Bricolage 部分。（这里很要紧——源里每一个 Bricolage 展示元素都是 `text-transform: uppercase`。）
- **中文句子里用中文全角标点**（`，。：；！？「」『』（）`），不要用拉丁等价物（`,.:;!?""''()`）。同一句里混用两套标点系统，读起来像排版错误。
- **中文标题末尾不要句号（。）。** 中文标题遵循与拉丁相同的规则——标题式行去掉句末标点。正文段落保留 。
- **在中日韩与拉丁段的交界处应用盘古之白。** 汉字与相邻的拉丁词或数字之间要有空格（或 0.25em 边距），例如 `2026 年 5 月` 而不是 `2026年5月`。可以手打空格，或用 `pangu.js` 一类的自动加空。
- **一句只用一套字体。** 不要在同一句里在 Noto Serif SC 字重 400 和 700 之间切换——按角色选字重（标题 = 700，正文 = 400），整段坚持用它。

### 本系统的审美说明

Long Table 的整体声音是「晚餐会海报 / Risograph zine / 小出版社晚宴节目单」——奶油上的单墨锈陶土、描边形状、纸纹叠加。在中文里，系统身份不依赖特定拉丁字体（Bricolage 和 Fraunces）；它依赖**单墨承诺**、**1.5px 描边形状词汇**、**4px 径向点纸纹**，以及**丰富但经过策展的密度**。全换成 Noto Serif SC 能干净地保住每一个身份标记。

默认斜体正文规则无法翻译到中文（中文没有斜体概念；倾斜的汉字读成坏掉，不像正文声音）。在中文里，每一个 Fraunces-斜体角色都变成**Noto Serif SC 字重 400 直立**——暖意来自明朝体性格本身，而不是倾斜。对本系统这是正确的取舍。

Hero 斜体 Fraunces 超大数字（最大 480px）是拉丁文里系统的签名锚——单个斜体数字充当排印中心。在中文里，**用中文序数或季节字符代替西文数字**： 「三」、「五」、「春」、「秋」，用 Noto Serif SC 字重 400 渲染。480px 时汉字更密的视觉重量比西文数字更能平衡封面页；奶油纸背景和暖锈墨把印刷节目单手感原样带过去。

系统的描边形状词汇（胶囊、版次徽章、矩形标签、描边卡片）在中文里同样工作——无需调整。与圆形徽章成对的 "EDITION N." 标签变成圆内的「第三期」或「第 03 期」，下方元标签用 Noto Serif SC 400。32% 不透明度实线 / 虚线内部分隔节奏纯属结构，不受语言影响。

### 已知中日韩缺口

Fraunces 默认斜体正文声音是 Long Table 在拉丁文里最鲜明的排印动作之一——斜体明朝体风格的衬线正文，给系统抒情、手写的暖意。中文没有等价物：Google Fonts CDN 上没有常用的「斜体明朝体」，倾斜汉字无论怎样都读成坏掉。中文渲染失去默认斜体性格——每一行正文都变成直立 Noto Serif SC 字重 400。这是真实的性格损失，部分由 Noto Serif SC 在正文字号上自身的暖意补偿，但中文内容的 Long Table deck 会可测量地更「中性杂志」，而不是「晚餐会海报」。对这点要紧的 deck，更用力地靠**单墨颜色**和**纸纹叠加**来承担斜体正文在拉丁文里会承担的暖意。

## 迭代指南

1. 幻灯片上任何新标记都用 `{colors.ink}` —— 主标记全不透明度，弱化元信息 78%，内部分隔 32%。没有第二色。
2. 任何新标题都是 Bricolage Grotesque 字重 800 全大写、负字距。从标题阶梯里选字号（最大 96 / 100 / 120 / 140 / 160 / 180px）——不要发明新字号。
3. 任何新正文段落都是 Fraunces 斜体、字重 400。正体只用于信息键（带字距全大写）和卡片正文说明。
4. 任何新版次 / 序数标记都用 `{components.ed-badge}`（圆形描边）配斜体 "EDITION N." Fraunces 标签。
5. 任何新动作按钮都是 `{components.pill}`（圆角 999px）；任何新元信息标签都是 `{components.rect-tag}`（尖角）。不要把两者混为一谈。
6. 任何新卡片都是 `{components.card-outlined}` 模式：1.5px 墨边框，内容上方 1px @ 32% 实线分隔，内容下方 1px @ 32% 虚线分隔。
7. 任何新账本 / 日程 / 日历行都用多列网格 + 1px @ 32% 实心底边框模式（`{components.ledger-row}`）。
8. 任何新章节开场都用顶栏模式：Bricolage 标题 + 右侧小斜体 Fraunces 标签 + 下方 1.5px 实心墨水平线。
9. 任何新封面级时刻都伸手去斜体 Fraunces 超大版次数字作为 hero 排印锚——下方配小字距 Bricolage 标签和一条斜体 Fraunces 元信息行。
10. 每一页都带页码标记。若跳过它，这一页会显得没锚。

## 已知缺口

- 两套 Google Fonts（Bricolage Grotesque，`opsz` 12..96；Fraunces，`opsz` 9..144）通过 `<link>` 加载。离线渲染会回退到系统无衬线（Bricolage）和 Georgia（Fraunces）——会失去光学字号轴和两套字体的性格。离线 / 印刷可靠性建议自托管。
- `opsz` 光学字号轴对大展示尺寸（480px 超大数字）和小元信息尺寸（14px 页码）的品质至关重要。没有 `opsz` 的回退字体在两端会明显显得平。
- 系统设计为单墨。若一套 deck 需要第二种强调色（「标注」或「警告」色相），系统无法容纳而不打破印刷节目单气质。只用 Bricolage 尺度 + 不透明度 + 斜体/正体切换作为强调机制。
- 纸纹叠加用 `background-image` 径向渐变，某些浏览器在高缩放时可能出现微妙压缩伪影。纹理对系统身份至关重要；不要把它当作「性能优化」去掉。
- 正文段落默认斜体。对正文字号斜体难读的 deck 内容（长技术段落、代码样例），系统没有干净的回退——斜体就是正文声音。把段落保持短而抒情。
- CSS 有几处空规则块（`.body-it { ... }`、`.s-cover .stats .num { font-weight: 600; }` 等），原先注释掉的斜体 / 字重属性已被剥掉。许多地方的预期处理是「斜体 Fraunces 字重 400」——默认样式——但空块让这一点变成隐含而不是显式。注释暗示斜体的地方，把斜体当作默认。
- 系统加载 Bricolage 字重 400 和 600，以及 Fraunces 字重 500——已发布 CSS 里没有主动使用。用它们会引入中间字重，打破每套字体的单字重承诺。
- 回退的 `.body-it` 和 `.body-ro` 工具类已定义，但 markup 里很少用这些显式类名。大多数幻灯片按元素设排印，而不是通过工具类——写新幻灯片时复制按元素的样式，不要复制工具类。
- 480px 的 hero 斜体 Fraunces 超大数字是字面数字字符——没有针对特定字符的字形替换或字距修正。"0" 和 "8" 字形在极端尺寸上可能需要光学调整；在目标视口上检查渲染。
- 系统没有 `@media print` 规则。打印导出不会分页；把 Long Table 当作屏幕优先。
