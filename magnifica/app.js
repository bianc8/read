// Magnifica Humanitas — small interactive bits.
// 1. Theme toggle (light/dark, persisted)
// 2. TOC collapse/expand (persisted)
// 3. Scroll-spy location tracker on chapters + sections
// 4. TOC active-link highlighting tied to the spy
// 5. Attention overlay (concept-attention on hover)

(function () {
  const root = document.documentElement;

  // ---- theme ----
  // Suppress CSS transitions for one paint during a deliberate theme flip so
  // colors swap atomically instead of staggering across elements (which used
  // to feel like a flicker).
  const themeBtn = document.getElementById("theme-toggle");
  themeBtn.addEventListener("click", () => {
    const next = root.dataset.theme === "dark" ? "light" : "dark";
    root.classList.add("theme-flipping");
    root.dataset.theme = next;
    localStorage.setItem("theme", next);
    // Two rAFs so the no-transition style applies, the colors paint, then
    // we restore normal transitions on the next frame.
    requestAnimationFrame(() => {
      requestAnimationFrame(() => {
        root.classList.remove("theme-flipping");
      });
    });
  });

  // ---- attention overlay ----
  const attnBtn = document.getElementById("attention-toggle");

  // Adjacency data is fetched lazily on first toggle-on; readers who never
  // turn on attention never pay the cost.
  let ATTENTION = null;     // null = not loaded, {} = loading, {neighbors,labels} = ready
  let attentionPromise = null;

  function loadAttention() {
    if (attentionPromise) return attentionPromise;
    // `cache: "no-cache"` so we always revalidate — important during dev
    // since the JSON shape has changed. Once stable we can re-enable
    // long-term caching via a hashed filename.
    attentionPromise = fetch("attention.json", { cache: "no-cache" })
      .then((r) => r.json())
      .then((data) => { ATTENTION = data; })
      .catch((err) => { console.warn("attention.json load failed", err); ATTENTION = { paragraphs: {} }; });
    return attentionPromise;
  }

  // Initial state from localStorage.
  const attnSaved = localStorage.getItem("attention");
  if (attnSaved === "on") {
    root.dataset.attention = "on";
    attnBtn.setAttribute("aria-pressed", "true");
    loadAttention();   // user had it on before — start fetching immediately
  }

  attnBtn.addEventListener("click", () => {
    const on = root.dataset.attention === "on";
    if (on) {
      delete root.dataset.attention;
      attnBtn.setAttribute("aria-pressed", "false");
      localStorage.setItem("attention", "off");
      clearAttention();
    } else {
      root.dataset.attention = "on";
      attnBtn.setAttribute("aria-pressed", "true");
      localStorage.setItem("attention", "on");
      loadAttention();
    }
  });

  // --- token attention hover ----
  // Each body word is <span class="w" data-w="N"> inside <p class="para" id="pX">.
  // On hover: read pid + word index, look up ATTENTION.paragraphs[pid][word_idx],
  // highlight the target words in the SAME paragraph with rank-based intensity.
  let activeKey = null;  // "pid:wordIdx" of the currently focused word

  function clearAttention() {
    document.querySelectorAll(
      ".w.attn-focus, .w.attn-strong, .w.attn-medium, .w.attn-weak"
    ).forEach((t) => {
      t.classList.remove("attn-focus", "attn-strong", "attn-medium", "attn-weak");
    });
    activeKey = null;
  }

  function applyAttention(para, wordIdx) {
    clearAttention();
    const focusEl = para.querySelector(`.w[data-w="${wordIdx}"]`);
    if (focusEl) focusEl.classList.add("attn-focus");

    if (!ATTENTION || !ATTENTION.paragraphs) {
      activeKey = `${para.id}:${wordIdx}`;
      return;
    }
    const entries = ATTENTION.paragraphs[para.id];
    if (!entries) { activeKey = `${para.id}:${wordIdx}`; return; }
    const top = entries[wordIdx];
    if (!top) { activeKey = `${para.id}:${wordIdx}`; return; }

    // Rank-based tiers: top 2 strong, next 3 medium, rest weak.
    top.forEach(([tgtIdx, weight], rank) => {
      const tgtEl = para.querySelector(`.w[data-w="${tgtIdx}"]`);
      if (!tgtEl || tgtEl.classList.contains("attn-focus")) return;
      const cls = rank < 2 ? "attn-strong"
                : rank < 5 ? "attn-medium"
                :           "attn-weak";
      tgtEl.classList.add(cls);
    });
    activeKey = `${para.id}:${wordIdx}`;
  }

  document.addEventListener("mouseover", (e) => {
    if (root.dataset.attention !== "on") return;
    const w = e.target.closest(".w");
    if (!w) return;
    const para = w.closest("p.para");
    if (!para) return;
    const key = `${para.id}:${w.dataset.w}`;
    if (key === activeKey) return;
    applyAttention(para, parseInt(w.dataset.w, 10));
  });

  document.addEventListener("mouseout", (e) => {
    if (root.dataset.attention !== "on") return;
    const w = e.target.closest(".w");
    if (!w) return;
    const to = e.relatedTarget && e.relatedTarget.closest && e.relatedTarget.closest(".w");
    if (to) {
      const toPara = to.closest("p.para");
      if (toPara && `${toPara.id}:${to.dataset.w}` === activeKey) return;
    }
    clearAttention();
  });

  // ---- toc ----
  const tocBtn = document.getElementById("toc-toggle");
  function setTocState(state) {
    // 'collapsed' | 'expanded' (desktop default = expanded, mobile default = collapsed)
    root.dataset.toc = state;
    localStorage.setItem("toc", state);
    tocBtn.setAttribute("aria-expanded", state === "expanded" ? "true" : "false");
  }
  // Initialize from saved or media-query.
  const saved = localStorage.getItem("toc");
  const isNarrow = window.matchMedia("(max-width: 1024px)").matches;
  setTocState(saved || (isNarrow ? "collapsed" : "expanded"));

  tocBtn.addEventListener("click", () => {
    const cur = root.dataset.toc === "collapsed" ? "collapsed" : "expanded";
    setTocState(cur === "collapsed" ? "expanded" : "collapsed");
  });

  // ---- paragraph rail + scroll spy ----
  const paraRailList = document.getElementById("para-rail-list");
  const tocItems = document.querySelectorAll(".toc-chapter, .toc-section");
  const paragraphs = Array.from(document.querySelectorAll("p.para"));
  const chapters = Array.from(document.querySelectorAll("h2.chapter"));
  const sections = Array.from(document.querySelectorAll("h3.section"));

  // Map each paragraph id to its chapter index, so we can mark chapter starts.
  // A paragraph is a "chapter start" if it's the first .para after a .chapter heading.
  // We also remember the chapter ordinal so the rail can show Roman numerals there.
  const chapterStartIds = new Set();
  const chapterRomanByPid = new Map();
  function toRoman(n) {
    const m = [[10,"X"],[9,"IX"],[5,"V"],[4,"IV"],[1,"I"]];
    let out = "";
    for (const [v, s] of m) { while (n >= v) { out += s; n -= v; } }
    return out;
  }
  {
    const allBodyChildren = Array.from(document.querySelectorAll(".body > *"));
    let pendingChapter = false;
    let chapterIdx = 0;
    for (const el of allBodyChildren) {
      if (el.matches("h2.chapter")) {
        pendingChapter = true;
        chapterIdx++;
      } else if (pendingChapter && el.matches("p.para")) {
        chapterStartIds.add(el.id);
        chapterRomanByPid.set(el.id, toRoman(chapterIdx));
        pendingChapter = false;
      }
    }
  }

  // Build the rail: one <li><a> per paragraph.
  const railItems = paragraphs.map((p) => {
    const n = p.id.replace(/^p/, "");
    const num = parseInt(n, 10);
    const li = document.createElement("li");
    li.dataset.pid = p.id;
    li.dataset.num = String(num);
    const isChapterStart = chapterStartIds.has(p.id);
    if (isChapterStart) li.classList.add("chapter-start");
    // Show labels at every 25 + the first/last (chapter starts are always shown via .chapter-start).
    if (num === 1 || num === paragraphs.length || num % 25 === 0) {
      li.classList.add("label");
    }
    const a = document.createElement("a");
    a.href = "#" + p.id;
    a.title = isChapterStart
      ? `Chapter ${chapterRomanByPid.get(p.id)} — paragraph ${num}`
      : `Paragraph ${num}`;
    const span = document.createElement("span");
    span.className = "num";
    // Chapter starts show the Roman numeral instead of the paragraph number.
    span.textContent = isChapterStart ? chapterRomanByPid.get(p.id) : num;
    a.appendChild(span);
    li.appendChild(a);
    return li;
  });
  railItems.forEach((li) => paraRailList.appendChild(li));

  const railByPid = new Map(railItems.map((li) => [li.dataset.pid, li]));

  // Paragraph-number links (in the left margin) copy a deep link instead of
  // navigating. They still update the URL hash so the user can verify visually.
  function flashCopied(el) {
    el.classList.add("copied");
    setTimeout(() => el.classList.remove("copied"), 1400);
  }
  document.querySelectorAll("a.paranum").forEach((a) => {
    a.addEventListener("click", (e) => {
      e.preventDefault();
      const href = a.getAttribute("href");
      const url = window.location.origin + window.location.pathname + href;
      const done = () => { flashCopied(a); history.replaceState(null, "", href); };
      if (navigator.clipboard && window.isSecureContext) {
        navigator.clipboard.writeText(url).then(done, () => {
          // Clipboard rejected — fall back to selecting the text.
          const r = document.createRange();
          r.selectNodeContents(a);
          const sel = window.getSelection();
          sel.removeAllRanges();
          sel.addRange(r);
          done();
        });
      } else {
        // Non-secure context (e.g. http://localhost on some browsers).
        const ta = document.createElement("textarea");
        ta.value = url;
        ta.style.position = "fixed";
        ta.style.opacity = "0";
        document.body.appendChild(ta);
        ta.select();
        try { document.execCommand("copy"); } catch {}
        document.body.removeChild(ta);
        done();
      }
    });
  });

  // Smooth-scroll on rail click (override the anchor jump for a kinder feel).
  paraRailList.addEventListener("click", (e) => {
    const a = e.target.closest("a");
    if (!a) return;
    const href = a.getAttribute("href");
    const target = href && document.querySelector(href);
    if (!target) return;
    e.preventDefault();
    target.scrollIntoView({ behavior: "smooth", block: "start" });
    history.replaceState(null, "", href);
  });

  // TOC active-link highlighting tied to the same scroll position.
  function tocHrefFor(el) { return "#" + el.id; }
  function setActiveToc(href) {
    tocItems.forEach((li) => {
      const a = li.querySelector("a");
      if (!a) return;
      if (a.getAttribute("href") === href) li.classList.add("active");
      else li.classList.remove("active");
    });
  }
  function currentBefore(list, y) {
    let cur = null;
    for (const el of list) {
      const top = el.getBoundingClientRect().top + window.scrollY;
      if (top - 120 <= y) cur = el;
      else break;
    }
    return cur;
  }

  // Track which paragraphs are currently intersecting the viewport. Then we
  // mark exactly ONE rail entry active: the topmost visible paragraph (smallest
  // paragraph number). Highlighting every visible paragraph was too noisy.
  const visiblePids = new Set();
  let activePid = null;

  function updateActive() {
    let bestPid = null;
    let bestNum = Infinity;
    for (const pid of visiblePids) {
      const num = parseInt(pid.slice(1), 10);
      if (num < bestNum) { bestNum = num; bestPid = pid; }
    }
    if (bestPid === activePid) return;
    if (activePid) {
      const prev = railByPid.get(activePid);
      if (prev) prev.classList.remove("active");
    }
    activePid = bestPid;
    if (activePid) {
      const cur = railByPid.get(activePid);
      if (cur) cur.classList.add("active");
    }
    // Sync the TOC highlight to the same scroll position.
    const y = window.scrollY;
    const ch = currentBefore(chapters, y);
    const sec = currentBefore(sections, y);
    const target = sec || ch;
    setActiveToc(target ? tocHrefFor(target) : null);
  }

  const io = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      if (entry.isIntersecting) visiblePids.add(entry.target.id);
      else visiblePids.delete(entry.target.id);
    }
    updateActive();
  }, {
    // No margins — anything with even a sliver on screen counts as visible.
    // We pick the topmost of those, so this is the right notion of "in view".
    rootMargin: "0px",
    threshold: 0,
  });
  paragraphs.forEach((p) => io.observe(p));
})();
