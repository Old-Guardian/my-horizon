---
layout: default
title: "Horizon Summary: 2026-06-13 (ZH)"
date: 2026-06-13
lang: zh
---

> 从 140 条内容中筛选出 20 条重要资讯。

---

1. [美国政府要求 Anthropic 暂停 Fable 5 和 Mythos 5 的访问权限](#item-1) ⭐️ 9.0/10
2. [FFmpeg 发现 21 个零日漏洞](#item-2) ⭐️ 9.0/10
3. [中国 RNA 编辑技术 LEAPER 首次用于 DMD 人体治疗](#item-3) ⭐️ 9.0/10
4. [vLLM v0.23.0 发布：深度优化 DeepSeek-V4 并扩展 Model Runner V2](#item-4) ⭐️ 8.0/10
5. [CRISPR-Cas12a2 选择性粉碎癌细胞](#item-5) ⭐️ 8.0/10
6. [开源 AI 必须获胜以防止中心化](#item-6) ⭐️ 8.0/10
7. [Apple 将 TrueType 微调解释器迁移至 Swift](#item-7) ⭐️ 8.0/10
8. [华为 1B 参数 SpaceMind 模型登顶空间智能基准](#item-8) ⭐️ 8.0/10
9. [欧洲初创公司 SOLiTHOR 实现 465 Wh/kg 固态电池演示电芯](#item-9) ⭐️ 8.0/10
10. [AUR 供应链攻击投毒超 400 软件包](#item-10) ⭐️ 8.0/10
11. [谷歌 Android 安全主管因军事 AI 合作辞职](#item-11) ⭐️ 8.0/10
12. [Linux 7.2 将自动创建多尺寸透明大页](#item-12) ⭐️ 8.0/10
13. [GitHub 利用 LLM 推理减少密钥扫描误报](#item-13) ⭐️ 8.0/10
14. [教皇 AI 信函指出治理失败，顾问如此主张](#item-14) ⭐️ 8.0/10
15. [学生耿引爆中国科研诚信丑闻](#item-15) ⭐️ 8.0/10
16. [人类在严格数学测试中超越 AI](#item-16) ⭐️ 8.0/10
17. [激光相位板提升冷冻电镜蛋白质结构成像质量](#item-17) ⭐️ 8.0/10
18. [SGLang v0.5.13 发布，新增模型支持并默认启用 Spec V2](#item-18) ⭐️ 7.0/10
19. [资深 Mozilla 成员离职，批评官僚化转型](#item-19) ⭐️ 7.0/10
20. [雷诺的无稀土电机：旧技术的新推动](#item-20) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [美国政府要求 Anthropic 暂停 Fable 5 和 Mythos 5 的访问权限](https://www.anthropic.com/news/fable-mythos-access) ⭐️ 9.0/10

这标志着政府对先进 AI 监管的重大升级，可能为控制强大 LLM 树立先例。它直接影响到依赖尖端模型的 AI 开发者、研究人员和用户，并引发了关于平衡创新与安全的讨论。 该指令适用于公开发布的 Claude Fable 5 以及此前仅限特定合作伙伴使用的无限制版本 Claude Mythos 5。Anthropic 未披露暂停的完整范围，但该指令似乎基于国籍和地点限制访问。

hackernews · Dylan1312 · 6月13日 00:51 · [社区讨论](https://news.ycombinator.com/item?id=48511072)

**背景**: Anthropic 于 2026 年 6 月 9 日推出了 Claude Fable 5，作为其最强大模型的安全公开版本，同时推出了面向授权合作伙伴的无限制版本 Claude Mythos 5。该公司一直强调 AI 安全并倡导负责任的部署，一些观察者认为这促使政府决定实施限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>
<li><a href="https://www.cnbc.com/2026/06/09/anthropic-mythos-claude-fable-5.html">Anthropic releases Mythos-like AI model to the public, Claude Fable 5</a></li>

</ul>
</details>

**社区讨论**: 社区评论意见分歧严重：一些人批评 Anthropic 的安全言论适得其反，而另一些人则强调政府对 AI 控制的更广泛影响。一个反复出现的主题是，Anthropic 的恐慌营销可能引来了它现在面临的限制，许多用户指出这为未来的监管树立了先例。

**标签**: `#AI safety`, `#government regulation`, `#LLM access`, `#Anthropic`, `#US policy`

---

<a id="item-2"></a>
## [FFmpeg 发现 21 个零日漏洞](https://depthfirst.com/research/21-zero-days-in-ffmpeg) ⭐️ 9.0/10

研究人员在广泛使用的多媒体处理库 FFmpeg 中发现了 21 个零日漏洞，展示了 LLM 辅助漏洞发现的有效性。 这些漏洞对任何依赖 FFmpeg 的服务构成严重风险，尤其是媒体摄取管道、监控系统和转码服务。这一发现也凸显了 FFmpeg 长期存在的安全问题以及人工智能发现关键缺陷的潜力。 其中一个特别严重的漏洞影响使用攻击者控制的 RTSP URL 的部署，使媒体管道、监控系统和转码服务可利用。该研究展示了 LLM 如何自动化漏洞发现，但也引发了对报告数量与实际修复之间比例的关注。

hackernews · redbell · 6月12日 22:13 · [社区讨论](https://news.ycombinator.com/item?id=48510046)

**背景**: FFmpeg 是一个自由开源的多媒体框架，处理音频、视频及其他媒体格式，被无数应用和服务广泛集成。多年来，模糊测试等工作表明它历来存在大量内存损坏错误。LLM 辅助的漏洞发现利用大型语言模型分析代码以识别潜在漏洞，这可以加快发现速度，但也可能使维护者不堪重负。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://link.springer.com/chapter/10.1007/978-3-032-03705-3_11">System for Automatic Bug Detection in Code and Programs Using ...</a></li>

</ul>
</details>

**社区讨论**: 评论指出 FFmpeg 的安全记录异常糟糕，且鉴于多年的模糊测试，这些发现并不令人意外。有人认为行业更倾向于生成错误报告而非修复问题，并提出自动化的拉取请求接受率更高。另一些人批评安全研究的激励结构，称其为志愿者带来了负担。

**标签**: `#security`, `#ffmpeg`, `#zero-day`, `#vulnerability`, `#multimedia`

---

<a id="item-3"></a>
## [中国 RNA 编辑技术 LEAPER 首次用于 DMD 人体治疗](https://www.ithome.com/0/963/933.htm) ⭐️ 9.0/10

北京大学魏文胜教授领衔的团队于 2026 年 6 月 10 日在《细胞》杂志上发表两项研究成果，显示其 RNA 编辑技术 LEAPER 已在全球首次应用于杜氏肌营养不良症（DMD）的临床治疗，并取得积极疗效信号。 这标志着全球首次将 RNA 编辑策略应用于杜氏肌营养不良症（一种尚无治愈方法的严重罕见病）的临床治疗，并证明我国原创 RNA 编辑技术能在患者中实现治疗效果，通过跳跃不同外显子有望覆盖约 80%的 DMD 患者。 LEAPER 技术通过 AAV 载体递送工程化环状 RNA（circ-arRNA），招募内源 ADAR 酶实现外显子跳跃，在三名接受治疗的 DMD 患儿中，一年随访后肌营养不良蛋白表达恢复，运动功能改善，且未观察到严重不良事件。

rss · IT HOME · 6月13日 11:31

**背景**: DMD 是一种由 DMD 基因突变引起的严重遗传性肌肉疾病，该基因是人体最大的蛋白编码基因。传统基因疗法因基因庞大、突变类型众多而面临挑战。RNA 编辑修改的是 RNA 而非 DNA，避免永久性基因组改变，并通过使用内源编辑机制降低免疫原性风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://biopic.pku.edu.cn/xwzx/zycghz1/511062.htm">新型 RNA 单碱基编辑技术 LEAPER - BIOPIC网站中文版</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC10591355/">Utilizing AAV-mediated LEAPER 2.0 for programmable RNA editing in non-human primates and nonsense mutation correction in humanized Hurler syndrome mice - PMC</a></li>

</ul>
</details>

**标签**: `#RNA editing`, `#gene therapy`, `#DMD`, `#clinical trial`, `#biotechnology`

---

<a id="item-4"></a>
## [vLLM v0.23.0 发布：深度优化 DeepSeek-V4 并扩展 Model Runner V2](https://github.com/vllm-project/vllm/releases/tag/v0.23.0) ⭐️ 8.0/10

vLLM v0.23.0 是一个重要版本，包含了来自 200 位贡献者的 408 次提交，主要特性包括对 DeepSeek-V4 的广泛优化、Model Runner V2 扩展到 Llama 和 Mistral 模型、Rust 前端的更新以及对新模型的支持。 此次发布显著提升了 DeepSeek-V4 及其他模型的推理性能，并吸引了更广泛的社区参与，使 vLLM 在生产环境中部署大语言模型时更加高效和灵活。 DeepSeek-V4 的稀疏 MLA 元数据与 V3.2 解耦，新增了 TRTLLM-gen 注意力内核以及针对 Mega-MoE 的 EPLB 支持。Model Runner V2 现已成为 Llama 和 Mistral 模型的默认运行器，集成了 FlashInfer 采样器和可中断 CUDA 图。

github · khluu · 6月12日 23:29

**背景**: vLLM 是一个开源的高吞吐量 LLM 推理库，支持多种模型。Model Runner V2 是一种较新的推理引擎，可提升稠密模型的性能。DeepSeek-V4 采用了多头潜在注意力（MLA）和混合专家（MoE）架构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/latest/api/vllm/v1/attention/backends/mla/flashmla_sparse/">vllm.v1.attention.backends.mla.flashmla_sparse</a></li>
<li><a href="https://deepwiki.com/NVIDIA/TensorRT-LLM/9.2-trtllm-attention-backend">TRTLLM Attention Backend | NVIDIA/TensorRT-LLM | DeepWiki</a></li>

</ul>
</details>

**标签**: `#vllm`, `#release`, `#LLM inference`, `#DeepSeek`, `#optimization`

---

<a id="item-5"></a>
## [CRISPR-Cas12a2 选择性粉碎癌细胞](https://innovativegenomics.org/news/crispr-technique-selectively-shreds-cancer-cells/) ⭐️ 8.0/10

研究人员展示了一种利用 Cas12a2 酶的新型 CRISPR 技术，通过检测肿瘤特异性突变，选择性摧毁癌细胞，包括之前被认为是'不可成药'的癌症。 这种方法为治疗对传统药物耐药的癌症提供了潜在新途径，扩展了基因编辑在肿瘤学中的应用前景。 与早期基于 Cas9 的方法仅在目标位点损伤 DNA 不同，Cas12a2 在激活后粉碎整个染色质，导致更彻底的细胞死亡。该技术在一篇 Nature 论文和 bioRxiv 预印本中有描述。

hackernews · gmays · 6月12日 15:15 · [社区讨论](https://news.ycombinator.com/item?id=48505231)

**背景**: CRISPR-Cas 系统是细菌中的适应性免疫机制，利用引导 RNA 靶向并切割外来 DNA。Cas12a2 是最近被鉴定的酶，在识别目标 DNA 序列后触发细胞染色质的破坏，从而杀死宿主细胞。'不可成药'癌症指的是由结构或功能上难以用传统小分子药物靶向的蛋白质驱动的癌症。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cas12a">Cas12a - Wikipedia</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC5945194/">Drugging the ‘ undruggable ’ cancer targets - PMC</a></li>

</ul>
</details>

**社区讨论**: 社区评论反应不一。一些用户对治疗遗传疾病抱有希望并称赞技术进展，而另一些人提醒肿瘤可能会进化出耐药性。一位评论者认为与病毒载体疗法相比，CRISPR 被过度炒作，后者已有更多获批疗法。

**标签**: `#CRISPR`, `#cancer`, `#gene editing`, `#Cas12a2`, `#biotechnology`

---

<a id="item-6"></a>
## [开源 AI 必须获胜以防止中心化](https://opensourceaimustwin.com/?share=v2) ⭐️ 8.0/10

一篇高分倡议文章认为，开源 AI 必须战胜专有系统，以防止中心化和审查，社区成员强调需要分布式推理和训练框架。 这场辩论很重要，因为它决定了 AI 开发是保持人人可用，还是被少数大公司控制，可能影响创新、自由和全球力量格局。 关键挑战包括单独运行最先进模型的成本过高、分布式训练中的通信速度慢，以及来自不可信节点的数据投毒风险；一些社区成员提出了自愈检查点回滚系统来解决后者。

hackernews · vednig · 6月13日 02:14 · [社区讨论](https://news.ycombinator.com/item?id=48511908)

**背景**: 最先进的 AI 模型需要巨大的计算资源，使得其开发和部署只有大公司才能实现。开源 AI 通常指的是开放模型权重，但训练仍然是中心化的。去中心化推理网络和分布式训练框架正在兴起以解决这些限制，尽管它们面临重大的技术障碍。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/dragonfly-research/dont-trust-verify-an-overview-of-decentralized-inference-c471a9f7a586">Don’t Trust, Verify: An Overview of Decentralized Inference | Medium</a></li>
<li><a href="https://spectrum.ieee.org/decentralized-ai-training-2676670858">Decentralized AI Training Turns Homes Into Data Hubs - IEEE Spectrum</a></li>
<li><a href="https://www.primeintellect.ai/blog/our-approach-to-decentralized-training">State-of-the-art in Decentralized Training</a></li>

</ul>
</details>

**社区讨论**: 社区情绪强烈支持开源 AI，许多人表示愿意贡献资源。关键讨论围绕去中心化推理和训练的技术可行性展开，一些人提出了自愈检查点等新颖解决方案。人们也认识到开放权重并不等同于完全开源，但认为这是必要的一步。

**标签**: `#open source`, `#AI`, `#decentralization`, `#LLM`, `#community discussion`

---

<a id="item-7"></a>
## [Apple 将 TrueType 微调解释器迁移至 Swift](https://www.swift.org/blog/migrating-truetype-hinting-to-swift/) ⭐️ 8.0/10

Apple 用 Swift 重写了 TrueType 微调解释器，替换了原有的 C 语言实现，通过内存安全提高安全性。 这展示了 Swift 在低级系统编程中的可行性，特别是在字体渲染等安全关键组件中，并可能启发类似的重写以减少操作系统中的内存漏洞。 TrueType 微调解释器处理不可信字体数据，构成安全攻击面；Apple 在 GitHub 上发布了 Swift 代码作为参考，执行迁移的团队正在招聘类似的系统工作职位。

hackernews · DASD · 6月12日 19:54 · [社区讨论](https://news.ycombinator.com/item?id=48508726)

**背景**: TrueType 微调使用嵌入在字体中的字节码指令来调整字形轮廓以适应光栅显示。传统上用 C 语言编写的解释器容易发生缓冲区溢出等内存错误。用内存安全的 Swift 重写可以消除整类漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Font_hinting">Font hinting - Wikipedia</a></li>
<li><a href="https://www.swift.org/blog/migrating-truetype-hinting-to-swift/">Swift at Apple: Migrating the TrueType Hinting Interpreter | Swift.org</a></li>
<li><a href="https://github.com/apple/truetype-hinting-interpreter-example">GitHub - apple/ truetype - hinting - interpreter -example: Swift TrueType ...</a></li>

</ul>
</details>

**社区讨论**: 博客文章公告中包含该团队的招聘信息，指出不要求掌握 Swift。评论者讨论了惰性 map/filter 和生命周期功能的编译器限制，一位用户报告了崩溃，表明解释器使用了特性的一个狭窄子集。另一条评论强调了 Swift 在 macOS 上的更广泛采用。

**标签**: `#Swift`, `#TrueType`, `#security`, `#systems programming`, `#Apple`

---

<a id="item-8"></a>
## [华为 1B 参数 SpaceMind 模型登顶空间智能基准](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247897320&idx=3&sn=07784c5d298edcd85f0796f1ddcca265) ⭐️ 8.0/10

华为的 1B 参数纯 RGB 视觉语言模型 SpaceMind 在空间智能榜单上以 70.6 分刷新了李飞飞团队保持的纪录。 这一成就表明，紧凑型模型也能在空间推理领域达到顶尖水平，推动了具身 AI 研究，并使空间智能更易于应用于实际场景。 SpaceMind 仅使用视觉输入（RGB），无需深度或激光雷达数据，且其 1B 参数量远小于典型大模型，却在多图像空间推理上表现更优。

rss · 量子位 · 6月13日 07:55

**背景**: 空间智能是指理解和推理三维环境中空间关系的能力，对机器人、自动驾驶和 AR/VR 至关重要。SITE 和 MMSI-Bench 等基准测试评估多模态模型在多个图像上的物体定位和导航等任务。之前的顶尖模型体积更大或依赖额外传感器数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2511.23075v1">SpaceMind : Camera-Guided Modality Fusion for Spatial Reasoning in...</a></li>
<li><a href="https://wenqi-wang20.github.io/SITE-Bench.github.io/">SITE: towards Spatial Intelligence Thorough Evaluation</a></li>

</ul>
</details>

**标签**: `#spatial intelligence`, `#visual language model`, `#benchmark`, `#Huawei`, `#AI research`

---

<a id="item-9"></a>
## [欧洲初创公司 SOLiTHOR 实现 465 Wh/kg 固态电池演示电芯](https://www.ithome.com/0/963/944.htm) ⭐️ 8.0/10

比利时初创公司 SOLiTHOR 宣布了一款 10Ah 固态电池演示电芯，堆叠能量密度达到 465 Wh/kg 和 1400 Wh/L，采用其专有的溶胶-凝胶复合电解质，完全无需液态电解质。 这一进展展示了高能量密度固态电池可大规模量产的可行路径，有望降低制造成本并提升安全性，适用于航空航天、国防和电动出行等领域。 该电芯实现 8 mAh/cm² 的面容量，支持最高 5C 持续放电且容量损失极小，并在 100% 荷电状态下通过过充和针刺测试，无烟雾或起火。该工艺兼容卷对卷制造，并将化成与老化时间缩短三分之二。

rss · IT HOME · 6月13日 12:41

**背景**: 固态电池用固态离子导体替代液态电解质，提供更高的能量密度和更好的安全性。溶胶-凝胶化学是一种湿化学工艺，从小分子生成固体材料，可实现均匀涂层和复合材料。卷对卷制造允许在柔性基板上连续生产电池电极，降低成本。化成和老化是电池制造中耗时且稳定电池性能的步骤。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.researchgate.net/publication/313804818_Sol-Gel_Processed_Cathode_Materials_for_Lithium-Ion_Batteries">Sol-Gel Processed Cathode Materials for Lithium-Ion Batteries | Request PDF</a></li>
<li><a href="https://www.infinitypv.com/roll-to-roll-academy/roll-to-roll-manufacturing-of-batteries-a-revolution-in-energy-storage">Roll-to-Roll Battery Manufacturing: Revolutionizing Energy ...</a></li>
<li><a href="https://www.batterydesign.net/manufacture/cell-manufacturing/battery-cell-manufacturing-process/formation-aging/">Formation & Aging - Battery Design</a></li>

</ul>
</details>

**标签**: `#solid-state battery`, `#energy storage`, `#battery technology`, `#startup`

---

<a id="item-10"></a>
## [AUR 供应链攻击投毒超 400 软件包](https://www.ithome.com/0/963/905.htm) ⭐️ 8.0/10

攻击者通过注入恶意构建脚本，对 Arch 用户仓库（AUR）中超过 400 个被遗弃的软件包进行了投毒，这些脚本会部署一个基于 Rust 的二进制程序，窃取浏览器数据、SSH 密钥和凭证，并在获得 root 权限的系统上安装 eBPF rootkit。 这是一起针对 Arch Linux 社区的严重供应链攻击，可能导致大量用户的敏感开发者信息泄露。该事件凸显了 AUR 等社区维护仓库固有的安全风险，这些仓库依赖对软件包维护者的信任。 攻击者未更改软件包名称或版本历史，仅修改了 PKGBUILD 构建脚本以下载名为'atomic-lockfile'的恶意 npm 包。该恶意软件会从 Chrome、Edge 等浏览器窃取 Cookie、Token 和会话数据，盗取 SSH 密钥、GitHub 凭证和 OpenAI/ChatGPT Bearer Token，并将它们上传至 temp.sh；若获得 root 权限，则会加载 eBPF rootkit 以隐藏自身。

rss · IT HOME · 6月13日 09:46

**背景**: Arch 用户仓库（AUR）是一个社区驱动的仓库，包含用于编译和安装官方仓库中未包含的软件包的 PKGBUILD 脚本。任何用户都可以上传软件包，并由可信用户审查，但过程并非万无一失。eBPF 是一种允许沙盒程序在 Linux 内核中运行的技术，而 eBPF rootkit 利用它来隐藏恶意活动并持久化运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aur.archlinux.org/">AUR (en) - Home</a></li>
<li><a href="https://github.com/Gui774ume/ebpfkit">GitHub - Gui774ume/ebpfkit: ebpfkit is a rootkit powered by eBPF</a></li>

</ul>
</details>

**标签**: `#Security`, `#Supply Chain Attack`, `#Malware`, `#Arch Linux`, `#AUR`

---

<a id="item-11"></a>
## [谷歌 Android 安全主管因军事 AI 合作辞职](https://www.ithome.com/0/963/888.htm) ⭐️ 8.0/10

谷歌 Android 安全负责人 René Mayrhofer 于 2025 年 5 月辞职，原因是反对公司与美国国防部的合作以及取消 AI 武器禁令，他认为谷歌已丧失道德指针。 此次辞职凸显了谷歌内部对其从“不作恶”信条转向军事 AI 合作日益增长的不满，可能影响员工士气及公众对公司 AI 伦理的信任。 Mayrhofer 的告别信指出，谷歌管理层“悄悄放弃”碳中和目标，并与“战争部”签署协议，将 AI 用于可能违反国际法的行动。他还担心这可能针对公民进行大规模监控。

rss · IT HOME · 6月13日 08:40

**背景**: 谷歌在 2018 年因员工抗议“天网计划”而制定了 AI 原则，承诺不将 AI 用于武器或监控。2025 年 2 月，谷歌更新了这些原则，删除了武器和监控禁令，此举遭到人权组织批评。这一政策变化使得触发 Mayrhofer 辞职的军事合同成为可能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2025/02/04/google-removes-pledge-to-not-use-ai-for-weapons-surveillance.html">Google removes pledge to not use AI for weapons, surveillance</a></li>
<li><a href="https://www.amnesty.org/en/latest/news/2025/02/global-googles-shameful-decision-to-reverse-its-ban-on-ai-for-weapons-and-surveillance-is-a-blow-for-human-rights/">Global: Google’s shameful decision to reverse its ban on AI ...</a></li>
<li><a href="https://ai.google/principles/">AI Principles — Google AI</a></li>

</ul>
</details>

**标签**: `#ethics`, `#Google`, `#AI`, `#military`, `#corporate governance`

---

<a id="item-12"></a>
## [Linux 7.2 将自动创建多尺寸透明大页](https://lwn.net/Articles/1077208/) ⭐️ 8.0/10

Nico Pache 为 Linux 7.2 提交了一个补丁系列，增加了自动创建多尺寸透明大页（mTHP）的功能，使大页的使用更加透明和灵活。 这一增强功能改进了内存管理性能，允许内核自动选择最合适的大页大小，从而降低开销并提高各种工作负载的效率。 该特性与现有的 mTHP 基础设施集成，支持传统 PMD 大小（2MB）大页之外的多种大页大小，例如在具有较大基础页大小的系统上支持 64KB、128KB 和 512KB。

rss · LWN.net · 6月11日 14:33

**背景**: Linux 内核长期以来使用透明大页来通过减少 TLB 未命中来提升性能。传统大页受限于硬件支持的大小，如 2MB 和 1GB。多尺寸透明大页（mTHP）被引入以提供软件定义的中间大小，在基础页和大页之间取得平衡。这种自动创建特性进一步简化了其使用，无需手动配置。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lwn.net/Articles/1009039/">Multi - size THP creation, two different ways [LWN.net]</a></li>
<li><a href="https://lwn.net/Articles/1070900/">mm: thp: always enable mTHP support [LWN.net]</a></li>
<li><a href="https://docs.kernel.org/admin-guide/mm/transhuge.html">Transparent Hugepage Support — The Linux Kernel documentation</a></li>

</ul>
</details>

**标签**: `#linux`, `#kernel`, `#memory-management`, `#huge-pages`

---

<a id="item-13"></a>
## [GitHub 利用 LLM 推理减少密钥扫描误报](https://github.blog/security/making-secret-scanning-more-trustworthy-reducing-false-positives-at-scale/) ⭐️ 8.0/10

GitHub 宣布为其密钥扫描功能新增了一个验证步骤，利用上下文感知的 LLM 推理来大规模减少误报。这一改进使警报对开发者更可信、更可操作。 密钥扫描中的误报会浪费开发者时间并削弱对自动化警报的信任。通过集成 LLM 推理，GitHub 大幅降低噪音，实现更快速、更准确的真实凭据泄露检测，这对大规模安全至关重要。 该方法改编自 Agentic Secret Finder 工具的验证方式，在上下文中检查潜在密钥，而非仅依赖模式匹配。这种上下文感知推理有助于区分生产密钥、测试密钥和示例值。

rss · GitHub Blog · 6月11日 16:00

**背景**: 密钥扫描自动检测代码仓库中暴露的凭据，如 API 密钥和令牌。传统上，它依赖正则表达式模式，可能产生大量误报——看似密钥实则无害的警报。GitHub 的改进增加了一个 LLM 推理步骤，分析周围代码上下文，从而减少这些误报。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.blog/security/making-secret-scanning-more-trustworthy-reducing-false-positives-at-scale/">Making secret scanning more trustworthy: Reducing false ...</a></li>
<li><a href="https://letsdatascience.com/news/github-improves-secret-scanning-verification-with-llm-reason-f7cade8e">GitHub improves secret scanning verification with LLM reasoning</a></li>

</ul>
</details>

**标签**: `#security`, `#secret-scanning`, `#LLM`, `#false-positives`, `#GitHub`

---

<a id="item-14"></a>
## [教皇 AI 信函指出治理失败，顾问如此主张](https://www.nature.com/articles/d41586-026-01876-z) ⭐️ 8.0/10

梵蒂冈和联合国的一位顾问在《自然》杂志的评论中表示，教皇方济各关于人工智能的信函应被解读为对人工智能治理失败的诊断，而不仅仅是神学声明。 这一观点架起了宗教界与科学界的桥梁，强调人工智能中的伦理与治理挑战需要跨学科关注。它可能影响联合国和梵蒂冈的政策讨论，进而塑造全球人工智能监管。 该评论由一位与梵蒂冈和联合国均有合作的知名人工智能顾问撰写，增强了论点分量。信函本身超越神学，对当前人工智能治理结构提出批评。

rss · Nature · 6月12日 00:00

**背景**: 教皇方济各持续就人工智能的伦理影响发声，发布信函和声明，呼吁全球团结与监管。梵蒂冈曾召集人工智能伦理讨论，包括 2020 年的《罗马人工智能伦理倡议》。人工智能治理是一个涉及伦理、法律和技术的复杂领域，许多人呼吁建立国际框架。

**标签**: `#AI governance`, `#ethics`, `#policy`, `#Vatican`, `#UN`

---

<a id="item-15"></a>
## [学生耿引爆中国科研诚信丑闻](https://www.nature.com/articles/d41586-026-01902-0) ⭐️ 8.0/10

一名被称为“Student Geng”的视频博主指控多篇发表在 Nature 期刊上的论文存在数据操纵，矛头直指资深学者，引发中国机构迅速调查。 这起丑闻凸显了中国科研诚信的持续问题以及举报人面临的挑战，可能削弱对顶级期刊的信任并推动更严格的监管。 指控涉及多位资深学者合著的多篇论文存在数据操纵，中国机构的快速反应表明这些指控正被严肃对待。

rss · Nature · 6月12日 00:00

**背景**: 科研诚信指在科学研究中遵守诚实和道德规范，包括正确处理和报告数据。初级研究人员举报资深学者在中国并不常见，因此本案格外引人注目且影响深远。

**标签**: `#research integrity`, `#data manipulation`, `#whistleblowing`, `#China`, `#scientific misconduct`

---

<a id="item-16"></a>
## [人类在严格数学测试中超越 AI](https://www.nature.com/articles/d41586-026-01888-9) ⭐️ 8.0/10

《自然》杂志发表的新基准测试表明，即使是最先进的 AI 系统，在以前未见过的严格数学问题上也无法达到顶尖人类数学家的水平。 这凸显了当前 AI 在数学推理方面的具体局限性，表明在复杂的、新颖的问题解决中，人类专业知识仍占主导地位。 该基准测试由 AI 和人类都未见过的题目组成，确保在没有训练数据污染的情况下公平比较推理能力。

rss · Nature · 6月12日 00:00

**背景**: 数学推理是机器智能的关键测试。许多 AI 基准测试已趋于饱和，但此次测试使用未见过的题目来衡量真正的泛化能力。结果显示，顶尖人类数学家仍在具有挑战性的新证明上优于 AI。

**标签**: `#AI`, `#mathematics`, `#benchmark`, `#reasoning`, `#human vs AI`

---

<a id="item-17"></a>
## [激光相位板提升冷冻电镜蛋白质结构成像质量](https://www.nature.com/articles/d41586-026-01858-1) ⭐️ 8.0/10

两个研究团队开发了“激光相位板”系统，显著提升了冷冻电子显微镜在测定蛋白质结构时的图像质量，该成果于 2026 年 6 月 12 日发表在《自然》杂志上。 这一突破可使冷冻电镜观察到超过 50%的细胞蛋白，加速结构生物学和药物发现，使以前难以可视化的蛋白质得以高分辨率成像。 激光相位板利用聚焦激光束在电子束中产生相移，增强生物样品的对比度而不损失分辨率，解决了传统相位板的关键局限。

rss · Nature · 6月12日 00:00

**背景**: 冷冻电子显微镜（cryo-EM）是一种通过快速冷冻样品以保持其天然状态，然后利用电子束生成生物分子三维结构的技术。然而，许多蛋白质对比度不足，使其可视化困难。激光相位板通过无物理障碍地操控电子束的相位来提高对比度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cryogenic_electron_microscopy">Cryogenic electron microscopy - Wikipedia</a></li>
<li><a href="https://biohub.org/blog/laser-phase-plate-cryo-em-making-invisible-visible/">Making the invisible visible – laser phase plate cryo-EM</a></li>

</ul>
</details>

**标签**: `#cryo-EM`, `#protein structures`, `#structural biology`, `#laser phase plate`, `#biotechnology`

---

<a id="item-18"></a>
## [SGLang v0.5.13 发布，新增模型支持并默认启用 Spec V2](https://github.com/sgl-project/sglang/releases/tag/v0.5.13) ⭐️ 7.0/10

SGLang v0.5.13 新增了多个自回归模型（Nemotron 3 Ultra、Step-3.7-Flash、Command A+）和扩散模型（Cosmos3、LingBot-World、SANA-WM、Ernie-Image、FLUX.2-Klein、Ideogram 4）的支持，并将 Spec V2 设为默认推测解码路径，弃用 Spec V1，将 EAGLE/MTP 统一到 V2 工作器中。 此版本为 Nemotron 3 Ultra 和 Step-3.7-Flash 等知名模型提供了第零天支持，可立即部署。将 Spec V2 设为默认，通过树状草稿和统一推测解码降低延迟，提升了生产环境中 LLM 推理的效率。 Spec V2 支持在 triton、FlashAttention3、MLA 和 aiter 后端上使用 topk > 1 的树状草稿，并兼容 page_size > 1 以及 Mamba/混合线性模型。此版本还通过 FutureMap 降低了每步调度器开销，扩展了分段/可中断 CUDA 图覆盖范围，并使用新的 FlashInfer 内核加快了 Qwen 3.5 在 Blackwell GPU 上的运行。

github · Fridge003 · 6月13日 00:17

**背景**: SGLang 是一个用于高性能服务大语言模型和多模态模型的开源框架。推测解码是一种推理优化技术，通过一个较小的草稿模型预测多个 token，再由较大的目标模型并行验证，从而在不牺牲输出质量的情况下降低延迟。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference/">An Introduction to Speculative Decoding for Reducing Latency ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/SGLang">SGLang - Wikipedia</a></li>
<li><a href="https://github.com/sgl-project/sglang">GitHub - sgl-project/sglang: SGLang is a high-performance ...</a></li>

</ul>
</details>

**标签**: `#SGLang`, `#LLM inference`, `#speculative decoding`, `#model support`

---

<a id="item-19"></a>
## [资深 Mozilla 成员离职，批评官僚化转型](https://blog.unitedheroes.net/5751) ⭐️ 7.0/10

一位长期在 Mozilla 担任志愿者和员工的人士发布了题为《离开 Mozilla》的博文，详述其离职原因，包括官僚主义惯性、使命偏移和社区关注度的丧失。 这篇反思在开源社区引发共鸣，凸显了组织扩张与维持草根志愿者文化之间的张力——对于像 Firefox 这样依赖社区信任的项目至关重要。 该博文在聚合平台上获得高关注（334 分，187 条评论），评论者讨论了 Mozilla 强制推出的 AI 功能，并引用 Pournelle 的官僚铁律来解释该组织的退化。

hackernews · martey · 6月13日 05:57 · [社区讨论](https://news.ycombinator.com/item?id=48513806)

**背景**: Mozilla 是 Firefox 背后的非营利基金会。Firefox 曾一度占据浏览器市场主导地位，但后来被 Chrome 超越。Mozilla 高度依赖致力于开放互联网使命的志愿者和员工。近年来，部分用户批评 Mozilla 引入不必要的 AI 功能，并热衷副项目而忽视浏览器本身。

**社区讨论**: 评论者观点多元：klez 回忆了积极的志愿者经历但最终感到失望；magpi3 引用 Pournelle 的官僚铁律解释目标偏移；red_admiral 谴责强制 AI 设置违背 Firefox 价值观；matsenmann 则警告不要简单归咎于领导层，认为多元化探索或许是生存所需。

**标签**: `#Mozilla`, `#organizational culture`, `#browser`, `#bureaucracy`, `#open source`

---

<a id="item-20"></a>
## [雷诺的无稀土电机：旧技术的新推动](https://www.renaultgroup.com/en/magazine/energy-and-powertrains/all-about-electric-motors-with-no-rare-earths/) ⭐️ 7.0/10

雷诺宣布推动开发不依赖稀土元素的电机，特别强调电励磁同步电机（EESM）作为一种替代方案。 减少对稀土的依赖可以缓解供应链脆弱性和地缘政治风险，因为中国主导稀土生产。但该技术并非新创，且与永磁电机相比存在效率或功率密度较低等已知权衡。 雷诺的 EESM 电机通过电流在转子中产生磁场，而非永磁体，从而消除稀土。但它们需要旋转变压器或滑环为转子供电，这增加了复杂性和维护需求。

hackernews · bestouff · 6月12日 22:08 · [社区讨论](https://news.ycombinator.com/item?id=48510010)

**背景**: 大多数现代电动汽车电机使用含有钕等稀土元素的永磁体，这些元素价格昂贵且地缘政治敏感。无稀土替代方案，如 EESM 或开关磁阻电机，已存在一个多世纪，但由于性能较低或可靠性问题未被采用。近期的供应链担忧重新激起了对这些旧技术的兴趣。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.spglobal.com/automotive-insights/en/blogs/2025/11/eliminating-rare-earth-elements-from-ev-motor-supply-chain">Eliminating rare earth elements from EV motor supply chains</a></li>
<li><a href="https://emag.directindustry.com/2026/02/04/rare-earth-free-motors-ev-supply-chain-oem/">How Rare-Earth-Free Motors Are Redefining the EV Supply Chain</a></li>

</ul>
</details>

**社区讨论**: 社区评论指出雷诺的标题具有误导性，因为绕线转子电机已有一个多世纪的历史。用户指出传统的 EESM 需要电刷，会磨损，而无刷版本需要复杂的旋转变压器。宝马的无稀土电机被认为更先进，提供更高功率（300kW 对比 160kW）和 800V 架构。

**标签**: `#electric motors`, `#rare earths`, `#EV technology`, `#automotive engineering`, `#Hacker News discussion`

---