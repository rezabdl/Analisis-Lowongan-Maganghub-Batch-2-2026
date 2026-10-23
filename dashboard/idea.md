# MagangHub Insight --- Project Idea & Product Brief

## 1. Project Overview

**MagangHub Insight** adalah interactive data analytics website untuk
mengeksplorasi dan memahami karakteristik lowongan magang pada
**MagangHub Batch 2 2026**.

Project ini bukan sekadar dashboard statis. Tujuan utamanya adalah
mengubah hasil proses:

> **Data Collection → Data Cleaning → EDA → Business Questions → Data
> Visualization → Interactive Exploration**

menjadi sebuah **data product** yang dapat digunakan oleh dua tipe
pengguna:

1.  **Data/analytics audience** --- ingin melihat hasil analisis dan
    insight dari dataset.
2.  **End user/calon pencari magang** --- ingin mengeksplorasi lowongan
    berdasarkan program studi, lokasi, kuota, pelamar, dan competition
    ratio.

Website harus terasa seperti sebuah **analytics product**, bukan sekadar
notebook yang dipindahkan ke web.

------------------------------------------------------------------------

# 2. Main Goals

Website harus mampu:

-   Menjelaskan apa itu project MagangHub Insight.
-   Menyajikan hasil analisis MagangHub Batch 2 2026 secara visual dan
    mudah dipahami.
-   Menampilkan KPI utama dataset.
-   Menampilkan distribusi lowongan, kuota, pelamar, program studi, dan
    lokasi.
-   Menampilkan analisis competition ratio.
-   Menyediakan visualisasi geografis/map berdasarkan provinsi atau
    kabupaten/kota.
-   Memberikan user kemampuan untuk mencari dan memfilter lowongan
    secara interaktif.
-   Menjelaskan metodologi, data processing, dan rumus yang digunakan.
-   Menampilkan informasi pembuat project dan link personal/professional
    profile.

------------------------------------------------------------------------

# 3. Recommended Technology Stack

## Core Framework

Gunakan:

**Streamlit**

Alasan:

-   Project berfokus pada data analytics/data science.
-   Seluruh proses analisis sudah menggunakan Python.
-   Mudah menghubungkan Pandas dengan visualization library.
-   Mendukung multipage application.
-   Cocok untuk interactive filtering.
-   Cepat untuk dikembangkan dan di-deploy.
-   Tidak perlu membangun frontend/backend terpisah pada tahap awal.

Website harus menggunakan **multipage architecture**, bukan satu
`app.py` yang berisi seluruh dashboard.

------------------------------------------------------------------------

## Data Processing

Gunakan:

-   Python
-   Pandas
-   NumPy

Dataset yang sudah dibersihkan sebaiknya disimpan dalam format yang
efisien seperti:

-   `.parquet`

daripada selalu membaca raw CSV ketika aplikasi dijalankan.

------------------------------------------------------------------------

## Visualization

Gunakan:

**Plotly**

Untuk:

-   Bar chart
-   Horizontal bar chart
-   Donut/pie chart jika memang relevan
-   Scatter plot
-   Histogram
-   Heatmap
-   Interactive chart
-   Geographic visualization

Gunakan Plotly karena visualisasi dapat memiliki:

-   hover information
-   zoom
-   filtering/interaction
-   responsive behavior

------------------------------------------------------------------------

## Map / Geographic Visualization

Gunakan pendekatan yang kompatibel dengan Streamlit + Plotly.

Prioritas:

1.  Plotly Map / Mapbox-compatible visualization jika sesuai.
2.  GeoJSON Indonesia untuk provinsi/kabupaten jika diperlukan.
3.  Choropleth map untuk menunjukkan distribusi
    lowongan/kuota/pelamar/competition ratio.

Map harus bersifat **analytical**, bukan hanya dekorasi.

User sebaiknya dapat memilih metric:

-   Jumlah Lowongan
-   Total Kuota
-   Total Pelamar
-   Competition Ratio

------------------------------------------------------------------------

## Styling

Gunakan custom CSS melalui Streamlit untuk mendekati visual mockup.

Color palette utama:

``` text
Background / Off-white
#F2F0EF

Neutral Gray
#BBBDBC

Primary Teal
#245F73

Accent Brown
#733E24
```

Karakter desain:

-   Clean
-   Modern
-   Minimal
-   Professional
-   Data-oriented
-   Tidak terlalu mencolok
-   Banyak whitespace
-   Card-based layout
-   Typography sederhana dan mudah dibaca

