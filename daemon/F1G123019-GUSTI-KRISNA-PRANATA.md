# 🚀 Web App Daemon dengan Flask

![Flask](https://flask.palletsprojects.com/en/2.2.x/_images/flask-logo.png)

Selamat datang di proyek **Web App Daemon** yang menggunakan **Flask**! Proyek ini menyajikan aplikasi web sebagai daemon di macOS, memungkinkan Anda untuk menjalankannya secara otomatis saat sistem dinyalakan.

---

## ✨ Fitur Unggulan

- **Mudah diakses**: Aplikasi dapat diakses melalui browser di alamat lokal.
- **Otomatisasi**: Berjalan otomatis saat sistem mulai, berkat integrasi dengan LaunchDaemon.
- **Kustomisasi Mudah**: Konfigurasi melalui file plist untuk penyesuaian sederhana.

---

## 🛠️ Persyaratan

- **macOS**
- **Python 3**
- **Flask**

---

## 📦 Instalasi

### Langkah 1: Buat Folder Proyek

1. Buka terminal Anda.
2. Buat folder untuk proyek:
   ```bash
   mkdir web_app_daemon
   cd web_app_daemon
   ```

   ![Screenshot Buat Folder Proyek](/daemon/screenshot/tahap1.png)

### Langkah 2: Buat Virtual Environment

1. Buat virtual environment dengan perintah:
   ```bash
   python3 -m venv venv
   ```

2. Aktifkan virtual environment dengan perintah:
   ```bash
   source venv/bin/activate
   ```

   ![Screenshot Buat Folder Proyek](/daemon/screenshot/tahap2.png)

### Langkah 3: Instal Flask

Instal Flask di dalam virtual environment dengan perintah:
```bash
pip install flask
```

![Screenshot Install Flask](/Users/gustikrisnapranata/ILMU KOMPUTTER/SEMESTER 3/SISTEM OPERASI/ilkom23-os-kelompok-5/daemon/screenshot/screenshot3.png)

### Langkah 4: Buat File Aplikasi Flask

1. Buat file baru bernama `app.py` di dalam folder proyek:
   ```bash
   touch app.py
   ```

2. Buka `app.py` di editor teks dan tambahkan kode berikut:
   ```python
   from flask import Flask

   app = Flask(__name__)

   @app.route('/')
   def home():
       return "Hello, World! This is your Flask daemon."

   if __name__ == "__main__":
       app.run(host='0.0.0.0', port=5006)  # Ganti port jika perlu
   ```

   ![Screenshot Buat File Aplikasi Flask](/Users/gustikrisnapranata/ILMU KOMPUTER/SEMESTER 3/SISTEM OPERASI/ilkom23-os-kelompok-5/daemon/screenshot/screenshot4.png)

### Langkah 5: Buat File Skrip `start_web.sh`

1. Buat skrip shell bernama `start_web.sh` di direktori proyek Anda:
   ```bash
   touch start_web.sh
   ```

2. Buka `start_web.sh` di editor teks dan tambahkan baris berikut:
   ```bash
   #!/bin/bash
   source venv/bin/activate
   python app.py
   ```

3. Berikan izin eksekusi pada skrip dengan perintah:
   ```bash
   chmod +x start_web.sh
   ```

   ![Screenshot Create Shell Script](/Users/gustikrisnapranata/ILMU KOMPUTER/SEMESTER 3/SISTEM OPERASI/ilkom23-os-kelompok-5/daemon/screenshot/screenshot5.png)

### Langkah 6: Buat File LaunchAgent plist

1. Buat file plist bernama `com.belajardaemon.webapp.plist di direktori `~/Library/LaunchAgents/`:
   ```bash
   touch ~/Library/LaunchAgents/com.belajardaemon.webapp.plist
   ```

2. Buka file plist di editor teks dan tambahkan konten berikut:
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <dict>
       <key>Label</key>
       <string>com.gustikrisna.webapp</string>
       <key>ProgramArguments</key>
       <array>
           <string>/path/to/your/start_web.sh</string>
       </array>
       <key>RunAtLoad</key>
       <true/>
   </dict>
   </plist>
   ```

3. Ganti `/path/to/your/start_web.sh` dengan path yang sebenarnya untuk skrip Anda.

   ![Screenshot Create plist File](/Users/gustikrisnapranata/ILMU KOMPUTER/SEMESTER 3/SISTEM OPERASI/ilkom23-os-kelompok-5/daemon/screenshot/screenshot6.png)

### Langkah 7: Muat LaunchAgent

Muat LaunchAgent untuk menjalankan daemon dengan perintah:
```bash
sudo launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.belajardaemon.webapp.plist
```

![Screenshot Load LaunchAgent](/Users/gustikrisnapranata/ILMU KOMPUTER/SEMESTER 3/SISTEM OPERASI/ilkom23-os-kelompok-5/daemon/screenshot/screenshot7.png)

### Langkah 8: Akses Aplikasi Web Anda

Setelah menyelesaikan langkah-langkah di atas, aplikasi Flask Anda harus sudah berjalan. Buka browser dan kunjungi:
- [http://127.0.0.1:5006](http://127.0.0.1:5006)
- [http://192.168.1.9:5006](http://192.168.1.9:5006) (sesuaikan dengan IP Anda)

![Screenshot Access Web Application](/Users/gustikrisnapranata/ILMU KOMPUTER/SEMESTER 3/SISTEM OPERASI/ilkom23-os-kelompok-5/daemon/screenshot/screenshot8.png)

## 🐞 Pemecahan Masalah

Jika Anda mengalami masalah, periksa log menggunakan:
```bash
log show --predicate 'eventMessage contains "com.gustikrisna.webapp"' --info --last 1h
```

### 🔧 Tips dan Trik

- **Port Sudah Digunakan**: Jika Anda menerima pesan bahwa port yang ditentukan sudah digunakan (seperti 5008), periksa proses yang berjalan dengan:
  ```bash
  lsof -i :5008
  ```
  Hentikan proses yang ada jika perlu atau ubah port di `app.py`.

- **Perizinan Skrip**: Pastikan skrip `start_web.sh` memiliki izin eksekusi. Gunakan:
  ```bash
  chmod +x start_web.sh
  ```

- **Menggunakan Virtual Environment**: Pastikan untuk selalu mengaktifkan virtual environment sebelum menjalankan aplikasi Flask Anda. Jika Anda melihat pesan bahwa Python tidak dapat menemukan file, pastikan Anda berada di dalam virtual environment.

---

## 🤝 Kontribusi

Kami menyambut baik kontribusi! Buatlah pull request atau laporkan masalah yang Anda temui.

## 📜 Lisensi

Proyek ini dilisensikan di bawah MIT License. Lihat file [LICENSE](LICENSE) untuk detail lebih lanjut.

---

Terima kasih telah menggunakan proyek ini! Semoga bermanfaat dan selamat berkoding! 🎉
```

### Catatan:
1. Pastikan untuk mengganti path pada bagian `com.belajardaemon.webapp.plist` dengan path yang benar untuk skrip `start_web.sh`.
2. Saya juga menambahkan beberapa tips dan trik untuk pemecahan masalah yang mungkin Anda temui selama proses pengembangan. Jika ada hal lain yang ingin Anda tambahkan atau ubah, silakan beri tahu!