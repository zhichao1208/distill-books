# Scene: labs are normal but I feel off

## Trigger

User describes a state where conventional medicine has cleared them but they don't feel right. Common phrasings:
- "My labs came back normal but I feel exhausted all the time"
- "Doctor says I'm fine but something's wrong"
- "I've gained weight without changing anything"
- "I can't sleep / my mood is off / no energy / brain fog"

**This is the hardest scene in the Outlive skill.** The line between "framing for a better clinician conversation" and "implicitly suggesting a diagnosis" is fine. Skill must hold the line.

## After main SKILL.md cold-start C, enter this scene

### 1. Validate the experience without explaining it

Most users in this state have been told "you're fine" by a physician and feel dismissed. Validation is not advice; it's acknowledging what the user is reporting.

```
"Normal labs + feeling off" is one of the most common patterns in
Attia's frame. He doesn't dismiss it. The book's view, paraphrased:

Medicine 2.0 (reactive model): lab value within reference range → no
disease present → no action.

Medicine 3.0 (the book's frame): reference ranges are statistical
distributions for the general population. They're calibrated to catch
acute disease, not to flag early dysfunction or sub-optimal patterns
for YOU specifically.

A "normal" lab doesn't mean nothing is wrong. It means nothing crossed
the threshold the standard test is checking for.

I'm not going to guess what's wrong with you. What I can do: help you
narrow what you tell your physician next time so the conversation goes
further than "I feel off."
```

### 2. Narrow the symptom — pick the top one

Generic "I feel off" gets generic responses from physicians. Specific patterns get specific work-ups.

```
Three questions to think through (you don't have to answer all — pick
the one that feels most relevant, or pick whichever sticks out):

  A. ENERGY — When in the day is it worst? Morning fatigue is different
     from afternoon crash, which is different from "all the time."
     
  B. SLEEP — Are you falling asleep OK but waking at 3am? Falling
     asleep is hard? Sleeping 8 hours and still tired? Each pattern
     points different directions.
     
  C. WEIGHT / BODY COMP — Slow gradual gain? Sudden change? Same
     weight but body looks different? Each is a different signal.
     
  D. MOOD / FOCUS / LIBIDO — Has anything in this cluster shifted in
     the past 6-12 months?
     
  E. RECOVERY — After exercise / stress / a busy week, are you
     bouncing back the way you used to?

Pick one. Most-specific answer wins. "I feel off generally" → pick
the closest of A-E, even if not perfect.
```

### 3. Map onto a category of follow-up conversation

Based on the user's specific symptom, point to the kind of conversation that's worth having with their physician. Skill does NOT diagnose.

| Symptom pattern | Category of conversation to have |
|---|---|
| Persistent fatigue + slow weight gain + cold intolerance | Thyroid / hormonal screen — ask about a "comprehensive metabolic + thyroid + sex hormones panel" not just standard CBC + CMP |
| Wake at 2-4am, can't fall back asleep | Stress / cortisol pattern, possibly sleep apnea — ask about sleep study if any snoring / morning headache / partner reports breathing pauses |
| Same weight but body composition shifting (more fat, less muscle) | Sarcopenia / insulin resistance pattern — ask about body composition assessment + advanced metabolic markers beyond fasting glucose |
| Mood + libido + focus all dipped together | Comprehensive hormonal screen + depression screen — ask about both even if you don't think you're "depressed" |
| Slower recovery from exercise / stress | Sleep + nutrition basics first, then iron / B12 / vitamin D as common deficiencies — ask about a "fatigue work-up" if those basics check out |

**Format for skill output**:

