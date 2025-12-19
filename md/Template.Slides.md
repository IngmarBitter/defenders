<meta charset="utf-8" lang="en">

**Title Goes Here**
    Subtitle / Series / Topic

<small><em><span class="current-date"></span></em></small><br>
Ingmar Bitter, PhD

---

# Section Divider Slide

---

## Regular Slide Title

* Top-level bullet
  * Nested bullet (2 spaces per indent level)
    * Deeper nested bullet (4 spaces per indent level)
* Another top-level bullet

---

## Scripture Quote Example (NKJV)

<p style="font-family: 'Gabriola', serif;">
    “Let the word of Christ dwell in you richly in all wisdom, teaching and admonishing one another in psalms and hymns and spiritual songs, singing with grace in your hearts to the Lord.”
</p><p style="text-align: right; margin-top: -1.25em; margin-bottom: -0.75em;"> <em>Colossians 3:16 (NKJV)</em></p>

* Use the same Gabriola quote block style for all Scripture quotations
* If you omit part of a verse, mark the omission inside the quote as `[…]` (do not label references with “(excerpt)”) 

---

## Omissions Example

<p style="font-family: 'Gabriola', serif;">
    “[…] the Holy Spirit said, ‘Now separate to Me Barnabas and Saul for the work to which I have called them.’”
</p><p style="text-align: right; margin-top: -1.25em; margin-bottom: -0.75em;"> <em>Acts 13:2 (NKJV)</em></p>

* Keep the exact phrase “the Holy Spirit said,” when that’s the point of the citation
* Put `[…]` inside the quote at the omission point
* No worries about copyright, this work is for educational purposes so has the right to quote

---

## Notes / House Rules

* Slide breaks use `---` on its own line
* Section divider slides use `# Heading`
* Normal slides use `## Heading`
* Nested lists always use 2 spaces per level

---

## Paths (When Copied to HTML)

* These decks are typically copied to `docs/<topic>/...Slides.html`
* If the resulting HTML is one folder deep under `docs/`, keep the `../markdeep-slides/...` paths below
* If the resulting HTML is directly under `docs/`, change paths below to `./markdeep-slides/...`

---

## Formatting Rules for Clean Slides

* **Slide separators**: Use exactly `---` (3 dashes) with empty lines before and after
* **Headers**: `##` headers must have an empty line after them
* **Bullets**: No empty lines between bullet points (including indented sub-bullets)
* **Spacing**: No multiple consecutive empty lines anywhere
* **Footer**: Keep Markdeep scripts compact without empty lines between blocks
* **Copy to HTML**: Use `Copy-Item "md\Trinity\Topic.Slides.X.md" "docs\Trinity\Topic.Slides.X.html" -Force` to create identical HTML files
* **Viewing**: Open `.html` files in VS Code's Simple Browser for proper rendering

---

## Multi-Part Presentations

For long presentations that span multiple weeks:

* Split the content into separate `.md` files (e.g., `Topic.Slides.0.md` for TOC, `Topic.Slides.1.md` for section 1, etc.)
* Each `.md` file must start with `<meta charset="utf-8" lang="en">` and end with the complete Markdeep scripts block
* The TOC file (`.0.md`) includes a table of contents with links to the section files
* Copy each `.md` to `.html` with identical content: `Copy-Item "md\Trinity\Topic.Slides.X.md" "docs\Trinity\Topic.Slides.X.html" -Force`
* Open the `.html` files in VS Code's Simple Browser for proper slide rendering

---

<!-- Markdeep slides stuff -->
<script>
    markdeepSlidesOptions = {
        aspectRatio: 16 / 9,
        theme: '../markdeep-slides/themes/dark.css',
        fontSize: 28,
        diagramZoom: 1.0,
        totalSlideNumber: false,
        progressBar: true,
        breakOnHeadings: false,
        slideChangeHook: (oldSlide, newSlide) => {},
        modeChangeHook: (newMode) => {}
    };
</script>
<link rel="stylesheet" href="../markdeep-slides/lib/markdeep-relative-sizes/1.11/relativize.css">
<link rel="stylesheet" href="../markdeep-slides/markdeep-slides.css">
<script src="../markdeep-slides/markdeep-slides.js"></script>

<script>
    markdeepOptions = {
        tocStyle: 'none',
        detectMath: false,
        onLoad: function() {
            initSlides();
        }
    };
</script>
<style class="fallback">body{visibility:hidden;white-space:pre;font-family:monospace}</style>
<script src="../markdeep-slides/lib/markdeep/1.11/markdeep.min.js" charset="utf-8"></script>
<script>window.alreadyProcessedMarkdeep||(document.body.style.visibility="visible")</script>
