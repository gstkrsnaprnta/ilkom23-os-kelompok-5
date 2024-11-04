# Menjalankan Program Sebagai Daemon dengan Task Scheduler di Windows

Berikut ini adalah langkah-langkah untuk menjalankan program `hello_web.py` sebagai daemon di Windows menggunakan Task Scheduler.

## 1. Membuka Task Scheduler
- Tekan **Windows + R**, ketik **`taskschd.msc`**, lalu tekan **Enter** untuk membuka Task Scheduler.

## 2. Membuat Task Baru
1. Klik **Create Basic Task** di menu sebelah kanan.
2. Beri nama task, misalnya **Hello Web Daemon**, lalu klik **Next**.

## 3. Mengatur Trigger (Pemicu)
- Pilih salah satu opsi berikut:
  - **When the computer starts** (agar program berjalan setiap kali komputer dinyalakan).
  - **At log on** (agar program berjalan setiap kali pengguna login).
- Klik **Next**.

## 4. Mengatur Aksi (Action)
1. Pilih **Start a Program**, lalu klik **Next**.
2. Pada bagian **Program/script**, masukkan path lengkap ke **python.exe**.  
   **Contoh:**
3. Pada **Add arguments (optional)**, masukkan path ke file **`hello_web.py`**.  
**Contoh:**
4. Klik **Next**.

## 5. Menyelesaikan Pembuatan Task
- Klik **Finish** untuk menyimpan task.

## 6. Pengujian dan Verifikasi
1. Di Task Scheduler, cari task yang telah dibuat, misalnya **Hello Web Daemon**.
2. Klik kanan pada task tersebut dan pilih **Run**.
3. Buka browser dan akses **http://localhost:8080**.
4. Jika berhasil, kamu akan melihat pesan **"Hello Web!"** di browser.



 