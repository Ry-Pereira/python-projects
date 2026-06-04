#Name: Ryan Pereira
#Project Name: Zodiac Sign Explorer Project
#Description: A program that scrapes zodiac sign data from a website and displays it to the user in a user-friendly way. The program allows the user to view information about different zodiac signs, including their birthday ranges, personality traits, and compatibility.
#Collaborators: None
#Module Name: zodiac_sign_requests.py
#Module Purpose: This program serves as the backend for the Zodiac Sign Explorer application. It defines functions to scrape zodiac sign data from a website. The functions include getting a list of all zodiac signs, getting the birthday ranges for each zodiac sign, getting the details for a specific zodiac sign, and getting the compatibility for a specific zodiac sign.
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 6/1/2026
#Last Modified: 6/4/2026






from datetime import datetime

from bs4 import BeautifulSoup
from requests import *
import requests
import sys

from datetime import datetime
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
        start_date, end_date = birthday_range.text.strip().split(" - ")
        start = datetime.strptime(start_date, "%B %d").strftime("%m:%d")
        end = datetime.strptime(end_date, "%B %d").strftime("%m:%d")
        zodiac_sign_to_birthday_ranges[sign.text.strip()] = (start, end)

    return zodiac_sign_to_birthday_ranges




def get_zodiac_sign_details(zodiac_sign):
    zodiac_sign_details = {}
    zodiac_sign_personality_dictionary = {}
    url = f"https://www.zodiacsign.com/zodiac-signs/{zodiac_sign.lower()}/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    t = soup.find_all("p")
    for r in t:
        if r.text.strip().split(":")[0] == "Strengths" or r.text.strip().split(":")[0] == "Weaknesses" or r.text.strip().split(":")[0] == f"{zodiac_sign} Likes" or r.text.strip().split(":")[0] == f"{zodiac_sign} Dislikes":
            zodiac_sign_personality_dictionary[r.text.strip().split(":")[0]] = r.text.strip().split(":")[1].strip()
        if r.text.strip().split(":")[0] != "Greatest Compatibility":
            zodiac_sign_details[r.text.strip().split(":")[0]] = r.text.strip().split(":")[1].strip()

    
    
    return zodiac_sign_details
  




def get_zodiac_sign_compatibility(zodiac_sign):
    url = f"https://www.zodiacsign.com/zodiac-signs/{zodiac_sign.lower()}/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    t =soup.find_all("p")
    for r in t:
        if "Greatest Compatibility" in r.text:
            zodiac_sign_compatibility = r.text.strip().split(":")[1].strip().split(",")
    return zodiac_sign_compatibility



print(get_zodiac_sign_details("Leo"))