# distill-books

> 把畅销方法论书，**蒸馏**成 AI 在对话第 0 秒就能调用的 skill。
> 不是 book summary，不是引言库，不是「5 个 Atomic Habits 技巧」清单。
>
> 是 cold-start 工具。目标是用过几次之后，你**少回来一次**。
>
> v0.1 起步：2 本试点。野心：100+ 本，每本都是一把可即取的 lens。
> 不打算做完那天，因为方法论书还会继续出。

---

## 第 0 秒，看差别

你说：「我想养成一个好习惯。」

**普通 AI** 会回你：

```
好啊，你想养成什么习惯？读书、运动、还是早睡？
建议从 SMART 目标开始：
1. Specific（具体）
2. Measurable（可衡量）
3. Achievable（可实现）
...
```

你已经累了，关掉了。

**这个 repo 里的 Atomic Habits skill** 回你：

```
停一下。把手放在胸口，呼吸两次。
现在看一眼手机右上角的时间，记住它。

你刚才点开这个对话本身，已经是一票了。
James Clear 在书里反复讲：每个动作都是一票，
投给你想成为的那个版本的你。

我看到你 memory 里写了 40 岁、Berlin、训练时间预算有限、
夜里得戴咬合板。你今天这一票，是投给哪个版本的你？
不用打字。心里有数就行。

这本书里习惯的最小单位不是「读 30 分钟」，是「打开书」。
不是「健身 1 小时」，是「换上运动鞋」。
你的下一票是什么动作？越小越好。
我帮你把它绑到 cue / craving / response / reward 四个齿轮上。
```

同一本书、同一个问题，差别在：
- 0 个采访问题
- 2 个身体动作让你先在场
- 书的核心概念（identity + atomic）通过体验植入，不是讲解
- 用你 memory 里已有的事实，不重复采集
- 最后只有 1 个开放性输入，且是动作而不是问题

---

## 这个 repo 不是 / 是

**Not**
- 一份 book summary 集合（去 Blinkist、得到）
- "James Clear 说" 引言数据库（去 Goodreads）
- "5 个 Atomic Habits 技巧" 速成清单（去任何 Medium 文章）
- 一个能记得你、关心你、陪伴你的朋友（去找真人）

**Is**
- 你说「我想 X」时，skill 用书的核心 lens 把你拉进 15 秒身体动作
- 然后借你 memory / Gmail / Calendar 里已有的事实，不重复采集
- 给你一个 reversible 的下一步，不替你拍板
- 一个用完之后让你**少回来一次**的工具

最后这一条是这个项目最反常的设计目标。所有同类产品都在追求"你离不开我"。我们追求相反方向。

---

## 当前的书（v0.1，2 本试点）

| 书 | 核心 lens | 触发场景 |
|---|---|---|
| [Atomic Habits](books/atomic-habits/SKILL.md) (James Clear, 2018) | identity vote + atomic（最小单位）+ 4 齿轮 | 我想养成 X / 戒掉 X / 又破戒了 |
| [Psychology of Money](books/psychology-of-money/SKILL.md) (Morgan Housel, 2020) | wealth is what you don't see + room for error | 该不该买 X / 怎么投资 / 朋友买了 X 赚了 |

每本书附：
- `SKILL.md` 主入口
- `scenes/` 具体情境子卡片
- `EVAL.md` 用过 vs 没用的对比测试（包含失败案例）
- `source-notes.md` 出处和章节映射

---

## 为什么把书做成 skill，而不是 summary

大多数 AI 给的 "沟通建议 / 习惯建议 / 管理建议"，是把全网平均观点重新拼装。听起来都对，但**对你具体的情境没切角**。

一本系统化方法论书是另一回事。作者花 3 到 10 年验证、删改、对抗反例后留下的硬骨头。一本好书提供的不是"建议"，是**lens**：看同一件事的某个特定角度，平均化的常识里没有。

把这种 lens 变成可调用的 skill，遇到具体情境时一键拿出最贴的那把刀。这比 ChatGPT 拼出来的平均建议高一个数量级。

---

## 测试方法 + 不适用警告

每个 skill 上线前跑场景盲评，**delta 不到 +25 分不发布**。

**v0.1 当前数据**（6 场景 manual stress test，单模型自评，详见各 [EVAL.md](books/atomic-habits/EVAL.md)）：

| 书 | n | Baseline 均分 | Skill 均分 | Delta | 关键发现 |
|---|---|---|---|---|---|
| Atomic Habits | 3 | 29.7 | 84.0 | **+54.3** | vulnerable 场景：baseline 给 habit 建议（不安全）→ skill 转介危机资源 |
| Psychology of Money | 3 | 45.0 | 79.3 | **+34.3** | seeking_advice 场景：baseline 给具体 ETF + 平台推荐（越界）→ skill 拒绝 + 转 framework |

