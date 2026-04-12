## Summary

- Fetched and wrote all 51 Craig Doctrine of Christ transcripts (Parts 1-51) as markdown files in `md/Christ/`
- Created 4 summary files: `Craig.Summary1.Incarnation.md`, `Craig.Summary2.Death.md`, `Craig.Summary3.Resurrection.md`, `Craig.Summary4.Access.md`
- Created high-level `Christ.Slides.md` (Markdeep TOC) with 9 sub-slide links
- Slide 1 (Overview) is done
- Slide 2 (Incarnation) is done
- Slide 3 (Death: Sacrifice, Propitiation, and Redemption) — DONE (motifs only, theories extracted)
- **Slide 4 (Theories of the Atonement) — NEW, extracted from Slides 3**
  - Contains: Five Motifs summary, Historical Landscape, Church Fathers, Ransom Theory, Satisfaction Theory, Moral Influence Theory, Penal Substitution intro, Diamond with Many Facets, Practical Takeaways
  - Images: MoralInfluence.jpg, PenalSubstitution.jpg added for their sections
- Updated `root.ai.md`: removed JW Rebuttal Standards, standardized on ASCII `"` quotes
- Editorial standards now merged into `root.ai.md` (no separate EditorialStandards.md)
- Slides renumbered: old 4-8 became 5-9, all nav links and TOC updated
- Fixed curly quote bug in Slides 5 (was 4) style attributes causing images to render centered instead of floating right

## Todo

| Slide | Title | Craig Parts | Status |
|-------|-------|-------------|--------|
| 1 | Overview: Who Is Christ? | Part 1 | DONE |
| 2 | The Incarnation: Two Natures, One Person | Parts 2-7 | DONE |
| 3 | Christ's Death: Sacrifice, Propitiation, and Redemption | Parts 8-13 | DONE |
| 4 | Theories of the Atonement | Parts 14-17 | DONE |
| 5 | Christ's Death: Penal Substitution Defended | Parts 18-24 | TODO |
| 6 | The Resurrection: Biblical Evidence | Parts 25-32 | TODO |
| 7 | The Resurrection: Defeating the Alternatives | Parts 33-46 | TODO |
| 8 | Access: Who Can Be Saved Through Christ? | Parts 47-51 | TODO |
| 9 | Doctrine of Christ Summary and Practical Takeaways | Synthesis | TODO |

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
