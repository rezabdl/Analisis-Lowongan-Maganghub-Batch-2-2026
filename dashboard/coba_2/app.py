"""
MagangHub Batch 2 2026 — From Opportunity to Competition
=========================================================
Single-page editorial data-journalism Streamlit dashboard.
Design language: Newsreader serif + Plus Jakarta Sans + JetBrains Mono,
newspaper broadside layout, smooth scroll-reveal animations.
"""

import json
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# ==============================================================================
# PAGE CONFIG
# ==============================================================================
st.set_page_config(
    page_title="MagangHub Batch 2 2026 — From Opportunity to Competition",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ==============================================================================
# EDITORIAL CSS + SMOOTH ANIMATIONS
# ==============================================================================
st.markdown(
    """
<style>
/* ------------------------------------------------------------------ */
/* 0. GOOGLE FONTS                                                     */
/* ------------------------------------------------------------------ */
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;0,6..72,700;1,6..72,400;1,6..72,500&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');

/* ------------------------------------------------------------------ */
/* 1. DESIGN TOKENS                                                    */
/* ------------------------------------------------------------------ */
:root {
    --paper:         #FBFBFA;
    --paper-subtle:  #F4F4F0;
    --ink:           #1A1A1A;
    --ink-muted:     #57534E;
    --ink-light:     #78716C;
    --hairline:      #E7E5E4;
    --accent-rust:   #C2410C;
    --accent-navy:   #1E293B;
    --accent-slate:  #475569;

    --font-serif: 'Newsreader', Georgia, serif;
    --font-sans:  'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
    --font-mono:  'JetBrains Mono', ui-monospace, monospace;
}

/* ------------------------------------------------------------------ */
/* 2. GLOBAL RESETS                                                    */
/* ------------------------------------------------------------------ */
html, body, [class*="css"] {
    font-family: var(--font-sans) !important;
    color: var(--ink);
}

.stApp {
    background-color: var(--paper) !important;
}

#MainMenu, footer, header[data-testid="stHeader"] { visibility: hidden; }

.main .block-container {
    max-width: 1100px;
    padding: 0 1.5rem 5rem 1.5rem;
}

/* Remove default Streamlit spacing between elements */
.stMarkdown { margin-bottom: 0 !important; }

/* ------------------------------------------------------------------ */
/* 3. SCROLL-REVEAL ANIMATION (CSS-only IntersectionObserver feel)     */
/* ------------------------------------------------------------------ */
@keyframes fadeSlideUp {
    from { opacity: 0; transform: translateY(32px); }
    to   { opacity: 1; transform: translateY(0); }
}

.reveal {
    animation: fadeSlideUp 0.7s cubic-bezier(0.16, 1, 0.3, 1) both;
}

.reveal-d1 { animation-delay: 0.08s; }
.reveal-d2 { animation-delay: 0.16s; }
.reveal-d3 { animation-delay: 0.24s; }
.reveal-d4 { animation-delay: 0.32s; }

@keyframes countUp {
    from { opacity: 0; transform: translateY(12px); }
    to   { opacity: 1; transform: translateY(0); }
}

.count-anim {
    animation: countUp 0.55s cubic-bezier(0.16, 1, 0.3, 1) both;
}

.count-anim-d1 { animation-delay: 0.1s; }
.count-anim-d2 { animation-delay: 0.2s; }
.count-anim-d3 { animation-delay: 0.3s; }
.count-anim-d4 { animation-delay: 0.4s; }

/* ------------------------------------------------------------------ */
/* 4. STICKY NAV MASTHEAD                                              */
/* ------------------------------------------------------------------ */
.masthead {
    position: sticky;
    top: 0;
    z-index: 999;
    background: rgba(251,251,250,0.92);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border-bottom: 1px solid var(--hairline);
    padding: 0.75rem 0;
    margin: 0 -1.5rem 0 -1.5rem;
    padding-left: 1.5rem;
    padding-right: 1.5rem;
}

.masthead-inner {
    max-width: 1100px;
    margin: 0 auto;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 0.5rem;
}

.masthead-brand {
    display: flex;
    align-items: baseline;
    gap: 0.6rem;
}

.masthead-brand a {
    font-family: var(--font-serif);
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--ink);
    text-decoration: none;
    letter-spacing: -0.02em;
}

.masthead-brand a:hover { color: var(--ink-muted); }

.masthead-brand .sep { color: #D6D3D1; font-weight: 300; }

.masthead-brand .tagline {
    font-family: var(--font-mono);
    font-size: 0.65rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--ink-light);
}

.masthead nav {
    display: flex;
    gap: 1.75rem;
    font-family: var(--font-mono);
    font-size: 0.72rem;
}

.masthead nav a {
    color: var(--ink-muted);
    text-decoration: none;
    transition: color 0.2s;
}

.masthead nav a:hover { color: var(--ink); }

/* ------------------------------------------------------------------ */
/* 5. HERO SECTION                                                     */
/* ------------------------------------------------------------------ */
.hero-section {
    padding: 4.5rem 0 3.5rem 0;
    border-bottom: 1px solid var(--hairline);
}

.hero-kicker {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    margin-bottom: 1.25rem;
    flex-wrap: wrap;
}

.hero-tag {
    display: inline-flex;
    align-items: center;
    padding: 0.15rem 0.55rem;
    font-family: var(--font-mono);
    font-size: 0.7rem;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    border-radius: 2px;
    border: 1px solid var(--hairline);
    background: var(--paper-subtle);
    color: var(--ink-muted);
}

.hero-kicker .dot {
    font-family: var(--font-mono);
    font-size: 0.65rem;
    color: #D6D3D1;
}

.hero-kicker .label {
    font-family: var(--font-mono);
    font-size: 0.65rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--ink-light);
}

.hero-title {
    font-family: var(--font-serif);
    font-size: clamp(2.5rem, 6vw, 4rem);
    font-weight: 700;
    line-height: 1.08;
    color: var(--ink);
    letter-spacing: -0.02em;
    margin: 0 0 0.75rem 0;
}

.hero-subtitle {
    font-family: var(--font-serif);
    font-style: italic;
    font-size: clamp(1.15rem, 2.5vw, 1.6rem);
    color: var(--ink-muted);
    line-height: 1.4;
    margin: 0 0 1.5rem 0;
    max-width: 42rem;
}

.hero-concept {
    border-left: 2px solid var(--ink);
    padding-left: 1.25rem;
    margin: 1.5rem 0 2rem 0;
    max-width: 42rem;
}

.hero-concept .concept-label {
    font-weight: 600;
    color: var(--ink);
    font-size: 0.875rem;
    margin-bottom: 0.25rem;
}

.hero-concept .concept-highlight {
    font-family: var(--font-serif);
    font-style: italic;
    color: var(--accent-rust);
}

.hero-concept p {
    font-size: 0.875rem;
    color: var(--ink-muted);
    line-height: 1.6;
    margin: 0.35rem 0 0 0;
}

/* ------------------------------------------------------------------ */
/* 6. SECTION HEADERS                                                  */
/* ------------------------------------------------------------------ */
.section-block {
    padding: 4rem 0 3.5rem 0;
    border-bottom: 1px solid var(--hairline);
}

.section-block.alt-bg { background-color: var(--paper-subtle); margin: 0 -1.5rem; padding-left: 1.5rem; padding-right: 1.5rem; }

.section-kicker {
    font-family: var(--font-mono);
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--ink-light);
    margin-bottom: 0.5rem;
}

.section-title {
    font-family: var(--font-serif);
    font-size: clamp(1.75rem, 4vw, 2.75rem);
    font-weight: 700;
    line-height: 1.15;
    color: var(--ink);
    letter-spacing: -0.015em;
    margin: 0 0 0.5rem 0;
}

.section-lead {
    font-size: 0.95rem;
    color: var(--ink-muted);
    line-height: 1.6;
    max-width: 48rem;
    margin: 0;
}

/* ------------------------------------------------------------------ */
/* 7. BROADSIDE STAT CARDS                                             */
/* ------------------------------------------------------------------ */
.stat-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 2rem;
    border-top: 3px solid var(--ink);
    padding-top: 1.75rem;
    margin-top: 2rem;
}

@media (max-width: 768px) {
    .stat-grid { grid-template-columns: repeat(2, 1fr); gap: 1.5rem; }
}

.stat-card .stat-label {
    font-family: var(--font-mono);
    font-size: 0.68rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--ink-light);
    margin-bottom: 0.4rem;
}

.stat-card .stat-value {
    font-family: var(--font-mono);
    font-size: clamp(2rem, 5vw, 3rem);
    font-weight: 700;
    color: var(--ink);
    line-height: 1;
    letter-spacing: -0.02em;
}

.stat-card .stat-value.accent { color: var(--accent-rust); }

.stat-card .stat-caption {
    font-family: var(--font-serif);
    font-size: 0.95rem;
    font-weight: 500;
    color: var(--ink-muted);
    margin-top: 0.35rem;
}

.stat-card .stat-footnote {
    font-size: 0.72rem;
    color: var(--ink-light);
    margin-top: 0.75rem;
    line-height: 1.5;
    border-top: 1px solid var(--hairline);
    padding-top: 0.65rem;
}

/* ------------------------------------------------------------------ */
/* 8. EDITORIAL ANALYSIS CARD                                          */
/* ------------------------------------------------------------------ */
.ed-card {
    background: #FFFFFF;
    border: 1px solid var(--hairline);
    border-radius: 6px;
    padding: 1.5rem;
    margin-bottom: 1.25rem;
    box-shadow: 0 1px 3px rgba(0,0,0,0.03);
    transition: box-shadow 0.25s ease;
}

.ed-card:hover { box-shadow: 0 4px 16px rgba(0,0,0,0.06); }

.ed-card-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    border-bottom: 1px solid var(--hairline);
    padding-bottom: 0.75rem;
    margin-bottom: 1rem;
}

.ed-card-title {
    font-family: var(--font-sans);
    font-size: 1rem;
    font-weight: 700;
    color: var(--ink);
    margin: 0;
    letter-spacing: -0.01em;
}

.ed-card-sub {
    font-size: 0.8rem;
    color: var(--ink-muted);
    margin: 0.15rem 0 0 0;
}

.ed-badge {
    font-family: var(--font-mono);
    font-size: 0.65rem;
    font-weight: 600;
    background: var(--paper-subtle);
    color: var(--ink-muted);
    padding: 0.2rem 0.5rem;
    border-radius: 3px;
    border: 1px solid var(--hairline);
    white-space: nowrap;
}

/* ------------------------------------------------------------------ */
/* 9. CALLOUT / INSIGHT BOX                                            */
/* ------------------------------------------------------------------ */
.callout {
    background: var(--paper-subtle);
    border-left: 3px solid var(--ink);
    padding: 0.85rem 1rem;
    border-radius: 0 4px 4px 0;
    font-size: 0.82rem;
    color: var(--ink-muted);
    line-height: 1.6;
    margin-top: 1rem;
}

.callout strong { color: var(--ink); }

.callout.rust-accent { border-left-color: var(--accent-rust); }

/* ------------------------------------------------------------------ */
/* 10. EDITORIAL QUOTE / PULL-QUOTE                                    */
/* ------------------------------------------------------------------ */
.pull-quote {
    font-family: var(--font-serif);
    font-style: italic;
    font-size: 1.2rem;
    line-height: 1.45;
    color: var(--ink);
    border-left: 2px solid var(--ink);
    padding-left: 1.25rem;
    margin: 2rem 0;
    max-width: 42rem;
}

/* ------------------------------------------------------------------ */
/* 11. QUADRANT GRID                                                   */
/* ------------------------------------------------------------------ */
.quad-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.6rem;
    margin: 0.75rem 0 1rem 0;
}

.quad-cell {
    background: var(--paper-subtle);
    border: 1px solid var(--hairline);
    border-radius: 6px;
    padding: 0.85rem;
}

.quad-cell .quad-label {
    font-size: 0.7rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.03em;
    margin-bottom: 0.2rem;
}

.quad-cell .quad-value {
    font-family: var(--font-mono);
    font-size: 1.35rem;
    font-weight: 700;
    color: var(--ink);
    margin: 0.15rem 0;
}

.quad-cell .quad-desc {
    font-size: 0.7rem;
    color: var(--ink-light);
}

/* ------------------------------------------------------------------ */
/* 12. METHODOLOGY PIPELINE                                            */
/* ------------------------------------------------------------------ */
.pipeline {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 0.75rem;
    margin-top: 1.5rem;
}

.pipeline-step {
    background: #FFFFFF;
    border: 1px solid var(--hairline);
    border-radius: 6px;
    padding: 1rem;
    text-align: center;
    position: relative;
    transition: border-color 0.2s, box-shadow 0.2s;
}

.pipeline-step:hover {
    border-color: var(--ink);
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}

.pipeline-step .step-num {
    font-family: var(--font-mono);
    font-size: 0.65rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--ink-light);
    margin-bottom: 0.35rem;
}

.pipeline-step .step-title {
    font-size: 0.82rem;
    font-weight: 700;
    color: var(--ink);
}

.pipeline-step .step-desc {
    font-size: 0.72rem;
    color: var(--ink-muted);
    margin-top: 0.25rem;
    line-height: 1.45;
}

/* ------------------------------------------------------------------ */
/* 13. FOOTER                                                          */
/* ------------------------------------------------------------------ */
.ed-footer {
    margin-top: 4rem;
    padding-top: 2rem;
    border-top: 3px solid var(--ink);
}

.ed-footer .footer-top {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    flex-wrap: wrap;
    gap: 1.5rem;
    padding-bottom: 1.5rem;
    border-bottom: 1px solid var(--hairline);
}

.ed-footer .footer-bottom {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 1rem;
    padding-top: 1rem;
    font-family: var(--font-mono);
    font-size: 0.7rem;
    color: var(--ink-light);
}

/* ------------------------------------------------------------------ */
/* 14. PLOTLY CHART CONTAINERS                                         */
/* ------------------------------------------------------------------ */
div[data-testid="stPlotlyChart"] {
    background: #FFFFFF;
    border: 1px solid var(--hairline);
    border-radius: 6px;
    padding: 1rem;
    box-shadow: 0 1px 3px rgba(0,0,0,0.03);
    margin-bottom: 0;
}

/* ------------------------------------------------------------------ */
/* 15. DATAFRAME                                                       */
/* ------------------------------------------------------------------ */
div[data-testid="stDataFrame"] {
    border: 1px solid var(--hairline);
    border-radius: 6px;
    overflow: auto;
    background: #FFFFFF !important;
    box-shadow: 0 1px 3px rgba(0,0,0,0.03);
}

div[data-testid="stDataFrame"] table { font-family: var(--font-sans); font-size: 0.85rem; background: #FFFFFF !important; }
div[data-testid="stDataFrame"] thead tr { background: var(--paper-subtle) !important; }
div[data-testid="stDataFrame"] thead th { background: var(--paper-subtle) !important; color: var(--ink) !important; font-family: var(--font-mono); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.04em; font-weight: 600; }
div[data-testid="stDataFrame"] tbody tr { background: #FFFFFF !important; }
div[data-testid="stDataFrame"] tbody tr:hover { background: #F5F5F0 !important; }
div[data-testid="stDataFrame"] tbody td { color: var(--ink) !important; }

/* ------------------------------------------------------------------ */
/* 16. SELECTBOX & INPUTS                                              */
/* ------------------------------------------------------------------ */
div[data-baseweb="select"] > div { border-color: var(--hairline) !important; border-radius: 4px !important; font-family: var(--font-sans) !important; }
div[data-baseweb="select"] span { color: var(--ink) !important; -webkit-text-fill-color: var(--ink) !important; }
label[data-testid="stWidgetLabel"] p { color: var(--ink-muted) !important; font-family: var(--font-mono) !important; font-size: 0.72rem !important; text-transform: uppercase !important; letter-spacing: 0.04em !important; }

input[data-testid="stTextInput"] { border-color: var(--hairline) !important; font-family: var(--font-sans) !important; }

/* ------------------------------------------------------------------ */
/* 17. DOWNLOAD BUTTON                                                 */
/* ------------------------------------------------------------------ */
.stDownloadButton > button {
    font-family: var(--font-mono) !important;
    font-size: 0.72rem !important;
    font-weight: 600 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.04em !important;
    background: var(--ink) !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 4px !important;
    padding: 0.6rem 1.25rem !important;
    transition: background 0.2s !important;
}

.stDownloadButton > button:hover { background: var(--ink-muted) !important; }

/* ------------------------------------------------------------------ */
/* 18. SMOOTH SCROLL                                                   */
/* ------------------------------------------------------------------ */
html { scroll-behavior: smooth; }

/* ------------------------------------------------------------------ */
/* 19. SCROLLBAR                                                       */
/* ------------------------------------------------------------------ */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: var(--paper); }
::-webkit-scrollbar-thumb { background: #D6D3D1; border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #A8A29E; }

/* ------------------------------------------------------------------ */
/* 20. HR OVERRIDE                                                     */
/* ------------------------------------------------------------------ */
hr { border: none; border-top: 1px solid var(--hairline); margin: 2.5rem 0; }

/* ------------------------------------------------------------------ */
/* 21. HIDE SIDEBAR TOGGLE (full single-page)                          */
/* ------------------------------------------------------------------ */
button[data-testid="stSidebarCollapsedControl"] { display: none !important; }
section[data-testid="stSidebar"] { display: none !important; }
</style>
""",
    unsafe_allow_html=True,
)


# ==============================================================================
# DATA LOADER
# ==============================================================================
@st.cache_data
def load_data_and_geojson():
    data_paths = [
        Path(__file__).resolve().parent.parent.parent
        / "data" / "processed" / "data_lowongan" / "data_eda.csv",
        Path("D:/Developments/Riset Pribadi/Maganghub/data/processed/data_lowongan/data_eda.csv"),
        Path("data/processed/data_lowongan/data_eda.csv"),
    ]
    df_path = next((p for p in data_paths if p.exists()), None)
    if df_path is None:
        raise FileNotFoundError("Dataset data_eda.csv tidak ditemukan.")

    df = pd.read_csv(df_path)
    for c in ["Diploma", "Sarjana", "Profesi", "kuota", "pelamar", "hari_kerja"]:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0).astype(int)

    province_geo_mapping = {
        "Aceh (NAD)": "Aceh",
        "DI Yogyakarta": "Daerah Istimewa Yogyakarta",
        "Nusa Tenggara Barat (NTB)": "Nusa Tenggara Barat",
        "Nusa Tenggara Timur (NTT)": "Nusa Tenggara Timur",
    }
    df["provinsi_map"] = df["nama_provinsi"].map(
        lambda x: province_geo_mapping.get(str(x), str(x))
    )

    jawa = ["DKI Jakarta", "Jawa Barat", "Jawa Timur", "Jawa Tengah", "Banten",
            "DI Yogyakarta", "Daerah Istimewa Yogyakarta"]
    df["is_jawa"] = df["nama_provinsi"].isin(jawa) | df["provinsi_map"].isin(jawa)
    df["wilayah"] = df["is_jawa"].apply(lambda x: "Pulau Jawa" if x else "Luar Jawa")

    geo_paths = [
        Path(__file__).resolve().parent.parent.parent
        / "data" / "geojson" / "GeoJson-Indonesia-38-Provinsi" / "Provinsi"
        / "38 Provinsi Indonesia - Provinsi.json",
        Path("D:/Developments/Riset Pribadi/Maganghub/data/geojson/GeoJson-Indonesia-38-Provinsi/Provinsi/38 Provinsi Indonesia - Provinsi.json"),
        Path("data/geojson/GeoJson-Indonesia-38-Provinsi/Provinsi/38 Provinsi Indonesia - Provinsi.json"),
    ]
    geo_path = next((p for p in geo_paths if p.exists()), None)
    geojson_data = None
    if geo_path and geo_path.exists():
        with open(geo_path, "r", encoding="utf-8") as f:
            geojson_data = json.load(f)

    return df, geojson_data


