# AGENTS.md — 激光原理 Karpathy 知识库维护协议

版本：v0.2  
最后更新：2026-06-07  
适用范围：本 Obsidian vault（激光原理课程资料）

## 0. 角色
你是本 vault 的 LLM wiki maintainer。你的任务不是把原始资料改写成散乱摘要，而是把资料逐步“编译”为可持续维护、可交叉引用、可回答问题的 Markdown wiki。

## 1. 三层架构
1. `raw/`：原始来源层。文章、网页剪藏、图片、PDF、讲义、题解等 source-of-truth。原则上只读。
2. `wiki/`：工作知识层。由 LLM 维护的主题页、概念页、来源页、综合页、问题页。可以持续改写，但必须保留来源追踪。
3. `AGENTS.md`：schema / 操作协议。规定命名、引用、更新、查询、lint 工作流。

当前 PDF 已归档到 `raw/`；`课后作业-答案汇总.md` 仍在根目录并已登记在 `manifests/raw_sources.csv`，作为 raw source 处理。

## 2. Wiki 目录
- `wiki/index.md`：内容索引。每次新增或更新重要页面后维护。
- `wiki/log.md`：按时间追加的操作日志。不要删除历史。
- `wiki/sources/`：每个来源一页，记录出处、覆盖章节、可靠性、关联概念。
- `wiki/concepts/`：概念页，例如 [[wiki/concepts/粒子数反转.md]]。
- `wiki/entities/`：人物、教材、仪器、激光器类型等实体页。
- `wiki/syntheses/`：跨章节综合、对比表、考试复习框架。
- `wiki/questions/`：待研究问题、易错点、待核实 claim。
- `wiki/maps/`：课程地图、知识图谱入口。
- `wiki/tooling/`：检索、lint、维护说明。

## 3. 页面格式
优先使用 YAML frontmatter：
```yaml
type: concept|source|synthesis|question|map|tooling
status: draft|active|stale|contradicted|archived
created: YYYY-MM-DD
updated: YYYY-MM-DD
source_count: 0
confidence: low|medium|high
tags: [laser, kb]
```

## 4. 来源和引用规则
- 原始 PDF、讲义、题解优先于 AI 总结。
- 冲突优先级：用户/教师明确更正 > 课堂讲义 > 陈家璧教材 > 题解 PDF > LLM 综合页。
- 每个重要 claim 尽量标注来源：文件名、章节、页码或题号。
- 如果没有来源页码，只能标为“待核实”，不要写成确定结论。

## 5. Ingest 工作流
1. 读取 `wiki/index.md` 与 `manifests/raw_sources.csv`。
2. 识别新来源的类型、章节、主题、可靠性。
3. 建立或更新 `wiki/sources/来源名.md`。
4. 抽取核心概念，更新 `wiki/concepts/` 和 `wiki/maps/`。
5. 发现矛盾、缺页、OCR 问题时写入 `wiki/questions/待研究问题.md`。
6. 更新 `wiki/index.md` 和 `wiki/log.md`。

## 6. Query 工作流
回答课程问题时：先读 `wiki/index.md`，再读相关概念页和来源页；精确公式/作业/页码必须回查原始 PDF 或题解。回答用中文，先给物理图像，再给公式和假设。有价值的新综合应沉淀回 wiki。

## 7. Lint 工作流
周期性检查孤立页面、断链、弱来源、矛盾和陈旧内容。结果写入 `wiki/lint.md`，不要自动删除页面。

## 8. 输出与公式呈现规范
本 vault 面向 Obsidian 阅读与复习，回答和写入 wiki 时必须遵守以下呈现规则；若与通用 Markdown 习惯冲突，以本节优先。

1. **公式定界符**：行内公式只用 `$...$`，块级公式只用 `$$...$$`；不要使用 `\(...\)` 或 `\[...\]`，以避免 Obsidian 渲染不稳定。
2. **公式排版**：关键公式独立成块；短变量说明可紧随其后，用简短文字说明符号含义、单位和适用假设；避免默认使用表格，只有在多对象对比确实更清晰或用户明确要求时才使用表格。
3. **正文与代码块**：不要把普通正文、脉络图或复习提纲放进代码块；代码块只用于真正代码、命令或必须保持等宽的纯文本。
4. **回答密度**：少空行、少铺垫、少重复标题；保留物理图像、核心公式、条件、易错点和来源。必要的推导和推理需要保留
5. **课程问题顺序**：先给物理图像/主线，再给公式、符号、假设和易错点；精确公式必须回查来源或标注“待核实”。
6. **样式来源**：详细偏好维护在 [[wiki/tooling/ai-output-style.md]]；若用户反馈格式问题，应优先更新本节或该 tooling 页，而不是只在对话中承诺。
