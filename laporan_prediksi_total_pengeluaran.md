# **Prediksi Total Pengeluaran Berdasarkan Transaksi Pembelian**

## **Domain Permasalahan**
Manajemen pengeluaran merupakan salah satu aspek krusial dalam pengelolaan keuangan perusahaan. Dengan memahami pola pembelian dan mengidentifikasi faktor-faktor yang memengaruhi total pengeluaran, perusahaan dapat mengoptimalkan anggaran, meningkatkan efisiensi pembelian, serta memperkuat posisi dalam negosiasi dengan supplier.

## **Business Understanding**
Proyek ini bertujuan membangun model machine learning yang mampu memprediksi total pengeluaran (`TotalCost`) dari sebuah transaksi berdasarkan atribut seperti kategori barang, jumlah pembelian, harga satuan, supplier, dan pembeli.

Permasalahan dikategorikan sebagai regresi karena target output berupa nilai kontinu (`TotalCost`).

## **Data Understanding**
Dataset yang digunakan merupakan data transaksi pembelian dengan 9 atribut:

- `TransactionID`: ID transaksi
- `ItemName`: Nama barang
- `Category`: Kategori barang
- `Quantity`: Jumlah barang
- `UnitPrice`: Harga satuan
- `TotalCost`: Harga total (target)
- `PurchaseDate`: Tanggal pembelian
- `Supplier`: Pemasok
- `Buyer`: Pembeli

Jumlah sampel: 980 baris data (>= 500, memenuhi syarat)

### Exploratory Data Analysis (EDA)
- Distribusi `TotalCost` menunjukkan rentang nilai yang lebar, terdapat kemungkinan outlier.
- Korelasi positif yang kuat antara `Quantity` dan `TotalCost`.
- Visualisasi rata-rata harga satuan (`UnitPrice`) per kategori menunjukkan perbedaan harga signifikan antar kategori barang.

## **Data Preparation**
- Menangani data kategorikal dengan One-Hot Encoding (`Category`, `Supplier`, `Buyer`)
- Tidak ada missing values
- Split data menjadi 80% training dan 20% testing

## **Modeling**
Model utama yang digunakan adalah **Random Forest Regressor**, dipilih karena kemampuannya menangani data numerik dan kategorikal serta memberikan hasil yang stabil tanpa perlu normalisasi data.

### Training
Model dilatih menggunakan data training (80%).

### Prediksi
Prediksi dilakukan pada data testing (20%).

## **Evaluation**
Model dievaluasi menggunakan metrik:

- **MAE (Mean Absolute Error)**: 135.65 → Rata-rata kesalahan prediksi ±135 satuan
- **RMSE (Root Mean Squared Error)**: 326.99 → Rata-rata kesalahan prediksi sekitar 327 satuan, lebih sensitif terhadap outlier
- **R² Score**: 0.99 → Model mampu menjelaskan 99% variasi dalam `TotalCost`

Hasil evaluasi menunjukkan bahwa model memiliki performa yang sangat baik dan akurat.

## **Model Improvement (Optional)**
Langkah-langkah selanjutnya untuk peningkatan performa:
- Coba algoritma lain seperti Linear Regression dan XGBoost
- Lakukan hyperparameter tuning
- Gunakan teknik feature selection untuk menyaring fitur paling berpengaruh
- Tambahkan fitur turunan seperti `Month` dari `PurchaseDate`

## **Referensi**
- [Scikit-Learn Documentation](https://scikit-learn.org/stable/)
- Dataset: *Company Purchasing Dataset* by Shahriar Kabir (Kaggle)