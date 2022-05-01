from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn
from download import get_image_list

app = FastAPI()
app.add_middleware(CORSMiddleware)
templates = Jinja2Templates(directory="../templates")
app.mount("/static", StaticFiles(directory="../static"), name="static")

# retrieves/downloads images from a website
def request_download_image(url):
    get_image_list(url)


# home
@app.get("/", response_class=HTMLResponse)
@app.get("/home", response_class=HTMLResponse)
async def hello_world(request: Request):
    return templates.TemplateResponse("Home.html", {"request": request})


# Website-1
@app.get("/website-1", response_class=HTMLResponse)
async def hello_world1(request: Request):
    return templates.TemplateResponse("website-1.html", {"request": request})


# Website-2
@app.get("/website-2", response_class=HTMLResponse)
async def hello_world2(request: Request):
    return templates.TemplateResponse("website-2.html", {"request": request})


# Website-3
@app.get("/website-3", response_class=HTMLResponse)
async def hello_world3(request: Request):
    return templates.TemplateResponse("website-3.html", {"request": request})


@app.post("/api/url")
async def scan_url(url: str):
    return url


if __name__ == "__main__":
    uvicorn.run(app)