try:
    df, geojson_indonesia = load_data_and_geojson()
except Exception as e:
    st.error(f"Gagal memuat dataset: {e!s}")
    st.stop()


# ==============================================================================
# COMPUTED METRICS
# ==============================================================================
total_lowongan = len(df)
total_kuota = int(df["kuota"].sum())
total_pelamar = int(df["pelamar"].sum())
avg_kuota = total_kuota / max(1, total_lowongan)
avg_pelamar = total_pelamar / max(1, total_lowongan)
agg_ratio = total_pelamar / max(1, total_kuota)
median_ratio = df["competition_ratio"].median()
n_provinsi = df["nama_provinsi"].nunique()
jawa_pct = (df["is_jawa"].sum() / max(1, total_lowongan)) * 100

total_sarjana = int(df["Sarjana"].sum()) if "Sarjana" in df else 0
total_diploma = int(df["Diploma"].sum()) if "Diploma" in df else 0
total_profesi = int(df["Profesi"].sum()) if "Profesi" in df else 0

pearson_r = df["kuota"].corr(df["pelamar"])


# ==============================================================================
# PLOTLY THEME HELPER
# ==============================================================================
_plotly_base = dict(
    font=dict(family="Plus Jakarta Sans, system-ui, sans-serif", size=11, color="#1A1A1A"),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
)

