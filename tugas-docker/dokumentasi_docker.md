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
3. *Simpan dan keluar* dari *nano*:
   - Tekan Ctrl + O untuk menyimpan file.
   - Tekan Enter untuk mengonfirmasi nama file.
   - Tekan Ctrl + X untuk keluar dari *nano*.

   Gambar kode dalam main.py yang dibuka dengan nano:
   
   ![Kode dalam main.py](screenshot/code_mainpy_nano.png)
   
---

### 🌐 Langkah 3: Menyiapkan Struktur Folder Template

1. *Buat folder templates/* untuk menyimpan file HTML:

   bash
   mkdir templates
   

2. *Buat file home.html* di dalam folder templates/:

   bash
   touch templates/home.html
   

3. *Buka file home.html* dengan *nano* untuk mengeditnya:

   bash
   nano templates/home.html
   

4. *Isi home.html* dengan HTML berikut:

   html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Welcome to FastAPI Web</title>
       <style>
           body {
               font-family: Arial, sans-serif;
               text-align: center;
               margin-top: 50px;
           }
           h1 {
               color: #3498db;
           }
           p {
               font-size: 18px;
           }
       </style>
   </head>
   <body>
       <h1>Welcome to FastAPI Web!</h1>
       <p>This is a simple web app served by FastAPI.</p>
       <a href="/about">Go to About Page</a>
   </body>
   </html>
   

5. *Simpan dan keluar* dari *nano*:
   - Tekan Ctrl + O untuk menyimpan file.
   - Tekan Enter untuk mengonfirmasi nama file.
   - Tekan Ctrl + X untuk keluar dari *nano*.

   Gambar file home.html setelah selesai diubah:

   ![Home Page Template](screenshot/home_page_template.png)

6. *Buat file about.html* untuk halaman "About" di dalam folder templates/:

   bash
   touch templates/about.html


   

7. **Buka file about.html** dengan *nano* untuk mengeditnya:

   bash
   nano templates/about.html
   

8. **Isi about.html** dengan HTML berikut:

   html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>About - FastAPI Web</title>
       <style>
           body {
               font-family: Arial, sans-serif;
               text-align: center;
               margin-top: 50px;
           }
           h1 {
               color: #e74c3c;
           }
           p {
               font-size: 18px;
           }
       </style>
   </head>
   <body>
       <h1>About This FastAPI Web App</h1>
       <p>This web app is created using FastAPI and serves dynamic HTML pages with Jinja2 templates.</p>
       <a href="/">Go to Home Page</a>
   </body>
   </html>
   

9. *Simpan dan keluar* dari *nano*.

   Gambar file about.html setelah selesai diubah:

   ![About Page Template](screenshot/about_page_template.png)

Dengan langkah ini, Anda telah berhasil menyiapkan folder templates/ dan membuat file template HTML untuk halaman utama dan halaman about. Anda sekarang siap untuk menjalankan aplikasi FastAPI!

---

