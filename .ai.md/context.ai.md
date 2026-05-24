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
- Slide 5 (Penal Substitution Defended) — DONE (expanded from 122-line skeleton to ~900 lines / ~70 slides)
  - Built from Craig Parts 18-24 (Atonement Reflection 1-4, Satisfaction of Divine Justice 1-2, Redemption)
  - Sections:
    1. Challenge/Setup — diamond recap, Craig's definition, strong vs modest version, Isaiah 53 foundation, Socinus (1578), approach
    2. Objection 1 (Incoherence) — 3-premise argument, Feinberg's expressivism, 5 replies (modest version, strict liability, Grotius's ancient substitutes, expressivism rightly understood, imputation / respondeat superior)
    3. Objection 2 (Injustice) — 6-premise argument, retributive vs consequentialist, 5 replies (Divine Command Theory, positive vs negative retributivism, prima facie vs ultima facie, Carson on Isaiah 53, imputation)
    4. Both Socinus Objections Refuted — synthesis bridging defensive and constructive halves
    5. Satisfaction of Divine Justice — Scotus's acceptation rejected, Turretin's proportionality, guilt = liability, David Lewis's tu quoque, God as Legislator/Judge/Ruler
    6. Representation — substitute footballer vs agent, MMO avatar combined-roles, proxy analogy (shareholders), Incarnation + baptism
    7. Forgiveness and Pardon — Socinus's objection, Grotius on private creditor, legal pardon, conditional pardon, Biden/Hunter (2024), future sins (Turretin), Colossians 2:13-14
    8. Responding to Contemporary Objections — defensive recap closing the apologetic arc
    9. Four Motifs Integrated — human nature suffering, ransom paid to God, Dale's burning house, justification + sanctification, diamond summary
    10. Practical Takeaways, Credits, Navigation
  - **Outline TOC slide** (slide 1) with clickable anchor links to each section divider; hashchange listener calls showSlide for mid-presentation jumps
  - **Teaching-pass polish DONE:** verse-first formatting, premise repeats as leading bullets on Replies, "censure" → "rebuke", "just desert" → "what is deserved", "pinch hitter" → "substitute footballer", em-dash audit (label:def → colon), 8 nesting fixes, "Penal Substitution" capitalization normalized
  - **scripture-quote-layout.js wired up** (footer script + slideChangeHook)
