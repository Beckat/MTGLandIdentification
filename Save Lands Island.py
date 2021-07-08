from bs4 import BeautifulSoup
import requests
import re
import urllib.request

land_urls = []

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

url = "https://www.mtgpics.com/art?gamerid=abu130&pointeur=0"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')

data = soup.find_all("div")
for div in data:
    if "pics/" in str(div):
        land_url = re.search("url((.*));", str(div))
        land_urls.append("https://www.mtgpics.com/" + str(land_url.group(1))[1:-1])

url = "https://www.mtgpics.com/art?gamerid=abu130&pointeur=60"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')

data = soup.find_all("div")
for div in data:
    if "pics/" in str(div):
        land_url = re.search("url((.*));", str(div))
        land_urls.append("https://www.mtgpics.com/" + str(land_url.group(1))[1:-1])

url = "https://www.mtgpics.com/art?gamerid=abu130&pointeur=120"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')

data = soup.find_all("div")
for div in data:
    if "pics/" in str(div):
        land_url = re.search("url((.*));", str(div))
        land_urls.append("https://www.mtgpics.com/" + str(land_url.group(1))[1:-1])

url = "https://www.mtgpics.com/art?gamerid=abu130&pointeur=180"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')

data = soup.find_all("div")
for div in data:
    if "pics/" in str(div):
        land_url = re.search("url((.*));", str(div))
        land_urls.append("https://www.mtgpics.com/" + str(land_url.group(1))[1:-1])


len(land_urls)

for i in range(len(land_urls)):
    urllib.request.urlretrieve(land_urls[i], "/ssd_data/MTG Land/Island/island_" + str(i) + ".jpg")