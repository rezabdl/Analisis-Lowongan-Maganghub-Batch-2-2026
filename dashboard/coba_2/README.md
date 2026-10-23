# MagangHub Analytics — Dashboard V2 (coba_2)

Dashboard analitik interaktif **MagangHub Batch 2 2026** yang dirancang ulang berdasarkan standar **`ngulikdata.com`** dan dokumen spesifikasi proyek pada [`docs/instruction`](file:///D:/Developments/Riset%20Pribadi/Maganghub/docs/instruction).

---

## Cara Menjalankan

Dari direktori root proyek `Maganghub`:

```bash
# Menjalankan dengan environment virtual proyek
.venv\Scripts\streamlit.exe run dashboard\coba_2\app.py

# Atau jika virtual environment sudah aktif di terminal
streamlit run dashboard\coba_2\app.py
```

Dashboard akan otomatis terbuka di browser pada alamat `http://localhost:8501`.

---

## Ringkasan Perubahan Sesuai Permintaan & Instruksi Proyek

### 1. Peta Interaktif (Peta Choropleth Heatmap 38 Provinsi)
- Ditempatkan pada tab **Distribusi Wilayah & Peta**.
- Menggunakan geometri resmi `38 Provinsi Indonesia - Provinsi.json` yang dicocokkan 100% dengan dataset.
- Dilengkapi **Pilihan Metrik Peta**:
  - **Rasio Persaingan (Pelamar / Kuota)** — visualisasi densitas persaingan dari skala warna amber hingga merah.
  - **Jumlah Lowongan** — skala warna gradien teal.
  - **Total Kuota Kursi** — skala warna gradien biru.
  - **Total Pelamar** — skala warna gradien oranye/amber.
- Hover tooltip menyajikan detail lengkap tiap provinsi (*Nama Provinsi, Jumlah Lowongan, Total Kuota, Total Pelamar, dan Rasio Persaingan*).
- Disertai tabel agregasi perbandingan wilayah **Pulau Jawa vs Luar Jawa** dan diagram batang **Top 15 Provinsi**.

### 2. Bebas Ikon & Emoji (Zero Emojis/Icons)
- Mengikuti arahan pengguna dan panduan `06_UI_UX_DESIGN_SYSTEM.md`: seluruh ikon dan emoji dihilangkan dari antarmuka, kartu KPI, legenda, badge, dan visualisasi grafik.
- Mengedepankan **tipografi berbasis Inter** yang bersih, teratur, dan profesional seperti referensi `ngulikdata.com`.

### 3. Mengatasi Kesan Kosong & Kurang Menarik (High Information Density)
- **Sticky Top Navbar**: Menyajikan identitas platform, edisi batch, dan status pill agregat (Lowongan, Kuota, Pelamar, Rasio Agregat).
- **6 Kotak KPI Utama**: Sesuai formula BQ1 & BQ2 (Total Lowongan, Total Kuota, Total Pelamar, Rata-rata Kuota per Lowongan [2,13], Rata-rata Pelamar [18,59], dan Rasio Agregat [8,74x]).
- **3 Strategic Takeaway Strip**: Memberikan konteks analitis instan (Disparitas Spasial Jawa vs Luar Jawa, Rasio Agregat Nasional, dan Aksesibilitas Multidisiplin).
- **Struktur Kartu Panel Berdampingan**: Setiap visualisasi didampingi kotak penjelasan (*Callout Box*) interpretasi bisnis dan catatan metodologi.

### 4. Implementasi Sesuai Dokumen Spesifikasi (`docs/instruction`)
- **BQ1 & BQ2**: Karakteristik umum dan tingkat persaingan agregat.
- **BQ4 & BQ5**: Distribusi spasial dan peta persaingan per wilayah.
- **BQ8**: Kualifikasi jenjang pendidikan (Sarjana, Diploma, Profesi) dan Top 20 Jurusan paling sering disyaratkan.
- **BQ9**: Hubungan kuota vs pelamar melalui *Scatter Plot* (Pearson $r = 0,743$) dan Analisis 4 Kuadran (*Median Kuota = 1, Median Pelamar = 12*).
- **BQ10**: Distribusi hari kerja per minggu (5 hari [77%] vs 6 hari [23%]).
- **Batasan Metodologi**: Secara transparan menyatakan bahwa BQ3 (Pemerintah vs Swasta) dan kategorisasi posisi IT/Data dikecualikan karena belum ada pemetaan tervalidasi.
