---
layout: default
title: "Horizon Summary: 2026-08-12 (ZH)"
date: 2026-08-12
lang: zh
---

> 从 460 条内容中筛选出 25 条重要资讯。

---

1. [阿里开源 Qwen3.8-2.4T-A95B：2.4T 参数 MoE 模型，激活 95B](#item-1) ⭐️ 9.0/10
2. [vLLM v0.27.0 发布：新增 Kimi K3 支持、升级 PyTorch 2.13 与 FlashAttention 4](#item-2) ⭐️ 8.0/10
3. [Tailscale 将数据库损坏追溯到存在 16 年的 SQLite WAL 重置缺陷](#item-3) ⭐️ 8.0/10
4. [历史车牌搜索应要求获得搜查令](#item-4) ⭐️ 8.0/10
5. [Qwen 发布 Qwen3.8-2.4T-A95B：2.4 万亿参数的开源 MoE 模型](#item-5) ⭐️ 8.0/10
6. [高尔斯探讨 LLM 擅长何种数学](#item-6) ⭐️ 8.0/10
7. [Addy Osmani 发布 agent-skills：面向 AI 编程智能体的生产级工程技能](#item-7) ⭐️ 8.0/10
8. [Anthropic 发布 Agent Skills 公共仓库，标准化 AI 代理扩展方式](#item-8) ⭐️ 8.0/10
9. [Manim：3Blue1Brown 的开源数学动画引擎](#item-9) ⭐️ 8.0/10
10. [研究者窃取专有 LLM API 的隐藏推理轨迹](#item-10) ⭐️ 8.0/10
11. [Meta 发布 Muse Glimmer：Apache 2.0 协议下的 30B 开源智能体模型](#item-11) ⭐️ 8.0/10
12. [DeepSeek V4 Pro 正式版上线 API，Agent 能力增强](#item-12) ⭐️ 8.0/10
13. [SpaceXAI 发布 Grok 4.6，对标 GPT-5.6 Sol](#item-13) ⭐️ 8.0/10
14. [Mojo 1.0 正式发布，编译器计划年内开源](#item-14) ⭐️ 8.0/10
15. [比亚迪 AI 团队首秀 HyWorldVLA，NAVSIM v1 获 90.59 分刷榜](#item-15) ⭐️ 8.0/10
16. [Claude 将黎曼猜想零点下界从 41.6% 提升至 67.2%](#item-16) ⭐️ 8.0/10
17. [DeepMind：LLM 事实性的瓶颈在于回忆而非存储](#item-17) ⭐️ 8.0/10
18. [谷歌 DeepMind 推进 AMIE，迈向专家级音视频临床咨询](#item-18) ⭐️ 8.0/10
19. [NVIDIA Nemotron 3.5 Lightning 加速长时运行智能体工作流](#item-19) ⭐️ 8.0/10
20. [NVIDIA NeMo Switchyard：跨模型路由 AI 智能体工作负载](#item-20) ⭐️ 8.0/10
21. [美团开源 LoHoSearch：用知识图谱校准搜索智能体能力](#item-21) ⭐️ 8.0/10
22. [MineExplorer 基准揭示多模态大模型能力断层](#item-22) ⭐️ 8.0/10
23. [美团正式开源 LongCat-2.0：1.6T 参数 Agentic Coding 大模型](#item-23) ⭐️ 8.0/10
24. [美团发布 LongCat-2.0：5 万国产芯片集群训练的万亿参数 MoE 模型](#item-24) ⭐️ 8.0/10
25. [以数据为中心的并行方法加速变长序列训练](#item-25) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [阿里开源 Qwen3.8-2.4T-A95B：2.4T 参数 MoE 模型，激活 95B](https://www.ithome.com/0/989/001.htm) ⭐️ 9.0/10

阿里 Qwen 团队正式开放了 Qwen3.8-2.4T-A95B 模型权重，这是一个总参数 2.4T、每个 Token 激活 95B 参数的 MoE 大模型。这是 Qwen-Max 级别模型首次开源权重，原生支持 262,144 Token 上下文，并可扩展至 1,010,000 Token。 开源 Qwen-Max 级别模型是开源大模型生态的重要里程碑，让研究者和开发者首次能获得此前仅通过云端 API 提供的顶尖规模架构与权重。这将加速社区在 MoE 训练、长上下文推理和 Agent 工作流等方向的探索。 模型的每个 MoE 层包含 512 个专家，每个 Token 路由到 10 个专家并同时激活 1 个共享专家；模型还进行了多步 MTP（多 Token 预测）训练。云端版 Qwen3.8-Max 基于该开放权重模型，并加入更多生产环境能力。

rss · IT HOME · 8月12日 16:10

**背景**: 专家混合（MoE）是一种机器学习架构，将模型拆分为多个专门化的子网络（即“专家”），并为每个输入只路由到其中部分专家，从而在保持总参数规模很大的同时降低计算成本。总参数决定存储占用和显存需求（因为所有专家都必须加载），而激活参数决定每个 Token 的计算成本。如此规模的开源模型非常少见，因此这次发布为研究社区提供了关于规模、内存与推理效率之间权衡的参考基准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2507.11181">[2507.11181] Mixture of Experts in Large Language Models</a></li>
<li><a href="https://spanvero.com/learn/active-vs-total-params/">Active vs total parameters — what it means (open AI models )...</a></li>

</ul>
</details>

**标签**: `#AI`, `#开源模型`, `#Qwen`, `#MoE`, `#大语言模型`

---

<a id="item-2"></a>
## [vLLM v0.27.0 发布：新增 Kimi K3 支持、升级 PyTorch 2.13 与 FlashAttention 4](https://github.com/vllm-project/vllm/releases/tag/v0.27.0) ⭐️ 8.0/10

vLLM v0.27.0 正式发布，包含来自 242 位贡献者的 561 次提交。该版本新增了对 Moonshot AI 的 Kimi K3 模型的全栈支持，升级到 PyTorch 2.13.0，并深化了 SM100 上的 FlashAttention 4 集成，支持 FP8 KV 缓存和 headdim-256。 这是 vLLM（广泛使用的开源 LLM 推理引擎）的一个重要版本。新增 Kimi K3 支持与 PyTorch 2.13 升级，使社区能够使用 2.8T 参数的最新开放权重模型，并提升了 DeepSeek-V4 等模型的推理性能。 Kimi K3 是一个 2.8T 参数的模型，具备原生视觉能力和 100 万 token 上下文窗口。该版本还新增了 Qwen3.5、K-EXAONE-2.0-750B、VaultGemma 等模型，将 Model Runner V2 扩展到非生成式工作负载，并启用了对 NVIDIA Rubin（sm_107）的早期支持。PyTorch 2.13 升级属于破坏性环境变更。

github · khluu · 8月10日 21:18

**背景**: vLLM 是一个开源的高吞吐量 LLM 推理与服务引擎。Kimi K3 是 Moonshot AI 最新的开放权重多模态推理模型，基于 Kimi 团队的注意力残差（AttnRes）架构与 DeepGEMM 内核。FlashAttention 4 是面向 NVIDIA Blackwell GPU 的下一代注意力算法，可提升训练与推理效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K 3 Tech Blog: Open Frontier Intelligence</a></li>
<li><a href="https://huggingface.co/moonshotai/Kimi-K3">moonshotai/ Kimi - K 3 · Hugging Face</a></li>
<li><a href="https://github.com/deepseek-ai/DeepGEMM">GitHub - deepseek-ai/ DeepGEMM : DeepGEMM : clean and efficient...</a></li>

</ul>
</details>

**标签**: `#vllm`, `#LLM inference`, `#release`, `#AI infrastructure`, `#PyTorch`

---

<a id="item-3"></a>
## [Tailscale 将数据库损坏追溯到存在 16 年的 SQLite WAL 重置缺陷](https://tailscale.com/blog/sqlite-wal-reset-bug) ⭐️ 8.0/10

Tailscale 公布了他们对间歇性数据库损坏的调查过程，最终将问题追溯到一个 SQLite WAL 重置竞态条件，SQLite 开发者估计该缺陷已存在至少 16 年。他们还资助了一个开源的 SQLite VFS shim，用于帮助隔离该缺陷。 这件事很重要，因为它展示了即使在单写入者场景下，一个隐蔽的、长期存在的竞态条件也能破坏数据库，并且展示了公司资助开源调试工具的模式。这些发现和工具能够帮助其他团队诊断类似的 WAL 模式损坏问题。 该缺陷只会在 WAL 模式下存在并发事务时发生；在损坏事件中，SQLite 报告的从 WAL 文件复制到数据库的页数超过了实际可用的页数。修复 WAL 重置缺陷后，Tailscale 与 SQLite 开发者还发现了一个过时表达式索引缺陷。

hackernews · ropbear · 8月12日 14:22 · [社区讨论](https://news.ycombinator.com/item?id=49272832)

**背景**: SQLite 是一种嵌入式数据库，常配合预写日志（WAL）模式以获得更好的并发性能。在 WAL 模式下，更改会先追加到单独的 WAL 文件中，然后再检查点（checkpoint）写入主数据库文件，WAL-index 文件用于跟踪状态。WAL 重置缺陷是 SQLite 重置和重用 WAL 文件时的一个竞态条件，可能导致写入丢失和数据库损坏。Tailscale 在其控制平面中使用 SQLite，并由一个 Go 进程独占访问该数据库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tailscale.com/blog/sqlite-wal-reset-bug">How Tailscale helped find the SQLite WAL-Reset bug</a></li>
<li><a href="https://www.youngju.dev/blog/2026-07-16-sqlite-wal-reset-bug.en">The SQLite WAL - Reset Bug: A Data Corruption Race That Hid for 15...</a></li>
<li><a href="https://sqldocs.org/sqlite-write-ahead-logging/">SQLite WAL: Write - Ahead Logging Explained - SQL Docs</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞这是一篇有趣的调试叙事，Simon Willison 特别指出公司资助特定开源工具的价值。也有人对解释的严谨性提出技术性质疑，并有一些关于措辞的较真意见。

**标签**: `#sqlite`, `#database`, `#debugging`, `#systems`, `#tailscale`

---

<a id="item-4"></a>
## [历史车牌搜索应要求获得搜查令](https://andrewpwheeler.com/2026/08/12/license-plate-reader-searches-should-require-a-warrant/) ⭐️ 8.0/10

文章主张，对车牌读取器（LPR）的历史数据进行检索应要求搜查令，而实时警报可以无须搜查令。文章提出了一种折中政策，以平衡调查需求与隐私保护。 这很重要，因为 LPR 数据形成了可搜查的行踪记录，无搜查令访问会引发严重的隐私和公民自由担忧。这场争论影响执法部门如何使用监控技术，以及法院如何解释宪法第四修正案。 文章区分了实时车牌标记与历史数据库查询，认为历史搜索更具侵犯性且不那么紧急。评论区还指出，LPR 实际上是可重新编程的通用联网摄像头，用途可能被改变。

hackernews · apwheele · 8月12日 14:43 · [社区讨论](https://news.ycombinator.com/item?id=49273165)

**背景**: 自动车牌读取器（ALPR）是能够捕捉车牌并储存带时间戳位置数据的摄像头，通常在车主不知情的情况下工作。它们可以固定安装或装在巡逻车上，记录可能被长期保存。美国宪法第四修正案禁止不合理的搜查，关键问题在于访问这些批量收集的数据是否需要搜查令。许多司法辖区尚未解决这一法律问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sls.eff.org/technologies/automated-license-plate-readers-alprs">Automated License Plate Readers</a></li>
<li><a href="https://www.flocksafety.com/blog/how-an-automatic-license-plate-recognition-system-works">How an Automatic License Plate Recognition System Works</a></li>

</ul>
</details>

**社区讨论**: 评论者大多同意，无搜查令访问历史 LPR 数据是有问题的，有人引用了警方屡次滥用这些数据的案例。也有人强调 LPR 实际上是通用摄像头；还有人认为折中提议具有说服力，但引发了数据应保留多久的问题。有评论者称这是宪法上的一个空白，可能需要通过立法或修宪来弥补。

**标签**: `#privacy`, `#surveillance`, `#law-enforcement`, `#policy`, `#technology`

---

<a id="item-5"></a>
## [Qwen 发布 Qwen3.8-2.4T-A95B：2.4 万亿参数的开源 MoE 模型](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) ⭐️ 8.0/10

Qwen 发布了 Qwen3.8-2.4T-A95B，这是一个稀疏混合专家（MoE）开源权重模型，总参数 2.4 万亿，激活参数 950 亿。该版本提供 BF16 和 FP8 检查点，定位为 Qwen3.8-Max 的开源权重版本。 此次发布将开源权重模型的规模推到新高度，同时通过 MoE 的 950 亿激活参数控制推理成本。它让研究者和部署者能够获得接近前沿水平的开源模型，并在激进量化下可能跑在消费级硬件上，从而扩大大模型能力的获取范围。 BF16 版本约 4.9TB，1-bit 量化版本据称可压缩到约 397GB，同时提供 FP8 检查点。该模型默认不支持视觉输入和 1M 上下文，这些功能仅保留给 Qwen3.8-Max；发布时也未提供 QAT 量化后的 Q4 权重。

hackernews · Philpax · 8月12日 15:01 · [社区讨论](https://news.ycombinator.com/item?id=49273478)

**背景**: 混合专家（MoE）是一种神经网络设计，门控网络会为每个输入只选择一部分专家模块，从而让模型扩展到极大的总参数规模，同时保持较低的每 Token 计算量。在 Qwen3.8-2.4T-A95B 中，推理时只有 2.4 万亿参数中的 950 亿处于激活状态，这使得它比总规模所暗示的更易于实际部署。根据 OpenRouter 的信息，它是 Qwen3.8 Max 的开源权重版本，总参数 2.4 万亿、激活参数 950 亿。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B">Qwen/ Qwen 3 . 8 - 2 . 4 T - A 95 B · Hugging Face</a></li>
<li><a href="https://openrouter.ai/qwen/qwen3.8-2.4t-a95b">Qwen 3 . 8 2 . 4 T A 95 B - API Pricing & Providers | OpenRouter</a></li>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained</a></li>

</ul>
</details>

**社区讨论**: 社区反应在兴奋与实际顾虑之间并存：有人称赞 1-bit 397GB 量化版本能让接近前沿的性能跑在可负担的硬件上；也有人指出该模型发布时缺少视觉输入、1M 上下文以及 QAT 量化的 Q4 权重，导致比 Kimi k3 更难部署。评论者还讨论了许可限制（年收入低于 5000 万美元免费）以及在消费级硬件上本地运行这类模型的可行性。另有评论提到新公布的 DeepSeek V4-Pro-0813 基准测试成绩，认为这是相关竞争信息。

**标签**: `#AI`, `#LLM`, `#Open Source`, `#MoE`, `#Hugging Face`

---

<a id="item-6"></a>
## [高尔斯探讨 LLM 擅长何种数学](https://gowers.wordpress.com/2026/08/12/what-sort-of-maths-are-llms-good-at/) ⭐️ 8.0/10

在 2026 年 8 月的博客文章中，菲尔兹奖得主蒂莫西·高尔斯讨论了 LLM 擅长哪些类型的数学，并强调测试时扩展（test-time scaling）和采样是关键因素。他还探讨了利用型科学与生成型科学工作之间的区别。 由于高尔斯是一位顶级数学家，他的观点可能会影响 AI 和数学研究者对 LLM 在数学发现中作用的看法。这也与测试时扩展的趋势相关，即在推理阶段投入更多计算能够提升推理性能。 这篇博文指出，采样才是 AI 真正擅长的，并以 AlphaCode 生成数百万候选程序为例。社区评论还指出 LLM 对寻找反例有天然偏好，以及学界存在解决著名且表述清晰问题的社会压力。

hackernews · ColinWright · 8月12日 10:04 · [社区讨论](https://news.ycombinator.com/item?id=49270022)

**背景**: 测试时扩展（TTS）是指在推理阶段分配额外计算资源以提升 LLM 性能，例如让模型生成并评估大量候选答案。温度、top-k 和 top-p 等采样技术控制生成输出的多样性。利用型科学与生成型科学的区别来自评论区讨论：利用型工作基于现有知识寻找新应用，而生成型工作则需要独特的人类感知和顿悟。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://testtimescaling.github.io/">What, How, Where, and How Well? A Survey on Test-Time Scaling in Large Language Models</a></li>
<li><a href="https://arxiv.org/abs/2503.24235">[2503.24235] A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?</a></li>
<li><a href="https://medium.com/@shashankag14/understanding-sampling-techniques-in-large-language-models-llms-dfc28b93f518">Sampling Techniques in Large Language Models (LLMs) | by Shashank Agarwal | Medium</a></li>

</ul>
</details>

**社区讨论**: 社区评论强调测试时扩展和采样是核心主题，有用户指出 AlphaCode 在 2022 年的成功。还有用户提到 AI 对搜索反例的偏好以及问题选择的社会学因素，并有人强调利用型科学与生成型科学的区别；也有评论提醒读者高尔斯是菲尔兹奖得主，另有人质疑问题的框架是否恰当。

**标签**: `#LLM`, `#Mathematics`, `#Test-time scaling`, `#AI research`, `#Machine Learning`

---

<a id="item-7"></a>
## [Addy Osmani 发布 agent-skills：面向 AI 编程智能体的生产级工程技能](https://github.com/addyosmani/agent-skills) ⭐️ 8.0/10

Addy Osmani 发布了名为 agent-skills 的 GitHub 仓库，将 24 项生产级工程技能（工作流、质量门禁和最佳实践）打包成可供 AI 编程智能体复用的资产。该仓库提供 8 个对应开发生命周期的斜杠命令，并提供 /build auto 模式，可在一次批准后自动制定计划并执行任务。 该项目有助于让 AI 编程智能体持续遵循资深工程师的工程纪律，例如先写规格再编码、测试驱动开发，而不是随意生成代码。随着 AI 辅助开发逐渐普及，它有望显著提升代码质量和项目可靠性。 这些技能可通过开源 skills CLI 安装到 70 多个智能体（如 Claude Code、Cursor、Codex、Copilot、Cline 等）：`npx skills add addyosmani/agent-skills`。技能还会根据上下文自动触发，例如设计 API 时启用 api-and-interface-design，构建界面时启用 frontend-ui-engineering；/build auto 仍会对每个任务进行测试驱动开发并单独提交，在遇到失败或风险步骤时会暂停。

rss · GitHub Trending - Daily · 8月12日 16:58

**背景**: Agent Skills 是一种轻量、开放的格式，用于通过专业知识和流程扩展 AI 智能体的能力；其核心是一个包含 SKILL.md 文件的文件夹。该仓库把资深工程师在软件开发中使用的流程、质量门禁和最佳实践封装成技能，让 AI 智能体在开发的每个阶段都能一致遵循。这也顺应了当前 AI 编程智能体生态向标准化发展的趋势，SkillsMP、agentskills.io 等平台都在推动技能的分发与复用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://agentskills.io/">A standardized way to give AI agents new capabilities and expertise.</a></li>
<li><a href="https://skillsmp.com/">Agent Skills Marketplace | Codex & Claude Skills | SkillsMP</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#developer tools`, `#coding best practices`, `#AI-assisted development`

---

<a id="item-8"></a>
## [Anthropic 发布 Agent Skills 公共仓库，标准化 AI 代理扩展方式](https://github.com/anthropics/skills) ⭐️ 8.0/10

Anthropic 发布了公共 GitHub 仓库“anthropics/skills”，其中包含适用于 Claude 的 Agent Skills 示例，以及 agentskills.io 上的 Agent Skills 规范。该仓库展示了技能如何组织为包含 SKILL.md 文件的自包含文件夹，Claude 可动态加载这些文件。 此次发布为 AI 代理封装可复用任务知识建立了一个轻量级开放标准，有助于提升 Claude Code、VS Code 等不同工具和代理平台之间的互操作性。它降低了开发者创建和共享可移植代理能力的门槛。 该仓库包含面向创意、技术、企业和文档任务的技能；支撑 Claude 文档功能的 docx、pdf、pptx 和 xlsx 技能为源码可用，但并非开源。仓库还提供了技能模板和规范，并可作为 Claude Code 插件市场注册。

rss · GitHub Trending - Daily · 8月12日 16:58

**背景**: Agent Skills 是一种轻量级开放格式，用于为 AI 代理扩展专业知识和流程；技能本质上是一个包含 SKILL.md 文件（内含指令和资源）的文件夹。这种方式让代理可以按需动态加载特定任务的上下文，而不是在每个提示中都包含这些内容。Claude Code、Claude.ai、Anthropic API 以及 VS Code 等主要工具已开始支持 Agent Skills，使这一标准在代理生态系统中具有广泛适用性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/anthropics/skills">GitHub - anthropics/ skills : Public repository for Agent Skills · GitHub</a></li>
<li><a href="https://agentskills.io/">A standardized way to give AI agents new capabilities and expertise.</a></li>
<li><a href="https://code.visualstudio.com/docs/agent-customization/agent-skills">Use Agent Skills in VS Code</a></li>

</ul>
</details>

**标签**: `#AI`, `#Agents`, `#Claude`, `#Anthropic`, `#Developer Tools`

---

<a id="item-9"></a>
## [Manim：3Blue1Brown 的开源数学动画引擎](https://github.com/3b1b/manim) ⭐️ 8.0/10

3Blue1Brown 的数学视频动画引擎 Manim 的 GitHub 仓库再次受到关注，突显了其在教育和内容创作领域的持续影响力。该项目拥有一个活跃的生态系统，包括 subreddit、Discord 服务器和文档。 Manim 使教育者、研究者和内容创作者能够以编程方式生成精确的数学动画，让复杂概念变得直观易懂。其开源特性和双版本生态（ManimGL 和社区版）确保了广泛采用和持续改进。 Manim 有两个版本：本仓库是 ManimGL（通过‘pip install manimgl’安装），以及 2020 年分叉的社区版（ManimCommunity/manim）。Manim 要求 Python 3.10 或更高版本，系统需求包括 FFmpeg 和 OpenGL，可选 LaTeX 用于文字渲染。

rss · GitHub Trending - Daily · 8月12日 16:58

**背景**: Manim 最初是 3Blue1Brown YouTube 频道创作者 Grant Sanderson 为制作数学教学视频而开发的个人项目。2020 年，一群开发者分叉了该项目，创建了更稳定、由社区驱动的版本。该工具使用基于 Python 的 API 来定义数学场景，并通过 OpenGL 渲染，从而精确控制每个视觉元素。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/3b1b/manim">GitHub - 3b1b/ manim : Animation engine for explanatory math videos</a></li>
<li><a href="https://www.manim.community/">Manim is a community-maintained Python library for creating...</a></li>
<li><a href="https://en.wikipedia.org/wiki/3Blue1Brown">3Blue1Brown</a></li>

</ul>
</details>

**标签**: `#animation`, `#mathematics`, `#education`, `#python`, `#open-source`

---

<a id="item-10"></a>
## [研究者窃取专有 LLM API 的隐藏推理轨迹](https://simonwillison.net/2026/Aug/11/stealing-reasoning-traces/#atom-everything) ⭐️ 8.0/10

一篇新论文展示，Anthropic、OpenAI 和 Google 的前沿模型返回的加密思维链（chain-of-thought）数据块，可以被重放到同系列较弱的模型中，并通过越狱攻击以明文形式恢复隐藏推理内容。厂商在收到报告后已修复该漏洞。 该攻击暴露了专有 LLM 提供商试图隐藏思维链推理过程中的一个关键缺陷，削弱了 AI 安全与隐私保障的假设。它表明隐藏推理可被提取，引发对知识产权、数据保护及 API 提供商信任的担忧。 该漏洞利用同一系列中所有模型共享相同加密密钥的特性，使数据块可以在会话、用户和模型之间重放。Claude Haiku 4.5 是最容易被攻击的目标，攻击者通过提示要求模型逐字转写推理内容并设置助手前缀；不过各厂商目前已阻止该攻击。

rss · Simon Willison · 8月11日 22:40

**背景**: 思维链（chain-of-thought, CoT）推理是指 LLM 在生成最终答案之前产生的逐步推理过程，在专有 API 中通常对用户隐藏。越狱（jailbreaking）是一种通过精心构造提示词来绕过 LLM 安全机制的攻击方法。重放攻击则是指将捕获的数据（例如加密的推理数据块）在不同上下文中重新使用，以实现未经授权的行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2201.11903">[2201.11903] Chain - of - Thought Prompting Elicits Reasoning in ...</a></li>
<li><a href="https://cybersecuritynews.com/top-ai-models-apis-flaw-exposes-hidden-reasoning/">OpenAI, Anthropic, and Google LLM APIs vulnerability Exposes...</a></li>
<li><a href="https://www.alphaxiv.org/abs/2608.09867">Stealing Reasoning Traces from Proprietary LLM APIs | alphaXiv</a></li>

</ul>
</details>

**社区讨论**: 讨论中提供了一个 curl 示例，展示返回的 encrypted_content 数据块，论文附录还展示了明显不打算供人类阅读的提取出的推理痕迹。论文还揭露了一种提示注入变体，诱使模型在推理过程中考虑数据外泄；作者指出所有供应商都已确认并修复了该问题。

**标签**: `#security`, `#LLM`, `#chain-of-thought`, `#AI safety`, `#adversarial attacks`

---

<a id="item-11"></a>
## [Meta 发布 Muse Glimmer：Apache 2.0 协议下的 30B 开源智能体模型](https://simonwillison.net/2026/Aug/10/introducing-muse-glimmer/#atom-everything) ⭐️ 8.0/10

Meta 发布了 Muse Glimmer，这是一个采用宽松 Apache 2.0 许可的 30B 开源权重模型，专为端到端智能体任务完成、可靠工具调用和多步推理而设计。Simon Willison 通过 LM Studio 和 llm-coding-agent 插件在本地测试了它，展示了它能够探索代码库并描述图像。 这件事很重要，因为 Meta 以真正宽松的许可协议发布了一款重要的开源权重模型，不同于以往限制较多的 Llama 许可，这增强了开源 AI 生态。30B 参数量使其在 32GB 或以上内存的机器上可本地部署，使强大的智能体模型对开发者和研究人员更易获得。 Muse Glimmer 还是一个能处理图像的视觉模型；Simon Willison 在 LM Studio 中运行了 18.16 GB 的量化版本，并使用了打过补丁的 llm-lmstudio 插件。Meta 声称该模型在 DeepSearch QA、MCP-Atlas、τ-Bench 和 SWE-Bench 等基准上表现出色，能够完成完整的智能体任务。

rss · Simon Willison · 8月10日 23:56

**背景**: 开源权重模型会公开训练好的参数，但使用和再分发限制由许可证决定；Apache 2.0 是一种宽松许可，允许广泛的商业和研究用途。智能体任务要求模型规划并执行多步工作流，通常通过函数调用使用外部工具。MCP-Atlas 评估模型在真实 MCP 服务器上的工具使用能力，τ-Bench 模拟工具-智能体-用户交互，DeepSearch QA 则测试深度研究智能体的表现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://llm-stats.com/benchmarks/mcp-atlas">MCP Atlas Leaderboard</a></li>
<li><a href="https://static.scale.com/uploads/674f4cc7a74e35bcaae1c29a/MCP_Atlas.pdf">MCP - Atlas : A Large-Scale Benchmark for Tool-Use Competency with...</a></li>
<li><a href="https://surrealyz.github.io/classes/llmsec-fall24/slides/21-tau-bench.pdf">τ - bench : A Benchmark for Tool-Agent-User Interaction in Real-World...</a></li>

</ul>
</details>

**标签**: `#AI`, `#open-source`, `#large language models`, `#agents`, `#Meta`

---

<a id="item-12"></a>
## [DeepSeek V4 Pro 正式版上线 API，Agent 能力增强](https://www.ithome.com/0/989/000.htm) ⭐️ 8.0/10

DeepSeek 已发布 DeepSeek V4 Pro 正式版（DeepSeek-V4-Pro-0813），现已通过 API 提供，模型名称保持不变。此次更新增强了 Agent 能力，支持 Responses API 和 Codex 接入，多项测试性能据称接近 Fable 5。 这是来自中国领先 AI 实验室的重要模型更新，提供了有竞争力的性能和极低的 API 定价。它可能通过为开发者提供一个性价比高、适合 Agent 场景的模型（相对于 OpenAI GPT 系列等）来影响大模型生态。 该模型保持相同的 API 名称，定价为缓存命中每百万 tokens 输入 0.025 元、缓存未命中 3 元，每百万 tokens 输出 6 元。V4 系列采用 Mixture-of-Experts（MoE）架构，总参数 1.6T，激活参数 49B，支持 100 万 token 上下文。

rss · IT HOME · 8月12日 16:05

**背景**: DeepSeek 是一家中国生成式 AI 公司，在 2025 年 1 月因发布 DeepSeek-R1 而受到全球关注，该模型以开放权重和能源效率著称。V4 系列是 DeepSeek 的下一代模型，此前 DeepSeek-V4-Pro 预览版已发布在 Hugging Face 上。Responses API 和 Codex 是 OpenAI 提供的用于构建 Agent 应用和编码 Agent 的工具，DeepSeek 现在支持这些接口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro">deepseek-ai/DeepSeek-V4-Pro · Hugging Face</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek_(product)">DeepSeek (product)</a></li>
<li><a href="https://openai.com/index/introducing-codex/">Introducing Codex | OpenAI</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#AI model`, `#API`, `#LLM`, `#Agent`

---

<a id="item-13"></a>
## [SpaceXAI 发布 Grok 4.6，对标 GPT-5.6 Sol](https://www.ithome.com/0/988/999.htm) ⭐️ 8.0/10

Grok 4.6 已正式发布，相比 Grok 4.5 增强了智能体推理能力和训练方法。在综合基准 Artificial Analysis Intelligence Index 上，Grok 4.6 与 GPT-5.6 Sol 取得相同成绩，并已在 Cursor 和 Grok Build 上线。 此次发布意义重大，因为 Grok 4.6 在一个综合基准上追平了前沿模型 GPT-5.6 Sol，同时推进了长周期智能体能力，将影响开发者和 AI 研究者。新模型立即在 Cursor、Grok Build 以及 API、OpenRouter、Vercel、Cloudflare 等平台开放，扩大了实际应用范围，不过长期影响仍有待观察。 Grok 4.6 经历了比 Grok 4.5 更长的补充训练，数据包括经过筛选的模型生成推理数据、高级技术概念数据和高质量工程数据，并配合改进后的优化器和训练方案。训练中还使用了广泛的智能体强化学习，覆盖知识工作、通用编程、内核优化、Web 开发和计算机辅助设计等领域；价格为每 100 万个输入 Token 2 美元、每 100 万个输出 Token 6 美元，速度更快的版本价格翻倍。

rss · IT HOME · 8月12日 15:57

**背景**: 智能体推理指模型能够自主规划和执行多步骤任务，而不仅仅是生成一次性回答。监督微调（SFT）利用带标签的示例来调整预训练模型，强化学习（RL）则让智能体通过与环境的试错交互来最大化奖励信号。Grok 4.6 结合了这些训练范式，以处理研究、代码库处理以及将产品构想转化为可用应用等复杂多步任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Safe_reinforcement_learning">Safe reinforcement learning</a></li>
<li><a href="https://gravity.fast/blog/what-is-agentic-reasoning/">What Is Agentic Reasoning ? A Clear Explanation | Gravity</a></li>

</ul>
</details>

**标签**: `#AI`, `#Grok`, `#Model Release`, `#Benchmarks`, `#Agents`

---

<a id="item-14"></a>
## [Mojo 1.0 正式发布，编译器计划年内开源](https://www.ithome.com/0/988/945.htm) ⭐️ 8.0/10

Modular 已正式发布 Mojo 1.0 版本，统一了语法和类型系统，并为“引用失效”问题加入了诊断能力。官方还重申计划在今年内开源 Mojo 编译器及相关工具链。 这一里程碑为 AI 开发者提供了一种稳定、高性能且面向 CPU、GPU 及其他加速器的编程语言。开源编译器将让更广泛的社区参与进来，并可能加速 Mojo 在 AI 基础设施中的采用。 Mojo 1.0 统一了变量、闭包和指针类型等多种表达方式，并新增类 Python 的 lambda 匿名函数语法。它还能识别引用失效情况，例如向 List 添加元素后原有引用失效。后续计划加入异步编程、模式匹配和联合类型等功能。

rss · IT HOME · 8月12日 11:47

**背景**: Mojo 是 Modular 开发的一种系统编程语言，面向 AI 硬件和异构加速计算。它的语法类似 Python，同时提供受 Rust 启发的静态类型和内存安全特性，并基于 MLIR 编译器框架而非直接基于 LLVM，因此能面向 CPU、GPU、TPU 及其他加速器编译。该语言最初计划成为 Python 的超集，但这一目标已被搁置；Modular 计划在 2026 年开源 Mojo。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mojo_(programming_language)">Mojo (programming language)</a></li>
<li><a href="https://mojolang.org/">Mojo</a></li>

</ul>
</details>

**标签**: `#AI programming`, `#Mojo`, `#compiler`, `#open source`, `#Modular`

---

<a id="item-15"></a>
## [比亚迪 AI 团队首秀 HyWorldVLA，NAVSIM v1 获 90.59 分刷榜](https://www.ithome.com/0/988/942.htm) ⭐️ 8.0/10

比亚迪汽车新技术研究院发表首篇研究论文，提出混合世界模型 HyWorldVLA，将像素级与潜在空间世界建模统一到视觉-语言-动作（VLA）架构中。该模型在 NAVSIM v1 基准上取得 90.59 的 PDMS 评分，刷新历史最佳，并在 NAVSIM v2 上取得 89.71 分。 这是比亚迪首次公开发表 AI 研究成果，展示了从算法到自研芯片的完整闭环，使其成为 L3 级自动驾驶领域的重要参与者。混合世界建模方法或将为自动驾驶系统在预测细节与计算效率之间如何取舍提供新思路。 消融实验显示，移除像素级预测后 PDMS 从 90.59 降至 87.50，移除潜在空间处理后则降至 89.91。在 655 个雨雾噪声场景测试中，HyWorldVLA 得分为 86.87，比最强基线高出 19 分以上。

rss · IT HOME · 8月12日 11:33

**背景**: HyWorldVLA 基于视觉-语言-动作（VLA）架构，将视觉感知、语言理解与驾驶动作策略相结合。NAVSIM 是一个数据驱动、非反应式的自动驾驶规划闭环仿真基准，采用预测性驾驶模型分数（PDMS）评估碰撞安全性、可行驶区域合规性、安全距离、目标完成度和乘坐舒适性。2026 年 5 月，比亚迪发布了中国首款 4nm 车规级智驾芯片“璇玑 A3”，单颗算力约 700TOPS，支持三颗并联，整车算力最高可超 2100TOPS。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.20988v1">HyWorldVLA : A Vision-Language-Action Model with Hybrid World ...</a></li>
<li><a href="https://www.alphaxiv.org/overview/2607.20988">HyWorldVLA : A Vision-Language-Action Model with Hybrid World ...</a></li>
<li><a href="https://www.tech360.tv/byd-ai-introduces-hybrid-world-model-exceeds-autonomous-driving-benchmark-2026-30-07">BYD AI Introduces Hybrid World Model , Exceeds... | tech360tv</a></li>

</ul>
</details>

**标签**: `#autonomous driving`, `#world models`, `#vision-language-action`, `#AI research`, `#BYD`

---

<a id="item-16"></a>
## [Claude 将黎曼猜想零点下界从 41.6% 提升至 67.2%](https://www.anthropic.com/research/riemann-zeta) ⭐️ 8.0/10

Anthropic 称，一个未发布的研究版 Claude 将满足黎曼猜想的黎曼 ζ 函数非平凡零点的比例下界从 41.6% 提高到 67.2%。 这显示了 AI 在高等数学中取得实质性进展的潜力，而不仅仅是解决教科书式习题。如果结果可复现并可验证，可能为数论及其他困难数学问题开启新的研究范式。 Anthropic 尚未公布相关证明或同行评审论文，公告只描述了一个未发布的研究模型。新的下界仍然低于黎曼猜想所预测的 100%，因此这是对下界的改进，而非对猜想的证明。

rss · Anthropic Research · 8月10日 17:00

**背景**: 黎曼 ζ 函数 ζ(s) 是数论的核心对象，其非平凡零点被普遍认为都位于临界线 Re(s)=1/2 上，这就是黎曼猜想。数学家目前还无法证明 100% 的零点都在该线上，但长期以来已经证明了其中必有某个比例。借助 Claude，研究者将这一比例的下界从约 41.6% 提高到约 67.2%，并且延续了此前同类方法的证明框架。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mathworld.wolfram.com/RiemannHypothesis.html">Riemann Hypothesis -- from Wolfram MathWorld</a></li>
<li><a href="https://www.datacamp.com/tutorial/claude-and-the-riemann-hypothesis">Claude Tried the Riemann Hypothesis . Here's What... | DataCamp</a></li>

</ul>
</details>

**标签**: `#AI research`, `#mathematics`, `#Riemann hypothesis`, `#Claude`, `#Anthropic`

---

<a id="item-17"></a>
## [DeepMind：LLM 事实性的瓶颈在于回忆而非存储](https://research.google/blog/empty-shelves-or-lost-keys-recall-is-the-bottleneck-for-parametric-factuality/) ⭐️ 8.0/10

谷歌 DeepMind 研究人员发表博客文章，认为大语言模型（LLM）在参数化事实性（利用已存储知识回答问题的能力）上的失败，主要源于回忆（recall）能力的不足，而非知识缺失。他们用“空货架”与“丢失的钥匙”的类比来重新定义这一问题。 这一重新定义将事实性研究的重点从扩充存储知识转向改进模型提取和检索知识的方式。如果该观点成立，那么推理轨迹或更好的推理期方法等技术，可以在不重新训练或增大模型的情况下提高可靠性。 参数化知识指预训练期间直接编码进模型权重的事实，区别于通过提示或检索提供的上下文知识。研究人员认为，“丢失的钥匙”的情况比“空货架”更常见，即许多事实已被存储，但未被成功回忆出来。

rss · Google Deepmind Blog · 8月12日 09:51

**背景**: LLM 的参数化知识在预训练期间获得，并以网络权重的形式存储，使模型无需外部检索即可回答问题。以往人们常认为事实性失败意味着模型从未学到该事实；但这项研究区分了“不知道”（空货架）和“知道但无法访问”（钥匙丢失）两种情形。谷歌 DeepMind 的另一篇博文《思考以回忆》（Thinking to recall）表明，推理轨迹有助于解锁这类潜在知识。此类工作与更广泛的研究相呼应，即 LLM 中的事实回忆在参数中是以分布式和冗余的方式实现的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://research.google/blog/thinking-to-recall-how-reasoning-unlocks-parametric-knowledge-in-llms/">Thinking to recall: How reasoning unlocks parametric knowledge in LLMs</a></li>
<li><a href="https://arxiv.org/html/2606.21345v1">Factual Retrieval in LLMs Is a Redundant, Distributed and Non-Contiguous Process</a></li>
<li><a href="https://www.emergentmind.com/topics/facts-parametric">FACTS Parametric : Factual Memory in LLMs</a></li>

</ul>
</details>

**标签**: `#Large Language Models`, `#Factuality`, `#Memory`, `#AI Research`, `#DeepMind`

---

<a id="item-18"></a>
## [谷歌 DeepMind 推进 AMIE，迈向专家级音视频临床咨询](https://research.google/blog/advancing-amie-towards-expert-level-audio-visual-clinical-consultations/) ⭐️ 8.0/10

谷歌 DeepMind 宣布推进 AMIE，将其能力从纯文本交互扩展至音视频临床咨询。据报道，该系统现在可以开展实时视频咨询，而不仅仅是文本聊天。 这一多模态升级可以让 AI 在咨询中观察视觉和听觉线索，有望显著改善远程医疗和临床决策支持。它将影响医生、患者以及整个医疗 AI 生态，使 AI 更接近真实世界的诊断实践。 AMIE 的全称是 Articulate Medical Intelligence Explorer，由 Google Research 和 Google DeepMind 开发。它目前仍是研究性系统，而非商业临床产品，其诊断准确性和安全性仍需严格验证。

rss · Google Deepmind Blog · 8月11日 17:04

**背景**: AMIE 是谷歌研发的实验性 AI“临床推理器”，旨在通过医患对话进行医学诊断。多模态 AI 能同时处理文本、图像、音频和视频，这一进展正是利用该能力来捕捉更丰富的临床线索，如面部表情、语调和肢体动作。向音视频咨询的拓展，使 AI 更贴近远程医疗中自然的医患交互方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mykreatool.com/en/news/google-amie-meditsinskiy-ai-konsultant">Google AMIE : AI Doctor for Video Consultations — MyKreaTool</a></li>
<li><a href="https://tech.hindustantimes.com/tech/news/ai-assistant-for-doctors-google-deepmind-working-on-ai-model-that-helps-diagnose-patients-71706510279319.html">AI assistant for doctors? Google DeepMind ... | Tech News (HT Tech)</a></li>
<li><a href="https://www.linkedin.com/posts/melvin-speisman-md-facp-faim-671a06266_read-this-nature-medicine-paper-on-using-activity-7426794770653487105-MKY-">Google ' s AMIE : AI Clinical Reasoner for Medical Diagnosis | LinkedIn</a></li>

</ul>
</details>

**标签**: `#AI`, `#Healthcare`, `#Multimodal`, `#Clinical AI`, `#Google DeepMind`

---

<a id="item-19"></a>
## [NVIDIA Nemotron 3.5 Lightning 加速长时运行智能体工作流](https://developer.nvidia.com/blog/nvidia-nemotron-3-5-lightning-delivers-fast-accurate-specialized-task-execution-for-long-running-agents/) ⭐️ 8.0/10

NVIDIA 发布了 Nemotron 3.5 Lightning，这是一个 30B 参数的开源混合专家（MoE）模型，仅激活 3B 参数，专为长时运行 AI 智能体中的高容量、低延迟专项任务执行而优化。该模型的输出速度最高可达同类模型的 4 倍。 长时运行的 AI 智能体大部分时间都花在工具调用、结果验证和子智能体委派等高容量操作上，容易造成延迟和成本瓶颈。此次发布为智能体开发者提供了更快、更高效的常驻生产工作流模型，有望降低智能体 AI 系统的运营开销。 该模型是开源的，在 Hugging Face 上提供 BF16 格式，并有一个 NVFP4 优化版本用于加速推理。NVIDIA 还在 NeMo Gym 中发布了评估配方、安装说明和命令，以确保可复现性。

rss · NVIDIA Developer Blog · 8月11日 13:01

**背景**: 智能体 AI（Agentic AI）指的是能够自主追求目标、使用工具、验证输出并将任务委派给子智能体的 AI 程序。在长时间运行的智能体工作流中，高容量的执行步骤会带来显著的延迟和计算开销。混合专家（MoE）模型在生成每个 token 时只激活一部分参数，从而在保持较大模型容量的同时实现更快的推理。Nemotron 3.5 Lightning 正是采用这种架构来服务需要快速、准确处理专项任务的常驻智能体。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/nvidia-nemotron-3-5-lightning-delivers-fast-accurate-specialized-task-execution-for-long-running-agents/">NVIDIA Nemotron 3 . 5 Lightning Delivers Fast, Accurate Specialized...</a></li>
<li><a href="https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16">nvidia / NVIDIA - Nemotron - 3 . 5 - Lightning -30B-A3B-BF16 · Hugging Face</a></li>
<li><a href="https://www.linkedin.com/posts/jenhsunhuang_lightning-strikes-for-continuous-and-long-run-activity-7492950397624414209-_oBz">Lightning strikes for continuous and long-run agents! Nemotron ...</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#AI agents`, `#agentic AI`, `#LLM`, `#model release`

---

<a id="item-20"></a>
## [NVIDIA NeMo Switchyard：跨模型路由 AI 智能体工作负载](https://developer.nvidia.com/blog/route-ai-agent-workloads-across-models-with-nvidia-nemo-switchyard/) ⭐️ 8.0/10

NVIDIA 发布了 NeMo Switchyard，这是一个面向 AI 智能体的开源模型路由库。它可将智能体工作流的每一步路由到最有效且最高效的模型，支持免调优和可调优路由器，并能转换 OpenAI Chat、Anthropic Messages 和 OpenAI Responses 等 API 格式。 这解决了 AI 智能体开发中日益增长的成本与性能优化需求——不同的模型具有不同的优势和成本特征。通过自动平衡能力、成本和延迟，Switchyard 有望成为构建高效多模型智能体系统的重要工具。 该库支持 Claude Code 和 Codex 等编程智能体，使它们能够指向开源模型的同时保持原生 API。它支持 vLLM、NVIDIA NIM、Ollama 以及任何 OpenAI 兼容端点等推理后端，并且路由器可针对特定工作负载进行调优。

rss · NVIDIA Developer Blog · 8月11日 13:00

**背景**: 模型路由是一种降低 LLM 推理成本的技术，它维护一个候选模型池，并学习将每个提示发送到仍能满足质量要求的最小或最具成本效益的模型。NeMo Switchyard 是 NVIDIA NeMo 生态系统的一部分，该生态系统提供了构建、定制和部署生成式 AI 模型的工具。该库将这一概念扩展到智能体 AI，在多步骤工作流的每一步中，不同模型可能各有优势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/NVIDIA-NeMo/Switchyard">GitHub - NVIDIA-NeMo/Switchyard · GitHub</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#model routing`, `#NVIDIA`, `#LLM`, `#cost optimization`

---

<a id="item-21"></a>
## [美团开源 LoHoSearch：用知识图谱校准搜索智能体能力](https://tech.meituan.com/2026/07/24/LongCat-LoHoSearch.html) ⭐️ 8.0/10

美团开源了下一代搜索智能体评测基准 LoHoSearch，利用知识图谱来校准 AI 能力。此举旨在应对 BrowseComp 等现有评测迅速饱和的问题，这些基准上顶尖模型的准确率在一年内从约 30%攀升至 90%以上。 随着现有搜索智能体基准逐渐饱和，它们区分模型能力的作用减弱，使进展难以测量。LoHoSearch 基于知识图谱的方法可能提供更稳健、更细致的评测方式，帮助研究者更准确地追踪搜索智能体的进步，并推动 AI 评测领域迈向更可靠的方向。 提供的资料显示，在 BrowseComp 上，顶尖模型的准确率在一年内从约 30%提升至 90%以上，凸显了 LoHoSearch 试图解决的饱和问题。目前公开来源中尚未披露 LoHoSearch 的具体技术构建或知识图谱方法的细节。

rss · 美团 Blog · 8月12日 16:58

**背景**: 搜索智能体基准如 OpenAI 的 BrowseComp，会测试 AI 代理持续浏览互联网以寻找难以发现、相互纠缠信息的能力；BrowseComp 包含 1,266 个此类问题。知识图谱是实体及其关系的结构化表示，可作为更严格的模型推理测试平台。当基准饱和——如 BrowseComp 已经出现的情况，顶级模型得分超过 90%——它就无法再区分模型强弱，因此需要像 LoHoSearch 这样的新基准来保持评测的意义。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://llm-stats.com/benchmarks/browsecomp">BrowseComp Leaderboard | LLM Stats</a></li>
<li><a href="https://openai-dotcom-git-main-openai.vercel.app/index/browsecomp/">BrowseComp : a benchmark for browsing agents | OpenAI</a></li>
<li><a href="https://benchlm.ai/benchmarks/browsecomp">BrowseComp Leaderboard & Scores — July 2026 | BenchLM.ai</a></li>

</ul>
</details>

**标签**: `#benchmark`, `#search agents`, `#knowledge graphs`, `#AI evaluation`, `#Meituan`

---

<a id="item-22"></a>
## [MineExplorer 基准揭示多模态大模型能力断层](https://tech.meituan.com/2026/07/24/LongCat-MineExplorer.html) ⭐️ 8.0/10

美团 LongCat 团队推出了 MineExplorer，这是首个在开放世界中评估多模态大模型在包含隐藏前置条件的分钟级长程任务的基准。该基准系统性地揭示了顶级模型的能力断层。 这填补了 AI 评估中的一个关键空白，因为大多数基准依赖于片段化、特定领域的任务，无法反映现实世界中带有隐藏约束的长程规划。它可能引导多模态智能体未来的发展，走向更适应性和开放世界的推理。 MineExplorer 使用 Minecraft Java Edition 环境，过滤掉 Minecraft 特有的先验知识，并通过多智能体合成构建多跳任务。任务被设计为原子和多跳步骤，要求模型具备长程规划以及发现隐藏前置结构的能力。

rss · 美团 Blog · 8月12日 16:58

**背景**: 多模态大语言模型越来越多地被用作交互环境中的智能体，但评估通常集中于短且定义明确的任务。长程规划涉及带记忆和执行的逐步推理，而隐藏前置条件是指任务中未显式说明的约束。现有的游戏基准往往将成功与特定的游戏机制绑定，因此 MineExplorer 旨在提供更通用和实用的评估。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/mineexplorer-benchmark">MineExplorer Benchmark Overview</a></li>
<li><a href="https://huggingface.co/papers/2605.30931">Paper page - MineExplorer : Evaluating Open-World Exploration of...</a></li>
<li><a href="https://benchmarklist.com/benchmarks/mineexplorer/">MineExplorer Benchmark Scores & AI Model... | BenchmarkList</a></li>

</ul>
</details>

**标签**: `#multimodal LLM`, `#benchmark`, `#long-horizon planning`, `#open-world evaluation`, `#AI research`

---

<a id="item-23"></a>
## [美团正式开源 LongCat-2.0：1.6T 参数 Agentic Coding 大模型](https://tech.meituan.com/2026/07/12/LongCat-2.0-Open-source.html) ⭐️ 8.0/10

美团正式开源了 LongCat-2.0，这是一个总参数 1.6T、平均激活约 48B 的稀疏大语言模型，并同步开放了国产 GPU 推理代码。该版本引入 LongCat 稀疏注意力与 N-gram Embedding，面向真实 Agentic Coding 任务提升长上下文处理能力。 此次开源意义重大，因为团队将百万级长上下文、1.6T 参数的编程大模型开放出来，为研究人员和工程师提供了可直接借鉴的稀疏注意力与 N-gram 嵌入方案。同步开放国产卡推理代码，也有助于降低对海外加速器的依赖，推动本土 AI 基础设施生态发展。 LongCat-2.0 采用 LongCat 稀疏注意力（LSA），只关注最相关的 token，使计算量接近线性增长，从而让 100 万 token 的上下文变得可用；N-gram Embedding 则通过聚合前 N-1 个 token 的信息增强短距离依赖的表示。模型还结合动态激活机制，进一步强化 Agentic Coding 场景下的代码理解、生成与执行能力。

rss · 美团 Blog · 8月12日 16:58

**背景**: 传统大模型的密集注意力机制计算量随上下文长度呈二次增长，导致 100 万 token 这样的超长上下文非常昂贵。LongCat 稀疏注意力等稀疏注意力方法只选择与当前查询最相关的 token 进行计算，将复杂度降到接近线性。Agentic Coding 是一种开发范式：AI Agent 自主阅读代码库、修改文件、运行测试并反复迭代逼近目标，因此对长上下文能力要求很高。N-gram Embedding 则通过建模连续 N 个 token（或子词）的局部序列来捕获短距离依赖关系。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepwiki.com/meituan-longcat/LongCat-2.0/2.2-longcat-sparse-attention-(lsa)">LongCat Sparse Attention (LSA) | DeepWiki</a></li>
<li><a href="https://felloai.com/longcat-2-0/">LongCat -2.0: China's 1.6T Open-Source Coding Model</a></li>
<li><a href="https://arxiv.org/pdf/2601.21204">Scaling Embeddings Outperforms Scaling Experts in Language Models</a></li>

</ul>
</details>

**标签**: `#large language models`, `#open source`, `#agentic coding`, `#long-context`, `#sparse attention`

---

<a id="item-24"></a>
## [美团发布 LongCat-2.0：5 万国产芯片集群训练的万亿参数 MoE 模型](https://tech.meituan.com/2026/06/30/LongCat2.0.html) ⭐️ 8.0/10

美团正式发布 LongCat-2.0，这是一个总参数达 1.6 万亿的混合专家（MoE）模型，平均激活约 480 亿参数，原生支持 100 万 token 上下文。官方称其为业界首个在 5 万张国产 AI 加速卡集群上完成全流程训练与推理的万亿参数模型，从零预训练，面向智能体编码（Agentic Coding）场景。 这一成果是国产 AI 芯片生态的重要里程碑，证明万亿参数级别的前沿模型可以在国产算力集群上端到端训练，而不必完全依赖 NVIDIA GPU。同时它推动了 MoE 架构和超长上下文智能体编码的发展，有望降低大规模 AI 开发对进口加速卡的依赖。 LongCat-2.0 总参数为 1.6 万亿，动态激活参数范围为 330 亿至 560 亿，平均约 480 亿。其架构从一开始就围绕真实智能体编码任务中的代码理解、生成与执行进行设计，原生支持 100 万 token 的上下文长度。

rss · 美团 Blog · 8月12日 16:58

**背景**: 混合专家（MoE）是一种大模型架构，模型包含多个专门的子网络（即“专家”），每个 token 只激活其中一部分，从而在参数规模大幅扩大的同时保持相对较低的计算成本。智能体编码（Agentic Coding）指的是 AI 智能体能够自主完成代码的规划、编写、测试和修复，而不仅仅是提供建议，这要求模型具备强大的长上下文处理与工具调用能力。在 5 万张国产加速卡集群上训练万亿参数模型，还涉及分布式训练、容错和集群级优化等一系列关键技术进步。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mixture-of-experts">A Visual Guide to Mixture of Experts ( MoE )</a></li>
<li><a href="https://arxiv.org/abs/2112.10684">Efficient Large Scale Language Modeling with Mixtures of Experts</a></li>
<li><a href="https://sourcegraph.com/blog/agentic-coding">Agentic Coding in 2026: A Practical Guide for Big Code | Sourcegraph</a></li>

</ul>
</details>

**标签**: `#Large Language Models`, `#AI Infrastructure`, `#MoE`, `#Training at Scale`, `#Agentic Coding`

---

<a id="item-25"></a>
## [以数据为中心的并行方法加速变长序列训练](https://arxiv.org/abs/2608.07524) ⭐️ 8.0/10

提出了以数据为中心的并行方法（DCP），该方法根据每个批次的序列长度动态调整并行度、梯度累积和重计算设置。在 32 块 H200 GPU 上取得了最高 2.88 倍的加速，且仅需约 10 行代码改动。 视频等变长数据的长时间序列训练常因静态配置导致工作负载不均衡，成为性能瓶颈。DCP 提供了一种简单且通用的方案，打破了效率与易用性之间的权衡，对机器学习系统研究者和实践者都具有参考价值。 DCP 让数据本身驱动运行时决策，按批次而非按模型调整配置。作者声称它仅需约 10 行代码即可泛化到任意模型，但目前作为预印本仍需要更多验证。

rss · arXiv cs.AI · 8月12日 04:00

**背景**: 在视频片段等长度可变的序列上训练深度学习模型时，固定的并行化配置通常针对特定形状优化，导致工作负载不均衡。现有方法要么使用简单但浪费资源的静态配置，要么需要大量代码改动的复杂系统。DCP 则观察每个批次的序列长度，并实时调整并行度、梯度累积和重计算，旨在兼顾两类方法的优点。以数据为中心的优化思想也出现在其他领域，例如数据中心的并行编程框架。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://oahzxl.github.io/DCP/">Training Variable Sequences with Data - Centric Parallel</a></li>

</ul>
</details>

**标签**: `#distributed training`, `#long sequences`, `#parallel computing`, `#deep learning systems`, `#efficiency`

---