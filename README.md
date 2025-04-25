# Laporan Proyek Machine Learning: Prediksi Total Pengeluaran

**Nama Proyek**: Spend Analysis Prediction  
**Pendekatan**: Regresi  
**Target**: TotalCost
**dataset**: https://www.kaggle.com/datasets/shahriarkabir/company-purchasing-dataset

---

## 1. Pendahuluan
Dalam pengelolaan anggaran perusahaan, penting untuk memahami faktor-faktor yang memengaruhi total pengeluaran dari tiap transaksi. Dengan prediksi yang akurat, perusahaan dapat mengelola anggaran dan negosiasi dengan supplier secara lebih efisien.

---

## 2. Problem Domain
- **Masalah**: Prediksi total biaya pembelian (`TotalCost`) berdasarkan data transaksi.
- **Solusi**: Model regresi untuk memprediksi nilai `TotalCost`.
- **Manfaat**: Menyediakan insight terhadap pengeluaran berdasarkan jenis barang, supplier, dan pembeli.

---

## 3. Data Understanding
Dataset terdiri dari 9 kolom:
- `TransactionID`: ID transaksi
- `ItemName`: Nama barang
- `Category`: Kategori barang
- `Quantity`: Jumlah barang
- `UnitPrice`: Harga satuan
- `TotalCost`: Harga total (target)
- `PurchaseDate`: Tanggal pembelian
- `Supplier`: Pemasok
- `Buyer`: Pembeli

---

## 4. Exploratory Data Analysis (EDA)
Analisis deskriptif dilakukan untuk memahami struktur dan pola dalam data:
- **Distribusi `TotalCost`** menunjukkan sebaran target yang cukup lebar, dengan kemungkinan outlier.
- **Heatmap Korelasi** menunjukkan korelasi positif yang kuat antara `Quantity` dan `TotalCost`.
- **Boxplot** menunjukkan variasi harga per kategori barang.
- Tidak ditemukan missing value pada dataset.

Contoh visualisasi yang digunakan:
- Histogram distribusi `TotalCost`
- Heatmap korelasi
- Boxplot `UnitPrice` per `Category` 

---

## 5. Data Preparation
Langkah-langkah:
- Encode kolom kategorikal: `Category`, `Supplier`, `Buyer`
- Gunakan fitur numerik dan kategorikal yang sudah di-encode
- Split data menjadi training dan testing

---

## 6. Modeling
Model utama yang digunakan adalah **Random Forest Regressor**.

---

## 7. Evaluation
Evaluasi dilakukan menggunakan:
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- R² Score

---

## 8. Kesimpulan
Model berhasil memprediksi total pengeluaran berdasarkan fitur `Category`, `Quantity`, `UnitPrice`, `Supplier`, dan `Buyer`.

Saran Langkah selanjutnya:
- Coba model lain seperti Linear Regression, XGBoost
- Tuning hyperparameter
- Tambah visualisasi untuk membandingkan prediksi vs real