# Editorial Standards for Holy Spirit Presentation

This document captures all editorial instructions and standards established during the development of HolySpirit.Slides.5.md. Use this as a reference for consistency across all presentation files.

---

## CRITICAL: Scripture Verification Protocol

### All Scripture Quotes MUST Be Verified
1. **Source:** https://www.blueletterbible.org/nkjv/[book]/[chapter]/[verses]
2. **Process:**
   - Fetch the actual page from Blue Letter Bible
   - Copy the NKJV text verbatim
   - Verify punctuation, capitalization, and formatting match exactly
3. **Never recite from memory** - always verify against authoritative source

---

## Encoding Standards

### Required Unicode Characters
- **Quotes:** Use " " (curly quotes), NOT straight quotes " "
- **Apostrophes:** Use ' (curly apostrophe), NOT straight apostrophe '
- **Em Dashes:** Use — (em dash), NOT hyphens or double hyphens
- **Ellipsis:** Use … (horizontal ellipsis), NOT three periods
- **Arrows:** Use → (rightwards arrow), NOT -> or question marks

### Search and Replace Pattern
When fixing encoding issues, systematically replace:
- � → appropriate Unicode character based on context
- Straight quotes → curly quotes
- -- → — (em dash)
- ... → […] (for scripture ellipsis) or … (for general ellipsis)

---

## Scripture Formatting

### Full Book Names Only
**NEVER use abbreviations.** Always spell out:
- Exodus (NOT Ex)
- Numbers (NOT Num)
- Judges (NOT Judg)
- Chronicles (NOT Chr)
- Ezekiel (NOT Ezek)
- Corinthians (NOT Cor)

### Scripture Quote Format
```markdown
<p style="font-family: 'Gabriola', serif;">"[NKJV text verbatim]"</p><p style="text-align: right; margin-top: -1.75em; margin-bottom: -0.75em;"> <em>[Full Book Name] [Chapter]:[Verses] (NKJV)</em></p>
```

**Margin adjustments:**
- `-1.25em` for shorter slides
- `-1.75em` for longer slides
- Adjust to prevent excessive white space

### Ellipsis in Scripture Quotes
When omitting text within quotes, use `[…]` format:
```markdown
"First part of verse […] continuation after omission"
```

---

## Markdown Formatting Standards

### Section Dividers
All `---` dividers MUST be surrounded by empty lines:

**Correct:**
```markdown
* Last bullet point

---

## Next Section Header
```

**Incorrect:**
```markdown
* Last bullet point
---
## Next Section Header
```

This ensures proper rendering in Markdeep slides.

---

## Section Structure Standards

### 11 Primary Ministries
Each ministry gets its own `#` (H1) section:

1. **(1) Creation** - Genesis 1:2, Job 33:4, Job 26:13
2. **(2) Revelation** - 1 Corinthians 2:9-13, John 16:13
3. **(3) Inspiration of Scripture** - 2 Peter 1:20-21
4. **(4) Conception of Christ** - Luke 1:35, Matthew 1:18,20
5. **(5) Spiritual Birth** - John 3:5-7, Revelation 7:4-9
6. **(6) Indwelling and Spirit-Baptism** - Romans 8:9, 1 Corinthians 12:13, 1 Corinthians 6:19-20
7. **(7) Assurance of Salvation** - Romans 8:14-16
8. **(8) Sanctification** - Galatians 5:16-18
9. **(9) Spiritual Gifts** - 1 Corinthians 12:4-11 + OT examples
10. **(10) Spiritual Fruits** - Galatians 5:22-24
11. **(11) Evangelism and Witness** - Acts 1:8

### Descriptive Section Headers
Use Craig's more descriptive style:
- "Inspiration of Scripture" (NOT just "Inspiration")
- "Conception of Christ" (NOT just "Conception")
- "Indwelling and Spirit-Baptism" (includes both concepts)
- "Assurance of Salvation" (NOT just "Assurance")
- "Spiritual Fruits" (plural, NOT "Fruit")

---

## Content Integration Standards

### OT/NT Distinction Belongs in Section (9) Spiritual Gifts
**DO NOT create separate OT/NT sections.** Instead:

1. **OT Pattern: Temporary Empowerment**
   - Bezalel for craftsmanship (Exodus 31:1-3)
   - Seventy elders for governance (Numbers 11:16-17, 25)
   - Judges for deliverance: Othniel, Gideon, Jephthah, Samson
   
2. **NT Pattern: Permanent Spiritual Gifts**
   - 1 Corinthians 12:4-11
   - Spirit distributes "as He wills"
   
3. **Note: NT Adds Permanent Indwelling**
   - Reference sections 4-7 already covered
   - OT: Spirit came temporarily for tasks
   - NT: Spirit dwells permanently + gives gifts

