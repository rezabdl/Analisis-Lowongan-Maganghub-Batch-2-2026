"07_PAGE_SPECIFICATIONS.md": r"""# 07 — Page Specifications

## 1. Struktur Navigasi

Gunakan navigasi utama horizontal di bagian atas aplikasi. Halaman yang disarankan:

1. **Beranda** — konteks proyek, ringkasan dataset, dan cara menggunakan dashboard.
2. **Dashboard** — indikator dan visualisasi utama yang sudah tervalidasi.
3. **Opportunity Explorer** — pencarian dan penyaringan lowongan.
4. **Metodologi** — definisi metrik, proses persiapan data, batasan, dan sumber data.

Nama halaman boleh disesuaikan saat implementasi, tetapi fungsinya harus tetap jelas.

## 2. Beranda

### Tujuan
Memperkenalkan proyek dan membantu pengguna memahami apa yang dapat dan tidak dapat dijawab oleh analisis.

### Konten
- Nama proyek: Analisis dan Dashboarding MagangHub Batch 2 2026.
- Deskripsi singkat tujuan analisis.
- Ringkasan cakupan dataset setelah jumlah final diverifikasi.
- Tautan ke Dashboard, Opportunity Explorer, dan Metodologi.
- Keterangan bahwa dashboard merupakan analisis data lowongan yang tersedia, bukan jaminan peluang diterima.

Jangan menampilkan angka jumlah baris atau rentang waktu sebelum diverifikasi dari dataset final.

## 3. Dashboard

### Tujuan
Menyajikan gambaran utama mengenai lowongan, kuota, pelamar, persaingan, lokasi, pendidikan, dan hari kerja berdasarkan analisis yang benar-benar dilakukan.

### Susunan yang disarankan
1. Judul dan deskripsi cakupan data.
2. Baris KPI utama.
3. Bagian karakteristik umum lowongan.
4. Bagian persaingan kuota dan pelamar.
5. Bagian lokasi dan distribusi geografis.
6. Bagian persyaratan pendidikan dan hari kerja, jika hasilnya tersedia.
7. Catatan interpretasi dan tautan menuju metodologi.

### Kandidat KPI
Pilih KPI berikut hanya setelah nilainya dihitung dari dataset final:
- Total lowongan.
- Total kuota.
- Total pelamar.
- Rata-rata kuota per lowongan.
- Rata-rata pelamar per lowongan.
- Rasio persaingan agregat, yaitu total pelamar dibagi total kuota.

Jangan menampilkan semua KPI jika membuat halaman terlalu padat. Prioritaskan metrik yang paling membantu menjawab pertanyaan utama.

### Batasan konten
- Jangan menampilkan perbandingan pemerintah vs swasta karena klasifikasi instansi belum dilakukan secara andal.
- Jangan menampilkan kategori pekerjaan seperti IT/Data atau Kesehatan karena klasifikasi posisi belum dilakukan.
- Jangan menyajikan angka korelasi, ranking, atau temuan sebagai hasil final sebelum diverifikasi terhadap notebook dan dataset final.

## 4. Opportunity Explorer

### Tujuan
Membantu pengguna menemukan lowongan yang sesuai melalui pencarian dan filter.

### Fitur yang disarankan
- Pencarian kata kunci pada nama posisi dan instansi.
- Filter provinsi dan kabupaten/kota, jika kolom lokasi sudah dinormalisasi dan tervalidasi.
- Filter jenjang pendidikan, jika format multi-nilai telah diproses dengan aturan yang konsisten.
- Filter jurusan/program studi, jika format jurusan telah diproses dengan aturan yang konsisten.
- Filter hari kerja per minggu.
- Pengurutan berdasarkan kuota, jumlah pelamar, atau rasio persaingan.
- Tabel hasil dengan tautan lowongan jika URL tersedia.

### Kolom tabel yang disarankan
- Posisi.
- Instansi.
- Lokasi.
- Jenjang.
- Hari kerja.
- Kuota.
- Pelamar.
- Rasio persaingan.
- Tautan lowongan.

Tampilkan hanya kolom yang tersedia dan valid. Jangan membuat kolom kategori instansi atau kategori pekerjaan yang belum didukung pemetaan.

### Perilaku
- Sediakan tombol reset filter.
- Tampilkan jumlah lowongan yang cocok dengan filter.
- Tampilkan keadaan kosong jika tidak ada hasil.
- Pastikan pengurutan dan filter tidak mengubah data sumber secara permanen.

## 5. Metodologi

### Konten minimum
- Sumber dan cakupan data.
- Unit observasi: satu baris merepresentasikan satu lowongan.
- Tahapan pembersihan dan transformasi.
- Definisi KPI dan metrik.
- Penanganan nilai kosong, duplikasi, dan format multi-nilai.
- Penjelasan rasio persaingan dan keterbatasan interpretasinya.
- Batasan analisis dan pertanyaan yang tidak dikerjakan.

### Business question yang tidak dikerjakan
Cantumkan secara eksplisit:
- Perbandingan lowongan instansi pemerintah dan swasta tidak dikerjakan karena klasifikasi instansi belum tervalidasi.
- Pengelompokan posisi ke kategori pekerjaan seperti IT/Data atau Kesehatan tidak dikerjakan karena belum tersedia pemetaan posisi yang tervalidasi.

Jangan membuat visual pengganti yang seolah-olah menjawab dua pertanyaan tersebut.

## 6. Ketentuan Publikasi

Sebelum aplikasi dipublikasikan:
- Cocokkan seluruh angka dengan dataset final.
- Pastikan judul dan catatan menjelaskan cakupan visual.
- Pastikan filter bekerja konsisten di semua komponen terkait.
- Periksa tampilan desktop dan layar kecil.
- Periksa semua tautan lowongan.
- Pastikan business question yang belum dikerjakan tidak muncul sebagai temuan.
"""