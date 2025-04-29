# Laporan Proyek Machine Learning: Prediksi Total Pengeluaran Bulanan

## 1. Pendahuluan

Proyek ini bertujuan untuk memprediksi total pengeluaran bulanan berdasarkan data transaksi yang tersedia. Metode yang digunakan adalah Long Short-Term Memory (LSTM), salah satu jenis Recurrent Neural Network (RNN) yang efektif untuk memproses data time series.

## 2. Dataset

Dataset berisi **500 data transaksi** dengan **9 kolom**. Kolom target adalah `TotalCost`, sedangkan kolom `PurchaseDate` digunakan sebagai acuan waktu.

### Informasi Dataset:
- Tidak terdapat nilai kosong (missing value).
- Data difokuskan hanya pada kolom `PurchaseDate` dan `TotalCost`.
- Data diresemple menjadi total per bulan untuk keperluan prediksi time series.

## 3. Exploratory Data Analysis (EDA)

Beberapa langkah EDA dilakukan untuk memahami karakteristik data:
- Distribusi `TotalCost` menunjukkan adanya outlier.
- Korelasi antara `Unitprice` dan `TotalCost` cukup kuat, menunjukkan bahwa harga unit berpengaruh besar terhadap pengeluaran.

## 4. Data Preparation

- Kolom `PurchaseDate` dikonversi ke datetime dan dijadikan index.
- Data diresample ke bentuk bulanan.
- Dilakukan scaling menggunakan `MinMaxScaler`.
- Dibuat window time series untuk data training dan testing.

## 5. Model Development

### Model: LSTM

#### Cara Kerja:
LSTM dirancang untuk mengingat informasi dalam jangka panjang. Sangat cocok untuk data berurutan seperti time series karena mampu menangkap pola musiman.

#### Arsitektur:
- LSTM dengan 64 unit dan aktivasi ReLU
- Output layer: Dense(1)
- Optimizer: Adam
- Loss Function: Mean Squared Error (MSE)
- Epoch: 130
- Parameter lain menggunakan nilai default.

## 6. Evaluasi Model

### Metrik Evaluasi:

- **MAE (Mean Absolute Error)**: Mengukur rata-rata selisih absolut antara prediksi dan nilai sebenarnya.
- **RMSE (Root Mean Squared Error)**: Memberikan penalti lebih besar terhadap error yang besar (lebih sensitif terhadap outlier).

### Hasil Evaluasi:

- **MAE: 4589.25**
- **RMSE: 4760.40**

### Interpretasi:
Model memiliki performa yang cukup baik, dengan kesalahan prediksi rata-rata sekitar 4,5 ribuan satuan. RMSE yang relatif kecil menunjukkan performa model yang stabil dan akurat.
## 7. Kesimpulan

Model LSTM mampu memprediksi total pengeluaran bulanan dengan cukup akurat. Ke depan, performa dapat ditingkatkan dengan tuning parameter, penambahan fitur tambahan, atau eksplorasi model time series lainnya seperti GRU atau Prophet.