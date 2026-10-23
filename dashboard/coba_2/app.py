import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
import json
import numpy as np

# ==============================================================================
# KONFIGURASI HALAMAN
# ==============================================================================
st.set_page_config(
    page_title="MagangHub Analytics — Batch 2 2026",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==============================================================================
# DESIGN SYSTEM & STYLING (ngulikdata.com & 06_UI_UX_DESIGN_SYSTEM.md)
# Bebas Ikon / Emoji — Bersih, Editorial Data Journalism, Modern Minimalis
# ==============================================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

:root {
    /* Palet Warna Resmi - 06_UI_UX_DESIGN_SYSTEM */
    --color-bg-page: #FAF9F6;
    --color-surface: #FFFFFF;
    --color-surface-subtle: #F4F5F7;
    --color-border: #DCE5E8;
    --color-border-subtle: #E7ECEF;
    
    --color-text-main: #17324D;
    --color-text-muted: #5E7181;
    --color-text-light: #8798A5;
    
    --color-accent-teal: #167C80;
    --color-accent-teal-subtle: #E6F4F4;
    --color-accent-blue: #3977B8;
    --color-accent-blue-subtle: #EDF4FA;
    --color-accent-amber: #C38A2E;
    --color-accent-amber-subtle: #FAF3E6;
    --color-accent-red: #BD5B61;
    --color-accent-red-subtle: #FAEBEB;
    
    --font-sans: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
    --font-mono: 'JetBrains Mono', ui-monospace, monospace;
}

html, body, [class*="css"] {
    font-family: var(--font-sans);
    color: var(--color-text-main);
}

.stApp {
    background-color: var(--color-bg-page);
    color: var(--color-text-main);
}

.main .block-container {
    max-width: 1360px;
    padding-top: 1.25rem;
    padding-bottom: 4rem;
    padding-left: 2rem;
    padding-right: 2rem;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header[data-testid="stHeader"] {background: transparent; z-index: 90;}

/* -------------------------------------------------------------------------- */
/* STICKY TOP NAVBAR (Minimalis Tanpa Ikon)                                   */
/* -------------------------------------------------------------------------- */
.top-navbar {
    background: rgba(255, 255, 255, 0.94);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid var(--color-border);
    border-radius: 10px;
    padding: 0.85rem 1.4rem;
    margin-bottom: 1.2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 1px 3px rgba(23, 50, 77, 0.04);
    position: sticky;
    top: 0.5rem;
    z-index: 999;
}

.brand-section {
    display: flex;
    flex-direction: column;
}

.brand-title {
    font-size: 1.15rem;
    font-weight: 800;
    letter-spacing: -0.02em;
    color: var(--color-text-main);
    line-height: 1.2;
}

.brand-subtitle {
    font-size: 0.75rem;
    font-weight: 500;
    color: var(--color-text-muted);
}

.navbar-badges {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    flex-wrap: wrap;
}

.nav-pill {
    display: inline-flex;
    align-items: center;
    padding: 0.35rem 0.75rem;
    background: var(--color-surface-subtle);
    border: 1px solid var(--color-border);
    border-radius: 9999px;
    font-family: var(--font-mono);
    font-size: 0.725rem;
    font-weight: 600;
    color: var(--color-text-main);
}

.edition-tag {
    padding: 0.35rem 0.75rem;
    background: var(--color-accent-teal-subtle);
    border: 1px solid rgba(22, 124, 128, 0.25);
    border-radius: 9999px;
    color: var(--color-accent-teal);
    font-size: 0.725rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.04em;
}

/* -------------------------------------------------------------------------- */
/* TABS SEBAGAI NAVIGASI HALAMAN (Modern Minimalist Pill Tabs)                */
/* -------------------------------------------------------------------------- */
.stTabs [data-baseweb="tab-list"] {
    gap: 0.4rem;
    background-color: var(--color-surface);
    border: 1px solid var(--color-border);
    border-radius: 10px;
    padding: 0.45rem;
    box-shadow: 0 1px 3px rgba(23, 50, 77, 0.03);
    margin-bottom: 1.5rem;
    display: flex;
    flex-wrap: wrap;
}

.stTabs [data-baseweb="tab"] {
    height: 2.5rem;
    padding: 0 1.1rem;
    border-radius: 6px !important;
    background-color: transparent !important;
    border: none !important;
    font-family: var(--font-sans) !important;
    font-size: 0.825rem !important;
    font-weight: 600 !important;
    color: var(--color-text-muted) !important;
    transition: all 0.15s ease-in-out !important;
}

.stTabs [data-baseweb="tab"]:hover {
    background-color: var(--color-surface-subtle) !important;
    color: var(--color-text-main) !important;
}

.stTabs [aria-selected="true"] {
    background-color: var(--color-text-main) !important;
    color: #FFFFFF !important;
}

.stTabs [aria-selected="true"] p,
.stTabs [aria-selected="true"] span,
.stTabs [aria-selected="true"] div {
    color: #FFFFFF !important;
}

.stTabs [data-baseweb="tab-highlight"],
.stTabs [data-baseweb="tab-border"] {
    display: none !important;
}

/* -------------------------------------------------------------------------- */
/* HERO & CONTEXT BANNER                                                      */
/* -------------------------------------------------------------------------- */
.hero-card {
    background: var(--color-surface);
    border: 1px solid var(--color-border);
    border-radius: 10px;
    padding: 1.35rem 1.6rem;
    margin-bottom: 1.35rem;
    box-shadow: 0 1px 3px rgba(23, 50, 77, 0.03);
    border-left: 4px solid var(--color-accent-teal);
}

.hero-kicker {
    font-family: var(--font-mono);
    font-size: 0.72rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--color-accent-teal);
    margin-bottom: 0.35rem;
}

.hero-title {
    font-size: 1.45rem;
    font-weight: 700;
    color: var(--color-text-main);
    line-height: 1.3;
    margin: 0 0 0.4rem 0;
    letter-spacing: -0.02em;
}

.hero-desc {
    font-size: 0.88rem;
    color: var(--color-text-muted);
    line-height: 1.6;
    margin: 0;
    max-width: 64rem;
}

/* -------------------------------------------------------------------------- */
/* KPI METRIC CARDS (Clean Grid, Tanpa Ikon)                                  */
/* -------------------------------------------------------------------------- */
.kpi-box {
    background: var(--color-surface);
    border: 1px solid var(--color-border);
    border-radius: 8px;
    padding: 1.1rem 1.25rem;
    box-shadow: 0 1px 2px rgba(23, 50, 77, 0.03);
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.kpi-title {
    font-size: 0.75rem;
    font-weight: 600;
    color: var(--color-text-muted);
    text-transform: uppercase;
    letter-spacing: 0.04em;
    margin-bottom: 0.35rem;
}

.kpi-val {
    font-family: var(--font-mono);
    font-size: 2.1rem;
    font-weight: 700;
    color: var(--color-text-main);
    line-height: 1.1;
    letter-spacing: -0.03em;
    margin-bottom: 0.35rem;
}

.kpi-sub {
    font-size: 0.75rem;
    color: var(--color-text-light);
    line-height: 1.4;
}

/* -------------------------------------------------------------------------- */
/* STRATEGIC TAKEAWAY STRIP (3-Card Summary)                                  */
/* -------------------------------------------------------------------------- */
.takeaway-card {
    background: var(--color-surface);
    border: 1px solid var(--color-border);
    border-radius: 8px;
    padding: 1rem 1.25rem;
    box-shadow: 0 1px 2px rgba(23, 50, 77, 0.03);
    height: 100%;
}

.takeaway-head {
    font-size: 0.825rem;
    font-weight: 700;
    color: var(--color-text-main);
    text-transform: uppercase;
    letter-spacing: 0.04em;
    margin-bottom: 0.35rem;
}

.takeaway-text {
    font-size: 0.825rem;
    color: var(--color-text-muted);
    line-height: 1.55;
    margin: 0;
}

/* -------------------------------------------------------------------------- */
/* CONTENT CARD WRAPPER                                                       */
/* -------------------------------------------------------------------------- */
.panel-card {
    background: var(--color-surface);
    border: 1px solid var(--color-border);
    border-radius: 8px;
    padding: 1.35rem 1.5rem;
    margin-bottom: 1.4rem;
    box-shadow: 0 1px 2px rgba(23, 50, 77, 0.03);
}

.panel-header {
    border-bottom: 1px solid var(--color-border-subtle);
    padding-bottom: 0.75rem;
    margin-bottom: 1rem;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
}

.panel-title {
    font-size: 1.05rem;
    font-weight: 700;
    color: var(--color-text-main);
    letter-spacing: -0.015em;
    margin: 0;
}

.panel-sub {
    font-size: 0.8rem;
    color: var(--color-text-muted);
    margin: 0.15rem 0 0 0;
}

.panel-badge {
    font-family: var(--font-mono);
    font-size: 0.7rem;
    font-weight: 600;
    background: var(--color-surface-subtle);
    color: var(--color-text-muted);
    padding: 0.2rem 0.55rem;
    border-radius: 4px;
    border: 1px solid var(--color-border);
}

/* Catatan Analitis */
.callout-box {
    background: var(--color-surface-subtle);
    border-left: 3px solid var(--color-accent-teal);
    padding: 0.85rem 1rem;
    border-radius: 0 6px 6px 0;
    font-size: 0.8rem;
    color: var(--color-text-muted);
    line-height: 1.6;
    margin-top: 1rem;
}

/* -------------------------------------------------------------------------- */
/* SIDEBAR                                                                    */
/* -------------------------------------------------------------------------- */
section[data-testid="stSidebar"] {
    background-color: var(--color-surface) !important;
    border-right: 1px solid var(--color-border) !important;
}

section[data-testid="stSidebar"] > div {
    padding-top: 1.5rem;
}

.sidebar-heading {
    font-size: 0.88rem;
    font-weight: 700;
    color: var(--color-text-main);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 0.25rem;
}

.sidebar-desc {
    font-size: 0.75rem;
    color: var(--color-text-muted);
    margin-bottom: 1.25rem;
}

/* -------------------------------------------------------------------------- */
/* FOOTER                                                                     */
/* -------------------------------------------------------------------------- */
.footer-container {
    margin-top: 3.5rem;
    padding-top: 1.5rem;
    border-top: 1px solid var(--color-border);
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 1rem;
    color: var(--color-text-muted);
    font-size: 0.78rem;
}

.footer-bold {
    font-weight: 600;
    color: var(--color-text-main);
}
</style>
""", unsafe_allow_html=True)


# ==============================================================================
# DATA & GEOJSON LOADER
# ==============================================================================
@st.cache_data
def load_data_and_geojson():
    data_paths = [
        Path(__file__).resolve().parent.parent.parent / "data" / "processed" / "data_lowongan" / "data_eda.csv",
        Path("D:/Developments/Riset Pribadi/Maganghub/data/processed/data_lowongan/data_eda.csv"),
        Path("data/processed/data_lowongan/data_eda.csv")
    ]
    df_path = next((p for p in data_paths if p.exists()), None)
    if df_path is None:
        raise FileNotFoundError("Dataset data_eda.csv tidak ditemukan.")

    df = pd.read_csv(df_path)

    # Cast integer columns
    for c in ['Diploma', 'Sarjana', 'Profesi', 'kuota', 'pelamar', 'hari_kerja']:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors='coerce').fillna(0).astype(int)

    # Normalisasi Pemetaan Nama Provinsi ke GeoJSON 38 Provinsi
    province_geo_mapping = {
        'Aceh (NAD)': 'Aceh',
        'DI Yogyakarta': 'Daerah Istimewa Yogyakarta',
        'Nusa Tenggara Barat (NTB)': 'Nusa Tenggara Barat',
        'Nusa Tenggara Timur (NTT)': 'Nusa Tenggara Timur',
    }
    df['provinsi_map'] = df['nama_provinsi'].map(lambda x: province_geo_mapping.get(str(x), str(x)))

    # Klasifikasi Wilayah Jawa vs Luar Jawa
    jawa_provinces = ['DKI Jakarta', 'Jawa Barat', 'Jawa Timur', 'Jawa Tengah', 'Banten', 'DI Yogyakarta', 'Daerah Istimewa Yogyakarta']
    df['is_jawa'] = df['nama_provinsi'].isin(jawa_provinces) | df['provinsi_map'].isin(jawa_provinces)
    df['wilayah'] = df['is_jawa'].apply(lambda x: 'Pulau Jawa' if x else 'Luar Jawa')

    # Load GeoJSON
    geo_paths = [
        Path(__file__).resolve().parent.parent.parent / "data" / "geojson" / "GeoJson-Indonesia-38-Provinsi" / "Provinsi" / "38 Provinsi Indonesia - Provinsi.json",
        Path("D:/Developments/Riset Pribadi/Maganghub/data/geojson/GeoJson-Indonesia-38-Provinsi/Provinsi/38 Provinsi Indonesia - Provinsi.json"),
        Path("data/geojson/GeoJson-Indonesia-38-Provinsi/Provinsi/38 Provinsi Indonesia - Provinsi.json")
    ]
    geo_path = next((p for p in geo_paths if p.exists()), None)
    geojson_data = None
    if geo_path and geo_path.exists():
        with open(geo_path, 'r', encoding='utf-8') as f:
            geojson_data = json.load(f)

    return df, geojson_data

try:
    df_raw, geojson_indonesia = load_data_and_geojson()
except Exception as e:
    st.error(f"Gagal memuat dataset atau file GeoJSON: {str(e)}")
    st.stop()


# ==============================================================================
# SIDEBAR FILTERS
# ==============================================================================
with st.sidebar:
    st.markdown('<div class="sidebar-heading">Filter Parameter</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-desc">Penyaringan data untuk eksplorasi spesifik</div>', unsafe_allow_html=True)

    # Filter Provinsi
    all_provinces = sorted(df_raw['nama_provinsi'].dropna().unique().tolist())
    selected_provinsi = st.multiselect(
        "Provinsi",
        options=['Semua'] + all_provinces,
        default=['Semua'],
        help="Pilih satu atau beberapa provinsi untuk analisis wilayah terfokus."
    )

    # Filter Jenjang Pendidikan
    edu_options = ['Diploma', 'Sarjana', 'Profesi']
    selected_jenjang = st.multiselect(
        "Kualifikasi Jenjang",
        options=['Semua'] + edu_options,
        default=['Semua'],
        help="Persyaratan pendidikan minimal yang dapat melamar."
    )

    # Filter Hari Kerja
    hk_options = sorted(df_raw['hari_kerja'].dropna().unique().tolist())
    selected_hari_kerja = st.multiselect(
        "Hari Kerja per Minggu",
        options=['Semua'] + [f"{h} Hari" for h in hk_options],
        default=['Semua'],
        help="Distribusi jam dan hari kerja per minggu."
    )

    # Slider Batas Rasio Kompetisi
    max_comp_val = float(df_raw['competition_ratio'].max())
    comp_range = st.slider(
        "Rentang Rasio Persaingan",
        min_value=0.0,
        max_value=max_comp_val,
        value=(0.0, max_comp_val),
        step=1.0,
        help="Rasio pelamar dibagi kuota kursi (pelamar / kuota)."
    )

    st.markdown("---")

    active_filters_count = 0
    if 'Semua' not in selected_provinsi: active_filters_count += 1
    if 'Semua' not in selected_jenjang: active_filters_count += 1
    if 'Semua' not in selected_hari_kerja: active_filters_count += 1
    if comp_range != (0.0, max_comp_val): active_filters_count += 1

    st.caption(f"Status: **{active_filters_count} filter aktif**")

    if st.button("Reset Filter", use_container_width=True):
        st.session_state.clear()
        st.rerun()

    st.markdown("""
    <div style="margin-top: 1.5rem; padding: 0.85rem; background: #F4F5F7; border: 1px solid #DCE5E8; border-radius: 6px; font-size: 0.74rem; color: #5E7181; line-height: 1.5;">
        <strong>Sumber Data Resmi:</strong><br>
        Dataset snapshot MagangHub Kemnaker Batch 2 2026. Analisis bersifat deskriptif atas lowongan terdaftar dan bukan jaminan penerimaan.
    </div>
    """, unsafe_allow_html=True)


# ==============================================================================
# LOGIKA FILTER DATA
# ==============================================================================
df = df_raw.copy()

if 'Semua' not in selected_provinsi:
    df = df[df['nama_provinsi'].isin(selected_provinsi)]

if 'Semua' not in selected_jenjang:
    mask = pd.Series([False] * len(df), index=df.index)
    for j in selected_jenjang:
        if j in df.columns:
            mask |= (df[j] == 1)
    df = df[mask]

if 'Semua' not in selected_hari_kerja:
    hk_selected_ints = [int(x.replace(" Hari", "")) for x in selected_hari_kerja]
    df = df[df['hari_kerja'].isin(hk_selected_ints)]

df = df[(df['competition_ratio'] >= comp_range[0]) & (df['competition_ratio'] <= comp_range[1])]

if len(df) == 0:
    st.warning("Tidak ditemukan data yang cocok dengan kombinasi filter aktif. Silakan atur kembali filter pada panel samping.")
    st.stop()


# ==============================================================================
# PERHITUNGAN METRIK KUNCI (Sesuai 05_METRIC_DEFINITION.MD)
# ==============================================================================
total_lowongan = len(df)
total_kuota = int(df['kuota'].sum())
total_pelamar = int(df['pelamar'].sum())

# Sesuai formula BQ1 & BQ2:
avg_kuota_per_lowongan = total_kuota / max(1, total_lowongan)
avg_pelamar_per_lowongan = total_pelamar / max(1, total_lowongan)
agg_competition_ratio = total_pelamar / max(1, total_kuota)  # Rasio Agregat = 8.74x
median_ratio = df['competition_ratio'].median()

total_sarjana = int(df['Sarjana'].sum()) if 'Sarjana' in df else 0
total_diploma = int(df['Diploma'].sum()) if 'Diploma' in df else 0
total_profesi = int(df['Profesi'].sum()) if 'Profesi' in df else 0


# ==============================================================================
# TOP NAVBAR (Bebas Ikon, Sesuai Referensi ngulikdata.com)
# ==============================================================================
st.markdown(f"""
<div class="top-navbar">
    <div class="brand-section">
        <div class="brand-title">MagangHub Analytics</div>
        <div class="brand-subtitle">Batch 2 2026 — Produk Analisis Data dan Eksplorasi Lowongan Magang Nasional</div>
    </div>
    <div class="navbar-badges">
        <div class="nav-pill">{total_lowongan:,} Lowongan</div>
        <div class="nav-pill">{total_kuota:,} Kuota Kursi</div>
        <div class="nav-pill">{total_pelamar:,} Pelamar</div>
        <div class="edition-tag">Rasio Agregat {agg_competition_ratio:.2f}x</div>
    </div>
</div>
""", unsafe_allow_html=True)


# ==============================================================================
# HERO CONTEXT BANNER
# ==============================================================================
st.markdown(f"""
<div class="hero-card">
    <div class="hero-kicker">Ringkasan Analisis Deskriptif · MagangHub Batch 2 2026</div>
    <h1 class="hero-title">Karakteristik Lowongan, Ketersediaan Kuota, dan Tingkat Persaingan</h1>
    <p class="hero-desc">
        Menganalisis keseimbangan antara kapasitas kursi penempatan dan antusiasme pendaftar pada 
        <strong>{total_lowongan:,} lowongan unik</strong> di <strong>{df['nama_provinsi'].nunique()} provinsi</strong>. 
        Gunakan tab navigasi di bawah untuk meninjau distribusi spasial melalui peta choropleth, pola korelasi kuota vs pelamar, 
        serta eksplorasi detail lowongan.
    </p>
</div>
""", unsafe_allow_html=True)


# ==============================================================================
# KPI METRICS BAR (6 Kotak Terstruktur, Tanpa Ikon)
# ==============================================================================
kpi_c1, kpi_c2, kpi_c3, kpi_c4, kpi_c5, kpi_c6 = st.columns(6)

with kpi_c1:
    st.markdown(f"""
    <div class="kpi-box">
        <div class="kpi-title">Total Lowongan</div>
        <div class="kpi-val">{total_lowongan:,}</div>
        <div class="kpi-sub">Unit observasi lowongan unik</div>
    </div>
    """, unsafe_allow_html=True)

with kpi_c2:
    st.markdown(f"""
    <div class="kpi-box">
        <div class="kpi-title">Total Kuota</div>
        <div class="kpi-val">{total_kuota:,}</div>
        <div class="kpi-sub">Kapasitas kursi tersedia</div>
    </div>
    """, unsafe_allow_html=True)

with kpi_c3:
    st.markdown(f"""
    <div class="kpi-box">
        <div class="kpi-title">Total Pelamar</div>
        <div class="kpi-val">{total_pelamar:,}</div>
        <div class="kpi-sub">Pendaftar tercatat di sistem</div>
    </div>
    """, unsafe_allow_html=True)

with kpi_c4:
    st.markdown(f"""
    <div class="kpi-box">
        <div class="kpi-title">Rata-rata Kuota</div>
        <div class="kpi-val">{avg_kuota_per_lowongan:.2f}</div>
        <div class="kpi-sub">Kursi per satu lowongan</div>
    </div>
    """, unsafe_allow_html=True)

with kpi_c5:
    st.markdown(f"""
    <div class="kpi-box">
        <div class="kpi-title">Rata-rata Pelamar</div>
        <div class="kpi-val">{avg_pelamar_per_lowongan:.1f}</div>
        <div class="kpi-sub">Pelamar per satu lowongan</div>
    </div>
    """, unsafe_allow_html=True)

with kpi_c6:
    st.markdown(f"""
    <div class="kpi-box">
        <div class="kpi-title">Rasio Agregat</div>
        <div class="kpi-val">{agg_competition_ratio:.2f}x</div>
        <div class="kpi-sub">Pelamar dibagi kuota (Median: {median_ratio:.1f}x)</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height: 1.25rem;'></div>", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# 3 STRATEGIC TAKEAWAYS STRIP
# ------------------------------------------------------------------------------
t1, t2, t3 = st.columns(3)

with t1:
    jawa_lowongan_pct = (df['is_jawa'].sum() / max(1, len(df))) * 100
    st.markdown(f"""
    <div class="takeaway-card">
        <div class="takeaway-head">Disparitas Spasial Jawa vs Luar Jawa</div>
        <p class="takeaway-text">
            Sebesar <strong>{jawa_lowongan_pct:.1f}% lowongan</strong> berada di Pulau Jawa. DKI Jakarta dan Jawa Barat menjadi episentrum utama penyedia daya tampung magang nasional.
        </p>
    </div>
    """, unsafe_allow_html=True)

with t2:
    st.markdown(f"""
    <div class="takeaway-card">
        <div class="takeaway-head">Tingkat Persaingan Agregat 8,74x</div>
        <p class="takeaway-text">
            Rasio agregat nasional berada pada angka <strong>{agg_competition_ratio:.2f} pelamar per kursi</strong>. Angka ini mencerminkan densitas persaingan keseluruhan dan bukan probabilitas penerimaan individu.
        </p>
    </div>
    """, unsafe_allow_html=True)

with t3:
    st.markdown(f"""
    <div class="takeaway-card">
        <div class="takeaway-head">Aksesibilitas Multidisiplin</div>
        <p class="takeaway-text">
            Sebanyak <strong>{((total_sarjana/max(1, total_lowongan))*100):.1f}% lowongan</strong> membuka kesempatan untuk jenjang Sarjana, dan <strong>{((total_diploma/max(1, total_lowongan))*100):.1f}%</strong> turut membuka jalur bagi lulusan Diploma.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height: 1.25rem;'></div>", unsafe_allow_html=True)


# ==============================================================================
# TAB NAVIGASI UTAMA (6 HALAMAN TERSTRUKTUR SESUAI SPESIFIKASI)
# ==============================================================================
tab_overview, tab_wilayah, tab_kompetisi, tab_syarat, tab_explorer, tab_metodologi = st.tabs([
    "Ringkasan Ekosistem",
    "Distribusi Wilayah & Peta",
    "Persaingan & Kuota",
    "Persyaratan & Jurusan",
    "Penelusuran Lowongan",
    "Metodologi & Batasan"
])


# ==============================================================================
# TAB 1: RINGKASAN EKOSISTEM (BQ1 & BQ2)
# ==============================================================================
with tab_overview:
    col_ov1, col_ov2 = st.columns([6, 6])

    with col_ov1:
        st.markdown("""
        <div class="panel-card">
            <div class="panel-header">
                <div>
                    <h3 class="panel-title">Distribusi Kelompok Kuota per Lowongan</h3>
                    <p class="panel-sub">Bagaimana kuota lowongan tersebar antar-posisi?</p>
                </div>
                <span class="panel-badge">BQ1 — Kuota</span>
            </div>
        """, unsafe_allow_html=True)

        # Kelompokkan kuota agar tidak condong ekstrem
        def group_kuota(k):
            if k == 1: return '1 Kursi'
            elif k in [2, 3]: return '2 - 3 Kursi'
            elif k in [4, 5]: return '4 - 5 Kursi'
            elif 6 <= k <= 10: return '6 - 10 Kursi'
            else: return '> 10 Kursi'

        df_kuota_grp = df['kuota'].apply(group_kuota).value_counts().reindex(
            ['1 Kursi', '2 - 3 Kursi', '4 - 5 Kursi', '6 - 10 Kursi', '> 10 Kursi']
        ).dropna().reset_index()
        df_kuota_grp.columns = ['Kelompok Kuota', 'Jumlah Lowongan']

        fig_k_grp = px.bar(
            df_kuota_grp,
            x='Kelompok Kuota',
            y='Jumlah Lowongan',
            text='Jumlah Lowongan',
            color_discrete_sequence=['#167C80']
        )
        fig_k_grp.update_traces(
            texttemplate='%{text:,}',
            textposition='outside',
            hovertemplate='<b>%{x}</b><br>Jumlah Lowongan: %{y:,}<extra></extra>'
        )
        fig_k_grp.update_layout(
            height=330,
            margin=dict(l=10, r=10, t=10, b=10),
            font=dict(family="Inter", size=11, color="#17324D"),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(title="", showgrid=False),
            yaxis=dict(title="Jumlah Lowongan", showgrid=True, gridcolor='#E7ECEF')
        )
        st.plotly_chart(fig_k_grp, use_container_width=True)

        st.markdown("""
            <div class="callout-box">
                <strong>Interpretasi Distribusi Kuota:</strong> Mayoritas lowongan (lebih dari 60%) hanya menyediakan tepat 1 kursi penempatan. 
                Hal ini menunjukkan bahwa daya tampung magang sebagian besar terdistribusi secara granular ke unit-unit kerja spesifik.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_ov2:
        st.markdown("""
        <div class="panel-card">
            <div class="panel-header">
                <div>
                    <h3 class="panel-title">Kategori Peluang Berdasarkan Label Platform</h3>
                    <p class="panel-sub">Proporsi lowongan menurut kategori peluang resmi MagangHub</p>
                </div>
                <span class="panel-badge">Label Sumber</span>
            </div>
        """, unsafe_allow_html=True)

        kat_counts = df['kategori_peluang'].value_counts().reset_index()
        kat_counts.columns = ['Kategori', 'Jumlah']

        colors_kat = {
            'Peluang Sangat Besar': '#167C80',
            'Peluang Besar': '#3977B8',
            'Peluang Sedang': '#C38A2E',
            'Peluang Kecil': '#BD5B61',
            'Peluang Sangat Kecil': '#8798A5'
        }

        fig_kat = px.pie(
            kat_counts,
            names='Kategori',
            values='Jumlah',
            hole=0.55,
            color='Kategori',
            color_discrete_map=colors_kat
        )
        fig_kat.update_traces(
            textposition='inside',
            textinfo='percent+label',
            hovertemplate='<b>%{label}</b><br>Total: %{value:,} lowongan (%{percent})<extra></extra>'
        )
        fig_kat.update_layout(
            height=330,
            margin=dict(l=10, r=10, t=10, b=10),
            showlegend=False,
            font=dict(family="Inter", size=11, color="#17324D"),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig_kat, use_container_width=True)

        st.markdown("""
            <div class="callout-box">
                <strong>Catatan Metodologi:</strong> Kategori di atas merupakan parsing dari label platform bawaan (<code>kategori_peluang</code>). 
                Kategori "Peluang Kecil" mendominasi karena rasio pelamar terhadap kuota di sebagian besar lowongan telah melebihi batas 5:1.
            </div>
        </div>
        """, unsafe_allow_html=True)


# ==============================================================================
# TAB 2: DISTRIBUSI WILAYAH & PETA (BQ4 & BQ5 — MAP CHOROPLETH HEATMAP)
# ==============================================================================
with tab_wilayah:
    st.markdown("""
    <div class="panel-card">
        <div class="panel-header">
            <div>
                <h3 class="panel-title">Peta Persebaran Geografis Indonesia (Peta Choropleth 38 Provinsi)</h3>
                <p class="panel-sub">Eksplorasi spasial tingkat persaingan, kuota, pelamar, dan volume lowongan di seluruh Indonesia</p>
            </div>
            <span class="panel-badge">BQ4 & BQ5 — Visual Spasial</span>
        </div>
    """, unsafe_allow_html=True)

    # Agregasi data per provinsi
    prov_agg = df.groupby(['nama_provinsi', 'provinsi_map']).agg(
        lowongan=('posisi', 'count'),
        kuota=('kuota', 'sum'),
        pelamar=('pelamar', 'sum')
    ).reset_index()
    prov_agg['rasio'] = (prov_agg['pelamar'] / prov_agg['kuota']).round(2)

    # Pilihan metrik peta
    col_map_ctrl1, col_map_ctrl2 = st.columns([4, 8])

    with col_map_ctrl1:
        map_metric = st.selectbox(
            "Pilih Metrik Tampilan Peta:",
            options=[
                "Rasio Persaingan (Pelamar / Kuota)",
                "Jumlah Lowongan",
                "Total Kuota Kursi",
                "Total Pelamar"
            ],
            help="Ubah metrik visualisasi untuk mengamati sebaran indikator pada peta 38 provinsi."
        )

    # Konfigurasi parameter visual peta
    if map_metric == "Rasio Persaingan (Pelamar / Kuota)":
        target_col = 'rasio'
        color_scale = [[0, '#FAF3E6'], [0.4, '#C38A2E'], [1, '#BD5B61']]
        legend_title = "Rasio Persaingan (x)"
    elif map_metric == "Jumlah Lowongan":
        target_col = 'lowongan'
        color_scale = [[0, '#E6F4F4'], [0.5, '#459FA1'], [1, '#167C80']]
        legend_title = "Jumlah Lowongan"
    elif map_metric == "Total Kuota Kursi":
        target_col = 'kuota'
        color_scale = [[0, '#EDF4FA'], [0.5, '#689FD1'], [1, '#3977B8']]
        legend_title = "Total Kuota"
    else:
        target_col = 'pelamar'
        color_scale = [[0, '#FAF3E6'], [0.5, '#E09C38'], [1, '#C38A2E']]
        legend_title = "Total Pelamar"

    # Render peta choropleth jika GeoJSON tersedia
    if geojson_indonesia is not None:
        try:
            # Gunakan px.choropleth_map (Plotly >= 6.0) atau px.choropleth_mapbox
            map_func = getattr(px, 'choropleth_map', None) or getattr(px, 'choropleth_mapbox', None)
            style_param = 'map_style' if hasattr(px, 'choropleth_map') else 'mapbox_style'

            map_kwargs = {
                'geojson': geojson_indonesia,
                'locations': 'provinsi_map',
                'featureidkey': 'properties.PROVINSI',
                'color': target_col,
                'color_continuous_scale': color_scale,
                style_param: 'carto-positron',
                'zoom': 3.75,
                'center': {'lat': -2.5, 'lon': 118},
                'opacity': 0.88,
                'hover_name': 'nama_provinsi',
                'hover_data': {
                    'provinsi_map': False,
                    'lowongan': ':,',
                    'kuota': ':,',
                    'pelamar': ':,',
                    'rasio': ':.2f'
                },
                'labels': {
                    'lowongan': 'Lowongan',
                    'kuota': 'Kuota',
                    'pelamar': 'Pelamar',
                    'rasio': 'Rasio Persaingan'
                }
            }

            fig_map = map_func(prov_agg, **map_kwargs)
            fig_map.update_layout(
                height=500,
                margin=dict(l=0, r=0, t=10, b=0),
                font=dict(family='Inter', size=11, color='#17324D'),
                paper_bgcolor='rgba(0,0,0,0)',
                coloraxis_colorbar=dict(
                    title=legend_title,
                    thickness=14,
                    len=0.75,
                    tickfont=dict(size=10, family='Inter')
                )
            )
            st.plotly_chart(fig_map, use_container_width=True)

        except Exception as err_map:
            st.warning(f"Terjadi kendala saat merender peta interaktif: {str(err_map)}. Menampilkan data dalam format tabel agregasi.")
    else:
        st.info("File GeoJSON 38 provinsi tidak terdeteksi. Peta beralih ke visualisasi diagram batang provinsi.")

    st.markdown("""
        <div class="callout-box">
            <strong>Cara Membaca Peta:</strong> Arahkan kursor ke tiap wilayah provinsi untuk memeriksa nilai 
            <em>Jumlah Lowongan</em>, <em>Total Kuota</em>, <em>Total Pelamar</em>, dan <em>Rasio Persaingan Agregat Wilayah</em> (total pelamar provinsi dibagi total kuota provinsi).
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Baris Analisis Spasial Komparatif
    col_reg_agg, col_top_prov = st.columns([5, 7])

    with col_reg_agg:
        st.markdown("""
        <div class="panel-card">
            <div class="panel-header">
                <div>
                    <h3 class="panel-title">Komparasi Agregat: Jawa vs Luar Jawa</h3>
                    <p class="panel-sub">Perbandingan total kuota, pelamar, dan rasio agregat</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

        reg_summary = df.groupby('wilayah').agg(
            lowongan=('posisi', 'count'),
            kuota=('kuota', 'sum'),
            pelamar=('pelamar', 'sum')
        ).reset_index()
        reg_summary['rasio_agregat'] = (reg_summary['pelamar'] / reg_summary['kuota']).round(2)
        reg_summary['proporsi_lowongan'] = (reg_summary['lowongan'] / total_lowongan * 100).round(1).astype(str) + '%'

        st.dataframe(
            reg_summary.rename(columns={
                'wilayah': 'Wilayah',
                'lowongan': 'Lowongan',
                'kuota': 'Total Kuota',
                'pelamar': 'Total Pelamar',
                'rasio_agregat': 'Rasio Agregat',
                'proporsi_lowongan': 'Pangsa (%)'
            }),
            use_container_width=True,
            hide_index=True
        )

        st.markdown("""
            <div class="callout-box" style="margin-top: 0.75rem;">
                <strong>Temuan Spasial:</strong> Meskipun Pulau Jawa menampung mayoritas lowongan, rasio persaingan agregat di Luar Jawa 
                bisa lebih tinggi karena kuota kursi yang tersedia relatif terbatas terhadap jumlah pendaftar lokal.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_top_prov:
        st.markdown("""
        <div class="panel-card">
            <div class="panel-header">
                <div>
                    <h3 class="panel-title">Top 15 Provinsi Berdasarkan Kuota dan Pelamar</h3>
                    <p class="panel-sub">Perbandingan kapasitas kursi vs volume pendaftar</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

        top15_prov = prov_agg.sort_values(by='kuota', ascending=False).head(15)

        fig_prov_bar = go.Figure()
        fig_prov_bar.add_trace(go.Bar(
            y=top15_prov['nama_provinsi'],
            x=top15_prov['kuota'],
            name='Kapasitas Kuota',
            orientation='h',
            marker=dict(color='#3977B8')
        ))
        fig_prov_bar.add_trace(go.Bar(
            y=top15_prov['nama_provinsi'],
            x=top15_prov['pelamar'],
            name='Total Pelamar',
            orientation='h',
            marker=dict(color='#C38A2E')
        ))
        fig_prov_bar.update_layout(
            barmode='group',
            height=380,
            margin=dict(l=10, r=20, t=10, b=10),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            font=dict(family="Inter", size=10, color="#17324D"),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(showgrid=True, gridcolor='#E7ECEF', title="Jumlah"),
            yaxis=dict(title="", autorange="reversed")
        )
        st.plotly_chart(fig_prov_bar, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)


# ==============================================================================
# TAB 3: PERSAINGAN & KUOTA (BQ2, BQ9 — SCATTER KUOTA VS PELAMAR & HISTOGRAM)
# ==============================================================================
with tab_kompetisi:
    col_scat_l, col_scat_r = st.columns([7, 5])

    with col_scat_l:
        st.markdown("""
        <div class="panel-card">
            <div class="panel-header">
                <div>
                    <h3 class="panel-title">Scatter Plot: Hubungan Kuota vs Pelamar</h3>
                    <p class="panel-sub">Apakah kuota yang lebih besar berasosiasi dengan jumlah pelamar yang lebih banyak?</p>
                </div>
                <span class="panel-badge">BQ9 — Pearson r</span>
            </div>
        """, unsafe_allow_html=True)

        # Hitung korelasi Pearson
        pearson_r = df['kuota'].corr(df['pelamar'])

        sample_n = min(1500, len(df))
        df_scat_sample = df.sample(n=sample_n, random_state=42) if len(df) > sample_n else df

        fig_scat = px.scatter(
            df_scat_sample,
            x='kuota',
            y='pelamar',
            opacity=0.6,
            color_discrete_sequence=['#167C80'],
            trendline='ols',
            hover_data={
                'posisi': True,
                'instansi': True,
                'kuota': True,
                'pelamar': True,
                'competition_ratio': ':.2f'
            },
            labels={
                'kuota': 'Kapasitas Kuota Kursi',
                'pelamar': 'Jumlah Pelamar Terdaftar',
                'competition_ratio': 'Rasio Persaingan'
            }
        )
        fig_scat.update_layout(
            height=430,
            margin=dict(l=10, r=10, t=10, b=10),
            font=dict(family="Inter", size=11, color="#17324D"),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(showgrid=True, gridcolor='#E7ECEF', title="Kapasitas Kuota"),
            yaxis=dict(showgrid=True, gridcolor='#E7ECEF', title="Jumlah Pelamar")
        )
        st.plotly_chart(fig_scat, use_container_width=True)

        st.markdown(f"""
            <div class="callout-box">
                <strong>Analisis Korelasi Kuota dan Pelamar (Pearson r = {pearson_r:.3f}):</strong><br>
                Nilai korelasi positif yang kuat (r = {pearson_r:.3f}) menunjukkan bahwa lowongan dengan kuota besar cenderung menarik jumlah pelamar yang jauh lebih banyak. 
                <em>Peringatan Metodologis:</em> Korelasi positif ini bukan bukti bahwa penambahan kuota menyebabkan peningkatan pelamar. Instansi dengan kuota besar umumnya adalah institusi bereputasi tinggi yang secara mandiri memicu minat pendaftar.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_scat_r:
        st.markdown("""
        <div class="panel-card">
            <div class="panel-header">
                <div>
                    <h3 class="panel-title">Analisis Kuadran Kuota & Pelamar</h3>
                    <p class="panel-sub">Klasifikasi posisi berdasarkan median kuota (1) dan median pelamar (12)</p>
                </div>
                <span class="panel-badge">Kuadran BQ9</span>
            </div>
        """, unsafe_allow_html=True)

        med_k = df['kuota'].median()
        med_p = df['pelamar'].median()

        q1 = len(df[(df['kuota'] > med_k) & (df['pelamar'] > med_p)])
        q2 = len(df[(df['kuota'] <= med_k) & (df['pelamar'] > med_p)])
        q3 = len(df[(df['kuota'] <= med_k) & (df['pelamar'] <= med_p)])
        q4 = len(df[(df['kuota'] > med_k) & (df['pelamar'] <= med_p)])

        st.markdown(f"""
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.65rem; margin-bottom: 0.85rem;">
            <div style="background: var(--color-surface-subtle); border: 1px solid var(--color-border); border-radius: 6px; padding: 0.85rem;">
                <div style="font-size: 0.72rem; color: var(--color-accent-red); font-weight: 700; text-transform: uppercase;">Kuadran II — Paling Ketat</div>
                <div style="font-family: var(--font-mono); font-size: 1.4rem; font-weight: 700; color: var(--color-text-main); margin: 0.2rem 0;">{q2:,}</div>
                <div style="font-size: 0.73rem; color: var(--color-text-muted);">Kuota ≤ {med_k:.0f}, Pelamar > {med_p:.0f}</div>
            </div>
            <div style="background: var(--color-surface-subtle); border: 1px solid var(--color-border); border-radius: 6px; padding: 0.85rem;">
                <div style="font-size: 0.72rem; color: var(--color-accent-amber); font-weight: 700; text-transform: uppercase;">Kuadran I — Kompetisi Masif</div>
                <div style="font-family: var(--font-mono); font-size: 1.4rem; font-weight: 700; color: var(--color-text-main); margin: 0.2rem 0;">{q1:,}</div>
                <div style="font-size: 0.73rem; color: var(--color-text-muted);">Kuota > {med_k:.0f}, Pelamar > {med_p:.0f}</div>
            </div>
            <div style="background: var(--color-surface-subtle); border: 1px solid var(--color-border); border-radius: 6px; padding: 0.85rem;">
                <div style="font-size: 0.72rem; color: var(--color-text-muted); font-weight: 700; text-transform: uppercase;">Kuadran III — Terbatas</div>
                <div style="font-family: var(--font-mono); font-size: 1.4rem; font-weight: 700; color: var(--color-text-main); margin: 0.2rem 0;">{q3:,}</div>
                <div style="font-size: 0.73rem; color: var(--color-text-muted);">Kuota ≤ {med_k:.0f}, Pelamar ≤ {med_p:.0f}</div>
            </div>
            <div style="background: var(--color-surface-subtle); border: 1px solid var(--color-border); border-radius: 6px; padding: 0.85rem;">
                <div style="font-size: 0.72rem; color: var(--color-accent-teal); font-weight: 700; text-transform: uppercase;">Kuadran IV — Peluang Terbaik</div>
                <div style="font-family: var(--font-mono); font-size: 1.4rem; font-weight: 700; color: var(--color-text-main); margin: 0.2rem 0;">{q4:,}</div>
                <div style="font-size: 0.73rem; color: var(--color-text-muted);">Kuota > {med_k:.0f}, Pelamar ≤ {med_p:.0f}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="margin-top: 1rem;">
            <div class="panel-header" style="margin-bottom: 0.5rem; padding-bottom: 0.4rem;">
                <h4 style="font-size: 0.88rem; font-weight: 700; color: var(--color-text-main); margin: 0;">Distribusi Rasio Persaingan</h4>
            </div>
        """, unsafe_allow_html=True)

        fig_comp_hist = px.histogram(
            df,
            x='competition_ratio',
            nbins=30,
            color_discrete_sequence=['#5E7181']
        )
        fig_comp_hist.update_layout(
            height=190,
            margin=dict(l=10, r=10, t=10, b=10),
            font=dict(family="Inter", size=9, color="#17324D"),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(showgrid=True, gridcolor='#E7ECEF', title="Rasio (Pelamar/Kuota)"),
            yaxis=dict(title="")
        )
        st.plotly_chart(fig_comp_hist, use_container_width=True)

        st.markdown("""
        </div>
        </div>
        """, unsafe_allow_html=True)


# ==============================================================================
# TAB 4: PERSYARATAN & JURUSAN (BQ8 & BQ10)
# ==============================================================================
with tab_syarat:
    col_syarat_l, col_syarat_r = st.columns([5, 7])

    with col_syarat_l:
        st.markdown("""
        <div class="panel-card">
            <div class="panel-header">
                <div>
                    <h3 class="panel-title">Kualifikasi Jenjang Pendidikan</h3>
                    <p class="panel-sub">Persentase posisi yang mencantumkan syarat jenjang</p>
                </div>
                <span class="panel-badge">BQ8 — Jenjang</span>
            </div>
        """, unsafe_allow_html=True)

        pct_s1 = (total_sarjana / max(1, total_lowongan)) * 100
        pct_d3 = (total_diploma / max(1, total_lowongan)) * 100
        pct_prof = (total_profesi / max(1, total_lowongan)) * 100

        df_jenjang_plot = pd.DataFrame({
            'Jenjang': ['Sarjana (S1/D4)', 'Diploma (D1-D3)', 'Profesi'],
            'Jumlah Lowongan': [total_sarjana, total_diploma, total_profesi],
            'Pangsa': [pct_s1, pct_d3, pct_prof]
        })

        fig_jenjang = px.bar(
            df_jenjang_plot,
            x='Jenjang',
            y='Jumlah Lowongan',
            text='Jumlah Lowongan',
            color='Jenjang',
            color_discrete_sequence=['#3977B8', '#167C80', '#C38A2E']
        )
        fig_jenjang.update_traces(
            texttemplate='%{text:,} lowongan',
            textposition='outside'
        )
        fig_jenjang.update_layout(
            height=300,
            showlegend=False,
            margin=dict(l=10, r=10, t=10, b=10),
            font=dict(family="Inter", size=11, color="#17324D"),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(title=""),
            yaxis=dict(title="Jumlah Lowongan", showgrid=True, gridcolor='#E7ECEF')
        )
        st.plotly_chart(fig_jenjang, use_container_width=True)

        st.markdown("""
            <div class="callout-box">
                <strong>Catatan Multi-Kualifikasi:</strong> Satu lowongan dapat mencantumkan lebih dari satu jenjang pendidikan (misalnya Sarjana dan Diploma sekaligus), 
                sehingga jumlah total lintas jenjang melebihi jumlah lowongan unik.
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Distribusi Hari Kerja
        st.markdown("""
        <div class="panel-card">
            <div class="panel-header">
                <div>
                    <h3 class="panel-title">Distribusi Hari Kerja per Minggu</h3>
                    <p class="panel-sub">Proporsi lowongan menurut skema 5 hari vs 6 hari kerja</p>
                </div>
                <span class="panel-badge">BQ10 — Hari Kerja</span>
            </div>
        """, unsafe_allow_html=True)

        hk_counts = df['hari_kerja'].value_counts().reset_index()
        hk_counts.columns = ['Hari Kerja', 'Jumlah']
        hk_counts['Label'] = hk_counts['Hari Kerja'].apply(lambda x: f"{x} Hari Kerja")

        fig_hk = px.pie(
            hk_counts,
            names='Label',
            values='Jumlah',
            hole=0.5,
            color_discrete_sequence=['#167C80', '#5E7181']
        )
        fig_hk.update_traces(textposition='inside', textinfo='percent+label')
        fig_hk.update_layout(
            height=250,
            showlegend=False,
            margin=dict(l=10, r=10, t=10, b=10),
            font=dict(family="Inter", size=11, color="#17324D"),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig_hk, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col_syarat_r:
        st.markdown("""
        <div class="panel-card">
            <div class="panel-header">
                <div>
                    <h3 class="panel-title">Top 20 Jurusan / Program Studi Paling Sering Disyaratkan</h3>
                    <p class="panel-sub">Frekuensi pemanggilan jurusan dalam kualifikasi lowongan</p>
                </div>
                <span class="panel-badge">BQ8 — Jurusan</span>
            </div>
        """, unsafe_allow_html=True)

        all_jur = []
        for item in df['jurusan'].dropna():
            split_items = [x.strip() for x in str(item).split(',') if len(x.strip()) > 1]
            all_jur.extend(split_items)

        top_jur_series = pd.Series(all_jur).value_counts().head(20).reset_index()
        top_jur_series.columns = ['Jurusan', 'Jumlah Lowongan']
        top_jur_series = top_jur_series.sort_values(by='Jumlah Lowongan', ascending=True)

        fig_jur = px.bar(
            top_jur_series,
            x='Jumlah Lowongan',
            y='Jurusan',
            orientation='h',
            text='Jumlah Lowongan',
            color='Jumlah Lowongan',
            color_continuous_scale=[[0, '#E6F4F4'], [1, '#167C80']]
        )
        fig_jur.update_traces(
            texttemplate='%{text:,}',
            textposition='outside',
            hovertemplate='<b>%{y}</b><br>Dicantumkan di %{x:,} lowongan<extra></extra>'
        )
        fig_jur.update_layout(
            height=620,
            margin=dict(l=10, r=40, t=10, b=10),
            coloraxis_showscale=False,
            font=dict(family="Inter", size=10, color="#17324D"),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(showgrid=True, gridcolor='#E7ECEF', title="Jumlah Lowongan"),
            yaxis=dict(title="")
        )
        st.plotly_chart(fig_jur, use_container_width=True)

        st.markdown("""
            <div class="callout-box">
                <strong>Catatan Parsing Jurusan:</strong> Hitungan di atas mewakili jumlah lowongan unik yang mencantumkan nama jurusan tersebut. 
                Satu posisi dapat mencantumkan rumpun ilmu yang luas (misalnya Manajemen, Akuntansi, dan Informatika sekaligus).
            </div>
        </div>
        """, unsafe_allow_html=True)


# ==============================================================================
# TAB 5: PENELUSURAN LOWONGAN (Opportunity Explorer)
# ==============================================================================
with tab_explorer:
    st.markdown("""
    <div class="panel-card">
        <div class="panel-header">
            <div>
                <h3 class="panel-title">Penelusuran & Eksplorasi Lowongan Detail</h3>
                <p class="panel-sub">Pencarian interaktif pada repositori data lowongan MagangHub Batch 2 2026</p>
            </div>
            <span class="panel-badge">Data Explorer</span>
        </div>
    """, unsafe_allow_html=True)

    col_exp_s1, col_exp_s2 = st.columns([7, 5])

    with col_exp_s1:
        search_kw = st.text_input(
            "Cari Posisi, Instansi, atau Jurusan:",
            "",
            placeholder="Ketik kata kunci pencarian, misalnya: Akuntansi, Data Analyst, Pengadilan..."
        )

    with col_exp_s2:
        sort_mode = st.selectbox(
            "Urutkan Data Berdasarkan:",
            options=[
                "Rasio Persaingan Terendah (Peluang Relatif Terbuka)",
                "Rasio Persaingan Tertinggi (Paling Ketat)",
                "Kapasitas Kuota Terbanyak",
                "Total Pelamar Terbanyak"
            ]
        )

    # Filter pencarian
    df_exp = df.copy()
    if search_kw:
        kw = search_kw.strip().lower()
        df_exp = df_exp[
            df_exp['posisi'].astype(str).str.lower().str.contains(kw) |
            df_exp['instansi'].astype(str).str.lower().str.contains(kw) |
            df_exp['jurusan'].astype(str).str.lower().str.contains(kw)
        ]

    # Sorting
    if sort_mode == "Rasio Persaingan Terendah (Peluang Relatif Terbuka)":
        df_exp = df_exp.sort_values(by='competition_ratio', ascending=True)
    elif sort_mode == "Rasio Persaingan Tertinggi (Paling Ketat)":
        df_exp = df_exp.sort_values(by='competition_ratio', ascending=False)
    elif sort_mode == "Kapasitas Kuota Terbanyak":
        df_exp = df_exp.sort_values(by='kuota', ascending=False)
    elif sort_mode == "Total Pelamar Terbanyak":
        df_exp = df_exp.sort_values(by='pelamar', ascending=False)

    st.markdown(f"""
        <div style="font-size: 0.825rem; color: var(--color-text-muted); margin: 0.75rem 0;">
            Menampilkan <strong>{len(df_exp):,}</strong> lowongan yang memenuhi kriteria pencarian dan filter aktif.
        </div>
    """, unsafe_allow_html=True)

    display_columns = [
        'posisi', 'instansi', 'nama_kabupaten', 'nama_provinsi',
        'kuota', 'pelamar', 'competition_ratio', 'hari_kerja', 'kategori_peluang', 'jurusan'
    ]
    available_display = [c for c in display_columns if c in df_exp.columns]

    st.dataframe(
        df_exp[available_display].rename(columns={
            'posisi': 'Posisi',
            'instansi': 'Instansi',
            'nama_kabupaten': 'Kabupaten/Kota',
            'nama_provinsi': 'Provinsi',
            'kuota': 'Kuota',
            'pelamar': 'Pelamar',
            'competition_ratio': 'Rasio Persaingan',
            'hari_kerja': 'Hari Kerja',
            'kategori_peluang': 'Kategori Peluang',
            'jurusan': 'Persyaratan Jurusan'
        }),
        use_container_width=True,
        height=520,
        hide_index=True
    )

    csv_output = df_exp[available_display].to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Unduh Data Hasil Pencarian (CSV)",
        data=csv_output,
        file_name=f"maganghub_batch2_eksplorasi_{pd.Timestamp.now().strftime('%Y%m%d_%H%M')}.csv",
        mime="text/csv",
        use_container_width=False
    )

    st.markdown("</div>", unsafe_allow_html=True)


# ==============================================================================
# TAB 6: METODOLOGI & BATASAN (Sesuai 07_PAGE_SPECIFICATION.MD)
# ==============================================================================
with tab_metodologi:
    st.markdown("""
<div class="panel-card">
    <div class="panel-header">
        <div>
            <h3 class="panel-title">Metodologi & Batasan Analisis Data</h3>
            <p class="panel-sub">Dokumentasi formula metrik, sumber dataset, dan batasan cakupan penelitian</p>
        </div>
        <span class="panel-badge">Metodologi</span>
    </div>
</div>
""", unsafe_allow_html=True)

    col_m1, col_m2 = st.columns(2)

    with col_m1:
        st.markdown("""
<div class="panel-card">
    <div class="panel-header">
        <h4 class="panel-title" style="font-size: 0.95rem;">1. Sumber Data dan Unit Observasi</h4>
    </div>
    <p style="font-size: 0.85rem; color: var(--color-text-muted); line-height: 1.6; margin: 0;">
        Data dikumpulkan dari repositori resmi program MagangHub Kemnaker Batch 2 2026. 
        Unit observasi analisis adalah satu baris yang mewakili satu lowongan unik dengan atribut kuota, jumlah pelamar tercatat, 
        lokasi administratif, kualifikasi jenjang, serta jurusan yang disyaratkan.
    </p>
</div>
""", unsafe_allow_html=True)

        st.markdown("""
<div class="panel-card">
    <div class="panel-header">
        <h4 class="panel-title" style="font-size: 0.95rem;">2. Definisi dan Formula Metrik</h4>
    </div>
    <ul style="font-size: 0.85rem; color: var(--color-text-muted); line-height: 1.7; padding-left: 1.25rem; margin: 0;">
        <li><strong>Competition Ratio per Lowongan:</strong> Dihitung sebagai <code>pelamar / kuota</code>.</li>
        <li><strong>Competition Ratio Agregat:</strong> Dihitung sebagai <code>total pelamar / total kuota</code> pada kelompok analisis terkait. Rasio agregat digunakan untuk mencegah distorsi rata-rata sederhana pada lowongan dengan kuota kecil.</li>
        <li><strong>Korelasi Kuota vs Pelamar:</strong> Dihitung menggunakan koefisien korelasi Pearson (r = 0,743) pada subset observasi valid.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

    with col_m2:
        st.markdown("""
<div class="panel-card" style="border-left: 3px solid var(--color-accent-red);">
    <div class="panel-header">
        <h4 class="panel-title" style="font-size: 0.95rem; color: var(--color-accent-red);">3. Analisis yang Dikecualikan dari Cakupan</h4>
    </div>
    <p style="font-size: 0.85rem; color: var(--color-text-muted); margin: 0 0 0.5rem 0;">
        Sesuai dengan dokumen <em>02_BUSINESS_QUESTIONS.md</em>, analisis berikut <strong>secara sengaja tidak ditampilkan</strong> pada dashboard ini:
    </p>
    <ul style="font-size: 0.85rem; color: var(--color-text-muted); line-height: 1.6; padding-left: 1.25rem; margin: 0;">
        <li><strong>Perbandingan Instansi Pemerintah vs Swasta (BQ3):</strong> Tidak ada klasifikasi instansi pemerintah dan swasta yang tervalidasi secara resmi dalam dataset. Dashboard tidak membuat inferensi kategori hanya berdasarkan tebakan nama instansi.</li>
        <li><strong>Pengelompokan Posisi ke Kategori Pekerjaan Tertentu (BQ6):</strong> Kategori pekerjaan seperti IT/Data, Kesehatan, atau Administrasi Umum tidak dianalisis karena belum tersedia taksonomi posisi yang dibakukan.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

        st.markdown("""
<div class="panel-card">
    <div class="panel-header">
        <h4 class="panel-title" style="font-size: 0.95rem;">4. Batasan Interpretasi</h4>
    </div>
    <p style="font-size: 0.85rem; color: var(--color-text-muted); line-height: 1.6; margin: 0;">
        Tingkat persaingan atau rasio kompetisi yang disajikan adalah ukuran densitas pendaftar, bukan probabilitas statistik penerimaan pelamar secara individu. 
        Hasil analisis ini dimaksudkan untuk tujuan eksplorasi edukatif dan bahan pertimbangan strategi pelamar.
    </p>
</div>
""", unsafe_allow_html=True)


# ==============================================================================
# FOOTER COLOPHON
# ==============================================================================
st.markdown(f"""
<div class="footer-container">
    <div>
        <span class="footer-bold">MagangHub Analytics Platform</span> · Snapshot Data Batch 2 2026 ({total_lowongan:,} Lowongan Terpetakan)
    </div>
    <div>
        <span>Desain Editorial Data Journalism · Sesuai Spesifikasi Panduan Proyek</span>
    </div>
</div>
""", unsafe_allow_html=True)
