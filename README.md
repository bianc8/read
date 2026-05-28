# Magnifica Humanitas - reader edition

A Tufte-style reader for Pope Leo XIV's encyclical *Magnifica Humanitas* (15 May 2026).
`build.py` parses the official Vatican HTML and emits a static site with numbered
citation sidenotes, editorial annotations, a token-attention overlay, a collapsible
table of contents, dark mode, and a **language switcher** across every official
language the encyclical was published in.

Live at <https://read.clarebir.ch/magnifica/>.

## Setup

Dependencies are managed with [uv](https://docs.astral.sh/uv/). Install it first (see the
[official guide](https://docs.astral.sh/uv/getting-started/installation/)):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then sync the project's dependencies:

```bash
uv sync
```

This installs BeautifulSoup + lxml (parsing) and sentence-transformers / transformers /
torch / numpy (the attention overlay).

## Build

```bash
uv run build.py
```

The first run downloads the `all-MiniLM-L6-v2` model and runs a CPU transformer pass
over every paragraph in every language, so it takes a while. Results are cached per
language in `.token_attention.{lang}.npz`; subsequent runs are fast.

## Viewing locally

Serve from the repository root so the reader can fetch `attention.json` and resolve
relative links the same way it will on GitHub Pages:

```bash
uv run python -m http.server 8000
```

Then open:

- <http://localhost:8000/magnifica/> - English
- <http://localhost:8000/magnifica/it/>, `/fr/`, `/es/`, `/pt/`, `/de/`, `/pl/`, `/ar/` - other languages

The in-page language switcher (top of the table-of-contents rail) links between them.
The generated links are relative, so the same files work both on a root domain
(`read.clarebir.ch/magnifica/`) and a GitHub Pages project path
(`bianc8.github.io/read/magnifica/`).

## Languages

The build produces a full, independently-rendered page for each official language. It
derives the per-language source by swapping the `/en/` segment of `SOURCE_URL`:

```
https://www.vatican.va/content/leo-xiv/en/encyclicals/documents/20260515-magnifica-humanitas.html
                                       ^^                     -> /it/, /fr/, /es/, /pt/, /de/, /pl/, /ar/
```

Each language's source HTML is fetched once and cached under `sources/{lang}.html`
(English uses the checked-in `source.html`). Any language that fails to fetch is simply
skipped, and the in-page switcher only lists languages that were actually built.

The localized masthead (the "Encyclical Letter" eyebrow and subtitle) is taken from each
source's own `<meta description>` - split on the Latin title "MAGNIFICA HUMANITAS" - so no
text is machine-translated. Arabic is rendered right-to-left (`dir="rtl"`).

### Output

```
magnifica/
  index.html          # English (canonical)
  attention.json
  style.css           # shared assets, referenced relatively by each page
  app.js
  it/index.html       # one directory per additional language
  it/attention.json
  fr/…  es/…  pt/…  de/…  pl/…  ar/…
```

### Per-language caveats

The Vatican's non-English exports use looser markup than the English one, so the build
normalizes footnotes and headings across them. Notes:

- **Editorial annotations** exist in all eight languages (`annotations/<lang>.py`). English
  is the authored source; the others are translations whose anchors are verified against
  each official text (every anchor matches exactly). A language without its own module
  simply shows no annotations.
- The **table of contents** mirrors each document's own index (chapter › section ›
  subsection). That index is read from the source, where subsection links are italic.
  Italian and Arabic exports omit the index, so their sidebar can't tell sections from
  subsections and lists every heading at section level.
- The attention model is English-trained, so the overlay on non-Latin scripts (Arabic) is
  weaker.

## Editing annotations

Editorial sidenotes live in the `annotations/` package, one module per language
(`annotations/en.py`, `annotations/it.py`, …). Each exposes `ANNOTATIONS`, a list of
`{"p": <paragraph>, "after": <anchor text>, "occurrence": <n>, "note": <html>}` entries.
The `after` snippet is matched against that language's prose; if it can't be matched, the
note is pinned to the end of the paragraph rather than dropped. Rebuild to apply.

## Files

| Path | Purpose |
| --- | --- |
| `build.py` | Parser + static-site generator |
| `annotations/` | Per-language editorial annotation content (`en.py`, `it.py`, …) |
| `source.html` | Cached English Vatican source |
| `sources/` | Cached per-language sources (fetched on first build) |
| `magnifica/` | Generated site (shipped) |
