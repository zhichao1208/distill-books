# Contributing a New Book

This repo is opinionated. Not every bestselling book deserves a skill, and not every skill is allowed to ship.

If you want to add a book, follow this.

---

## Step 0 — does this book belong here?

A book belongs here only if **all** of the following are true:

- It's a **methodology** book, not a memoir, narrative non-fiction, or pure opinion essay
- It has a **structured framework** with at least 1 lens that a generic AI doesn't already know
- The methodology has been **publicly validated** (sales 500k+ over 5+ years, or strong evidence base, or both)
- It doesn't already exist in [booklib-ai/skills](https://github.com/booklib-ai/skills) or [bookforge-ai/bookforge-skills](https://github.com/bookforge-ai/bookforge-skills) (avoid duplication)

**Examples that pass**: Deep Work, Tiny Habits, Outlive, Stolen Focus, The Power of Now, Mindset, Range, How to Change

**Examples that fail**:
- Educated (memoir)
- Sapiens (narrative, no methodology to call)
- The 7 Habits (already covered by other skill repos)
- Most Malcolm Gladwell (observation, no callable methodology)
- Anything that requires the user to read 400 pages before any step makes sense

---

## Step 1 — proposal.md

Before writing any skill, open an issue or write a `proposals/<slug>.md` with:

1. **Book** (title, author, year, sales)
2. **Core lens** — what specific angle does this book offer that GPT-5 / Claude doesn't already give?
3. **Why cold-start works** — what 15-second body action / sensory cue could embody this book's lens?
4. **3 trigger scenarios** — concrete user utterances that should call this skill
5. **Why not a summary** — what would a generic summary fail to do that this skill will succeed at?

A reviewer (currently @zhichao1208) reads it. If the lens isn't differentiated, the proposal is closed.

---

## Step 2 — write the skill

Copy `books/atomic-habits/` as template. Replace contents.

Required files per book:

```
books/<slug>/
├── SKILL.md          # main entry, follow Atomic Habits structure
├── EVAL.md           # A/B test results (see Step 4)
├── source-notes.md   # chapter → field mapping + non-use rationale
└── scenes/
    ├── <scene1>.md   # at least 3 concrete scenarios
    ├── <scene2>.md
    └── <scene3>.md
```

### SKILL.md required fields (frontmatter)

```yaml
---
name: <slug>
book: <Title> — <Author> (<Year>, <sales+>)
version: 0.1
description: |
  Bilingual (zh first, en second) auto-trigger description.
  Must mention: who, when, what lens, what NOT to do.

triggers:
  zh: [list]
  en: [list]

not_for:
  - <state/audience where this skill is harmful, with redirect>
  - ...

eval_summary:
  scenarios_tested: N
  delta_with_skill: +X.X
  significantly_useful: X%
  no_difference: X%
  harmful: X%
---
```

### SKILL.md required sections

