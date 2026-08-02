# this file is `<RepoRoot>/.ai.md/root.ai.md`

## .ai.md lookup rules

- On startup, read all `*.ai.md` files in `<RepoRoot>/.ai.md/`, but not its subfolders

## context.ai.md rules

- Always maintain a `context.ai.md` file in `<RepoRoot>/.ai.md/` throughout the conversation
- Update it whenever a significant decision is made, a task is completed, or a new todo item is discussed
- The file must contain:
  - **## Summary** -- brief summary of what has been discussed and accomplished in the current conversation
  - **## Todo** -- list of items discussed but not yet completed, so work can resume after a conversation restart
- Keep it concise -- this is a working scratchpad, not a detailed log

## General rules

- Focus on the task at hand; avoid scope creep but suggest relevant improvements when they prevent bugs or improve maintainability
- When editing is sufficient, prefer it over creating new files
- NEVER proactively create documentation files unless explicitly requested
- Unless there is minimal scope in your response, first make a list of todo items, then work on each in turn showing progress along the way
- If some requirement is not clear or there are ambiguous interpretations or multiple options, ask clarifying questions before implementing
- For any path, use linux style '/', not '\' or '\\'

## Git conventions

- Do not add Co-Authored-By or author attribution lines to git commit messages
- Commit message format: `<subject>: <what changed>` (e.g., "Christ slides: Adds overview and incarnation slides")
- Create checkpoint commits before major restructuring

## Prompt shortcuts

- interpret the prompt "rs" as "(r)ead your (s)tartup files"
- interpret "CR" as "do a review of all source files in the project that changes were made in"
- interpret the prompt "cd" as "do a context dump, write everything relevant in the current conversation into memory so that I can close this conversation and pick it up at a later point"

---

## CRITICAL: Scripture Verification Protocol

1. **Source:** <https://www.blueletterbible.org/nkjv/[book]/[chapter]/[verses>]
2. **Process:**
   - Fetch the actual page from Blue Letter Bible
   - Copy the NKJV text verbatim
   - Verify punctuation, capitalization, and formatting match exactly
3. **Never recite from memory** -- always verify against authoritative source

## Slide Deck Structure (Argument Flow)

Craig's lecture method (state the view → defend → re-state in synthesis) bakes in repetition: Scripture and the interpretations each get re-treated two or three times across a unit. Default to this **compact, evidence-first** structure instead, which cites each passage **once**:

1. **State the interpretations** — present the candidate theological views up front, *defined but not yet argued*. Exposition only: what each view claims, no defense and no challenges. Keep it crisp, like a hypothesis list, so the audience can evaluate the evidence that follows.
2. **Review the relevant Scripture** — walk the key passages once. For **each** passage, add bullets noting how it **supports** or **challenges** the interpretations from step 1. This is the only place Scripture is quoted; it does double duty as both the biblical data and the basis for the later objections.
3. **Revisit the interpretations** — for each view, summarize the challenges (their biblical basis is already established in step 2 — refer back, do not re-quote), give the answers to those challenges, and state a conclusion on whether the view can be adopted today.
4. **Application** — practical takeaways.

**Two modes — signal which one the deck is in:**

