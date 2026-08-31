---
layout: default
title: "Horizon Summary: 2026-08-31 (ZH)"
date: 2026-08-31
lang: zh
---

> 从 436 条内容中筛选出 25 条重要资讯。

---

1. [NSA 开源逆向工程框架 Ghidra：反汇编与反编译一体化](#item-1) ⭐️ 9.0/10
2. [破解 Claude Code Opus 5 自动模式：安全分析揭示攻击途径](#item-2) ⭐️ 8.0/10
3. [LiveKit Agents：构建实时语音 AI 智能体的框架](#item-3) ⭐️ 8.0/10
4. [腾讯发布 Hy4 预览版：7700 亿参数的开源权重 MoE 大语言模型](#item-4) ⭐️ 8.0/10
5. [英伟达与联发科深化合作：投资 35 亿美元，基于 NVLink Fusion 打造定制 XPU](#item-5) ⭐️ 8.0/10
6. [DeepSeek 开源首款多模态模型 V4-Flash-Vision-Exp，采用 MIT 许可](#item-6) ⭐️ 8.0/10
7. [谷歌 DeepMind 发布 TimesFM-3，实现零样本多元时间序列预测](#item-7) ⭐️ 8.0/10
8. [美团 GeoRA：为 RLVR 设计的 LoRA 荣获 ACL 2026 杰出论文奖](#item-8) ⭐️ 8.0/10
9. [美团技术博客：由浅入深详解 Agent 评测](#item-9) ⭐️ 8.0/10
10. [MineExplorer 基准揭示多模态大模型被忽视的能力断层](#item-10) ⭐️ 8.0/10
11. [美团正式开源 LongCat-2.0：面向 Agentic Coding 的 1.6T MoE 模型](#item-11) ⭐️ 8.0/10
12. [概率依赖图融合 LLM 与贝叶斯网络，改进因果发现](#item-12) ⭐️ 8.0/10
13. [WM-R1：通过强化学习和世界模型训练移动 GUI 智能体](#item-13) ⭐️ 8.0/10
14. [LongGuard 揭示长上下文安全护栏失效机制并提供免训练缓解方案。](#item-14) ⭐️ 8.0/10
15. [带外策略执行：在可信边界约束 AI 代理越权](#item-15) ⭐️ 8.0/10
16. [用吉布斯采样与生成控制探查多模态大模型的感知先验](#item-16) ⭐️ 8.0/10
17. [Credo：为智能体工作流恢复可复用的声明式原语](#item-17) ⭐️ 8.0/10
18. [RealSWE：面向真实用户请求的编码智能体组合式基准](#item-18) ⭐️ 8.0/10
19. [以博弈论视角综述 AI 对齐研究](#item-19) ⭐️ 8.0/10
20. [跨会话分解攻击的形式化分析及意图对齐检索防御](#item-20) ⭐️ 8.0/10
21. [WhatIfBench 与 PRISM 揭示 LLM 反事实推理的脆弱性](#item-21) ⭐️ 8.0/10
22. [RA-OPD：用奖励对齐的在线蒸馏纠正教师的误导性指导](#item-22) ⭐️ 8.0/10
23. [AERA：可学习控制器高效分配测试时计算资源](#item-23) ⭐️ 8.0/10
24. [量化触发的大模型后门：利用验证-部署间隙发起攻击](#item-24) ⭐️ 8.0/10
25. [DAMP：面向循环状态的衰减感知混合精度量化](#item-25) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [NSA 开源逆向工程框架 Ghidra：反汇编与反编译一体化](https://github.com/NationalSecurityAgency/ghidra) ⭐️ 9.0/10

Ghidra 是美国国家安全局（NSA）开源的软件逆向工程（SRE）框架，现已在 GitHub 上发布，具备反汇编、汇编、反编译、图形化分析和脚本扩展能力。它支持 Windows、macOS 和 Linux 平台，并可处理多种处理器指令集与可执行文件格式。 Ghidra 为安全社区提供了免费且高水平的商业逆向工具（如 IDA Pro）替代方案，使高级反编译能力得以普及。它被恶意软件分析师、漏洞研究人员和安全团队广泛用于分析编译代码、发现软件中的潜在弱点。 安装官方发布版需要 64 位 JDK 21，且应下载 ghidra_<版本>_<发布>_<日期>.zip 资产，而非源码压缩包。项目警告部分版本存在已知安全漏洞；同时支持用 Java 或 Python 开发扩展和脚本，并提供 PyGhidra 启动方式。

rss · GitHub Trending - Daily · 8月31日 21:22

**背景**: 软件逆向工程是在缺少或没有源代码的情况下，通过信息提取、建模和审查等步骤分析已编译程序、理解其工作原理的过程。反汇编器将机器码转换为汇编语言，而反编译器则更进一步，重建近似的高级语言源码表示，但原始变量名和注释通常无法恢复。Ghidra 由 NSA 研究部门开发，旨在解决复杂逆向工程中的规模化与团队协作问题，并支持该机构的网络安全使命。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Software_reverse_engineering">Software reverse engineering</a></li>
<li><a href="https://en.wikipedia.org/wiki/Decompilation">Decompilation</a></li>

</ul>
</details>

**标签**: `#reverse-engineering`, `#security`, `#decompiler`, `#NSA`, `#open-source`

---

<a id="item-2"></a>
## [破解 Claude Code Opus 5 自动模式：安全分析揭示攻击途径](https://embracethered.com/blog/posts/2026/breaking-claude-code-opus-5-and-automode/) ⭐️ 8.0/10

一项安全分析展示了如何通过提示注入（prompt injection）和恶意文件破坏 Claude Code Opus 5 的自动模式。该攻击利用木马式载荷，利用模型的行为模式来执行非预期操作。 这项研究凸显了代理沙箱化的紧迫性，因为像 Claude Code 这样的人工智能编程代理越来越多地处理敏感任务。它表明即使是先进模型也容易受到定向攻击，开发者必须假设代理可能被诱骗执行恶意代码。 该攻击利用基于目录的遮蔽（shadowing）技术，恶意文件（例如伪造的 struct.py）在代理导入模块时覆盖 Python 标准库。社区成员指出，该攻击针对 Claude 特定的工具使用模式，例如频繁依赖 'python -c' 快速执行代码。

hackernews · Recursing · 8月31日 07:49 · [社区讨论](https://news.ycombinator.com/item?id=49506819)

**背景**: Claude Code 是 Anthropic 的代理式编程工具，在终端中运行，能够理解代码库并通过自然语言执行任务。Claude Opus 5 是一个强大的代理式编程模型，专为长时间、多步骤的工作而设计。提示注入是一类攻击，将恶意指令隐藏在输入数据中，导致 AI 代理执行非预期操作。代理沙箱化通过限制代理可以访问和运行的代码，提供隔离的执行环境来降低此类风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-opus-5">Introducing Claude Opus 5 \ Anthropic</a></li>
<li><a href="https://github.com/anthropics/claude-code/releases">Releases · anthropics/ claude - code · GitHub</a></li>
<li><a href="https://cursor.com/blog/agent-sandboxing">Implementing a secure sandbox for local agents · Cursor</a></li>

</ul>
</details>

**社区讨论**: 评论者讨论了该攻击的巧妙之处及其对 Claude 可预测工具使用模式的关注，同时有人争论它是否属于提示注入，还是更适合称为木马。一些用户分享了他们自己被遮蔽导入的经历，并建议对代理进行沙箱化，另外有人指出该攻击可能与自动模式关系不大。总体情绪是，尽管此类攻击技术高超，但强大的沙箱化仍至关重要。

**标签**: `#AI security`, `#prompt injection`, `#Claude Code`, `#agent sandboxing`, `#LLM attacks`

---

<a id="item-3"></a>
## [LiveKit Agents：构建实时语音 AI 智能体的框架](https://github.com/livekit/agents) ⭐️ 8.0/10

LiveKit Agents 是一个开源 Python 框架，用于构建支持音频和视频的实时语音 AI 智能体。它提供 STT、LLM、TTS 和实时 API 的灵活集成，并内置任务调度、电话集成和语义停顿检测等功能。 该框架简化了对话式多模态语音智能体的开发，使实时语音 AI 对开发者更加友好。它基于 LiveKit 强大的 WebRTC 基础设施，有望加速各行业对语音 AI 应用的采用。 主要特性包括使用 transformer 模型进行语义停顿检测、原生 MCP 支持、带评估器的内置测试框架，以及全面的 WebRTC 客户端 SDK。该库可通过 pip 安装（例如 `livekit-agents[openai,deepgram,cartesia]`），采用 Apache 2.0 许可证，支持完全自托管。

rss · GitHub Trending - Daily · 8月31日 21:22

**背景**: LiveKit 是一家美国科技公司，提供用于构建语音、视频和实体 AI 智能体的软件及云基础设施。LiveKit Agents 框架旨在创建运行在服务器上的实时可编程参与者，使智能体能够看见、听见和理解。它与 LiveKit 开源且广泛使用的 WebRTC 媒体服务器集成，用于实时通信。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/livekit/agents">GitHub - livekit / agents : A framework for building realtime voice AI...</a></li>
<li><a href="https://docs.livekit.io/agents/">Introduction | LiveKit Documentation</a></li>
<li><a href="https://en.wikipedia.org/wiki/LiveKit">LiveKit</a></li>

</ul>
</details>

**标签**: `#realtime-ai`, `#voice-agents`, `#livekit`, `#agent-framework`, `#open-source`

---

<a id="item-4"></a>
## [腾讯发布 Hy4 预览版：7700 亿参数的开源权重 MoE 大语言模型](https://simonwillison.net/2026/Aug/29/hy4/) ⭐️ 8.0/10

2026 年 8 月 29 日，腾讯发布了 Hy4 Preview，这是一款开放权重、仅支持文本输入的混合专家（MoE）大语言模型，总参数 7700 亿，激活参数 490 亿，上下文窗口达 100 万 token。该模型已在 Hugging Face 上开放下载（1.56TB），相比腾讯 7 月发布的 Hy3（总参数 2950 亿、激活参数 210 亿）规模大幅提升。 Hy4 Preview 是迄今发布的最大开放权重模型之一，让研究人员和开发者无需受 API 限制即可使用接近前沿水平的能力。其百万级上下文窗口和大型 MoE 设计可能加速长上下文任务的研究与开放模型开发，并加剧开放权重提供商之间的竞争。 该模型仅支持文本输入，不具备视觉能力。其 chat_template 显示只有两种推理强度模式：‘high’（默认）和 ‘no_think’，传入其他值会报错；作者用 SVG 生成提示词实测时，能看到以略显简略的英文写成的推理轨迹，且发布公告未提供详细基准测试结果。

rss · Simon Willison · 8月29日 23:53

**背景**: 混合专家（MoE）模型会把模型划分为多个专门的子模型（即‘专家’），每次输入只激活其中一部分。因此 MoE 模型会同时报告两个参数：总参数代表整体规模，激活参数决定每次推理所需的计算量与速度。‘开放权重’意味着训练好的权重可以公开下载，任何人都能在自己的设备上运行、研究或微调该模型，但这与完全开源并不等同。Hy4 继承自腾讯 Hy3，将开放权重模型的规模推到了新的量级。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://latenteast.com/insights/moe-total-vs-active-parameters">MoE Total vs Active Parameters , Explained | The Latent East</a></li>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>

</ul>
</details>

**标签**: `#LLM`, `#Tencent`, `#open-weights`, `#MoE`, `#AI`

---

<a id="item-5"></a>
## [英伟达与联发科深化合作：投资 35 亿美元，基于 NVLink Fusion 打造定制 XPU](https://www.ithome.com/0/996/645.htm) ⭐️ 8.0/10

2025 年 8 月 31 日，英伟达与联发科宣布深化长期合作关系：联发科将基于英伟达的 NVLink Fusion 平台为客户开发定制的 XPU 芯片，并集成到英伟达的机柜级系统及 AI 工厂中。同时，英伟达通过海外可转换公司债向联发科投资 35 亿美元。 这一合作标志着 AI 硬件生态系统的重大转变，将英伟达在加速计算和 AI 软件生态方面的领先地位，与联发科在 SoC 设计和定制芯片方面的实力相结合。它可能加速定制化 AI 基础设施在云端、边缘和汽车平台的普及，帮助客户大规模构建具有差异化优势的 AI 系统。 除了 XPU 合作，双方还将继续合作开发未来数代的 RTX Spark 和 DGX Spark 电脑芯片，以及具备 AI 功能的软件定义汽车（SDV）平台。据 IT 之家注释，35 亿美元的投资按现行汇率约合人民币 235.75 亿元。

rss · IT HOME · 8月31日 12:34

**背景**: NVLink Fusion 是英伟达于 2025 年 5 月推出的高带宽、低延迟的连接技术和 IP，允许超大规模企业和 AI 原生公司将其定制的 XPU 和 CPU 部署到英伟达的 AI 基础设施平台中。XPU 通常指定制的 AI 加速器芯片，这一术语由博通等公司推广使用。DGX Spark 是英伟达基于 Blackwell 架构的个人 AI 超级计算机，RTX Spark 则是面向笔记本电脑的变体，两者都旨在本地运行 AI 工作负载。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/data-center/nvlink-fusion/">Build Semi-Custom AI Infrastructure | NVIDIA NVLink Fusion</a></li>
<li><a href="https://nvidianews.nvidia.com/news/nvidia-nvlink-fusion-semi-custom-ai-infrastructure-partner-ecosystem">NVIDIA Unveils NVLink Fusion for Industry to Build Semi ...</a></li>
<li><a href="https://www.nvidia.com/en-us/products/workstations/dgx-spark/">Personal AI Supercomputer Powered by Blackwell | NVIDIA DGX Spark</a></li>

</ul>
</details>

**标签**: `#AI Hardware`, `#NVIDIA`, `#MediaTek`, `#XPU`, `#AI Infrastructure`

---

<a id="item-6"></a>
## [DeepSeek 开源首款多模态模型 V4-Flash-Vision-Exp，采用 MIT 许可](https://www.ithome.com/0/996/637.htm) ⭐️ 8.0/10

DeepSeek 已在 Hugging Face 上以 MIT License 开源其首款多模态模型 DeepSeek-V4-Flash-Vision-Exp。开源内容包括模型文件、Tokenizer、Prompt Encoding 参考实现，以及覆盖视觉编码器、Aligner、DFlash Attention、MoE、Hyper-Connections 与 DSpark 等模块的最小化 PyTorch 推理实现。 此次发布标志着 DeepSeek 进军开源多模态 AI 领域，以宽松许可提供视觉语言模型，可能惠及全球开发者和研究人员。官方声称其多模态 Agent 能力接近 Opus-4.8，这可能改变开放权重模型的竞争格局，尤其是在 Agent 和视觉语言工作流方面。 该模型为实验版‘Exp’，原生支持 JPEG、PNG、GIF、WebP 格式的图片输入，可用于图片描述、截图文字识别、图表分析等任务。它自 2026 年 8 月 21 日起已上线 DeepSeek API 平台，纯文本任务表现与 V4-Flash 正式版持平，在需要视觉理解的 Agent 基准测试中有显著提升。

rss · IT HOME · 8月31日 11:35

**背景**: DeepSeek V4 系列采用混合专家（MoE）架构，每个 token 只激活部分参数，从而在规模与算力之间取得平衡。DFlash Attention 是一种基于块扩散的投机解码技术，可在多种后端上将大模型推理速度提升 2 到 3 倍。Hyper-Connections 是 DeepSeek 研究中的连接机制，它为模型扩展提供了除深度和宽度之外的第三维度——连通性。在多模态模型中，Aligner 模块负责对齐视觉特征与文本表示，使模型能够协同理解图像与文本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pyshine.com/DFlash-Block-Diffusion-Speculative-Decoding/">DFlash : Block Diffusion for Lightning-Fast LLM Speculative... | PyShine</a></li>
<li><a href="https://www.linkedin.com/posts/artificial-intelligence-and-safety_mhc-research-paper-activity-7412588536710881280-Cnep">DeepSeek-AI Introduces Manifold-Constrained Hyper - Connections</a></li>
<li><a href="https://www.emergentmind.com/topics/implicit-aligner">Implicit Aligner Overview</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#Multimodal AI`, `#Open Source`, `#Hugging Face`, `#AI Model`

---

<a id="item-7"></a>
## [谷歌 DeepMind 发布 TimesFM-3，实现零样本多元时间序列预测](https://research.google/blog/timesfm-3-a-zero-shot-foundation-model-for-multivariate-forecasting/) ⭐️ 8.0/10

谷歌 DeepMind 发布了 TimesFM-3，这是一个拥有 3.3 亿参数的时间序列基础模型，在超过 1 万亿个时间点上预训练，能够以零样本方式实现原生多元预测。 TimesFM-3 在零样本多元预测领域树立了新的技术标杆，在多个主要基准测试中超越了其他预测模型，降低了缺乏大规模行业特定数据集的使用者的应用门槛。 该模型交替使用因果时间注意力与全变量注意力来捕捉跨序列依赖，并支持仅过去以及过去和未来的协变量。模型已以 TimesFM 3.0 版本在 GitHub 上发布。

rss · Google Deepmind Blog · 8月31日 17:19

**背景**: 时间序列预测是根据历史观测值预测未来数值；多元时间序列预测则同时对多个相互关联的变量建模。传统模型通常需要针对特定任务进行微调，而 TimesFM 这样的基础模型在海量数据上预训练后，可以不经过训练直接泛化到新任务。零样本泛化意味着模型无需额外示例即可直接应用于未见过的数据集。TimesFM-3 建立在谷歌早期 TimesFM 工作的基础之上，早期版本曾在超过 1000 亿个时间点上预训练。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://research.google/blog/timesfm-3-a-zero-shot-foundation-model-for-multivariate-forecasting/">TimesFM-3: A zero-shot foundation model for multivariate forecasting</a></li>
<li><a href="https://github.com/google-research/timesfm/">GitHub - google-research/timesfm: TimesFM (Time Series Foundation Model ...</a></li>
<li><a href="https://www.marktechpost.com/2026/08/31/google-ai-releases-timesfm-3-a-330m-parameter-zero-shot-foundation-model-for-multivariate-time-series-forecasting/">Google AI Releases TimesFM-3: A 330M Parameter Zero-Shot Foundation ...</a></li>

</ul>
</details>

**标签**: `#time-series forecasting`, `#foundation models`, `#zero-shot learning`, `#Google DeepMind`, `#multivariate forecasting`

---

<a id="item-8"></a>
## [美团 GeoRA：为 RLVR 设计的 LoRA 荣获 ACL 2026 杰出论文奖](https://tech.meituan.com/2026/08/27/ACL-Outstanding-Paper-GeoRA.html) ⭐️ 8.0/10

美团履约技术团队凭借 GeoRA——一种专为基于可验证奖励的强化学习（RLVR）设计的低秩训练方法——荣获 ACL 2026 杰出论文奖。该论文阐述了这一方法及其在业务 Agentic RL 中的成功落地经验。 这一荣誉体现了学术研究与工业落地的罕见结合：GeoRA 将参数高效的低秩微调方法引入 RLVR，而 RLVR 对提升大模型推理能力和智能体行为至关重要。同时，它验证了 RLVR 在生产业务环境中的实用性，可能影响企业未来在大模型后训练方面的策略。 GeoRA 是 ACL 2026 年入选的仅 18 篇杰出论文之一。该工作针对 RLVR 训练大模型时的稳定性与计算开销问题，并分享了在美团业务 Agentic RL 系统中部署的实践经验。

rss · 美团 Blog · 8月31日 21:23

**背景**: 基于可验证奖励的强化学习（RLVR）是一种后训练方法，通过强化学习对语言模型进行微调，其奖励来自自动化的、基于规则的检查器（如单元测试、精确匹配答案或形式化证明），而非学习的奖励模型或人工评分。LoRA（低秩自适应）是一种参数高效的微调技术，通过在模型注意力权重上添加并优化小型低秩矩阵，通常可将可训练参数减少约 90%，从而降低显存和计算开销。Agentic RL 是指用于训练 AI 智能体的强化学习方法，这些智能体通过多轮轨迹与动态环境交互，通常使用 PPO、GRPO 或 REINFORCE 等优化器。GeoRA 的独特之处在于将这些理念相结合——在 RLVR 场景中应用低秩训练，并在真实业务部署中得到验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reinforcement-learning.com/kb/rlvr">RLVR: Reinforcement Learning with Verifiable Rewards</a></li>
<li><a href="https://en.wikipedia.org/wiki/LoRA_(machine_learning)">LoRA (machine learning) - Wikipedia</a></li>
<li><a href="https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter11/Chapter11-Agentic-RL.md">hello-agents/docs/chapter11/Chapter11-Agentic-RL.md at main · datawhalechina/hello-agents</a></li>

</ul>
</details>

**标签**: `#RLVR`, `#LoRA`, `#Agentic RL`, `#Efficient Fine-tuning`, `#ACL 2026`

---

<a id="item-9"></a>
## [美团技术博客：由浅入深详解 Agent 评测](https://tech.meituan.com/2026/08/07/Agent-Evaluation.html) ⭐️ 8.0/10

美团技术博客于 2026 年 8 月 7 日发布了一篇科普文章，由浅入深地介绍 Agent 评测。文章分享了美团图灵 Agent 评测团队两年来的实践经验，这些经验来自他们深入各业务团队的 BP 总结。 随着基于大语言模型的智能体在生产环境中广泛应用，评测成为关键且富有挑战的任务。美团经过实践检验的评测体系为构建和评估 AI 智能体的工程师与研究者提供了宝贵的实战经验，有助于弥合指标与业务成果之间的鸿沟。 文章前两章系统介绍了评测是什么以及如何建立评测体系；其中第二章是核心，总结了美团图灵 Agent 评测团队深入各业务团队 BP 的实践经验。本文定位为科普文章，而非深入的技术论文。

rss · 美团 Blog · 8月31日 21:23

**背景**: Agent 评测是指对由大语言模型驱动的智能体（Agent）的能力、可靠性和安全性进行评估，这类智能体能够使用工具和推理完成多步骤任务。常用的评测框架包括 RAGAS、TruLens 和 DeepEval，也有像 OdysseyBench 这样的基准专门针对长周期办公流程。美团是中国主要的互联网公司，经常通过其技术博客分享工程实践。正如相关分析所指出的，Agent 评测的一个常见陷阱是评测指标与业务结果不一致，因此实践经验尤为宝贵。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tech.meituan.com/2026/08/07/Agent-Evaluation.html">Agent评测漫谈 —— 由浅入深讲解Agent评测 | 美团 · 技术团队</a></li>
<li><a href="https://blog.mushroom.cv/blog/meituan-agent-evaluation-trajectory-rubric-harness-practice/">meituan-agent-evaluation-trajectory-rubric-harness-practice</a></li>
<li><a href="https://genalphai.com/ragas-vs-trulens-vs-deepeval-the-2026-llm-eval-showdown/">RAGAS vs TruLens vs DeepEval: The 2026 LLM Eval Showdown...</a></li>

</ul>
</details>

**标签**: `#Agent Evaluation`, `#LLM Agents`, `#AI Engineering`, `#Testing`, `#Meituan`

---

<a id="item-10"></a>
## [MineExplorer 基准揭示多模态大模型被忽视的能力断层](https://tech.meituan.com/2026/07/24/LongCat-MineExplorer.html) ⭐️ 8.0/10

美团 LongCat 团队发布了 MineExplorer，这是首个在 Minecraft 开放世界中评测分钟级长程任务、并包含隐藏前置条件的基准。该基准系统性地揭示了顶级多模态大模型在长程规划和隐式条件发现方面的能力断层。 其重要性在于，多数 AI 评测聚焦于短时、明确指定的任务，而现实部署需要模型在不可预测环境中保持长期自主性。MineExplorer 通过揭示顶级多模态大模型的短板，为提升智能体的鲁棒性和长程推理能力指明了改进方向。 该基准采用复合任务合成和基于里程碑的评测方式，要求智能体自行发现隐藏前置条件，而非获得完整指令。其评测目标是分钟级任务时长，这一时间尺度在以往的开放世界基准中基本缺失。

rss · 美团 Blog · 8月31日 21:23

**背景**: Minecraft 是一款流行的沙盒游戏，因其拥有丰富的开放环境和复杂的合成系统，常被用作 AI 智能体的测试平台。长程任务要求智能体在多步操作中持续追踪目标，同时根据新信息调整策略，其难度远超单次问答。隐藏前置条件意味着许多必要动作或物品并未明确说明，智能体必须通过推理或探索才能成功。该基准契合了近年来评测 AI 系统可完成任务时长的研究趋势，这一指标近年来呈指数级提升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://benchmarklist.com/benchmarks/mineexplorer/">MineExplorer Benchmark Scores & AI Model... | BenchmarkList</a></li>
<li><a href="https://www.emergentmind.com/topics/mineexplorer-benchmark">MineExplorer Benchmark Overview</a></li>
<li><a href="https://huggingface.co/papers/2605.30931">Paper page - MineExplorer : Evaluating Open-World Exploration of...</a></li>

</ul>
</details>

**标签**: `#benchmark`, `#multimodal LLM`, `#open-world`, `#evaluation`, `#agents`

---

<a id="item-11"></a>
## [美团正式开源 LongCat-2.0：面向 Agentic Coding 的 1.6T MoE 模型](https://tech.meituan.com/2026/07/12/LongCat-2.0-Open-source.html) ⭐️ 8.0/10

美团正式开源了 LongCat-2.0，这是一个总参数达 1.6T 的混合专家（MoE）模型，平均激活参数约 48B，专为真实的 Agentic Coding 任务设计。此次发布还同步开放了面向国产 GPU 的推理代码，使其成为首个在五万张国产卡集群上完成全流程训练与推理的万亿参数模型。 这是首个在国产 GPU 集群上完成全流程训练与推理的万亿参数开源 MoE 模型，对国内 Agentic Coding 的研究与部署意义重大。其架构创新——LongCat 稀疏注意力与 N-gram Embedding——提升了长上下文处理与 Token 级表示效率，有望推动代码智能体的进一步发展。 该模型从零开始预训练，原生支持 1M 超长上下文，动态激活参数范围在 33B 到 56B 之间。开源的推理代码针对国产 GPU 优化，LongCat 稀疏注意力通过流式感知索引、跨层索引和分层索引来降低内存与索引开销。

rss · 美团 Blog · 8月31日 21:23

**背景**: 混合专家（MoE）模型每次只激活部分参数，从而在不显著增加计算成本的前提下扩大模型容量。Agentic Coding 指的是 AI 智能体自主规划并执行代码生成、调试、测试等软件开发任务。LongCat 稀疏注意力将稀疏注意力技术扩展到超长上下文，而 N-gram Embedding 则通过捕捉多词组合模式来增强 Token 级表示能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.01662">[2608.01662] LongCat Sparse Attention: Taming the Lightning ...</a></li>
<li><a href="https://deepwiki.com/meituan-longcat/LongCat-2.0/2.2-longcat-sparse-attention-(lsa)">LongCat Sparse Attention (LSA) | meituan-longcat/LongCat-2.0 ...</a></li>
<li><a href="https://arxiv.org/pdf/2601.21204">Scaling Embeddings Outperforms Scaling Experts in Language Models</a></li>

</ul>
</details>

**标签**: `#AI`, `#Open Source`, `#MoE`, `#Agentic Coding`, `#Sparse Attention`

---

<a id="item-12"></a>
## [概率依赖图融合 LLM 与贝叶斯网络，改进因果发现](https://arxiv.org/abs/2608.27472) ⭐️ 8.0/10

该论文提出概率依赖图（PDG），将每条边的状态（有向、无向、不存在）用概率分布表示，从而加权融合贝叶斯网络结构学习（BNSL）与 LLM 的因果知识。在 26 个基准网络上的实验表明，简单的 50/50 融合在 22/26 个网络上超越了任一单一来源的 F1，平均提升 0.056（p<0.001）。 这是混合 AI 方向上的重要一步，表明不完美的 LLM 先验知识与经典因果发现方法可以系统性地结合，而非仅作为黑盒预言机。PDG 表示直接回应了 BNSL 中长期存在的方向可识别性问题，其互补性分析也为构建更准确的因果模型提供了实用指导。 研究使用了三种 BNSL 算法（FGES、Tabu、PC）和三种 LLM（Gemini、Claude、GPT），并跨多个提示词和随机种子进行测试。结果显示，BNSL 提供了高召回率的边骨架（80%对 60%），而 LLM 提供了更高的方向准确率（96%对 77%），印证了两类来源的互补性。

rss · arXiv cs.AI · 8月31日 04:00

**背景**: 因果发现旨在从观测数据中推断因果关系，通常通过贝叶斯网络结构学习（BNSL）实现，即学习一个编码条件独立性的有向无环图。然而，BNSL 往往无法区分蕴含相同独立性的等价图，这个问题称为方向（或马尔可夫等价类）可识别性。概率依赖图（PDG）此前被提出为一类灵活的定向图模型，可以表示不确定或不一致的信念；本文将其思想改造为表示因果图中边层面的不确定性。LLM 也已被用作因果知识的来源，但其输出往往有噪声或不够完整，因此与数据驱动方法融合颇具吸引力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2012.10800">[2012.10800] Probabilistic Dependency Graphs</a></li>
<li><a href="https://www.ccd.pitt.edu/pdfs/fgesc.pdf">Fast Greedy Search ( FGES ) Algorithm for Continuous Variables</a></li>
<li><a href="https://www.tandfonline.com/doi/full/10.1080/08839514.2018.1526760">Full article: Bayesian Network Learning with the PC Algorithm: An Improved and Correct Variation</a></li>

</ul>
</details>

**标签**: `#causal discovery`, `#LLM`, `#Bayesian networks`, `#structure learning`, `#probabilistic graphs`

---

<a id="item-13"></a>
## [WM-R1：通过强化学习和世界模型训练移动 GUI 智能体](https://arxiv.org/abs/2608.27508) ⭐️ 8.0/10

WM-R1 是首个使用世界模型而非真实 Android 环境来训练移动 GUI 智能体的强化学习框架。它用基于世界模型的状态转换替代真实环境交互，并将世界模型直接嵌入智能体的推理过程。 该方法显著降低了 GUI 智能体在真实环境中进行强化学习训练的高资源消耗和不稳定性。它支持大规模并行和步骤级轨迹生成，有望加速移动 GUI 自动化和基于模型的强化学习研究。 WM-R1 使用多维规则奖励，联合优化任务成功率、轨迹效率和世界模型利用率。该框架在精心整理的 2000 个挑战性任务数据集上训练，在 Android 基准测试中优于仅使用 GRPO 的基线和推理时模拟方法。

rss · arXiv cs.AI · 8月31日 04:00

**背景**: 针对 GUI 智能体的强化学习通常需要大量真实环境交互，成本高且不稳定。世界模型是环境的预测模型，能够模拟状态转换，使基于模型的强化学习无需真实交互即可询问“如果我执行 x 会发生什么”。此前的工作如 UI-R1 探索了用于 GUI 动作预测的基于规则的强化学习，但 WM-R1 是首个在训练过程中完全用世界模型替代真实环境的框架。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.27508v1">WM-R1: Training GUI Agents to Reason and leverage World ...</a></li>
<li><a href="https://arxiv.org/abs/2503.21620">[2503.21620] UI-R1: Enhancing Efficient Action Prediction of ... GitHub - AgentR1/Agent-R1: Agent-R1: Training Powerful LLM ... [2504.10458] GUI-R1 : A Generalist R1-Style Vision-Language ... UI-R1: Enhancing Action Prediction of GUI Agents by - arXiv.org</a></li>
<li><a href="https://bair.berkeley.edu/blog/2019/12/12/mbpo/">Model -Based Reinforcement Learning : Theory and Practice</a></li>

</ul>
</details>

**标签**: `#reinforcement learning`, `#world models`, `#GUI agents`, `#mobile`, `#AI research`

---

<a id="item-14"></a>
## [LongGuard 揭示长上下文安全护栏失效机制并提供免训练缓解方案。](https://arxiv.org/abs/2608.27580) ⭐️ 8.0/10

该论文提出 LongGuard 框架，引入覆盖 0.25k 至 32k 长度网格的 SafetyNIAH 基准，并发现 15 个主流安全护栏的平均不安全召回率随上下文变长而下降超过 50%。论文还定位了注意力→logit→行为的机制链条，并提出两种免训练缓解方法——分块检测（CD）与注意力头锐化（AHS）——以及名为 CAHR 的部署协议。 这很重要，因为安全护栏是 LLM 抵御有害输入和输出的最后防线，但它们通常仅在短文本上训练和评估，在真实世界的长上下文部署中留下了关键安全缺口。缓解方法是免训练的，因此无需昂贵的微调即可立即应用；而机制层面的洞察可为更稳健的护栏设计提供指导。 研究通过 Benign-Fill 与 Needle-Repeat 的配对设计，将失效归因于不安全“针”被按比例稀释，而非绝对长度本身。在涵盖合成数据、长上下文攻击和推理模型输出的五个基准上，CAHR-CD 与 CAHR-AHS 配置分别将六个护栏的平均效果提升 22%和 13%。

rss · arXiv cs.AI · 8月31日 04:00

**背景**: 安全护栏是用于筛查 LLM 输入和输出中有害内容的分类器或模型。针-草垛（NIAH）测试原本用于评估长上下文检索能力，衡量模型能否在冗长无关上下文中找到一小条信息（“针”）；该工作将其改造为 SafetyNIAH，用来检验护栏能否检测被良性文本包围的不安全片段。注意力稀释指随着上下文变长，模型有限的注意力被摊薄，位于长文本中间的重要细节获得的注意力减少，甚至被忽略。本文正是利用这些概念对护栏失效进行机制归因并提出缓解方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.27580">LongGuard: Mechanistic Analysis and Training-Free Mitigation of Long-Context Failure in Safety Guardrails</a></li>
<li><a href="https://github.com/czyPL/LongGuard">Mechanistic analysis and training-free mitigation of long ...</a></li>
<li><a href="https://levelup.gitconnected.com/long-context-attention-dilution-why-more-isnt-always-better-c4b274509dee">Long Context Attention Dilution : Why More... | Level Up Coding</a></li>

</ul>
</details>

**标签**: `#LLM safety`, `#long-context`, `#guardrails`, `#mechanistic interpretability`, `#benchmark`

---

<a id="item-15"></a>
## [带外策略执行：在可信边界约束 AI 代理越权](https://arxiv.org/abs/2608.27646) ⭐️ 8.0/10

该论文提出了带外策略执行（OBPE），一种位于代理推理之外的受信任策略边界，用于授权操作、收窄查询并过滤响应。在涉及四个模型的 3,621 次基准测试中，OBPE 将追踪失败率从 57.6%降至 0.2%，同时将安全有效完成率提升了 21.8 个百分点。 这很重要，因为携带凭据的 AI 代理可能继承人类的访问权限，却缺乏安全使用该权限的判断力，使基于提示词的防护措施不够充分。OBPE 提供了一个可验证、与顺序无关的治理层，可在真实企业系统中保护敏感数据。 OBPE 的类型化 Cedar 策略核心包含在带一致性测试的 HTTP 代理原型中，论文在给定条件下证明了顺序无关性和上限不扩大性。评估不包括写入控制、持久审批以及时间/聚合策略，并指出塑造单次执行并非无干扰。

rss · arXiv cs.AI · 8月31日 04:00

**背景**: 带外执行是指在模型提示词、对话状态或代理记忆之外进行策略决策和控制操作，通常通过网关、代理或策略引擎实现。在代理系统中，这种边界会在操作到达模型之前或模型输出执行之前对其进行评估，从而应对检索数据中的隐藏指令可能操纵代理的风险。该论文将此概念应用于类型化操作和资源授权，在后端调用前收窄查询，并过滤或掩盖响应。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nhimg.org/glossary/out-of-band-enforcement/">What Is Out-of-Band Enforcement? Definition & Examples</a></li>
<li><a href="https://patents.justia.com/patent/20260093587">U.S. Patent Application for OUT-OF-BAND POLICY ENFORCEMENT ...</a></li>
<li><a href="https://medium.com/codex/agentcore-the-definitive-strategic-framework-for-ai-agent-cost-optimization-2fcbae65ef01">AgentCore: The Definitive Strategic Framework for AI Agent ... | Medium</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#policy enforcement`, `#AI agents`, `#governance`, `#security`

---

<a id="item-16"></a>
## [用吉布斯采样与生成控制探查多模态大模型的感知先验](https://arxiv.org/abs/2608.27727) ⭐️ 8.0/10

这篇论文提出一种方法，通过沿可控轴引导生成模型，并以多模态大语言模型（MLLM）作为评判者运行吉布斯采样，从而直接对模型的感知先验进行采样。该方法既能恢复典型的偏见，也能揭示仅靠直接提示无法暴露的新颖先验。 理解感知先验至关重要，因为模型行为同时取决于它接收到的输入和它内隐持有的预期，然而这些先验至今仍未被充分理解。该方法为可解释性研究开辟了新方向，并可能改进对现实世界中多模态大语言模型行为的审计，例如人脸可信度或艺术图像廉价感判断中的偏见。 该方法将可解释的生成控制与吉布斯采样相结合，使用目标多模态大语言模型作为评判者，沿着指定的轴对生成的刺激进行评分，例如人脸的可信度和艺术图像的廉价感。该方法面向视觉语言模型所面对的高维真实世界输入空间而设计。

rss · arXiv cs.AI · 8月31日 04:00

**背景**: 感知先验是指模型对可能遇到的刺激分布所持有的内隐期望，这不同于其内部表征能够编码的内容。传统的可解释性方法要么分析输入，要么分析内部结构，但从未直接重建先验分布本身。既有研究表明，语言模型在预训练过程中会获得视觉先验，而这项工作在此基础上，利用生成模型直接激发并采样这些先验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2509.26625">Learning to See Before Seeing: Demystifying LLM Visual Priors ...</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S105381001630277X">Priors in perception: Top-down modulation, Bayesian ...</a></li>

</ul>
</details>

**标签**: `#interpretability`, `#multimodal LLMs`, `#perceptual priors`, `#Gibbs sampling`, `#generative controls`

---

<a id="item-17"></a>
## [Credo：为智能体工作流恢复可复用的声明式原语](https://arxiv.org/abs/2608.27790) ⭐️ 8.0/10

论文提出了 Credo 框架，它从编码智能体为 LLM 应用搜索得到的不透明命令式 harness（执行框架）中恢复出结构化的声明式描述。Credo 为每个抽取出的原语标记元数据，并带有来源信息进行编目，随后用编译器将存储的原语绑定生成新的 harness，而无需从头重新搜索。 这件事很重要，因为搜索得到的 harness 中蕴含着关于逻辑步骤、运行时信号和提示词策略的宝贵经验，但目前这些经验都埋藏在特定于任务的命令式代码里，无法复用。通过让这些隐性知识可检视、可复用，Credo 有望大幅降低构建和迭代 LLM 应用的成本，并开启数据库社区非常适合推进的研究议程。 论文只给出了初步结果来证明该方法潜力，尚未进行完整评估。它提出的研究议程包括：基于声明式目录进行代价驱动的编译，以及在模型和负载漂移情况下维护目录。

rss · arXiv cs.AI · 8月31日 04:00

**背景**: Agent harness（又称 agent scaffolding，智能体脚手架）是围绕 LLM 的软件基础设施，负责处理除模型本身之外的一切，例如决定每次调用能看到什么、该信任哪些答案。在智能体工作流中，系统是非确定性的，每次运行可能因输入、工具选择、决策和错误处理而得到不同结果。Credo 关注的是编码智能体通过搜索候选程序发现的 harness；与手写的声明式规范不同，这些搜索得到的程序是命令式且不透明的。声明式原语是可复用的构建块，描述系统应该做什么而非怎么做，论文认为从搜索得到的 harness 中恢复这种结构能够实现复用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Agent_harness">Agent harness - Wikipedia</a></li>
<li><a href="https://www.langchain.com/blog/the-anatomy-of-an-agent-harness">The Anatomy of an Agent Harness - langchain.com</a></li>
<li><a href="https://mastra.ai/articles/agentic-workflows">Agentic workflows: how they work, key components, and how to ...</a></li>

</ul>
</details>

**标签**: `#agentic workflows`, `#LLM applications`, `#declarative programming`, `#reusability`, `#arxiv`

---

<a id="item-18"></a>
## [RealSWE：面向真实用户请求的编码智能体组合式基准](https://arxiv.org/abs/2608.27831) ⭐️ 8.0/10

本文介绍了 RealSWE，一个包含 381 个多变体任务族的组合式基准，这些任务族源自 SWE-bench Verified 和 Pro，变体之间仅在信息组成和语言风格上有所不同。对七个当代 LLM 的评估显示，真实风格的输入平均使解决率下降 6.4 个百分点，并可能改变模型排名。 RealSWE 揭示了编码智能体评估中的一个关键差距：SWE-bench 等基准依赖较长、结构化、正式的 issue，而真实用户请求通常简短、随意且仅含问题陈述。它提供了可操作的建议，表明明确表述期望行为和动机能显著提升 LLM 的软件工程性能，而环境信息和复现步骤的增益很小。 RealSWE 中的每个任务族共享相同的底层任务和黄金补丁，变体仅在信息组成和语言风格上有所不同。受控分析发现，包含期望行为和动机显著影响性能，而环境信息和复现步骤只是增加 token，没有可测量的收益；语言风格的影响较小且因模型而异。

rss · arXiv cs.AI · 8月31日 04:00

**背景**: SWE-bench 是评估编码智能体常用的基准系列，其任务来自精心整理的 GitHub issue，通常较长、结构化且信息丰富。然而，真实用户请求（例如从 SWE-chat 收集的请求）往往更短、结构更松散，很大一部分只包含问题陈述。RealSWE 使用六类信息分类法和四个语言风格维度形式化地刻画了这一差距，并构建了一个基准来衡量这些差异如何影响智能体的性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.swebench.com/">SWE - bench Leaderboards</a></li>
<li><a href="https://arxiv.org/abs/2207.04136">[2207.04136] CompoSuite: A Compositional Reinforcement ... [2605.08988] Benchmarking Compositional Generalisation for ... CompoSuite: A Compositional Reinforcement Learning Benchmark GitHub - Lifelong-ML/CompoSuite: Official release of ... ComPABench: Multi-Domain ML Benchmarks Compositional Reasoning Benchmarks - emergentmind.com Benchmarking and Understanding Compositional Relational ...</a></li>

</ul>
</details>

**标签**: `#coding agents`, `#benchmark`, `#evaluation`, `#SWE-bench`, `#LLM agents`

---

<a id="item-19"></a>
## [以博弈论视角综述 AI 对齐研究](https://arxiv.org/abs/2608.27910) ⭐️ 8.0/10

一篇新的 arXiv 综述（编号 2608.27910）以博弈论视角审视 AI 对齐，围绕三个挑战组织近期工作：偏好多样性、对齐优先级和时间动态。该综述综合了多智能体对齐的文献，并指出博弈论分析真正有用的地方。 该综述为研究人员提供了博弈论与 AI 对齐这一有前景交叉领域的结构化地图，既阐明了优势，也指出了未解决的问题。它有助于引导未来在高风险环境中构建稳健、自适应且可验证 AI 系统的研究。 该综述围绕博弈论要素组织研究进展，并按偏好多样性、对齐优先级和时间动态综合文献。它还指出博弈论框架较松散的地方以及尚存的挑战。

rss · arXiv cs.AI · 8月31日 04:00

**背景**: AI 对齐旨在引导 AI 系统朝向人类的目标、偏好或伦理原则，但现有方法往往难以处理依赖情境且非传递的偏好。博弈论研究多个智能体之间的策略互动，为建模动态多方偏好提供了工具。该综述探讨了如何将这些工具应用于对齐问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_alignment">AI alignment</a></li>

</ul>
</details>

**标签**: `#AI alignment`, `#game theory`, `#survey`, `#LLM`, `#AI safety`

---

<a id="item-20"></a>
## [跨会话分解攻击的形式化分析及意图对齐检索防御](https://arxiv.org/abs/2608.27945) ⭐️ 8.0/10

该论文提出了“组合安全风险”（compositional safety risk）的概念，并证明了跨会话分解攻击的条件风险转移界：部署组合风险与参考组合风险之间的差距受模型在允许子查询上的额外损失控制。论文还提出了 22M 参数的 IntentAlign-MiniLM 检索器，在意图检索和有害召回率上优于更大的嵌入模型。 这项研究意义重大，因为它将缩放定律与安全直接联系起来：更大、能力更强的 LLM 可能更容易将看似良性的查询组合成被禁止的目标。轻量级的基于检索的防御提供了一种实用的防护栏，其表现优于大得多的嵌入模型，有望显著改善真实场景中的 LLM 安全部署。 通过合成保留实验，论文表明更宽的 Transformer 会对训练中从未逐字出现、但可从注入的支持事实中恢复的保留指令分配更低的损失。在 Qwen3 和 Gemma3 系列上的 600 意图评估显示，在固定的分解-组合流程下，更大的模型成员可能带来更高的有害能力提升；代码已在 GitHub 上公开。

rss · arXiv cs.AI · 8月31日 04:00

**背景**: 跨会话分解攻击将恶意目标拆分为多个看似良性的子查询，并在不同、独立的交互会话中分别提出，因此单个会话看起来并无危害；之后再将子查询重新组合以实现被禁止的目标。缩放定律通常描述更低的语言建模损失如何带来更有能力的模型，而本文考察了该机制的一个安全后果。组合安全风险将这种重组子查询产生有害结果的可能性形式化。所提出的防御方法 IntentAlign-MiniLM 是一个 22M 参数的意图对齐检索器，在查询到达模型前过滤或检索可能有危害的查询。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.27945">[2608.27945] Cross-Session Decomposition Attacks: Scaling ...</a></li>
<li><a href="https://github.com/liaodisen/Cross-Session-Decomposition-Attacks">GitHub - liaodisen/Cross-Session-Decomposition-Attacks ...</a></li>
<li><a href="https://arxiv.org/abs/2605.11029">[2605.11029] FragBench: Cross-Session Attacks Hidden in ... GitHub - liaodisen/Cross-Session-Decomposition-Attacks ... Validating Cross-Session Goal Decomposition Attacks and ... Context-Fractured Decomposition Attacks on Tool-Using Agents FragBench: Cross-Session Attacks Hidden in Benign-Looking ... Split the Request, Smuggle the Payload: How "Context ...</a></li>

</ul>
</details>

**标签**: `#LLM safety`, `#scaling laws`, `#adversarial attacks`, `#language models`, `#security`

---

<a id="item-21"></a>
## [WhatIfBench 与 PRISM 揭示 LLM 反事实推理的脆弱性](https://arxiv.org/abs/2608.27953) ⭐️ 8.0/10

该论文提出了 WhatIfBench，一个包含 220 个跨 STEM、HSS 和 Hybrid 场景的开放域“what-if”问题基准，以及 PRISM——一种将自由文本回答转换为语义因果图并加以评估的基于图的方法。将该框架应用于六个前沿 LLM 时，即使最强模型也仅获得 64.62% 的分数，说明该基准远未饱和。 该工作聚焦于开放域反事实推理这一 LLM 尚未被充分探索的能力，并提供了公开的基准资源用于诊断该能力。研究结果表明，LLM 生成流畅的反事实叙述往往掩盖了脆弱的因果过程，促使社区反思如何衡量推理质量。 PRISM 首先将每个解释构建为响应派生语义因果图（Response-Derived Semantic Causal Graph），然后应用过程指标评估图级因果有效性，应用评分指标评估答案级解释充分性。分析发现 LLM 回答中持续的因果缺口、前提漂移和拓扑碎片化问题，基准、代码和评估脚本已在 GitHub 上发布。

rss · arXiv cs.AI · 8月31日 04:00

**背景**: 反事实推理要求模型回答“如果初始条件发生了变化，结果会怎样”，并在开放式情景中推演后续影响。现有的这类能力基准大多采用固定变量或单一标准答案的受限设置，难以代表现实中的开放域场景。因果图是一种用于编码因果关系假设的工具，PRISM 借助该工具将模型生成的因果链与问题所预期的推理过程进行比较。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/zju-gt/WhatIfBench">GitHub - zju-gt/WhatIfBench: Code of "The Illusion of What If ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Causal_graph">Causal graph - Wikipedia</a></li>

</ul>
</details>

**标签**: `#LLM`, `#counterfactual reasoning`, `#benchmark`, `#evaluation`, `#causal reasoning`

---

<a id="item-22"></a>
## [RA-OPD：用奖励对齐的在线蒸馏纠正教师的误导性指导](https://arxiv.org/abs/2608.27960) ⭐️ 8.0/10

该论文提出“奖励对齐的在线蒸馏”（RA-OPD），在在线蒸馏过程中过滤掉那些蒸馏更新与结果奖励不一致的轨迹。使用 Qwen3 和 DeepSeek-R1 系列模型在数学和代码基准上的评估显示，RA-OPD 显著优于标准 OPD 及其他测试变体。 这解决了 LLM 后训练中的一个关键弱点：教师模型可能引导学生走向错误结果，而目标却是最大化奖励。通过让在线蒸馏与奖励对齐，RA-OPD 可以在不增加额外计算成本的情况下提高蒸馏模型的可靠性和性能，惠及对齐与知识迁移研究。 RA-OPD 会检查每条采样轨迹的轨迹级蒸馏回报是否与其结果奖励一致，并丢弃不一致的轨迹。该方法不需要额外计算成本，并使用 Qwen3 和 DeepSeek-R1 系列模型在七个数学基准和三个代码基准上进行了测试。

rss · arXiv cs.AI · 8月31日 04:00

**背景**: 在线蒸馏（OPD）是一种后训练范式，学生 LLM 通过模仿教师对学生自己生成输出的指导来学习，常用于将大模型的能力迁移到小模型。在标准流程中，教师指导可能与实际结果奖励（如正确性）不一致，从而误导优化。RA-OPD 借鉴 RLHF 式的奖励信号，结合轨迹过滤，只保留能让学生朝更高奖励移动的更新。这与强化学习中关于奖励模型和对齐的广泛研究相关联。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2604.00626">A Survey of On - Policy Distillation for Large Language Models</a></li>
<li><a href="https://arxiv.org/html/2409.19024">Elephant in the Room: Unveiling the Impact of Reward Model Quality...</a></li>
<li><a href="https://www.linkedin.com/pulse/on-policy-distillation-vs-reinforcement-learning-florent-liu-tc9ne">On - Policy Distillation vs. Reinforcement Learning</a></li>

</ul>
</details>

**标签**: `#LLM`, `#distillation`, `#alignment`, `#reinforcement learning`, `#post-training`

---

<a id="item-23"></a>
## [AERA：可学习控制器高效分配测试时计算资源](https://arxiv.org/abs/2608.27964) ⭐️ 8.0/10

AERA 是一种新的序列控制器，通过学习额外计算是否能恢复更优答案来自适应分配大语言模型推理的测试时计算，而非依赖置信度或一致性。在 300 道 GSM8K 问题的冻结阈值评估中，AERA 达到 92.61%的准确率（对比 128 个回答时的 93.01%），同时减少了 95.99%的完成 token。 该工作挑战了自适应停止方法中普遍存在的假设——即当前证据越强意味着不需要继续计算，为测试时扩展提供了一种更通用且高效的思路。它可以在保持准确率的同时降低推理模型的推理成本，惠及研究者和部署大语言模型的从业人员。 AERA 使用答案分布、时间、重新求解、语义和计算特征来刻画累积响应前缀，并反复决定是停止还是分配下一个响应块。未来的检查点正确性仅用于构建离线监督，推理时完全不可用。该方法在 GSM8K 和 GPQA Diamond 上进行了评估。

rss · arXiv cs.AI · 8月31日 04:00

**背景**: 测试时扩展通过生成更多候选解来提升语言模型的推理能力，但对每个问题分配相同的推理预算在计算上是浪费的。现有的自适应停止方法通常依赖置信度、一致性或答案稳定性，隐含假设当前证据越强就说明无需继续计算。AERA 转而学习估计额外计算的未来价值，从而处理检查点级正确性非单调变化的情况。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.27964v1">AERA: Adaptive Evidence Residual Allocation for Efficient ...</a></li>
<li><a href="https://arxiv.org/abs/2408.03314">[2408.03314] Scaling LLM Test - Time Compute Optimally can be More...</a></li>
<li><a href="https://arxiv.org/abs/2604.01413">[2604.01413] Adaptive Stopping for Multi-Turn LLM Reasoning Adaptive Stopping for Multi-Turn LLM Reasoning - arXiv.org Adaptive Stopping for Multi-Turn LLM Reasoning - ADS Adaptive Stopping for Multi-Turn LLM Reasoning | AI Strides Adaptive Stopping for Multi-Turn LLM Reasoning - Adaptive Stopping for Multi-Turn LLM Reasoning | Arxiv ... Adaptive Stopping for Multi-Turn LLM Reasoning</a></li>

</ul>
</details>

**标签**: `#LLM reasoning`, `#test-time compute`, `#adaptive stopping`, `#efficiency`, `#arXiv`

---

<a id="item-24"></a>
## [量化触发的大模型后门：利用验证-部署间隙发起攻击](https://arxiv.org/abs/2608.27512) ⭐️ 8.0/10

本文提出了语言模型中的量化触发后门，将后训练量化造成的“验证-部署间隙”形式化。作者通过三阶段对抗微调框架植入恶意载荷，使其通过全精度校验，却在 INT8 或 4-bit 压缩后激活恶意行为。 这项研究揭示了 LLM 部署流程中的一个新攻击面：仅靠源精度认证无法保证量化后的模型行为安全。它对边缘 AI 以及所有使用量化模型的安全敏感型应用都很重要，说明行为认证必须覆盖最终部署形态。 该攻击可跨不同量化方案和模型架构持续存在，因此仅凭标称位宽无法判断风险。研究还将其从仅解码器因果语言模型扩展到多语言编码器-解码器序列到序列模型，在翻译任务上实现最高 85.02% 的翻转，并使立场分类器的意识形态偏移达到 ΔBias=0.33。

rss · arXiv cs.CR · 8月31日 04:00

**背景**: 后训练量化是一种常见优化，将模型权重从高精度（如 FP16）压缩到低精度（如 INT8 或 4-bit），以减少内存占用并支持边缘部署。由于量化是参数空间上的多对一映射，不同的全精度模型在压缩后可能变得相同，但行为却不一定等同。该论文通过量化行为等价类（QBEC）形式化了这一问题，并证明 QBEC 成员关系并不蕴含行为等价，从而为量化触发后门提供了理论基础。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.27512">[2608.27512] Quantization - Triggered Backdoors in Language ...</a></li>
<li><a href="https://arxiv.org/pdf/2608.27512">Quantization -Triggered Backdoors in Language Models...</a></li>
<li><a href="https://cctest.ai/en/articles/quantization-may-activate-hidden-backdoors-in-language-models">How Quantization Can Activate LLM Backdoors - CCTest</a></li>

</ul>
</details>

**标签**: `#LLM Security`, `#Backdoor Attacks`, `#Quantization`, `#AI Safety`, `#Model Deployment`

---

<a id="item-25"></a>
## [DAMP：面向循环状态的衰减感知混合精度量化](https://arxiv.org/abs/2608.27513) ⭐️ 8.0/10

论文提出了 DAMP，这是首个针对 Gated DeltaNet（GDN）和 Kimi Delta Attention（KDA）语言模型循环状态的后训练量化方法。在 Qwen3.6-35B 和 Kimi-Linear-48B 上的评估显示，DAMP 在每状态值 9.9 比特下保持了接近 FP32 基线的准确率。 GDN/KDA 模型中的循环状态占用大量显存且受内存带宽限制，成为关键效率瓶颈。DAMP 的混合精度方法在不牺牲准确率的情况下降低了存储和延迟，有助于高效长上下文语言模型的实际部署。 作者发现均匀量化对循环状态效果不佳：INT8/FP8 会降低推理准确率，而 INT4/NVFP4 几乎使其降为零。DAMP 通过量化误差能量和基于衰减的持久性识别高风险通道，以较高精度存储这些通道，其余用 INT8，实现了 69.1%的存储缩减、最高 2.01 倍的核加速和最高 10.9%的 TPOT 下降。

rss · arXiv cs.LG · 8月31日 04:00

**背景**: 传统 softmax 注意力需要为每个历史 token 存储键值向量，导致内存随序列长度增长。GDN 和 KDA 用固定大小的循环状态替换大部分层中的 KV 缓存，但这些状态以 FP32 存储，解码时受内存带宽限制。后训练量化无需重训练即可减小模型规模和内存流量；DAMP 利用量化误差集中在少量通道、且通道衰减强度在不同提示间保持稳定这一发现，将这一思路应用于循环状态。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2412.06464">[2412.06464] Gated Delta Networks: Improving Mamba2 with Delta Rule</a></li>
<li><a href="https://arxiv.org/abs/2510.26692">[2510.26692] Kimi Linear: An Expressive, Efficient Attention ... Linear Attention: Kimi Delta Attention | Jianyu Huang GitHub - MoonshotAI/Kimi-Linear What is Kimi Delta Attention (KDA) in Kimi K3? - Medium Behind Kimi K3: Understanding Kimi Delta Attention (KDA)</a></li>

</ul>
</details>

**标签**: `#quantization`, `#efficient inference`, `#large language models`, `#mixed-precision`, `#recurrent states`

---