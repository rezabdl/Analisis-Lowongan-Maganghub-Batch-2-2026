"02_BUSINESS_QUESTIONS.md": r"""# 02 — Business Questions dan Status Analisis
## MagangHub Batch 2 2026

Dokumen ini menjadi acuan untuk menentukan konten dashboard. Status berikut membedakan BQ yang sengaja tidak dilanjutkan dari BQ yang hasil akhirnya masih harus dicocokkan dengan notebook final.

## Ringkasan status

| BQ | Topik | Status | Aturan untuk dashboard |
|---|---|---|---|
| BQ1 | Karakteristik umum lowongan | Periksa notebook final | Tampilkan hanya KPI/analisis yang benar-benar dihitung |
| BQ2 | Tingkat persaingan | Periksa notebook final | Gunakan definisi competition ratio pada dokumen 05 |
| BQ3 | Pemerintah vs swasta | **Tidak dilanjutkan** | Jangan tampilkan perbandingan atau insight klasifikasi instansi |
| BQ4 | Persebaran geografis | Periksa notebook final | Tampilkan hanya level wilayah dan metrik yang sudah divalidasi |
| BQ5 | Persaingan berdasarkan wilayah | Periksa notebook final | Rasio wilayah harus dihitung dari total pelamar/total kuota |
| BQ6 | Posisi dengan peluang dan peminat terbesar | **Tidak dilanjutkan dalam bentuk kategori pekerjaan** | Jangan membuat kategori IT/Data, Kesehatan, dan sejenisnya tanpa klasifikasi tervalidasi |
| BQ7 | Posisi dengan persaingan tertinggi | Periksa notebook final | Tampilkan hanya jika agregasi posisi benar-benar dikerjakan dan diverifikasi |
| BQ8 | Akses berdasarkan jurusan/jenjang | Periksa notebook final | Perhatikan lowongan multi-jurusan/multi-jenjang |
| BQ9 | Hubungan kuota dan pelamar | Analisis tercatat di notebook; verifikasi angka final | Scatter plot dan statistik hanya memakai data final yang valid |
| BQ10 | Distribusi hari kerja per minggu | Analisis visualisasi telah dibahas; verifikasi notebook final | Tampilkan distribusi aktual, jangan mengasumsikan hanya dua kategori tanpa audit |

**Penting:** label “Periksa notebook final” bukan klaim bahwa seluruh BQ tersebut sudah selesai. Sebelum implementasi, OpenCode harus memeriksa notebook dan menandai status akhir berdasarkan bukti yang tersedia.

## BQ1 — Karakteristik Umum Lowongan
**Pertanyaan:** Bagaimana karakteristik umum lowongan berdasarkan jumlah lowongan, kuota, pelamar, serta rata-rata kuota dan pelamar per lowongan?

**Kandidat metrik:** jumlah lowongan unik, total kuota, total pelamar, rata-rata kuota, rata-rata pelamar.

**Aturan:** gunakan hanya metrik yang sudah dihitung dan tervalidasi dalam notebook final.

## BQ2 — Tingkat Persaingan
**Pertanyaan:** Seberapa tinggi persaingan berdasarkan jumlah pelamar dibandingkan kuota?

**Metrik yang disarankan:** competition ratio agregat = total pelamar / total kuota.

**Aturan:** jangan menyebut rasio ini sebagai probabilitas penerimaan individu.

## BQ3 — Perbandingan Instansi Pemerintah vs Swasta
**Status: tidak dilanjutkan.**

Alasan: tidak ada klasifikasi instansi pemerintah/swasta yang tervalidasi. Proyek tidak memiliki dasar yang cukup untuk menetapkan kategori tersebut hanya dari nama instansi.

**Aturan dashboard:** jangan menampilkan chart, KPI, atau insight perbandingan pemerintah vs swasta. Jangan membuat label berdasarkan tebakan. BQ ini boleh dicantumkan di Methodology sebagai analisis yang tidak dilanjutkan beserta alasannya.

## BQ4 — Persebaran Geografis
**Pertanyaan:** Bagaimana persebaran lowongan dan metrik terkait antarwilayah?

**Aturan:** gunakan kolom lokasi yang telah dibersihkan dan level wilayah yang berhasil dicocokkan dengan data geografis. Jika GeoJSON belum tervalidasi, jangan menampilkan peta seolah-olah akurat.

## BQ5 — Persaingan Berdasarkan Wilayah
**Pertanyaan:** Wilayah mana yang menunjukkan rasio persaingan tertinggi?

**Metrik:** total pelamar wilayah / total kuota wilayah.

**Aturan:** tampilkan konteks jumlah lowongan, kuota, dan pelamar agar wilayah dengan volume kecil tidak mudah disalahartikan.

## BQ6 — Posisi dengan Peluang dan Peminat Terbesar
**Status: tidak dilanjutkan dalam bentuk kategorisasi pekerjaan.**

Alasan: analisis yang direncanakan membutuhkan pemrosesan untuk mengelompokkan posisi menjadi kategori seperti IT/Data, Kesehatan, dan lainnya. Klasifikasi tersebut tidak dilakukan dalam notebook.

**Aturan dashboard:** jangan membuat kategori pekerjaan atau menyajikan kesimpulan berdasarkan kategori tersebut. Jangan menyatakan bahwa BQ ini telah dijawab melalui analisis kategori yang tidak ada. Jika notebook memuat analisis posisi individual yang terpisah, verifikasi dan beri nama pertanyaan sesuai metrik sebenarnya sebelum memasukkannya.

## BQ7 — Posisi dengan Persaingan Tertinggi
**Pertanyaan:** Posisi apa yang menunjukkan rasio pelamar terhadap kuota tertinggi?

**Aturan:** hanya implementasikan jika notebook benar-benar memuat agregasi posisi yang tervalidasi. Rasio per posisi dihitung sebagai total pelamar posisi / total kuota posisi, bukan rata-rata sederhana rasio setiap lowongan.

## BQ8 — Akses Berdasarkan Jurusan dan Jenjang
**Pertanyaan:** Jurusan atau jenjang apa yang paling banyak tercantum dalam kesempatan magang?

**Aturan:** periksa hasil analisis final terlebih dahulu. Satu lowongan dapat mencantumkan banyak jurusan atau jenjang; jelaskan apakah hitungan berdasarkan lowongan unik, kemunculan, atau kuota.

## BQ9 — Hubungan Kuota dan Pelamar
**Pertanyaan:** Bagaimana hubungan kuota yang tersedia dengan jumlah pelamar?

Analisis yang direncanakan mencakup scatter plot dengan X=kuota dan Y=pelamar, serta identifikasi kombinasi kuota/pelamar. Nilai Pearson `r = 0.743` pernah tercatat pada EDA, tetapi harus diverifikasi kembali terhadap dataset final sebelum ditampilkan.

**Aturan:** korelasi positif bukan bukti sebab-akibat. Statistik dan garis tren harus dihitung dari observasi valid yang sama dengan chart.

## BQ10 — Distribusi Hari Kerja
**Pertanyaan:** Bagaimana distribusi jumlah hari kerja per minggu pada lowongan magang, termasuk kategori 5 dan 6 hari jika tersedia?

**Aturan:** hitung jumlah dan persentase dari data hari kerja yang valid. Periksa semua kategori aktual; jangan menganggap kategori lain tidak ada tanpa audit.

## Aturan implementasi lintas-BQ
1. Notebook EDA final menjadi sumber kebenaran hasil analisis.
2. Jangan menambahkan chart untuk BQ yang belum dijawab.
3. Angka dari mockup hanya ilustrasi dan tidak boleh tampil sebagai data produksi.
4. Bila BQ tidak dilanjutkan, dokumentasikan sebagai keterbatasan, bukan nilai nol.
5. Bila sebuah BQ baru sebagian dianalisis, tampilkan hanya bagian yang benar-benar didukung.
"""