 "11_ACCEPTANCE_CRITERIA.md": r"""# 11 — Acceptance Criteria

## 1. Tujuan

Dokumen ini menetapkan kriteria penerimaan untuk dashboard Analisis dan Dashboarding MagangHub Batch 2 2026. Implementasi dianggap siap ketika fitur, perhitungan, visualisasi, dan dokumentasi telah diperiksa terhadap kriteria di bawah.

Kriteria ini adalah target pengujian. Kriteria bukan pernyataan bahwa aplikasi atau seluruh analisis sudah selesai.

## 2. Kesesuaian Data

- [ ] Aplikasi membaca dataset final dari lokasi yang telah dikonfigurasi.
- [ ] Aplikasi menampilkan pesan yang jelas jika dataset tidak ditemukan.
- [ ] Kolom wajib divalidasi sebelum KPI dan grafik dibuat.
- [ ] Tipe data numerik untuk kuota dan pelamar diperiksa dan ditangani secara konsisten.
- [ ] Nilai kosong tidak otomatis dianggap nol.
- [ ] Aturan duplikasi dijelaskan dan diterapkan secara konsisten.
- [ ] Unit observasi pada dataset utama tetap satu baris per lowongan.
- [ ] Jumlah baris dan ringkasan dataset yang ditampilkan sesuai dengan dataset final.

## 3. Akurasi KPI dan Metrik

- [ ] Total lowongan dihitung berdasarkan unit observasi yang ditetapkan.
- [ ] Total kuota dihitung dari lowongan yang termasuk dalam cakupan atau filter aktif.
- [ ] Total pelamar dihitung dari lowongan yang termasuk dalam cakupan atau filter aktif.
- [ ] Rata-rata kuota per lowongan menggunakan denominator yang dijelaskan.
- [ ] Rata-rata pelamar per lowongan menggunakan denominator yang dijelaskan.
- [ ] Rasio persaingan agregat dihitung sebagai total pelamar dibagi total kuota.
- [ ] Rasio persaingan per lowongan dibedakan dari rasio persaingan agregat.
- [ ] Denominator nol atau tidak tersedia ditangani tanpa menghasilkan pembagian yang tidak valid.
- [ ] Hasil KPI dibandingkan dengan perhitungan independen atau hasil notebook EDA final.

## 4. Filter dan Opportunity Explorer

- [ ] Pencarian kata kunci berfungsi pada kolom yang ditentukan.
- [ ] Filter lokasi hanya menggunakan nilai yang telah dibersihkan dan divalidasi.
- [ ] Filter jenjang, jurusan, dan hari kerja hanya tersedia jika datanya telah diproses dengan aturan yang jelas.
- [ ] Filter dapat digabungkan tanpa mengabaikan pilihan pengguna.
- [ ] Jumlah lowongan setelah filter ditampilkan dengan benar.
- [ ] KPI dan grafik yang terkait mengikuti subset filter yang sama.
- [ ] Pengurutan tabel menghasilkan urutan yang sesuai dengan kolom dan arah yang dipilih.
- [ ] Tombol reset mengembalikan filter ke kondisi awal.
- [ ] Kondisi tanpa hasil ditampilkan melalui pesan yang jelas.
- [ ] Lowongan yang memiliki banyak jurusan atau jenjang tidak menggandakan kuota dan pelamar dalam KPI agregat.

## 5. Visualisasi

- [ ] Setiap grafik memiliki judul yang menjelaskan metrik atau pertanyaan analitis.
- [ ] Sumbu, satuan, legenda, dan format angka dapat dibaca.
- [ ] Setiap visualisasi menggunakan data dan aturan agregasi yang sesuai.
- [ ] Grafik konsisten dengan hasil notebook EDA final.
- [ ] Korelasi antara kuota dan pelamar tidak dijelaskan sebagai hubungan sebab-akibat.
- [ ] Grafik peta hanya memasukkan lokasi yang dapat dipetakan sesuai aturan pencocokan wilayah.
- [ ] Nilai atau kategori yang tidak diketahui ditangani secara transparan.
- [ ] Visualisasi tidak mengklaim hasil analisis yang belum dilakukan.

## 6. Batasan Business Question

- [ ] Tidak ada grafik perbandingan instansi pemerintah dan swasta karena klasifikasi instansi belum tervalidasi.
- [ ] Tidak ada grafik kategori pekerjaan seperti IT/Data atau Kesehatan karena pemetaan posisi belum dilakukan.
- [ ] Business question yang tidak dikerjakan dicantumkan sebagai batasan, bukan disajikan sebagai hasil.
- [ ] Nilai korelasi sementara, termasuk `r = 0.743`, diverifikasi terhadap notebook dan dataset final sebelum dipublikasikan.

## 7. UI/UX dan Aksesibilitas

- [ ] Navigasi ant halaman berfungsi.
- [ ] Desain mengikuti sistem visual yang terdokumentasi.
- [ ] Tidak ada ikon atau emoji pada antarmuka.
- [ ] Kontras teks dan latar belakang memadai.
- [ ] Label filter dan kontrol interaktif jelas.
- [ ] Tata letak dapat digunakan pada desktop dan layar yang lebih sempit.
- [ ] Grafik memiliki penjelasan pendamping ketika diperlukan untuk interpretasi.
- [ ] Halaman tidak menampilkan komponen kosong atau placeholder yang seolah-olah merupakan hasil final.

## 8. Stabilitas dan Penggunaan

- [ ] Aplikasi dapat dijalankan dari instruksi instalasi yang terdokumentasi.
- [ ] Dependensi yang diperlukan dicantumkan dalam file dependensi proyek.
- [ ] Kesalahan pemuatan data ditangani dengan pesan yang dapat dipahami.
- [ ] Tidak ada kredensial atau rahasia yang disimpan di repository.
- [ ] Tautan lowongan berfungsi jika URL tersedia.
- [ ] Waktu pemuatan dan interaksi telah diperiksa pada ukuran data target.

## 9. Dokumentasi

- [ ] Definisi metrik dan aturan agregasi tersedia.
- [ ] Sumber data, tahapan persiapan, dan batasan analisis didokumentasikan.
- [ ] Instruksi menjalankan aplikasi telah diuji.
- [ ] Angka yang ditampilkan dapat ditelusuri kembali ke dataset atau notebook EDA.
- [ ] Dokumentasi tidak menyatakan fitur atau analisis selesai jika belum diverifikasi.

## 10. Keputusan Penerimaan

Aplikasi dapat dinyatakan siap untuk dipublikasikan setelah seluruh kriteria wajib terpenuhi, hasil pengujian dicatat, dan tidak ada masalah kritis pada akurasi metrik, filter, pemuatan data, atau interpretasi visualisasi.

Jika ada kriteria yang belum terpenuhi, catat statusnya sebagai belum selesai, jelaskan dampaknya, dan tentukan tindak lanjut sebelum rilis.
"""