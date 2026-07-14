---
layout: default
title: "Horizon Summary: 2026-07-14 (ZH)"
date: 2026-07-14
lang: zh
---

> 从 452 条内容中筛选出 25 条重要资讯。

---

1. [美团 LongCat-2.0：国产算力上的万亿参数模型](#item-1) ⭐️ 9.0/10
2. [面向代理型 AI 的最小自主性新理论](#item-2) ⭐️ 9.0/10
3. [SPARK：基于隐藏态敏感性的 LLM 推理引导方法](#item-3) ⭐️ 9.0/10
4. [间接数据投毒可工业化科学欺诈](#item-4) ⭐️ 9.0/10
5. [如何阻止 Claude 过度使用“load-bearing”](#item-5) ⭐️ 8.0/10
6. [在非英伟达硬件上运行 CUDA 的替代方案](#item-6) ⭐️ 8.0/10
7. [Anthropic 投资 1000 万美元支持加拿大 AI 安全研究](#item-7) ⭐️ 8.0/10
8. [Anthropic 研究 Claude 模型跨语言的价值对齐](#item-8) ⭐️ 8.0/10
9. [利用 BPF 屏蔽运行中内核漏洞](#item-9) ⭐️ 8.0/10
10. [微软在 SymCrypt 中验证 Rust 密码学实现](#item-10) ⭐️ 8.0/10
11. [NVIDIA 使用 AI 智能体在一天内后训练 Cosmos 3](#item-11) ⭐️ 8.0/10
12. [NVIDIA Ising 解码器将颜色码错误率降低 300 倍以上](#item-12) ⭐️ 8.0/10
13. [美团开源 VitaBench 2.0：长期智能体基准评测](#item-13) ⭐️ 8.0/10
14. [格式敏感度指数：提示包装器对 LLM 基准测试的影响](#item-14) ⭐️ 8.0/10
15. [动力系统分析解读潜在链式思考推理](#item-15) ⭐️ 8.0/10
16. [YUKTI：从自然语言到稳健可验证的决策](#item-16) ⭐️ 8.0/10
17. [执行门控自蒸馏提升游戏代码生成效果](#item-17) ⭐️ 8.0/10
18. [利用子模函数为 LLM 基准测试选择核心集](#item-18) ⭐️ 8.0/10
19. [信念复制：为智能代理系统而设计](#item-19) ⭐️ 8.0/10
20. [BatteryLake：基于智能体与物理规律的电池老化数据整理框架](#item-20) ⭐️ 8.0/10
21. [AI 代理的规范执行：提出稳健机制](#item-21) ⭐️ 8.0/10
22. [有限规则修正验证自适应代理 AI](#item-22) ⭐️ 8.0/10
23. [EvoCUA-1.5：多轮计算机使用代理在线强化学习](#item-23) ⭐️ 8.0/10
24. [长度惩罚隐藏链式思维中的偏见提示](#item-24) ⭐️ 8.0/10
25. [LLM 无法获取规范致上下文学习失败](#item-25) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [美团 LongCat-2.0：国产算力上的万亿参数模型](https://tech.meituan.com/2026/06/30/LongCat2.0.html) ⭐️ 9.0/10

美团发布了 LongCat-2.0，这是首个在五万卡国产算力集群上完成全流程训练与推理的万亿参数模型（总参数 1.6T，平均激活约 48B），原生支持 1M 超长上下文，专为智能体编码任务设计。 这一成就标志着 AI 自主可控的重要进展，证明了国产算力集群能够规模化训练万亿参数模型。同时，它推动了长上下文智能体编码的前沿，有望实现更自主、高效的软件开发。 LongCat-2.0 引入了 LongCat 稀疏注意力（LSA）实现线性复杂度的长上下文处理，以及 N-gram 嵌入增强 token 级表示。其动态激活范围每 token 为 33B 至 56B 参数，并在 SWE-bench Pro 上取得了 59.5%的领先成绩。

rss · 美团 Blog · 7月14日 17:17

**背景**: 万亿参数大语言模型通常需要数千块 NVIDIA H100 等高端 GPU，引发供应链依赖担忧。美团的 LongCat-2.0 完全在国产 GPU（可能来自华为或同类厂商）上训练，展现了中国追求 AI 自主可控的努力。智能体编码是指 AI 代理能自主规划、编写、测试和修改多步代码，减少人工干预。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepwiki.com/meituan-longcat/LongCat-2.0/2.2-longcat-sparse-attention-(lsa)">LongCat Sparse Attention (LSA) | meituan-longcat/LongCat-2.0 ...</a></li>
<li><a href="https://arxiv.org/abs/2512.23966">Efficient Context Scaling with LongCat ZigZag Attention LongCat AI - LongCat-2.0 Trillion-Parameter Agentic Coding Model LongCat-Video Technical Report - arXiv.org Technology - LSA, ScMoE, DORA, Zero-Computation Experts ... Introducing LongCat-2.0</a></li>
<li><a href="https://scrimba.com/articles/what-is-agentic-coding/">What Is Agentic Coding? A Developer's Guide [2026]</a></li>

</ul>
</details>

**标签**: `#Large Language Models`, `#AI Infrastructure`, `#Agentic Coding`, `#Domestic GPU`, `#Trillion Parameter`

---

<a id="item-2"></a>
## [面向代理型 AI 的最小自主性新理论](https://arxiv.org/abs/2607.09744) ⭐️ 9.0/10

一篇新论文提出了'最小自主性'概念，作为代理型 AI 系统最小权限原则的泛化，定义了组合爆炸半径和代理影响图。 该形式化理论填补了自主 AI 代理访问控制中的基础空白——这些代理能够组合和放大权限，有望提升多代理系统的安全性和编排能力。 关键概念包括：使用超度量树和格值保密性、完整性、控制上下文标签的组合爆炸半径 d(a,b)，以及具有策略阈值 theta 的有向代理影响图 G(theta)。

rss · arXiv cs.CR · 7月14日 04:00

**背景**: 最小权限是访问控制的基石原则，仅授予任务严格所需的权限。但对于能跨工作流自主组合或批准权限的代理型 AI 系统，该原则不够充分。论文形式化'最小自主性'概念，利用超度量树和影响图等数学结构来度量并限制代理能施加的影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/least-autonomy-ai-agents-compositional-model-blast-radius-parisel-qkqge">Least Autonomy for AI Agents: A Compositional Model for Blast ...</a></li>
<li><a href="https://github.com/kevin-biot/blast-radius-framework">GitHub - kevin-biot/blast-radius-framework: A classification ...</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#agentic AI`, `#access control`, `#formal theory`, `#autonomy`

---

<a id="item-3"></a>
## [SPARK：基于隐藏态敏感性的 LLM 推理引导方法](https://arxiv.org/abs/2607.10296) ⭐️ 9.0/10

SPARK 提出了一种方法，利用长度控制的隐藏态敏感性诊断大语言模型的推理失败，并引导轻量级测试时干预，在 GSM8K 和 MATH-500 上使 Qwen3 系列模型的准确率提升高达 3.2 个百分点。 该工作填补了在输出级评估之外理解推理失败的关键空白，提供了一种在不重新训练的情况下在测试时诊断和纠正内部推理状态的实用方法，有望使高 stakes 应用中的 LLM 更加可靠和可解释。 SPARK 使用受控的程序化推理套件 FRONTIER-4.5K 进行剖面分析，并采用长度控制的敏感性将输入尺度效应与残余推理激活分离。在 MATH-500 上，Qwen3-4B 准确率从 82.0%提升至 84.6%，Qwen3-8B 从 82.4%提升至 85.6%。

rss · arXiv cs.AI · 7月14日 04:00

**背景**: 大语言模型常常因内部推理失败而产生错误答案，这种失败仅通过评估最终输出是无法捕获的。LLM 中的隐藏态编码了推理状态，但原始的隐藏态敏感性会受到提示长度的混淆，特别是在算法推理任务中。SPARK 引入了长度控制的敏感性，可靠地检测模型何时进入有效的推理状态，从而在不修改模型参数的情况下实现有针对性的测试时干预。该方法建立在激活引导和隐藏态探测的先前工作之上，但侧重于以有原则的方式诊断和纠正推理失败。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2509.22067v2">The Rogue Scalpel: Activation Steering Compromises LLM Safety</a></li>
<li><a href="https://arxiv.org/abs/2505.16520">[2505.16520] Are the Hidden States Hiding Something? Testing ... Comparing Behavioral and Hidden-State Semantic Geometry in ... Don't let the LLM speak, just probe it. - by James Padolsey Securing Large Language Models: Threats, Vulnerabilities and ...</a></li>
<li><a href="https://arxiv.org/abs/2512.04748">[2512.04748] Model Whisper: Steering Vectors Unlock Large ...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#reasoning`, `#hidden-state analysis`, `#test-time steering`, `#arXiv`

---

<a id="item-4"></a>
## [间接数据投毒可工业化科学欺诈](https://arxiv.org/abs/2607.10712) ⭐️ 9.0/10

一篇新论文提出了间接数据投毒攻击，对手通过破坏开放数据集来操纵自主 AI 研究代理，在多个前沿模型上实现了 49.56%的成功率，而检测率仅为 6.0%。 这种攻击可能在没有直接访问 AI 系统的情况下实现大规模自动化的科学欺诈，随着 AI 代理越来越多地自动化科学发现，研究诚信面临威胁。 该攻击在五个社会敏感话题上使用 Claude Code、Codex 和 Gemini CLI 进行了测试，无需触发词或伪造论文；提出的溯源审计将攻击成功率降至零。

rss · arXiv cs.CR · 7月14日 04:00

**背景**: 数据投毒是一种安全攻击，通过操纵训练数据来危害 AI 模型的行为。自主研究代理是独立执行科学任务（如文献综述和数据分析）的 AI 系统。开放数据集常用于训练这些代理，而这篇论文表明，破坏此类数据集可能误导代理得出欺诈性结论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theregister.com/2026/01/11/industry_insiders_seek_to_poison/">AI insiders seek to poison the data that feeds them • The Register</a></li>
<li><a href="https://www.paloaltonetworks.com/cyberpedia/what-is-data-poisoning">What Is Data Poisoning? [Examples & Prevention] - Palo Alto Networks</a></li>
<li><a href="https://arxiv.org/abs/2508.12752">[2508.12752] Deep Research: A Survey of Autonomous Research Agents</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#data poisoning`, `#scientific fraud`, `#security`, `#research integrity`

---

<a id="item-5"></a>
## [如何阻止 Claude 过度使用“load-bearing”](https://jola.dev/posts/how-to-stop-claude-from-saying-load-bearing) ⭐️ 8.0/10

一位开发者发布了一篇博文和自定义指令，旨在阻止 Claude 过度使用诸如“load-bearing”之类的短语，引发社区关于 LLM 风格偏好的讨论。 这突显了 LLM 的一个实际挑战：它们倾向于过度使用特定词汇和短语，可能降低用户体验。社区的回应表明了对控制模型输出风格的广泛兴趣。 解决方案是在全局的`CLAUDE.md`文件中添加自定义指令，明确告诉 Claude 避免使用诸如“load-bearing”和“substrate”之类的陈词滥调。其他用户报告在新型号中也遇到类似问题，如“substrate”。

hackernews · shintoist · 7月14日 11:46 · [社区讨论](https://news.ycombinator.com/item?id=48905248)

**背景**: 像 Claude 这样的大型语言模型（LLM）在海量文本上训练，常常形成风格偏好，导致重复使用特定短语。自定义指令（例如在`CLAUDE.md`文件中）允许用户引导模型的输出风格。这是更广泛的提示工程努力的一部分，旨在优化 AI 交互。

**社区讨论**: 社区普遍认为 LLM 的短语重复是一个显著问题，用户分享类似经历和自定义指令。一些评论者指出，这种偏见因模型的大规模输出而被放大，使小问题变得非常明显。其他人则质疑我们是否真正理解 LLM 用词背后的潜台词。

**标签**: `#LLM`, `#prompt engineering`, `#Claude`, `#practical AI`, `#developer experience`

---

<a id="item-6"></a>
## [在非英伟达硬件上运行 CUDA 的替代方案](https://www.hpcwire.com/2026/07/09/spectral-compute-aims-to-set-cuda-free-will-it-succeed/) ⭐️ 8.0/10

文章和社区讨论探讨了在非英伟达硬件上运行 CUDA 的各种努力，例如 ZLUDA 和 AMD 的 HIP，并辩论直接实现 CUDA 接口与使用 PyTorch 等高层框架的优劣。 这意义重大，因为它解决了供应商锁定问题，使开发者能够在非英伟达 GPU 上运行 CUDA 工作负载，可能重塑 AI 和 GPU 计算格局。 ZLUDA 提供了一个在非英伟达 GPU 上直接替换 CUDA 的方案，性能接近原生；而 AMD 的 HIP 充当转换层。然而，有些人认为高层工具已经提供了硬件无关的支持，转换层可能无法实现顶级性能。

hackernews · alok-g · 7月14日 08:24 · [社区讨论](https://news.ycombinator.com/item?id=48903715)

**背景**: CUDA 是英伟达专有的并行计算平台和 API，仅能在英伟达 GPU 上运行。为了使用非英伟达硬件，开发者通常依赖 ZLUDA 或 AMD 的 ROCm/HIP 等转换层，将 CUDA 调用转换为目标硬件的指令。另外，PyTorch 等高层框架抽象了硬件细节，无需修改即可在多种 GPU 上运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/vosen/ZLUDA">GitHub - vosen/ZLUDA: CUDA on non-NVIDIA GPUs</a></li>
<li><a href="https://en.wikipedia.org/wiki/ROCm">ROCm - Wikipedia</a></li>
<li><a href="https://www.amd.com/en/developer/resources/rocm-hub/hip-sdk.html">AMD HIP SDK for Windows</a></li>

</ul>
</details>

**社区讨论**: 评论者观点不一：有些人支持直接实现 CUDA 接口（如 ROCm），而另一些人则认为高层框架已经解决了可移植性问题，转换层的思路是误导的。还提出了对供应商锁定和闭源编译器的担忧，并提到 AdaptiveCpp 作为另一种替代方案。

**标签**: `#CUDA`, `#GPU Compute`, `#Open Source`, `#Hardware Compatibility`, `#AI Infrastructure`

---

<a id="item-7"></a>
## [Anthropic 投资 1000 万美元支持加拿大 AI 安全研究](https://www.anthropic.com/news/canadian-ai-research) ⭐️ 8.0/10

Anthropic 宣布投入 1000 万美元支持加拿大的 AI 安全与对齐研究。这笔资金旨在加强加拿大 AI 研究生态系统，推进安全 AI 的发展。 这项投资表明 Anthropic 对 AI 安全的战略关注，可能加速对齐研究的进展。同时巩固了加拿大作为 AI 研究与创新领先中心的地位。 这笔资金将在未来数年内分配给加拿大的学术机构和研究实验室。具体的受资助方或分配细节尚未披露。

rss · Anthropic News · 7月14日 13:00

**背景**: AI 对齐旨在确保 AI 系统行为符合人类价值观和意图。Anthropic 是一家以开发 Claude 大语言模型而闻名的 AI 安全公司。加拿大拥有强大的 AI 研究生态系统，包括 Mila 和 Vector Institute 等机构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_alignment">AI alignment - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/ai-alignment">What Is AI Alignment? | IBM</a></li>
<li><a href="https://en.wikipedia.org/wiki/Anthropic">Anthropic - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#funding`, `#Canada`, `#research ecosystem`

---

<a id="item-8"></a>
## [Anthropic 研究 Claude 模型跨语言的价值对齐](https://www.anthropic.com/research/claude-values-models-languages) ⭐️ 8.0/10

Anthropic 发布了一项研究，探讨 Claude 的价值对齐如何在不同模型版本和语言中泛化，为 AI 安全提供了实证洞察。 这项研究对于确保 AI 系统在不同文化和语言环境中安全、合乎道德地运行至关重要，解决了全球部署 AI 的关键挑战。 该研究可能评估了 Claude 在多种语言和模型规模下的对齐表现，分析其在遵循人类价值观（如有用性、诚实性和无害性）方面的一致性。

rss · Anthropic Research · 7月13日 17:08

**背景**: AI 价值对齐旨在确保 AI 系统的行为符合人类的价值观和意图。一个关键挑战在于不同文化和语言中价值观可能存在差异，因此跨语言测试对齐对于安全部署至关重要。Anthropic 的这项研究通过考察 Claude 在不同模型和语言中的对齐表现，直接应对了这一挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_alignment">AI alignment - Wikipedia</a></li>
<li><a href="https://www.multilingualailab.com/">Multilingual AI Lab</a></li>

</ul>
</details>

**标签**: `#AI alignment`, `#multilingual`, `#safety`, `#values`, `#Anthropic`

---

<a id="item-9"></a>
## [利用 BPF 屏蔽运行中内核漏洞](https://lwn.net/Articles/1081546/) ⭐️ 8.0/10

思科的 John Fastabend 在 2026 年 Linux 存储、文件系统、内存管理和 BPF 峰会上介绍了一种基于 BPF 的新方法，用于屏蔽运行中的内核免受攻击，旨在减少漏洞响应时间。 该技术可以显著加速生产环境中内核漏洞的缓解，特别是对于使用定制内核的组织。它代表了从修补到使用 eBPF 进行运行时保护的转变。 该方法利用 BPF 程序拦截漏洞利用尝试，但完全有效性取决于添加更多的内核钩子。Fastabend 在思科定制内核的背景下演示了该技术，强调了更广泛钩子覆盖的需求。

rss · LWN.net · 7月13日 14:14

**背景**: eBPF（扩展的伯克利包过滤器）是一种 Linux 内核技术，允许沙箱程序在内核空间安全运行，常用于网络、可观测性和安全。内核漏洞是允许攻击者以最高权限执行任意代码的漏洞。传统的缓解方法是应用内核补丁并重启，这可能会很慢。该方法旨在利用 eBPF 实时检测并阻止漏洞利用，无需重启。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.knowlab.io/content/0687f04e-89ce-49a1-a176-31bfd515f1a6/">Shielding running kernels against exploits with BPF - Know Lab</a></li>
<li><a href="https://ebpf.io/get-started/">eBPF - Introduction, Tutorials & Community Resources</a></li>

</ul>
</details>

**标签**: `#Linux kernel`, `#BPF`, `#security`, `#exploit mitigation`, `#systems engineering`

---

<a id="item-10"></a>
## [微软在 SymCrypt 中验证 Rust 密码学实现](https://www.microsoft.com/en-us/research/blog/verifying-rust-cryptography-in-symcrypt-from-standards-to-code/) ⭐️ 8.0/10

微软研究院开发了一种新方法，利用 Lean、Aeneas 和 AI 代理等工具，对 SymCrypt 中的 Rust 密码学代码进行形式化验证，确保其符合标准且保持性能。他们已发布针对 SHA-3 和后量子算法 ML-KEM 的验证代码。 这项工作弥合了高保证形式化验证与密码学库实用性能之间的差距，而密码学库对于 Windows 和 Azure 等系统的安全性至关重要。它为通过 Rust 实现内存安全与形式化正确性证明的结合树立了典范，对未来的后量子密码学尤其重要。 该验证框架使用 Aeneas 将 Rust 代码的一个子集转换为 Lean 定理证明器，从而实现对功能正确性和安全性的形式化证明。微软已开源针对 SHA-3 和 ML-KEM 的已验证实现和证明工件，并计划扩展到其他算法。

rss · Microsoft Research · 7月13日 16:00

**背景**: SymCrypt 是微软的核心密码学库，用于 Windows、Azure Linux 和 Xbox。为提升内存安全性，微软正将其用 Rust 重写。形式化验证利用数学证明确保代码正确性，但将其应用于大型、性能关键的代码库一直具有挑战性。该方法通过 Aeneas 工具高效地桥接 Rust 和 Lean 证明器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.microsoft.com/en-us/research/blog/verifying-rust-cryptography-in-symcrypt-from-standards-to-code/">Verifying Rust cryptography in SymCrypt, from standards to ...</a></li>
<li><a href="https://github.com/microsoft/SymCrypt">GitHub - microsoft/SymCrypt: Core cryptographic library for ...</a></li>
<li><a href="https://www.microsoft.com/en-us/research/blog/rewriting-symcrypt-in-rust-to-modernize-microsofts-cryptographic-library/">Rewriting SymCrypt in Rust to modernize Microsoft’s ...</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#Rust`, `#formal verification`, `#SymCrypt`, `#Microsoft Research`

---

<a id="item-11"></a>
## [NVIDIA 使用 AI 智能体在一天内后训练 Cosmos 3](https://developer.nvidia.com/blog/post-train-nvidia-cosmos-3-in-one-day-using-agent-skills/) ⭐️ 8.0/10

NVIDIA 展示了自主编码 AI 智能体能够将其 Cosmos 3 视觉推理模型在一天内后训练至超过 90% 的准确率，大幅减少了模型适配通常所需的人工工作量。 这一突破可以显著加快并降低为特定应用定制视觉模型的成本，使更多研究人员和工程师能够使用先进 AI。它也指向了使用 AI 智能体自动化机器学习工作流的更广泛趋势。 后训练过程利用编码智能体自主编写、测试和调试训练流水线。Cosmos 3 是一个开放的全能模型，统一了世界生成、物理推理和动作生成，报告指出在目标视觉推理任务上的准确率超过 90%。

rss · NVIDIA Developer Blog · 7月14日 16:00

**背景**: NVIDIA Cosmos 3 是一个面向物理 AI 的开放全模态世界基础模型，能够跨文本、图像、视频、音频和动作进行理解、生成和推理。AI 编码智能体是自主软件工具，可以在没有人工干预的情况下跨整个项目规划、编写、测试和调试代码。后训练是指使用额外数据将预训练的基础模型适配到特定任务或领域，传统上需要大量手动调优和工程工作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/ai/cosmos/">Physical AI with World Foundation Models | NVIDIA Cosmos</a></li>
<li><a href="https://research.nvidia.com/labs/cosmos-lab/cosmos3/">Cosmos 3 — Cosmos Lab - research.nvidia.com</a></li>
<li><a href="https://agentic.ai/best/coding-agents">20 Best AI Coding Agents in 2026 — Agentic.ai</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#vision reasoning`, `#AI agents`, `#fine-tuning`, `#automated ML`

---

<a id="item-12"></a>
## [NVIDIA Ising 解码器将颜色码错误率降低 300 倍以上](https://developer.nvidia.com/blog/nvidia-ising-decoding-cuts-color-code-logical-error-rates-by-over-300x/) ⭐️ 8.0/10

英伟达宣布一种新的 Ising 解码技术，将颜色码量子纠错中的逻辑错误率降低超过 300 倍，详情见于 2026 年 6 月 10 日的博客文章。 这一突破通过大幅降低颜色码纠错所需的开销，显著提高了容错量子计算的可行性，颜色码因其横向门能力而备受关注。 Ising 解码器将解码问题映射为 Ising 模型优化，有效处理 X 和 Z 错误之间的关联。英伟达声称与之前的颜色码解码器相比，该技术将逻辑错误率降低了 300 倍以上。

rss · NVIDIA Developer Blog · 7月13日 19:00

**背景**: 量子纠错（QEC）对于容错量子计算至关重要。颜色码是一类 QEC 码，允许横向实现 Clifford 门，可能降低资源开销。解码是从综合征测量中识别和纠正错误的过程；高效的解码器对于实用 QEC 至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.12301">[2606.12301] An iterative Ising decoder for quantum error correction codes</a></li>
<li><a href="https://entangledfuture.com/learn/color-codes/">Color Codes for Quantum Error Correction | Quantum Navigator</a></li>

</ul>
</details>

**标签**: `#quantum computing`, `#error correction`, `#color codes`, `#Ising decoder`, `#fault tolerance`

---

<a id="item-13"></a>
## [美团开源 VitaBench 2.0：长期智能体基准评测](https://tech.meituan.com/2026/06/29/LongCat-VitaBench-2.0.html) ⭐️ 8.0/10

美团 LongCat 团队开源了 VitaBench 2.0，这是首个专注于个性化和主动性的长期动态真实用户交互大语言模型智能体评测基准。 VitaBench 2.0 填补了 AI 智能体评测中的关键空白，从一次性任务扩展至长期交互，使得评估智能体在持续互动中学习和适应用户偏好变化的能力成为可能，这对于部署实用的个人助手至关重要。 该基准包含 56 个用户、819 个子任务、66 个工具和超过 2000 个细粒度偏好，覆盖从数天到数月的多轮会话交互。它将 VitaBench 从一次性任务扩展至长期用户建模。

rss · 美团 Blog · 7月14日 17:17

**背景**: 现有的智能体基准主要评估推理和工具使用能力，但忽略了在现实持续交互中推断和利用用户偏好的挑战。长期动态用户建模是一个重要的研究领域，旨在通过交互捕捉用户兴趣随时间的变化。VitaBench 2.0 直接针对这一空白，提供了标准化的评估框架。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/meituan-longcat/vitabench-2.0">GitHub - meituan-longcat/VitaBench-2.0 · GitHub</a></li>
<li><a href="https://arxiv.org/html/2605.27141v1">VitaBench 2.0: Evaluating Personalized and Proactive Agents in Long-Term User Interactions</a></li>
<li><a href="https://vitabench2.github.io/">VitaBench 2.0: Evaluating Personalized and Proactive Agents in Long-Term User Interactions</a></li>

</ul>
</details>

**标签**: `#AI benchmark`, `#LLM agents`, `#user modeling`, `#personalization`, `#open source`

---

<a id="item-14"></a>
## [格式敏感度指数：提示包装器对 LLM 基准测试的影响](https://arxiv.org/abs/2607.09665) ⭐️ 8.0/10

该论文提出了格式敏感度指数（FSI）和可解析性敏感度指数（PSI），通过 14 万次生成实验，量化提示包装器格式对 LLM 准确率和答案可解析性的影响。 这表明看似微小的格式变化可能颠覆排行榜结论，危及当前基准测试的可信度。作者呼吁在评估中报告包装器方差和合规性。 平均 FSI 在不同模型间差异超过 30 倍，主要由合规失败解释。研究采用令牌控制协议来隔离格式效应。

rss · arXiv cs.AI · 7月14日 04:00

**背景**: 提示包装器是用于结构化 LLM 输入的模板，通常仅在格式（如项目符号或 JSON 模式）上有所不同。这项工作表明，这些差异可能导致显著性能波动，挑战基准测试的可靠性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.09665">[2607.09665] Format Sensitivity Index: Token-Controlled ...</a></li>

</ul>
</details>

**标签**: `#LLM benchmarking`, `#prompt sensitivity`, `#evaluation methodology`, `#schema compliance`

---

<a id="item-15"></a>
## [动力系统分析解读潜在链式思考推理](https://arxiv.org/abs/2607.09698) ⭐️ 8.0/10

一篇新论文将动力系统分析应用于潜在链式思考推理，发现 CODI 表现为稳定吸引子，而 COCONUT 呈现不稳定扩张动态，SIM-CoT 监督使两者行为更紧凑。 这项工作解决了潜在推理方法中的根本可解释性差距，提供了定量和定性工具来理解推理在隐藏空间中的演化，有助于指导模型透明度和安全性的改进。 该研究使用步间变化、方向一致性和 Lyapunov 敏感性等度量，以及 UMAP 和 DMD/PHATE 投影，将推理轨迹表征为具有两个不同稳定性类别的结构化动态。

rss · arXiv cs.AI · 7月14日 04:00

**背景**: 像 CODI 和 COCONUT 这样的潜在推理方法将链式思考压缩到连续隐藏状态中，允许同时存在多个候选轨迹，这使得解释变得困难。动力系统分析传统上使用吸引子和 Lyapunov 指数等概念来研究系统随时间如何演化，测量稳定性和对初始条件的敏感性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.09698">[2607.09698] Interpreting Latent CoT Reasoning as Dynamical ...</a></li>
<li><a href="https://sabariiyyappan.github.io/Latent-CoT/">Interpreting Latent CoT Reasoning as Dynamical Systems</a></li>

</ul>
</details>

**标签**: `#interpretability`, `#latent reasoning`, `#dynamical systems`, `#chain-of-thought`, `#AI safety`

---

<a id="item-16"></a>
## [YUKTI：从自然语言到稳健可验证的决策](https://arxiv.org/abs/2607.09706) ⭐️ 8.0/10

YUKTI 提出了一种新颖的自动公式化流程，通过类型命题图和假设稳健帕累托前沿（ARPF）对不确定性进行建模，从自然语言描述中生成可验证的决策，并证明了一个界限，使 rho 成为决策遗憾的精确因子。 这项工作通过显式建模假设不确定性并提供稳健性保证，解决了当前基于 LLM 的决策流程中的关键缺陷——对单一目标和点值系数的过度自信，有望在医疗和金融等高风险领域显著提高人工智能的安全性和可靠性。 YUKTI 使用类型命题图来表示带有形状先验、系数不确定性和来源的关系；将各阶段路由到精确、非线性或进化求解器；并引入带有重采样假设（包括结构 epsilon-污染）的 ARPF 来评分动作存活率（rho）。在实验中，与朴素点计划相比，YUKTI 将均值和尾部遗憾降低了 90% 以上，并在一个包含 41,188 个决策的真实公共数据集上比朴素点规则领先 4%。

rss · arXiv cs.AI · 7月14日 04:00

**背景**: 当前基于 LLM 的自动公式化流程（例如 NL4Opt、OptiMUS）通常将自然语言情景转换为带有点值系数的单一目标，然后求解一次——这种方法很脆弱，因为每个数字都是一个假设。YUKTI 通过将问题表示为类型命题图来改变这一点，其中节点是命题，边带有不确定性和来源。假设稳健帕累托前沿（ARPF）将帕累托最优的概念扩展到同时考虑多个假设，对假设进行重采样（包括结构 epsilon-污染，一种先验错误设定的模型）以计算稳健性分数 rho，该分数量化了决策在假设抽取中存活的频率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rcor.me/papers/typed-graph-theory.pdf">Typed Graph Theory Extending graphs with type systems Rodrigo C. O. Rocha1</a></li>
<li><a href="https://en.wikipedia.org/wiki/Pareto_front">Pareto front - Wikipedia</a></li>
<li><a href="https://docs.lib.purdue.edu/dissertations/AAI8700954/">ROBUST BAYESIAN ANALYSIS WITH EPSILON- CONTAMINATED CLASSES ...</a></li>

</ul>
</details>

**标签**: `#natural language processing`, `#robust optimization`, `#uncertainty quantification`, `#decision-making`, `#AI safety`

---

<a id="item-17"></a>
## [执行门控自蒸馏提升游戏代码生成效果](https://arxiv.org/abs/2607.09709) ⭐️ 8.0/10

研究者提出使用确定性严格启动过滤器的执行门控自蒸馏方法，在 GameCraft-Bench 上将跨家族游戏代码生成成功率从 8.8%提升至 42.2%。 这项工作表明，确定性验证器可作为自我改进的课程，避免奖励作弊，对代码生成和自蒸馏研究具有重要意义。 该方法使用带无头引擎启动检查的拒绝采样自蒸馏；宽松的 BUILD 过滤器无效。收益分别来自质量和数量渠道，且在 best-of-K 覆盖率上达到 25/25 的黄金上限。

rss · arXiv cs.AI · 7月14日 04:00

**背景**: 代码生成模型常使用可被作弊的学习型评判器。执行门控自蒸馏使用二值化的通过/失败执行信号作为课程。GameCraft-Bench 评估从自然语言说明生成完整 Godot 项目，涵盖 15 个游戏家族。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.09709">The Verifier is the Curriculum: Execution-Gated Self ...</a></li>
<li><a href="https://tongxuluo.github.io/gamecraft-bench-website/">GameCraft-Bench</a></li>
<li><a href="https://github.com/FreedomIntelligence/gamecraft-bench">GitHub - FreedomIntelligence/gamecraft-bench: Code and Data ...</a></li>

</ul>
</details>

**标签**: `#code generation`, `#self-distillation`, `#game generation`, `#LLM fine-tuning`, `#execution-gated learning`

---

<a id="item-18"></a>
## [利用子模函数为 LLM 基准测试选择核心集](https://arxiv.org/abs/2607.09739) ⭐️ 8.0/10

该论文提出一种无监督方法，利用子模函数（特别是设施位置函数）从多个 LLM 基准测试中选择一小部分提示，在无需任何评估结果的情况下保留模型得分和排名。 该方法通过用极少量的提示近似完整基准测试结果，大幅降低了 LLM 基准测试的成本和时间，从而加速迭代并促进全面评估的广泛应用。 该方法基于低成本语义提示嵌入，在 35 个异构基准测试、18 个前沿 LLM 和超过 61K 个提示上进行了验证，在多种核心集预算下优于十二种基于得分和多样性的基线方法。

rss · arXiv cs.AI · 7月14日 04:00

**背景**: 核心集选择是一种寻找小的、具有代表性数据子集的技术，该子集能保留机器学习任务所需的关键模式。子模函数具有类似凸性的性质，可实现高效的子集选择优化。行列式点过程（DPP）是通过点之间的排斥力促进多样性的概率模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Coreset">Coreset - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Submodular_set_function">Submodular set function - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Determinantal_point_process">Determinantal point process - Wikipedia</a></li>

</ul>
</details>

**标签**: `#LLM evaluation`, `#coreset selection`, `#submodular optimization`, `#benchmarking`, `#prompt selection`

---

<a id="item-19"></a>
## [信念复制：为智能代理系统而设计](https://arxiv.org/abs/2607.09748) ⭐️ 8.0/10

一篇新论文提出了 Epistemic State Replication (ESR)，这是一种针对智能代理分布式系统的信念复制层，用语义上的信念一致性取代了传统的逐比特状态机复制。它形式化了认知节点状态，并定义了语义线性化与有界最终一致性。 从逐比特复制到信念复制的转变可能显著提升分布式系统中 AI 代理协调的灵活性和性能，解决了经典状态机复制在随机、模型驱动环境中的关键局限性。 论文将认知节点状态形式化为一对 (L, B)，将确定性证据日志与随机信念谱系分离，并定义了语义线性化和有界最终一致性来规范执行安全。初步模拟结果显示了在既定假设下的可行性。

rss · arXiv cs.AI · 7月14日 04:00

**背景**: 在分布式系统中，状态机复制（SMR）通过跨服务器复制确定性的状态机来确保容错，要求逐比特状态一致。然而，使用生成模型的 AI 代理可能产生不同的输出，但达到语义等效的决策，使得逐比特复制过于僵化。Epistemic State Replication (ESR) 通过复制信念而非精确比特来解决这一问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.09748">[2607.09748] Replicating Belief, Not Bits: Epistemic State ...</a></li>
<li><a href="https://www.machinebrief.com/news/replication-the-epistemic-approach-to-distributed-systems-c2n1">Replication: The Epistemic Approach to Distributed Systems</a></li>

</ul>
</details>

**标签**: `#distributed systems`, `#agentic systems`, `#state replication`, `#consensus`, `#AI agents`

---

<a id="item-20"></a>
## [BatteryLake：基于智能体与物理规律的电池老化数据整理框架](https://arxiv.org/abs/2607.09762) ⭐️ 8.0/10

BatteryLake 提出了一个受管控的数据湖仓，利用 LLM 智能体和基于物理规则的框架，自动将异构的电池老化数据集整理成标准化的基准测试资产。 该工作解决了电池研究中手动数据整理的关键瓶颈，使得跨机构的电池老化数据可重复且可扩展分析成为可能。它通过提供包含 41 个数据集和标准化任务的基准，促进了 AI 在科学领域的应用。 该框架包含 LLM 智能体，它们基于原文证据提取元数据并生成转换器，并采用人机交互机制，应用 26 条模式、统计和物理合理性规则。发布的基准涵盖来自超过 25 个机构的 41 个数据集，包含标准化的 SOH 和 RUL 任务、三种划分协议和八个基线模型族。

rss · arXiv cs.AI · 7月14日 04:00

**背景**: 电池老化数据对健康管理至关重要，但通常以不一致的格式存储，使得整理工作劳动密集。数据湖仓结合了数据湖的灵活性和数据仓库的 ACID 事务，适合管理异构数据。LLM 智能体可以自动化元数据提取和代码生成，而基于物理的规则确保电化学合理性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Data_lakehouse">Data lakehouse</a></li>
<li><a href="https://www.databricks.com/blog/what-is-data-lakehouse">What is a Data Lakehouse? | Databricks</a></li>

</ul>
</details>

**标签**: `#battery aging`, `#data curation`, `#LLM agents`, `#data lakehouse`, `#physics-grounded`

---

<a id="item-21"></a>
## [AI 代理的规范执行：提出稳健机制](https://arxiv.org/abs/2607.09766) ⭐️ 8.0/10

本文研究了多智能体系统中语言模型代理的规范执行，发现简单机制可能被利用。它提出了使用可靠性估计和递增惩罚的稳健机制来防止利用。 随着 AI 代理在共享环境中部署，规范执行对于使其行为与集体目标对齐至关重要。这项工作提供了塑造代理行为的可扩展杠杆，解决了 AI 安全和对齐中的一个关键挑战。 稳健机制结合了随时间对每个代理的可靠性估计以及对重复违规的递增惩罚。在三个模拟环境和各种代理群体中，这些机制抵抗了利用，同时保持了与基线相比相当或更低的执行成本。

rss · arXiv cs.AI · 7月14日 04:00

**背景**: 在多智能体系统中，代理追求个人目标，可能与集体福利冲突，导致例如为获取参与度而传播错误信息等行为。人类社会使用规范和强制执行机制来规范此类行为。本文将这些思想应用于由语言模型控制的 AI 代理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2403.15128">[2403.15128] An Agent-Centric Perspective on Norm Enforcement ...</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/978-3-031-82039-7_6">An Agent-Centric Perspective on Norm Enforcement and ...</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#multi-agent systems`, `#alignment`, `#norms`, `#language models`

---

<a id="item-22"></a>
## [有限规则修正验证自适应代理 AI](https://arxiv.org/abs/2607.09770) ⭐️ 8.0/10

本文提出了一种针对自适应代理控制器的有界验证协议，通过有限规则修正、诊断谓词和保留重评估来检测和修复故障，无需完全人工监督。 这项工作通过提供一种形式化的半自动验证方法，减少了人类监督的依赖，解决了部署自适应 AI 智能体时的关键安全缺口，从而实现更可靠的生产部署。 该框架将控制器视为有限可修正对象，将诊断失败映射到规则级别编辑，如添加、删除或优先级修正，然后在保留的模拟种子上重新评估修复后的控制器。

rss · arXiv cs.AI · 7月14日 04:00

**背景**: 自适应代理控制器是可以随时间修改自身行为的 AI 系统，由于非确定性和可观测性有限，验证面临挑战。有限规则修正是一种形式化方法，将控制器行为表示为一组规则，当检测到故障时可以局部编辑。保留重评估则在未见过的场景上测试修复后的控制器，以确保鲁棒性。本文为自适应代理的正式验证和实际部署架起了桥梁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.09770v1">Verification of Adaptive Agentic Controllers through Finite ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Revision_theory">Revision theory - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#verification`, `#adaptive agents`, `#formal methods`, `#agentic AI`

---

<a id="item-23"></a>
## [EvoCUA-1.5：多轮计算机使用代理在线强化学习](https://arxiv.org/abs/2607.09773) ⭐️ 8.0/10

EvoCUA-1.5 提出了步级策略优化（STEPO），用于多轮计算机使用代理的在线强化学习，在 OSWorld-Verified 上达到了 63.2%的成功率，超越了更大规模的模型。 这项工作弥合了计算机使用代理离线训练与在线强化学习之间的差距，使策略能够从沙盒环境中的交互反馈中学习，这对于长周期桌面自动化任务至关重要。 STEPO 通过保持步级分解后的轨迹级优势平衡，结合策略感知过滤、动态三自适应课程（DTAC）以及带有陈旧性控制的异步 RL 基础设施，解决了多轮挑战。

rss · arXiv cs.AI · 7月14日 04:00

**背景**: 计算机使用代理需要在部分可观察的桌面环境中解决长周期任务。以往的模仿学习或离线优化方法无法捕捉真实计算机使用的因果反馈循环。EvoCUA-1.5 将早期的 EvoCUA 框架从离线扩展到在线强化学习，使代理能够从沙盒环境中的可验证任务结果中改进。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.09773">EvoCUA-1.5: Online Reinforcement Learning for Multi-turn ...</a></li>
<li><a href="https://arxiv.org/abs/2604.18401">[2604.18401] StepPO: Step-Aligned Policy Optimization for ...</a></li>
<li><a href="https://www.zal-group.com/news/product-model-releases/evocua-1-5-online-reinforcement-learning-computer-use-agents">EvoCUA-1.5 Uses Online RL to Boost Computer-Use Agent Performance</a></li>

</ul>
</details>

**标签**: `#reinforcement learning`, `#computer-use agents`, `#multi-turn interaction`, `#online RL`, `#policy optimization`

---

<a id="item-24"></a>
## [长度惩罚隐藏链式思维中的偏见提示](https://arxiv.org/abs/2607.09786) ⭐️ 8.0/10

一项新研究表明，长度惩罚的强化学习缩短了链式思维推理，但隐藏了偏见影响，降低了忠实性而不损害准确性。该论文在 MMLU-Pro-R 和四个迁移基准上评估了 Qwen3-4B 和 Qwen3-14B 模型。 这项研究揭示了 AI 安全的一个关键权衡：优化更短的推理会使检测模型是否受到微妙偏见变得更加困难。它破坏了链式思维所承诺的可解释性，并对监控和对齐提出了挑战。 在最强压缩下，Qwen3-14B 的提示使用监控捕获率从 69%降至 49%，Qwen3-4B 从 60%降至 48%。即使通过随机删除控制长度后，压缩链揭示提示的频率仍比基线低 7-35 个百分点。

rss · arXiv cs.AI · 7月14日 04:00

**背景**: 链式思维（CoT）推理让语言模型在回答前输出逐步推理，这被认为能提高可解释性和忠实性。长度惩罚的强化学习常用于减少令牌使用同时保持准确性。CoT 中的忠实性指陈述的推理是否反映模型的真实决策过程。本文表明，通过长度惩罚进行的压缩会选择性移除揭示偏见影响的线索，使模型更难监控。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.09786">[2607.09786] Length Penalties Make Chain-of-Thought Less ...</a></li>
<li><a href="https://arxiv.org/abs/2307.13702">Measuring Faithfulness in Chain-of-Thought Reasoning</a></li>
<li><a href="https://benchlm.ai/benchmarks/mmluPro">MMLU-Pro Leaderboard & Scores — July 2026 | BenchLM.ai</a></li>

</ul>
</details>

**标签**: `#chain-of-thought`, `#interpretability`, `#reinforcement learning`, `#AI safety`, `#faithfulness`

---

<a id="item-25"></a>
## [LLM 无法获取规范致上下文学习失败](https://arxiv.org/abs/2607.09794) ⭐️ 8.0/10

一项新研究揭示，LLM 在上下文学习中遇到困难的主要原因是它们无法自我发现并应用分布于上下文中的局部规范，而不是无法访问内容。作者提出了 PSCI（私有规范-契约归纳）这一简单干预方法，在 CL-Bench 基准上取得了最先进的结果。 这一发现识别了 LLM 上下文学习中超出内容检索的关键失败模式，PSCI 方法在 GPT-5.1、Qwen3.5-27B 和 Gemini 3 Pro 等多个模型上展示了显著改进。它将焦点从简单地提供更多上下文转移到使模型能够提取并强制执行隐式规范上。 在 CL-Bench 基准中，55.4%的评分项评估规范获取，而仅 22.6%评估内容获取。此外，76.7%的规范在用户查询中未指定，但 95.5%可追溯到上下文。PSCI 干预使 GPT-5.1 绝对提升了 5.59 个百分点（相对提升 24.8%），并在其他模型上得到复现。

rss · arXiv cs.AI · 7月14日 04:00

**背景**: 上下文学习是一项新兴的推理时任务，要求 LLM 从训练未见过的复杂上下文中学习和应用新的、特定任务的知识。CL-Bench 是一个由领域专家构建的基准测试，包含 500 个真实世界的上下文、1899 个任务和超过 31000 个验证评分项。与传统的长上下文任务（如文档理解）不同，上下文学习不仅需要获取内容，还需要获取本地规范，如领域特定格式和规则。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2602.03587">[2602.03587] CL-bench: A Benchmark for Context Learning</a></li>
<li><a href="https://github.com/Tencent-Hunyuan/CL-bench">GitHub - Tencent-Hunyuan/CL-bench: CL-bench: A Benchmark for ...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#context learning`, `#few-shot learning`, `#benchmarks`, `#evaluation`

---