#!/usr/bin/env node
/**
 * check-slide-overflow.js - detect slide content clipped by .slide-content { overflow: hidden }
 *
 * Markdeep slides silently CLIP anything that does not fit the slide box, so an
 * overlong bullet simply disappears when presenting. This renders each deck in
 * headless Chrome and measures every leaf element against the content box.
 *
 *   node tools/check-slide-overflow.js                       # every deck under docs/
 *   node tools/check-slide-overflow.js docs/Christ           # one folder
 *   node tools/check-slide-overflow.js docs/Christ/X.html    # one deck
 *
 * Exit code 0 = nothing clipped, 1 = at least one slide overflows, 2 = setup problem.
 *
 * Section dividers and title slides report a constant ~85px from vertical
 * centering; those are skipped (the only leaf is the heading itself).
 */

const fs = require('fs');
const path = require('path');
const os = require('os');
const { execFileSync } = require('child_process');

const REPO = path.resolve(__dirname, '..');
const TOLERANCE_PX = 2;      // sub-pixel rounding
const DIVIDER_SLACK = 4;     // heading-only slides: ignore centering artifact

function findChrome() {
  if (process.env.CHROME_PATH && fs.existsSync(process.env.CHROME_PATH)) return process.env.CHROME_PATH;
  const candidates = [
    'C:/Program Files/Google/Chrome/Application/chrome.exe',
    'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe',
    'C:/Program Files/Microsoft/Edge/Application/msedge.exe',
    'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
    '/usr/bin/google-chrome',
    '/usr/bin/chromium',
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  ];
  return candidates.find(p => fs.existsSync(p));
}

const PROBE = `
<script>
window.addEventListener("load", function () {
  setTimeout(function () {
    var out = [];
    document.querySelectorAll(".slide").forEach(function (sl, i) {
      var c = sl.querySelector(".slide-content");
      if (!c) return;
      var cb = c.getBoundingClientRect();
      var worst = -99999, what = "";
      c.querySelectorAll("li,p,img,h1,h2,h3,table,pre,blockquote").forEach(function (el) {
        if (el.querySelector("li,p,img,table")) return;   // leaves only
        var r = el.getBoundingClientRect();
        if (r.height === 0) return;
        var spill = Math.round(r.bottom - cb.bottom);
        if (spill > worst) { worst = spill; what = (el.textContent || el.tagName).trim().slice(0, 60); }
      });
      var h = sl.querySelector("h1,h2");
      var title = h ? h.textContent.trim().slice(0, 60) : "";
      var row = document.createElement("i");
      row.className = "slide-overflow-row";
      row.setAttribute("data-slide", String(i));
      row.setAttribute("data-spill", String(worst));
      row.setAttribute("data-title", title);
      row.setAttribute("data-cut", what);
      out.push(row);
    });
    var box = document.createElement("div");
    box.id = "SLIDE_OVERFLOW_REPORT";
    out.forEach(function (r) { box.appendChild(r); });
    document.body.appendChild(box);
  }, 2500);
});
</script>
`;

function decksIn(target) {
  const abs = path.resolve(REPO, target);
  if (fs.statSync(abs).isFile()) return [abs];
  const out = [];
  (function walk(dir) {
    for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
      const p = path.join(dir, entry.name);
      if (entry.isDirectory()) {
        if (entry.name !== 'markdeep-slides' && entry.name !== 'pics') walk(p);
      } else if (entry.name.endsWith('.html') && !entry.name.startsWith('_')) {
        // a deck is any page wiring up markdeep-slides
        if (fs.readFileSync(p, 'utf8').includes('markdeep-slides.js')) out.push(p);
      }
    }
  })(abs);
  return out.sort();
}

function checkDeck(chrome, deck) {
  // the probe copy must sit beside the original so its relative asset paths resolve
  const probeFile = path.join(path.dirname(deck), `_overflowprobe_${process.pid}.html`);
  fs.writeFileSync(probeFile, fs.readFileSync(deck, 'utf8') + PROBE);
  let dom = '';
  try {
    dom = execFileSync(chrome, [
      '--headless=new', '--disable-gpu', '--no-sandbox', '--hide-scrollbars',
      '--window-size=1920,1080', '--virtual-time-budget=30000',
      '--dump-dom', 'file:///' + probeFile.replace(/\\/g, '/'),
    ], { encoding: 'utf8', maxBuffer: 64 * 1024 * 1024, stdio: ['ignore', 'pipe', 'ignore'] });
  } finally {
    fs.unlinkSync(probeFile);
  }

  if (process.env.OVERFLOW_DEBUG) {
    fs.writeFileSync(path.join(os.tmpdir(), 'overflow_dump.html'), dom);
    console.error(`[debug] ${dom.length} bytes, report present: ${dom.includes('SLIDE_OVERFLOW_REPORT')}`);
  }
  if (!dom.includes('SLIDE_OVERFLOW_REPORT')) return null;   // page never reported

  const unescape = s => s.replace(/&quot;/g, '"').replace(/&#39;/g, "'")
                         .replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&');
  const rows = [];
  const re = /data-slide="(\d+)" data-spill="(-?\d+)" data-title="([^"]*)" data-cut="([^"]*)"/g;
  let m;
  while ((m = re.exec(dom)) !== null) {
    const px = parseInt(m[2], 10);
    const title = unescape(m[3]), cut = unescape(m[4]);
    // heading-only slides (title page, section dividers) are vertically centered
    // and always report a constant offset - that is not a clip
    const headingOnly = cut && title && cut.startsWith(title.slice(0, 30));
    const limit = headingOnly ? 90 + DIVIDER_SLACK : TOLERANCE_PX;
    if (px > limit) rows.push({ num: Number(m[1]), px, title, what: cut });
  }
  return rows;
}

function main() {
  const chrome = findChrome();
  if (!chrome) {
    console.error('No Chrome or Edge found. Set CHROME_PATH to the browser executable.');
    process.exit(2);
  }
  const targets = process.argv.slice(2).length ? process.argv.slice(2) : ['docs'];
  let decks = [];
  for (const t of targets) decks = decks.concat(decksIn(t));
  if (!decks.length) { console.error('No decks found in: ' + targets.join(', ')); process.exit(2); }

  let bad = 0, checked = 0;
  for (const deck of decks) {
    const rel = path.relative(REPO, deck).replace(/\\/g, '/');
    const rows = checkDeck(chrome, deck);
    if (rows === null) { console.log(`?  ${rel}  (no report - did it render?)`); continue; }
    checked++;
    if (!rows.length) { console.log(`OK ${rel}`); continue; }
    bad += rows.length;
    console.log(`!! ${rel}`);
    for (const r of rows) {
      console.log(`     slide ${String(r.num).padEnd(3)} clipped by ${String(r.px).padStart(4)}px  ${r.title}`);
      console.log(`       cut: ${r.what}`);
    }
  }
  console.log(`\n${checked} deck(s) checked, ${bad} slide(s) clipped.`);
  process.exit(bad ? 1 : 0);
}

main();
