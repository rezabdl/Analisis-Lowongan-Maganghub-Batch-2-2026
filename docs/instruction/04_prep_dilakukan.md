"04_DATA_PREPARATION.md": r"""
        raise FileNotFoundError(f"Dataset tidak ditemukan: {file_path}")
    return pd.read_csv(file_path)
```# 04 — Data Preparation
## MagangHub Batch 2 2026

Dashboard harus menggunakan dataset hasil preparation yang sudah diperiksa. Hindari menjalankan cleaning berat berulang kali saat halaman Streamlit dirender.

## 1. Tujuan 
- Menyediakan data yang konsisten untuk visualisasi pada dashboard
- mempertahankan satu baris per lowonan pada dataset utama, jika terdapat duplikasi lowongan maka diperbolehkan untuk dihapus.
- melakukan duplikasi terhadap data_eda yang bertujuan duplikat dari data_eda akan digunakan dalam sumber data visualisasi.
- tidak menambahkan klasifikasi tambahan apapun tanpa ada dasar pendukung dari pengklasifikasian tersebut (jika terdapat pengklasifikasian tersebut harus bisa divalidasi untuk cara pengklasifikasiannya)

## 2. Alur Preparation (sudah saya lakukan)
- dataset sumber berasal dari `data/raw/data_lowongan/data_gabungan` untuk data lowongan hasil scraping, untuk data geo jsonnya ada di `D:\Developments\Riset Pribadi\Maganghub\data\geojson\GeoJson-Indonesia-38-Provinsi\Provinsi\38 Provinsi Indonesia - Provinsi.json` untuk data geo json provinsi dan untuk geo_json kabupaten ada di `D:\Developments\Riset Pribadi\Maganghub\data\geojson\GeoJson-Indonesia-38-Provinsi\Kabupaten\38 Provinsi Indonesia - Kabupaten.json`
- sedangkan data pendukung untuk memvalidasi nama_provinsi dan nama_kabupaten itu ada di `data/raw/data_provinsi` didalamnya ada `kabupaten.csv, kecamatan.csv, kelurahan.csv serta provinsi.csv`
jadi untuk nama kabupaten sudah saya seuaikan dengan data di `data/raw/data_provinsi/kabupaten.csv` sedangkan untuk provinsi sudah saya sesuaikan dengan ``D:\Developments\Riset Pribadi\Maganghub\data\geojson\GeoJson-Indonesia-38-Provinsi\Provinsi\38 Provinsi Indonesia - Provinsi.json` jadi sudah siap untuk digunakan dari 2 kolom tersebut 
- untuk beberapa lolom yang sudah ada didalam data_eda itu adalah sebetulnya hasil pemrosesan saya seperti 
* kolom `lokasi` saya decode dijadikan 2 kolom baru yaitu `nama_kabupaten` dan `nama_provinsi` karena jika hanya menggunakan `nama_kabupaten` maka kurang valid untuk menentukan diprovinsi manakah lowongan tersebut dan data kurang lengkap untuk analisis provinsi mana dengan lowongamn terbanyak dan pelamar terbanyak.
* kolom `jenjang` saya decode menjadi 3 kolom baru yaitu `Diploma, Sarjana dan Profesi` karena ketika saya lihat isinya hanyalah nama nama dari tiap Jenjang tersebut, jadi saya hanya perlu untuk melakukan one hot encoding tiap jenjang tersebut menjadikan berisikan boolean 1 atau 0, dengan jika isi dari kolom tersebut adalah 1 maka dapat diartikan lowongan A yang diperbolehkan mendaftar adlaah jenjang Diploma misalnya, jika dari 3 kolom tersebut ada 2 kolom yang berisikan 2 jenjang yang berupa yes, maka dapat diartikan lowongan tersebut bisa menerima 2 jenjang misalnya (Sarjana dan Profesi) dst.
* kolom `hari_kerja`: dilakukan cleansing dengan cara menghapus frasa `hari/minggu`
* kolom `peluang`: saya split menjadi 2 kolom baru menjadi `kategori_peluang` yang berisikan kategori yang sudah diberikan dari pihak maganghub seperti `Peluang Kecil` dst. lalu ada kolom `persentase_peluang` berisikan persentase peluangnya dalam bentuk integer.
* kolom `link` dihapus karena saya rasa kurang relevan untuk analisis ini. 

## 3. Data loading
OpenCode wajib menemukan path dataset yang sebenarnya di repository. Contoh berikut hanya pola implementasi, bukan path final:

```python
from pathlib import Path
import pandas as pd
import streamlit as st

@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    file_path = Path(path)
    if not file_path.exists():

Sesuaikan pembacaan dengan format aktual format yang digunakan dalam analisis ini adalah csv dan geo_json.

## 4. Jenis instansi
Klasifikasi pemerintah/swasta **tidak dilakukan dalam analisis final saat ini** karena belum ada dasar klasifikasi yang tervalidasi. Jangan menambahkan kategori berdasarkan tebakan nama organisasi. Jangan menjalankan proses klasifikasi otomatis hanya untuk memenuhi BQ 3.

## 5. Validasi akhir
- Jumlah baris utama tidak berubah secara tidak sengaja.
- Identitas/duplikat diperiksa.
- Tipe data benar.
- Missing dan invalid tercatat.
- Rasio memiliki denominator valid.
- Distribusi hari kerja cocok dengan notebook.
- Normalisasi lokasi dan GeoJSON diverifikasi bila peta digunakan.
- Hasil split jurusan/jenjang tidak menggandakan metrik.
- BQ yang tidak dianalisis tidak dibuatkan hasil tiruan.
- KPI dashboard cocok dengan notebook final.

## 6. Output
Output preparation dapat terdiri dari:
- dataset utama processed;
- dataset turunan jurusan/jenjang jika diperlukan;
- mapping lokasi jika tervalidasi;
- laporan validasi;
- dokumentasi kolom dan definisi metrik.

Nama file dan path final harus ditemukan dari repository, bukan ditebak.