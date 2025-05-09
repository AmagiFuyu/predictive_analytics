# -*- coding: utf-8 -*-
"""spend_analysis_prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SWNI2xMFOHlEru0aE2U6wRICH2f7iC18

# Proyek Machine Learning: Prediksi Total Pengeluaran Bulanan dengan LSTM

## Domain Proyek

Dalam pengelolaan bisnis, salah satu tantangan utama adalah mengontrol dan memprediksi pengeluaran operasional secara akurat. Ketidakpastian dalam proyeksi anggaran bisa berdampak besar terhadap efisiensi keuangan perusahaan. Oleh karena itu, perusahaan membutuhkan sistem yang dapat membantu dalam melakukan prediksi pengeluaran berdasarkan data historis transaksi. Pemanfaatan teknologi machine learning, khususnya pendekatan time series forecasting dengan LSTM, menawarkan solusi untuk mempelajari pola pengeluaran dari masa lalu guna meramalkan pengeluaran di masa depan. Dengan prediksi yang akurat, perusahaan dapat mengelola anggaran lebih efisien, menghindari pemborosan, dan mendukung pengambilan keputusan strategis.

## Business Understanding

### Problem Statement
Perusahaan mengalami kesulitan dalam memprediksi pengeluaran bulanannya akibat fluktuasi dalam volume transaksi pembelian. Hal ini menyulitkan dalam menyusun perencanaan anggaran dan strategi pengadaan.

Dari pernyataan diatas diusulkan masalah berikut:
1. Bagaimana memprediksi total pengeluaran bulanan berdasarkan histori transaksi pembelian?
2. Bagaimana membantu divisi keuangan menyusun anggaran secara lebih efisien dan akurat?

### Goals
Tujuan Dari Problem Statement tersebut adalah:
1. Mengembangkan model machine learning yang mampu memprediksi total pengeluaran bulanan dengan **MAE < 5000**.
2. Memberikan sistem prediktif berbasis data historis untuk membantu perencanaan anggaran perusahaan.


### Solution Statement
Solusi yang diusulkan adalah membangun model Long Short-Term Memory (LSTM) untuk memprediksi total pengeluaran bulanan berdasarkan data time series dari transaksi pembelian. Model ini akan dilatih dari data historis dan digunakan sebagai alat bantu untuk divisi keuangan dalam menyusun anggaran.

## 1. Import Library

mengimpor berbagai library yang dibutuhkan. Library seperti `pandas` dan `numpy` digunakan untuk manipulasi data, `matplotlib` dan `seaborn` untuk visualisasi data, serta `tensorflow.keras` untuk membangun model deep learning.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.callbacks import EarlyStopping

"""## 2. Load Dataset

memuat dataset transaksi yang akan digunakan untuk analisis dan prediksi.

"""

df = pd.read_csv('/content/spend_analysis_dataset.csv')

"""## 3. Data Understanding
Pada tahapan ini kita melihat struktur awal data.

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

### Menampilkan 5 data teratas
Digunakan untuk melihat struktur awal data.
"""

print(df.head())

"""### Cek informasi dataset
Digunakan untuk mengetahui jumlah kolom, tipe data, dan apakah ada nilai kosong.

"""

print(df.info())

"""### Cek missing values
Penting untuk melihat apakah ada data yang hilang dan perlu ditangani.
"""

print(df.isnull().sum())

"""### Cek duplikat
melihat apakah ada data duplikat
"""

print(df.duplicated().sum())

"""### Exploratory Data Analysis (EDA)
melakukan eksplorasi data

### Statistik Deskriptif
Memberikan gambaran umum distribusi dan nilai-nilai statistik tiap fitur numerik.
"""

df.describe()

"""### Plot distribusi TotalCost
Visualisasi distribusi kolom target (TotalCost) untuk mengidentifikasi outlier dan pola umum.


"""

plt.figure(figsize=(8,4))
sns.histplot(df['TotalCost'], kde=True)
plt.title('Distribusi TotalCost')
plt.xlabel('TotalCost')
plt.ylabel('Frekuensi')
plt.grid()
plt.show()

"""### Korelasi Quantity, UnitPrice, TotalCost
Menampilkan korelasi antar fitur numerik untuk memahami hubungan antar fitur.

