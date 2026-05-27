"""Parse the Vatican source HTML for Magnifica Humanitas and emit a Tufte-style index.html.

Output features:
- Numbered citation sidenotes (right margin) that preserve the source [N].
- Editorial annotations (right margin, light blue, lettered) for uncited references.
- Left-rail collapsible/sticky TOC, location tracker, dark mode (handled in CSS/JS).
"""

from __future__ import annotations

import hashlib
import importlib
import json
import math
import re
import string
import unicodedata
import urllib.error
import urllib.request
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString, Tag

ROOT = Path(__file__).parent
SOURCE = ROOT / "source.html"     # cached English source (also the build's golden copy)
SOURCES_DIR = ROOT / "sources"    # cached per-language source HTML fetched from the Vatican
DIST = ROOT / "magnifica"          # all shipped assets go here — served at read.clarebir.ch/magnifica/
ASSET_BASE = "/magnifica"          # absolute asset root so sub-language pages resolve css/js

# Official languages Magnifica Humanitas was published in. English is the
# canonical build (annotations + masthead are authored against it); the others
# are produced by swapping the /en/ segment of SOURCE_URL.
LANGUAGES = ["en", "it", "fr", "es", "pt", "de", "pl", "ar"]

# Native names shown in the switcher, and which scripts read right-to-left.
LANG_NAMES = {
    "en": "English",
    "it": "Italiano",
    "fr": "Français",
    "es": "Español",
    "pt": "Português",
    "de": "Deutsch",
    "pl": "Polski",
    "ar": "العربية",
}
RTL_LANGS = {"ar"}

SOURCE_URL = "https://www.vatican.va/content/leo-xiv/en/encyclicals/documents/20260515-magnifica-humanitas.html"

# Canonical English masthead. Other languages derive theirs from the source's
# own <meta description> so we never ship a guessed translation.
EN_MASTHEAD = {
    "eyebrow": "Encyclical letter",
    "addressee": "Of His Holiness Pope Leo XIV",
    "subtitle": "On safeguarding the human person in the time of artificial intelligence",
}