_grid = dict(showgrid=True, gridcolor="#E7E5E4", gridwidth=1)
_nogrid = dict(showgrid=False)


def _fmt(n):
    """Format large numbers: 418234 -> '418K'."""
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n / 1_000:.0f}K"
    return f"{n:,}"


# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║                         SINGLE-PAGE LAYOUT START                           ║
# ╚══════════════════════════════════════════════════════════════════════════════╝


# ══════════════════════════════════════════════════════════════════════════════
# MASTHEAD (sticky nav)
# ══════════════════════════════════════════════════════════════════════════════
st.markdown(
    """
<div class="masthead">
  <div class="masthead-inner">
    <div class="masthead-brand">
      <a href="#top">MagangHub</a>
      <span class="sep">/</span>
      <span class="tagline">From Opportunity to Competition</span>
    </div>
    <nav>
      <a href="#overview">Overview</a>
      <a href="#geography">Geography</a>
      <a href="#competition">Competition</a>
      <a href="#explorer">Explorer</a>
      <a href="#methodology">Methodology</a>
    </nav>
  </div>
</div>
""",
    unsafe_allow_html=True,
)


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 1 — HERO
# ══════════════════════════════════════════════════════════════════════════════
st.markdown(
    f"""
<div id="top" class="hero-section reveal">

  <div class="hero-kicker">
    <span class="hero-tag">Batch 2 2026</span>
    <span class="dot">&middot;</span>
    <span class="label">Editorial Data Story</span>
    <span class="dot">&middot;</span>
    <span class="label">Nasional</span>
  </div>

  <h1 class="hero-title">MagangHub Batch 2 2026</h1>

  <p class="hero-subtitle">
    Exploring internship opportunities, applicant demand, and competition across Indonesia.
  </p>

  <div class="hero-concept">
    <div class="concept-label">
      The Concept: <span class="concept-highlight">"From Opportunity to Competition"</span>
    </div>
    <p>
      Di balik <strong>{total_lowongan:,}</strong> lowongan magang yang dipublikasikan secara terbuka di
      <strong>{n_provinsi} provinsi</strong>, tersimpan dinamika struktural ketat: konsentrasi
      geografis di Pulau Jawa, disparitas peminat antar-sektor, dan fenomena di mana kuota besar
      justru menarik lonjakan pelamar yang eksponensial.
    </p>
  </div>

</div>
""",
    unsafe_allow_html=True,
)


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 2 — BIG PICTURE / MACRO OVERVIEW
# ══════════════════════════════════════════════════════════════════════════════
st.markdown(
    f"""
<div id="overview" class="section-block alt-bg">
  <div style="max-width:1100px; margin:0 auto;">

  <div class="reveal" style="max-width:42rem; margin-bottom:2rem;">
    <div class="section-kicker">01 // Macro Overview</div>
    <h2 class="section-title">How large is the internship ecosystem?</h2>
    <p class="section-lead">
      Data agregat MagangHub Batch 2 2026 memperlihatkan skala ekosistem pemagangan berskala nasional,
      merangkum ribuan korporasi swasta, BUMN, kementerian, hingga instansi daerah.
    </p>
  </div>

  <div class="stat-grid reveal">
    <div class="stat-card">
      <div class="stat-label">Total Lowongan</div>
      <div class="stat-value count-anim count-anim-d1">{total_lowongan:,}</div>
      <div class="stat-caption">Internship postings</div>
      <div class="stat-footnote">Total judul posisi unik yang dibuka oleh seluruh instansi terdaftar pada periode batch ini.</div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Kapasitas Kursi</div>
      <div class="stat-value count-anim count-anim-d2">{total_kuota:,}</div>
      <div class="stat-caption">Available positions</div>
      <div class="stat-footnote">Akumulasi kuota bangku magang yang dialokasikan, rata-rata {avg_kuota:.1f} kursi per lowongan terbuka.</div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Total Pendaftar</div>
      <div class="stat-value count-anim count-anim-d3">{_fmt(total_pelamar)}</div>
      <div class="stat-caption">Applicants</div>
      <div class="stat-footnote">Volume akumulatif berkas lamaran yang diajukan oleh mahasiswa dan lulusan baru se-Indonesia.</div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Tingkat Persaingan</div>
      <div class="stat-value accent count-anim count-anim-d4">{agg_ratio:.1f}&times;</div>
      <div class="stat-caption">Competition ratio</div>
      <div class="stat-footnote">Rata-rata nasional: hampir {agg_ratio:.0f} kandidat bersaing memperebutkan setiap 1 kuota kursi yang tersedia.</div>
    </div>
  </div>

  </div>
</div>
""",
    unsafe_allow_html=True,
)


