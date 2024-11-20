from bs4 import BeautifulSoup
import requests


res = requests.get("https://sustainability.atmeta.com/map/")
scripts = BeautifulSoup(res.text).find_all("script")
for result in scripts:
    if "var markers" not in str(result):
        continue
    print(result.text.strip().split("var markers = ")[1])
