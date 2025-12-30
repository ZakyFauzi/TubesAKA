# Analisis Perbandingan Kompleksitas Waktu Asimtotik Algoritma Iteratif dan Rekursif pada Operasi Dot Product

## Abstrak

Proyek ini menyajikan analisis komparatif terhadap algoritma iteratif dan rekursif untuk operasi dot product. Penelitian berfokus pada analisis kompleksitas waktu asimtotik, pengukuran performa praktis, dan pertimbangan implementasi dalam konteks komputasi Neural Network. Aplikasi web interaktif berbasis Streamlit menyediakan kemampuan visualisasi dan benchmarking untuk tujuan edukatif.

**Kata Kunci:** Analisis Kompleksitas Algoritma, Dot Product, Algoritma Iteratif, Algoritma Rekursif, Perbandingan Performa, Neural Networks

---

## 1. Pendahuluan

### 1.1 Latar Belakang

Pemahaman kompleksitas algoritma merupakan fundamental dalam ilmu komputer dan rekayasa perangkat lunak. Proyek ini mengkaji karakteristik performa dari dua paradigma pemrograman—iterasi dan rekursi—melalui komputasi dot product, operasi kritis dalam arsitektur neural network dan aplikasi aljabar linear.

### 1.2 Tujuan

Tujuan utama dari studi ini adalah:

1. Mengimplementasikan dan menganalisis algoritma dot product menggunakan pendekatan iteratif dan rekursif
2. Menentukan kompleksitas waktu asimtotik dari setiap implementasi
3. Mengukur dan membandingkan performa runtime pada berbagai ukuran input
4. Memvisualisasikan perbedaan performa melalui benchmarking komprehensif
5. Mengidentifikasi keterbatasan praktis dan memberikan rekomendasi implementasi

---

## 2. Metodologi

### 2.1 Implementasi Algoritma

#### Algoritma Iteratif

```python
def dot_product_iterative(vector_a: list, vector_b: list) -> float:
    result = 0
    n = len(vector_a)
    for i in range(n):
        result += vector_a[i] * vector_b[i]
    return result
```

**Analisis Kompleksitas:**
- Kompleksitas Waktu: O(n)
- Kompleksitas Ruang: O(1)

#### Algoritma Rekursif

```python
def dot_product_recursive(vector_a: list, vector_b: list, n: int) -> float:
    if n == 0:
        return 0
    return (vector_a[n-1] * vector_b[n-1]) + dot_product_recursive(vector_a, vector_b, n-1)
```

**Analisis Kompleksitas:**
- Kompleksitas Waktu: O(n)
- Kompleksitas Ruang: O(n) - call stack

**Relasi Rekurensi:**
```
T(n) = T(n-1) + c
T(0) = c
⟹ T(n) = nc = O(n)
```

### 2.2 Tools dan Teknologi

- **Python 3.8+**: Bahasa pemrograman utama
- **Streamlit**: Framework aplikasi web untuk visualisasi interaktif
- **Plotly**: Library visualisasi data interaktif
- **Pandas**: Manipulasi dan analisis data
- **NumPy**: Komputasi numerik
- **Matplotlib**: Plotting (versi Jupyter Notebook)

### 2.3 Konfigurasi Eksperimen

- Ukuran input: 10, 50, 100, 250, 500, 750, 1000, 1500, 2000, 2500, 3000
- Pengulangan per ukuran: 3 kali (rata-rata)
- Rentang nilai acak: [-100, 100]
- Python recursion limit: 15,000

---

## 3. Instalasi dan Penggunaan

### 3.1 Prasyarat

- Python 3.8 atau lebih tinggi
- pip (Python package manager)

### 3.2 Instalasi Dependencies

```bash
pip install -r requirements.txt
```

Paket yang dibutuhkan:
- `streamlit` - Framework aplikasi web
- `plotly` - Library visualisasi interaktif
- `pandas` - Toolkit manipulasi data
- `numpy` - Library komputasi numerik

### 3.3 Menjalankan Aplikasi

**Streamlit Web Application:**

```bash
streamlit run app.py
```

Atau menggunakan:

```bash
python -m streamlit run app.py
```

Aplikasi dapat diakses di `http://localhost:8501`

**Jupyter Notebook:**

```bash
jupyter notebook dot_product_analysis.ipynb
```

---

## 4. Struktur Proyek

```
TubesAKA/
├── app.py                                  # Aplikasi Streamlit utama
├── dot_product_analysis.ipynb              # Analisis Jupyter Notebook
├── requirements.txt                        # Python dependencies
├── README.md                               # Dokumentasi proyek
├── Laporan Tugas Besar AKA.pdf             # Laporan teknis (PDF)
├── Laporan Tugas Besar AKA.docx            # Laporan teknis (DOCX)
└── deskripsi tubes-TELU.pdf               # Spesifikasi tugas
```

