# Business Questions — MagangHub Batch 2 2026

Dokumen ini berisi daftar business questions yang digunakan sebagai acuan proses Exploratory Data Analysis (EDA) dan penyusunan Dashboard MagangHub Batch 2 2026.

---

## BQ1 — Karakteristik Umum Lowongan

**Tujuan:** memberikan overview skala dan karakteristik dataset.

- Berapa jumlah total lowongan yang tersedia?
- Berapa total kuota peserta yang tersedia?
- Berapa total pelamar yang tercatat?
- Berapa rata-rata kuota per lowongan?
- Berapa rata-rata pelamar per lowongan?
- Bagaimana distribusi jumlah pelamar dan kuota antar-lowongan?

---

## BQ2 — Tingkat Persaingan

**Indikator:**

$$
Competition\ Ratio = \frac{Total\ Pelamar}{Total\ Kuota}
$$

- Berapa total pelamar dibandingkan total kuota?
- Berapa rata-rata pelamar untuk setiap kuota?
- Bagaimana distribusi `competition_ratio` antar-lowongan?
- Lowongan mana yang memiliki tingkat persaingan paling tinggi?
- Lowongan mana yang memiliki jumlah pelamar paling besar?

> `Competition Ratio` adalah indikator jumlah pelamar relatif terhadap kuota, bukan probabilitas diterima.

---

## BQ3 — Perbandingan Instansi Pemerintah vs Swasta

**Perbandingan mencakup:** jumlah lowongan, total kuota, total pelamar, rata-rata kuota/lowongan, rata-rata pelamar/lowongan, competition ratio.

> Apakah terdapat perbedaan karakteristik antara kesempatan magang dari instansi pemerintah dan swasta?

Bersifat deskriptif — tidak digunakan untuk menyimpulkan superioritas salah satu jenis instansi.

---

## BQ4 — Distribusi Wilayah (Lowongan & Pelamar)

**Tingkat analisis:** Provinsi, Kabupaten/Kota.

**Indikator:** jumlah lowongan, total kuota, total pelamar.

- Wilayah mana yang memiliki jumlah lowongan paling banyak?
- Wilayah mana yang memiliki total kuota paling besar?
- Wilayah mana yang memiliki jumlah pelamar paling tinggi?

Divisualisasikan dengan grafik dan peta.

---

## BQ5 — Wilayah dengan Tingkat Persaingan Tertinggi

$$
Competition\ Ratio_{wilayah} = \frac{\sum Pelamar}{\sum Kuota}
$$

- Wilayah mana yang memiliki jumlah pelamar per kuota paling tinggi?
- Apakah wilayah dengan jumlah lowongan tinggi juga memiliki persaingan tinggi?
- Bagaimana persebaran tingkat persaingan antarwilayah?

---

## BQ6 — Posisi dengan Peluang & Peminat Terbesar

**Indikator:** jumlah lowongan per posisi, total kuota per posisi, total pelamar per posisi, competition ratio per posisi.

- Posisi apa yang paling banyak tersedia?
- Posisi apa yang memiliki total kuota terbesar?
- Posisi apa yang memiliki jumlah pelamar terbesar?
- Bagaimana perbandingan jumlah kesempatan dengan jumlah peminat per posisi?

> Nama posisi dipertahankan asli, tanpa pengelompokan kategori (IT, Business, Healthcare, dll.) kecuali taxonomy jelas dapat ditentukan pada tahap lanjutan.

---

## BQ7 — Jurusan dengan Akses Peluang Paling Luas

- Jurusan apa yang muncul pada paling banyak lowongan?
- Berapa banyak kesempatan yang dapat diakses masing-masing jurusan?
- Jurusan apa yang memiliki variasi posisi/instansi paling luas?

> Menggambarkan ketersediaan lowongan yang mencantumkan suatu jurusan sebagai syarat, bukan jumlah mahasiswa yang benar-benar mendaftar.

---

## BQ8 — Distribusi Berdasarkan Jenjang Pendidikan

**Perbandingan:** jumlah lowongan Diploma, jumlah lowongan Sarjana, kombinasi jenjang, total kuota per jenjang.

> Bagaimana distribusi kesempatan magang berdasarkan jenjang pendidikan yang dipersyaratkan?

---

## BQ9 — Hubungan Kuota dan Pelamar (Supply & Demand)

- Apakah lowongan dengan kuota besar cenderung memiliki lebih banyak pelamar?
- Apakah ada lowongan berkuota kecil tapi pelamar sangat tinggi?
- Apakah ada lowongan berkuota besar tapi pelamar relatif rendah?
- Bagaimana posisi tiap lowongan berdasarkan kombinasi kuota & pelamar (scatter plot)?

Bersifat eksploratif — bukan untuk menyimpulkan hubungan sebab-akibat.

---

## BQ10 — Pola Jadwal Kerja *(tambahan/opsional)*

- Bagaimana distribusi jumlah hari kerja/minggu pada lowongan magang (5 vs 6 hari)?
- Apakah pola ini berbeda antara instansi pemerintah vs swasta, atau antar posisi/sektor?

---

## BQ11 — Validasi Label Peluang Platform *(tambahan/opsional)*

- Bagaimana distribusi kategori peluang ("Peluang Besar/Sedang/Kecil") yang ditampilkan platform?
- Apakah label tersebut konsisten dengan `competition_ratio` yang dihitung secara independen?

---

## BQ12 — Instansi dengan Lowongan Terbanyak *(tambahan/opsional)*

- Instansi/organizer mana yang membuka lowongan magang paling banyak?
- Bagaimana total kuota dan total pelamar pada instansi-instansi tersebut (Top-N)?

---

## BQ13 — Korelasi Jumlah Jurusan Diterima vs Persaingan *(tambahan/opsional)*

- Apakah lowongan yang menerima lebih banyak jurusan (lebih fleksibel) cenderung memiliki competition ratio lebih tinggi?

---

## BQ14 — Korelasi Jenjang Pendidikan vs Persaingan *(tambahan/opsional)*

- Bagaimana perbandingan competition ratio antara lowongan jenjang Diploma vs Sarjana vs kombinasi?

---

## Ringkasan

| ID    | Business Question                                                        | Fokus Analisis              |
| ----- | -------------------------------------------------------------------------- | ---------------------------- |
| BQ1   | Karakteristik umum lowongan                                               | Overview                     |
| BQ2   | Tingkat persaingan lowongan                                               | Competition                  |
| BQ3   | Perbandingan instansi pemerintah vs swasta                                | Institution                  |
| BQ4   | Wilayah dengan lowongan & pelamar tertinggi                               | Geographic                   |
| BQ5   | Wilayah dengan tingkat persaingan tertinggi                               | Geographic & Competition     |
| BQ6   | Posisi dengan peluang & peminat terbesar                                  | Position                     |
| BQ7   | Jurusan dengan akses peluang paling luas                                  | Major                        |
| BQ8   | Distribusi berdasarkan jenjang pendidikan                                 | Education                    |
| BQ9   | Hubungan kuota dan pelamar                                                | Supply & Demand              |
| BQ10* | Pola jadwal kerja                                                         | Work Schedule                |
| BQ11* | Validasi label peluang platform                                          | Opportunity Label Validation |
| BQ12* | Instansi dengan lowongan terbanyak                                        | Institution (Top-N)          |
| BQ13* | Korelasi jumlah jurusan vs persaingan                                    | Major & Competition          |
| BQ14* | Korelasi jenjang pendidikan vs persaingan                                | Education & Competition      |

`*` = pertanyaan tambahan/opsional.