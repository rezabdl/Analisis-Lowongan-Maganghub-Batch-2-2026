# 📊 Panduan Dashboard Analisis Lowongan MagangHub

## 🚀 Cara Menjalankan Dashboard

### Langkah 1: Buka Terminal/Command Prompt
Buka terminal dan masuk ke folder dashboard:
```bash
cd "D:\Developments\Riset Pribadi\Maganghub\dashboard"
```

### Langkah 2: Jalankan Dashboard
```bash
streamlit run app_streamlit.py
```

Dashboard akan otomatis terbuka di browser Anda pada alamat:
**http://localhost:8501**

### Langkah 3: Gunakan Dashboard
Dashboard sudah siap digunakan! 🎉

---

## 📱 Fitur-Fitur Dashboard

### 1️⃣ **Filter Interaktif (Sidebar Kiri)**
- **Filter Provinsi**: Pilih provinsi yang ingin Anda analisis
- **Jenis Instansi**: Filter berdasarkan Pemerintah atau Swasta
- **Jenjang Pendidikan**: Filter Diploma, Sarjana, atau Profesi
- **Competition Ratio**: Atur range tingkat persaingan

### 2️⃣ **Tab Analisis**

#### 🏢 Tab Instansi
- Perbandingan lowongan Pemerintah vs Swasta
- Top 15 instansi dengan lowongan terbanyak
- Perbandingan kuota dan pelamar

#### 📍 Tab Geografis
- Top 15 provinsi berdasarkan jumlah lowongan
- Top 15 provinsi berdasarkan jumlah pelamar
- Provinsi dengan competition ratio tertinggi
- Top 15 kabupaten/kota

#### 💼 Tab Posisi & Persaingan
- Top 15 posisi terbanyak
- Posisi dengan pelamar terbanyak
- Distribusi kategori peluang (Besar/Sedang/Kecil)
- Analisis hubungan competition ratio dan kuota

#### 🎓 Tab Jurusan & Jenjang
- Distribusi jenjang pendidikan
- Top 20 jurusan paling banyak dicari
- Statistik jumlah jurusan per lowongan

#### 📊 Tab Supply & Demand
- Scatter plot kuota vs pelamar dengan trendline
- Distribusi kuota dan pelamar
- Distribusi competition ratio
- Analisis berdasarkan hari kerja

#### 🔍 Tab Detail Data
- Pencarian lowongan berdasarkan kata kunci
- Filter dan sorting data
- Export data ke CSV

---

## 💡 Tips Menggunakan Dashboard

### Mencari Lowongan dengan Persaingan Rendah
1. Buka tab **"Supply & Demand"**
2. Lihat scatter plot untuk lowongan dengan kuota besar tapi pelamar sedikit
3. Atau gunakan filter **Competition Ratio** di sidebar (set ke 0-5)

### Mencari Lowongan di Wilayah Tertentu
1. Gunakan filter **"Pilih Provinsi"** di sidebar
2. Lihat tab **"Geografis"** untuk analisis per wilayah
3. Gunakan tab **"Detail Data"** untuk melihat daftar lengkap

### Mencari Lowongan Sesuai Jurusan
1. Buka tab **"Detail Data"**
2. Gunakan kotak pencarian, ketik nama jurusan Anda
3. Hasil akan muncul secara real-time

### Export Data
1. Buka tab **"Detail Data"**
2. Filter data sesuai kebutuhan
3. Klik tombol **"📥 Download Data (CSV)"**

---

## 🎯 Contoh Analisis

### Contoh 1: Mencari Peluang Terbaik untuk Jurusan Teknik Informatika
1. Filter Jenjang: **Sarjana**
2. Tab **"Detail Data"** → Cari: **"Teknik Informatika"**
3. Sort by: **Competition Ratio** (Ascending)
4. Lihat lowongan dengan persaingan terendah

### Contoh 2: Bandingkan Lowongan Jakarta vs Surabaya
1. Filter Provinsi: **DKI Jakarta, Jawa Timur**
2. Tab **"Geografis"** → Lihat perbandingan
3. Tab **"Detail Data"** → Export untuk analisis lebih lanjut

### Contoh 3: Analisis Instansi Pemerintah
1. Filter Jenis Instansi: **Pemerintah**
2. Tab **"Instansi"** → Lihat top instansi pemerintah
3. Tab **"Posisi & Persaingan"** → Lihat posisi paling kompetitif

---

## ❓ FAQ

**Q: Dashboard tidak muncul setelah dijalankan?**  
A: Buka browser dan akses manual ke http://localhost:8501

**Q: Bagaimana cara menghentikan dashboard?**  
A: Tekan `Ctrl + C` di terminal tempat dashboard berjalan

**Q: Apakah data bisa diupdate?**  
A: Ya, ganti file `data/processed/data_lowongan/data_eda.csv` dengan data terbaru, lalu refresh dashboard

**Q: Filter tidak bekerja?**  
A: Pastikan Anda memilih setidaknya satu opsi di setiap filter, atau pilih "Semua"

**Q: Visualisasi lambat loading?**  
A: Ini normal untuk dataset besar (22,477 lowongan). Gunakan filter untuk mempercepat.

---

## 📞 Informasi Dataset

- **Sumber**: Platform MagangHub (maganghub.kemnaker.go.id)
- **Periode**: Batch 2 Tahun 2026
- **Tanggal Pengumpulan**: 21-22 September 2026
- **Total Lowongan**: 22,477 lowongan
- **Cakupan**: Seluruh Indonesia
- **Total Instansi**: 4,162 instansi
- **Total Provinsi**: 34 provinsi

---

## 🎨 Tentang Visualisasi

Dashboard ini menggunakan:
- **Streamlit**: Framework untuk dashboard interaktif
- **Plotly**: Library visualisasi interaktif
- **Pandas**: Library pengolahan data

Semua visualisasi bersifat **interaktif**:
- Hover untuk melihat detail
- Zoom in/out
- Pan (geser)
- Export gambar

---

**Selamat Mengeksplorasi Data! 🚀**

Jika ada pertanyaan atau menemukan bug, silakan laporkan.
