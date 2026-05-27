# Name: Ryan Pereira
# Project Name: Background Color Changer
# Description: A Flask web application that changes the background color of a webpage based on the color name inputted in the form request.
# Module Name: server.py
# Module Purpose: This module serves as the backend server for the Background Color Changer application. It defines Flask routes that render an HTML page and dynamically change the background color based on user input from the URL.
# Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation, previous project code reuse.
# Date: 5/27/2026
# Last Modified: 5/27/2026



# Import Flask tools and the custom color conversion function
from flask import Flask, render_template, request
from color_data import get_color_hex


# Create the Flask application instance
app = Flask(__name__)


# Create the home route that accepts GET and POST requests
@app.route("/", methods=["GET", "POST"])
def home():
    # Set the default background color
    background_color = "white"
    # Set the default instruction message
    instruction = (
        "Instruction: Enter a color name of your choosing, "
        "and hit the button to change the background color."
    )
    # Check if the form was submitted
    if request.method == "POST":
        # Get the color name from the form input
        color = request.form.get("color_name")
        # Convert the color name into a hex code
        color_hex = get_color_hex(color)
        # Check if the color exists
        if color_hex != "No Color of Description":
            # Update the background color
            background_color = color_hex
        # Handle invalid color names
        else:
            # Display an error instruction message
            instruction = "Instruction: Color not found, try again."
    # Render the HTML template with updated values
    return render_template(
        "index.html",
        instruction=instruction,
        background_color=background_color
    )


# Run the Flask app only when this file is executed directly
if __name__ == "__main__":
    # Start the Flask development server
    app.run()