---

## 5. Fitur Aplikasi

### 5.1 Aplikasi Web Streamlit

Aplikasi terdiri dari 4 modul utama:

1. **Studi Kasus**: Latar belakang teoritis dot product dan relevansinya pada Neural Network
2. **Perbandingan Algoritma**: Generasi vektor interaktif, pengukuran performa real-time, perbandingan hasil
3. **Benchmarking & Visualisasi**: Benchmarking otomatis, grafik interaktif, analisis statistik
4. **Analisis Kompleksitas**: Analisis asimtotik detail, solusi relasi rekurensi, tabel perbandingan

### 5.2 Jupyter Notebook

- Implementasi step-by-step dengan dokumentasi lengkap
- Validasi algoritma dengan test cases
- Benchmarking performa
- Visualisasi data menggunakan Matplotlib
- Analisis statistik dan kesimpulan

---

## 6. Hasil Analisis

### 6.1 Perbandingan Kompleksitas

| Aspek | Iteratif | Rekursif |
|-------|----------|----------|
| Kompleksitas Waktu | O(n) | O(n) |
| Kompleksitas Ruang | O(1) | O(n) |
| Overhead Function Call | Minimal | Tinggi |
| Risiko Stack Overflow | Tidak Ada | Ada |
| Skalabilitas | Sangat Baik | Terbatas |

### 6.2 Temuan Utama

1. **Ekuivalensi Asimtotik**: Kedua algoritma memiliki kompleksitas waktu O(n)
2. **Efisiensi Ruang**: Pendekatan iteratif memerlukan ruang konstan vs. linear untuk rekursi
3. **Performa Praktis**: Implementasi iteratif secara konsisten lebih cepat
4. **Keterbatasan Skalabilitas**: Pendekatan rekursif mengalami stack overflow pada input besar
5. **Gap Performa**: Speedup rata-rata menunjukkan keunggulan signifikan untuk iterasi

### 6.3 Faktor Performa

Algoritma iteratif menunjukkan performa superior karena:
- **Overhead Function Call**: Panggilan rekursif memerlukan penyimpanan dan pemulihan konteks eksekusi
- **Pola Akses Memori**: Iterasi sekuensial memiliki cache locality yang lebih baik
- **Manajemen Stack**: Operasi call stack menambah latensi
- **Optimasi Compiler**: Struktur loop lebih mudah dioptimasi

---

## 7. Konteks Aplikasi: Neural Networks

Dalam Artificial Neural Network, operasi dot product adalah fundamental untuk aktivasi neuron:

```
z = Σ(x_i × w_i) = x · w
```

Di mana:
- x_i = fitur input
- w_i = bobot yang dipelajari
- z = nilai pre-activation

**Implikasi Praktis:**
1. Model deep learning modern mengandung jutaan hingga miliaran parameter
2. Training dan inference memerlukan miliaran komputasi dot product
3. Pilihan algoritma berdampak langsung pada biaya komputasi
4. Edge computing dan mobile deployment memerlukan implementasi yang efisien memori

---

## 8. Rekomendasi

### 8.1 Pedoman Pemilihan Algoritma

**Gunakan Pendekatan Iteratif:**
- Memproses dataset besar
- Terdapat keterbatasan memori
- Performa maksimal diperlukan
- Deployment production

**Pertimbangkan Pendekatan Rekursif:**
- Struktur masalah secara natural cocok untuk rekursi
- Ukuran input dijamin kecil
- Elegankode diprioritaskan
- Tujuan edukatif atau demonstrasi

### 8.2 Implementasi Production

Untuk aplikasi real-world:
1. Gunakan library teroptimasi (NumPy, BLAS, cuBLAS)
2. Manfaatkan vektorisasi dan instruksi SIMD
3. Pertimbangkan akselerasi hardware (GPU, TPU)
4. Implementasikan error handling dan validasi yang proper

---

## 9. Referensi

Anton, H., & Rorres, C. (2013). *Elementary linear algebra: Applications version* (1st ed.). Wiley.

Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to algorithms* (3rd ed.). MIT Press.

Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep learning*. MIT Press.

Levitin, A. (2011). *Introduction to the design and analysis of algorithms* (3rd ed.). Pearson.

Munir, R. (2006). *Diktat strategi algoritmik IF2251*. Departemen Teknik Informatika, Institut Teknologi Bandung.

Neapolitan, R., & Naimipour, K. (2014). *Foundations of algorithms* (5th ed.). Jones & Bartlett Learning.

Nielsen, M. A. (2015). *Neural networks and deep learning*. Determination Press.

Ummah, I., dkk. (2025). *Buku ajar: Analisis kompleksitas algoritma*. KBM.

---

**Zaky Muhammad Fauzi**