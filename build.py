"""Parse the Vatican source HTML for Magnifica Humanitas and emit a Tufte-style index.html.

Output features:
- Numbered citation sidenotes (right margin) that preserve the source [N].
- Editorial annotations (right margin, light blue, lettered) for uncited references.
- Left-rail collapsible/sticky TOC, location tracker, dark mode (handled in CSS/JS).
"""

from __future__ import annotations

import hashlib
import json
import math
import re
import string
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString, Tag

ROOT = Path(__file__).parent
SOURCE = ROOT / "source.html"
DIST = ROOT / "magnifica"          # all shipped assets go here — served at read.clarebir.ch/magnifica/
OUT = DIST / "index.html"
ATTENTION_OUT = DIST / "attention.json"

SOURCE_URL = "https://www.vatican.va/content/leo-xiv/en/encyclicals/documents/20260515-magnifica-humanitas.html"


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


def load() -> BeautifulSoup:
    return BeautifulSoup(SOURCE.read_text(encoding="utf-8"), "lxml")


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
    notes: dict[int, str] = {}
    for p in content.find_all("p", class_="MsoFootnoteText"):
        anchor = p.find("a", attrs={"name": re.compile(r"^_ftn\d+$")})
        if not anchor:
            continue
        num = int(anchor["name"].removeprefix("_ftn"))
        anchor.decompose()
        html = p.decode_contents().strip()
        html = html.lstrip("\xa0 ").lstrip("&nbsp;").lstrip()
        notes[num] = html
    return notes


# ---------------------------------------------------------------------------
# Classification
# ---------------------------------------------------------------------------

PARA_NUM_RE = re.compile(r"^\s*(\d+)\.\s+")


def classify(p: Tag) -> tuple[str, dict]:
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
    italic_inside_bold = bool(bold and bold.find("i"))

    if has_anchor and bold:
        if is_centered:
            return "h1", {"text": t, "anchor": first_anchor_name(p)}
        if italic_inside_bold:
            return "h3", {"text": t, "anchor": first_anchor_name(p)}
        return "h2", {"text": t, "anchor": first_anchor_name(p)}

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

    # Convert footnote-reference anchors into Tufte sidenote markup.
    # Marker carries the *real* footnote number as text (no CSS counters).
    for a in p2.find_all("a", attrs={"name": re.compile(r"^_ftnref\d+$")}):
        n = int(a["name"].removeprefix("_ftnref"))
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
            new = re.sub(r"^\s*\d+\.\s+", "", s, count=1)
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

    # Build markup
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


def load_annotations() -> list[tuple[int, str, int, str]]:
    """Returns list of (paragraph_number, after_text, occurrence, note_html) in document order."""
    try:
        from annotations import ANNOTATIONS  # type: ignore
    except ImportError:
        return []
    items: list[tuple[int, str, int, str]] = []
    for entry in ANNOTATIONS:
        p_num = entry["p"]
        after = entry["after"]
        occ = entry.get("occurrence", 1)
        note = entry["note"]
        items.append((p_num, after, occ, note))
    return items


# ---------------------------------------------------------------------------
# Word wrapping (for token-attention overlay)
# ---------------------------------------------------------------------------
# Every body word becomes <span class="w" data-w="N">word</span>. The data-w
# index is the word's position within the paragraph (matches the tokenizer's
# word grouping), so JS can look up attention[paragraph_id][N].

_W_EXCLUDE_CLASSES = ("sidenote", "sidenote-marker", "annotation-marker", "paranum", "w")


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
            span = helper.new_tag("span", **{"class": "w", "data-w": str(w_i)})
            span.append(NavigableString(s[ws:we]))
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
ATTN_CACHE = ROOT / ".token_attention.npz"


