# Brief: building one Creation-unit slide deck

You are building ONE Markdeep slide deck for Ingmar Bitter's church apologetics class ("Creekside Defenders"), Topic 10 "Doctrine of Creation vs Evolutionism". Repo root: `C:/_/me/bible/Defenders/github/defenders` (call it R).

## Read first (mandatory)
1. `R/.ai.md/root.ai.md` – all slide rules (scripture format, encoding, dashes, book names, pronoun capitalization, images, overflow check). Follow it exactly.
2. `R/md/Creation/Creation.Slides.Structure.md` – the plan. Your deck's section is the authority for content, order, stance and sources. Also read "Stance and Method" and "Overlap with Existing Decks".
3. `R/md/Creation/Creation.Slides.1.CreationOutOfNothing.md` – the finished Deck 1: copy its format exactly (title slide, Outline with `#slideN` anchors, `# Section` divider slides, `## Slide` slides each with one right-floated image, scripture quote blocks, Practical Takeaways section, Credits slide, Navigation slide, and the Markdeep tail).
4. `R/md/Creation/README.md` – where the sources are.
5. The sources your plan section names (in `R/md/Creation/Craig/`, `R/md/Creation/Notes/...`, `R/md/Creation/Sources/...`). Read them properly – content must come from them, not from memory. Craig transcripts are the primary theological source where the plan names them; for science decks Ingmar prefers creation.com / AiG / ICR / Discovery Institute and his own GodScience notes, with opposing views (RTB, BioLogos, Craig's evolution-friendly positions) steelmanned and then answered.

## Stance (Ingmar)
- Young-earth, historical six 24h days as the core of a "diamond" of true facets (historical, literary structure, purpose, anti-myth polemic, Sabbath pattern). Every figure has a referent. Reject concordism (reading modern science into Genesis).
- Be fair to opposing views (steelman), then answer them.
- Molinist on providence (Deck 8), but deck 8 is mode (b): balanced until the verdict.

## Output
- Write exactly one file: `R/md/Creation/Creation.Slides.<N>.<Subtitle>.md` (name given in your task). Then copy it to `R/docs/Creation/<same base name>.html` (identical content, only the extension changes).
- Append the Markdeep tail copied verbatim from the end of Deck 1 (everything from `<!-- Markdeep slides stuff -->` on) after the last `---`.
- CRLF line endings. US English. ASCII straight quotes and apostrophes. Spaced en dash ( – ), never em dashes (except inside verbatim NKJV). Unicode ellipsis …, `[...]` for omissions inside scripture. Full book names (abbreviate inline only if a line would overflow). Capitalize He/Him/His for God.
- Size: no ceiling – take as many slides as a proper representation of the ideas needs; never cut content to hit a count. Keep bullets short – 16:9 slides at font size 28 with a right-floated image hold about 5–6 short bullets; a slide with a scripture quote holds about 3 bullets.
- Do NOT edit any other file (no TOC, no CreeksideDefenders.md, no structure doc, no other deck). Do NOT git commit. Ingmar's coordinator does that.

## Scripture (critical)
- Every Bible quote verbatim NKJV, fetched – never from memory. Tool: `python R/tools/blb.py gen:1:1 exo:20:8-11 rom:5:12` (Blue Letter Bible abbreviations: gen exo lev num deu jos jdg rut 1sa 2sa 1ki 2ki 1ch 2ch ezr neh est job psa pro ecc sng isa jer lam eze dan hos joe amo oba jon mic nah hab zep hag zec mal mat mar luk joh act rom 1co 2co gal eph phl col 1th 2th 1ti 2ti tit phm heb jas 1pe 2pe 1jo 2jo 3jo jud rev). It prints the NKJV text; the console may garble curly quotes – write them as ASCII straight quotes (inner quotes as single quotes). Remove "[fn]" markers.
- Quote each passage only once in the deck; later slides refer back by reference.
- Quote block format and stacked-quote spacing exactly as root.ai.md says (between two stacked quotes use `margin-bottom: 0.75em;` on the first reference line).
- Bold (`**…**`) the key words inside a quote is allowed.

## Images
- One right-floated image per content slide: `![](pics/<Name>.jpg style="float: right; width: <W>rem")`. Width by aspect: portrait 7rem, square 8rem, landscape 10–11rem (check with Python PIL).
- Reuse existing repo images: inventory with `find R/docs -iname "*.jpg" -o -iname "*.png" | grep -v markdeep`. Prefer slide-specific ones; Creation-relevant pics already in `R/docs/Creation/pics/`. Also the unit's own diagrams: `GenesisInterpretations.svg` (Deck 2 roadmap – reference as `pics/GenesisInterpretations.svg`, landscape ~11rem or larger on its own slide), `day-age-timeline.png`, `DayAgeOfficialTimeLine.jpg`, `FatManSpandexYomDay1.jpg`, `BibleNatureTheologyScience.png`, `BigBangModel.png`.
- Images from Ingmar's notes media folders (`R/md/Creation/Notes/**/media/`) may be used too.
- Copy every image you use into `R/docs/Creation/pics/` (keep the filename; if a different image with the same name already exists there, pick another name). Verify every referenced path exists.
- Skip images whose embedded text names a different topic.

## Checks before you finish
1. `node R/tools/check-slide-overflow.js R/docs/Creation/<your file>.html` must report 0 clipped slides. Fix by shortening or splitting, not by shrinking images below the widths above.
2. Outline anchors: title is slide #0; count `---` separators to verify each `#slideN` points at its `# Section` divider (e.g. `awk 'BEGIN{n=0} /^---\r?$/{n++} /^# /{print n": "$0}' file`).
3. `python -c` scan: 0 em dashes (outside NKJV quotes), 0 curly quotes, no `...` except `[...]`.
4. Every image path exists in `R/docs/Creation/pics/`.

## Motivation slide (science decks 3–7)
Right after "Where We Are": "Why This Deck: Has Science Disproven the Bible?" – Psalm 111:2, then: schools and universities teach science has disproven the Bible; science done well supports creation and with it the Bible; then the deck's own claim in one line.

## Navigation slide (last content slide)
```
## Navigation

* [Return to Creation Overview](Creation.Slides.html)
* Prev: [<prev title>](<prev file>.html)
* Next: [<next title>](<next file>.html)
* [Creekside Defenders Main Page](../CreeksideDefenders.html)
```
Deck file names/titles:
1 Creation.Slides.1.CreationOutOfNothing – Creation out of Nothing
2 Creation.Slides.2.TheDaysOfGenesis – The Days of Genesis
3 Creation.Slides.3.PhysicsBeginningDesignAndStarlight – Physics: Beginning, Design, and Starlight
4 Creation.Slides.4.GeologyTheFloodFossilsAndTheAgeOfTheEarth – Geology: The Flood, Fossils, and the Age of the Earth
5 Creation.Slides.5.ChemistryTheOriginOfLife – Chemistry: The Origin of Life
6 Creation.Slides.6.BiologyMutationsDesignAndCommonAncestry – Biology: Mutations, Design, and Common Ancestry
7 Creation.Slides.7.TheOriginOfMan – The Origin of Man
8 Creation.Slides.8.ProvidenceGodsDecreeAndHumanFreedom – Providence: God's Decree and Human Freedom
9 Creation.Slides.9.MiraclesDoesScienceRuleThemOut – Miracles: Does Science Rule Them Out?
10 Creation.Slides.10.TheInvisibleCreationAngelsAndDemons – The Invisible Creation: Angels and Demons

Deck 10 has no Next. Cross-references to other decks in bullets: "(Deck N)" or a relative link to the file.

## Credits slide
Format as in Deck 1: **Ingmar Bitter**, slides content; **William Lane Craig**, *Defenders ...*, Parts ..., with the reasonablefaith.org URL sub-bullet (if Craig is used); then the other authors/organizations actually used (bold name, work, role).

## Report back (short)
File written, slide count, the Outline sections, any sources you could not use or quotes you could not verify, any judgment calls Ingmar should review (list them), and the overflow-check result.
