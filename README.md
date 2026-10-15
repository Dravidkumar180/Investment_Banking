# Stackly

A responsive, seven-page investment banking demonstration built with HTML5, CSS3 and vanilla ES modules. Four additional article pages are included. No frontend framework or build dependencies are required.

## Run with VS Code Live Server

1. Open this folder in VS Code.
2. Install the Live Server extension by Ritwick Dey.
3. Right-click `index.html` and choose **Open with Live Server**.

You can also double-click any HTML page to open it directly in your browser. The shared script is a deferred classic script, so navigation, filters, forms and charts also work without a server. Alternatively run `python -m http.server 8080` and visit http://localhost:8080.

## Hero image

The chat reference image was not available as a filesystem attachment. Save that original image as `assets/images/investment-banking-hero.png` and run `python package.py` to use it. Until then, the site uses a locally stored architectural photograph from Unsplash. Google Fonts require an internet connection; serif and sans-serif system fonts are provided as fallbacks. The exact uploaded image has not been reproduced or misrepresented as the original.

## Features

The homepage uses locally stored photography for service, industry, transaction and insight cards. Image identifiers and usage notes are recorded in `assets/images/CREDITS.md`. `homepage.py` maintains the homepage composition; `css/home.css` contains its responsive layout styles.

- Responsive navigation, active page states, scroll progress and back-to-top.
- Service detail accordions, category filters, insights search and article pages.
- Career search, role selection and PDF size/type validation.
- Accessible native form validation with explicit frontend-only feedback.
- Four SVG chart modes with accessible data descriptions.
- Animated counters, scroll reveals, manual perspective carousel and reduced-motion support.

All company statistics, transactions, roles, office locations and testimonial-style perspectives are clearly illustrative. No real licenses, results or client relationships are claimed. Forms do not send or persist information. Replace all demonstration content and connect a secure backend before using the site for real inquiries.

## Packaging

All editable HTML pages are in the main folder, with one file per page. `python build.py` regenerates these pages. After editing feature JavaScript or CSS files, run `python package.py` to refresh `js/main.js` and `css/site.css` without creating duplicate pages. Only run `python package.py --deploy` when you need a separate `dist/` hosting copy. Styles load in base-to-responsive order, without CSS imports. Every HTML page contains its own readable page content.
