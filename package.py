from pathlib import Path
import shutil
import argparse
parser=argparse.ArgumentParser(description='Prepare website assets; optionally create a hosting copy.')
parser.add_argument('--deploy', action='store_true', help='Create dist/ for hosting.')
args=parser.parse_args()
p=Path('.')
hero=p/'css/hero.css'
import re
css=hero.read_text()
css=re.sub(r"url\('../assets/images/investment-banking-hero.png'\),url\('https://images.unsplash.com/[^']+'\)","url('../assets/images/architecture.jpg')",css)
if (p/'assets/images/investment-banking-hero.png').exists():
    css=css.replace("url('../assets/images/architecture.jpg')","url('../assets/images/investment-banking-hero.png')")
hero.write_text(css)

from prepare import prepare
prepare()
if args.deploy:
    d=p/'dist'
    d.mkdir(exist_ok=True)
    for f in p.glob('*.html'): shutil.copy2(f,d/f.name)
    for name in ['assets','css','js']: shutil.copytree(p/name,d/name,dirs_exist_ok=True)
    print('Hosting copy created in dist/')
else:
    print('Website assets prepared in the main folder; no duplicate pages created.')
