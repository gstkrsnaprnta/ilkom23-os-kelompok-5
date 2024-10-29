# Tahapan Pembuatan Daemon Process untuk Aplikasi Flask di Windows

## 1. Persiapan Aplikasi Web Flask
   - Buat file `app.py` sebagai aplikasi web sederhana menggunakan Flask.
   - Kode contoh untuk aplikasi Flask:

     ```python
     from flask import Flask

     app = Flask(__name__)

     @app.route('/')
     def hello():
         return "Hello, Flask is running as a Windows Service!"

     if __name__ == "__main__":
         app.run()
     ```

## 2. Persiapan Service untuk Menjalankan Flask
   - Buat file `flask_service.py` untuk mengonversi aplikasi Flask menjadi Windows Service.

   - Kode contoh untuk `flask_service.py`:

     ```python
     import win32serviceutil
     import win32service
     import win32event
     import servicemanager
     from app import app
     import socket

     class FlaskService(win32serviceutil.ServiceFramework):
         _svc_name_ = "FlaskService"
         _svc_display_name_ = "Flask Web Service"
         _svc_description_ = "This service runs a Flask web app as a background service."

         def __init__(self, args):
             win32serviceutil.ServiceFramework.__init__(self, args)
             self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
             socket.setdefaulttimeout(60)

         def SvcStop(self):
             self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
             win32event.SetEvent(self.hWaitStop)

         def SvcDoRun(self):
             servicemanager.LogMsg(
                 servicemanager.EVENTLOG_INFORMATION_TYPE,
                 servicemanager.PYS_SERVICE_STARTED,
                 (self._svc_name_, "")
             )
             app.run(host="0.0.0.0", port=5000)  # Menjalankan aplikasi Flask

     if __name__ == '__main__':
         win32serviceutil.HandleCommandLine(FlaskService)
     ```

## 3. Instalasi dan Jalankan Service

### a. Instalasi Modul yang Diperlukan
   - Install modul `pywin32` untuk mendukung pembuatan service di Windows.
     ```bash
     pip install pywin32
     ```

### b. Instalasi Service
   - Buka Command Prompt sebagai Administrator.
   - Navigasikan ke direktori yang berisi file `flask_service.py`.
   - Instal service dengan menjalankan perintah berikut:
     ```cmd
     python flask_service.py install
     ```

### c. Memulai Service
   - Untuk memulai service, jalankan:
     ```cmd
     python flask_service.py start
     ```

### d. Verifikasi Service
   - Buka browser dan akses `http://localhost:5000` untuk memastikan bahwa aplikasi Flask berjalan sebagai service.

### e. Menghentikan Service
   - Jika ingin menghentikan service, jalankan perintah:
     ```cmd
     python flask_service.py stop
     ```

## 4. Bukti Screenshot
   - Berikut adalah bukti bahwa aplikasi berhasil berjalan di background sebagai service:

     ![Screenshot Aplikasi Berjalan](screenshots/screenshot_app_running.png)
