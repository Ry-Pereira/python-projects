# Name: Ryan Pereira
# Project Name: Background Color Changer
# Description: A helper module that retrieves color hex codes from an external CSS colors API based on a given color name.
# Module Name: colordata.py
# Module Purpose: This module contains a function that requests color data from an API and returns the corresponding hex value for a given color name.
# Collaborators: None
# Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
# Date: 4/19/2026
# Last Modified: 4/21/2026


# Import the requests library for making HTTP requests
import requests


# Function that returns the hex code for a given color name
def get_color_hex(color_name):
    # API endpoint that provides CSS color data
    url = "https://csscolorsapi.com/api/colors"
    # Header to mimic a browser request
    headers = {"User-Agent": "Mozilla/5.0"}
    # Send GET request to API
    response = requests.get(url, headers=headers)
    # Convert response JSON into Python dictionary and extract color list
    color_data = response.json()["colors"]
    # Loop through each color in the dataset
    for color in color_data:
        # Check if the color name matches the input (capitalized)
        if color["name"] == color_name.capitalize():
            # Return formatted hex color code
            return f'#{color["hex"]}'
    # Return message if color is not found
    return "No Color of Description"


