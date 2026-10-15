from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
import subprocess
import re
errors=[]
class Check(HTMLParser):
    def handle_starttag(self, tag, attrs):
        for key,value in attrs:
            if key in ('href','src') and value and not urlsplit(value).scheme and not value.startswith('#'):
                target=urlsplit(value).path
                if target and not Path(target).exists(): errors.append(target)
for page in Path('.').glob('*.html'):
    html = page.read_text(encoding='utf-8')
    Check().feed(html)
    if page.name != '404.html':
        assert '<script defer src="js/main.js">' in html, page
    assert 'type="module"' not in html, page
    assert 'href="css/site.css"' in html, page
    assert html.count('<h1>') == 1, page
    navigation = re.search(r'<nav\b[^>]*>(.*?)</nav>', html, re.S)
    if page.name == '404.html':
        assert not navigation and '<header' not in html and '<footer' not in html, page
        assert '<script' not in html and 'href="index.html"' in html, page
    else:
        assert navigation, page
        assert re.findall(r'href="([^"]+)"', navigation.group(1)) == ['index.html'] + ['404.html'] * 6, page
        footer = re.search(r'<footer\b[^>]*>(.*?)</footer>', html, re.S)
        assert footer, page
        footer_links = re.findall(r'href="([^"]+)"', footer.group(1))
        assert set(footer_links) == {'index.html', '404.html'}, page
    if Path('dist').exists():
        assert (Path('dist') / page.name).read_text(encoding='utf-8') == html, page
styles=Path('css/site.css').read_text(encoding='utf-8')
home=Path('index.html').read_text(encoding='utf-8')
insight_cards=re.search(r'<div class="cards articles">(.*?)</section>', home, re.S)
assert insight_cards, 'Latest Thinking cards are missing'
insight_images=re.findall(r'<img\b[^>]*class="insight-photo"[^>]*>', insight_cards.group(1))
assert len(insight_images)==3, 'Each Latest Thinking card must contain a photo'
for image in insight_images:
    src=re.search(r'src="([^"]+)"',image).group(1)
    assert Path(src).read_bytes().startswith(b'\xff\xd8'), f'Invalid JPEG: {src}'
assert '@import' not in styles
assert styles.index(':root') < styles.index('/* pages */') < styles.index('/* responsive */')
for script in Path('js').glob('*.js'):
    subprocess.run(['node','--check',str(script)],check=True)
assert not errors,errors
print(f'PASS: {len(list(Path(".").glob("*.html")))} pages, local links, direct-open script loading, stylesheet order and JavaScript syntax.')
