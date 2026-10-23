    "09_CHARTS_AND_VISUALIZATION_SPEC.md": r"""# 09 — Charts and Visualization Specification

## 1. Prinsip Umum

Setiap visualisasi harus menjawab pertanyaan analitis tertentu. Pilih jenis grafik berdasarkan struktur data, tampilkan satuan, dan berikan penjelasan singkat mengenai cara membacanya.

**Penting:** Tidak menggunakan ikon atau emoji dalam visualisasi. Semua label dan legenda menggunakan teks saja dengan font Inter atau fallback sans-serif yang konsisten dengan design system.

Daftar berikut adalah spesifikasi kandidat, bukan klaim bahwa seluruh grafik sudah tersedia atau sudah dianalisis. Implementasikan hanya grafik yang didukung oleh hasil notebook EDA final.

## 2. Ringkasan KPI

### KPI yang dapat dipertimbangkan
- Total lowongan.
- Total kuota.
- Total pelamar.
- Rata-rata kuota per lowongan.
- Rata-rata pelamar per lowongan.
- Rasio persaingan agregat.

### Aturan
- Hitung dari dataset final dan subset filter aktif.
- Tampilkan format angka yang konsisten.
- Berikan definisi ringkas melalui teks bantuan atau bagian metodologi.
- Jangan menampilkan perubahan persentase atau tren tanpa periode pembanding yang valid.
- **Tidak menggunakan ikon** pada KPI cards.

## 3. Karakteristik Umum Lowongan

### Kandidat grafik: distribusi kuota
- **Pertanyaan:** bagaimana kuota lowongan tersebar?
- **Visual:** histogram atau bar chart berdasarkan kelompok kuota.
- **Catatan:** distribusi kuota dapat condong ke nilai kecil; pilih bin yang mudah dibaca dan jelaskan jika data dikelompokkan.

### Kandidat grafik: distribusi pelamar
- **Pertanyaan:** bagaimana jumlah pelamar tersebar antar-lowongan?
- **Visual:** histogram atau box plot.
- **Catatan:** bedakan jumlah pelamar per lowongan dari total pelamar keseluruhan.

### Kandidat grafik: distribusi hari kerja
- **Pertanyaan:** bagaimana distribusi jumlah hari kerja per minggu, misalnya lima hari dibanding enam hari?
- **Visual:** bar chart dengan jumlah dan/atau persentase lowongan.
- **Catatan:** gunakan hanya nilai yang telah dibersihkan; laporkan kategori tidak diketahui secara transparan bila relevan.

## 4. Persaingan Lowongan

### Kandidat grafik: distribusi rasio persaingan
- **Pertanyaan:** bagaimana variasi rasio pelamar terhadap kuota antar-lowongan?
- **Visual:** histogram atau box plot.
- **Definisi:** rasio persaingan per lowongan = pelamar dibagi kuota.
- **Catatan:** rasio per lowongan tidak sama dengan rasio agregat.

### Kandidat tabel: lowongan dengan rasio persaingan tertinggi/terendah
- **Pertanyaan:** lowongan mana yang memiliki rasio pelamar terhadap kuota paling tinggi atau rendah?
- **Visual:** tabel terurut.
- **Catatan:** tampilkan kuota dan pelamar bersama rasio agar angka dapat diinterpretasikan. Jangan menyebut hasil sebagai probabilitas diterima.

## 5. Hubungan Kuota dan Pelamar

### Kandidat grafik: scatter plot
- **Pertanyaan:** bagaimana hubungan antara kuota dan jumlah pelamar pada tiap lowongan?
- **Sumbu X:** kuota.
- **Sumbu Y:** pelamar.
- **Satu titik:** satu lowongan.
- **Catatan:** titik bertumpuk dapat ditangani dengan transparansi atau jitter ringan jika tidak menyesatkan. Berikan penjelasan bahwa korelasi tidak membuktikan sebab-akibat.

Nilai korelasi Pearson `r = 0.743` pernah tercatat sebagai hasil sementara. Verifikasi kembali dari notebook dan subset data final sebelum angka tersebut dipublikasikan. Jika hasil final berbeda, gunakan nilai final beserta cakupan data yang jelas.

### Kandidat analisis kuadran
Jika digunakan, tetapkan batas kuadran secara eksplisit, misalnya median kuota dan median pelamar. Jelaskan bahwa kuadran adalah alat eksplorasi, bukan klasifikasi kualitas lowongan.

## 6. Analisis Geografis

### Kandidat grafik: jumlah lowongan per provinsi
- **Visual:** bar chart horizontal yang diurutkan.
- **Tujuan:** membandingkan persebaran jumlah lowongan antarprovinsi.

### Kandidat peta choropleth
- **Visual:** peta choropleth interaktif menggunakan `plotly.graph_objects.Choroplethmapbox`.
- **Tujuan:** memperlihatkan persebaran geografis secara visual pada peta Indonesia.
- **Data yang divisualisasikan:**
  1. **Jumlah lowongan per provinsi** - menunjukkan provinsi mana yang memiliki lowongan terbanyak
  2. **Rasio persaingan per provinsi** - menunjukkan provinsi mana yang persaingannya paling ketat
  3. **Total kuota per provinsi** - menunjukkan provinsi mana yang memiliki kuota terbanyak
  4. **Total pelamar per provinsi** - menunjukkan provinsi mana yang paling banyak pelamar
- **Spesifikasi teknis:**
  - GeoJSON: `data/geojson/GeoJson-Indonesia-38-Provinsi/Provinsi/38 Provinsi Indonesia - Provinsi.json`
  - Feature key: `properties.PROVINSI`
  - Mapbox style: `carto-positron` (clean, professional)
  - Zoom level: 3.5 (untuk Indonesia)
  - Center: lat=-2.5, lon=118
  - **Color scale:** gunakan gradient yang sesuai design system (teal untuk lowongan, amber untuk persaingan, blue untuk kuota, orange untuk pelamar)
  - **Tidak menggunakan ikon** pada marker atau legend
  - Font: Inter, Arial, sans-serif (konsisten dengan design system)
  - Color bar: vertikal di sisi kanan dengan ukuran font 10-12px
  - Hover template: tampilkan nama provinsi dan nilai metrik tanpa ikon
- **Catatan:** dokumentasikan pencocokan nama provinsi dengan geometri. Tampilkan jumlah wilayah yang tidak cocok atau tidak memiliki koordinat bila relevan. Normalisasi nama provinsi mungkin diperlukan (misal: "DKI Jakarta", "DI Yogyakarta").

Jangan membandingkan jumlah wilayah dengan ukuran data yang berbeda tanpa menyebutkan metrik dan cakupannya.

## 7. Jenjang dan Jurusan

### Kandidat grafik: distribusi jenjang pendidikan
- **Visual:** bar chart kategori jenjang.
- **Catatan:** satu lowongan dapat menerima lebih dari satu jenjang. Jika menghitung kemunculan kategori dari format long, jangan menjumlahkan frekuensi kategori seolah-olah setiap baris adalah lowongan unik.

### Kandidat grafik: jurusan/program studi
- **Visual:** bar chart untuk jurusan yang paling sering muncul.
- **Catatan:** perlu aturan parsing multi-nilai dan hitungan lowongan unik. Dokumentasikan jika satu lowongan dapat muncul di beberapa jurusan.

## 8. Grafik yang Tidak Dibuat pada Cakupan Saat Ini

Jangan membuat visualisasi berikut tanpa pekerjaan klasifikasi tambahan:
- Perbandingan jumlah lowongan instansi pemerintah dan swasta, karena klasifikasi instansi belum tervalidasi.
- Distribusi kategori pekerjaan seperti IT/Data, Kesehatan, dan kategori sejenis, karena pemetaan posisi belum dilakukan.

Jangan mengganti kedua grafik tersebut dengan label atau angka hasil perkiraan.

## 9. Standar Label dan Format

- Judul menjelaskan metrik dan cakupan.
- Sumbu menampilkan nama metrik dan satuan.
- Format angka konsisten dengan bahasa antarmuka (gunakan titik untuk ribuan dalam format Indonesia).
- Legenda hanya digunakan bila membantu.
- Gunakan warna yang konsisten dengan dokumen UI/UX (Teal #167C80, Blue #3977B8, Amber #C38A2E).
- Hindari label yang bertumpuk; gunakan bar chart horizontal untuk banyak kategori.
- Sediakan tabel atau teks pendamping ketika grafik saja tidak cukup menjelaskan data.
- **Font:** Inter atau sans-serif fallback, ukuran 10-14px untuk label, 16-18px untuk judul.
- **Tidak menggunakan ikon atau emoji** dalam chart elements, legend, atau annotations.

## 10. Pemeriksaan Sebelum Publikasi

Untuk setiap grafik, verifikasi:
1. Business question yang dijawab.
2. Dataset dan subset yang digunakan.
3. Unit observasi dan aturan agregasi.
4. Penanganan nilai kosong dan duplikat.
5. Judul, satuan, dan definisi metrik.
6. Kesesuaian hasil dengan notebook EDA final.
7. **Tidak ada ikon atau emoji yang digunakan.**
8. Font dan ukuran konsisten dengan design system.
9. Warna mengikuti palette yang sudah ditetapkan.
"""