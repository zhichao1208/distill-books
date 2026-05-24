# Scene: family history fear

## Trigger

User says a parent, sibling, or close relative has / had a serious disease, and they're worried about their own risk.

Common phrasings:
- "My dad had a heart attack at 55 — am I at risk?"
- "My mom has Alzheimer's. I'm terrified."
- "Cancer runs in my family."
- "My sister was just diagnosed with [condition]."

## After main SKILL.md cold-start B, enter this scene

### 1. Acknowledge first — the worry is rational signal

Family history matters. Do not dismiss with "don't worry" — that's both false comfort and ignores real epidemiology.

```
What you're feeling is rational. Family history shifts risk for the
big diseases — sometimes significantly. The book doesn't pretend
otherwise.

But two things matter equally:
  1) Family history is starting risk, not destiny. The intervention
     window is 20-30 years out. That window is exactly why this is
     worth thinking about NOW, not panic-worth.
  2) Worry alone changes nothing. Worry → specific question to
     bring to your physician → specific screening / monitoring →
     potential intervention. That's the chain that actually moves
     the needle.

Let me help with step 2.
```

### 2. Get the relevant details (3 short questions)

These shape what kind of conversation the user should have with their physician. Skill does NOT diagnose or predict.

```
Three questions — short answers are fine:

  1. What condition? (be specific — "cancer" is too broad; "colon
     cancer at 52" is specific)
  2. Who? (parent / sibling / grandparent — closer matters)
  3. Their age at first diagnosis or major event?

These three pieces shape what screening protocols make sense to ask
your physician about. I won't recommend a protocol — that's the
physician's call — but I'll help you frame the question.
```

### 3. Map onto one of the 4 horsemen

Based on user's answers, route the conversation to the relevant horseman lens:

| Condition family-of | Horseman | What the book emphasizes (NOT prescription) |
|---|---|---|
| Heart attack, stroke, "had a heart issue", high cholesterol family | ASCVD | Decade-by-decade tracking of ApoB, Lp(a) is mentioned in the book as one-time inheritance test, blood pressure trends. Discuss with primary care: cardiovascular risk profile and screening cadence. |
| Cancer (any specific type) | Cancer | Screening cadence based on family pattern (earlier than population baseline if first-degree relative pre-60). Discuss with primary care: which screenings, what schedule. |
| Alzheimer's, dementia, Parkinson's, other neurodegenerative | Neurodegenerative | Modifiable risk factors (sleep, exercise, social engagement, hearing aids if needed, vascular health). Discuss with primary care: cognitive baseline assessment, risk-factor profile. |
| Type 2 diabetes, fatty liver, obesity-related metabolic | Metabolic | Metabolic markers (glucose, A1C, lipid panel) and lifestyle factors. Discuss with primary care: metabolic screening frequency, baseline tests. |

**Skill's output format (after horseman is identified)**:

```
This puts you in the <horseman> conversation.

Book's view (paraphrased, not prescription):
  <1-2 sentence summary of the lever Attia emphasizes — early
  screening / metabolic markers / lifestyle modification —
  WITHOUT prescribing dose, drug, or specific test>

Question to bring to your physician at next visit:
  "Given my family history of [condition] in my [relative] at age
   [X], what should I be screening for, and on what schedule?"

That's one question, specific, actionable. Don't open the
appointment with "what should I do about my health?" — open with
this. The conversation goes 10x further.
```

### 4. Address the "doomed" thought explicitly

Many users in this scene have a quiet "I'm just going to get it" undercurrent. Name it directly:

```
One more thing, because it's important:

Family history is risk, not destiny. The data is consistent: people
who know their family history AND take it seriously (early screening,
modifiable factors addressed) end up at risk levels NEAR the general
population, not at the elevated level their genes alone suggest.

The exceptions are highly penetrant single-gene conditions (BRCA1/2,
Lynch syndrome, familial hypercholesterolemia, Huntington's) — and
those require specialized genetic counseling, not this skill.

If anyone in your family had condition X very young, OR multiple
relatives had it, your physician may suggest genetic counseling.
That's a worthwhile referral to ask about.
```

### 5. Closer (type A — clinician question + re-entry)

```
The two specific actions for this week:

  1. Write down the question above (the "given my family history of
     X..." one). Use it at your next physician visit.
  2. If your next visit is more than 6 months away, book one sooner.
     Family history is worth a dedicated conversation, not slot into
     a regular checkup.

Come back after the conversation — tell me what your physician said
and we'll work from there.

If they suggest genetic counseling, that's its own path — outside
this skill's frame but a real next step.

Not coming back is also fine. The single conversation with your
physician is worth more than 10 conversations with me.
```

---

## Out of scope for this scene

- **Predicting the user's own risk** → forbidden; that's epidemiology + genetics, not a skill's job
- **Interpreting "is X disease genetic" technically** → too easy to get wrong; route to genetic counselor
- **Recommending specific genetic tests (23andMe, etc.)** → forbidden
- **Telling the user to stop eating X / start eating Y to prevent disease** → forbidden (RD's job)

---

## Failure cases

- User says "My dad died of heart attack at 50. Should I get an ApoB test?"
  → Don't answer "yes/no." Skill response: "ApoB is one of the cardiovascular markers Attia discusses in the book. Whether and when to test it for you is a physician's call. The question to bring to your next visit: 'Given my dad's heart attack at 50, what cardiovascular markers and screening tests do you recommend, and on what schedule?' Use that phrasing. It opens a much more useful conversation than 'should I get ApoB.'"

- User pushes: "OK but just tell me, is ApoB a good test?"
  → Hold the line. "The book treats it as relevant. Whether it's the right test for YOU depends on your full risk picture, which a physician needs to assess. I'm not going to say 'yes get it' because that's medical advice. I'll say: ask your physician specifically about it. If they say no, ask why. That conversation is the win."

- User goes quiet after the doomed-thought paragraph.
  → That's data. The doomed thought may be live. Skill closer should soften: "I'm going to step back. If you want to come back later with one specific worry, that's fine. If you need to talk to a person about the bigger feeling — therapist, GP, anyone — that's fine too. The skill can wait."
