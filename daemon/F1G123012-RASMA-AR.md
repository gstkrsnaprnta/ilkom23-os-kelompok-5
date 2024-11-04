# Tutorial: Membuat Website Login Sederhan dengan PHP dan Daemon Process

## Deskripsi
Tutorial ini akan membimbing Anda dalam membuat website login sederhana menggunakan PHP yang memanfaatkan daemon process. Daemon ini dapat digunakan untuk menangani tugas di latar belakang, seperti memonitor aktivitas login.

## Prasyarat
- Server web dengan PHP (misalnya, XAMPP atau LAMP).
- Pengetahuan dasar tentang PHP dan HTML.

## Struktur Direktori
Buat struktur direktori berikut untuk proyek Anda:

## Langkah-langkah

### 1. Membuat Script PHP untuk Login (`login.php`)
Buat file `login.php` 

### 2. Membuat Halaman Utama Setelah Login (index.php)
Buat file `index.php`

### 3. Membuat Script Logout (logout.php)
Buat file `logout.php`

### 4. Membuat Daemon Process Script (daemon.php)
Buat file `daemon.php`

## Cara Menjalankan Daemon
Daemon dijalankan ketika pengguna berhasil login dengan menggunakan fungsi exec() dari PHP yang menjalankan daemon di latar belakang secara asinkron. Ini memastikan bahwa daemon tetap berjalan meskipun pengguna sudah tidak melakukan aktivitas di situs web.

## Keamanan dan Optimasi
*Sanitasi Input* : Pastikan untuk melakukan sanitasi dan validasi input agar lebih aman.
*Enkripsi Password*: Gunakan fungsi password_hash() dan password_verify() untuk enkripsi password.
*Optimasi Daemon*: Sesuaikan daemon process untuk menangani berbagai tugas latar belakang sesuai kebutuhan.
=======