"""

plt.figure(figsize=(6,5))
sns.heatmap(df[['Quantity', 'UnitPrice', 'TotalCost']].corr(), annot=True, cmap='coolwarm')
plt.title('Heatmap Korelasi Fitur Numerik')
plt.grid()
plt.show()

"""## 4. Data Preparation
Pada tahap ini dilakukan persiapan data untuk memastikan model dapat dilatih dengan baik.

### Langkah-langkah:
1. **Konversi Tanggal:** Kolom `PurchaseDate` dikonversi ke format datetime.
2. **Set Index:** Kolom tanggal diatur sebagai index agar dapat dilakukan resampling time series.
3. **Agregasi Bulanan:** Data dirangkum menjadi total pengeluaran per bulan menggunakan fungsi `resample('M').sum()`.
4. **Normalisasi:** Nilai `TotalCost` dinormalisasi menggunakan MinMaxScaler agar sesuai dengan input LSTM.
5. **Pembuatan Window Time Series:** Dataset diubah menjadi format sekuensial (window size = 3) agar bisa diproses oleh model LSTM.
6. **Split Dataset:** Dataset dibagi menjadi 80% training dan 20% testing.

Tahapan ini penting untuk memastikan bahwa model menerima input yang relevan dan terstruktur.

### Konversi Kolom Tanggal dan Set Index
Mengubah kolom tanggal menjadi format datetime dan menjadikannya index agar bisa digunakan untuk resampling.
"""

df['PurchaseDate'] = pd.to_datetime(df['PurchaseDate'])
df = df[['PurchaseDate', 'TotalCost']]
df.set_index('PurchaseDate', inplace=True)

"""### Resample Data Bulanan
Mengelompokkan data per bulan agar pola musiman dapat dianalisis.
"""

df_monthly = df.resample('M').sum()

"""### Scaling dan Membuat Windowed Dataset
LSTM membutuhkan data dalam bentuk yang terstandardisasi dan dalam bentuk window time series.
"""

scaler = MinMaxScaler()
df_scaled = scaler.fit_transform(df_monthly)

def create_windowed_dataset(series, window_size):
    X, y = [], []
    for i in range(len(series) - window_size):
        X.append(series[i:i+window_size])
        y.append(series[i+window_size])
    return np.array(X), np.array(y)

window_size = 3
X, y = create_windowed_dataset(df_scaled, window_size)

split_idx = int(len(X)*0.8)
X_train, X_test = X[:split_idx], X[split_idx:]
y_train, y_test = y[:split_idx], y[split_idx:]

"""## 5. Modeling

### Model 1: LSTM

#### Cara Kerja:
LSTM (Long Short-Term Memory) adalah jenis Recurrent Neural Network (RNN) yang digunakan untuk menangani data sekuensial seperti data time series. LSTM memiliki kemampuan untuk mengingat informasi dalam jangka panjang, sehingga cocok untuk prediksi berdasarkan urutan waktu.

#### Arsitektur dan Parameter:
- `LSTM(64, activation='relu')`: Layer LSTM dengan 64 unit dan fungsi aktivasi ReLU.
- `Dense(1)`: Layer output untuk prediksi nilai tunggal.
- Optimizer: `adam`, Loss function: `mse` (Mean Squared Error).
- Parameter lain menggunakan default.
"""

#LTSM
model = Sequential([
    LSTM(64, activation='relu', input_shape=(window_size, 1)),
    Dense(1)
])

model.compile(optimizer='adam', loss='mse')

"""## 6. Training
Model dilatih dengan data training, dan menggunakan early stopping untuk menghentikan pelatihan jika validasi tidak membaik dalam 10 epoch berturut-turut.

"""

history = model.fit(
    X_train, y_train,
    epochs=130,
    validation_data=(X_test, y_test),
    callbacks=[EarlyStopping(patience=10, restore_best_weights=True)],
    verbose=1
)

"""## 7. Evaluasi Model

