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
