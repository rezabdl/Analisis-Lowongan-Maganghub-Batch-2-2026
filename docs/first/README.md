# Analisis Data & Dashboard MagangHub Batch 2 2026

## 1. Latar Belakang

MagangHub adalah platform yang menampilkan lowongan program magang (termasuk program magang bersertifikat/nasional) dari berbagai instansi pemerintah maupun perusahaan swasta di Indonesia. Setiap lowongan memuat informasi seperti nama posisi, instansi penyelenggara, jurusan yang dapat mendaftar, lokasi (kabupaten/kota, provinsi), jenjang pendidikan yang dipersyaratkan, jadwal kerja (hari/minggu), kuota peserta, jumlah pelamar, serta indikator "peluang" yang ditampilkan platform.

Proyek ini bertujuan untuk melakukan **eksplorasi dan analisis data (EDA)** terhadap data lowongan MagangHub Batch 2 2026, kemudian menyusun **dashboard interaktif** yang dapat digunakan untuk memahami karakteristik lowongan, tingkat persaingan, serta distribusi peluang magang berdasarkan wilayah, instansi, posisi, dan jurusan.

## 2. Tujuan Proyek

- Memahami karakteristik umum dan skala lowongan magang pada Batch 2 2026.
- Mengukur tingkat persaingan (competition ratio) antar-lowongan, wilayah, posisi, dan jenjang pendidikan.
- Membandingkan karakteristik lowongan antara instansi pemerintah dan swasta.
- Mengidentifikasi distribusi geografis lowongan dan pelamar.
- Mengidentifikasi posisi dan jurusan dengan akses peluang magang paling luas.
- Menyajikan seluruh temuan dalam bentuk dashboard yang mudah dipahami oleh pengguna non-teknis.

## 3. Ruang Lingkup Data

Data bersumber dari halaman lowongan MagangHub, dengan atribut utama (hasil parsing) sebagai berikut:

| Kolom              | Deskripsi                                                       |
| ------------------ | ---------------------------------------------------------------- |
| `posisi`           | Nama posisi/lowongan magang                                     |
| `instansi`         | Nama instansi/organisasi penyelenggara                          |
| `jenis_instansi`   | Pemerintah / Swasta (diturunkan dari nama instansi)              |
| `jurusan_1..n`     | Daftar jurusan yang dapat mendaftar pada lowongan tersebut       |
| `lokasi_kabupaten` | Kabupaten/kota lokasi penempatan                                 |
| `lokasi_provinsi`  | Provinsi lokasi penempatan                                       |
| `jenjang`          | Jenjang pendidikan yang dipersyaratkan (Diploma/Sarjana/Kombinasi) |
| `hari_kerja`       | Jumlah hari kerja per minggu                                     |
| `hari_libur`       | Hari libur yang berlaku                                          |
| `kuota`            | Jumlah kuota peserta                                             |
| `pelamar`          | Jumlah pelamar tercatat                                          |
| `label_peluang`    | Kategori peluang yang ditampilkan platform (mis. "Peluang Besar") |
| `persen_peluang`   | Persentase peluang yang ditampilkan platform                     |
| `url_lowongan`     | Tautan menuju detail lowongan                                    |

> Catatan: struktur kolom final mengikuti hasil proses *data cleaning* dan *parsing* dari data mentah (HTML/CSV export).

## 4. Business Questions

Business questions berikut disusun untuk mengarahkan proses EDA agar tetap fokus pada kebutuhan analisis dan dashboard.