Gunakan **horizontal top navigation**, bukan sidebar navigation.

------------------------------------------------------------------------

# 4. Website Architecture

Website terdiri dari **4 halaman utama**:

``` text
MagangHub Insight
│
├── 01. Home
├── 02. Interactive Dashboard
├── 03. Opportunity Explorer
└── 04. Methodology & About
```

Business Questions tidak harus menjadi satu halaman per BQ.

Business Questions adalah **kerangka analisis**, sedangkan halaman
website merupakan cara untuk menyajikan hasil analisis.

Tidak semua BQ harus masuk dashboard.

------------------------------------------------------------------------

# 5. Page 1 --- Home

## Purpose

Halaman Home berfungsi sebagai introduction/landing page.

User harus langsung memahami:

> Apa itu MagangHub Insight?
>
> Data apa yang digunakan?
>
> Apa yang dapat dilakukan di website ini?

------------------------------------------------------------------------

## Hero Section

Gunakan headline seperti:

> **MagangHub Insight**

Subheadline:

> **Understanding Internship Opportunities through Data**

Tambahkan konteks:

> Explore internship opportunities from MagangHub Batch 2 2026 through
> data, visualization, and interactive analysis.

CTA:

``` text
[ Explore Dashboard ]
[ Opportunity Explorer ]
```

------------------------------------------------------------------------

## About Project

Jelaskan secara singkat:

-   Dataset berasal dari MagangHub Batch 2 2026.
-   Project melakukan data cleaning dan exploratory data analysis.
-   Analisis berfokus pada lowongan, kuota, pelamar, program studi,
    lokasi, dan competition.
-   Website dibuat sebagai interactive data analytics product.

Jangan membuat section ini terlalu panjang.

------------------------------------------------------------------------

## What Can You Explore?

Buat beberapa card:

### Internship Landscape

Gambaran umum lowongan dan kuota.

### Program Study Demand

Program studi yang tercantum dalam lowongan.

### Geographic Distribution

Persebaran peluang berdasarkan wilayah.

### Competition

Perbandingan pelamar terhadap kuota.

### Opportunity Explorer

Eksplorasi lowongan berdasarkan kebutuhan user.

------------------------------------------------------------------------

## Creator Section

Di bagian akhir Home, tampilkan informasi pembuat:

``` text
Reza Irwansyah Aryanto
Alumni Universitas Teknologi Yogyakarta
Data Science
```

Tambahkan link:

-   GitHub
-   LinkedIn
-   Portfolio
-   CV

Gunakan icon/button yang sederhana.

------------------------------------------------------------------------

# 6. Page 2 --- Interactive Dashboard

## Purpose

Ini adalah halaman utama untuk menyajikan **hasil analisis**.

Dashboard harus bersifat curated.

Artinya:

> Jangan memasukkan seluruh BQ hanya karena BQ tersebut sudah dibuat.

Pilih BQ yang paling penting untuk storytelling dan visualisasi.

Dashboard harus menjawab:

> **"Apa yang ditemukan dari dataset MagangHub Batch 2 2026?"**

------------------------------------------------------------------------

# 7. Dashboard Structure

## Section A --- Overall Landscape

Tampilkan KPI utama.

Contoh:

``` text
Total Lowongan
Total Kuota
Total Pelamar
Competition Ratio
```

KPI harus dihitung langsung dari dataset, bukan hardcoded.

------------------------------------------------------------------------

## Section B --- Internship Overview

Analisis kemungkinan mencakup:

-   Jumlah lowongan berdasarkan jenis instansi jika tersedia.
-   Distribusi kuota.
-   Distribusi pelamar.
-   Distribusi hari kerja/hari libur jika relevan.
-   Distribusi jenjang jika relevan.

Jangan menampilkan chart yang tidak memberikan insight.

------------------------------------------------------------------------

# 8. Section C --- Program Study Analysis

Tampilkan:

### Top Program Studi

Contoh:

``` text
Manajemen
Ilmu Komunikasi
Akuntansi
Administrasi Bisnis
Sistem Informasi
...
```

Gunakan horizontal bar chart.

Data program studi berasal dari kolom `jurusan` yang dapat berisi banyak
program studi dalam satu lowongan.

Untuk analisis program studi, pertahankan kemampuan untuk menghitung:

> berapa banyak lowongan yang mencantumkan suatu program studi.

Hindari menghitung satu lowongan sebagai beberapa lowongan hanya karena
terdapat beberapa program studi di dalamnya.

------------------------------------------------------------------------

