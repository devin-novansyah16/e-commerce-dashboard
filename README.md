# E-Commerce Sales Analytics Dashboard

Dashboard interaktif analisis penjualan e-commerce — live demo, instruksi menjalankan lokal, dan ringkasan proyek.

## Demo
- Live app: https://e-commerce-dashboard-4ypsnvhy59ch8jncabkhhw.streamlit.app

	> Jika URL berbeda, ganti link di atas dengan URL Streamlit Cloud Anda.

## Ringkasan
Dashboard ini menampilkan metrik utama penjualan, grafik pesanan harian, dan performa kategori produk menggunakan dataset penjualan bersih.

## Fitur
- Total orders & revenue
- Grafik pesanan harian
- Best & worst performing product categories

## Cara menjalankan (lokal)
1. Clone repository:
```bash
git clone https://github.com/devinnovva/e-commerce-dashboard.git
cd e-commerce-dashboard
```
2. Buat virtual environment dan install dependency:
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
pip install -r requirements.txt
```
3. Jalankan Streamlit:
```bash
streamlit run dashboard/dashboard.py
```

## Struktur project
- `dashboard/` — kode Streamlit utama (`dashboard.py`)
- `data/` — dataset CSV yang digunakan
- `assets/` — (opsional) screenshot dan GIF demo

## Data
Dataset yang digunakan ada di folder `data/` (pastikan file `all_data.csv` tersedia).

## Dependensi
Lihat `requirements.txt` untuk daftar paket Python yang dibutuhkan.

## Lisensi & Kontak
Licensed under MIT. Untuk pertanyaan, hubungi: devinnovva (GitHub profile) atau email.

---
_Created for portfolio — feel free to adapt content, add screenshots, and a short case study._
 