# Proposal: Outlive

**Slug**: `outlive`  
**Author**: Peter Attia, MD (with Bill Gifford)  
**Published**: 2023 (Harmony / Crown)  
**Status**: 🟡 awaiting editorial review (Phase 2)  
**Target version**: v0.3

---

## Why this book

| Reach | Note |
|---|---|
| Bestseller | #1 NYT bestseller across 2023-2024 |
| Author authority | Practicing longevity physician; runs *The Drive* podcast (#1 medical podcast) |
| Genre | Longevity / preventive medicine |
| Differentiator | The only mainstream longevity book treated seriously by clinicians |

Peter Attia's argument: most medical practice is reactive (treat disease after symptoms). What he calls **Medicine 3.0** is proactive — forecast which of the **4 horsemen** (atherosclerotic disease, cancer, neurodegenerative disease, metabolic dysfunction) you're most at risk for, and intervene 20-30 years before they would have struck.

---

## Core lens (≤2 keywords) — `Medicine 3.0` + `Centenarian Decathlon`

These are the two pieces that don't appear in any other distill skill and uniquely belong to Attia's frame:

1. **Medicine 3.0** — the shift from "wait for symptoms" to "forecast and intervene on 30-year horizon." Re-frames every "I'll deal with it later" into "later is when it's already too late."
2. **Centenarian Decathlon** — pick 10 physical things you want to do at age 90 (pick up grandkid, climb 3 flights, carry groceries, get off the floor). Reverse-engineer fitness now from what 90 needs. Concrete, vivid, anti-abstract.

Concepts in the book that **don't** become lenses:
- The 4 Horsemen taxonomy → useful but technical; lives in scenes, not in lens
- ApoB / Lp(a) / continuous glucose monitoring → specifics that risk turning skill into medical advice (skill must NOT do this)
- Zone 2 / VO2max / grip strength → specific training prescriptions; live in scenes, not in lens
- Emotional health chapter → present but feels bolted on; not strong enough to be lens
- Specific supplements (rapamycin, metformin) → actively avoid (medical-advice trap)

---

## 15-second cold-start sketch (3 candidates, will pick strongest)

**Candidate A · Centenarian Decathlon entry (most distinctive to Outlive)**  
> Right now, name one physical thing you want to be able to do at age 90.  
> Pick up a grandchild. Climb 3 flights without stopping. Carry your own grocery bag up to a 4th-floor apartment.  
> Don't pick something abstract like "be healthy." Pick a specific scene, with a verb.

**Candidate B · the stand-test (strongest body action)**  
> Stand from your chair without using your hands. Just try it once.  
> One of the strongest predictors of all-cause mortality in older adults is whether you can do that. You just measured something the book takes seriously.

**Candidate C · the 30-year horizon shift (most Medicine-3.0 pure)**  
> Look at the calendar. Find the year you'll be 30 years older than today.  
> The diseases that will probably end your life — heart, cancer, brain, metabolic — are being decided right now, in this decade. Not at the year you wrote.

Recommended: **A** as primary (concrete, vivid, opens conversation about what fitness is FOR) + **B** baked into scenes when user asks about fitness specifically.

---

## 3 trigger user utterances

- "I want to be healthier / live longer / not die young"
- "My parent had [heart attack / Alzheimer's / cancer] — am I at risk?"
- "I'm 40+ and starting to worry about my body / labs / energy"

Optional secondary:
- "Should I get [a specific test / supplement / new health gadget]?"
- "My labs are 'normal' but I feel off"
- "I want to lift / run / train but don't know where to start"

---

## not_for list (mandatory; ≥2 items + ≥1 crisis route)

- **Specific medical questions** — "is this lump cancer," "should I take this med," "interpret my lab results" → skill refuses, routes to a physician. Hard rule, no exception.
- **Eating disorders** — Outlive talks calmly about nutrition / fasting / body composition. For someone in an active ED these topics are accelerants. Route to clinical psych or RD specialist.
- **Acute health crisis** — chest pain, sudden weakness, possible stroke, suicidal thought → route to emergency, not skill.
- **Pediatric / pregnancy** — book is for adult longevity. Routes for kids' health and prenatal care are different specialists.

This skill has the **same advice-refusal posture as Psychology of Money**. The hard rule:
- Never prescribe a specific drug, supplement, or dose
- Never interpret specific lab values
- Never name a specific training program by reps/sets/weight
- Never give a calorie / macro number

What it CAN do: surface the FRAMEWORK (Medicine 3.0, the 4 horsemen as risk categories, the Centenarian Decathlon as a planning tool), suggest categories of conversation to have with a real doctor.

---

## Why this book vs adjacent books in archetype

This is the **first health/body archetype book** in the repo. Closest competitors:

| Adjacent book | Why Outlive wins as first | When the other should be added |
|---|---|---|
| **Why We Sleep** (Walker, 2017) | Walker is single-domain (sleep). Attia is whole-body longevity. Outlive is a better entry; sleep is one piece of it. | v0.5 — when 5+ books in, sleep deserves its own skill |
| **Lifespan** (Sinclair, 2019) | Sinclair is more speculative (rapamycin, NMN). Attia is more conservative + clinically grounded. Less risk of bad advice routing. | Probably never — Sinclair's specific-supplement focus violates skill's hard rule |
| **The Body Keeps the Score** (van der Kolk) | Different problem space — trauma, not longevity. Worth a slot, but sensitive (vulnerable users). | v0.8 — needs careful not_for design |
| **Breath** (Nestor, 2020) | Single-mechanism (breathing). Useful but narrow. | v0.8 — companion to Outlive |
| **The Comfort Crisis** (Easter, 2021) | Adjacent (discomfort training, primal exposure). Less rigorous. | Maybe v1.5 |

**Risk of overlap with Atomic Habits**: Both books eventually point to "do the small thing daily." But the lenses are completely different:
- AH lens = "atomic unit + identity vote" — universal behavior change
- Outlive lens = "Medicine 3.0 + Centenarian Decathlon" — specifically health-longevity framing
- A user saying "I want to start running" might route to either. AH if the question is "how do I build the habit." Outlive if the question is "what training matters for my long life." Triggers handle this.

---

## Archetype: health / body

First book in this archetype. Validates whether the meta-skill adapts to:
- Books where the **hard rule** is even more critical than PoM (medical advice is more dangerous than financial advice)
- Books where cold-start ranges from imaginative (Centenarian Decathlon) to physical-measurement (stand-test)
- Books that need **stronger routing to professionals** — primary care, cardiologist, RD, sleep medicine, mental health
- Books where the user's `memory` (age, health constraints, existing conditions, family history) becomes **load-bearing** for personalization

Outlive is the **dogfood candidate for user's own fitness project** (memory.user_health_profile is already populated: 40, 185cm, 87kg, TMJ, training budget). The skill can use that context fully.

---

## Boot-message sketch (will refine in Phase 3)

```
I'm the Outlive skill. I help you think about your health on a 30-year
horizon, not a 6-month one.

**Hard rule**: I never give specific medical advice — no drug names,
no dose, no lab interpretation, no reps/sets/weight prescriptions.
Specific questions → take to your doctor / RD / qualified trainer.
What I do: help you frame the conversation with them, and pick what
to ask.

The whole flow is about 3-5 minutes, in 3 stages:
  1. 15-second warm-up (one Centenarian Decathlon item)
  2. Pin down which of the 4 horsemen is the most likely concern
     for someone in your shape
  3. One concrete next step (usually: a question to ask a real
     clinician, or one habit area to focus on)

Want to do any of the following first?
  A. Paste 1-2 lines (age / known conditions / family history /
     current activity level / biggest worry)
  B. Pick a scenario:
     1) Want to live longer, don't know where to start
     2) Parent had [condition], am I at risk
     3) 40+, starting to feel things shifting
     4) Labs are "normal" but I feel off
     5) Acute concern: pain / sudden change / immediate worry
  C. Just say what's on your mind

I'll wait.
```

---

## Estimated effort (Phase 3)

| Artifact | Effort | Notes |
|---|---|---|
| SKILL.md | ~3 hours | Higher complexity due to hard rule + more not_for branches than other skills |
| 3 scenes | ~4 hours | Scenes likely: "I want to start training" / "parent had X disease" / "interpreting my own situation" — last one is the hardest because the line between "framing" and "advising" is fine |
| EVAL.md | ~1.5 hours | Must include: vulnerable + advice-demand + acute health (B5) + specific-lab-question + family-history-fear cases |
| source-notes.md | ~1 hour | Chapter mapping; explicit list of WHAT THE SKILL DOES NOT TOUCH (drug names, doses, etc.) |
| **Total** | **~1.5 days focused work** | Slightly more than Deep Work due to medical-edge complexity |

---

## Special complexity: where Outlive is harder than other skills

Three areas where the design will need extra care:

1. **The "framework vs advice" line**  
   PoM has a clean rule: don't recommend specific stocks. Outlive's version is harder because users will often ask "what should I do" expecting a specific recommendation. Skill must redirect to framework without sounding evasive. Phase 3 needs careful scene work here.

2. **Memory borrow on health data is sensitive**  
   AH and PoM borrow age, city, family. Outlive will want to borrow conditions (TMJ, ApoB, etc.) — but if the user hasn't disclosed, the skill must NOT infer or fish. Stricter transparency rule.

3. **Real-time emergencies**  
   "I'm having chest pain right now" needs an immediate hard exit to 911 / 112 — no boot, no cold-start, no framework. The skill must detect this in the very first input.

Phase 3 will likely produce a longer SKILL.md than the others for this reason. That's acceptable — medical context warrants it.

---

## Reviewer decisions needed (your turn)

1. **Go / kill / change?** If change: specify which field.
2. **Best cold-start candidate?** A (Centenarian Decathlon name) / B (stand-test) / C (30-year horizon).
3. **Build order**: do Outlive first (matches your fitness project, max dogfood) or Deep Work first (lower medical risk, easier framework validation)?
4. **The "framework vs advice" line is the hardest design issue.** Want to look at a few scene drafts side-by-side before I commit to one approach?
5. **Anything I missed?** Especially: edge cases I haven't thought of (chronic pain, disability accommodations, pregnancy adjacency).

---

*v0.1 proposal · 2026-05-24 · awaiting Phase 2 review*
