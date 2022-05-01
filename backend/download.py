import requests 
from bs4 import BeautifulSoup 
import urllib.request

    
def getdata(url): 
    r = requests.get(url) 
    return r.text 
    
def get_image_list(url):
    htmldata = getdata(url) 
    soup = BeautifulSoup(htmldata, 'html.parser') 
    urls = []
    for item in soup.find_all('img'):
        urls.append(item['src'])
    download_images_function(urls)

def download_image(url, file_path, file_name):
        full_path = file_path + file_name + '.png'
        urllib.request.urlretrieve(url, full_path)

def download_images_function(urls):
    for url in urls:
        file_name = str(id(url))
        download_image(url, '../backend/temp_images/', file_name)