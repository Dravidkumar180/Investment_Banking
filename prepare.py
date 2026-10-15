"""Generate browser-ready assets without requiring a server or dependencies."""
from pathlib import Path
import re
from branding import brand_html
from footer import footer_html

ROOT = Path(__file__).resolve().parent
MODULES = ['navigation', 'animations', 'counters', 'charts', 'filters', 'carousel', 'forms']

def prepare():
    # Isolate module variables while allowing classic scripts to run over file://.
    chunks = ['/* Generated from the individual JavaScript feature files. */']
    for name in MODULES:
        source = (ROOT / 'js' / (name + '.js')).read_text(encoding='utf-8')
        chunks.append(f'// {name}\n(function () {{\n"use strict";\n{source}\n}})();')
    (ROOT / 'js/main.js').write_text('\n\n'.join(chunks) + '\n', encoding='utf-8')

    global_css = (ROOT / 'css/global.css').read_text(encoding='utf-8')
    base = re.sub(r"@import\s+url\([^)]*\);\s*", '', global_css)
    styles = [base]
    for name in ['navbar', 'hero', 'components', 'animations', 'pages', 'responsive', 'home', 'error', 'brand', 'footer']:
        styles.append(f'/* {name} */\n' + (ROOT / 'css' / (name + '.css')).read_text(encoding='utf-8'))
    (ROOT / 'css/site.css').write_text('\n\n'.join(styles), encoding='utf-8')

    # Keep the requested header destinations consistent on every page.
    template = (ROOT / 'about.html').read_text(encoding='utf-8')
    error_content = '''<body class="error-page">
<main id="main" class="error-layout">
<div class="error-card">
<p class="error-brand">STACKLY <span>CAPITAL</span></p>
<div class="error-number" aria-hidden="true">404</div>
<p class="eyebrow">PAGE NOT FOUND</p>
<h1>A moment off course.</h1>
<p class="error-description">The page you’re looking for is currently unavailable.<br>Let’s take you back to familiar ground.</p>
<a class="button gold" href="index.html"><span aria-hidden="true">←</span> Back to Home</a>
<p class="error-note">Independent thinking. Enduring value.</p>
</div>
</main>
</body>'''
    error_page = re.sub(r'<body\b[^>]*>.*?</body>', lambda _: error_content, template, count=1, flags=re.S)
    error_page = re.sub(r'<script\b[^>]*>.*?</script>', '', error_page, flags=re.S)
    error_page = re.sub(r'<title>.*?</title>', '<title>404 — Page Not Found | Stackly</title>', error_page, count=1)
    error_page = re.sub(r'<meta property="og:title"[^>]*>', '<meta property="og:title" content="404 — Page Not Found | Stackly">', error_page, count=1)
    error_page = error_page.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n<meta name="robots" content="noindex">')
    (ROOT / '404.html').write_text(error_page, encoding='utf-8')

    for page in ROOT.glob('*.html'):
        html = brand_html(page.read_text(encoding='utf-8'))
        if page.name != '404.html':
            html = re.sub(r'<footer\b[^>]*>.*?</footer>', lambda _: footer_html(), html, count=1, flags=re.S)
        def redirect_header(match):
            return re.sub(r'href="(?:about|services|industries|insights|careers|contact)\.html"', 'href="404.html"', match.group(0))
        html = re.sub(r'<nav\b[^>]*>.*?</nav>', redirect_header, html, count=1, flags=re.S)
        html = html.replace('href="css/global.css"', 'href="css/site.css"')
        html = html.replace('<script type="module" src="js/main.js"></script>', '<script defer src="js/main.js"></script>')
        # Break structural boundaries onto separate lines without changing text nodes.
        html = re.sub(r'>\s*<', '>\n<', html)
        page.write_text(html + '\n', encoding='utf-8')

if __name__ == '__main__':
    prepare()
    print('Prepared readable HTML and direct-open compatible assets.')
