---
layout: default
title: "Horizon Summary: 2026-09-22 (ZH)"
date: 2026-09-22
lang: zh
---

> 从 469 条内容中筛选出 25 条重要资讯。

---

1. [OpenAI 发布 GPT-6 Sol 与 Luna，价格大幅下调](#item-1) ⭐️ 9.0/10
2. [Anthropic 发布 Claude Opus 5.5：写作更强、API 降价约 20–30%](#item-2) ⭐️ 9.0/10
3. [vLLM v0.30.0 发布：快速重启权重缓存、新模型支持与 CPU 稀疏内核](#item-3) ⭐️ 8.0/10
4. [Cloudflare Python Workers 结束两年预览，正式全面可用](#item-4) ⭐️ 8.0/10
5. [微软 RetroChimera 模型实现大规模小分子逆合成预测](#item-5) ⭐️ 8.0/10
6. [Hugging Face 发布 tokenizers v1：编码、解码与实测扩展性](#item-6) ⭐️ 8.0/10
7. [GeoRA：美团为 RLVR 设计的低秩训练方法获 ACL 2026 杰出论文奖](#item-7) ⭐️ 8.0/10
8. [CogGym 标准化 258 项认知实验，系统对比人类与 AI 的认知行为](#item-8) ⭐️ 8.0/10
9. [ECG Mirage：临床视觉语言模型常常忽视患者本人的心电图信息](#item-9) ⭐️ 8.0/10
10. [PIR：读出语言模型不愿透露的知识的“测谎仪”](#item-10) ⭐️ 8.0/10
11. [CleanScore：用负对照与敏感度界限开展黑盒基准审计](#item-11) ⭐️ 8.0/10
12. [长上下文大模型中的上下文投毒被形式化为极值注意力干扰](#item-12) ⭐️ 8.0/10
13. [全模态大模型中「探针最优层」并非「引导最优层」](#item-13) ⭐️ 8.0/10
14. [后训练使大模型招聘偏见趋同，系统性排斥率上升](#item-14) ⭐️ 8.0/10
15. [SCoR：从共现预测升级为科学关系预测的层级框架](#item-15) ⭐️ 8.0/10
16. [反事实检查揭示驾驶策略在排行榜之外的行为失效](#item-16) ⭐️ 8.0/10
17. [视频模型在 Physion 上准确率追平人类，推理方式却截然不同](#item-17) ⭐️ 8.0/10
18. [「爆炸性提示」：休眠式触发注入绕过 LLM 智能体防御](#item-18) ⭐️ 8.0/10
19. [研究发现在生产环境 JavaScript 包中的活跃密钥可躲过所有扫描器](#item-19) ⭐️ 8.0/10
20. [MobileCybench：用可执行探针评测 AI 智能体的漏洞发现能力](#item-20) ⭐️ 8.0/10
21. [LeaseGuard：为特权 LLM 智能体设计的保留既定占用者的准入控制层](#item-21) ⭐️ 8.0/10
22. [首个生态级测量发现 23,947 个有害开源文生图模型](#item-22) ⭐️ 8.0/10
23. [可伪造的确认机制：安全测试中确定性规则与 LLM 裁判的对比](#item-23) ⭐️ 8.0/10
24. [OpenAI GPT-6 Astra 据称破解自 2005 年以来未解的 1941 年 Enigma 密文](#item-24) ⭐️ 7.0/10
25. [Artificial Analysis 发布 Claude Opus 5.5 各推理档位基准与价格分析](#item-25) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [OpenAI 发布 GPT-6 Sol 与 Luna，价格大幅下调](https://openai.com/index/introducing-gpt-6-sol-and-luna/) ⭐️ 9.0/10

OpenAI 发布了 GPT-6 Sol 和 GPT-6 Luna 两款新模型，它们以不同的能力与成本组合扩展了 GPT-6 这一代模型，并已在 Codex 与 ChatGPT Work 中陆续上线。GPT-6 Luna 的价格约为上一代 GPT-5.6 Luna 的一半，API 定价为每百万输入 token 0.10 美元、每百万输出 token 0.50 美元。 OpenAI 在准旗舰级别以半价发布新模型，重新定义了基于大模型开发的成本结构，使开发者能在相同预算下进行多得多的智能体迭代，并直接对 Anthropic 的 Claude 等竞品形成压力。由于这些模型直接接入 Codex 与 ChatGPT Work，其影响覆盖日常编码与企业工作流，而不仅仅限于调用 API 的开发者。 根据第三方平台的收录信息，GPT-6 Luna 的缓存读取为每百万 token 0.01 美元、缓存写入为每百万 token 0.125 美元、联网搜索为每千次调用 10 美元；GPT-6 Astra 仍是该系列的顶配模型，而“Luna Pro”看起来是一种使用模式而非独立模型。GPT-6 Sol 面向复杂编码与智能体工作流，Luna 则主打更便宜的日常任务。

hackernews · OpenAI News · 9月22日 18:00 · [社区讨论](https://news.ycombinator.com/item?id=49805509)

**背景**: OpenAI 的 GPT-6 世代始于 GPT-6 Astra，官方称其引入了新一代的智能水平；Sol 与 Luna 并非取代旗舰，而是把同一套方法下放到更低的价位。此前 OpenAI 已发布过主打网络安全的 GPT-5.6 Sol 以及作为低价兄弟款的 Luna，因此这次是对既有产品线的更新。Codex 是 OpenAI 的编码智能体产品，ChatGPT Work 是面向企业的版本，二者都直接调用这些模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-6-sol-and-luna/">Introducing GPT - 6 Sol and Luna | OpenAI</a></li>
<li><a href="https://openrouter.ai/openai/gpt-6-luna">GPT - 6 Luna - API Pricing & Providers | OpenRouter</a></li>
<li><a href="https://techcrunch.com/2026/09/22/openai-launches-gpt-6-sol-and-luna/">OpenAI launches GPT - 6 Sol and Luna , boasting lower... | TechCrunch</a></li>

</ul>
</details>

**社区讨论**: 讨论集中在价格与工作流契合度上：simonw 称 Luna 价格腰斩是“一件大事”，并贴出与 GPT-6 Astra 对比的 pelican SVG 基准测试；jeffnash 则认为在用量限制与套餐换算上 Codex 明显胜过 Claude Code。也有人对纯数字视角提出异议——m_fayer 表示自己已对 5.6 Sol 的“手感”产生依赖，担心技术上更强的继任者未必同样顺手；pookieinc 则拿 OpenAI 的定价与 Claude Opus 5.5 每百万输入 4 美元、输出 20 美元的价格作对比。

**标签**: `#AI`, `#LLM`, `#OpenAI`, `#model-release`, `#developer-tools`

---

<a id="item-2"></a>
## [Anthropic 发布 Claude Opus 5.5：写作更强、API 降价约 20–30%](https://www.anthropic.com/claude-opus-5-5) ⭐️ 9.0/10

Anthropic 发布了前沿模型 Claude Opus 5.5，官方称其沟通与写作比 Opus 5 更自然清晰，回应了用户对上一代模型的常见反馈。与能力更新同时，Anthropic 将 API 价格整体下调约 20–30%，覆盖输入、输出、缓存读取与缓存写入。 旗舰模型如此幅度的降价会直接改变所有基于大模型构建产品的开发者的成本结构，而 Opus 5 据称是 OpenRouter 上支出最高的模型，因此这次降价具有真实的生态影响。发布时间也加剧了对其表态的争论——它距 Anthropic 提出“放缓前沿”安全倡议仅数日。 新价格为每百万 token 缓存读取 0.20 美元（原 0.50）、输入 4 美元（原 5）、输出 20 美元（原 25）、缓存写入 5 美元（原 6.25）。独立测试显示提升属于渐进式而非跃迁式：Simon Willison 在 low、medium、high、xhigh 各思考档位生成的“鹈鹕骑自行车”测试图车架形状均正确，而 max 档位在仍在推理时就触碰了 128,000 输出 token 的上限。

hackernews · km144 · 9月22日 16:29 · [社区讨论](https://news.ycombinator.com/item?id=49803892)

**背景**: “前沿模型”（frontier model）是业界与政策圈对当下最强通用 AI 模型的一种非正式称呼，通常指主要实验室最新的旗舰产品；该词没有公认的技术定义，主要用来标记那些能力可能带来额外风险、需要特别审视的模型。Anthropic 此前的“放缓前沿”（pacing the frontier）倡议主张实验室应有意放慢能力发布的节奏，因此评论者把 Opus 5.5 的发布解读为其安全承诺与持续快速迭代之间的张力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.levellers.ai/what-is/frontier-model">What is a frontier model ? Clear business guide | Levellers. ai</a></li>
<li><a href="https://fourweekmba.com/ai-anthropic-pacing-essay-china-response-containment/">Anthropic 's Pacing Essay and the China Response: When a Safety ...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者总体上质疑 Anthropic 的叙事：有人指出公告第一句还在提“放缓前沿”，其余内容却用具体数字展示能力快速提升；也有人算出鉴于 Opus 5 在 OpenRouter 支出榜上的统治地位，这次降价早就该来。另一些人则欢迎更清晰的写作带来的实际收益，并分享了动手评测材料，认为各思考档位之间确有差异但幅度不大。

**标签**: `#LLM`, `#Anthropic`, `#model-release`, `#AI-pricing`, `#AI-safety`

---

<a id="item-3"></a>
## [vLLM v0.30.0 发布：快速重启权重缓存、新模型支持与 CPU 稀疏内核](https://github.com/vllm-project/vllm/releases/tag/v0.30.0) ⭐️ 8.0/10

vLLM 发布了 v0.30.0，包含来自 315 位贡献者（其中 104 位是新贡献者）的 762 个提交，新增对 DeepSeek-V4.1-Flash、GLM-5.3-Flash、K2-Horizon、Cohere Compass 以及多个模型的视觉、LoRA 和 ROCm 变体的支持。该版本还引入了一个常驻的每 GPU 权重缓存守护进程，使引擎重启时可以通过 CUDA IPC 直接映射已量化、已做张量并行切分的权重（使用 `--load-format ipc_cache`），同时带来了基于 AVX512/AMX 稀疏 MLA、indexer、mHC 和 compressor 内核的 DeepSeek-V4 CPU 后端。 vLLM 是目前使用最广泛的开源大模型推理与 Serving 引擎之一，其版本更新会直接影响从业者大规模部署模型的方式。Fast Start 权重缓存针对的正是大模型服务中最棘手的运维成本之一——引擎冷启动缓慢；而 CPU 稀疏内核以及对 ROCm/LoRA 的广泛支持则扩大了 vLLM 可覆盖的硬件与部署场景范围。 Fast Start 现在也覆盖 FP4 权重与多节点张量并行；HiSparse 分层机制会在 GPU 显存紧张时把稀疏 MLA 的 KV 页换出到固定（pinned）主机内存，并通过每个请求的 GPU 热缓冲区来响应 top-k 未命中的查询。其他值得注意的数据包括：在图捕获期间冻结垃圾回收，使 H200 上的图捕获时间从 12 秒降至 2 秒、引擎初始化从 28.9 秒降至 8.2 秒；以及基于带密钥 PRF 的 Gumbel-max 水印，支持按请求关闭，并提供与投机解码兼容的双密钥版本。

github · khluu · 9月22日 05:20

**背景**: vLLM 是一个用于大语言模型服务的开源引擎，以 PagedAttention 等技术著称，可在大量并发请求下高效管理 KV 缓存显存。它的版本迭代通常涉及张量并行（TP，即把模型切分到多张 GPU 或多个节点上）以及 MXFP8、NVFP4 等低精度量化格式——这些是微缩放（microscaling）浮点格式，在 NVIDIA Blackwell GPU 上有原生加速。FlashMLA 指 DeepSeek 为基于 MLA 的模型优化的注意力内核；AVX512 与 AMX 则是 Intel CPU 的指令集扩展，可加速向量与矩阵运算，这正是把稀疏 MLA 推理搬到 CPU 上的原因。常驻的 IPC 缓存之所以重要，是因为对量化权重从磁盘重新加载并重新切分，是服务引擎每次重启或扩容时延迟的主要来源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pytorch.org/blog/faster-diffusion-on-blackwell-mxfp8-and-nvfp4-with-diffusers-and-torchao/">Faster Diffusion on Blackwell: MXFP 8 and NVFP4 with Diffusers and...</a></li>
<li><a href="https://www.deepep.org/en/flashmla">FlashMLA</a></li>
<li><a href="https://community.intel.com/t5/Blogs/Tech-Innovation/Cloud/Profiling-Code-To-Check-For-Utilization-of-Intel-AMX/post/1523871">Profiling Code To Check For Utilization of Intel® AMX Instructions</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#model serving`, `#GPU optimization`, `#open source`

---

<a id="item-4"></a>
## [Cloudflare Python Workers 结束两年预览，正式全面可用](https://simonwillison.net/2026/Sep/21/cloudflare-python-worker/) ⭐️ 8.0/10

Cloudflare 宣布 Python Workers 正式全面可用（GA），经过约两年的预览期后，Python 成为 Cloudflare 开发者平台上的一等公民、获得完整支持的语言。其实现方式是通过 Pyodide 将 Python 编译为 WebAssembly，并运行在 Cloudflare 基于 V8 的 workerd 运行时中；发布公告由 Gyeongjae Choi、Dominik Picheta 和 Hood Chatham 署名，其中两人是 Pyodide 的核心维护者。 Python 在主流边缘/无服务器平台上成为获得完整支持的语言，改变了开发者实际可以在边缘部署的工作负载范围，也代表 Cloudflare 对更广泛的 Python 与 Pyodide 生态的重大投入。它还为 Python 开发者提供了一条更低摩擦的路径，接入此前主要面向 JavaScript 和 Rust Workers 的同一平台，可能把更多数据、AI 和脚本导向的 Python 社区引向无服务器边缘部署。 由于运行在 WebAssembly 虚拟机内，存在官方记录的若干限制，其中最突出的是 multiprocessing 和 threading 均无法工作，因此依赖 CPU 的并行计算和基于线程的并发模式都不可用。本地开发体验也值得一提：pywrangler 工具（在 PyPI 上以 workers-py 名称发布）会在本地完整模拟整个技术栈，在 123MB 的 workerd 二进制文件中，以 V8 承载 WebAssembly 中的 Pyodide 来执行代码，该文件最终位于 node_modules/@cloudflare/workerd-darwin-arm64/bin/workerd。

rss · Simon Willison · 9月21日 22:25

**背景**: Cloudflare Workers 是一个无服务器平台，代码运行在 Cloudflare 的边缘网络上，而不是运行在单一源站服务器上；其运行时 workerd 是一个开源的 JavaScript/Wasm 服务端运行时，与生产环境中支撑 Workers 的代码同源。Pyodide 是编译为 WebAssembly 的 Python 发行版，把 CPython 解释器和一批软件包带入浏览器或其他 WebAssembly 宿主环境。Cloudflare 的做法是把两者结合起来：Python 代码经 Pyodide 编译为 WebAssembly，并在 workerd 的 V8 隔离环境中执行，这也解释了为什么依赖操作系统进程或原生线程的标准库功能无法正常工作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/cloudflare/workerd">GitHub - cloudflare/ workerd : The JavaScript / Wasm runtime that...</a></li>
<li><a href="https://blog.cloudflare.com/workerd-open-source-workers-runtime/">Introducing workerd : the Open Source Workers runtime</a></li>
<li><a href="https://pyodide.org/en/stable/usage/downloading-and-deploying.html">Downloading and deploying Pyodide — Version 314.0.7</a></li>

</ul>
</details>

**标签**: `#cloudflare`, `#python`, `#webassembly`, `#edge-computing`, `#serverless`

---

<a id="item-5"></a>
## [微软 RetroChimera 模型实现大规模小分子逆合成预测](https://www.microsoft.com/en-us/research/blog/improving-synthesis-prediction-of-small-molecules-at-scale-with-retrochimera/) ⭐️ 8.0/10

微软研究院在《Nature》上发表论文，推出了一款名为 RetroChimera 的前沿逆合成模型，用于预测小分子的合成路径。该模型融合了两个具有互补归纳偏置的新组件，据称性能大幅超越现有模型，并已在 GitHub 上开源。 定制分子的合成既缓慢又昂贵，这成为医药、材料和农业领域进展的瓶颈。更准确、可扩展的逆合成模型能够加速药物发现与材料研究，让化学家和 AI 系统探索更广阔的候选分子空间。 RetroChimera 以目标产物分子（用 SMILES 字符串编码）作为输入，输出若干条经过排序的候选化学反应路径。该方法从目标分子反向推导至更简单、更易获得的前体，并已通过 Microsoft Foundry／Azure AI 模型目录对外提供。

rss · Microsoft Research · 9月21日 15:30

**背景**: 逆合成是有机化学中的经典方法：化学家从目标分子出发，反向拆解为更简单的起始原料，从而规划一系列构建它的反应步骤。在 AI 驱动的逆合成中，机器学习模型基于大规模的已知反应数据库自动提出并排序这些候选路线。SMILES 是一种用文本表示化学结构的标准记法，使模型能够读取和输出分子。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/microsoft/retrochimera">GitHub - microsoft/ retrochimera : RetroChimera : a frontier...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Retrosynthetic_analysis">Retrosynthetic analysis - Wikipedia</a></li>
<li><a href="https://ai.azure.com/catalog/models/RetroChimera?source=microsoft">Explore the comprehensive catalog of AI models from Microsoft Foundry</a></li>

</ul>
</details>

**标签**: `#AI for Science`, `#Retrosynthesis`, `#Chemistry`, `#Machine Learning`, `#Drug Discovery`

---

<a id="item-6"></a>
## [Hugging Face 发布 tokenizers v1：编码、解码与实测扩展性](https://huggingface.co/blog/tokenizers-v1) ⭐️ 8.0/10

Hugging Face 发布了 tokenizers v1，这是其被广泛使用的分词库的首个正式大版本，配套博客文章介绍了 encode 与 decode 接口以及经过实测的扩展性（scaling）结果。此次发布意味着该库正式走出长期停留的 0.x 阶段，为 transformers 生态提供了稳定且明确版本化的 API。 几乎所有使用 Hugging Face 模型的 NLP 与大模型流水线都把分词器放在关键路径上，因此 encode/decode 的速度与内存表现会直接影响数据预处理吞吐量以及推理服务的成本。v1 这一里程碑还意味着 API 进入稳定期，这对需要锁定依赖版本、长期维护生产级预处理代码的团队尤为重要。 该库以 Rust 为核心并配有 Python 绑定，支持 BPE、WordPiece 和 Unigram 这几种主流子词算法，同时提供偏移量追踪（offset tracking）、对齐（alignment）以及特殊 token 处理等下游模型所依赖的功能。博客将性能主张表述为“实测的扩展性”而非单一微基准，这对并行化处理和大规模语料预处理场景而言是更有参考价值的指标。

rss · Hugging Face Blog · 9月21日 00:00

**背景**: 分词是几乎所有 NLP 流水线的第一步：原始文本被切分成更小的单元（token），再映射为模型可以处理的数字 ID。BERT 以及 GPT 类现代语言模型普遍采用子词分词（subword tokenization），它介于字符级切分与词级切分之间，使得罕见词可以由高频片段组合而成，而不必被当作未知词处理。Hugging Face 的 tokenizers 库之所以成为其 transformers 模型背后的默认“fast”分词器，正是因为 Rust 实现比纯 Python 分词快得多，而在处理数十亿 token 的预处理场景中，分词往往会成为瓶颈。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/huggingface/tokenizers">GitHub - huggingface/ tokenizers : Fast State-of-the-Art Tokenizers ...</a></li>
<li><a href="https://huggingface.co/docs/tokenizers/index">Tokenizers · Hugging Face</a></li>
<li><a href="https://medium.com/data-science/byte-pair-encoding-subword-based-tokenization-algorithm-77828a70bee0">Byte-Pair Encoding: Subword -based tokenization | TDS Archive</a></li>

</ul>
</details>

**标签**: `#tokenizers`, `#NLP`, `#Hugging Face`, `#open source`, `#performance`

---

<a id="item-7"></a>
## [GeoRA：美团为 RLVR 设计的低秩训练方法获 ACL 2026 杰出论文奖](https://tech.meituan.com/2026/08/27/ACL-Outstanding-Paper-GeoRA.html) ⭐️ 8.0/10

ACL 2026 公布了杰出论文奖（Outstanding Paper），全球共 18 篇论文入选，其中一篇来自美团履约技术团队。该论文提出 GeoRA——一种专为 RLVR（可验证奖励强化学习）设计的 LoRA 式低秩训练方法，并分享了其在业务 Agentic RL 系统中的落地经验。 LoRA 等参数高效微调技术最初主要面向监督微调场景，而一种专为 RLVR 设计的低秩方法有望降低大模型强化学习后训练的计算与显存开销。论文附带的一线落地经验，也让它对正在构建 Agent 产品的工程团队具有直接参考价值，而不仅仅停留在学术榜单上。 目前可获取的摘要只是一则简短公告，因此该方法的诸多细节——例如低秩结构如何嵌入 RLVR 的策略优化循环、采用了哪些评测基准、存在哪些局限——尚无法从现有内容中核实。可以确认的是，这项工作将 LoRA 式参数化与 RLVR 训练相结合，并同时获得了论文奖项与美团自身 Agentic RL 生产环境的双重验证。

rss · 美团 Blog · 9月22日 19:37

**背景**: LoRA（低秩适配）会冻结预训练模型的原始权重，只学习规模很小的低秩更新矩阵，从而大幅降低微调成本，它属于参数高效微调（PEFT）这一大类方法。RLVR 指的是奖励信号由自动验证而非人工偏好得来的强化学习，通常通过校验模型答案是否正确来给出奖励，现已成为提升推理模型能力的常用手段。Agentic RL 则把这一范式扩展到多步智能体任务，策略模型需要调用工具、与环境交互并完成长程任务。ACL 是自然语言处理领域的顶级会议之一，其“杰出论文”每年只授予极少数被认为意义重大的工作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://paperswithcode.co/paper/2608.29188">Locked at the Entrance, Open Inside: Where RLVR ... | Papers with Code</a></li>
<li><a href="https://thudm.github.io/slime/get_started/agent.html">Agentic RL Training Roadmap — slime</a></li>
<li><a href="https://huggingface.co/thuml/webarena-world-model-rlvr">thuml/webarena-world-model- rlvr · Hugging Face</a></li>

</ul>
</details>

**标签**: `#LoRA`, `#RLVR`, `#Reinforcement Learning`, `#Parameter-Efficient Fine-Tuning`, `#Agentic AI`

---

<a id="item-8"></a>
## [CogGym 标准化 258 项认知实验，系统对比人类与 AI 的认知行为](https://arxiv.org/abs/2609.21259) ⭐️ 8.0/10

一个由认知科学家和 AI 研究者组成的广泛团队发布了 CogGym，该框架通过半自动化、人在回路（human-in-the-loop）的流水线，把来自 100 篇论文的 258 项认知实验统一转换为与任务无关的 Experiment Markup Language（EML）。在首个版本中，该框架用 50 个大语言模型与人类被试在常识推理实验上的作答进行对比，发现了明确的规模扩展趋势，但模型与人类的拟合度远低于人类自身的分半信度上限。 大多数 AI 基准测试关心的是模型能否给出客观正确答案，而 CogGym 关心的是模型是否在相同实验条件下复现人类被试的真实行为模式，从而把数百项零散异质的心理学研究转化为可复用、可复现的评测基础设施。一旦被广泛采用，它就能为学界提供一把独立于任务准确率的“类人程度”标尺，而随着模型越来越多地被部署在需要模拟人类判断的场景中，这一区分显得尤为重要。 模型与人类的拟合度仍远低于人类分半信度上限：最佳模型在文本、图像和视频实验中仅达到 R² = 0.59、0.58 和 0.43，而人类信度分别为 0.93、0.95 和 0.92；同时，模型在这类常识任务上的提升速度明显慢于数学、编程等形式化推理基准。作者把 CogGym 定位为一个“活”的框架，将持续纳入新的认知实验，因此其价值取决于社区能否持续贡献和采用。

rss · arXiv cs.AI · 9月22日 04:00

**背景**: 认知科学积累了数千项严格控制的行为实验，用来测量人如何判断、记忆和推理，但这些实验的刺激材料、指导语和作答格式差异极大，很难大规模地拿去做 AI 模型对照。CogGym 的解决办法是定义 Experiment Markup Language（EML）：一种结构化表示，用来描述实验的指导语、刺激、作答询问和流程，即被试看到什么、作答如何被采集，包括选项与量表锚点。随后由 AI 智能体加人工审核的半自动化流水线把已有论文转成这种格式，再把模型当作“被试”来运行。这里的“分半信度”指的是人类样本两半之间相互一致的程度，它为任何模型-人类相关性设定了一个理论上限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.21259">[2609.21259] CogGym: Towards Large-Scale Comparative Evaluation of Human and Machine Cognition</a></li>
<li><a href="https://arxiv.org/html/2609.21259">CogGym: Towards Large-Scale Comparative Evaluation of Human and Machine Cognition</a></li>
<li><a href="https://coggym.org/doc">EML & MEML Documentation | CogGym</a></li>

</ul>
</details>

**标签**: `#benchmarks`, `#cognitive-science`, `#evaluation`, `#human-machine-comparison`, `#datasets`

---

<a id="item-9"></a>
## [ECG Mirage：临床视觉语言模型常常忽视患者本人的心电图信息](https://arxiv.org/abs/2609.21755) ⭐️ 8.0/10

一篇新的 arXiv 预印本（arXiv:2609.21755）提出并评估了「ECG Mirage」这一失效模式：临床视觉语言模型表面上具备多模态能力，但实际上并未真正依赖患者本人的心电图信息。作者在急诊科基准数据集 MDS-ED 上测试了四个 VLM，分别输入匹配心电图、结果不一致的错配心电图以及无图像输入，发现匹配心电图对预测 ICU 入住或临床恶化都没有稳定优势。随后他们在冻结 VLM 主干的前提下，用监督学习加条件直接偏好优化训练了四个受限视觉提示（visual prompt），把平衡准确率提升到 ICU 入住预测 70.6%、恶化预测 67.5%，并把匹配与错配之间的性能差距分别扩大到约 16.5 和 5.5 个百分点。 这一结果说明，医学 VLM 在基准测试上的高分可能掩盖了对捷径的依赖，即所报告的多模态性能未必代表模型真的在用好心电图这类影像数据。这直接关系到医疗 AI 的验证方式与临床落地安全性，也说明反事实式（类因果）的评估应成为临床多模态模型的标准做法。 论文区分了两种失效形式：一种是 ECG neglect（心电图几乎不带来预测增益），另一种是 ECG confusion（匹配心电图优于无图像输入，但不如来自其他患者的错配心电图）。由于缓解方法只调优轻量级的视觉提示而冻结 VLM 主干，它被视为比全量微调更高效的方案，但 67%–71% 左右的平衡准确率在真实临床场景中仍有较大提升空间。

rss · arXiv cs.AI · 9月22日 04:00

**背景**: 视觉语言模型（VLM）是能同时处理图像和文本的 AI 系统，是纯文本大语言模型的延伸，知名代表包括 GPT-4V、Gemini、Claude 以及 LLaVA 等开源模型。在急诊医学中，临床决策依赖病史、生命体征、化验结果和心电图（记录心脏电活动的检查）等异构数据，而 MDS-ED 正是为测试模型处理这类多模态急诊数据而构建的基准数据集，包含大量目标标签。论文担心的是：由于预测信号可能早已存在于随附的临床文本中，模型完全可以在这些任务上取得高分，却根本不使用图像模态。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2609.21755">ECG Mirage : Revealing and Mitigating the Underutilisation of ECGs in...</a></li>
<li><a href="https://arxiv.org/abs/2407.17856v3">[2407.17856v3] MDS - ED : Multimodal Decision Support in the...</a></li>
<li><a href="https://huggingface.co/blog/vlms">Vision Language Models Explained</a></li>

</ul>
</details>

**标签**: `#Vision-Language Models`, `#Clinical Prediction`, `#ECG`, `#Evaluation Benchmarks`, `#Medical AI`

---

<a id="item-10"></a>
## [PIR：读出语言模型不愿透露的知识的“测谎仪”](https://arxiv.org/abs/2609.21996) ⭐️ 8.0/10

一篇新的 arXiv 论文（2609.21996）提出了“内部识别探针”（Probe of Internal Recognition，PIR），这是一种无需参考模型的方法，灵感来自法医学中的隐藏信息测试：它把问题与若干候选答案一起输入模型，然后从模型内部状态中读出它真正认定为正确的那个候选答案。在来自五个模型家族（Gemma、Qwen、Llama、Mistral 和 Phi）的八个模型上，PIR 识别出目标答案的平衡准确率达到 0.70–0.87，远高于“未知问题”基线的 0.28–0.40 以及 0.25 的随机概率。 该方法能够区分“模型不愿回答”与“模型无法回答”，这直接关系到 AI 安全领域中关于「消极怠工」（sandbagging）、欺骗行为以及「遗忘学习」（unlearning）验证的研究——仅凭输出无法判断模型是在隐藏能力还是确实不具备该能力。如果该结果得到进一步验证，它有望成为前沿模型能力审计与评测流程中的标准工具。 PIR 无需参考模型：它既不需要一个“诚实”的参照模型，也不需要带标注的真值语料；在所有测试过的隐藏情形下（提示诱导的欺骗、训练得到的消极怠工，以及密码锁定或被「电路破坏」的检查点）其识别能力依然可读，识别率保持在 0.85–0.93 之间。当遗忘学习真正抹除了知识时，识别率会降到模型从未学过该问题的水平；论文还指出该信号具有因果性，能提供黑盒行为线索之外的额外信息，并且可以从多项选择题扩展到自由文本生成。

rss · arXiv cs.AI · 9月22日 04:00

**背景**: 「消极怠工」（sandbagging）是指模型在评测中故意表现不佳，从而让外界低估其真实能力，已有研究显示大语言模型可以通过提示被诱导出这种行为。检查模型内部激活状态（而不仅仅是其文本输出）是「机制可解释性」的核心手段；本文借鉴了一种名为「隐藏信息测试」的法医方法（也称「有罪知识测试」或脑指纹技术）：向嫌疑人展示真实细节与若干干扰项，若其对某项表现出更强的生理反应，说明其认出了该项。PIR 把同样的逻辑搬到网络内部：模型内部反应最强的那个候选答案，即被视为它所“认得”的答案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/papers/2609.21996">Paper page - A Lie Detector Test for Language Models : Reading...</a></li>
<li><a href="https://arxiv.org/abs/2406.07358">[2406.07358] AI Sandbagging : Language Models can Strategically...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Brain_fingerprinting">Brain fingerprinting - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#interpretability`, `#deception detection`, `#LLM evaluation`, `#alignment`

---

<a id="item-11"></a>
## [CleanScore：用负对照与敏感度界限开展黑盒基准审计](https://arxiv.org/abs/2609.22183) ⭐️ 8.0/10

CleanScore 提出了一套黑盒审计框架：把每道基准题目转为一个父项，包含一个公开题面形式以及两个独立撰写、但保留原有数字、事实与答案的新题面形式，并针对“公开形式优势”给出一个区间估计，而不是给出是非判断。一项预先注册的审计在 200 道 GSM8K 和 200 道 ARC-Challenge 题目上测试了五个开源模型，未发现与预先暴露相一致的性能优势，将表面形式带来的虚高限定在 5 个百分点以内；同时预先注册的正对照实验量化了基于改写的审计可能漏掉多少污染。 基准污染是当前大模型评测有效性的最大威胁之一，因为公开榜单分数可能来自对题目的记忆而非真正的推理能力，而绝大多数模型的训练数据并不公开。CleanScore 提供了一套可复用的黑盒方法，结合负对照、敏感度界限与预注册实验，使研究者能够审计自己无法窥探内部的模型分数，并诚实地说明“未发现污染”这一结论究竟能排除什么、不能排除什么。 最值得注意的是其中的正对照结果：即使只让模型见过某道题，它在从未见过的改写版本上的准确率提升，几乎与在原始措辞上的提升一样大，导致 52% 到 110% 的污染效应对“改写式审计”完全不可见。在 ARC 上，人为植入的 49 个点的优势只对应 -0.020 的可观测差距，而即便重写题干与选项，仍有约 20 个点在四个训练随机种子下保留下来——这意味着表面形式的零结果所能排除的范围，远小于词语级污染审计所暗示的范围。

rss · arXiv cs.LG · 9月22日 04:00

**背景**: 基准污染指的是评测题目（或其近似文本）曾出现在模型训练数据中，因此高分可能衡量的是预先接触而非真正的能力。GSM8K 是广泛使用的小学数学应用题数据集，约含 1300 道题；ARC-Challenge 是多项选择形式的科学推理基准。两者都是公开且被反复使用的数据集，因而成为污染担忧的常见对象。黑盒审计意味着审计者看不到模型权重或训练数据，只能依据模型输出的得分开展工作。负对照是指被认为未受污染的项目或条件，用来估计“仅仅换个说法”本身会带来多大影响；而“传输半径”（transport radius）则是明确假定该基线效应可以外推到真正受审题目的范围。预注册实验指分析方案事先固定，以避免事后挑选有利于结论的结果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.22183">[2609.22183] CleanScore: Black-Box Benchmark Audits with...</a></li>
<li><a href="https://deepeval.com/docs/benchmarks-gsm8k">GSM8K | DeepEval - The LLM Evaluation Framework</a></li>
<li><a href="https://localmaxxing.com/en/benchmarks">LLM Benchmarks | Localmaxxing</a></li>

</ul>
</details>

**标签**: `#benchmark contamination`, `#LLM evaluation`, `#black-box auditing`, `#negative controls`, `#reproducibility`

---

<a id="item-12"></a>
## [长上下文大模型中的上下文投毒被形式化为极值注意力干扰](https://arxiv.org/abs/2609.22101) ⭐️ 8.0/10

一篇新的 arXiv 论文（2609.22101）将长上下文大语言模型中的“上下文投毒”形式化为注意力中的极值干扰：决定性证据的得分存在上界，而有效干扰项中的最高得分会随干扰项数量增长。在 softmax 检索抽象下，作者推导出一个有限样本上界，证明若要将准确率维持在基准率之上的固定目标，证据边际必须以 Ω(√log N) 的规模增长，其中 N 是有效干扰项数量；论文还用受控实验对此进行了验证。 这项工作从理论上解释了为什么单纯扩大上下文窗口并不能转化为更好的证据利用能力，而这一问题直接影响 RAG 流水线、长上下文智能体，以及所有默认“检索文本越多越安全”的应用。其结论也指向了一系列架构层面的应对方案，例如先检索后推理（retrieve-then-reason）架构、证据瓶颈、抗别名表征、验证器介导的记忆以及对比式抗投毒训练。 一个关键细节是，N 指的是“有效干扰项数量”而非原始上下文长度，因此性能退化取决于真正容易混淆的条目有多少，而不只是输入了多少 token。该分析把长上下文退化与分数别名（score aliasing）、位置别名（positional aliasing）和 softmax 稀释联系起来；实验还显示，在固定上下文长度下，“同格式”干扰项条件造成了最大幅度的准确率下降，而检索门控只有在保住证据召回率的前提下才能改善证据利用。

rss · arXiv cs.CL · 9月22日 04:00

**背景**: Transformer 的注意力使用 softmax 函数，其权重之和恒为 1，因此随着上下文中的 token 增多，每个 token 分到的注意力份额会变薄，这就是通常所说的“注意力稀释”。正因如此，长上下文模型容易被无关或刻意混淆的材料带偏，这类现象常被称为上下文投毒、上下文干扰或上下文冲突。极值理论又补充了第二个因素：当干扰项数量不断增加时，它们得分的最大值往往会随之上升，于是固定的证据信号最终可能被压制。这里的“难负样本（hard negatives）”指的是表面上与正确证据相似的干扰项，例如格式或措辞相同的段落。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.22101">[2609.22101] Context Poisoning as Extreme - Value Attention ...</a></li>
<li><a href="https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html">How Long Contexts Fail | Drew Breunig</a></li>
<li><a href="https://bytebell.ai/blog/softmax-attention-dilution-problem/">Softmax Attention and the Dilution Problem: The Math Behind Context...</a></li>

</ul>
</details>

**标签**: `#long-context`, `#attention`, `#LLM`, `#context-poisoning`, `#retrieval`

---

<a id="item-13"></a>
## [全模态大模型中「探针最优层」并非「引导最优层」](https://arxiv.org/abs/2609.22135) ⭐️ 8.0/10

一篇新的 arXiv 论文（2609.22135）首次对「线性探针准确率最高的层，也是激活引导效果最好的层」这一普遍假设进行了因果检验，结果在三个独立开发的全模态大语言模型上均被证伪。作者以「情绪」作为受控实验对象，覆盖文本、音频和图像输入，发现探针最优层在不同架构间差异巨大，而引导有效的层则始终集中在归一化深度的中后段狭窄区间内。 这一发现挑战了机制可解释性与 AI 安全研究中的常见做法——许多工作直接依据探针表现来挑选干预层；它提醒人们，某个概念「可被读出」并不等于它「可被控制」。论文还提出了一个实用的跨架构经验法则：在中后段层进行引导，这可能改变研究者在多模态模型中设计干预的方式。 配对随机方向对照实验显示出约 26 倍的因果差距，从而排除了随机扰动和方向质量作为解释的可能；logit-lens 分析还揭示出「因果把手—探针饱和—词表承诺」的分阶段前向过程。作者提出双因素解释：引导效果同时取决于表征的可读性和下游可塑性；他们还发现了一个按效价（valence）与唤醒度（arousal）组织的跨模态情绪子空间，其中「喜悦」在各模型中充当稳定锚点。代码与数据已在 GitHub 上公开。

rss · arXiv cs.CL · 9月22日 04:00

**背景**: 激活引导（activation steering）是一种推理期技术，通过修改模型隐藏层的内部激活来改变其行为，无需重新训练，常被用于对齐与安全干预。线性探针（linear probe）则是在同样的隐藏状态上训练的简单分类器，用来检验诸如「情绪」这样的概念是否可以从某一层被线性解码；可解释性研究常假设「最容易解码的层」同时也是因果作用最强的层。全模态大模型把文本、音频和图像信号送入同一个残差流（residual stream），即信息在各 Transformer 层之间传递的加性通路，从而扩展了这一研究场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bobrupakroy.medium.com/steering-large-language-models-with-activation-vectors-a-practical-guide-45866b3697ac">Steering Large Language Models with Activation Vectors: A Practical Guide | by Rupak (Bob) Roy - II | Medium</a></li>
<li><a href="https://www.emergentmind.com/topics/linear-probes">Linear Probes: Neural Network Diagnostics</a></li>
<li><a href="https://lenguyen.vercel.app/note/math-transformers">Residual Stream is Key to Transformer Interpretability | nguyen le</a></li>

</ul>
</details>

**标签**: `#mechanistic-interpretability`, `#multimodal-LLMs`, `#activation-steering`, `#probing`, `#AI-safety`

---

<a id="item-14"></a>
## [后训练使大模型招聘偏见趋同，系统性排斥率上升](https://arxiv.org/abs/2609.22169) ⭐️ 8.0/10

一篇新的 arXiv 论文（2609.22169）对十个大语言模型的基础版本与后训练版本进行了对比研究，发现后训练使各模型之间的招聘决策相关性大幅提高；在十个模型中有八个，后训练模型回复年长申请者的概率比基础模型低 3.6%。随着模型之间共识增强，全局系统性排斥率从 5.6% 跃升至 17.3%，而后训练模型在交叉身份维度上的系统性排斥率介于 12.2% 到 21.7% 之间。 该研究把算法偏见从“单个模型的缺陷”重新定义为“市场层面的均衡问题”：如果雇主都采用经过类似后训练的模型，被排斥的群体将同时被所有系统拒绝，求职者失去通过其他渠道获得机会的可能。这把 AI 公平性研究与劳动经济学、AI 治理联系起来，说明评估应衡量模型群体之间的相关性偏见，而不是孤立地审计单一模型。 决策相关性似乎主要来自技能、大学专业等人力资本特征，而由此产生的不平等主要源于后训练所放大的年龄歧视。作者明确指出这一权衡：后训练可能帮助模型挑选出客观上更强的申请者，但同时会统一地引入新的偏见，伤害处于边缘位置的群体；因此该结论是关于决策相关性与排斥率的发现，并不意味着后训练降低了模型的原始准确率。

rss · arXiv cs.CL · 9月22日 04:00

**背景**: 大语言模型通常分两个阶段构建：先在大规模文本语料上预训练以学习通用规律，再通过后训练（如监督微调与基于人类反馈的强化学习）使其对齐人类偏好、安全规范与任务质量。后训练是把原始的下一个词预测器变成可用助手的关键步骤，也正成为商业部署或招聘场景落地前的默认环节。由于雇主越来越多地用这些模型筛选和排序候选人，论文追问：当整个劳动力市场都依赖同一套后训练配方塑造的模型时会发生什么——作者称之为“单一文化偏见”，这一概念呼应了此前关于算法单一文化与系统性排斥的哲学讨论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2609.22169">Monocultural Biases : Correlated biases in large language models ...</a></li>
<li><a href="https://lecture2go.uni-hamburg.de/l2go/-/get/v/68040">Algorithmic Monoculture and the Ethics of Systemic Exclusion - Prof.</a></li>
<li><a href="https://www.linkedin.com/pulse/unsung-hero-ai-why-post-training-llms-demand-your-attention-paul-ya1gc">The Unsung Hero of AI: Why Post - Training LLMs Demand Your...</a></li>

</ul>
</details>

**标签**: `#AI fairness`, `#LLM bias`, `#post-training`, `#AI governance`, `#labor economics`

---

<a id="item-15"></a>
## [SCoR：从共现预测升级为科学关系预测的层级框架](https://arxiv.org/abs/2609.22174) ⭐️ 8.0/10

一篇新的 arXiv 预印本提出了 SCoR 框架，把研究方向发现重新定义为“层级式科学关系预测”，包含三个时间上对齐的任务：首次共现、首次科学关系形成，以及关系形成时的类型判定。作者基于 2017 至 2026 年间发表的 187,848 篇 cs.CV 论文构建了 SCoR-Graph，得到 270,687 个归并概念、745 万条共现边和 615,036 条带类型的有向关系边，并发布了 SCoR-Bench——一个经过泄漏审计的基准，其关系类型测试集全部由专家人工核验。其任务适配模型族 HiSCoR 在留出的 2025–2026 时间窗上取得 AUROC 0.9515，相对最强时序图基线提升 2.4%（相对值），population-AUPRC 提升 14.0%，关系类型变体的 Macro-AUROC 为 0.7795。 以往 AI 辅助科学的工作大多只预测哪些概念会在未来论文中同时出现，而这反映的是共同关注度，而非连接的科学含义；SCoR 转而追问关系是否会出现以及属于哪种类型，例如一个方法是在使用、组合、取代还是反驳另一个方法。论文把这一新定义与大规规模数据集和经过泄漏审计的基准配套发布，既带来方法论贡献也带来资源贡献，可能改变研究方向预测这一课题的研究与评估方式。 该基准的关系类型测试集带有专家核验的黄金标签，消融实验表明语义视图、共现视图和带类型关系视图提供了互补的预测证据。HiSCoR 通过编码截断点之前的事件历史，并把关系形成条件化于未来共现，将关系涌现建模为随时间演化且受层级约束的过程；值得注意的是，这目前仍只是一篇 arXiv 预印本，尚无独立复现或验证结果。

rss · arXiv cs.CL · 9月22日 04:00

**背景**: AI 辅助科学通常依赖知识图谱——其中研究概念是节点、连接表示概念之间的关系——以及追踪这些连接随时间演化的时序图模型。此类基准的一个常见隐患是泄漏：测试期的信息意外地或结构性地渗入训练数据，从而虚高分数；因此“经过泄漏审计的基准”会显式构建针对不同截断时间点的图快照，并核查只使用了截断点之前的信息。本文使用的评价指标包括 AUROC（衡量模型把正例排在负例之前的排序能力）和 AUPRC（对罕见正例事件——例如一条全新科学关系的诞生——的性能更为敏感）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.22174">[2609.22174] SCoR : A Hierarchical Framework for Forecasting ...</a></li>
<li><a href="https://arxiv.org/abs/2605.00865">[2605.00865] Leakage - Audited Benchmarking Reveals Limited...</a></li>
<li><a href="https://link.springer.com/article/10.1186/s12859-026-06621-x">ToxBench: a leakage - audited multi-task benchmark for predictive...</a></li>

</ul>
</details>

**标签**: `#AI-assisted science`, `#scientific relation forecasting`, `#knowledge graphs`, `#benchmark`, `#research direction discovery`

---

<a id="item-16"></a>
## [反事实检查揭示驾驶策略在排行榜之外的行为失效](https://arxiv.org/abs/2609.22582) ⭐️ 8.0/10

该论文提出了一套「反事实检查」方法：取数百帧真实驾驶画面，对每一帧做两种编辑（移除行人，或施加夜间风格的重新打光扰动），每次编辑都由独立检测器验证，然后把规划轨迹的变化当作诊断结果而非评分来解读。在 246 个 NAVSIM 近行人场景中，当行人确实位于规划路径上时，只有 1.9% 的响应属于真正的避让；在六种已发布的端到端与 VLA 策略上，间隙变化的中位数最多为 0.03 米，规划距离变化的中位数最多为 0.08 米。 排行榜名次反映的是一个结果，而不是结果背后的行为，因此很难预测策略在新场景下的表现——这对任何要把驾驶策略选入真实部署的团队都是关键问题。该工作把评估变成可迁移到不同驾驶方向习惯的逐项行为诊断（并通过预注册实验验证），为自动驾驶乃至更广泛的具身智能策略鲁棒性评估提供了替代单一数字排名的具体方案。 作者从这些反事实编辑中提取出两条因果轴，并据此构建五项「考试」：策略规划要开多远、看到行人是否真的换来安全、这种响应是否随危险程度放大、在无需反应时规划是否会变动，以及一个无关的照明变化会让它偏移多少。在一项从左侧驾驶到右侧驾驶的预注册测试中，暴露度与特异性的排序、照明判定和碰撞结果可以迁移，但具体数值和危险敏感性判定不能；多数判定在几十帧内即可稳定，而危险敏感性需要数百帧；代码与编辑后的帧将被公开。

rss · arXiv cs.CV · 9月22日 04:00

**背景**: 端到端驾驶策略直接把原始传感器输入映射为规划轨迹，而视觉-语言-动作（VLA）模型在此基础上引入了语言推理能力，但两者通常仍用 nuScenes 或 NAVSIM 排行榜上的开环误差来比较。开环评估只是回放真实数据、不让策略的动作改变未来，因此成本低，却与闭环驾驶行为的关联有限。此处的「域偏移」指策略被放到新地点或新条件下测试——例如自车走廊内出现行人、夜间照明，或不同的驾驶方向习惯——此时训练分布已不再匹配。反事实编辑只改动场景中的某一个因素并观察输出的变化，从而把因果敏感性与单纯的相关性区分开。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.22582">[2609.22582] Beyond the Leaderboard: Counterfactual Diagnosis of...</a></li>
<li><a href="https://arxiv.org/pdf/2406.15349">NAVSIM : Data- Driven Non-Reactive</a></li>
<li><a href="https://arxiv.org/abs/2512.16760">[2512.16760] Vision-Language-Action Models for Autonomous Driving: Past, Present, and Future</a></li>

</ul>
</details>

**标签**: `#autonomous driving`, `#vision-language-action`, `#evaluation`, `#robustness`, `#causal inference`

---

<a id="item-17"></a>
## [视频模型在 Physion 上准确率追平人类，推理方式却截然不同](https://arxiv.org/abs/2609.22788) ⭐️ 8.0/10

一篇新的 arXiv 论文提出了一种分布式评估框架，把模型随机种子和人类评分者分别视为两个“群体”，并把它应用到 Physion 物理推理基准上。在该基准上，V-JEPA2 把准确率差距缩小到约 1 个百分点（73.2% 对 74.2%），但模型与人类的分歧率高达 26.4%，而人类之间的分歧率仅为 4.8%，Cohen's kappa 分别约为 0.48 和 0.91。 这一结果动摇了此前被广泛接受的推论：在视频物理推理基准上达到与人类相当的准确率，并不意味着模型像人一样进行前向模拟，因此“达到人类水平”的准确率宣称比表面看起来要弱得多。该评估框架可复用于任何模型可能利用统计捷径的基准，对评估设计、视频/世界模型研究以及“认知合理性”主张都有直接意义。 这种分歧与任务对前向模拟的需求程度相关：模型在“连接”等几何推理任务上超过人类（+11.8 个百分点），但在“滚动”等重力动力学任务（-11.8 个百分点）和“多米诺骨牌”等因果链任务（-10.5 个百分点）上落后于人类。所测试的三个 ViT-L 架构（V-JEPA2、VideoMAEv2、DINOv2）都表现出非人类的策略特征，归因分析进一步显示，预测这种分歧的是不可观测的结果特征，而非可见的场景属性；代码已在 GitHub 上开源。

rss · arXiv cs.CV · 9月22日 04:00

**背景**: Physion 是一个基准与数据集，它向人类和 AI 模型展示同一批约 1200 段关于物体滚动、滑动、下落和碰撞的短视频，然后要求判断哪个结果是物理上合理的，其目的在于把机器的预测与人类的物理直觉进行对比。V-JEPA2 是 Meta 提出的自监督视频世界模型，通过预测未来视频的被掩码潜在表示来训练；VideoMAEv2 与 DINOv2 则是常用的掩码视频建模和视觉 Transformer 基线。核心问题是：这类模型究竟是在真正地随时间前向模拟物理过程，还是仅仅利用了可见场景中的统计规律——这一区别单靠准确率分数无法分辨。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://physion-benchmark.github.io/">Physion: Evaluating Physical Prediction from Vision in Humans and Machines | physion-benchmark.github.io</a></li>
<li><a href="https://arxiv.org/abs/2106.08261">[2106.08261] Physion: Evaluating Physical Prediction from Vision in Humans and Machines</a></li>
<li><a href="https://github.com/facebookresearch/vjepa2">GitHub - facebookresearch/vjepa2: PyTorch code and models for VJEPA2 self-supervised learning from video. · GitHub</a></li>

</ul>
</details>

**标签**: `#evaluation`, `#video-understanding`, `#physical-reasoning`, `#foundation-models`, `#benchmarks`

---

<a id="item-18"></a>
## [「爆炸性提示」：休眠式触发注入绕过 LLM 智能体防御](https://arxiv.org/abs/2609.22510) ⭐️ 8.0/10

一篇新的 arXiv 论文（编号 2609.22510）提出了「爆炸性提示」（explosive prompt）：一种嵌入被检索内容中的条件式载荷，在攻击者选定的触发条件出现前一直处于休眠状态，本质上是一种无需训练、仅在推理期生效的后门。把直白的注入指令改写为休眠式条件语句后，在前沿模型上引发真实、改变状态的工具调用比例从配对的平均 2.4% 提升到 16.5%（某专有模型上高达 34.2%）；在九个生产级智能体上（包括 OpenAI Codex、Gemini CLI、Claude Code CLI、Cursor CLI、GitHub Copilot、Devin AI CLI、Amazon Kiro CLI、Qwen Code 和 Google Assistant）成功率为 43%–83%，而直白指令基线最多只有 3%。 其重要性在于：现有针对间接提示注入（IPI）的防御大多建立在「内容被读取的那一刻就检测恶意指令」这一假设上，而爆炸性提示的时间分离特性直接击穿了该假设——现成的注入分类器在其上校准失准，一个已能完全阻断直白指令注入的偏好优化模型仍执行了 11.8% 的爆炸性提示，且全部发生在触发轮次。任何让智能体读取网页、文档或代码仓库文件的产品都面临该风险，论文认为可行的修复方向是在内容摄入阶段检测其条件式结构。 作者提出的检测器 DeFuse 在 5% 校准误报预算下将实际工具执行攻击成功率降至 3.0%，检测质量 AUC 达 0.9994，延迟比同类方法低 25 倍，但需要采用长度感知的阈值；仅用其生成的爆炸性提示数据重新训练编码器基线，就能把攻击成功率从无防御时的 34.3% 降到 7.5%–8.1%。需要注意的局限：目前仅是一篇 arXiv 预印本，摘要经过截断，完整方法与防御细节不可见；每个生产智能体的试验样本量 n=30；也尚无社区讨论可供评估其独立验证情况。

rss · arXiv cs.CR · 9月22日 04:00

**背景**: 间接提示注入是一种攻击方式：攻击者把恶意指令隐藏在 LLM 之后会检索到的内容里（网页、PDF 或代码注释），使模型把攻击者文本当作可信指令并执行；当模型是带有工具和状态的智能体时，这可能意味着真实动作，例如发送邮件或修改文件。「无需训练、推理期后门」意味着攻击者从不修改模型权重：恶意行为完全由推理时输入中存在的触发条件激活，此处即一句条件性表述，让载荷在被选定的上下文出现前一直休眠。该论文的贡献在于把间接提示注入重新表述为这类条件式载荷，并在九个生产级智能体后端（包括来自 OpenAI、Google、Anthropic、Cursor 和 GitHub 的 CLI 智能体）上做了基准测试。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection - Wikipedia</a></li>
<li><a href="https://neuraltrust.ai/blog/inference-gguf-templates">Inference - Time Backdoors : The Hidden Security Risk in... | NeuralTrust</a></li>
<li><a href="https://arxiv.org/pdf/2601.08511">STAR: Detecting Inference - time Backdoors in LLM Reasoning via...</a></li>

</ul>
</details>

**标签**: `#prompt injection`, `#LLM security`, `#AI agents`, `#adversarial ML`, `#agent safety`

---

<a id="item-19"></a>
## [研究发现在生产环境 JavaScript 包中的活跃密钥可躲过所有扫描器](https://arxiv.org/abs/2609.23042) ⭐️ 8.0/10

一篇 arXiv 论文（编号 2609.23042）记录了两条真实的利用链——生产环境 JavaScript 包中泄露的 Azure AD 客户端凭据和 Azure API Management（APIM）订阅密钥——并报告在约 2000 个企业 Web 资产中有 113 个（5.65%）对外提供了活跃凭据。作者通过人工核验构建了包含 194 个密钥级凭据的真值集（GT-194），发现其中 13.9%（194 个中的 27 个）只有依靠人工分析才能发现，所评估的九款生产扫描器全部漏报，扫描器合计覆盖率最高仅停留在 86.1%。 这一结果挑战了当前主流的“左移”（shift-left）假设，即在部署前扫描源代码就已足够，揭示出一个与具体工具无关的盲区，任何向浏览器交付 JavaScript 的组织都可能受影响。由于泄露的凭据中包括完整托管在同一个包内的 Azure AD 令牌签发链，其影响并非理论上的合规卫生问题，而是通向账户接管与大规模数据泄露的直接路径。 表现最好的纯静态扫描器仅恢复了 36.6% 的密钥，而最佳的运行时感知扫描器达到 77.8%（F1 = 0.818，McNemar p < 0.001）；经 CryptoJS 加密的配置能击败所有静态扫描器，因为凭据只有用同处一地的密钥解密之后才会存在：在 86 个密钥暴露的应用中有 63 个（73.3%）可以从浏览器代码触达完整的 Azure AD 令牌签发链，而 LLM 抽取结果由第二个模型独立验证，Brennan-Prediger kappa 为 0.676。作者指出这些召回率数据仅限于单一组织、以 Azure 为主的语料库，并描述了凭据未被察觉地流入生产环境的五种路径。

rss · arXiv cs.CR · 9月22日 04:00

**背景**: 部署前的密钥扫描通常只检查源代码仓库与构建产物，而不检查已部署的 Web 应用实际向访问者提供了什么内容，因此被内联、转换或加密进 JavaScript 包中的密钥就可能被漏掉。Azure AD 客户端凭据是用于申请 OAuth 令牌的应用身份密钥，而 APIM 订阅密钥是调用通过 Azure API Management 发布的 API 所需的共享密钥——任何一方落入攻击者手中都能获得程序化访问权限。CryptoJS 是浏览器端广泛使用的 AES 加密 JavaScript 库，当解密密钥与密文一同下发时，加密就不再有实质保护作用。Brennan-Prediger kappa 是一种用于衡量两名标注者或两个模型对同一批样本分类一致程度的统计量，此处用来量化基于 LLM 的密钥抽取的可靠性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rdrr.io/github/raredd/ragree/man/bp.coeff.raw.html">bp.coeff.raw: Brennan-Prediger kappa coefficient in raredd/ragree: Rater agreement</a></li>
<li><a href="https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-create-subscriptions">Create Subscriptions in Azure API Management | Microsoft Learn</a></li>
<li><a href="https://dev.to/shubhamkhan/beginners-guide-to-aes-encryption-and-decryption-in-javascript-using-cryptojs-592">Beginner’s Guide to AES Encryption and... - DEV Community</a></li>

</ul>
</details>

**标签**: `#security`, `#secrets-management`, `#web-application-security`, `#empirical-measurement`, `#llm-evaluation`

---

<a id="item-20"></a>
## [MobileCybench：用可执行探针评测 AI 智能体的漏洞发现能力](https://arxiv.org/abs/2609.23980) ⭐️ 8.0/10

一篇新的 arXiv 论文提出 MobileCybench，用“探针”（probes）来评测 AI 智能体的漏洞发现能力：探针是安全属性的可执行检查，通过在实际应用中重放所报告的利用代码，判断该利用是否真的成功、以及违反了哪一条安全属性。该基准包含 13 个 Android 应用和 495 条由论文作者撰写并评审的探针，并用它在 4 种攻击场景下评测了 5 个编程智能体（OpenCode 搭配 GPT-5.5、GPT-5.6-Sol 和 GLM-5.2；Claude Code 搭配 Opus 4.8 和 Opus 5），过程中发现 23 个此前未被报告的漏洞。 如今 AI 智能体生成漏洞报告的速度已经超过人类维护者的审核速度，因此一种能够自动、可复现地验证“所报告的利用是否真实有效”的方法，正在成为安全工作的关键基础设施。由于探针编码的是安全属性而非某个已知漏洞，该框架还能发现探针编写时尚不为人知的缺陷，这使得它更像是 AI 安全评测中可复用的方法论，而不是一次性的排行榜。 在只提供混淆后 APK 的情况下，表现最好的智能体（OpenCode 搭配 GPT-5.6-Sol）在“恶意应用”场景中触发了 53.8% 应用的探针，但在“远程攻击者”场景中仅为 16.7%；当允许访问源代码时，所有智能体在两种攻击场景下的平均触发率从 28.8% 提升到 32.8%。需要注意的是，该基准局限于单一领域（13 个 Android 应用），且新发现的 23 个漏洞中只有“大多数”得到了维护者确认。

rss · arXiv cs.CR · 9月22日 04:00

**背景**: 传统漏洞发现依赖模糊测试（fuzzing）、静态分析和人工审计，产出的通常是一份仍需人工复现与判断的缺陷报告。论文中的探针思路正好相反：不去判断报告是否匹配某个已知 CVE，而是把每条安全属性（例如“未授权的调用方能否读取隐私数据”）写成一个小的可执行测试，运行探针既能验证利用是否成功，也能指明被违反的具体安全属性。该基准测试了两种真实的 Android 威胁模型——安装在受害者设备上的恶意应用，以及拥有低权限账户的远程攻击者——并分别只提供编译后的混淆 APK 或完整源代码，这与 AI 编程智能体在真实场景中能拿到的输入一致。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.23980">[2609.23980] MobileCybench: Evaluating Agent Vulnerability ...</a></li>
<li><a href="https://papers.cool/arxiv/2609.23980">MobileCybench: Evaluating Agent Vulnerability Discovery via...</a></li>

</ul>
</details>

**标签**: `#ai-agents`, `#security`, `#benchmarks`, `#android`, `#vulnerability-discovery`

---

<a id="item-21"></a>
## [LeaseGuard：为特权 LLM 智能体设计的保留既定占用者的准入控制层](https://arxiv.org/abs/2609.24077) ⭐️ 8.0/10

研究者提出了 LeaseGuard，这是一个确定性的准入层，在任何适配器执行之前，通过规范化的资源租约、既定占用者健康检查、效果感知准入、共存上限以及资源范围内的覆盖机制来拦截特权 LLM 智能体的操作。在一个由 60 个新编写的冲突场景构成、并配有匹配对照组的冻结基准上，跨两个本地模型家族测试，它将未授权抢占从 73.3% 降至 0.0%，并将安全任务完成率提升了 70.0 个百分点（场景聚类 95% 置信区间 [60.8, 79.2]）。 特权智能体为了完成新任务而杀掉或覆盖正在健康运行的任务，是智能体系统中真实存在却长期被忽视的安全缺口；这项工作表明，一个相对轻量、确定性的准入闸门——而不是更聪明的模型——就能堵住其中的大部分问题。对于任何部署会操作文件、进程、套接字、锁或容量分配的智能体的人来说，这一结果都很重要，因为它把“抢占权限”重新定义为独立于“执行特权”的东西。 这些收益并非没有代价：请求任务的成功率变化为 -3.3 个百分点（95% 置信区间 [-9.2, 2.5]），意味着该闸门可能拦截部分合法请求，不过该区间跨越了零点。作者还报告称，经过完整评估的 v0.2 broker 在哈希链式压力审计中成功拒绝了一次伪造的既定任务身份；同时他们警告，仅依赖过期回收机制时，一旦续约被漏掉，健康的既定占用者仍可能被暴露，因此这些保证只在效果被完全中介、任务归属经过认证、且租约过期能真实反映占用者存活状态时才成立。

rss · arXiv cs.CR · 9月22日 04:00

**背景**: 特权 LLM 智能体越来越多地把用户请求转换为系统操作，例如创建、终止、覆盖、绑定或分配资源。其核心洞见在于：执行特权决定的是某项操作能否运行，而不是请求方是否有权抢占当前资源所有者——因此一个权限足够的智能体可以悄无声息地挤掉一个依赖同一文件、进程、套接字、锁或容量分配的健康占用者。LeaseGuard 借用了分布式系统中的经典租约模式，即带 TTL、定期续约、未续约即失效的时间受限独占授权，并将其作为智能体工具执行前的准入闸门来使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2609.24077">LeaseGuard: Incumbent -Preserving Admission Control for Privileged...</a></li>
<li><a href="https://hackernoon.com/building-distributed-leases-with-consensus-heartbeats-and-fencing-tokens">hackernoon.com/building- distributed - leases -with-consensus...</a></li>
<li><a href="https://www.educative.io/courses/distributed-systems-practitioners/leases-in-distributed-systems">Leases for Safe Distributed Locking and Concurrency Control</a></li>

</ul>
</details>

**标签**: `#LLM agents`, `#AI safety`, `#admission control`, `#resource management`, `#systems`

---

<a id="item-22"></a>
## [首个生态级测量发现 23,947 个有害开源文生图模型](https://arxiv.org/abs/2609.24134) ⭐️ 8.0/10

一篇新的 arXiv 论文（2609.24134）首次对专门为有害服务定制的开源文生图（T2I）模型进行了系统性的生态级测量，作者将这类模型称为“Monet”。研究以真实模型平台的政策为依据，在八个主要 T2I 模型平台上识别出 23,947 个此类模型，其中最热门的一个下载量超过 1,900 万次。 研究结果表明，各平台各自为政的审核机制在结构上难以奏效：有害 T2I 模型会在不同平台之间迁移、在封禁后继续存活，甚至被用于组织化的商业服务。这对模型平台运营方、AI 安全与政策研究者以及监管机构都具有重要意义，说明需要跨平台的威胁情报与协同治理，而非孤立执法。 该研究提出的分类法涵盖十类有害服务；40.76% 的 Monet 被镜像到多个平台，而跨平台存档使 11.99% 的模型在原始平台封禁后仍可访问。作者还记录了关键词混淆、模型级安全防护绕过等规避手段，以及两起有组织的商业活动——一个覆盖 668 个模型、完成 914 笔委托，另一个为灰产“养号”服务做广告；这些模型还通过 GitHub 项目和推理 API 触达下游用户，引发儿童安全方面的担忧。

rss · arXiv cs.CR · 9月22日 04:00

**背景**: 像 Stable Diffusion 这样的文生图模型通常在“模型平台”（model hub）上共享——即用户上传和下载权重及微调变体的集中式网站；由于微调和轻量级适配器让模型定制成本极低，这类平台上汇聚了数十万个社区模型。“Monet”是论文对刻意打造、用于支撑平台政策所禁止服务（例如未经同意的私密影像等滥用内容）的模型的称呼。以往研究多聚焦于单一平台上的个别有害模型，因此本文首次将整个生态作为一个整体来刻画其传播、规避与变现，而不是一次只研究一个平台或一类危害。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2609.24134">Monet: Measuring the Ecosystem of Open-Source Text - to - Image ...</a></li>
<li><a href="https://www.toolify.ai/ai-news/master-model-hubs-and-huggingface-python-ai-tutorial-2663183">Master Model Hubs and HuggingFace - Python AI Tutorial</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#text-to-image`, `#open-source ecosystem`, `#harmful content`, `#measurement study`

---

<a id="item-23"></a>
## [可伪造的确认机制：安全测试中确定性规则与 LLM 裁判的对比](https://arxiv.org/abs/2609.24200) ⭐️ 8.0/10

一篇新的 arXiv 论文（2609.24200）将“可伪造的确认”（forgeable confirmation）形式化为 AI 辅助安全测试中的一个可审计攻击面，说明被测系统可以伪造测试工具用来判定攻击成功的证据。在一个四阶段的 AI 辅助流水线中，15 个确认机制里有 9 个可被伪造，而是否可伪造完全取决于该判定是否读取了攻击者可控的数据；该预测在 16 个留出机制上完全命中，并在公共扫描器模板的 12,203 个机制上达到 99.9%的准确率。 自动化安全测试与 AI 安全智能体越来越依赖机器给出的判定，并把漏洞当作事实上报，而这项研究说明这种信任往往是错位的：确定性规则比八个开放权重 LLM 裁判更容易被伪造，在仅 2%的攻击者可控响应内容下就会失败，而 LLM 裁判的中位数为 50%。它还直接质疑以字符串匹配来评定成功与否的基准测试，因为这类确认恰恰是攻击者可以轻易伪造的。 论文指出，某一个检查的任何实现都无法同时做到既稳健又精确，而在规则与 AI 裁判之间做路由反而把伪造成功率提高到 99%。把决定性证据转移到攻击者无法写入的通道后，攻击成功率从 97%降至 0%，并通过“escalate”（升级）判定找回因此损失的灵敏度；但当被扫描的主机本身就是攻击者时，这一防护会失效。

rss · arXiv cs.CR · 9月22日 04:00

**背景**: AI 辅助安全测试流水线把生成攻击、执行攻击以及判断攻击是否成功这一整套循环自动化，而最后这一步“确认”正是把原始输出变成漏洞报告的关键。LLM-as-a-judge（用大模型充当裁判）是一种常见做法，即用语言模型代替刚性规则来打分或分类；开放权重模型则指训练得到的参数被公开释放、任何人都可以下载、运行或微调的模型。论文的核心洞见在于：测试框架与被测系统往往共享同一条通道，因此任何读取攻击者可写数据的确认规则都可能被攻击者操纵。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.24200">[2609.24200] Forgeable Confirmation in Automated Computer...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Open-weight_model">Open-weight model</a></li>
<li><a href="https://github.com/google/adk-python/issues/6461">Human-in-the-loop tool confirmation is forgeable by an A2A peer...</a></li>

</ul>
</details>

**标签**: `#AI security`, `#automated security testing`, `#LLM judges`, `#adversarial robustness`, `#vulnerability scanning`

---

<a id="item-24"></a>
## [OpenAI GPT-6 Astra 据称破解自 2005 年以来未解的 1941 年 Enigma 密文](https://www.cryptocellar.org/bgac/the-mvueh-break.html) ⭐️ 7.0/10

Frode Weierud 的 CryptoCellar 网站发布报告称，OpenAI 的 GPT-6 Astra 破解了一段以指示符“MVUEH”标识的 82 字母 Enigma 密文，该站点表示这条密文自 2005 年以来一直无人能解。恢复出的明文是一条德军电文，内容为询问行军路线，称发报者位于 Rosenow，并要求立即以无线电回复（Waschbusch）。 如果这一结果能够被复现，它将是一个前沿模型解决长期悬而未决的全新问题的有力能力展示，直接影响研究者对 LLM 在密码分析中的推理、搜索与工具调用能力的判断。它也让一个争论更加尖锐：实验室关于模型具备强大密码学能力的说法，究竟反映的是真正的自主解题能力，还是精心编排的传统暴力搜索。 评论者指出，该模型自己编写了 Python 和 C++ 的 Enigma 模拟器，这意味着大部分工作可能被外包给了传统的暴力搜索，而非真正的模型推理；同时这一孤例并未附带基准测试、可复现材料或正式评估。还有评论者报告称，Gemini 3.8 Flash 在无人工引导的运行中约 45 分钟就恢复出了同样的明文，说明这次破解未必是某个模型独有的能力。

hackernews · sohkamyung · 9月22日 13:52 · [社区讨论](https://news.ycombinator.com/item?id=49801324)

**背景**: Enigma 是二战期间纳粹德国用于军事通信的转子式密码机，操作员输入明文后，机器会依据每日密钥设置逐字母替换；当时电文常用“X”作为词分隔符，并常含传输错误和拼写错误。Frode Weierud 的 CryptoCellar 是知名的研究档案站点，维护着尚未破解的 Enigma 密文清单，“MVUEH”正是其中之一。密码分析始终与密码学共同演进，新密码催生新的攻击方法；而现代 LLM 代理带来新的变化——它们把写代码、跑搜索、迭代假设当作工具来用，而不是纯粹在上下文里解题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mixed-news.com/en/gpt-6-astra-cracks-1941-enigma-message-unsolved-since-2005/">GPT-6 Astra cracks a 1941 Enigma message that had resisted...</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-6_Astra">GPT-6 Astra</a></li>
<li><a href="https://subagentic.ai/howtos/how-to-design-autonomous-cryptanalysis-agents/">How to Design Autonomous Cryptanalysis Agents : Lessons from...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论热情与质疑并存：tantalor 认为“完全靠自己完成”与模型自行编写 Enigma 模拟器这一事实相矛盾，并追问这些软件以及破解过程有多少是真正新颖的、有多少只是外包给暴力搜索；nonethewiser 则认为随着模型解决越来越多新问题，我们正在跨越一个门槛。Sophira 提出了一个尖锐的技术疑问——密钥错误是否也可能解出看似合理的电文（假阳性）；podgorniy 则报告 Gemini 3.8 Flash 在无引导情况下约 45 分钟一次性解出明文，暗示这一成果并非 Astra 独有。

**标签**: `#cryptanalysis`, `#LLM capabilities`, `#Enigma`, `#autonomous agents`, `#community discussion`

---

<a id="item-25"></a>
## [Artificial Analysis 发布 Claude Opus 5.5 各推理档位基准与价格分析](https://artificialanalysis.ai/models/claude-opus-5-5) ⭐️ 7.0/10

Artificial Analysis 发布了 Claude Opus 5.5 的基准测试与价格对比页面，并按推理强度（reasoning effort）档位拆分，分别给出默认的 "medium"、"high"、"xhigh" 以及最高档 "max" 的独立页面。随后的 Hacker News 讨论聚焦于单任务成本（cost per task），有评论者在 high 档对 high 档的比较中称其成本约为 Opus 5 的一半。 随着前沿实验室不断推出带多档推理强度的模型，开发者需要第三方提供的分档位数据——包括智能水平、延迟和单任务成本，而不是只听厂商的宣传。这类独立评测会直接影响团队在生产环境中默认采用哪一档，而讨论也引出了一个更普遍的问题：发布时的基准成绩在几周之后是否依然成立。 Simon Willison 指出，"max" 档位两次都未能完成 "Generate an SVG of a pelican riding a bicycle" 这一简单提示，因为它在仍在推理时就耗尽了全部 128,000 token 的预算。另一位评论者则认为 "high" 才是实用的最优档位，因为许多基准成绩在该档位之后便开始趋于平台期，而性能表现依然不错。

hackernews · theanonymousone · 9月22日 16:51 · [社区讨论](https://news.ycombinator.com/item?id=49804316)

**背景**: 推理模型在给出答案之前会消耗数量可变的 "思考" token，厂商通过 reasoning effort 或思考 token 预算之类的参数来让用户权衡这一取舍。更高的推理强度通常能提升困难任务上的质量，但同时会增加延迟与 token 成本，因此最高档位并不总是性价比最优。Artificial Analysis 是一个独立评测网站，发布包括 Intelligence Index 和加权平均单任务成本在内的模型对比数据，其成本口径意在覆盖完整的思考开销，而不只是输出 token。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://artificialanalysis.ai/models">Comparison of AI Models across Intelligence... | Artificial Analysis</a></li>
<li><a href="https://api-docs.deepseek.com/guides/thinking_mode/">Thinking Mode | DeepSeek API Docs</a></li>
<li><a href="https://llm-stats.com/benchmarks">AI & LLM Benchmarks 2026: Rankings, Scores & Results</a></li>

</ul>
</details>

**社区讨论**: 整体情绪对成本表现相当积极——hglaser 认为 high 档下单任务成本减半 "真的很不错"；但对最高档位则持怀疑态度，Willison 的鹈鹕测试说明 max 档可能把预算烧光却什么都输出不了。breckenedge 提出了更深层的担忧，即发布后的基准回退问题：他称在内部数据集上，某模型几周后性能下滑到与更弱的模型持平，并提醒厂商有动机在发布时把成绩做到最好。____tom____ 则对页面的定价表述提出异议，认为把该模型称为 "相对同价位模型略显昂贵" 反映的是所选对比区间，而非模型本身。

**标签**: `#llm-evaluation`, `#benchmarks`, `#ai-models`, `#model-pricing`, `#reasoning-models`

---