// Auto-position scripture reference labels.
// When the last line of a quote is short enough, the right-aligned reference
// label is pulled up to sit beside it, saving vertical space.
(function () {
    function adjustLabel(quote) {
        var label = quote.nextElementSibling;
        if (!label) return;
        var style = label.getAttribute('style') || '';
        if (style.indexOf('text-align: right') === -1) return;
        if (quote.offsetParent === null) return;

        label.style.marginTop = '';

        var probe = document.createElement('span');
        probe.textContent = '\u200B';
        quote.appendChild(probe);
        var pr = probe.getBoundingClientRect();
        var qr = quote.getBoundingClientRect();
        quote.removeChild(probe);
        if (pr.height === 0) return;

        var labelText = label.querySelector('em') || label.firstChild;
        var lr = labelText.getBoundingClientRect();
        var fs = parseFloat(getComputedStyle(quote).fontSize) || 16;

        // Detect float images in the slide that overlap with the last line
        var floatWidth = 0;
        var slide = quote.closest('.slide-content') || quote.parentElement;
        slide.querySelectorAll('img, center, div').forEach(function (el) {
            var cs = getComputedStyle(el);
            if (cs.cssFloat === 'right' || cs.float === 'right') {
                var fr = el.getBoundingClientRect();
                if (fr.top < pr.bottom && fr.bottom > pr.top) {
                    floatWidth = Math.max(floatWidth, fr.width);
                }
            }
        });
        var floatGap = floatWidth > 0 ? floatWidth + fs * 0.2 : 0;
        var availRight = qr.right - floatGap;

        if (pr.right + fs + lr.width < availRight) {
            var lh = parseFloat(getComputedStyle(quote).lineHeight);
            if (isNaN(lh)) lh = fs * 1.3;
            label.style.marginTop = (-lh + 0.25 * fs) + 'px';
        }
    }

    function adjustAllLabels() {
        document.querySelectorAll('p[style*="EB Garamond"]').forEach(adjustLabel);
    }

    window.adjustScriptureQuoteLabels = adjustAllLabels;

    window.addEventListener('load', function () {
        setTimeout(adjustAllLabels, 500);
    });
})();
