# Dashboard Analisis Lowongan MagangHub Batch 2 2026

Dashboard interaktif berbasis Streamlit untuk menganalisis data lowongan magang dari platform MagangHub.

## 📋 Fitur Dashboard

Dashboard ini menjawab semua Business Questions yang telah didefinisikan:

### 1. **Overview & Ringkasan Umum**
- Total lowongan, kuota, pelamar, dan competition ratio
- Metrik utama yang dapat difilter secara dinamis

### 2. **Analisis Instansi** 
- Perbandingan lowongan Pemerintah vs Swasta
- Top instansi dengan lowongan terbanyak
- Perbandingan kuota dan pelamar per jenis instansi

### 3. **Analisis Geografis**
- Distribusi lowongan per provinsi dan kabupaten/kota
- Peta persebaran pelamar
- Competition ratio per wilayah
- Top 15 provinsi dan kabupaten/kota

### 4. **Analisis Posisi & Persaingan**
- Top posisi berdasarkan jumlah lowongan
- Posisi dengan pelamar terbanyak
- Distribusi kategori peluang
- Scatter plot competition ratio vs kuota

### 5. **Analisis Jurusan & Jenjang**
- Distribusi jenjang pendidikan (Diploma/Sarjana/Profesi)
- Top 20 jurusan paling banyak dicari
- Statistik jumlah jurusan per lowongan

### 6. **Analisis Supply & Demand**
- Hubungan kuota vs pelamar dengan trendline
- Distribusi kuota dan pelamar
- Distribusi competition ratio
- Analisis berdasarkan hari kerja

### 7. **Eksplorasi Data Detail**
- Pencarian dan filtering lowongan
- Sorting dan custom column selection
- Export data hasil filter ke CSV

## 🚀 Cara Menjalankan

### 1. Install Dependencies

Pastikan Anda berada di folder `dashboard`:

```bash
cd "D:\Developments\Riset Pribadi\Maganghub\dashboard"
```

Install dependencies yang diperlukan:

```bash
pip install -r requirements_streamlit.txt
```

### 2. Jalankan Dashboard

```bash
streamlit run app_streamlit.py
```

Dashboard akan otomatis terbuka di browser pada `http://localhost:8501`

## 🎯 Filter Interaktif

Dashboard dilengkapi dengan filter di sidebar:

- **Filter Provinsi**: Pilih satu atau beberapa provinsi
- **Jenis Instansi**: Pemerintah / Swasta
- **Jenjang Pendidikan**: Diploma / Sarjana / Profesi
- **Competition Ratio Range**: Slider untuk filter berdasarkan tingkat persaingan

Semua visualisasi dan metrik akan otomatis ter-update sesuai filter yang dipilih.

## 📊 Struktur Data

Dashboard menggunakan data dari:
```
data/processed/data_lowongan/data_eda.csv
```

Kolom yang digunakan:
- `posisi`: Nama posisi magang
- `instansi`: Nama instansi penyelenggara
- `jurusan`: Jurusan yang dapat mendaftar (multivalue)
- `nama_kabupaten`: Kabupaten/kota lokasi
- `nama_provinsi`: Provinsi lokasi
- `Diploma`, `Sarjana`, `Profesi`: Jenjang pendidikan (boolean)
- `hari_kerja`: Jumlah hari kerja per minggu
- `kuota`: Jumlah kuota peserta
- `pelamar`: Jumlah pelamar
- `competition_ratio`: Rasio pelamar terhadap kuota
- `kategori_peluang`: Kategori peluang (Besar/Sedang/Kecil)
- `persentase_peluang`: Persentase peluang

## 💡 Tips Penggunaan

1. **Eksplorasi Cepat**: Mulai dari tab "Instansi" untuk melihat overview umum
2. **Analisis Geografis**: Gunakan tab "Geografis" untuk melihat distribusi wilayah
3. **Cari Peluang**: Tab "Supply & Demand" menunjukkan lowongan dengan persaingan rendah
4. **Detail Search**: Gunakan tab "Detail Data" untuk pencarian spesifik dan export data
5. **Filter Kombinasi**: Kombinasikan beberapa filter untuk analisis yang lebih spesifik

## 🔧 Troubleshooting

### Error: File not found
Pastikan struktur folder sesuai:
```
Maganghub/
├── dashboard/
│   └── app_streamlit.py
└── data/
    └── processed/
        └── data_lowongan/
            └── data_eda.csv
```

### Error: Module not found
Jalankan kembali instalasi dependencies:
```bash
pip install -r requirements_streamlit.txt
```

### Dashboard tidak muncul di browser
Cek port yang digunakan, atau jalankan dengan port custom:
```bash
streamlit run app_streamlit.py --server.port 8502
```

## 📈 Insight Utama dari Dashboard

Dashboard ini membantu menjawab:
- Wilayah mana yang memiliki lowongan terbanyak?
- Posisi apa yang paling kompetitif?
- Jurusan mana yang memiliki akses peluang paling luas?
- Bagaimana perbandingan instansi pemerintah vs swasta?
- Berapa rata-rata competition ratio per wilayah?

## 📝 Catatan

- Data dikumpulkan pada 21-22 September 2026
- Total: 22,477 lowongan magang
- Mencakup seluruh Indonesia

---

**Developed for MagangHub Batch 2 2026 Analysis**
