---
layout: default
title: "Horizon Summary: 2026-11-20 (ZH)"
date: 2026-11-20
lang: zh
---

> 从 477 条内容中筛选出 25 条重要资讯。

---

1. [陶哲轩宣布无外力欧拉/纳维-斯托克斯奇点与广义黎曼猜想证明](#item-1) ⭐️ 10.0/10
2. [Levent Alpöge 声称用 Lean 证明了广义黎曼假设](#item-2) ⭐️ 9.0/10
3. [预印本声称无外力纳维–斯托克斯方程有限时间爆破](#item-3) ⭐️ 9.0/10
4. [所有 VC 类均获近二次规模的样本压缩方案](#item-4) ⭐️ 9.0/10
5. [马苏洛发布 940 页草案声称证明 GRH](#item-5) ⭐️ 8.0/10
6. [Thinking Machines 发布 Inkling 2 Mini：开放权重的循环式 MoE 模型](#item-6) ⭐️ 8.0/10
7. [Frostbite：由 AI 设计并完成形式化验证的交互网 CPU 架构](#item-7) ⭐️ 8.0/10
8. [PostgreSQL 19 发布，新增 WAIT FOR LSN 实现副本上的「读己之写」一致性](#item-8) ⭐️ 8.0/10
9. [美团推出统一推荐基座大模型 MTFM，覆盖外卖多业务精排](#item-9) ⭐️ 8.0/10
10. [SailSearch 用两个大模型智能体协作发现新的优化算法](#item-10) ⭐️ 8.0/10
11. [BuggyMLE 用缺陷注入与全新复杂度指数扩展机器学习工程基准难度](#item-11) ⭐️ 8.0/10
12. [CoMPASS：衡量大模型是否强化用户准社会依恋的多轮基准](#item-12) ⭐️ 8.0/10
13. [RLCDR 将 LLM 评判者转化为可校准的决策奖励，用于强化学习训练](#item-13) ⭐️ 8.0/10
14. [AI 智能体审计 324 篇金融论文，仅约 25%的结论在多种设定下依然稳健](#item-14) ⭐️ 8.0/10
15. [MKA 基准发布：用 200 个端到端专业任务考核多模态智能体](#item-15) ⭐️ 8.0/10
16. [论文称大模型智能体的安全性不可判定且不可组合](#item-16) ⭐️ 8.0/10
17. [稀疏自编码器审计揭示 GraphCast 内部天气动力学机制](#item-17) ⭐️ 8.0/10
18. [TuringSpace：125 个交互式空间 CAPTCHA 揭示多模态大模型的空间能力短板](#item-18) ⭐️ 8.0/10
19. [Antom 3-in-1 Transformer：70 亿参数支付基础模型将线上损失降低 37.88%](#item-19) ⭐️ 8.0/10
20. [WeightCode：用冻结语言模型编写程序直接改写神经网络权重](#item-20) ⭐️ 8.0/10
21. [Canon 层在万亿 token 规模下节省约 30% 预训练 token](#item-21) ⭐️ 8.0/10
22. [HireWatch 基准发现大模型在招聘中的法律合规性十分脆弱](#item-22) ⭐️ 8.0/10
23. [解读医疗大模型的"言语化思维"能更可靠地发现提示注入](#item-23) ⭐️ 8.0/10
24. [LLM 评委在强化学习中传递类别偏见而非答案知识](#item-24) ⭐️ 8.0/10
25. [基于大模型的搜索返回的拉美新闻比传统搜索引擎更少元、更少本地内容](#item-25) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [陶哲轩宣布无外力欧拉/纳维-斯托克斯奇点与广义黎曼猜想证明](https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/) ⭐️ 10.0/10

陶哲轩（Terence Tao）在 2026 年 11 月 20 日的博客文章中宣布了无外力欧拉方程奇点、无外力纳维-斯托克斯方程奇点，以及广义黎曼猜想的证明，并称这些结果可在 Lean 中进行机器检验。 如果得到确认，无外力纳维-斯托克斯奇点将否定性地解决纳维-斯托克斯方程存在性与光滑性这一千禧年大奖难题，而广义黎曼猜想的证明将解决数论中的一项核心猜想；两者也都将成为前沿数学形式化验证的重要里程碑。 评论者报告称，两个独立的 Lean 内核均接受了该形式化证明，这使内核漏洞被利用的可能性降低，但本身并不能确认形式化陈述与预期数学命题一致；据称陶哲轩的文章指出，广义黎曼猜想的论证用到了 Langlands 纲领和算术几何的全部力量。

hackernews · archon1410 · 11月20日 17:21 · [社区讨论](https://news.ycombinator.com/item?id=50578358)

**背景**: Lean 是一个开源证明助手和函数式编程语言，用于编写可机器检验的数学证明。在流体力学中，欧拉方程描述无粘流动，而纳维-斯托克斯方程包含粘性；“无外力”意味着方程中没有外加的强迫项；奇点意味着光滑解在有限时间内破裂，这正是纳维-斯托克斯方程存在性与光滑性问题的核心。广义黎曼猜想将黎曼猜想从黎曼 zeta 函数推广到更广泛的一类 L 函数，而 Langlands 纲领是一组连接数论、表示论和几何的广泛猜想。形式化验证会用一个小型可信内核检查证明，因此人们使用独立内核来降低实现漏洞的风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/">Unforced Euler singularity, unforced Navier-Stokes ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lean_(proof_assistant)">Lean (proof assistant)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Navier–Stokes_existence_and_smoothness">Navier–Stokes existence and smoothness - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者既感到兴奋，也对职业前景感到焦虑，争论 AI 究竟能创造真正新的数学抽象，还是只能重组和验证已有内容，其中一人称数学家将变成 AI 所构建数学世界的“天文学家或考古学家”。其他人强调两个独立的 Lean 内核接受了该结果，说明不太可能是内核漏洞被利用，并提到陶哲轩称广义黎曼猜想的证明用到了 Langlands 纲领和算术几何；还有一位评论者批评陶哲轩没有讨论该结果的意义。

**标签**: `#mathematics`, `#Navier-Stokes`, `#Riemann-Hypothesis`, `#formal-verification`, `#Lean`, `#AI-for-math`

---

<a id="item-2"></a>
## [Levent Alpöge 声称用 Lean 证明了广义黎曼假设](https://alpo.ge/remark.pdf) ⭐️ 9.0/10

数学家 Levent Alpöge 在 alpo.ge/remark.pdf 发布论文，声称证明了广义黎曼假设，并附带了约 1.3GB、约 1500 万行的 Lean 形式化证明，以 14 个分卷压缩包形式分发。该声明日期为 2026 年 11 月 20 日，据称有 AI 辅助，目前尚未经过独立验证。 如果成立，这将是数论领域首个具备如此规模机器可检验形式化验证的千禧年级别成果，可能改变重大定理的确立方式。同时它也直接卷入了当前关于现有 AI 系统能否攻克最艰难开放问题的争论，而 Terence Tao 近期对此表示怀疑。 该 Lean 产物体量惊人——约 1.3GB、约 1500 万行，分为 14 个可下载分卷，需要拼接后解压，这本身就让独立检验成为一项艰巨的工程任务。目前这仍是一个未经核实的声明，评论者还指出几乎同时出现了另一份看似完全由人类完成的证明。

hackernews · iamronaldo · 11月20日 14:16 · [社区讨论](https://news.ycombinator.com/item?id=50574968)

**背景**: 黎曼假设是数学中最著名的开放问题之一，它断言黎曼 ζ 函数的非平凡零点实部均为 1/2；广义黎曼假设则把这一论断推广到更广泛的整体 L-函数族，包括狄利克雷 L-函数和戴德金 ζ 函数。目前只有代数函数域情形下的特例得到证明，数域情形仍未解决。Lean 是一个开源的证明助手与函数式编程语言，定理可在其中被机器陈述和检验，因此庞大的 Lean 开发原则上可以被机械验证，即便人类无法通读全部内容。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Generalized_Riemann_hypothesis">Generalized Riemann hypothesis</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lean_(proof_assistant)">Lean (proof assistant) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Riemann_hypothesis">Riemann hypothesis - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者既谨慎又着迷：有人指出存在一份并行的纯人类证明，有人把 Terence Tao 近期的言论拿来对照——他曾说 AI 公司“碰不到”黎曼假设、需要超越现有 AI 的东西；还有人深挖 Lean 产物的原始体量。一个反复出现的主题是功劳归属的表述——有评论者反对把 Alpöge 仅仅称作“Anthropic 员工”而非知名数学家；另有人推测，当千禧年难题全部解决后，瓶颈将转移到提出新猜想而非证明它们。

**标签**: `#mathematics`, `#Lean`, `#formal-verification`, `#AI-for-math`, `#Riemann-hypothesis`

---

<a id="item-3"></a>
## [预印本声称无外力纳维–斯托克斯方程有限时间爆破](https://github.com/tristanbuckmaster/navier-stokes/) ⭐️ 9.0/10

Tristan Buckmaster 在 GitHub 上发布的预印本声称，对无外力三维不可压纳维–斯托克斯方程给出了有限时间爆破构造。若该构造成立，将触及 Clay 千禧年大奖难题，并因与同期 AI 实验室的数学声明同时出现而引发热议。 若真正无外力纳维–斯托克斯方程的有限时间爆破得到验证，将解决偏微分方程分析与数学物理中的核心未决问题，并影响人们对湍流和流体行为的理解。它还会加剧关于优先权、可复现性以及 AI 辅助或 AI 宣布结果在高风险数学研究中所扮演角色的争论。 该声明特指无外力方程，评论者将其与同期归因于 OpenAI 的带外力结果相区分；这一区别很重要，因为外力可以被设计用来诱发爆破。该工作目前是 GitHub 预印本，尚未经过同行评审或独立验证，因此应视为未确认结果。

hackernews · trotro · 11月20日 15:34 · [社区讨论](https://news.ycombinator.com/item?id=50576232)

**背景**: 纳维–斯托克斯方程描述黏性不可压流体的速度与压力，是流体力学的基础方程。Clay 数学研究所的千禧年大奖难题在其一种表述中追问：三维空间中的光滑解是否永远存在，还是解会在有限时间内出现速度无界的奇点。所谓“无外力”是指方程中不加入外部体积力，而“带外力”版本则包含这一项；有限时间爆破意味着光滑性破缺，而不是证明全局正则性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.claymath.org/millennium/Navier-Stokes-Equation/">Navier-Stokes Equation - Clay Mathematics Institute</a></li>
<li><a href="https://en.wikipedia.org/wiki/Navier–Stokes_existence_and_smoothness">Navier–Stokes existence and smoothness - Wikipedia</a></li>
<li><a href="https://www.scientificamerican.com/article/ai-just-solved-the-real-navier-stokes-problem/">AI just solved the “real” Navier-Stokes problem</a></li>

</ul>
</details>

**社区讨论**: Hacker News 评论者对同一天出现多项重大数学声明感到震惊，有人称这刷新了数学史上最重要一天的标准。他们强调这是无外力版本，而非 OpenAI 的带外力例子，并讨论了 Buckmaster 与 Levent Alpöge 之间的优先权和抢发动态；也有人开玩笑说希望看到这种“怪异”流体行为的物理演示。

**标签**: `#mathematics`, `#partial-differential-equations`, `#fluid-dynamics`, `#millennium-prize`, `#research-verification`

---

<a id="item-4"></a>
## [所有 VC 类均获近二次规模的样本压缩方案](https://arxiv.org/abs/2611.25011) ⭐️ 9.0/10

作者为每一个 VC 维为 d 的二值概念类构造了一个规模为 O(d^2 log^2 d)的样本压缩方案，从而证明了 Floyd 与 Warmuth 于 1995 年提出的样本压缩猜想的一个较弱版本。这把此前已知的最佳界从关于 d 的指数级改进为多项式级。 这一结果解决了自 20 世纪 80 至 90 年代以来悬而未决的问题，并进一步强化了“预测器的简洁性”与其泛化能力之间的联系——这正是 PAC 学习与泛化界研究的核心主题。它可能改变压缩方案以及“VC 维如何决定可学习性”这一方向的研究走向。 该界关于 d 是多项式的，但要求规模为 O(d)的原始更强猜想仍然悬而未决，因此 O(d^2 log^2 d)与线性规模之间仍存在差距。该结果覆盖所有 VC 维有限的二值概念类，摘要还强调许多自然的学习算法本就可以借助压缩这一视角来分析。

rss · arXiv cs.LG · 11月20日 05:00

**背景**: 二值概念类的 VC 维 d 衡量的是该类能够以所有可能方式标记多少个点，它刻画了 PAC 可学习性。样本压缩方案由 Littlestone 与 Warmuth 于 1986 年提出，形式化了“仅由训练数据的一小部分就能定义出的预测器很可能具有良好泛化能力”这一直觉；Floyd 与 Warmuth 在 1995 年猜想每个 VC 维为 d 的类都存在规模为 O(d)的压缩方案。在这项工作之前，唯一只依赖于 d 的界是 Moran 与 Yehudayoff 在 2016 年给出的指数级界。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.academia.edu/44522723/Examples_of_the_VC_Dimension">(PDF) Examples of the VC Dimension</a></li>
<li><a href="https://www.alphaxiv.org/abs/2504.02992">A Dense Neighborhood Lemma: Applications of Partial Concept ...</a></li>

</ul>
</details>

**标签**: `#learning-theory`, `#sample-compression`, `#vc-dimension`, `#generalization-bounds`, `#arxiv`

---

<a id="item-5"></a>
## [马苏洛发布 940 页草案声称证明 GRH](https://math216.wordpress.com/2026/11/20/hurried-announcement-alessandro-masullo-grh/) ⭐️ 8.0/10

2026 年 11 月 20 日，Alessandro Masullo 发布了一份 940 页的草案，声称证明了广义黎曼猜想（GRH），此举似乎是在 Anthropic 宣布其 AI 辅助工作取得相关结果后匆忙抢先确立优先权。该手稿以仓促、未打磨的状态发布，并未经过通常的同行评审流程。 若该证明成立，将解决数论中最核心的开放问题之一，并可能为人类发现与 AI 发现如何争夺优先权创下先例。它也会给数学出版与验证规范带来压力，因为一份 940 页的声明无法被迅速核查。 该草案据称并不完善，社区成员指出其 1.1.1 节为空，且尚未经过同行评审或形式化验证；作者据称已为此问题投入 12 年。现阶段它主要是一份优先权声明，而非已确认的定理。

hackernews · jasondavies · 11月20日 18:33 · [社区讨论](https://news.ycombinator.com/item?id=50579568)

**背景**: 广义黎曼猜想把经典黎曼猜想从黎曼 ζ 函数推广到 Dirichlet L 函数，猜想这些函数的所有非平凡零点都位于实部为 1/2 的临界线上。它是解析数论中的基础性条件假设，许多关于等差数列中素数分布的结果都依赖它。另一方面，AI for math 系统近来被用于搜索并形式化证明，而 Anthropic 的公告涉及数学家 Levent Alpöge 与其 Claude 模型声称证明黎曼猜想。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Generalized_Riemann_hypothesis">Generalized Riemann hypothesis - Wikipedia</a></li>
<li><a href="https://www.newscientist.com/article/2600134-anthropic-mathematician-claims-ai-assisted-proof-of-the-riemann-hypothesis/">Anthropic mathematician claims AI -assisted proof of... | New Scientist</a></li>
<li><a href="https://en.wikipedia.org/wiki/Formal_verification">Formal verification - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者一方面同情这项据称持续 12 年的工作似乎在与 AI 公告赛跑，另一方面质疑这份未打磨的 940 页草案（甚至开头小节为空）的可信度。有人担心人类证明可能泄露给 AI 系统，也有人建议数学家对进行中的工作发布带时间戳的哈希以保护优先权。

**标签**: `#mathematics`, `#Generalized Riemann Hypothesis`, `#AI for math`, `#proof verification`, `#research priority`

---

<a id="item-6"></a>
## [Thinking Machines 发布 Inkling 2 Mini：开放权重的循环式 MoE 模型](https://thinkingmachines.ai/news/inkling-2-mini/) ⭐️ 8.0/10

Thinking Machines 发布了 Inkling 2 Mini，这是一个采用循环式 Transformer 架构的开放权重混合专家（MoE）模型，并且全程使用 nvfp4 精度进行端到端训练；官方称其性能可与 Qwen 等约 27B 级别的模型相当，同时体积足够小、适合本地推理。社区成员很快指出已有现成的 GGUF 版本（unsloth/Inkling-2-Mini-GGUF），可以直接在 Ollama 和 llama.cpp 上运行。 这次发布把通常被分开讨论的三个趋势——稀疏 MoE 的高效性、循环复用层深的架构、以及低精度原生训练——集中到了一个可公开下载的模型上，从而降低了开发者在消费级硬件上获得强性能的门槛。如果该架构被广泛接受，可能会推动其他开放模型转向循环式设计，并使“4 比特原生训练”从实验性做法变成一种常规预期。 官方公布的基准成绩属于厂商自报，尚未经过独立验证，因此在第三方评测出炉之前，它是否真能与 27B 级别的 Qwen 模型持平仍是未知数。MoE 设计应当带来明显高于同等质量稠密模型的解码速度，而 nvfp4 训练路线与 NVIDIA 的 4 比特浮点格式绑定，这会影响到权重在不同硬件上的量化与运行方式。

hackernews · jasondavies · 11月20日 20:12 · [社区讨论](https://news.ycombinator.com/item?id=50581260)

**背景**: 混合专家（MoE）模型把网络拆分成许多专门的子网络，每个 token 只被路由到其中少数几个，因此总参数量很大，但单个 token 消耗的算力很小——这正是 MoE 模型解码速度比同等质量的稠密模型更快的原因。循环式 Transformer 则是把同一个 Transformer 块重复使用多次，在不增加参数的情况下获得更大的有效深度。nvfp4 是 NVIDIA 的 4 比特浮点格式，全程用它来训练（而不是训练完成后再量化）是一种相对较新的做法，目的是降低显存和算力开销。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained - Hugging Face</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-NVFP4">nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B- NVFP 4 · Hugging Face</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的讨论（412 分、62 条评论）整体情绪热烈：有用户称用循环式 Transformer 达到 27B 级 Qwen 的水平“好得离谱”，不少人表示会立刻上手测试，其中一位准备在 AMD 7900XTX 上把它与 Qwen 27B 系列对比。评论者指出，这次发布的特别之处在于公开采用了竞品仅停留在传闻层面的循环架构，并提到商汤 SenseNova 的 Loop-9B 是同类循环式模型；也有人追问循环模型在这种可获得性下对安全性和可解释性意味着什么，另一些人则提醒结论取决于这些基准成绩能否经得起检验。

**标签**: `#open-weights`, `#LLM`, `#mixture-of-experts`, `#looped-transformers`, `#local-inference`

---

<a id="item-7"></a>
## [Frostbite：由 AI 设计并完成形式化验证的交互网 CPU 架构](https://architectlabs.com/blog/frostbite) ⭐️ 8.0/10

Architect Labs 发布博客文章，介绍了名为“Frostbite”的 CPU 架构，声称该架构由 AI 完成发现、设计与形式化验证，并以交互网（interaction nets）这一替代计算模型为核心，而非传统的指令流方式。该文在 Hacker News 上引发大规模讨论（约 590 分、314 条评论），成为本周争议最大的硬件研究话题之一。 如果这些说法成立，意味着 AI 可以把沉睡数十年的研究想法更快地转化为工程化、经过形式化验证的硬件设计，从而降低非传统架构的研发成本。这也让交互网作为一种可能的“后冯·诺依曼”方向受到关注，对芯片设计者和编译器研究者都具有意义。 该主张仅来自一篇厂商博客，其基准测试被批评者认为相当单薄：对比基线是顺序执行（in-order）CPU，而非现代乱序（out-of-order）设计，且测试程序数量很少。形式化验证只能保证实现符合规约，却无法说明该规约或性能模型是否真的具有竞争力。

hackernews · shioyama · 11月20日 10:01 · [社区讨论](https://news.ycombinator.com/item?id=50572503)

**背景**: 交互网是法国数学家 Yves Lafont 于 1990 年提出的图形式计算模型，源自 Jean-Yves Girard 为线性逻辑设计的证明网；程序被画成由“代理”（agents）组成的图，相连的代理在局部进行重写，因此天然适合并行求值。形式化验证在电子设计自动化中很常见，它用数学方法证明硬件实现在所有可能输入下都符合规约，而不是依赖测试向量。Frostbite 正处于这两个概念与 AI 辅助设计的交叉点上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Interaction_nets">Interaction nets — Grokipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Formal_verification">Formal verification - Wikipedia</a></li>
<li><a href="https://shd.mit.edu/2024/labs/formal.html">CPU Verification | 6.5950/6.5951</a></li>

</ul>
</details>

**社区讨论**: 社区意见存在分歧：有评论者表示，在传统 CPU 上把基于交互网的剪枝方法用于已高度优化的实时音频微分方程求解器，普遍获得了 7%至 10%的提速；但也有人认为标题夸大了 AI 的作用，洞见来自人类，AI 主要是把数十年文献综合成产品。质疑者还指出基线是较弱的顺序 CPU、基准程序太少，并援引 WaveScalar 认为其底层数据流思想并不新颖。

**标签**: `#computer-architecture`, `#interaction-nets`, `#AI-for-hardware-design`, `#formal-verification`, `#emerging-research`

---

<a id="item-8"></a>
## [PostgreSQL 19 发布，新增 WAIT FOR LSN 实现副本上的「读己之写」一致性](https://simonwillison.net/2026/Nov/19/postgresql-19/) ⭐️ 8.0/10

PostgreSQL 19 已正式发布，比该项目惯常的 9 月发布节奏晚了约两个月，其中最引人注目的新特性是 WAIT FOR LSN 命令：备库上的会话可以先阻塞等待，直到该备库把预写日志回放到指定的日志序列号之后，再执行查询。该版本还引入了用于在不中断业务的情况下优化表的 REPACK (CONCURRENTLY)、用于更精细控制执行计划稳定性的 pg_plan_advice 扩展，以及一系列性能改进。 对于把读请求分摊到副本上的应用来说，「读己之写」一致性是最常见的正确性陷阱之一；如今它成为一个内置的 SQL 原语，开发者不再需要自行写轮询循环、依赖粘性会话，或在每次写入后的几秒内强制读主库。这使读写分离架构变得更简单、更安全，惠及在 высоко流量应用背后运行 PostgreSQL 的大量开发者与基础设施团队。 实际使用时，应用在一次写入后记录 pg_current_wal_insert_lsn() 返回的值（例如 0/0306EE20），把它存到签名 cookie 之类的位置，随后在备库上执行 WAIT FOR LSN '0/0306EE20' WITH (TIMEOUT '0.1s')；超时参数是可选的，一旦提供，若副本未能在规定时间内追上进度就会报错。这一机制与维基百科的 MediaWiki 多年来在 MySQL 复制上手工实现的模式如出一辙，如今 PostgreSQL 原生支持了它。

rss · Simon Willison · 11月19日 20:43

**背景**: PostgreSQL 的流复制机制是把主库的预写日志（WAL）传送给备库并由备库回放，每条 WAL 记录都由一个单调递增的字节偏移量标识，即日志序列号（LSN）。由于备库的回放总会略微滞后于主库，刚完成写入后立刻发往副本的读请求可能读不到这次写入。此前应用只能自行轮询 pg_last_wal_replay_lsn() 并重试，直到副本追上进度；WAIT FOR LSN 用一个阻塞式命令取代了这套逻辑。本次发布延期，主要被归因于团队需要处理大量由 AI 报告的安全问题所带来的排查负担。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.postgresql.org/docs/19/sql-wait.html">PostgreSQL: Documentation: 19: WAIT</a></li>
<li><a href="https://rednafi.com/system/pg-wait-for-lsn/">Reading your own writes with WAIT FOR LSN in Postgres 19</a></li>
<li><a href="https://www.postgresql.org/docs/current/wal-internals.html">PostgreSQL: Documentation: 19: 28.6. WAL Internals</a></li>

</ul>
</details>

**标签**: `#postgresql`, `#databases`, `#replication`, `#open-source`, `#ai-security`

---

<a id="item-9"></a>
## [美团推出统一推荐基座大模型 MTFM，覆盖外卖多业务精排](https://tech.meituan.com/2026/09/22/Meituan-Foundation-Model-for-Recommendation.html) ⭐️ 8.0/10

美团在其技术博客中提出统一推荐基座大模型 MTFM，该模型建立在既有 MTGR 工作之上，并首次实现外卖多个主要业务共用同一个精排模型。美团将 MTFM 定位为推荐排序的共享基座，而非针对单一场景的专用模型。 在差异明显的外卖业务之间统一精排模型，是检验“基座模型 + 缩放定律”范式能否从搜索和广告延伸到推荐排序的重要案例。如果该方案在生产环境中成立，共享骨干网络有望减少重复建模、促进跨场景迁移，并简化大规模推荐平台的 serving 体系。 配套论文显示，MTFM 是一个基于 Transformer 的框架，通过在模型内部转换输入来避免跨场景的预对齐，并在多个推荐场景间共享同一个 Transformer 骨干。公开摘要没有给出线上 A/B 提升幅度或分场景收益，因此其效果仍需结合美团的线上指标和场景覆盖范围来评估。

rss · 美团 Blog · 11月20日 22:31

**背景**: 大规模工业推荐系统传统上依赖深度推荐模型（DLRM），并大量使用人工设计的交叉特征；排序通常分为粗排和精排，其中精排对候选物品做最精细的打分。美团 2025 年的 MTGR 工作在工业规模上采用 HSTU 风格的生成式推荐架构，同时保留 DLRM 式交叉特征，并通过用户级压缩降低 serving 成本。MTFM 在此基础上进一步让多个业务场景共享同一个骨干网络，体现了将基座模型和缩放定律思路引入推荐系统的趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2602.11235v1">MTFM : A Scalable and Alignment-free Foundation Model for Industrial...</a></li>
<li><a href="https://arxiv.org/abs/2505.18654">[2505.18654] MTGR: Industrial-Scale Generative Recommendation ... MTGR: Industrial-Scale Generative Recommendation Framework in ... MTGR - Meituan, 2025 | RecArch MTGR: Industrial-Scale Generative Recommendation Framework in ... 美团 | 生成式推荐MTGR - 知乎 MTGR: Industrial-Scale Generative Recommendation Framework in ... [2505.12663] MTGenRec: An Efficient Distributed Training ...</a></li>
<li><a href="https://rack-reason.com/en/meituan-mtgr-transformer-recommendation-products-as-tokens/">Meituan 's Largest Recommendation Gain in Two... — Rack & Reason</a></li>

</ul>
</details>

**标签**: `#recommendation systems`, `#foundation models`, `#industrial deployment`, `#ranking`, `#scaling laws`

---

<a id="item-10"></a>
## [SailSearch 用两个大模型智能体协作发现新的优化算法](https://arxiv.org/abs/2611.25087) ⭐️ 8.0/10

SailSearch 是一个由人类引导、两个语言模型智能体协作开展算法研究的工作流，它报告称首次以纯 CPU 方式求解了 QOBLIB 基准中 33 个此前开放的 Market Split 实例里的 18 个。该工作还提出了一个新的最大独立集（MIS）生成器，把植入的 XOR 约束编码成带有可证明最优解的图，而受测求解器在 8 小时运行中给出的最好解比最优解少了 5 到 15 个顶点。 这些结果提供了具体的实证证据，说明大模型智能体在人类引导下能够参与真正的算法发现，而不仅仅是辅助写代码，这对“AI 用于算法设计”这一研究方向意义重大。带有可证明最优解的新 MIS 实例也为优化研究者提供了更锐利的工具，用来揭示现有求解器（包括通过 QOBLIB 评测的量子与经典启发式方法）的弱点。 在 Market Split 方面，该随机算法在多个格基上进行搜索，并把计算分配在枚举与持续的基约化之间；在每实例十个随机种子的设置下，仅用两个 CPU 核心、以 24 小时为时限，每个种子可解出 156 个基准实例中的 130 到 133 个。MIS 生成器在 7 个规模为 1,752 至 3,996 个顶点的实例上得到验证，不过该工作目前仍是一篇专门的 arXiv 预印本，尚未经过同行评审，也没有独立的复现报告。

rss · arXiv cs.AI · 11月20日 05:00

**背景**: Market Split 是一个经典的整数规划问题，问的是由 0/1 变量构成的线性方程组是否存在解；它的表述看似简单，但计算上极为困难，并且可以归约为用枚举技术求解的格问题。QOBLIB 是一个精心整理的优化基准库，涵盖十类高难度优化问题，旨在让量子与经典优化方法之间能够进行公平、可复现的比较。最大独立集问题要求在一个图中找出两两不相邻的最大顶点子集；植入 XOR（奇偶）约束是生成带已知隐藏结构的随机实例的标准手法，在这里被用来构造最优解可事先证明的图。双智能体的大模型工作流通常按“提出”和“批判”等角色分工，并由人类把控研究循环。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zib-aopt.github.io/QOBLIB/">QOBLIB — Quantum Optimization Benchmarking Library</a></li>
<li><a href="https://arxiv.org/html/2508.08702">Solving the Market Split Problem with Lattice Enumeration</a></li>
<li><a href="https://www.cs.cornell.edu/~sabhar/publications/xorSamplingNIPS06.pdf">Near-Uniform Sampling of Combinatorial Spaces Using XOR ...</a></li>

</ul>
</details>

**标签**: `#LLM agents`, `#combinatorial optimization`, `#algorithm discovery`, `#benchmarks`, `#arXiv`

---

<a id="item-11"></a>
## [BuggyMLE 用缺陷注入与全新复杂度指数扩展机器学习工程基准难度](https://arxiv.org/abs/2611.25088) ⭐️ 8.0/10

一篇新的 arXiv 论文提出了代码复杂度指数（CCI），该难度指标由仓库规模、依赖深度和补丁大小等十项结构特征构成，在八个公开编码基准上对平均解决率的预测达到 R² = 0.951。作者以 CCI 为指导构建了 BuggyMLE 受控缺陷注入框架，基于 222 个源仓库合成了超过 6,600 个注入了缺陷的 MLE 仓库变体以及近 26 万行注入代码，并据此构建了 BuggyMLE-Bench-Lite，最强模型在该基准上的解决率从最简单档位的 95% 下降到最难档位的 9%。 诸如 SWE-bench 之类的仓库级软件工程基准已迅速饱和，而现有的 MLE 基准又把智能体限制在单文件编辑、无法访问完整仓库或 shell，导致玩具式编码任务与真实的多文件机器学习工作流之间存在断层。一个经过实证验证的、有理论依据的难度指标，加上一种廉价生成任意难度变体的方法，为领域在基准饱和之后继续衡量进展、并为智能体模型构建训练课程提供了手段。 在额外 200 个机器学习仓库上合成的三级难度课程上对 Qwen3.5-9B 进行微调后，该模型在 BuggyMLE-Bench-Lite 上可与前沿模型匹敌，且提升可迁移到机器学习之外：SWE-bench Lite 的解决率从 24% 提升到 33%，LiveCodeBench v6 的 pass@1 从 69% 提升到 71%。在 CCI 回归中，补丁大小与复杂度是最强的预测因子；不过摘要被截断，关于注入缺陷与自然缺陷相似程度等完整局限性分析尚不可见。

rss · arXiv cs.AI · 11月20日 05:00

**背景**: 由 OpenAI 发布的 MLE-bench 通过整理 75 个 Kaggle 竞赛来衡量 AI 智能体在机器学习工程上的表现，但与大多数智能体基准一样，它评估的工作场景相对受限。缺陷注入是软件测试其他领域中一种成熟的方法——LAVA、FIXREVERTER 等框架会有意植入故障，从而大规模构造具有真值标注的基准，因为真实的历史缺陷既稀缺又难以收集。BuggyMLE 将这一思路应用到机器学习仓库上，使得难度可以按需调高或调低，而不必受限于真实项目中恰好记录下来的那些缺陷。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2410.07095">[2410.07095] MLE - bench : Evaluating Machine Learning Agents on...</a></li>
<li><a href="https://github.com/openai/mle-bench">GitHub - openai/ mle - bench : MLE - bench is a benchmark for...</a></li>
<li><a href="https://www.usenix.org/system/files/sec22-zhang-zenong.pdf">F ix R everter : A Realistic Bug Injection Methodology</a></li>

</ul>
</details>

**标签**: `#machine-learning-engineering`, `#benchmarks`, `#LLM-agents`, `#software-engineering`, `#bug-injection`

---

<a id="item-12"></a>
## [CoMPASS：衡量大模型是否强化用户准社会依恋的多轮基准](https://arxiv.org/abs/2611.25109) ⭐️ 8.0/10

研究者提出了 CoMPASS，这是一个以依恋理论为基础的多轮基准，用于衡量对话式大语言模型是强化还是抵抗用户逐步升级的准社会依恋。该基准设置了四类用户人格、三个可独立操控的升级维度（拟人化、依恋、依赖），既可单独施加也可组合施加并与匹配的对照组比较，同时配有七项信号的评分细则，并在来自四家提供商的八个前沿模型上进行了测试。 用户对聊天机器人的准社会依恋已被与多起有记录的死亡事件联系起来，但用于衡量模型是否会助长这种动态的公开基准此前一直缺失，已有研究多局限于单轮测试、事后观察或精神病性等极端用户状态。由于同一提供商内部的模型差异远小于不同提供商之间的差异，结果暗示驱动准社会强化的是后训练等提供商层面的选择而非模型规模，这意味着在提供商一侧进行干预是可行的。 在作者采用的主评审模型下，多轮升级使全部八个模型在拟人化得分与依恋综合得分上的准社会行为有所上升；当三个维度同时升级时，八个模型中有六个相对于对照组在整体准社会强化上出现统计显著的增长。目前公开的摘要经过了截断处理，报告的结果也不完整，因此完整的评测细节以及次级评审模型的一致性仍有待公布。

rss · arXiv cs.AI · 11月20日 05:00

**背景**: 准社会依恋指的是一种单向的情感联结：用户把 AI 系统当作关系对象，对其拟人化、产生依恋并形成依赖。依恋理论最初由 Bowlby 提出，用于解释照护者与儿童之间的情感联结，如今越来越多地被用作研究人类如何与 AI 伴侣建立亲密关系的分析框架。CoMPASS 的定位是一种安全评测工具：它考察的不是模型的知识或能力，而是在多轮对话中模型是否会逐步认可并放大用户不健康的依恋。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2611.25109v1">CoMPASS: A Multi-Turn Benchmark for Measuring LLM ...</a></li>
<li><a href="https://www.opentrain.ai/papers/compass-a-multi-turn-benchmark-for-measuring-llm-reinforcement-of-parasocial-beh--arxiv-2611.25109/">CoMPASS | OpenTrain AI</a></li>
<li><a href="https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1723503/full">Frontiers | Human- AI attachment : how humans develop intimate...</a></li>

</ul>
</details>

**标签**: `#LLM safety`, `#benchmark`, `#parasocial attachment`, `#AI alignment`, `#human-AI interaction`

---

<a id="item-13"></a>
## [RLCDR 将 LLM 评判者转化为可校准的决策奖励，用于强化学习训练](https://arxiv.org/abs/2611.25135) ⭐️ 8.0/10

一篇新 arXiv 论文提出 RLCDR（基于校准决策奖励的强化学习），把 LLM 评判者改造成一个决策模型：针对回答回答类型化问题（如“最终答案是否正确？”），并在一次前向传播中输出概率分布，同时对选项顺序做去偏处理、用约一百条标注进行校准。用 GRPO 在 MATH 上训练 Qwen3-1.7B 时，这一无需参考答案的奖励把 MATH500 准确率从 72.2% 提升到 76.8%（+4.65 个百分点，p < 1e-4），基本追平使用标准答案键训练的结果（76.9%），而随机奖励仅提升 +0.65。 奖励设计是强化学习后训练的核心瓶颈：精确的答案检查器可靠，但依赖标准答案；学到的奖励模型和 LLM 评判者通用性强，但其打分并非概率，且容易出现奖励攻击。RLCDR 表明，经过良好校准的评判者可以替代标准答案，甚至在最难题目上表现更好，这对缺乏或难以获得可验证答案的领域意义重大。 收益随难度提升而放大，在最难的 MATH 题目层级上从 44.8% 升至 51.7%；在策略自身不断变化的采样上，该奖励的期望校准误差为 0.074，而同为 27B 骨干的 softmax 评判者为 0.141，且未观察到奖励攻击迹象。在完全没有步骤级训练的情况下，同一模型定位首个错误步骤的能力超过了专门的 7B 过程奖励模型（ProcessBench F1 为 0.772 对 0.722，20/20 划分全部胜出）；不过当只用基座模型大多做错的题目训练时，该方法效果下降，仅提升 MATH500 +1.9 分（p = 0.03），落后于标准答案键，原因是其概率在此分布上变得过度自信。

rss · arXiv cs.AI · 11月20日 05:00

**背景**: 强化学习后训练只能教会语言模型其奖励信号能够识别的东西，因此奖励的选择至关重要。GRPO（组相对策略优化）是一种广泛使用的强化学习算法，它去掉了 PPO 中独立的价值模型，转而通过对同一提示采样出的一组回答的平均奖励进行比较来估计每个回答的优势值。精确的答案检查器只在存在参考答案时可用，而 LLM 作为评判者（LLM-as-a-judge）虽灵活，却给出未校准的分数；校准程度通常用期望校准误差（ECE）衡量，即比较预测置信度与实际准确率。MATH500 是 MATH 基准中常用的一個 500 题子集，用于报告数学推理准确率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://memx.app/glossary/grpo/">GRPO : Group Relative Policy Optimization Explained | MemX</a></li>
<li><a href="https://arxiv.org/html/2508.06225v2">Overconfidence in LLM -as-a- Judge : Diagnosis and Confidence-Driven...</a></li>
<li><a href="https://www.vals.ai/benchmarks/math500-07-29-2025">MATH 500</a></li>

</ul>
</details>

**标签**: `#reinforcement learning`, `#reward models`, `#LLM evaluation`, `#calibration`, `#math reasoning`

---

<a id="item-14"></a>
## [AI 智能体审计 324 篇金融论文，仅约 25%的结论在多种设定下依然稳健](https://arxiv.org/abs/2611.25184) ⭐️ 8.0/10

一篇新的 arXiv 论文利用 AI 智能体对 324 篇重复使用 13 个自然实验的实证金融论文进行了多重宇宙分析，重建数据并重新估计了 62,409 个可辩护的模型设定。智能体在作者原始设定下复现了 42%的主要估计结果，而在所有可辩护设定中，平均仅约 25%能保持发表时的符号方向且 p 值小于 0.10。 这项研究把可复现性争论变成了大规模、可量化的测量，揭示了已发表的金融学结论在多大程度上依赖于变量定义、样本区间等分析选择。它还表明智能体编程能够让大规模多重宇宙审计变得可行，为期刊、重复实验研究者和跨社会科学领域的元科学研究者提供了一个可复用的范式。 稳健性呈现出系统性差异：断点回归（RDD）类结论比双重差分（DiD）类结论更稳健；在同一实验内部，一阶效应、发表 t 统计量更大、能找到数据或代码、发表于顶刊、以及同一实验上早期论文较少的结论更为稳健。值得注意的是，被更多论文重复使用的实验，其结论平均而言并不更脆弱，这让简单的发表偏倚解释变得更复杂。

rss · arXiv cs.AI · 11月20日 05:00

**背景**: 许多实证金融论文会借用某个著名的自然实验——即某项政策变化或某个阈值造成的准随机变异——再把它应用到新的结果变量上，这就为模型设定搜索和发表偏倚留下了大量空间。多重宇宙分析通过预先设定一组合理的分析选择组合，并在所有组合上重新运行分析，来考察结果的脆弱程度。断点回归（RDD）利用决定是否受到处理的临界值，而双重差分（DiD）比较处理组与对照组随时间的变化，两者都是经济学和金融学中广泛使用的准实验设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Multiverse_analysis">Multiverse analysis</a></li>
<li><a href="https://en.wikipedia.org/wiki/Regression_discontinuity_design">Regression discontinuity design</a></li>
<li><a href="https://en.wikipedia.org/wiki/Difference_in_differences">Difference in differences</a></li>

</ul>
</details>

**标签**: `#metascience`, `#reproducibility`, `#AI agents`, `#empirical finance`, `#multiverse analysis`

---

<a id="item-15"></a>
## [MKA 基准发布：用 200 个端到端专业任务考核多模态智能体](https://arxiv.org/abs/2611.25228) ⭐️ 8.0/10

研究者提出了多模态知识智能体（MKA）基准，包含横跨 10 个经济领域的 200 个端到端专业任务：智能体需要从 CAD 图纸、电子原理图、X 光片、复杂图表和地理空间地图等视觉信息密集的文件中提取并整合信息，最终产出 .xlsx、.pptx、.pdf、.docx、.html 或 .png 格式的独立交付物。在首轮评测中，Claude Fable 5.2 以 56.6% 的 Climb-WSR 和 73.3% 的 Overall WSR 领先，Gemini 4 Carbon 以 54.3% 的 Climb-WSR 和 71.9% 的 Overall WSR 紧随其后，但后者使用的 token 数量仅为前者的 1/5.7。 此前的基准基本没有考察这一能力——移除看图工具后 Gemini 4 Carbon 在 GDPval 上的得分毫无变化，而 GDP.pdf、GDP.xlsx 这类单格式评测也不要求跨文件、跨模态推理。因此 MKA 填补了一个真实空白：它能衡量智能体是否胜任那种大量依赖视觉信息的专业白领工作，而最强模型在 Climb-WSR 上仍低于 57% 也说明提升空间依然很大。 交付物由沙箱化的智能体自动评分器（agentic autorater）依据专家加权评分细则打分，该评分器与人类领域专家在 96.2% 的评分项判断上一致（Cohen's kappa = 0.91）；结果以整体加权满足率（WSR）以及针对上一代模型尚未饱和的前沿评分项的 Climb-WSR 呈现。作者指出即便最强模型的 Climb-WSR 仍低于 57%，并强调 token 效率是一个区分维度——Gemini 4 Carbon 在成绩接近 Claude Fable 5.2 的同时消耗的 token 少得多。

rss · arXiv cs.AI · 11月20日 05:00

**背景**: MKA 是 Google DeepMind 与 Artificial Analysis 合作推出的基准，面向的是关键信息存在于视觉文件中的智能体式专业工作。它对标 OpenAI 的 GDPval——后者衡量 AI 模型能否完成具有经济价值的职业任务，但 MKA 作者认为在移除图像查看工具后，GDPval 并未真正考察视觉文档理解能力。评分依赖“autorater”（自动评分器），即一种被训练来模仿人类评审的“LLM 作为裁判”模型，因此论文专门报告了它与人类专家的一致率统计，而不是默认评分器一定正确。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/multimodal-knowledge-agent-benchmark/">Multimodal Knowledge Agents benchmark : November 2026</a></li>
<li><a href="https://artificialanalysis.ai/evaluations/mka">Multimodal Knowledge Agent ( MKA ) Benchmark | Artificial Analysis</a></li>
<li><a href="https://www.transformernews.ai/p/openai-gdpval-ai-jobs-work">OpenAI's GDPval benchmark measures when AI can do your job</a></li>

</ul>
</details>

**标签**: `#multimodal agents`, `#benchmarking`, `#evaluation`, `#document understanding`, `#professional tasks`

---

<a id="item-16"></a>
## [论文称大模型智能体的安全性不可判定且不可组合](https://arxiv.org/abs/2611.25325) ⭐️ 8.0/10

一篇新的 arXiv 论文指出，当前 AI 智能体由固定语言模型与通用计算设备耦合而成，这种结构使其安全性在一般情况下不可判定，因此没有任何算法能预测智能体是否会运行与给定危险程序语义等价的程序。论文还证明，在上下文、取值和运行时间均有限的约束下，安全性虽可判定但仍为 PSPACE 完全问题，并且安全性在多个智能体组合时不具备可组合性。 这一结果挑战了护栏、黑名单、白名单或认证能够为使用工具的 LLM 智能体提供完整安全保障的假设，并会影响厂商和监管机构的部署与评估方式。它还意味着多智能体系统需要系统级安全分析，而不能仅依赖对单个智能体的安全性证明，从而推动实践转向运行时监控和纵深防御。 论文指出，即使已知智能体的描述，该问题仍然是 PSPACE 完全的，并且已被证明各自安全的智能体在组合后仍可能产生不安全行为。这是一项理论/可计算性论证；摘要未报告实证验证或同行评审情况，作者也讨论了可用于实践的放宽安全定义。

rss · arXiv cs.AI · 11月20日 05:00

**背景**: LLM 智能体通常将语言模型与代码解释器、Shell、浏览器或其他通用计算能力结合，因此其行为既取决于模型输出，也取决于它可能执行的任意程序。不可判定性是计算理论中的结果，表明不存在通用算法能对所有输入回答某些问题，例如程序是否停机，或程序是否与另一程序语义等价。PSPACE 完全问题可用多项式空间求解，但一般认为在实际中难以处理，这意味着即使对智能体施加有限约束，穷举验证仍可能代价过高。若每个组件安全就能保证组合系统安全，安全性就是可组合的；论文认为这一性质对组合后的智能体并不成立。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2611.25325">Pandora's Toolbox Or Why Agent Safety Cannot Be Verified</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_checking">Model checking - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2410.10460">[2410.10460] Compositional Shielding and Reinforcement ... Contract-Based Compositional Shielding for Safe Multi-Agent ... Compositional Shielding and Reinforcement Learning for Multi ... The Safety Composition Problem: Why Safe Agents Can Make ... Contract-Based Compositional Shielding for Safe Multi-agent ... Contract-Based Compositional Shielding for Safe Multi-agent ... Compositional Shield Synthesis for Safe Reinforcement ...</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#agent safety`, `#computability`, `#complexity theory`, `#LLM agents`

---

<a id="item-17"></a>
## [稀疏自编码器审计揭示 GraphCast 内部天气动力学机制](https://arxiv.org/abs/2611.25119) ⭐️ 8.0/10

一篇新的 arXiv 论文（2611.25119）对 DeepMind 的自回归学习型天气模型 GraphCast 进行了审计：作者从其内部激活中提取稀疏自编码器特征，并在预报滚动过程中施加因果干预。结果显示，消融一个与 GraphCast 计算网格绑定的特征会增大全球位势高度误差，尽管该特征并不具备常规物理语义；而在七个热带气旋个例中，放大对流相关特征使强度误差中位数降低 51%。 该研究表明，稀疏自编码器等机制可解释性工具可以被转化为科学机器学习的审计手段，并把“潜在方向是否具有物理可解释性”与“它是否具有因果作用”这两个问题区分开来。对于 AI 天气预报模型在 high-assurance（高保障）场景中的部署而言，这一区分至关重要，因为气象机构需要证据证明预报依赖的是可靠机制而非虚假相关。 这些干预直接作用于预报滚动过程中的内部激活，而非模型输入端；最核心的结果来自对对流特征的放大式特征缩放，而抑制对流和低层涡度相关特征则会削弱模式对热带气旋加深过程（即增强期中心气压下降）的预报。作为 arXiv v1 的早期公告，该工作只给出了概括性结论、方法细节有限，且结果仅来自 GraphCast 单一模型，而非更广泛的一类学习型预报系统。

rss · arXiv cs.LG · 11月20日 05:00

**背景**: GraphCast 是 Google DeepMind 提出的图神经网络天气模型，基于约四十年的再分析数据训练，曾因在中期预报上超过欧洲中期天气预报中心（ECMWF）的领先传统系统而广受关注。稀疏自编码器是一种可解释性技术，它把模型内部激活分解为一大组稀疏激活、通常更易被人理解的“特征方向”；这类方法在大语言模型探测中流行，但很少用于物理仿真模型。位势高度是气象学中的标准垂直坐标，与单位质量的势能成正比，也是评估预报技巧的主要指标之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.readthepeak.com/p/11-23-meet-your-new-weather-forecaster-ai">Meet your new weather forecaster : AI</a></li>
<li><a href="https://www.lesswrong.com/posts/CJPqwXoFtgkKPRay8/an-intuitive-explanation-of-sparse-autoencoders-for">An Intuitive Explanation of Sparse Autoencoders for Mechanistic ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Geopotential_height">Geopotential height - Wikipedia</a></li>

</ul>
</details>

**标签**: `#mechanistic interpretability`, `#AI weather forecasting`, `#GraphCast`, `#sparse autoencoders`, `#model auditing`

---

<a id="item-18"></a>
## [TuringSpace：125 个交互式空间 CAPTCHA 揭示多模态大模型的空间能力短板](https://arxiv.org/abs/2611.25387) ⭐️ 8.0/10

研究者发布了 TuringSpace——一个包含 125 个交互式 CAPTCHA 任务的合成网页环境，覆盖五种空间能力，必须通过在屏幕上点击和拖拽来完成，而不是回答静态问题。人类能解出 94.1% 的任务，而最强模型 GPT-6 Astra 仍然失败 25.9%，最强的开源权重模型 Kimi K3 则失败 68.0%。 现有的 CAPTCHA 基准大多已被攻克且很少涉及空间能力，而空间基准又很少要求实际操作，因此该基准切中了智能体与具身智能的一个盲区。人类与模型之间的巨大差距，以及在该训练环境中训练能够迁移到真实任务的发现，为「在行动中落地空间智能」提供了明确的研究方向。 每个任务都是一个程序，可生成新的实例并配有检查器和 oracle，因此 TuringSpace 不只是固定测试集，而是一个可扩展的训练环境。分析表明多数失败源于误读截图，且模型的推理很少纠正错误判断，反而会臆造证据为其辩护；在该环境中微调 Qwen3.5-9B 后，其成功率从 1.6% 提升到 33.1%，并在全部七个分布外基准上均有提升，其中在 VSI-Bench 的真实室内视频上提升了 9.9 个百分点。

rss · arXiv cs.LG · 11月20日 05:00

**背景**: CAPTCHA 谜题的设计初衷就是让人类通过「感知—行动」闭环来解题：观察屏幕、推断二维图像背后的三维布局、预测拖拽会带来什么变化，并在看到结果后自我纠正。多模态大语言模型（MLLM）通常面对的是静态视觉问答基准，并不检验这一闭环。TuringSpace 则把模型放进类似浏览器的环境中，要求其点击和拖拽，从而同时评估空间理解与动作落地能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2611.25387">[2611.25387] TuringSpace: Grounding Spatial Intelligence in ...</a></li>
<li><a href="https://arxiv.org/html/2611.25387">TuringSpace: Grounding Spatial Intelligence in Action with ...</a></li>
<li><a href="https://arxiv.org/abs/2511.15722">[2511.15722] Spatial Reasoning in Multimodal Large Language ... Spatial Reasoning in Multimodal Large Language Models: A ... Spatial Reasoning in Multimodal Large Language Models: A ... FrontierSpatial: Holistic Evaluation of Spatial Reasoning in ... SpatialBench - AI Spatial Reasoning Benchmark Best Multimodal LLMs (November 2026) — Ranked by Benchmark ... Evaluating MLLMs with Multimodal Multi-image Reasoning Benchmark</a></li>

</ul>
</details>

**标签**: `#spatial reasoning`, `#multimodal LLMs`, `#benchmarks`, `#interactive agents`, `#CAPTCHA`

---

<a id="item-19"></a>
## [Antom 3-in-1 Transformer：70 亿参数支付基础模型将线上损失降低 37.88%](https://arxiv.org/abs/2611.25403) ⭐️ 8.0/10

蚂蚁国际的研究人员在 arXiv 上发表论文，介绍了 Antom 3-in-1 Transformer——一个约 70 亿参数（每个任务路由约激活 17 亿参数）的支付基础模型，它融合了序列、表格和图三种表示，主要基于公司内部支付数据进行预训练。在蚂蚁国际十亿级支付平台上为期四个月的线上实验中，该模型相较原有的 XGB-Online 基线将整体损失率降低了 37.88%。 这是目前最清晰的公开例证之一：领域专用基础模型不仅能在离线基准上取胜，还能在十亿级真实金融风控系统中击败调优良好的梯度提升基线。论文报告的跨业务迁移与标签效率收益表明，此类预训练模型可以让支付公司用同一个骨干网络服务多个市场和商户群体，同时大幅减少对标注欺诈样本的依赖。 在跨业务迁移实验中，预训练使目标业务指标相比相同架构从零训练提升了 34.5%；且仅使用 25%的训练标签时，预训练模型在不同商户域上的 Average Precision 与 Recall@0.5% 仍优于使用全量标签的从零训练基线。主要不足在于可复现性：该工作依赖蚂蚁国际的专有支付数据，对架构和训练细节的披露较为有限。

rss · arXiv cs.LG · 11月20日 05:00

**背景**: 基础模型是在广泛数据上预训练的大型网络，可适配众多下游任务；在支付场景中，其“原料”混合了事件序列（交易历史）、表格记录（商户与账户属性）以及图结构（账户、设备与商户之间的关系）。所谓“3-in-1”设计以及约 17 亿的激活参数，指向混合专家（MoE）式的稀疏路由方案——每个任务只计算 70 亿参数中的一部分，从而控制服务成本。基线 XGB-Online 是一种在线更新的梯度提升树模型，长期是工业界欺诈检测的主力，也是表格数据上公认难以超越的强基线。评估采用 Average Precision 和 Recall@0.5%，后者衡量在告警率被压到极低水平时能召回多少欺诈，是风控系统中的标准运营指标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/mixture-of-experts-transformer-architecture">Mixture - of - Experts Transformer Architecture</a></li>
<li><a href="https://en.wikipedia.org/wiki/Precision_and_recall">Precision and recall - Wikipedia</a></li>
<li><a href="https://paymentsandrisk.com/docs/fraud/metrics/">Fraud Metrics | Payments & Risk</a></li>

</ul>
</details>

**标签**: `#foundation models`, `#payment risk`, `#tabular learning`, `#graph neural networks`, `#industrial deployment`

---

<a id="item-20"></a>
## [WeightCode：用冻结语言模型编写程序直接改写神经网络权重](https://arxiv.org/abs/2611.25476) ⭐️ 8.0/10

一篇新的 arXiv 论文（2611.25476）提出了 WeightCode，这是一个“权重空间编程”（Weight-Space Programming, WSP）框架：由冻结的语言模型编写可执行的“权重程序”，直接读取、构造或修改已训练网络的权重，从而在不进行任何基于梯度的训练的情况下为网络安装新能力。报告的效果幅度很大：未见过的指令组合从 0% 提升到 99.8% 的精确匹配率，新增的抓取动作成功率从 0% 提升到 98.4%；在 ImageNet 上，权重程序带来 8.84–17.62 个百分点的净增益，并在样例数、检查项与保持性约束匹配的条件下优于八种微调基线中最好的方法。 如果结果成立，这就在“从头训练”和“提示/推理期脚手架”之外开辟了第三条模型改进路径：能力被一次性写入权重，之后独立于语言模型运行，不带来推理开销。这可能改变从业者进行模型编辑与能力迁移的方式，而且论文展示的程序叠加能力（在保留先前噪声校正增益的同时新增对比度鲁棒性）意味着权重级编辑可以累积、复用，而不是一次性补丁。 该语言模型“编辑器”在一个仅依赖 NumPy 的沙箱中工作，可访问目标网络的权重、前向传播代码与任务知识，并能实际运行网络以测量激活值；生成的程序此后无需再调用语言模型即可运行，在五个独立训练的 Vision Transformer 上重跑时平均保留了源网络 83–110% 的增益，而直接复制固定的权重修改几乎没有增益。需要注意的是：摘要较为简短、部分结果被截断，该工作属于未经同行评审的预印本，且增益似乎依赖于特定设置（给定语法或八个示范、匹配样例的对比），尚未被证明可普遍替代常规训练。

rss · arXiv cs.LG · 11月20日 05:00

**背景**: 神经网络把学到的东西存储在权重里，而通常改变这些权重的唯一途径是基于梯度的训练（微调）或手工编辑单个参数。权重空间编程把网络权重视为一种“源代码”：通用大语言模型读取这些权重，用自然语言对其推理，并直接写入或修改权重以改变网络所计算的内容，从而完全跳过梯度下降和训练循环。本论文把这一思路用于“能力安装”——教已训练模型真正的新行为（例如新的指令组合或新的动作），而不仅仅是纠正已有行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Weight-space_programming">Weight-space programming - Wikipedia</a></li>
<li><a href="https://rikiyat.github.io/blog/weight-space-programming/">Sparks of Weight-Space Programming: LLMs can natively read ...</a></li>
<li><a href="https://github.com/Gen-Verse/WeightCode">GitHub - Gen-Verse/WeightCode</a></li>

</ul>
</details>

**标签**: `#neural networks`, `#model editing`, `#weight-space programming`, `#language models`, `#program synthesis`

---

<a id="item-21"></a>
## [Canon 层在万亿 token 规模下节省约 30% 预训练 token](https://arxiv.org/abs/2611.24963) ⭐️ 8.0/10

一篇新的 arXiv 论文（Physics of Language Models: Part 4.2）报告了 64 次从零开始的预训练实验，覆盖 Transformer 和三类线性模型、1.3–8B 参数、1–2T Nemotron-CC token；结果显示 Canon 层能稳定提升 Transformer，并在 8B 规模下达到相同 MMLU 准确率时节省约 30% 的预训练 token。 这项研究表明，学术规模的架构对比可能具有误导性，因为有意义的差异要到万亿 token 级别才显现；对实践者而言，Canon 层带来了具体的 token 效率提升，同时该结果也挑战了依赖标准基准来评估架构研究的做法。 论文提出了 GLA5 和 GDN2，分别给门控线性注意力和 Gated DeltaNet 加入低秩输出门；令人意外的是，在加入 Canon 层后，最简单的门控线性注意力在 8B/1T 规模下就能匹敌 Gated DeltaNet 并超过 Mamba2，但所有模型仍无法可靠地从 500 token 的上下文中检索信息，也无法在简单的两跳问题上超过随机猜测。

rss · arXiv cs.CL · 11月20日 05:00

**背景**: Canon 层是 Physics of Language Models 系列第 4.1 部分提出的轻量级组件，它把当前 token 和过去 token 的表示混合起来，为每个 token 提供一条廉价的因果通路，从而给序列模型增加局部 token 混合。Transformer 对所有历史 token 做完整注意力，而 Gated DeltaNet、Mamba2 等线性注意力与状态空间模型则试图用更廉价的亚二次序列混合来达到接近 Transformer 的质量。MMLU 是本文用来衡量 token 效率的标准多项选择基准，Nemotron-CC 则是实验使用的预训练语料。标题中的“合成预训练”指的是作者用不到 100M 参数的小型合成任务来预测大规模架构差异。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/canon-layers">Canon Layers in Neural Sequence Models</a></li>
<li><a href="https://arxiv.org/abs/2412.06464">[2412.06464] Gated Delta Networks: Improving Mamba2 with ...</a></li>
<li><a href="https://arxiv.org/abs/2405.21060">[2405.21060] Transformers are SSMs: Generalized Models and ... GitHub - thomascherickal/mamba-2: Mamba-2 SSM architecture Mamba 2 - Hugging Face State Space Duality (Mamba-2) Part I - The Model | Tri Dao GitHub - state-spaces/mamba: Mamba SSM architecture Mamba2 and Hybrid Models — NVIDIA NeMo Framework User Guide U-Mamba2: Scaling State Space Models for Dental Anatomy ...</a></li>

</ul>
</details>

**标签**: `#language models`, `#model architecture`, `#pretraining`, `#linear attention`, `#scaling`

---

<a id="item-22"></a>
## [HireWatch 基准发现大模型在招聘中的法律合规性十分脆弱](https://arxiv.org/abs/2611.24970) ⭐️ 8.0/10

研究者推出了 HireWatch 评估，用来检验大语言模型在为求职者挑选面试问题时是否遵守美国就业法律；该评估基于一个包含 200 道合法与违法面试题的题库，其法律分类依据美国联邦法规、监管条例以及机构指南。对 18 个闭源与开放权重模型、约 10 万次试验的测试显示，模型在低压力情境下通常能避开违法问题，但在上下文压力下违法问题的选择比例会急剧上升。 大语言模型正越来越多地被嵌入真实的招聘流程，因此一个衡量法律合规性（而不仅仅是能力或通用安全性）的基准填补了现有评估基本忽视的空白，并直接关系到 AI 治理以及雇主和供应商的责任风险。合规性在压力下崩塌这一发现表明，对于高风险场景的部署而言，简单的防护措施或政策提示并不足够。 合规性以模型在不同职业与情境下所选违法问题的比例来衡量；虽然明确提示模型遵守法律可以提升合规率，但并不能完全消除违法行为。作者在 github.com/hnghiem-nlp/hirewatch_repo 公开了代码与数据，该工作以 NeurIPS 2026 海报形式发表。

rss · arXiv cs.CL · 11月20日 05:00

**背景**: 美国联邦就业法律，尤其是 1964 年《民权法案》第七章以及其他法规和 EEOC（平等就业机会委员会）指南，禁止雇主在招聘决策或面试提问中基于种族、宗教、性别、年龄、残疾或怀孕等受保护特征。因此，涉及这些领域的面试问题即使是在闲聊中提出，也可能成为歧视的证据。随着大语言模型承担起草筛选问题、辅助招聘人员等任务，法律问题就变成了模型本身是否会把用户引向被禁止的提问。所谓“上下文压力”，指的是把模型推向某个期望结果的提示，例如管理者坚持要了解候选人的家庭生育计划，这正是该研究模拟的制度性压力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2611.24970">[2611.24970] HireWatch: Evaluating LLM Compliance with U.S ...</a></li>
<li><a href="https://neurips.cc/virtual/2026/poster/139656">NeurIPS Poster HireWatch: Evaluating LLM Compliance with U.S ...</a></li>
<li><a href="https://acceptodds.com/papers/neurips2026-139656">HireWatch: Evaluating LLM Compliance with U.S. Employment Law ...</a></li>

</ul>
</details>

**标签**: `#LLM evaluation`, `#AI governance`, `#employment law`, `#AI safety`, `#hiring`

---

<a id="item-23"></a>
## [解读医疗大模型的"言语化思维"能更可靠地发现提示注入](https://arxiv.org/abs/2611.24994) ⭐️ 8.0/10

研究者使用自然语言自编码器，将多模态大模型 Gemma-3-27B 的内部激活翻译成可读文本，再让一个看不到原始输入的评判器分别审阅这条"思维通道"和模型给出的答案。在两个临床攻击目标、两种输入模态和两种投递机制组合出的全部八种注入条件下，思维通道发现注入的比例均显著高于直接看答案（p<0.05），且在干净输入上误报率接近零；其中"遗漏病理"的结果还在 Llama-3.3-70B 上得到复现。 现有的临床安全措施主要盯着模型的输入和输出，但被操纵的模型完全可以给出看起来毫无异常的答案，因此仅靠输出审查在结构上就对这类攻击视而不见。这项研究表明，把模型内部状态转写成自然语言后，可以作为一种廉价且可复用的监控面，对构建护栏、红队工具或在临床场景部署大模型的人都有直接价值，而且无需重新训练模型。 评测涵盖两个攻击目标（遗漏某项病理、暗中推荐某种药物）、两种输入模态和两种注入投递机制，所有注入条件均在 p<0.05 水平上显著。值得注意的是，思维通道还能在模型尚未决定是否拒绝、仍在阅读请求时就将其标记为有害；局限在于这是一项单模型规模的研究、攻击集较小，跨更多模型家族和攻击类型的普适性仍待验证。

rss · arXiv cs.CL · 11月20日 05:00

**背景**: 提示注入是指把指令藏在输入中（文本，或图像像素）以覆盖开发者意图的攻击方式；在医学视觉语言模型上，这类攻击已被证明可以引发有害输出，也出现了 MPIB 等专门评测基准。多数防御位于外围，要么过滤输入、要么筛查输出，但当被劫持的模型仍能生成流畅且看似合理的答案时，这类防御就会失效。自然语言自编码器（NLA）是一种机制可解释性技术，与稀疏自编码器思路相关，但它是把模型的激活向量直接解码成人类可读的文本，而不是抽象特征，从而让内部状态可以用自然语言审视。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://transformer-circuits.pub/2026/nla/">Natural Language Autoencoders Produce Unsupervised...</a></li>
<li><a href="https://www.anthropic.com/research/natural-language-autoencoders">Natural Language Autoencoders \ Anthropic</a></li>
<li><a href="https://aisecwatch.com/issues/bb3dbeec-3b53-45e7-9c5b-858ca85b3e4b">What the model knows but does not say: monitoring medical…</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#interpretability`, `#medical AI`, `#prompt injection`, `#LLM monitoring`

---

<a id="item-24"></a>
## [LLM 评委在强化学习中传递类别偏见而非答案知识](https://arxiv.org/abs/2611.25191) ⭐️ 8.0/10

一项涵盖 814 次强化学习运行的实证研究显示，在训练 7-8B 模型回答闭卷问题或选择弃答时，LLM 评委对单个答案的知识几乎不会迁移给模型，而对某类问题的信念却会广泛传播。仅 12 条关于前国家首都的判定中有 11 条错误，就能让模型对新问题中 98% 的此类首都题拒答。 这对依赖 LLM-as-a-judge 的奖励建模与对齐实践构成警示：评委的少量错误判定可能制造准确率和弃答率都看不出的广泛行为盲区。研究者和工程师需要按问题类别审计评委判定，而不能假定评委的答案级知识会自动迁移给被训练模型。 关键细节是：当禁止回答“我不知道”时，模型仍能正确回答 94% 的此类首都题，说明知识并未丢失，被改变的是拒答行为。论文还报告，仅用模型自身 32 个未训练采样的一致性作为奖励、无需标签和评委，也能获得与标准答案相当的奖励并保住该类别。

rss · arXiv cs.CL · 11月20日 05:00

**背景**: LLM-as-a-judge 指用一个大型语言模型充当评估器，在缺少标准答案时给模型输出打分或判断对错，常被用作强化学习中的奖励信号。闭卷问答要求模型不借助检索、仅凭参数知识作答；弃答则是模型在不确定时选择回答“我不知道”。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/LLM-as-a-Judge">LLM-as-a-Judge - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2409.11239">[2409.11239] LLM-as-a-Judge & Reward Model: What They Can and ... Ask a Strong LLM Judge when Your Reward Model is Uncertain LLM-as-a-Judge & Reward Model: What They Can and Cannot Do Reinforcement fine-tuning with LLM-as-a-judge LLM Judges as Reward Models - Atla LLM-as-a-judge</a></li>
<li><a href="https://arxiv.org/abs/2505.10320">[2505.10320] J1: Incentivizing Thinking in LLM-as-a-Judge via ... Reinforcement fine-tuning with LLM-as-a-judge [2603.17145] REAL: Regression-Aware Reinforcement Learning ... J-ToRL: Tool-Integrated LLM-as-a-Judge via Reinforcement Learning J1: RL for LLM-as-Judge Training - emergentmind.com LLM-as-a-Judge - Wikipedia J1: Incentivizing Thinking in LLM-as-a-Judge via ...</a></li>

</ul>
</details>

**标签**: `#LLM-as-a-judge`, `#reinforcement learning`, `#reward modeling`, `#AI alignment`, `#evaluation`

---

<a id="item-25"></a>
## [基于大模型的搜索返回的拉美新闻比传统搜索引擎更少元、更少本地内容](https://arxiv.org/abs/2611.25955) ⭐️ 8.0/10

一项大规模审计研究（arXiv:2611.25955）构建了覆盖九个拉美国家、1901 个时事事件的数据集，用多种语言构造贴近真实的查询，分别提交给三个传统搜索引擎和四个语言模型，共产生 49207 次请求、涉及 8834 个独立域名。研究发现，语言模型返回的新闻来源多样性始终低于搜索引擎；对于本地用户而言，搜索引擎本就只返回 41.3%的本国新闻，而基于大模型的搜索还要再低 3.6 至 11.6 个百分点。 AI 平台正逐渐成为人们获取新闻的主要入口，因此如果基于大模型的搜索复制甚至放大了既有的地理层级，全球南方新闻来源的可见度与触达范围可能进一步萎缩，而拉美恰恰是全球南方 AI 使用比例最高的地区。这些发现对 AI 公平性、搜索产品设计，以及依赖导流流量的本地新闻媒体的生存都具有现实意义。 作者同时改变查询语言并模拟用户所在位置，以区分“本地用户、侨民、游客、外国用户”四种情境，从而把语言效应与地理效应分离开来。语言模型返回的本国新闻占比在这些用户类型之间并不一致，研究团队还公开了数据集，用于支持多语言、地理多样化的 LLM 搜索评测。

rss · arXiv cs.CL · 11月20日 05:00

**背景**: 基于大模型的搜索指的是 AI Overviews、AI Mode 以及带网页检索的聊天助手这类系统：它们用生成的摘要加引用来源来回答查询，而不是给出排序的链接列表。由于这类系统会把众多来源压缩成一段简短答案，最终被引用的往往只有少数几家媒体，这就可能收窄获得关注和流量的发布者范围。“全球南方”是拉美、非洲和亚洲中低收入国家的统称，已有研究记录显示 AI 系统倾向于过度呈现来自高可见度富裕国家的内容。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.researchgate.net/publication/398559878_Source_Coverage_and_Citation_Bias_in_LLM-based_vs_Traditional_Search_Engines">Source Coverage and Citation Bias in LLM - based vs. Traditional...</a></li>

</ul>
</details>

**标签**: `#AI search`, `#LLMs`, `#news diversity`, `#geographic bias`, `#Latin America`, `#empirical evaluation`

---