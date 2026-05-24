# Stolen Focus · sources and chapter mapping

## Book

- **Original**: *Stolen Focus: Why You Can't Pay Attention—and How to Think Deeply Again*
- **Author**: Johann Hari
- **Publisher**: Crown, 2022
- **ISBN**: 978-0593138526
- **Chinese edition**: 《被偷走的注意力》, 中信出版集团, 2023 (verify)
- **Goodreads**: ~4.27 / 5
- **Reception**: NYT bestseller; widely discussed in tech / attention-policy circles

## Author credibility note (load-bearing for skill design)

Johann Hari had a public plagiarism scandal in 2011-2012 when he was a journalist at *The Independent*. He was caught:
- Fabricating quotes (presenting interview subjects' written work as oral interview answers)
- Editing Wikipedia entries about his critics anonymously

He left journalism for several years and returned with books on mental health, addiction, and attention (*Chasing the Scream*, *Lost Connections*, *Stolen Focus*). Some critics still don't trust his journalism; some accept that the books represent a different mode of work.

The skill handles this by **citing the underlying researchers** rather than "Hari says." When the skill needs to cite a finding, it cites Gloria Mark (switching cost), Tristan Harris (attention engineering), Csikszentmihalyi (flow), Przybylski (social media research) — not Hari. Hari is the synthesizer; the underlying research is the source of authority.

This is the same approach the skill takes with Mindset (cites Sisk 2018 + Yeager 2019 to qualify Dweck's stronger claims).

## Chapter → skill mapping

The book has 14 chapters identifying causes. Skill uses these as the 12-force diagnostic taxonomy in `which-force-is-biggest.md` scene.

| Hari chapter / cause | Skill use |
|---|---|
| Ch 1: The Increase in Speed (switching cost) | Group 1A in diagnostic — Gloria Mark research |
| Ch 2: The Crippling of Our Flow States | Csikszentmihalyi cited; skill doesn't lean heavily on flow framing (overlaps with Deep Work) |
| Ch 3: The Rise of Physical and Mental Exhaustion | Sleep debt / stress branches; routes to Why We Sleep |
| Ch 4: The Collapse of Sustained Reading | Group 3I — re-train reading muscle |
| Ch 5: The Disruption of Mind-Wandering | Group 3J — unstructured time |
| Ch 6: The Rise of Technology That Can Track and Manipulate You | Group 1B — engagement engineering; Tristan Harris / Center for Humane Technology |
| Ch 7: The Causes of Cruel Optimism — bigger forces | Carries into systemic conversation in `when-individual-fixes-arent-enough.md` |
| Ch 8: The First Glimpses of the Deeper Solution | Systemic scene |
| Ch 9: The First Glimpses of the Deeper Solution (continued) | Same |
| Ch 10: Stress and the Rise of the Surveillance State | Mentioned briefly in systemic scene |
| Ch 11: ADHD and Its Causes | **Contested chapter** — see ADHD routing exit |
| Ch 12: The Confinement of Our Children, Both Physical and Psychological | Group 4L + pediatric scene briefly |
| Ch 13: An Attention Rebellion | Systemic scene; not core to skill (collective action framing) |
| Ch 14: Epilogue / hope | Not used |

## Concepts deliberately not used

| Book concept | Why not in skill |
|---|---|
| Specific company / platform shaming | Skill is platform-agnostic; calls out the engagement-engineering pattern not the brand |
| The book's "Attention Rebellion" rhetoric | More activist than the skill's diagnostic framing; reader can engage on their own |
| Hari's personal narrative arcs | Not actionable; skill is diagnostic, not memoir |
| The book's stronger claims about institutional culpability | Skill is more neutral; you can decide what to make of them |
| The "monastery in Provincetown" personal experiment | Memoir, not method |

## The ADHD chapter (Ch 11) — most contested

Hari frames ADHD as partly environmental / partly social, with notable critique:

**ADHD community views** (both real, both held by people with the diagnosis):
- Some welcomed Hari's framing: environmental factors DO contribute to attention symptoms even in clinical ADHD; chronic environment can produce ADHD-like symptoms in people without clinical ADHD
- Others criticized: the chapter risks minimizing the neurological reality; some readers used "it's environmental" to delay clinical evaluation, missing treatable clinical ADHD; the prescription / treatment evidence is strong and shouldn't be downplayed

The skill's `adhd_routing_question` exit explicitly tells users this controversy exists and routes:
- Unevaluated + functional impairment → get evaluated; the reframe doesn't substitute
- Already diagnosed → stick with clinician; this skill is environmental layer not primary tool
- Sure no clinical ADHD + environment-eroded → diagnostic reframe is yours; Deep Work / Tiny Habits for individual work

## Underlying researchers (cited preferentially over "Hari says")

| Researcher | Topic | Why cited directly |
|---|---|---|
| **Gloria Mark** (UC Irvine) | Switching cost; 23-min recovery; ~63 interruptions/day | Original empirical work; replicated |
| **Tristan Harris** (Center for Humane Technology) | Engagement engineering; ethics of attention design | Direct primary source on the industry side |
| **Mihaly Csikszentmihalyi** | Flow states | Foundational research; Hari is summarizing |
| **Andrew Przybylski** (Oxford) | Social media and well-being | Best-quality research on adolescent social media effects (effects real but smaller than popular framing) |
| **Jean Twenge** (San Diego State) | Adolescent screen time and mood (more contested than Przybylski) | Contested figure; skill cites carefully |
| **Cal Newport** (Georgetown) | Deep work; digital minimalism | Hari builds on Newport; skill routes to Newport's Deep Work as operational manual |
| **Adam Alter** (NYU Stern) | Behavioral addiction; product design | Foundational on the "designed to be addictive" thesis |
| **Tim Wu** (Columbia Law) | *The Attention Merchants* | Historical / policy frame on attention economy |
| **Shoshana Zuboff** (Harvard) | Surveillance capitalism | Broader political-economic frame |

## Chinese edition notes

- Title 《被偷走的注意力》 (literally "stolen attention") works well in Chinese; faithful translation
- Hari's plagiarism context has not been widely discussed in Chinese press; Chinese readers may be less aware

Key terminology:
| English | Chinese |
|---|---|
| Stolen Focus | 被偷走的注意力 / 失焦 |
| Attention economy | 注意力经济 |
| Switching cost | 切换成本 |
| Engagement engineering | 参与度工程 / 沉迷设计 |
| Flow state | 心流状态 |
| Surveillance capitalism | 监视资本主义 |

## Related / complementary books

- **Deep Work** (Cal Newport, 2016) — individual operating manual; complement to Hari
- **Digital Minimalism** (Newport, 2019) — individual environmental design; closer to Hari's individual prescription
- **The Shallows** (Nicholas Carr, 2010) — earlier internet-attention book
- **Indistractable** (Nir Eyal, 2019) — covers similar territory; some friction with Hari over framing
- **The Attention Merchants** (Tim Wu, 2016) — historical / policy
- **Age of Surveillance Capitalism** (Shoshana Zuboff, 2019) — broader frame
- **Lost Connections** (Hari, 2018) — Hari's previous book; similar method (synthesis + critique of medicalization), applied to depression

## Important limitations / counterpoints (skill carries)

- **Hari's journalism credibility issues** — skill addresses by citing underlying researchers, not "Hari says"
- **ADHD chapter is contested** — skill routes carefully
- **The book is heavy on diagnosis, light on individual prescription** — that's why this skill is diagnostic-only and routes to Deep Work / Tiny Habits for operational work
- **Some specific evidence claims are stronger in the book than in the underlying research** — skill cites carefully, qualifies where the original literature is more uncertain
- **The "Attention Rebellion" closing chapter is activist** — skill carries the spirit (systemic levels exist) but doesn't prescribe the activism specifics

## Public-domain sources used

No quotation exceeds reasonable use. Method descriptions based on:

1. stolenfocusbook.com (author site)
2. Hari's TED talk and podcast interviews (post-2018, after his return to writing)
3. Underlying researchers' work (Gloria Mark's "Multitasking in the Digital Age," Tristan Harris's CHT public materials, Csikszentmihalyi's published flow research)
4. Critical reviews of *Stolen Focus* (Irish Times, Washington Post, LightbulbADHD)
5. Public coverage of Hari's plagiarism (2011-2012 articles in major UK press)
6. The book's Amazon Look Inside preview
7. Wikipedia entries for cross-reference (Hari, Stolen Focus, Center for Humane Technology)

If Johann Hari or Crown believes any part of this skill exceeds fair use, file an issue and it will be modified or removed within 24 hours.

---

*v0.4.0 · 2026-05-24 · Diagnostic-not-operational design + cite-underlying-researchers approach to handle Hari's credibility history*
