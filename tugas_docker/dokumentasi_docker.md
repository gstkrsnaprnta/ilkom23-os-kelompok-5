### 📁 Langkah 1: Membuat Folder Proyek

1. **Buka terminal** dan buat folder untuk proyek FastAPI Anda:

   ```bash
   mkdir tugas-docker
   cd tugas-docker
   ```

2. **Verifikasi folder telah dibuat**.

   ```bash
   ls
   ```

   Gambar folder yang dibuat:
   ![Membuat Folder Proyek](screenshot/create_folder.png)

---

### 📝 Langkah 2: Membuat File `main.py`

1. **Buat file `main.py`** untuk aplikasi FastAPI:

   ```bash
   touch main.py
   ```

2. **Buka `main.py` dan masukkan kode berikut**:

   ```python
   from fastapi import FastAPI

   app = FastAPI()

   @app.get("/")
   def read_root():
       return {"message": "Hello, World!"}
   ```

   Gambar file `main.py`:
   ![Buat File main.py](images/create_mainpy.png)

3. **Verifikasi bahwa file telah dibuat dan berisi kode yang benar**:

   ```bash
   cat main.py
   ```

   Gambar tampilan kode dalam `main.py`:
   ![Verifikasi Kode main.py](images/code_mainpy.png)

---

### 🚀 Langkah 3: Menjalankan Aplikasi FastAPI dengan Uvicorn

1. **Install FastAPI dan Uvicorn** menggunakan pip (pastikan Python sudah terinstal):

   ```bash
   pip install fastapi uvicorn
   ```

   Gambar proses instalasi FastAPI dan Uvicorn:
   ![Install FastAPI dan Uvicorn](images/install_fastapi.png)

2. **Jalankan aplikasi menggunakan Uvicorn**:

   ```bash
   uvicorn main:app --reload
   ```

   Gambar aplikasi berjalan di terminal:
   ![Jalankan Aplikasi dengan Uvicorn](images/uvicorn_running.png)

3. **Akses aplikasi di browser** dengan membuka alamat berikut:

   ```
   http://127.0.0.1:8000
   ```

   Gambar tampilan aplikasi di browser:
   ![Tampilan Aplikasi di Browser](images/browser_view.png)

---

### 🐳 Langkah 4: Membuat Dockerfile

1. **Buat file `Dockerfile`** untuk mengonfigurasi Docker container:

   ```bash
   touch Dockerfile
   ```

2. **Edit `Dockerfile` dan masukkan kode berikut**:

   ```dockerfile
   # Menggunakan image python 3.9 sebagai base image
   FROM python:3.9

   # Menetapkan direktori kerja di dalam container
   WORKDIR /app

   # Menyalin semua file ke dalam container
   COPY . .

   # Menginstall dependensi dari requirements.txt
   RUN pip install --no-cache-dir -r requirements.txt

   # Menjalankan aplikasi menggunakan uvicorn
   CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
   ```

   Gambar file `Dockerfile`:
   ![Buat Dockerfile](images/create_dockerfile.png)

3. **Verifikasi file `Dockerfile`** dengan perintah berikut:

   ```bash
   cat Dockerfile
   ```

   Gambar tampilan kode dalam `Dockerfile`:
   ![Verifikasi Kode Dockerfile](images/code_dockerfile.png)

---

### 📦 Langkah 5: Membuat File `requirements.txt`

1. **Buat file `requirements.txt`** untuk mendefinisikan dependensi:

   ```bash
   touch requirements.txt
   ```

2. **Masukkan dependensi berikut ke dalam file `requirements.txt`**:

   ```
   fastapi
   uvicorn
   ```

   Gambar file `requirements.txt`:
   ![Buat requirements.txt](images/create_requirements_txt.png)

3. **Verifikasi isi `requirements.txt`**:

   ```bash
   cat requirements.txt
   ```

   Gambar tampilan isi `requirements.txt`:
   ![Verifikasi isi requirements.txt](images/code_requirements_txt.png)

---

### 🐳 Langkah 6: Membangun Docker Image

1. **Bangun Docker image** menggunakan perintah berikut:

   ```bash
   docker build -t fastapi-hello-world .
   ```

   Gambar proses build Docker:
   ![Proses Build Docker](images/build_docker_image.png)

2. **Verifikasi bahwa Docker image telah berhasil dibuat**:

   ```bash
   docker images
   ```

   Gambar tampilan daftar image Docker:
   ![Verifikasi Docker Image](images/docker_images.png)

---

### 🐳 Langkah 7: Menjalankan Docker Container

1. **Jalankan Docker container** dengan perintah berikut:

   ```bash
   docker run -d -p 8000:8000 fastapi-hello-world
   ```

   Gambar Docker container berjalan:
   ![Docker Container Running](images/docker_running.png)

2. **Verifikasi Docker container sedang berjalan**:

   ```bash
   docker ps
   ```

   Gambar tampilan container yang berjalan:
   ![Verifikasi Docker Container](images/docker_ps.png)

---

### 🌐 Langkah 8: Mengakses Aplikasi melalui Docker

1. **Buka browser** dan kunjungi alamat berikut untuk melihat aplikasi berjalan:

   ```
   http://127.0.0.1:8000
   ```

   Gambar tampilan aplikasi di browser (dari Docker):
   ![Tampilan di Browser (Docker)](images/browser_view_docker.png)

---

### 🚀 Langkah 9: Menyelesaikan dan Membersihkan

1. **Hentikan Docker container** jika tidak lagi diperlukan:

   ```bash
   docker stop <container_id>
   ```

2. **Hapus Docker container** jika sudah tidak diperlukan lagi:

   ```bash
   docker rm <container_id>
   ```

3. **Hapus Docker image** jika sudah tidak diperlukan lagi:

   ```bash
   docker rmi fastapi-hello-world
   ```

---

## 🎉 Selesai!

Selamat, Anda telah berhasil membuat aplikasi **FastAPI** dengan Docker menggunakan terminal di macOS! Aplikasi ini berjalan dalam container Docker dan dapat diakses melalui browser.

---

## 📌 Referensi

- [Dokumentasi FastAPI](https://fastapi.tiangolo.com/)
- [Docker Documentation](https://docs.docker.com/)
  
---

### Instruksi untuk Menyertakan Screenshot:
- Gambar disimpan di dalam folder `images` di dalam proyek Anda.
- Setiap langkah disertai dengan screenshot sesuai dengan nama gambar yang digunakan, contohnya `create_folder.png`, `create_mainpy.png`, dan sebagainya.
- Pastikan gambar disimpan dengan nama yang mudah dipahami dan konsisten, sehingga mudah digunakan di dalam tutorial ini.

Jika Anda membutuhkan penjelasan lebih lanjut atau mengalami kesulitan, silakan beri tahu saya!