# The eyebrow ("Encyclical Letter") is normally derived from the meta-description
# (the text before the Latin title). Arabic uniquely places its localized title
# *before* "MAGNIFICA HUMANITAS", which would leak the title into the eyebrow, so
# we pin the genre instead.
EYEBROW_OVERRIDE = {
    "ar": "رسالة بابويّة عامّة",
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def text_of(node: Tag) -> str:
    return node.get_text(" ", strip=True).replace("\xa0", " ")


def _paragraph_plain_text(p_tag: Tag) -> str:
    """Plain text of a paragraph excluding sidenote bodies (citations/annotations)
    and marker labels. Used as the input to sentence embeddings so the model
    sees only Leo's prose, not our editorial layer."""
    parts: list[str] = []
    for ns in p_tag.descendants:
        if not isinstance(ns, NavigableString):
            continue
        skip = False
        for parent in ns.parents:
            cls = getattr(parent, "get", lambda *_: None)("class", None)
            if cls and any(c in cls for c in ("sidenote", "sidenote-marker", "annotation-marker", "paranum")):
                skip = True
                break
        if skip:
            continue
        parts.append(str(ns))
    return " ".join("".join(parts).split()).replace("\xa0", " ")


def source_url_for(lang: str) -> str:
    """Swap the /en/ language segment of SOURCE_URL for another language code."""
    return SOURCE_URL.replace("/en/", f"/{lang}/")


def fetch_source(lang: str) -> str | None:
    """Return the source HTML for ``lang``, fetching from the Vatican once and
    caching under ``sources/``. English prefers the checked-in ``source.html``.
    Returns None if the language page can't be retrieved."""
    if lang == "en" and SOURCE.exists():
        return SOURCE.read_text(encoding="utf-8")

    cache = SOURCES_DIR / f"{lang}.html"
    if cache.exists():
        return cache.read_text(encoding="utf-8")

    url = source_url_for(lang)
    req = urllib.request.Request(url, headers={"User-Agent": "magnifica-build/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            html = resp.read().decode("utf-8", "replace")
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
        print(f"  warning: could not fetch {lang} source ({exc}) — skipping")
        return None
    SOURCES_DIR.mkdir(exist_ok=True)
    cache.write_text(html, encoding="utf-8")
    print(f"  fetched {lang} source ({len(html):,} bytes) -> {cache.relative_to(ROOT)}")
    return html


def _clean_meta(desc: str) -> str:
    """Trim the Vatican boilerplate ("[ Multimedia ]" and rule lines) from a
    meta-description tail."""
    desc = desc.split("[")[0]                 # drop "[ Multimedia ] ..."
    desc = re.sub(r"_{3,}", "", desc)         # drop the long underscore rules
    return " ".join(desc.split()).strip(" .·")


def extract_masthead(soup: BeautifulSoup, lang: str) -> dict:
    """Localized masthead strings. For English we use the curated copy; for
    other languages we split the source's own meta-description on the Latin
    title "MAGNIFICA HUMANITAS" — text before it is the localized "Encyclical
    Letter" eyebrow, text after it is the addressee + subtitle line."""
    if lang == "en":
        return dict(EN_MASTHEAD)

    md = soup.find("meta", attrs={"name": "description"})
    desc = (md.get("content") if md else "") or ""
    parts = re.split(r"MAGNIFICA\s+HUMANITAS", desc, maxsplit=1, flags=re.IGNORECASE)
    eyebrow = EYEBROW_OVERRIDE.get(lang) or _sentence_case(_clean_meta(parts[0]) if parts else "")
    subtitle = _sentence_case(_clean_meta(parts[1]) if len(parts) > 1 else "")
    return {"eyebrow": eyebrow, "addressee": "", "subtitle": subtitle}


# Strict Roman-numeral matcher. The naive ``[ivxlcdm]+`` matched ordinary words
# made only of those letters ("im", "civil", "mid") and shouted them; this only
# accepts well-formed numerals (and is applied to the punctuation-stripped core,
# so "XIV." is still recognized).
_ROMAN_RE = re.compile(r"^m{0,4}(cm|cd|d?c{0,3})(xc|xl|l?x{0,3})(ix|iv|v?i{0,3})$")


def _sentence_case(s: str) -> str:
    """Lower-case an ALL-CAPS meta string into sentence case, but keep genuine
    Roman numerals (e.g. the pope's "XIV") upper-cased, even with trailing
    punctuation."""
    if not s:
        return ""
    words = []
    for w in s.lower().split():
        core = w.strip(".,;:()[]")
        if core and _ROMAN_RE.fullmatch(core):
            words.append(w.replace(core, core.upper(), 1))
        else:
            words.append(w)
    out = " ".join(words)
    return out[0].upper() + out[1:] if out else out


def find_content_div(soup: BeautifulSoup) -> Tag:
    candidates = soup.select("div.vaticanrichtext")
    return max(candidates, key=lambda d: len(d.get_text()))


def first_anchor_name(p: Tag) -> str | None:
    a = p.find("a", attrs={"name": True})
    return a["name"] if a else None


# ---------------------------------------------------------------------------
# Footnotes
# ---------------------------------------------------------------------------

def extract_footnotes(content: Tag) -> dict[int, str]:
    """Pull footnote definitions out of the document.

    The Vatican's per-language exports disagree on markup: English wraps each
    definition in <p class="MsoFootnoteText"> (nested below the body), while
    other languages emit plain <p class="MsoNormal"> definitions sitting as
    direct children of the content div. Both anchor the definition with
    <a name="_ftnN">, so we key off that and then remove the whole paragraph —
    otherwise the non-English definitions would re-appear as stray body text."""
    notes: dict[int, str] = {}
    for anchor in content.find_all("a", attrs={"name": re.compile(r"^_ftn\d+$")}):
        p = anchor.find_parent("p")
        if p is None:
            continue
        num = int(anchor["name"].removeprefix("_ftn"))
        anchor.decompose()
        html = p.decode_contents().strip()
        html = html.lstrip("\xa0 ").lstrip("&nbsp;").lstrip()
        notes[num] = html
        p.decompose()
    return notes


# ---------------------------------------------------------------------------
# Classification
# ---------------------------------------------------------------------------

# Trailing whitespace is optional: some translated exports glue the number to
# the text ("68.O princípio…"), and requiring a space silently dropped those
# paragraphs (misread as TOC rows or headings).
PARA_NUM_RE = re.compile(r"^\s*(\d+)\.\s*")


def _anchor_slug(text: str) -> str:
    """A stable ascii id for headings whose source markup has no <a name>
    anchor (e.g. the Arabic export). Hash-based so it survives non-Latin text."""
    return "h-" + hashlib.md5(text.encode("utf-8")).hexdigest()[:10]


def slugify_heading(text: str) -> str:
    """A clean, URL-safe id derived from a heading's text. The Vatican source
    bookmarks are unreliable (truncated to a single word like "Una", or
    containing spaces), so we ignore them for ids and build our own. Falls back
    to a content hash for scripts that don't reduce to ASCII (e.g. Arabic)."""
    ascii_text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_text).strip("-").lower()
    return slug if len(slug) >= 2 else _anchor_slug(text)


def extract_toc_levels(content: Tag) -> dict[str, str]:
    """Read the document's own table of contents (the index near the top) to
    learn each heading's level. In the Vatican TOC, a subsection entry's link is
    wholly wrapped in <i> while a section entry's is not. Returns
    ``{anchor_name: 'sub' | 'sec'}`` keyed by the link target (so it can be
    matched against each heading's <a name>). Most exports include this index
    (en/fr/es/de/pt/pl); a few (it/ar) omit it, yielding ``{}`` — those fall back
    to the markup heuristic in :func:`classify`."""
    levels: dict[str, str] = {}
    for a in content.find_all("a", href=re.compile(r"^#")):
        href = a["href"]
        if href.startswith("#_ftn"):           # footnote ref/back-link, not a TOC entry
            continue
        anchor = href[1:]
        if not anchor:
            continue
        txt = a.get_text(" ", strip=True)
        if not txt or re.match(r"^\[?\d+\]?$", txt):   # bare-number links aren't TOC entries
            continue
        level = "sub" if a.find_parent("i") is not None else "sec"
        levels.setdefault(anchor, level)
    return levels


def classify(p: Tag, toc_levels: dict[str, str] | None = None) -> tuple[str, dict]:
    classes = p.get("class") or []
    if "MsoFootnoteText" in classes:
        return "skip", {}

    t = text_of(p)
    if not t or t == " ":
        return "skip", {}

    style = (p.get("style") or "").lower()
    is_centered = "text-align: center" in style
    inner_links = p.find_all("a", href=True)
    if inner_links and all(a["href"].startswith("#") for a in inner_links) and not PARA_NUM_RE.match(t):
        return "toc", {"html": p.decode_contents()}

    m = PARA_NUM_RE.match(t)
    if m:
        return "paragraph", {"number": int(m.group(1))}

    has_anchor = bool(p.find("a", attrs={"name": True}))
    bold = p.find(["b", "strong"])
    # A subsection heading is *wholly* italic (<b><i>full title</i></b>); a
    # section heading may merely contain an italicized term — a Latin phrase
    # ("res novae"), a work's title ("Magnificat") — without being a subsection.
    # So compare how much of the bold text is italicized rather than testing for
    # any italic at all. The 0.7 threshold tolerates a non-italic drop-cap letter
    # (e.g. "R" + <i>esponsibility…</i>).
    italic_inside_bold = False
    if bold:
        bold_text = bold.get_text(" ", strip=True)
        italic_len = sum(len(i.get_text(" ", strip=True)) for i in bold.find_all("i"))
        italic_inside_bold = bool(bold_text) and italic_len >= 0.7 * len(bold_text)

    if has_anchor or bold:
        # A heading. The Vatican's per-language exports disagree on markup:
        #   - English bolds AND anchors every heading;
        #   - Italian/French/... anchor without bolding;
        #   - Arabic bolds without an anchor.
        # Centering always marks a chapter line. For the section/subsection
        # split we prefer the document's own table of contents (authoritative,
        # works in every language that ships one); only when that index is
        # absent (it/ar) or doesn't list this anchor do we fall back to the
        # bold+italic markup cue. The id comes from the heading text (the source
        # bookmarks are unreliable); the raw bookmark is only used for the lookup.
        raw_anchor = first_anchor_name(p)
        anchor = slugify_heading(t)
        if is_centered:
            return "h1", {"text": t, "anchor": anchor}
        level = (toc_levels or {}).get(raw_anchor)
        if level == "sub":
            return "h3", {"text": t, "anchor": anchor}
        if level == "sec":
            return "h2", {"text": t, "anchor": anchor}
        if has_anchor and italic_inside_bold:
            return "h3", {"text": t, "anchor": anchor}
        return "h2", {"text": t, "anchor": anchor}

    if t in {"___________________________"}:
        return "skip", {}
    return "other", {"html": p.decode_contents(), "text": t}


# ---------------------------------------------------------------------------
# Paragraph transformation
# ---------------------------------------------------------------------------

def transform_paragraph(p: Tag, number: int) -> Tag:
    """Return a fresh <p> Tag with cleaned, marker-enriched contents."""
    holder = BeautifulSoup(str(p), "lxml")
    p2 = holder.p

    # Convert in-text footnote references into Tufte sidenote markup. Every
    # language marks them as <a href="#_ftnN"> (the name="_ftnref" attribute is
    # only present in some exports), so we key off the href for consistency.
    # Marker carries the *real* footnote number as text (no CSS counters).
    for a in p2.find_all("a", href=re.compile(r"^#_ftn\d+$")):
        n = int(a["href"].removeprefix("#_ftn"))
        marker = holder.new_tag("label", **{
            "for": f"sn-{n}",
            "class": "margin-toggle sidenote-marker",
            "data-n": str(n),
        })
        marker.append(NavigableString(str(n)))
        cb = holder.new_tag("input", type="checkbox", id=f"sn-{n}",
                            **{"class": "margin-toggle"})
        span = holder.new_tag("span", **{
            "class": "sidenote citation",
            "data-footnote": str(n),
        })
        # Order in DOM: marker, checkbox, sidenote
        a.insert_after(span)
        a.insert_after(cb)
        a.insert_after(marker)
        a.decompose()

    # Drop leading "N. " from first text node.
    for child in p2.descendants:
        if isinstance(child, NavigableString):
            s = str(child)
            new = re.sub(r"^\s*\d+\.\s*", "", s, count=1)
            if new != s:
                child.replace_with(new)
                break

    # External links open in a new tab.
    for a in p2.find_all("a", href=True):
        href = a["href"]
        if href.startswith("http"):
            a["target"] = "_blank"
            a["rel"] = "noopener noreferrer"

    # Remove stray <br clear=...>
    for br in p2.find_all("br"):
        if br.get("clear"):
            br.decompose()

    return p2  # caller will use decode_contents()


# ---------------------------------------------------------------------------
# Editorial annotations
# ---------------------------------------------------------------------------

def letter_label(i: int) -> str:
    """0 -> a, 25 -> z, 26 -> aa, 27 -> ab, ..."""
    s = ""
    n = i
    while True:
        s = string.ascii_lowercase[n % 26] + s
        n = n // 26 - 1
        if n < 0:
            break
    return s


_EXCLUDE_CLASSES = ("sidenote", "sidenote-marker", "annotation-marker")


def _is_excluded(ns) -> bool:
    for p in ns.parents:
        cls = getattr(p, "get", lambda *_: None)("class", None)
        if not cls:
            continue
        if any(c in cls for c in _EXCLUDE_CLASSES):
            return True
    return False


def _normalize(s: str) -> str:
    return s.replace("\xa0", " ").replace("–", "-").replace("—", "-")


def _make_annotation_nodes(ann_idx: int, note_html: str) -> tuple[Tag, Tag, Tag]:
    """Build the (marker label, hidden checkbox, sidenote span) trio for one
    editorial annotation, with the lettered label and the note body filled in."""
    helper = BeautifulSoup("", "lxml")
    label = letter_label(ann_idx)
    ann_id = f"ann-{label}"
    marker = helper.new_tag("label", **{
        "for": ann_id,
        "class": "margin-toggle annotation-marker",
        "data-label": label,
    })
    marker.append(NavigableString(label))
    cb = helper.new_tag("input", type="checkbox", id=ann_id,
                        **{"class": "margin-toggle"})
    span = helper.new_tag("span", **{
        "class": "sidenote annotation",
        "data-label": label,
    })
    inner = BeautifulSoup(note_html, "lxml")
    body = inner.body
    if body:
        for child in list(body.children):
            span.append(child)
    else:
        span.append(NavigableString(note_html))
    return marker, cb, span


def append_annotation(p_tag: Tag, note_html: str, ann_idx: int) -> None:
    """Fallback placement: pin the annotation to the end of the paragraph.

    Used when an `after` anchor can't be matched in a translated paragraph — the
    note still appears (marker at the end of the prose) instead of being dropped."""
    marker, cb, span = _make_annotation_nodes(ann_idx, note_html)
    p_tag.append(marker)
    p_tag.append(cb)
    p_tag.append(span)


def insert_annotation(p_tag: Tag,
                      after: str, occurrence: int,
                      note_html: str, ann_idx: int) -> bool:
    """Find the Nth occurrence of `after` in the paragraph text; insert marker + sidenote.

    If the match ends within an <a> link, place the marker *after* the link so the
    marker stays outside the clickable area.
    """
    target = _normalize(after.lower())

    nodes = [n for n in p_tag.descendants
             if isinstance(n, NavigableString) and not _is_excluded(n)]
    flat = ""
    ranges: list[tuple[int, int, NavigableString]] = []
    for n in nodes:
        s = _normalize(str(n))
        ranges.append((len(flat), len(flat) + len(s), n))
        flat += s
    flat_lower = flat.lower()

    seen = 0
    pos = 0
    end_pos = -1
    while True:
        idx = flat_lower.find(target, pos)
        if idx < 0:
            return False
        seen += 1
        if seen == occurrence:
            end_pos = idx + len(target)
            break
        pos = idx + 1

    target_node = None
    offset_in_node = 0
    for start, stop, n in ranges:
        if start < end_pos <= stop:
            target_node = n
            offset_in_node = end_pos - start
            break
    if target_node is None:
        return False

    marker, cb, span = _make_annotation_nodes(ann_idx, note_html)

    s = str(target_node)
    # Walk up to detect an <a> ancestor (within this paragraph)
    link_ancestor = None
    walker = target_node.parent
    while walker is not None and walker is not p_tag:
        if getattr(walker, "name", None) == "a":
            link_ancestor = walker
            break
        walker = walker.parent

    if link_ancestor is not None and offset_in_node == len(s):
        # Hop out of the link entirely
        link_ancestor.insert_after(span)
        link_ancestor.insert_after(cb)
        link_ancestor.insert_after(marker)
    else:
        before = s[:offset_in_node]
        rest = s[offset_in_node:]
        parent = target_node.parent
        children = list(parent.children)
        idx_in_parent = children.index(target_node)
        target_node.extract()
        for i, item in enumerate([
            NavigableString(before), marker, cb, span, NavigableString(rest),
        ]):
            parent.insert(idx_in_parent + i, item)

    return True


def load_annotations(lang: str = "en") -> list[tuple[int, str, int, str]]:
    """Editorial annotations for a language, as (paragraph, after, occurrence,
    note_html) in document order, from ``annotations/<lang>.py``. Returns [] if
    that module is absent."""
    try:
        mod = importlib.import_module(f"annotations.{lang}")
    except ImportError:
        return []
    entries = getattr(mod, "ANNOTATIONS", None)
    if not entries:
        return []
    items: list[tuple[int, str, int, str]] = []
    for entry in entries:
        items.append((entry["p"], entry["after"], entry.get("occurrence", 1), entry["note"]))
    return items


# ---------------------------------------------------------------------------
# Word wrapping (for token-attention overlay)
# ---------------------------------------------------------------------------
# Most body words become <span class="w" data-w="N">word</span>. The data-w
# index is the word's position within the paragraph (matches the tokenizer's
# word grouping), so JS can look up attention[paragraph_id][N]. To keep the
# DOM lean we skip wrapping stop-words; their attention is also stripped at
# build time so hover never tries to point at an unwrapped position.

_W_EXCLUDE_CLASSES = ("sidenote", "sidenote-marker", "annotation-marker", "paranum", "w")

# Function words we don't bother wrapping. ~120 of the most common English
# stop-words plus a few that show up specifically in this corpus. Roughly
# 30–40% of tokens in normal prose, so dropping them halves the DOM.
_STOPWORDS = set("""
a about above after again against all also although am among an and another any are
aren as at back be because been before being below between beyond both but by came
can cannot could day did do does doing done down due during each either else even
ever every except few for from further get gets getting give given gives go goes
going gone got had has have having he her here hers herself him himself his how
however i if in indeed instead into is isn it its itself just keep kept last let
like little long made make makes making many may me might more most much must my
myself never nevertheless no nor not now of off often on once one only onto or
other others ought our ours ourselves out over own per perhaps put quite rather
really said same see seen seems shall she should since so some something soon still
such sure take taken than that the their theirs them themselves then there these
they this those though through thus to too toward towards under until up upon us
use used uses using usually very via was way we well went were what when where
whether which while who whom whose why will with within without would yes yet you
your yours yourself yourselves
""".lower().split())


def _is_stopword(text: str) -> bool:
    # Strip trailing punctuation, lowercase, check membership. Matches forms
    # like "the,", "And,", "is.", "(of"
    s = text.lower().strip(".,;:!?()[]{}\"'“”‘’—–-")
    return s in _STOPWORDS


def _is_w_excluded(ns) -> bool:
    for p in ns.parents:
        cls = getattr(p, "get", lambda *_: None)("class", None)
        if cls and any(c in cls for c in _W_EXCLUDE_CLASSES):
            return True
    return False


def paragraph_raw_text(p_tag: Tag) -> str:
    """Concatenate the visible prose text nodes of a paragraph, *exactly* as
    they will be presented to the tokenizer. Important: no normalization, so
    character offsets returned by the tokenizer align with text-node content
    used later to wrap words."""
    parts: list[str] = []
    for ns in p_tag.descendants:
        if isinstance(ns, NavigableString) and not _is_w_excluded(ns):
            parts.append(str(ns))
    return "".join(parts)


def wrap_words_in_paragraph(p_tag: Tag, word_spans: list[tuple[int, int]]) -> None:
    """Wrap each (start, end) word span (offsets into ``paragraph_raw_text``)
    with ``<span class="w" data-w="N">word</span>``. Walks text nodes outside
    sidenote/marker contexts. Assumes a word lies entirely within one text node
    (true for the encyclical: inline <i>/<a> wrap whole phrases, not partial
    words)."""
    if not word_spans:
        return
    helper = BeautifulSoup("", "lxml")

    # Build a flat-offset map of the text nodes we'll modify.
    text_nodes: list[tuple[int, int, NavigableString]] = []
    flat_pos = 0
    for ns in list(p_tag.descendants):
        if not isinstance(ns, NavigableString):
            continue
        if _is_w_excluded(ns):
            continue
        s = str(ns)
        text_nodes.append((flat_pos, flat_pos + len(s), ns))
        flat_pos += len(s)

    # Pair each word with the text node that contains it (by start offset).
    # If a word's end falls in a later node (i.e., word straddles inline
    # markup like <i>…</i> mid-word — rare), we still wrap the first portion
    # so its index never goes missing from the DOM (otherwise attention
    # targets pointing at it would find no span).
    word_iter = iter(enumerate(word_spans))
    word_idx, word = next(word_iter, (None, None))

    for n_start, n_end, ns in text_nodes:
        if word is None:
            break
        local_words = []
        while word is not None and word[0] >= n_start and word[0] < n_end:
            # Clip the word's end to this node's boundary.
            we_clipped = min(word[1], n_end)
            local_words.append((word_idx, word[0], we_clipped))
            word_idx, word = next(word_iter, (None, None))
        if not local_words:
            continue

        s = str(ns)
        new_nodes = []
        cursor = 0  # local cursor in s
        for w_i, ws_abs, we_abs in local_words:
            ws = ws_abs - n_start
            we = we_abs - n_start
            if cursor < ws:
                new_nodes.append(NavigableString(s[cursor:ws]))
            word_text = s[ws:we]
            if _is_stopword(word_text):
                # Skip wrapping — emit the bare text. The word still occupies
                # its data-w index in the attention array, but there's no DOM
                # span to highlight, and the attention computation has already
                # zeroed it out as a target.
                new_nodes.append(NavigableString(word_text))
            else:
                span = helper.new_tag("span", **{"class": "w", "data-w": str(w_i)})
                span.append(NavigableString(word_text))
                new_nodes.append(span)
            cursor = we
        if cursor < len(s):
            new_nodes.append(NavigableString(s[cursor:]))

        parent = ns.parent
        children = list(parent.children)
        idx = children.index(ns)
        ns.extract()
        for offset, item in enumerate(new_nodes):
            parent.insert(idx + offset, item)


def compute_attention(paragraph_concepts: list[set[str]],
                      k: int = 8,
                      min_score: float = 0.12,
                      min_cooc: int = 2) -> dict[str, list[list]]:
    """Cosine similarity over binary paragraph occurrence vectors. Returns
    {concept_id: [[neighbor_id, score], ...]} with top-K neighbors per concept.

    Co-occurrence variant — kept as a fallback / comparison. The default
    pipeline now uses :func:`compute_attention_via_embeddings`.

    ``min_cooc`` is the minimum number of paragraphs in which two concepts must
    *both* appear. Without this, rare auto-concepts generate spurious 1.0
    cosines on the strength of a single shared paragraph.
    """
    counts: dict[str, int] = {}
    cooc: dict[tuple[str, str], int] = {}
    for cs in paragraph_concepts:
        ordered = sorted(cs)
        for c in ordered:
            counts[c] = counts.get(c, 0) + 1
        for i, a in enumerate(ordered):
            for b in ordered[i + 1:]:
                cooc[(a, b)] = cooc.get((a, b), 0) + 1
                cooc[(b, a)] = cooc[(a, b)]

    neighbors: dict[str, list[list]] = {}
    for c in counts:
        scores = []
        for c2 in counts:
            if c2 == c:
                continue
            cc = cooc.get((c, c2), 0)
            if cc < min_cooc:
                continue
            denom = math.sqrt(counts[c] * counts[c2])
            score = cc / denom
            if score >= min_score:
                scores.append((c2, score))
        scores.sort(key=lambda x: -x[1])
        if scores:
            neighbors[c] = [[n, round(s, 3)] for n, s in scores[:k]]
    return neighbors


# ---------------------------------------------------------------------------
# Transformer-embedding attention
# ---------------------------------------------------------------------------

EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"   # 6 layers, 12 heads, 384-dim


def compute_token_attention(paragraph_texts: list[str],
                             cache_path: Path,
                             top_k: int = 8) -> tuple[list[list[list]], list[list[tuple[int, int]]]]:
    """Real transformer attention, per paragraph.

    For each paragraph:
      1. Tokenize with the model's WordPiece tokenizer (offset-aware).
      2. Forward pass with ``output_attentions=True`` — every layer returns its
         per-head attention matrix.
      3. **Attention rollout** across layers: A_l ← 0.5·A_l + 0.5·I (account
         for residual connections), then multiply A_L · A_{L-1} · … · A_1. This
         is the standard way to express "how much does the output position
         for token X actually depend on token Y, all layers compounded."
      4. Aggregate subword tokens back to words via the tokenizer's offset
         map: word-to-word attention = mean over its subword block.
      5. For each word, store its top-K attended words within this paragraph.

    Returns:
      attention: list[paragraph_idx] -> list[word_entry], each entry being
                 {"s": char_start, "e": char_end, "attn": [[target_w, weight],...]}
      word_spans: list[paragraph_idx] -> list of (char_start, char_end)
                 (same data, just convenient for the HTML wrapper)
    """
    import numpy as np
    import torch

    # Cache invalidation key
    text_hash = hashlib.sha256("\n\n".join(paragraph_texts).encode("utf-8")).hexdigest()
    if cache_path.exists():
        try:
            d = np.load(cache_path, allow_pickle=True)
            if str(d["hash"]) == text_hash:
                print(f"  loaded cached token attention for {len(paragraph_texts)} paragraphs")
                return d["attention"].tolist(), d["word_spans"].tolist()
        except Exception:
            pass

    print(f"  loading {EMBED_MODEL} for token-attention extraction ...")
    from sentence_transformers import SentenceTransformer
    from transformers import AutoModel
    model = SentenceTransformer(EMBED_MODEL, device="cpu")
    # The default SDPA attention implementation discards attention weights.
    # Load the backbone with eager attention so output_attentions=True works.
    backbone = AutoModel.from_pretrained(EMBED_MODEL, attn_implementation="eager")
    backbone.to("cpu")
    tokenizer = model.tokenizer
    backbone.eval()

    attention_per_para: list[list[dict]] = []
    word_spans_per_para: list[list[tuple[int, int]]] = []

    print(f"  running forward pass on {len(paragraph_texts)} paragraphs ...")
    for ptext in paragraph_texts:
        enc = tokenizer(
            ptext,
            return_offsets_mapping=True,
            return_tensors="pt",
            truncation=True,
            max_length=512,
            add_special_tokens=True,
        )
        offsets = enc.pop("offset_mapping")[0].tolist()
        with torch.no_grad():
            out = backbone(**enc, output_attentions=True, output_hidden_states=False)

        # out.attentions: tuple of (1, num_heads, seq, seq) per layer.
        # Use the LAST layer's attention averaged across heads — sharper and
        # more directly interpretable than rollout (rollout dilutes weights
        # by multiplying through every layer).
        last_layer = out.attentions[-1][0]                 # (heads, seq, seq)
        attn_t = last_layer.mean(dim=0)                    # (seq, seq)

        # Mask special tokens ([CLS], [SEP], [PAD]) so they don't dominate
        # the top-K. BERT routinely puts ~30% of its attention on [CLS].
        special_cols = [i for i, (s, e) in enumerate(offsets) if s == 0 and e == 0]
        if special_cols:
            attn_t[:, special_cols] = 0.0
            row_sums = attn_t.sum(dim=-1, keepdim=True).clamp(min=1e-9)
            attn_t = attn_t / row_sums
        attn = attn_t.numpy()

        # Group subwords back into whole-word groups, using offsets.
        word_groups: list[dict] = []
        cur = None
        for ti, (s, e) in enumerate(offsets):
            if s == 0 and e == 0:        # special token (CLS / SEP / PAD)
                continue
            if cur is None or s != cur["end"]:
                if cur is not None:
                    word_groups.append(cur)
                cur = {"tokens": [ti], "start": s, "end": e}
            else:                         # contiguous subword
                cur["tokens"].append(ti)
                cur["end"] = e
        if cur is not None:
            word_groups.append(cur)

        n_words = len(word_groups)
        if n_words == 0:
            attention_per_para.append([])
            word_spans_per_para.append([])
            continue

        # Word×word attention by averaging the corresponding sub-blocks.
        # Build via numpy indexing for speed.
        word_attn = np.zeros((n_words, n_words), dtype="float32")
        token_groups = [g["tokens"] for g in word_groups]
        for i, ti in enumerate(token_groups):
            block = attn[ti]                  # (|ti|, seq)
            for j, tj in enumerate(token_groups):
                if i == j:
                    continue
                word_attn[i, j] = block[:, tj].mean()

        # Mark which words are stop-words (by text content). Their attention
        # entries will be emptied (you can't hover them) and they'll be
        # excluded from being *neighbors* of other words.
        word_texts = [ptext[g["start"]:g["end"]] for g in word_groups]
        is_stop = [_is_stopword(t) for t in word_texts]

        # Mask stop-word columns so they never win the top-K as targets.
        if any(is_stop):
            stop_cols = [i for i, s in enumerate(is_stop) if s]
            word_attn[:, stop_cols] = 0.0

        # Top-K per word. Output shape is compact: each word entry is just
        # [[target_word_idx, weight], ...] — the frontend looks up by data-w
        # so we don't ship character offsets.
        para_entries: list[list] = []
        spans: list[tuple[int, int]] = []
        kk = min(top_k, n_words - 1)
        for i, g in enumerate(word_groups):
            spans.append((g["start"], g["end"]))
            if is_stop[i] or kk <= 0:
                # Stop-words don't get hover behavior — empty entry.
                para_entries.append([])
                continue
            row = word_attn[i]
            top_idx = np.argpartition(-row, kk)[:kk]
            top_idx = top_idx[np.argsort(-row[top_idx])]
            # Drop any target whose weight is 0 (i.e., stop-word target).
            para_entries.append([
                [int(j), round(float(row[j]), 4)]
                for j in top_idx if row[j] > 0
            ])

        attention_per_para.append(para_entries)
        word_spans_per_para.append(spans)

    print("  caching token attention ...")
    np.savez(
        cache_path,
        hash=text_hash,
        attention=np.array(attention_per_para, dtype=object),
        word_spans=np.array(word_spans_per_para, dtype=object),
    )
    return attention_per_para, word_spans_per_para


# ---------------------------------------------------------------------------
# Sidenote filling
# ---------------------------------------------------------------------------

def fill_citation_sidenotes(soup: BeautifulSoup, notes: dict[int, str]) -> None:
    for span in soup.find_all("span", attrs={"class": re.compile(r"\bcitation\b")}):
        n = int(span["data-footnote"])
        note_html = notes.get(n)
        if note_html is None:
            # The source provides no definition for this footnote (happens in a
            # couple of translations, e.g. Polish 33/219). Drop the orphan
            # marker, its toggle checkbox and the empty sidenote rather than
            # shipping a "[missing footnote N]" placeholder.
            cb = span.find_previous_sibling("input", id=f"sn-{n}")
            marker = span.find_previous_sibling("label", attrs={"for": f"sn-{n}"})
            if cb:
                cb.decompose()
            if marker:
                marker.decompose()
            span.decompose()
            continue
        inner = BeautifulSoup(note_html, "lxml")
        body = inner.body
        if body:
            for child in list(body.children):
                span.append(child)
        else:
            span.append(NavigableString(note_html))
        # External links inside notes
        for a in span.find_all("a", href=True):
            if a["href"].startswith("http"):
                a["target"] = "_blank"
                a["rel"] = "noopener noreferrer"
        # Prepend the citation number as a styled label
        label_tag = soup.new_tag("span", **{"class": "sn-label"})
        label_tag.append(NavigableString(str(n)))
        span.insert(0, label_tag)


# ---------------------------------------------------------------------------
# Build pipeline
# ---------------------------------------------------------------------------

def render_lang_switch(current: str, available: list[str]) -> str:
    """A native <details> dropdown for the toc-head control row. Lists every
    built language; the summary shows the current language's 2-letter code."""
    items: list[str] = []
    for code in LANGUAGES:
        if code not in available:
            continue
        href = f"{ASSET_BASE}/" if code == "en" else f"{ASSET_BASE}/{code}/"
        active = " active" if code == current else ""
        aria = ' aria-current="true"' if code == current else ""
        name = LANG_NAMES.get(code, code)
        items.append(
            f'<li><a class="lang-opt{active}" href="{href}" hreflang="{code}" '
            f'lang="{code}"{aria}>{name}</a></li>'
        )
    cur_name = LANG_NAMES.get(current, current)
    return (
        '<details class="lang-switch">'
        f'<summary class="ctl-toggle lang-summary" title="Change language" '
        f'aria-label="Change language (currently {cur_name})">'
        f'<span class="lang-code">{current.upper()}</span></summary>'
        f'<ul class="lang-menu">{"".join(items)}</ul>'
        '</details>'
    )


def build(lang: str, source_html: str, available_langs: list[str]) -> None:
    is_en = lang == "en"
    soup = BeautifulSoup(source_html, "lxml")
    content = find_content_div(soup)
    notes = extract_footnotes(content)
    # The document's own index gives authoritative section/subsection levels.
    toc_levels = extract_toc_levels(content)
    # Editorial annotations per language (annotations.py / annotations_<lang>.py).
    # Letter labels follow document order, so the index is shared across all
    # paragraphs; an anchor that can't be matched falls back to end-of-paragraph.
    annotations = load_annotations(lang)
    n_fallback = 0

    # Index annotations by paragraph for fast lookup. Each entry carries its own
    # document-order index (the source of its letter label) so two annotations
    # that happen to share (paragraph, after, occurrence) can't collide onto the
    # same label.
    ann_by_p: dict[int, list[tuple[str, int, str, int]]] = {}
    for idx, (p_num, after, occ, note) in enumerate(annotations):
        ann_by_p.setdefault(p_num, []).append((after, occ, note, idx))

    # First pass — transform paragraphs, insert annotations, capture raw text
    # (which is what the tokenizer will see and what word offsets index into).
    items: list[tuple[str, dict]] = []
    para_p_tags: list[Tag] = []
    paragraph_texts: list[str] = []
    paragraph_numbers: list[int] = []
    for p in content.find_all("p", recursive=False):
        kind, info = classify(p, toc_levels)
        if kind == "skip" or kind == "toc":
            continue
        if kind == "paragraph":
            p_tag = transform_paragraph(p, info["number"])
            for (after, occ, note, ann_idx) in ann_by_p.get(info["number"], []):
                ok = insert_annotation(p_tag, after, occ, note, ann_idx)
                if not ok:
                    # Anchor not found (common in translations) — pin to the
                    # paragraph end so the note still shows.
                    append_annotation(p_tag, note, ann_idx)
                    n_fallback += 1
            info["p_tag"] = p_tag
            para_p_tags.append(p_tag)
            paragraph_texts.append(paragraph_raw_text(p_tag))
            paragraph_numbers.append(info["number"])
        items.append((kind, info))

    # Compute real transformer attention per paragraph (cached per language).
    attn_cache = ROOT / (".token_attention.npz" if is_en
                         else f".token_attention.{lang}.npz")
    attn_data, word_spans = compute_token_attention(paragraph_texts, attn_cache)

    # Wrap every word in the body with data-w. Then serialize the html.
    for p_tag, spans in zip(para_p_tags, word_spans, strict=True):
        wrap_words_in_paragraph(p_tag, spans)

    for kind, info in items:
        if kind == "paragraph":
            info["html"] = info["p_tag"].decode_contents()
            del info["p_tag"]

    # Attention payload: { "pN": [ {s,e,attn:[[target_idx, weight]...]} ... ] }
    attention_payload = {
        "version": 2,
        "paragraphs": {
            f"p{num}": entries
            for num, entries in zip(paragraph_numbers, attn_data, strict=True)
        },
    }

    # Merge consecutive h1 items: the encyclical splits chapter headings into two
    # centered-bold paragraphs ("CHAPTER ONE" + "A DYNAMIC APPROACH FAITHFUL TO THE GOSPEL").
    # We combine them into a single chapter heading with an eyebrow + title.
    merged: list[tuple[str, dict]] = []
    i = 0
    while i < len(items):
        kind, info = items[i]
        if kind == "h1":
            group = [(kind, info)]
            j = i + 1
            while j < len(items) and items[j][0] == "h1":
                group.append(items[j])
                j += 1
            if len(group) >= 2:
                # First is the "CHAPTER N" label, rest joined as title.
                label = group[0][1]["text"]
                title_parts = [g[1]["text"].rstrip(".") for g in group[1:]]
                anchor = group[0][1]["anchor"] or group[1][1].get("anchor")
                joined_title = ". ".join(title_parts)
                merged.append(("h1", {
                    "label": label,
                    "title": joined_title,
                    "anchor": anchor,
                    "text": label + " — " + joined_title,
                }))
            else:
                info["label"] = ""
                info["title"] = info["text"]
                merged.append((kind, info))
            i = j
            continue
        merged.append((kind, info))
        i += 1
    items = merged

    # Ensure heading ids are unique (text-derived slugs can collide, e.g. two
    # "The principle of …" subsections). Suffix duplicates -2, -3, … The body id
    # and the TOC href both read info["anchor"], so they stay in sync.
    seen_anchors: dict[str, int] = {}
    for kind, info in items:
        if kind in ("h1", "h2", "h3") and info.get("anchor"):
            base = info["anchor"]
            if base in seen_anchors:
                seen_anchors[base] += 1
                info["anchor"] = f"{base}-{seen_anchors[base]}"
            else:
                seen_anchors[base] = 1

    # Compose body HTML
    chapter_idx = 0
    body_parts: list[str] = []
    for kind, info in items:
        if kind == "h1":
            chapter_idx += 1
            title = info.get("title") or info.get("text")
            label = info.get("label") or ""
            label_html = f'<span class="chapter-label">{label}</span>' if label else ""
            body_parts.append(
                f'<h2 class="chapter" id="{info["anchor"]}" data-chapter="{chapter_idx}" '
                f'data-chapter-title="{title}">{label_html}<span class="chapter-title">{title}</span></h2>'
            )
        elif kind == "h2":
            body_parts.append(
                f'<h3 class="section" id="{info["anchor"]}" data-section-title="{info["text"]}">'
                f'{info["text"]}</h3>'
            )
        elif kind == "h3":
            body_parts.append(
                f'<h4 class="subsection" id="{info["anchor"]}">{info["text"]}</h4>'
            )
        elif kind == "paragraph":
            body_parts.append(
                f'<p class="para" id="p{info["number"]}">'
                f'<a class="paranum" href="#p{info["number"]}" '
                f'title="Copy link to paragraph {info["number"]}" '
                f'aria-label="Copy link to paragraph {info["number"]}">'
                f'{info["number"]}</a>'
                f'{info["html"]}</p>'
            )
        elif kind == "other":
            body_parts.append(f'<p class="other">{info["html"]}</p>')

    body_html = "\n".join(body_parts)

    # Fill citation sidenote bodies in one pass
    out_soup = BeautifulSoup(body_html, "lxml")
    fill_citation_sidenotes(out_soup, notes)
    body_html_filled = "".join(str(c) for c in out_soup.body.children) if out_soup.body else body_html

    # Build TOC
    toc_items: list[str] = []
    ch = 0
    for kind, info in items:
        if kind == "h1":
            ch += 1
            title = info.get("title") or info.get("text")
            toc_items.append(
                f'<li class="toc-chapter" data-chapter="{ch}">'
                f'<a href="#{info["anchor"]}"><span class="toc-roman">{roman(ch)}</span>'
                f'<span class="toc-title">{title.title() if title.isupper() else title}</span></a></li>'
            )
        elif kind == "h2":
            toc_items.append(
                f'<li class="toc-section"><a href="#{info["anchor"]}">{info["text"]}</a></li>'
            )
        elif kind == "h3":
            toc_items.append(
                f'<li class="toc-subsection"><a href="#{info["anchor"]}">{info["text"]}</a></li>'
            )
    toc_html = "<ol class=\"toc-list\">" + "".join(toc_items) + "</ol>"

    # Localized masthead + chrome.
    mh = extract_masthead(soup, lang)
    addressee_block = (
        f'<p class="addressee">{mh["addressee"]}</p>' if mh.get("addressee") else ""
    )
    if is_en:
        doc_title = "Magnifica Humanitas — Pope Leo XIV"
    else:
        doc_title = soup.title.get_text(strip=True) if soup.title else "Magnifica Humanitas"
    lang_switch = render_lang_switch(lang, available_langs)
    dir_attr = ' dir="rtl"' if lang in RTL_LANGS else ""

    out_dir = DIST if is_en else DIST / lang
    out_dir.mkdir(parents=True, exist_ok=True)
    attention_out = out_dir / "attention.json"
    out_html = out_dir / "index.html"

    attention_json = json.dumps(attention_payload, ensure_ascii=False, separators=(",", ":"))
    attention_out.write_text(attention_json, encoding="utf-8")
    page = PAGE_TEMPLATE.format(
        body=body_html_filled,
        toc=toc_html,
        source_url=source_url_for(lang),
        lang=lang,
        dir_attr=dir_attr,
        asset_base=ASSET_BASE,
        doc_title=doc_title,
        lang_switch=lang_switch,
        eyebrow=mh["eyebrow"],
        addressee_block=addressee_block,
        subtitle=mh["subtitle"],
    )
    out_html.write_text(page, encoding="utf-8")
    n_ann = sum(1 for _ in annotations)
    n_words = sum(len(spans) for spans in word_spans)
    ann_note = f"{n_ann} annotations" + (f" ({n_fallback} pinned to paragraph)" if n_fallback else "")
    print(f"Wrote {out_html} ({len(page):,} bytes) — {len(notes)} citations, "
          f"{ann_note}, {n_words} word tokens across "
          f"{len(paragraph_texts)} paragraphs")


def roman(n: int) -> str:
    vals = [(10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    out = ""
    for v, s in vals:
        while n >= v:
            out += s
            n -= v
    return out


def toc_title(raw: str, chapter_idx: int) -> str:
    """Encyclical TOC titles are like 'CHAPTER ONE' alone; show the running head."""
    # We pass the actual h1 text. For chapter pages where it just says "CHAPTER ONE",
    # we'll keep that. The next h1 (the subtitle line) merges via runtime later; for now
    # use raw text but title-case.
    return raw.title() if raw.isupper() else raw


PAGE_TEMPLATE = """<!doctype html>
<html lang="{lang}"{dir_attr}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{doc_title}</title>
<link rel="icon" type="image/png" href="/logo.png">
<link rel="stylesheet" href="{asset_base}/style.css">
<script>
  // Set UI state before paint to avoid flash. Light unless opted in.
  (function () {{
    var saved = localStorage.getItem('theme');
    document.documentElement.dataset.theme = saved === 'dark' ? 'dark' : 'light';
    var tocSaved = localStorage.getItem('toc');
    if (tocSaved === 'collapsed') document.documentElement.dataset.toc = 'collapsed';
    if (localStorage.getItem('attention') === 'on') document.documentElement.dataset.attention = 'on';
  }})();
</script>
</head>
<body>

<aside class="toc-rail" aria-label="Table of contents">
  <div class="toc-head">
    <button id="toc-toggle" class="ctl-toggle toc-toggle" type="button"
            aria-expanded="true" aria-controls="toc-body"
            title="Toggle contents" aria-label="Toggle contents">
      <svg class="ico" viewBox="0 0 16 16" aria-hidden="true" fill="none"
           stroke="currentColor" stroke-width="1.5" stroke-linecap="round">
        <line x1="3" y1="5" x2="13" y2="5"/>
        <line x1="3" y1="8" x2="13" y2="8"/>
        <line x1="3" y1="11" x2="13" y2="11"/>
      </svg>
    </button>
    <button id="attention-toggle" class="ctl-toggle attention-toggle" type="button"
            title="Toggle attention overlay" aria-label="Toggle attention overlay" aria-pressed="false">
      <svg class="ico attn-icon attn-icon-off" viewBox="0 0 16 16" aria-hidden="true"
           fill="none" stroke="currentColor" stroke-width="1.3"
           stroke-linecap="round" stroke-linejoin="round">
        <!-- closed eye: a calm downward eyelid curve -->
        <path d="M 2 7.2 Q 8 11.6 14 7.2"/>
      </svg>
      <svg class="ico attn-icon attn-icon-on" viewBox="0 0 16 16" aria-hidden="true"
           fill="none" stroke="currentColor" stroke-width="1.3"
           stroke-linecap="round" stroke-linejoin="round">
        <!-- open eye: cubic almond, opened wide, with a roomy iris -->
        <path d="M 1.5 8 C 4 1.6, 12 1.6, 14.5 8 C 12 14.4, 4 14.4, 1.5 8 Z"/>
        <circle cx="8" cy="8" r="2.6"/>
      </svg>
    </button>
    <button id="theme-toggle" class="ctl-toggle theme-toggle" type="button"
            title="Toggle dark mode" aria-label="Toggle dark mode">
      <span class="theme-icon theme-icon-light" aria-hidden="true">&#9728;</span>
      <span class="theme-icon theme-icon-dark" aria-hidden="true">&#9789;</span>
    </button>
    {lang_switch}
    <a class="ctl-toggle comments-link"
       href="https://docs.google.com/document/d/1MV_TvmP-8DUv7_OAcz8XzIOkq5g2-ai8Lv7Aen9ashw/edit?usp=sharing"
       target="_blank" rel="noopener noreferrer"
       title="Add a comment (Google Doc)" aria-label="Open comments doc in new tab">
      <span class="comments-icon" aria-hidden="true">&#9998;</span>
    </a>
  </div>
  <nav id="toc-body" class="toc">
    <a class="toc-top" href="#top">Magnifica Humanitas</a>
    {toc}
  </nav>
</aside>

<aside class="para-rail" aria-label="Paragraph navigator">
  <ol id="para-rail-list" class="para-rail-list" aria-hidden="false"></ol>
</aside>


<main class="page">
  <article>
    <header class="masthead" id="top">
      <p class="eyebrow">{eyebrow}</p>
      <h1><em>Magnifica Humanitas</em></h1>
      {addressee_block}
      <p class="subtitle">{subtitle}</p>
      <p class="source">
        Given in Rome &middot; 15 May 2026
        &nbsp;&middot;&nbsp;
        <a href="{source_url}" target="_blank" rel="noopener noreferrer">Vatican source &rarr;</a>
        &nbsp;&middot;&nbsp;
        &copy; Libreria Editrice Vaticana
      </p>
    </header>

    <section class="body">
      {body}
    </section>
  </article>
</main>

<script src="{asset_base}/app.js" defer></script>
</body>
</html>
"""


def build_all() -> None:
    # Fetch every language up front so the switcher only lists what we can build.
    sources: dict[str, str] = {}
    for lang in LANGUAGES:
        html = fetch_source(lang)
        if html:
            sources[lang] = html
    available = [lang for lang in LANGUAGES if lang in sources]
    if "en" not in available:
        raise SystemExit("English source unavailable — cannot build.")
    print(f"Building {len(available)} language(s): {', '.join(available)}")
    for lang in available:
        print(f"\n== {lang} ==")
        build(lang, sources[lang], available)


if __name__ == "__main__":
    build_all()
