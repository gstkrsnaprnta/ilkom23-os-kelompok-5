# 🌐 Aplikasi Web Container

**Proyek ini** adalah aplikasi web berbasis container yang dikembangkan sebagai bagian dari **Tugas Besar Mata Kuliah Sistem Operasi**. Aplikasi ini menggunakan **Docker** untuk otomatisasi pengelolaan lingkungan pengembangan, mempermudah distribusi, dan deployment aplikasi. Kami mengimplementasikan **Laravel** sebagai framework backend dan **MySQL** sebagai basis data.

## 🚀 Teknologi yang Digunakan
- **Docker** - Containerization platform untuk lingkungan pengembangan.
- **Laravel** - PHP framework untuk pengembangan aplikasi web.
- **MySQL** - Relational Database Management System (RDBMS).

## 🎯 Tujuan Proyek
Proyek ini bertujuan untuk:
1. Memahami dan menerapkan konsep **containerisasi** menggunakan Docker.
2. Mengembangkan aplikasi web yang berjalan di dalam container Docker.
3. Mengotomatiskan **deployment** aplikasi web dengan konfigurasi container Docker.

## ⚙️ Fitur Aplikasi
- **CRUD** (Create, Read, Update, Delete) untuk mengelola entitas di dalam aplikasi.
- **Authentication** untuk melindungi dan membatasi akses pengguna.

## 🛠️ Cara Menjalankan Proyek

### Prasyarat
Sebelum memulai, pastikan kamu sudah menginstal:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Langkah-langkah

1. **Clone repository ini:**
   ```bash
   git clone https://github.com/gstkrsnaprnta/ilkom23-os-kelompok-5.git
   cd ilkom23-os-kelompok-5
   ```

2. **Bangun dan jalankan container Docker:**
   ```bash
   docker-compose up --build
   ```

3. **Akses aplikasi:**
   - Buka browser dan akses `http://localhost:8000` untuk membuka aplikasi web.
   - MySQL database dapat diakses di `localhost:3306` (default port).

4. **Buat Database:**
   - Akses container `mysql` dengan:
     ```bash
     docker-compose exec mysql mysql -u root -p
     ```
   - Buat database baru jika belum ada:
     ```sql
     CREATE DATABASE nama_database;
     ```

## 📂 Struktur Proyek

```
.
├── docker-compose.yml   # Mengelola container Docker
├── Dockerfile           # Membuat image Docker untuk Laravel
├── src/                 # Aplikasi Laravel
│   ├── app/             # Folder inti aplikasi Laravel
│   └── ...              # File dan folder Laravel lainnya
└── README.md            # Dokumentasi proyek ini
```

## 🧑‍💻 Tim Pengembang

| NIM        | Nama                         |
|------------|------------------------------|
| F1G123019  | Gusti Krisna Pranata         |
| F1G123012  | Rasma AR                     |
| F1G123002  | Ahfan                        |
| F1G123049  | Maisun Mufliha Aprilia M.     |
| F1G123045  | Indah Haerunisa              |
| F1G123050  | Miftahul Jannah              |
| F1G123042  | Aulia Ayu Rafanisti          |

## 🌐 Penjelasan Docker dan Aplikasi
### Apa itu Docker?
**Docker** adalah platform yang memungkinkan pengembang untuk mengemas aplikasi dan dependensinya ke dalam container, yang bisa dijalankan di mana saja.

### Mengapa menggunakan Docker?
Dengan Docker, kita dapat menjalankan aplikasi secara konsisten di berbagai lingkungan (development, testing, production) tanpa khawatir tentang perbedaan konfigurasi.

## 📝 Lisensi
Proyek ini dilisensikan di bawah [MIT License](LICENSE).

---

Dengan README ini, proyekmu akan lebih terstruktur, profesional, dan mudah dipahami oleh pengembang lain yang ingin berkontribusi atau menggunakan aplikasimu!