def compute_token_attention(paragraph_texts: list[str],
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
    if ATTN_CACHE.exists():
        try:
            d = np.load(ATTN_CACHE, allow_pickle=True)
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
    for pi, ptext in enumerate(paragraph_texts):
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

        # Top-K per word. Output shape is compact: each word entry is just
        # [[target_word_idx, weight], ...] — the frontend looks up by data-w
        # so we don't ship character offsets.
        para_entries: list[list] = []
        spans: list[tuple[int, int]] = []
        kk = min(top_k, n_words - 1)
        for i, g in enumerate(word_groups):
            row = word_attn[i]
            spans.append((g["start"], g["end"]))
            if kk <= 0:
                para_entries.append([])
                continue
            top_idx = np.argpartition(-row, kk)[:kk]
            top_idx = top_idx[np.argsort(-row[top_idx])]
            para_entries.append([[int(j), round(float(row[j]), 4)] for j in top_idx])

        attention_per_para.append(para_entries)
        word_spans_per_para.append(spans)

    print(f"  caching token attention ...")
    np.savez(
        ATTN_CACHE,
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
        note_html = notes.get(n, f"[missing footnote {n}]")
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

def build() -> None:
    soup = load()
    content = find_content_div(soup)
    notes = extract_footnotes(content)
    annotations = load_annotations()

    # Index annotations by paragraph for fast lookup, preserving order.
    ann_by_p: dict[int, list[tuple[str, int, str]]] = {}
    ann_order: dict[tuple[int, str, int], int] = {}
    for idx, (p_num, after, occ, note) in enumerate(annotations):
        ann_by_p.setdefault(p_num, []).append((after, occ, note))
        ann_order[(p_num, after, occ)] = idx

    # First pass — transform paragraphs, insert annotations, capture raw text
    # (which is what the tokenizer will see and what word offsets index into).
    items: list[tuple[str, dict]] = []
    para_p_tags: list[Tag] = []
    paragraph_texts: list[str] = []
    paragraph_numbers: list[int] = []
    for p in content.find_all("p", recursive=False):
        kind, info = classify(p)
        if kind == "skip" or kind == "toc":
            continue
        if kind == "paragraph":
            p_tag = transform_paragraph(p, info["number"])
            for (after, occ, note) in ann_by_p.get(info["number"], []):
                ann_idx = ann_order[(info["number"], after, occ)]
                ok = insert_annotation(p_tag, after, occ, note, ann_idx)
                if not ok:
                    print(f"  warning: annotation not anchored in p{info['number']}: {after!r}")
            info["p_tag"] = p_tag
            para_p_tags.append(p_tag)
            paragraph_texts.append(paragraph_raw_text(p_tag))
            paragraph_numbers.append(info["number"])
        items.append((kind, info))

    # Compute real transformer attention per paragraph.
    attn_data, word_spans = compute_token_attention(paragraph_texts)

    # Wrap every word in the body with data-w. Then serialize the html.
    for p_tag, spans in zip(para_p_tags, word_spans):
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
            for num, entries in zip(paragraph_numbers, attn_data)
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
    toc_html = "<ol class=\"toc-list\">" + "".join(toc_items) + "</ol>"

    DIST.mkdir(exist_ok=True)
    attention_json = json.dumps(attention_payload, ensure_ascii=False, separators=(",", ":"))
    ATTENTION_OUT.write_text(attention_json, encoding="utf-8")
    page = PAGE_TEMPLATE.format(
        body=body_html_filled,
        toc=toc_html,
        source_url=SOURCE_URL,
    )
    OUT.write_text(page, encoding="utf-8")
    n_ann = sum(1 for _ in annotations)
    n_words = sum(len(spans) for spans in word_spans)
    print(f"Wrote {OUT} ({len(page):,} bytes) — {len(notes)} citations, "
          f"{n_ann} annotations, {n_words} word tokens across "
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
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Magnifica Humanitas &mdash; Pope Leo XIV</title>
<link rel="stylesheet" href="style.css">
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
      <p class="eyebrow">Encyclical letter</p>
      <h1><em>Magnifica Humanitas</em></h1>
      <p class="addressee">Of His Holiness Pope Leo XIV</p>
      <p class="subtitle">On safeguarding the human person in the time of artificial intelligence</p>
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

<script src="app.js" defer></script>
</body>
</html>
"""


if __name__ == "__main__":
    build()
