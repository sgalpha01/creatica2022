from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from download import get_image_list

app = FastAPI()
app.add_middleware(CORSMiddleware)
#retrieves/downloads images from a website
get_image_list("https://www.geeksforgeeks.org/")

@app.post("/api/url")
async def scan_url(url: str):
    return url
