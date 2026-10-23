"10_STREAMLIT_IMPLEMENTATION_GUIDE.md": r"""# 10 — Streamlit Implementation Guide

## 1. Tujuan

Dokumen ini memberi arahan implementasi aplikasi dashboard menggunakan Streamlit. Struktur kode harus memisahkan pemuatan data, transformasi, metrik, visualisasi, dan antarmuka agar mudah diuji dan dirawat.

## 2. Struktur Proyek yang Disarankan

```text
Maganghub/
├── .venv/
├── .agents/
├──
├── pages/
│   ├── 1_Beranda.py
│   ├── 2_Dashboard.py
│   ├── 3_Opportunity_Explorer.py
│   └── 4_Metodologi.py
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── metrics.py
│   ├── charts.py
│   └── filters.py
├── data/
├── ├── geojson/
├── ├── └── GeoJson-Indonesia-38-Provinsi/
│   ├── raw/
├── ├   └── data_lowongan/
├── ├   └──data_provinsi/
│   └── processed/
│   │   └── data_lowongan/
├── ├   └──data_provinsi/
├── docs/
│   ├── 01_PROJECT_OVERVIEW.md
│   ├── 02_BUSINESS_QUESTIONS.md
│   ├── 03_DATA_DICTIONARY.md
│   ├── 04_DATA_PREPARATION.md
│   ├── 05_METRIC_DEFINITIONS.md
│   ├── 06_UI_UX_DESIGN_SYSTEM.md
│   ├── 07_PAGE_SPECIFICATIONS.md
│   ├── 08_INTERACTION_AND_FILTER_SPEC.md
│   ├── 09_CHARTS_AND_VISUALIZATION_SPEC.md
│   └── 10_STREAMLIT_IMPLEMENTATION_GUIDE.md
└── requirements.txt
```

Sesuaikan struktur ini dengan repository yang sudah ada; jangan memindahkan atau menggandakan data mentah tanpa kebutuhan. tulis kembali struktur ini untuk mempermudah dalam mengidentifikasi kedepannya

## 3. Dependensi

Pilih dependensi sesuai implementasi aktual. Kandidat yang umum:
- `streamlit` untuk antarmuka.
- `pandas` untuk pengolahan data.
- `plotly` untuk grafik interaktif.
- `geopandas` atau library peta lain jika diperlukan untuk data geografis.

Jangan menambahkan dependensi yang tidak digunakan. Catat versi yang diuji dalam `requirements.txt`.

## 4. Pemuatan Data

Buat fungsi khusus untuk membaca dataset final. Contoh pola:

```python
from pathlib import Path
import pandas as pd
import streamlit as st

DATA_PATH = Path("data/processed/data_eda.csv")

@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df

df = load_data(str(DATA_PATH))
```

Pastikan path sesuai dengan lokasi file yang benar. Validasi kolom wajib dan tampilkan pesan kesalahan yang dapat dipahami jika file tidak ditemukan atau skemanya berubah.

## 5. Validasi Dataset

Sebelum membuat KPI atau grafik:
- Periksa kolom wajib.
- Periksa jumlah baris dan kolom.
- Periksa tipe data metrik numerik.
- Periksa nilai kosong pada kolom penting.
- Periksa duplikasi sesuai definisi unit observasi.
- Pastikan satu baris pada tabel utama tetap mewakili satu lowongan.
- Jangan menyimpulkan bahwa duplikat adalah kesalahan sebelum aturan deduplikasi ditetapkan.

Contoh validasi ringan:

```python
REQUIRED_COLUMNS = {
    "posisi", "instansi", "lokasi", "kuota", "pelamar"
}

missing_columns = REQUIRED_COLUMNS.difference(df.columns)
if missing_columns:
    st.error(
        "Kolom wajib tidak ditemukan: "
        + ", ".join(sorted(missing_columns))
    )
    st.stop()
```

Sesuaikan daftar kolom dengan dataset final; contoh di atas bukan pengganti validasi skema yang lengkap.

## 6. Fungsi Metrik

Letakkan rumus metrik di `src/metrics.py`, bukan menulis ulang rumus berbeda pada tiap halaman.

Contoh rasio persaingan agregat:

```python
def aggregate_competition_ratio(df):
    total_quota = df["kuota"].sum()
    total_applicants = df["pelamar"].sum()

    if pd.isna(total_quota) or total_quota == 0:
        return None

    return total_applicants / total_quota
```

Pastikan nilai kosong dan tipe data ditangani sesuai kebijakan preprocessing. Tentukan apakah baris dengan kuota atau pelamar kosong dikeluarkan dari metrik tertentu, lalu dokumentasikan keputusan itu.
jika folder `src` belum ada, maka buat saja terlebih dahulu

## 7. Filter dan State

- Gunakan filter Streamlit untuk kata kunci, lokasi, jenjang, jurusan, dan hari kerja hanya jika kolomnya sudah valid.
- Terapkan filter pada salinan atau subset data, bukan mengubah dataset dasar secara permanen.
- Hitung ulang KPI dari subset yang telah difilter.
- Gunakan `st.session_state` bila state perlu dipertahankan lintas interaksi.
- Sediakan mekanisme reset filter yang jelas.
- Pastikan data multi-nilai pada jurusan dan jenjang tidak menggandakan kuota atau pelamar dalam agregasi.

## 8. Visualisasi

Buat fungsi terpisah di `src/charts.py` untuk grafik yang digunakan lebih dari sekali. Setiap grafik harus menerima dataset yang sesuai dan menghasilkan visualisasi dengan judul, label sumbu, serta satuan yang jelas.

Sebelum memublikasikan grafik:
- Cocokkan hasil dengan notebook EDA final.
- Periksa filter dan agregasi.
- Pastikan label kategori dapat dibaca.
- Tambahkan penjelasan interpretasi dan keterbatasan bila perlu.

Jangan membuat grafik pemerintah vs swasta atau kategori pekerjaan sebelum klasifikasi yang valid tersedia.

## 9. Gaya Antarmuka

- Terapkan warna dan tipografi dari `06_UI_UX_DESIGN_SYSTEM.md`.
- Gunakan navigasi atas sesuai struktur halaman yang disepakati.
- Jangan menambahkan ikon atau emoji pada antarmuka.
- Gunakan layout responsif dan hindari komponen yang terlalu padat.
- Hindari CSS kustom yang rapuh jika komponen Streamlit bawaan sudah memadai.

## 10. Penanganan Error

Berikan pesan yang jelas untuk kondisi berikut:
- Dataset tidak ditemukan.
- Kolom wajib tidak tersedia.
- Nilai numerik tidak dapat diproses.
- Filter menghasilkan nol baris.
- Data geografis tidak cocok dengan geometri.
- Metrik tidak dapat dihitung karena denominator nol atau data tidak tersedia.

Jangan menampilkan traceback mentah kepada pengguna akhir kecuali dalam mode pengembangan.

## 11. Pengujian

Sebelum rilis, uji:
- Aplikasi berjalan dari environment bersih.
- Semua halaman dapat dibuka.
- Filter bekerja dan dapat di-reset.
- KPI berubah sesuai subset data.
- Rasio persaingan dihitung dengan rumus yang benar.
- Grafik konsisten dengan notebook EDA.
- Tautan lowongan bekerja.
- Kondisi data kosong dan file hilang ditangani.
- Tampilan desktop dan layar sempit tetap terbaca.
- Dokumentasi tidak mengklaim analisis yang belum dikerjakan.

## 12. Publikasi

Sebelum deploy:
1. Pastikan tidak ada rahasia atau kredensial di repository.
2. Pastikan path dataset sesuai environment deployment.
3. Periksa ukuran dataset dan waktu pemuatan aplikasi.
4. Pin dependensi yang sudah diuji.
5. Tambahkan README tentang instalasi dan menjalankan aplikasi.
6. Nyatakan keterbatasan data dan analisis secara terbuka.
7. buat code nya sekalian dipersiapkan untuk dipublikasikan ke online ya untuk path semua dibuat relative, karena kedepannya mau dipublikasikan via github atau sejenisnya
"""
}