## Summary

- Fetched and wrote all 51 Craig Doctrine of Christ transcripts (Parts 1-51) as markdown files in `md/Christ/`
- Created 4 summary files: `Craig.Summary1.Incarnation.md`, `Craig.Summary2.Death.md`, `Craig.Summary3.Resurrection.md`, `Craig.Summary4.Access.md`
- Created high-level `Christ.Slides.md` (Markdeep TOC) with 9 sub-slide links
- Slide 1 (Overview) — DONE
- Slide 2 (Incarnation) — DONE
- Slide 3 (Death: Sacrifice, Propitiation, and Redemption) — DONE (motifs only; theories extracted to Slide 4)
- Slide 4 (Theories of the Atonement) — DONE
  - Extracted from Slide 3; polished for teaching
  - Contains: Five Motifs, Historical Landscape, Church Fathers, Ransom, Satisfaction, Moral Influence, Penal Substitution intro, Diamond summary, Practical Takeaways
  - Parallel "What the X Theory Captures / Misses" titles across all four theories
  - Images: `MoralInfluence.jpg`, `PenalSubstitution.jpg`
- Slide 5 (Penal Substitution Defended) — DONE (expanded from 122-line skeleton to ~540 lines / ~45 slides)
  - Built from Craig Parts 18-24 (Atonement Reflection 1-4, Satisfaction of Divine Justice 1-2, Redemption)
  - Sections:
    1. Challenge/Setup — diamond recap, Craig's definition, strong vs modest version, Isaiah 53 foundation, Socinus (1578), approach
    2. Objection 1 (Incoherence) — 3-premise argument, Feinberg's expressivism, 5 replies (modest version, strict liability, Grotius's ancient substitutes, expressivism rightly understood, imputation / respondeat superior)
    3. Objection 2 (Injustice) — 6-premise argument, retributive vs consequentialist, 5 replies (Divine Command Theory, positive vs negative retributivism, prima facie vs ultima facie, Carson on Isaiah 53, imputation)
    4. Satisfaction of Divine Justice — Scotus's acceptation rejected, Turretin's proportionality, guilt = liability, David Lewis's tu quoque, God as Legislator/Judge/Ruler
    5. Representation — pinch hitter vs agent, proxy analogy (shareholders), Incarnation + baptism
    6. Forgiveness and Pardon — Socinus's objection, Grotius on private creditor, legal pardon, conditional pardon, Ford/Nixon, future sins (Turretin), Colossians 2:13-14
    7. Four Motifs Integrated — human nature suffering, ransom paid to God, Dale's burning house, justification + sanctification, diamond summary
    8. Practical Takeaways, Credits, Navigation
- Updated `root.ai.md`: standardized on ASCII `"` quotes; editorial standards merged in
- Slides renumbered previously: old 4-8 became 5-9, all nav links and TOC updated

## Todo

| Slide | Title | Craig Parts | Status |
|-------|-------|-------------|--------|
| 1 | Overview: Who Is Christ? | Part 1 | DONE |
| 2 | The Incarnation: Two Natures, One Person | Parts 2-7 | DONE |
| 3 | Christ's Death: Sacrifice, Propitiation, and Redemption | Parts 8-13 | DONE |
| 4 | Theories of the Atonement | Parts 14-17 | DONE |
| 5 | Christ's Death: Penal Substitution Defended | Parts 18-24 | DONE |
| 6 | The Resurrection: Biblical Evidence | Parts 25-32 | TODO |
| 7 | The Resurrection: Defeating the Alternatives | Parts 33-46 | TODO |
| 8 | Access: Who Can Be Saved Through Christ? | Parts 47-51 | TODO |
| 9 | Doctrine of Christ Summary and Practical Takeaways | Synthesis | TODO |

### Next up: Slide 6 (Resurrection: Biblical Evidence)

- Source: Craig Parts 25-32 (Resurrection_1 through Resurrection_PostMortemAppearances2)
- Current state: check existing `md/Christ/Christ.Slides.6.ResurrectionBiblicalEvidence.md` — likely a skeleton
- Expand similarly to Slide 5: read the 8 Craig transcripts, build out sections covering the biblical evidence for the resurrection (empty tomb, post-mortem appearances, etc.)

### Slide 5 teaching-pass review (possible future polish)

- File is fresh; user has not taught from it yet
- When user starts teaching, expect the same kind of polish pass as Slide 4:
  - Overflow fixes on any bullet that runs to 3+ lines
  - Tightening wording in premise arguments
  - Possibly splitting dense slides (e.g., the 5-replies slides in each objection) if they feel rushed

### Pending: Apply quote spacing changes to other slide decks

CSS changes (dark.css) apply globally, but these per-file changes still need to be applied to other decks:
- Strip inline `margin-top`/`margin-bottom` from reference `<p>` labels (sed pattern: `text-align: right; margin-top: -Xem; margin-bottom: -Xem;` -> `text-align: right;`)
- Add `scripture-quote-layout.js` script tag and `slideChangeHook` to each slide file's footer
- Files: all `md/Christ/*.Slides.*.md`, all `md/Trinity/*.Slides.*.md`, and their `docs/` HTML copies

### Pending: Heresy variant images

User needs to edit these copies of `Trinity.and.JesusTrueGodTrueMan.png`:
- `FalseModel.Docetism.png` — dashed/ghostly human nature circle
- `FalseModel.Apollinarianism.png` — human circle missing "Rational, Self-conscious, Free Will"
- `FalseModel.Nestorianism.png` — TWO separate Person circles
- `FalseModel.Eutychianism.png` — merged blended circle
- `FalseModel.RadicalKenosis.png` — Son's circle outside God circle, divine attributes crossed out
- `FalseModel.Metamorphosis.png` — three sequential diagrams

## Source Material

- Transcripts: `md/Christ/Craig.01` through `Craig.51`
- Summaries: `Craig.Summary1.Incarnation.md` through `Craig.Summary4.Access.md`
- Style reference: `HolySpirit.Slides.md` series in `md/Trinity/`
- Editorial standards: `.ai.md/root.ai.md`
- Image pool: `docs/Christ/pics/` (diamond.png, RansomTheory.jpg, SatisfactionTheory.jpg, MoralInfluence.jpg, PenalSubstitution.jpg, Representation.jpg, Redemption.jpg, DivineJustice.jpg, ChristOverview.jpg, ChristWork.jpg, DiedForOurSins.jpg, LambSacrifice.jpg, SufferingServant.jpg, FalseModel.*.png)

## Working Notes

- Slide 5 reuses verified NKJV quotes from Slide 3 to avoid re-verification: Isaiah 53:5-6, Exodus 34:7, Romans 8:3, 2 Corinthians 5:21, 2 Corinthians 5:14, Isaiah 33:22, Hebrews 2:14-15, Colossians 2:13-14
- Colossians 2:13-14 quote in Slide 5 uses `[...]` ellipsis for an internal omission
- Markdeep `#` headings create section-divider slides (no bullets); `##` headings are content slides
- Section dividers in Slide 5: "The Challenge", "Objection 1: Incoherence", "Objection 2: Injustice", "Satisfaction of Divine Justice", "Representation", "Forgiveness and Pardon", "The Four Motifs Integrated", "Practical Takeaways"
