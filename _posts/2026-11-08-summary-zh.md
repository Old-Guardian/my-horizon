---
layout: default
title: "Horizon Summary: 2026-11-08 (ZH)"
date: 2026-11-08
lang: zh
---

> 从 128 条内容中筛选出 18 条重要资讯。

---

1. [Apiiro 发现 1,122 个 GitHub 公开文件通过 Claude Code 设置泄露凭据](#item-1) ⭐️ 8.0/10
2. [上海交大 AutoDNA AI 原生实验室实现自主分子生物学实验，成果登上《自然》](#item-2) ⭐️ 8.0/10
3. [美团详解「不能出错」的分布式存储系统中如何使用 AI Coding](#item-3) ⭐️ 8.0/10
4. [高盛据报撤销银行家与交易员的 Claude Code 访问权限](#item-4) ⭐️ 7.0/10
5. [Cloudflare 开源 security-audit-skill，让编码智能体化身安全审计员](#item-5) ⭐️ 7.0/10
6. [谷歌发布面向谷歌云及自家产品的官方 Agent Skills 仓库](#item-6) ⭐️ 7.0/10
7. [Anthropic 开源 Claude Agent Skills 仓库，并指向跨厂商技能标准](#item-7) ⭐️ 7.0/10
8. [NVIDIA 开源 NVKE：面向裸金属 GPU 集群的 Kubernetes 管理平面](#item-8) ⭐️ 7.0/10
9. [Anthropic 被曝 34 亿美元购入 1.7GW 燃气发电机组，创 AI 公司最大电力设备订单](#item-9) ⭐️ 7.0/10
10. [SpaceX 星舰第 15 次试飞将首次尝试完整返回发射场回收](#item-10) ⭐️ 7.0/10
11. [反对数据中心浪潮席卷欧洲多国，抗议活动接连爆发](#item-11) ⭐️ 7.0/10
12. [美国司法部起诉三名男子，利用 AI 深度伪造高管身份诈骗逾 1.29 亿美元](#item-12) ⭐️ 7.0/10
13. [Asahi Linux 将全部仓库从 MIT 许可证改为 GPLv2 及以后版本](#item-13) ⭐️ 7.0/10
14. [Amutable OS 亮相：无 Shell、无 SSH、无解释器的镜像式 Linux](#item-14) ⭐️ 7.0/10
15. [美团发布 LongCat-2.5：1.6 万亿参数原生多模态智能体模型](#item-15) ⭐️ 7.0/10
16. [美团 MTFM：一个基座大模型统一外卖多业务精排](#item-16) ⭐️ 7.0/10
17. [美团搜索 3.0：将 LLM 语义表征应用于排序模型](#item-17) ⭐️ 7.0/10
18. [美团盘点 KDD 2026 八篇入选论文及 KDD Cup DataAgents 赛道夺冠方案](#item-18) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Apiiro 发现 1,122 个 GitHub 公开文件通过 Claude Code 设置泄露凭据](https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again) ⭐️ 8.0/10

安全公司 Apiiro 扫描了 GitHub 上的公开仓库，报告发现 1,122 个文件中存在泄露的凭据，这些凭据位于被提交到仓库的 .claude/settings.local.json 文件里——该本地文件正是 Claude Code 记录用户点击“不再询问”（don't ask again）后所批准命令的地方。这一发现促使 Claude Code 团队公开回应，称其过去并未进行密钥擦除（secret scrubbing），但正在研究防止此类泄露的办法。 它为一个所有采用智能体编程工具的人都面临的普遍风险给出了具体数字：权限白名单会原样持久化保存完整命令字符串，于是一次图方便的操作就可能把令牌固化进文件，日后被公开推送出去。随着 AI 编程智能体在团队和 CI 中快速普及，这已从个别开发者的失误演变为董事会层面关注的供应链与密钥卫生问题。 标题在因果上有所夸大：真正泄露需要同时满足两个条件——把本地设置文件提交到仓库，以及在已批准的命令中直接写入明文密钥；而 Claude Code 在自己创建 .claude/settings.local.json 时会自动将其加入 .gitignore，因此受影响文件多为手动创建或修改的。可行的修复手段也很具体：通过环境变量而非内联值传递密钥，并把 .claude/ 加入机器级的全局 gitignore 而不是仓库内。

hackernews · shmulc · 11月7日 20:45 · [社区讨论](https://news.ycombinator.com/item?id=50407882)

**背景**: Claude Code 是 Anthropic 推出的终端编程智能体，在执行 shell 命令或修改文件前会向用户请求授权。选择“是，不再询问”会把该规则（包含完整命令字符串）写入仓库根目录的 .claude/settings.local.json，并在该仓库未来的每次会话中生效。该文件明确设计为仅保留在本地、不应纳入版本控制，但当用户手动创建时很容易被误提交。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://code.claude.com/docs/en/settings-reference">Claude Code settings reference - Claude Code Docs</a></li>
<li><a href="https://dev.to/ottoflightrules/claude-code-permissions-how-allow-ask-and-deny-actually-compose-3kme">Claude Code permissions : how allow , ask, and... - DEV Community</a></li>
<li><a href="https://yaw.sh/claude-code-in-production/claude-code-settings/">Claude Code settings . json : A Practical Reference (2026) - yaw</a></li>

</ul>
</details>

**社区讨论**: Claude Code 团队的 Boris 确认该文件本应只保留在本地，指出密钥擦除一直不是 Claude Code 的功能，并表示团队正在研究预防措施。Hacker News 上的讨论（533 分、381 条评论）总体认同问题存在，但反驳了标题的表述，认为单纯点击“不再询问”本身并不会暴露任何东西；其他人则分享了缓解方案，例如使用隔离的临时虚拟机配合 --dangerously-skip-permissions、限制权限的 API 代理，以及仅通过环境变量传递密钥。

**标签**: `#ai-agents`, `#security`, `#secrets-management`, `#claude-code`, `#developer-tools`

---

<a id="item-2"></a>
## [上海交大 AutoDNA AI 原生实验室实现自主分子生物学实验，成果登上《自然》](https://www.ithome.com/1/024/001.htm) ⭐️ 8.0/10

上海交通大学计算机学院 IPADS 实验室陈海波、王肇国团队与化学化工学院樊春海、王飞团队合作，构建了 AI 原生科学实验室 AutoDNA 装置（思源一号），可自主完成复杂分子生物学实验操作。该成果发表于《自然》（Nature）并获官网首页头条报道，已在核酸检测、酶促 DNA 合成、癌症检测以及端到端 DNA 存储等场景中完成验证。 现有 AI 自主科学实验室多为“外挂式”架构，由专家预先配置仪器、规定流程和优化规则，AI 只接入文献检索或数据分析等局部环节，难以应对流程复杂、仪器多样且对时序、环境稳定性和操作精度要求严苛的生物分子实验。AutoDNA 转向模型—实验—仪器协同设计与多智能体架构，贯通“设计—实验—优化”全过程，是迈向真正自主的 AI for Science 实验室的实质性一步。 AutoDNA 将复杂实验任务分解给文献检索、试剂选择、方案设计、代码生成、硬件执行、结果分析和迭代优化等专业智能体，并把各类仪器的能力提炼为带自然语言说明和统一代码接口的“原子服务”，从而屏蔽不同型号仪器的底层差异。平台将具备微米级定位和微升级液体处理能力的高精度自动化硬件与执行调度系统结合，负责任务的程序检查、仪器状态跟踪和资源分配，并集成了基于 OpenHarmony 操作系统的控制终端，可协同 25 台以上仪器。

rss · IT HOME · 11月8日 13:23

**背景**: 自驱动实验室（也称实验室自动化或自主实验平台）把机器人仪器与人工智能结合起来，使系统能够提出实验方案、在物理世界执行、读取结果并据此改进下一轮实验，几乎无需人工介入。分子生物学场景难度更高，因为实验流程涉及多种仪器、严格的时序和微升级液体处理，此前的系统大多只自动化单个环节而非完整流程。DNA 数据存储——把数字文件编码为 DNA、合成、保存、测序读取再解码——是检验这类平台的严苛基准，因为它要求一长串对误差高度敏感的生化操作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41586-026-11228-6">An AI-native experimental laboratory for autonomous ... - Nature</a></li>
<li><a href="https://ipads.sjtu.edu.cn/autodna/">AutoDNA — AI-Native Autonomous Laboratory</a></li>
<li><a href="https://arxiv.org/abs/2507.02379">[2507.02379] An AI-native experimental laboratory for ...</a></li>

</ul>
</details>

**标签**: `#AI for Science`, `#self-driving labs`, `#multi-agent systems`, `#lab automation`, `#molecular biology`

---

<a id="item-3"></a>
## [美团详解「不能出错」的分布式存储系统中如何使用 AI Coding](https://tech.meituan.com/2026/10/29/AI-Coding-IN-Distributed-Storage-System.html) ⭐️ 8.0/10

美团基础技术部发布了一篇工程实践报告，介绍其分布式存储系统中 AI 编程助手的落地方式，覆盖 AI 评审、问题排查和自动化开发三类场景。报告并未强调「写代码更快更多」，而是梳理了 AI 在哪些环节确实能帮上忙、在哪些地方容易出错，以及哪些关键节点必须由人来把关。 分布式存储属于「一个隐蔽 bug 就可能导致数据丢失或损坏」的领域，因此这份来自生产环境的信任边界校准，比笼统的「AI 提效」说法有价值得多。文中总结的验证优先的评审方式、明确的失效边界以及必须保留的人工签字环节，对其他要把编程智能体引入高可靠基础设施的团队具有直接复用价值。 报告按场景而非按工具来组织 AI 的使用方式，并强调价值在于让代码和结论经得起验证，而不是产出数量本身。它把人工评审定位为正确性关键变更的硬性关口，意味着在该领域中 AI 的输出被视为待校验的提案，而非可直接采信的答案。

rss · 美团 Blog · 11月8日 20:17

**背景**: 分布式存储系统通过副本和共识协议把数据分散在大量机器上，使单点故障不会破坏数据完整性；由于正确性要求极为严格，变更通常要经过大量评审并逐步灰度上线。代码补全、代码评审等 AI 编程助手已在软件团队中普及，但它们容易生成「看起来合理、逻辑却微妙错误」的内容，在这类系统中风险尤其高。本文介绍的正是一个大型基础设施团队如何在这样的环境下划定 AI 辅助与人类责任之间的界线。

**标签**: `#AI coding`, `#distributed storage`, `#reliability engineering`, `#human-in-the-loop`, `#code review`, `#production practices`

---

<a id="item-4"></a>
## [高盛据报撤销银行家与交易员的 Claude Code 访问权限](https://www.thestateofai.com/news/goldman-sachs-claude-code-traders-bankers) ⭐️ 7.0/10

据一份报道称，高盛已撤销其银行家和交易员对 Claude Code 的访问权限，此事在 Hacker News 上引发了热烈讨论（252 分、158 条评论）。社区成员指出，该限制似乎主要针对交易员这一群体——即拥有向市场发送订单和记录客户交易权限的员工——而非在全公司范围内禁用该工具。 这是一家大型受监管金融机构限制 AI 编程智能体的具体案例，为银行及其他高风险行业企业如何治理智能体工具树立了先例。它还凸显了影响企业 AI 落地的两股力量：智能体在拥有高权限的工作站上运行所带来的安全风险，以及不可预测的按量计费模式带来的账单摩擦。 原始报道内容较为单薄，讨论中也有不少推测成分，但评论者指出，即便只是针对交易员这一小范围的收回权限也意义重大，因为这些账户拥有发送订单和记录客户交易的权限。其他人则表示，按量计费的超额支出正促使自己所在的组织采取类似的收回措施，Anthropic 无法提供标准化的费率，而 Gemini 等竞争对手则提供固定价格并用限流代替意外账单。

hackernews · TheWiggles · 11月8日 18:16 · [社区讨论](https://news.ycombinator.com/item?id=50415628)

**背景**: Claude Code 是 Anthropic 推出的智能体编程工具，运行在终端和 IDE 中，能够读取代码库、编辑文件并在用户机器上执行命令。安全研究者用「致命三元组」（lethal trifecta）来描述 AI 智能体的风险组合：同时具备访问私有数据、接触不可信内容以及对外通信通道这三项条件——而这正是提示注入攻击（prompt injection）得以成立的土壤，攻击者把恶意指令藏在被抓取的内容中即可劫持智能体。一台拥有市场交易权限、可访问内部网络和电子邮件的交易员工作站恰好满足这一组合，因此在该环境中运行无人值守的智能体被认为格外危险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI coding agent and assistant</a></li>
<li><a href="https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/">The lethal trifecta for AI agents: private data, untrusted ...</a></li>
<li><a href="https://keito.ai/blog/ai-agent-costs-unpredictable-consumption/">Why AI Agent Costs Are Unpredictable: How to Control ...</a></li>

</ul>
</details>

**社区讨论**: 最主要的观点聚焦于安全：评论者认为，在同时掌握客户信息、交易数据、自营信息以及电子邮件和互联网访问权限的机器上运行半无人值守的编程智能体，会直接撞上「致命三元组」，实在太危险。另一些人则关注经济因素——长期超额账单正把团队推向 Gemini 这类固定费率的竞品；还有人关注时机问题，怀疑高盛并非主动切断交易员的访问权限，而是在发生运营损失之后才这么做，尤其是在据称由高盛牵头 Anthropic IPO 的背景下。

**标签**: `#ai-agents`, `#enterprise-ai`, `#ai-security`, `#prompt-injection`, `#ai-economics`

---

<a id="item-5"></a>
## [Cloudflare 开源 security-audit-skill，让编码智能体化身安全审计员](https://github.com/cloudflare/security-audit-skill) ⭐️ 7.0/10

Cloudflare 开源了 cloudflare/security-audit-skill，这是一个编码智能体技能，可驱动智能体完成六阶段安全审计：侦察、覆盖率驱动的漏洞狩猎、候选漏洞验证、结构化输出、独立记录复核以及目标无关的报告生成。该仓库正是 Cloudflare 在其《Build your own vulnerability harness》博客中所述的、后来扩展为全舰队漏洞发现平台的单仓库起点。 它把此前深藏于 Cloudflare 内部漏洞挖掘平台中的“对抗式、验证优先”审计方法论，封装成任何编码智能体都能加载的通用技能，显著降低了团队对自有代码库开展结构化漏洞发现的门槛。这也标志着 AI 代码审查正从一次性扫描，转向带有显式覆盖率账本与独立复核的多智能体流水线。 每个去重后的候选漏洞都会被交给一个全新的验证智能体，其任务是设法证伪该候选；结论被严格分为三类：confirmed（具备完整源码溯源且有边界的可观测结果）、needs_validation（存在某个确切未解决事实，但不评定严重级别）和 rejected（被证伪的候选）。结果写入 findings.json，并通过 validate-findings.cjs 与 validate-coverage-ledger.cjs 对照 report-schema.json 进行校验。对同一仓库的多次运行是增量叠加的，会复用既有账本与发现来定位空白区、复核变更过的源码；技能还附带覆盖内存安全/二进制/内核、AI 与 LLM 目标、Web 协议与认证、客户端问题等方向的攻击类别提示词模块。

rss · GitHub Trending - Daily · 11月8日 20:16

**背景**: 所谓“编码智能体技能”（coding-agent skill），是一套打包好的指令与配套文件，供 Claude Code 之类的编码智能体加载以获得某种专门工作流；在这里，它把通用编码智能体变成了安全审计员。Cloudflare 的漏洞发现平台将漏洞工作拆成两个相互独立的阶段——负责测绘与搜寻弱点的“发现平台”，以及负责去重、判断生产环境相关性并管理修复的“验证系统”——两个阶段往往使用不同的模型；而本次开源的技能正是这一架构的精简版单仓库前身。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/build-your-own-vulnerability-harness/">Build your own vulnerability harness | Cloudflare Blog</a></li>
<li><a href="https://github.com/cloudflare/security-audit-skill">GitHub - cloudflare/security-audit-skill: A coding-agent ...</a></li>
<li><a href="https://cldnavi.com/en/blog/cloudflare-security-audit-skill-2026/">Cloudflare's security-audit-skill (2026): Turning Your Coding ...</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#security auditing`, `#vulnerability discovery`, `#coding agents`, `#open source`

---

<a id="item-6"></a>
## [谷歌发布面向谷歌云及自家产品的官方 Agent Skills 仓库](https://github.com/google/skills) ⭐️ 7.0/10

谷歌发布了一个官方开源仓库 google/skills，其中包含面向谷歌产品与技术（包括谷歌云）的可安装 Agent Skills。开发者只需运行一条命令 `npx skills add google/skills` 即可安装，随后可选择具体技能、目标智能体以及项目级或全局的安装范围。 这标志着主流云厂商对开放的 Agent Skills 格式给予了背书，使技能从社区自发项目走向由厂商官方维护的一手内容，任何能够读取 SKILL.md 的智能体都能使用。它实际上把谷歌云的入门引导、IAM 认证、解决方案架构等指导内容转化为智能体可按需加载的机器可读包。 仓库列出的技能涵盖谷歌云入门、IAM 认证与授权、解决方案架构工作流，以及基于 Agent Gateway 的多智能体安全、AlloyDB 动态混合搜索、跨云智能体分析、基于 GKE 与 SQL 数据库的 RAG、将 AI 工作负载迁移至 GKE Inference 等场景。安装需要环境中有 Node.js/npx，`npx skills update` 命令可更新已安装技能，并可选择清理已废弃的技能。

rss · GitHub Trending - Daily · 11月8日 20:16

**背景**: Agent Skills 是一种用于扩展 AI 智能体能力的轻量开放格式：一个技能就是一个包含 SKILL.md 文件的文件夹，其中写明元数据与操作指令，也可以附带脚本、模板和参考资料，供智能体在需要时按需加载。来自 vercel-labs/skills 项目的 `npx skills` 命令行工具相当于这类技能的包管理器，一条命令即可把技能安装到 Claude Code、Cursor、Codex 等智能体中。谷歌的这个仓库通过 skills.sh 这一公开的技能发现与安装目录接入该生态。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://agentskills.io/home">Agent Skills Overview - Agent Skills</a></li>
<li><a href="https://github.com/vercel-labs/skills">GitHub - vercel-labs/skills: The open agent skills tool - npx ...</a></li>
<li><a href="https://www.skills.sh/docs/cli">CLI | Skills Documentation</a></li>

</ul>
</details>

**标签**: `#agents`, `#agent-skills`, `#google-cloud`, `#developer-tools`, `#open-source`

---

<a id="item-7"></a>
## [Anthropic 开源 Claude Agent Skills 仓库，并指向跨厂商技能标准](https://github.com/anthropics/skills) ⭐️ 7.0/10

Anthropic 公开发布了 GitHub 仓库 anthropics/skills，其中包含其 Claude「Agent Skills（智能体技能）」的实现——即以独立文件夹形式封装的指令、脚本和资源，Claude 可按需动态加载以完成特定任务。仓库内既有覆盖创意、技术和企业场景的示例技能，也包含 ./spec 目录下的 Agent Skills 规范、技能模板，以及以 Apache 2.0 协议开源的 docx、pdf、pptx、xlsx 文档技能（正是支撑 Claude 文档能力的底层实现）。 将生产环境中使用的文档技能作为参考代码开源，为开发者提供了打包程序性知识的具体范本，而非泛泛的指导，这对任何构建或评估智能体架构的人都有实际价值。仓库明确指向 agentskills.io，说明 Skills 正被定位为一种轻量、跨厂商的开放格式，与负责工具连接的 MCP 形成互补关系，而非替代。 每个技能存放在独立文件夹中，包含一个 SKILL.md 文件，用于承载指令与元数据（如名称和描述），并可附带脚本、模板等资源；该仓库还可以被注册为 Claude Code 的插件市场。Anthropic 明确声明这些技能仅用于演示与教学目的，提醒 Claude 实际表现可能与仓库中的实现存在差异，用于关键任务前务必自行充分测试。

rss · GitHub Trending - Daily · 11月8日 20:16

**背景**: Agent Skills 是 Anthropic 于 2025 年 10 月推出的扩展机制，无需微调即可增强 Claude 能力：技能不是把冗长的提示词或工具定义塞进上下文，而是一个文件夹，只有当任务相关时模型才会加载，因而更像按需调用的「程序性记忆」。这与 MCP（模型上下文协议）不同，后者标准化的是智能体如何连接外部工具和数据源，而非指令与工作流的打包方式。发布在 agentskills.io 的 Agent Skills 规范定义了最简的 SKILL.md 格式，使同一个技能文件夹原则上也能被 Claude 之外的其它智能体和编辑器复用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://agentskills.io/home">Agent Skills Overview - Agent Skills</a></li>
<li><a href="https://claude.com/resources/articles/skills">Introducing Agent Skills | Claude by Anthropic</a></li>
<li><a href="https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview">Agent Skills - Claude Platform Docs</a></li>

</ul>
</details>

**标签**: `#agents`, `#LLM tooling`, `#Anthropic`, `#open source`, `#standards`

---

<a id="item-8"></a>
## [NVIDIA 开源 NVKE：面向裸金属 GPU 集群的 Kubernetes 管理平面](https://github.com/dsx-ai-factory/nvke) ⭐️ 7.0/10

NVIDIA 在 GitHub 上以 Apache-2.0 协议开源了 NVKE（NVIDIA Kubernetes Engine），这是一个管理平面，平台团队可以把它安装在自己的裸金属 NVIDIA GPU 基础设施上，从而对外提供受管的 Kubernetes 服务。每个工作负载集群都拥有独立的 Kubernetes 控制平面、etcd 和节点池，NVKE 通过其 API 负责节点供给、扩缩容、Kubernetes 升级、节点替换和证书续期。该项目被明确标注为预览版（目前为 v0.24.0 候选发布版），NVIDIA 表示暂不建议用于生产环境。 这标志着 NVIDIA 从 GPU 驱动和设备插件层向上延伸到集群编排层本身，直接影响企业如何构建和运维自建的本地 AI 集群。对于那些无法或不希望使用云厂商托管 Kubernetes 的 AI 平台团队而言，它提供了一个由厂商支持的方案，替代以往手工拼装 Cluster API、GPU Operator 和自研自动化脚本的做法。 在预览阶段，NVIDIA Infra Controller（NICo）是唯一兼容的基础设施提供方，机器、网络、节点镜像和镜像仓库仍需用户自行准备；而且该仓库目前仅有 README 骨架，没有架构文档、性能基准或采用情况证据。官方提供了本地快速上手方案，无需 GPU 硬件即可在 Linux 主机或虚拟机上评估（amd64/arm64、至少 6 核 CPU、12 GiB 内存、100 GiB 磁盘，并需 Docker 与虚拟 TPM 支持），macOS 用户可通过 Colima 虚拟机运行，全部使用模拟机器且无需 NVIDIA 账号。

rss · GitHub Trending - Daily · 11月8日 20:16

**背景**: Kubernetes 通常在单个集群内运行控制平面（API Server、调度器、etcd）来管理集群状态；而管理平面位于更高一层，负责创建并全生命周期管理众多这样的集群。NVIDIA 此前已推出 GPU Operator，它在既有集群内部安装驱动、容器运行时和设备插件，使 GPU 成为可调度资源；NVKE 属于另一个层次，它在裸金属上供给整个集群，而不是在单个集群内配置 GPU。NVKE 面向“AI 工厂”模式，即运营方在本地运行 GPU 算力，并把相互隔离的集群交付给内部团队或租户使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.nvidia.com/nvke/documentation/overview/what-is-nvke">What is NVKE | NVIDIA Kubernetes Engine</a></li>
<li><a href="https://github.com/dsx-ai-factory/nvke">GitHub - dsx-ai-factory/nvke: NVIDIA Kubernetes Engine (NVKE ...</a></li>
<li><a href="https://elsolitario.org/en/2026/11/06/nvke-nvidias-factory-for-bare-metal-kubernetes/">GPU Management in Kubernetes: What Is NVKE? - elsolitario.org</a></li>

</ul>
</details>

**标签**: `#kubernetes`, `#gpu-infrastructure`, `#ai-infrastructure`, `#nvidia`, `#open-source`

---

<a id="item-9"></a>
## [Anthropic 被曝 34 亿美元购入 1.7GW 燃气发电机组，创 AI 公司最大电力设备订单](https://www.ithome.com/1/023/989.htm) ⭐️ 7.0/10

据 IT 之家援引英国《金融时报》报道，Anthropic 在 9 月下旬从美国圣安东尼奥设备供应商 OnePWR Solutions 手中接过了一份价值 34 亿美元、总功率达 1.7GW 的重型燃气发电机组订单，而不是单纯向对方购买电力服务。OnePWR 大约两年前就向卡特彼勒下了这笔设备订单，但一直需要融资才能完成采购，Anthropic 最终直接接手了这份订单。 按已知交易记录，这是 AI 公司迄今规模最大的一笔发电设备采购，说明头部 AI 实验室正在绕过公用事业公司和中间商，亲自掌握发电能力。这也进一步印证：制约 AI 规模扩张的瓶颈已不只是 GPU，还有电力，AI 公司因此正加速向能源行业纵向整合。 由于接手的是数年前、设备涨价之前签订的订单，部分发电机组近期就能交付，其余设备也将在约两年内到位，从而避开了当前燃气轮机和发电机组普遍长达数年的交货周期。报道还提到，Anthropic 同时是 SpaceX 的大客户，预计到今年年底其每月向 SpaceX 支付的算力租赁费用将达 31 亿美元。

rss · IT HOME · 11月8日 11:51

**背景**: 大型 AI 数据中心需要海量、稳定、全天候的电力供应，但接入公共电网往往要在并网队列中等待数年。于是运营商转向“表后”（behind-the-meter）自建发电，通常采用卡特彼勒等厂商的天然气往复式发电机组或燃气轮机，这类设备部署速度快于新建公用事业电厂。其他 AI 玩家也在用不同方式达成同一目标：xAI 据称斥资 20 亿美元购入移动式燃气轮机，谷歌母公司 Alphabet 则收购了能源开发商 Intersect。OnePWR Solutions 则是一家成立不久的小型电力解决方案公司，为客户设计发电项目并提供购电协议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://onepwrsolutions.com/solutions/">Solutions - OnePWR Solutions</a></li>
<li><a href="https://www.linkedin.com/pulse/louise-ai-why-i-like-caterpillar-primary-energy-data-nishimoto-wua6c">Louise ai : Why I like Caterpillar as a primary energy generator for data ...</a></li>
<li><a href="https://a2xenergy.com/">Behind the Meter Prime Power for AI Data Centers | A2X Energy</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#energy & power`, `#data centers`, `#industry news`, `#compute scaling`

---

<a id="item-10"></a>
## [SpaceX 星舰第 15 次试飞将首次尝试完整返回发射场回收](https://www.ithome.com/1/023/986.htm) ⭐️ 7.0/10

SpaceX 于 11 月 7 日深夜宣布，计划最早于美国中部时间 11 月 13 日进行星舰第 15 次试飞，发射窗口于当地时间下午 4 时 45 分（北京时间 14 日上午 6 时 45 分）开启并持续 75 分钟，但仍需监管部门批准。此次任务将首次尝试让星舰飞船和 V3 版本超重型助推器全部返回发射场，由发射塔机械臂分别捕获。 如果成功，这将是人类首次实现一整套轨道发射系统的完整回收，是星舰迈向可靠、快速重复使用目标的重要突破。飞船与助推器双双实现塔臂捕获一旦成功，将重塑发射经济性，并为整个航天工业树立新的标杆。 此次飞行计划持续超过 22 小时，在 275 公里高度环绕地球约 14 圈，并准备了被动安全的亚轨道轨迹或在预定海域受控离轨等备选方案。只有飞行控制团队确认飞船在再入机动、最终着陆点火及接近发射塔时所需的关键系统全部正常，才会允许其返回发射场；飞船还沿用第 14 次试飞的隔热罩改进，包括加强隔热瓦固定结构、处理高温等离子体可能侵入隔热瓦背面的薄弱部位，以及换用弧形隔热瓦以降低接缝处受热。

rss · IT HOME · 11月8日 11:02

**背景**: 星舰是 SpaceX 正在研制的完全可重复使用两级运载系统，由超重型一级助推器和星舰二级飞船组成。SpaceX 用发射塔上被昵称为“筷子”或“Mechazilla”的巨型机械臂在半空中夹住返航的助推器，而不是依靠着陆腿，此前已借此成功回收 3 枚 V1 版本助推器，其中 2 枚还实现了重复飞行。飞船迎风面覆盖着数千块六边形陶瓷隔热瓦，用于抵御再入时的极端高温，早期试飞中曾出现瓦片脱落问题，促使 SpaceX 不断改进热防护系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SpaceX_Starship">SpaceX Starship - Wikipedia</a></li>
<li><a href="https://baike.baidu.com/en/item/Mechazilla/4754634">Mechazilla（the robotic arm catch system on the SpaceX ...</a></li>
<li><a href="https://spacexstock.com/starship-heat-shield-how-it-handles-extreme-temperatures/">Starship Heat Shield: How It Handles Extreme Temperatures</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#Starship`, `#reusable launch`, `#aerospace engineering`, `#spaceflight`

---

<a id="item-11"></a>
## [反对数据中心浪潮席卷欧洲多国，抗议活动接连爆发](https://www.ithome.com/1/023/977.htm) ⭐️ 7.0/10

11 月 7 日，约 2000 人在都柏林游行、约 1300 人在赫尔辛基集会，苏格兰、西班牙、法国、丹麦以及芬兰多个城镇也同步举行了抗议，这些活动由“Stop Dirty Data Centres”联盟协调组织。此前一天，数百名抗议者在阿姆斯特丹的一座微软数据中心与警方发生冲突，一人被捕。 这些抗议表明，AI 基础设施建设正从技术与资本问题转变为政治议题，各国政府面临暂停大型数据中心建设的诉求。由于爱尔兰数据中心已占全国电表计量用电量的 23%，而芬兰处于规划与建设阶段的项目总投资约 800 亿欧元，这股反对声浪可能拖慢审批流程，并改变科技巨头在欧洲布局 AI 算力的方式。 抗议者要求立即暂停大型数据中心建设，直到民众能通过民主程序决定 AI 基础设施应如何造福人类与地球；该联盟明确将议题定调为“防止民主被大型科技企业的利益绑架”。在芬兰，谷歌 130 亿欧元（其欧洲最大单笔投资）项目被曝在环境影响评估尚未完成时就清理林地、剥离表土并修建道路，引发刑事调查，芬兰政府也着手立法限制 AI 产业扩张。

rss · IT HOME · 11月8日 10:18

**背景**: AI 模型（尤其是大语言模型）的训练与推理依赖高耗能的 GPU 集群，因此 AI 的快速扩张带动了全球数据中心用电需求的空前增长。得益于微软、亚马逊和谷歌的大举投资，爱尔兰已成为欧洲最大的数据中心聚集地之一，用电量与电网压力也随之成为该国的重要政治议题。欧洲的抗议与美国的情况相互呼应：数据中心扩张成为本周美国中期选举的议题之一，多个州选出了承诺叫停或暂缓相关项目的地方官员。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://stopdirtydatacentres.eu/">Stop Dirty Data Centres - Days of Action 6-7 Nov 2026</a></li>
<li><a href="https://news.ucsb.edu/2025/021835/power-ai-data-centers-need-more-and-more-energy">To power AI , data centers need more and more energy | The Current</a></li>

</ul>
</details>

**标签**: `#data centers`, `#AI infrastructure`, `#energy policy`, `#big tech`, `#Europe`

---

<a id="item-12"></a>
## [美国司法部起诉三名男子，利用 AI 深度伪造高管身份诈骗逾 1.29 亿美元](https://www.ithome.com/1/023/925.htm) ⭐️ 7.0/10

美国司法部公布了一份起诉书，指控雅各布·索尔、沙龙·哈赞和盖伊·谢特里特三名外籍男子利用 AI 伪造企业高管和律师的声音与影像，诱骗企业员工向指定账户汇款超过 1.29 亿美元。索尔和哈赞今年夏天在西班牙被捕，谢特里特于 9 月在英国落网，检方称诈骗活动从 2024 年一直持续到 2026 年。 这是目前公开记录中规模最大的生成式 AI 大规模社会工程诈骗案之一，说明克隆语音与合成视频足以击穿财务团队长期以来依赖的人工核验环节。它标志着冒充高管的汇款诈骗正从基于文字的商务邮件诈骗（BEC）升级为实时的多渠道欺骗，医院、银行、基金管理公司及其承保保险公司都直接处于风险之中。 检方称，三人先冒充企业高管联系员工，谎称有敏感财务交易需要处理，再让员工联系一家所谓的大型国际律师事务所，随后由同样由 AI 冒充的"律师"指示汇款；赃款通过分布在美国、欧洲和亚洲的账户转移，并兑换成加密货币以掩盖资金来源与所有权。已披露的损失包括密苏里州某医院集团和佛罗里达州某宠物食品公司各约 500 万美元、马萨诸塞州某共同基金公司逾 460 万美元、加州某医院集团约 300 万美元、罗得岛州某银行约 270 万美元，以及一家英国科技公司逾 1100 万美元；三人被控共谋实施电信欺诈、洗钱共谋及加重身份盗用等罪名。

rss · IT HOME · 11月8日 08:48

**背景**: 如今的 AI 语音克隆与深度伪造视频工具只需一小段声音样本或少量公开露面素材，就能生成极具说服力的合成语音和人脸，使犯罪分子得以在实时通话或视频会议中冒充他人。这类能力被叠加在商务邮件诈骗（BEC）之上——这是一种更早出现的诈骗类型，攻击者冒充高管或供应商以骗取付款授权，每年已给企业造成数十亿美元损失。在法律层面，克隆技术本身通常是被允许的，但利用它实施诈骗或冒充他人，则可能依据欺诈、身份盗用和洗钱相关法律被追究刑事责任。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.adaptivesecurity.com/blog/ai-deepfake-scams">AI Deepfake Scams: How Voice and Video Attacks Work</a></li>
<li><a href="https://infosecfederation.com/deepfake-voice-wire-transfer-executive-impersonation-fraud-2026/">Deepfake Voice Calls and the Wire Transfer: How Executive ...</a></li>
<li><a href="https://www.forbes.com/sites/steveweisman/2026/08/08/how-ai-powered-business-email-compromise-scams-are-stealing-billions/">How AI-Powered Business Email Compromise Scams Are ... - Forbes</a></li>

</ul>
</details>

**标签**: `#AI fraud`, `#deepfakes`, `#voice cloning`, `#cybersecurity`, `#AI safety & governance`

---

<a id="item-13"></a>
## [Asahi Linux 将全部仓库从 MIT 许可证改为 GPLv2 及以后版本](https://lwn.net/Articles/1105936/) ⭐️ 7.0/10

Asahi Linux 在 7.3 进度报告中宣布，正在将旗下所有代码仓库从宽松的 MIT 许可证迁移到 GNU 通用公共许可证第 2 版或更高版本，今后所有 Asahi Linux 代码都只采用强 copyleft 许可证发布。开发者表示，这一决定源于多起利用其宽松许可证的事件：尚未发布的开发中功能代码被直接从个人 fork 中取走，在未署名的情况下发布，或被用大语言模型草率改写以掩盖来源。 Asahi Linux 是让 Linux 在 Apple Silicon Mac 上原生运行的最受关注的项目，因此其转向 copyleft 的举措，为志愿驱动的逆向工程项目如何抵御商业搭便车提供了一个重要案例。这也凸显了开源可持续性方面的一个新隐忧：借助 AI 改写代码会抹去来源信息，使归属认定和许可证维权变得更加困难。 MIT 许可证明确允许在无署名义务、无 copyleft 条件的情况下复用和再分发代码，项目方因此称其无法防范恶意行为者。此次调整适用于今后所有仓库，意味着贡献者都将在 GPLv2 及以后版本的条款下工作；报告将这一改变定位为防御性的必要之举，而非技术里程碑。

rss · LWN.net · 11月7日 09:49

**背景**: Asahi Linux 通过逆向工程 Apple 的片上系统，将 Linux 内核及相关用户态软件移植到 Apple Silicon Mac 上，而 Apple 并未公开这些芯片的文档。由于该项目由社区驱动并公开其成果，它依赖许可证来约束他人如何复用这些工作。GPL 这类 copyleft 许可证要求：向他人分发的衍生作品也必须以相同或等效条款发布；而 MIT 这类宽松许可证基本不对下游用户施加此类条件。报告中提到的“借助 LLM 改写”，指的是用大语言模型对源代码进行改写，使来源更难被追溯。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Asahi_Linux">Asahi Linux - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/GNU_General_Public_License">GNU General Public License - Wikipedia</a></li>
<li><a href="https://asahilinux.org/">Asahi Linux</a></li>

</ul>
</details>

**标签**: `#open-source-licensing`, `#Asahi Linux`, `#Apple Silicon`, `#copyleft`, `#LLM attribution`

---

<a id="item-14"></a>
## [Amutable OS 亮相：无 Shell、无 SSH、无解释器的镜像式 Linux](https://lwn.net/Articles/1105934/) ⭐️ 7.0/10

Lennart Poettering、Michael Vogt 和 Joaquim Rocha 共同发布了一份关于 Amutable 操作系统（AOS）及其配套基础设施的详细技术概览。按其设计，AOS 是一种镜像式 Linux：默认不安装 UNIX shell，节点上不提供 SSH 远程访问，也不预装 Python、Perl 等常见语言解释器。 该设计刻意用牺牲交互式运维的方式换取更小的攻击面，其理由是大多数节点根本不需要 shell 或解释器，去掉它们就能消除一整类攻击者得手后的利用手段。这份概览出自三位知名 Linux 开发者之手并经 LWN 报道，预示着加固型、不可变服务器与设备操作系统可能成为一个有影响力的方向。 该概览列举了七项核心安全属性，其中包括“无 Shell、无 SSH、无语言解释器”以及“仅限签名镜像”：只有携带由 Verity 密钥环中所列密钥签名的 Verity 数据的镜像才允许被激活。值得注意的是，这仍只是一份架构层面的描述，而非已发布或经过基准测试的系统，因此在没有 shell 的情况下调试与排障等实际代价仍有待验证。

rss · LWN.net · 11月7日 09:32

**背景**: 镜像式操作系统以完整的只读文件系统镜像形式构建和分发，而不是在每台目标机器上逐个安装软件包，这与更广泛的“不可变基础设施”实践一致——即通过替换服务器或镜像来变更，而不是就地修改。Verity 指的是 dm-verity，这是 Linux 内核中依据哈希树校验块设备内容完整性的机制，对这一哈希树签名便可使系统拒绝启动被篡改的镜像。Poettering 是 systemd 的创建者，Vogt 以 Snap 和 Ubuntu 相关工作闻名，Rocha 则与 elementary OS 和 Flatpak 相关。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://amutable.com/foundations?ref=itsfoss.com">Amutable Foundations - Amutable</a></li>
<li><a href="https://www.phoronix.com/news/Amutable">Systemd Founder Lennart Poettering Announces Amutable ... - Phoronix</a></li>
<li><a href="https://docs.centos.org/automotive-sig-documentation/features-and-concepts/con_image-based-operating-systems/">Image-based operating systems - CentOS Documentation</a></li>

</ul>
</details>

**标签**: `#operating-systems`, `#linux`, `#security`, `#immutable-infrastructure`, `#systems-design`

---

<a id="item-15"></a>
## [美团发布 LongCat-2.5：1.6 万亿参数原生多模态智能体模型](https://tech.meituan.com/2026/11/02/Meituan-LongCat-2.5.html) ⭐️ 7.0/10

美团正式发布 LongCat-2.5，这是一个原生多模态的混合专家（MoE）模型，总参数量达 1.6 万亿，每个 token 约激活 480 亿参数，明确定位于长程智能体任务。该模型在 LongCat-2.0 基础上进一步强化了原生视觉理解与智能体编程能力，美团称其提升来自大规模长上下文训练与长程强化学习。 一家中国大型平台公司推出面向自主智能体的万亿参数稀疏多模态模型，说明美团已不只是应用层公司，而是认真的基础模型玩家。这也为快速演进的多模态智能体赛道增加了一个有分量的竞争者，而长程工具调用与编程能力正成为前沿实验室的主战场。 稀疏 MoE 架构使推理算力大致与每 token 约 480 亿激活参数挂钩，但完整的 1.6 万亿参数仍需全部驻留显存，因此部署门槛依然很高。值得注意的是，目前公开的发布信息中没有基准测试成绩、架构细节、训练数据说明、许可证条款，也没有对长程智能体表现的独立评测，因此关于智能体能力的说法尚无法验证。

rss · 美团 Blog · 11月8日 20:17

**背景**: 混合专家（MoE）模型用多个专家子网络替代单一的稠密前馈层，并通过学习到的路由器为每个 token 只激活其中少数几个，从而把总知识容量与单 token 计算量解耦——这正是 LongCat-2.5 能宣称 1.6 万亿总参数却只激活约 480 亿参数的原因。“长程智能体任务”指 AI 智能体自主执行大量相互依赖的步骤（规划、调用工具、修改代码、检查结果）以完成开放式目标的工作流，它对长上下文记忆和多步推理的要求远高于单轮对话。美团以 food delivery 与本地生活服务平台闻名，近年持续建设 LongCat 模型家族，这是中国互联网公司自研基础模型浪潮的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://longcat.ai/blog/longcat-2.5/">Introducing LongCat-2.5</a></li>
<li><a href="https://www.explainx.ai/blog/longcat-2-5-1-6-trillion-agent-model-2026">LongCat 2.5: Meituan 1.6T Model Targets AI Agents | explainx ...</a></li>
<li><a href="https://localmodel.run/guides/mixture-of-experts">Mixture of experts (MoE) explained for local LLMs · localmodel.run</a></li>

</ul>
</details>

**标签**: `#multimodal LLM`, `#mixture-of-experts`, `#agents`, `#model release`, `#Meituan`

---

<a id="item-16"></a>
## [美团 MTFM：一个基座大模型统一外卖多业务精排](https://tech.meituan.com/2026/09/22/Meituan-Foundation-Model-for-Recommendation.html) ⭐️ 7.0/10

美团推荐算法团队发布统一推荐基座大模型 MTFM（Meituan Foundation Model for Recommendation），首次实现外卖多个主要业务的统一精排模型，取代此前各业务各自独立训练排序模型的模式。MTFM 建立在此前的生成式推荐工作 MTGR 之上，围绕规模可扩展性（Scalability）、场景可延展性（Extensibility）与架构高效性（Efficiency）三大目标设计，相关论文已被 KDD 2026 收录。 在工业生产环境中把异构业务场景的精排统一到一个模型，是一项颇具分量的机器学习系统工程成果：原本无法共享的数据与算力可以在业务线之间复用，这正是把“基座大模型”思路从自然语言处理迁移到推荐系统的核心论点。文中记录的多场景迁移、特征对齐与线上服务成本等权衡，对同样运营多个推荐场景的公司具有直接的复用价值。 MTFM 用异构 Token 序列替代固定特征模板，并配合动态掩码，使不同场景的信号无需人工对齐即可统一输入；同时通过混合注意力与 Target Scale-Up 策略提升模型 Scaling 能力，并借鉴大语言模型的训练优化实践来稳定深层网络训练。据美团介绍，此前的 MTGR 已将单样本前向推理 FLOPs 提升约 65 倍，并依靠自建的训练/推理引擎把线上推理成本控制在可接受范围。

rss · 美团 Blog · 11月8日 20:17

**背景**: 传统工业推荐模型（DLRM 类）依赖人工构造的交叉特征，且通常按业务场景分别训练，每新增一个场景就要新建模型与流水线，难以共享学习成果。HSTU 等生成式推荐模型把排序问题重构为序列预测，具备良好的可扩展性，但早期方案舍弃了精心构造的交叉特征，导致效果下降。美团的 MTGR 在保留这些特征的同时引入基于 Transformer 的生成式架构；MTFM 则把这条路线从单一场景扩展到多场景，目标是成为推荐领域的共享“基座模型”。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tech.meituan.com/2026/09/22/Meituan-Foundation-Model-for-Recommendation.html">MTFM：美团统一推荐基座大模型在外卖多业务场景的落地实践</a></li>
<li><a href="https://arxiv.org/abs/2602.11235">[2602.11235] MTFM: A Scalable and Alignment-free Foundation ... MTFM：美团统一推荐基座大模型在外卖多业务场景的落地实践 MTFM：美团统一推荐基座大模型在外卖多业务场景的落地实践（2026-09-2... 从MTGR到MTFM：美团异构多场景推荐Foundation Model MTFM：美团统一推荐基座大模型在外卖多业务场景的落地实践 MTFM：美团统一推荐基座大模型在外卖多业务场景的落地实践 | BriefSum...</a></li>
<li><a href="https://arxiv.org/abs/2505.18654">[2505.18654] MTGR: Industrial-Scale Generative Recommendation ... MTGR：美团外卖生成式推荐Scaling Law落地实践 - 知乎 llm4rec/MTGR/MTGR.md at main · LJJ1118/llm4rec · GitHub MTGR: Industrial-Scale Generative Recommendation Framework in ... MTFM：美团统一推荐基座大模型在外卖多业务场景的落地实践 MTGR（美团生成式推荐框架）总结文档 - 技术栈</a></li>

</ul>
</details>

**标签**: `#recommender-systems`, `#foundation-models`, `#industrial-ml`, `#ranking`, `#large-scale-systems`

---

<a id="item-17"></a>
## [美团搜索 3.0：将 LLM 语义表征应用于排序模型](https://tech.meituan.com/2026/08/20/01-meituan-Query-3.0.html) ⭐️ 7.0/10

美团搜索团队发布了「美团搜索 3.0」系列技术博客的首篇文章，介绍了将基于大模型的语义表征引入本地生活搜索排序环节的三期实践。该工作聚焦服务零售排序场景，从单点特征验证起步，进而构建系统性表征体系，最终实现跨场景迁移与复用。 它提供了一份少见的工业实践记录，说明生成式大模型表征如何与大规模搜索系统中的传统排序模型结合，而这正是当下众多搜索与推荐团队在探索的问题。其中跨场景复用的推进对美团尤其有意义——外卖、到店餐饮、酒店、旅游等众多垂直业务共享同一个搜索入口。 该文被定位为系列文章的开篇，依托美团重构后的「团垂融合」搜索架构，因此摘要中并未给出具体的模型选型、训练目标、时延与成本权衡以及线上 A/B 收益。文中明确界定的范围较为聚焦：服务零售场景下排序环节的语义匹配信号，而非完整的搜索链路。

rss · 美团 Blog · 11月8日 20:17

**背景**: 大语言模型能够生成稠密向量表征，捕捉用户查询与商品文本之间的语义相似度，这对于关键词字面匹配失效的搜索系统尤为有价值——例如「公司附近暖和又辣的」这类口语化、改写过的本地生活查询。传统学习排序模型依赖人工构造特征和基于 ID 的 embedding，因此核心工程问题在于：如何在不显著抬高推理时延和服务成本的前提下，把大模型产出的表征喂给这些模型。跨场景复用则进一步追问：为某个垂直业务学到的表征，能否以很少甚至无需额外训练的方式迁移到另一个业务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.aibase.com/news/30507">How Does Meituan Search 3.0 Use Large Models to Reconstruct the...</a></li>
<li><a href="https://arxiv.org/html/2602.12968v1">RGAlign-Rec: Ranking -Guided Alignment for Latent Query Reasoning...</a></li>

</ul>
</details>

**标签**: `#LLM embeddings`, `#search ranking`, `#semantic representation`, `#recommender systems`, `#industry practice`

---

<a id="item-18"></a>
## [美团盘点 KDD 2026 八篇入选论文及 KDD Cup DataAgents 赛道夺冠方案](https://tech.meituan.com/2026/08/13/KDD-2026-meituan-papers.html) ⭐️ 7.0/10

美团技术团队发布文章，集中介绍了被 KDD 2026 收录的 8 篇论文，覆盖推荐大模型、生成与奖励建模框架、智能体搜索、Transformer 框架以及元泛化等方向，并同步解读了其团队在 KDD Cup 2026 DataAgents 赛道夺冠的解题思路。 这篇文章较为集中地展示了一家大型工业实验室如何把以大模型为核心的推荐、智能体与泛化研究推向生产系统，对关注应用型 AI 走向的研究者和工程师具有参考价值；同时，KDD Cup 的解题复盘也为业界在竞赛约束下构建自主数据分析智能体提供了可借鉴的参考方案。 这 8 篇论文按技术方向分类呈现，并非围绕单一系统展开，而且目前公开的仅是导览式摘要，具体技术细节、基准指标与消融实验结果仍需查阅论文全文。DataAgents 冠军方案中的智能体流程与评测策略等细节，也需阅读完整文章才能获取，摘录部分并未涵盖。

rss · 美团 Blog · 11月8日 20:17

**背景**: KDD 是数据挖掘与知识发现领域的旗舰会议之一，其配套的 KDD Cup 竞赛通常会给出贴近实际应用的赛题，吸引数百支队伍参加。近年来，会议与赛事都在向基于大模型的方法倾斜：推荐系统越来越多地以大模型作为主干；所谓“智能体搜索”（agentic search）是指由大模型把复杂查询拆解为多个子查询、并迭代检索与推理的流水线；而元泛化（meta-generalization）则指借助元学习让模型快速适应新领域或新任务。KDD Cup 2026 的 DataAgents 赛道要求参赛队伍构建能够自主完成数据分析任务的智能体。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview">Agentic Retrieval Overview - Azure AI Search | Microsoft Learn</a></li>
<li><a href="https://arxiv.org/abs/2606.00979">[2606.00979] UME: A Unified Meta-Generalization Framework for ...</a></li>
<li><a href="https://devlery.com/en/blog/kdd-cup-data-agents-evaluation">KDD Cup Data Agents Delayed by 700 Teams and Docker... - Devlery</a></li>

</ul>
</details>

**标签**: `#KDD 2026`, `#industrial research`, `#LLM agents`, `#recommendation systems`, `#meta-learning`

---