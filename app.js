// ── Org logos (styled initials) ──────────────────────────────────────────────
document.querySelectorAll(".org-logo").forEach(el => {
  const name  = el.dataset.name  || "?";
  const color = el.dataset.color || "#444";
  el.style.background = color;
  // Two lines if name has 2+ words, else up to 3 chars
  const parts = name.trim().split(/\s+/);
  el.textContent = parts.length >= 2
    ? parts.slice(0, 2).map(w => w[0]).join("")
    : name.slice(0, 3);
});

// ── Mobile nav ──────────────────────────────────────────────────────────────
const hamburger = document.getElementById("hamburger");
const navMobile = document.getElementById("nav-mobile");

hamburger.addEventListener("click", () => {
  navMobile.classList.toggle("hidden");
});

navMobile.querySelectorAll("a").forEach(a => {
  a.addEventListener("click", () => navMobile.classList.add("hidden"));
});

// ── Active nav link on scroll ────────────────────────────────────────────────
const sections = document.querySelectorAll("section[id]");
const navLinks = document.querySelectorAll(".nav-links a");

const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      navLinks.forEach(a => {
        a.style.color = a.getAttribute("href") === "#" + entry.target.id
          ? "var(--text)"
          : "";
      });
    }
  });
}, { threshold: 0.35 });

sections.forEach(s => observer.observe(s));

// ── Terminal typewriter ──────────────────────────────────────────────────────
const lines = [
  { type: "prompt", text: "whoami" },
  { type: "out",    text: "pyae-heinn-kyaw" },
  { type: "prompt", text: "cat specialisation.txt" },
  { type: "hi",     text: "Threat Hunting | DFIR | Cloud IR" },
  { type: "prompt", text: "cat rank.txt" },
  { type: "warn",   text: "BTLO Global #1 / THM Top 1%" },
  { type: "prompt", text: "ls certs/" },
  { type: "out",    text: "GSP  GCFA  GCFE  GCIH  GIME  GX-FA  GX-FE" },
  { type: "prompt", text: "cat mitre_contributions.txt" },
  { type: "hi",     text: "T1546.018 — Python Startup Hooks" },
  { type: "prompt", text: "" },
];

const body = document.getElementById("terminal-body");
let lineIdx = 0;
let charIdx = 0;
let phase = "typing"; // typing | newline | pause

function renderTerminal() {
  let html = "";
  for (let i = 0; i < lineIdx; i++) {
    const l = lines[i];
    if (l.type === "prompt") {
      html += `<span class="t-line"><span class="t-prompt">phk@csirt:~$</span> <span class="t-cmd">${esc(l.text)}</span></span>`;
    } else {
      html += `<span class="t-line t-${l.type}">${esc(l.text)}</span>`;
    }
  }

  // Current line being typed
  if (lineIdx < lines.length) {
    const cur = lines[lineIdx];
    const partial = cur.text.slice(0, charIdx);
    if (cur.type === "prompt") {
      html += `<span class="t-line"><span class="t-prompt">phk@csirt:~$</span> <span class="t-cmd">${esc(partial)}</span><span class="t-cursor"></span></span>`;
    } else {
      html += `<span class="t-line t-${cur.type}">${esc(partial)}<span class="t-cursor"></span></span>`;
    }
  } else {
    html += `<span class="t-cursor"></span>`;
  }

  body.innerHTML = html;
  body.scrollTop = body.scrollHeight;
}

function esc(s) {
  return String(s)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

function tick() {
  if (lineIdx >= lines.length) return;

  const cur = lines[lineIdx];

  if (phase === "typing") {
    charIdx++;
    renderTerminal();
    if (charIdx >= cur.text.length) {
      phase = "pause";
      const delay = cur.type === "prompt" ? 400 : 100;
      setTimeout(tick, delay);
      return;
    }
    const speed = cur.type === "prompt" ? 55 : 25;
    setTimeout(tick, speed + Math.random() * 30);
  } else if (phase === "pause") {
    lineIdx++;
    charIdx = 0;
    phase = "typing";
    const gap = lines[lineIdx - 1].type === "out" || lines[lineIdx - 1].type === "hi" || lines[lineIdx - 1].type === "warn"
      ? 200 : 80;
    renderTerminal();
    setTimeout(tick, gap);
  }
}

// Start after short delay
setTimeout(tick, 800);
