# 🧾 Python Multi-threading: Payment Processing and Notification System

**Proyek ini** adalah simulasi multi-threading sederhana di Python yang mensimulasikan proses pembayaran dan pengiriman notifikasi secara paralel menggunakan `threading`. Program ini dibuat untuk menunjukkan bagaimana dua tugas independen dapat dilakukan secara bersamaan menggunakan multi-threading, seperti pada sistem pemrosesan pesanan di e-commerce.

## 🎯 Tujuan Proyek

Proyek ini bertujuan untuk:
1. Memahami konsep **multi-threading** menggunakan modul `threading` pada Python.
2. Mengimplementasikan dua proses simultan, yaitu **proses pembayaran** dan **pengiriman notifikasi**.
3. Membangun simulasi sederhana yang menggambarkan sistem yang efisien dengan tugas-tugas yang berjalan secara paralel.

## 🚀 Teknologi yang Digunakan

- **Python 3.x** - Bahasa pemrograman yang digunakan untuk mengembangkan simulasi ini.
- **Threading Module** - Modul untuk menjalankan proses secara paralel dengan thread.

## ⚙️ Penjelasan Kode

Kode ini terdiri dari beberapa bagian utama:

1. **Fungsi `process_payment`**: Mensimulasikan proses pembayaran untuk sebuah pesanan. Proses ini berjalan selama 3 detik menggunakan `time.sleep(3)`.
    ```python
    def process_payment(order_id):
        print(f'Proses pembayaran untuk pesanan {order_id} dimulai.')
        time.sleep(3)  # Simulasi proses pembayaran
        print(f'Pembayaran untuk pesanan {order_id} berhasil.')
    ```

2. **Fungsi `send_notification`**: Mensimulasikan pengiriman notifikasi setelah pembayaran selesai. Proses ini berjalan selama 1 detik menggunakan `time.sleep(1)`.
    ```python
    def send_notification(order_id):
        time.sleep(1)  # Simulasi waktu tunggu untuk pengiriman notifikasi
        print(f'Notifikasi pengiriman untuk pesanan {order_id} dikirim.')
    ```

3. **Membuat dan Menjalankan Thread**: Dua thread dibuat untuk menjalankan proses pembayaran dan pengiriman notifikasi secara bersamaan.
    ```python
    order_id = 12345

    # Membuat thread untuk proses pembayaran dan pengiriman notifikasi
    payment_thread = threading.Thread(target=process_payment, args=(order_id,))
    notification_thread = threading.Thread(target=send_notification, args=(order_id,))

    # Memulai thread
    payment_thread.start()
    notification_thread.start()

    # Menunggu thread selesai
    payment_thread.join()
    notification_thread.join()
    ```

4. **Menunggu Thread Selesai**: Program menunggu kedua thread selesai menggunakan `.join()` untuk memastikan kedua proses selesai sebelum menampilkan pesan akhir.
    ```python
    print('Semua proses selesai.')
    ```

## 🛠️ Cara Menjalankan Program

### Prasyarat

- Pastikan kamu sudah menginstal **Python 3.x** di sistemmu. Jika belum, kamu dapat mengunduhnya [di sini](https://www.python.org/downloads/).

### Langkah-langkah Menjalankan Program:

1. **Clone repository ini** (jika ini bagian dari repository proyek):
    ```bash
    git clone https://github.com/username/python-multithreading-example.git
    cd python-multithreading-example
    ```

2. **Jalankan program**:
    Untuk menjalankan program di terminal/command prompt, ketik perintah berikut:
    ```bash
    python3 threading_payment_notification.py
    ```

3. **Output Program**:
    Ketika program dijalankan, output akan menunjukkan bahwa proses pembayaran dan pengiriman notifikasi dijalankan secara bersamaan:
    ```
    Proses pembayaran untuk pesanan 12345 dimulai.
    Notifikasi pengiriman untuk pesanan 12345 dikirim.
    Pembayaran untuk pesanan 12345 berhasil.
    Semua proses selesai.
    ```

## 🧑‍💻 Tim Pengembang
| Nama         | Kontribusi             |
|--------------|------------------------|
| Developer    | Pengembangan program dan dokumentasi multi-threading |

## 📝 Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).

