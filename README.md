# Prediksi Nilai Pembelian Perusahaan Berdasarkan Karakteristik dan Segmen Pasar

Proyek Machine Learning untuk submission kelas Dicoding: Machine Learning  
**Pendekatan**: Regresi  
**Target**: Purchase Amount

---

## 1. Pendahuluan
Perusahaan membutuhkan strategi yang lebih baik untuk memprioritaskan pelanggan potensial. 
Dengan memprediksi `Purchase Amount` berdasarkan data historis, perusahaan dapat lebih efektif 
mengalokasikan sumber daya dan strategi pemasaran.

---

## 2. Problem Domain
- **Latar Belakang**: Data pembelian perusahaan dari berbagai negara dan industri
- **Masalah**: Sulit memprediksi nilai pembelian perusahaan baru
- **Solusi**: Gunakan machine learning untuk memprediksi nilai pembelian
- **Manfaat**: Membantu tim sales fokus pada klien bernilai tinggi

---

## 3. Data Understanding
Dataset berisi informasi:
- Nama perusahaan, negara, wilayah
- Kategori produk, jumlah karyawan, revenue tahunan
- Jumlah pembelian (`Purchase Amount`)
- Segmen pelanggan

---

## 4. Data Preparation
- Cek missing value
- Encode kolom kategorikal
- Normalisasi fitur numerik
- Split data ke train/test

```python
# Preprocessing dasar
cat_cols = ['Country', 'Region', 'Product Category', 'Customer Segment']
num_cols = ['Employee Count', 'Annual Revenue']

# Encode categorical
le = LabelEncoder()
for col in cat_cols:
    df[col] = le.fit_transform(df[col])

# Scale numerical
scaler = StandardScaler()
df[num_cols] = scaler.fit_transform(df[num_cols])
```

---

## 5. Modeling
Model awal: Linear Regression  
Langkah selanjutnya: Random Forest, XGBoost

```python
# Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)
```

---

## 6. Evaluation
Gunakan metrik:
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- R² Score

```python
mae = mean_absolute_error(y_test, y_pred_lr)
rmse = np.sqrt(mean_squared_error(y_test, y_pred_lr))
r2 = r2_score(y_test, y_pred_lr)

print(f"MAE: {mae:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R²: {r2:.2f}")
```

---

## 7. Kesimpulan
Model regresi dapat digunakan untuk memprediksi nilai pembelian berdasarkan karakteristik perusahaan.

Langkah selanjutnya:
- Eksperimen dengan model lain
- Tuning hyperparameter
- Visualisasi hasil prediksi vs aktual
