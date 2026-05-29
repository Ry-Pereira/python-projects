import sys
sys.stdout.reconfigure(encoding="utf-8")

from requests import *
import requests
from datetime import datetime

from bs4 import BeautifulSoup


def get_moon_phase():
    url = "https://www.moongiant.com/phase/today/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text,'html.parser')
    return soup.find("h2", attrs={"id": "signH2"})



print(get_moon_phase())
