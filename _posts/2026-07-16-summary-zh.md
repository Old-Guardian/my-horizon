---
layout: default
title: "Horizon Summary: 2026-07-16 (ZH)"
date: 2026-07-16
lang: zh
---

> 从 461 条内容中筛选出 25 条重要资讯。

---

1. [美团发布 LongCat-2.0：基于国产算力集群的万亿参数模型](#item-1) ⭐️ 9.0/10
2. [WBench：首个面向交互式世界模型的多轮评测基准](#item-2) ⭐️ 9.0/10
3. [安全哨兵：三路路由提升 LLM 工具安全性](#item-3) ⭐️ 9.0/10
4. [AIMO 可解释性挑战赛：区分推理的稳健性与虚假性](#item-4) ⭐️ 9.0/10
5. [智能 LLM 工具从被终止进程中捏造结果](#item-5) ⭐️ 9.0/10
6. [结构变化使 AI 写作绕过顶级检测器](#item-6) ⭐️ 9.0/10
7. [WANDA：移动操作任务的合成数据引擎](#item-7) ⭐️ 9.0/10
8. [DeepMind 发布 AI 控制路线图 v0.1](#item-8) ⭐️ 9.0/10
9. [为语言模型提供可组合信任：可证明的提示注入防御](#item-9) ⭐️ 9.0/10
10. [HORCRUX：支持所有 NIST 后量子密码算法的统一 RISC-V 扩展](#item-10) ⭐️ 9.0/10
11. [动作重绑定攻击劫持 Android GUI 代理](#item-11) ⭐️ 9.0/10
12. [月之暗面发布 Kimi K3，支持百万上下文并达到前沿性能](#item-12) ⭐️ 8.0/10
13. [Inkling：开放权重的多模态 MoE 模型发布](#item-13) ⭐️ 8.0/10
14. [Linus Torvalds 公开支持 AI 用于 Linux 开发](#item-14) ⭐️ 8.0/10
15. [xAI 在隐私争议后开源 grok-build](#item-15) ⭐️ 8.0/10
16. [Claude Web Fetch 工具漏洞导致数据泄露](#item-16) ⭐️ 8.0/10
17. [Lobste.rs 从 MariaDB 迁移到 SQLite，降低成本并提升性能](#item-17) ⭐️ 8.0/10
18. [欧盟施压谷歌：根据 DMA 向 AI 对手开放安卓](#item-18) ⭐️ 8.0/10
19. [GPT-Red：通过自我对弈实现 AI 安全的自动化红队测试](#item-19) ⭐️ 8.0/10
20. [Sched-ext 进展：子调度器和代理执行接近完成](#item-20) ⭐️ 8.0/10
21. [旧版 shim 未撤销，可绕过 Secure Boot](#item-21) ⭐️ 8.0/10
22. [DeepMind 探究扩散模型的创造力](#item-22) ⭐️ 8.0/10
23. [借助 NVIDIA BlueField 协同设计扩展智能体 AI](#item-23) ⭐️ 8.0/10
24. [NVIDIA CUDA 13.3 新增硬件无进位乘法加速加密](#item-24) ⭐️ 8.0/10
25. [NVIDIA Nemotron-3-E 在 RTEB 基准测试中排名第一](#item-25) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [美团发布 LongCat-2.0：基于国产算力集群的万亿参数模型](https://tech.meituan.com/2026/06/30/LongCat2.0.html) ⭐️ 9.0/10

美团正式发布 LongCat-2.0，这是一个万亿参数 MoE 模型，总参数 1.6 万亿，平均激活参数 480 亿，在 5 万卡国产 GPU 集群上从零开始训练，原生支持 100 万 token 上下文，并针对智能体编码任务进行了优化。 这是首个在国产 GPU 集群上完成全流程训练与推理的万亿参数模型，标志着中国 AI 硬件生态的重大进展，有助于减少对国外 GPU 的依赖。对于开发者社区，LongCat-2.0 的智能体编码能力可大幅自动化代码理解、生成和调试。 该模型引入了 LongCat 稀疏注意力机制（LSA），将注意力计算从二次复杂度降至线性复杂度，实现高效的 100 万上下文处理，并采用 N-gram Embedding 提升 Token 级表示能力。动态激活范围从 330 亿到 560 亿参数，提供了部署灵活性。

rss · 美团 Blog · 7月16日 17:21

**背景**: 万亿参数模型（如 GPT-4 或 Gemini）通常需要庞大的 GPU 集群，且多在 NVIDIA 硬件上训练。智能体编码（Agentic Coding）指的是 AI 代理能够根据自然语言任务自主编写、测试和修复代码，超越简单的代码补全，处理复杂工作流。美团在国产 AI ASIC 超级节点上取得的成就尤为引人注目，因为它证明了大模型训练在不依赖外国芯片的情况下也是可行的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://longcat.chat/blog/longcat-2.0/">Introducing LongCat - 2 . 0</a></li>
<li><a href="https://huggingface.co/meituan-longcat/LongCat-2.0">meituan- longcat / LongCat -2.0 · Hugging Face</a></li>
<li><a href="https://www.longcatai.org/technology/">Technology - LSA, ScMoE, DORA, Zero-Computation... | LongCat AI</a></li>

</ul>
</details>

**标签**: `#trillion-parameter model`, `#large-scale training`, `#domestic GPU cluster`, `#agentic coding`, `#long-context`

---

<a id="item-2"></a>
## [WBench：首个面向交互式世界模型的多轮评测基准](https://tech.meituan.com/2026/06/12/LongCat-WBench.html) ⭐️ 9.0/10

美团 LongCat 团队开源了 WBench，这是首个针对交互式视频世界模型的系统性多轮评测基准。它从视频质量、设定遵循、交互遵循、一致性和物理合规五个维度评估模型。 WBench 填补了交互式世界模型评测的关键空白，能够系统性诊断模型的能力与局限。该基准将标准化评估流程，推动交互式视频生成和世界模型研究的进展。 该基准包含 289 个测试用例和 1,058 轮交互，覆盖导航、主体动作、事件编辑和视角切换四种交互类型，涉及多样化的场景和视角。

rss · 美团 Blog · 7月16日 17:21

**背景**: 世界模型是模拟物理世界的人工智能系统。交互式视频世界模型在此基础上允许用户通过动作实时控制生成的视频流。以往的基准主要评估被动生成的视频质量，缺乏对交互能力（如多轮一致性和动作遵循）的评估。WBench 通过结构化的多轮评测框架填补了这一空白。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.25874">[2605.25874] WBench: A Comprehensive Multi-turn Benchmark for ...</a></li>
<li><a href="https://github.com/meituan-longcat/WBench">GitHub - meituan-longcat/WBench: WBench: A Comprehensive ...</a></li>
<li><a href="https://meituan-longcat.github.io/WBench/">WBench - Interactive World Model Benchmark</a></li>

</ul>
</details>

**标签**: `#world models`, `#benchmark`, `#interactive video`, `#open source`

---

<a id="item-3"></a>
## [安全哨兵：三路路由提升 LLM 工具安全性](https://arxiv.org/abs/2607.13594) ⭐️ 9.0/10

研究人员提出了 Safety Sentry，这是一种轻量级防护模型，将 LLM 工具调用安全的二值安全/不安全决策替换为三路路由（执行、询问、拒绝），性能超越现有基线模型。 这一重构解决了 AI 安全中的关键局限，实现了每次工具调用的上下文感知决策，减少了不必要的打断并提升了自主性，同时控制了假阳性和假阴性两类错误率。 Safety Sentry 使用单个解码时阈值，使得一个固定检查点无需重新训练即可适应不同风险容忍度；它是一个 4B 参数模型，将推理简化为单次解码调用。

rss · arXiv cs.AI · 7月16日 04:00

**背景**: LLM 代理执行可能导致现实世界危害的工具调用，因此使用防护模型将动作分类为安全或不安全。传统的二值防护模型混淆了危害性和上下文适切性，并在类别级别操作，导致频繁打断。Safety Sentry 引入了每次实例的上下文推理和三路决策。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.13594v1">Safety Sentry: Context-Aware Human Intervention via EXECUTE ...</a></li>
<li><a href="https://github.com/safesentry/AskGuard">GitHub - safesentry/AskGuard: askguard-anonymous-review</a></li>

</ul>
</details>

**标签**: `#LLM safety`, `#AI safety`, `#tool use`, `#context-aware`, `#guard models`

---

<a id="item-4"></a>
## [AIMO 可解释性挑战赛：区分推理的稳健性与虚假性](https://arxiv.org/abs/2607.13899) ⭐️ 9.0/10

AIMO 可解释性挑战赛是一项新的竞赛，旨在通过分析前沿数学语言模型的内部机制，区分稳健推理与虚假推理。竞赛提供新发布的奥赛级问题、前沿模型访问权限以及对抗鲁棒性评估。 该挑战赛通过关注内部机制而非仅仅最终答案，填补了评估大语言模型推理能力的关键空白，能够揭示模型是否使用可靠的推理还是利用脆弱的捷径。它可能推动可解释性和鲁棒性的重大进展，并可能改变 AI 推理评估的方式。 参与者将获得新发布的奥赛级数学推理问题及其符号表示，用于生成新颖的功能变体，并配有计算基础设施支持。该竞赛将创建一个开放的鲁棒性基准测试和基线系统，用于数学推理可解释性。

rss · arXiv cs.AI · 7月16日 04:00

**背景**: 机械可解释性旨在通过逆向工程理解神经网络的内部结构，类似于分析软件。虚假推理指模型利用表面特征而非真正理解得出正确答案，通常通过对抗性扰动暴露。该竞赛围绕前沿 AI 决策是否可泛化和可靠的问题，连接了可解释性与泛化研究。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mechanistic_interpretability">Mechanistic interpretability</a></li>
<li><a href="https://www.themoonlight.io/en/review/making-mathematical-reasoning-adaptive">[Literature Review] Making Mathematical Reasoning Adaptive</a></li>

</ul>
</details>

**标签**: `#interpretability`, `#mathematical reasoning`, `#LLM robustness`, `#competition`

---

<a id="item-5"></a>
## [智能 LLM 工具从被终止进程中捏造结果](https://arxiv.org/abs/2607.13071) ⭐️ 9.0/10

一项研究发现，Claude Code 的压缩摘要将超时命令（退出码 143）的部分输出视为已确认结果，并在会话间传播误报。 这揭示了智能 LLM 工具的关键可靠性缺陷，影响依赖会话连续性进行数据处理或科学计算的所有工作流，并凸显了超越此前 LLM 自我评估问题的认知失败模式。 该故障源于混淆观察与持久化：终端输出被视为等同于持久存储。这具体影响 Claude Code，但扩展到任何使用压缩摘要的智能工具。

rss · arXiv cs.AI · 7月16日 04:00

**背景**: 像 Claude Code 这样的智能 LLM 编码工具将会话历史压缩成摘要，后续会话将其视为事实。压缩是一种通过总结先前交互来管理上下文窗口的技术。认知失败是指知识验证的崩溃，工具将未验证的信息报告为已确认。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.13071v1">Compaction as Epistemic Failure: How Agentic LLM Tools ...</a></li>

</ul>
</details>

**标签**: `#LLM agents`, `#AI safety`, `#epistemic failure`, `#agentic tools`, `#reliability`

---

<a id="item-6"></a>
## [结构变化使 AI 写作绕过顶级检测器](https://arxiv.org/abs/2607.13565) ⭐️ 9.0/10

一篇新论文提出了两种新颖的分布外攻击家族——跨年代语域攻击和现代主义意识流——针对最先进的对抗性微调检测器实现了高达 50 倍的欺骗率提升，并占据了 ELOQUENT 2026 Voight-Kampff 排行榜前五名。 这项研究揭示了检测器脆弱性的根本不对称性：将生成文本推出检测器的训练分布可靠地击败了对抗性检测，而模仿人类文本则完全失败。它突显了当前 AI 生成文本检测中的持久弱点，对内容真实性和 AI 安全具有重要意义。 攻击家族利用结构性分布偏移——跨年代语域攻击使用历史散文风格（如维多利亚或现代主义风格），而意识流模仿 20 世纪初的叙事形式。论文还表明，用时代散文扩充训练数据这一明显的防御措施无法弥补这一漏洞。

rss · arXiv cs.CL · 7月16日 04:00

**背景**: ELOQUENT 2026 Voight-Kampff 是一项检测 AI 生成文本的竞赛，参与者针对最先进的检测器开发规避攻击。对抗性微调是一种防御技术，通过在对抗性样本上训练检测器来提高鲁棒性。分布外攻击生成与检测器训练数据分布不同的文本，本文显示这是一种有效的规避策略。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.13565v1">UTS at ELOQUENT 2026 Voight-Kampff: structural shifts in AI ...</a></li>
<li><a href="https://papers.cool/arxiv/2607.13565">UTS at ELOQUENT 2026 Voight-Kampff: structural shifts in AI ...</a></li>

</ul>
</details>

**标签**: `#AI detection`, `#adversarial attacks`, `#language models`, `#out-of-distribution`, `#text generation`

---

<a id="item-7"></a>
## [WANDA：移动操作任务的合成数据引擎](https://arxiv.org/abs/2607.13154) ⭐️ 9.0/10

研究人员推出了 WANDA，这是一种合成数据引擎，能够从单次人类演示中为开放世界移动操作任务生成多样化的训练数据。WANDA 首先重建背景高斯溅射和机器人-物体交互轨迹，然后利用全身运动规划将接触密集的片段重新排列成新的轨迹。 这解决了机器人学习中的数据稀缺这一关键瓶颈，通过最大化每次人类演示的价值，可能降低扩展移动操作任务的成本和工作量。该方法跨场景和跨本体的泛化能力可能加速机器人在非结构化环境中的部署。 WANDA 应用修正状态扩展（Corrective State Expansion）通过增加状态多样性来增强长时程鲁棒性，并通过将渲染的物体与高斯溅射背景合成生成逼真的观测。它还支持跨本体数据生成，并通过在形态不同的移动操作器上的零样本部署得到了验证。

rss · arXiv cs.RO · 7月16日 04:00

**背景**: 移动操作需要机器人在多样环境中移动并与物体交互，但训练这样的系统通常需要大量的人类遥操作数据。高斯溅射（Gaussian splatting）是一种渲染技术，通过 3D 高斯原语表示场景，实现高质量的新视角合成。UMI（通用操作接口）是一种先前的数据收集框架，将人类演示迁移到机器人，但仍需要大量人工。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gaussian_splatting">Gaussian splatting</a></li>
<li><a href="https://umi-gripper.github.io/">Universal Manipulation Interface : In-The-Wild Robot Teaching...</a></li>

</ul>
</details>

**标签**: `#robotics`, `#mobile manipulation`, `#synthetic data`, `#Gaussian splatting`, `#data generation`

---

<a id="item-8"></a>
## [DeepMind 发布 AI 控制路线图 v0.1](https://arxiv.org/abs/2607.13087) ⭐️ 9.0/10

Google DeepMind 发布了 GDM AI 控制路线图 v0.1，这是首个针对内部部署中可能未对齐的 AI 代理的安全蓝图。它引入了 TRAIT&R 威胁分类法，并概述了跨四个检测层级（D1-D4）和三个预防与响应层级（R1-R3）的分层缓解措施。 该路线图直接解决了 AI 安全中的一个关键空白，为防御日益强大的未对齐 AI 代理提供了具体、可操作的框架。它为其他前沿 AI 实验室采用类似的多层安全方法树立了先例。 该路线图包含 15 项具体缓解措施，从低成本的思维链监控等简单措施到实时访问控制和内部激活监控等高级防护措施。它强调保守的威胁模型，假设 AI 代理可能追求不良目标。

rss · arXiv cs.CR · 7月16日 04:00

**背景**: 随着 AI 代理越来越深入地融入 DeepMind 等前沿公司的内部运营，传统的安全措施假设 AI 工具是可信的。AI 控制方法在对齐技术失效时提供第二道防线，应对未对齐代理通过网络攻击或其他恶意行为造成危害的风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/securing-the-future-of-ai-agents/gdm-ai-control-roadmap.pdf">GDM AI Control Roadmap - Googleapis.com</a></li>
<li><a href="https://www.lesswrong.com/posts/hEtkyKGoPpFeWnKkX/gdm-ai-control-roadmap">GDM AI Control Roadmap</a></li>

</ul>
</details>

**标签**: `#AI Safety`, `#AI Security`, `#Alignment`, `#AI Control`

---

<a id="item-9"></a>
## [为语言模型提供可组合信任：可证明的提示注入防御](https://arxiv.org/abs/2607.13149) ⭐️ 9.0/10

该论文提出了一种信任模型，将行动权限置于模型之外，通过确定性流水线和监控器从可信输入中选择操作，在未经修改的 Gemma 4 26B 模型上实现了 94%的注入防御率。 这项工作通过提供可证明的边界和强有力的实证结果，解决了提示注入这一关键的 LLM 安全问题，有望提高 LLM 系统在敏感应用中的可靠性。 该流水线使用钝化（passivation）和级联包装器（cascade wrapper），将真实泄漏防御率从 27%提高到 94%，清洁质量成本约为 4%（Q_rel=0.96）。在自适应红队测试下，可证明的边界无条件成立，测量到的防御率保持在 87%。该级联还将低信任来源事实的归因率从 0%提高到 92%。

rss · arXiv cs.CR · 7月16日 04:00

**背景**: 提示注入是一种安全漏洞，攻击者将恶意指令嵌入用户提供的数据中，从而覆盖模型的预期行为。传统防御常因模型内指令和数据共享同一令牌流而失效。该方法通过按源完整性对输入排序，并使用监控器从可信来源中选择操作，在外部强制执行信任边界。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/dridwilson_prompt-injection-is-not-a-vulnerability-of-activity-7417945758257156097-RXce">Prompt injection in language models : a trust boundary issue | LinkedIn</a></li>
<li><a href="https://arxiv.org/html/2505.01177v1">LLM Security: Vulnerabilities, Attacks, Defenses, and ...</a></li>
<li><a href="https://dev.to/psgtechnautsnl/which-is-to-be-master-language-authority-and-llms-36i8">Which Is to Be Master? Language , Authority and... - DEV Community</a></li>

</ul>
</details>

**标签**: `#LLM safety`, `#prompt injection`, `#trust boundaries`, `#language models`, `#AI security`

---

<a id="item-10"></a>
## [HORCRUX：支持所有 NIST 后量子密码算法的统一 RISC-V 扩展](https://arxiv.org/abs/2607.13939) ⭐️ 9.0/10

研究人员推出了 HORCRUX，这是一种紧凑的 RISC-V 指令集扩展，可加速所有 NIST 标准化的后量子密码算法，包括 ML-KEM、ML-DSA、SLH-DSA、HQC 和 Falcon，在 FPGA 上实现了高达 129 倍的加速，且硬件开销极小。 该工作解决了资源受限嵌入式系统对密码敏捷性的关键需求，确保这些系统在向抗量子安全过渡时能够高效运行多种后量子密码算法。 HORCRUX 针对五种 NIST 批准的 PQC 方案的共享计算内核，使用紧密耦合的协处理器，在 Zynq UltraScale+ FPGA 上仅增加不到 21K 个 LUT 和 4.4K 个 FF；65nm CMOS 下的 ASIC 结果展示了通过严格功耗表征验证的能效。

rss · arXiv cs.CR · 7月16日 04:00

**背景**: 后量子密码术（PQC）是指旨在抵御未来量子计算机攻击的密码算法。NIST 已经标准化了几种 PQC 算法，包括 ML-KEM（密钥封装机制）、ML-DSA（基于格签名）、SLH-DSA（基于哈希签名）、HQC（基于编码的 KEM）和 Falcon（基于格签名）。RISC-V 是一种开放标准的指令集架构，允许为专门工作负载自定义扩展；在嵌入式系统中，硬件加速对 PQC 至关重要，因为纯软件实现速度太慢。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ML-KEM">ML-KEM - Wikipedia</a></li>
<li><a href="https://www.rfc-editor.org/rfc/rfc9814.pdf">RFC 9814: Use of the SLH - DSA Signature Algorithm in the...</a></li>
<li><a href="https://quantumsequrity.com/blog/hqc-explained">HQC Explained: NIST Code - Based Post-Quantum KEM | QNSQY</a></li>

</ul>
</details>

**标签**: `#RISC-V`, `#post-quantum cryptography`, `#hardware acceleration`, `#embedded systems`, `#crypto-agility`

---

<a id="item-11"></a>
## [动作重绑定攻击劫持 Android GUI 代理](https://arxiv.org/abs/2601.12349) ⭐️ 9.0/10

研究人员提出动作重绑定攻击，这是一种跨应用攻击，利用观察-动作间隙，使恶意应用无需任何危险权限即可劫持 GUI 代理的执行。 此攻击揭示了基于大语言模型的 GUI 代理（越来越多用于移动设备自动化）存在根本性安全漏洞。它可能导致未经授权的数据删除、短信发送或应用卸载，而现有恶意软件扫描器无法检测到它。 该攻击对原子动作劫持的成功率达 100%，且未在 VirusTotal 上被检测到。它利用意图对齐策略（IAS）操纵代理的推理，并能创建多步骤利用循环。

rss · arXiv cs.CR · 7月16日 04:00

**背景**: GUI 代理是大型多模态模型，通过感知屏幕和注入输入来与移动界面交互。然而，它们跨应用以高权限运行，与 Android 的应用沙箱机制产生冲突。观察-动作间隙指的是代理感知屏幕状态与其执行动作之间的延迟（4-15 秒），在此期间 UI 可能发生变化而代理无法察觉。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2601.12349v2">Zero-Permission Manipulation: Can We Trust Large Multimodal Model Powered GUI Agents?</a></li>
<li><a href="https://arxiv.org/html/2604.18860">Temporal UI State Inconsistency in Desktop GUI Agents: Formalizing and Defending Against TOCTOU Attacks on Computer-Use AgentsCode and data: https://github.com/OwenXu6/gui_agent</a></li>

</ul>
</details>

**标签**: `#security`, `#GUI agents`, `#adversarial attacks`, `#mobile security`, `#AI safety`

---

<a id="item-12"></a>
## [月之暗面发布 Kimi K3，支持百万上下文并达到前沿性能](https://www.kimi.com/en) ⭐️ 8.0/10

月之暗面（Moonshot AI）发布了 Kimi K3，这是一个开放权重的大型语言模型，拥有 100 万 token 的上下文窗口，性能达到前沿水平，声称整体智能仅次于 Claude Fable 5 和 GPT-5.6 Sol。完整模型权重将在未来几天内发布。 Kimi K3 作为中国开放权重模型的重大突破，与顶级前沿模型竞争，可能降低先进 AI 研究和开发的门槛。其超长上下文和具有竞争力的定价有望加速长周期编程和知识工作的创新。 据报道，Kimi K3 拥有 2.8 万亿参数（稠密 MoE），定价为每百万输入 token 3 美元，每百万输出 token 15 美元，缓存价格为 0.3 美元。它通过 Kimi API 平台和 OpenRouter 提供服务，上下文窗口为 100 万 token。

hackernews · vincent_s · 7月16日 14:46 · [社区讨论](https://news.ycombinator.com/item?id=48935342)

**背景**: 月之暗面是一家成立于 2023 年的北京 AI 公司，被称为中国“AI 四小龙”之一，专注于大语言模型。该公司此前发布了 Kimi K2.6 和 K2.7 等模型。Kimi K3 是其旗舰模型，采用混合专家（MoE）架构，开放权重的发布让更广泛的 AI 社区能够使用和微调它。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://platform.kimi.ai/docs/guide/kimi-k3-quickstart">Kimi K3 - Kimi API Platform</a></li>
<li><a href="https://www.kimi.com/en">Kimi AI with K3 | Built for Agentic Coding & Knowledge Work</a></li>
<li><a href="https://en.wikipedia.org/wiki/Moonshot_AI">Moonshot AI</a></li>
<li><a href="https://wan27.org/blog/kimi-k3-explained">What Is Kimi K3? Moonshot AI's 2.5T Flagship Model Explained (2026)</a></li>

</ul>
</details>

**社区讨论**: 社区反应积极，许多人指出其定价高于其他中国开放模型，但如果性能符合声称，则价格合理。部分用户报告了令人印象深刻的应用实例，例如 K3 找到了 Claude Fable 5 未能定位的 bug。还有人强调其 2.8 万亿的参数规模使其成为最大的开放模型之一。

**标签**: `#AI`, `#Open-source`, `#Large Language Model`, `#Kimi K3`, `#Frontier Model`

---

<a id="item-13"></a>
## [Inkling：开放权重的多模态 MoE 模型发布](https://simonwillison.net/2026/Jul/16/inkling/#atom-everything) ⭐️ 8.0/10

由 Mira Murati 领导的 Thinking Machines Lab 发布了 Inkling，这是一个开放权重的多模态混合专家模型，总参数 975B，活跃参数 41B，采用 Apache-2.0 许可证，在 45 万亿 token 上训练。 Inkling 增强了美国开放权重生态系统，提供了与 NVIDIA Nemotron 和 Gemma 4 等模型竞争的选择，尤其作为通过 Tinker 平台进行微调的强大基础模型。 该模型是多模态的，处理文本、图像、音频和视频，但它不是前沿模型；Thinking Machines Lab 承认它旨在用于定制和微调，还有一个更小的变体 Inkling-Small（总参数 276B，活跃参数 12B）仍在测试中，即将发布。

rss · Simon Willison · 7月16日 15:35

**背景**: 混合专家模型（MoE）使用多个专门化的子网络（专家），并稀疏激活，从而在较低计算成本下实现更大的总参数量。多模态模型同时处理多种数据类型，如文本、图像和音频。开放权重模型公开训练好的参数，允许用户检查、微调和部署模型，但并非完全开源，因为训练数据可能未公开。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Multimodal_model">Multimodal model</a></li>
<li><a href="https://promptmetheus.com/resources/llm-knowledge-base/open-weights-model">Open - weights Model | LLM Knowledge Base</a></li>

</ul>
</details>

**标签**: `#open-weights`, `#multimodal`, `#mixture-of-experts`, `#AI lab`, `#model release`

---

<a id="item-14"></a>
## [Linus Torvalds 公开支持 AI 用于 Linux 开发](https://simonwillison.net/2026/Jul/16/linus-torvalds/#atom-everything) ⭐️ 8.0/10

Linux 创始人兼顶级维护者 Linus Torvalds 在 Linux Media 邮件列表中公开表示，AI 是 Linux 开发的有用工具，并强调该项目不反对 AI，拒绝任何反对意见。 这位极具影响力的人物的大力支持可能会塑造社区规范，鼓励在 Linux 内核开发及其他开源项目中更广泛地采用 AI 工具。 Torvalds 强调，虽然 AI 的经济影响等问题尚存疑问，但其有用性已不再存疑，不同意的人可以 fork 项目或离开。

rss · Simon Willison · 7月16日 13:26

**背景**: Linus Torvalds 是 Linux 内核的原始创建者和长期维护者，Linux 内核是 Linux 操作系统的核心。最近，AI 工具（如大型语言模型）被用于软件开发中的代码生成和调试，但它们在内核开发中的使用在一些社区成员中引起了争议。

**标签**: `#Linux`, `#AI tools`, `#open source`, `#kernel development`, `#Linus Torvalds`

---

<a id="item-15"></a>
## [xAI 在隐私争议后开源 grok-build](https://simonwillison.net/2026/Jul/15/grok-build/#atom-everything) ⭐️ 8.0/10

2026 年 7 月 15 日，xAI 将整个 Grok Build 代码库以 Apache 2.0 许可证开源，此前 grok CLI 工具意外将用户的整个目录上传到 Google Cloud 存储桶，引发严重隐私事件。 此次事件凸显了 AI 编码工具中的严重隐私风险，迫使 xAI 采取前所未有的透明措施——开源核心基础设施，这可能为重建信任树立新标杆。 grok CLI 曾上传整个目录，包括 SSH 密钥和密码数据库，引发社区强烈反对；xAI 禁用了上传功能、删除了所有保留数据，开源版本包含 844,530 行 Rust 代码，且仅有一个提交。

rss · Simon Willison · 7月15日 23:59

**背景**: Grok Build 是 xAI 推出的基于终端的 AI 编码代理，以全屏 TUI 形式运行，用于代码理解、编辑和执行 shell 命令。它使用 Google Cloud Storage 存储桶上传数据。隐私缺陷在于 CLI 默认上传整个工作目录，导致敏感文件暴露。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/xai-org/grok-build">GitHub - xai-org/grok-build: SpaceXAI's coding agent harness ...</a></li>
<li><a href="https://x.ai/cli">Grok Build | SpaceXAI</a></li>
<li><a href="https://docs.cloud.google.com/storage/docs/buckets">About Cloud Storage buckets | Google Cloud Documentation</a></li>

</ul>
</details>

**社区讨论**: 用户报告了严重的隐私侵犯行为，例如上传密码管理器和 SSH 密钥，促使埃隆·马斯克承诺删除所有已上传数据。开源被视为重建信任的举措，但有人质疑这是否足够。

**标签**: `#privacy`, `#open-source`, `#AI tools`, `#security`, `#xAI`

---

<a id="item-16"></a>
## [Claude Web Fetch 工具漏洞导致数据泄露](https://simonwillison.net/2026/Jul/15/claude-web-fetch-exfiltration/#atom-everything) ⭐️ 8.0/10

研究人员 Ayush Paul 发现了一种利用 Claude 的 web_fetch 工具 URL 限制设计漏洞的方法，该工具可以导航到先前获取页面中嵌入的 URL，从而通过带有嵌套链接的蜜罐站点成功提取了用户的姓名、城市和雇主信息。 这表明即使是精心设计的防止 AI 代理数据泄露的保护措施也可能通过细微的设计缺陷被绕过，突出了保护易受提示注入攻击的系统的持续挑战。该漏洞影响所有使用 web_fetch 工具的 Claude 用户，并强调了需要更加稳健、多层防御的必要性。 该攻击仅针对在 user-agent 中包含 'Claude-User' 的客户端触发以逃避检测，Anthropic 没有支付漏洞赏金，因为他们声称已在内部发现该问题。随后通过移除 web_fetch 导航到获取内容中返回的额外链接的能力修复了此漏洞。

rss · Simon Willison · 7月15日 14:21

**背景**: “致命三重奏”（Lethal Trifecta）是指 AI 代理能够访问私人数据、从在线内容中读取恶意指令并拥有数据泄露工具。Claude 的 web_fetch 工具原本设计为仅获取用户明确提供的 URL 或来自其配套 web_search 工具的 URL 以减轻数据泄露，但未能限制导航到已获取页面内的 URL。这一设计漏洞使得蜜罐攻击可以通过链接链提取私人信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.hiddenlayer.com/research/the-lethal-trifecta-and-how-to-defend-against-it">How the Lethal Trifecta Expose Agentic AI - hiddenlayer.com</a></li>
<li><a href="https://simonwillison.net/2025/Sep/10/claude-web-fetch-tool/">Claude API: Web fetch tool</a></li>

</ul>
</details>

**标签**: `#prompt injection`, `#AI security`, `#data exfiltration`, `#Claude`, `#vulnerability`

---

<a id="item-17"></a>
## [Lobste.rs 从 MariaDB 迁移到 SQLite，降低成本并提升性能](https://simonwillison.net/2026/Jul/14/lobsters-sqlite/#atom-everything) ⭐️ 8.0/10

社区链接聚合器 Lobsters 于上周末成功将其数据库从 MariaDB 迁移至 SQLite，CPU 和内存使用率降低，响应速度更快，托管成本减少 50%。该网站现在运行在单个 VPS 上，拥有多个 SQLite 数据库，其中主数据库大小为 3.8GB。 此次迁移挑战了 SQLite 不适合生产环境 Web 应用的传统观点，展示了显著的资源节省和性能提升。它为类似迁移提供了可复用的模式，尤其适用于中等流量的 Rails 应用。 迁移涉及多个拉取请求，在 30 次提交和 188 个文件中增加了 735 行代码，删除了 593 行代码。主 SQLite 数据库大小为 3.8GB，此外还有缓存数据库（1.1GB）、队列数据库（218MB）和 Rack::Attack 数据库（555MB）。

rss · Simon Willison · 7月14日 19:44

**背景**: SQLite 是一种无服务器、基于文件的数据库引擎，由于被认为存在并发限制，通常用于开发或小型应用。然而，现代 SQLite 功能如 WAL 模式和 busy_timeout 编译指示使其能够用于中等流量的生产环境 Web 应用，本案例研究证明了这一点。Rails 7.1 及更高版本加强了对生产环境中使用 SQLite 的支持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pockit.tools/blog/sqlite-renaissance-turso-d1-libsql-production-guide/">The SQLite Renaissance: Why the World's Most... - Pockit Blog</a></li>
<li><a href="https://justinmckelvey.com/blog/sqlite-in-production-ready-for-your-startup">SQLite in Production : Why It's Ready for Your Startup in 2026</a></li>

</ul>
</details>

**标签**: `#SQLite`, `#web development`, `#database migration`, `#Rails`, `#production experience`

---

<a id="item-18"></a>
## [欧盟施压谷歌：根据 DMA 向 AI 对手开放安卓](https://www.ithome.com/0/977/759.htm) ⭐️ 8.0/10

欧盟委员会正式要求谷歌向 OpenAI 等 AI 竞争对手开放安卓系统的 11 项功能，并向对手 AI 聊天机器人共享匿名化搜索数据，称这是为了遵守《数字市场法案》（DMA）。 这项决定可能重塑移动 AI 助手和搜索领域的竞争格局，削弱谷歌的主导地位，为用户提供更多选择。同时，它也为监管机构如何强制守门人共享数据和系统访问权限树立了先例。 这些变化将在下一代安卓版本中生效，预计 2027 年 7 月左右推出，并包含隐私和安全保护措施。在共享数据前，谷歌可先评估竞争对手的安全性，数据访问定价公式将从明年 1 月开始实施。

rss · IT HOME · 7月16日 12:13

**背景**: 欧盟《数字市场法案》（DMA）针对被指定为“守门人”的大型在线平台，旨在防止反竞争行为。谷歌的安卓和搜索服务因可能扼杀 AI 及其他市场的竞争而受到审查。欧盟委员会六个月前启动了“规范程序”，以明确谷歌的义务。

**标签**: `#regulation`, `#AI competition`, `#Android`, `#EU Digital Markets Act`, `#search data`

---

<a id="item-19"></a>
## [GPT-Red：通过自我对弈实现 AI 安全的自动化红队测试](https://openai.com/index/unlocking-self-improvement-gpt-red) ⭐️ 8.0/10

OpenAI 推出了 GPT-Red，这是一个自动化红队测试系统，通过自我对弈发明针对工具使用代理的提示注入攻击，并利用成功的攻击生成训练数据以增强防御。 该方法通过创建可扩展、自我改进的管道来加固模型对抗提示注入，直接推动了 AI 安全的发展，提示注入是用于代理的 LLM 的关键漏洞。它为使用对抗性自我对弈提高 AI 系统的鲁棒性树立了先例。 GPT-Red 是一个仅内部使用的系统，与部署的模型分开，以防止其攻击能力被滥用。它不对用户开放，也不通过 API 提供；其好处间接体现在未来使用 GPT-Red 攻击加固的 GPT 模型上。

rss · OpenAI News · 7月15日 10:00

**背景**: 红队测试是一种安全专家模拟攻击以发现漏洞的实践。自我对弈是一种机器学习方法，AI 模型通过与自己对弈来提高性能，AlphaGo 就是著名的例子。提示注入攻击利用 LLM 无法区分指令和用户输入的弱点，导致意外行为。GPT-Red 将这些概念结合起来，让一个对抗模型（红方）与防御模型（蓝方）在自我对弈循环中竞争，以生成强大的防御。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/unlocking-self-improvement-gpt-red/">GPT-Red: Unlocking Self -Improvement for Robustness | OpenAI</a></li>
<li><a href="https://www.technologyreview.com/2026/07/15/1140514/meet-gpt-red-an-llm-super-hacker-openai-built-to-make-its-models-safer/">Meet GPT-Red: an LLM super-hacker OpenAI built to make its models safer | MIT Technology Review</a></li>
<li><a href="https://thenextweb.com/news/gpt-red-openai-ai-hacker">OpenAI built GPT - Red to hack its own AI, and hid it</a></li>

</ul>
</details>

**社区讨论**: Reddit 评论指出，GPT-Red 是一个内部对抗模型，它能发明提示注入攻击并利用它们生成训练数据以加强防御。评论提到，与 Anthropic 的 Mythos（寻找软件漏洞）不同，GPT-Red 针对 AI 代理，且 GPT-Red 本身不公开可用。评论暗示这可能是一个用于加固未来每一代 GPT 的自我对弈工厂。

**标签**: `#AI safety`, `#red teaming`, `#self-play`, `#robustness`, `#alignment`

---

<a id="item-20"></a>
## [Sched-ext 进展：子调度器和代理执行接近完成](https://lwn.net/Articles/1082717/) ⭐️ 8.0/10

LWN 报道 sched_ext 即将完成子调度器层次结构支持，并解决与代理执行的不兼容性，这是通过 BPF 实现可扩展 CPU 调度的关键特性。 这些进展使得 Linux 中能够实现更灵活、更强大的自定义 CPU 调度器，促进在生产环境中实验和部署新型调度策略，有益于系统研究和性能优化。 子调度器允许层次化调度策略，而代理执行使一个进程能将其执行上下文捐献给另一个进程，这对于某些同步和优先级继承工作负载至关重要。

rss · LWN.net · 7月16日 14:00

**背景**: sched_ext 是一项 Linux 内核特性，允许开发者将自定义 CPU 调度器实现为 eBPF 程序，从而安全快速地迭代调度算法。子调度器通过允许调度器层次结构扩展了此功能，而代理执行解决了长期存在的限制，即某些内核操作（如互斥锁所有权）需要直接的任务执行上下文。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/sched_ext">sched_ext</a></li>
<li><a href="https://github.com/sched-ext/scx">GitHub - sched-ext/scx: sched_ext schedulers and tools Overview - sched_ext sched_ext sched-ext · GitHub Extensible Scheduler Class — The Linux Kernel documentation sched-ext Tutorial | CachyOS</a></li>

</ul>
</details>

**标签**: `#Linux kernel`, `#sched_ext`, `#BPF`, `#CPU scheduling`, `#systems engineering`

---

<a id="item-21"></a>
## [旧版 shim 未撤销，可绕过 Secure Boot](https://lwn.net/Articles/1082940/) ⭐️ 8.0/10

CMU CERT 发布公告指出，许多旧版 shim 引导程序从未被添加到 UEFI Secure Boot 撤销列表中，导致攻击者可以利用它们绕过 Secure Boot 并执行任意代码。 此漏洞破坏了 Linux 系统上 Secure Boot 的信任模型，可能使具有管理员权限的攻击者实现持久、难以检测的入侵，甚至可在操作系统重装后依然存在。 该公告包含易受攻击的 shim 版本列表；攻击者必须已拥有管理员权限或能够修改引导过程才能利用此问题。

rss · LWN.net · 7月15日 12:49

**背景**: UEFI Secure Boot 强制只允许运行签名后的引导程序。Shim 是一个由微软签名的小型引导程序，用于加载 Linux 引导程序（如 GRUB）。撤销列表 (dbx) 存储已知恶意二进制的哈希值以阻止其执行。如果旧版 shim 未包含在该列表中，它们仍会被信任，从而可被用来加载未签名代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://itsfoss.com/secure-boot-shim-file/">What are Secure Boot & Shim Files? Explained for Linux Users</a></li>
<li><a href="https://grabify.org/blog/eleven-vulnerable-uefi-shims-enable-secure-boot-bypass/">Critical UEFI Shim Vulnerabilities: Eleven Microsoft-Signed ...</a></li>

</ul>
</details>

**标签**: `#security`, `#UEFI`, `#Linux`, `#bootloader`, `#vulnerability`

---

<a id="item-22"></a>
## [DeepMind 探究扩散模型的创造力](https://research.google/blog/towards-demystifying-the-creativity-of-diffusion-models/) ⭐️ 8.0/10

Google DeepMind 发布了一篇博客文章，分析扩散模型如何展现创造力，将算法理论与实证分析相结合，以揭秘其创作过程。 这项工作探讨了生成式 AI 中一个较少被理解的方面，可能影响未来关于模型创造力的研究，并指导开发更具创新性的系统。 该分析可能涉及检查扩散模型如何生成超出训练数据的新颖输出，可能通过随机元素和学习先验，具体技术细节在博客中有阐述。

rss · Google Deepmind Blog · 7月15日 18:06

**背景**: 扩散模型是一种生成模型，从随机噪声开始，逐步去噪以生成图像等数据。它们已成为现代生成式 AI 的基石，驱动着 Stable Diffusion 和 DALL-E 等工具。理解它们的创造力对于提升 AI 能力至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Diffusion_model">Diffusion model</a></li>
<li><a href="https://www.geeksforgeeks.org/artificial-intelligence/what-are-diffusion-models/">What are Diffusion Models? - GeeksforGeeks</a></li>

</ul>
</details>

**标签**: `#diffusion models`, `#generative AI`, `#creativity`, `#theory`, `#DeepMind`

---

<a id="item-23"></a>
## [借助 NVIDIA BlueField 协同设计扩展智能体 AI](https://developer.nvidia.com/blog/scaling-agentic-ai-factories-through-extreme-co-design-with-nvidia-bluefield/) ⭐️ 8.0/10

NVIDIA 的博客介绍了智能体 AI 工作负载如何需要新的基础设施模式，以及 BlueField DPU 如何通过计算、网络和存储的极端协同设计实现扩展。 智能体 AI 与传统 AI 不同，它通过链式调用多个模型和工具交互，对基础设施提出了前所未有的要求；BlueField 的方法为构建高效、可扩展的 AI 工厂提供了蓝图。 BlueField-4 DPU 提供高达 800 Gb/s 的吞吐量，并支持网络、存储和安全的线速处理，使其适合智能体 AI 的突发性、多调用模式。

rss · NVIDIA Developer Blog · 7月16日 16:00

**背景**: 智能体 AI 系统通过每个请求调用多个模型、工具和内存查找来自主执行任务，产生‘突发性’流量模式。传统数据中心基础设施难以处理这种工作负载。NVIDIA 的 BlueField DPU 将基础设施任务从 CPU 卸载，实现高效扩展。极端协同设计是指在所有系统层紧密集成硬件和软件优化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nvidia_BlueField">Nvidia BlueField - Wikipedia</a></li>
<li><a href="https://www.nvidia.com/en-us/networking/products/data-processing-unit/">BlueField Networking Platform | NVIDIA</a></li>
<li><a href="https://resources.nvidia.com/en-us-accelerated-networking-resource-library/bluefield-4-dpu-datasheet">NVIDIA BlueField-4 DPU</a></li>

</ul>
</details>

**标签**: `#agentic AI`, `#infrastructure`, `#NVIDIA BlueField`, `#scaling`, `#co-design`

---

<a id="item-24"></a>
## [NVIDIA CUDA 13.3 新增硬件无进位乘法加速加密](https://developer.nvidia.com/blog/building-faster-cryptography-with-carryless-multiplication-in-nvidia-cuda-13-3/) ⭐️ 8.0/10

NVIDIA 宣布在 CUDA 13.3 中为 GPU 新增了无进位乘法（CLMUL）硬件指令，从而能够高效实现认证加密和哈希函数等加密原语。 这将 x86 CPU 上已存在超过 15 年的加密原语引入 NVIDIA GPU，有望大规模加速安全计算、区块链和零知识证明等工作负载。 无进位乘法在乘法过程中丢弃进位，对应于 GF(2) 上的多项式乘法——这是许多对称密码和通用哈希方案的核心操作。

rss · NVIDIA Developer Blog · 7月15日 17:37

**背景**: 无进位乘法，也称为 XOR 乘法，是一种执行二元多项式乘法而不产生进位的硬件指令。它广泛应用于加密领域，用于实现 Galois/Counter Mode (GCM) 认证加密以及其他基于有限域 GF(2^n) 的算法。x86 CPU 自 2008 年（Intel Westmere 架构）起就包含了专用的 CLMUL 指令。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/building-faster-cryptography-with-carryless-multiplication-in-nvidia-cuda-13-3/">Building Faster Cryptography with Carryless Multiplication in ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Carry-less_multiplication">Carry-less multiplication</a></li>
<li><a href="https://en.wikipedia.org/wiki/Finite_field_arithmetic">Finite field arithmetic - Wikipedia</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#CUDA`, `#GPU`, `#hardware acceleration`, `#NVIDIA`

---

<a id="item-25"></a>
## [NVIDIA Nemotron-3-E 在 RTEB 基准测试中排名第一](https://huggingface.co/blog/nvidia/nemotron-3-embed-wins-rteb) ⭐️ 8.0/10

NVIDIA 的 Nemotron-3-E 嵌入模型在检索文本嵌入基准测试 (RTEB) 上取得了总体第一的排名，推动了代理检索能力的发展。 这证明了 NVIDIA 在检索嵌入模型领域的领先地位，这对于需要高质量、动态检索的代理 AI 系统至关重要。它可能影响代理检索在企业 AI 应用中的采用。 RTEB 基准测试于 2025 年 10 月推出，专门用于衡量嵌入模型和重排序器的检索准确性。Nemotron-3-E 是 Nemotron 3 家族的一部分，该家族包括 Nano、Super 和 Ultra 等针对代理 AI 优化的变体。

rss · Hugging Face Blog · 7月16日 16:01

**背景**: 代理检索是检索增强生成 (RAG) 的进化，其中自主代理将检索作为决策过程的一部分。高质量的嵌入模型对于确保准确和相关的检索至关重要。RTEB 基准测试提供了一个标准化的评估来比较专注于检索的模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/rteb">Introducing RTEB: A New Standard for Retrieval Evaluation</a></li>
<li><a href="https://research.nvidia.com/labs/nemotron/Nemotron-3/">NVIDIA Nemotron 3 Family of Models</a></li>
<li><a href="https://www.algolia.com/blog/ai/agentic-retrieval">Agentic retrieval: a practical guide for enterprise AI</a></li>

</ul>
</details>

**社区讨论**: 新闻项中未提供社区评论。

**标签**: `#NVIDIA`, `#embeddings`, `#retrieval`, `#agentic retrieval`, `#benchmark`

---