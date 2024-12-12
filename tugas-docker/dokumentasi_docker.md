# 🚀 Tutorial: Membuat Aplikasi FastAPI dengan Web Interface dan Docker

Tutorial ini akan membawa Anda melalui langkah-langkah untuk membuat aplikasi FastAPI dengan web interface menggunakan Jinja2 dan menjalankannya di dalam Docker container. Anda akan belajar bagaimana membuat halaman web menggunakan template HTML, merender halaman dengan FastAPI, dan mengemas aplikasi menggunakan Docker.

---

### 📁 Langkah 1: Membuat Folder Proyek

1. Buka terminal dan buat folder untuk proyek FastAPI Anda:

   bash
   mkdir tugas-docker
   cd tugas-docker
   

2. Verifikasi folder telah dibuat:

   bash
   ls
   

   Gambar folder yang dibuat:
   
   ![Membuat Folder Proyek](screenshot/create_folder.png)

---
### 📝 Langkah 2: Membuat File main.py

1. Buka terminal dan buat file main.py menggunakan nano:

   bash
   nano main.py
   

2. *Buka main.py* dan tambahkan kode berikut untuk menginisialisasi aplikasi FastAPI serta menyiapkan halaman web menggunakan Jinja2:

   python
   from fastapi import FastAPI
   from fastapi.templating import Jinja2Templates
   from starlette.responses import HTMLResponse
   from starlette.requests import Request

   # Inisialisasi FastAPI dan Jinja2Templates
   app = FastAPI()
   templates = Jinja2Templates(directory="templates")

   # Endpoint untuk halaman utama (Home)
   @app.get("/", response_class=HTMLResponse)
   def read_root(request: Request):
       return templates.TemplateResponse("home.html", {"request": request})

   # Endpoint untuk halaman about
   @app.get("/about", response_class=HTMLResponse)
   def about(request: Request):
       return templates.TemplateResponse("about.html", {"request": request})