# 📊 Prediksi Total Pengeluaran Transaksi Pembelian

Proyek ini membangun model Machine Learning untuk memprediksi total biaya pembelian (`TotalCost`) berdasarkan data transaksi perusahaan. Model ini bermanfaat untuk analisis pengeluaran perusahaan dan pengambilan keputusan keuangan.

## 🚀 Tujuan Proyek
Memprediksi nilai `TotalCost` dari sebuah transaksi menggunakan atribut:
- Jumlah barang (`Quantity`)
- Harga satuan (`UnitPrice`)
- Kategori barang (`Category`)
- Supplier
- Buyer

## 🧠 Pendekatan
- Tipe masalah: **Regresi**
- Algoritma: **Random Forest Regressor**
- Metode evaluasi: MAE, RMSE, R² Score

## 📁 Dataset
Dataset digunakan dari [Kaggle - Company Purchasing Dataset](https://www.kaggle.com/datasets/shahriarkabir/company-purchasing-dataset)

Fitur yang digunakan:
- `Category`
- `Quantity`
- `UnitPrice`
- `Supplier`
- `Buyer`

Target: `TotalCost`

Jumlah data: **980 baris**

## 📊 Hasil Evaluasi
| Metrik | Nilai |
|-------|--------|
| MAE   | 135.65 |
| RMSE  | 326.99 |
| R²    | 0.99   |

Model memiliki performa yang sangat baik dalam memprediksi pengeluaran.

## 🛠 Tools & Library
- Python
- Pandas, Numpy
- Matplotlib, Seaborn
- Scikit-learn

## 📌 Struktur Proyek
- `notebook.ipynb` — Notebook utama proyek
- `prediksi_total_pengeluaran.md` — Laporan akhir (sesuai format Dicoding)
- `README.md` — Deskripsi singkat proyek

## 📬 Kontak
Dibuat sebagai bagian dari submission kelas Machine Learning Dicoding 2025.