1. **State-first** (5+ states, branch table)
2. **Cold-start** (3+ states' templates with: body action + lens keyword + memory borrow + open-ended close)
3. **Crisis/vulnerable exit** (mandatory, even if you think your book is "safe")
4. **Core method** (the book's actual framework, max 1 table or 5 bullets)
5. **Context borrowing rules** (what to borrow, how to disclose, what's forbidden)
6. **Scenes index**
7. **EVAL summary + link**
8. **Self-check against 7 principles** (table mapping principle → skill mechanism)
9. **Source notes link**

---

## Step 3 — 7 principles self-check

In SKILL.md, include a table:

| Principle | How this skill implements it |
|---|---|
| 1. State-first | ... |
| 2. No questions in first 3 steps | ... |
| 3. Body before mind | ... |
| 4. Transparent context borrow | ... |
| 5. Return agency | ... |
| 6. Visible reversibility | ... |
| 7. Honest self | ... |

If you can't fill in any row honestly, the skill isn't ready.

---

## Step 4 — User test (the actual quality gate)

After v0.2.4 we **stopped using formal A/B evals as the ship gate**. Reasons:

- Single-model self-eval is fundamentally circular (model favors its own writing style)
- Independent-evaluator runs cost real API spend with marginal signal
- The honest test is: does the skill behave humanely under pressure when a real user invokes it?

**The new ship gate**: a working "paste block" version of the skill, tested by the project owner across at least 5 risky-branch scenarios (must include `vulnerable` and `not_for` branches), in a fresh AI chat. If the skill misbehaves, fix the SKILL.md and re-test. Only ship when the risky branches behave as designed.

`tools/eval.py` and `tools/scenarios.json` are preserved for future regression testing once the skill set stabilizes, but **EVAL.md is no longer a required artifact** for new books.

Old EVAL.md files for Atomic Habits / Psychology of Money / Deep Work are kept as historical record of the methodology we explored.

Failure modes that still disqualify a skill from shipping (checked manually by the project owner during testing):

- The skill **deepens** a vulnerable user's distress instead of routing to professional help
- The skill gives advice the book explicitly cautions against (e.g. specific medical or investment recommendations)
- The skill pretends emotion / pretends memory of past sessions (violates principle 7)
- The skill leaves a reply without a destination close

---

## Step 5 — source notes

`source-notes.md` must contain:

1. Full book metadata (title, author, publisher, year, ISBN, translations used)
2. Chapter → skill section mapping table (every skill concept traceable to a chapter)
3. **List of concepts NOT used and why** (forces you to make active editorial choices, not just summarize)
4. Public sources used (author blog, podcast interviews, talks — for legal "fair use" defensibility)
5. Disclaimer: if author / publisher believes there's infringement, they can file an issue for immediate removal

This file is also defense against "this is just a paraphrase of the book" criticism. By documenting what you left out and why, you prove this is editorial work.

---

## Step 6 — propose package membership

If your book fits a `packages/` bundle (e.g., new-parent-pack, new-grad-pack), propose adding it. Each package is a curated 5-8 skill bundle with its own README explaining the "shape" of the bundle.

Currently planned packages (none implemented yet, post-v0.1):

- `new-parent-pack` (Atomic Habits + The Whole-Brain Child + Hunt Gather Parent + How to Talk So Kids Will Listen + Drive)
- `new-grad-pack` (Atomic Habits + Deep Work + Psychology of Money + Designing Your Life + So Good They Can't Ignore You)
- `midlife-health-pack` (Outlive + Why We Sleep + Atomic Habits + The Body Keeps the Score)
- `student-focus-pack` (Deep Work + Make It Stick + Stolen Focus + Tiny Habits)

---

## What we will close without merging

- Books that fail Step 0 criteria (we'll say why, briefly)
- Skills that skip the not_for / crisis exit ("but my book is positive, no one will be hurt")
- Skills that imitate therapist / coach / teacher voice
- Skills that pretend to remember past conversations
- Skills where user testing reveals unmitigated harmful behavior on `vulnerable` / `not_for` branches
- Summary-flavored skills ("this book says X, Y, Z. Here are 5 tips.")

---

## What we celebrate

- Skills that have **one** distinctive cold-start body action no other skill uses
- Skills that document their failures (-12% harmful, here's why) better than their wins
- Skills that **actively redirect users away** from themselves to a real human in some cases
- Skills that make the EVAL.md as compelling as the SKILL.md

---

## Reviewer time commitment

Currently 1 person (@zhichao1208). Expect 1-2 weeks for proposal review, 1 week for skill review after submission.

If this scales, we'll add reviewers. Maintainers will be invited from people who have shipped 2+ skills that passed without rework.

---

## License

CC BY-SA 4.0. All contributions accept this license.

Books' copyrights belong to authors and publishers. This repo is editorial interpretation + AI interaction design, not text reproduction.

---

*v0.1 · 2026-05-24*
