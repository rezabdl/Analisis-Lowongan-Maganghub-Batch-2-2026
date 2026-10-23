# MagangHub Analytics — Batch 2 2026

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io/cloud)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Plotly](https://img.shields.io/badge/Plotly-5.20%2B-3F4F75?logo=plotly&logoColor=white)](https://plotly.com/)

Platform analitik dan data storytelling interaktif untuk mengeksplorasi karakteristik lowongan, daya tampung kuota, antusiasme pelamar, dan dinamika persaingan pada program **MagangHub Kemnaker Batch 2 2026**.

> **Filosofi Analisis:** *"From Opportunity to Competition"* — Di balik puluhan ribu kursi magang yang dipublikasikan secara terbuka, tersimpan dinamika struktural ketat: konsentrasi spasial di Pulau Jawa, disparitas peminat antar-daerah, serta fenomena di mana kuota besar justru menarik lonjakan pendaftar eksponensial.

---

## 🌐 Demo Aplikasi Langsung

Aplikasi dapat diakses secara langsung di browser:
- 🔗 **Live Web Dashboard:** `https://<username-anda>-maganghub.streamlit.app` *(sesuaikan setelah deploy ke Streamlit Cloud)*

---

## 🎯 Gambaran Utama Proyek

Dataset ini merupakan snapshot resmi dari portal MagangHub Kemnaker Batch 2 2026 yang telah melalui tahapan *Data Extraction, Data Cleaning, Aggregation,* dan *Exploratory Data Analysis (EDA)*.

| Metrik Kunci | Nilai | Definisi & Formula |
| :--- | :--- | :--- |
| **Total Lowongan** | **22.477** | Unit observasi lowongan unik terdata |
| **Total Kuota Kursi** | **47.813** | Akumulasi kapasitas daya tampung penempatan |
| **Total Pelamar** | **417.793** | Total pendaftar tercatat di seluruh sistem |
| **Rata-rata Kuota / Lowongan** | **2,13 kursi** | Daya tampung rata-rata tiap posisi |
| **Rata-rata Pelamar / Lowongan** | **18,59 pelamar** | Peminat rata-rata tiap posisi |
| **Rasio Persaingan Agregat** | **8,74x** | `Total Pelamar / Total Kuota` (Median per posisi: **8,0x**) |
| **Korelasi Kuota vs Pelamar** | **r = 0,743** | Koefisien Pearson (korelasi positif kuat) |

---

## 🚀 Fitur & Halaman Dashboard

Dashboard disusun dalam **6 tab analitis terstruktur** yang dapat diakses melalui **Sticky Top Navbar**:

### 1. Ringkasan Ekosistem (BQ1 & BQ2)
- **Bento KPI Grid (6 Kartu Metrik)**: Total lowongan, kuota, pelamar, rata-rata kuota, rata-rata pelamar, dan rasio kompetisi agregat.
- **3 Strategic Takeaway Strip**: Intisari disparitas Jawa vs Luar Jawa, rasio agregat nasional, dan aksesibilitas kualifikasi.
- **Distribusi Kelompok Kuota**: Visualisasi kuota 1 kursi (62%), 2-3 kursi, 4-5 kursi, 6-10 kursi, dan >10 kursi.
- **Proporsi Kategori Peluang Platform**: Pemetaan label bawaan platform (*Peluang Sangat Besar s.d. Peluang Kecil*).

### 2. Distribusi Wilayah & Peta (BQ4 & BQ5)
- **Peta Interaktif Choropleth Heatmap 38 Provinsi**: Terintegrasi dengan GeoJSON resmi Indonesia. Mendukung pergantian metrik langsung:
  - *Rasio Persaingan (Pelamar / Kuota)* — Skala warna amber ke merah.
  - *Jumlah Lowongan* — Skala warna teal.
  - *Total Kuota Kursi* — Skala warna biru.
  - *Total Pelamar* — Skala warna oranye.
- **Komparasi Spasial Agregat**: Perbandingan Pulau Jawa (70,6% lowongan) vs Luar Jawa (29,4% lowongan).
- **Top 15 Provinsi**: Diagram batang terkelompok membandingkan Kuota vs Pelamar.

### 3. Persaingan & Kuota (BQ2 & BQ9)
- **Scatter Plot Kuota vs Pelamar**: Garis tren OLS dengan koefisien korelasi Pearson $r = 0,743$.
- **Analisis 4 Kuadran (Median Kuota = 1, Median Pelamar = 12)**:
  - *Kuadran I (Kompetisi Masif):* Kuota tinggi, pelamar tinggi.
  - *Kuadran II (Paling Ketat):* Kuota rendah, pelamar tinggi (*Red Ocean*).
  - *Kuadran III (Terbatas):* Kuota rendah, pelamar rendah (*Niche*).
  - *Kuadran IV (Peluang Terbaik):* Kuota tinggi, pelamar rendah (*Hidden Opportunity*).
- **Histogram Sebaran Rasio**: Sebaran rasio kompetisi per lowongan.

### 4. Persyaratan & Jurusan (BQ8 & BQ10)
- **Kualifikasi Jenjang Pendidikan**: Sarjana/D4 (92,6%), Diploma/D1-D3 (55,6%), dan Profesi (10,7%).
- **Distribusi Hari Kerja**: Skema 5 hari kerja (77,0%) vs 6 hari kerja (23,0%).
- **Top 20 Jurusan Paling Dicari**: Pemeringkatan program studi yang paling sering disyaratkan oleh instansi.

### 5. Penelusuran Lowongan (Opportunity Explorer)
- Mesin pencari kata kunci live (*Posisi, Instansi, atau Jurusan*).
- Pengurutan data fleksibel (*Rasio Terendah / Rasio Tertinggi / Kuota Terbanyak / Pelamar Terbanyak*).
- Tabel data responsif dengan pemilihan kolom dan tombol **Unduh Hasil Pencarian (CSV)**.

### 6. Metodologi & Batasan Analisis
- Dokumentasi rumus matematis dan sumber unit observasi.
- **Pengecualian Tervalidasi**: Secara transparan mendokumentasikan bahwa analisis BQ3 (*Pemerintah vs Swasta*) dan pengelompokan posisi IT/Data dikecualikan karena belum ada taksonomi yang tervalidasi resmi dalam dataset.

---

## 🎨 Desain & Filosofi Antarmuka (UI/UX)

Mengadopsi kaidah desain editorial data journalism terinspirasi dari standar **`ngulikdata.com`** dan dokumen spesifikasi `06_UI_UX_DESIGN_SYSTEM.md`:
- **Bebas Ikon & Emoji (Zero Emojis/Icons)**: Menjaga fokus pengguna pada kejernihan angka dan informasi analitis tanpa distraksi visual dekoratif.
- **Aturan 80/20 Palet Warna**: 80% area berupa warna netral (latar canvas off-white `#FAF9F6`, kartu putih murni `#FFFFFF`, garis border tipis `#DCE5E8`, dan teks utama `#17324D`).
- **Aksen Terarah**: Warna aksen Teal (`#167C80`), Biru (`#3977B8`), Amber (`#C38A2E`), dan Merah (`#BD5B61`) hanya disematkan pada data penting yang memerlukan penekanan.
- **Tipografi Bersih**: Menggunakan font **Inter** untuk keterbacaan teks yang optimal dan **JetBrains Mono** untuk angka numerik.

---

## 💻 Panduan Menjalankan Secara Lokal

### Prasyarat
- Python 3.10 atau versi yang lebih baru
- Git

### Langkah Instalasi
```bash
# 1. Clone repositori ini
git clone https://github.com/rezabdl/Analisis-Lowongan-Maganghub-Batch-2-2026.git
cd maganghub

# 2. Buat dan aktifkan virtual environment (opsional tetapi disarankan)
python -m venv .venv

# Untuk Windows:
.venv\Scripts\activate
# Untuk macOS/Linux:
source .venv/bin/activate

# 3. Install dependensi proyek
pip install -r requirements.txt

# 4. Jalankan aplikasi Streamlit
streamlit run app.py
```
Aplikasi akan otomatis terbuka pada peramban web di alamat: `http://localhost:<port anda>`.

---

## ☁️ Panduan Deploy Gratis ke Streamlit Community Cloud

Aplikasi ini siap dideploy secara instan ke [Streamlit Community Cloud](https://streamlit.io/cloud):

1. **Push Proyek ke GitHub**:
   - Pastikan seluruh file proyek (kecuali folder `.venv` dan file pada `.gitignore`) sudah ter-push ke repositori GitHub Anda.
2. **Masuk ke Streamlit Cloud**:
   - Kunjungi [share.streamlit.io](https://share.streamlit.io/) dan login menggunakan akun GitHub Anda.
3. **Buat Aplikasi Baru (*New App*)**:
   - Klik tombol **"Create app"** > **"Deploy a public app from GitHub"**.
   - **Repository:** Pilih repositori Anda (contoh: `<username>/maganghub`).
   - **Branch:** `main` (atau `master`).
   - **Main file path:** `app.py`.
4. **Deploy**:
   - Klik **"Deploy!"**.
   - Streamlit Cloud akan membaca `requirements.txt` dan meluncurkan dashboard secara publik dalam beberapa menit.

---

## 📂 Struktur Direktori Repositori

```text
maganghub/
├── app.py                      # Main entrypoint Streamlit (root)
├── requirements.txt            # Dependensi library Python (UTF-8)
├── .gitignore                  # Berkas pengecualian Git
├── README.md                   # Dokumentasi proyek lengkap
├── dashboard/
│   └── coba_2/
│       ├── app.py              # Dashboard arsitektur modern minimalis
│       └── README.md           # Catatan spesifikasi v2
├── data/
│   ├── geojson/
│   │   └── GeoJson-Indonesia-38-Provinsi/
│   │       └── Provinsi/
│   │           └── 38 Provinsi Indonesia - Provinsi.json # Geometri peta 38 provinsi
│   └── processed/
│       └── data_lowongan/
│           └── data_eda.csv    # Dataset final yang telah dibersihkan (22.477 baris)
└── docs/
    └── instruction/            # Dokumen spesifikasi dan aturan analisis
```

---

## 🛠️ Tech Stack & Library

- **Bahasa Pemrograman:** Python 3.10+
- **Framework Dashboard:** [Streamlit](https://streamlit.io/)
- **Manipulasi & Agregasi Data:** [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/)
- **Visualisasi Data Interaktif:** [Plotly Express & Graph Objects](https://plotly.com/python/)
- **Analisis Regresi & Tren:** [Statsmodels](https://www.statsmodels.org/)
- **Geospasial:** GeoJSON 38 Provinsi Indonesia

---

## 👤 Profil Penulis & Atribusi

**Reza Irwansyah Aryanto**  
*Data Science & Analytics*

- 💼 **LinkedIn:** [linkedin.com/in/reza-irwansyah-aryanto-0b1483274](https://www.linkedin.com/in/reza-irwansyah-aryanto-0b1483274)
- 🐙 **GitHub:** [github.com/rezabdl](https://github.com/rezabdl)

---

## 📄 Lisensi & Pernyataan Batasan

Proyek ini dirilis di bawah lisensi [MIT License](LICENSE). Seluruh data bersumber dari publikasi resmi platform MagangHub Kemnaker. Analisis ini bersifat independen, deskriptif, dan ditujukan untuk tujuan edukasi serta eksplorasi data.
