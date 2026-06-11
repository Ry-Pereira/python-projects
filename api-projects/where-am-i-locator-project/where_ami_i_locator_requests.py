#Name: Ryan Pereira
#Project Name: Where Am I Locator Project
#Description: 
#Module Name: main.py
#Module Purpose: 
#Collaborators: None
#Sources:  Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 6/10/2026
#Last Modified: 6/11/2026




#Headers setting the user agent to Mozilla/5.0 .
headers = {"User-Agent": "Mozilla/5.0"}
#From bs4 module imporrting the BeautifulSoup class.
from bs4 import BeautifulSoup
#From requests module importing.
from requests import *
#Importing the requests module
import requests
#Importing the sys module.
import sys
#From datetime, importing the datetime module information
from datetime import datetime,timezone
sys.stdout.reconfigure(encoding="utf-8")



# Retrieves all zodiac sign links from the homepage.
def get_ip_address():
    # Stores the URL of the zodiac sign homepage.
    url = "https://ipchicken.com/"
    # Sends an HTTP GET request to the website.
    response = requests.get(url, headers=headers)
    # Parses the HTML content of the webpage.
    soup = BeautifulSoup(response.text, 'html.parser')
    # Returns all zodiac sign link elements.
    return soup.find("span",id="public-ip").text



# Retrieves all zodiac sign links from the homepage.
def get_additional_ip_location(ip):
    # Stores the URL of the zodiac sign homepage.
    url = f"http://ip-api.com/json/{ip}"
    # Sends an HTTP GET request to the website.
    response = requests.get(url, headers=headers)
    # Parses the HTML content of the webpage.

    # Returns all zodiac sign link elements.
    return response.json()





test = get_ip_address()
print(get_additional_ip_location(test))