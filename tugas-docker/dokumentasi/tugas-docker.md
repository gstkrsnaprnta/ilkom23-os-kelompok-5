
# 🎉 Tutorial: Membuat Aplikasi FastAPI dengan Docker - Hello World

## 📁 Langkah 1: Membuat Folder Proyek

1. **Buka terminal dan buat folder untuk proyek Anda:**

```bash
mkdir tugas-docker
cd tugas-docker
```

Gambar folder yang dibuat:
![Membuat Folder Proyek](screenshot/membuat_file_py.png)

---

## 📝 Langkah 2: Membuat File `main.py`

2. **Buat file Python bernama `main.py`:**

```bash
touch main.py
```

Gambar file `main.py`:
![Buat File main.py](images/create_mainpy.png)

3. **Buka `main.py` dan tambahkan kode berikut:**

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
```

Gambar kode dalam `main.py`:
![Kode dalam main.py](images/code_mainpy.png)

---

## 🚀 Langkah 3: Menjalankan FastAPI dengan Uvicorn

4. **Install FastAPI dan Uvicorn menggunakan pip:**

```bash
pip install fastapi uvicorn
```

Gambar instalasi FastAPI:
![Install FastAPI](images/install_fastapi.png)

5. **Jalankan aplikasi FastAPI menggunakan Uvicorn:**

```bash
uvicorn main:app --reload
```

Gambar aplikasi berjalan:
![Aplikasi Berjalan](images/uvicorn_running.png)

---

## 🌐 Langkah 4: Akses Aplikasi di Browser

6. **Buka browser dan akses aplikasi di alamat berikut:**

```
http://127.0.0.1:8000
```

Gambar tampilan aplikasi di browser:
![Tampilan di Browser](images/browser_view.png)

---

## 🐳 Langkah 5: Membuat Dockerfile

7. **Buat file `Dockerfile` untuk aplikasi FastAPI:**

```bash
touch Dockerfile
```

Gambar file `Dockerfile`:
![Buat Dockerfile](images/create_dockerfile.png)

8. **Tambahkan kode berikut ke dalam `Dockerfile`:**

```dockerfile
FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Gambar kode dalam `Dockerfile`:
![Kode Dockerfile](images/code_dockerfile.png)

---

## 📦 Langkah 6: Membuat File `requirements.txt`

9. **Buat file `requirements.txt` dan masukkan dependensi berikut:**

```bash
touch requirements.txt
```

Gambar file `requirements.txt`:
![Buat requirements.txt](images/create_requirements_txt.png)

Isi `requirements.txt`:
```
fastapi
uvicorn
```

---

## 🐳 Langkah 7: Membuat Docker Image dan Menjalankan Kontainer

10. **Bangun Docker image:**

```bash
docker build -t fastapi-hello-world .
```

Gambar proses build Docker:
![Build Docker Image](images/build_docker_image.png)

11. **Jalankan Docker container:**

```bash
docker run -d -p 8000:8000 fastapi-hello-world
```

Gambar Docker container berjalan:
![Docker Container Running](images/docker_running.png)

---

## 🎉 Langkah 8: Akses Aplikasi melalui Docker

12. **Buka browser dan akses aplikasi yang berjalan di Docker di alamat berikut:**

```
http://127.0.0.1:8000
```

Gambar tampilan aplikasi di browser (dari Docker):
![Tampilan di Browser (Docker)](images/browser_view_docker.png)

---

## 🚀 Selesai!

Selamat, Anda telah berhasil membuat aplikasi **FastAPI** dengan Docker dan menjalankannya di dalam container. Anda sekarang dapat mengembangkan dan mengintegrasikan aplikasi ini lebih lanjut!

---

## 📌 Referensi

- [Dokumentasi FastAPI](https://fastapi.tiangolo.com/)
- [Docker Documentation](https://docs.docker.com/)
```

### Penjelasan Struktur Dokumentasi
- **Langkah-langkah**: Setiap langkah tutorial dimulai dengan perintah terminal yang harus dijalankan.
- **Screenshot**: Setiap langkah diikuti dengan gambar yang relevan, yang disimpan di dalam folder `images`. Anda akan mengganti nama file gambar sesuai dengan nama screenshot yang Anda ambil.
- **Perintah Terminal**: Perintah terminal diberikan secara langsung untuk setiap langkah.
  
### Menyertakan Gambar dalam Markdown
Gambar disertakan menggunakan sintaks berikut:

```markdown
![Deskripsi Gambar](images/nama_gambar.png)
```

Pastikan untuk menyesuaikan `nama_gambar.png` dengan nama file gambar yang Anda simpan di dalam folder `images`.

---

Jika Anda membutuhkan bantuan dalam menyiapkan gambar atau menyesuaikan tutorial ini, jangan ragu untuk bertanya!
