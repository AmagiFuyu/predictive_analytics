# Proyek Machine Learning: Prediksi Total Pengeluaran Bulanan dengan LSTM

## Domain Proyek

Dalam pengelolaan bisnis, salah satu tantangan utama adalah mengontrol dan memprediksi pengeluaran operasional secara akurat. Ketidakpastian dalam proyeksi anggaran bisa berdampak besar terhadap efisiensi keuangan perusahaan. Oleh karena itu, perusahaan membutuhkan sistem yang dapat membantu dalam melakukan prediksi pengeluaran berdasarkan data historis transaksi. Pemanfaatan teknologi machine learning, khususnya pendekatan time series forecasting dengan LSTM, menawarkan solusi untuk mempelajari pola pengeluaran dari masa lalu guna meramalkan pengeluaran di masa depan. Dengan prediksi yang akurat, perusahaan dapat mengelola anggaran lebih efisien, menghindari pemborosan, dan mendukung pengambilan keputusan strategis.

## Business Understanding

### Problem Statement
Perusahaan mengalami kesulitan dalam memprediksi pengeluaran bulanannya akibat fluktuasi dalam volume transaksi pembelian. Hal ini menyulitkan dalam menyusun perencanaan anggaran dan strategi pengadaan.

### Goals
Membangun model prediksi yang dapat mengestimasi total pengeluaran bulanan perusahaan berdasarkan data historis transaksi. Tujuannya adalah untuk:
- Memberikan estimasi pengeluaran dengan akurasi tinggi.
- Meminimalisasi risiko pemborosan anggaran.
- Mendukung pengambilan keputusan berbasis data.

### Solution Statement
Solusi yang diusulkan adalah membangun model Long Short-Term Memory (LSTM) untuk memprediksi total pengeluaran bulanan berdasarkan data time series dari transaksi pembelian. Model ini akan dilatih dari data historis dan digunakan sebagai alat bantu untuk divisi keuangan dalam menyusun anggaran.

## Data Understanding

### Sumber Data
Dataset yang digunakan adalah "Company Purchasing Dataset" yang tersedia di Kaggle:  
🔗 https://www.kaggle.com/datasets/shahriarkabir/company-purchasing-dataset

### Jumlah Data
- **Baris (rows):** 500
- **Kolom (columns):** 9

### Kondisi Data
- **Missing values:** Tidak ditemukan.
- **Data duplikat:** Tidak ada duplikasi.
- **Outlier:** Terdapat outlier pada kolom `TotalCost`, teridentifikasi melalui EDA.

### Deskripsi Fitur
- `TransactionID`: ID unik untuk setiap transaksi
- `ItemName`: Nama barang yang dibeli
- `Category`: Kategori barang
- `Quantity`: Jumlah unit barang yang dibeli
- `UnitPrice`: Harga satuan barang
- `TotalCost`: Biaya total untuk transaksi (Quantity × UnitPrice)
- `PurchaseDate`: Tanggal pembelian (digunakan sebagai penanda waktu)
- `Supplier`: Pemasok barang
- `Buyer`: Nama pembeli

Hanya kolom `PurchaseDate` dan `TotalCost` yang digunakan untuk keperluan prediksi time series.

## Modeling

### Model yang Digunakan: Long Short-Term Memory (LSTM)

LSTM merupakan jenis Recurrent Neural Network (RNN) yang dirancang khusus untuk menangani data berurutan seperti time series. Keunggulan utama LSTM adalah kemampuannya dalam menangkap pola jangka panjang dan mengatasi masalah vanishing gradient.

### Arsitektur Model
- **Input shape:** 3 time steps (window size)
- **Layer 1:** LSTM dengan 64 unit dan aktivasi ReLU
- **Layer Output:** Dense(1)

### Parameter yang Digunakan
- Optimizer: `adam`
- Loss function: `mean_squared_error`
- Epoch: 130
- Callbacks: EarlyStopping(patience=10)

Model dilatih dengan data pengeluaran bulanan yang telah diskalakan, dan diuji menggunakan data validasi untuk menghindari overfitting.

## Evaluation

### Hasil Evaluasi Model
- **MAE (Mean Absolute Error):** 4589.25
- **RMSE (Root Mean Squared Error):** 4760.40

### Interpretasi dan Dampaknya terhadap Bisnis
Model LSTM yang dikembangkan berhasil mengurangi rata-rata kesalahan prediksi hingga 4.589 satuan, yang menunjukkan performa prediksi yang akurat dan stabil. Prediksi ini membantu divisi keuangan dan pengadaan dalam menyusun rencana anggaran dan melakukan pemesanan dengan lebih terstruktur.

### Apakah Problem Statement Terjawab?
✅ Ya. Model menjawab kebutuhan untuk memprediksi pengeluaran dengan cukup akurat.

### Apakah Goals Tercapai?
✅ Ya. Prediksi yang dihasilkan mampu memberikan informasi awal yang relevan untuk perencanaan bulanan, dengan tingkat kesalahan yang dapat ditoleransi secara bisnis.

### Apakah Solusi Berdampak?
✅ Ya. Model LSTM menunjukkan dampak yang signifikan dalam mengungkap pola pengeluaran dan menghasilkan estimasi yang dapat diandalkan sebagai alat bantu pengambilan keputusan keuangan.

## Kesimpulan

Proyek ini membuktikan bahwa model LSTM efektif dalam memprediksi total pengeluaran bulanan berdasarkan data historis transaksi. Hasil evaluasi menunjukkan bahwa model dapat memberikan estimasi pengeluaran yang akurat dengan tingkat kesalahan yang relatif rendah. Implementasi model ini dapat meningkatkan efisiensi perencanaan keuangan perusahaan.

Langkah selanjutnya yang dapat dilakukan untuk peningkatan adalah:
- Menambahkan fitur eksternal (exogenous features) seperti kategori barang atau supplier.
- Mencoba arsitektur lain seperti GRU atau kombinasi CNN-LSTM.
- Melakukan hyperparameter tuning untuk optimasi performa model.