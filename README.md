

----------

# Crude Oil Price Forecasting with LSTM and DNN Models

## Deskripsi Proyek

Proyek ini bertujuan untuk memprediksi harga minyak mentah (Crude Oil) menggunakan dua jenis model pembelajaran mesin, yaitu **LSTM (Long Short-Term Memory)** dan **DNN (Deep Neural Network)**. Proyek ini mengimplementasikan aplikasi web menggunakan **Streamlit** yang memungkinkan pengguna untuk mengunggah dataset harga minyak dan melihat hasil prediksi menggunakan kedua model. Proyek ini bertujuan untuk memberikan wawasan mengenai perbandingan performa kedua model dalam melakukan prediksi harga.

### Tujuan Pengembangan:

-   Membangun aplikasi web yang mudah digunakan untuk memprediksi harga minyak mentah.
-   Menyediakan alat bagi pengguna untuk memilih model (LSTM atau DNN) dan mendapatkan hasil prediksi.
-   Memberikan analisis performa model dengan metrik seperti MAE (Mean Absolute Error), RMSE (Root Mean Squared Error), dan Akurasi.

## Langkah Instalasi

### 1. Persyaratan

Sebelum memulai, pastikan Anda memiliki **Python 3.x** yang terinstal di sistem Anda.

### 2. Menginstal Dependencies

Untuk menginstal semua dependensi yang dibutuhkan oleh aplikasi ini, jalankan perintah berikut di terminal atau command prompt:

```bash
pip install -r requirements.txt

```

Buat file `requirements.txt` dengan daftar dependensi berikut:

```
streamlit
pandas
numpy
matplotlib
scikit-learn

```

### 3. Menjalankan Aplikasi

Setelah semua dependensi terinstal, jalankan aplikasi dengan perintah berikut:

```bash
streamlit run app.py

```

Gantilah `app.py` dengan nama file Python yang Anda gunakan untuk aplikasi jika berbeda. Aplikasi akan berjalan di browser lokal Anda dan siap digunakan.

## Deskripsi Model

### 1. LSTM (Long Short-Term Memory)

LSTM adalah jenis jaringan saraf dalam yang dirancang untuk menangani data urutan (time series) dan belajar dari konteks yang lebih panjang dalam data. Model LSTM digunakan untuk memprediksi harga minyak berdasarkan fitur-fitur teknikal seperti moving average, pengembalian harian, dan volatilitas. LSTM sangat efektif dalam menangani ketergantungan jangka panjang pada data deret waktu.

### 2. DNN (Deep Neural Network)

DNN adalah jaringan saraf berlapis dalam yang terdiri dari beberapa lapisan tersembunyi dan digunakan untuk menemukan pola kompleks dalam data. DNN dalam proyek ini digunakan untuk memprediksi harga minyak berdasarkan fitur-fitur teknikal yang sama, namun menggunakan arsitektur yang lebih sederhana dibandingkan LSTM. Meskipun DNN kurang efisien dalam menangani data urutan panjang, model ini tetap dapat memberikan hasil yang baik untuk data yang terstruktur.

## Hasil dan Analisis

### Perbandingan Model

Setelah menjalankan aplikasi, hasil dari perbandingan model ditampilkan dalam bentuk metrik evaluasi seperti MAE (Mean Absolute Error), RMSE (Root Mean Squared Error), dan akurasi prediksi. Pengguna dapat memilih model (LSTM atau DNN) dan melihat perbandingan performanya. Berikut adalah contoh metrik evaluasi yang ditampilkan:

-   **MAE (Mean Absolute Error):** Menunjukkan seberapa jauh prediksi model dari nilai aktual dalam rata-rata absolut.
-   **RMSE (Root Mean Squared Error):** Memberikan gambaran lebih baik tentang kesalahan besar, karena RMSE memberikan bobot lebih pada kesalahan yang besar.
-   **Akurasi:** Menghitung akurasi model berdasarkan persentase kesalahan prediksi dibandingkan dengan harga aktual.

#### Contoh Visualisasi

Pada bagian visualisasi, perbandingan antara harga aktual dan harga prediksi dari model yang dipilih akan ditampilkan dalam bentuk grafik garis. Berikut adalah contoh visualisasi yang dihasilkan oleh aplikasi:

-   **Grafik Perbandingan:**
    -   **Harga Aktual vs Harga Prediksi**: Menampilkan perbandingan harga minyak yang sebenarnya dan harga yang diprediksi oleh model (LSTM atau DNN).

#### Contoh Hasil Akurasi

Misalkan hasil dari model LSTM dan DNN diukur pada data yang sama:

-   **Model LSTM:**
    
    -   **MAE:** 16.76
    -   **RMSE:** 20.96
    -   **Akurasi:** 76.36%
-   **Model DNN:**
    
    -   **MAE:** 53.71
    -   **RMSE:** 61.74
    -   **Akurasi:** 20.66%

Dengan hasil ini, kita bisa melihat bahwa model LSTM memberikan prediksi yang lebih akurat (lebih tinggi akurasinya) dibandingkan dengan model DNN, meskipun kedua model memberikan hasil yang cukup baik.

----------

**Terima kasih telah menggunakan aplikasi ini!**

Jika ada pertanyaan atau saran, silakan hubungi pengembang.

----------

Dengan tambahan ini, pengguna bisa lebih mudah memahami bagaimana model berperforma berdasarkan akurasi yang dihitung.
