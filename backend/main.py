import uvicorn
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from image_downloader import get_image_list
from nsfw_detector import get_score
from model import NSFW_score

app = FastAPI()
app.add_middleware(CORSMiddleware)
templates = Jinja2Templates(directory="../frontend/templates")
app.mount("/static", StaticFiles(directory="../frontend/static"), name="static")


# Landing Page
@app.get("/", response_class=HTMLResponse)
async def hello_world(request: Request):
    return templates.TemplateResponse("Custom.html", {"request": request})


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


@app.post("/api/url/")
def scan_url(url: str):
    # retrieves/downloads images from a website
    get_image_list(url)
    response = get_score(url)
    if response:
        return response
    raise HTTPException(400, "Something Went Wrong!")


if __name__ == "__main__":
    uvicorn.run(app)
