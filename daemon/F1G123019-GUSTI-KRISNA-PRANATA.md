Berikut adalah versi lengkap dari `README.md` dengan penambahan ikon dan kelanjutan isi yang Anda minta, semuanya dalam satu file:

```markdown
# 🚀 Web App Daemon with Flask

![Flask](https://flask.palletsprojects.com/en/2.2.x/_images/flask-logo.png)

Selamat datang di proyek Web App Daemon yang menggunakan Flask! Proyek ini menyajikan aplikasi web sebagai daemon di macOS, memungkinkan Anda untuk menjalankannya secara otomatis saat sistem dinyalakan.

## ✨ Fitur Unggulan

- **Mudah diakses**: Aplikasi dapat diakses melalui browser di alamat lokal.
- **Otomatisasi**: Berjalan otomatis saat sistem mulai, berkat integrasi dengan LaunchDaemon.
- **Kustomisasi Mudah**: Konfigurasi melalui file plist untuk penyesuaian sederhana.

## 🛠️ Persyaratan

- **macOS**
- **Python 3**
- **Flask**

## 📦 Instalasi

1. **Clone Repository**:
   ```bash
   git clone https://github.com/username/repo-name.git
   cd repo-name
   ```

2. **Buat dan Aktifkan Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instal Flask**:
   ```bash
   pip install flask
   ```

4. **Buat File plist**:
   Simpan file `com.gustikrisna.webapp.plist` di `~/Library/LaunchAgents/`:
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

5. **Berikan Izin Eksekusi**:
   ```bash
   chmod +x /path/to/your/start_web.sh
   ```

6. **Muat Daemon**:
   ```bash
   sudo launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.gustikrisna.webapp.plist
   ```

## 🌐 Menjalankan Aplikasi

Setelah langkah-langkah di atas, aplikasi Anda siap diakses! Cukup buka browser dan kunjungi:
- [http://127.0.0.1:5006](http://127.0.0.1:5006)
- [http://192.168.1.9:5006](http://192.168.1.9:5006) (sesuaikan dengan IP Anda)

## 🐞 Debugging

Jika ada masalah, periksa log menggunakan:
```bash
log show --predicate 'eventMessage contains "com.gustikrisna.webapp"' --info --last 1h
```

## 🤝 Kontribusi

Kami menyambut baik kontribusi! Buatlah pull request atau laporkan masalah yang Anda temui.

## 📜 Lisensi

Proyek ini dilisensikan di bawah MIT License. Lihat file [LICENSE](LICENSE) untuk detail lebih lanjut.

---

Terima kasih telah menggunakan proyek ini! Semoga bermanfaat dan selamat berkoding! 🎉
```

### Catatan
- Pastikan untuk mengganti `https://github.com/username/repo-name.git` dengan URL repositori Anda yang sesuai.
- Sesuaikan `/path/to/your/start_web.sh` dengan path yang benar untuk skrip Anda.
- Anda dapat menambahkan ikon lain sesuai kebutuhan proyek Anda. Jika ada perubahan atau tambahan lain yang diinginkan, silakan beri tahu!