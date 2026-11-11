# Holy Grawlix Games: site

Source for the Holy Grawlix Games websites.

| Path | What it is | Live at |
|---|---|---|
| `index.html` | Temporary "in development" landing page | [holygrawlix.com](https://holygrawlix.com) |
| `site/index.html` | Full studio site (comic-book + 16-bit direction) | [grawlix-games.pages.dev](https://grawlix-games.pages.dev) |
| `archive/grawlix-figma-v1/` | The earlier "Grawlix Games" site, kept for reference | [grawlix-games.pages.dev/archive](https://grawlix-games.pages.dev/archive) |

Both live sites read their files straight from this repo's `main` branch, so a push goes live within a few minutes. Both are hidden from search engines for now. The contact form posts to the `respeclabs-contact` Cloudflare Worker (source in the respeclabs-site repo), which emails hello@holygrawlix.com with the subject "New message from <name> via the Holy Grawlix Games website".

## Brand (`brand/`)

| File | Use |
|---|---|
| `logo/holygrawlix-horizontal-{dark,light}.svg/.png` | Rectangular lockup, one line: HOLY [#$@!] GAMES |
| `logo/holygrawlix-stacked-{dark,light}.svg/.png` | Square lockup, three rows: HOLY / [#$@!] / GAMES |
| `logo/holygrawlix-icon.svg` | Icon-only mark: "#!" in the logo's burst shape, transparent (favicon). Deliberately irregular, not a regular toothed badge |
| `logo/icon-options/` | Alternative icon shapes (speech balloon, shout balloon) kept for comparison |
| `logo/holygrawlix-icon-app.svg` | Icon on a dark rounded square (app / social avatar) |
| `icons/` | Favicons (32, 48), Apple touch icon (180), 192 / 512 app icons |

`dark` = for dark backgrounds (cream letters); `light` = for light backgrounds (black letters).
Spacing between HOLY, the burst and GAMES is set optically (the slanted Y overhangs its letter box). Letters are outlined from the Bangers font, so the SVGs need no font installed. Rebuild with
`python3 brand/build_logos.py path/to/bangers.woff2 brand/logo` (needs `fonttools` and `brotli`).

Colors: black `#0B0B10`, cream `#F4F1EA`, yellow `#FFD23F`, red accent `#FF4D4D`.

## Archive
`archive/grawlix-figma-v1/` holds the earlier "Grawlix Games" page from the first Figma round.
