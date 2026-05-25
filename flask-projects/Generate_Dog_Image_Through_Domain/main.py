# Name: Ryan Pereira
# Project Name: Background Color Changer
# Description: An entry-point module that imports a Flask application from the server module and runs the web server.
# Module Name: colordata.py
# Module Purpose: This module serves as the application launcher, starting the Flask development server defined in the server module.
# Collaborators: None
# Sources: GitHub Copilot, Stack Overflow, ChatGPT, Python documentation
# Date: 4/22/2026
# Last Modified: 4/25/2026





# Import the 'app' object from the 'server' module
from server import app


# Define the main function that will start the application
def main():
    # Assign the imported Flask app instance to a local variable
    flask_app_instance = app
    # Run the Flask application (starts the development server)
    flask_app_instance.run()


# Check if this script is being run directly (not imported as a module)
if __name__ == "__main__":
    # Call the main function to start the app
    main()