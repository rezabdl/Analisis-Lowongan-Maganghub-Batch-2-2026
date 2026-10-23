"06_UI_UX_DESIGN_SYSTEM.md": r"""# 06 — UI/UX Design System

## 1. Tujuan Desain

Dashboard MagangHub Batch 2 2026 dirancang sebagai produk analitik yang membantu pengguna memahami karakteristik lowongan magang, kuota, pelamar, persaingan, persyaratan, dan persebaran lokasi. Antarmuka perlu mendukung eksplorasi data sekaligus menjelaskan konteks dan keterbatasan analisis.

Prinsip utama:
- **Jelas:** setiap KPI dan grafik memiliki judul, satuan, dan penjelasan singkat.
- **Konsisten:** format angka, warna, jarak, dan pola interaksi digunakan secara seragam.
- **Berbasis data:** visualisasi hanya menampilkan hasil yang dapat ditelusuri ke dataset dan notebook EDA.
- **Tidak berlebihan:** prioritaskan informasi yang menjawab business question, bukan dekorasi.
- **Responsif:** konten tetap mudah dibaca pada layar desktop maupun layar yang lebih sempit.

## 2. Arah Visual

Gunakan gaya editorial data storytelling: profesional, tenang, bersih, dan tidak terlalu padat.

| Elemen | Nilai |
|---|---|
| Font utama | Inter |
| Fallback font | Arial, Helvetica, sans-serif |
| Background halaman | `#F8F8F5F4` |
| Surface/kartu | `#FFFFFF` |
| Teks utama | `#17324D` |
| Teks sekunder | `#5E7181` |
| Border | `#DCE5E8` |
| Aksen teal | `#167C80` |
| Aksen biru | `#3977B8` |
| Aksen amber | `#C38A2E` |
| Aksen merah | `#BD5B61` |
| Gridline grafik | `#E7ECEF` |

### Aturan warna
- Gunakan warna teks utama untuk judul dan label penting.
- Gunakan teal atau biru sebagai aksen utama, bukan untuk mewarnai semua elemen.
- Gunakan amber dan merah hanya jika makna analitisnya jelas.
- Jangan mengandalkan warna saja untuk membedakan kategori; sertakan label atau legenda.
- Jangan memberikan warna “baik/buruk” pada metrik tanpa dasar interpretasi yang terdokumentasi.

## 3. Tipografi dan Hierarki

- Judul halaman: singkat dan deskriptif.
- Subjudul: menjelaskan cakupan halaman atau pertanyaan yang dijawab.
- Judul grafik: berbentuk pertanyaan atau pernyataan analitis yang spesifik.
- Deskripsi grafik: berikan kalimat yang cukup panjang untuk menjelaskan cara membaca visualisasi.
- Catatan sumber/metode: gunakan ukuran lebih kecil, tetapi tetap terbaca.

Hindari judul umum seperti “Grafik 1” atau “Analisis Data”. Gunakan judul yang menyebut metrik dan cakupan, misalnya “Distribusi Lowongan Berdasarkan Hari Kerja per Minggu”.

## 4. Tata Letak

- Gunakan navigasi utama di bagian atas halaman, bukan sidebar navigasi permanen.
- Kelompokkan konten menjadi bagian yang jelas: ringkasan, visualisasi, eksplorasi, dan metodologi.
- Gunakan KPI cards hanya untuk metrik yang penting bagi halaman tersebut.
- Jaga jarak antarkomponen agar halaman tidak terasa sesak.
- Pada layar kecil, susun KPI dan grafik menjadi satu kolom.
- Hindari tabel lebar yang memerlukan scrolling horizontal jika tabel ringkas atau filter dapat digunakan.

## 5. KPI Cards

Setiap kartu KPI sebaiknya berisi:
1. Nama metrik.
2. Nilai yang diformat dengan konsisten.
3. Definisi atau konteks singkat.
4. Periode/cakupan data jika relevan.

Jangan menambahkan ikon atau emoji pada KPI cards maupun elemen antarmuka. Jangan membuat angka pembanding atau tren jika tidak tersedia data pembanding yang sah.

## 6. Aturan Visualisasi

- Tampilkan satuan pada sumbu atau label ketika relevan.
- Gunakan format ribuan yang konsisten.
- Hindari efek 3D, bayangan berat, dan dekorasi yang tidak membantu pembacaan.
- Tampilkan jumlah observasi atau catatan cakupan bila penting untuk interpretasi.
- Untuk grafik dengan banyak kategori, tampilkan kategori utama dan sediakan tabel atau filter untuk detail.
- Jelaskan bahwa korelasi tidak membuktikan sebab-akibat.
- Jika ada data kosong atau kategori tidak diketahui, tampilkan penanganannya secara transparan.

## 7. Aksesibilitas

- Pastikan kontras teks memadai.
- Label tidak boleh terlalu kecil.
- Jangan membedakan seri hanya dengan warna jika pola, label, atau legenda dapat membantu.
- Gunakan teks alternatif atau penjelasan untuk visual yang kompleks.
- Pastikan filter memiliki label yang jelas dan kondisi reset yang mudah dipahami.

## 8. Konsistensi dan Batasan

Desain antarmuka tidak boleh menyiratkan bahwa analisis yang belum dilakukan sudah tersedia. Secara khusus:
- Jangan membuat grafik perbandingan instansi pemerintah dan swasta tanpa klasifikasi yang tervalidasi.
- Jangan membuat grafik kategori pekerjaan seperti IT/Data atau Kesehatan tanpa pemetaan posisi yang terdokumentasi.
- Jika suatu business question belum dianalisis, tandai sebagai di luar cakupan atau jangan tampilkan sebagai hasil.
"""