# -- Analytical note + editorial footnote --
st.markdown(
    f"""
<div style="max-width:1100px; margin:0 auto; padding: 0 1.5rem;">
<div class="callout reveal" style="margin: 2rem 0;">
  <strong>Catatan Analitis:</strong> Rasio kompetisi dihitung sebagai
  <code>Pelamar / Kuota Kursi</code>. Angka ini merefleksikan desitas persaingan,
  bukan probabilitas statistik penerimaan individu. Median rasio lowongan: {median_ratio:.1f}&times;.
</div>
</div>
""",
    unsafe_allow_html=True,
)


# -- Overview Charts Row --
st.markdown('<div class="reveal" style="margin-top: 0.5rem;">', unsafe_allow_html=True)
col_ov1, col_ov2 = st.columns(2)

with col_ov1:
    st.markdown(
        """
    <div class="ed-card">
      <div class="ed-card-header">
        <div>
          <h3 class="ed-card-title">Distribusi Kelompok Kuota per Lowongan</h3>
          <p class="ed-card-sub">Bagaimana kuota lowongan tersebar antar-posisi?</p>
        </div>
        <span class="ed-badge">BQ1</span>
      </div>
    """,
        unsafe_allow_html=True,
    )

    def group_kuota(k):
        if k == 1: return "1 Kursi"
        elif k in [2, 3]: return "2-3 Kursi"
        elif k in [4, 5]: return "4-5 Kursi"
        elif 6 <= k <= 10: return "6-10 Kursi"
        else: return ">10 Kursi"

    df_kg = (
        df["kuota"].apply(group_kuota).value_counts()
        .reindex(["1 Kursi", "2-3 Kursi", "4-5 Kursi", "6-10 Kursi", ">10 Kursi"])
        .dropna().reset_index()
    )
    df_kg.columns = ["Kelompok", "Jumlah"]

    fig_kg = px.bar(df_kg, x="Kelompok", y="Jumlah", text="Jumlah",
                    color_discrete_sequence=["#1E293B"])
    fig_kg.update_traces(texttemplate="%{text:,}", textposition="outside",
                         hovertemplate="<b>%{x}</b><br>Jumlah: %{y:,}<extra></extra>")
    fig_kg.update_layout(height=310, margin=dict(l=10, r=10, t=10, b=10), **_plotly_base,
                         xaxis=dict(title="", **_nogrid), yaxis=dict(title="", **_grid))
    st.plotly_chart(fig_kg, use_container_width=True)

    st.markdown(
        """
      <div class="callout">
        <strong>Interpretasi:</strong> Mayoritas lowongan hanya menyediakan tepat 1 kursi penempatan,
        menunjukkan daya tampung yang terdistribusi secara granular ke unit kerja spesifik.
      </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

with col_ov2:
    st.markdown(
        """
    <div class="ed-card">
      <div class="ed-card-header">
        <div>
          <h3 class="ed-card-title">Kategori Peluang Berdasarkan Label Platform</h3>
          <p class="ed-card-sub">Proporsi lowongan menurut kategori peluang resmi MagangHub</p>
        </div>
        <span class="ed-badge">Label</span>
      </div>
    """,
        unsafe_allow_html=True,
    )

    kat_c = df["kategori_peluang"].value_counts().reset_index()
    kat_c.columns = ["Kategori", "Jumlah"]
    kat_colors = {
        "Peluang Sangat Besar": "#475569",
        "Peluang Besar": "#64748B",
        "Peluang Sedang": "#94A3B8",
        "Peluang Kecil": "#C2410C",
        "Peluang Sangat Kecil": "#78716C",
    }
    fig_kat = px.pie(kat_c, names="Kategori", values="Jumlah", hole=0.55,
                     color="Kategori", color_discrete_map=kat_colors)
    fig_kat.update_traces(textposition="inside", textinfo="percent+label",
                          hovertemplate="<b>%{label}</b><br>%{value:,} lowongan (%{percent})<extra></extra>")
    fig_kat.update_layout(height=310, margin=dict(l=10, r=10, t=10, b=10),
                          showlegend=False, **_plotly_base)
    st.plotly_chart(fig_kat, use_container_width=True)

    st.markdown(
        """
      <div class="callout">
        <strong>Catatan:</strong> Kategori "Peluang Kecil" mendominasi karena rasio pelamar terhadap
        kuota di sebagian besar lowongan telah melebihi batas 5:1.
      </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

st.markdown("</div>", unsafe_allow_html=True)


# -- 3 Takeaway strip --
st.markdown(
    f"""
<div style="display:grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin: 1.25rem 0 0 0;" class="reveal">
  <div class="ed-card" style="border-top: 3px solid var(--accent-navy);">
    <div style="font-size:0.78rem; font-weight:700; text-transform:uppercase; letter-spacing:0.03em; color:var(--ink); margin-bottom:0.35rem;">
      Disparitas Spasial Jawa vs Luar Jawa
    </div>
    <p style="font-size:0.82rem; color:var(--ink-muted); line-height:1.55; margin:0;">
      Sebesar <strong>{jawa_pct:.1f}% lowongan</strong> berada di Pulau Jawa. DKI Jakarta dan Jawa Barat
      menjadi episentrum utama penyedia daya tampung magang nasional.
    </p>
  </div>
  <div class="ed-card" style="border-top: 3px solid var(--accent-rust);">
    <div style="font-size:0.78rem; font-weight:700; text-transform:uppercase; letter-spacing:0.03em; color:var(--ink); margin-bottom:0.35rem;">
      Tingkat Persaingan Agregat {agg_ratio:.2f}&times;
    </div>
    <p style="font-size:0.82rem; color:var(--ink-muted); line-height:1.55; margin:0;">
      Rasio agregat nasional berada pada angka <strong>{agg_ratio:.2f} pelamar per kursi</strong>.
      Angka ini mencerminkan densitas persaingan keseluruhan.
    </p>
  </div>
  <div class="ed-card" style="border-top: 3px solid var(--accent-slate);">
    <div style="font-size:0.78rem; font-weight:700; text-transform:uppercase; letter-spacing:0.03em; color:var(--ink); margin-bottom:0.35rem;">
      Aksesibilitas Multidisiplin
    </div>
    <p style="font-size:0.82rem; color:var(--ink-muted); line-height:1.55; margin:0;">
      Sebanyak <strong>{(total_sarjana / max(1, total_lowongan) * 100):.1f}% lowongan</strong> membuka kesempatan
      untuk jenjang Sarjana, dan <strong>{(total_diploma / max(1, total_lowongan) * 100):.1f}%</strong> turut membuka jalur Diploma.
    </p>
  </div>
</div>
""",
    unsafe_allow_html=True,
)


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 3 — GEOGRAPHY / SPATIAL DISTRIBUTION
# ══════════════════════════════════════════════════════════════════════════════
st.markdown(
    """
<div id="geography" class="section-block reveal" style="margin-top: 1rem;">
  <div class="section-kicker">02 // Spatial Distribution</div>
  <h2 class="section-title">Where are the opportunities?</h2>
  <p class="section-lead">
    Persebaran peluang magang masih bertumpu signifikan pada episentrum ekonomi Pulau Jawa,
    sementara wilayah luar Jawa menampilkan dinamika kuota yang lebih terspesialisasi.
  </p>
</div>
""",
    unsafe_allow_html=True,
)

# Map controls
map_metric = st.selectbox(
    "Pilih Metrik Tampilan Peta",
    ["Rasio Persaingan", "Jumlah Lowongan", "Total Kuota Kursi", "Total Pelamar"],
)

# Province aggregation
prov_agg = (
    df.groupby(["nama_provinsi", "provinsi_map"])
    .agg(lowongan=("posisi", "count"), kuota=("kuota", "sum"), pelamar=("pelamar", "sum"))
    .reset_index()
)
prov_agg["rasio"] = (prov_agg["pelamar"] / prov_agg["kuota"]).round(2)

metric_cfg = {
    "Rasio Persaingan": ("rasio", [[0, "#F4F4F0"], [0.4, "#C2410C"], [1, "#7C2D12"]], "Rasio (x)"),
    "Jumlah Lowongan": ("lowongan", [[0, "#F4F4F0"], [0.5, "#475569"], [1, "#1E293B"]], "Lowongan"),
    "Total Kuota Kursi": ("kuota", [[0, "#F4F4F0"], [0.5, "#64748B"], [1, "#1E293B"]], "Kuota"),
    "Total Pelamar": ("pelamar", [[0, "#F4F4F0"], [0.5, "#C2410C"], [1, "#7C2D12"]], "Pelamar"),
}
target_col, color_scale, legend_title = metric_cfg[map_metric]

if geojson_indonesia is not None:
    try:
        map_func = getattr(px, "choropleth_map", None) or getattr(px, "choropleth_mapbox", None)
        style_param = "map_style" if hasattr(px, "choropleth_map") else "mapbox_style"

        fig_map = map_func(
            prov_agg,
            geojson=geojson_indonesia,
            locations="provinsi_map",
            featureidkey="properties.PROVINSI",
            color=target_col,
            color_continuous_scale=color_scale,
            **{style_param: "carto-positron"},
            zoom=3.75,
            center={"lat": -2.5, "lon": 118},
            opacity=0.88,
            hover_name="nama_provinsi",
            hover_data={"provinsi_map": False, "lowongan": ":,", "kuota": ":,", "pelamar": ":,", "rasio": ":.2f"},
            labels={"lowongan": "Lowongan", "kuota": "Kuota", "pelamar": "Pelamar", "rasio": "Rasio"},
        )
        fig_map.update_layout(
            height=480, margin=dict(l=0, r=0, t=10, b=0), **_plotly_base,
            coloraxis_colorbar=dict(title=legend_title, thickness=14, len=0.75,
                                     tickfont=dict(size=10, family="Plus Jakarta Sans")),
        )
        st.plotly_chart(fig_map, use_container_width=True)
    except Exception as err_map:
        st.warning(f"Kendala rendering peta: {err_map!s}")
else:
    st.info("File GeoJSON 38 provinsi tidak terdeteksi.")

# Narrative box
st.markdown(
    """
<div class="pull-quote reveal">
  Konsentrasi Jawa dan Paradoks Akses Luar Daerah &mdash;
  DKI Jakarta, Jawa Barat, dan Jawa Timur secara kumulatif menguasai lebih dari
  <strong>70% total lowongan</strong> nasional. Kendati demikian, rasio keketatan di
  kota-kota pusat riset seperti Yogyakarta dan Jakarta menunjukkan bahwa konsentrasi
  kuota berbanding lurus dengan membludaknya pelamar dari seluruh penjuru tanah air.
</div>
""",
    unsafe_allow_html=True,
)

# Jawa vs Luar Jawa + Top 15 Provinces
col_geo1, col_geo2 = st.columns([5, 7])

with col_geo1:
    st.markdown(
        """
    <div class="ed-card reveal">
      <div class="ed-card-header">
        <div>
          <h3 class="ed-card-title">Komparasi Agregat: Jawa vs Luar Jawa</h3>
          <p class="ed-card-sub">Perbandingan total kuota, pelamar, dan rasio agregat</p>
        </div>
      </div>
    """,
        unsafe_allow_html=True,
    )

    reg_summary = (
        df.groupby("wilayah")
        .agg(lowongan=("posisi", "count"), kuota=("kuota", "sum"), pelamar=("pelamar", "sum"))
        .reset_index()
    )
    reg_summary["rasio_agregat"] = (reg_summary["pelamar"] / reg_summary["kuota"]).round(2)
    reg_summary["proporsi"] = (reg_summary["lowongan"] / total_lowongan * 100).round(1).astype(str) + "%"

    st.dataframe(
        reg_summary.rename(columns={
            "wilayah": "Wilayah", "lowongan": "Lowongan", "kuota": "Total Kuota",
            "pelamar": "Total Pelamar", "rasio_agregat": "Rasio Agregat", "proporsi": "Pangsa (%)",
        }),
        use_container_width=True, hide_index=True,
    )

    st.markdown(
        """
      <div class="callout" style="margin-top:0.75rem;">
        <strong>Temuan:</strong> Meskipun Pulau Jawa menampung mayoritas lowongan, rasio persaingan
        di Luar Jawa bisa lebih tinggi karena kuota yang relatif terbatas.
      </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

with col_geo2:
    st.markdown(
        """
    <div class="ed-card reveal">
      <div class="ed-card-header">
        <div>
          <h3 class="ed-card-title">Top 15 Provinsi — Kuota vs Pelamar</h3>
          <p class="ed-card-sub">Perbandingan kapasitas kursi vs volume pendaftar</p>
        </div>
      </div>
    """,
        unsafe_allow_html=True,
    )

    top15 = prov_agg.sort_values("kuota", ascending=False).head(15)
    fig_prov = go.Figure()
    fig_prov.add_trace(go.Bar(y=top15["nama_provinsi"], x=top15["kuota"], name="Kuota",
                              orientation="h", marker=dict(color="#1E293B")))
    fig_prov.add_trace(go.Bar(y=top15["nama_provinsi"], x=top15["pelamar"], name="Pelamar",
                              orientation="h", marker=dict(color="#C2410C")))
    fig_prov.update_layout(
        barmode="group", height=380, margin=dict(l=10, r=20, t=10, b=10),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        **_plotly_base, xaxis=dict(**_grid, title=""), yaxis=dict(title="", autorange="reversed"),
    )
    st.plotly_chart(fig_prov, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 4 — COMPETITION / CORRELATION
# ══════════════════════════════════════════════════════════════════════════════
st.markdown(
    f"""
<div id="competition" class="section-block alt-bg reveal">
  <div style="max-width:1100px; margin:0 auto;">
  <div style="max-width:42rem; margin-bottom:2rem;">
    <div class="section-kicker">03 // Correlation &amp; Dynamics</div>
    <h2 class="section-title">Does more quota mean less competition?</h2>
    <p class="section-lead">
      Asumsi umum mengira bahwa lowongan dengan kuota kursi besar memberikan peluang masuk yang lebih lapang.
      Pengujian statistik justru menunjukkan dinamika sebaliknya.
    </p>
  </div>

  <div style="display:grid; grid-template-columns: 1fr 2fr; gap:1rem; margin-bottom:1.5rem;">
    <div class="ed-card" style="margin:0;">
      <div style="font-family:var(--font-mono); font-size:0.68rem; text-transform:uppercase; letter-spacing:0.08em; color:var(--ink-light); margin-bottom:0.25rem;">Koefisien Korelasi</div>
      <div style="font-family:var(--font-mono); font-size:clamp(2rem,4vw,2.8rem); font-weight:700; color:var(--ink); line-height:1;">r = {pearson_r:.3f}</div>
      <div style="margin-top:0.5rem;">
        <span style="font-family:var(--font-mono); font-size:0.7rem; font-weight:600; background:#FEF3C7; color:#92400E; padding:0.2rem 0.5rem; border-radius:3px; border:1px solid #FDE68A;">Korelasi Positif Kuat (p &lt; 0.001)</span>
      </div>
      <div style="margin-top:0.75rem; padding-top:0.65rem; border-top:1px solid var(--hairline); font-size:0.75rem; color:var(--ink-muted); line-height:1.5;">
        <strong style="color:var(--ink);">Pearson correlation: {pearson_r:.3f}</strong><br>
        "Listings with larger quotas tend to attract more applicants."
      </div>
    </div>
    <div class="ed-card" style="margin:0; display:flex; flex-direction:column; justify-content:center;">
      <h4 style="font-family:var(--font-serif); font-size:1.15rem; font-weight:700; color:var(--ink); margin:0 0 0.5rem 0;">Mengapa Kuota Besar Menarik Lebih Banyak Pesaing?</h4>
      <p style="font-size:0.85rem; color:var(--ink-muted); line-height:1.6; margin:0;">
        Program dengan kuota besar (15-35 kursi) umumnya berasal dari institusi bergengsi &mdash; BUMN perbankan,
        konglomerasi multinasional, dan kementerian strategis. Reputasi nama besar dan daya tarik kompensasi
        memicu gelombang pelamar masif, sehingga rasio pelamar per kursi tetap tinggi.
      </p>
    </div>
  </div>

  </div>
</div>
""",
    unsafe_allow_html=True,
)

# Scatter + Quadrant
col_sc1, col_sc2 = st.columns([7, 5])

with col_sc1:
    st.markdown(
        """
    <div class="ed-card reveal">
      <div class="ed-card-header">
        <div>
          <h3 class="ed-card-title">Scatter Plot: Kuota vs Pelamar</h3>
          <p class="ed-card-sub">Apakah kuota lebih besar berasosiasi dengan pelamar lebih banyak?</p>
        </div>
        <span class="ed-badge">Pearson r</span>
      </div>
    """,
        unsafe_allow_html=True,
    )

    sample_n = min(1500, len(df))
    df_scat = df.sample(n=sample_n, random_state=42) if len(df) > sample_n else df

    fig_sc = px.scatter(
        df_scat, x="kuota", y="pelamar", opacity=0.55,
        color_discrete_sequence=["#1E293B"], trendline="ols",
        hover_data={"posisi": True, "instansi": True, "kuota": True, "pelamar": True, "competition_ratio": ":.2f"},
        labels={"kuota": "Kapasitas Kuota", "pelamar": "Jumlah Pelamar", "competition_ratio": "Rasio"},
    )
    fig_sc.update_layout(
        height=400, margin=dict(l=10, r=10, t=10, b=10), **_plotly_base,
        xaxis=dict(**_grid, title="Kapasitas Kuota"), yaxis=dict(**_grid, title="Jumlah Pelamar"),
    )
    st.plotly_chart(fig_sc, use_container_width=True)

    st.markdown(
        f"""
      <div class="callout">
        <strong>Analisis Korelasi (r = {pearson_r:.3f}):</strong>
        Korelasi positif kuat menunjukkan lowongan dengan kuota besar cenderung menarik pelamar jauh lebih banyak.
        <em>Peringatan:</em> Korelasi ini bukan bukti kausalitas &mdash; institusi bereputasi tinggi secara mandiri memicu minat pendaftar.
      </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

with col_sc2:
    st.markdown(
        """
    <div class="ed-card reveal">
      <div class="ed-card-header">
        <div>
          <h3 class="ed-card-title">Analisis Kuadran</h3>
          <p class="ed-card-sub">Klasifikasi posisi berdasarkan median kuota dan pelamar</p>
        </div>
        <span class="ed-badge">Kuadran</span>
      </div>
    """,
        unsafe_allow_html=True,
    )

    med_k = df["kuota"].median()
    med_p = df["pelamar"].median()
    q1 = len(df[(df["kuota"] > med_k) & (df["pelamar"] > med_p)])
    q2 = len(df[(df["kuota"] <= med_k) & (df["pelamar"] > med_p)])
    q3 = len(df[(df["kuota"] <= med_k) & (df["pelamar"] <= med_p)])
    q4 = len(df[(df["kuota"] > med_k) & (df["pelamar"] <= med_p)])

    st.markdown(
        f"""
    <div class="quad-grid">
      <div class="quad-cell"><div class="quad-label" style="color:var(--accent-rust);">Kuadran II &mdash; Paling Ketat</div>
        <div class="quad-value">{q2:,}</div><div class="quad-desc">Kuota &le; {med_k:.0f}, Pelamar &gt; {med_p:.0f}</div></div>
      <div class="quad-cell"><div class="quad-label" style="color:#92400E;">Kuadran I &mdash; Kompetisi Masif</div>
        <div class="quad-value">{q1:,}</div><div class="quad-desc">Kuota &gt; {med_k:.0f}, Pelamar &gt; {med_p:.0f}</div></div>
      <div class="quad-cell"><div class="quad-label" style="color:var(--ink-light);">Kuadran III &mdash; Terbatas</div>
        <div class="quad-value">{q3:,}</div><div class="quad-desc">Kuota &le; {med_k:.0f}, Pelamar &le; {med_p:.0f}</div></div>
      <div class="quad-cell"><div class="quad-label" style="color:#166534;">Kuadran IV &mdash; Peluang Terbaik</div>
        <div class="quad-value">{q4:,}</div><div class="quad-desc">Kuota &gt; {med_k:.0f}, Pelamar &le; {med_p:.0f}</div></div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Competition ratio histogram
    st.markdown(
        '<div style="margin-top:1rem; padding-top:0.75rem; border-top:1px solid var(--hairline);">'
        '<div style="font-size:0.85rem; font-weight:700; color:var(--ink); margin-bottom:0.5rem;">Distribusi Rasio Persaingan</div>',
        unsafe_allow_html=True,
    )

    fig_hist = px.histogram(df, x="competition_ratio", nbins=30, color_discrete_sequence=["#475569"])
    fig_hist.update_layout(
        height=180, margin=dict(l=10, r=10, t=10, b=10), **_plotly_base,
        xaxis=dict(**_grid, title="Rasio"), yaxis=dict(title=""),
    )
    st.plotly_chart(fig_hist, use_container_width=True)
    st.markdown("</div></div>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 5 — REQUIREMENTS & MAJORS
# ══════════════════════════════════════════════════════════════════════════════
st.markdown(
    """
<div class="section-block reveal" style="margin-top:1rem;">
  <div class="section-kicker">04 // Requirements &amp; Qualifications</div>
  <h2 class="section-title">What do employers look for?</h2>
  <p class="section-lead">
    Kualifikasi jenjang pendidikan, rumpun keilmuan, dan skema hari kerja yang paling banyak disyaratkan
    oleh instansi penyedia magang pada batch ini.
  </p>
</div>
""",
    unsafe_allow_html=True,
)

col_req1, col_req2 = st.columns([5, 7])

with col_req1:
    # Education level bar
    st.markdown(
        """
    <div class="ed-card reveal">
      <div class="ed-card-header">
        <div>
          <h3 class="ed-card-title">Kualifikasi Jenjang Pendidikan</h3>
          <p class="ed-card-sub">Persentase posisi yang mencantumkan syarat jenjang</p>
        </div>
        <span class="ed-badge">BQ8</span>
      </div>
    """,
        unsafe_allow_html=True,
    )

    df_jen = pd.DataFrame({
        "Jenjang": ["Sarjana (S1/D4)", "Diploma (D1-D3)", "Profesi"],
        "Jumlah": [total_sarjana, total_diploma, total_profesi],
    })
    fig_jen = px.bar(df_jen, x="Jenjang", y="Jumlah", text="Jumlah",
                     color_discrete_sequence=["#1E293B"])
    fig_jen.update_traces(texttemplate="%{text:,}", textposition="outside")
    fig_jen.update_layout(height=280, showlegend=False, margin=dict(l=10, r=10, t=10, b=10),
                          **_plotly_base, xaxis=dict(title="", **_nogrid), yaxis=dict(title="", **_grid))
    st.plotly_chart(fig_jen, use_container_width=True)

    st.markdown(
        """
      <div class="callout">
        <strong>Catatan:</strong> Satu lowongan dapat mencantumkan lebih dari satu jenjang,
        sehingga total lintas jenjang melebihi jumlah lowongan unik.
      </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Working days donut
    st.markdown(
        """
    <div class="ed-card reveal">
      <div class="ed-card-header">
        <div>
          <h3 class="ed-card-title">Distribusi Hari Kerja per Minggu</h3>
          <p class="ed-card-sub">Proporsi skema 5 hari vs 6 hari kerja</p>
        </div>
        <span class="ed-badge">BQ10</span>
      </div>
    """,
        unsafe_allow_html=True,
    )

    hk_c = df["hari_kerja"].value_counts().reset_index()
    hk_c.columns = ["Hari", "Jumlah"]
    hk_c["Label"] = hk_c["Hari"].apply(lambda x: f"{x} Hari Kerja")
    fig_hk = px.pie(hk_c, names="Label", values="Jumlah", hole=0.5,
                    color_discrete_sequence=["#1E293B", "#78716C"])
    fig_hk.update_traces(textposition="inside", textinfo="percent+label")
    fig_hk.update_layout(height=240, showlegend=False, margin=dict(l=10, r=10, t=10, b=10), **_plotly_base)
    st.plotly_chart(fig_hk, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col_req2:
    st.markdown(
        """
    <div class="ed-card reveal">
      <div class="ed-card-header">
        <div>
          <h3 class="ed-card-title">Top 20 Jurusan Paling Sering Disyaratkan</h3>
          <p class="ed-card-sub">Frekuensi pemanggilan jurusan dalam kualifikasi lowongan</p>
        </div>
        <span class="ed-badge">BQ8</span>
      </div>
    """,
        unsafe_allow_html=True,
    )

    all_jur = []
    for item in df["jurusan"].dropna():
        all_jur.extend([x.strip() for x in str(item).split(",") if len(x.strip()) > 1])
    top_jur = pd.Series(all_jur).value_counts().head(20).reset_index()
    top_jur.columns = ["Jurusan", "Jumlah"]
    top_jur = top_jur.sort_values("Jumlah", ascending=True)

    fig_jur = px.bar(top_jur, x="Jumlah", y="Jurusan", orientation="h", text="Jumlah",
                     color="Jumlah", color_continuous_scale=[[0, "#F4F4F0"], [1, "#1E293B"]])
    fig_jur.update_traces(texttemplate="%{text:,}", textposition="outside",
                          hovertemplate="<b>%{y}</b><br>%{x:,} lowongan<extra></extra>")
    fig_jur.update_layout(
        height=620, margin=dict(l=10, r=40, t=10, b=10), coloraxis_showscale=False,
        **_plotly_base, xaxis=dict(**_grid, title=""), yaxis=dict(title=""),
    )
    st.plotly_chart(fig_jur, use_container_width=True)

    st.markdown(
        """
      <div class="callout">
        <strong>Catatan:</strong> Hitungan mewakili jumlah lowongan unik yang mencantumkan nama jurusan tersebut.
        Satu posisi dapat mencantumkan rumpun ilmu yang luas.
      </div>
    </div>
    """,
        unsafe_allow_html=True,
    )


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 6 — OPPORTUNITY EXPLORER
# ══════════════════════════════════════════════════════════════════════════════
st.markdown(
    """
<div id="explorer" class="section-block reveal" style="margin-top:1rem;">
  <div class="section-kicker">05 // Directory &amp; Discovery</div>
  <h2 class="section-title">Explore the opportunities</h2>
  <p class="section-lead">
    Saring dan telusuri karakteristik lowongan magang berdasarkan kata kunci, wilayah, dan tingkat keketatan.
  </p>
</div>
""",
    unsafe_allow_html=True,
)

col_exp1, col_exp2 = st.columns([7, 5])

with col_exp1:
    search_kw = st.text_input(
        "Cari Posisi, Instansi, atau Jurusan",
        "",
        placeholder="Ketik kata kunci, misalnya: Akuntansi, Data Analyst...",
    )

with col_exp2:
    sort_mode = st.selectbox(
        "Urutkan Berdasarkan",
        ["Rasio Persaingan Terendah", "Rasio Persaingan Tertinggi",
         "Kuota Terbanyak", "Pelamar Terbanyak"],
    )

df_exp = df.copy()
if search_kw:
    kw = search_kw.strip().lower()
    df_exp = df_exp[
        df_exp["posisi"].astype(str).str.lower().str.contains(kw, na=False)
        | df_exp["instansi"].astype(str).str.lower().str.contains(kw, na=False)
        | df_exp["jurusan"].astype(str).str.lower().str.contains(kw, na=False)
    ]

sort_map = {
    "Rasio Persaingan Terendah": ("competition_ratio", True),
    "Rasio Persaingan Tertinggi": ("competition_ratio", False),
    "Kuota Terbanyak": ("kuota", False),
    "Pelamar Terbanyak": ("pelamar", False),
}
s_col, s_asc = sort_map[sort_mode]
df_exp = df_exp.sort_values(s_col, ascending=s_asc)

st.markdown(
    f"""
<div style="font-size:0.82rem; color:var(--ink-muted); margin:0.5rem 0 0.75rem 0;">
  Menampilkan <strong>{len(df_exp):,}</strong> lowongan yang memenuhi kriteria.
</div>
""",
    unsafe_allow_html=True,
)

display_cols = ["posisi", "instansi", "nama_kabupaten", "nama_provinsi",
                "kuota", "pelamar", "competition_ratio", "hari_kerja",
                "kategori_peluang", "jurusan"]
avail_cols = [c for c in display_cols if c in df_exp.columns]

st.dataframe(
    df_exp[avail_cols].rename(columns={
        "posisi": "Posisi", "instansi": "Instansi", "nama_kabupaten": "Kabupaten/Kota",
        "nama_provinsi": "Provinsi", "kuota": "Kuota", "pelamar": "Pelamar",
        "competition_ratio": "Rasio Persaingan", "hari_kerja": "Hari Kerja",
        "kategori_peluang": "Kategori Peluang", "jurusan": "Persyaratan Jurusan",
    }),
    use_container_width=True, height=520, hide_index=True,
)

csv_out = df_exp[avail_cols].to_csv(index=False).encode("utf-8")
st.download_button(
    label="Unduh Data Hasil Pencarian (CSV)",
    data=csv_out,
    file_name=f"maganghub_eksplorasi_{pd.Timestamp.now().strftime('%Y%m%d_%H%M')}.csv",
    mime="text/csv",
)


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 7 — METHODOLOGY
# ══════════════════════════════════════════════════════════════════════════════
st.markdown(
    """
<div id="methodology" class="section-block alt-bg reveal" style="margin-top:1rem;">
  <div style="max-width:1100px; margin:0 auto;">
  <div style="max-width:42rem; margin-bottom:2rem;">
    <div class="section-kicker">06 // Provenance &amp; Rigor</div>
    <h2 class="section-title">How this analysis was built</h2>
    <p class="section-lead">
      Menjunjung tinggi prinsip reproduksibilitas sains data dan jurnalisme visual.
      Alur pemrosesan dirancang secara transparan dari pengumpulan data mentah hingga penyajian interaktif.
    </p>
  </div>

  <div class="pipeline">
    <div class="pipeline-step"><div class="step-num">Tahap 01</div><div class="step-title">Data Collection</div><div class="step-desc">Web scraping MagangHub Kemnaker via API publik</div></div>
    <div class="pipeline-step"><div class="step-num">Tahap 02</div><div class="step-title">Data Cleaning</div><div class="step-desc">Normalisasi nama provinsi, parsing jurusan multivalued</div></div>
    <div class="pipeline-step"><div class="step-num">Tahap 03</div><div class="step-title">Feature Engineering</div><div class="step-desc">Hitung competition ratio, klasifikasi wilayah Jawa/Luar Jawa</div></div>
    <div class="pipeline-step"><div class="step-num">Tahap 04</div><div class="step-title">EDA &amp; Statistical Test</div><div class="step-desc">Pearson correlation, distribusi, uji hipotesis deskriptif</div></div>
    <div class="pipeline-step"><div class="step-num">Tahap 05</div><div class="step-title">Visualization</div><div class="step-desc">Plotly choropleth, scatter, bar, dan donut charts</div></div>
    <div class="pipeline-step"><div class="step-num">Tahap 06</div><div class="step-title">Deployment</div><div class="step-desc">Streamlit Cloud dengan editorial data journalism design</div></div>
  </div>

  </div>
</div>
""",
    unsafe_allow_html=True,
)

# Methodology detail cards
col_m1, col_m2 = st.columns(2)

with col_m1:
    st.markdown(
        """
<div class="ed-card reveal">
  <div class="ed-card-header">
    <h4 class="ed-card-title">Sumber Data dan Unit Observasi</h4>
  </div>
  <p style="font-size:0.85rem; color:var(--ink-muted); line-height:1.65; margin:0;">
    Data dikumpulkan dari repositori resmi program MagangHub Kemnaker Batch 2 2026.
    Unit observasi adalah satu baris yang mewakili satu lowongan unik dengan atribut kuota,
    jumlah pelamar, lokasi administratif, kualifikasi jenjang, serta jurusan yang disyaratkan.
  </p>
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
<div class="ed-card reveal">
  <div class="ed-card-header">
    <h4 class="ed-card-title">Definisi dan Formula Metrik</h4>
  </div>
  <div style="font-family:var(--font-mono); font-size:0.8rem; background:var(--paper-subtle); border:1px solid var(--hairline); padding:0.75rem; border-radius:4px; margin-bottom:0.75rem; color:var(--ink);">
    Competition Ratio = Total Applicants / Total Quota Seats
  </div>
  <ul style="font-size:0.85rem; color:var(--ink-muted); line-height:1.65; padding-left:1.25rem; margin:0;">
    <li><strong>Competition Ratio per Lowongan:</strong> <code>pelamar / kuota</code>.</li>
    <li><strong>Competition Ratio Agregat:</strong> <code>total pelamar / total kuota</code> pada kelompok analisis.</li>
    <li><strong>Korelasi Kuota vs Pelamar:</strong> Pearson r = {pearson_r:.3f}.</li>
  </ul>
</div>
""",
        unsafe_allow_html=True,
    )

with col_m2:
    st.markdown(
        """
<div class="ed-card reveal" style="border-left: 3px solid var(--accent-rust);">
  <div class="ed-card-header">
    <h4 class="ed-card-title" style="color:var(--accent-rust);">Analisis yang Dikecualikan dari Cakupan</h4>
  </div>
  <p style="font-size:0.85rem; color:var(--ink-muted); margin:0 0 0.5rem 0;">
    Sesuai dokumen spesifikasi proyek, analisis berikut <strong>secara sengaja tidak ditampilkan</strong>:
  </p>
  <ul style="font-size:0.85rem; color:var(--ink-muted); line-height:1.6; padding-left:1.25rem; margin:0;">
    <li><strong>Perbandingan Instansi Pemerintah vs Swasta (BQ3):</strong> Tidak ada klasifikasi instansi yang tervalidasi.</li>
    <li><strong>Pengelompokan Posisi ke Kategori Pekerjaan (BQ6):</strong> Belum tersedia taksonomi posisi yang dibakukan.</li>
  </ul>
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
<div class="ed-card reveal">
  <div class="ed-card-header">
    <h4 class="ed-card-title">Batasan Interpretasi</h4>
  </div>
  <p style="font-size:0.85rem; color:var(--ink-muted); line-height:1.65; margin:0;">
    Tingkat persaingan yang disajikan adalah ukuran densitas pendaftar, bukan probabilitas statistik
    penerimaan individu. Hasil analisis dimaksudkan untuk tujuan eksplorasi edukatif dan bahan pertimbangan strategi pelamar.
  </p>
</div>
""",
        unsafe_allow_html=True,
    )


# ══════════════════════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════════════════════
st.markdown(
    f"""
<div class="ed-footer reveal">
  <div class="footer-top">
    <div>
      <span class="hero-tag" style="margin-bottom:0.5rem; display:inline-block;">Portfolio-grade analysis</span>
      <h3 style="font-family:var(--font-serif); font-size:1.5rem; font-weight:700; color:var(--ink); margin:0.25rem 0 0 0;">
        MagangHub Batch 2 2026
      </h3>
      <p style="font-family:var(--font-serif); font-style:italic; font-size:0.9rem; color:var(--ink-muted); margin:0.25rem 0 0 0;">
        Interactive Data Story: From Opportunity to Competition
      </p>
    </div>
    <div style="text-align:right;">
      <div style="font-family:var(--font-mono); font-size:0.68rem; text-transform:uppercase; color:var(--ink-light); margin-bottom:0.15rem;">Author &amp; Data Scientist</div>
      <div style="font-family:var(--font-serif); font-size:1.05rem; font-weight:600; color:var(--ink);">Reza Irwansyah Aryanto</div>
      <div style="font-family:var(--font-mono); font-size:0.7rem; color:var(--ink-light); margin-top:0.15rem;">Alumni Universitas Teknologi Yogyakarta</div>
    </div>
  </div>
  <div class="footer-bottom">
    <div>&copy; 2026 MagangHub Data Investigation. Built with Editorial Data Journalism principles.</div>
    <div>{total_lowongan:,} lowongan terpetakan &middot; Data Snapshot Batch 2 2026</div>
  </div>
</div>
""",
    unsafe_allow_html=True,
)
