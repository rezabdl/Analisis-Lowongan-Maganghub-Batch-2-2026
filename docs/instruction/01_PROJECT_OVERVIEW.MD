"01_PROJECT_OVERVIEW.md": r"""# 01 — Project Overview
## Analisis dan Dashboard MagangHub Batch 2 2026

## 1. Ringkasan proyek
Proyek ini menyajikan hasil Exploratory Data Analysis (EDA) terhadap data lowongan MagangHub Batch 2 2026. Dashboard Streamlit akan menjadi media untuk membaca temuan analisis, menelusuri distribusi data, dan memahami pola kuota, pelamar, persaingan, lokasi, jurusan, jenjang pendidikan, serta hari kerja berdasarkan pertanyaan yang benar-benar dianalisis di notebook.

Dashboard harus merepresentasikan hasil notebook secara jujur. Dashboard bukan tempat untuk membuat hasil analisis baru yang belum dikerjakan atau menampilkan angka ilustrasi seolah-olah angka aktual.

## 2. Tujuan
1. Menyajikan gambaran umum lowongan, kuota, dan pelamar.
2. Menggambarkan persaingan berdasarkan rasio pelamar terhadap kuota.
3. Menampilkan distribusi geografis lowongan dan metrik terkait.
4. Menyajikan analisis posisi atau jurusan hanya sesuai analisis yang benar-benar dilakukan.
5. Menjelaskan hubungan kuota dan jumlah pelamar.
6. Menyajikan distribusi hari kerja per minggu.
7. Menjelaskan definisi metrik, proses data preparation, dan keterbatasan analisis.
8. Menjadikan proyek sebagai portofolio Data Science yang transparan dan dapat diverifikasi.

## 3. Status Business Questions
Tidak semua BQ dalam rancangan awal dilanjutkan ke notebook final.

- **BQ 3 — Perbandingan Instansi Pemerintah vs Swasta: tidak dilanjutkan.** Dataset belum memiliki klasifikasi instansi yang tervalidasi dan proyek tidak akan menebak jenis instansi berdasarkan nama.
- **BQ 6 — Posisi dengan Peluang dan Peminat Terbesar: tidak dilanjutkan dalam bentuk kategorisasi kelompok pekerjaan.** Pengelompokan seperti IT/Data, Kesehatan, dan kategori lain memerlukan proses klasifikasi tambahan yang tidak dilakukan dalam notebook.
- BQ lain hanya boleh ditampilkan sebagai hasil final setelah keberadaan analisis, visualisasi, dan angkanya diperiksa di notebook.

Catatan: BQ 6 yang berbasis kategori pekerjaan tidak boleh diganti diam-diam dengan chart lain yang mengklaim menjawab pertanyaan yang sama. Jika ada analisis posisi individual yang benar-benar dibuat di notebook, analisis itu hanya boleh ditampilkan dengan judul dan metrik yang tepat.

## 4. Target pengguna
- Recruiter atau hiring manager yang meninjau portofolio.
- Praktisi data yang ingin memahami alur EDA.
- Mahasiswa atau pencari magang yang ingin mengeksplorasi informasi agregat lowongan.
- Reviewer portofolio akademik atau profesional.

## 5. Ruang lingkup
### Termasuk
- Ringkasan jumlah lowongan, kuota, dan pelamar.
- Rasio persaingan sesuai definisi metrik.
- Analisis wilayah yang telah dikerjakan dan divalidasi.
- Analisis jurusan/jenjang hanya jika tersedia di notebook final.
- Hubungan kuota dan pelamar.
- Distribusi hari kerja per minggu.
- Filter dan tabel eksplorasi jika didukung oleh dataset final.
- Metodologi dan batasan.

### Tidak termasuk
- Perbandingan pemerintah vs swasta yang belum tervalidasi.
- Kategorisasi posisi ke kelompok pekerjaan seperti IT/Data atau Kesehatan yang belum dilakukan.
- Prediksi peluang penerimaan individu.
- Klaim bahwa korelasi menunjukkan sebab-akibat.
- Angka, insight, atau chart yang hanya berasal dari mockup.
- Mengklaim tingkat penerimaan aktual tanpa data penerimaan aktual.

## 6. Prinsip analisis
1. Satu baris dataset utama merepresentasikan satu lowongan.
2. Jangan menggandakan baris utama karena satu lowongan memiliki banyak jurusan atau jenjang.
3. Pertahankan nilai sumber bila memungkinkan.
4. Semua KPI dan chart harus dapat ditelusuri ke data dan notebook.
5. Missing values tidak otomatis dianggap nol.
6. Jangan mengarang kategori atau klasifikasi yang belum divalidasi.
7. Korelasi tidak sama dengan kausalitas.
8. Bedakan rasio agregat dari rata-rata rasio per lowongan.
9. Bila suatu BQ tidak dianalisis, tampilkan sebagai di luar cakupan—bukan sebagai hasil kosong atau nol.
10. **Antarmuka tidak boleh menggunakan ikon atau emoji.**

## 7. Arah desain
Gaya editorial data storytelling yang bersih dan profesional. Gunakan latar netral terang, teks navy, aksen teal, ruang kosong yang cukup, dan chart yang mudah dibaca. Hindari ikon, emoji, dekorasi berlebihan, neon, dan glassmorphism.

## 8. Teknologi
Target aplikasi: Python, Streamlit, Pandas, Plotly, CSS, serta GeoJSON bila peta yang telah divalidasi memang dibutuhkan. OpenCode wajib memeriksa struktur repository dan file aktual sebelum mengubah arsitektur.

## 9. Kriteria keberhasilan
- Angka dashboard konsisten dengan notebook.
- BQ yang tidak dianalisis tidak ditampilkan seolah-olah terjawab.
- Pengguna memahami definisi competition ratio dan keterbatasannya.
- Chart mempunyai judul, satuan, konteks, dan sumber data yang jelas.
- Seluruh kontrol yang tampil benar-benar berfungsi.
- UI konsisten dan tanpa ikon/emoji.
"""