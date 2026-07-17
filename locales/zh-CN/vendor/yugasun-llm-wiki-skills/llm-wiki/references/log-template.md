# 日志模板

`log.md` 追加写入，不改写历史条目。日期用当天。

## 格式

```markdown
## [YYYY-MM-DD] <action> | <主题或主页面标题>

- 可选细节行
- Updated: <级联更新的页面标题>
```

## 操作类型取值

| 操作 | 何时使用 |
|--------|----------|
| `init` | 初始化 wiki |
| `ingest` | 摄取来源并编译 |
| `query` | 归档问答（纯对话回答不写 log） |
| `lint` | 健康检查 |
| `archive` | 页面移入 `_archive/` |
| `schema` | 修改 `SCHEMA.md` / 标签分类 |

## 示例

```markdown
## [2026-07-09] ingest | AGI 之路工程知识地图
- 新建: synthesis/agi-roadmap-engineering-knowledge-map.md
- Updated: personal-knowledge-and-skills
- Updated: domain-skills-and-agent-skills

## [2026-07-09] query | 归档: wiki 覆盖范围与开放问题

## [2026-07-09] lint | 发现 5 项，自动修复 2 项
- 自动修复: 补全 index 缺失条目 2
- 报告: 孤儿页 1；争议主张 2
```

约超过 500 条时，轮转为 `log-YYYY.md`，并在新 `log.md` 顶部注明上一卷路径。
