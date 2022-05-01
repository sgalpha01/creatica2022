import urllib.request
from pathlib import Path, PurePath
import os

import requests
from bs4 import BeautifulSoup

workdir = Path(__file__).resolve().parent
imgdir = PurePath.joinpath(workdir, ".image_cache")
Path(imgdir).mkdir(exist_ok=True)


def getdata(url):
    r = requests.get(url)
    return r.text


def get_image_list(url):
    htmldata = getdata(url)
    soup = BeautifulSoup(htmldata, "html.parser")
    urls = []
    for item in soup.find_all("img"):
        urls.append(item["src"])
    download_images_function(urls)


def download_image(url, file_path, file_name):
    full_path = os.path.join(file_path, (file_name + ".png"))
    urllib.request.urlretrieve(url, full_path)


def download_images_function(urls):
    for url in urls:
        file_name = str(id(url))
        download_image(url, str(imgdir), file_name)
