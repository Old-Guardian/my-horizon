---
layout: default
title: "Horizon Summary: 2026-11-25 (ZH)"
date: 2026-11-25
lang: zh
---

> 从 458 条内容中筛选出 25 条重要资讯。

---

1. [PrismML 发布 Ternary Bonsai 2.5 27B：可在本地跑智能体编程的三值量化模型](#item-1) ⭐️ 8.0/10
2. [OpenAI 称 GPT-6.2 靠写代码设计出蛋白质迷你结合物，社区质疑其实际贡献](#item-2) ⭐️ 8.0/10
3. [Quad9 因法律限制停止在法国提供公共 DNS 服务](#item-3) ⭐️ 8.0/10
4. [智谱 Z.ai 发布 GLM-5.4，首次采用循环 Transformer 架构](#item-4) ⭐️ 8.0/10
5. [Ladybird 发布首个 Alpha 版本，推出自研浏览器引擎](#item-5) ⭐️ 8.0/10
6. [美团推出统一推荐基座大模型 MTFM，首次实现外卖多业务统一精排](#item-6) ⭐️ 8.0/10
7. [AutoPILOT 框架让视觉智能体通过宏与控制器实现实时行动](#item-7) ⭐️ 8.0/10
8. [当工具失效时，智能体编造：工具使用型 LLM 智能体中的静默失败与验证优先监督](#item-8) ⭐️ 8.0/10
9. [OWASP 安全提示词使 AI 生成应用的漏洞减少三分之一，但依赖面翻倍](#item-9) ⭐️ 8.0/10
10. [Agent Money 基准测试：AI 智能体能否被信任花好钱？](#item-10) ⭐️ 8.0/10
11. [LLM“数字分身”能通过模拟初次对话预测真实好感度](#item-11) ⭐️ 8.0/10
12. [DiscernBench：评估 LLM 智能体在机构场景中的协同判断力](#item-12) ⭐️ 8.0/10
13. [SMB Bench：90 天模拟器检验语言模型智能体能否应对延迟后果](#item-13) ⭐️ 8.0/10
14. [AI 智能体无需反向传播，即可将新能力直接写入语言模型权重](#item-14) ⭐️ 8.0/10
15. [训练神经符号式语言模型外壳可实现组合泛化](#item-15) ⭐️ 8.0/10
16. [Muted Distillation：对教师隐藏学生推理，智能体输出 token 减少 57%](#item-16) ⭐️ 8.0/10
17. [PBPT：面向大模型后训练的种群式超参数自动调优方法](#item-17) ⭐️ 8.0/10
18. [VidRouteBench 基准让文本生成视频的预算感知路由成为可能](#item-18) ⭐️ 8.0/10
19. [审计揭示：最强生成器加拒绝重试即可追平多数智能体文生图增益](#item-19) ⭐️ 8.0/10
20. [RadioVISTA 基准测试：视觉语言模型能否从城市图像推断不可见的无线电场](#item-20) ⭐️ 8.0/10
21. [VideoJSON：极简 JSON 索引加编码智能体，超越专用视频记忆系统](#item-21) ⭐️ 8.0/10
22. [NAVSIMv1 测试场景紧邻训练数据，导致驾驶分数虚高](#item-22) ⭐️ 8.0/10
23. [ScaleEvals：无重置自主玩耍实现可扩展通用机器人策略评估](#item-23) ⭐️ 8.0/10
24. [SANA-Robot：4.5B 混合记忆世界动作模型实现边缘端实时运行](#item-24) ⭐️ 8.0/10
25. [Tacinf 发布开源全栈触觉基础设施，助力机器人灵巧操作](#item-25) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [PrismML 发布 Ternary Bonsai 2.5 27B：可在本地跑智能体编程的三值量化模型](https://prismml.com/news/bonsai-2-5-27b) ⭐️ 8.0/10

PrismML 发布了 Ternary Bonsai 2.5 27B，这是一个将 270 亿参数模型的权重量化为三值形式、并以 Q2_0 GGUF 文件分发的版本。Hacker News 上的早期用户报告称，在 24GB 内存的 Mac Mini M5 Pro 上生成速度约为 22-25 tokens/s、上下文可达 128K，其中一位评论者表示该模型首次通过了其在 256K 上下文上进行的 2048 针密集检索测试。 如果这些数字站得住脚，那么一个被大幅压缩的 27B 模型就能在消费级硬件上真正用于智能体编程，从而降低本地 AI 工作流的成本和隐私门槛。评论者还指出，它在 SWE-bench Verified 上的得分大致相当于约六个月前的前沿模型，这也让“小模型追赶前沿基准表现的速度有多快”这一讨论更加热烈。 该 GGUF 版本将每个权重存为 {-1, 0, +1} 三者之一，并每 128 个权重共享一个 FP16 缩放因子，使这个 27B 模型体积缩小到约 7.6GB。实测吞吐在预填充阶段偏高，约为 223 tok/s，而生成阶段约为 22 tok/s、首个 token 约需 2.1 秒；至少有一位评论者提醒，SWE-bench Verified 并非最具代表性的基准。

hackernews · b0m · 11月24日 20:08 · [社区讨论](https://news.ycombinator.com/item?id=50633922)

**背景**: 三值量化（也称 1.58-bit 量化）把模型权重限制为 -1、0、+1 三种取值，而非 16 位浮点数，从而大幅压缩显存占用，并能在高效支持低位运算的硬件上加速推理。GGUF 是 llama.cpp 及相关本地推理工具使用的文件格式，Q2 表示每个权重约 2 比特。SWE-bench Verified 是 SWE-bench 中经人工筛选出的 500 个实例子集，模型必须通过生成能通过项目测试的补丁来解决真实 GitHub issue，因此被视为衡量 AI 编程智能体最常被引用的基准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf">prism-ml/ Ternary -Bonsai-2-27B- gguf · Hugging Face</a></li>
<li><a href="https://en.wikipedia.org/wiki/1.58-bit_large_language_model">1.58-bit large language model - Wikipedia</a></li>
<li><a href="https://www.swebench.com/verified.html">SWE-bench Verified</a></li>

</ul>
</details>

**社区讨论**: 整体反响相当正面：用户贴出了具体的吞吐和长上下文检索结果，一项长周期本地智能体测试显示 Bonsai 2.5 用 76 分钟完成任务，而上一版本用了 107 分钟（步数减少 17%）。怀疑者则质疑这种 SWE-bench 持平有多少来自“刷榜”或基准本身的变化、有多少是真正的小模型进步；另有评论者认为市场已经饱和，未来焦点将转向全能型 MoE 模型。

**标签**: `#local-llm-inference`, `#quantization`, `#small-language-models`, `#gguf`, `#swe-bench`

---

<a id="item-2"></a>
## [OpenAI 称 GPT-6.2 靠写代码设计出蛋白质迷你结合物，社区质疑其实际贡献](https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/) ⭐️ 8.0/10

OpenAI 的一篇博文称，在给出五个靶标蛋白的三维结构并标注期望结合位点后，GPT-6.2 自行编写代码生成了三维迷你结合物（minibinder）设计方案，且未调用专门的蛋白质 AI 模型。但同一篇博文也说明，OpenAI 使用 SolubleMPNN 为这些设计生成氨基酸序列，并借助其他专门化的蛋白质模型筛选那些被预测能正确折叠、并在预期位点结合的候选分子。 如果一个通用代码模型能够切实推动从头蛋白质设计，就会降低计算生物学流程的门槛，并把瓶颈从专用蛋白质模型转向纯粹的代码编写能力。这种混合流程也向整个领域提出了一个更大的问题：一项“涌现”的科研能力，究竟应归功于大语言模型本身，还是归功于它所调度的那些专用工具。 这项声明的范围比标题所暗示的要窄：GPT-6.2 生成的是三维骨架几何结构，而在很大程度上决定蛋白质能否真正折叠并结合的序列设计步骤，则是由 SolubleMPNN 完成的。该博文只涉及五个靶标蛋白，对湿实验成功率或实验验证的细节着墨甚少，因此很难判断所展示能力的实际幅度。

hackernews · OpenAI News · 11月24日 21:02 · [社区讨论](https://news.ycombinator.com/item?id=50634658)

**背景**: 蛋白质的功能在很大程度上取决于其三维结构，而三维结构又由氨基酸序列所编码。所谓逆向折叠（inverse folding）模型，如 ProteinMPNN 以及仅用可溶性蛋白训练的变体 SolubleMPNN，会接收一个固定的骨架，并提出被预测能折叠成该骨架的序列。迷你结合物（minibinder）是通过从头设计得到的、能结合特定靶标的小型蛋白质，通常由 RFdiffusion 之类的生成式骨架工具与逆向折叠序列设计相配合的流程产生。OpenAI 在此声称的是：一个通用代码大模型可以通过自行编写设计代码，替代这套专用工具链中的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepwiki.com/dauparas/ProteinMPNN/5.2-soluble-models">Soluble Models | dauparas/ProteinMPNN | DeepWiki</a></li>
<li><a href="https://idl.uw.edu/mosaic/examples/protein-design.html">Protein Design Explorer | Mosaic</a></li>

</ul>
</details>

**社区讨论**: 评论者对这种“自主性”叙事提出了质疑，有人追问：既然对蛋白质而言“序列就是结构”，而序列又是由 SolubleMPNN 给出的，那 GPT-6.2 究竟设计出了什么。一位在 Baker 实验室获得博士学位的评论者认为这个方向合理，是语言模型向原生多模态蛋白质设计自然延伸的一步；也有人对通用模型在没有任务特定强化学习的情况下展现出设计直觉表示赞叹。

**标签**: `#AI for science`, `#protein design`, `#LLM capabilities`, `#computational biology`, `#research methodology`

---

<a id="item-3"></a>
## [Quad9 因法律限制停止在法国提供公共 DNS 服务](https://quad9.net/news/blog/quad9-service-deactivation-in-france/) ⭐️ 8.0/10

瑞士非营利公共 DNS 解析服务 Quad9 已停止向法国用户提供服务，现在向 9.9.9.9 发起的查询会返回 REFUSED 状态，并附带 EDNS 扩展 DNS 错误码 18，内容为“Prohibited: Service unavailable due to French legal constraints（因法国法律限制，服务不可用）”。此举源于一项据称与版权/盗版过滤相关的法国法律命令，服务下线已导致那些将路由器或自建解析器（如 AdGuard Home）上游指向 Quad9 的法国用户出现断网。 这是一个具体案例，说明中间人责任与 DNS 层过滤制度如何把一个注重隐私的公共解析器挤出整个国家，并为其他司法辖区和其他解析服务商树立了先例。它直接影响法国普通用户和网络运维人员，也表明加密、无日志的 DNS 解析正从“中立基础设施”变成法律上有争议的服务。 封锁是在解析器一侧执行的：受影响的查询会收到 REFUSED 状态以及携带明确法律限制说明的扩展 DNS 错误码 18，而像 AdGuard Home 这类上游客户端只会把它显示为上游不可达。作为应对，社区成员搭建了志愿性质的 DoH/DoT/Do53（UDP 与 TCP、IPv4 与 IPv6）代理，仅做缓存并向 Quad9 转发请求，让法国用户能获得近乎开箱即用的替代方案。

hackernews · farrokhi · 11月24日 08:33 · [社区讨论](https://news.ycombinator.com/item?id=50625384)

**背景**: DNS 是互联网的“查号台”，负责把域名翻译成 IP 地址，而默认情况下这些查询以明文发往设备或路由器所配置的解析器——通常就是运营商提供的那个。Quad9 是由瑞士非营利基金会运营的免费、注重隐私的公共解析器，地址为 9.9.9.9 和 149.112.112.112，同时还提供加密的 DNS over TLS（DoT）与 DNS over HTTPS（DoH），使查询对中间人不可见。由于解析器位于用户与其访问的每个网站之间，监管机构越来越倾向于把它视为可被命令封禁域名的“中间人”，这与施加于平台和接入服务商的責任逻辑相同。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://quad9.net/">Quad 9 | A public and free DNS service for a better security and privacy</a></li>
<li><a href="https://en.wikipedia.org/wiki/DNS_over_HTTPS">DNS over HTTPS - Wikipedia</a></li>
<li><a href="https://www.cloudflare.com/learning/dns/dns-over-tls/">DNS over TLS vs. DNS over HTTPS | Secure DNS - Cloudflare</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论普遍同情 Quad9，且非常务实：一位评论者公布了面向法国用户的开放 DoH/DoT/Do53 代理，附上了具体主机名与 IP；另一位贴出 dig 输出，证实了 REFUSED 响应和 EDE 错误码 18；还有人表示自家局域网断网，原因是 AdGuard Home 无法再连上上游。其他人则贴出此前关于同一事件的两个大型讨论帖，以及 TorrentFreak 关于该盗版相关命令到期的后续报道，把这次退出形容为 DNS 过滤问题的“煤矿里的金丝雀”。

**标签**: `#DNS`, `#internet policy`, `#privacy`, `#censorship`, `#network infrastructure`

---

<a id="item-4"></a>
## [智谱 Z.ai 发布 GLM-5.4，首次采用循环 Transformer 架构](https://simonwillison.net/2026/Nov/23/glm-54/) ⭐️ 8.0/10

Z.ai 发布了 GLM-5.4，这是其首个采用循环 Transformer 架构的模型：一组共享权重的层会多次迭代运行，不断精炼隐藏状态，从而在不增加参数量的前提下提升网络的等效深度。据相关报道，GLM-5.4 将 GLM-5 基座模型的 28 层各运行两遍，而它距离 Thinking Machines Lab 于 2026 年 11 月 20 日发布的 Inkling 2 Mini（对每个 token 将中间层循环三次）仅隔三天。 两家资金充裕的实验室在短短一周内先后采用循环 Transformer，这强烈表明“用推理时算力换取架构深度”正在成为前沿大模型设计的主流方向。如果该思路被验证有效，就有望在不按比例扩大参数量和训练成本的情况下提升推理与智能体编程能力，这对所有基于此类模型进行开发或评测的人都意义重大。 GLM-5.4 目前尚未开放权重，Z.ai 表示会在完成必要的安全加固后再开源，而且发布时没有公布任何基准测试成绩；用户只能通过 Z.ai 的 Coding Plan 订阅使用，常规 API 暂时无法访问（两者共用位于 https://api.z.ai/api/v1 的 OpenAI 兼容接口）。Z.ai 将该思路追溯到 2018 年的 Universal Transformer；Simon Willison 还指出，GLM-5.1 和 5.2 生成的 SVG 鹈鹕图风格十分独特，而 5.3 和 5.4 的输出则更接近 OpenAI 与 Anthropic 模型的风格。

rss · Simon Willison · 11月23日 23:40

**背景**: 在标准 Transformer 中，每一层在每次前向传播时只执行一次，因此要让模型更深就必须增加参数和训练算力。循环 Transformer 则复用同一组共享权重进行多轮循环计算，让模型在推理阶段投入更多算力，对同一批隐藏状态“多想几遍”。这一概念可追溯到 2018 年的 Universal Transformer，近期又在 Thinking Machines 的 Inkling 2 Mini 等模型上复兴——后者是一个总参数 264 亿、激活参数 34 亿的混合专家模型，对每个 token 将中间层循环三次。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thenextweb.com/news/zai-glm-5-4-loop-transformer-coding-model">Z . ai ’s GLM - 5 . 4 runs its layers twice to rival 2T-parameter models</a></li>
<li><a href="https://thinkingmachines.ai/news/inkling-2-mini/">Introducing Inkling 2 Mini - Thinking Machines Lab</a></li>
<li><a href="https://sebastianraschka.com/llm-architecture-gallery/looped-depth-sharing/">Looped Transformer | Sebastian Raschka, PhD</a></li>

</ul>
</details>

**标签**: `#LLM architecture`, `#looped transformers`, `#model releases`, `#inference-time compute`, `#AI research`

---

<a id="item-5"></a>
## [Ladybird 发布首个 Alpha 版本，推出自研浏览器引擎](https://simonwillison.net/2026/Nov/23/ladybird/) ⭐️ 8.0/10

2026 年 11 月 23 日，Ladybird 项目发布了首个 Alpha 版本，提供了 macOS 和 Linux 的可安装二进制包，用户不再需要自行编译浏览器。该版本包含一个全新的独立浏览器引擎，拥有自研的 HTML 解析器、CSS 引擎、布局、JavaScript 以及 WebAssembly 实现。 独立浏览器引擎实际上被三家厂商主导，因此一个从零开始打造的引擎能够推出首个可安装的 Alpha 版本，是极为罕见的里程碑，有望切实提升 Web 平台的多样性，并让标准制定工作多出一个真正可测试的第四种实现。Simon Willison 的实测印象——渲染速度快、界面轻量直观——表明这个 Alpha 并非只是宣传噱头。 Ladybird 仍依赖少数外部组件：用于文字整形的 HarfBuzz、用于 2D 图形的 Skia、用于视频的 ffmpeg 以及用于存储的 SQLite；它像大多数浏览器一样把不同标签页隔离在独立进程中，但实测显示 WebContent 进程内存占用可达 819 MB。基于 ffmpeg 的工具和 Pyodide REPL 等重度依赖 WebAssembly 的负载可以正常运行，但 Datasette Lite 会报错 `undefined is not a function (evaluated from 'navigator.serviceWorker.startMessages')`，这对应源码中一个已存在的 FIXME 标注。

rss · Simon Willison · 11月23日 21:46

**背景**: Ladybird 最初是随 SerenityOS 一起开发的浏览器，而 SerenityOS 是 Andreas Kling 从零构建的桌面操作系统，其引擎代码很大一部分来自这个更为宏大的前身项目。从零编写浏览器引擎的成本极其高昂，这也是大多数新浏览器选择封装现有引擎、而非自行实现 HTML 解析、CSS、布局和 JavaScript 的原因。它所借用的外部组件都相当成熟：HarfBuzz 能把 Unicode 文本与字体结合，为任何书写系统生成位置正确的字形；Skia 则是开源的 2D 图形库，同时也是 Chrome、ChromeOS、Android 和 Flutter 的图形引擎。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://harfbuzz.github.io/">HarfBuzz Manual: HarfBuzz Manual</a></li>
<li><a href="https://skia.org/">Skia</a></li>
<li><a href="https://en.wikipedia.org/wiki/SerenityOS">SerenityOS - Wikipedia</a></li>

</ul>
</details>

**标签**: `#browsers`, `#open-source`, `#web-engines`, `#systems-programming`, `#web-standards`

---

<a id="item-6"></a>
## [美团推出统一推荐基座大模型 MTFM，首次实现外卖多业务统一精排](https://tech.meituan.com/2026/09/22/Meituan-Foundation-Model-for-Recommendation.html) ⭐️ 8.0/10

美团技术博客发布了一篇关于 MTFM 的工程实践文章，该模型在其此前的 MTGR 工作基础上构建，被描述为首次将外卖多个主要业务的精排阶段统一到同一个模型中的推荐基座大模型。与过去每条业务线各自维护独立排序模型不同，MTFM 将这些场景的精排能力整合进单一模型。 将异构业务线的精排统一起来，指向了“推荐系统基座模型”这一范式：用一个大骨干模型跨场景迁移，而不是维护众多任务专用模型，这会直接影响团队在训练与 serving 基础设施上的资源分配方式。如果该方案在生产中站得住脚，它就是美团规模下多域、多任务排序的一个有分量的工业界样本，对机器学习系统研究者和实际运维大型推荐系统的工程师都有参考价值。 目前可获得的摘要只有一句话，因此具体的架构选型、特征体系设计、线上 A/B 指标、延迟与成本权衡以及已知的失效场景都无法从这段摘录中看到。可以确认的是 MTFM 继承了 MTGR 的路线，而 MTGR 基于 HSTU 架构建模，并刻意保留了原有 DLRM 类模型的能力（包括交叉特征），这暗示 MTFM 把这条生成式推荐的技术脉络延伸到了多场景设定中。

rss · 美团 Blog · 11月25日 00:27

**背景**: MTGR（Meituan Generative Recommendation）是美团的工业级生成式推荐框架，其 2025 年的一篇 arXiv 论文称该框架基于 HSTU 架构建模，同时保留了原有深度学习推荐模型（DLRM）的能力，包括交叉特征，这种混合设计意在采纳生成式序列建模骨干的同时保留经典排序模型的优势。所谓“精排”是推荐流水线中用最重的模型对候选集打分的阶段，因此用单一共享模型替换多个按业务划分的精排模型，是一项分量很重的架构承诺。更广义的“推荐系统基座模型”研究方向正是在探索这件事：预训练大型骨干模型，并让其跨领域、跨任务迁移，也包括冷启动场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2505.18654">[2505.18654] MTGR : Industrial-Scale Generative Recommendation ...</a></li>
<li><a href="https://aitoolly.com/de/ai-news/article/2026-09-23-meituan-unveils-mtfm-a-unified-recommendation-foundation-model-powering-multi-scenario-food-delivery">Meituan MTFM : Einheitliches KI-Empfehlungsmodell | AIToolly</a></li>
<li><a href="https://arxiv.org/html/2402.11143">Foundation Models for Recommender Systems: A Survey and New...</a></li>

</ul>
</details>

**标签**: `#recommender-systems`, `#foundation-models`, `#large-scale-ml-systems`, `#industrial-deployment`, `#ranking`

---

<a id="item-7"></a>
## [AutoPILOT 框架让视觉智能体通过宏与控制器实现实时行动](https://arxiv.org/abs/2611.28202) ⭐️ 8.0/10

AutoPILOT 提出了一种新的视觉智能体框架：在一次模型调用中，模型既可以发出单个原子动作，也可以启动一段开环宏，或者直接编写一个闭环控制器，让它在无需再次调用模型的情况下持续根据屏幕像素进行操作，直到把控制权交还给模型。在与 VISTA 框架同等预算、同样使用 GPT-6.1 Sol 的条件下，AutoPILOT 的实时成功率达到 68.6%，而 VISTA 仅为 38.3%；作者同时发布了 AFK-Bench，一套包含 120 款浏览器游戏的测试集，并按游戏对“玩家不操作”的响应方式进行分组。 论文指出，框架如何把模型输出随时间转化为动作，是智能体设计中核心却长期被忽视的一环，因此这一方向的进展意义远不止于游戏——任何在模型思考期间仍在持续变化的界面或环境都会遇到同样的问题。由于 AutoPILOT 还能以大约五分之一的 API 成本达到 VISTA 的最终成功率，这说明改进框架设计可以在不换更强模型的前提下同时降低延迟和成本。 该框架提供三种逐级升级的动作粒度——单次原子动作、开环宏、以及由模型编写的闭环控制器——并且所报告的增益在多个模型上都成立；在 GameWorld 基准上，AutoPILOT 在实时条件下仍保持 80.0% 的成功率，而 VISTA 则从 84.1% 骤降至 42.9%。目前的评估仅基于论文摘要，完整的实验细节、控制器生成失败的情形，以及围绕模型自写代码的安全注意事项尚未公开说明。

rss · arXiv cs.AI · 11月24日 05:00

**背景**: 多模态基础模型在游戏会暂停等待它们时表现良好，但一旦游戏时钟持续运行，性能就会明显下降。所谓“框架”（harness）是指包裹在模型外面的脚手架，它决定模型看到什么、记住什么，以及模型的输出随时间如何被转化为动作；此前的 VISTA 等工作改进了观察与记忆环节，但每次模型调用仍最多只能产生一个动作，因此智能体的行动频率受限于模型的思考频率。AutoPILOT 针对的正是第三块拼图，并借用了控制论中开环执行（按固定脚本运行、不依赖反馈）与闭环控制（持续读取状态并自我纠正）的经典区分。AFK-Bench 的名字来自“away from keyboard”（离开键盘），它特意纳入那些会对“不操作”施加惩罚或奖励的游戏，从而直接衡量智能体在两次模型调用之间持续行动的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2611.28202">AutoPILOT: A Visual Agent Harness for Real-Time Gameplay</a></li>
<li><a href="https://explainx.ai/blog/autopilot-visual-agent-harness-afk-bench-november-2026">AutoPILOT Harness: 68.6% Real-Time Game Success - explainx.ai</a></li>
<li><a href="https://fast.io/resources/open-loop-vs-closed-loop-agents/">Open Loop vs Closed Loop: Designing AI Agent Loops | Fastio</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#multimodal models`, `#game AI`, `#benchmarking`, `#real-time systems`

---

<a id="item-8"></a>
## [当工具失效时，智能体编造：工具使用型 LLM 智能体中的静默失败与验证优先监督](https://arxiv.org/abs/2611.28341) ⭐️ 8.0/10

一项针对工具使用型 LLM 智能体的故障注入研究发现，其恢复能力并不可靠（正确率为 19–68%），且往往以静默方式发生；部分数据工具故障会导致高达 38%的运行中出现自信编造，这促使采取验证优先的监督。

rss · arXiv cs.AI · 11月24日 05:00

**标签**: `#LLM agents`, `#tool use`, `#agent reliability`, `#fault injection`, `#evaluation benchmarks`, `#AI safety`

---

<a id="item-9"></a>
## [OWASP 安全提示词使 AI 生成应用的漏洞减少三分之一，但依赖面翻倍](https://arxiv.org/abs/2611.28408) ⭐️ 8.0/10

arXiv 上的一项受控实验（编号 2611.28408）将 100 份冻结的规格说明各实现四次，把两款智能体编程工具（Claude Code、Codex CLI）与两种提示词交叉组合——一种不含（A 组）、一种含有（B 组）一段固定的 OWASP 对齐安全要求，共生成 400 个 Web 应用和 6,721 条经分诊的发现。追加安全要求块使每个应用的平均问题数下降约三分之一（发生率比 0.65，95% 置信区间 0.60–0.71），且两款工具效果一致，但同时使声明的依赖面大约翻了一倍。 这一结果表明，一段成本低廉、可移植的提示词附加内容——且在不同智能体工具上都有效——能够显著改善 AI 生成应用的安全状况，这对任何使用编程智能体交付代码的团队都具有意义。但与此同时，依赖面翻倍说明这种收益并非没有代价：安全导向的提示把风险转移到了软件供应链上，需要另行审计。 在校正了扩大的依赖面之后，每个应用的依赖告警率并未上升（按应用计持平，汇总层面低 18%），而第一方源码中的高危问题减少了近一半；作者认为额外依赖源于库的选择，而非安全要求本身。研究使用固定的静态与动态扫描流水线，并采用计数混合模型、逻辑混合模型以及依赖差异分析，因此所有数字都是相对于该特定工具链的。

rss · arXiv cs.AI · 11月24日 05:00

**背景**: Claude Code 和 Codex CLI 这类智能体编程工具会把自然语言规格说明直接变成一个可运行的 Web 应用，因此它们在认证、会话处理、输入校验和第三方库上的默认选择，实际上就成了该应用的安全状况。OWASP 是一家非营利组织，发布诸如 Top 10 和 Cheat Sheet 系列等被广泛采纳的共识性安全指南，因此“OWASP 对齐要求”指的是一段清单式的安全要求，可粘贴进提示词中。所谓“声明的依赖面”，是指应用所声明的第三方包集合（类似 SBOM），它决定了应用在供应链告警中暴露的程度。发生率比为 0.65 意味着处理组每个应用的问题数比对照组少 35%。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cheatsheetseries.owasp.org/cheatsheets/Secure_Coding_with_AI_Cheat_Sheet.html">Secure Coding with AI - OWASP Cheat Sheet Series</a></li>
<li><a href="https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html">AI Agent Security - OWASP Cheat Sheet Series</a></li>
<li><a href="https://anchor-defense.com/sbom-components-guide/">Common Components Found in a Software Bill of... - Anchor Defense</a></li>

</ul>
</details>

**标签**: `#AI coding agents`, `#application security`, `#empirical study`, `#LLM evaluation`, `#software supply chain`

---

<a id="item-10"></a>
## [Agent Money 基准测试：AI 智能体能否被信任花好钱？](https://arxiv.org/abs/2611.28610) ⭐️ 8.0/10

研究者提出了 Agent Money 基准测试（AMB），用 80 个搭配模拟卖家的支付任务和 76 个使用实时数据的研究问题来评估 12 个 AI 模型，所有购买都通过 x402 协议以 USDC 在 Solana 主网上结算。12 个模型中只有 3 个能在 80 个支付任务中完成 79 个而不出现支付或预算错误，另有 9 个模型至少一次落入卖家的陷阱，重复扣费和高于标价的报价合计占诈骗事件的 79%。 当智能体从回答问题转向真正购买数据、向供应商付款和转移资金时，它们的失误会直接变成财务损失，因此基准测试需要衡量“花钱的判断力”而不仅是任务完成度。在 x402 这类自主商业协议让机器发起支付变得可行之际，AMB 为研究者和开发者提供了一个具体、以成本为尺度的智能体可信度衡量标准。 该基准通过把失败的支付任务全额计入、把研究答案按失分比例计入来估算浪费，在两条赛道支出均分的情况下，Claude Fable 5.2 每花费 100 美元浪费 21.0 美元，而 GPT-6 Luna 高达 70.8 美元。需要注意的是，这是一篇摘要被截断的预印本，卖家是模拟的而非真实对抗性商家，且范围仅限于为金融决策购买信息这一场景。

rss · arXiv cs.AI · 11月24日 05:00

**背景**: x402 是一个围绕 HTTP 402“需要付款”状态码构建的开放支付协议：服务方返回支付指令，客户端在正常的请求流程中以编程方式完成付款，无需账户、会话或 API 密钥。USDC 是一种锚定美元的稳定币，Solana 则是高吞吐、低手续费的区块链，常用于此类稳定币支付流程，使按请求计费的微支付对智能体而言变得可行。传统智能体基准测试衡量的是智能体能否完成任务，而 AMB 追问的是能否放心地给它一个钱包——在智能体可以自主交易的今天，这正成为一条新的评估维度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://x402.org/wp-content/uploads/sites/10/2026/06/x402-whitepaper.pdf">x402: The Payment Protocol for Agentic Commerce</a></li>
<li><a href="https://developers.cloudflare.com/agents/tools/payments/x402/">x402 · Cloudflare Agents docs</a></li>
<li><a href="https://agentmoneybench.com/">Agent Money Benchmark: Can AI agents be trusted with money?</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#agent safety`, `#benchmarks`, `#autonomous payments`, `#financial decision-making`

---

<a id="item-11"></a>
## [LLM“数字分身”能通过模拟初次对话预测真实好感度](https://arxiv.org/abs/2611.28692) ⭐️ 8.0/10

研究人员利用 CANDOR 语料库中的对话数据，为 710 位真实个体构建了 LLM 分身，并让这些分身在 5,680 场模拟初次对话中彼此“见面”，再用 355 对参与者互不重叠的留出真实配对进行检验。结果显示，分身的预演对话能够预测真人的实际好感度（ρ=0.277），并且携带了问卷和个人评分历史之外的额外信息（偏相关 ρ=0.16 [0.05, 0.26]），大约复现了人类读者从真实对话中获取信号的 0.321。 这项研究罕见地提供了严谨证据，说明模拟特定个体的 LLM 智能体能够预测真实社交结果——这一主张通常只由智能体演示来宣称，而少有实测，因此对 AI 智能体、个性化、社会模拟和人机交互研究都有意义。它还重新定义了设计目标：分身真正需要的是习得的评价判断能力，而非逼真地模仿主人的说话风格。 置换对照实验表明，预测信号是通过对话本身而非“人设卡片”传递的；而让分身更像主人那样说话——使用个体专属的激活引导（activation steering）以及在其本人语音/话语上训练的 LoRA——在预注册检验中并无帮助，并在探索性第二轮中反而降低了准确率（-0.183 [-0.294, -0.066]）。一个小的“评价头”模型将分身的事后回答与主人的评分历史结合后，使基于预演的预测在折外超越历史基线（+0.059 [0.001, 0.115]，而无分身回答时仅为 +0.022），不过预注册的主要对比（+0.056 [-0.001, 0.111]）跨越零值；此外该研究为预印本，且只聚焦初次对话中的好感度，而非广泛的任务能力。

rss · arXiv cs.AI · 11月24日 05:00

**背景**: CANDOR 是一个大型公开多模态语料库，收录了约 1,650 场陌生人在视频聊天中进行的自然对话，并附带丰富的前测与后测问卷数据，因而非常适合研究人们如何形成印象。研究中使用两种常见的 LLM 技术来构建分身：激活引导（activation steering），即直接操控模型内部激活，使输出偏向某一概念或风格；以及 LoRA，一种参数高效微调方法，它冻结基础权重、注入少量可训练的低秩矩阵。论文的核心问题是：这样的分身能否在社交层面代表其主人，以及究竟是风格、陈述的偏好还是判断力在驱动准确预测。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.science.org/doi/10.1126/sciadv.adf3197">The CANDOR corpus: Insights from a large multimodal dataset ...</a></li>
<li><a href="https://convokit.cornell.edu/documentation/candor.html">CANDOR Corpus — convokit 5.0.0 documentation</a></li>
<li><a href="https://en.wikipedia.org/wiki/LoRA_(machine_learning)">LoRA (machine learning) - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2410.12877">[2410.12877] Improving Instruction-Following in Language ... Efficient and accurate steering of large language models ... DiffuSteer: Conditional generative steering of large language ... Activation Steering: A New Frontier in AI Control—But Does It ... Latent Feature Activation Steering for Enhancing Semantic ...</a></li>

</ul>
</details>

**标签**: `#LLM agents`, `#social simulation`, `#personalization`, `#human-AI interaction`, `#evaluation`

---

<a id="item-12"></a>
## [DiscernBench：评估 LLM 智能体在机构场景中的协同判断力](https://arxiv.org/abs/2611.28787) ⭐️ 8.0/10

研究者提出了 DiscernBench，这是一个用于评估“协同判断力”的新基准，即 LLM 智能体在机构场景中应当选择遵从、拒绝还是上报请求。该基准的场景取自航空、执法和应急管理等领域的真实事件报告。研究团队在三种决策配置下评测了 8 个 LLM，并同时分析最终决策与多智能体审议过程中产生的中间判断。 论文记录了一种具体的多智能体失效模式——“少数信号覆盖”（Minority-Signal Override），即某一位专家的建议会不成比例地左右集体决策。角色专门化的审议将平均过度上报率从单智能体直接判断时的 3.79% 提升到 28.27%，这一发现直接关系到团队如何为高风险业务场景设计和治理智能体系统。 少数信号影响的方向和幅度在不同模型与不同专家角色之间差异显著，说明不存在可普遍适用的聚合行为。作者认为，仅凭最终答案的准确率无法刻画这些集体决策动态，因此可信的多智能体系统不仅要评估单个专家的推理能力，还要评估相互冲突的判断是如何被转化为集体决策的。

rss · arXiv cs.AI · 11月24日 05:00

**背景**: LLM 智能体是指在语言模型基础上配备工具、记忆和执行循环，使其不仅能回答问题还能采取行动的系统，目前越来越多地被提议用于受监管或安全攸关机构的业务流程中。在这类机构场景里，除了简单“遵从”或“拒绝”之外，“上报”（将决策交由人类或更高层级权威处理）是一项核心安全机制。多智能体审议——即多个角色专门化的智能体（如政策专家与安全专家）先进行辩论，再由最终响应者拍板——是一种常见的、旨在提升可靠性的设计模式。DiscernBench 检验的正是这种模式是否真的改善了判断，并表明聚合机制的重要性不亚于底层模型本身的能力。

**标签**: `#LLM agents`, `#benchmark`, `#AI safety`, `#multi-agent deliberation`, `#evaluation`

---

<a id="item-13"></a>
## [SMB Bench：90 天模拟器检验语言模型智能体能否应对延迟后果](https://arxiv.org/abs/2611.28158) ⭐️ 8.0/10

研究者发布了 SMB Bench——一个经过校准的 90 天批发业务模拟器，包含 18 个存在因果配对的任务以及 859 条前沿模型运行轨迹数据集；结果显示，在 16 个前沿模型中只有 3 个能超过一条固定的采购规则。在许多运行中，模型甚至在笔记里写下了正确的诊断，却没能及时改变后续采购，说明“发现问题”与“据此行动”是两回事。团队还用历史经营记录训练了一个开放模型（Qwen3.8-27B），并把归档的前沿模型季度作为起始状态，使其在未见过的测试业务上更一致地遵守客户保护承诺，并减少了严重亏损的季度。 随着语言模型智能体从单轮任务转向持续多日的运营，识别并回应数周后才显现的后果已成为一项核心能力，而不再是可有可无的加分项。SMB Bench 为智能体研究者提供了一个可复现、经过校准的环境和一份轨迹数据集来衡量这一能力，而“前沿模型几乎打不过一个简单启发式规则”的结论，对任何打算把智能体投入业务运营的人来说都是一个值得警醒的信号。 该基准把 18 个存在因果关联的任务与一个 90 天模拟相结合，其中空货架会掩盖流失的进店需求，发货不足的客户会在数周后悄然减少订单；作者指出，诊断问题、持续改变行为、提升利润是三项彼此独立的成就。在训练实验中，额外的利润收益仍不确定，而在整季度贯彻客户保护承诺也暴露出真实代价：季度初的备货习惯使采购方依赖紧急补货，并导致供应商关系恶化。

rss · arXiv cs.LG · 11月24日 05:00

**背景**: 大语言模型智能体越来越多地被用于执行持续性运营任务，而不再只是回答孤立问题；但在这种场景下，今天的决策会重塑明天的观测与现金约束，从而产生“延迟信用分配”问题：判断究竟是过去哪个动作导致了后来的结果。信用分配是强化学习中长期存在的难题，近来也出现了 AgentGym-RL 等面向长程决策的智能体训练框架来处理多轮决策。SMB Bench 由 ORO AI 团队发布在 arXiv 上，并可通过 Hugging Face 上的排行榜浏览，它以中小型批发业务作为检验这些问题的具体试验场。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2611.28158">[2611.28158] Measuring and Teaching Language Model Agents to ...</a></li>
<li><a href="https://oroagents.com/benchmarks/smb-bench">SMB Bench v1.0: an AI agent benchmark for small business | ORO AI</a></li>
<li><a href="https://huggingface.co/spaces/oro-agents/smb-bench">SMB Bench - a Hugging Face Space by oro-agents</a></li>

</ul>
</details>

**标签**: `#LLM agents`, `#benchmark`, `#long-horizon decision-making`, `#credit assignment`, `#agent evaluation`

---

<a id="item-14"></a>
## [AI 智能体无需反向传播，即可将新能力直接写入语言模型权重](https://arxiv.org/abs/2611.28483) ⭐️ 8.0/10

一篇新的 arXiv 预印本（2611.28483v1）报告称，一个 AI 智能体可以在不进行反向传播、也完全不针对任务答案拟合权重的情况下，通过向已冻结的预训练语言模型内部层插入门控注意力头（gated attention heads）和 MLP 神经元，把新能力写入模型之中。该智能体仅有 50 次模型前向调用的预算，且看不到任何验证集或测试集实例，却将 Qwen2.5-1.5B-Instruct 的 BIG-Bench Hard 归一化分数从 19.95 提升到 41.05，将 Gemma-3-1B-it 从 10.25 提升到 32.86；同时还写入 20 位以内的精确乘法能力（在密封测试的未见长度上达到 100.0%，而相同预算下的 LoRA 最多只有 2.1%）。 如果这些结果能够被复现，这就指向了一条与微调或 LoRA 截然不同的模型改进路径：由智能体驱动的模块化能力注入，并且据称在无关输入上让基座模型的行为保持完全一致（KL 恰好为 0）。这对避免灾难性遗忘的持续学习、模块化模型编辑以及机制可解释性都具有重要意义，因为它暗示特定能力可以被定位并以可分离组件的形式写入权重。 该研究采用预注册方式：任务集、规则与报告语句在首次会话之前就已封存于 git，其清单带有比特币时间戳，并由一个冻结的评估器对密封测试只运行一次，报告称大多数假设（H5、H6、H8、H9、H10、H12）成功，只有 Gemma 在 H9 上得到部分成功的结果。作者也披露了失败情况——45 个单模块中有 4 个出现轻微副作用，50 次会话中有 5 次在 12 小时时限内未能产出模块——并且该组合模型据称在 1,023,000 个 WikiText token 上保持下一 token 分布不变；但这一切都来自一篇尚未经过同行评审的单一预印本，仍需独立复现。

rss · arXiv cs.LG · 11月24日 05:00

**背景**: BIG-Bench Hard（BBH）是一个广泛使用的基准，由 23 个特别困难的 BIG-Bench 任务组成，此前的语言模型在这些任务上未能超过普通人类评分者的平均水平，因此归一化分数从约 20 分跃升到约 41 分是相当可观的。Qwen2.5-1.5B-Instruct 和 Gemma-3-1B-it 都是小型指令微调对话模型，实验成本较低。通常新能力是通过基于梯度的训练加入的，例如 LoRA 这种参数高效微调方法，它更新低秩适配器权重；而这里智能体改为插入门控注意力头（其输出由学习到的门控进行调制的注意力模块）和额外的 MLP 神经元，同时冻结原始权重。摘要中给出的 KL 散度数值衡量的是修改后模型的输出分布相对原模型偏移了多少——恰好为 0 意味着在这些输入上没有可测量的变化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepeval.com/docs/benchmarks-big-bench-hard">BIG-Bench Hard | DeepEval - The LLM Evaluation Framework</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct">Qwen/ Qwen 2 . 5 - 1 . 5 B - Instruct · Hugging Face</a></li>
<li><a href="https://huggingface.co/QwQZh/gated_attention">QwQZh/gated_attention · Hugging Face</a></li>

</ul>
</details>

**标签**: `#LLM capability injection`, `#model editing`, `#AI agents`, `#mechanistic interpretability`, `#evaluation benchmarks`

---

<a id="item-15"></a>
## [训练神经符号式语言模型外壳可实现组合泛化](https://arxiv.org/abs/2611.28298) ⭐️ 8.0/10

一篇新的 arXiv 论文（2611.28298）提出，在强化学习后训练阶段训练本身即为神经符号式的语言模型外壳（harness，例如递归语言模型 RLM），可以让模型学会对任务进行分解，使其神经网络接收到的每一次观测都处于局部同分布范围内。作者报告称，仅在短任务上训练即可泛化到长 2–64 倍的任务；在一个领域训练可迁移到共享潜在结构的新领域；并且用其称为“代理外壳训练”的方法在合成数据上训练出的 RLM-27B，在同一外壳下于 CTC-Bench 和 ExpertLongBench 等困难长上下文任务上平均优于 Qwen3.8-27B 达 26.9%，同时推理时使用的 token 数约少 2 倍。 这为长程智能体训练指出了一条更省算力的路径：与其强迫神经网络在不断累积膨胀的上下文中做泛化，不如让外壳以程序化方式完成分解，从而有可能大幅提升算力回报。如果结论成立，研究重心将从扩展上下文和后训练数据转向设计与训练模型外围的脚手架，这会影响所有构建智能体系统或对智能体进行强化学习后训练的团队。 该工作提出了“代理外壳训练”（surrogate harness training）：通过生成带有虚假工具调用和子调用的、更简单的合成环境，来针对性地训练外壳内部的单次 LLM 调用；论文还进一步表明，外壳可以借助递归的子外壳调用在所习得的分解之上进行组合。需要注意的局限是：这只是一篇早期 arXiv 摘要，结果被截断，未经过同行评审，完整方法也尚不可见；核心数字来自一个 27B 模型在两个长上下文基准套件（CTC-Bench 与 ExpertLongBench）上的评测。

rss · arXiv cs.CL · 11月24日 05:00

**背景**: 所谓“外壳”（harness）是指模型作为智能体部署时包裹在其外围的脚手架，负责管理提示词、工具调用、记忆与控制流；在标准设计中，对话和工具输出只是不断堆叠为上下文，交由神经网络自行应对。神经符号式外壳则把神经模型与显式的符号程序逻辑配对，由程序将上下文外化并加以管理，因此任务分解由确定性的代码完成，而非隐式学习得到——递归语言模型（RLM）就是这类设计之一，它可以递归地调用子外壳。组合泛化指的是模型能够解决训练中只分别见过、但组合起来全新的子问题，而这正是长程智能体任务所要求的核心能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.alphaxiv.org/abs/2611.harness-cg">Language Model Harnesses Can Be Compositional ... | alphaXiv</a></li>
<li><a href="https://matthewkruczek.ai/blog/neurosymbolic-harness.html">Why Your Agent Forgets the Rules: The Neurosymbolic Case for the...</a></li>
<li><a href="https://signaldiff.news/events/long-horizon-agent-harnesses">Long - horizon agent harnesses | Signal Diff</a></li>

</ul>
</details>

**标签**: `#language model agents`, `#compositional generalization`, `#neurosymbolic AI`, `#reinforcement learning`, `#LLM harnesses`

---

<a id="item-16"></a>
## [Muted Distillation：对教师隐藏学生推理，智能体输出 token 减少 57%](https://arxiv.org/abs/2611.28445) ⭐️ 8.0/10

一篇新的 arXiv 论文（2611.28445）提出了 Muted Distillation（MD），这是面向多轮 LLM 智能体的在线策略蒸馏（OPD）的一种变体：在教师模型为学生行为打分时，把学生的推理过程隐藏起来。与标准 OPD 相比，MD 在 OfficeQA Pro 上把每个回合的输出 token 减少了 57%，在 SpreadsheetBench 上减少了 53%，同时在 OfficeQA Pro 上保持与 OPD 相同的准确率，并在 SpreadsheetBench 上把 pass@1 提升了 4.8 个百分点。 推理长度膨胀是已部署智能体系统成本的直接来源，因此一种能把输出 token 减半、同时保持甚至提升准确率的改动，对所有提供多轮智能体服务的团队都有立竿见影的实用价值。该方法的另一亮点是简单——只需几行代码，不需要额外数据或超参数——因此可以作为一个即插即用的改动，直接加入现有的 OPD 后训练流程。 作者通过实证分析认为，学生推理变长的原因在于学生的推理会“干扰”教师的打分信号，因此干脆把这条通道完全切断。评估范围仅限于两个知识工作类智能体基准（OfficeQA Pro 和 SpreadsheetBench），摘要中没有给出其他智能体领域或不同模型规模的结果，因此泛化性仍有待验证。

rss · arXiv cs.CL · 11月24日 05:00

**背景**: 在线策略蒸馏是一种后训练技术：由学生模型自己生成轨迹，再由更强的教师模型对这些轨迹打分或给出稠密反馈，从而兼具在线策略训练的可靠性和稠密奖励信号的效率。在多轮智能体任务中，学生在每次行动前都会写出较长的推理，已有工作观察到这种推理在 OPD 训练后往往会变长，从而推高推理成本。OfficeQA Pro 是一个面向异构文档语料、考察有据可依的多文档推理的企业级基准，SpreadsheetBench 则评测智能体在电子表格操作任务上的表现；pass@1 指一次尝试即完成任务的比率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thinkingmachines.ai/blog/on-policy-distillation/">On-Policy Distillation - Thinking Machines Lab</a></li>
<li><a href="https://arxiv.org/html/2603.08655">OfficeQA Pro : An Enterprise Benchmark for End-to-End Grounded...</a></li>
<li><a href="https://llm-boss.com/blog/pass-at-k-explained">pass @k, maj@k and Sampling: LLM Eval Metrics Explained | LLM Boss</a></li>

</ul>
</details>

**标签**: `#LLM post-training`, `#knowledge distillation`, `#agentic AI`, `#token efficiency`, `#reasoning`

---

<a id="item-17"></a>
## [PBPT：面向大模型后训练的种群式超参数自动调优方法](https://arxiv.org/abs/2611.29014) ⭐️ 8.0/10

一篇新的 arXiv 论文（2611.29014）提出了“种群式后训练”（Population-Based Post-Training，PBPT）：在 RLVR 框架下并行训练多个大模型，并周期性地在验证集上评估它们，表现好的模型会被复制并扰动其超参数，表现差的模型则停止训练并被这些副本取代。在推理基准（Enigmata、Nemotron）以及交互式工具使用环境（Gaia2、AppWorld）上，PBPT 训练出的智能体优于算力匹配的独立 RLVR 学习器组。 超参数敏感是 RLVR 后训练中公认的痛点，从业者通常要连续跑多次训练、再挑选最好的一次来调参。PBPT 把这一搜索过程并入单次训练，并证明它能够从糟糕的初始超参数中自动恢复，这有望节省算力，并让强化学习后训练对构建推理模型和工具使用智能体的团队来说更加稳健。 PBPT 会周期性地在验证集上评估整个模型种群，随后复制表现好的模型并扰动其超参数，同时终止并替换表现差的模型；所有对比都在与独立 RLVR 学习器算力匹配的条件下进行。评估同时覆盖静态推理基准和交互式工具使用环境，但摘要并未量化种群规模、扰动策略以及性能提升的具体幅度。

rss · arXiv cs.CL · 11月24日 05:00

**背景**: 带可验证奖励的强化学习（RLVR）是一种流行的后训练范式：模型依据客观、可由程序自动检查的奖励进行训练——例如通过单元测试或匹配已知数学答案——而不是依赖学习得到的奖励模型，从而减少奖励作弊和对人工标注的依赖。种群式训练（PBT）是一种受遗传算法启发的超参数优化技术：它不训练单个模型，而是维护一个模型种群，周期性地复制并扰动表现最好的成员的权重与超参数，同时淘汰表现最差的成员。AppWorld 等基准测试的是智能体在多个模拟应用中完成多步任务的能力，考察代码生成、API 调用与状态管理，而不仅仅是单轮问答。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ultralytics.com/glossary/reinforcement-learning-with-verifiable-rewards-rlvr">RLVR : Training on Verifiable Rewards | Ultralytics</a></li>
<li><a href="https://arxiv.org/html/2404.08233">Generalized Population - Based Training for Hyperparameter ...</a></li>
<li><a href="https://benchmarkingagents.com/appworld-benchmark/">AppWorld Benchmark : 750 Tasks Across 9 Apps , Code-as-Action</a></li>

</ul>
</details>

**标签**: `#LLM post-training`, `#reinforcement learning`, `#population-based training`, `#hyperparameter optimization`, `#tool-use agents`

---

<a id="item-18"></a>
## [VidRouteBench 基准让文本生成视频的预算感知路由成为可能](https://arxiv.org/abs/2611.28099) ⭐️ 8.0/10

研究者发布了 VidRouteBench，这是一个基准与数据集，覆盖来自 7 个开源视频生成家族的 16 个"臂"（模型与采样配置的组合），实测成本跨度达 121 倍，从每条视频 0.0025 美元到 0.298 美元。它包含 1,625 个分组提示词上生成的 27,110 条视频（消耗 1,421 A800 小时）、9 个可识别质量维度的逐条打分、重复随机种子、加密测试集，以及一个用于冷启动评估的密封新家族模型；其质量评分器在针对人类偏好校准后冻结，交叉验证准确率为 68.7%，而最佳单一评分器为 66.2%。 文本生成视频模型的价格差异高达约两个数量级，但现有公开的视频偏好数据集只覆盖闭源模型的单一配置，因此此前没有数据可以研究"在固定预算下把每个提示词路由到更便宜的配置是否更划算"这一问题。VidRouteBench 让这个问题可以实证检验，并表明视频生成中的逐提示词特化是真实存在且部分可复现的——这与大语言模型路由不同，同样的流程在那里没有发现这种效应。 该评测框架将路由器与"提示词无关的最佳臂混合"作对比，而不是与单一最佳臂对比，并报告了 0.642 的预言机差距（oracle gap）、跨随机种子 47% 的可复现性，以及 F=4.47、p=1.6e-63 的提示词与臂交互效应。作者还提出 OPMU（一次探测、多种效用）方法：用 K 个探测提示词为新臂打标签，一次性预测其 9 个质量维度，之后再标量化以服务任意效用场景；在 215 个效用方向上，它在 94% 的方向上帕累托优于提示词无关基线，而逐场景路由器的这一比例为 90%，且无需逐场景重新训练。

rss · arXiv cs.CV · 11月24日 05:00

**背景**: Veo、Kling 等文本生成视频服务通常提供多个模型变体和设置（分辨率、时长、采样数量），不同配置下每条视频的价格可能相差悬殊。"模型路由"指的是把每个请求发送给预期能对该输入产生最佳结果的模型或配置，这一技术在大型语言模型上已有研究。视频领域的一个关键障碍是：此前没有任何公开数据集能把逐提示词的质量测量与跨多种配置的成本标注配对起来；而用于生成这些视频的 A800 GPU 是 Ampere 架构加速卡，通常按小时租用运行 AI 任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/google/veo-3.1">Veo 3.1 - Video Generation API Pricing | OpenRouter</a></li>
<li><a href="https://www.nvidia.com/en-us/products/workstations/a800/">A800 40GB Active Graphics Card | NVIDIA</a></li>
<li><a href="https://developers.google.com/machine-learning/crash-course/overfitting/dividing-datasets">Datasets: Dividing the original dataset | Machine Learning ...</a></li>

</ul>
</details>

**标签**: `#video-generation`, `#benchmark`, `#model-routing`, `#evaluation`, `#AI-systems`

---

<a id="item-19"></a>
## [审计揭示：最强生成器加拒绝重试即可追平多数智能体文生图增益](https://arxiv.org/abs/2611.28116) ⭐️ 8.0/10

一篇新的 arXiv 论文（2611.28116）使用各系统官方评测器审计了四个近期智能体文生图系统，发现一个极简基线——单工具拒绝重试（SRR）：直接采用系统候选池中已有的最强生成器，配一个现成验证器，在相同预算下反复生成直到出现第一张被接受的图像——就能复现大部分被报告的组合性增益。在 GenEval 上，SRR 达到 0.962 的准确率，而 OctoT2I 为 0.96；按验证器不同可回收 GEMS 增益的 63% 至 90%；并且以平均每张图 2.3 次生成的代价超过 GenPilot 12 个百分点。 这一结果挑战了“智能体”流水线增益的宣称与报告方式：如果不设置拒绝采样基线，论文可能把本质上只是“用验证器做 best-of-N 选择”的效果，归功于规划、路由与精修等机制。由于该批评具有很强的通用性——给出了闭式上界、一份报告清单，并在其他生成器和 T2I-CompBench++ 上得到验证——其意义远超图像生成，适用于更广泛的智能体系统评测。 一项闭式分析可预测 SRR 在任意预算下的准确率，并表明其提升幅度受验证器似然比的上限约束；同时证明跨生成器路由最多只能带来 1 至 3 个百分点的准确率提升（在 OctoT2I 自身的模型池上），也就是说 OctoT2I 的路由换来的是在同等准确率下约 2.5 倍的计算节省，而非更高的准确率。该分析还识别出真正属于智能体的增益：在 GenEval 2 上，即便由评测器从五个样本中挑出最优者，仍比 GEMS 报告分数低 15 个百分点（即使取其 95% 置信区间上端也低 12 个百分点）；离线蒸馏实验则显示，被选中的样本对生成器的教学效果并不优于随机样本。

rss · arXiv cs.CV · 11月24日 05:00

**背景**: 智能体文生图系统会把图像生成器包裹进规划、工具/模型路由、验证与精修的循环之中，并且通常在 GenEval、T2I-CompBench++ 等组合性基准上报告大幅提升——这些基准考察模型能否正确绑定属性、数清物体数量并遵守空间关系。此类增益几乎总是相对于单一生成器的单次采样来衡量，这就把“智能体机制本身的价值”与“多采样再筛选的价值”混为一谈。拒绝采样——生成多个候选并保留验证器打分最高的第一个——是一种经典技术，其收益完全取决于验证器区分好坏输出的能力，而这一能力可由验证器的似然比来刻画。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.01803">[2606.01803] OctoT2I: A Self-Evolving Agentic Text-to-Image ...</a></li>
<li><a href="https://arxiv.org/html/2606.01803">OctoT2I: A Self-Evolving Agentic Text-to-Image Router - arXiv.org</a></li>

</ul>
</details>

**标签**: `#text-to-image`, `#agentic systems`, `#evaluation methodology`, `#rejection sampling`, `#benchmarks`

---

<a id="item-20"></a>
## [RadioVISTA 基准测试：视觉语言模型能否从城市图像推断不可见的无线电场](https://arxiv.org/abs/2611.28123) ⭐️ 8.0/10

一篇新的 arXiv 论文（2611.28123）提出了 RadioVISTA，这是一个基准与训练数据集，其底层是一个无标注引擎，可把地球上任意坐标转换为可做射线追踪的城市仿真，并生成匹配的单因素反事实样本，答案被精确计算得出。作者在六大洲的前沿视觉语言模型上测试后发现一种“场—路径解离”现象：模型能够判断无线电场在哪里强，却无法判断某处只存在一条直射路径还是存在一条经墙面反射的路径。 这一结果暴露了当前视觉语言模型在物理推理上的具体短板：它们能根据视觉线索近似出一张平滑的场强图，却没有真正还原产生该场强的底层传播几何结构。对于希望用多模态模型做无线网络规划、数字孪生建模，或让具身智能体推理“相机看不见的信号”的人来说，这一点非常关键。 开源模型在“读场”这一步就失败得更早，得分甚至低于随机猜测——即使给它四次尝试中任意一次正确就算对也依然如此；在未见过的城市上，微调能让一个 9B 的开源模型在场强预测上接近前沿闭源模型，但监督微调和强化学习微调都无法改善路径追踪能力。作者因此得出结论：只用最终答案做监督，只能让模型学会近似场强，却无法让它掌握单条路径的几何关系。

rss · arXiv cs.CV · 11月24日 05:00

**背景**: 无线电信号对相机而言不可见，但它在城市中的强弱很大程度上由图像中可见的建筑物和街道决定，因为电波是沿直射、反射和绕射等多条路径传播的。射线追踪是计算这些多径贡献的标准仿真技术，近期研究正推动无线电传播的快速、可微射线追踪模型。视觉语言模型把图像编码器与语言模型结合，使系统能回答关于图片的问题；DeepPHY 以及空间—物理推理探测等基准已开始检验它们是在真正进行物理推理，还是仅在做模式识别。RadioVISTA 进一步引入受控反事实——即只改变单一物理因素的干预——从而使正确答案无法仅靠表面相关性获得。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2509.19337">Radio Propagation Modelling: To Differentiate or To Deep Learn, That...</a></li>
<li><a href="https://huggingface.co/papers/2508.05405">Paper page - DeepPHY: Benchmarking Agentic VLMs on Physical ...</a></li>
<li><a href="https://christophm.github.io/interpretable-ml-book/counterfactual.html">15 Counterfactual Explanations – Interpretable Machine Learning</a></li>

</ul>
</details>

**标签**: `#vision-language models`, `#radio propagation`, `#physical reasoning`, `#benchmark`, `#ray tracing`

---

<a id="item-21"></a>
## [VideoJSON：极简 JSON 索引加编码智能体，超越专用视频记忆系统](https://arxiv.org/abs/2611.28167) ⭐️ 8.0/10

一篇新的 arXiv 预印本（2611.28167）提出 VideoJSON：一种用于超长视频理解的极简框架，在索引阶段由视觉语言模型把每一分钟视频转换成一条 JSON 记录，其中包含一段稠密描述以及事件、实体、地点、语音转写等结构化字段。查询时，编码智能体在沙箱容器中自行编写 Python 或 Bash 程序，多步地对这些记录进行过滤、关联和读取；搭配 DeepSeek V4.1 Flash，它在 EgoLifeQA、Ego-R1-Bench 和 MM-Lifelong Week 上分别以 7.0、20.0 和 24.75 分的优势超过专门构建的 MAGIC-Video 记忆系统，并比此前最佳的 EgoMemReason 成绩高出 12.6 分。 这一结果对当前为长视频智能体构建复杂记忆图和固定检索流程的主流思路提出了反证，说明「简单的结构化索引 + 以代码为动作的搜索」可能是更强也更通用的设计。如果该结论成立，这一思路的适用范围远超视频领域——任何需要在大量异构记录中检索的智能体都可借鉴——并对智能体研究、长上下文推理和视频理解产生直接影响。 消融实验表明，智能体式代码搜索和结构化 JSON 记录这两个组件共同带来了性能提升，而额外增加按小时摘要、更多工具或原始视频访问权限，只会让平均分变动不到 1.5 分；此外，仅用从一段无关的 100 小时直播中采集的 64 条 VideoJSON 轨迹对 Qwen-3.5-Flash 做微调，就能把其 MM-Lifelong 成绩提升最多 8.25 分。需要注意的是：这只是单篇预印本，代码尚未发布（称将在正式发表后开源），也没有可见的局限性章节；摘要中所说的「四个基准」实际上是三项正面对比，外加一次与此前已公布成绩的比较。

rss · arXiv cs.CV · 11月24日 05:00

**背景**: 超长视频——例如长达数天乃至数周、以第一人称视角连续拍摄的生活记录——远远超出任何模型的上下文窗口，因此系统通常先把视频索引成某种记忆表示，在问题到来时再检索相关片段。此前的 MAGIC-Video、Ego-R1 等方案会构建复杂的记忆图或固定的工具调用流程，从而限制了智能体搜索的灵活度。EgoLifeQA 和 Ego-R1-Bench 都是基于长达一周的第一人称录像构建的问答基准，专门用于测试这类跨越长时间线的推理能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/egolifeqa">EgoLifeQA : Egocentric Video QA Benchmark</a></li>
<li><a href="https://egolife-ai.github.io/Ego-R1/">Ego-R1: Chain-of-Tool-Thought for Ultra-Long Egocentric Video ...</a></li>
<li><a href="https://arxiv.org/abs/2506.13654">[2506.13654] Ego-R1: Chain-of-Tool-Thought for Ultra-Long ... Ego-R1: Chain-of-Tool-Thought for Ultra-Long Egocentric Video ... GitHub - egolife-ai/Ego-R1: [TPAMI 2026] Ego-R1: Agentic ... EGO-R1: CHAIN OF-TOOL-THOUGHT FOR ULTRA ... - OpenReview Ego-R1: Agentic Chain-of-Tool-Thought for Ultra-Long ... Ego-R1: Chain-of-Tool-Thought for Ultra-Long Egocentric Video ...</a></li>

</ul>
</details>

**标签**: `#agents`, `#video-understanding`, `#long-context`, `#retrieval`, `#tool-use`

---

<a id="item-22"></a>
## [NAVSIMv1 测试场景紧邻训练数据，导致驾驶分数虚高](https://arxiv.org/abs/2611.28177) ⭐️ 8.0/10

一篇新的 arXiv 论文（2611.28177）指出，在端到端驾驶标准基准 NAVSIMv1 中，89.6% 的测试场景与某个训练场景的距离在 4 米以内。作者构建了一个地理上完全不重叠的划分，并在同一批双方都未见过的新场景上重新评测，结果显示基于传感器的规划器 DiffusionDrive、Latent TransFuser 和 DrivoR 的 PDMS 分数下降了 3.4 到 6.1 分，而无传感器基线仅下降 1.5 分。 这一结果表明，基于日志场景的基准排行榜在一定程度上衡量的是模型对测试地点的记忆能力，而非泛化能力，这会影响所有比较端到端驾驶模型或设计基准的人。它也为自动驾驶评测中的数据泄漏与捷径学习提供了一个具体且可复用的案例。 性能差距恰好集中在原始划分中的训练行驶轨迹经过同一地点的位置，而在其他位置，用原始划分训练的模型并不优于用地理划分训练的模型；值得注意的是，模型能预测出任何摄像头都看不到的道路几何结构，而且即使移除辅助地图损失，差距依然存在，说明模型在没有显式监督的情况下也记住了地点。在 nuScenes 上，地理划分使 SparseDrive 的建图精度下降 59%，并同时损害其规划性能；作者已公开该划分以供进一步的泛化测试。

rss · arXiv cs.CV · 11月24日 05:00

**背景**: NAVSIM v1 是一个数据驱动的自动驾驶基准，定位介于开环回放与完整闭环仿真之间，在真实日志场景上运行非反应式仿真，并用 PDMS 这一综合安全性、进度与舒适性的复合指标来评测规划器。端到端驾驶模型直接以摄像头（及其他传感器）输入为输入，输出规划轨迹，通常在同一批城市和传感器日志中按场景级别划分训练集与测试集。由于这类数据集中连续的行驶记录会覆盖相同的道路，随机划分可能让测试场景距离训练场景仅几米，从而使模型利用视觉和地图上的熟悉度，而不是学习泛化到新地点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://kvynlim.github.io/industry-research/30-autonomy-stack/end-to-end-driving/evaluation-benchmarks-navsim-bench2drive">Evaluation Benchmarks for End-to-End Driving: NAVSIM ...</a></li>
<li><a href="https://www.emergentmind.com/topics/predictive-driver-model-score-pdms">Predictive Driver Model Score (PDMS) - emergentmind.com</a></li>
<li><a href="https://scholarcompass.net/en/tasks/autonomous-driving/benchmarks/navsim-v1">NAVSIM v1 Leaderboard — SOTA Autonomous Driving | Scholar Compass</a></li>

</ul>
</details>

**标签**: `#autonomous-driving`, `#benchmark-evaluation`, `#data-leakage`, `#end-to-end-learning`, `#research-methodology`

---

<a id="item-23"></a>
## [ScaleEvals：无重置自主玩耍实现可扩展通用机器人策略评估](https://arxiv.org/abs/2611.28411) ⭐️ 8.0/10

ScaleEvals 提出了一种无重置评估协议，让机器人集群持续进行物理环境中的自主玩耍，由 VLM AutoPrompter 生成带有难度估计和技能标签的场景化任务，并由 VLM AutoGrader 评估任务进展，与人工评分达到 90.7% 的一致率。在 DROID 和 YAM 上超过 3,000 次自主物理 rollout 中，它对五个最先进的通用策略进行了排名，同时将主动人工劳动减少 98%。 真实世界机器人评估一直受限于人工重置、人工评分以及诊断覆盖有限的小型固定任务集，因此该协议有望让策略比较成本更低、更持续。它对机器人基准测试和选择通用策略的团队都很重要，因为其排名与留出的人工排名高度相关，并且能够预测策略排序在哪些情况下发生反转。 该系统使用软胜 Bradley-Terry 模型聚合结果，并通过按标签分层的方差分析（ANOVA）提供可解释的能力诊断，在每个工作站实现每小时 23.0 次净 rollout，同时在 DROID 上报告 r=0.94（rho=0.90，p=0.018），在 YAM 上报告 r=0.839（rho=0.80）。它还展示了行为组合性，在 240 次前瞻性物理 rollout 中以 96% 的成对一致率恢复三策略排序，不过摘要对可复现性细节和失败模式的说明仍不充分。

rss · arXiv cs.RO · 11月24日 05:00

**背景**: 通用机器人策略是旨在执行多种任务并操作多样物体的学习型控制器，但在真实世界中评估它们通常需要人工重置场景、人工评分以及规模很小的固定任务集。无重置自主玩耍让机器人持续行动并自行生成练习，而视觉语言模型（VLM）可以根据图像提出任务并判断进展。Bradley-Terry 模型把成对比较转化为排名，DROID 和 YAM 则是用于真实机器人操作实验的平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bradley–Terry_model">Bradley–Terry model - Wikipedia</a></li>
<li><a href="https://i2rt.com/products/yam-6-dof-arm">YAM – I2RT Robotics</a></li>
<li><a href="https://proceedings.mlr.press/v229/sharma23b/sharma23b.pdf">Proceedings of the 7th Conference on Robot Learning (CoRL 2023)</a></li>

</ul>
</details>

**标签**: `#robotics`, `#benchmark-evaluation`, `#vision-language-models`, `#robot-policies`, `#autonomous-systems`

---

<a id="item-24"></a>
## [SANA-Robot：4.5B 混合记忆世界动作模型实现边缘端实时运行](https://arxiv.org/abs/2611.28943) ⭐️ 8.0/10

一篇新论文（arXiv:2611.28943）提出 SANA-Robot —— 一个 4.5B 参数的世界动作模型，其混合记忆设计将带有固定大小状态的线性注意力与滑动窗口 softmax 注意力相结合，从而以恒定成本实现分钟级的记忆回溯能力。该模型可在边缘设备上实时运行：在 RTX 5090 上使用 FP8 GEMM 时每个动作块耗时 135 ms，使用 NVFP4 GEMM 时为 115 ms，并能在边缘设备上以 30 Hz 实现闭环、实时的异步机器人控制。 世界动作模型此前一直受制于推理开销，难以在机器人上实时部署，而 SANA-Robot 的恒定成本记忆加上 30 Hz 边缘控制表明，这一路线有望从离线基准测试走向真实的具身部署。统一的策略/世界模拟器设计还意味着单个网络既能执行动作又能预测场景演化，这对具身智能中的规划与数据高效训练都很有价值。 该架构的恒定成本记忆正是其在不增加推理时延的前提下实现整段回合记忆的关键；SANA-Robot 在约 5B 规模的模型中于 RoboDojo 的记忆维度上取得最佳表现，并在 LIBERO-Plus、LIBERO-Pro 和 LIBERO-Max 上取得最高成功率。其全栈基础设施包括面向记忆训练的高效数据打包与混洗，以及基于记忆阶段的异步执行；需要注意的是摘要经过截断，除这些基准之外更完整的实验细节尚未公开。

rss · arXiv cs.RO · 11月24日 05:00

**背景**: 世界动作模型（WAM）借用视频生成模型所具备的视觉世界知识，训练策略同时预测未来画面与动作，相比纯粹的动作预测策略通常能带来更好的泛化能力。问题在于逐步预测视频代价高昂，而标准 Transformer 注意力的开销会随上下文长度增长，因此长时程记忆既慢又占内存。线性注意力用固定大小的循环状态替代不断增长的键值缓存，成本低但对精确回溯有损；滑动窗口 softmax 注意力则保留精确的局部细节，并通过网络层间传播信息。SANA-Robot 的混合层将两者结合，以恒定的推理成本获得全局的、分钟尺度的记忆。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/nicolascc1/Awesome-World-Action-Model">GitHub - nicolascc1/Awesome- World - Action - Model · GitHub</a></li>
<li><a href="https://lmversity.com/learn/llm-foundations/sparse-sliding-and-linear-attention">Sparse, Sliding - Window , and Linear Attention · LLM Foundations...</a></li>
<li><a href="https://www.danilchenko.dev/posts/nemotron-3-mamba/">Nemotron 3: How a Mamba- Transformer Hybrid ... | danilchenko.dev</a></li>

</ul>
</details>

**标签**: `#robotics`, `#world-models`, `#efficient-inference`, `#attention-mechanisms`, `#edge-ai`

---

<a id="item-25"></a>
## [Tacinf 发布开源全栈触觉基础设施，助力机器人灵巧操作](https://arxiv.org/abs/2611.29240) ⭐️ 8.0/10

一篇新的 arXiv 论文（2611.29240）提出了 Tacinf，这是一个低成本、模块化且完全开源的触觉基础设施，使机器人策略能够根据任务语言、视觉与触觉信息同时预测动作和指尖力，并可选择性地指定目标力大小。该栈包含四个组件：Tabero（仿真数据合成与触觉基准测试）、视觉-触觉-语言-动作（VTLA）策略学习、与部署用夹爪完全相同的 Tacumi 手持数据采集夹爪，以及任务对齐的仿真到现实评估协议 Taco。 力感知操作是具身智能领域的一大瓶颈，而 Tacinf 将数据采集、基础模型训练与硬件部署打包为一条可复现的工作流并开源，降低了无力承担定制触觉硬件的实验室的准入门槛。其仿真与真实之间的强相关性表明，研究者可以主要在仿真中迭代并仍能预测真机表现，这有望加速整个机器人社区的触觉策略研究。 仅使用触觉仿真数据微调的基础模型可零样本迁移到不同的真机任务；在八种策略变体上，仿真与真机的平均任务成功率高度相关（Pearson r=0.998，平均最大排名违例 MMRV=0.010）。在四个报告力测量的策略中，两个域内的全部三个任务上都表现为“用力”指令下的平均抓握力高于“轻柔”指令；在物体位置与实例均随机化时，混合遥操作、仿真与 Tacumi 数据可将真机平均任务成功率从仅用遥操作的 20% 提升到 60%。

rss · arXiv cs.RO · 11月24日 05:00

**背景**: 触觉感知让机器人能直接获得接触力反馈，这对于抓取易碎物体或插装零件等任务至关重要，但触觉硬件历来昂贵，且软件栈彼此割裂。视觉-语言-动作（VLA）模型将相机图像与自然语言指令映射为机器人动作，加入触觉后便形成视觉-触觉-语言-动作（VTLA）策略，可对接触过程进行推理。UMI 系列等手持数据采集夹爪让人类无需机器人即可快速演示操作技能；而仿真到现实的差距（仿真动力学与真实物理之间的不匹配）仍是信任仿真训练策略的主要障碍。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.27886">Tabero : Learning Gentle Manipulation with Closed-Loop Force...</a></li>
<li><a href="https://github.com/NathanWu7/Tabero">GitHub - NathanWu7/ Tabero : Code base for ICML paper " Tabero "</a></li>
<li><a href="https://arxiv.org/html/2601.14550">TacUMI: A Multi-Modal Universal Manipulation Interface for...</a></li>

</ul>
</details>

**标签**: `#robotics`, `#tactile sensing`, `#robot manipulation`, `#vision-language-action`, `#sim-to-real`, `#open-source`

---