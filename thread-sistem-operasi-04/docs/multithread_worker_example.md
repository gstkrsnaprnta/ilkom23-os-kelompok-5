# 🧵 Python Multi-threading Example

**Proyek ini** adalah contoh sederhana implementasi multi-threading di Python. Program ini menjalankan dua thread secara bersamaan untuk mensimulasikan proses paralel yang bekerja secara simultan.

## 🎯 Tujuan Proyek

Proyek ini bertujuan untuk:
1. Memahami dan menerapkan **multi-threading** menggunakan modul `threading` pada Python.
2. Mensimulasikan dua thread yang berjalan secara bersamaan, dimana masing-masing thread menjalankan tugas secara paralel.

## 🚀 Teknologi yang Digunakan

- **Python 3.x** - Bahasa pemrograman yang digunakan untuk membangun simulasi.
- **Threading Module** - Modul bawaan Python untuk menjalankan thread.

## ⚙️ Penjelasan Kode

Kode ini terdiri dari beberapa bagian:

1. **Fungsi `worker`**: Fungsi yang akan dijalankan di dalam setiap thread. Fungsi ini akan menampilkan pesan ketika thread mulai bekerja dan berakhir.
   ```python
   def worker(thread_name):
       print(f'Thread {thread_name} mulai bekerja.')
       time.sleep(2)  # Simulasi pekerjaan yang memakan waktu 2 detik
       print(f'Thread {thread_name} selesai.')
   ```

2. **Membuat thread**: Kita membuat dua thread, masing-masing menjalankan fungsi `worker` dengan parameter berbeda ('A' dan 'B').
   ```python
   thread1 = threading.Thread(target=worker, args=('A',))
   thread2 = threading.Thread(target=worker, args=('B',))
   ```

3. **Memulai thread**: Kedua thread dimulai menggunakan `start()`.
   ```python
   thread1.start()
   thread2.start()
   ```

## 🛠️ Cara Menjalankan Program

### Prasyarat
- Pastikan kamu sudah menginstal **Python 3.x** di sistemmu. Jika belum, kamu dapat mengunduhnya [di sini](https://www.python.org/downloads/).

### Langkah-Langkah Menjalankan
1. **Clone repository ini** (jika ini bagian dari repository proyek):
   ```bash
   git clone https://github.com/username/python-multithreading-example.git
   cd python-multithreading-example
   ```

2. **Jalankan program:**
   Untuk menjalankan program di terminal/command prompt, ketik perintah berikut:
   ```bash
   python3 threading_example.py
   ```

3. **Output Program**:
   Ketika program dijalankan, output akan menunjukkan bahwa dua thread bekerja secara paralel:
   ```
   Thread A mulai bekerja.
   Thread B mulai bekerja.
   Thread A selesai.
   Thread B selesai.
   ```

## 🧑‍💻 Tim Pengembang
| Nama         | Kontribusi             |
|--------------|------------------------|
| Developer    | Pembuatan program contoh multi-threading |

## 📝 Lisensi
Proyek ini dilisensikan di bawah [MIT License](LICENSE).
