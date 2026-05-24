# Demo Recording Guide

How to record the demo GIF that goes in the README. This script produces ~30 seconds of footage showing a real Atomic Habits skill conversation, which is the strongest belief-installation element for first-time visitors.

## Tools needed

Pick one — both export to GIF:

**Option A · asciinema + agg** (terminal-style, lightweight, themable)
```bash
# install
brew install asciinema agg

# record
asciinema rec demo.cast

# convert to GIF
agg demo.cast demo.gif
```

**Option B · VHS by charm** (deterministic, scripted, no live typing)
```bash
brew install vhs
vhs demo.tape    # uses the script below
```

Recommendation: VHS if you want a clean, repeatable result (the script does the typing for you).

## VHS script (`docs/demo.tape`)

Save the file below as `docs/demo.tape`, run `vhs docs/demo.tape`, get `demo.gif`.

```vhs
# distill-books · Atomic Habits demo
Output docs/demo.gif

Set FontSize 16
Set Width 1280
Set Height 720
Set Theme "Catppuccin Mocha"
Set TypingSpeed 35ms
Set PlaybackSpeed 1.0

# Open a fake "Claude conversation" in a terminal
Type "# Imagine this is any Claude / ChatGPT / Gemini conversation."
Enter
Sleep 800ms
Type "# I just pasted the Atomic Habits SKILL.md as my first message."
Enter
Sleep 1s

# Show the boot output
Type "AI:"
Enter
Type "  I'm the Atomic Habits skill. I take your 'I want to start / quit X'"
Enter
Type "  and break it down into something you can begin in 15 seconds."
Enter
Sleep 600ms
Type "  "
Enter
Type "  The whole flow is about 3-5 minutes, in 3 stages:"
Enter
Type "    1. 15-second warm-up (one or two body actions)"
Enter
Type "    2. I cut your goal to a 2-minute version you can do tonight"
Enter
Type "    3. One concrete next step + a clear exit"
Enter
Sleep 800ms
Type "  "
Enter
Type "  Want to do any of the following first?"
Enter
Type "    A. Paste 1-2 lines of context about you"
Enter
Type "    B. Pick a common scenario by letter"
Enter
Type "    C. Just say it in your own words"
Enter
Sleep 1s

# User picks C, says something specific
Type "You: I want to read more, every night before bed."
Enter
Sleep 1.5s

# Skill cold-start
Type "AI:"
Enter
Type "  Stop a moment. Put a hand on your chest. Take two breaths."
Enter
Type "  Look at the time in the top right of your phone. Hold it one second."
Enter
Sleep 800ms
Type "  "
Enter
Type "  You just opened this conversation — that's already a vote."
Enter
Type "  Every action is a vote for the person you want to become."
Enter
Sleep 800ms
Type "  "
Enter
Type "  The smallest unit of a habit here is 'open the book.'"
Enter
Type "  Thirty minutes is the outcome. One page is the action."
Enter
Sleep 800ms
Type "  "
Enter
Type "  Your minimum version tonight: after brushing your teeth,"
Enter
Type "  open the book to page 1. Finishing one page counts as a win."
Enter
Sleep 800ms
Type "  "
Enter
Type "  cue:      book next to your toothbrush"
Enter
Type "  craving:  pick a book you actually want, not 'should' read"
Enter
Type "  response: bar is 'open to page 1'"
Enter
Type "  reward:   mark an X on a paper calendar by the bed"
Enter
Sleep 800ms
Type "  "
Enter
Type "  Tonight, after brushing teeth, open the book. You don't need"
Enter
Type "  to tell me. Come back tomorrow, or don't. Either is fine."
Enter
Sleep 3s
```

## After recording

1. Confirm GIF size is < 5MB (GitHub embeds best under this size; trim if needed)
2. Save to `docs/demo.gif`
3. Add to README right after the hook section:

```markdown
> 6 months ago you finished *Atomic Habits*. Right now you're about to skip the workout, again. The whole book was about exactly this moment. None of it shows up.

That gap is what this repo closes.

![distill-books in action](docs/demo.gif)
```

## What this demo proves to a first-time visitor

| Beat | Belief installed |
|---|---|
| Boot message arrives instantly, no questionnaire | "I won't be interrogated." |
| 3-stage expectation (~3-5 min) | "I know what I'm getting into." |
| User says ONE sentence, gets a concrete plan | "It works without me explaining my life." |
| Body action first (chest / breath / time) | "This isn't lecture mode." |
| 4-gear plan with specific objects (book, toothbrush, calendar) | "Concrete, not abstract." |
| Closer: "come back, or don't" | "No subscription guilt." |

If a viewer watches this once, the README's other sections (data, principles, copyright) become confirmation rather than discovery. That's belief installation working.

## Alternative: live-screenshot a real conversation

If you'd rather not record:

1. Open Claude / ChatGPT in a clean window
2. Paste `books/atomic-habits/SKILL.md` as the first message
3. Wait for boot output
4. Send: "I want to read more, every night before bed."
5. Screenshot the full thread (use a long-screenshot tool like Tailor or shottr)
6. Save as `docs/demo-screenshot.png`
7. Embed in README the same way

A static screenshot is ~60% as effective as a GIF, but takes 2 minutes instead of 20.

---

*Created 2026-05-24 for v0.2.0 README demo asset*