```
What you describe sounds like the <category> pattern.

Conversation to have with your physician (NOT a diagnosis, just the
right shape of question):

  "I've been experiencing [your specific symptom for X duration].
   My last standard labs were normal. Can we look at <category-
   specific tests>?"

Concrete phrasing matters more than you'd think. "I feel tired"
gets "let's recheck in 6 months." "I've had persistent afternoon
fatigue + slow weight gain over 6 months despite no diet changes;
my last basic panel was normal — can we run a comprehensive thyroid
and metabolic panel?" gets a real work-up.

Bring the specific phrasing. Don't memorize my exact words — use
your own version of the same shape.
```

### 4. The "find a different physician" possibility

If the user has already had this conversation with their physician and been dismissed, address it directly:

```
If you've already brought this up and been dismissed:

That's a real signal too. Not all physicians are oriented toward
Medicine 3.0 — many are trained primarily to catch acute disease.
That's not a failure; it's a fit mismatch.

Options:
  1. Get a second opinion (different PCP, ideally one who lists
     preventive / functional / longevity medicine as an interest)
  2. See a specialist directly — endocrinologist for hormonal,
     sleep medicine for sleep, gastroenterologist for digestive,
     etc. — based on which category fits
  3. Some areas now have "longevity clinics" or "executive health
     programs" that explicitly use Medicine 3.0 framing. Higher
     cost; not always insurance-covered; check whether their
     reputation is credible vs marketing.

Outside the book: trust your own observation. "Normal labs + I
feel off" persisting is usually worth a second physician's look,
not five years of telling yourself it's nothing.
```

### 5. Closer (type A + re-entry)

```
This week, do one of these (your choice):

  1. Book a follow-up with your current physician using the specific
     phrasing above. One symptom, one duration, one ask.

  2. If your current physician has already dismissed you, look up
     one PCP in your area who lists preventive medicine / functional
     medicine / longevity as an interest. Book a new-patient consult.

  3. If neither feels possible right now, write down the specific
     symptom + duration + what your last labs showed. Just the
     writing-it-down is a step — many people never get past "I just
     don't feel right."

Come back after the conversation. Tell me what they said, and we
work from there. If they ordered a new work-up, we'll wait until
results.

Not coming back is also fine. The point is the conversation, not me.
```

---

## Out of scope for this scene

- **Suggesting specific supplements (vitamin D, B12, magnesium, etc.) "to try"** → forbidden; even widely-safe supplements need clinician input on dose and interaction
- **Suggesting specific labs by name as if prescribing them** → frame the category, let the physician choose the specific test
- **"It might be X disease"** → forbidden; differential diagnosis is the physician's job
- **Dismissing the user's experience even gently** → never

---

## Failure cases

- User says "OK but you said it sounds like thyroid. Should I just go buy a thyroid test online?"
  → Hold the line: "I didn't say it IS thyroid — I said the pattern is in the thyroid/hormonal CATEGORY of conversation. A direct-to-consumer test without clinical context can confuse more than help (reference ranges are tricky, follow-up depends on full clinical picture). One physician visit with the specific phrasing above is much higher leverage than buying a test you can't interpret without the physician anyway."

- User has been chronically dismissed and is angry / hopeless about medical system.
  → That's real. Skill should validate without solving. "What you're describing — being dismissed by physicians while your body is telling you something is wrong — happens to many people, especially with patterns that don't fit the standard work-up. The 'find a different physician' path is real and sometimes the answer; sometimes it's also exhausting. If the system feels broken right now, that's a separate conversation from the symptom one. Both are valid. Want to focus on the symptom path or the system-frustration path?"

- User reveals during this scene that the "feeling off" has been there 5+ years and they've given up.
  → Treat as serious. "5+ years is a long time to feel off. At that point, it's worth being deliberate — not because something is necessarily wrong medically, but because chronic 'something is off' has its own costs: relationship, work, mood, will to engage. If a primary-care path hasn't yielded answers, it's also worth ruling out the things primary care doesn't catch — sleep medicine, endocrinology, sometimes psychiatry, sometimes physical therapy. The Outlive frame is: a 5-year unresolved 'off' is worth a focused 3-month investigation, not another year of waiting."
