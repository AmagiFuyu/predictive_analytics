# **Prediksi Total Pengeluaran Berdasarkan Transaksi Pembelian**

## **Domain Permasalahan**
Manajemen pengeluaran merupakan aspek krusial dalam operasional perusahaan. Dengan memahami pola pembelian dan faktor-faktor yang memengaruhi total pengeluaran, perusahaan dapat mengoptimalkan anggaran dan meningkatkan efisiensi.

## **Business Understanding**
### Problem Statements
Perusahaan mengalami tantangan dalam memperkirakan pengeluaran bulanan berdasarkan histori transaksi pembelian. Kesalahan dalam prediksi dapat mengganggu alokasi anggaran dan perencanaan keuangan.

### Goals
Membangun model Machine Learning berbasis time series forecasting yang mampu memprediksi total pengeluaran (`TotalCost`) per bulan di masa depan, menggunakan data historis transaksi pembelian.

## **Data Understanding**
Dataset berasal dari [Kaggle - Company Purchasing Dataset](https://www.kaggle.com/datasets/shahriarkabir/company-purchasing-dataset).

### Jumlah Data
- Jumlah baris: 500
- Jumlah kolom: 9

### Kondisi Data
- Tidak ditemukan missing value.
- Tidak terdapat data duplikat.
- Ditemukan outlier pada kolom `TotalCost` (dianalisis melalui distribusi data).

### Uraian Fitur
- `TransactionID`: ID transaksi
- `ItemName`: Nama barang
- `Category`: Kategori barang
- `Quantity`: Jumlah barang
- `UnitPrice`: Harga satuan
- `TotalCost`: Harga total (target)
- `PurchaseDate`: Tanggal pembelian
- `Supplier`: Pemasok
- `Buyer`: Pembeli

### Exploratory Data Analysis (EDA)
- Distribusi `TotalCost` menunjukkan sebaran yang luas, dengan indikasi adanya outlier.
- Korelasi kuat antara `Quantity` dan `TotalCost`.
- Rata-rata `UnitPrice` berbeda signifikan antar kategori.
- Tren pembelian total per bulan cenderung fluktuatif.

## **Data Preparation**
- Konversi `PurchaseDate` menjadi tipe datetime.
- Menjadikan `PurchaseDate` sebagai indeks.
- Resampling data menjadi agregasi bulanan.
- Normalisasi data menggunakan MinMaxScaler.
- Membuat windowed dataset untuk LSTM dengan window size = 3.
- Membagi data menjadi 80% training dan 20% testing.

## **Modeling**
Model yang digunakan adalah **LSTM (Long Short-Term Memory)**.

### Arsitektur Model
- Input: 3 time steps
- 1 LSTM layer dengan 64 unit, activation `relu`
- 1 Dense layer sebagai output

### Konfigurasi Training
- Optimizer: Adam
- Loss function: Mean Squared Error (MSE)
- EarlyStopping dengan patience 10
- Maksimal 100 epoch

### Penjelasan LSTM
LSTM efektif dalam mempelajari pola jangka panjang pada data time series karena memiliki mekanisme memory cell yang mengatasi masalah vanishing gradient.

## **Evaluation**
Model dievaluasi menggunakan metrik berikut:

- **Mean Absolute Error (MAE)**: 7108.12  
  → Rata-rata kesalahan prediksi model sekitar ±7108 satuan TotalCost setiap bulannya.

- **Root Mean Squared Error (RMSE)**: 7935.66
  → Rata-rata kesalahan model sekitar 7935 satuan TotalCost, sensitif terhadap outlier.

### Visualisasi
Plot prediksi vs aktual menunjukkan bahwa model mampu **mengikuti pola fluktuasi** pengeluaran bulanan dengan baik, meskipun terdapat sedikit deviasi pada beberapa titik data.

### Insight
Model mampu menghasilkan prediksi yang akurat terhadap tren pengeluaran bulanan, meskipun akurasi bisa ditingkatkan lagi dengan tuning parameter atau penggunaan model lanjutan seperti GRU.

## **Model Improvement (Optional)**
- Menambahkan fitur turunan seperti `Month`, `Quarter`, `Day of Week`.
- Mencoba arsitektur lain seperti GRU.
- Hyperparameter tuning (jumlah neuron, learning rate, batch size).
- Menggunakan lebih banyak data historis untuk memperpanjang sequence input.

## **Referensi**
- [Scikit-Learn Documentation](https://scikit-learn.org/stable/)
- [Keras LSTM Documentation](https://keras.io/api/layers/recurrent_layers/lstm/)
- Dataset: *Company Purchasing Dataset* by Shahriar Kabir (Kaggle)