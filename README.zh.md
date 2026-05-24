# distill-books

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-v0.4.0-orange.svg)](#roadmap)
[![Books](https://img.shields.io/badge/books-10-purple.svg)](#书目已发--计划)
[![Seed Slate](https://img.shields.io/badge/种子-完成-success.svg)](BOOKS.md)
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
- [Meta skill（这个 repo 的核心 IP）](#meta-skill这个-repo-的核心-ip)
- [30 秒上手](#30-秒上手)
- [书目（已发 + 计划）](#书目已发--计划)
- [什么时候**不**要用](#什么时候不要用)
- [测评数据 (v0.1)](#测评数据-v01)
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

## Meta skill（这个 repo 的核心 IP）

这个 repo 真正的资产不是一本本书，是 **meta-skill** —— 每个 per-book skill 都按这个 blueprint 实现。这个 blueprint 让一个 distill skill 和一个普通的「请扮演 Atomic Habits 教练」prompt 行为不一样。

Blueprint 的 9 条：

1. **状态优先** —— 输出之前先判断用户当下状态（curious / stuck / lapse / vulnerable / urgent / quick_q）。给错了对象，再正确的方法也是伤害。
2. **主动 boot** —— skill 加载完立即输出 3 阶段流程预期 + 3 个启动路径（贴 memory / 选情境 / 直接说）。永远不等用户先想"怎么开口"。
3. **零问题开局** —— 前 3 步零疑问句。用身体动作代替问题。
4. **一本书 = 一把 lens** —— 每个 cold-start 只携带 ≤2 个该书独有的关键词 lens（AH = identity vote + atomic；PoM = wealth-invisible + enough）。lens 不在书之间互通。
5. **借势 memory 透明** —— 用用户 memory 里的信息可以，但必须明说："我看到你 memory 里写了 ..."
6. **每条回应都有下一步** —— 具体动作 / YES-NO / 重入 / 危机转介。绝不"加油"。
7. **硬 not_for** —— skill 边界外的情境，主动转介真人或专业服务。不假装能帮。
8. **可逆性显眼** —— 每个建议旁边明示「跳过 / 改方向 / 撤销」的话术。
9. **Extension test** —— 让用户更依赖的 skill 不发布。少回来一次才是目标。

（第 1、3、5、6、7、8、9 条来自 [docs/ai-interaction-philosophy.md](docs/ai-interaction-philosophy.md) 里的 7 条哲学原则。第 2 和第 6 是实现层补充，详见各 [SKILL.md](books/atomic-habits/SKILL.md)。一起构成每本新书签约时认的"operating contract"。）

**为什么这是项目主 IP**：市面上已经有几个"书→AI skill" repo（[booklib-ai](https://github.com/booklib-ai/skills)、[bookforge-ai](https://github.com/bookforge-ai/bookforge-skills)、[book2skills](https://github.com/simbajigege/book2skills) 等）。差异化不在书目本身——在 skill 在压力情境下的行为是否"人性化"：脆弱用户、要求越权建议、心理脆弱状态。Meta skill 就是那道试金石。

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

## 书目（已发 + 计划）

| # | 书 | 核心 lens | 状态 | 详情 |
|---|---|---|---|---|
| 1 | **Atomic Habits** · James Clear (2018) | identity vote + atomic unit | ✓ v0.2 (delta +54.3) | [→ BOOKS](BOOKS.md#1-atomic-habits--james-clear-2018) |
| 2 | **The Psychology of Money** · Morgan Housel (2020) | wealth-invisible + enough + tail events + room for error | ✓ v0.2 (delta +34.3) | [→ BOOKS](BOOKS.md#2-the-psychology-of-money--morgan-housel-2020) |
| 3 | **Deep Work** · Cal Newport (2016) | shallow audit + 4 调度哲学 | ✓ v0.2.3（待测评） | [→ BOOKS](BOOKS.md#3-deep-work--cal-newport-2016) |
| 4 | **Outlive** · Peter Attia (2023) | Medicine 3.0 + Centenarian Decathlon | ✓ v0.2.4（医疗警告显眼） | [→ BOOKS](BOOKS.md#4-outlive--peter-attia-md-2023) |
| 5 | **Tiny Habits** · BJ Fogg (2019) | celebration as engine + B = MAP | ✓ v0.3 | [→ BOOKS](BOOKS.md#5-tiny-habits--bj-fogg-2019) |
| 6 | **Mindset** · Carol S. Dweck (2006/2016) | fixed-vs-growth + "yet" + honest-scope warning | ✓ v0.3 | [→ BOOKS](BOOKS.md#6-mindset--carol-s-dweck-2006-updated-2016) |
| 7 | **Why We Sleep** · Matthew Walker (2017) | 睡眠操作核心 + 对 Walker overclaim 的诚实 | ✓ v0.4（honest-scope）| [→ BOOKS](BOOKS.md#7-why-we-sleep--matthew-walker-2017) |
| 8 | **Stolen Focus** · Johann Hari (2022) | 注意力被集体偷走；诊断不操作 | ✓ v0.4（cite-researchers）| [→ BOOKS](BOOKS.md#8-stolen-focus--johann-hari-2022) |
| 9 | **Die With Zero** · Bill Perkins (2020) | 反 PoM；只给 over-savers | ✓ v0.4（wrong-reader 路由）| [→ BOOKS](BOOKS.md#9-die-with-zero--bill-perkins-2020) |
| 10 | **The Let Them Theory** · Mel Robbins (2024) | "Let them / Let me" 认知中断 | ✓ v0.4（refusal-when-wrong 设计）| [→ BOOKS](BOOKS.md#10-the-let-them-theory--mel-robbins-2024) |

完整 per-book 内容（介绍 / 影响 / 特点 / 用法 / 期待）见 [**BOOKS.md**](BOOKS.md)（英文），含 10 本种子书的 archetype 平衡逻辑 + 不做哪几类书。

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

## Roadmap

- [x] **v0.1** — 框架就位 · 2 本试点 · A/B 测评机制（6 场景）· 7 条设计原则
- [x] **v0.1.5** — Boot 主动启动 + 3 路径 + 预期管理 · Every-reply destination close 硬规则 · 清 cliché
- [x] **v0.2.0** — 全部 deliverable 改成英文为主 · Demo gif 录制脚本 · 更新 README hook
- [x] **v0.2.1** — README 中英双语
- [x] **v0.2.2** — Meta-skill blueprint 上升为 repo 主 IP · 书目内容折叠到 [BOOKS.md](BOOKS.md) · 10 本种子 slate（archetype 平衡）
- [x] **v0.2.3** — 第 3 本上线：[Deep Work](books/deep-work/SKILL.md)（cognitive/focus archetype）· 10 本方法论的 Phase 3 · Outlive proposal 已定
- [x] **v0.2.4** — 第 4 本上线：[Outlive](books/outlive/SKILL.md)（health archetype，boot 顶部显眼医疗警告，急救词在 boot 之前先拦）· EVAL.md 不再是必需 artifact（用户测试就是质量门）；CONTRIBUTING 已更新
- [x] **v0.3.0** — 第 5 + 6 本上线：[Tiny Habits](books/tiny-habits/SKILL.md)（celebration-as-engine，与 Atomic Habits 形成对照）+ [Mindset](books/mindset/SKILL.md)（honest-scope-warning 设计，正面引用 Sisk 2018 / Yeager 2019 学术批评）· **Hybrid 方法验证**：研究 agent 并行跑 + 我写 SKILL.md + 你测。10 本种子 slate 走完一半
- [x] **v0.4.0** — **10 本种子 slate 完成。** 一轮 ship 4 本（Why We Sleep, Stolen Focus, Die With Zero, The Let Them Theory），用 4 个并行 research agent + 我写 SKILL.md。Slate 横跨 5 个 archetype，每个 2 本。**6 个 honest-scope / safety 设计**（Outlive 医疗 / Mindset 学术批评 / Why We Sleep Guzey 批评 / Stolen Focus 引用底层研究者 / Die With Zero 错误读者路由 / Let Them 安全拒绝）—— 这是 repo 与其它 book-to-skill 项目的最强差异化
- [ ] **v0.5** — 第一个 `packages/` bundle（拟选 midlife-health-pack）· 开始接受外部贡献者 PR · 用户可选自带 API key 跑真测评
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

*v0.4.0 · 2026-05-24 · **10 本种子 slate 完成** · 5 archetype × 2 本 · 6 个 honest-scope 设计 · hybrid 方法规模化验证*
