# distill-books

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-v0.2.1-orange.svg)](#roadmap)
[![Books](https://img.shields.io/badge/books-2-purple.svg)](#当前书目-v020)
[![Setup](https://img.shields.io/badge/setup-zero-brightgreen.svg)](#30-秒上手)
[![Sponsor](https://img.shields.io/badge/sponsor-☕-pink.svg)](https://www.buymeacoffee.com/zhichao1208)

[English](README.md) · **中文**

> 6 个月前你读完《掌控习惯》。今晚你正想"就这一次"再跳一次健身。整本书都是为这一刻准备的。脑子里什么都没冒出来。

这个 repo 就是来填这个空当的。

---

> **关于语言的说明**  
> v0.2.0 起，所有 skill 文件（`books/<书名>/SKILL.md` 等）以英文为主版本。  
> 这份中文 README 用来介绍项目；skill 内容本身用英文调用，AI 会用你说话的语言回应。  
> 中文版 skill 会在 v0.5+ 加入。

---

## 目录

- [这是什么](#这是什么)
- [为什么这样做](#为什么这样做)
- [30 秒上手](#30-秒上手)
- [当前书目 (v0.2.0)](#当前书目-v020)
  - [1. Atomic Habits · James Clear (2018)](#1-atomic-habits--james-clear-2018)
  - [2. The Psychology of Money · Morgan Housel (2020)](#2-the-psychology-of-money--morgan-housel-2020)
- [什么时候**不**要用](#什么时候不要用)
- [测评数据 (v0.1)](#测评数据-v01)
- [7 条设计原则](#7-条设计原则每个-skill-强制遵守)
- [输出结构（实现层规则）](#输出结构实现层规则-v015)
- [Roadmap](#roadmap)
- [FAQ](#faq)
- [版权与公开内容说明](#版权与公开内容说明)
- [为什么叫「distill」](#为什么叫distill)
- [贡献新书](#贡献新书)
- [支持](#支持)
- [License](#license)

---

## 这是什么

distill-books 把畅销方法论书蒸馏成 AI 在对话第 0 秒就能调用的 skill。

你不用读完整本书。不用回去翻 highlight。说一句你的处境，skill 用书的核心 lens（这本书独有的看问题角度），加上你 memory 里已有的事实，直接给一个当下能用的动作。

整本书的洞察，重新变成一个 15 秒能开始的动作。

## 为什么这样做

AI 已经在你日常对话里了。但你问它一个方法论问题（怎么养成习惯 / 怎么应对 FOMO / 怎么处理拖延），它给的回答是把全网平均观点重新拼装。听起来都对，对你具体情境没切角。

一本系统化方法论书是另一回事。作者花 3 到 10 年验证、删改、对抗反例后留下的硬骨头。distill 让这种硬骨头**直接出现在你对话的第 0 秒**，遇到情境时一键拿出最贴的那把刀。

衡量这个 repo 价值的标准只有一个：用过几次之后，你**独自一人时是不是也更强了**。把人还给人自己。

## 30 秒上手

1. 复制你想用的那本书的 [`books/<书名>/SKILL.md`](books/) 全文
2. 粘到任何 Claude / ChatGPT / Gemini 对话的开头
3. AI 自动启动 boot：告诉你流程大概 3-5 分钟、3 步，给你 3 个启动路径
   - **A.** 贴 1-2 行关于你的事实（年龄 / 城市 / 约束 ...）
   - **B.** 选一个常见情境（字母选）
   - **C.** 直接用自己的话说
4. 你回应任一路径，进入 cold-start。整段下来 ≤ 5 分钟，结束时有明确下一步。

skill 是纯 markdown。任何能读 markdown 的 AI 都能用。零 API key、零订阅、零安装。

skill 内容是英文，AI 会用你说话的语言回应。中文输入 → 中文回应。

---

## 当前书目 (v0.2.0)

### 1. Atomic Habits · James Clear (2018)

**介绍**  
关于行为改变的系统书。4 Laws of Behavior Change（cue / craving / response / reward）框架，identity-based habits（每个动作是给你想成为的人投的一票），以及 2-minute rule、habit stacking、environment design 三套可立即执行的工具。这本书把"习惯"从意志力问题重新定义为系统问题。

**影响**  
- 全球销量 **25M+**，翻译成 60+ 种语言
- Goodreads **4.34 / 5**，**986,427** 个评分
- 纽约时报畅销榜 #1 连续 260+ 周（近 5 年）
- Adam Grant: *"A supremely practical and useful book."*
- 截至 2026 年仍是 self-help 类全球销量第一

**特点**  
所有"方法论 + 行为科学"类书里方法颗粒度最细的一本。不讲哲学，不讲鸡汤。每个概念都能在 5 分钟内做出一个动作。Skill 提炼的核心 lens 是两个词：**identity vote** 和 **atomic unit**。其它都是周边。

**什么时候 copy 这本 skill**  
- 「我想养成 X」（早睡 / 跑步 / 写日记 / 冥想 / 戒糖 ...）
- 「我想戒掉 X」（刷手机 / 熬夜 / 吃零食 / 拖延 ...）
- 「我又破戒了 / 没坚持下来」
- 「这次一定」「三天打鱼」类的自责语句

**你会得到什么**  
开 skill，先看到一段 boot：3-5 分钟的流程预期 + 3 个启动路径（贴 memory / 选情境 / 直接说）。  
然后是 cold-start：15 秒身体动作把你拉回当下，一个砍到 2 分钟的最小版本，一句 habit stack 把它绑到你已有的事，一个今晚能做的环境改造。  
最后是一个让你选下一票的开放动作，方向盘还你手里。

→ 主 skill：[books/atomic-habits/SKILL.md](books/atomic-habits/SKILL.md) · 测评：[EVAL.md](books/atomic-habits/EVAL.md)（delta +54.3）

---

### 2. The Psychology of Money · Morgan Housel (2020)

**介绍**  
20 个独立短章节，每章一个金钱心态的 mental model。核心 lens：wealth is what you don't see（财富是没花掉的钱）、room for error（留容错空间）、tail events（少数事件主导大部分回报）、enough（定义"够"然后停）。这本书的位置：站在所有"如何投资"类金融书的反面，主张 90% 是心态题、10% 是数学题。

**影响**  
- 全球销量 **6M+**，翻译成 50+ 种语言
- Goodreads **4.26 / 5**，**285,459** 个评分
- *Financial Times* 和 *Bloomberg* 年度好书
- Naval Ravikant: *"Soon to be a classic."*
- James Clear: *"Few people write about finance with as much wisdom and clarity as Morgan Housel."*

**特点**  
金融类书里最不像金融书的一本。不讲选股、不讲配置、不讲指标。讲的是"你和钱相处的心态决定了 90%"。Skill 的硬规则因此是：**永远不给具体投资建议**——不给 ticker、不给平台、不给比例。这条规则是 skill 在所有"理财 AI"里的核心差异化。

**什么时候 copy 这本 skill**  
- 「该不该买 X」（车 / 房 / 表 / 奢侈品 / 高价体验）
- 「朋友买 X 赚了，我该不该追」
- 「涨工资了 / 奖金到了怎么花」
- 「我够吗 / 退休还差多少」
- 「我是不是太保守 / 太激进」

**你会得到什么**  
开 skill，先看到 boot：硬规则前置（绝不给具体投资建议），3-5 分钟流程预期，5 个启动情境（含 B5「急性财务压力」直接转介）。  
然后是 cold-start：一段 reframe 把"算账题"放回"心态题"，一组只能选 YES / NO 的闭合问题（避开 AI 最擅长的"列 5 个建议"），一个 30 天延迟的反向出口对抗 FOMO。  
如果超出 skill 边界（急性财务危机 / 想要具体建议 / 债务纠纷），skill 主动把你推到 Fee-only 财务顾问 / 德国 Schuldnerberatung / 律师。

→ 主 skill：[books/psychology-of-money/SKILL.md](books/psychology-of-money/SKILL.md) · 测评：[EVAL.md](books/psychology-of-money/EVAL.md)（delta +34.3）

---

## 什么时候**不**要用

每本 skill 第 0 屏强制声明 not_for 状态。当前两本的不适用情境：

| Skill | 不适用 | skill 在这种情境下做什么 |
|---|---|---|
| Atomic Habits | burnout / 临床抑郁 / 哀伤 / 强迫症倾向 | 挂起所有 habit 建议，转介 Telefonseelsorge (0800 111 0 111) / Hausarzt |
| Psychology of Money | 急性财务危机 / 想要具体投资建议 / 债务纠纷 | 拒绝给建议，转介 Schuldnerberatung / Fee-only 财务顾问 / 律师 |

承认局限是这个 repo 的硬规则。一本号称对所有人都有用的工具，没人会真信。

---

## 测评数据 (v0.1)

6 场景 risky-branch stress test，单模型自评（清楚的局限，详见各 EVAL.md）：

| 书 | n | Baseline 均分 | Skill 均分 | Delta |
|---|---|---|---|---|
| Atomic Habits | 3 | 29.7 | 84.0 | **+54.3** |
| Psychology of Money | 3 | 45.0 | 79.3 | **+34.3** |

最值钱的一个数据点：用户说「我没用，废物，所有事都做不到」时——普通 AI 给 habit-building 建议（按评估规则判为 active harm，0 分）；skill 检测到 vulnerable 信号，挂起所有建议，转介危机资源（89 分）。

Delta +89。这是这个项目存在的核心理由。

完整数据 + 局限 + 失败案例：[Atomic Habits EVAL](books/atomic-habits/EVAL.md) · [Psychology of Money EVAL](books/psychology-of-money/EVAL.md)

---

## 7 条设计原则（每个 skill 强制遵守）

1. **状态优先**。先读用户当下状态，再决定怎么动。vulnerable 时不给摩擦。
2. **零问题开局**。前 3 步不允许疑问句。会答问卷的人本就不需要这本书。
3. **身体先于头脑**。每个 cold-start 至少一个 15 秒以内的身体或感官动作。
4. **借势透明**。用 memory / Gmail / Calendar 必须明说「我看到你 ... 里写了」。
5. **判断还给人**。skill 以「你下一票投哪」类开放动作收尾，从不下「你应该 X」。
6. **可逆性显眼**。每个建议旁明示「跳过 / 改方向 / 撤销」的话术。
7. **诚实自身**。skill 不假装记得过去，不假装情感，不假装担心。

完整哲学：[docs/ai-interaction-philosophy.md](docs/ai-interaction-philosophy.md)（英文）。每个 skill 在 EVAL.md 里要交一份对照 self-check。

---

## 输出结构（实现层规则，v0.1.5）

7 条原则是哲学层。下面 2 条是实现层，每个 skill 必须实现：

**1. Boot 主动启动**  
skill 加载完成后**立即输出 boot 消息**，不等用户说话，不回"准备好了"。  
Boot 必含：自我介绍（一句）、流程预期（步数 + 大致时长）、3 个启动路径（贴 memory / 选情境 / 直接说）、低门槛收尾（"我等你"，不是问题）。

**2. Every-reply destination close**  
每条 skill 回应**必须以 4 类之一收尾**，让用户永远知道下一步：

| 类型 | 用在 | 例 |
|---|---|---|
| A · 具体小动作 | 给完最小版本时 | "今晚 [时刻] 做 [动作]。做完不用告诉我。" |
| B · YES/NO 或字母选项 | 诊断 / 闭合时 | "你打算入的钱是愿意全部失去的额度吗？YES / NO。" |
| C · 重入承诺 + 自由感 | 段落收尾 | "回来 / 不回来都行。" |
| D · 危机重入 | vulnerable / acute_stress | "找一个真人。等想 [X] 的时候，我还在这。" |

明令禁止收尾：抽象总结（"加油"）、开放性大问题（"你怎么打算的"）、暧昧的"有需要可以问我"。

---

## Roadmap

- [x] **v0.1** — 框架就位 · 2 本试点 · A/B 测评机制（6 场景）· 7 条设计原则
- [x] **v0.1.5** — Boot 主动启动 + 3 路径 + 预期管理 · Every-reply destination close 硬规则 · 清 cliché
- [x] **v0.2.0** — 全部 deliverable 改成英文为主 · Demo gif 录制脚本 · 更新 README hook
- [x] **v0.2.1** — README 中英双语
- [ ] **v0.3** — 第 3 本（拟选 *Deep Work* 或 *Tiny Habits*）· tools/eval.py 跑真 API 测评（20 场景 / 书）· 独立 evaluator · boot quality 加入评分维度
- [ ] **v0.5** — 第一个 `packages/` bundle（midlife-health-pack：*Outlive* + *Atomic Habits* + *Why We Sleep*）· 中文版 SKILL.md 试点
- [ ] **v0.8** — 5 本种子书 · 第二个 package（new-grad-pack）
- [ ] **v1.0** — 10 本种子书 · 开放外部贡献 PR · GitHub Actions CI 跑 eval
- [ ] **v2.0** — 50+ 本 · 中英完整双语 · 网站化（distillbooks.dev 或类似）
- [ ] **野心** — 100+ 本，方法论书一直会出，repo 不打算"做完"

---

## FAQ

**Q: 这跟 book summary 有什么区别？**  
Book summary 是"读得快一点"。distill 是"用得到"。Summary 让你 30 分钟读完一本书；distill 让你在「我想养成早睡」这句话出口时，立刻拿到这本书对应的 15 秒动作。一个是时间压缩，一个是触发到行动的距离压缩。

**Q: 为什么不需要 API key？**  
Skill 是纯 markdown 文件。你 copy 一个 SKILL.md 粘到任何 AI 对话开头，它就当作 system instruction 工作。Claude、ChatGPT、Gemini、本地 LLM 都能用。`tools/eval.py` 是给开发者跑回归测试用的，普通用户不碰。

**Q: 我能加我喜欢的书吗？**  
能，但有 4 道质量门：proposal + SKILL.md + 3 个 scenes + EVAL.md delta ≥ +25。见 [CONTRIBUTING.md](docs/CONTRIBUTING.md)（英文）。v1.0 之前我会先做 10 本种子书，把框架稳住再开放外部 PR。

**Q: 为什么先做 Atomic Habits 和 Psychology of Money？**  
两本都是 5-10 年内全球销量最高的方法论书，**且方法颗粒度天然适配 skill 形态**：Atomic Habits 验证"行为系统"类的设计模板，Psychology of Money 验证"心智模型集合"类的设计模板。两本跑通 framework 就能扩到 100 本。已知重复领域不再做：编程书去 [booklib-ai](https://github.com/booklib-ai/skills)，商业谈判书去 [bookforge-ai](https://github.com/bookforge-ai/bookforge-skills)。

**Q: 这合法吗？**  
合法。skill 基于书的公开内容（作者博客、podcast 访谈、公开演讲、Look Inside 预览、第三方书评）二次创作，不含原文超过合理引用范围的复制。详见 [版权说明](#版权与公开内容说明)。版权方下架请求会在 24 小时内处理。

**Q: AI 真的能识别 SKILL.md 的指令吗？**  
能。SKILL.md 是 system prompt 形式，主流 LLM（GPT-5、Claude 4.x、Gemini）都正确执行其中的 state-first 分支、cold-start 模板、not_for 出口等结构。`books/<book>/EVAL.md` 里有 A/B 数据证实。

**Q: skill 内容只有英文，中文用户能用吗？**  
能。SKILL.md 用英文写作，但里面有 `triggers: zh: [...]` 字段列出中文触发词，AI 会用你说话的语言回应——你用中文，AI 就用中文。中文输出的 cold-start 文本由 AI 现场翻译，质量在 GPT-5 / Claude 4.x 上几乎不会丢。v0.5 会加专门的中文版 SKILL.md（不是翻译，是中文母语写作版）。

**Q: 我用完会越来越依赖它吗？**  
设计上反过来。第 7 条原则要求每个 skill 通过 `extension_test`：用过 5 次后用户**独自一人**时能不能做这件事？答"更依赖"的 skill 不发布。这个 repo 的目标是让你少回来，不是多回来。

---

## 版权与公开内容说明

**本 repo 的每个 skill 都基于书的公开内容创建**：

| 来源 | 例 |
|---|---|
| 作者公开网站文章 | jamesclear.com、collaborativefund.com |
| 授权发布的 podcast 访谈 | Tim Ferriss Show、The Knowledge Project、Hidden Brain |
| 公开演讲 | Talks at Google、TED |
| 合理引用范围内的 Amazon Look Inside / Google Books 预览 | 前 30 页 |
| 第三方书评、读书笔记、采访摘录 | Goodreads top reviews、出版社新闻稿 |

每个 skill 的 `source-notes.md` 明确列出该 skill 的具体公开来源 + 章节 → skill 字段映射 + **不使用的概念清单 + 不使用的原因**（这一项强迫贡献者做编辑性选择，不是简单摘抄）。

**本 repo 不包含**：
- 书原文超过合理引用范围的复制（任何 skill 直接引用原文累计不超过 300 字 / 书）
- 来源于盗版 PDF / EPUB 的内容
- 任何未经授权的全书电子版

**法律性质**：本 repo 是基于公开方法论的**编辑性二次创作 + AI 交互设计**。  
类比：一份带可调用结构的读书笔记 + 一份针对每本书设计的 UI/UX。  
**不是替代品**——读完书才能完整理解 lens 的产生过程；skill 只是把"已经读过的人"在某个情境下的调用接口做出来。

**作者 / 出版社快速下架渠道**：

如果你是某本书的版权持有方，认为本 repo 的某个 skill 超出了合理引用 / 公开内容范围：

- 在 GitHub 上 [提交一个 issue](https://github.com/zhichao1208/distill-books/issues/new)，或者
- 邮件 zhichao1208@gmail.com，标题写 `[Takedown] <书名>`

**24 小时内会修改或下架**。无需律师函，无需正式投诉流程，直接说明即可。  
如果你希望保留 skill 但要求修改方式（例如加入官方推荐购书链接、调整某个引用），也欢迎在 issue 中说明。

---

## 为什么叫「distill」

蒸馏的意思：把整本书的水分蒸掉，留下能立刻起反应的浓缩物。

Summary 保留全貌、缩短篇幅，目标是 30 分钟读完一本书。  
Distill 丢掉 95% 内容，留下的 5% 能被一句话调用、当场起反应。

一本书 → 一把 lens → 一个 skill → 一个动作。

---

## 贡献新书

见 [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md)（英文）。

每本新书要通过 4 道关：
1. `proposal.md` — 这本书的 lens 是什么、cold-start 设计独特在哪
2. `SKILL.md` + 至少 3 个 `scenes/`
3. `EVAL.md` 跑 A/B 测评，delta 必须 ≥ +25
4. 7 条设计原则的 self-check

会主动拒绝的几类：
- 回忆录 / 小说 / 纯叙事书
- 已被 [bookforge-ai](https://github.com/bookforge-ai/bookforge-skills) 或 [booklib-ai](https://github.com/booklib-ai/skills) 做过的领域
- summary 风格的提案（一本书 + 5 个 tips）

v1.0 前先做 10 本「种子书」再开放外部 PR。

---

## 支持

如果这个 repo 帮你少回来找它一次：

[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-☕-yellow?style=for-the-badge)](https://www.buymeacoffee.com/zhichao1208)
[![GitHub Sponsors](https://img.shields.io/badge/GitHub%20Sponsors-♥-ea4aaa?style=for-the-badge)](https://github.com/sponsors/zhichao1208)

完全自愿。repo 永远免费、开源。

### Star History

[![Star History Chart](https://api.star-history.com/svg?repos=zhichao1208/distill-books&type=Date)](https://star-history.com/#zhichao1208/distill-books&Date)

如果方向你认可，加个 star 让别人也看见。

---

## License

[CC BY-SA 4.0](LICENSE)。本 repo 的编辑性内容 + AI 交互设计部分。  
书的版权归作者和出版社。下架请求 24 小时内处理。

---

*v0.2.1 · 2026-05-24 · 2 本试点 · 英文主版 + 中文 mirror · boot + every-reply 实现层规则就位*
