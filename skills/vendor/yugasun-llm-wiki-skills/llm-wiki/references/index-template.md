# Knowledge Base Index

## {topic-name}

{该主题一行描述。}

| Article | Summary | Updated |
|---------|---------|---------|
| [{Article Title}]({topic-name}/{article}.md) | {一句话摘要} | {YYYY-MM-DD} |
| [{Archived Article}]({topic-name}/{archived}.md) | [Archived] {一句话摘要} | {YYYY-MM-DD} |

## {another-topic}

{该主题一行描述。}

| Article | Summary | Updated |
|---------|---------|---------|
| [{Article Title}]({another-topic}/{article}.md) | {一句话摘要} | {YYYY-MM-DD} |

---

## PersonalWiki 变体（wikilink 列表）

本仓库现有索引使用分组列表亦可：

```markdown
# Wiki 索引

## 综合

- [[page-slug]]：一句话摘要。
- [[archived-query]]：[归档] 一句话摘要。

## 实体

- [[entity-slug]]：一句话摘要。

## 概念

- [[concept-slug]]：一句话摘要。
```

## Lint 约定

- 文件存在但不在索引 → 补条目，摘要可用 `(no summary)` / `(无摘要)`
- 索引指向不存在文件 → 标 `[MISSING]` / `[缺失]`，不擅自删除
- 归档页摘要保留 `[Archived]` / `[归档]` 前缀
- Updated 反映知识内容实质变更日，不是文件系统 mtime
