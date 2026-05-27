







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