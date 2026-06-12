---
type: source-layer
status: active
created: 2026-06-07
updated: 2026-06-07
tags: [kb, raw]
---
# raw 原始来源层

此目录用于放置 Karpathy 知识库的 source-of-truth：网页剪藏、PDF、图片、讲义、题解、实验记录等。

原则：
- LLM 可以读取，但不要随意改写 raw 文件。
- 新来源放入后，在 `manifests/raw_sources.csv` 登记。
- 重要网页建议剪藏为 Markdown，图片下载到 `raw/assets/`，避免外链失效。

当前 PDF 已归档到 `raw/` 并登记在 `manifests/raw_sources.csv`。
