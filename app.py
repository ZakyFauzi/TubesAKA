import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import time
import sys

st.set_page_config(
    page_title="Analisis Kompleksitas Algoritma - Dot Product",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    /* Header styling */
    .main-header {
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
        padding: 2rem;
        border-radius: 12px;
        margin-bottom: 1.5rem;
    }
    
    .main-header h1 {
        color: #ffffff;
        text-align: center;
        font-size: 1.8rem;
        margin-bottom: 0.3rem;
        font-weight: 700;
    }
    
    .main-header p {
        color: #ffffff;
        text-align: center;
        font-size: 1rem;
        opacity: 0.95;
    }
    
    /* Card styling - Light backgrounds with dark text */
    .info-card {
        background: #f0f4ff;
        padding: 1.25rem;
        border-radius: 10px;
        border-left: 4px solid #4f46e5;
        margin: 1rem 0;
    }
    
    .info-card h4 {
        color: #1e293b;
        margin-bottom: 0.5rem;
        font-weight: 600;
    }
    
    .info-card p, .info-card li {
        color: #334155;
    }
    
    .result-card {
        background: #f0fdf4;
        padding: 1.25rem;
        border-radius: 10px;
        border-left: 4px solid #22c55e;
        margin: 1rem 0;
    }
    
    .result-card h4 {
        color: #166534;
        margin-bottom: 0.5rem;
        font-weight: 600;
    }
    
    .result-card p, .result-card li {
        color: #15803d;
    }
    
    .warning-card {
        background: #fffbeb;
        padding: 1.25rem;
        border-radius: 10px;
        border-left: 4px solid #f59e0b;
        margin: 1rem 0;
    }
    
    .warning-card h4 {
        color: #92400e;
        margin-bottom: 0.5rem;
        font-weight: 600;
    }
    
    .warning-card p, .warning-card li {
        color: #a16207;
    }
    
    .error-card {
        background: #fef2f2;
        padding: 1.25rem;
        border-radius: 10px;
        border-left: 4px solid #ef4444;
        margin: 1rem 0;
    }
    
    .error-card h4 {
        color: #991b1b;
        margin-bottom: 0.5rem;
        font-weight: 600;
    }
    
    .error-card p, .error-card li {
        color: #b91c1c;
    }
    
    /* Algorithm box - Light theme */
    .algo-box {
        background: #f8fafc;
        padding: 1.25rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        border: 1px solid #e2e8f0;
    }
    
    .algo-box h4 {
        color: #4f46e5;
        margin-bottom: 0.5rem;
        font-weight: 600;
    }
    
    .algo-box p {
        color: #334155;
    }
    
    /* Button styling */
    .stButton > button {
        background: #4f46e5;
        color: #ffffff;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 1.5rem;
        font-weight: 600;
        transition: background 0.2s ease;
    }
    
    .stButton > button:hover {
        background: #4338ca;
    }
    
    /* Complexity badge */
    .complexity-badge {
        display: inline-block;
        background: #4f46e5;
        color: #ffffff;
        padding: 0.25rem 0.75rem;
        border-radius: 16px;
        font-weight: 600;
        font-size: 1rem;
    }
    
    /* Code block styling */
    .stCodeBlock {
        border-radius: 8px !important;
    }
</style>
""", unsafe_allow_html=True)


def dot_product_iterative(vector_a: list, vector_b: list) -> float:
    """
    Menghitung Dot Product dua vektor menggunakan metode ITERATIF.
    
    Kompleksitas Waktu: O(n)
    Kompleksitas Ruang: O(1)
    
    Args:
        vector_a: Vektor pertama
        vector_b: Vektor kedua
    
    Returns:
        Hasil dot product (skalar)
    """
    result = 0
    n = len(vector_a)
    for i in range(n):
        result += vector_a[i] * vector_b[i]
    return result


def dot_product_recursive(vector_a: list, vector_b: list, n: int) -> float:
    """
    Menghitung Dot Product dua vektor menggunakan metode REKURSIF.
    
    Kompleksitas Waktu: O(n)
    Kompleksitas Ruang: O(n) - karena call stack
    
    Args:
        vector_a: Vektor pertama
        vector_b: Vektor kedua
        n: Ukuran vektor (indeks terakhir + 1)
    
    Returns:
        Hasil dot product (skalar)
    """
    # Base case: jika n = 0, tidak ada elemen yang dikalikan
    if n == 0:
        return 0
    # Recursive case: hitung elemen terakhir + rekursi untuk sisanya
    return (vector_a[n-1] * vector_b[n-1]) + dot_product_recursive(vector_a, vector_b, n-1)


def measure_execution_time(func, *args):
    """Mengukur waktu eksekusi suatu fungsi dalam milidetik."""
    start_time = time.perf_counter()
    result = func(*args)
    end_time = time.perf_counter()
    execution_time_ms = (end_time - start_time) * 1000
    return result, execution_time_ms


st.markdown("""
<div class="main-header">
    <h1>Analisis Perbandingan Kompleksitas Waktu Asimtotik Algoritma Iteratif dan Rekursif pada Operasi Dot Product</h1>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## Konfigurasi")
    st.markdown("---")
    
    # Input ukuran vektor
    st.markdown("### Ukuran Vektor (n)")
    n_size = st.number_input(
        "Masukkan ukuran vektor:",
        min_value=1,
        max_value=10000,
        value=100,
        step=1,
        help="Ukuran vektor yang akan digunakan untuk perhitungan dot product (1-10.000)"
    )
    
    st.markdown("---")
    
    # Rentang nilai random
    st.markdown("### Rentang Nilai Random")
    min_val = st.number_input("Nilai Minimum:", value=-100, step=1)
    max_val = st.number_input("Nilai Maksimum:", value=100, step=1)
    
    st.markdown("---")
    
    # Set recursion limit
    st.markdown("### Batas Rekursi")
    recursion_limit = st.number_input(
        "Recursion Limit:",
        min_value=1000,
        max_value=50000,
        value=15000,
        step=1000,
        help="Batas maksimum kedalaman rekursi Python"
    )
    sys.setrecursionlimit(recursion_limit)
    st.caption(f"Current limit: {recursion_limit}")

tab1, tab2, tab3, tab4 = st.tabs([
    "📖 Studi Kasus", 
    "🧮 Perbandingan Algoritma", 
    "📈 Benchmark & Grafik",
    "📚 Analisis Kompleksitas"
])

with tab1:
    st.markdown("## 🧠 Studi Kasus: Dot Product dalam Neural Network")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="info-card">
            <h4>📌 Apa itu Dot Product?</h4>
            <p>
                <strong>Dot Product</strong> (Perkalian Titik) adalah operasi matematika fundamental yang 
                menghasilkan nilai skalar dari dua vektor. Operasi ini sangat penting dalam berbagai 
                bidang komputasi, terutama dalam <strong>Machine Learning</strong> dan <strong>Neural Networks</strong>.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        ### 🔬 Konteks: Komputasi Neuron pada Neural Network
        
        Dalam **Artificial Neural Network (ANN)**, setiap neuron melakukan operasi dot product 
        antara **input vector** dan **weight vector** untuk menghasilkan nilai aktivasi:
        
        $$z = \\sum_{i=1}^{n} x_i \\cdot w_i = \\vec{x} \\cdot \\vec{w}$$
        
        Di mana:
        - $x_i$ = nilai input ke-i
        - $w_i$ = bobot (weight) ke-i
        - $z$ = hasil dot product sebelum fungsi aktivasi
        
        ---
        
        ### 🎯 Relevansi Studi Kasus
        
        1. **Skala Besar**: Model Deep Learning modern memiliki jutaan parameter, 
           sehingga efisiensi operasi dot product sangat krusial.
        
        2. **Real-time Processing**: Aplikasi seperti autonomous driving atau speech recognition 
           membutuhkan perhitungan yang sangat cepat.
        
        3. **Resource Constraint**: Perangkat edge computing memiliki keterbatasan memori, 
           sehingga penggunaan stack pada rekursi bisa menjadi masalah.
        """)
    
    with col2:
        st.markdown("""
        <div class="algo-box">
            <h4>📐 Formula Dot Product</h4>
            <p style="text-align: center; font-size: 1.2rem;">
                <strong>a · b = Σ(aᵢ × bᵢ)</strong>
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="algo-box">
            <h4>🔢 Contoh Sederhana</h4>
            <p>
                <strong>Vektor A:</strong> [1, 2, 3]<br>
                <strong>Vektor B:</strong> [4, 5, 6]<br><br>
                <strong>Dot Product:</strong><br>
                = (1×4) + (2×5) + (3×6)<br>
                = 4 + 10 + 18<br>
                = <strong>32</strong>
            </p>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.markdown("## 🧮 Perbandingan Algoritma Iteratif vs Rekursif")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🔄 Algoritma Iteratif")
        st.code("""
def dot_product_iterative(vector_a, vector_b):
    result = 0
    n = len(vector_a)
    for i in range(n):
        result += vector_a[i] * vector_b[i]
    return result
        """, language="python")
        
        st.markdown("""
        <div class="info-card">
            <h4>✅ Kelebihan Iteratif</h4>
            <ul>
                <li>Efisien dalam penggunaan memori (O(1) space)</li>
                <li>Tidak ada batasan ukuran input</li>
                <li>Lebih cepat karena tidak ada overhead pemanggilan fungsi</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 🔁 Algoritma Rekursif")
        st.code("""
def dot_product_recursive(vector_a, vector_b, n):
    if n == 0:
        return 0
    return (vector_a[n-1] * vector_b[n-1]) + 
           dot_product_recursive(vector_a, vector_b, n-1)
        """, language="python")
        
        st.markdown("""
        <div class="warning-card">
            <h4>⚠️ Kekurangan Rekursif</h4>
            <ul>
                <li>Membutuhkan O(n) ruang untuk call stack</li>
                <li>Risiko Stack Overflow pada input besar</li>
                <li>Overhead fungsi call pada setiap iterasi</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # EKSEKUSI PERBANDINGAN
    st.markdown("### 🚀 Eksekusi Perbandingan")
    
    col1, col2, col3 = st.columns([1, 1, 2])
    
    with col1:
        generate_btn = st.button("🎲 Generate Vektor", use_container_width=True)
    
    with col2:
        run_btn = st.button("▶️ Jalankan Perbandingan", use_container_width=True)
    
    with col3:
        st.info(f"📏 Ukuran vektor saat ini: **n = {n_size}**")
    
    # Session state untuk menyimpan vektor
    if 'vector_a' not in st.session_state:
        st.session_state.vector_a = None
        st.session_state.vector_b = None
    
    if generate_btn:
        st.session_state.vector_a = list(np.random.randint(min_val, max_val + 1, size=n_size))
        st.session_state.vector_b = list(np.random.randint(min_val, max_val + 1, size=n_size))
        st.success(f"✅ Berhasil generate 2 vektor dengan ukuran n = {n_size}")
    
    # Tampilkan preview vektor
    if st.session_state.vector_a is not None:
        with st.expander("👁️ Preview Vektor (10 elemen pertama)"):
            preview_col1, preview_col2 = st.columns(2)
            with preview_col1:
                st.markdown("**Vektor A:**")
                st.write(st.session_state.vector_a[:10])
            with preview_col2:
                st.markdown("**Vektor B:**")
                st.write(st.session_state.vector_b[:10])
    
    # Jalankan perbandingan
    if run_btn:
        if st.session_state.vector_a is None:
            st.warning("⚠️ Silakan generate vektor terlebih dahulu!")
        else:
            vector_a = st.session_state.vector_a
            vector_b = st.session_state.vector_b
            n = len(vector_a)
            
            st.markdown("---")
            st.markdown("### 📊 Hasil Perbandingan")
            
            # Hasil Iteratif
            result_iter, time_iter = measure_execution_time(dot_product_iterative, vector_a, vector_b)
            
            # Hasil Rekursif dengan error handling
            try:
                result_recur, time_recur = measure_execution_time(dot_product_recursive, vector_a, vector_b, n)
                recursion_error = False
            except RecursionError:
                result_recur = None
                time_recur = None
                recursion_error = True
            
            # Tampilkan hasil
            res_col1, res_col2 = st.columns(2)
            
            with res_col1:
                st.markdown("""
                <div class="result-card">
                    <h4>🔄 Hasil Iteratif</h4>
                </div>
                """, unsafe_allow_html=True)
                st.metric("Dot Product", f"{result_iter:,.2f}")
                st.metric("Waktu Eksekusi", f"{time_iter:.4f} ms")
            
            with res_col2:
                if not recursion_error:
                    st.markdown("""
                    <div class="result-card">
                        <h4>🔁 Hasil Rekursif</h4>
                    </div>
                    """, unsafe_allow_html=True)
                    st.metric("Dot Product", f"{result_recur:,.2f}")
                    st.metric("Waktu Eksekusi", f"{time_recur:.4f} ms")
                else:
                    st.markdown("""
                    <div class="error-card">
                        <h4>❌ Recursion Error!</h4>
                        <p>Batas rekursi tercapai pada <strong>n = {}</strong>.</p>
                        <p>Gunakan metode <strong>iteratif</strong> untuk data yang lebih besar, 
                        atau tingkatkan batas rekursi di sidebar.</p>
                    </div>
                    """.format(n), unsafe_allow_html=True)
            
            # Tabel perbandingan
            if not recursion_error:
                st.markdown("### 📋 Tabel Perbandingan")
                
                comparison_data = {
                    "Metrik": ["Hasil Dot Product", "Waktu Eksekusi (ms)"],
                    "Iteratif": [f"{result_iter:,.2f}", f"{time_iter:.4f}"],
                    "Rekursif": [f"{result_recur:,.2f}", f"{time_recur:.4f}"],
                }
                
                df_comparison = pd.DataFrame(comparison_data)
                st.dataframe(df_comparison, use_container_width=True, hide_index=True)
                


with tab3:
    st.markdown("## 📈 Benchmark Lengkap & Visualisasi Grafik")
    
    st.markdown("""
    <div class="info-card">
        <h4>ℹ️ Tentang Benchmark</h4>
        <p>
            Benchmark ini akan menjalankan kedua algoritma pada berbagai ukuran input 
            dan mengukur waktu eksekusi masing-masing. Hasil akan divisualisasikan 
            dalam bentuk grafik garis untuk memudahkan analisis perbandingan.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Konfigurasi benchmark
    st.markdown("### ⚙️ Konfigurasi Benchmark")
    
    col1, col2 = st.columns(2)
    
    with col1:
        test_sizes_input = st.text_input(
            "Ukuran Input (pisahkan dengan koma):",
            value="10, 50, 100, 250, 500, 750, 1000, 1500, 2000, 2500, 3000",
            help="Contoh: 10, 100, 500, 1000, 5000"
        )
    
    with col2:
        num_runs = st.slider(
            "Jumlah pengulangan per ukuran:",
            min_value=1,
            max_value=10,
            value=3,
            help="Rata-rata dari beberapa run untuk hasil yang lebih akurat"
        )
    
    benchmark_btn = st.button("🚀 Jalankan Benchmark Lengkap", use_container_width=True)
    
    if benchmark_btn:
        try:
            test_sizes = [int(x.strip()) for x in test_sizes_input.split(",")]
        except ValueError:
            st.error("❌ Format ukuran input tidak valid! Gunakan format: 10, 100, 500, ...")
            test_sizes = []
        
        if test_sizes:
            # Progress bar
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # Data untuk grafik
            benchmark_results = []
            
            for idx, size in enumerate(test_sizes):
                status_text.text(f"⏳ Menjalankan benchmark untuk n = {size}...")
                
                # Generate vektor
                vec_a = list(np.random.randint(-100, 101, size=size))
                vec_b = list(np.random.randint(-100, 101, size=size))
                
                # Benchmark Iteratif
                iter_times = []
                for _ in range(num_runs):
                    _, exec_time = measure_execution_time(dot_product_iterative, vec_a, vec_b)
                    iter_times.append(exec_time)
                avg_iter_time = np.mean(iter_times)
                
                # Benchmark Rekursif
                try:
                    recur_times = []
                    for _ in range(num_runs):
                        _, exec_time = measure_execution_time(dot_product_recursive, vec_a, vec_b, size)
                        recur_times.append(exec_time)
                    avg_recur_time = np.mean(recur_times)
                    recur_error = False
                except RecursionError:
                    avg_recur_time = None
                    recur_error = True
                
                benchmark_results.append({
                    "Ukuran (n)": size,
                    "Iteratif (ms)": avg_iter_time,
                    "Rekursif (ms)": avg_recur_time,
                    "Recursion Error": recur_error
                })
                
                progress_bar.progress((idx + 1) / len(test_sizes))
            
            status_text.text("✅ Benchmark selesai!")
            
            # Buat DataFrame
            df_results = pd.DataFrame(benchmark_results)
            
            # Tampilkan tabel hasil
            st.markdown("### 📋 Tabel Hasil Benchmark")
            
            # Format tabel untuk ditampilkan
            df_display = df_results.copy()
            df_display["Iteratif (ms)"] = df_display["Iteratif (ms)"].apply(lambda x: f"{x:.4f}")
            df_display["Rekursif (ms)"] = df_display["Rekursif (ms)"].apply(
                lambda x: f"{x:.4f}" if x is not None else "❌ Error"
            )
            df_display = df_display.drop(columns=["Recursion Error"])
            
            st.dataframe(df_display, use_container_width=True, hide_index=True)
            
            # GRAFIK PERBANDINGAN
            st.markdown("### 📊 Grafik Perbandingan Waktu Eksekusi")
            
            # Persiapan data grafik
            fig = go.Figure()
            
            # Line untuk Iteratif
            fig.add_trace(go.Scatter(
                x=df_results["Ukuran (n)"],
                y=df_results["Iteratif (ms)"],
                mode='lines+markers',
                name='Iteratif',
                line=dict(color='#667eea', width=3),
                marker=dict(size=10, symbol='circle')
            ))
            
            # Line untuk Rekursif (hanya yang tidak error)
            df_recur_valid = df_results[df_results["Recursion Error"] == False]
            if not df_recur_valid.empty:
                fig.add_trace(go.Scatter(
                    x=df_recur_valid["Ukuran (n)"],
                    y=df_recur_valid["Rekursif (ms)"],
                    mode='lines+markers',
                    name='Rekursif',
                    line=dict(color='#f59e0b', width=3),
                    marker=dict(size=10, symbol='diamond')
                ))
            
            # Layout grafik
            fig.update_layout(
                title={
                    'text': 'Perbandingan Waktu Eksekusi: Iteratif vs Rekursif',
                    'x': 0.5,
                    'xanchor': 'center',
                    'font': dict(size=20)
                },
                xaxis_title='Ukuran Input (n)',
                yaxis_title='Waktu Eksekusi (ms)',
                legend=dict(
                    yanchor="top",
                    y=0.99,
                    xanchor="left",
                    x=0.01,
                    bgcolor="rgba(0,0,0,0.5)"
                ),
                template='plotly_dark',
                hovermode='x unified',
                height=500
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Grafik tambahan: Bar Chart perbandingan
            st.markdown("### 📊 Bar Chart Perbandingan")
            
            fig_bar = go.Figure()
            
            fig_bar.add_trace(go.Bar(
                x=[str(x) for x in df_results["Ukuran (n)"]],
                y=df_results["Iteratif (ms)"],
                name='Iteratif',
                marker_color='#667eea'
            ))
            
            if not df_recur_valid.empty:
                # Untuk bar chart, perlu handle None values
                recur_values = []
                for idx, row in df_results.iterrows():
                    if row["Recursion Error"]:
                        recur_values.append(0)
                    else:
                        recur_values.append(row["Rekursif (ms)"])
                
                fig_bar.add_trace(go.Bar(
                    x=[str(x) for x in df_results["Ukuran (n)"]],
                    y=recur_values,
                    name='Rekursif',
                    marker_color='#f59e0b'
                ))
            
            fig_bar.update_layout(
                title={
                    'text': 'Perbandingan Waktu Eksekusi (Bar Chart)',
                    'x': 0.5,
                    'xanchor': 'center'
                },
                xaxis_title='Ukuran Input (n)',
                yaxis_title='Waktu Eksekusi (ms)',
                barmode='group',
                template='plotly_dark',
                height=400
            )
            
            st.plotly_chart(fig_bar, use_container_width=True)
            
            # Analisis otomatis
            st.markdown("### 🔍 Analisis Hasil Benchmark")
            
            # Hitung speedup
            if not df_recur_valid.empty:
                avg_speedup = (df_recur_valid["Rekursif (ms)"] / df_recur_valid["Iteratif (ms)"]).mean()
                
                st.markdown(f"""
                <div class="result-card">
                    <h4>📊 Ringkasan Analisis</h4>
                    <ul>
                        <li>Rata-rata speedup iteratif dibanding rekursif: <strong>{avg_speedup:.2f}x lebih cepat</strong></li>
                        <li>Jumlah ukuran yang berhasil diuji: <strong>{len(df_recur_valid)}/{len(test_sizes)}</strong></li>
                        <li>Ukuran maksimum tanpa error rekursi: <strong>n = {df_recur_valid["Ukuran (n)"].max()}</strong></li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
            
            # Cek jika ada recursion error
            df_error = df_results[df_results["Recursion Error"] == True]
            if not df_error.empty:
                st.markdown(f"""
                <div class="error-card">
                    <h4>⚠️ Recursion Error Terdeteksi</h4>
                    <p>
                        Algoritma rekursif mengalami <strong>RecursionError</strong> pada ukuran input berikut:
                        <strong>{", ".join([str(x) for x in df_error["Ukuran (n)"].tolist()])}</strong>
                    </p>
                    <p>
                        Hal ini menunjukkan keterbatasan algoritma rekursif pada data berskala besar 
                        karena kedalaman call stack yang terbatas.
                    </p>
                </div>
                """, unsafe_allow_html=True)

with tab4:
    st.markdown("## 📚 Analisis Kompleksitas Asimtotik")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🔄 Algoritma Iteratif")
        st.markdown("""
        <div class="algo-box">
            <h4>Analisis Kompleksitas Waktu</h4>
            <p>
                <span class="complexity-badge">T(n) = O(n)</span>
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        **Penjelasan:**
        
        ```python
        def dot_product_iterative(vector_a, vector_b):
            result = 0                      # O(1)
            n = len(vector_a)               # O(1)
            for i in range(n):              # Loop n kali
                result += vector_a[i] * vector_b[i]  # O(1)
            return result                   # O(1)
        ```
        
        **Perhitungan:**
        - Inisialisasi: $O(1)$
        - Loop: $n \\times O(1) = O(n)$
        - Return: $O(1)$
        
        $$T(n) = O(1) + O(n) + O(1) = O(n)$$
        
        ---
        
        **Kompleksitas Ruang:** $O(1)$
        
        Hanya menggunakan variabel konstan (`result`, `n`, `i`) tanpa 
        alokasi memori tambahan yang bergantung pada ukuran input.
        """)
    
    with col2:
        st.markdown("### 🔁 Algoritma Rekursif")
        st.markdown("""
        <div class="algo-box">
            <h4>Analisis Kompleksitas Waktu</h4>
            <p>
                <span class="complexity-badge">T(n) = O(n)</span>
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        **Penjelasan:**
        
        ```python
        def dot_product_recursive(vector_a, vector_b, n):
            if n == 0:                      # O(1)
                return 0
            return (vector_a[n-1] * vector_b[n-1]) +  # O(1)
                   dot_product_recursive(..., n-1)    # T(n-1)
        ```
        
        **Relasi Rekurensi:**
        
        $$T(n) = T(n-1) + O(1)$$
        $$T(0) = O(1)$$
        
        **Penyelesaian:**
        
        $$T(n) = T(n-1) + c$$
        $$T(n) = T(n-2) + 2c$$
        $$...$$
        $$T(n) = T(0) + nc = O(n)$$
        
        ---
        
        **Kompleksitas Ruang:** $O(n)$
        
        Setiap pemanggilan rekursif menambah frame baru ke call stack.
        Dengan kedalaman rekursi $n$, dibutuhkan ruang $O(n)$.
        """)
    
    st.markdown("---")
    
    # Tabel Perbandingan Lengkap
    st.markdown("### 📊 Tabel Perbandingan Kompleksitas")
    
    complexity_data = {
        "Aspek": [
            "Kompleksitas Waktu (Time)",
            "Kompleksitas Ruang (Space)",
            "Overhead per Operasi",
            "Risiko Stack Overflow",
            "Skalabilitas",
            "Kemudahan Implementasi"
        ],
        "Iteratif": [
            "O(n)",
            "O(1)",
            "Rendah",
            "Tidak Ada",
            "Sangat Baik",
            "Mudah"
        ],
        "Rekursif": [
            "O(n)",
            "O(n)",
            "Tinggi (function call overhead)",
            "Ada (tergantung depth)",
            "Terbatas",
            "Mudah"
        ]
    }
    
    df_complexity = pd.DataFrame(complexity_data)
    st.dataframe(df_complexity, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # Kesimpulan
    st.markdown("### 🎯 Kesimpulan")
    
    st.markdown("""
    <div class="result-card">
        <h4>📌 Mengapa Rekursif Lebih Lambat?</h4>
        <p>
            Meskipun kedua algoritma memiliki <strong>kompleksitas waktu O(n)</strong> yang sama,
            versi rekursif cenderung <strong>lebih lambat</strong> dalam praktiknya karena:
        </p>
        <ol>
            <li><strong>Function Call Overhead:</strong> Setiap pemanggilan rekursif membutuhkan 
                waktu untuk menyimpan dan memulihkan konteks eksekusi (register, return address, dll).</li>
            <li><strong>Stack Memory Access:</strong> Akses ke call stack lebih lambat dibanding 
                akses ke memori lokal dalam loop.</li>
            <li><strong>Cache Miss:</strong> Pemanggilan fungsi berulang dapat menyebabkan lebih 
                banyak cache miss dibanding iterasi sequensial.</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="warning-card">
        <h4>⚠️ Keterbatasan Rekursi pada Input Besar</h4>
        <p>
            Python memiliki <strong>batas kedalaman rekursi default (~1000)</strong> untuk mencegah 
            stack overflow. Meskipun dapat ditingkatkan dengan <code>sys.setrecursionlimit()</code>,
            penggunaan rekursi pada data besar tetap <strong>tidak disarankan</strong> karena:
        </p>
        <ul>
            <li>Risiko <strong>RecursionError</strong> atau crash</li>
            <li>Penggunaan memori yang tinggi (O(n) untuk call stack)</li>
            <li>Performa yang lebih lambat dibanding iteratif</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-card">
        <h4>💡 Rekomendasi</h4>
        <p>
            Untuk operasi <strong>Dot Product</strong> dan operasi vektor lainnya yang memproses 
            data dalam jumlah besar, <strong>gunakan pendekatan iteratif</strong> atau manfaatkan 
            library yang sudah dioptimasi seperti <strong>NumPy</strong> yang menggunakan 
            vectorized operations dengan implementasi dalam bahasa C.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #9ca3af; padding: 1rem;">
    <p>
        <strong>Tugas Besar - Analisis Kompleksitas Algoritma</strong><br>
        Perbandingan Algoritma Dot Product: Iteratif vs Rekursif<br>
        <em>Zaky Muhammad Fauzi</em>
    </p>
</div>
""", unsafe_allow_html=True)
