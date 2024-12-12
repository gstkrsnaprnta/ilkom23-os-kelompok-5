# perintah dasar docker
Berikut adalah beberapa perintah dasar yang sering digunakan dalam Docker untuk mengelola container, image, dan volume.

##1. `docker --version`
Menampilkan versi Docker yang terinstal di sistem.
contoh:
```bash
docker --version

##2. `docker ps`
Menampilkan daftar container yang sedang berjalan.
contoh:
docker ps

##3. `docker ps -a`
Menampilkan semua container, termasuk yang berhenti (exited). Ini berguna untuk memeriksa container yang sudah tidak aktif.
contoh:
docker ps -a

##4. `docker run`
Perintah ini digunakan untuk menjalankan container baru dari sebuah image.
contoh:
docker run -d -p 80:80 nginx

##5. `docker stop`
perintah untuk menghentikan container yang sedang berjalan.
contoh:
docker stop <container_id>

##6. `docker start`
perintah untuk memulai kembali container yang sudah dihentikan.
contoh:
docker start <container_id>




