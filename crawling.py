import requests
from bs4 import BeautifulSoup

source = requests.get("https://www.naver.com/").text
soup = BeautifulSoup(source, "html.parser")
hotkeys = soup.select("strong.title")

for i, key in enumerate(hotkeys):
    print(i, key.text)