# 9. Section D --- Geographic Analysis

Tampilkan map Indonesia.

Metric yang dapat dipilih:

``` text
Jumlah Lowongan
Total Kuota
Total Pelamar
Competition Ratio
```

User dapat melihat wilayah mana yang memiliki:

-   jumlah lowongan tinggi
-   kuota tinggi
-   jumlah pelamar tinggi
-   competition ratio tinggi/rendah

Gunakan choropleth atau visualisasi geografis yang sesuai.

------------------------------------------------------------------------

# 10. Section E --- Competition Analysis

Tampilkan:

-   Distribution of Competition Ratio
-   Top/Bottom competition berdasarkan lokasi
-   Competition berdasarkan program studi jika relevan
-   Competition berdasarkan lowongan jika relevan

Definisi utama:

``` text
Competition Ratio = Total Applicants / Total Seats
```

Interpretasi:

> Nilai yang lebih tinggi berarti jumlah pelamar relatif lebih banyak
> dibandingkan kuota yang tersedia.

Jangan menyebut Competition Ratio sebagai probabilitas diterima.

------------------------------------------------------------------------

# 11. Section F --- Key Findings

Di bagian bawah dashboard, tampilkan beberapa insight utama dalam bentuk
text/card.

Contoh struktur:

``` text
Key Finding 01
Program studi dengan jumlah lowongan terbesar adalah ...

Key Finding 02
Wilayah dengan jumlah lowongan terbesar adalah ...

Key Finding 03
...

Key Finding 04
...
```

Insight harus dihasilkan berdasarkan data aktual.

Jangan membuat klaim yang tidak dapat didukung dataset.

------------------------------------------------------------------------

# 12. Business Questions vs Dashboard

Tidak semua Business Question harus ditampilkan.

Gunakan prinsip:

``` text
Business Questions
        ↓
EDA
        ↓
Identify important findings
        ↓
Select useful visualizations
        ↓
Interactive Dashboard
```

BQ yang kurang cocok menjadi visual utama dapat tetap:

-   digunakan dalam EDA
-   digunakan sebagai dasar insight
-   dimasukkan ke Opportunity Explorer
-   atau cukup didokumentasikan dalam methodology

Dashboard harus mengutamakan **clarity dan storytelling**, bukan jumlah
chart.

------------------------------------------------------------------------

# 13. Page 3 --- Opportunity Explorer

## Purpose

Opportunity Explorer berbeda dengan Dashboard.

Dashboard menjawab:

> **"Apa yang ditemukan dari data?"**

Opportunity Explorer menjawab:

> **"Apa yang dapat saya cari dari data?"**

Halaman ini harus menjadi interactive search/filter tool.

------------------------------------------------------------------------

# 14. Opportunity Explorer Filters

Sediakan filter:

## Keyword Search

User dapat mencari berdasarkan keyword.

Contoh:

``` text
data analyst
machine learning
marketing
finance
software
```

Keyword dapat diterapkan pada field yang relevan seperti:

-   posisi
-   instansi
-   jurusan
-   field lain yang tersedia

------------------------------------------------------------------------

## Program Studi

Dropdown/searchable multiselect.

Contoh:

``` text
Sains Data
Sistem Informasi
Informatika
Manajemen
Akuntansi
...
```

------------------------------------------------------------------------

## Province

Filter provinsi.

------------------------------------------------------------------------

## Kabupaten/Kota

Filter kabupaten/kota.

Kabupaten/kota harus mengikuti standardisasi location mapping yang telah
dilakukan pada data processing.

------------------------------------------------------------------------

## Competition Ratio

User dapat mencari berdasarkan:

-   lowest competition
-   highest competition
-   range tertentu

Contoh:

``` text
Lowest Competition Ratio
Highest Competition Ratio
Custom Range
```

------------------------------------------------------------------------

## Kuota

User dapat mencari:

-   kuota paling sedikit
-   kuota paling banyak
-   minimum kuota
-   maximum kuota

------------------------------------------------------------------------

## Applicants

Opsional jika relevan:

-   pelamar paling sedikit
-   pelamar paling banyak
-   custom range

------------------------------------------------------------------------

# 15. Opportunity Sorting

Sediakan sorting:

``` text
Competition Ratio — Lowest
Competition Ratio — Highest
Kuota — Highest
Kuota — Lowest
Pelamar — Highest
Pelamar — Lowest
```

------------------------------------------------------------------------

# 16. Opportunity Result

Tampilkan hasil dalam bentuk table/card.

