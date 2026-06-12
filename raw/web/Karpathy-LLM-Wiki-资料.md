---
type: source
status: active
created: 2026-06-07
updated: 2026-06-07
confidence: medium
tags: [karpathy, llm-wiki, source]
---
# Karpathy LLM Wiki 资料

## 用户给定来源
- 知乎专栏：https://zhuanlan.zhihu.com/p/2034019211660542173
  - 访问状态：本地请求返回 403，未能直接抓取全文；后续可由用户用 Obsidian Web Clipper 或浏览器复制正文到本页。

## 已核对网页资料
- Andrej Karpathy 的 gist：<https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f>
- Karpathy Wiki 说明站：<https://karpathy-wiki.lol/en>
- Aikompassen 对 LLM Wiki 的报道：<https://aikompassen.com/artiklar/llm-wiki-karpathy-ai-agentminne/>
- FutureWeb 中文/繁中解析：<https://futureweb.pro/tools/ai-application/karpathy-llm-ai-workflow/>

## 提炼出的本 vault 实施原则
- 三层：`raw/` 原始资料、`wiki/` 可维护知识层、`AGENTS.md` schema。
- 三个循环：ingest（导入）、query（查询并沉淀）、lint（健康检查）。
- Obsidian 是阅读和图谱界面；LLM 负责整理、交叉引用、维护一致性。
- 与传统 RAG 的差异：不是每次提问都重新拼接碎片，而是把高价值综合写入持久 wiki。
