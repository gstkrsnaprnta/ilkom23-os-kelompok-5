# Dokumentasi Daemon Process untuk Hello Web

## 1. Deskripsi Program

Program ini menggunakan Python untuk membuat **web server sederhana**. Ketika diakses melalui browser, server akan menampilkan pesan **"Hello Web!"**. Program akan dijalankan sebagai **daemon process** di Windows menggunakan **Task Scheduler** agar dapat berjalan otomatis di latar belakang.

---

## 2. Kode Program Web Server

Buat file bernama **`hello_web.py`** dengan kode berikut:

```python
from http.server import SimpleHTTPRequestHandler, HTTPServer

class HelloHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<html><body><h1>Hello Web!</h1></body></html>")

def run():
    server_address = ("", 8080)
    httpd = HTTPServer(server_address, HelloHandler)
    print("Starting server on http://localhost:8080...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
