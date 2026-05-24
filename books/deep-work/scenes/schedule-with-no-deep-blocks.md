# Scene: schedule has no deep blocks

## Trigger

Structural complaint: "I'm in meetings all day" / "my calendar has no time" / "I can never find 2 hours" / "as a manager I'm always interrupted."

This is about the *recurring shape of the week*, not today.

## After main SKILL.md cold-start C, enter this scene

### 1. The first move is honesty about constraint

Most users in this state try to design their ideal schedule. Newport's frame: start from what's actually defendable, not what's ideal.

```
Before we pick a philosophy, one honest sentence: how much control do
you have over your calendar? Pick a letter:

  A. Full control (founder / freelancer / executive)
  B. Mostly control, some required meetings
  C. Half-and-half (calendar is shared, but I can block)
  D. Minimal control (assigned meetings, manager owns my time)
  E. None (on-call / shift / customer-facing)

Be honest. The philosophy we pick depends entirely on this answer.
```

### 2. Route by control level

| Control | Philosophy Newport's book recommends | Why |
|---|---|---|
| A. Full | Monastic or Bimodal | You can disappear; use it |
| B. Mostly | Bimodal (2-3 days deep / 2-3 shallow) | Concentrated time wins over scattered |
| C. Half-and-half | **Rhythmic** (daily 90-min block) | Realistic for most; the default the book recommends |
| D. Minimal | Rhythmic (60 min early or late) | Use the edges of the day, not the middle |
| E. None | Skill **does not apply** — route to structural_shallow exit | The book is for people with attention to schedule, not for people whose time is sold by the hour |

### 3. Designing the Rhythmic block (most common case)

If user picks C or D, walk through these in order:

**Pick the window (not multiple windows — one)**:
```
Same time every day. Not "when I have time" — that's the trap.
Realistic candidates:
  - 06:00-07:30 (before household / kids wake up)
  - 07:00-08:30 (before office, at office)
  - 09:00-10:30 (first thing at desk — only if you can block it)
  - 16:00-17:30 (end of day, when meetings tail off)
  - 21:00-22:30 (after household / kids down)

Pick one. Not "I'll try both 06 and 09" — that's two failed habits, not one.
```

**Defend it (Newport's 3 defenses)**:
```
1. Calendar block titled "Deep Work" (visible to your team / family)
2. Physical or digital wall (door closed / phone elsewhere / Slack closed)
3. A pre-block ritual to enter the state — same one every day
   (coffee → desk → noise-cancelling headphones → first specific task)
```

**Fill it (specific, not categorical)**:
```
The block doesn't say "writing" or "thinking" or "the project."
It says exactly one of:
  - "Outline of section 3"
  - "Solve the bug from yesterday's stack trace"
  - "Draft the email to [name]"
  - "Read pages 40-80 of [paper]"

If you can't name the deliverable in one sentence, the block fails
before it starts.
```

### 4. Defending against the inevitable interruptions

Newport's realistic claim: even rhythmic blocks get attacked. Have a default response ready.

```
When someone says "got a minute?" during your block:
  - "I'm in deep work until 10:30. Want to grab 5 min at 10:35?"
  - "Sure" then immediately note where you were so you can resume

When a meeting tries to grab the block:
  - Default decline + suggest alternative time
  - If unavoidable: move the block to the end of the day, don't skip it

Newport's data: people who treat the block as moveable lose it
within 2 weeks. People who treat it as fixed (with rare exceptions)
keep it for years.
```

### 5. Closer

```
Your block: <Day + Time>
Defended by: <3 protections>
Filled with: <one specific deliverable for tomorrow>

Try it for 5 working days. Tomorrow, do tomorrow's deliverable.
Come back at the end of the week and say:
  - "Defended all 5" → we expand the block or add a second
  - "Defended 3 of 5" → normal; we tune the defenses
  - "Defended 0-2" → the philosophy is wrong; we re-pick (probably
    Journalistic for now, not Rhythmic)

Not coming back is also fine.
```

---

## Out of scope for this scene

- **User wants to redesign their whole calendar** → 1 block at a time, not a full overhaul. Overhauls fail.
- **User wants a productivity app recommendation** → Newport's book is platform-agnostic. Don't suggest specific apps; suggest the protections instead.
- **User is in "E. None" control bucket** → route to `structural_shallow` exit; this scene doesn't apply.

---

## Failure cases

- User picks the Monastic philosophy when they have a regular job.
  → Refuse politely. Monastic is for people with no shallow obligations. With a regular job, even one weekly all-hands kills Monastic. Re-route to Rhythmic.

- User commits to Rhythmic 06:00-07:30, comes back week 2 saying they did it once.
  → Don't add motivation. The window's wrong, not their willpower. Ask: what got in the way at 06:00? Often: sleep debt, partner schedule, or kid waking. Re-pick window based on the real constraint, not the aspirational one.

- User says "I tried Rhythmic for 5 days but every block was attacked by my boss."
  → That's structural, not personal. The skill should escalate: "Can you have one conversation with your boss about a single weekly hour being protected? If the answer is no, you're in a job that doesn't permit deep work, and we should be honest about that. See the structural_shallow exit."
