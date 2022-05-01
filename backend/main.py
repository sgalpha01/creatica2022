from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(CORSMiddleware)


@app.post("/api/url")
async def scan_url(url: str):
    return url
