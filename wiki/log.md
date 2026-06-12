---
type: log
status: active
created: 2026-06-07
updated: 2026-06-07
tags: [kb, log]
---
# 知识库日志

## [2026-06-07] setup | Karpathy LLM Wiki scaffold
- 根据 Karpathy LLM Wiki 模式建立 `raw/`、`wiki/`、`AGENTS.md` 三层结构。
- 建立索引、日志、来源页、概念页、课程地图、lint 页和维护工作流。
- 将根目录现有 PDF/Markdown 登记到 `manifests/raw_sources.csv`，暂未移动原文件。
- 已记录用户给定知乎链接与可访问的公开资料链接。


## [2026-06-07] archive | PDF raw layer
- 已将根目录 7 个 PDF 移动到 `raw/`。
- 已重建 `manifests/raw_sources.csv`。
- 已更新 [[wiki/sources/陈家璧-激光原理及应用-第四版.md]]、[[wiki/sources/课程讲义与重点资料.md]]、[[wiki/sources/课后习题答案汇总.md]] 中的 PDF 路径。
- 未移动 `课后作业-答案汇总.md`，它仍作为根目录 raw Markdown 来源登记。


## [2026-06-07] ingest | 前两章重点 PDF 第 1 章

- 使用 `$laser-mechanism` 全局索引：`source_map.md`、`chapter_index.md`、`topic_index.md`、`kb_maintenance.md`。
- 读取 `raw/激光原理与技术 前两章 重点(1).pdf` PDF p3-p24，并用教材 PDF p17-p23、p33-p36 交叉核对。
- 新增/完善：[[wiki/concepts/自发辐射.md]]、[[wiki/concepts/受激辐射.md]]、[[wiki/concepts/受激吸收.md]]、[[wiki/concepts/爱因斯坦系数关系.md]]、[[wiki/concepts/玻尔兹曼分布.md]]、[[wiki/concepts/粒子数反转.md]]、[[wiki/concepts/激光形成条件.md]]、[[wiki/concepts/光学谐振腔.md]]、[[wiki/concepts/光谱线增宽.md]]。
- 新增综合页：[[wiki/syntheses/第1章核心概念总览.md]]。
- 新增全局索引摘要：[[wiki/tooling/laser-mechanism全局索引摘要.md]]。
- 更新来源页：[[wiki/sources/课程讲义与重点资料.md]]、[[wiki/sources/陈家璧-激光原理及应用-第四版.md]]。
## [2026-06-07] tooling | 记录 AI 输出格式偏好
- 新增 [[wiki/tooling/ai-output-style.md|AI 回答格式偏好]]，按 Karpathy 知识库 tooling 页格式记录 Fridrich 的“紧凑知识库格式”偏好。
- 更新 [[wiki/tooling/维护工作流.md]]：回答问题前先遵守输出格式偏好。
- 更新 [[wiki/index.md]]：加入维护页入口。



## [2026-06-07] ingest | 第 2、3 章核心概念

- 使用 `$laser-mechanism` 全局索引定位教材第 2 章 PDF p38-p57、第 3 章 PDF p58-p100。
- 读取 `raw/激光原理与技术 前两章 重点(1).pdf` PDF p25-p54 作为第 2 章讲义重点。
- 读取教材第 2 章全文和第 3 章关键页，更新第 2、3 章核心概念页。
- 新增综合页：[[wiki/syntheses/第2章核心概念总览.md]]、[[wiki/syntheses/第3章核心概念总览.md]]。
- 更新来源页：[[wiki/sources/课程讲义与重点资料.md]]、[[wiki/sources/陈家璧-激光原理及应用-第四版.md]]。


## [2026-06-07] correction | 补入课程总结重点 PDF

- 用户指出 `raw/激光原理与技术-课程总结 重点.pdf` 也是老师划重点 PDF，前次 ingest 未参考。
- 已抽取该 PDF 34 页概要，并将其设为教师重点/高优先级来源。
- 已回填第 3 章相关页：[[wiki/concepts/自再现模.md]]、[[wiki/concepts/激光模式.md]]、[[wiki/concepts/高斯光束.md]]、[[wiki/concepts/激光输出功率.md]]、[[wiki/concepts/线宽极限.md]]、[[wiki/concepts/光束质量因子M2.md]]、[[wiki/syntheses/第3章核心概念总览.md]]。
- 已在 [[wiki/questions/待研究问题.md]] 登记需视觉核对的公式页。
## [2026-06-07] maintenance | formula rendering protocol