Contoh:

``` text
PT ABC
Data Analyst

Jakarta Selatan

Kuota       2
Pelamar     14
Competition 7.0 applicants/seat

[ Detail ]
```

Jika data memiliki link lowongan asli, tampilkan tombol:

``` text
View Original Vacancy
```

Jangan membuat URL jika data sumber tidak tersedia.

------------------------------------------------------------------------

# 17. Opportunity Detail

Jika memungkinkan, ketika user memilih suatu lowongan, tampilkan:

-   Instansi
-   Posisi
-   Lokasi
-   Program studi
-   Jenjang
-   Kuota
-   Pelamar
-   Competition Ratio
-   Hari kerja
-   Hari libur
-   Link original listing

Detail harus berasal langsung dari dataset.

------------------------------------------------------------------------

# 18. Page 4 --- Methodology & About

Halaman ini menjelaskan bagaimana analisis dibuat.

Tujuan:

> Membuat project transparan dan reproducible.

------------------------------------------------------------------------

# 19. Data Source

Jelaskan:

``` text
Dataset:
MagangHub Batch 2 2026
```

Jelaskan:

-   unit analisis
-   field yang tersedia
-   periode/data batch
-   proses pengumpulan data jika memang terdokumentasi

------------------------------------------------------------------------

# 20. Data Processing

Jelaskan pipeline:

``` text
Raw Data
   ↓
Data Cleaning
   ↓
Standardization
   ↓
Location Mapping
   ↓
Program Study Processing
   ↓
Derived Metrics
   ↓
Analysis Dataset
```

Bahas proses penting seperti:

### Location Standardization

Contoh:

``` text
Kota Adm. Jakarta Selatan
        ↓
Jakarta Selatan
```

Kemudian mapping ke:

``` text
Kabupaten/Kota
        ↓
Provinsi
```

------------------------------------------------------------------------

## Program Study Processing

Jelaskan bahwa satu lowongan dapat memiliki banyak program studi.

Contoh:

``` text
Manajemen, Akuntansi, Sistem Informasi, ...
```

Untuk analisis program studi, program studi diproses agar dapat
dihitung:

> jumlah lowongan yang mencantumkan program studi tersebut.

Hindari salah interpretasi antara:

-   jumlah program studi yang tercantum
-   jumlah lowongan

------------------------------------------------------------------------

# 21. Formula & Metrics

## Competition Ratio

``` text
Competition Ratio =
Total Applicants / Total Seats
```

Contoh:

``` text
14 applicants
──────────────
2 seats

= 7.0 applicants / seat
```

Interpretasi:

> Secara deskriptif, terdapat sekitar 7 pelamar untuk setiap satu kuota.

Bukan:

> peluang diterima 1/7.

------------------------------------------------------------------------

# 22. MagangHub Opportunity Percentage

Jika field `peluang` pada data merupakan persentase yang ditampilkan
oleh MagangHub, dokumentasikan formula sesuai hasil reverse-checking
terhadap dataset.

Contoh kasus yang ditemukan:

``` text
Seats = 2
Existing Applicants = 8
Intended Application = 1
```

Nilai yang ditampilkan:

``` text
2 / (8 + 1) × 100%
= 22.22%
```

Jelaskan bahwa nilai tersebut merupakan **displayed opportunity
percentage berdasarkan mekanisme data/platform yang diamati**, bukan
probabilitas penerimaan seorang individu.

Jangan menyebutnya acceptance probability.

------------------------------------------------------------------------

# 23. Important Analytical Limitations

Tambahkan section:

## Limitations

Contoh:

-   Dataset hanya menggambarkan MagangHub Batch 2 2026.
-   Competition Ratio bukan acceptance rate.
-   Jumlah pelamar tidak sama dengan jumlah pelamar yang benar-benar
    mengikuti seluruh proses seleksi.
-   Tidak tersedia outcome penerimaan kandidat.
-   Tidak dapat digunakan untuk menyimpulkan probabilitas individu
    diterima.
-   Analisis menggambarkan kondisi batch tersebut dan tidak otomatis
    merepresentasikan batch berikutnya.
-   Jika suatu program studi tidak tercantum dalam lowongan, hal
    tersebut tidak berarti program studi tersebut tidak dapat diterima
    oleh perusahaan secara umum.

Bagian ini penting agar website tidak overclaim.

------------------------------------------------------------------------

# 24. Visual Design System

Gunakan style yang konsisten di semua halaman.

## Colors