### Apa itu Metrik Evaluasi?
- **MAE (Mean Absolute Error)**: Rata-rata kesalahan absolut antara nilai aktual dan prediksi. Semakin kecil nilainya, semakin akurat model.
- **RMSE (Root Mean Squared Error)**: Akar dari rata-rata kuadrat kesalahan. Lebih sensitif terhadap outlier daripada MAE.

### Hasil Evaluasi
Model diuji dengan data test. Nilai prediksi dan aktual dikembalikan ke skala aslinya (inverse transform) untuk dihitung metrik evaluasinya.
"""

# Prediksi
y_pred = model.predict(X_test)

"""### Inverse transform hasil prediksi dan y_test

 mengembalikan hasil prediksi (y_pred) dan data aktual (y_test) ke skala aslinya (sebelum dilakukan scaling). Hal ini penting agar kita dapat membandingkan hasil prediksi dengan nilai aktual dalam satuan yang sebenarnya
"""

y_pred_inv = scaler.inverse_transform(np.concatenate((np.zeros((len(y_pred), df_monthly.shape[1]-1)), y_pred), axis=1))[:, -1]
y_test_inv = scaler.inverse_transform(np.concatenate((np.zeros((len(y_test), df_monthly.shape[1]-1)), y_test), axis=1))[:, -1]

""" menghitung nilai Mean Absolute Error (MAE) dan Root Mean Squared Error (RMSE) untuk mengukur performa model dalam memprediksi total biaya (TotalCost)."""

mae = mean_absolute_error(y_test_inv, y_pred_inv)
rmse = np.sqrt(mean_squared_error(y_test_inv, y_pred_inv))

print(f"MAE: {mae:.2f}")
print(f"RMSE: {rmse:.2f}")

"""### Visualisasi Prediksi vs Aktual
Visualisasi ini bertujuan untuk melihat seberapa dekat hasil prediksi dengan nilai aktualnya.

"""

# Plot hasil prediksi vs aktual
plt.figure(figsize=(12,6))
plt.plot(y_test_inv, label='Actual')
plt.plot(y_pred_inv, label='Prediction')
plt.legend()
plt.title('Comparison: Actual vs Prediction')
plt.xlabel('Time')
plt.ylabel('Total Cost')
plt.grid()
plt.show()

"""### Insight Evaluasi:
- Model mampu mengikuti tren data pengeluaran bulanan dengan cukup baik.

- MAE = 4589.25 → menunjukkan bahwa rata-rata kesalahan prediksi hanya sekitar 4,5 ribu satuan, yang tergolong rendah dan menandakan model cukup akurat.

- RMSE = 4760.40 → menunjukkan kesalahan prediksi keseluruhan relatif kecil, menunjukkan performa model yang stabil dan akurat.

### Interpretasi dan Dampaknya terhadap Bisnis
Model LSTM yang dikembangkan berhasil mengurangi rata-rata kesalahan prediksi hingga 4.589 satuan, yang menunjukkan performa prediksi yang akurat dan stabil. Prediksi ini membantu divisi keuangan dan pengadaan dalam menyusun rencana anggaran dan melakukan pemesanan dengan lebih terstruktur.

### Apakah Problem Statement Terjawab?
 Ya. Model menjawab kebutuhan untuk memprediksi pengeluaran dengan cukup akurat.

### Apakah Goals Tercapai?
 Ya. Prediksi yang dihasilkan mampu memberikan informasi awal yang relevan untuk perencanaan bulanan, dengan tingkat kesalahan yang dapat ditoleransi secara bisnis.

### Apakah Solusi Berdampak?
 Ya. Model LSTM menunjukkan dampak yang signifikan dalam mengungkap pola pengeluaran dan menghasilkan estimasi yang dapat diandalkan sebagai alat bantu pengambilan keputusan keuangan.

---

Seluruh tahapan proyek ini menunjukkan bahwa machine learning, khususnya pendekatan time series, dapat diterapkan secara langsung untuk mendukung kebutuhan bisnis nyata, khususnya dalam manajemen pengeluaran dan perencanaan anggaran.



"""