// ── Dark mode toggle ────────────────────────────────────────────────────────
const DARK_KEY = "phk-about-dark";
const toggle = document.getElementById("dark-toggle");
const toggleIcon = document.getElementById("dark-icon");

function applyDark(on) {
  document.body.classList.toggle("dark", on);
  toggleIcon.textContent = on ? "☀️" : "🌙";
  localStorage.setItem(DARK_KEY, on ? "1" : "0");
}

// Init from storage or system preference
const stored = localStorage.getItem(DARK_KEY);
if (stored !== null) {
  applyDark(stored === "1");
} else {
  applyDark(window.matchMedia("(prefers-color-scheme: dark)").matches);
}

toggle.addEventListener("click", () => {
  applyDark(!document.body.classList.contains("dark"));
});

// ── Mobile nav ──────────────────────────────────────────────────────────────
const hamburger = document.getElementById("hamburger");
const mobileNav = document.getElementById("mobile-nav");

hamburger.addEventListener("click", () => {
  mobileNav.classList.toggle("hidden");
});

mobileNav.querySelectorAll("a").forEach(a => {
  a.addEventListener("click", () => mobileNav.classList.add("hidden"));
});

// ── Org / cert logos — Google favicon with initials fallback ────────────────
function renderInitials(el, name, color) {
  el.style.background = color;
  el.style.padding = "";
  const parts = name.trim().split(/\s+/);
  el.textContent = parts.length >= 2
    ? parts.slice(0, 2).map(w => w[0]).join("")
    : name.slice(0, 3);
}

document.querySelectorAll(".tl-org-logo, .cert-logo").forEach(el => {
  const domain = el.dataset.domain;
  const name   = el.dataset.name  || "?";
  const color  = el.dataset.color || "#0025ff";

  if (domain) {
    const img = document.createElement("img");
    img.src = `https://www.google.com/s2/favicons?domain=${domain}&sz=64`;
    img.alt = name;
    img.style.cssText = "width:100%;height:100%;object-fit:contain;";
    img.onerror = () => {
      el.removeChild(img);
      renderInitials(el, name, color);
    };
    el.style.background = "#fff";
    el.style.padding = "4px";
    el.appendChild(img);
  } else {
    renderInitials(el, name, color);
  }
});

// ── Clean URL parameters (remove tracking params) ──────────────────────────
if (window.location.search) {
  const url = new URL(window.location.href);
  const paramsToRemove = ['_gl', '_ga', '_ga_TT1ELNHWXP'];
  let hasTracking = false;

  paramsToRemove.forEach(param => {
    if (url.searchParams.has(param)) {
      hasTracking = true;
    }
  });

  // Remove all tracking parameters
  if (hasTracking) {
    const cleanUrl = url.origin + url.pathname + url.hash;
    window.history.replaceState({}, document.title, cleanUrl);
  }
}

// ── Active nav on scroll ────────────────────────────────────────────────────
const sections = document.querySelectorAll("section[id]");
const navLinks = document.querySelectorAll(".main-nav a, .mobile-nav a");

const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      navLinks.forEach(a => {
        const href = a.getAttribute("href");
        if (href && href.startsWith("#")) {
          a.style.color = href === "#" + entry.target.id ? "var(--pri)" : "";
        }
      });
    }
  });
}, { threshold: 0.3 });

sections.forEach(s => observer.observe(s));