``` css
--background: #F2F0EF;
--neutral: #BBBDBC;
--primary: #245F73;
--accent: #733E24;
```

Tambahan warna hanya jika diperlukan untuk semantic chart:

-   success
-   warning
-   danger
-   muted gray

Jangan menggunakan terlalu banyak warna.

------------------------------------------------------------------------

## Layout

Gunakan:

-   horizontal top navigation
-   max-width content
-   responsive grid
-   card
-   rounded corners secukupnya
-   subtle border
-   subtle shadow
-   whitespace yang cukup

Jangan membuat UI terlalu ramai.

------------------------------------------------------------------------

# 25. Suggested Streamlit Project Structure

Gunakan struktur modular.

``` text
maganghub-insight/
│
├── app.py
│
├── pages/
│   ├── 01_Home.py
│   ├── 02_Dashboard.py
│   ├── 03_Opportunity_Explorer.py
│   └── 04_Methodology.py
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── data_processing.py
│   ├── metrics.py
│   ├── filters.py
│   ├── analysis.py
│   ├── charts.py
│   └── styles.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── assets/
│   ├── logo/
│   └── images/
│
├── .streamlit/
│   └── config.toml
│
├── requirements.txt
├── README.md
└── idea.md
```

------------------------------------------------------------------------

# 26. Responsibility of Each Python Module

## `data_loader.py`

Bertanggung jawab untuk:

-   membaca dataset
-   caching data
-   memastikan dataset tersedia

Gunakan Streamlit caching seperti `st.cache_data` jika sesuai.

------------------------------------------------------------------------

## `data_processing.py`

Bertanggung jawab untuk:

-   cleaning
-   standardization
-   transformation
-   location mapping
-   program-study processing

------------------------------------------------------------------------

## `metrics.py`

Bertanggung jawab untuk metric:

``` text
total vacancies
total seats
total applicants
competition ratio
opportunity percentage
```

Jangan menghitung metric yang sama berulang kali di setiap page.

------------------------------------------------------------------------

## `filters.py`

Bertanggung jawab untuk:

-   keyword filtering
-   program study filtering
-   province filtering
-   city filtering
-   competition filtering
-   quota filtering
-   applicant filtering

------------------------------------------------------------------------

## `analysis.py`

Bertanggung jawab untuk agregasi:

-   top program study
-   location analysis
-   institution analysis
-   competition analysis
-   distribution analysis

------------------------------------------------------------------------

## `charts.py`

Berisi reusable Plotly chart functions.

Contoh:

``` python
plot_top_program_studies()
plot_competition_distribution()
plot_location_choropleth()
plot_quota_distribution()
plot_applicant_distribution()
```

------------------------------------------------------------------------

## `styles.py`

Berisi custom CSS dan styling Streamlit.

Tujuannya agar seluruh halaman menggunakan design system yang sama.

------------------------------------------------------------------------

# 27. Important Development Principle

Jangan langsung membuat semua fitur.

Gunakan tahap:

``` text
PHASE 1
Data finalization
        ↓
PHASE 2
Dashboard
        ↓
PHASE 3
Opportunity Explorer
        ↓
PHASE 4
Methodology
        ↓
PHASE 5
UI refinement
        ↓
PHASE 6
Deployment
```

------------------------------------------------------------------------

# 28. Phase 1 --- Data Finalization

Pastikan:

-   data_lowongan sudah bersih
-   location mapping selesai
-   province mapping selesai
-   program study processing selesai
-   metric dasar sudah tervalidasi
-   duplicate sudah diperiksa
-   missing value sudah ditangani
-   derived columns sudah final

Jangan mulai membuat banyak chart sebelum struktur data final.

------------------------------------------------------------------------

# 29. Phase 2 --- Dashboard

Implementasikan:

1.  Page layout
2.  KPI
3.  Overview charts
4.  Program study analysis
5.  Geographic visualization
6.  Competition analysis
7.  Key findings

Pastikan seluruh angka berasal dari dataset.

Tidak boleh hardcode angka analisis final.

------------------------------------------------------------------------

# 30. Phase 3 --- Opportunity Explorer

Implementasikan:

1.  keyword search
2.  program study filter
3.  province filter
4.  city filter
5.  competition filter
6.  quota filter
7.  applicant filter
8.  sorting
9.  result table
10. detail view

------------------------------------------------------------------------

# 31. Phase 4 --- Methodology

Implementasikan:

-   data source
-   data pipeline
-   cleaning explanation
-   location mapping
-   program study handling
-   metric formulas
-   competition ratio
-   opportunity percentage
-   limitations

