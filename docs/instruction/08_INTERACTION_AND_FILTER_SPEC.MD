"08_INTERACTION_AND_FILTER_SPEC.md": r"""# 08 — Interaction and Filter Specification

## 1. Prinsip Interaksi

Interaksi harus membantu pengguna menyaring, membandingkan, dan memahami data tanpa mengubah arti metrik. Filter yang sama harus menghasilkan subset data yang konsisten pada semua komponen yang bergantung padanya.

## 2. Filter Global

Gunakan filter global hanya untuk dimensi yang telah tersedia dan divalidasi.

| Filter | Sumber data | Aturan |
|---|---|---|
| Kata kunci | `posisi`, `instansi` | Pencarian teks tanpa membedakan huruf besar/kecil |
| Provinsi | Kolom provinsi hasil normalisasi | Tampilkan nilai valid dan opsi semua lokasi |
| Kabupaten/kota | Kolom kabupaten/kota hasil normalisasi | Pilihan dapat disesuaikan dengan provinsi yang dipilih |
| Jenjang | `jenjang` atau kolom turunan tervalidasi | Tangani nilai multi-jenjang secara konsisten |
| Jurusan | `jurusan` atau struktur turunan tervalidasi | Jangan menggandakan lowongan dalam metrik agregat |
| Hari kerja | `hari_kerja` | Gunakan nilai kategori/numerik yang telah dibersihkan |

Tidak semua filter harus ditampilkan secara global. Pilih berdasarkan kebutuhan halaman dan pastikan implementasinya tidak membingungkan.

## 3. Filter dan Agregasi

- Pertahankan satu baris per lowongan pada tabel utama.
- Jangan melakukan `explode` pada kolom multi-nilai lalu menjumlahkan kuota atau pelamar tanpa deduplikasi yang sesuai.
- Jika analisis jurusan atau jenjang membutuhkan format long, gunakan dataset analisis terpisah dan dokumentasikan cara menghitung jumlah lowongan unik.
- Total kuota dan total pelamar dihitung dari lowongan yang masuk ke subset filter.
- Rasio persaingan agregat dihitung ulang sebagai total pelamar dibagi total kuota pada subset terpilih, bukan sebagai rata-rata sederhana rasio tiap lowongan.
- Jika denominator total kuota nol atau tidak tersedia, tampilkan nilai tidak tersedia alih-alih membagi dengan nol.

## 4. Pengurutan Opportunity Explorer

Pengguna dapat mengurutkan tabel berdasarkan:
- Kuota terbesar atau terkecil.
- Pelamar terbanyak atau tersedikit.
- Rasio persaingan terbesar atau terkecil.
- Posisi atau instansi secara alfabetis.

Jelaskan arah pengurutan melalui label atau indikator teks yang jelas. Jangan menyebut rasio persaingan rendah sebagai jaminan lebih mudah diterima; rasio tersebut hanya perbandingan jumlah pelamar terhadap kuota yang tercatat.

## 5. Reset dan Status Filter

- Sediakan kontrol **Reset filter** yang mengembalikan filter ke kondisi awal.
- Tampilkan jumlah baris/lowongan setelah filter diterapkan.
- Tampilkan ringkasan filter aktif jika jumlah filter cukup banyak.
- Jika filter tidak menghasilkan data, tampilkan pesan yang menjelaskan bahwa tidak ada lowongan yang cocok.
- Jangan diam-diam mengganti filter pilihan pengguna.

## 6. Tooltip dan Penjelasan Metrik

Tooltip atau teks bantuan dapat menjelaskan:
- Definisi kuota dan pelamar.
- Rumus rasio persaingan.
- Perbedaan rasio persaingan per lowongan dan rasio persaingan agregat.
- Keterbatasan korelasi antara kuota dan pelamar.
- Arti kategori peluang dari sumber, jika definisinya sudah diverifikasi.

Hindari tooltip yang menyatakan sebab-akibat atau peluang diterima secara pasti.

## 7. Interaksi Grafik

Jika grafik mendukung pemilihan titik atau kategori:
- Jelaskan apakah pemilihan memfilter halaman atau hanya menyoroti data.
- Sediakan cara membatalkan pilihan.
- Pastikan seleksi tidak membuat KPI menggunakan denominator yang berbeda secara tersembunyi.
- Berikan label atau tabel pendamping untuk membantu aksesibilitas.

## 8. Penanganan Data Tidak Tersedia

- Nilai kosong tidak boleh ditampilkan sebagai nol kecuali nol memang nilai yang tercatat.
- Gunakan label seperti “Tidak tersedia” atau “Tidak diketahui” bila tepat.
- Jangan mengarang kategori untuk mengisi data kosong.
- Jika data lokasi tidak dapat dipetakan, jelaskan apakah baris tersebut dikeluarkan dari peta atau dimasukkan ke kategori lokasi tidak diketahui.

## 9. Batasan Filter

Jangan menambahkan filter berdasarkan:
- Jenis instansi pemerintah/swasta, sampai klasifikasinya tervalidasi.
- Kategori posisi seperti IT/Data atau Kesehatan, sampai pemetaan kategorinya disusun dan divalidasi.

Filter jurusan dan jenjang harus dirancang agar satu lowongan yang memiliki beberapa nilai tidak dihitung berulang pada KPI agregat.
"""