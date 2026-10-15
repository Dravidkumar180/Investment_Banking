"""Shared four-column footer, matching the supplied visual reference."""
from branding import LOGO
import re

def icon(kind):
    paths = {
        'mail': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 6 9 7 9-7"/>',
        'pin': '<path d="M20 10c0 6-8 11-8 11S4 16 4 10a8 8 0 1 1 16 0Z"/><circle cx="12" cy="10" r="2.5"/>',
        'chat': '<path d="M21 11a8 8 0 0 1-8 8H7l-5 3 2-6a8 8 0 1 1 17-5Z"/>',
        'arrow': '<path d="M5 12h14m-6-6 6 6-6 6"/>',
        'home': '<path d="m3 10 9-7 9 7v11h-7v-7h-4v7H3Z"/>',
        'insights': '<path d="M5 20V10m7 10V4m7 16v-7"/>',
    }
    return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'+paths[kind]+'</svg>'

def footer_html():
    explore = [('Home','index'),('About us','about'),('Services','services'),('Industries','industries'),('Insights','insights'),('Careers','careers'),('Contact','contact')]
    expertise = ['Mergers & acquisitions','Capital raising','Capital markets','Corporate advisory','Investment management','Risk management']
    html = '''<footer class="site-footer">
<div class="footer-grid">
<div class="footer-brand-column">
<a class="brand" href="index.html" aria-label="Stackly home">'''+LOGO+'''</a>
<p>Independent financial perspective for your next chapter. Thoughtful advice to help you grow, navigate complexity, and create lasting value.</p>
<a class="footer-conversation" href="contact.html">Let’s talk about your ambitions '''+icon('arrow')+'''</a>
<div class="footer-shortcuts" aria-label="Quick actions">
<a href="index.html" aria-label="Go to homepage">'''+icon('home')+'''</a>
<a href="insights.html" aria-label="Explore market insights">'''+icon('insights')+'''</a>
<a href="contact.html" aria-label="Contact our team">'''+icon('mail')+'''</a>
</div>
</div>
<div class="footer-column"><h2>Explore</h2><ul>'''+''.join(f'<li><a href="{url}.html">{text}</a></li>' for text,url in explore)+'''</ul></div>
<div class="footer-column"><h2>Our expertise</h2><ul>'''+''.join(f'<li><a href="services.html">{text}</a></li>' for text in expertise)+'''</ul></div>
<div class="footer-column footer-contact"><h2>Get in touch</h2>
<a class="contact-row" href="contact.html">'''+icon('mail')+'''<span>Send a business inquiry</span></a>
<div class="contact-row">'''+icon('pin')+'''<span>Global perspective<br>London · New York<br>Singapore · Mumbai</span></div>
<a class="contact-row" href="contact.html">'''+icon('chat')+'''<span>Contact our team</span></a>
<p class="footer-contact-note">Illustrative locations for this demonstration website.</p>
</div>
</div>
<div class="footer-legal"><span>© 2026 Stackly. Demonstration website.</span><span>Independent thinking. Enduring value.</span></div>
<p class="footer-disclaimer">Illustrative investment banking website. No banking licenses, client relationships or investment results are represented. Forms are frontend demonstrations; no information is transmitted.</p>
</footer>'''
    return re.sub(r'href="(?:about|services|industries|insights|careers|contact)\.html"', 'href="404.html"', html)