------------------------------------------------------------------------

# 32. Phase 5 --- UI Refinement

Gunakan HTML mockup yang sudah dibuat sebagai **visual reference**.

Target visual:

``` text
Professional
        +
Minimal
        +
Data-focused
        +
Interactive
        +
Portfolio-ready
```

Jangan mengubah project menjadi frontend-heavy.

Prioritas tetap:

> **Data quality → Analysis quality → UX → Visual polish**

------------------------------------------------------------------------

# 33. Phase 6 --- Deployment

Target akhir adalah website yang dapat diakses secara online.

Deployment strategy dapat menggunakan platform yang mendukung Streamlit.

Pastikan:

-   requirements.txt tersedia
-   data processed tersedia
-   aplikasi dapat dijalankan dari clean environment
-   tidak bergantung pada absolute local path
-   secret/API key tidak dimasukkan ke repository
-   README menjelaskan cara menjalankan project

------------------------------------------------------------------------

# 34. Future AI Integration

AI **bukan bagian wajib dari MVP**.

Namun arsitektur project harus memungkinkan AI ditambahkan kemudian.

Potensi fitur:

``` text
Ask MagangHub Insight

"Program studi Sains Data,
wilayah mana yang memiliki
lowongan paling banyak?"
```

AI kemudian menggunakan hasil analytics/data yang sudah tersedia untuk
memberikan jawaban.

Contoh lain:

``` text
"Carikan lowongan dengan
competition ratio paling rendah
untuk Sains Data di Jakarta."
```

AI sebaiknya menjadi **natural-language interface terhadap analytics**,
bukan menggantikan proses analisis.

Urutan pengembangan:

``` text
Data
 ↓
Analytics
 ↓
Interactive Explorer
 ↓
AI Assistant
```

Jangan membangun AI terlebih dahulu.

------------------------------------------------------------------------

# 35. Product Philosophy

MagangHub Insight harus menjawab tiga pertanyaan utama:

### 1. What happened?

Dijawab oleh:

**Interactive Dashboard**

------------------------------------------------------------------------

### 2. What can I find?

Dijawab oleh:

**Opportunity Explorer**

------------------------------------------------------------------------

### 3. How was it calculated?

Dijawab oleh:

**Methodology**

------------------------------------------------------------------------

# 36. Final Product Structure

``` text
┌─────────────────────────────────────────────────────────────┐
│ MAGANGHUB INSIGHT                                           │
│                                                             │
│ Home | Dashboard | Opportunity Explorer | Methodology       │
└─────────────────────────────────────────────────────────────┘

HOME
│
├── Project Introduction
├── What Can You Explore?
└── About Creator
        │
        ▼
DASHBOARD
│
├── KPI
├── Overall Landscape
├── Program Study
├── Geographic Analysis
├── Competition
└── Key Findings
        │
        ▼
OPPORTUNITY EXPLORER
│
├── Keyword
├── Program Study
├── Province
├── Kabupaten/Kota
├── Competition
├── Quota
├── Applicants
├── Sorting
└── Opportunity Detail
        │
        ▼
METHODOLOGY
│
├── Data Source
├── Data Processing
├── Location Mapping
├── Program Study Processing
├── Formula
├── Competition Ratio
├── Opportunity Percentage
└── Limitations
```

------------------------------------------------------------------------

# 37. Instructions for Claude Code

When implementing this project:

1.  **Do not immediately rewrite the entire project.**
2.  First inspect the existing repository and dataset structure.
3.  Understand the existing cleaned data and analysis code.
4.  Reuse existing data-processing logic where possible.
5.  Do not create fake/fictitious final analytical results.
6.  Any number displayed in the actual application must come from the
    dataset or a clearly derived metric.
7.  Use the HTML mockup as a **visual reference**, not as the source of
    analytical values.
8.  Keep business logic separate from UI code.
9.  Use reusable functions.
10. Avoid duplicated filtering/metric logic across pages.
11. Make the application responsive.
12. Keep the design consistent across all four pages.
13. Prioritize correctness of data and calculations over visual effects.
14. Do not add AI functionality until the core analytics application is
    stable.
15. Before adding a new feature, check whether it supports one of the
    four main product goals:
    -   understanding the dataset
    -   exploring opportunities
    -   explaining methodology
    -   presenting the project/creator

The final application should feel like a **professional Data Science
portfolio project and an interactive analytics product**, while
remaining technically maintainable and faithful to the MagangHub Batch 2
2026 dataset.
