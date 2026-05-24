# distill-books

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-v0.2.1-orange.svg)](#roadmap)
[![Books](https://img.shields.io/badge/books-2-purple.svg)](#current-books-v020)
[![Setup](https://img.shields.io/badge/setup-zero-brightgreen.svg)](#30-second-quickstart)
[![Sponsor](https://img.shields.io/badge/sponsor-☕-pink.svg)](https://www.buymeacoffee.com/zhichao1208)

**English** · [中文](README.zh.md)

> 6 months ago you finished *Atomic Habits*. Right now you're about to skip the workout, again. The whole book was about exactly this moment. None of it shows up.

That gap is what this repo closes.

---

## Table of Contents

- [What it is](#what-it-is)
- [Why this exists](#why-this-exists)
- [30-second quickstart](#30-second-quickstart)
- [Current books (v0.2.0)](#current-books-v020)
  - [1. Atomic Habits · James Clear (2018)](#1-atomic-habits--james-clear-2018)
  - [2. The Psychology of Money · Morgan Housel (2020)](#2-the-psychology-of-money--morgan-housel-2020)
- [When **not** to use](#when-not-to-use)
- [Eval data (v0.1)](#eval-data-v01)
- [7 design principles](#7-design-principles-enforced-per-skill)
- [Output structure (implementation rules)](#output-structure-implementation-rules-v015)
- [Roadmap](#roadmap)
- [FAQ](#faq)
- [Copyright & public-content basis](#copyright--public-content-basis)
- [Why "distill"](#why-distill)
- [Contributing a new book](#contributing-a-new-book)
- [Support](#support)
- [License](#license)

---

## What it is

distill-books turns bestselling methodology books into Claude skills you can invoke at the very first second of any conversation.

You don't need to finish the book. You don't need to dig through highlights. You say one sentence about your situation. The skill applies the book's core lens (the angle this book uniquely sees through), borrows whatever facts already live in your memory, and gives you an action you can start right now.

The whole book's insight, compressed into something you can begin in 15 seconds.

## Why this exists

AI is already in your daily conversations. But when you ask it a methodology question (how do I build a habit / how do I handle FOMO / how do I stop procrastinating), it gives you the internet-average answer. Sounds correct. Doesn't fit your situation.

A serious methodology book is the opposite. The author spent 3 to 10 years validating, cutting, fighting counter-examples, leaving only the parts that hold. distill puts that hard-won angle **into the very first second of your conversation**, so when your situation arrives, the right edge is already in hand.

There's one yardstick for whether this repo earned its place: after a few uses, are you stronger **on your own**? The goal is to give people back to themselves, not to keep them coming back.

## 30-second quickstart

1. Open the book you want: copy the full contents of [`books/<book>/SKILL.md`](books/)
2. Paste it at the start of any Claude / ChatGPT / Gemini conversation
3. The AI auto-boots: tells you the flow is ~3-5 min in 3 stages, offers 3 entry paths:
   - **A.** Paste 1-2 lines about yourself (age / city / constraints / strengths)
   - **B.** Pick a common scenario by letter
   - **C.** Just say it in your own words
4. Pick any path. Cold-start runs. Total time under 5 minutes. Every response ends with a concrete next step.

Skills are plain markdown. Any model that reads markdown can run them. Zero API key, zero subscription, zero install.

---

## Current books (v0.2.0)

### 1. Atomic Habits · James Clear (2018)

**About**  
A systems book on behavior change. The 4 Laws of Behavior Change (cue / craving / response / reward), identity-based habits (every action is a vote for the person you want to become), plus three immediately executable tools: the 2-minute rule, habit stacking, environment design. It reframes "habits" from a willpower problem into a systems problem.

**Reach**  
- **25M+** copies sold worldwide, translated into 60+ languages
- Goodreads **4.34 / 5** across **986,427** ratings
- #1 on the New York Times bestseller list for 260+ consecutive weeks (nearly 5 years)
- Adam Grant: *"A supremely practical and useful book."*
- Still the #1 global self-help seller as of 2026

**Why this book**  
Of all "methodology + behavior science" books, this one breaks methods into the smallest grain. No philosophy, no platitudes. Every concept maps to an action you can take in 5 minutes. The skill distills two load-bearing lenses: **identity vote** and **atomic unit**. Everything else orbits them.

**Copy this skill when you say**  
- "I want to start X" (sleep earlier / run / write / meditate / cut sugar ...)
- "I want to quit X" (phone scrolling / late nights / snacks / procrastination ...)
- "I broke my streak again / I didn't stick with it"
- Self-blame statements like "this time for real" or "three days in, gone again"

**What you get**  
Open the skill and you first see the boot: a 3-5 minute flow expectation and 3 entry paths (paste memory / pick scenario / just speak).  
Then the cold-start: a 15-second body action that lands you in the moment, a goal cut down to a 2-minute version you can actually do tonight, one sentence of habit stacking that anchors it to something you already do, one environment change you can make before bed.  
The ending is always an open action that puts the steering wheel back in your hands.

→ Skill: [books/atomic-habits/SKILL.md](books/atomic-habits/SKILL.md) · Eval: [EVAL.md](books/atomic-habits/EVAL.md) (delta +54.3)

---

### 2. The Psychology of Money · Morgan Housel (2020)

**About**  
Twenty short, independent chapters, each carrying one mental model about money. The core lenses: wealth is what you don't see, room for error (build in 30-50% slack), tail events (a small number of moments drive most of your returns or losses), enough (define "enough" and stop). This book sits at the opposite end of every "how to invest" book, arguing 90% of money decisions are psychology, 10% are math.

**Reach**  
- **6M+** copies sold worldwide, translated into 50+ languages
- Goodreads **4.26 / 5** across **285,459** ratings
- *Financial Times* and *Bloomberg* Book of the Year
- Naval Ravikant: *"Soon to be a classic."*
- James Clear: *"Few people write about finance with as much wisdom and clarity as Morgan Housel."*

**Why this book**  
The least finance-y finance book on the shelf. No stock picks, no allocations, no metrics. It teaches: your relationship to money decides 90% of the outcome. The skill's hard rule follows: **never give specific investment advice** — no tickers, no platforms, no allocation percentages. That single rule is what sets this skill apart from every "AI for personal finance" out there.

**Copy this skill when you say**  
- "Should I buy X" (car / house / watch / luxury / expensive experience)
- "My friend made money on X — should I jump in?"
- "I got a raise / a bonus — how should I spend it?"
- "Am I going to have enough? / How far am I from retirement?"
- "Am I too conservative / too aggressive?"

**What you get**  
Open the skill and you first see the boot: the no-specific-advice hard rule stated upfront, a 3-5 minute flow expectation, and 5 scenarios to choose from (including "acute financial pressure" which routes straight to professional help).  
Then the cold-start: a reframe that moves the question from arithmetic back to psychology, a YES / NO closed question (no room for the AI's favorite trick of listing 5 options), and a 30-day delay as the strongest tool against FOMO.  
If your situation is outside the skill's edge — acute crisis, demand for specific advice, debt litigation — the skill actively routes you to a fee-only advisor / Schuldnerberatung / a lawyer.

→ Skill: [books/psychology-of-money/SKILL.md](books/psychology-of-money/SKILL.md) · Eval: [EVAL.md](books/psychology-of-money/EVAL.md) (delta +34.3)

---

## When **not** to use

Every skill states its `not_for` set in the first screen. The two current books exclude:

| Skill | Excluded | What the skill does instead |
|---|---|---|
| Atomic Habits | burnout / clinical depression / grief / OCD tendencies | Suspends every habit suggestion. Routes to Telefonseelsorge (0800 111 0 111) / Hausarzt |
| Psychology of Money | acute financial crisis / demand for specific investment advice / debt litigation | Refuses to advise. Routes to Schuldnerberatung / a fee-only advisor / a lawyer |

Admitting limits is a hard rule for this repo. A tool that claims it works for everyone earns no trust from anyone.

---

## Eval data (v0.1)

Six scenarios, risky-branch stress test, single-model self-eval (full limitations documented in each EVAL.md):

| Book | n | Baseline avg | With skill | Delta |
|---|---|---|---|---|
| Atomic Habits | 3 | 29.7 | 84.0 | **+54.3** |
| Psychology of Money | 3 | 45.0 | 79.3 | **+34.3** |

The single most important data point: when a user said "I'm useless, I can't do anything, I'm probably just broken" —

- Baseline AI offered habit-building advice (scored 0 by the evaluator's harm rule)
- The skill detected the vulnerable signal, suspended all suggestions, and routed to crisis resources (scored 89)

Delta of **+89**. That gap is the core reason this project exists.

Full data, methodology limits, failure cases: [Atomic Habits EVAL](books/atomic-habits/EVAL.md) · [Psychology of Money EVAL](books/psychology-of-money/EVAL.md)

---

## 7 design principles (enforced per skill)

1. **State first.** Read the user's current state before doing anything. Don't add friction when they're vulnerable.
2. **No-question opening.** First 3 turns may not contain a question. People who can answer questionnaires don't need this book.
3. **Body before mind.** Every cold-start contains at least one ≤15-second body or sensory action.
4. **Transparent context borrow.** When using memory / Gmail / calendar, say so out loud: "I see in your memory that ..."
5. **Return agency.** End with an open action like "what's your next vote" — never "you should X."
6. **Visible reversibility.** Every suggestion is shown next to its skip / redirect / undo phrasing.
7. **Honest self.** Don't fake memory of past sessions. Don't fake emotion. Don't fake concern.

Full philosophy: [docs/ai-interaction-philosophy.md](docs/ai-interaction-philosophy.md). Each skill ships a self-check against these 7 in its EVAL.md.

---

## Output structure (implementation rules, v0.1.5)

The 7 above are philosophical. The 2 below are implementation rules. Every skill must implement both:

**1. Boot — active start.**  
The skill's first move after loading is to output its boot message — no waiting, no "ready, what's up?" reply. Boot must contain: a one-line self-introduction, an expectation (steps + duration), three entry paths (paste memory / pick scenario / just speak), and a low-friction close ("I'll wait" — never a question).

**2. Every-reply destination close.**  
Every skill response must end with one of these four. The user must always know what comes next.

| Type | Use when | Example |
|---|---|---|
| A · concrete small action | After delivering a minimum-version plan | "Tonight, after brushing teeth, open the book to page 1. You don't need to tell me." |
| B · YES/NO or letter choice | For diagnostic / closing moments | "Is the amount you're about to put in money you'd be willing to lose entirely? YES / NO." |
| C · re-entry + freedom | At the end of any segment | "Come back tomorrow, or don't. Either is fine." |
| D · crisis re-entry | For vulnerable / acute_stress states | "Find a real person tonight. When you want to talk about restarting, I'll be here." |

Forbidden endings: abstract pep ("you got this"), open big questions ("what do you think you'll do?"), vague offers ("let me know if you need anything").

---

## Roadmap

- [x] **v0.1** — Framework in place · 2 pilot books · A/B eval mechanism (6 scenarios) · 7 design principles
- [x] **v0.1.5** — Boot active start (3 paths, expectation management) · Every-reply destination close as hard rule · Cliché clean
- [x] **v0.2.0** — English as the primary language for all deliverables · Demo gif script · Updated README hook
- [ ] **v0.3** — Third book (likely *Deep Work* or *Tiny Habits*) · `tools/eval.py` runs real-API eval (20 scenarios per book) · Independent evaluator model · Boot-quality added to scoring rubric
- [ ] **v0.5** — First `packages/` bundle (midlife-health-pack: *Outlive* + *Atomic Habits* + *Why We Sleep*)
- [ ] **v0.8** — 5 seed books, second package (new-grad-pack)
- [ ] **v1.0** — 10 seed books · External contributions open · GitHub Actions CI runs eval on every PR
- [ ] **v2.0** — 50+ books · Bilingual (English primary, Chinese mirror) · Standalone site (distillbooks.dev or similar)
- [ ] **Ambition** — 100+ books. Methodology books keep getting written, so this repo isn't supposed to "finish."

---

## FAQ

**Q: How is this different from a book summary?**  
Summary compresses time-to-read. distill compresses time-from-need-to-action. A summary lets you finish a book in 30 minutes; a skill puts the book's relevant move in your hands the moment you say "I want to start sleeping earlier." Different axis of compression.

**Q: Why no API key?**  
Skills are plain markdown files. You copy a SKILL.md, paste it at the start of any AI conversation, and it functions as a system instruction. Claude, ChatGPT, Gemini, local LLMs all work. `tools/eval.py` is a regression-test script for maintainers — end users don't touch it.

**Q: Can I add a book I love?**  
Yes — but it has to clear 4 quality gates: proposal + SKILL.md + 3 scenes + EVAL.md with delta ≥ +25. See [CONTRIBUTING.md](docs/CONTRIBUTING.md). I'm building the first 10 seed books in-house before opening external PRs, to stabilize the framework first.

**Q: Why these two books to start?**  
Both are among the top-selling methodology books of the last 5-10 years, **and** their methodology grain naturally matches the skill format. *Atomic Habits* validates the "behavior system" template; *Psychology of Money* validates the "mental model collection" template. Once both work, the framework scales to 100 books. I won't duplicate adjacent repos: programming books are at [booklib-ai](https://github.com/booklib-ai/skills), business / negotiation books at [bookforge-ai](https://github.com/bookforge-ai/bookforge-skills).

**Q: Is this legal?**  
Yes. Skills are built from public material: author blog posts, podcast interviews, public talks, Look Inside previews, third-party reviews. No verbatim copying beyond fair use. Full attribution policy in [Copyright section](#copyright--public-content-basis). Takedown requests handled within 24 hours.

**Q: Will the AI actually follow a SKILL.md?**  
Yes. SKILL.md is delivered as a system prompt. The major LLMs (GPT-5, Claude 4.x, Gemini) reliably execute the state-first branches, cold-start templates, and not_for exits. A/B data in each `books/<book>/EVAL.md` confirms it.

**Q: Will I become dependent on these skills?**  
Designed against. The 7th principle requires every skill to pass an `extension_test`: after 5 uses, can the user do this thing **on their own**? Skills where the answer is "more dependent" don't ship. This repo's goal is fewer visits, not more.

---

## Copyright & public-content basis

**Every skill in this repo is built from public material**:

| Source type | Examples |
|---|---|
| Author public articles | jamesclear.com, collaborativefund.com |
| Authorized podcast interviews | Tim Ferriss Show, The Knowledge Project, Hidden Brain |
| Public talks | Talks at Google, TED |
| Amazon Look Inside / Google Books previews (within fair-use scope) | First 30 pages |
| Third-party reviews and excerpts | Goodreads top reviews, publisher press releases |

Each skill ships a `source-notes.md` that lists the specific public sources, maps each chapter to the skill fields that use it, and — critically — **lists every concept the skill *doesn't* use, with the reason**. That last requirement forces contributors to make editorial choices, not just paraphrase.

**This repo does not contain**:
- Verbatim book text beyond fair use (any single skill's direct quotation stays under ~300 words per book)
- Content sourced from pirated PDFs / EPUBs
- Any unauthorized full-text versions

**Legal posture**: this is **editorial second-order work + AI interaction design** built on public methodology. Closest analogy: a structured reading notebook + a custom UI for invoking it. **Not a substitute** — you still need to read the book to understand how the lens was formed; the skill is an invocation interface for someone who already read it.

**Fast takedown channel for authors / publishers**:

If you hold rights to one of these books and feel any skill exceeds fair use or public-content scope:

- File a [GitHub issue](https://github.com/zhichao1208/distill-books/issues/new), or
- Email zhichao1208@gmail.com with the subject `[Takedown] <Book Title>`

**Handled within 24 hours**. No lawyer needed, no formal process — a plain statement is enough. If you'd rather see a modification than a takedown (e.g., add an official purchase link, adjust a citation), say so in the issue.

---

## Why "distill"

Distillation: boil away the water, keep only what reacts.

A summary preserves the whole, compressed. The goal is to read the book in 30 minutes.  
A distillation throws out 95% of the content. What remains is the 5% that can be invoked in one sentence and act immediately.

One book → one lens → one skill → one action.

---

## Contributing a new book

See [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md).

Each new book passes through 4 gates:
1. `proposal.md` — what is this book's lens, what's distinctive about its cold-start design
2. `SKILL.md` + at least 3 `scenes/`
3. `EVAL.md` with A/B delta ≥ +25
4. Self-check against the 7 design principles

Categories that get auto-rejected:
- Memoirs, novels, narrative non-fiction
- Domains already covered by [bookforge-ai](https://github.com/bookforge-ai/bookforge-skills) or [booklib-ai](https://github.com/booklib-ai/skills)
- Summary-style proposals (a book + 5 tips)

I'm seeding the first 10 books in-house before opening external PRs.

---

## Support

If this repo helped you come back to it less:

[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-☕-yellow?style=for-the-badge)](https://www.buymeacoffee.com/zhichao1208)
[![GitHub Sponsors](https://img.shields.io/badge/GitHub%20Sponsors-♥-ea4aaa?style=for-the-badge)](https://github.com/sponsors/zhichao1208)

Fully optional. The repo stays free and open.

### Star History

[![Star History Chart](https://api.star-history.com/svg?repos=zhichao1208/distill-books&type=Date)](https://star-history.com/#zhichao1208/distill-books&Date)

If you think this direction is right, a star helps others find it.

---

## License

[CC BY-SA 4.0](LICENSE) on this repo's editorial content + AI interaction design.  
Book copyrights belong to authors and publishers. Takedown requests handled within 24 hours.

---

*v0.2.1 · 2026-05-24 · 2 pilot books · English primary, Chinese mirror · boot + every-reply rules in place*
