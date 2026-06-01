

from requests import *
import requests
import sys
sys.stdout.reconfigure(encoding="utf-8")






def get_zodiac_sign_infor(sign):
    url = "https://www.zodiacsign.com/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text,'html.parser')

