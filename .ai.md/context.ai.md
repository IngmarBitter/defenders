## Summary

- Fetched and wrote all 51 Craig Doctrine of Christ transcripts (Parts 1-51) as markdown files in `md/Christ/`
- Created 4 summary files: `Craig.Summary1.Incarnation.md`, `Craig.Summary2.Death.md`, `Craig.Summary3.Resurrection.md`, `Craig.Summary4.Access.md`
- Created high-level `Christ.Slides.md` (Markdeep TOC) with 8 sub-slide links
- Slide 1 (Overview) is done
- Slide 2 (Incarnation) is done
- Updated `root.ai.md`: removed JW Rebuttal Standards, standardized on ASCII `"` quotes
- Editorial standards now merged into `root.ai.md` (no separate EditorialStandards.md)
- **Slide 3 (Death: Sacrifice, Propitiation, and Redemption) — DONE**
  - All 5 motif sections complete with dedicated images
  - Theories of Atonement: 4 section heading slides added (Ransom, Satisfaction, Moral Influence, Penal Substitution)
  - "Not Wounded Ego" slide split in two for overflow; Euthyphro Dilemma expanded
  - Images: Representation.jpg, Redemption.jpg, SatisfactionTheory.jpg added
  - Editorial standard updated: markdown `**` preferred over `<b>` for scripture emphasis

## Todo

| Slide | Title | Craig Parts | Status |
|-------|-------|-------------|--------|
| 1 | Overview: Who Is Christ? | Part 1 | DONE |
| 2 | The Incarnation: Two Natures, One Person | Parts 2-7 | DONE |
| 3 | Christ's Death: Sacrifice, Propitiation, and Redemption | Parts 8-17 | DONE |
| 4 | Christ's Death: Penal Substitution Defended | Parts 18-24 | TODO |
| 5 | The Resurrection: Biblical Evidence | Parts 25-32 | TODO |
| 6 | The Resurrection: Defeating the Alternatives | Parts 33-46 | TODO |
| 7 | Access: Who Can Be Saved Through Christ? | Parts 47-51 | TODO |
| 8 | Doctrine of Christ Summary and Practical Takeaways | Synthesis | TODO |

### Slide 3 section status

| Section | Slides | Status |
|---------|--------|--------|
| Sacrifice | ~9 slides | DONE |
| Suffering Servant | ~6 slides | DONE |
| Divine Justice | #25-#32 (8 slides) | DONE — reviewed against Craig, committed |
| Representation | ~7 slides + summary | DONE |
| Redemption | ~7 slides + summary | DONE |
| Theories of Atonement | 26 slides | DONE — reviewed and refined with user |

### Pending: Apply quote spacing changes to other slide decks

CSS changes (dark.css) apply globally, but these per-file changes still need to be applied to other decks:
- Strip inline `margin-top`/`margin-bottom` from reference `<p>` labels (sed pattern: `text-align: right; margin-top: -Xem; margin-bottom: -Xem;` → `text-align: right;`)
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
