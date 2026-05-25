# Name: Ryan Pereira
# Project Name: Background Color Changer
# Description: A Flask web application that changes the background color of a webpage based on the color name provided in the URL.
# Module Name: server
# Module Purpose: This module serves as the backend server for the Background Color Changer application. It defines Flask routes that render an HTML page and dynamically change the background color based on user input from the URL.
# Collaborators: None
# Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
# Date: 4/19/2026
# Last Modified: 4/21/2026


# Import Flask framework and template rendering function
from flask import Flask, render_template
# Import function that converts a color name into a hex value
from colordata import get_color_hex


# Create Flask application instance
app = Flask(__name__)


# Define route for homepage "/"
@app.route("/")
# Function executed when user visits "/"
def home():
    # Render index.html and pass instructions to the template
    return render_template(
        "index.html",
        instruction="Instruction:In domain put /color/ and after the backlsach put specifc color\nExample:/color/Red"
    )




# Define dynamic route that accepts a color name in the URL
@app.route("/color/<color>")
# Function executed when user visits /color/<color>
def color_page(color):
    # Get hex value for the provided color name
    color_hex = get_color_hex(color)
    # Check if the color was not found in dataset
    if color_hex == "No Color of Description":
        # Render page with error message and default white background
        return render_template(
            "index.html",
            instruction=" ",
            color_name="Color Not Found",
            background_color="#ffffff"
        )

    # If color is found in dataset
    else:
        # Render page with selected color
        return render_template(
            "index.html",
            instruction=" ",
            color_name=f"{color}",
            background_color=color  # NOTE: likely should be color_hex instead
        )


# Run the Flask app only if this file is executed directly
if __name__ == "__main__":
    # Start Flask development server
    app.run()