# 摄取适配约定（Source Adapters）

按输入通道把材料写入 `raw/`，再编译进知识页。Agent 负责理解与综合；本文件规定 **raw 落点、必填字段、清洗规则、编译目标**。

通用 raw frontmatter 见 [raw-template.md](raw-template.md)。`source_type` 取值与 SCHEMA 对齐。

---

## 1. 博客 / 文章 / PDF（优先级最高）

### 博客 / 网页文章（`blog` / `article`）

| 项 | 约定 |
|----|------|
| 落点 | `raw/articles/YYYY-MM-DD-slug.md` |
| 抓取 | URL → 正文 Markdown；系列文先建 inventory note，再逐篇摄取 |
| 必填 | `source_url`、`ingested`、`source_type: blog`（或 `article`） |
| 编译 | 新概念 → `concepts/` 或并入既有 synthesis；系列 → 一张 synthesis 地图 + 必要时 entity |
| 样例 | `raw/articles/yugasun-agi-roadmap-*.md` → `synthesis/agi-roadmap-engineering-knowledge-map.md` |

### PDF（`pdf`）

| 项 | 约定 |
|----|------|
| 落点 | 文本：`raw/notes/YYYY-MM-DD-slug.md`；二进制：`raw/assets/<同名>.pdf` |
| 抓取 | 提取可读文本；保留页码/章节标题；不改写观点 |
| 必填 | `source_type: pdf`；正文注明资产相对路径 |
| 编译 | 并入相关 synthesis / entity；决策点可进 `comparisons/` |
| 样例 | `raw/notes/2026-q2-product-review-and-outlook.md` |

---

## 2. 日常随手记 / 对话导出

### Inbox 随手记（`inbox`）

| 项 | 约定 |
|----|------|
| 落点 | `raw/inbox/YYYY-MM-DD-slug.md` |
| 流程 | 暂存 →「加入 wiki」编译 → 移入正式子目录或删除 inbox 副本 |
| 必填 | `source_type: inbox` |
| 编译 | 优先合并既有页；达阈值再新建 |
| 样例 | 用 `scripts/new-raw.sh <wiki> inbox "标题"` 生成 |

### 对话导出（`chat-export`）

| 项 | 约定 |
|----|------|
| 落点 | `raw/transcripts/YYYY-MM-DD-slug.md` |
| 清洗 | 去掉 runtime / system / developer 指令、子 agent JSON、IDE 上下文转储；保留用户意图与可追溯路径 |
| 追溯 | inventory 中保留原始文件路径与 SHA-256；不必整库复制 assistant 全文 |
| 必填 | `source_type: chat-export` |
| 编译 | 主题进 synthesis/entity；覆盖缺口进 `queries/` |
| 样例 | `raw/transcripts/codex-user-prompts-2026-03-19-to-2026-07-09.md` |

---

## 3. Git / 项目仓库（`git`）

| 项 | 约定 |
|----|------|
| 落点 | `raw/git/YYYY-MM-DD-<repo>-summary.md`（或 `raw/notes/`） |
| 内容 | README 要点、CHANGELOG/近期 tag、代表性 commit 摘要、开放 issue 主题；**不**整库 dump |
| 必填 | `source_type: git`；注明仓库 URL 或本地路径 |
| 编译 | 每个活跃项目一张 `entities/<project>.md`；交付事实校正工作地图 |
| 样例 | `raw/git/` 下项目摘要 → 对应 entity |

---

## 4. 飞书 / 邮件 / 会议（`lark` / `mail` / `meeting`）

| 项 | 约定 |
|----|------|
| 落点 | `raw/lark/`、`raw/mail/`、`raw/meeting/`（或统一 `raw/notes/`） |
| 内容 | **默认摘要化**：结论、待办、决策、参与方；敏感原文不进 wiki，只留 doc token / 消息链指针 |
| 工具 | 优先既有飞书 / 邮件 skills 拉取后再写入 raw |
| 必填 | 对应 `source_type`；`source_url` 可为飞书链接或 `message_id` 说明 |
| 编译 | 决策进 synthesis 或 comparisons；待办不单独建页除非反复出现 |
| 样例 | 各通道一条 adapter 样例 raw（摘要占位，可被真实导入替换） |

---

## 编译后检查清单

1. 知识页 `sources` 指向 raw 路径
2. 更新 `index.md` 触达条目
3. 追加 `log.md`：`## [YYYY-MM-DD] ingest | ...`
4. 扫描同主题级联（勿盲改 10+ 页）
5. 新通道首次导入前更新覆盖范围 / 开放问题页
