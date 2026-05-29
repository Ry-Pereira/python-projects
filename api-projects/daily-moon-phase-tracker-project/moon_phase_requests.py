import sys
sys.stdout.reconfigure(encoding="utf-8")

from requests import *
import requests
from datetime import datetime

from bs4 import BeautifulSoup


def get_moon_phase():
    moon_info = {"moon_phase": None, "illumination": None, "moon_age": None, "moon_angle": None, "moon_distance": None, "moon_sun_angle": None, "moon_sun_distance": None}
    url = "https://www.moongiant.com/phase/05/30/2026/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text,'html.parser')

    

    moon_phase_info = soup.find("div",id="moonDetails").find_all("span")




    moon_info["moon_phase"] = moon_phase_info[0].get_text().replace("\n", "")
    moon_info["illumination"] = moon_phase_info[1].get_text().replace("\n", "")
    moon_info["moon_age"] = moon_phase_info[2].get_text().replace("\n", "")
    moon_info["moon_angle"] = moon_phase_info[3].get_text().replace("\n", "")
    moon_info["moon_distance"] = moon_phase_info[4].get_text().replace("\n", "")
    moon_info["moon_sun_angle"] = moon_phase_info[5].get_text().replace("\n", "")
    moon_info["moon_sun_distance"] = moon_phase_info[6].get_text().replace("\n", "")


    return moon_info


if __name__ == "__main__":
    print("Testing moon phase retrieval...")
    moon_info = get_moon_phase()
    print(moon_info)