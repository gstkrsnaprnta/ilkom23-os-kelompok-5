# Tahapan Pembuatan Daemon Process

1. **Membuat Program Web**: Menggunakan Flask untuk membuat aplikasi web sederhana.
2. **Install Dependensi**: Install python-daemon menggunakan perintah:
3. **Mengubah Aplikasi Menjadi Daemon**: 
- Buat file daemon (`daemon_flask.py`) yang menjalankan aplikasi Flask di background.
- Gunakan `with daemon.DaemonContext()` agar proses berjalan di background.
4. **Menjalankan Daemon**:
Jalankan perintah berikut untuk menjalankan daemon:
python daemon_flask.py
5. **Bukti Screenshot**:
Berikut adalah bukti bahwa aplikasi berhasil berjalan:

![Screenshot Aplikasi Berjalan](screenshots/screenshot_app_running.png)
