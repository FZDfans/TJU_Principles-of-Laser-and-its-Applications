---
type: tooling
status: active
created: 2026-06-07
updated: 2026-06-07
source_count: 4
confidence: high
tags: [laser, skill, index]
---
# laser-mechanism 全局索引摘要

## 说明

用户提醒：全局 `$laser-mechanism` skill 已带有内容索引。本页把已用到的全局索引沉淀到 vault，方便后续 ingest 时不用重复查找。

## 全局索引文件

- `C:/Users/Administrator/.codex/skills/LASER_mechanism/references/source_map.md`
- `C:/Users/Administrator/.codex/skills/LASER_mechanism/references/chapter_index.md`
- `C:/Users/Administrator/.codex/skills/LASER_mechanism/references/topic_index.md`
- `C:/Users/Administrator/.codex/skills/LASER_mechanism/references/kb_maintenance.md`

## 教材页码映射

全局索引指出：教材正文中 PDF p10 对应印刷页 p1，因此常规章节页码可用：

```text
PDF page = printed page + 9
```

## 当前课程高优先级

| 章节 | 标题 | 教材 PDF 页码 | 状态 |
|---|---|---:|---|
| 第 1 章 | 辐射理论概要与激光产生的条件 | p10-p37 | 高优先级 |
| 第 2 章 | 激光器的工作原理 | p38-p57 | 高优先级 |
| 第 3 章 | 激光器的输出特性 | p58-p100 | 高优先级 |
| 第 4 章 | 激光的基本技术 | 不作为当前课程重点 | 低优先级 |
| 第 5 章 | 典型激光器介绍 | p101-p125 | 高优先级 |

## 第 1 章定位

| 主题 | 教材 PDF 页码 |
|---|---:|
| 光的波粒二象性 | p10-p17 |
| 玻尔兹曼分布 | p17 |
| 自发辐射 / 受激辐射 / 受激吸收 | p18-p23 |
| 爱因斯坦系数关系 | p22 |
| 光谱线、线型、线宽 | p23-p32 |
| 自然、碰撞、多普勒增宽 | p26-p30 |
| 激光形成条件、光放大、阈值条件 | p33-p36 |
| 思考练习题 1 | p37 |

## 本次 ingest 使用方式

本次优先读取了：

- `raw/激光原理与技术 前两章 重点(1).pdf`，PDF p3-p24：第 1 章讲义重点。
- `raw/激光原理及应用(第四版) ... .pdf`，PDF p17-p23、p33-p36：教材核对。

## 维护提醒

全局 skill 的 `source_map.md` 里仍记录旧根目录 PDF 路径；本 vault 已把 PDF 归档到 `raw/`。本 vault 内引用以 `raw/...pdf` 为准。
