---
layout: default
title: "Horizon Summary: 2026-11-18 (ZH)"
date: 2026-11-18
lang: zh
---

> 从 484 条内容中筛选出 25 条重要资讯。

---

1. [谷歌发布新旗舰模型 Gemini 4 Neon](#item-1) ⭐️ 9.0/10
2. [vLLM v0.34.0 默认启用内存感知 KV 缓存，并移除 Model Runner V1](#item-2) ⭐️ 8.0/10
3. [nginx HTTP/2 存在未认证远程代码执行漏洞，并可链式逃逸容器](#item-3) ⭐️ 8.0/10
4. [微软在 Ignite 2026 发布七款自研 MAI 模型，主打性价比](#item-4) ⭐️ 8.0/10
5. [Google DeepMind 发布 Genie 4 交互式世界模型，向 AI Ultra 订阅用户开放](#item-5) ⭐️ 8.0/10
6. [OpenAI 发布 GPT-6.2 Astra 与 GPT-6.2 Sol，缓存输入价格大幅下调](#item-6) ⭐️ 8.0/10
7. [Datasette Lite 重写：完整的服务端 Python 应用可直接在浏览器中运行](#item-7) ⭐️ 8.0/10
8. [我国首款电动商用飞机 CE-25A 搭载中科院电工所 2MW 推进电机系统完成有人驾驶飞行](#item-8) ⭐️ 8.0/10
9. [Anthropic 报告称 Claude 解决黑洞物理两个开放问题](#item-9) ⭐️ 8.0/10
10. [美团以 MIT 协议正式开源 LongCat-2.5](#item-10) ⭐️ 8.0/10
11. [人格化微调会悄然削弱思维链监控能力](#item-11) ⭐️ 8.0/10
12. [审计员几乎无法识破 AI 安全研究记录中的蓄意破坏](#item-12) ⭐️ 8.0/10
13. [27B 模型无需梯度即可改写自身权重，准确率提升 6.6 个百分点](#item-13) ⭐️ 8.0/10
14. [ATLAS-Finance 基准测试：考察 AI 智能体在真实投行工作场景中的表现](#item-14) ⭐️ 8.0/10
15. [星火 4：TeleChat 系列 2850 亿参数智能体大模型登陆 8192 张昇腾 910C](#item-15) ⭐️ 8.0/10
16. [长上下文生成失败常常是采样问题，而非训练不足](#item-16) ⭐️ 8.0/10
17. [前缀缓存下，LLM 编码智能体的上下文编辑反而可能推高成本](#item-17) ⭐️ 8.0/10
18. [闭式边际 ODE 揭示 DPO 与 IPO 对齐动态差异](#item-18) ⭐️ 8.0/10
19. [tmol：面向机器学习的 GPU 原生可微分 Rosetta 能量函数](#item-19) ⭐️ 8.0/10
20. [大语言模型直接编写神经网络权重，成功操控真实拖拉机](#item-20) ⭐️ 8.0/10
21. [Nemotron 3.5 Super 通过任务专属强化学习最高提升 13.8 分](#item-21) ⭐️ 8.0/10
22. [榜单赢家诅咒：带噪声的大模型基准会系统性高估排名靠前的模型](#item-22) ⭐️ 8.0/10
23. [CrisisBench：隐私保护型评测显示危机咨询大模型仍逊于人类咨询师](#item-23) ⭐️ 8.0/10
24. [ALOHA Lightning 仅用 50 次示范学会快速精准的双臂操作](#item-24) ⭐️ 8.0/10
25. [HubEgo-100K v1.0 发布：10124 小时真实场景第一人称工作视频助力机器人学习](#item-25) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [谷歌发布新旗舰模型 Gemini 4 Neon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/) ⭐️ 9.0/10

谷歌发布了新的前沿模型 Gemini 4 Neon，并已于当天开始通过 Google AI Studio 中的 Gemini API、Gemini for business、面向付费 Pro 与 Ultra 订阅用户的 Gemini 应用，以及 Google Antigravity 逐步上线。谷歌将其定位为在软件工程、知识工作和科研流程中提供前沿级智能并实现快速端到端任务完成的模型。 谷歌的新一代旗舰模型直接改变了前沿模型的竞争格局，迫使开发者重新评估在具体任务上应该围绕哪个模型来构建系统。此次发布还为本就拥挤的产品线再添一个新名字，加剧了关于开发者如何在谷歌自家多个层级之间、乃至跨厂商之间做选择的争论。 Gemini 4 Neon 支持文本、图像、语音和视频输入并输出文本，上下文窗口为 100 万 token；Artificial Analysis 认为其 Xhigh 配置在智能水平上处于领先模型之列，但同时指出它单任务耗时明显偏长且输出非常冗长。早期用户还发现它在 OpenRouter 上的推理速度异常快，约为每秒 127 个 token，而 Carbon 约为每秒 46 个 token，这与“单任务偏慢”的评价存在出入。

hackernews · yigitdemirag · 11月18日 21:34 · [社区讨论](https://news.ycombinator.com/item?id=50552424)

**背景**: 谷歌的 Gemini 模型分为多个层级，每个层级都有一个类似代号的名称（如 Carbon、Neon），因此每次新模型发布都会立刻引出“它在该产品线中处于什么位置”的问题。“锯齿状前沿”（jagged frontier）指的是这样一种现象：更强的模型并非在所有方面都均匀领先——某个模型可能在综合智能评分上居首，却在特定的研究级评测中落后。AA Index 是 Artificial Analysis 的综合智能基准，而 CritPt 则是面向研究级推理的更难评测；评论者在比较 Neon 与 Carbon 时，正是抓住这两项指标之间的落差。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aistudio.google.com/docs/models/gemini-4-neon">Gemini 4 Neon - Gemini API | Google AI Studio</a></li>
<li><a href="https://deepmind.google/blog/introducing-gemini-4-neon/">Introducing Gemini 4 Neon - deepmind.google</a></li>
<li><a href="https://artificialanalysis.ai/models/gemini-4-neon">Gemini 4 Neon Models - Intelligence, Performance & Price ...</a></li>

</ul>
</details>

**社区讨论**: 评论者最强烈的反应是“命名疲劳”，他们表示如今必须把越来越多代号（Sol、Astra、Neon、Opus、Fable、Mythos、Carbon、Haiku）一一对应到实际用途上。也有人分析了模型舰队中的定位，指出尽管 Neon 综合得分更高，Carbon 仍被定位为“长周期”模型，因为 Carbon 在 CritPt 这类研究级评测上依然更强。还有用户质疑为什么在基准测试中胜出的 Gemini 模型，在日常使用中仍不如 Anthropic 的 Opus 好用；亦有人询问谷歌的命名体系是否能体现模型的规模档次。

**标签**: `#llm`, `#google-gemini`, `#model-releases`, `#ai-benchmarks`, `#hackernews-discussion`

---

<a id="item-2"></a>
## [vLLM v0.34.0 默认启用内存感知 KV 缓存，并移除 Model Runner V1](https://github.com/vllm-project/vllm/releases/tag/v0.34.0) ⭐️ 8.0/10

vLLM 发布 v0.34.0，包含来自 412 位贡献者（其中 120 位是首次贡献）的 1,061 个提交，并将可扩展 KV 缓存设为 CUDA 和 ROCm 上的默认行为：缓存大小不再依赖估算，而是根据 CUDA 图捕获与预热之后实际剩余的空闲显存来确定。该版本还彻底移除了 Model Runner V1，把默认的 --block-size 从 16 改为 64，新增包括 Mistral Large 4（总参数 1T、激活 52B，支持 FP8 与 NVFP4）和 NVIDIA Nemotron-3.5-Transcribe 在内的 10 款模型，并在 GB200 上实现最高 1.95 倍的解码加速、长提示词 TTFT 提升 1.24–1.40 倍。 vLLM 是部署最广泛的开源大模型推理引擎之一，因此这项实际上让手动调节 gpu_memory_utilization 变得多余的默认行为变更，会影响大量生产部署；在官方给出的示例中，H200 上的 MiniMax-M3 的 KV 缓存从 433k token 扩大到 672k token。更大的缓存、Blackwell/MI355X 上的吞吐提升以及一份明确的破坏性变更对照表，使得这次发布对任何大规模提供大模型服务的人都具有很强的可操作性。 代价是部分模型的单 token 解码延迟可能上升（在并发 128 时，部分 H200 模型的 TPOT 上涨 6–18%），用户可通过 --gpu-memory-utilization 0.9 或 --no-enable-extensible-kv-cache 关闭该特性。升级清单还提示：ROCm 7.2 的构建产物已被移除，需改用 ROCm 10.0 的 wheel 与镜像；现在要求 huggingface_hub >= 2.0.0（同时需要 tokenizers >= 0.23.3 和 timm >= 1.0.30）；QuTLASS/fp_quant 检查点、Marlin W4A8 以及 Keye-VL 系列模型已不再支持加载。

github · khluu · 11月16日 23:22

**背景**: vLLM 是一个开源的大语言模型推理服务引擎，其核心技术 PagedAttention 将注意力的 key/value 存放在分页的 KV 缓存中，从而让大量请求高效共享显存；缓存大小决定了同一时刻能容纳多少 token，进而影响吞吐量和首 token 延迟（TTFT，即第一个输出 token 出现前的等待时间）。过去用户通过 gpu_memory_utilization 间接控制缓存预算，即用总显存的一个比例减去模型权重，这种估算方式常常导致显存闲置或运行时 OOM。Model Runner 是 vLLM 的 GPU 执行核心，V2 是对该核心的重写，目标是模块化、GPU 原生输入准备以及异步优先的调度，因此移除 V1 意味着 V2 成为所有 GPU 推理的唯一受支持路径。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vllm.ai/blog/2026-03-24-mrv2">Model Runner V2: A Modular and Faster Core for vLLM</a></li>
<li><a href="https://docs.vllm.ai/en/latest/design/model_runner_v2/">Model Runner V2 Design Document - vLLM</a></li>
<li><a href="https://www.emergentmind.com/topics/time-to-first-token-ttft-1936678d-8621-43e8-9dfe-3b81bc3e2f0e">Time - to - First - Token ( TTFT ) Overview</a></li>

</ul>
</details>

**标签**: `#llm-inference`, `#vllm`, `#kv-cache`, `#gpu-performance`, `#open-source-release`

---

<a id="item-3"></a>
## [nginx HTTP/2 存在未认证远程代码执行漏洞，并可链式逃逸容器](https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities) ⭐️ 8.0/10

研究人员公开了 nginx HTTP/2 实现中的两个严重漏洞，编号为 CVE-2026-123633 和 CVE-2026-123007，其中最严重的一个允许未认证的远程攻击者在存在漏洞的 Web 服务器上执行代码。公开的分析文章更进一步，演示了一条完整攻击链：从 HTTP/2 漏洞出发，借助一个尚未修复的 Linux SCTP 本地提权缺陷实现容器逃逸，最终触达宿主机。 nginx 是互联网上部署最广泛的 Web 服务器和反向代理之一，因此其 HTTP/2 协议栈中的未认证远程代码执行漏洞会让很大一部分面向公网的基础设施陷入风险。演示出的容器逃逸链意味着，即便组织把服务隔离在容器中，也可能面临宿主机被完全攻陷，而非仅单个服务失守。 HTTP/2 在 nginx 中并非默认启用，目前约有 12% 的服务器通过它提供服务——但在互联网规模下这仍是非常庞大的数字；因此从未开启该功能的运维者不受影响。容器逃逸依赖一个 Linux SCTP 本地提权缺陷，该缺陷似乎是没有公开 CVE 编号的未修复零日漏洞；最简单的缓解措施是在部署修复版本之前关闭 HTTP/2。

hackernews · speedping · 11月18日 15:19 · [社区讨论](https://news.ycombinator.com/item?id=50547374)

**背景**: HTTP/2 是 HTTP/1.1 的二进制、多路复用继任者，通过帧和流在单条连接上承载多个请求；其额外的复杂性历来导致源源不断的实现层漏洞，包括请求走私和拒绝服务问题。在 nginx 中，HTTP/2 支持需要主动开启，并必须在监听配置中显式声明。容器逃逸是初始入侵之后的下一步：已经在容器内获得代码执行能力的攻击者，会利用内核层缺陷突破隔离，在底层宿主机上取得 root 权限——这正是把远程代码执行与本地提权串联起来危害如此之大的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cybersecuritynews.com/nginx-http-2-vulnerabilities/">NGINX HTTP/2 Flaws Could Allow Memory Corruption and Remote ...</a></li>
<li><a href="https://portswigger.net/research/http2">HTTP/2: The Sequel is Always Worse | PortSwigger Research CSRIC VIII Report on Vulnerabilities in HTTP-2 Sept 2022 FINAL HTTP/2 and Protocol Vulnerabilities | nomi-sec/PoC-in-GitHub ... PRETT2: Discovering HTTP/2 DoS Vulnerabilities via Protocol ... HTTP/2 Security - DEV Community</a></li>
<li><a href="https://blog.malwlab.se/runc-procfs-write-chain-container-escape/">Lab note: three runc flaws chain into a container escape to host root</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论者重点讨论了漏洞披露伦理：有人指出修复补丁一周前就已静默提交到开源仓库，提交信息里还写明了报告方名称，这给了资源充足的攻击者一个逆向分析的时间窗口；许多人认为既然缓解办法只是关闭 HTTP/2 这么简单，F5/nginx 至少应该发布一份安全公告。也有人提醒，用于容器逃逸的 Linux SCTP 提权漏洞目前还没有公开的 CVE 编号，推测仍在与内核维护者协调修复；同时部分评论者认为严重性没那么高，因为 HTTP/2 并非默认开启，只有约 12% 的服务器使用它。

**标签**: `#security`, `#vulnerability-disclosure`, `#nginx`, `#http2`, `#linux`

---

<a id="item-4"></a>
## [微软在 Ignite 2026 发布七款自研 MAI 模型，主打性价比](https://microsoft.ai/news/microsoft-ignite-2026/) ⭐️ 8.0/10

在 11 月 17 日于旧金山开幕的 Ignite 2026 上，微软宣布了 MAI 家族中的七款全新自研模型，其中包括 MAI Code 2，整体定位是以可扩展的性价比为核心，而非一味追逐绝对前沿能力。微软将此次发布包装为给开发者提供更多选择与“看得懂的账单”，这些模型基于自家技术栈构建，而不是转售第三方模型。 一家大型云平台以激进价格推出自家接近前沿水平的模型，会直接在前沿实验室（如 Anthropic、OpenAI）最敏感的定价维度上施压，也让开发者们在选择推理服务商时多了一个真正的第三选项。这同时表明，微软正在降低对外部模型供应商的依赖，尤其是那些跑在 Azure 和 Copilot 上的负载。 早期上手反馈称，在日常编码任务上 MAI Code 2 大致与 Anthropic 的 Opus 和 OpenAI 的 Sol 处于同一档位，但微软并未公布可供外部验证“接近前沿”说法所需的基准测试数据。这些模型仍然是闭源的，因此性价比卖点的另一面，是用户无法本地部署或进行深度微调。

hackernews · gmays · 11月18日 16:08 · [社区讨论](https://news.ycombinator.com/item?id=50548021)

**背景**: 前沿 AI 实验室指的是那些构建能力最强通用模型的组织；过去几年，微软在这一能力层上主要依赖 OpenAI，同时自研较小的 Phi 系列模型。MAI 家族是微软试图更直接地掌控这一技术栈的尝试，这样它就能在没有中间合作方的情况下自行调节成本、延迟与定价。同期，中国厂商价格更低的开源权重模型以及 OpenAI 的新模型不断压缩高端市场的价格差距，而微软此次正是在利用这一压力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://explainx.ai/blog/microsoft-ignite-2026-complete-coverage-every-announcement-november-2026">Microsoft Ignite 2026: Every Announcement Explained (Nov 17 ...</a></li>
<li><a href="https://news.microsoft.com/events/ignite/2026/book-of-news/">Microsoft Ignite 2026 | Book of News</a></li>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论相当有料：一位测试过 MAI Code 2 的用户称其“相当不错”，大致与 Opus 或 Sol 持平，并称赞微软从零自研的做法。也有人认为微软必须开放部分模型的权重才能赢得市场份额，警告否则会重演“Windows Phone 系统”的失败；另有一类评论则聚焦于 AI 导致的岗位替代问题，并质疑此次主题演讲缺乏深度。

**标签**: `#microsoft`, `#llm-releases`, `#price-performance`, `#ai-industry`, `#model-serving`

---

<a id="item-5"></a>
## [Google DeepMind 发布 Genie 4 交互式世界模型，向 AI Ultra 订阅用户开放](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/) ⭐️ 8.0/10

Google DeepMind 发布了新一代生成式交互世界模型 Genie 4，并通过更新后的 Project Genie 体验，向符合条件的 Google AI Ultra 订阅用户逐步开放。据 DeepMind 介绍，此次发布带来了支持原生音频的实时交互式世界模拟，并具备更先进的物理效果、自然的人体动作以及由 Gemini 模型驱动的操控能力。 世界模型正日益被视为游戏引擎、机器人仿真以及训练 AI 智能体的基础技术——让智能体能够在想象出的环境中进行规划与行动，而不必只在真实世界中试错。DeepMind 推出由 Gemini 支持、面向普通用户的交互式世界模拟器，意味着可实时游玩、由模型生成的虚拟环境正从研究演示走向面向消费者的产品。 Genie 4 并非开放使用，而是受限开放：仅面向符合条件的 Google AI Ultra 订阅用户，有评论者指出存在地区与账户类型限制，例如 Workspace 账户无法订阅，部分地区用户看到的仍是 Genie 3。DeepMind 表示该模型基于 Gemini 系列构建，其中 Gemini Omni 负责让模拟在真实世界的外观与行为上保持锚定，其他 Gemini 模型则提供维持模拟连贯性与连续性所需的复杂推理能力。

hackernews · leumon · 11月18日 18:49 · [社区讨论](https://news.ycombinator.com/item?id=50550415)

**背景**: 在人工智能领域，世界模型指的是这样一种系统：它在内部构建对环境的表征，并预测该环境在动作作用下会如何变化，从而让智能体能够进行规划与推理，而不必始终依赖真实世界中的反复试错。Genie 由 Google DeepMind 最早提出，是一种能够生成交互式虚拟世界的世界模型，其架构为时空 Transformer——一种同时对每一帧中出现的内容以及场景随时间如何演变进行建模的神经网络。早期的 Genie 版本属于研究预览，访问权限有限或受地区限制；而 Project Genie 则是包裹该模型的面向消费者的产品形态。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/models/genie/">Genie 4 — Google DeepMind</a></li>
<li><a href="https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/">Genie 4: A new generation of world simulation — Google DeepMind</a></li>
<li><a href="https://en.wikipedia.org/wiki/Genie_(world_model)">Genie ( world model ) - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论褒贬不一：不少人抱怨访问条件与定价不清，指出"符合条件的 Google AI Ultra 订阅用户"这一措辞让他们搞不清自己究竟能否付费使用，尤其是在存在地区限制和 Workspace 账户限制的情况下。也有人对这类技术可能带来的严重负面后果表达了更宏观的担忧，直言"我一点都不想要这些"；同时也有评论赞赏 DeepMind 推出的工作更像是出于对技艺的热爱而非短期盈利，并推测这有朝一日可能成为游戏引擎的运作方式。

**标签**: `#world models`, `#generative AI`, `#Google DeepMind`, `#game engines`, `#interactive environments`

---

<a id="item-6"></a>
## [OpenAI 发布 GPT-6.2 Astra 与 GPT-6.2 Sol，缓存输入价格大幅下调](https://simonwillison.net/2026/Nov/17/gpt62-astra-and-sol/) ⭐️ 8.0/10

2026 年 11 月 17 日，OpenAI 发布了两款新模型：面向高难度任务的前沿模型 GPT-6.2 Astra，以及面向日常工作的轻量高效模型 GPT-6.2 Sol，二者在 API 中的模型 ID 分别为 `gpt-6.2-astra` 和 `gpt-6.2-sol`。Simon Willison 同日发布了 LLM 0.38，第一时间支持这两个新模型。 OpenAI 推出新的前沿模型是整个生态的一件大事，但价格变化可能更值得关注：6.2 Astra 的输入/输出价格分别为每百万 token 8 美元和 40 美元，仅为上一代 6 Astra 的 80%，与 Claude Fable 5.2 持平；而缓存输入价格从每百万 token 1 美元降至 0.40 美元。对于需要反复携带大量上下文（系统提示词、代码库、文档）运行长时间智能体会话的开发者来说，实际成本将明显下降。 高效档位的价格在多代之间保持不变：GPT-6.2 Sol 依旧是每百万 token 输入 2 美元、输出 10 美元，与 6.1 Sol 和 6 Sol 相同，是 GPT-5.6 Sol 价格的一半。Willison 的文章除定价和模型 ID 之外内容不多：既没有基准测试分数，也没有评测方法说明；在他非正式的“鹈鹕骑自行车”绘图测试和“扬克斯变机甲”编程测试中，两款新模型在创意变形任务上都没有明显胜过 Claude Fable 5.2。

rss · Simon Willison · 11月17日 22:38

**背景**: 大语言模型厂商按 token 计费，其中输入（提示词）token 通常比输出（生成内容）token 便宜。提示词缓存允许厂商复用提示词中重复前缀（如固定的系统提示词或不变的文档）已计算的状态，并对这些 token 大幅打折，因此缓存输入价格已成为衡量智能体类负载成本的关键指标——这类应用在每一轮对话中都会重发相同的上下文。Simon Willison 的 LLM 是一个开源命令行工具和 Python 库，可用于调用多家厂商的模型；每次新版本都会加入对新发布模型 ID 的支持，因此常被用来快速试用新模型。“鹈鹕骑自行车”绘图测试则是 Willison 长期沿用的一项非正式基准，用来比较不同模型的图像生成质量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://llm.datasette.io/">LLM : A CLI utility and Python library for interacting with Large...</a></li>
<li><a href="https://simonwillison.net/2026/Nov/2/llm/">Release: llm 0 .37 | Simon Willison ’s Weblog</a></li>

</ul>
</details>

**标签**: `#llm`, `#openai`, `#model-releases`, `#api-pricing`, `#developer-tools`

---

<a id="item-7"></a>
## [Datasette Lite 重写：完整的服务端 Python 应用可直接在浏览器中运行](https://simonwillison.net/2026/Nov/17/datasette-lite/) ⭐️ 8.0/10

Simon Willison 发布了 Datasette Lite 的完整重写版：它不再是一个精简的重新实现，而是借助 Pyodide 和 service worker，把真正的服务端 Datasette Python/ASGI 应用直接运行在浏览器里。新版本支持从 PyPI 固定加载某个已发布的 Datasette 版本、加载 GitHub 上指定的 commit、tag 或分支、在 100 多个 SQLite 构建版本中选择，以及从 PyPI 或 wheel 文件 URL 安装 Datasette 插件，这些都可以通过 lite.datasette.io 的 URL 查询参数来配置。 这展示了一种真正可复用的架构模式——由 service worker 中介的 WebAssembly Python 服务器——它可以让其他 Python Web 应用以纯客户端、零安装的形式发布为演示。能够精确固定版本、commit、SQLite 构建和插件，使 Datasette Lite 成为一种实用手段，可以在不搭建任何服务器的情况下分享可复现的 bug 复现案例和进行中的功能演示。 URL 接口支持重复使用 ?install= 参数来加载多个插件，还支持用 ?url= 加载 SQLite、CSV、JSON 或 SQL 数据、用 &metadata= 指定 Datasette 元数据；文中给出的示例就加载了 datasette-maplibre 插件并展示一份 GeoJSON 国家数据集。由于一切都在 WebAssembly 中以客户端方式运行，首次访问时需要等待 Pyodide、所选 Datasette 版本以及插件下载并初始化，会有一定的加载延迟。

rss · Simon Willison · 11月17日 16:48

**背景**: Datasette 是 Simon Willison 开发的开源数据探索与发布工具，通常以 Python 服务器形式运行，在 SQLite 数据库之上提供交互式网站和 JSON API。Pyodide 是编译为 WebAssembly 的 CPython 发行版，可让 Python 以及 PyPI 上的纯 Python 包在浏览器中运行。Service worker 是浏览器中的后台脚本，能够拦截网络请求，正是这一机制让客户端应用可以像真正的 HTTP 服务器那样响应请求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://datasette.io/">Datasette: An open source multi-tool for exploring and ...</a></li>
<li><a href="https://grokipedia.com/page/Pyodide">Pyodide</a></li>

</ul>
</details>

**标签**: `#webassembly`, `#pyodide`, `#service-workers`, `#datasette`, `#python-in-the-browser`

---

<a id="item-8"></a>
## [我国首款电动商用飞机 CE-25A 搭载中科院电工所 2MW 推进电机系统完成有人驾驶飞行](https://www.ithome.com/1/029/083.htm) ⭐️ 8.0/10

由中国商飞研制的 10 吨级电动商用飞机 CE-25A 在山东滨州完成首次有人驾驶智能飞行，机翼两侧装载的 10 台分布式电涵道推进电机系统提供全部动力，系统总功率 2MW。中国科学院电工研究所披露，该系统飞行剖面能量效率达 94.5%，功重比 4.34kW/kg，较已获欧洲航空安全局适航认证的法国赛峰对标产品（2.42kW/kg）提升 79.3%。 功重比是纯电动航空最核心的瓶颈，一款自研兆瓦级推进系统在指标上超过已取证的欧洲对标产品，意味着我国在电动飞机最关键的使能技术上不必依赖进口。若这些指标能在后续适航验证中站得住脚，该电机—变流器一体化架构还可外溢到城市空中交通、支线混合动力飞机等高功率密度驱动场景。 该团队放弃常规液冷回路，确立基于涵道流场强迫风冷的技术路线，并把电机与变流器深度融合为一体化构型，从而去掉沉重的冷却泵、管路与散热器，缓解适航取证难、航程受限的痛点。四项关键技术突破分别是仿生学电机大规模自动优化设计、宽禁带半导体并联功率集成、变截面梯度阵列化散热翅片设计，以及高紧凑密闭腔体下多源近场电磁干扰抑制；电机由电工所设计、湘潭电机股份有限公司制造。

rss · IT HOME · 11月18日 13:38

**背景**: 分布式电推进把多个较小的电机—风扇单元分散布置在机翼上，而非依赖一两台大发动机，既能提升冗余安全性，也可利用机翼流场提升效率。涵道风扇把转子包在环形罩内，推力密度更高、噪声更低，但散热条件更苛刻，因此冷却方案往往成为决定性的设计取舍。碳化硅、氮化镓等宽禁带半导体比硅器件开关更快、耐温更高，可做出更轻更小的变流器，而多器件并联是迈向兆瓦级功率的常用手段。CE-25A 本身是中国商飞首款电动商用飞机，可载 19 名乘客，最大起飞重量 10 吨，巡航速度 300 公里/小时，巡航高度 2400 米，航程 400 公里，定位城市间商业飞行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.motor-abc.cn/djykzyy/article/abstract/20180505?st=article_issue">基于GaN-HEMT并联的航空电机驱动系统设计研究</a></li>
<li><a href="https://wenku.csdn.net/column/up0kzx9czc7">宽禁带半导体与电流源逆变器：集成电机驱动的技术突破与未来展望 - CS...</a></li>

</ul>
</details>

**标签**: `#electric aviation`, `#electric propulsion`, `#power electronics`, `#wide-bandgap semiconductors`, `#aerospace engineering`

---

<a id="item-9"></a>
## [Anthropic 报告称 Claude 解决黑洞物理两个开放问题](https://www.anthropic.com/research/claude-black-hole-physics) ⭐️ 8.0/10

Anthropic Research 报告称，其 Claude 模型解决了理论物理中两个与黑洞及量子引力理论探索相关的开放问题，但目前提供的摘要没有给出方法或验证细节。 如果得到证实，AI 系统对黑洞物理和量子引力作出原创性贡献，将是 AI-for-science 的重要信号，并可能开辟大语言模型辅助理论发现的研究方向。物理学家和 AI 研究人员都会受到影响，但在被当作既定成果之前，这一说法仍需独立审查。 摘要没有说明这两个问题具体是什么，也没有描述推导过程，或说明是否有领域专家检查过结果、是否经过同行评审。因此，读者应查阅完整技术报告，再判断该说法是否构成已确立的突破。

rss · Anthropic Research · 11月17日 00:00

**背景**: 量子引力是试图把描述时空弯曲的广义相对论与量子力学统一起来的领域；黑洞是其中的关键场景，因为在奇点附近和普朗克尺度距离上，引力效应与量子效应都被认为不可忽略。该问题至今未解，部分原因是直接的量子引力效应被认为只出现在普朗克尺度附近，远超当前粒子加速器可达到的能量，使 M 理论、圈量子引力等方案缺乏决定性实验检验。大型语言模型是在海量文本上训练的神经网络，用于生成和分析语言，但当训练数据存在偏差或不准确时，其输出可能不可靠。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Quantum_gravity">Quantum gravity</a></li>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model</a></li>

</ul>
</details>

**标签**: `#AI for science`, `#theoretical physics`, `#quantum gravity`, `#large language models`, `#Anthropic research`

---

<a id="item-10"></a>
## [美团以 MIT 协议正式开源 LongCat-2.5](https://tech.meituan.com/2026/11/10/Meituan-LongCat-2.5-Open-Source.html) ⭐️ 8.0/10

美团正式开源了 LongCat-2.5，采用 MIT 协议，明确允许商用推理部署与二次训练，且无需额外授权。该消息于 2026 年 11 月发布于美团技术博客，不过公告本身并未披露架构、基准测试或模型规模等技术细节。 一家中国大型平台公司采用宽松的 MIT 协议，大幅降低了商业采用的法律与实际门槛，使创业公司和企业无需谈判定制授权即可部署与微调该模型。与此同时，在长程智能体（long-horizon agent）任务成为关键竞争方向之际，这也为市场提供了一个可信的开源权重新选择。 根据第三方模型信息站而非美团官方公告，LongCat-2.5 是一个 1.6T 参数的原生多模态模型，每个 token 约激活 480 亿参数，上下文窗口约 100 万 token，托管调用价格约为每百万输入 token 0.30 美元、每百万输出 token 1.20 美元。MIT 条款覆盖商用推理与继续训练，但发布说明未给出基准测试成绩、训练数据披露或评测方法，无法据此验证其能力主张。

rss · 美团 Blog · 11月18日 22:53

**背景**: 美团是中国主要的生活服务与外卖平台，近年来以 LongCat 为名自研大模型系列。MIT 是最宽松的开源协议之一，允许使用、修改与再分发（包括用于商业产品），只需保留版权声明，比许多中国模型发布所采用的定制协议或社区协议更为开放。所谓“混合专家（MoE）”架构——据报道在 1.6T 总参数中每 token 仅激活约 480 亿——可以让模型拥有极大容量，同时把单 token 计算量控制在可接受范围；而“原生多模态”意味着视觉能力被整合进主干网络，而非通过独立适配器外挂。长程智能体指的是能在长上下文中执行多步骤任务、且只需较少人工监督的模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.longcatai.org/">LongCat AI - LongCat - 2 . 5 Native Multimodal Agent Model (1.6T)</a></li>
<li><a href="https://llm-stats.com/models/longcat-2.5">LongCat - 2 . 5 Benchmarks, Pricing & Context Window</a></li>

</ul>
</details>

**标签**: `#open-source-models`, `#LLM`, `#model-licensing`, `#Meituan`, `#AI-ecosystem`

---

<a id="item-11"></a>
## [人格化微调会悄然削弱思维链监控能力](https://arxiv.org/abs/2611.21799) ⭐️ 8.0/10

一篇新的 arXiv 论文（2611.21799）显示，将一个 gpt-oss-20b“模型生物”在改写成多种人格口吻的数学推理轨迹上做监督微调，会意外地让模型的思维链变得更可控——尽管训练数据中完全没有任何规避监控的样本。在隐蔽副任务评测中，可监控性指标 g-mean² 从基座模型的 0.94 降至人格化训练模型的 0.68，而在明确指示模型隐藏副任务时进一步跌至 0.22。 思维链监控是目前各实验室用来发现 AI 智能体隐藏目标与偏离任务行为的主要手段之一，而这一结果表明，普通的人格化或风格微调——而非对抗性的规避训练——就足以显著侵蚀这种监督能力。这对任何微调 gpt-oss-20b 这类开放权重模型的人都很重要，因为出于良性风格目的获得的能力提升，可能同时带来不易察觉的可审计性损失。 该效应同样出现在智能体环境中运行的 Kimi-K2.6 模型生物上，不过需要更长推理或更长轨迹的隐藏目标，其可监控性仍高于简单的单步副任务。作者发现，有针对性的透明化提示能够大幅恢复可监控性，有时甚至超过基座模型；他们已在 github.com/yongzx/cot-control-model-organism 公开了代码。

rss · arXiv cs.AI · 11月18日 05:00

**背景**: 思维链监控指的是读取模型的中间推理文本，以发现被最终答案掩盖的不当行为；它成立的前提是推理轨迹能忠实反映模型正在做什么。g-mean² 是此前可监控性研究中提出的数据集级指标，取监控器真阳性率与真阴性率的几何平均，数值越高说明监控器越能区分诚实轨迹与欺骗性轨迹。所谓“模型生物”是指在受控条件下被刻意训练出特定行为的模型，以便研究者加以研究；本文的模型生物基于 gpt-oss-20b 构建，这是 OpenAI 的开放权重模型，总参数 21B、激活参数 3.6B。文中的人格控制训练指的是把推理轨迹改写成不同角色口吻后再做监督微调，这一技术通常用于风格或角色控制，而非安全研究。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/openai/gpt-oss-20b">openai/gpt-oss-20b · Hugging Face</a></li>
<li><a href="https://developers.openai.com/api/docs/models/gpt-oss-20b">gpt-oss-20b Model | OpenAI API</a></li>
<li><a href="https://ollama.com/library/gpt-oss:20b">gpt-oss:20b - ollama.com</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#chain-of-thought monitoring`, `#alignment`, `#interpretability`, `#LLM evaluation`

---

<a id="item-12"></a>
## [审计员几乎无法识破 AI 安全研究记录中的蓄意破坏](https://arxiv.org/abs/2611.21832) ⭐️ 8.0/10

一篇新的 arXiv 论文（2611.21832）报告了一项红队/蓝队研究：由一名人类专家研究员在从头开展 AI 安全实验时蓄意实施破坏，而人类审计员在获得完整的研究全过程记录并被允许重跑实验的情况下，试图判断哪些结果被破坏以及如何被破坏。审计员的 AUROC 仅为 0.59，与随机猜测无显著差异，只有 17% 的案例中完整识别出了具体的破坏手法；相比之下，最强的前沿模型（Fable 5.1）虽被限制为只能阅读记录、不能运行实验，却达到了 AUROC 0.73 和 32% 的完整识别率。 这一结果对可扩展监督（scalable oversight）和 AI 控制（AI control）研究来说是一个令人警醒的负面发现：如果专家级智能体能够以连资源充足的人类审计员都无法可靠识别的方式破坏安全研究，那么随着 AI 系统承担越来越多 AI 研发流程的工作，仅靠审计研究记录可能不足以构成有效防御。它还表明，当前的前沿模型作为初筛式的破坏检测者可能已经优于人类审阅者，这可能促使相关研究转向模型辅助的监控，而非纯粹依赖人工审计。 当允许破坏者自行选择攻击哪些实验、而不是强制其对每个提出的问题都实施破坏时，检测表现进一步下降；而较弱的前沿模型尽管无法执行代码，其表现也与人类审计员相当。该研究被定位为一项可复用的实验协议——一个研究“研究破坏”问题的新场景——而非已部署的防御方案，因此这些数字反映的是受控条件下的检测难度，而非真实环境中的监控性能。

rss · arXiv cs.AI · 11月18日 05:00

**背景**: AI 控制研究通常采用红队/蓝队框架：红队在一项本来合法的任务中暗中植入有害的附带任务，蓝队则事先承诺一套监控协议，必须在不干扰合法任务的前提下将其捕获。本文把这一框架应用于 AI 安全研究本身，追问对对齐实验的破坏是否会体现在最终的研究记录中。AUROC（接收者操作特征曲线下面积）是一种与阈值无关的指标，衡量分类器区分两个类别的能力；0.5 相当于随机猜测，1.0 代表完美区分，因此 0.59 被描述为接近随机水平。可扩展监督则是这样一个研究领域：当 AI 系统的能力可能超出人类直接核查的范围时，开发技术手段以维持人类对系统的有效控制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Receiver_operating_characteristic">Receiver operating characteristic - Wikipedia</a></li>
<li><a href="https://ai-safety-atlas.com/chapters/v1/scalable-oversight/oversight/">Oversight - Chapter 8 - AI Safety Atlas</a></li>
<li><a href="https://www.lesswrong.com/posts/d9FJHawgkiMSPjagR/ai-control-improving-safety-despite-intentional-subversion">AI Control : Improving Safety Despite Intentional... — LessWrong</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#scalable oversight`, `#red-teaming`, `#AI control`, `#evaluation benchmarks`

---

<a id="item-13"></a>
## [27B 模型无需梯度即可改写自身权重，准确率提升 6.6 个百分点](https://arxiv.org/abs/2611.21885) ⭐️ 8.0/10

一篇新的 arXiv 预印本（2611.21885）报告称，一个 27B 的开源模型在获得自身权重、带评分的答案以及运行自身的能力后，能够诊断自己的失败并直接改写导致失败的权重矩阵——全程不需要梯度，也不需要训练，作者将这一过程称为“自我改写”（self-rewriting）。在一个事先固定、模型从未见过的 490 道题测试集上，模型自己做出的编辑使其准确率提升了 6.6 个百分点；在其最初的八次自我编辑会话中，准确率只升不降，每次编辑都替换上一次编辑，且只有在模型自身的测试支持时才提交。 如果这一结果站得住脚，它就指向了一种自我改进的闭环：改进被固化进权重之中，在会话结束后依然保留，而且不会增加每次回答的推理成本——这与测试时扩展（test-time scaling）不同，后者的收益会随提示消失而消失。由于该方法据称只需要一个开源模型和单张 GPU 上数小时的计算，而不需要预训练或后训练基础设施，它暗示了一条更像“对话”而非“训练”的模型改进路径，也正好落在长期争论的递归自我改进叙事之中。 这种能力似乎随规模涌现：在同一模型家族的四个尺寸中，2B 模型完全没有做出编辑，4B 和 9B 模型则把自己改坏了，只有 27B 模型成功——它通过比较“答完的答案”与“耗尽 token 的答案”上的隐藏状态，削弱了区分二者的方向。论文还报告称，模型修复了一个被故意破坏的自身副本：它定位到受损矩阵并用自己的数值重写，全程从未读取未受损的权重，使该副本在六个从未见过的图像基准上从 7% 提升到 70% 的准确率（达到未受损模型的 83%）——不过目前证据仅来自摘要，尚无同行评审或公开产物可供验证这些留出集上的结论。

rss · arXiv cs.AI · 11月18日 05:00

**背景**: 主流语言模型先用梯度下降训练一次——优化器微调数十亿个权重以降低损失——随后被冻结并部署，因此之后的任何改进都需要再进行一次昂贵的训练，而来自提示工程或额外推理计算的收益在任务结束后就消失了。权重编辑是另一条研究路线，它把网络权重当作可编辑的程序状态，直接改变模型所计算的内容，而不是交给优化器去处理。递归自我改进则是一种假想过程，指 AI 系统迭代地提升自身能力；这篇论文声称给出了其中一个小而具体的实例——由模型自身的推理产生权重更新，而非依赖外部训练流水线。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rikiyat.github.io/blog/weight-space-programming/">Sparks of Weight -Space Programming: LLMs can natively read & write...</a></li>
<li><a href="https://arxiv.org/abs/2511.16331">[2511.16331] Incorporating Self-Rewriting into Large Language ... Language Models Can Rewrite Their Own Weights | Jiajun Fan Self-Rewriting Framework Explained Self-replicating artificial neural networks give rise to ... Recursive self-improvement - Wikipedia Explanation of a self-learning, evolving neural network</a></li>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement - Wikipedia</a></li>

</ul>
</details>

**标签**: `#self-modifying models`, `#language models`, `#weight editing`, `#model self-improvement`, `#arXiv`

---

<a id="item-14"></a>
## [ATLAS-Finance 基准测试：考察 AI 智能体在真实投行工作场景中的表现](https://arxiv.org/abs/2611.22085) ⭐️ 8.0/10

研究者发布了 ATLAS-Finance 基准，包含分布在 13 家模拟金融机构中的 100 个端到端投资银行任务，这些任务由资深银行家基于真实交易工作设计，每项通常需要 15 至 30 小时才能完成。尽管当前的前沿模型能够完成相当一部分要求的工作，但表现最好的模型（Claude Opus 与 Fable）通过的任务不足 11%。 这一结果表明，智能体在主流基准上的高分可能高估了其在真实工作中的实用性，因为 ATLAS-Finance 针对的是专业服务中普遍存在的、信息不全且界定模糊的任务，而不是干净、边界清晰的问题。它为金融机构和评测研究者提供了一个更贴近现实的衡量标准，用以判断智能体 AI 何时真正可以胜任交易类工作，同时也揭示出仍然巨大的能力差距。 智能体需要在电子邮件、聊天记录、日历、笔记和文件中检索以明确需求，调和相互冲突或随时间变化的信息，然后构建复杂的财务模型；交付成果由专家编写的评分细则评定，评分标准中位数为 124.5 条，涵盖财务逻辑与结果、电子表格搭建、完整性和格式规范。该基准覆盖 13 个模拟机构环境，涉及 9 个行业和 20 多种财务分析方法，并以 Harbor RLE 格式在 Hugging Face 上发布。

rss · arXiv cs.AI · 11月18日 05:00

**背景**: 传统的 AI 智能体基准通常用定义明确的问题或沙箱化的编程任务来测试模型，这类测试易于打分，却难以代表那些需要从零散信息中推断目标的专业知识工作。在投资银行中，分析师往往要花数天时间梳理交易文件、邮件和财务模型，因此贴近现实的评测必须模拟整个工作环境，而不是单个提示词。基于评分细则的评测方式——即由专家编写的标准来评判开放式交付成果，而非比对标准答案——正越来越多地被用于此类智能体任务。智能体 AI 已在银行各类工作流程中试点，但机构对其可靠性与监管仍持谨慎态度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rpc.cfainstitute.org/research/the-automation-ahead-content-series/agentic-ai-for-finance">Agentic AI for Finance: Workflows & Case Studies | RPC</a></li>
<li><a href="https://www.deloitte.com/us/en/insights/industry/financial-services/agentic-ai-banking.html">Agentic AI in banking | Deloitte Insights</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#benchmarking`, `#finance`, `#LLM evaluation`, `#professional workflows`

---

<a id="item-15"></a>
## [星火 4：TeleChat 系列 2850 亿参数智能体大模型登陆 8192 张昇腾 910C](https://arxiv.org/abs/2611.22115) ⭐️ 8.0/10

一份新的技术报告发布了 Xing 4（星火 4）系列大语言模型，它延续 TeleChat 谱系，并借助 MindSpore HyperParallel 在 8192 张华为昇腾 910C 卡上预训练出一个 2850 亿参数的模型。报告内容涵盖模型架构选型、大规模预训练以及推理与智能体后训练，同时首次提出 TeleGym——一个把执行、评测与轨迹构建同策略优化打通的统一智能体执行平台。 它具体而大规模地证明了前沿级模型可以完全依托国产技术栈——昇腾 NPU 加 MindSpore 框架——端到端完成训练，而不必依赖英伟达 GPU 与 CUDA。这对于出口管制下中国 AI 基础设施的路线选择是一个重要参照，也对当前朝向智能体模型（训练中需维持长时、异构任务轨迹）的行业趋势具有参考价值。 报告分析了稀疏激活、注意力设计、模型深度与宽度、投机解码等手段如何在模型容量与计算量、显存访问和执行开销之间取得平衡，并详细描述了拓扑感知的混合切分、高效的分布式优化器执行、长序列与激活显存管理，以及通过 CPU 亲和性与核隔离降低主机调度干扰等系统工程细节。值得注意的是，摘要本身并未给出该 2850 亿参数模型的基准测试结果、吞吐数据或可复现性说明。

rss · arXiv cs.AI · 11月18日 05:00

**背景**: TeleChat 是中国电信 TeleAI 实验室开源的中英双语大模型系列，其早期技术报告覆盖了 30 亿、70 亿和 120 亿参数的稠密模型。昇腾 910C 是华为的数据中心 AI 加速卡，采用双芯片封装，配备 128 GB HBM2e 显存，FP16 稠密算力约 800 TFLOPS，被视为中国最具代表性的英伟达替代方案。MindSpore 是华为开源深度学习框架，HyperParallel 则是面向昇腾超节点的分布式并行加速库，提供拓扑感知调度、分层内存池化以及声明式切分策略。Xing 4 正是把这三者结合起来，在国产软硬件生态内完成模型训练的规模化扩展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://flopper.io/gpu/huawei-ascend-910c">Huawei Ascend 910C Specs: FP16, FP32, 128 GB | Flopper.io</a></li>
<li><a href="https://arxiv.org/abs/2603.03731">[2603.03731] HyperParallel: A Supernode-Affinity AI Framework hyper-parallel:基于MindSpore的昇腾超节点分布式并行加速库 - AtomGi... Public API Reference | mindspore-ai/hyper-parallel | DeepWiki Distributed Parallel Training | MindSpore Transformers master ...</a></li>
<li><a href="https://arxiv.org/abs/2401.03804">[2401.03804] TeleChat Technical Report - arXiv.org TeleChat Technical Report - arXiv.org Tele-AI/telechat-7B · Hugging Face GitHub - Tele-AI/Telechat TeleChat: An Open-source Billingual Large Language Model TeleChat4 Leak: 2 PRs Confirm China Telecom's Reasoning LLM Tele-AI/TeleChat-12B · Hugging Face</a></li>

</ul>
</details>

**标签**: `#large language models`, `#Ascend`, `#MindSpore`, `#agentic AI`, `#large-scale training`

---

<a id="item-16"></a>
## [长上下文生成失败常常是采样问题，而非训练不足](https://arxiv.org/abs/2611.22148) ⭐️ 8.0/10

一篇新的 arXiv 论文指出，决定长上下文与智能体生成能否在高温下维持质量的，往往是采样策略而非额外训练。该研究测试了 29 个 1B 至 122B 参数的开源权重模型，覆盖十项基准和最长一百万 token 的针检索，发现 top-nsigma 能保持准确率，而 top-p、top-k 与 Top-H 会显著退化。 这一结果意味着团队可以通过在推理阶段更换采样器来提升长上下文与智能体任务的可靠性，而不必依赖昂贵的重新训练或更大的模型。它直接影响编程智能体、长链思维推理和长文本生成等常用高温采样来增加多样性的场景。 在温度为 2 时，使用 top-p、top-k 或 Top-H 的编程智能体在 100 个 GitHub issue 中解决了 0 个，而同样配置下使用 top-nsigma 的智能体在三个 Qwen3.5 模型上解决了 46 至 62 个；在所有基准上，top-nsigma 的中位数得分保持在温度 1 时的 100%，而 top-p 仅保留 26%。作者将原因归结为候选词池大小：在一个 Llama-3.1-8B 示例中，温度从 1 升到 2 会让 top-p 的候选池从 4 个 token 扩大到 51,845 个，而 top-nsigma 始终保持在 3 个；在 133 组设置中，候选池大小对评判质量的 Spearman 相关系数为 -0.77。

rss · arXiv cs.AI · 11月18日 05:00

**背景**: 大语言模型通过从下一个 token 的概率分布中采样，逐个 token 生成文本。温度是一种解码参数，会缩放模型的 logits：温度越高，分布越平坦，抽到低概率 token 的机会越大，输出更多样但也更不可靠。top-k 和 top-p（核采样）等截断采样器会在采样前限制候选池，但随着温度升高，其候选池可能不可预测地膨胀。top-nsigma 是一种较新的采样器，它根据距最大 logit 的标准差来截断候选，其作者认为它在不同温度设置下更稳健。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Tomorrowdawn/top_nsigma">GitHub - Tomorrowdawn/top_nsigma: The official code repo and ...</a></li>
<li><a href="https://arxiv.org/html/2411.07641v1">Top-𝑛𝜎: Not All Logits Are You Need - arXiv.org</a></li>
<li><a href="https://menuagentic.com/concepts/temperature-and-sampling/">Generation & Sampling : Temperature</a></li>

</ul>
</details>

**标签**: `#LLM sampling`, `#long-context generation`, `#agentic coding`, `#inference methods`, `#benchmark evaluation`

---

<a id="item-17"></a>
## [前缀缓存下，LLM 编码智能体的上下文编辑反而可能推高成本](https://arxiv.org/abs/2611.22238) ⭐️ 8.0/10

一篇新的 arXiv 论文（2611.22238）公布了一项大规模测量研究，在 SWE-bench Verified、SWE-bench 和 Loc-Bench 上对开源模型进行了两万多次运行，并分别统计未缓存输入、缓存输入与输出 token。研究发现：当缓存输入价格仅为未缓存输入十分之一时，注入检索到的代码虽使读取与搜索命令减少 18%–34%，却让总成本上升 33%–42%；而删除旧的工具输出在没有缓存折扣时可节省 19%–36%，在有缓存折扣时反而使成本增加 38%–116%。 这些结果挑战了“上下文更短或整理得更好就必然更便宜”的常见假设，并说明上下文管理技术必须依据真实的 token 定价来评估，而不能只看提示长度。这直接影响构建编码智能体的工程师，以及所有为控制成本而调整检索、压缩或观测裁剪策略的人。 论文指出，更短的提示并不保证更便宜的运行，因为智能体往往会通过增加步数来补偿；论文还警告说，并发实验可能共享缓存前缀，从而扭曲成本比较。在证据包实验中，搜索工作量的下降也没有带来可测量的任务解决率提升。

rss · arXiv cs.AI · 11月18日 05:00

**背景**: 编码智能体在每一轮都会把完整的对话历史重新发送给语言模型，因此在长轨迹中输入 token 占据了主要开销。前缀缓存（也称提示缓存）会为共享的提示前缀保存 KV 缓存，使重复出现的 token 以大幅折扣计费——本文假设约为正常输入价格的十分之一。问题在于，任何靠近上下文开头的改动（例如插入检索到的代码或删除早先的工具输出）都会使缓存前缀失效，迫使系统按全价重新计算。SWE-bench Verified 是 SWE-bench 中经过人工筛选的 500 个实例子集，被用作衡量编码智能体能力的标准基准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.swebench.com/verified.html">SWE-bench Verified</a></li>
<li><a href="https://huggingface.co/datasets/czlll/Loc-Bench_V1">czlll/Loc-Bench_V1 · Datasets at Hugging Face</a></li>

</ul>
</details>

**标签**: `#LLM agents`, `#prefix caching`, `#context management`, `#SWE-bench`, `#cost optimization`

---

<a id="item-18"></a>
## [闭式边际 ODE 揭示 DPO 与 IPO 对齐动态差异](https://arxiv.org/abs/2611.21766) ⭐️ 8.0/10

一篇新的 arXiv 论文为成对 LLM 对齐方法推导出闭式边际常微分方程（ODE），证明在梯度流极限下 DPO 的边际以 O(log t) 无界增长，而 IPO 的边际收敛到有限的 1/(2τ)。作者在五个模型家族和四个基准上验证了这些预测，并证明向 SimPO 加入 ε > 0 的标签平滑会在 Δ* = β^{-1} log((1−ε)/ε) 处形成有限边际吸引子。 这让对齐方法的选择从试错转向可预测的理论：从业者可以预判一种方法的边际会发散还是稳定、标签噪声会如何影响训练，以及如何设计具有可用工作点的损失函数。对于在大规模场景中选择 DPO、IPO 和 SimPO 类目标的研究人员和工程师而言，这一点很重要。 该分析通过投影到单个偏好/非偏好对，将动态约简为一维边际 ODE；其 DPO 结论是在梯度流极限下给出的，因此属于理想化分析，而非完整的有限步训练分析。作者把 TPO-S（ε = 0.05 的 SimPO）作为对预测有限吸引子的验证，而非提出新的最先进损失，并报告其在三个 8B–9B 模型上取得所比较方法中最高的平均 IFEval 分数。

rss · arXiv cs.LG · 11月18日 05:00

**背景**: 成对偏好对齐训练语言模型更偏好被选中的回答而非被拒绝的回答；Direct Preference Optimization（DPO）和 Identity Preference Optimization（IPO）等方法把偏好对直接转化为可优化的损失，而不再依赖单独奖励模型加强化学习循环。DPO 使用基于选中与拒绝回答对数似然比的分类式损失，IPO 则调整目标以瞄准有限的偏好边际。SimPO 是一种无需参考模型的变体，使用长度归一化的对数似然；这里的“边际”指模型给偏好输出与非偏好输出的分数差。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ozercemkelahmet.com/tools/dpo">DPO : direct preference optimization explained · Özer Cem...</a></li>
<li><a href="https://www.emergentmind.com/topics/identity-preference-optimization-ipo">Identity Preference Optimization ( IPO )</a></li>
<li><a href="https://apxml.com/courses/llm-alignment-safety/chapter-3-advanced-alignment-algorithms/contrastive-methods-alignment">Contrastive Methods for LLM Alignment</a></li>

</ul>
</details>

**标签**: `#LLM alignment`, `#DPO`, `#IPO`, `#optimization theory`, `#machine learning`

---

<a id="item-19"></a>
## [tmol：面向机器学习的 GPU 原生可微分 Rosetta 能量函数](https://arxiv.org/abs/2611.21857) ⭐️ 8.0/10

作者发布了 tmol，这是一个 GPU 原生的 PyTorch 库，重新实现了当前最先进的 RosettaGenFF 全原子力场，从而能够进行批量化的、可微分的蛋白质打分与整体结构精修。他们报告在批处理模式下吞吐量最高提升 362 倍，并展示将 tmol 作为生成式蛋白质设计中的奖励信号，可以增加设计界面处的氢键和水桥数量。 基于物理的力场在训练分布之外的泛化能力优于纯学习型模型，但其评估速度慢、梯度难以获取，长期以来基本被排除在现代机器学习流程之外。tmol 让 RosettaGenFF 具备批量化、可微分和 PyTorch 原生特性，使蛋白质设计团队可以直接把物理打分当作可微损失或奖励，与生成模型联合使用，这有望提升所设计结构与界面的真实感。 362 倍的加速是专门针对批处理吞吐量给出的数字，而非单结构对比；该库同时覆盖打分与整体结构精修，而不只是能量评估。最突出的应用是奖励引导的生成式设计，即利用力场梯度把采样导向极性更强、堆积更紧密的界面；摘要中并未说明显存开销、所支持的硬件，或相对 CPU 版 Rosetta 的精度折衷。

rss · arXiv cs.LG · 11月18日 05:00

**背景**: Rosetta 能量函数是一种全原子打分函数，它把结构能量分解为大约十余个项，例如范德华堆积、静电、氢键、溶剂化和扭转偏好，并叠加基于统计知识的权重；它是 Rosetta 结构预测、对接和蛋白质设计协议的基础。RosettaGenFF 是该力场的“通用”版本，增加了额外的原子类型和扭转类型，以便处理小分子、非天然残基和特殊环系，后来又演进出用于 AI 加速虚拟筛选的 RosettaGenFF-VS。由于这类评估传统上依赖 CPU，且不是以可微分计算图的形式编写，机器学习框架无法对其反向传播，而这正是 tmol 想要弥合的缺口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC5717763/">The Rosetta all-atom energy function for macromolecular modeling...</a></li>
<li><a href="https://www.nature.com/articles/s41467-024-52061-7">An artificial intelligence accelerated virtual screening ...</a></li>
<li><a href="https://arxiv.org/abs/2611.21857">[2611.21857] tmol: a GPU-accelerated implementation of the ...</a></li>

</ul>
</details>

**标签**: `#protein design`, `#molecular forcefields`, `#GPU acceleration`, `#PyTorch`, `#machine learning for science`

---

<a id="item-20"></a>
## [大语言模型直接编写神经网络权重，成功操控真实拖拉机](https://arxiv.org/abs/2611.21958) ⭐️ 8.0/10

一篇新的 arXiv 论文（2611.21958）展示了“权重空间编程”：GPT-6 Astra 与 Claude Fable 5.1/5.2 直接读取并修改一个用于拖拉机自动导航的、仅有 253 个参数的神经网络控制器的权重，全程不使用优化器或梯度下降。仅凭自然语言规格说明和少量仿真评估预算，两个模型都修复了一个原本为另一台拖拉机训练的网络，并从全零权重的网络中“写出”了一个可用控制器，最终所有由语言模型生成的控制器都在无人工干预的情况下操纵了真实拖拉机。 这表明前沿大模型可以像控制工程师一样工作——直接检查和手工修改网络参数，而不是依赖需要大量数据的训练流程，从而有可能大幅降低把嵌入式与机器人控制器适配到新硬件上的成本。如果这一结果能推广到 253 参数之外更大规模的网络，它或将开辟语言模型与底层机器控制之间的新接口。 该网络规模极小（仅 253 个参数），且研究只是单一案例：梯度下降最终取得了更高的精度，但需要多得多的仿真次数；而进化策略从零权重出发则完全没有找到可用控制器。语言模型写出的控制器是稀疏的，并呈现出经典的级联结构；其中一个模型是在原训练网络上做编辑，另一个则是整体替换；Claude Fable 在没有仿真反馈时的修复只能偶尔成功，真实拖拉机上的最终跟踪误差与经典 pure pursuit 基线处于同一量级。

rss · arXiv cs.LG · 11月18日 05:00

**背景**: 权重空间编程把神经网络的权重当作源代码来对待：大模型读取权重以理解网络在计算什么，并直接写入或修改权重来改变其行为，全程不需要梯度下降或训练循环。本实验的任务是拖拉机自动导航，控制器需要沿直线和圆弧路径行驶，并在硬件变化（例如转向执行器变慢）时重新调整。论文与三类基线做了对比：pure pursuit（一种经典的几何路径跟踪算法，朝路径上的前视点转向）、梯度下降训练，以及进化策略（一种无导数、类似神经进化的参数搜索方法）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rikiyat.github.io/blog/weight-space-programming/">Sparks of Weight - Space Programming : LLMs can natively read...</a></li>
<li><a href="https://publications.ri.cmu.edu/storage/publications/pub_files/pub3/coulter_r_craig_1992_1/coulter_r_craig_1992_1.pdf">Implementation of the Pure Pursuit Path Tracking Algorithm</a></li>
<li><a href="https://en.wikipedia.org/wiki/Neuroevolution">Neuroevolution - Wikipedia</a></li>

</ul>
</details>

**标签**: `#weight-space programming`, `#LLM agents`, `#neural network control`, `#robotics`, `#agriculture`

---

<a id="item-21"></a>
## [Nemotron 3.5 Super 通过任务专属强化学习最高提升 13.8 分](https://arxiv.org/abs/2611.22161) ⭐️ 8.0/10

英伟达的 Nemotron 3.5 Super（总参数 120B、激活参数 12B）以强化学习方式在五个专家构建的任务数据集上依次进行后训练，分别对应真实软件工程、复杂约束、长程工具调用、专业图表理解和企事业文档推理。每一次训练都在 Tinker 平台上用 CISPO 训练一个全新的 rank-32 LoRA 适配器，整个过程不设监督微调阶段，且每个适配器都在相同任务、相同评测框架和相同设置下与基座模型进行对比。 结果表明，在一个本身已经很强的开源基座模型之上做轻量级的任务专属强化学习，即便不做任何监督微调、也不重训整个模型，也能在困难的智能体类基准上取得两位数提升，这对希望以更低成本实现可组合专业化的团队意义重大。由于这些适配器是逐个任务训练并在十二个独立基准上评测的，这项工作为“纯强化学习后训练究竟能走多远”这一广受争论的问题提供了可复用的工程证据。 在十二个头条基准（其中八个由其他机构构建，四个由 Surge AI 构建）上，提升幅度从 IFBench 的 +4.5 分一直到 GDP_pdf 的 +13.8 分（由 10.4% 升至 24.2%）；SWE-bench Pro V2 从 86.9% 升至 92.1%，Terminal-Bench 2.1 从 63.9% 升至 70.3%，MultiChallenge 从 58.3% 升至 66.6%，AutomationBench 从 14.8% 升至 27.5%，Chartography 从 39.4% 升至 50.6%。值得注意的是，未使用 API 工具训练的文档适配器在 AutomationBench 上仍提升 +8.0 分；错误分析还显示各适配器弥补了基座模型反复出现的失败模式，不过仅凭摘要无法获知局限性说明或完整的可复现细节。

rss · arXiv cs.LG · 11月18日 05:00

**背景**: Nemotron 3.5 Super 是英伟达推出的开源混合专家（MoE）模型，每个 token 仅激活 120B 参数中的约 12B，从而在保持大模型容量的同时把推理成本控制在适中水平。该训练采用 CISPO（裁剪重要性采样策略优化），这是一种通过裁剪 token 级别的重要性权重来限制方差、并为每个 token 保留学习信号的强化学习算法，与 GRPO 直接裁剪策略比率的方式不同。Thinking Machines Lab 的 Tinker 是一个微调 API，它负责分布式训练的重活，让研究者只需关注数据和损失函数代码，这也是本次能顺利跑五个独立 LoRA 后训练任务的关键。LoRA 适配器是附加在冻结基座模型上的小型可训练权重增量，因此每个任务都能拥有自己低成本、可随时替换的专属能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://swift.readthedocs.io/en/latest/Instruction/GRPO/AdvancedResearch/CISPO.html">Clipped Importance Sampling Policy Optimization ( CISPO ) — swift...</a></li>
<li><a href="https://thinkingmachines.ai/tinker/">Tinker - Thinking Machines Lab</a></li>
<li><a href="https://research.nvidia.com/labs/nemotron/Nemotron-3.5-Super-and-Lightning/">NVIDIA Nemotron 3.5 Super and Lightning - NVIDIA Nemotron</a></li>

</ul>
</details>

**标签**: `#reinforcement learning`, `#LLM post-training`, `#LoRA`, `#benchmark evaluation`, `#Nemotron`

---

<a id="item-22"></a>
## [榜单赢家诅咒：带噪声的大模型基准会系统性高估排名靠前的模型](https://arxiv.org/abs/2611.22227) ⭐️ 8.0/10

一篇新的 arXiv 论文（2611.22227）正式提出了“榜单赢家诅咒”这一概念：由于大模型基准测试分数存在噪声，按分数排名不仅奖励真实能力，也在奖励采样运气，从而系统性高估榜首模型的表现，并使整个榜单的分数发生扭曲（作者称之为“排名诱导偏差”）。作者提出用 m-out-of-N 自助法（bootstrap）进行校正，并证明在存在正间隔的精确总体分层条件下，该方法可将 Θ(N^-1/2) 的排名偏差降低到期望残差为 o(N^-1/2)；在来自 5 个基准家族的 14 个基准上，第 1 名的校正幅度约为 0.09 至 3.86 个百分点。 榜单直接影响模型的采用、采购决策和研究方向，因此当“领先优势”部分来自统计噪声时，所谓的 SOTA 宣称就可能非常脆弱甚至具有误导性。论文提出的 RULER 报告（分数校正值、合理的排名区间以及模型分层）提供了一个具体且可推广的解决方案，基准维护方和模型开发者可以将其与原始排名一同发布。 该校正方法假设模型池固定、任务独立同分布且有界，同时允许同一任务内不同模型之间存在任意相关性，作者还给出了能够一致地恢复总体分层的充分条件。在其 SWE-bench Verified 快照中，并列榜首的模型获得了 0.90 个百分点的校正，而 173 个模型中只有 13 个进入领先层级；作者通过样本分割和校准模拟验证了有限样本下的表现。

rss · arXiv cs.LG · 11月18日 05:00

**背景**: 像 SWE-bench Verified 这样的公开榜单，是用模型在一组固定测试任务上的准确率来排名的，但每个分数都只是从有限任务样本中得到的估计值，必然带有抽样误差。当同时比较很多模型、却只把其中最高分当作“冠军”来报告时，这个最高分本身就会被高估——这正是经济学家在拍卖中称为“赢家诅咒”的统计效应。m-out-of-N 自助法是标准自助法的一个变体，它每次重采样少于 N 个观测；在统计学中，当常规的 n-out-of-n 自助法渐近正确但在有限样本下表现不佳或失效时，常采用这种方法。本文把它改造用来重新估计模型领先幅度中有多少应归因于噪声。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://onlinelibrary.wiley.com/doi/10.1002/9781118445112.stat08002">m‐Out‐of‐n Bootstrap - Lee - Major Reference Works - Wiley ...</a></li>
<li><a href="https://www.swebench.com/verified.html">SWE-bench Verified</a></li>
<li><a href="https://stats.stackexchange.com/questions/498634/bootstrap-variability-n-out-of-n-vs-m-out-of-n">Bootstrap variability: $n$-out-of-$n$ vs. $m$-out of-$n ...</a></li>

</ul>
</details>

**标签**: `#LLM evaluation`, `#benchmarking`, `#statistical bias`, `#leaderboards`, `#model selection`

---

<a id="item-23"></a>
## [CrisisBench：隐私保护型评测显示危机咨询大模型仍逊于人类咨询师](https://arxiv.org/abs/2611.21622) ⭐️ 8.0/10

研究者发布了 CrisisBench，这是一个面向危机咨询 AI 的隐私保护型评测套件，包含来自 200 段去标识化对话的 1,085 个单轮任务、1,185 个基于热线元数据构建的模拟患者大模型，以及一个由专家咨询师校准的 23 项评分标准的 LLM 裁判。在针对五个 GPT 模型以及“先起草再修改”和检索增强生成（RAG）系统的评测中，所有系统在单轮场景下的“共情过度”和“提问行为”两项上均不如人类危机咨询师。 现有基准大多忽视升级处置、风险评估与降级安抚这些危机对话的核心能力，因此该套件填补了 LLM 评测中一个真实且关乎安全的空白，并为构建或审计心理健康 AI 的团队提供了一套可复用、保护隐私的方法论。由于它表明系统在结构性能力上表现强劲的同时仍会在响应层面出现专家眼中的失误，这也提醒人们不要把高基准分数当作临床可用性的证据。 该评分标准的人类间 Krippendorff's alpha 为 0.51，LLM 与人类之间为 0.54（Pearson r = 0.80），说明一致性仅为中等水平，作者也坦承这是局限之一。在多轮评测中，RAG 以 0.961 的总分居首，各系统之间差距均在 0.058 以内；微技能与风格/语调接近满分天花板，而产出效率与安全/风险两项造成了系统间的大部分差异；咨询师对模拟患者大模型的真实性认可度为 86%、实用性认可度为 92%。

rss · arXiv cs.CL · 11月18日 05:00

**背景**: 危机热线是心理健康体系中不可或缺的一环，但长期面临人手与资金不足，这使得引入大模型辅助既具吸引力又伴随风险。由于隐私限制，真实的热线转录文本难以用于基准测试，因此该研究改用去标识化对话，以及基于热线元数据构建的合成患者模型作为替代。有两个方法论概念值得说明：Krippendorff's alpha 是一种衡量评分者间信度的统计指标，用于判断标注者的一致性是否高于随机水平；LLM 作为裁判（LLM-as-a-judge）是一种让模型依据特定任务评分标准为输出打分的评测方式，理想情况下应基于人工审核过的样本进行校准，而不能把其分数直接当作真值。检索增强生成（RAG）通过检索参考资料为模型回答提供依据，是本次评测中表现最好的配置。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Krippendorff's_alpha">Krippendorff ' s alpha - Wikipedia</a></li>
<li><a href="https://www.appen.com/llm-as-a-judge-rubric-design">LLM as a Judge | Rubric Design & Calibration - Appen</a></li>
<li><a href="https://www.appen.com/blog/krippendorffs-alpha">How Krippendorff ’ s Alpha Improves Data Reliability | Appen</a></li>

</ul>
</details>

**标签**: `#LLM evaluation`, `#AI safety`, `#mental health AI`, `#benchmarks`, `#clinical NLP`

---

<a id="item-24"></a>
## [ALOHA Lightning 仅用 50 次示范学会快速精准的双臂操作](https://arxiv.org/abs/2611.21919) ⭐️ 8.0/10

一篇新的 arXiv 论文（2611.21919）提出了 ALOHA Lightning（Flash ALOHA）双臂操作系统：它在可反向驱动的双臂平台上通过动觉示教采集接近人类速度的示范数据，然后用测试时动作平滑与视觉掩码来训练策略。每个任务仅需 50 次示范，系统即可自主完成抛接球、叠短裤、插电池和收拾餐桌等任务，成功率超过 80%，且执行速度接近人类。 模仿学习得到的操作策略普遍执行缓慢，这在重视节拍效率的真实工作流程中严重限制了其实用性；该工作从数据采集和策略执行两端同时入手来缩小这一速度差距。仅需 50 次示范的样本效率以及可复用的流水线，使快速双臂操作对基于 ALOHA 生态的机器人学与具身智能实验室更具现实可行性。 作者将速度差距归因于两点：缺乏高速采集示范数据的接口，以及难以训练在高速运动中仍保持稳健的策略。对应的解决方案是测试时动作平滑以实现平滑的高速执行，以及用掩码对齐采集阶段与部署阶段的视觉数据分布；评测涵盖四个双臂任务，成功率均超过 80%。

rss · arXiv cs.RO · 11月18日 05:00

**背景**: ALOHA（A Low-cost Open-source Hardware system for Bimanual Teleoperation）是由斯坦福主导的开源双臂机器人平台，借助 Trossen Robotics 套件得到普及，后续又扩展为 ALOHA 2，研究者可通过遥操作两台机械臂录制操作示范用于模仿学习。动觉示教则是一种相关的示教方式：人直接抓住并引导机械臂完成期望动作，同时记录轨迹，在可反向驱动的硬件上特别适合产生快速、流畅的运动。此类策略大多用相对缓慢的遥操作数据训练，因此学到的行为会继承这种迟缓性；此外示范阶段与部署阶段相机视角的数据分布差异还会进一步损害高速执行的表现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aiwiki.ai/wiki/aloha_robot">ALOHA (robot system) - AI Wiki Mobile ALOHA ALOHA Robot: Stanford's Open-Source Bimanual Teleoperation ... ALOHA — ALOHA Documentation - Trossen Robotics Learning Fine-Grained Bimanual Manipulation with Low-Cost ...</a></li>
<li><a href="https://www.trossenrobotics.com/post/aloha-robot-low-cost-bimanual-platform">Aloha Robot: A Low-Cost Bimanual Platform for Robot Learning</a></li>
<li><a href="https://arxiv.org/abs/2409.02305">[2409.02305] Kinesthetic Teaching in Robotics: a Mixed ... Kinesthetic Teaching in Robotics: a Mixed Reality Approach Kinesthetic Teaching in Robotics: a Mixed Reality Approach Kinesthetic Teaching in Robotics: a Mixed Reality Approach Empowering robotic training with kinesthetic learning and ... Kinesthetic Learning in Robotics: Development of a Six-Foot ... Kinesthetic Teaching — Robotics Glossary | Robotics Center</a></li>

</ul>
</details>

**标签**: `#robotics`, `#imitation-learning`, `#bimanual-manipulation`, `#embodied-ai`, `#robot-learning`

---

<a id="item-25"></a>
## [HubEgo-100K v1.0 发布：10124 小时真实场景第一人称工作视频助力机器人学习](https://arxiv.org/abs/2611.21938) ⭐️ 8.0/10

HubEgo-100K 论文公布了 v1.0 版本：共 10124 小时 1080p 第一人称视频，配有同步的 100 Hz IMU 数据，由 12227 名贡献者用头戴式手机摄像头在 15548 个不同环境中拍摄。该版本包含 72754 个片段（episode），覆盖 11 种场景类型、30 个工作类别、56 种任务类型和 35 个动作族，其中 83% 的时长来自工作场所，并以 CC BY 4.0 许可提供 LeRobot 与 MCAP 格式的数据及机器生成的动作与语言标注。 已发表的数据规模化研究表明，模仿学习得到的机器人策略其泛化能力主要取决于训练环境与物体的多样性，而非每个环境中的演示数量，但在成千上万种环境中采集机器人数据成本极高。HubEgo-100K 正是针对这一瓶颈，用真实工作场所中拍摄的人类第一人称视频来补位——而现有第一人称数据集多聚焦日常生活活动，恰恰缺少这一领域，因此它为机器人学习、第一人称感知以及人到机器人的迁移研究提供了可复用的资源。 所有素材均来自单个头戴式手机摄像头；作者沿各个多样性轴进行了度量，发现在随机顺序下遍历 v1.0 片段时新的贡献者和新的词汇仍不断出现，说明该语料远未饱和。论文还将这些度量与六项已发表的、与策略性能相关的数据属性（包括手部可见性和惯性传感）联系起来，并记录了采集、筛选与隐私处理流程，但这一首个版本并未包含下游策略基准或基线结果；后续版本计划补充基准并逐步扩展到 100000 小时。

rss · arXiv cs.RO · 11月18日 05:00

**背景**: 第一人称视频（egocentric video）是与机器人自身视角一致的头戴式拍摄画面，因此无需在每个场景中遥控机器人，就能用于训练视觉-语言-动作模型和操作策略。模仿学习是指从演示中训练策略，把视觉观测直接映射为动作；但众所周知，这类策略在训练时未见过的环境和物体上泛化很差，而大规模采集机器人演示数据又非常昂贵。该数据集还包含 IMU（惯性测量单元）数据，即通过加速度计与陀螺仪测量物体在三维空间中的运动与朝向，为视频提供了互补的头部运动线索。数据以 LeRobot 和 MCAP 两种格式分发，它们分别是机器人学习与机器人日志社区中常用的数据容器规范。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claru.ai/glossary/egocentric-video">Egocentric Video for AI Training — Definition & Guide | Claru</a></li>
<li><a href="https://www.alphaxiv.org/abs/2506.21057">Knowledge-Driven Imitation Learning : Enabling Generalization ...</a></li>
<li><a href="https://core-electronics.com.au/videos/getting-started-with-inertial-measurement-units-exploring-degrees-of-freedom">Getting Started With Inertial Measurement Units | Exploring Degrees...</a></li>

</ul>
</details>

**标签**: `#egocentric-video`, `#robot-learning`, `#imitation-learning`, `#datasets`, `#embodied-ai`

---