---
layout: default
title: "Horizon Summary: 2026-11-22 (ZH)"
date: 2026-11-22
lang: zh
---

> 从 120 条内容中筛选出 10 条重要资讯。

---

1. [MiniMax 称其内部模型实现自动化密码分析，攻破多个前沿密码方案](#item-1) ⭐️ 9.0/10
2. [菲尔兹奖得主梅纳德：AI 的黎曼猜想证明须被人理解才可能获认可](#item-2) ⭐️ 9.0/10
3. [OpenAI 主张困惑度仍是衡量模型智能的清晰指标](#item-3) ⭐️ 7.0/10
4. [蒂姆·奥莱利：硅谷在为股东价值而非人类福祉优化](#item-4) ⭐️ 7.0/10
5. [分析预测 Anthropic 2028 年数据中心电力 87%来自天然气、11%来自煤炭](#item-5) ⭐️ 7.0/10
6. [Muru](#item-6) ⭐️ 7.0/10
7. [天津大学脑机海河实验室首次实现人体超声调制脑电高时空分辨解码](#item-7) ⭐️ 7.0/10
8. [美团分享商家 AI 助手评测与优化闭环实践](#item-8) ⭐️ 7.0/10
9. [美团分享在“不能出错”的分布式存储系统中使用 AI Coding 的实践](#item-9) ⭐️ 7.0/10
10. [美团 MTFM：统一外卖多业务精排的推荐基座大模型](#item-10) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [MiniMax 称其内部模型实现自动化密码分析，攻破多个前沿密码方案](https://www.ithome.com/1/030/711.htm) ⭐️ 9.0/10

11 月 22 日，MiniMax 宣布其最新内部模型对现代密码方案开展了系统性的自动化密码分析，挖掘出多处此前未知的算法构造缺陷，并把多项原本只停留在论文理论层面的攻击推进到秒级至分钟级的可执行破解。官方称，该模型首次实际攻破了多个此前“尚无已知实际攻击”的 NIST 竞赛候选算法，对多个经同行评审的前沿方案实现了高效的密文伪造或密钥恢复，刷新了新型分组密码的最高破解轮数纪录，并在国际公开挑战赛中首次攻克数十个尚无公开解的高阶实例，相比当前最优求解算法实现数百至数万倍的实测加速。 这表明大模型的推理能力可以被用于以攻击为导向的数学搜索，而不仅仅是代码生成，可能改变密码方案在标准化前后接受安全压力测试的方式。MiniMax 明确说明 AES、RSA、SHA-256 等现行主流标准的安全性不受影响，因此其冲击主要落在前沿研究与同行评审实践上，而非日常加密。 该研究的范围限定在学术前沿方案、历史竞赛候选设计和公开参数挑战，而非实际部署的系统，MiniMax 表示已提前将分析结果同步给相关方案的作者。公司还把模型生成的推理轨迹与代码以技术报告形式公开在其 GitHub 研究仓库（github.com/MiniMax-AI/Research），不过原始报道本身技术细节有限，各项具体结论仍需独立验证。

rss · IT HOME · 11月22日 13:23

**背景**: 密码分析是指在不知道密钥的情况下破解或削弱加密的学科，其中很大一部分本质上是搜索问题：分析者寻找密码中可被利用的代数结构或统计偏差，再求解由此产生的方程组或优化问题。例如代数密码分析就是把密码方案改写为关于密钥的多项式方程组并尝试求解。NIST 的密码标准化竞赛（尤其是自 2016 年起分多轮推进的后量子密码项目）是候选方案在成为标准之前接受外部研究者检验的主要公开场合。分组密码还常以攻击能够穿透多少轮来衡量安全性，因此“轮数纪录”是针对某一设计进展程度的常用指标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/NIST_Post-Quantum_Cryptography_Standardization">NIST Post-Quantum Cryptography Standardization - Wikipedia</a></li>
<li><a href="https://csrc.nist.gov/projects/post-quantum-cryptography/post-quantum-cryptography-standardization">Post-Quantum Cryptography | CSRC - NIST Computer Security ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cryptanalysis">Cryptanalysis - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI for cryptanalysis`, `#LLM reasoning`, `#cryptography`, `#security research`, `#automated theorem/attack discovery`

---

<a id="item-2"></a>
## [菲尔兹奖得主梅纳德：AI 的黎曼猜想证明须被人理解才可能获认可](https://www.ithome.com/1/030/677.htm) ⭐️ 9.0/10

11 月 20 日，Anthropic 数学家莱文特·阿尔珀格（Levent Alpöge）宣布自己与 AI 模型 Claude 合作证明了黎曼猜想（及其对狄利克雷 L 函数的推广）；11 月 21 日，Lean 与 Mathlib 社区确认这份约 1700 万行的 Lean 形式化证明可以通过编译与核验。11 月 22 日的报道中，2022 年菲尔兹奖得主、牛津大学教授詹姆斯·梅纳德（James Maynard）表示他相信该结果正确，但只有当有人真正理解这份证明并能向他人解释清楚时，它才可能获得数学界的全面认可。 如果这一结果成立，它将是数学史上最著名的未解难题之一首次在 AI 深度参与下完成证明，并经过端到端的机器核验，因而成为“AI 用于数学”以及“形式化验证作为信任机制”的标志性案例。梅纳德的观点还有超出标题的意义：它表明“机器可验证的正确性”与“人类对数学的理解”正在成为两种不同的评价标准，这将深刻影响科研共同体如何评估 AI 产出的成果。 梅纳德的信心建立在两点上：该结果已经过形式化验证，而且这一验证又被 Lean/Mathlib 社区独立复核；同时阿尔珀格在提出此类重大主张方面一向有可靠记录。值得注意的是，据维基百科“黎曼猜想”条目，目前尚未发表可供人类阅读的自然语言证明——这正是梅纳德所指的缺口，他警告说，在人们真正理解证明中的思想与整体框架之前，这项成果很可能无法带来人们所期待的变革。

rss · IT HOME · 11月22日 09:35

**背景**: 黎曼猜想由波恩哈德·黎曼于 1859 年提出，断言黎曼 ζ 函数的所有非平凡零点都位于实部为 1/2 的临界线上；它属于克雷数学研究所的“千禧年大奖难题”，并且在数论中处于核心地位，因为它本质上给出了素数分布误差的最优可能上界。Lean 是一个开源证明助手兼函数式编程语言，基于带归纳类型的构造演算，证明以代码形式书写并由机器检查；Mathlib 则是建立在其之上的、由社区维护的形式化数学库。形式化验证能够保证证明由公理推出，但它本身并不能告诉数学家命题为何成立、证明又引入了哪些新思想。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Riemann_hypothesis">Riemann hypothesis</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lean_theorem_prover">Lean theorem prover</a></li>
<li><a href="https://mathlib.org/">Mathlib</a></li>

</ul>
</details>

**标签**: `#AI for mathematics`, `#formal verification`, `#Lean/Mathlib`, `#Riemann Hypothesis`, `#research epistemology`

---

<a id="item-3"></a>
## [OpenAI 主张困惑度仍是衡量模型智能的清晰指标](https://openai.com/index/perplexity-and-intelligence/) ⭐️ 7.0/10

OpenAI 发布了一篇题为《Perplexity and Intelligence》的观点文章，认为困惑度（即在留出数据上测得的下一 token 交叉熵）在其自 GPT-3.5 以来的各代模型中呈现出出奇清晰且可预测的下降趋势，因此实验室应更透明地公开这一指标，把它当作能力信号来报告。文章给出的数字来自 OpenAI 内部的留出数据集，而非公开基准。 如果困惑度确实能如此清晰地反映模型能力，那么在基准测试日益泛滥、设计越来越复杂的当下，它将为整个领域提供一个廉价而简单的单一数字，并可能改变实验室报告和比较进展的方式。由于该提议出自一家前沿实验室且在方法论上存在争议，它也加剧了关于“什么才算模型智能的有效证据”的讨论。 据报道，文章并未说明其困惑度数字具体是在哪个留出数据集上计算的，只称来自内部代码库的一个固定快照，这使得这些数字既无法复现，也难以在不同实验室之间比较。此外，困惑度只有相对于特定数据集和分词器才有意义，因此跨机构的比较本身就很脆弱。

hackernews · OpenAI News · 11月22日 17:06 · [社区讨论](https://news.ycombinator.com/item?id=50601525)

**背景**: 困惑度是语言模型的经典评价指标：它等于模型为文本中每个 token 分配的平均负对数似然取指数，因此困惑度为 1 意味着模型对每个 token 都预测得完全正确，而最差情况（均匀随机预测）则等于词表大小。它在 GPT-2 等早期自回归模型的评估中居于核心地位，至今仍是标准指标，但它适用于因果语言模型，对 BERT 这类掩码模型并没有良好定义。关键在于，困惑度分数高度依赖数据集的结构、词汇和复杂度——在新闻文本上困惑度低的模型在代码上可能表现很差——这正是 OpenAI 这篇文章招致批评的核心。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Perplexity">Perplexity - Wikipedia</a></li>
<li><a href="https://huggingface.co/docs/transformers/perplexity">Perplexity of fixed-length models - Hugging Face</a></li>
<li><a href="https://enigmatica.ai/glossary/perplexity-metric">What Is Perplexity (Metric)? Definition & Guide</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者持怀疑态度且颇具技术含量：多人指出文章始终没有真正定义或说明其困惑度数字背后的留出数据，这让“应更透明”的呼吁显得尴尬，并强调困惑度必须限定为“在什么数据上的困惑度”。还有人提出数据污染的担忧——前沿实验室的大量新代码由 AI 生成，使用内部代码评测集可能导致困惑度被人为压低；也有一位评论者对在强化学习和推理模型时代交叉熵趋势依然如此清晰感到惊讶，并对拥有这样一个简单基准表示欢迎。

**标签**: `#AI evaluation`, `#language models`, `#perplexity`, `#benchmarks`, `#OpenAI`

---

<a id="item-4"></a>
## [蒂姆·奥莱利：硅谷在为股东价值而非人类福祉优化](https://www.oreilly.com/radar/what-happened-to-silicon-valley/) ⭐️ 7.0/10

O'Reilly Media 创始人蒂姆·奥莱利在 Radar 上发表长文，认为硅谷的种种弊病源于把市场当作自然现象而非人为设计的机器，并指出整个行业已从“为人类福祉而做技术”滑向“为股东价值做优化”。他提出用机制设计（他称之为“逆向博弈论”）作为思考框架：与其追问当前游戏规则是什么，不如追问我们本应玩哪一场游戏。 作者是技术出版与开源倡导领域最具影响力的人物之一，这篇文章把当下关于裁员、AI 驱动的削减成本和风投文化的讨论重新框定为“激励机制如何设计”的问题，而非个别坏人的问题。对工程师和创业者而言，它提供了一套话语工具，用来质疑“市场结果天然如此、无可更改”的默认假设。 文章的核心论点——应当有意识地运用机制设计来选择人类要优化的目标——出现在一篇长文的靠后位置，有读者认为这属于“把重点埋得太深”。全文属于政治经济学层面的分析而非技术方案，也没有为它所呼吁的重构给出具体的实施蓝图。

hackernews · greenyouse · 11月22日 19:20 · [社区讨论](https://news.ycombinator.com/item?id=50602947)

**背景**: 机制设计是经济学的一个分支，常被称作“逆向博弈论”：它不分析既有博弈会产生什么结果，而是从期望的结果出发，倒推应当制定怎样的规则与激励来达成该结果，广泛应用于拍卖设计、投票制度和市场设计。讨论还涉及 ZIRP，即零利率政策——美联储在 2008 年 12 月至 2015 年 12 月、以及 2020 年 3 月至 2022 年 3 月两度实行该政策，廉价资本充裕，促使风投支持的初创公司把增长置于盈利之上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mechanism_design">Mechanism design - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zero_interest-rate_policy">Zero interest-rate policy - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者大体认同奥莱利的诊断，但在成因与问责上各有侧重：多人把行业膨胀归因于 ZIRP 时代，并指出利率回升后科技公司正靠 AI 蚕食自身核心业务。也有人批评“风投网红”以自我服务的方式空谈未来；一位评论者认为全文最好的观点——我们应当认真思考人类集体要优化什么——被埋没了；还有人质疑用股东资本主义来解释谷歌的境遇是否站得住脚。

**标签**: `#silicon-valley`, `#tech-industry`, `#mechanism-design`, `#venture-capital`, `#political-economy`

---

<a id="item-5"></a>
## [分析预测 Anthropic 2028 年数据中心电力 87%来自天然气、11%来自煤炭](https://betterdatacenterproject.com/2026/11/16/how-ai-is-powered-a-breakdown-of-byop-and-grid-power/) ⭐️ 7.0/10

Better Data Center Project 发布分析，预测到 2028 年，Anthropic 数据中心用电中将有 87% 来自天然气、11% 来自煤炭，其余来自其他能源。该文拆解了这些电力中有多少来自“表后自建发电”（bring your own power，BYOP）而非公共电网，并在 Hacker News 上获得 775 分和 806 条评论。 AI 基础设施建设规模已大到足以重塑电力行业，而这份分析表明，一家头部实验室的算力扩张将锁定新的化石能源发电，而非可再生能源。由于 Anthropic 一直以安全与长期责任作为自我定位，其气候表态与实际电力采购之间的落差，使其成为要求信息披露与监管的焦点。 87% 与 11% 的比例是对 2028 年已规划与已签约装机容量的前瞻性推算，而非实际计量发电量，且高度依赖绕过多年电网并网排队的表后自建燃气电厂。由于这类自建电厂只服务单一客户，其排放与本地空气污染可能游离于并网发电所面对的核算与选址审查之外。

hackernews · happosai · 11月22日 08:57 · [社区讨论](https://news.ycombinator.com/item?id=50597612)

**背景**: 数据中心需要持续且极大量的电力，而在美国，新增发电装机的电网并网排队时间如今可长达约五年。为更快获得电力，运营商转向在园区内或紧邻园区建设表后自建天然气发电；2026 年 11 月，Anthropic 达成了一笔约 34 亿美元的燃气发动机供能交易，用于其数据中心。读者可能还会遇到 PUE（电能使用效率）这一指标，即数据中心总用电量与 IT 设备用电量之比——数值越低越好，它反映制冷等辅助开销，但并不说明进线电力本身的清洁程度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ft.com/content/41bf5c6a-9735-4f1a-a8e3-2bcccad58ba0?syn-25a6b1a6=1">Anthropic strikes $3.4bn deal to generate gas-fired power for ...</a></li>
<li><a href="https://www.enverus.com/blog/why-data-centers-are-looking-to-natural-gas-for-behind-the-meter-power/">Natural Gas Behind-the-Meter Power for Data Centers</a></li>
<li><a href="https://en.wikipedia.org/wiki/Power_usage_effectiveness">Power usage effectiveness - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者总体上持批评态度：有人称 Anthropic 是“名副其实的不良行为者”，理由是其在孟菲斯租用 Colossus 1 带来的本地污染，以及与 Alphabet 相比在美国没有任何可再生能源承诺。另一些人认为监管必不可少，因为纯粹以财务记账会把环境与社会成本转嫁给远离决策者的社区；还有人指出数据中心能耗之巨难以让公众直观想象，并提到美国大量天然气其实是页岩油开采的副产品，有时被火炬燃烧甚至出现负价格。

**标签**: `#AI infrastructure`, `#datacenter energy`, `#climate policy`, `#AI compute scaling`, `#regulation`

---

<a id="item-6"></a>
## [Muru](https://simonwillison.net/2026/Nov/21/muru/) ⭐️ 7.0/10

西蒙·威利森重点介绍了 Graham Dumpleton 的新 AI 辅助 Rust 服务器 Muru，它用于在开发和生产环境中运行 ASGI 与 WSGI Python 应用，并配有一系列详细的多篇“公开构建”文章。

rss · Simon Willison · 11月21日 23:56

**标签**: `#python`, `#asgi`, `#wsgi`, `#rust`, `#web-servers`

---

<a id="item-7"></a>
## [天津大学脑机海河实验室首次实现人体超声调制脑电高时空分辨解码](https://www.ithome.com/1/030/622.htm) ⭐️ 7.0/10

天津大学脑机海河实验室团队在《科学·进展》（Science Advances）发表成果，提出一种高鲁棒性的超声调制脑电信号解码技术，首次在人体被试数据层面实现了稳态视觉诱发电位（SSVEP）脑电源信号的高精度无创重建。团队提出声电调制比（AMR）这一指标来量化微弱、适度与过度三种声电调制场景，并配套设计了可跨场景应用的脉冲重复频率（PRF）解码算法。 超声调制脑电技术同时具备脑电的高时间分辨率与经颅聚焦超声的高空间分辨率，有望缓解传统无创脑机接口因头皮脑电空间分辨率低而导致的信息读取量受限问题，因此受到关注。该研究使解码在真人体数据中不稳定的声电耦合条件下依然稳健，推动这一仍处早期阶段的无创脑机接口路线向实用化靠近，对关注神经技术与生物医学信号处理的人群具有参考价值。 研究基于自研的 128 阵元超声相控阵系统实现亚毫米级焦域控制（HPBW 最低 0.79 mm），先在数值仿真和仿脑组织体模中验证 PRF 算法，随后基于 MetaBCI 平台开展 10 人次双指令 SSVEP 实验。在弱调制（0 < AMR ≤ 0.6）、中等调制（0.6 < AMR ≤ 1）和过调制（AMR > 1）状态下，PRF 算法的平均解码相关性分别为 0.84、0.90 和 0.89，优于包络提取、相干解调、时频分析和自适应解调等传统算法。

rss · IT HOME · 11月22日 08:36

**背景**: 稳态视觉诱发电位（SSVEP）是人观看以固定频率闪烁的刺激时大脑产生的节律性响应，大脑会像音叉共振一样“锁定”该频率，因此 SSVEP 成为无创脑机接口中广泛使用的范式。传统头皮脑电成本低、时间分辨率高，但由于容积传导效应，多个脑源的信号在头皮上混合，空间分辨率较差；而经颅聚焦超声则可以把能量聚焦到颅内很小的深部区域。声电效应把两者联系起来：聚焦超声在局部调制组织的电导特性，使头皮采集到的脑电中出现携带超声焦点位置标签的边带信号，从而为电生理记录赋予超声提供的空间标记。但在实际中，颅骨强声衰减、经颅焦点偏移以及深部神经源活动波动会使这种耦合极不稳定，如何可靠解码带标签的信号一直是主要障碍。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://neurosity.co/guides/what-is-ssvep-steady-state-visual-evoked-potentials">What Is SSVEP ? Steady - State Visual Evoked Potentials | Neurosity</a></li>
<li><a href="https://www.nature.com/articles/s44172-026-00598-4?error=cookies_not_supported&code=f409b333-baf6-484b-8108-8ed98da47af5">In vivo acoustoelectric neural recording in mice enabled by...</a></li>
<li><a href="https://hal.science/hal-03269442/document">An integrated and highly sensitive ultrafast acoustoelectric imaging...</a></li>

</ul>
</details>

**标签**: `#brain-computer interface`, `#neurotechnology`, `#ultrasound`, `#EEG signal processing`, `#research paper`

---

<a id="item-8"></a>
## [美团分享商家 AI 助手评测与优化闭环实践](https://tech.meituan.com/2026/11/17/Agent-Evaluation-White-Paper-02.html) ⭐️ 7.0/10

美团发布《Agent 评测白皮书》系列第二篇，以商家 AI 助手的巡检任务为贯穿案例，介绍评测与优化闭环实践。文章涵盖构建业务 Benchmark、评测器校准、错误分析，以及借助图灵平台支撑持续回归与模型选型。 这是一份有实质内容的工业案例，说明 Agent 评测可以做成持续迭代的工程闭环，而不是一次性跑分，并将评测器质量、错误分析、回归测试和模型选型串联起来。面向商家或任务自动化的 LLM Agent 团队可以复用这套方法，让评测更贴近业务并可持续运行。 该实践通过业务 Benchmark 和评测器校准提升自动评判与人工或业务预期之间的一致性，再把错误分析结果反馈到评测体系和 Agent 能力优化中。它属于系列中的实践者报告而非突破性成果，结论基于商家助手巡检场景，迁移到其他领域可能需要调整。

rss · 美团 Blog · 11月22日 21:37

**背景**: LLM Agent 是利用大语言模型进行规划并执行多步任务的 AI 系统，通常会调用工具或 API。此类系统的评测比单轮回答打分更难，因为成功与否取决于完整执行轨迹、业务规则和工具使用，因此团队会构建领域专属 Benchmark，并采用 LLM-as-judge 评测器。评测器校准通过调整提示词或评分方式，让自动评判结果与人类偏好更一致；回归测试则在变更后重跑基准用例，以发现质量下降。文中提到的图灵平台被用于支撑持续回归和模型选型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.31371v1">Calibrating the Evaluator: Does Probability Calibration ...</a></li>
<li><a href="https://aclanthology.org/2024.lrec-main.237.pdf">Calibrating LLM-Based Evaluator - ACL Anthology</a></li>
<li><a href="https://zylos.ai/zh/research/2026-05-26-llm-as-judge-agent-evaluation-patterns/">LLM-as-Judge Patterns for Agent Evaluation: Calibration, Bias ...</a></li>

</ul>
</details>

**标签**: `#Agent Evaluation`, `#Benchmarking`, `#LLM Agents`, `#Model Selection`, `#AI Engineering`

---

<a id="item-9"></a>
## [美团分享在“不能出错”的分布式存储系统中使用 AI Coding 的实践](https://tech.meituan.com/2026/10/29/AI-Coding-IN-Distributed-Storage-System.html) ⭐️ 7.0/10

美团基础技术部发布了一篇工程实践文章，介绍其如何在“不能出错”的分布式存储系统中使用 AI 编程工具，具体覆盖 AI 评审、问题排查和自动化开发三个方向。文章并非发布新模型或新基准，而是记录了真实的失效案例，并主张让代码和结论“经得起验证”比“多写代码”更重要。 当前关于 AI 编程的公开讨论大多集中在 Web 或应用层代码的提效上，而这份报告聚焦于可靠性至上的基础设施——这里的隐蔽错误可能导致数据丢失或服务中断。它对人类把关环节与 AI 结论验证的强调，为在高风险生产环境中部署大模型 Agent 的团队提供了一套可复用的方法论。 文章围绕 AI 代码评审、故障排查和自动化开发三个场景展开实践，并坦率说明了大模型容易出错的环节，将人工评审定位为必须的边界而非可选的保险措施。美团给出的结论是：衡量价值的标准应是 AI 产出的代码与结论是否正确、是否可被验证，而不是产出的数量。

rss · 美团 Blog · 11月22日 21:37

**背景**: 分布式存储系统将数据和副本分散在多台机器上，因此一致性、故障切换或数据放置逻辑中的缺陷可能在不被察觉的情况下损坏或丢失数据，这使该领域对 AI 生成代码的审查要求格外严格。AI 编程助手通常指基于大模型的工具，可以起草代码、评审代码变更或协助定位线上问题，它们在工业界已相当普及，但多数报告以开发者产出效率而非故障场景下的正确性来衡量其价值。

**标签**: `#AI coding`, `#distributed storage`, `#reliability engineering`, `#LLM code review`, `#engineering practice`

---

<a id="item-10"></a>
## [美团 MTFM：统一外卖多业务精排的推荐基座大模型](https://tech.meituan.com/2026/09/22/Meituan-Foundation-Model-for-Recommendation.html) ⭐️ 7.0/10

美团技术团队提出 MTFM，这是一个基于 MTGR 构建的统一推荐基座大模型，并称其首次在生产环境中以单一精排模型覆盖外卖多个主要业务场景。该消息描述的是工业级落地，而非纯实验性模型。 这反映了工业推荐系统向基座模型架构演进的趋势：不再为每个场景单独维护排序模型，而是跨业务共享表示和参数。如果该方案能够泛化，它有望减少重复的建模与 serving 投入，并提升较小或较新业务的数据利用效率。 根据美团此前的论文，MTFM 所依托的 MTGR 采用 HSTU 架构建模，并保留了 DLRM 类特征（包括交叉特征）。不过，目前公开摘要未提供方法细节、评估指标或消融结果，因此尚无法独立评估其线上收益与取舍。

rss · 美团 Blog · 11月22日 21:37

**背景**: 在大规模推荐系统中，排序通常采用级联结构：召回负责取回候选，粗排进行初步筛选，精排则用最重的模型对剩余物品精确打分。美团的 MTGR 是一个基于 HSTU 架构、同时保留 DLRM 特征的工业级生成式推荐框架，而 MTFM 将这一路线进一步推向共享基座模型。业界正在探索能够跨场景迁移的统一基座模型，而不是为每个业务分别维护独立模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2505.18654">[2505.18654] MTGR : Industrial-Scale Generative Recommendation ...</a></li>
<li><a href="https://arxiv.org/pdf/2505.18654">MTGR : Industrial-Scale Generative Recommendation Framework in...</a></li>

</ul>
</details>

**标签**: `#recommendation systems`, `#foundation models`, `#industry practice`, `#large-scale ML`, `#ranking`

---