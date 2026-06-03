
from bs4 import BeautifulSoup
from requests import *
import requests
import sys
sys.stdout.reconfigure(encoding="utf-8")






def get_all_zodiac_signs():
    url = "https://www.zodiacsign.com/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text,'html.parser')
    return soup.find_all("a",class_="tittle portfolio-2")






def get_zodiac_sign_birthday_ranges():
    zodiac_sign_to_birthday_ranges = {}
    url = "https://www.zodiacsign.com/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    signs = soup.find_all("a", class_="tittle portfolio-2")
    birthday_ranges = soup.find_all("div", class_="category _2")

    zodiac_sign_to_birthday_ranges = {}

    for sign, birthday_range in zip(signs, birthday_ranges):
        zodiac_sign_to_birthday_ranges[sign.text.strip()] = birthday_range.text.strip()

   
    return zodiac_sign_to_birthday_ranges



def get_zodiac_sign_compatibility(zodiac_sign):
    url = f"https://www.zodiacsign.com/zodiac-signs/{zodiac_sign.lower()}/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    for p in soup.find_all("p"):
        b = p.find("b"):
        if b.text.strip() == "Compatible Signs {zodaic_sign} ":
            return p.text.strip().replace(f"Compatible Signs {zodiac_sign} is most compatible with:", "").strip()
