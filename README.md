# distill-books

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-v0.5.0-orange.svg)](#roadmap)
[![Books](https://img.shields.io/badge/books-20-purple.svg)](BOOKS.md)
[![Archetypes](https://img.shields.io/badge/archetypes-10-success.svg)](BOOKS.md)
[![Setup](https://img.shields.io/badge/setup-zero-brightgreen.svg)](#30-second-quickstart)
[![Sponsor](https://img.shields.io/badge/sponsor-☕-pink.svg)](https://www.buymeacoffee.com/zhichao1208)

**English** · [中文](README.zh.md)

> 6 months ago you finished *Atomic Habits*. Right now you're about to skip the workout, again. The whole book was about exactly this moment. None of it shows up.

That gap is what this repo closes.

---

## Table of Contents

- [What it is](#what-it-is)
- [Why this exists](#why-this-exists)
- [The meta-skill](#the-meta-skill)
- [30-second quickstart](#30-second-quickstart)
- [Books (current + planned)](#books-current--planned)
- [When **not** to use](#when-not-to-use)
- [Eval data (v0.1)](#eval-data-v01)
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

## The meta-skill

The IP of this repo isn't the individual books. It's the **meta-skill** — one blueprint that every per-book skill implements. The meta-skill is what makes a distill skill behave differently from a generic "act like Atomic Habits coach" prompt.

The blueprint, in 9 points:

1. **State-first reading** — before any output, classify the user's state (curious / stuck / lapse / vulnerable / urgent / quick_q). Wrong recipient turns even the right method into harm.
2. **Active boot** — on load, output a 3-stage expectation and 3 entry paths (paste memory / pick scenario / just speak). Never wait for the user to figure out how to start.
3. **No-question opening** — first 3 turns contain zero questions. Body action instead.
4. **One book = one lens** — each cold-start carries ≤2 keyword lenses unique to that book (AH = identity vote + atomic; PoM = wealth-invisible + enough). Lenses don't transfer between books.
5. **Memory borrow transparent** — using the user's stored context is allowed, but announced: "I see in your memory that ..."
6. **Every reply has a next step** — concrete action / YES-NO / re-entry / crisis routing. Never "you got this."
7. **Hard not_for** — when a situation is outside the skill's competence, route to a real human or professional service. Don't fake helpfulness.
8. **Reversibility visible** — every suggestion is shown next to its skip / redirect / undo phrasing.
9. **Extension test** — a skill that makes the user more dependent doesn't ship. Fewer return visits is the goal.

(Points 1, 3, 5, 6, 7, 8, 9 derive from the 7 philosophical principles in [docs/ai-interaction-philosophy.md](docs/ai-interaction-philosophy.md). Points 2 and 6 are implementation-layer additions documented in detail in each [SKILL.md](books/atomic-habits/SKILL.md). Together they form the operating contract every new book signs.)

**Why this is the project's main IP**: there are several "book → AI skill" repos in the wild ([booklib-ai](https://github.com/booklib-ai/skills), [bookforge-ai](https://github.com/bookforge-ai/bookforge-skills), [book2skills](https://github.com/simbajigege/book2skills), and others). The differentiator isn't the books — it's whether the resulting skills behave humanely under pressure: vulnerable users, demand for unauthorized advice, fragile psychological state. The meta-skill is the test.

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

## Books (current + planned)

| # | Book | Core lens | Status | Detail |
|---|---|---|---|---|
| 1 | **Atomic Habits** · James Clear (2018) | identity vote + atomic unit | ✓ v0.2 (delta +54.3) | [→ BOOKS#atomic-habits](BOOKS.md#1-atomic-habits--james-clear-2018) |
| 2 | **The Psychology of Money** · Morgan Housel (2020) | wealth-invisible + enough + tail events + room for error | ✓ v0.2 (delta +34.3) | [→ BOOKS#psychology-of-money](BOOKS.md#2-the-psychology-of-money--morgan-housel-2020) |
| 3 | **Deep Work** · Cal Newport (2016) | shallow audit + 4 scheduling philosophies | ✓ v0.2.3 (pre-eval) | [→ BOOKS#deep-work](BOOKS.md#3-deep-work--cal-newport-2016) |
| 4 | **Outlive** · Peter Attia (2023) | Medicine 3.0 + Centenarian Decathlon | ✓ v0.2.4 (medical-warning-prominent) | [→ BOOKS#outlive](BOOKS.md#4-outlive--peter-attia-md-2023) |
| 5 | **Tiny Habits** · BJ Fogg (2019) | celebration as engine + B = MAP | ✓ v0.3 | [→ BOOKS#tiny-habits](BOOKS.md#5-tiny-habits--bj-fogg-2019) |
| 6 | **Mindset** · Carol S. Dweck (2006/2016) | fixed-vs-growth detection + "yet" + honest-scope warning | ✓ v0.3 | [→ BOOKS#mindset](BOOKS.md#6-mindset--carol-s-dweck-2006-updated-2016) |
| 7 | **Why We Sleep** · Matthew Walker (2017) | sleep tactics that hold up + honest scope re Walker's overclaims | ✓ v0.4 (honest-scope) | [→ BOOKS#why-we-sleep](BOOKS.md#7-why-we-sleep--matthew-walker-2017) |
| 8 | **Stolen Focus** · Johann Hari (2022) | attention as collectively stolen; diagnostic-not-operational | ✓ v0.4 (cite-researchers approach) | [→ BOOKS#stolen-focus](BOOKS.md#8-stolen-focus--johann-hari-2022) |
| 9 | **Die With Zero** · Bill Perkins (2020) | counter-frame to PoM; over-savers only | ✓ v0.4 (wrong-reader routing) | [→ BOOKS#die-with-zero](BOOKS.md#9-die-with-zero--bill-perkins-2020) |
| 10 | **The Let Them Theory** · Mel Robbins (2024) | "Let them / Let me" cognitive interrupt; narrower skill | ✓ v0.4 (refusal-when-wrong design) | [→ BOOKS#let-them-theory](BOOKS.md#10-the-let-them-theory--mel-robbins-2024) |
| 11 | **The Power of Habit** · Charles Duhigg (2012) | Habit Loop + Golden Rule (swap routine; keep cue + reward) | ✓ v0.5 (ego-depletion honest) | [→ BOOKS#11](BOOKS.md#11-the-power-of-habit--charles-duhigg-2012) |
| 12 | **Thinking, Fast and Slow** · Daniel Kahneman (2011) | System 1/2 + bias catalog (replication-aware) | ✓ v0.5 (Kahneman 2017 retraction integrated) | [→ BOOKS#12](BOOKS.md#12-thinking-fast-and-slow--daniel-kahneman-2011) |
| 13 | **Range** · David Epstein (2019) | Kind vs wicked + match quality + late-specialization | ✓ v0.5 (survivorship-bias honest) | [→ BOOKS#13](BOOKS.md#13-range--david-epstein-2019) |
| 14 | **So Good They Can't Ignore You** · Cal Newport (2012) | Passion is output not input + Career Capital | ✓ v0.5 (Law of Financial Viability) | [→ BOOKS#14](BOOKS.md#14-so-good-they-cant-ignore-you--cal-newport-2012) |
| 15 | **Crucial Conversations** · Patterson et al. (2002/2021) | STATE script + Path to Action | ✓ v0.5 (corporate-pitch honest) | [→ BOOKS#15](BOOKS.md#15-crucial-conversations--patterson--grenny--mcmillan--switzler-2002-3rd-ed-2021) |
| 16 | **Nonviolent Communication** · Marshall B. Rosenberg (2003) | OFNR template (Observation/Feeling/Need/Request) | ✓ v0.5 (power-imbalance refusal) | [→ BOOKS#16](BOOKS.md#16-nonviolent-communication--marshall-b-rosenberg-2003-3rd-ed-2015) |
| 17 | **Daring Greatly** · Brené Brown (2012) | Vulnerability redefined + shame resilience | ✓ v0.5 (Vulnerability Inc. critique) | [→ BOOKS#17](BOOKS.md#17-daring-greatly--brené-brown-2012) |
| 18 | **The Whole-Brain Child** · Siegel & Bryson (2011) | Connect-before-redirect + "name it to tame it" | ✓ v0.5 (neuroscience-simplification honest) | [→ BOOKS#18](BOOKS.md#18-the-whole-brain-child--daniel-j-siegel--tina-payne-bryson-2011) |
| 19 | **Decisive** · Heath brothers (2013) | WRAP framework + 4 villains of decision-making | ✓ v0.5 (opinion-on-when-WRAP-applies) | [→ BOOKS#19](BOOKS.md#19-decisive--chip-heath--dan-heath-2013) |
| 20 | **Thinking in Bets** · Annie Duke (2018) | Resulting + calibrated confidence + bet framing | ✓ v0.5 (pairs with Decisive) | [→ BOOKS#20](BOOKS.md#20-thinking-in-bets--annie-duke-2018) |

Full per-book entries (intro / reach / what's distinctive / when to copy / what you get) live in [**BOOKS.md**](BOOKS.md), including archetype rationale for the 10-book seed slate and what we will *not* ship.

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

## Roadmap

- [x] **v0.1** — Framework in place · 2 pilot books · A/B eval mechanism (6 scenarios) · 7 design principles
- [x] **v0.1.5** — Boot active start (3 paths, expectation management) · Every-reply destination close as hard rule · Cliché clean
- [x] **v0.2.0** — English as the primary language for all deliverables · Demo gif script · Updated README hook
- [x] **v0.2.1** — README bilingual (English primary + Chinese mirror)
- [x] **v0.2.2** — Meta-skill blueprint surfaced as repo's main IP · Book detail folded into [BOOKS.md](BOOKS.md) · 10-book seed slate planned with archetype balance
- [x] **v0.2.3** — Third book shipped: [Deep Work](books/deep-work/SKILL.md) (cognitive/focus archetype) · Phase 3 of 10-book methodology · Outlive proposal locked
- [x] **v0.2.4** — Fourth book shipped: [Outlive](books/outlive/SKILL.md) (health archetype, medical-warning-prominent in boot, emergency-detection before boot) · EVAL.md dropped as required artifact going forward (user testing IS the gate now); CONTRIBUTING updated
- [x] **v0.3.0** — Fifth + sixth books shipped: [Tiny Habits](books/tiny-habits/SKILL.md) (celebration-as-engine, contrasts Atomic Habits) + [Mindset](books/mindset/SKILL.md) (honest-scope-warning design, openly cites Sisk 2018 / Yeager 2019 critiques). **Hybrid methodology validated**: research-only agents (in parallel) + I write SKILL.md + user tests. Halfway through 10-book seed slate.
- [x] **v0.4.0** — **10-BOOK SEED SLATE COMPLETE.** Shipped 4 books in one round (Why We Sleep, Stolen Focus, Die With Zero, The Let Them Theory) using 4 parallel research agents + me writing SKILL.md. Slate now spans 5 archetypes with 2 books each. **Six honest-scope / safety designs across the slate** (Outlive medical / Mindset academic critique / Why We Sleep Guzey critique / Stolen Focus researcher-citing / Die With Zero wrong-reader-routing / Let Them safety-refusal). This is the repo's most distinctive feature vs other book-to-skill projects.
- [x] **v0.5.0** — **BATCH 2: 10 more books = 20-BOOK SHELF.** Shipped Power of Habit, Thinking Fast and Slow, Range, So Good They Can't Ignore You, Crucial Conversations, Nonviolent Communication, Daring Greatly, Whole-Brain Child, Decisive, Thinking in Bets. 5 NEW archetypes added (Career, Communication, Vulnerability, Parenting, Decision-making). 10 parallel research agents + me writing SKILL.md. Nearly every skill in 20-book shelf carries honest-scope design (ego depletion retraction / Kahneman priming retraction / survivorship bias / corporate-pitch flag / power-imbalance refusal / Vulnerability Inc. critique / neuroscience simplification flag / etc.). **Scenes deferred to v0.5.1** — SKILL.md + source-notes shipped; scene depth files coming next round.
- [ ] **v0.5.1** — Scene files for all 10 batch-2 books (2 scenes each, ~20 files) + scene files for the 4 batch-1 books that had only stub scenes. Bring scenes to parity with batch-1 books.
- [ ] **v0.6** — First `packages/` bundle (midlife-health-pack = Outlive + Why We Sleep + Atomic Habits) · external contributor PRs accepted
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

*v0.5.0 · 2026-05-24 · **20-book shelf** · 10 archetypes covered · honest-scope nearly every skill · hybrid methodology shipped 10 books in one round*
