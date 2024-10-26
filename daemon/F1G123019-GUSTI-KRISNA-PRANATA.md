# 🐍 Panduan Membuat Layanan Flask dengan systemd di Kali Linux

Panduan ini akan memandu Anda menjalankan aplikasi Flask sebagai layanan sistem menggunakan `systemd` di Kali Linux. Dengan panduan ini, aplikasi Flask Anda akan berjalan otomatis saat booting dan dapat dikelola dengan perintah `systemctl`.

---

## ✅ Prasyarat
Pastikan Anda memiliki:
- **Python 3** dan **Flask** sudah terpasang di Kali Linux.
- **Hak akses `sudo`** untuk menjalankan perintah administrasi.

---

## 🚀 Langkah-Langkah

### 1. 📝 Siapkan Aplikasi Flask
1. **Buat file `app.py`** di direktori yang Anda inginkan, misalnya di `/home/kali/app.py`.
2. **Tambahkan kode dasar Flask** berikut ke dalam file `app.py`:

    ```python
    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def hello():
        return "Hello, Flask!"

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8000)
    ```

3. **Uji Aplikasi secara Lokal**  
   Jalankan aplikasi untuk memastikan berjalan dengan benar:

    ```bash
    python3 /home/kali/app.py
    ```

   Buka `http://localhost:8000` di browser Anda dan pastikan halaman menampilkan "Hello, Flask!" sebelum melanjutkan.

---

### 2. 📄 Buat File Unit systemd
1. Buat file unit layanan dengan perintah berikut:

    ```bash
    sudo nano /etc/systemd/system/flaskapp.service
    ```

2. Isi file dengan konfigurasi berikut:

    ```ini
    [Unit]
    Description=Flask App Service
    After=network.target

    [Service]
    User=kali                # Nama pengguna yang menjalankan layanan
    ExecStart=/usr/bin/python3 /home/kali/app.py  # Path ke aplikasi Flask
    WorkingDirectory=/home/kali
    Restart=always           # Restart layanan otomatis jika mati mendadak

    [Install]
    WantedBy=multi-user.target
    ```

   - **User**: Nama pengguna yang menjalankan layanan ini (misalnya, `kali`).
   - **ExecStart**: Path ke Python dan file aplikasi Flask Anda (`/usr/bin/python3 /home/kali/app.py`).
   - **Restart**: Memastikan layanan restart otomatis jika terjadi crash.

---

### 3. 🔄 Reload systemd
Setelah membuat file unit, reload `systemd` untuk mengenali layanan baru:

   ```bash
   sudo systemctl daemon-reload
   ```

---

### 4. ▶️ Mulai Layanan
Mulai layanan Flask dengan perintah berikut:

   ```bash
   sudo systemctl start flaskapp.service
   ```

---

### 5. 🌟 Aktifkan Layanan saat Booting
Agar layanan otomatis berjalan saat sistem boot, aktifkan layanan:

   ```bash
   sudo systemctl enable flaskapp.service
   ```

---

### 6. 🔍 Periksa Status Layanan
Cek status layanan untuk memastikan aplikasi Flask berjalan dengan baik:

   ```bash
   sudo systemctl status flaskapp.service
   ```

---

### 7. 🛠️ Debugging Layanan
Jika layanan tidak berjalan sebagaimana mestinya, Anda bisa memeriksa error di log:

   ```bash
   sudo journalctl -u flaskapp.service -f
   ```

   **📸 Contoh Bukti Layanan Berjalan**:  
   ![Bukti](daemon/screenshot/F1G123019-GUSTI-KRISNA-PRANATA.png)

```

Dengan cara ini, Markdown akan menampilkan gambar saat Anda melakukan preview atau melihat file tersebut di platform seperti GitHub.
## 🎉 Kesimpulan
Dengan mengikuti langkah-langkah di atas, Anda telah berhasil membuat dan mengelola layanan Flask menggunakan `systemd` di Kali Linux. Pastikan untuk memeriksa log dan status layanan secara berkala untuk menjaga stabilitas aplikasi Anda.
```