### 144,000 Rebuttal Structure
Include in Section (5) Spiritual Birth:
1. Quote Revelation 7:4-9 showing context
2. JW interpretation (literal number, symbolic tribes)
3. Logical rebuttals:
   - Inconsistency (why literal number but symbolic tribes?)
   - Lineage problem (JWs can't trace to tribes)
   - Great multitude in heaven (contradicts earth-only view)
   - Mathematical proof: 12 apostles × 3-year discipleship × exponential growth → 144,000 filled by end of 1st century

---

## JW Rebuttal Standards

### Every Section MUST Include:
1. **JW Objection:**
   - Format: `**JWs:** [their interpretation]`
   - Must be verse-specific (not general theology)
   - Should reflect official Watchtower teaching

2. **Logical Rebuttal:**
   - Format: `**Illogical:** [specific rebuttal]`
   - Must directly address the verse-specific interpretation
   - Show internal contradiction or inconsistency
   - Use the text itself to refute the objection

### Example Pattern:
```markdown
* **JWs:** The "holy spirit" was God's force that impelled men to write
* **Illogical:** Being "moved by" someone implies personal direction, not impersonal force. The text contrasts human will with the Spirit's agency - showing two personal wills, not force vs. will
```

---

## File Management

### File Structure
```
md/Trinity/HolySpirit.Slides.5.md  → Source file
docs/Trinity/HolySpirit.Slides.5.html → Presentation file
```

### Sync to HTML Command
```powershell
Copy-Item "c:\_\me\bible\Defenders\github\defenders\md\Trinity\HolySpirit.Slides.5.md" "c:\_\me\bible\Defenders\github\defenders\docs\Trinity\HolySpirit.Slides.5.html"
```

### Git Checkpoint Protocol
- Create checkpoint commits before major restructuring
- Example: `git commit -m "Checkpoint: Pre-reorganization state"`
- Document commit hash for recovery reference
- Commit 98668b3 was used as restoration point

---

## Markdeep Slide Configuration

### Standard Settings
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

### File Structure
1. Header and metadata
2. Overview section (##)
3. 11 ministry sections (#)
4. Navigation links
5. `<!-- Markdeep slides stuff -->` comment
6. Markdeep scripts

**CRITICAL:** Ensure no duplicate content after Markdeep comment line.

---

## Quality Checklist Before Presentation

- [ ] All Scripture quotes verified against blueletterbible.org
- [ ] All encoding issues fixed (no � characters)
- [ ] All book names spelled out in full
- [ ] All sections have JW objection + rebuttal
- [ ] Section headers match descriptive standards
- [ ] OT/NT distinction integrated into Gifts section (not standalone)
- [ ] No duplicate content in file
- [ ] File synced to HTML
- [ ] Navigation links working

---

## Comparison to Craig's Material

### Coverage Completeness
Your presentations should include everything in Craig's corresponding section PLUS:
- JW-specific rebuttals
- Mathematical proofs where applicable (144,000)
- Integration of OT/NT patterns within ministry sections
- Additional Scripture quotes for comprehensiveness

### Craig's "Work of the Holy Spirit" = Your Sections 1-11
1. ~~Old Testament Activities~~ → Your **(1) Creation** (Craig mentions but doesn't list as ministry)
2. Divine revelation → Your **(2) Revelation**
3. Inspiration of Scripture → Your **(3) Inspiration of Scripture**
4. Conception of Christ → Your **(4) Conception of Christ**
5. Regeneration → Your **(5) Spiritual Birth**
6. Indwelling/baptizing → Your **(6) Indwelling and Spirit-Baptism**
7. Assurance → Your **(7) Assurance of Salvation**
8. Enablement for spiritual living → Your **(8) Sanctification**
9. Spiritual gifts → Your **(9) Spiritual Gifts**
10. Fruit of the Spirit → Your **(10) Spiritual Fruits**
11. ~~Not listed separately~~ → Your **(11) Evangelism and Witness**

---

## Common Pitfalls to Avoid

1. **DON'T** recite Scripture from memory - always verify
2. **DON'T** use abbreviated book names
3. **DON'T** create standalone OT/NT sections - integrate into ministry sections
4. **DON'T** leave duplicate content after Markdeep comment
5. **DON'T** forget to sync to HTML after edits
6. **DON'T** use generic JW rebuttals - make them verse-specific
7. **DON'T** rush - verify encoding and formatting throughout

---

## Tools and Commands

### Verify Encoding Issues
```powershell
$file = "path\to\file.md"
$content = Get-Content $file
$content | Select-String "�"
```

### Count Lines
```powershell
$content = Get-Content $file
Write-Host "Total lines: $($content.Count)"
```

### Find Section Headers
```powershell
$content | Select-String "^# \(\d+\)"
```

### Multi-Replace Pattern (PowerShell)
```powershell
$file = "path\to\file.md"
$content = Get-Content $file
$newContent = $content[0..339] + $content[427..($content.Count-1)]
$newContent | Set-Content $file
```

---

## Version Control

**Current State (2026-01-17):**
- HolySpirit.Slides.5.md: 370 lines, 11 sections
- All Scripture verified
- All encoding fixed
- All JW rebuttals present
- OT/NT integrated
- Ready for presentation

**Restoration Reference:**
- Git commit 98668b3: Stable checkpoint before major edits
- Use for recovery if needed: `git checkout 98668b3 -- [file]`

---

## Next Session Preparation

When starting the next editing session:
1. Review this document first
2. Check current state of file
3. Verify no encoding regressions
4. Apply same standards to other Holy Spirit slide files (.6-.8)
5. Maintain consistency across entire presentation series