- Updated: [[AGENTS.md]]。
- Change: 增加“输出与公式呈现规范”，明确 Obsidian 中公式只用行内 `$...$` 与块级 `$$...$$`，禁止 `\(...\)` / `\[...\]`；同时写入紧凑知识库格式、正文不用代码块等要求。
- Reason: 用户明确反馈公式呈现方法需固化到 agent 协议，避免后续回答重复犯错。

## [2026-06-07] synthesis | 1.5 激光形成的条件章节梳理
- 新增 [[wiki/syntheses/1.5 激光形成的条件.md]]：按教材 PDF p33-p36 梳理 1.5.1 介质中光的受激辐射放大、吸收/增益系数、粒子数反转条件，以及 1.5.2 光学谐振腔、阈值条件物理意义和考试抓手。
- 更新 [[wiki/index.md]]：加入第 1.5 节章节梳理入口。

## [2026-06-08] ingest | 第 3、5 章完整章节入口

- 第 3 章：在既有核心概念基础上补建 [[wiki/concepts/共焦腔场分布.md]]、[[wiki/concepts/稳定球面腔等价共焦腔.md]]、[[wiki/concepts/厄密高斯与拉盖尔高斯光束.md]]，并更新 [[wiki/syntheses/第3章核心概念总览.md]] 的完整章节结构。
- 第 5 章：抽取教材 PDF p101-p125，并结合 `raw/激光原理与技术-课程总结 重点.pdf` PDF p12-p17，新增 [[wiki/syntheses/第5章核心概念总览.md]]。
- 新增第 5 章概念页：[[wiki/concepts/固体激光器.md]]、[[wiki/concepts/气体激光器.md]]、[[wiki/concepts/染料激光器.md]]、[[wiki/concepts/半导体激光器.md]]、[[wiki/concepts/准分子自由电子与化学激光器.md]]。
- 更新 [[wiki/sources/陈家璧-激光原理及应用-第四版.md]]、[[wiki/sources/课程讲义与重点资料.md]]、[[wiki/maps/激光原理课程地图.md]]、[[wiki/index.md]] 和 [[wiki/questions/待研究问题.md]]。
## [2026-06-09] correction | 题 5 自发辐射功率

- 更新 [[课后作业-答案汇总.md]] 题 5 第二问：按教材自发辐射原式 $dN_2/dt=-A_{21}N_2$ 展开，明确 $P_\text{sp}=A_{21}N_2h\nu=E_{\max}/\tau\approx230\,\mathrm{W}$。
- 记录易错点：本题求瞬时自发辐射功率，不是一个寿命内平均释放功率，不能乘 $1-1/e$。

## [2026-06-09] ingest | 第 6、9、10 章应用讲义

- 读取 `raw/激光原理与技术-第6章.pdf`、`raw/激光原理与技术-第9章.pdf`、`raw/激光原理与技术-第10章-V2.pdf`，并对照 `raw/激光原理与技术-课程总结 重点.pdf` PDF p18-p29、p34 的教师总结重点。
- 新增综合页：[[wiki/syntheses/第6章核心概念总览.md]]、[[wiki/syntheses/第9章核心概念总览.md]]、[[wiki/syntheses/第10章核心概念总览.md]]。
- 新增第 6 章概念页：[[wiki/concepts/激光干涉测长.md]]、[[wiki/concepts/激光衍射测量.md]]、[[wiki/concepts/激光测距.md]]、[[wiki/concepts/激光准直与多自由度测量.md]]、[[wiki/concepts/激光多普勒测速.md]]、[[wiki/concepts/Sagnac效应与光纤陀螺.md]]。
- 新增第 9 章概念页：[[wiki/concepts/光纤通信中的激光器与光放大器.md]]、[[wiki/concepts/激光全息三维显示.md]]、[[wiki/concepts/激光存储技术.md]]、[[wiki/concepts/激光扫描与激光打印机.md]]。
- 新增第 10 章概念页：[[wiki/concepts/激光核聚变.md]]、[[wiki/concepts/激光冷却与光捕获.md]]、[[wiki/concepts/激光化学.md]]、[[wiki/concepts/激光光谱技术.md]]。
- 更新 [[wiki/sources/课程讲义与重点资料.md]]、[[wiki/maps/激光原理课程地图.md]]、[[wiki/syntheses/激光原理复习总览.md]]、[[wiki/index.md]] 和 [[wiki/questions/待研究问题.md]]。

- 2026-06-10：根据两张课后作业截图，更新 [[课后作业-答案汇总.md]]，新增“增益介质与阈值补充作业”，整理稳定图、三/四能级系统、均匀/非均匀增宽、烧孔效应、阈值反转密度，以及红宝石和 He-Ne 增益计算题答案。
