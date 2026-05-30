#Name: Ryan Pereira
#Project Name: Moon Phase Tracker Project
#Description: A program that scrapes moon phase data from a website and displays it to the user in a user-friendly way. The program allows the user to view the current moon phase, the moon phases for the current week, the moon phases for the next week, and the moon phase for a specific date. The program also includes ASCII art representations of each moon phase.
#Collaborators: None
#Module Name: moon_phase_requests.py
#Module Purpose: This module contains functions for retrieving moon phase data from a website.
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 5/28/2026
#Last Modified: 5/30/2026




#From the requests library, import everything. This is used to make HTTP requests to the website to retrieve moon phase data.
from requests import requests
#From the datetime library, import the datetime class. This is used to work with dates and times in the program.
from datetime import datetime
#From the bs4 library, import the BeautifulSoup class. This is used to parse the HTML of the website and extract the moon phase data.
from bs4 import BeautifulSoup
#Imported the sys library and reconfigure the standard output to use UTF-8 encoding. This is necessary to ensure that the ASCII art and other text in the program is displayed correctly, especially if it contains special characters.
import sys
#Reconfigure the standard output to use UTF-8 encoding to ensure that ASCII art and other text is displayed correctly.
sys.stdout.reconfigure(encoding="utf-8")



#Defining a get_moon_phase function that takes a date as an argument and returns a dictionary containing moon phase information for that date. The function makes an HTTP request to the moongiant.com website, parses the HTML to extract the moon phase data, and returns it in a structured format.
def get_moon_phase(date):
    #Date year is extracted from the date argument and stored in date_year variable. The strftime method is used to format the date as a string in the desired format.
    date_year = date.strftime("%Y")
    #Date month is extracted from the date argument and stored in date_month variable. The strftime method is used to format the date as a string in the desired format.
    date_month = date.strftime("%m")
    #Date day is extracted from the date argument and stored in date_day variable. The strftime method is used to format the date as a string in the desired format.
    date_day = date.strftime("%d")



    #Moon info dictionary is initialized with keys for different moon phase information and values set to None. This dictionary will be populated with the actual moon phase data retrieved from the website.
    moon_info_dictionary = {"moon_phase": None, "illumination": None, "moon_age": None, "moon_angle": None, "moon_distance": None, "moon_sun_angle": None, "moon_sun_distance": None}
    #The URL for the moongiant.com website is constructed using the date information. The URL is formatted to include the year, month, and day in the appropriate format for the website's URL structure.
    url = f"https://www.moongiant.com/phase/{date_month}/{date_day}/{date_year}/"
    #A User-Agent header is included in the HTTP request to mimic a web browser and avoid potential blocking by the website. The requests.get function is used to make the HTTP request to the specified URL with the headers.
    headers = {"User-Agent": "Mozilla/5.0"}
    #The response from the HTTP request is stored in the response variable. The BeautifulSoup class is used to parse the HTML content of the response, allowing for easy extraction of the moon phase data from the website's HTML structure.
    response = requests.get(url, headers=headers)
    #The BeautifulSoup object is created by parsing the HTML content of the response. This allows for easy navigation and extraction of specific elements from the HTML, such as the moon phase information contained within specific tags and classes on the webpage.
    soup = BeautifulSoup(response.text,'html.parser')    
    #The moon phase information is extracted from the parsed HTML using BeautifulSoup's find and find_all methods. The specific HTML structure of the moongiant.com website is used to locate the relevant data, which is then stored in the moon_info_dictionary with appropriate keys for each piece of information.
    moon_phase_info = soup.find("div",id="moonDetails").find_all("span")



    #Moon_infoc_dictionary at the moon phase key is updated with the moon phase information extracted from the HTML. The get_text method is used to extract the text content from the relevant HTML elements, and the replace method is used to remove any newline characters for cleaner formatting. This process is repeated for each piece of moon phase information, populating the moon_info_dictionary with all the relevant data retrieved from the website.
    moon_info_dictionary["moon_phase"] = moon_phase_info[0].get_text().replace("\n", "")
    #The moon phase info dictionary at the illuminatio key is updated with the illumination information extracted from the HTML. The get_text method is used to extract the text content from the relevant HTML element, and the replace method is used to remove any newline characters for cleaner formatting.
    moon_info_dictionary["illumination"] = moon_phase_info[1].get_text().replace("\n", "")
    #The moon phase info dictionary at the moon age key is updated with the moon age information extracted from the HTML. The get_text method is used to extract the text content from the relevant HTML element, and the replace method is used to remove any newline characters for cleaner formatting.
    moon_info_dictionary["moon_age"] = moon_phase_info[2].get_text().replace("\n", "")
    #The moon phase info dictionary at the moon angle key is updated with the moon angle information extracted from the HTML. The get_text method is used to extract the text content from the relevant HTML element, and the replace method is used to remove any newline characters for cleaner formatting.
    moon_info_dictionary["moon_angle"] = moon_phase_info[3].get_text().replace("\n", "")
    #The moon phase info dictionary at the moon distance key is updated with the moon distance information extracted from the HTML. The get_text method is used to extract the text content from the relevant HTML element, and the replace method is used to remove any newline characters for cleaner formatting.
    moon_info_dictionary["moon_distance"] = moon_phase_info[4].get_text().replace("\n", "")
    #The moon phase info dictionary at the moon sun angle key is updated with the moon sun angle information extracted from the HTML. The get_text method is used to extract the text content from the relevant HTML element, and the replace method is used to remove any newline characters for cleaner formatting.
    moon_info_dictionary["moon_sun_angle"] = moon_phase_info[5].get_text().replace("\n", "")
    #The moon phase info dictionary at the moon sun distance key is updated with the moon sun distance information extracted from the HTML. The get_text method is used to extract the text content from the relevant HTML element, and the replace method is used to remove any newline characters for cleaner formatting.
    moon_info_dictionary["moon_sun_distance"] = moon_phase_info[6].get_text().replace("\n", "")


    #Return the moon_info_dictionary containing all the extracted moon phase information. This dictionary can then be used by other parts of the program to display the moon phase data to the user in a user-friendly way, including the ASCII art representations of each moon phase.
    return moon_info_dictionary