- **(a) Non-exclusive interpretations** (complementary facets, e.g. the motifs/"diamond" of Christ's death): step 3 is *integration*, not adjudication — all the views are adopted together. Be **assertive throughout**.
- **(b) Exclusive interpretations** (genuine rivals, e.g. Calvinism vs. Arminianism, molinism): steelman each view fairly in step 1, keep step 2's support/challenge bullets honestly cutting **both ways**, and stay **balanced** until step 3, where the cons and their answers reveal which side is more compelling. Do not stack step 2 toward the favored side — that begs the question.
- **(c) Hypothesis-trial decks** (apologetics with many rival explanations of agreed evidence, e.g. resurrection alternatives): with 5+ rivals, do NOT state all views up front and revisit later — the gap between statement and verdict overloads memory. Instead: establish the **facts** once (compressed; refer back to prior decks for their defense), state the **judging criteria** (e.g. McCullagh), then run each rival chronologically as an **adjacent pair**: statement slide (fair exposition, steelmanned) -> "Why X Fails" slide (multi-slide rebuttals: "Why X Fails (1) — ..."). Views whose refutation is self-contained may be single statement-plus-verdict slides. Close the parade with the weakest/terminal view as the bridge into the positive case, then argue the favored hypothesis against the same criteria. (Established in Christ Deck 8; see `md/Christ/Christ.Slides.8.Structure.md` for a worked example.)

**Cautions:**

- Step 1 must make each view *intelligible* without arguing it — define the position, withhold the case for it.
- For decks taught live, some deliberate restatement aids retention (e.g. a one-line recap of each view at the step-3 verdict) even when the argument no longer strictly requires it.

## Encoding Standards (Slide Files)

Slide `.md` files render as HTML via Markdeep, so use proper Unicode:

- **Quotes:** Use ASCII straight quotes `"` (avoids encoding issues with the Edit tool)
- **Apostrophes:** Use ASCII apostrophe `'`
- **Em Dashes:** Use em dash, NOT hyphens or double hyphens
- **Ellipsis:** Use horizontal ellipsis, NOT three periods
- **Arrows:** Use rightwards arrow, NOT -> or question marks

When fixing encoding issues, systematically replace:

- Mojibake characters -> appropriate Unicode character based on context
- Curly quotes -> ASCII straight quotes
- `--` -> em dash
- `...` -> `[...]` (for scripture ellipsis) or ellipsis (for general)

## Scripture Formatting

### Pronoun Capitalization

Capitalize pronouns (He, Him, His) when referring to God, Christ, or the Holy Spirit in slide commentary text, matching the convention used in NKJV scripture quotes.

### Full Book Names Only

**NEVER use abbreviations.** Always spell out: Exodus (NOT Ex), Numbers (NOT Num), Judges (NOT Judg), Chronicles (NOT Chr), Ezekiel (NOT Ezek), Corinthians (NOT Cor), etc.

### Scripture Quote Format (Slides)

```markdown
<p style="font-family: 'EB Garamond', serif; font-style: italic;">"[NKJV text verbatim]"</p><p style="text-align: right; margin-top: -1.25em; margin-bottom: -0.75em;"> <em>[Full Book Name] [Chapter]:[Verses] (NKJV)</em></p>
```

Use the template margins for new quotes. Some slides have hand-adjusted margin values — do not change those.


**Bold emphasis permitted:** You may use markdown `**` (preferred) or `<b>` tags inside scripture quotes to highlight the words most relevant to the slide's topic. The base text must still be NKJV verbatim.

**Non-biblical primary sources** (e.g. the Qur'an) may use the same quote styling when the slide engages that source directly; attribute clearly (e.g. `Qur'an, Surah 4:157`). The NKJV verification protocol applies only to Bible quotes.
If you stack multiple scripture quotes on the same slide, use `margin-bottom: -1.5em;` on intermediate reference lines and `margin-bottom: -0.75em;` on the final one.

### Ellipsis in Scripture Quotes

When omitting text within quotes, use `[...]` format with a space before and after.

## Markdeep Slide Numbering

The title slide (first `#` heading) is slide **#0**. The first `##` content slide is **#1**, and so on.

## Markdown Formatting Standards

All `---` dividers MUST be surrounded by empty lines (required for Markdeep rendering).

## File Management

### File Structure

```
md/<Topic>/...                  -> Source Markdown (authoritative)
docs/<Topic>/...                -> Rendered Markdeep HTML (generated output)

# Slide decks
md/<Topic>/<Deck>.Slides.md                               -> Deck TOC / index (source)
md/<Topic>/<Deck>.Slides.<N>.<Subtitle>.md                -> Slide page (source)
docs/<Topic>/<Deck>.Slides.html                           -> Deck TOC / index (rendered copy)
docs/<Topic>/<Deck>.Slides.<N>.<Subtitle>.html            -> Slide page (rendered copy)
```

### Docs Folder Rule

- `docs/` is output-only: **do not place source `.md` files in `docs/`**.
- Exception: third-party/library docs that already live under `docs/markdeep-slides/`.

### Working Docs (md-only)

- `md/<Topic>/<Deck>.Slides.<N>.Structure.md` — plain-markdown (not Markdeep) outline/planning doc for restructuring a deck; source-only, **never mirrored to `docs/`**.

### Slide Page Naming Rules

- Use the pattern: `Deck.Slides.<N>.<Subtitle>`.
- `<Subtitle>` must be **CamelCase**, derived from the TOC title, and should omit punctuation.
- Avoid underscores; use dots only for the `Slides.<N>.<Subtitle>` separators.

### Renaming Rule (Slides)

If you rename slide pages:

- Perform **real filesystem renames** for both the `md/` source and the matching `docs/` `.html`.
- Update all links (TOC + Prev/Next) in both `md/<Topic>/<Deck>.Slides.md` and `docs/<Topic>/<Deck>.Slides.html`, and within the slide pages themselves.

### Sync to HTML

After editing a slide file, sync it:

```powershell
# Single file (keep the same base name; only extension changes)
Copy-Item "md/<Topic>/<file>.md" "docs/<Topic>/<file>.html"

# Whole deck (copy all slide sources + TOC in one go)
Get-ChildItem "md/<Topic>/<Deck>.Slides*.md" | ForEach-Object {
  $dest = Join-Path "docs/<Topic>" ($_.BaseName + ".html")
  Copy-Item $_.FullName $dest -Force
}
```

## Markdeep Slide Configuration

```javascript
markdeepSlidesOptions = {
    aspectRatio: 16 / 9,
    theme: "../markdeep-slides/themes/dark.css",
    fontSize: 28,
    diagramZoom: 1.0,
    totalSlideNumber: false,
    progressBar: true,
    breakOnHeadings: false,
    slideChangeHook: (oldSlide, newSlide) => {},
    modeChangeHook: (newMode) => {}
};
```

**CRITICAL:** Ensure no duplicate content after the `<!-- Markdeep slides stuff -->` comment line.

## Quality Checklist Before Presentation

- [ ] All Scripture quotes verified against blueletterbible.org
- [ ] All encoding issues fixed (no mojibake characters)
- [ ] All book names spelled out in full
- [ ] No duplicate content in file
- [ ] File synced to HTML
- [ ] Navigation links working
