# Analisis Perbandingan Kompleksitas Waktu Asimtotik Algoritma Iteratif dan Rekursif pada Operasi Dot Product

## 📋 Deskripsi

Proyek ini merupakan Tugas Besar untuk Mata Kuliah **Analisis Kompleksitas Algoritma** yang bertujuan untuk membandingkan efisiensi algoritma **Dot Product** dalam dua versi: **Iteratif** dan **Rekursif**. 

Aplikasi web interaktif ini dibangun menggunakan **Streamlit** dan menyediakan analisis mendalam tentang kompleksitas waktu asimtotik, visualisasi perbandingan performa, dan studi kasus implementasi dot product dalam konteks Neural Network.

## 🎯 Tujuan Pembelajaran

1. Memahami perbedaan kompleksitas waktu antara algoritma iteratif dan rekursif
2. Menganalisis efisiensi algoritma melalui pengukuran running time
3. Memvisualisasikan perbandingan performa pada berbagai ukuran input
4. Memahami keterbatasan pendekatan rekursif pada data berskala besar

## ✨ Fitur

- **4 Tab Interaktif:**
  - 📖 **Studi Kasus**: Penjelasan dot product dan relevansinya dalam Neural Network
  - 🧮 **Perbandingan Algoritma**: Eksekusi dan perbandingan langsung kedua algoritma
  - 📈 **Benchmark & Grafik**: Visualisasi performa pada berbagai ukuran input
  - 📚 **Analisis Kompleksitas**: Penjelasan detail tentang kompleksitas asimtotik O(n)

- **Fitur Utama:**
  - Generate vektor random dengan ukuran custom (1-10,000)
  - Pengukuran waktu eksekusi real-time
  - Grafik interaktif perbandingan performa (line chart & bar chart)
  - Error handling untuk RecursionError
  - Analisis kompleksitas waktu dan ruang
  - Konfigurasi recursion limit

## 🚀 Instalasi

### Prasyarat
- Python 3.8 atau lebih tinggi
- pip (Python package manager)

### Langkah Instalasi

1. **Clone atau download repository ini**

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

Dependencies yang dibutuhkan:
- `streamlit` - Framework web aplikasi
- `plotly` - Library visualisasi interaktif
- `pandas` - Manipulasi data
- `numpy` - Operasi numerik

## 📖 Cara Menjalankan

### Streamlit Web App

Jalankan aplikasi Streamlit:

```bash
streamlit run app.py
```

atau:

```bash
python -m streamlit run app.py
```

Aplikasi akan berjalan di `http://localhost:8501`

### Jupyter Notebook

Buka file `dot_product_analysis.ipynb` dengan Jupyter Notebook atau JupyterLab:

```bash
jupyter notebook dot_product_analysis.ipynb
```

## 📁 Struktur Proyek

```
TubesAKA/
├── app.py                          # Aplikasi Streamlit utama
├── dot_product_analysis.ipynb      # Jupyter Notebook version
├── requirements.txt                # Python dependencies
├── README.md                       # Dokumentasi proyek
└── deskripsi tubes-TELU.pdf       # Deskripsi tugas
```

## 🧮 Algoritma

### 1. Dot Product Iteratif

```python
def dot_product_iterative(vector_a: list, vector_b: list) -> float:
    result = 0
    n = len(vector_a)
    for i in range(n):
        result += vector_a[i] * vector_b[i]
    return result
```

**Kompleksitas:**
- Waktu: **O(n)**
- Ruang: **O(1)**

### 2. Dot Product Rekursif

```python
def dot_product_recursive(vector_a: list, vector_b: list, n: int) -> float:
    if n == 0:
        return 0
    return (vector_a[n-1] * vector_b[n-1]) + dot_product_recursive(vector_a, vector_b, n-1)
```

**Kompleksitas:**
- Waktu: **O(n)**
- Ruang: **O(n)** (call stack)

## 📊 Hasil Analisis

### Kesimpulan Utama

1. **Kompleksitas Waktu:** Kedua algoritma memiliki kompleksitas waktu O(n) yang sama secara asimtotik
2. **Kompleksitas Ruang:** Iteratif lebih efisien (O(1)) dibanding rekursif (O(n))
3. **Performa Praktis:** Algoritma iteratif **lebih cepat** dalam praktiknya karena:
   - Tidak ada overhead pemanggilan fungsi
   - Akses memori lebih efisien
   - Tidak ada risiko stack overflow
4. **Keterbatasan Rekursif:** Python memiliki batas kedalaman rekursi default (~1000), yang membatasi ukuran input yang dapat diproses

### Rekomendasi

Untuk operasi **Dot Product** dan operasi vektor lainnya:
- ✅ **Gunakan pendekatan iteratif** untuk skalabilitas dan efisiensi
- ✅ Gunakan library teroptimasi seperti **NumPy** untuk performa maksimal
- ❌ Hindari pendekatan rekursif untuk data berskala besar

## 🎓 Konteks Pembelajaran

### Studi Kasus: Neural Network

Dalam **Artificial Neural Network (ANN)**, setiap neuron melakukan operasi dot product antara input vector dan weight vector:

$$z = \sum_{i=1}^{n} x_i \cdot w_i = \vec{x} \cdot \vec{w}$$

Di mana:
- $x_i$ = nilai input ke-i
- $w_i$ = bobot (weight) ke-i
- $z$ = hasil dot product sebelum fungsi aktivasi

### Relevansi

1. **Skala Besar**: Model Deep Learning modern memiliki jutaan parameter
2. **Real-time Processing**: Aplikasi seperti autonomous driving membutuhkan perhitungan cepat
3. **Resource Constraint**: Edge computing memiliki keterbatasan memori

---

**Zaky Muhammad Fauzi**
