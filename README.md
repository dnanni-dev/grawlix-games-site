# Holy Grawlix Games: site

Source for [holygrawlix.com](https://holygrawlix.com). The current `index.html` is the temporary "in development" page and the aesthetic direction for the main site (Bangers display type, comic burst, black / cream / yellow).

## Brand (`brand/`)

| File | Use |
|---|---|
| `logo/holygrawlix-horizontal-{dark,light}.svg/.png` | Rectangular lockup, one line: HOLY [#$@!] GAMES |
| `logo/holygrawlix-stacked-{dark,light}.svg/.png` | Square lockup, three rows: HOLY / [#$@!] / GAMES |
| `logo/holygrawlix-icon.svg` | Icon-only mark: grawlix burst (#$ over @!), transparent |
| `logo/holygrawlix-icon-app.svg` | Icon on a dark rounded square (app / social avatar) |
| `icons/` | Favicons (32, 48), Apple touch icon (180), 192 / 512 app icons |

`dark` = for dark backgrounds (cream letters); `light` = for light backgrounds (black letters).
Letters are outlined from the Bangers font, so the SVGs need no font installed. Rebuild with
`python3 brand/build_logos.py path/to/bangers.woff2 brand/logo` (needs `fonttools` and `brotli`).

Colors: black `#0B0B10`, cream `#F4F1EA`, yellow `#FFD23F`, red accent `#FF4D4D`.

## Archive
`archive/grawlix-figma-v1/` holds the earlier "Grawlix Games" page from the first Figma round.
