import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
import numpy as np

# Konfigurasi halaman
st.set_page_config(
    page_title="MagangHub Batch 2 2026 — From Opportunity to Competition",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Editorial Data Journalism CSS - Inspired by prototype
st.markdown("""
    <style>
    /* Import Google Fonts - Editorial Typography */
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;0,6..72,700;1,6..72,400;1,6..72,500&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');
    
    /* Design Tokens - Editorial Data Journalism */
    :root {
        /* Paper Colors */
        --color-paper: #FBFBFA;
        --color-paper-subtle: #F4F4F0;
        
        /* Ink Colors */
        --color-ink: #1A1A1A;
        --color-ink-muted: #57534E;
        --color-ink-light: #78716C;
        
        /* Hairline Borders */
        --color-hairline: #E7E5E4;
        --color-hairline-dark: #292524;
        
        /* Editorial Accents */
        --color-accent-rust: #C2410C;
        --color-accent-navy: #1E293B;
        --color-accent-slate: #475569;
        
        /* Typography */
        --font-serif: 'Newsreader', Georgia, serif;
        --font-sans: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
        --font-mono: 'JetBrains Mono', ui-monospace, monospace;
        
        /* Spacing */
        --space-xs: 0.25rem;
        --space-sm: 0.5rem;
        --space-md: 1rem;
        --space-lg: 1.5rem;
        --space-xl: 2rem;
        --space-2xl: 3rem;
        --space-3xl: 4rem;
    }
    
    /* Global Base - Paper Background */
    .stApp {
        background-color: var(--color-paper);
        font-family: var(--font-sans);
        color: var(--color-ink);
    }
    
    /* Main Content */
    .main .block-container {
        max-width: 1200px;
        padding-top: var(--space-xl);
        padding-bottom: var(--space-3xl);
    }
    
    /* Editorial Header - Newspaper Masthead Style */
    .editorial-header {
        border-bottom: 3px solid var(--color-ink);
        padding-bottom: var(--space-lg);
        margin-bottom: var(--space-2xl);
    }
    
    .editorial-kicker {
        font-family: var(--font-mono);
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: var(--color-ink-muted);
        margin-bottom: var(--space-sm);
    }
    
    .editorial-title {
        font-family: var(--font-serif);
        font-size: 3.5rem;
        font-weight: 700;
        line-height: 1.1;
        color: var(--color-ink);
        margin: 0 0 var(--space-md) 0;
        letter-spacing: -0.02em;
    }
    
    .editorial-subtitle {
        font-family: var(--font-serif);
        font-style: italic;
        font-size: 1.5rem;
        color: var(--color-ink-muted);
        line-height: 1.4;
        margin: 0;
    }
    
    .editorial-concept {
        border-left: 2px solid var(--color-ink);
        padding-left: var(--space-lg);
        margin: var(--space-xl) 0;
        max-width: 50rem;
    }
    
    .editorial-concept-label {
        font-weight: 600;
        color: var(--color-ink);
        margin-bottom: var(--space-xs);
        font-size: 0.875rem;
    }
    
    .editorial-concept-highlight {
        font-family: var(--font-serif);
        font-style: italic;
        color: var(--color-accent-rust);
    }
    
    .editorial-concept p {
        margin: var(--space-sm) 0;
    }
    
    /* Sidebar - Minimal Paper Style */
    section[data-testid="stSidebar"] {
        background-color: var(--color-paper-subtle);
        border-right: 1px solid var(--color-hairline);
    }
    
    section[data-testid="stSidebar"] > div {
        padding-top: var(--space-xl);
    }
    
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        font-family: var(--font-mono);
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: var(--color-ink-muted);
        font-weight: 600;
        margin-top: var(--space-lg);
        margin-bottom: var(--space-md);
    }
    
    section[data-testid="stSidebar"] label {
        font-family: var(--font-mono);
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: var(--color-ink-muted);
    }
    
    /* Editorial Metric Cards - Broadside Layout */
    div[data-testid="stMetric"] {
        background-color: transparent;
        border: none;
        border-top: 3px solid var(--color-ink);
        border-radius: 0;
        padding: var(--space-lg) 0;
        box-shadow: none;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }
    
    div[data-testid="stMetric"] label {
        font-family: var(--font-mono);
        font-size: 0.7rem;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: var(--color-ink-muted);
        font-weight: 500;
        margin-bottom: var(--space-md);
    }
    
    div[data-testid="stMetric"] [data-testid="stMetricValue"] {
        font-family: var(--font-mono);
        font-size: 3rem;
        font-weight: 700;
        color: var(--color-ink);
        line-height: 1;
        letter-spacing: -0.02em;
        margin: var(--space-md) 0;
    }
    
    div[data-testid="stMetric"] [data-testid="stMetricDelta"] {
        display: none;
    }
    
    /* Caption below metrics - centered */
    div[data-testid="stMetric"] + div[data-testid="stCaptionContainer"] {
        text-align: center;
        margin-top: var(--space-sm);
    }
    
    /* Section Headers - Editorial Style */
    h1, h2, h3 {
        font-family: var(--font-serif);
        color: var(--color-ink);
        font-weight: 700;
        line-height: 1.2;
    }
    
    h1 {
        font-size: 2.5rem;
        margin-top: var(--space-2xl);
        margin-bottom: var(--space-md);
        border-bottom: 1px solid var(--color-hairline);
        padding-bottom: var(--space-sm);
    }
    
    h2 {
        font-size: 2rem;
        margin-top: var(--space-xl);
        margin-bottom: var(--space-md);
    }
    
    h3 {
        font-size: 1.5rem;
        margin-top: var(--space-lg);
        margin-bottom: var(--space-sm);
    }
    
    /* Section Kicker */
    .section-kicker {
        font-family: var(--font-mono);
        font-size: 0.7rem;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: var(--color-ink-muted);
        margin-bottom: var(--space-sm);
    }
    
    /* Tabs - Minimal Editorial Navigation */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0;
        border-bottom: 1px solid var(--color-hairline);
        background-color: transparent;
        padding: 0;
    }
    
    .stTabs [data-baseweb="tab"] {
        font-family: var(--font-mono);
        font-size: 0.75rem;
        font-weight: 500;
        height: 3rem;
        padding: 0 var(--space-lg);
        color: var(--color-ink) !important;
        background-color: transparent;
        border: none;
        border-bottom: 2px solid transparent;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        color: var(--color-accent-rust) !important;
        background-color: transparent;
    }
    
    .stTabs [aria-selected="true"] {
        color: var(--color-ink) !important;
        border-bottom-color: var(--color-accent-rust);
        background-color: transparent;
        font-weight: 700;
    }
    
    /* Tab button text color override */
    .stTabs button[role="tab"] div {
        color: var(--color-ink) !important;
    }
    
    /* Chart Containers - Minimal Paper Style */
    div[data-testid="stPlotlyChart"] {
        background-color: white;
        border: 1px solid var(--color-hairline);
        border-radius: 0;
        padding: var(--space-lg);
        margin: var(--space-lg) 0;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
    }
    
    /* Dataframe/Table - Editorial Style with Scrolling */
    div[data-testid="stDataFrame"] {
        border: 1px solid var(--color-hairline);
        border-radius: 0;
        overflow: auto;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
        background-color: white !important;
        max-height: 600px;
    }
    
    div[data-testid="stDataFrame"] table {
        font-family: var(--font-sans);
        font-size: 0.875rem;
        background-color: white !important;
    }
    
    div[data-testid="stDataFrame"] thead tr {
        background-color: var(--color-paper-subtle) !important;
        color: var(--color-ink) !important;
        font-family: var(--font-mono);
        font-size: 0.7rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        font-weight: 600;
        position: sticky;
        top: 0;
        z-index: 10;
    }
    
    div[data-testid="stDataFrame"] thead th {
        background-color: var(--color-paper-subtle) !important;
        color: var(--color-ink) !important;
    }
    
    div[data-testid="stDataFrame"] tbody tr {
        background-color: white !important;
    }
    
    div[data-testid="stDataFrame"] tbody tr:hover {
        background-color: #F5F5F0 !important;
    }
    
    div[data-testid="stDataFrame"] tbody tr:nth-child(even) {
        background-color: #FAFAF9 !important;
    }
    
    div[data-testid="stDataFrame"] tbody td {
        color: var(--color-ink) !important;
        background-color: transparent !important;
    }
    
    /* Dividers - Editorial Hairline */
    hr {
        border: none;
        border-top: 1px solid var(--color-hairline);
        margin: var(--space-2xl) 0;
    }
    
    /* Footer - Editorial Colophon */
    .editorial-footer {
        margin-top: var(--space-3xl);
        padding-top: var(--space-xl);
        border-top: 3px solid var(--color-ink);
        font-family: var(--font-sans);
        font-size: 0.875rem;
        color: var(--color-ink-muted);
        line-height: 1.8;
    }
    
    .editorial-footer strong {
        color: var(--color-ink);
        font-weight: 600;
    }
    
    /* Buttons - Editorial Style */
    .stButton > button {
        font-family: var(--font-mono);
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        background-color: var(--color-ink);
        color: white !important;
        border: none;
        border-radius: 0;
        padding: var(--space-sm) var(--space-lg);
        transition: background-color 0.2s ease;
    }
    
    .stButton > button:hover {
        background-color: var(--color-ink-muted);
        color: white !important;
    }
    
    .stDownloadButton > button {
        font-family: var(--font-mono);
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        background-color: white;
        color: var(--color-ink) !important;
        border: 1px solid var(--color-ink);
        border-radius: 0;
        padding: var(--space-sm) var(--space-lg);
    }
    
    .stDownloadButton > button:hover {
        background-color: var(--color-paper-subtle);
        border-color: var(--color-ink);
        color: var(--color-ink) !important;
    }
    
    /* Radio button text */
    .stRadio label {
        color: var(--color-ink) !important;
    }
    
    /* Info/Warning boxes - Editorial Note Style */
    .stAlert {
        background-color: white;
        border: 1px solid var(--color-hairline);
        border-radius: 0;
        border-left: 2px solid var(--color-ink);
        font-family: var(--font-sans);
        font-size: 0.875rem;
        color: var(--color-ink-muted);
    }
    
    /* Input fields - Minimal Editorial Style */
    .stSelectbox, .stMultiSelect, .stTextInput {
        font-family: var(--font-sans);
        font-size: 0.875rem;
    }
    
    input, select, textarea {
        border-color: var(--color-hairline) !important;
        border-radius: 0 !important;
        font-family: var(--font-sans);
        color: var(--color-ink) !important;
        background-color: white !important;
    }
    
    input:focus, select:focus, textarea:focus {
        border-color: var(--color-ink) !important;
        box-shadow: none !important;
    }
    
    /* Multiselect options and dropdowns */
    div[data-baseweb="select"] span,
    div[data-baseweb="popover"] span,
    div[role="listbox"] span {
        color: var(--color-ink) !important;
    }
    
    /* Remove Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Responsive */
    @media (max-width: 768px) {
        .editorial-title {
            font-size: 2.5rem;
        }
        
        div[data-testid="stMetric"] [data-testid="stMetricValue"] {
            font-size: 2rem;
        }
    }
    
    /* Utility: Editorial Tag */
    .editorial-tag {
        display: inline-block;
        padding: 0.15rem 0.5rem;
        font-family: var(--font-mono);
        font-size: 0.7rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        border: 1px solid var(--color-hairline);
        background-color: var(--color-paper-subtle);
        color: var(--color-ink-muted);
        margin-right: var(--space-sm);
    }
    
    /* Analytical Note Box */
    .analytical-note {
        padding: var(--space-md);
        background-color: white;
        border: 1px solid var(--color-hairline);
        border-radius: 0;
        font-size: 0.75rem;
        color: var(--color-ink-muted);
        margin: var(--space-lg) 0;
    }
    
    .analytical-note strong {
        font-family: var(--font-mono);
        text-transform: uppercase;
        font-size: 0.7rem;
        letter-spacing: 0.05em;
        color: var(--color-ink);
    }
    </style>
""", unsafe_allow_html=True)

# Fungsi untuk load data
@st.cache_data
def load_data():
    """Load semua data yang diperlukan"""
    data_path = Path("D:/Developments/Riset Pribadi/Maganghub/data/processed/data_lowongan/data_eda.csv")
    df = pd.read_csv(data_path)
    
    for col in ['Diploma', 'Sarjana', 'Profesi']:
        if col in df.columns:
            df[col] = df[col].astype(int)
    
    return df

def calculate_metrics(df):
    """Hitung metrik-metrik utama"""
    metrics = {
        'total_lowongan': len(df),
        'total_kuota': df['kuota'].sum(),
        'total_pelamar': df['pelamar'].sum(),
        'avg_competition_ratio': df['competition_ratio'].mean(),
        'total_instansi': df['instansi'].nunique(),
        'total_provinsi': df['nama_provinsi'].nunique(),
        'total_kabupaten': df['nama_kabupaten'].nunique(),
    }
    return metrics

def classify_institution(df):
    """Klasifikasi instansi menjadi Pemerintah atau Swasta"""
    df = df.copy()
    
    gov_keywords = [
        'kementerian', 'kemen', 'deputi', 'direktorat', 'bps', 'kppn', 
        'pemerintah', 'pemda', 'dinas', 'badan', 'lembaga', 'kejaksaan',
        'pengadilan', 'polda', 'polres', 'tni', 'kemenko', 'sekretariat',
        'inspektorat', 'rsud', 'rs ', 'rumah sakit'
    ]
    
    def is_government(instansi):
        if pd.isna(instansi):
            return 'Tidak Diketahui'
        instansi_lower = str(instansi).lower()
        for keyword in gov_keywords:
            if keyword in instansi_lower:
                return 'Pemerintah'
        return 'Swasta'
    
    df['jenis_instansi'] = df['instansi'].apply(is_government)
    return df

# Editorial Chart Colors - Muted & Professional
CHART_COLORS = {
    'primary': '#1A1A1A',        # Ink
    'secondary': '#57534E',      # Ink muted  
    'accent': '#C2410C',         # Rust accent
    'navy': '#1E293B',           # Navy
    'slate': '#475569',          # Slate
    'stone_light': '#D6D3D1',
    'stone_dark': '#78716C',
    'categorical': ['#1A1A1A', '#57534E', '#78716C', '#A8A29E', '#C2410C', '#1E293B']
}

# Load data
try:
    df = load_data()
    df = classify_institution(df)
    metrics = calculate_metrics(df)
except Exception as e:
    st.error(f"Error loading data: {str(e)}")
    st.stop()

# ============================================================
# EDITORIAL HEADER - Newspaper Masthead Style
# ============================================================
st.markdown("""
<div class="editorial-header">
    <div class="editorial-kicker">
        <span class="editorial-tag">Batch 2 2026</span>
        <span>Editorial Data Story · Nasional</span>
    </div>
    <h1 class="editorial-title">MagangHub Batch 2 2026</h1>
    <p class="editorial-subtitle">Exploring internship opportunities, applicant demand, and competition across Indonesia.</p>
</div>
""", unsafe_allow_html=True)

# Editorial Concept Section - Using proper formatting
st.markdown("---")
st.markdown("**The Concept:** *\"From Opportunity to Competition\"*")
st.markdown("""
Di balik puluhan ribu kursi magang yang dipublikasikan secara terbuka, tersimpan dinamika struktural ketat: 
konsentrasi geografis di pulau Jawa, disparitas peminat antar-sektor, dan fenomena di mana kuota besar 
justru menarik lonjakan pelamar yang eksponensial.
""")
st.markdown("---")

# ============================================================
# SIDEBAR - Minimal Editorial Filters
# ============================================================
with st.sidebar:
    st.markdown("### Filter & Navigation")
    st.caption("Sesuaikan parameter analisis")
    
    selected_provinsi = st.multiselect(
        "Provinsi",
        options=['Semua'] + sorted(df['nama_provinsi'].unique().tolist()),
        default=['Semua']
    )
    
    jenis_instansi = st.multiselect(
        "Jenis Instansi",
        options=['Semua', 'Pemerintah', 'Swasta'],
        default=['Semua']
    )
    
    jenjang_options = []
    if df['Diploma'].sum() > 0:
        jenjang_options.append('Diploma')
    if df['Sarjana'].sum() > 0:
        jenjang_options.append('Sarjana')
    if df['Profesi'].sum() > 0:
        jenjang_options.append('Profesi')
    
    selected_jenjang = st.multiselect(
        "Jenjang Pendidikan",
        options=['Semua'] + jenjang_options,
        default=['Semua']
    )
    
    st.markdown("### Competition Ratio")
    min_comp, max_comp = st.slider(
        "Range",
        min_value=0.0,
        max_value=float(df['competition_ratio'].max()),
        value=(0.0, float(df['competition_ratio'].max())),
        step=1.0
    )
    
    st.markdown("---")
    st.info("Gunakan filter untuk mengeksplorasi subset data yang spesifik")

# Apply filters
df_filtered = df.copy()

if 'Semua' not in selected_provinsi:
    df_filtered = df_filtered[df_filtered['nama_provinsi'].isin(selected_provinsi)]

if 'Semua' not in jenis_instansi:
    df_filtered = df_filtered[df_filtered['jenis_instansi'].isin(jenis_instansi)]

if 'Semua' not in selected_jenjang:
    filter_mask = pd.Series([False] * len(df_filtered), index=df_filtered.index)
    if 'Diploma' in selected_jenjang:
        filter_mask |= df_filtered['Diploma'] == 1
    if 'Sarjana' in selected_jenjang:
        filter_mask |= df_filtered['Sarjana'] == 1
    if 'Profesi' in selected_jenjang:
        filter_mask |= df_filtered['Profesi'] == 1
    df_filtered = df_filtered[filter_mask]

df_filtered = df_filtered[
    (df_filtered['competition_ratio'] >= min_comp) & 
    (df_filtered['competition_ratio'] <= max_comp)
]

metrics_filtered = calculate_metrics(df_filtered)

# ============================================================
# SECTION 01: MACRO OVERVIEW - Editorial Statistics
# ============================================================
st.markdown('<div class="section-kicker">01 // Macro Overview</div>', unsafe_allow_html=True)
st.markdown("## How large is the internship ecosystem?")
st.caption("Data agregat MagangHub Batch 2 2026 memperlihatkan skala ekosistem pemagangan berskala nasional.")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Lowongan", f"{metrics_filtered['total_lowongan']:,}")
    st.caption("Internship postings")

with col2:
    st.metric("Kapasitas Kursi", f"{metrics_filtered['total_kuota']:,}")
    st.caption("Available positions")

with col3:
    st.metric("Total Pendaftar", f"{metrics_filtered['total_pelamar']:,}")
    st.caption("Applicants")

with col4:
    st.metric("Competition Ratio", f"{metrics_filtered['avg_competition_ratio']:.1f}×")
    st.caption("Avg competition")

st.markdown("""
<div class="analytical-note">
    <strong>Catatan Analitis:</strong> 
    Rasio kompetisi dihitung sebagai <code>Pelamar / Kuota Kursi</code>. 
    Angka ini merefleksikan densitas persaingan, bukan probabilitas statistik penerimaan individu.
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ============================================================
# SECTION 02: INSTANSI - Top Institutions
# ============================================================
st.markdown('<div class="section-kicker">02 // Institutional Distribution</div>', unsafe_allow_html=True)
st.markdown("## Top 15 Instansi")
st.caption("Institusi dengan lowongan terbanyak di MagangHub Batch 2 2026")

top_instansi = df_filtered['instansi'].value_counts().head(15).reset_index()
top_instansi.columns = ['Instansi', 'Jumlah']

fig_top_inst = px.bar(
    top_instansi,
    y='Instansi',
    x='Jumlah',
    orientation='h',
    color_discrete_sequence=[CHART_COLORS['primary']]
)
fig_top_inst.update_layout(
    height=500,
    font=dict(family="Plus Jakarta Sans, sans-serif", size=11, color='#1A1A1A'),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    margin=dict(l=20, r=20, t=20, b=60),
    xaxis=dict(title_font=dict(color='#1A1A1A'), tickfont=dict(color='#1A1A1A')),
    yaxis=dict(title_font=dict(color='#1A1A1A'), tickfont=dict(color='#1A1A1A'))
)
st.plotly_chart(fig_top_inst, use_container_width=True)

st.markdown("---")

# ============================================================
# SECTION 03: GEOGRAFIS - Spatial Distribution
# ============================================================
st.markdown('<div class="section-kicker">03 // Spatial Distribution</div>', unsafe_allow_html=True)
st.markdown("## Where are the opportunities?")
st.caption("Distribusi geografis lowongan dan pelamar di seluruh Indonesia")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Top 15 Provinsi — Lowongan")
    prov_lowongan = df_filtered['nama_provinsi'].value_counts().head(15).reset_index()
    prov_lowongan.columns = ['Provinsi', 'Jumlah']
    
    fig_prov = px.bar(
        prov_lowongan,
        x='Jumlah',
        y='Provinsi',
        orientation='h',
        color_discrete_sequence=[CHART_COLORS['primary']]
    )
    fig_prov.update_layout(
        font=dict(family="Plus Jakarta Sans, sans-serif", size=11, color='#1A1A1A'),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=20, t=20, b=60),
        xaxis=dict(title_font=dict(color='#1A1A1A'), tickfont=dict(color='#1A1A1A')),
        yaxis=dict(title_font=dict(color='#1A1A1A'), tickfont=dict(color='#1A1A1A'))
    )
    st.plotly_chart(fig_prov, use_container_width=True)

with col2:
    st.markdown("### Top 15 Provinsi — Pelamar")
    prov_pelamar = df_filtered.groupby('nama_provinsi')['pelamar'].sum().sort_values(ascending=False).head(15).reset_index()
    prov_pelamar.columns = ['Provinsi', 'Total']
    
    fig_pel = px.bar(
        prov_pelamar,
        x='Total',
        y='Provinsi',
        orientation='h',
        color_discrete_sequence=[CHART_COLORS['accent']]
    )
    fig_pel.update_layout(
        font=dict(family="Plus Jakarta Sans, sans-serif", size=11, color='#1A1A1A'),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=20, t=20, b=60),
        xaxis=dict(title_font=dict(color='#1A1A1A'), tickfont=dict(color='#1A1A1A')),
        yaxis=dict(title_font=dict(color='#1A1A1A'), tickfont=dict(color='#1A1A1A'))
    )
    st.plotly_chart(fig_pel, use_container_width=True)

st.markdown("""
<div style="border-left: 2px solid #1A1A1A; padding-left: 1.5rem; margin: 2rem 0; font-family: 'Newsreader', serif; font-style: italic; font-size: 1.125rem; line-height: 1.6; color: #1A1A1A;">
    DKI Jakarta, Jawa Barat, dan Jawa Timur secara kumulatif menguasai lebih dari 70% total lowongan nasional.
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ============================================================
# SECTION 04: POSISI - Position Analysis
# ============================================================
st.markdown('<div class="section-kicker">04 // Position Analysis</div>', unsafe_allow_html=True)
st.markdown("## Posisi dengan Peminat Tertinggi")
st.caption("Posisi yang paling banyak dicari dan dengan jumlah pelamar tertinggi")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Top 15 Posisi — Jumlah Lowongan")
    top_posisi = df_filtered['posisi'].value_counts().head(15).reset_index()
    top_posisi.columns = ['Posisi', 'Jumlah']
    
    fig_pos = px.bar(
        top_posisi,
        y='Posisi',
        x='Jumlah',
        orientation='h',
        color_discrete_sequence=[CHART_COLORS['navy']]
    )
    fig_pos.update_layout(
        height=500,
        font=dict(family="Plus Jakarta Sans, sans-serif", size=11, color='#1A1A1A'),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(title_font=dict(color='#1A1A1A'), tickfont=dict(color='#1A1A1A')),
        yaxis=dict(title_font=dict(color='#1A1A1A'), tickfont=dict(color='#1A1A1A'))
    )
    st.plotly_chart(fig_pos, use_container_width=True)

with col2:
    st.markdown("### Top 15 Posisi — Total Pelamar")
    pos_pelamar = df_filtered.groupby('posisi')['pelamar'].sum().sort_values(ascending=False).head(15).reset_index()
    pos_pelamar.columns = ['Posisi', 'Total']
    
    fig_pos_pel = px.bar(
        pos_pelamar,
        y='Posisi',
        x='Total',
        orientation='h',
        color_discrete_sequence=[CHART_COLORS['accent']]
    )
    fig_pos_pel.update_layout(
        height=500,
        font=dict(family="Plus Jakarta Sans, sans-serif", size=11, color='#1A1A1A'),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(title_font=dict(color='#1A1A1A'), tickfont=dict(color='#1A1A1A')),
        yaxis=dict(title_font=dict(color='#1A1A1A'), tickfont=dict(color='#1A1A1A'))
    )
    st.plotly_chart(fig_pos_pel, use_container_width=True)

st.markdown("---")

# ============================================================
# SECTION 05: JURUSAN - Academic Fields
# ============================================================
st.markdown('<div class="section-kicker">05 // Academic Fields</div>', unsafe_allow_html=True)
st.markdown("## Top 20 Jurusan Paling Dicari")
st.caption("Jurusan pendidikan yang paling banyak dibutuhkan oleh institusi")

all_jurusan = []
for jurusan_list in df_filtered['jurusan'].dropna():
    jurusan_items = [j.strip() for j in str(jurusan_list).split(',')]
    all_jurusan.extend(jurusan_items)

jurusan_counts = pd.Series(all_jurusan).value_counts().head(20).reset_index()
jurusan_counts.columns = ['Jurusan', 'Jumlah']

fig_jurusan = px.bar(
    jurusan_counts,
    y='Jurusan',
    x='Jumlah',
    orientation='h',
    color_discrete_sequence=[CHART_COLORS['primary']]
)
fig_jurusan.update_layout(
    height=600,
    font=dict(family="Plus Jakarta Sans, sans-serif", size=11, color='#1A1A1A'),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(title_font=dict(color='#1A1A1A'), tickfont=dict(color='#1A1A1A')),
    yaxis=dict(title_font=dict(color='#1A1A1A'), tickfont=dict(color='#1A1A1A'))
)
st.plotly_chart(fig_jurusan, use_container_width=True)

st.markdown("---")

# ============================================================
# SECTION 06: SUPPLY & DEMAND - Dynamics
# ============================================================
st.markdown('<div class="section-kicker">06 // Supply & Demand Dynamics</div>', unsafe_allow_html=True)
st.markdown("## Does more quota mean less competition?")
st.caption("Analisis hubungan antara kuota kursi dan jumlah pelamar")

df_sample = df_filtered.sample(n=min(1000, len(df_filtered)), random_state=42) if len(df_filtered) > 1000 else df_filtered

fig_scatter = px.scatter(
    df_sample,
    x='kuota',
    y='pelamar',
    color='jenis_instansi',
    hover_data=['posisi', 'instansi'],
    labels={'kuota': 'Kuota', 'pelamar': 'Pelamar'},
    color_discrete_map={'Pemerintah': CHART_COLORS['primary'], 'Swasta': CHART_COLORS['stone_dark']},
    trendline="ols"
)
fig_scatter.update_layout(
    font=dict(family="Plus Jakarta Sans, sans-serif", size=11, color='#1A1A1A'),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(title_font=dict(color='#1A1A1A'), tickfont=dict(color='#1A1A1A')),
    yaxis=dict(title_font=dict(color='#1A1A1A'), tickfont=dict(color='#1A1A1A')),
    legend=dict(font=dict(color='#1A1A1A'))
)
st.plotly_chart(fig_scatter, use_container_width=True)

st.markdown("""
<div style="border-left: 2px solid #C2410C; padding-left: 1.5rem; margin: 2rem 0; font-size: 0.875rem; line-height: 1.6; color: #57534E;">
    Program dengan kuota besar umumnya berasal dari institusi bergengsi. 
    Reputasi nama besar memicu gelombang pelamar masif, sehingga rasio persaingan tetap tinggi.
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ============================================================
# SECTION 07: EXPLORER - Data Explorer
# ============================================================
st.markdown('<div class="section-kicker">07 // Data Explorer</div>', unsafe_allow_html=True)
st.markdown("## Telusuri Lowongan Detail")
st.caption("Cari dan filter data lowongan sesuai kebutuhan")

search_query = st.text_input("Cari posisi, instansi, atau jurusan:", "")

if search_query:
    mask = (
        df_filtered['posisi'].str.contains(search_query, case=False, na=False) |
        df_filtered['instansi'].str.contains(search_query, case=False, na=False) |
        df_filtered['jurusan'].str.contains(search_query, case=False, na=False)
    )
    df_display = df_filtered[mask]
else:
    df_display = df_filtered

st.caption(f"Menampilkan {len(df_display):,} dari {len(df_filtered):,} lowongan")

display_cols = st.multiselect(
    "Kolom tampilan:",
    options=df_display.columns.tolist(),
    default=['posisi', 'instansi', 'nama_provinsi', 'kuota', 'pelamar', 'competition_ratio']
)

if display_cols:
    sort_col = st.selectbox("Urutkan:", options=display_cols)
    sort_order = st.radio("Urutan:", ["Ascending", "Descending"], horizontal=True)
    
    df_sorted = df_display[display_cols].sort_values(
        by=sort_col,
        ascending=(sort_order == "Ascending")
    )
    
    st.dataframe(df_sorted, use_container_width=True, height=600)
    
    csv = df_sorted.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Data (CSV)",
        data=csv,
        file_name=f'maganghub_export_{pd.Timestamp.now().strftime("%Y%m%d_%H%M%S")}.csv',
        mime='text/csv',
    )

# ============================================================
# EDITORIAL FOOTER - Colophon Style
# ============================================================
st.markdown("""
<div class="editorial-footer">
    <p><strong>MagangHub Batch 2 2026 — Interactive Data Story</strong></p>
    <p>Data dikumpulkan pada 21-22 September 2026 dari platform MagangHub (maganghub.kemnaker.go.id)</p>
    <p><strong>Dataset:</strong> {:,} lowongan · {:,} instansi · {} provinsi · {} kabupaten/kota</p>
    <p><strong>Metodologi:</strong> Competition ratio dihitung sebagai <code>Total Pelamar / Total Kuota</code>. 
    Klasifikasi instansi berdasarkan kata kunci pada nama instansi. 
    Data yang ditampilkan adalah snapshot pada periode pengumpulan data.</p>
    <p><strong>Catatan:</strong> Dashboard ini dibuat untuk tujuan analisis dan eksplorasi data. 
    Untuk informasi terkini dan pendaftaran resmi, kunjungi website resmi MagangHub.</p>
    <p style="margin-top: 1.5rem; padding-top: 1rem; border-top: 1px solid #E7E5E4; font-family: 'JetBrains Mono', monospace; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.05em; color: #78716C;">
        Built with UI/UX Pro Max Editorial Guidelines · Streamlit Dashboard
    </p>
</div>
""".format(
    metrics['total_lowongan'],
    metrics['total_instansi'],
    metrics['total_provinsi'],
    metrics['total_kabupaten']
), unsafe_allow_html=True)