- Slide 6 (Resurrection: Biblical Evidence) — DONE (expanded from 100-line skeleton to ~855 lines / 63 slides)
  - Built from Craig Parts 25-32 (1 Cor 15 + Gospel resurrection narratives)
  - Sections:
    1. Why It Matters — cross/resurrection two sides of one coin (Romans 4:25), roadmap
    2. Paul's Early Tradition (1 Cor 15:3-5) — four-line creed, rabbinical transmission markers, non-Pauline style, Semitic features, dating to AD 36 (Galatians 1:18-19, Dodd), "according to the Scriptures" (Isaiah 53 / Jonah), echoed in Acts 13 and Mark 15-16
    3. The Witnesses (1 Cor 15:5-8) — witnesses not appearances, why women omitted, Cephas/Twelve/500, James (skeptic to pillar), all apostles + Paul, Damascus Road as real post-ascension appearance, modus tollens, the stakes (1 Cor 15:14, 17, 20)
    4. Nature of the Resurrection Body (1 Cor 15:35-49) — Corinthian objection, three analogies (seed/flesh/glory), four contrasts (1 Cor 15:42-44), psychikos vs pneumatikos misreading corrected (1 Cor 2 and 10), Hering's "supernatural", First/Last Adam (1 Cor 15:45)
    5. Transformation Not Body-Swap (1 Cor 15:50-58) — flesh and blood as Jewish idiom, compatible with Luke 24:39 "flesh and bones", Ezekiel 37 (bones at heart of Jewish hope), continuity (1 Cor 15:51-52), final application (1 Cor 15:55, 58)
    6. The Burial — Joseph of Arimathea (Sanhedrist + sympathizer hints in Mark), Nicodemus + tomb type (arcosolium/bench, rolling stone, wealth), women's triple witness
    7. The Empty Tomb — Roman guard set Saturday (timing argues against legend), Sunday devotional anointing not unfinished burial, angel proclamation (Mark 16:6), "said nothing to anyone" read rightly (Mark 1:43-44 parallel), Mark presupposes Galilee appearances, disciples' inspection (John 20 + Luke 24:24), folded face cloth (blepo/theoreo/horao)
    8. Post-Mortem Appearances — six gospel appearances + four named by Paul; women (Matthew 28 / John 20:11-18); "do not cling" in light of grasping ankles; Emmaus + non-recognition as supernatural inhibition; Peter; Twelve in Jerusalem (Luke 24:39, 42-43; rabbinical food test); materiality + identity; through closed doors (supernatural body); wounds as eternal trophy; Thomas (John 20:27-28); Sea of Tiberias (Galilean rendezvous wait, Nathanael landlocked, "nets did not tear"); Peter recommissioning (John 21:17, not rehabilitation); Galilean mountaintop (Matthew 28:16-19, "some doubted" possibly the 500)
    9. Chronology — feast pilgrimage ordering, resolving Matthew/John women-appearance tension (Matthew leapfrogs 1→3), Acts 1:3 forty days, glorified at resurrection not at ascension
    10. Practical Takeaways — what resurrection establishes, "labor not in vain", hope of Christian future
    11. Credits (Craig 25-32, Dodd, Hering, N. T. Wright), Navigation
  - Verified NKJV quotes against blueletterbible.org: Romans 4:25; 1 Cor 15:3-8, 14, 17, 20, 42-44, 45, 50-52, 55, 58; Mark 16:6; Luke 24:39, 42-43; John 20:17, 27-28; John 21:17; Matthew 28:16-19; Acts 1:3; Ezekiel 37:5-6
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
| 6 | The Resurrection: Biblical Evidence | Parts 25-32 | DONE |
| 7 | The Resurrection: Defeating the Alternatives | Parts 33-46 | TODO |
| 8 | Access: Who Can Be Saved Through Christ? | Parts 47-51 | TODO |
| 9 | Doctrine of Christ Summary and Practical Takeaways | Synthesis | TODO |

### Next up: Slide 7 (Resurrection: Defeating the Alternatives)

- Source: Craig Parts 33-46 (Theories 1-3, Facts 1-6, Hypotheses 1-3, Best Hypothesis, Conclusion)
- Current state: check existing `md/Christ/Christ.Slides.7.ResurrectionDefeatingAlternatives.md` — likely a skeleton
- Expand similarly to Slides 5 and 6: this is the *historical apologetic* half (the biblical evidence is in Slide 6)
- Likely sections: Enlightenment skepticism (Reimarus, Strauss); existential vs evidential method; Ehrman objection; the three core facts (empty tomb, appearances, origin of belief) with detailed sub-arguments; McCullagh criteria for hypothesis evaluation; conspiracy/apparent-death/wrong-tomb/myth/hallucination critiqued; resurrection as best explanation; pastoral conclusion

### Slide 6 teaching-pass review (possible future polish)

- Like Slide 5, file is fresh; user has not taught from it yet
- When user starts teaching, expect the same kind of polish pass as Slides 4 and 5:
  - Overflow fixes on any bullet that runs to 3+ lines
  - Tightening wording on dense slides (especially the appearances section, which has many sub-slides)
  - Possibly splitting/combining adjacent slides if pacing feels off

### Pending: Apply quote spacing changes to remaining slide decks

CSS changes (dark.css) apply globally, but these per-file changes still need to be applied to other decks:
- Strip inline `margin-top`/`margin-bottom` from reference `<p>` labels (sed pattern: `text-align: right; margin-top: -Xem; margin-bottom: -Xem;` -> `text-align: right;`)
- Add `scripture-quote-layout.js` script tag and `slideChangeHook` to each slide file's footer
- **Slides 5 and 6 — DONE**; remaining: Slides 1-4, 7-9 in Christ; all Trinity decks; matching `docs/` HTML copies

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
- Slide 5 Outline TOC is slide 1; type `1` + Enter to jump there during teaching; click any link to jump to that section
- "Responding to Contemporary Objections" was moved out of Practical Takeaways to close the defensive arc right before "The Four Motifs Integrated"
