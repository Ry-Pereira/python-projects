#Name: Ryan Pereira
#Project Name: Zodiac Sign Explorer Project
#Description: A program that scrapes zodiac sign data from a website and displays it to the user in a user-friendly way. The program allows the user to view information about different zodiac signs, including their birthday ranges, personality traits, and compatibility.
#Collaborators: None
#Module Name: zodiac_sign_requests.py
#Module Purpose: This program serves as the backend for the Zodiac Sign Explorer application. It defines functions to scrape zodiac sign data from a website. The functions include getting a list of all zodiac signs, getting the birthday ranges for each zodiac sign, getting the details for a specific zodiac sign, and getting the compatibility for a specific zodiac sign.
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 6/1/2026
#Last Modified: 6/4/2026




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
from datetime import datetime
sys.stdout.reconfigure(encoding="utf-8")






# Retrieves all zodiac sign links from the homepage.
def get_all_zodiac_signs():
    # Stores the URL of the zodiac sign homepage.
    url = "https://www.zodiacsign.com/"
    # Sends an HTTP GET request to the website.
    response = requests.get(url, headers=headers)
    # Parses the HTML content of the webpage.
    soup = BeautifulSoup(response.text, 'html.parser')
    # Returns all zodiac sign link elements.
    return soup.find_all("a", class_="tittle portfolio-2")





# Retrieves the birthday range for each zodiac sign.
def get_zodiac_sign_birthday_ranges():
    # Stores zodiac signs and their birthday ranges.
    zodiac_sign_to_birthday_ranges = {}
    # Stores the URL of the zodiac sign homepage.
    url = "https://www.zodiacsign.com/"
    # Sends an HTTP GET request to the website.
    response = requests.get(url, headers=headers)
    # Parses the HTML content of the webpage.
    soup = BeautifulSoup(response.text, 'html.parser')
    # Finds all zodiac sign elements.
    signs = soup.find_all("a", class_="tittle portfolio-2")
    # Finds all birthday range elements.
    birthday_ranges = soup.find_all("div", class_="category _2")
    # Pairs each zodiac sign with its birthday range.
    for sign, birthday_range in zip(signs, birthday_ranges):
        # Splits the birthday range into start and end dates.
        start_date, end_date = birthday_range.text.strip().split(" - ")
        # Stores the birthday range for the zodiac sign.
        zodiac_sign_to_birthday_ranges[sign.text.strip()] = [start_date.split(" "),end_date.split(" ")]
    # Returns the zodiac sign birthday ranges dictionary.
    return zodiac_sign_to_birthday_ranges




# Retrieves detailed information about a zodiac sign.
def get_zodiac_sign_details(zodiac_sign):
    # Stores general zodiac sign details.
    zodiac_sign_general_details = {}
    # Stores zodiac sign personality traits.
    zodiac_sign_personal_traits = {}
    # Stores all zodiac sign details.
    zodiac_sign_details = {"general_details": zodiac_sign_general_details,"personal_traits": zodiac_sign_personal_traits}
    # Creates the zodiac sign page URL.
    url = f"https://www.zodiacsign.com/zodiac-signs/{zodiac_sign.lower()}/"
    # Sends an HTTP GET request to the zodiac sign page.
    response = requests.get(url, headers=headers)
    # Parses the HTML content of the webpage.
    soup = BeautifulSoup(response.text, 'html.parser')
    # Finds all paragraph elements on the page.
    paragraphs = soup.find_all("p")
    # Loops through each paragraph.
    for paragraph in paragraphs:
        # Stops processing when the author section is reached.
        if paragraph.text.split(":")[0] == "By":
            break
        # Stores personality trait information.
        elif (paragraph.text.split(":")[0] == "Strengths" or paragraph.text.split(":")[0] == "Weaknesses" or paragraph.text.split(":")[0] == f"{zodiac_sign} likes" or paragraph.text.split(":")[0] == f"{zodiac_sign} dislikes"):
            zodiac_sign_details["personal_traits"][paragraph.text.split(":")[0]] = paragraph.text.split(":")[1]
        # Stores general zodiac sign information.
        elif paragraph.text.split(":")[0] != "Greatest Compatibility":
            zodiac_sign_details["general_details"][paragraph.text.split(":")[0]] = paragraph.text.split(":")[1]
    # Returns all zodiac sign details.
    return zodiac_sign_details




# Retrieves compatible zodiac signs for a zodiac sign.
def get_zodiac_sign_compatibility(zodiac_sign):
    # Creates the zodiac sign page URL.
    url = f"https://www.zodiacsign.com/zodiac-signs/{zodiac_sign.lower()}/"
    # Sends an HTTP GET request to the zodiac sign page.
    response = requests.get(url, headers=headers)
    # Parses the HTML content of the webpage.
    soup = BeautifulSoup(response.text, 'html.parser')
    # Finds all paragraph elements on the page.
    paragraphs = soup.find_all("p")
    # Loops through each paragraph.
    for paragraph in paragraphs:
        # Finds the compatibility information paragraph.
        if "Greatest Compatibility" in paragraph.text:
            # Extracts compatible zodiac signs into a list.
            zodiac_sign_compatibility = paragraph.text.strip().split(":")[1].strip().split(",")
    # Returns the list of compatible zodiac signs.
    return zodiac_sign_compatibility