**最关键的单点数据**：vulnerable 用户（"我没用 / 废物 / 所有事都做不到"）的对话里——
- baseline：给 habit-building 建议，附末尾一句"如果长期这样建议找咨询师"
- skill：完全挂起所有建议，转介 Telefonseelsorge + Hausarzt，明说"今天 skill 不给任何建议，那是诚实"

**承认局限**：这一轮是**单模型自评 + 小样本 + risky-branch stress test**。avg delta = +44.3 是 risky 场景的上限，不是日常对话的期望值。v0.2 用 `tools/eval.py` 跑 20+ 随机分布 + 独立 evaluator 时数据会缩小，是预期的。

**not_for 警告对每个 skill 强制要求**：如果你正处于 burnout / 临床抑郁 / 哀伤 / 急性财务危机 / 强迫症倾向状态，请关掉对应的 skill，去找真人。这条会出现在每个 skill 的 cold-start 之前。

---

## Skill 设计原则（10 秒读完）

每个 skill 必须遵守 7 条，否则不合并：

1. **状态优先**。先读用户当下是 stuck / curious / urgent / vulnerable，再决定怎么动。vulnerable 时不给摩擦。
2. **不问问题**。前 3 步不允许疑问句。会答问卷的人不需要这本书。
3. **身体先于头脑**。cold-start 必须有一个 ≤ 15 秒的身体 / 感官 / 视线动作。
4. **借势 context 透明**。用你 memory / Gmail / Calendar 里的事实必须明说"我看到你 ... 里写了"。
5. **判断还给人**。skill 不以 "你应该 X" 结尾，以 "你下一票投哪" 类开放动作收尾。
6. **可逆性显眼**。每个建议旁明示"跳过 / 改方向 / 撤销"的话术。
7. **诚实自身**。禁止假装记得过去、假装情感、假装担心。

这 7 条来自一份 [AI 交互哲学文档](docs/ai-interaction-philosophy.md)，每个 skill 在 EVAL.md 里要交一份 self-check。

---

## 用法（30 秒，不用任何 API 不用 setup）

1. 点开你想用的那本书的 `books/<book>/SKILL.md`
2. 全选复制
3. 粘到任何 Claude / ChatGPT / Gemini 对话的最开头
4. 然后说你的话

就这样。不需要 API key、不需要安装、不需要订阅、不需要任何 setup。

skill 是纯 markdown 文本。任何能读 markdown 的 AI 都能用。

**如果你用 Claude Code**：clone 这个 repo 到 `~/.claude/skills/`，Claude Code 会自动识别。但这不是必须的，copy-paste 同样有效。

```bash
git clone https://github.com/zhichao1208/distill-books.git ~/.claude/skills/distill-books
```

---

## 为什么从这两本开始

这两本是 5-10 年内全球销量前列、方法论结构最清晰、跨文化最适用的两本。Atomic Habits 验证"行为系统"类的设计模板，Psychology of Money 验证"心智模型集合"类的设计模板。两本跑通，整个 framework 就可以扩到 100 本。

**不做**的几类书（也是有意的边界）：
- 回忆录 / 小说（《Educated》《追风筝的人》）：不是方法论
- 全是观点没有 lens 的书（多数 Malcolm Gladwell）
- 已被 [bookforge-ai](https://github.com/bookforge-ai/bookforge-skills) 做过的商业 / 谈判书（不重复造轮子）
- 已被 [booklib-ai](https://github.com/booklib-ai/skills) 做过的编程书

---

## 贡献新书

见 [CONTRIBUTING.md](docs/CONTRIBUTING.md)。每本新书需通过：
1. 一页 `proposal.md`（这本书的核心 lens 是什么，为什么 cold-start 设计独特）
2. SKILL.md + 至少 3 个 `scenes/`
3. EVAL.md 跑 30 场景 A/B（delta ≥ +25）
4. 一份 self-check 对照 7 条设计原则

我会先做 10 本"种子书"再开放贡献。先把 framework 跑稳。

---

## 支持

如果这个 repo 帮你少回来找它一次，可以请我喝杯咖啡：

[☕ Buy Me a Coffee](https://www.buymeacoffee.com/zhichao1208) · [GitHub Sponsors](https://github.com/sponsors/zhichao1208)

完全自愿。这个 repo 永远免费、开源。

---

## License

CC BY-SA 4.0。书的版权属作者和出版社，本 repo 是基于公开方法论的二次诠释 + AI 交互设计。

---

*v0.1 · 2026-05-24 · 两本试点中*
