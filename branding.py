"""Shared Stackly branding for every generated page."""
import re

LOGO = '<img class="stackly-logo" src="assets/images/stackly-logo.png" alt="Stackly" width="346" height="100" decoding="async">'

def brand_html(html):
    for old, new in [('Aurelion Capital', 'Stackly'), ('AURELION CAPITAL', 'STACKLY'),
                     ('AURELION', 'STACKLY'), ('Aurelion', 'Stackly'), ('aurelion', 'stackly'),
                     ('AC / PERSPECTIVES', 'STACKLY / PERSPECTIVES')]:
        html = html.replace(old, new)
    html = re.sub(r'<a\b[^>]*class="brand"[^>]*>.*?</a>',
                  lambda _: '<a class="brand" href="index.html" aria-label="Stackly home">' + LOGO + '</a>', html, flags=re.S)
    html = re.sub(r'<p class="error-brand">.*?</p>',
                  lambda _: '<div class="error-brand">' + LOGO + '</div>', html, flags=re.S)
    return html
