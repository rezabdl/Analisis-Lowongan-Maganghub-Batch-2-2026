"05_METRIC_DEFINITIONS.md": r"""# 05 — Metric Definitions
## MagangHub Batch 2 2026

Dokumen ini menetapkan definisi metrik yang boleh digunakan dashboard. Seluruh angka produksi harus dihitung dari dataset aktual dan diverifikasi terhadap notebook EDA.

## 1. Jumlah lowongan
Jumlah lowongan unik pada cakupan data atau filter aktif. Gunakan ID/aturan identitas yang tervalidasi. Nama posisi saja belum tentu unik.

## 2. Total kuota
Jumlah nilai `kuota` yang valid pada cakupan analisis. Dokumentasikan bagaimana missing atau nilai invalid diperlakukan.

## 3. Total pelamar
Jumlah nilai `pelamar` yang valid pada cakupan analisis. Sebut sebagai jumlah pelamar tercatat; jangan menganggap semua nilai merupakan individu unik lintas lowongan tanpa bukti.

## 4. Rata-rata per lowongan
- Rata-rata kuota = total kuota valid / jumlah lowongan dengan kuota valid.
- Rata-rata pelamar = total pelamar valid / jumlah lowongan dengan pelamar valid.

Tampilkan denominator atau catatan jika missing values menyebabkan jumlah lowongan berbeda.

## 5. Competition ratio
### Per lowongan
`competition_ratio = pelamar / kuota`, jika kuota valid dan lebih besar dari nol.

### Agregat
`competition_ratio_agregat = total pelamar / total kuota`, jika total kuota lebih besar dari nol.

Gunakan rasio agregat untuk membandingkan kelompok jika analisis tersebut memang tersedia. Jangan mengganti rasio agregat dengan rata-rata sederhana rasio per lowongan.

Interpretasi: rasio 8,7 berarti secara agregat terdapat sekitar 8,7 pelamar tercatat per satu kuota. Rasio ini bukan probabilitas penerimaan individu.

## 6. Estimated acceptance rate
Jika digunakan sebagai metrik eksploratif, rumus matematisnya `kuota / pelamar * 100`, ketika pelamar valid dan lebih besar dari nol. Metrik ini **bukan tingkat penerimaan aktual** dan tidak boleh disamakan dengan label peluang dari platform. Jangan tampilkan jika tidak digunakan atau tidak relevan dengan notebook.

## 7. Label peluang platform
- `peluang_original`: nilai sumber.
- `peluang_kategori`: kategori hasil parsing jika tersedia.
- `peluang_persen`: persentase hasil parsing jika tersedia.

Jangan mengklaim rumus internal platform tanpa sumber yang memverifikasinya. Persentase label peluang tidak otomatis sama dengan acceptance rate aktual.

## 8. Agregasi posisi/wilayah/kelompok
Jika agregasi telah dikerjakan dan masuk ke dashboard:
- jumlah lowongan = jumlah lowongan unik dalam kelompok;
- total kuota = jumlah kuota valid;
- total pelamar = jumlah pelamar valid;
- competition ratio kelompok = total pelamar kelompok / total kuota kelompok.

Jangan menampilkan agregasi untuk kategori yang tidak tersedia atau tidak tervalidasi. Khususnya, jangan membuat metrik pemerintah vs swasta atau kategori pekerjaan IT/Data, Kesehatan, dan sejenisnya pada versi analisis ini.

## 9. Hubungan kuota dan pelamar — BQ9
Scatter plot:
- sumbu X = kuota;
- sumbu Y = pelamar;
- satu titik merepresentasikan satu lowongan pada data yang valid.

Nilai Pearson `r = 0.743` pernah tercatat pada EDA. Verifikasi terhadap dataset final dan subset observasi yang digunakan sebelum menampilkan angka ini di dashboard.

Interpretasi korelasi positif: kuota yang lebih besar cenderung berasosiasi dengan jumlah pelamar yang lebih besar pada data yang dianalisis. Ini bukan bukti bahwa kuota menyebabkan peningkatan pelamar.

Jika menampilkan Spearman, regresi, atau R², hitung dari data yang sama dan dokumentasikan jumlah observasi serta penanganan missing values.

## 10. Analisis kuadran BQ9
Jika analisis kuadran tersedia di notebook:
- X = kuota;
- Y = pelamar;
- batas rendah/tinggi menggunakan median atau aturan yang secara eksplisit telah dipilih dalam notebook.

Kategori:
1. Kuota rendah, pelamar rendah.
2. Kuota rendah, pelamar tinggi.
3. Kuota tinggi, pelamar rendah.
4. Kuota tinggi, pelamar tinggi.

Terapkan aturan konsisten untuk nilai tepat di median. Jika median dihitung setelah filter, jelaskan bahwa batas mengikuti subset aktif.

## 11. Distribusi hari kerja — BQ10
- Hitung jumlah lowongan untuk setiap kategori `jumlah_hari_kerja` yang valid.
- Persentase = jumlah lowongan pada kategori / jumlah lowongan dengan data hari kerja valid × 100%.
- Tampilkan kategori tidak diketahui secara terpisah bila relevan.
- Jangan mengasumsikan hanya ada dua kategori tanpa memeriksa data.

## 12. Jurusan dan jenjang
Jika visualisasi jurusan/jenjang digunakan, nyatakan apakah hitungan berarti:
- jumlah lowongan unik yang mencantumkan nilai tersebut;
- jumlah kemunculan nilai;
- atau total kuota pada lowongan yang menerima nilai tersebut.

Satu lowongan dapat mencantumkan beberapa nilai, sehingga total antar-kategori bisa lebih besar dari total lowongan unik.

## 13. Missing, nol, dan invalid
- Kuota nol: competition ratio per lowongan tidak terdefinisi.
- Pelamar nol: competition ratio dapat nol jika kuota valid; estimated acceptance rate tidak terdefinisi.
- Missing tidak otomatis berarti nol.
- Nilai negatif/invalid harus diperiksa.
- Total kuota kelompok nol atau tidak tersedia: rasio kelompok tidak terdefinisi.
- Jika denominator berbeda, berikan catatan yang jelas.

## 14. KPI global vs filter aktif
Setiap halaman harus jelas apakah angka merupakan:
- angka global seluruh dataset; atau
- angka setelah filter aktif.

Jangan mencampur KPI global dengan chart terfilter tanpa label yang menjelaskan perbedaannya.

## 15. Aturan sumber kebenaran
1. Notebook EDA final dan dataset processed adalah acuan angka.
2. Mockup atau contoh angka bukan hasil produksi.
3. Jangan hard-code statistik hasil analisis.
4. Jika hasil belum tersedia, jangan tampilkan angka yang diperkirakan.
5. BQ yang tidak dilanjutkan harus dinyatakan sebagai di luar cakupan, bukan bernilai nol.
"""
