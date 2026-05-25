# Name: Ryan Pereira
# Project Name: Generate Dog Image Through Domain
# Description: A Flask web application that retrieves and displays random dog images by breed and sub-breed using external helper functions from the dog_data module.
# Module Name: generate_dog_image_through_domain.py
# Module Purpose: This module defines a Flask server with routes that return random dog images, breed-specific images, and sub-breed images using helper functions from dog_data.py.
# Collaborators: None
# Sources: GitHub Copilot, Stack Overflow, ChatGPT, Python documentation
# Date: 4/22/2026
# Last Modified: 4/25/2026






# Import the Flask class and render_template function from the flask module
from flask import Flask, render_template

# Import all functions and variables from the dog_data module
from dog_data import *


# Create a Flask application instance
app = Flask(__name__)


# Create a Flask application instance again (this is redundant and overwrites the previous one)
app = Flask(__name__)


# Define a route for the home page ("/")
@app.route("/")
def home():
    # Define instructions to display on the homepage
    instructions = "Use /Dog/Random for a random dog image, /Dog/<breed>/Random for a specific breed, or /Dog/<breed>/<sub_breed>/Random for a sub-breed."
    # Render the index.html template with default values
    return render_template("index.html", dog_breed="Please specify dog breed", instructions=instructions, image_description=" ")


# Define a route to get a random dog image
@app.route("/Dog/Random")
def random_dog_picture():
    # Get a random dog image URL
    image_url = get_dog_image("Random")
    # Split the URL into parts using "/" as a separator
    url_parts = image_url.split("/")
    # Extract the breed name from the URL
    breed_name = url_parts[url_parts.index("breeds") + 1]
    # Render the template with the breed name and image
    return render_template("index.html", dog_breed=breed_name, dog_image=image_url, instructions="", image_description=f"Image of a {breed_name} dog")


# Define a route to get a random image for a specific breed
@app.route("/Dog/<breed>/Random")
def random_breed_dog_picture(breed):
    # Get a list of all dog breeds
    all_breeds = get_all_dog_breeds()
    # Check if the requested breed exists
    if breed in all_breeds:
        # Get a random image for the specified breed
        image_url = get_dog_breed_image(breed)
        # Split the URL into parts
        url_parts = image_url.split("/")
        # Extract the breed name from the URL
        breed_name = url_parts[url_parts.index("breeds") + 1]
        # Render the template with breed-specific image
        return render_template("index.html", dog_breed=breed_name, dog_image=image_url, image_description=f"Image of a {breed_name} dog")
    else:
        # Render template with error message if breed not found
        return render_template("index.html", dog_breed="Dog Breed Not found", dog_image=" ", instructions="", image_description=" ")


# Define a route to get a random image for a specific sub-breed
@app.route("/Dog/<breed>/<sub_breed>/Random")
def random_sub_breed_dog_picture(breed, sub_breed):
    # Get all available dog breeds
    all_breeds = get_all_dog_breeds()
    # Check if the breed exists
    if breed in all_breeds:
        # Get all sub-breeds for the given breed
        all_sub_breeds = get_all_dog_sub_breeds(breed)
        # Check if the sub-breed exists
        if sub_breed in all_sub_breeds:
            # Get a random image for the sub-breed
            image_url = get_dog_sub_breed(breed, sub_breed)
            # Split the URL into parts
            url_parts = image_url.split("/")
            # Extract the breed name from the URL
            breed_name = url_parts[url_parts.index("breeds") + 1]
            # Render template with sub-breed image
            return render_template("index.html", dog_breed=breed_name, dog_image=image_url, image_description=f"Image of a {breed_name} dog")
        else:
            # Render template if sub-breed is not found
            return render_template("index.html", dog_breed="Dog Breed but Sub-Breed Not found", dog_image=" ", instructions="", image_description=" ")
    else:
        # Render template if breed is not found
        return render_template("index.html", dog_breed="Dog Breed Not found", dog_image=" ", instructions="", image_description=" ")


# Run the Flask app only if this file is executed directly
if __name__ == "__main__":
    # Start the Flask development server
    app.run()