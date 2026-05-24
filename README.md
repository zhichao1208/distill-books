# distill-books

> 一本你读过的方法论书，下次真需要它的时候，你想得起来吗？

Atomic Habits 你 6 个月前读完。今天你说「我又破戒了」。  
脑子里只剩下「书里好像有一句话关于 ... 算了忘了」。

---

## 这是什么

distill-books 把畅销方法论书蒸馏成 AI 在对话第 0 秒就能调用的 skill。

你不用读完整本书。不用回去翻 highlight。说一句你的处境，skill 用书的核心 lens，加上你 memory 里已有的事实，直接给一个当下能用的动作。

整本书的洞察，重新变成一个 15 秒能开始的体验。

## 为什么这样做

AI 已经在你日常对话里了。但你问它一个方法论问题（怎么养成习惯 / 怎么应对 FOMO / 怎么处理拖延），它给的回答是把全网平均观点重新拼装。听起来都对，对你具体情境没切角。

一本系统化方法论书是另一回事。作者花 3 到 10 年验证、删改、对抗反例后留下的硬骨头。distill 让这种硬骨头**直接出现在你对话的第 0 秒**，遇到情境时一键拿出最贴的那把刀。

衡量这个 repo 价值的标准只有一个：用过几次之后，你**独自一人时是不是也更强了**。把人还给人自己。

## 30 秒上手（零 setup）

1. 打开你想用的那本书的 `books/<书名>/SKILL.md`
2. 全选复制
3. 粘到任何 Claude / ChatGPT / Gemini 对话开头
4. 然后说你想说的话

skill 是纯 markdown。任何能读 markdown 的 AI 都能用。零 API key、零订阅、零安装。

---

## 当前 2 本（v0.1）

### 1. Atomic Habits · James Clear (2018)

**介绍**  
关于行为改变的系统书。4 Laws of Behavior Change （cue / craving / response / reward）框架，identity-based habits（每个动作是给你想成为的人投的一票），以及 2-minute rule、habit stacking、environment design 三套可立即执行的工具。这本书把"习惯"从意志力问题重新定义为系统问题。

**影响**  
- 全球销量 **25M+**，翻译成 60+ 种语言
- Goodreads **4.34 / 5**，**986,427** 个评分
- 纽约时报畅销榜 #1 连续 260+ 周（近 5 年）
- Adam Grant: *"A supremely practical and useful book."*
- 截至 2026 年仍是 self-help 类全球销量第一

**特点**  
所有"方法论 + 行为科学"类书里方法颗粒度最细的一本。它不讲哲学，不讲鸡汤。每个概念都能在 5 分钟内做出一个动作。Skill 提炼的核心 lens 是两个词：**identity vote** 和 **atomic unit**。其它都是周边。

**什么时候 copy 这本 skill**  
- 「我想养成 X」（早睡 / 跑步 / 写日记 / 冥想 / 戒糖 ...）
- 「我想戒掉 X」（刷手机 / 熬夜 / 吃零食 / 拖延 ...）
- 「我又破戒了 / 没坚持下来」
- 「这次一定」「三天打鱼」类的自责语句

**你会得到什么**  
一段 15 秒身体动作，把你拉回当下。一个砍到 2 分钟的最小版本，把目标变成今晚能做的事。一句把它绑到你已有习惯的 habit stack。一个今晚就能做的环境改造。最后一个让你选下一票的开放动作，方向盘还你手里。

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
一段 reframe，把"算账题"重新放回"心态题"。一组只能选 YES / NO 的闭合问题，避开 AI 最擅长的"列 5 个建议"。一个 30 天延迟决定的反向出口，对抗 FOMO 的最强工具。如果你的状况超出 skill 边界（急性财务危机、想要具体投资建议、债务纠纷），skill 会**主动把你推到** Fee-only 财务顾问 / 德国 Schuldnerberatung / 律师。

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

完整哲学：[docs/ai-interaction-philosophy.md](docs/ai-interaction-philosophy.md)。每个 skill 在 EVAL.md 里要交一份对照 self-check。

---

## 为什么叫「distill」

蒸馏的意思：把整本书的水分蒸掉，留下能立刻起反应的浓缩物。

Summary 保留全貌、缩短篇幅，目标是 30 分钟读完一本书。  
Distill 丢掉 95% 内容，留下的 5% 能被一句话调用、当场起反应。

一本书 → 一把 lens → 一个 skill → 一个动作。

---

## 贡献新书

见 [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md)。

每本新书要通过 4 道关：
1. `proposal.md` — 这本书的 lens 是什么、cold-start 设计独特在哪
2. `SKILL.md` + 至少 3 个 `scenes/`
3. `EVAL.md` 跑 A/B 测评，delta 必须 ≥ +25
4. 7 条设计原则的 self-check

会主动拒绝的几类：
- 回忆录 / 小说 / 纯叙事书
- 已被 [bookforge-ai](https://github.com/bookforge-ai/bookforge-skills) 或 [booklib-ai](https://github.com/booklib-ai/skills) 做过的领域
- summary 风格的提案（一本书 + 5 个 tips）

我会先做 10 本「种子书」再开放外部贡献。

---

## 支持

如果这个 repo 帮你少回来找它一次：

[☕ Buy Me a Coffee](https://www.buymeacoffee.com/zhichao1208) · [GitHub Sponsors](https://github.com/sponsors/zhichao1208)

完全自愿。repo 永远免费、开源。

---

## License

CC BY-SA 4.0。书的版权属作者和出版社。本 repo 是基于公开方法论的编辑性重组 + AI 交互设计，不含原文复制。

---

*v0.1 · 2026-05-24 · 2 本试点，框架就位*