| ID    | Business Question                                                             | Fokus Analisis            |
| ----- | ------------------------------------------------------------------------------ | -------------------------- |
| BQ1   | Bagaimana karakteristik umum lowongan MagangHub Batch 2 2026?                  | Overview                   |
| BQ2   | Seberapa tinggi tingkat persaingan lowongan?                                   | Competition                |
| BQ3   | Bagaimana perbandingan instansi pemerintah dan swasta?                         | Institution                |
| BQ4   | Wilayah mana yang memiliki lowongan dan pelamar paling tinggi?                 | Geographic                 |
| BQ5   | Wilayah mana yang memiliki tingkat persaingan paling tinggi?                   | Geographic & Competition   |
| BQ6   | Posisi apa yang memiliki peluang dan peminat paling besar?                    | Position                   |
| BQ7   | Jurusan apa yang memiliki akses peluang magang paling luas?                   | Major                      |
| BQ8   | Bagaimana distribusi lowongan berdasarkan jenjang pendidikan?                 | Education                  |
| BQ9   | Bagaimana hubungan antara kuota dan jumlah pelamar?                           | Supply & Demand            |
| BQ10* | Bagaimana pola jadwal kerja (hari kerja/minggu) pada lowongan magang?         | Work Schedule              |
| BQ11* | Bagaimana distribusi kategori "peluang" dan konsistensinya dengan competition ratio aktual? | Opportunity Label Validation |
| BQ12* | Instansi/organizer mana yang membuka lowongan magang terbanyak?               | Institution (Top-N)        |
| BQ13* | Apakah jumlah jurusan yang diterima berkorelasi dengan tingkat persaingan?    | Major & Competition        |
| BQ14* | Bagaimana korelasi antara jenjang pendidikan dan competition ratio?           | Education & Competition    |

`*` = pertanyaan tambahan (opsional, dapat disesuaikan sesuai kebutuhan/waktu pengerjaan).

## 5. Metodologi

1. **Data Collection** — pengumpulan data lowongan dari MagangHub (scraping/export).
2. **Data Cleaning & Preparation** — parsing HTML/teks menjadi struktur tabular, penanganan missing value, normalisasi nama wilayah dan jurusan, transformasi kolom jurusan menjadi format long (satu baris per jurusan per lowongan) untuk kebutuhan BQ7 & BQ13.
3. **Exploratory Data Analysis (EDA)** — menjawab BQ1–BQ9 (dan BQ10–BQ14 bila digunakan) menggunakan statistik deskriptif dan visualisasi (bar chart, histogram, scatter plot, peta choropleth).
4. **Dashboard Development** — menyusun dashboard interaktif berdasarkan hasil EDA.
5. **Validation & Review** — memastikan hasil analisis konsisten dan interpretasi tidak menyimpulkan sebab-akibat di luar lingkup data deskriptif.

## 6. Struktur Proyek (usulan)

```
magang-hub-batch2-2026/
├── data/
│   ├── raw/                # data mentah hasil scraping/export
│   └── processed/          # data hasil cleaning, siap dianalisis
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda_overview.ipynb
│   ├── 03_eda_competition.ipynb
│   ├── 04_eda_geographic.ipynb
│   ├── 05_eda_position_major_education.ipynb
│   └── 06_eda_supply_demand.ipynb
├── dashboard/
│   └── app.py               # atau file dashboard (Streamlit/Looker Studio/Power BI, dsb.)
├── docs/
│   ├── business_questions.md
│   └── README.md            # dokumen ini
└── requirements.txt
```

## 7. Luaran Proyek (Output)

1. Dataset bersih (`processed`) yang siap digunakan untuk analisis lanjutan.
2. Notebook EDA yang menjawab seluruh business questions.
3. **Dashboard MagangHub Batch 2 2026**, mencakup minimal:
   - Ringkasan umum (total lowongan, total kuota, total pelamar, rata-rata competition ratio).
   - Peta/visualisasi distribusi lowongan & pelamar per provinsi/kabupaten.
   - Perbandingan instansi pemerintah vs swasta.
   - Top posisi & top jurusan berdasarkan jumlah lowongan dan pelamar.
   - Distribusi jenjang pendidikan.
   - Scatter plot hubungan kuota vs pelamar.
4. Dokumentasi insight dan rekomendasi (bersifat deskriptif, bukan kesimpulan sebab-akibat).

## 8. Batasan (Limitations)

- `Competition Ratio` merupakan indikator jumlah pelamar relatif terhadap kuota, **bukan** probabilitas diterima.
- Analisis jurusan menggambarkan ketersediaan lowongan yang mencantumkan jurusan tersebut sebagai syarat, bukan jumlah pelamar aktual dari jurusan tersebut.
- Perbandingan instansi pemerintah vs swasta bersifat deskriptif, tidak digunakan untuk menyimpulkan superioritas salah satu jenis instansi.
- Hubungan kuota vs pelamar (BQ9) bersifat eksploratif, tidak menyiratkan hubungan sebab-akibat.