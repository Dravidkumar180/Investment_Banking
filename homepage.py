"""Homepage composition and locally stored editorial photography."""
import re

PHOTOS = {
    'advisory': 'Contemporary office meeting space overlooking the city',
    'markets': 'Financial district architecture viewed from street level',
    'technology': 'Modern glass towers in a business district',
    'healthcare': 'Modern clinical equipment in a hospital operating room',
    'energy': 'Solar panels capturing renewable energy',
    'city': 'City skyline and illuminated buildings at dusk',
}

def photo(name, cls='card-photo'):
    return f'<img class="{cls}" src="assets/images/{name}.jpg" alt="{PHOTOS[name]}" width="1000" height="667" loading="lazy" decoding="async">'

def refine_home(html):
    # Service cards retain their working detail accordions.
    images = iter(['advisory', 'markets', 'city', 'technology'])
    html = re.sub(r'(<article class="card filter-item reveal"[^>]*>)', lambda m: m[0] + photo(next(images)), html)

    sectors = [('Technology', 'technology'), ('Healthcare', 'healthcare'),
               ('Financial Services', 'markets'), ('Real Estate', 'city'),
               ('Energy', 'energy'), ('Infrastructure', 'advisory')]
    sector_grid = '<div class="sector-grid">' + ''.join(
        f'<a class="sector-card" href="industries.html">{photo(image, "sector-photo")}<span class="sector-caption"><span>{title}</span><span aria-hidden="true">↗</span></span></a>'
        for title, image in sectors) + '</div>'
    html = re.sub(r'<div class="industry-strip">.*?</div>', lambda _: sector_grid, html, count=1, flags=re.S)

    # Add photographs above each fictional transaction's information.
    def deals(match):
        images = iter(['technology', 'energy', 'healthcare'])
        return re.sub(
            r'<article>', lambda _: '<article>' + photo(next(images), 'deal-photo'), match[0])
    html = re.sub(r'<div class="deals">.*?</div>', deals, html, count=1, flags=re.S)

    article_images = ['city', 'advisory', 'technology', 'markets']
    html = re.sub(r'<div class="article-art art-(\d)">\s*<span>[^<]*</span>\s*</div>',
                  lambda m: '<div class="article-art">' + photo(article_images[int(m[1])], 'insight-photo') + '</div>', html)
    # Three featured stories create one balanced editorial row; all four remain on Insights.
    html = re.sub(r'<article class="card filter-item" data-category="Research">.*?</article>', '', html, flags=re.S)
    html = html.replace('<p class="intro"></p>', '')
    html = html.replace('<h2>Your ambition.<br>Our conviction.</h2>',
                        '<h2>Your ambition.<br>Our conviction.</h2><p>Independent advice starts with understanding what matters to you. We bring focus, discipline and a long-term perspective to each decision.</p>' + photo('advisory', 'approach-photo'))
    return html
