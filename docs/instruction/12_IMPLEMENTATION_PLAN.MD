 "12_IMPLEMENTATION_PLAN.md": r"""# 12 — Implementation Plan

## 1. Tujuan

Dokumen ini menyusun urutan pengerjaan dashboard MagangHub Batch 2 2026 agar implementasi dapat dilakukan secara bertahap, mudah diuji, dan konsisten dengan hasil EDA yang sudah tersedia.

Urutan di bawah merupakan rencana kerja. Status setiap tahap perlu diperbarui berdasarkan kondisi repository dan hasil implementasi yang sebenarnya.

## 2. Prinsip Pelaksanaan

- Jadikan dataset final dan notebook EDA sebagai sumber acuan untuk angka analisis.
- Selesaikan validasi data dan definisi metrik sebelum membangun visualisasi final.
- Bangun fitur secara bertahap agar kesalahan lebih mudah dilacak.
- Pisahkan pemrosesan data, perhitungan metrik, grafik, dan UI.
- Jangan menambahkan analisis yang memerlukan klasifikasi yang belum tersedia.
- Uji hasil aplikasi terhadap perhitungan independen sebelum dipublikasikan.

## 3. Tahapan Implementasi

### Tahap 1 — Audit Repository dan Data

**Aktivitas**
- Periksa struktur folder dan file proyek yang sudah ada.
- Tentukan dataset final yang akan digunakan aplikasi.
- Periksa kolom, tipe data, nilai kosong, duplikasi, dan jumlah baris.
- Cocokkan struktur dataset dengan dokumentasi data dictionary.
- Catat dependensi dan cara menjalankan proyek saat ini.

**Hasil yang diharapkan**
- Lokasi dataset final ditetapkan.
- Skema dataset terdokumentasi.
- Masalah data yang memengaruhi KPI dan grafik tercatat.

**Kriteria selesai**
- Dataset yang digunakan dapat diidentifikasi secara jelas.
- Kolom yang dibutuhkan aplikasi telah diverifikasi.
- Keputusan tentang nilai kosong dan duplikasi terdokumentasi.

### Tahap 2 — Finalisasi Definisi Metrik

**Aktivitas**
- Tetapkan definisi total lowongan, total kuota, dan total pelamar.
- Tetapkan denominator untuk rata-rata per lowongan.
- Bedakan rasio persaingan per lowongan dari rasio persaingan agregat.
- Tetapkan aturan untuk kuota atau pelamar yang kosong atau tidak valid.
- Cocokkan nilai penting dengan notebook EDA final.

**Hasil yang diharapkan**
- Definisi metrik yang konsisten.
- Fungsi metrik yang dapat digunakan ulang.
- Catatan verifikasi terhadap hasil notebook.

**Kriteria selesai**
- Rumus dan aturan denominator didokumentasikan.
- Hasil pengujian metrik sesuai dengan perhitungan pembanding.

### Tahap 3 — Fondasi Aplikasi

**Aktivitas**
- Siapkan environment dan dependensi.
- Buat entry point aplikasi Streamlit.
- Buat fungsi pemuatan data dan validasi skema.
- Pisahkan modul preprocessing, metrics, filters, dan charts jika sesuai dengan ukuran proyek.
- Tambahkan penanganan error untuk dataset yang hilang atau skema yang berubah.

**Hasil yang diharapkan**
- Aplikasi dapat dijalankan.
- Dataset dapat dimuat dan divalidasi.
- Kesalahan dasar ditampilkan dengan pesan yang jelas.

**Kriteria selesai**
- Aplikasi berjalan dari instruksi yang terdokumentasi.
- Kegagalan pemuatan data tidak menghasilkan tampilan yang menyesatkan.

### Tahap 4 — Sistem UI/UX dan Navigasi

**Aktivitas**
- Terapkan sistem warna, tipografi, jarak, dan gaya visual.
- Bangun navigasi utama.
- Buat kerangka halaman Beranda, Dashboard, Opportunity Explorer, dan Metodologi.
- Pastikan tampilan responsif dan tidak menggunakan ikon atau emoji.

**Hasil yang diharapkan**
- Struktur halaman konsisten.
- Navigasi mudah dipahami.
- Tampilan dasar siap menerima konten data.

**Kriteria selesai**
- Semua halaman dapat dibuka.
- Navigasi bekerja dan tampilan dasar mengikuti dokumen desain.

### Tahap 5 — KPI dan Dashboard Utama

**Aktivitas**
- Implementasikan KPI yang sudah diverifikasi.
- Tambahkan visualisasi karakteristik umum lowongan.
- Tambahkan visualisasi persaingan dan hubungan kuota-pelamar jika hasilnya telah divalidasi.
- Tambahkan visualisasi lokasi, jenjang, jurusan, atau hari kerja hanya jika data dan analisis pendukungnya siap.
- Tambahkan penjelasan dan catatan keterbatasan.

**Hasil yang diharapkan**
- Dashboard berisi indikator dan visualisasi yang dapat ditelusuri ke EDA.
- Interpretasi visual tidak melampaui dukungan data.

**Kriteria selesai**
- KPI dan grafik cocok dengan hasil pembanding.
- Setiap grafik memiliki judul, satuan, dan definisi yang cukup jelas.

### Tahap 6 — Opportunity Explorer

**Aktivitas**
- Buat pencarian berdasarkan kata kunci.
- Tambahkan filter lokasi, jenjang, jurusan, dan hari kerja sesuai kesiapan data.
- Tambahkan pengurutan berdasarkan kuota, pelamar, atau rasio persaingan.
- Tampilkan jumlah hasil dan tautan lowongan jika tersedia.
- Tambahkan reset filter dan penanganan kondisi tanpa hasil.

**Hasil yang diharapkan**
- Pengguna dapat menemukan lowongan sesuai kriteria.
- Filter dan tabel menghasilkan subset data yang konsisten.

**Kriteria selesai**
- Filter gabungan, reset, pengurutan, dan kondisi tanpa hasil telah diuji.
- KPI terkait tidak menghitung ganda lowongan multi-jurusan atau multi-jenjang.

### Tahap 7 — Halaman Metodologi

**Aktivitas**
- Jelaskan sumber dan cakupan data.
- Jelaskan preprocessing, definisi metrik, dan aturan agregasi.
- Catat keterbatasan data dan analisis.
- Nyatakan bahwa perbandingan pemerintah-swasta dan kategori pekerjaan tidak dikerjakan pada cakupan saat ini.

**Hasil yang diharapkan**
- Pengguna dapat memahami bagaimana angka dan grafik dibentuk.
- Batasan analisis terlihat jelas.

**Kriteria selesai**
- Definisi pada halaman Metodologi konsisten dengan kode dan notebook.
- Analisis yang belum dikerjakan tidak disajikan sebagai hasil.

### Tahap 8 — Pengujian dan Validasi

**Aktivitas**
- Jalankan semua kriteria pada `11_ACCEPTANCE_CRITERIA.md`.
- Uji data kosong, denominator nol, file hilang, dan filter tanpa hasil.
- Bandingkan KPI serta visualisasi dengan notebook EDA final.
- Uji navigasi, tautan, tampilan desktop, dan layar sempit.
- Catat bug dan lakukan perbaikan.

**Hasil yang diharapkan**
- Daftar hasil pengujian.
- Daftar isu tersisa beserta prioritasnya.
- Versi aplikasi yang stabil untuk ditinjau.

**Kriteria selesai**
- Tidak ada isu kritis pada akurasi metrik, filter, atau pemuatan data.
- Kriteria wajib telah terpenuhi atau memiliki keputusan tindak lanjut yang jelas.

### Tahap 9 — Dokumentasi dan Publikasi

**Aktivitas**
- Perbarui README.
- Dokumentasikan instalasi, konfigurasi dataset, dan perintah menjalankan aplikasi.
- Pastikan dependensi dan path sesuai environment deployment.
- Hapus rahasia dari repository.
- Publikasikan aplikasi setelah pemeriksaan akhir.

**Hasil yang diharapkan**
- Proyek dapat dijalankan oleh orang lain mengikuti dokumentasi.
- Aplikasi yang dipublikasikan memiliki konteks dan batasan yang jelas.

**Kriteria selesai**
- Instruksi telah diuji dari environment yang sesuai.
- Dataset dan konfigurasi deployment tersedia sesuai kebutuhan.
- Dokumentasi dan aplikasi konsisten.

## 4. Prioritas Pengerjaan

Urutan prioritas yang disarankan:

1. **P0 — Wajib:** audit data, validasi skema, definisi metrik, pemuatan data, KPI inti, penanganan error.
2. **P1 — Penting:** visualisasi utama, navigasi, Opportunity Explorer, filter, dan metodologi.
3. **P2 — Penyempurnaan:** peningkatan aksesibilitas, performa, detail tooltip, dan perbaikan visual berdasarkan pengujian.

Prioritas dapat disesuaikan jika kondisi repository menunjukkan ada tahap yang sudah selesai atau memiliki dependensi lain.

## 5. Di Luar Cakupan Saat Ini

Jangan memasukkan pekerjaan berikut sebagai fitur yang sudah disepakati untuk rilis awal:
- Klasifikasi instansi menjadi pemerintah dan swasta.
- Klasifikasi posisi ke kategori pekerjaan seperti IT/Data atau Kesehatan.

Keduanya hanya dapat dipertimbangkan pada iterasi berikutnya setelah aturan klasifikasi disusun, divalidasi, dan didokumentasikan.

## 6. Pelacakan Progres

Gunakan tabel berikut untuk mencatat progres implementasi. Perbarui status sesuai kondisi aktual; jangan menganggap semua tahap sudah selesai.

| Tahap | Status | Catatan |
|---|---|---|
| Audit repository dan data | Belum diverifikasi | Tentukan dataset final dan skema |
| Finalisasi definisi metrik | Belum diverifikasi | Cocokkan dengan notebook EDA |
| Fondasi aplikasi | Belum diverifikasi | Pemuatan data dan validasi |
| Sistem UI/UX dan navigasi | Belum diverifikasi | Terapkan design system |
| KPI dan dashboard utama | Belum diverifikasi | Verifikasi hasil sebelum publikasi |
| Opportunity Explorer | Belum diverifikasi | Uji filter dan agregasi |
| Halaman Metodologi | Belum diverifikasi | Dokumentasikan rumus dan batasan |
| Pengujian dan validasi | Belum diverifikasi | Gunakan acceptance criteria |
| Dokumentasi dan publikasi | Belum diverifikasi | Uji instruksi dan deployment |

## 7. Definisi Selesai

Implementasi dinyatakan selesai ketika:
- Fitur yang disertakan telah memenuhi kriteria penerimaan.
- KPI dan grafik cocok dengan data serta perhitungan pembanding.
- Filter tidak menyebabkan agregasi ganda.
- Batasan analisis dijelaskan secara terbuka.
- Dokumentasi telah diperbarui.
- Aplikasi dapat dijalankan dan diuji mengikuti instruksi proyek.
"""