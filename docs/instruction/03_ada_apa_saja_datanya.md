"ada_apa_daja_datanya.md": r"""# 03 — Data Dictionary
## MagangHub Batch 2 2026

Dokumen ini merangkum kolom sumber yang diketahui dan kolom turunan yang mungkin digunakan. Nama kolom, tipe, serta ketersediaan final wajib diverifikasi pada dataset processed di repository.

## 1. Unit analisis
Dataset utama menggunakan prinsip **satu baris = satu lowongan**. Jangan melakukan transformasi yang menggandakan baris utama dan mengubah total kuota/pelamar.

## 2. Kolom dataset awal 
jadi dataset raw lowongan itu terdapat 11 kolom yaitu 
- posisi: ama posisi atau lowongan yang dicari/diupload dari instansi terkait
- instansi: nama lembaga/perusahaan dsb sebagai penyelenggara dari lowongan tersebut
- jurusan: berisikan kumpulan nama jurusan yang diperbolehkan melar pada posisi tertentu berdasarkan ketentuan tiap instansi terkait.
- lokasi: alamat dari instansi yang menerbitkan lowongan (alamat tersebut hanyalah berisikan nama kabupaten/kota dari lowongan tersebut)
- jenjang: berupa jenis jenjang yang bisa mendaftar kedalam lowongan tersebut, bisa berisikan lebih dari 1 jenjang (isinya bisa Diploma, Sarjana dan Profesi)
- hari_kerja: jumlah hari kerja dari posisi tersebut (5hari/minggu) atau (6hari/minggu)
- kuota: jumlah yang dibutuhkan dari lowongan tersebut
- pelamar: jumlah yang melamar ke lowongan tersebut
- peluang: klasifikasi peluang ( Peluang Kecil atau dsb ) dan dibarengi dengan persentase hasil perhitungan dari (kuota/(1+pelamar))
- hari_libur: merupakan kumpulan nama hari untuk libur bekerja bisa berisikan >1 nama hari (umumnya berisikan Sabtu. Minggu ) 
- link: link dari lowongan yang ditempatkan dalam sebuah website maganghub 

### 1. Kolom dataset siap digunakan
jadi untuk datanya itu ada 15 kolom hasil yang sudah saya preparationkan dan sudah dipastikan tidak ada duplicate serta missing valuenya.
15 Kolom tersebut adalah
- posisi: nama posisi atau lowongan yang dicari/diupload dari instansi terkait
- instansi: nama lembaga/perusahaan dsb sebagai penyelenggara dari lowongan tersebut
- jurusan: berisikan kumpulan nama jurusan yang diperbolehkan melar pada posisi tertentu berdasarkan ketentuan tiap instansi terkait.
- nama_kabupaten: nama kabupaten dari instansi yang memposting lowongan.
- nama_provinsi: nama provinsi dari instansi yang memposting lowongan. 
- Diploma: lowongan tersebut bisa dilamar oleh lulusan Diploma, isinya boolean (1= yes dan 0= no)
- Sarjana: lowongan tersebut bisa dilamar oleh lulusan Sarjana, isinya boolean (1=yes dan 0=no)
- Profesi: lowongan tersebut bisa dilamar oleh lulusan Profesi, isinya bolean (1=yes dan 0=no)
- hari kerja: berupa angka saja jumlah hari kerja per minggu yaitu 5 atau 6 per minggu.
- kuota: suatu lowongan itu bisa diisi sekian orang yang ditentukan oleh instansi terkait.
- pelamar: jumlah pelamar yang melamar kedalam sebuah posisi tersebut dalam batch 2.
- hari libur: hari libur itu hanya berupa nama hari umumnya adalah "Sabtu, Minggu"
- persentase_peluang: persentase peluang itu adalah berasal dari website maganghub dengan perhitungan (kuota/(1+jumlah pelamar)), berupa angka integer bukan float.
- kategori_peluang: itu didapatkan dari website maganghub, jadi mereka sudah mengkategorikannya sendiri, jika memungkinkan untuk dibuatkan dictionarynya jadi mungkin bisa dibuatkan saja untuk mengetahui parameternya itu seperti apa kok dia bisa dikategorikan seperti pada kolom saya. berarti memanfaatkan kolom persentase_peluang untuk menemukan/membuat dictionarynya 
- competition_ratio: didapatkan rasio berdasarkan perhitungan (kuota/pelamar)

Jangan menambahkan `jenis_instacnsi` sebagai fitur analisis final kecuali ada sumber klasifikasi yang dapat dipertanggungjawabkan. Jangan menambahkan kategori pekerjaan seperti IT/Data atau Kesehatan sebagai fakta jika klasifikasi belum dilakukan.


## 3. Multi-value: jurusan, hari_libur
Jurusan dan jenjang dapat memuat beberapa nilai dalam satu lowongan. Dataset utama dapat memisahkannya menjadi `jurusan_1 ... jurusan_n` dan `jenjang_1 ... jenjang_n` jika sesuai dengan proses preparation yang sudah dipilih. untuk hari libur isinya adalah `Sabtu, Minggu` atau `Sabtu` ataupun hanya `Minggu`

## 4. Khusus kolom `kategori_peluang`
pada kolom tersebut isinya hanyalah jenis kategorinya dari hasil pengkategorian berdasarkan persentase peluang yang dibuat oleh pihak maganghub

Untuk analisis khusus, dataset turunan long format boleh dibuat, tetapi:
- jangan menggandakan dataset utama;
- jangan menjumlahkan kuota/pelamar berulang kali akibat satu lowongan muncul pada beberapa jurusan;
- dokumentasikan apakah metrik menghitung lowongan unik, kemunculan, atau kuota.

## 5. Lokasi dan geometri
Kolom `kab_kota` dan `provinsi` hanya boleh digunakan jika hasil normalisasi dapat diverifikasi. Untuk peta, periksa properti GeoJSON dan hasil join. Jangan menyajikan peta jika kecocokan wilayah belum memadai. namun sudah saya cek untuk kolom tersebut sudah saya mormalisasi dan samakan tiap nama kabupaten maupun provinsinya agar mempermudah dalam membuat plotnya ya

untuk memastikan 