# Name: Ryan Pereira
# Project Name: Background Color Changer
# Description: A helper module that interacts with the Dog CEO API to retrieve random dog images, breed-specific images, sub-breed images, and lists of available breeds.
# Module Name: colordata.py
# Module Purpose: This module provides functions that request data from the Dog CEO API, including random dog images, breed-specific images, sub-breed images, and available breed/sub-breed lists.
# Collaborators: None
# Sources: GitHub Copilot, Stack Overflow, ChatGPT, Python documentation
# Date: 4/22/2026
# Last Modified: 4/25/2026





# Import the requests library to make HTTP requests to external APIs
import requests


# Function to get a random dog image (currently ignores dog_breed parameter)
def get_dog_image(dog_breed):
    # API endpoint that provides a random dog image
    api_url = "https://dog.ceo/api/breeds/image/random"
    # Header to mimic a real browser request (helps avoid blocking)
    request_headers = {"User-Agent": "Mozilla/5.0"}
    # Send a GET request to the API with headers
    api_response = requests.get(api_url, headers=request_headers)
    # Extract the image URL from the JSON response
    image_url = api_response.json()["message"]
    # Return the image URL
    return image_url
    

# Function to get a random image for a specific dog breed
def get_dog_breed_image(dog_breed):
    # API endpoint for a random image of a specific breed
    api_url = f"https://dog.ceo/api/breed/{dog_breed}/images/random"
    # Header to mimic a browser request
    request_headers = {"User-Agent": "Mozilla/5.0"}
    # Send GET request to API
    api_response = requests.get(api_url, headers=request_headers)
    # Extract image URL from response
    image_url = api_response.json()["message"]
    # Return the image URL
    return image_url


# Function to get a random image for a specific sub-breed
def get_dog_sub_breed(dog_breed, dog_sub_breed):
    # API endpoint for a sub-breed image
    api_url = f"https://dog.ceo/api/breed/{dog_breed}/{dog_sub_breed}/images/random"
    # Header to mimic browser request
    request_headers = {"User-Agent": "Mozilla/5.0"}
    # Send request to API
    api_response = requests.get(api_url, headers=request_headers)
    # Extract image URL from response
    image_url = api_response.json()["message"]
    # Return image URL
    return image_url


# Function to get a list of all dog breeds
def get_all_dog_breeds():
    # API endpoint that returns all dog breeds
    api_url = "https://dog.ceo/api/breeds/list/all"
    # Header to mimic browser request
    request_headers = {"User-Agent": "Mozilla/5.0"}
    # Send request to API
    api_response = requests.get(api_url, headers=request_headers)
    # Extract dictionary of breeds from response
    breeds_dict = api_response.json()["message"]
    # Return dictionary of breeds
    return breeds_dict
    

# Function to get all sub-breeds for a specific breed
def get_all_dog_sub_breeds(dog_breed):
    # API endpoint for sub-breeds of a specific breed
    api_url = f"https://dog.ceo/api/breed/{dog_breed}/list"
    # Header to mimic browser request
    request_headers = {"User-Agent": "Mozilla/5.0"}
    # Send request to API
    api_response = requests.get(api_url, headers=request_headers)
    # Extract list of sub-breeds from response
    sub_breeds_dict = api_response.json()["message"]
    # Return list of sub-breeds
    return sub_breeds_dict





    











