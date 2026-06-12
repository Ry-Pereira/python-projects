# Name: Ryan Pereira
# Project Name: Where Am I Locator Project
# Description: A program that uses an IP address API to determine a user's approximate geographic location and display information such as location, time zone, coordinates, and ISP details.
# Module Name: main.py
# Module Purpose:
# Collaborators: None
# Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
# Date: 6/10/2026
# Last Modified: 6/11/2026



# Creates a dictionary containing an HTTP User-Agent header.
# This makes the request appear to come from a web browser.
headers = {"User-Agent": "Mozilla/5.0"}
# Imports the BeautifulSoup class from the bs4 module
# for parsing and navigating HTML documents.
from bs4 import BeautifulSoup
# Imports all functions and classes from the requests module.
from requests import *
# Imports the requests module for making HTTP requests.
import requests
# Imports the sys module for interacting with the Python interpreter.
import sys
# Imports the datetime and timezone classes from the datetime module.
from datetime import datetime, timezone
# Configures standard output to use UTF-8 encoding.
sys.stdout.reconfigure(encoding="utf-8")



# Retrieves the user's public IP address from ipchicken.com.
def get_ip_address():
    # Stores the URL of the website that displays the user's public IP address.
    url = "https://ipchicken.com/"
    # Sends an HTTP GET request to the website using the custom headers.
    response = requests.get(url, headers=headers)
    # Parses the HTML content returned by the website.
    soup = BeautifulSoup(response.text, 'html.parser')
    # Finds the span element with the id "public-ip"
    # and returns the text containing the public IP address.
    return soup.find("span", id="public-ip").text



# Retrieves location and network information for a given IP address.
def get_additional_information_from_location(ip):
    # Creates the API URL using the supplied IP address.
    url = f"http://ip-api.com/json/{ip}"
    # Sends an HTTP GET request to the IP location API.
    response = requests.get(url, headers=headers)
    # Returns the JSON response as a Python dictionary.
    return response.json()


