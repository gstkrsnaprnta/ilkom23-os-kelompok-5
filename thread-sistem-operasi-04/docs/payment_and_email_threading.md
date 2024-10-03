# 🧾 Python Multi-threading: Payment Processing and Email Notification System

**Proyek ini** adalah simulasi multi-threading sederhana di Python yang mensimulasikan proses pembayaran dan pengiriman email notifikasi secara paralel menggunakan `threading`. Program ini dirancang untuk menunjukkan bagaimana dua tugas independen dapat dilakukan secara bersamaan, seperti pada sistem pemrosesan pesanan di e-commerce.

## 🎯 Tujuan Proyek

Proyek ini bertujuan untuk:
1. Memahami konsep **multi-threading** menggunakan modul `threading` pada Python.
2. Mengimplementasikan dua proses simultan, yaitu **proses pembayaran** dan **pengiriman email**.
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
        return True  # Mengembalikan status pembayaran sukses
    ```

2. **Fungsi `send_email`**: Mensimulasikan pengiriman email konfirmasi setelah pembayaran selesai. Proses ini berjalan selama 2 detik menggunakan `time.sleep(2)`.

    ```python
    def send_email(order_id):
        print(f'Mengirim email untuk pesanan {order_id}...')
        time.sleep(2)  # Simulasi waktu pengiriman email
        print(f'Email untuk pesanan {order_id} telah dikirim.')
    ```

3. **Fungsi `handle_order`**: Mengelola seluruh proses. Jika pembayaran berhasil, fungsi ini akan memulai thread untuk mengirim email.

    ```python
    def handle_order(order_id):
        if process_payment(order_id):
            email_thread = threading.Thread(target=send_email, args=(order_id,))
            email_thread.start()  # Memulai pengiriman email di thread terpisah
            email_thread.join()   # Menunggu email dikirim sebelum melanjutkan
    ```

4. **Menjalankan Program**: Menjalankan program dengan memberikan `order_id` dan memanggil fungsi `handle_order`.

    ```python
    order_id = 12345
    handle_order(order_id)
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
    python threading_payment_email.py
    ```

3. **Output Program**:
    Ketika program dijalankan, output akan menunjukkan bahwa proses pembayaran dan pengiriman email dijalankan secara bersamaan:
    ```
    Proses pembayaran untuk pesanan 12345 dimulai.
    Pembayaran untuk pesanan 12345 berhasil.
    Mengirim email untuk pesanan 12345...
    Email untuk pesanan 12345 telah dikirim.
    Semua proses selesai.
    ```

## 🧑‍💻 Tim Pengembang
| Nama         | Kontribusi             |
|--------------|------------------------|
| Developer    | Pengembangan program dan dokumentasi multi-threading |

## 📄 Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).
