# Name: Ryan Pereira
# Project Name: Higher or Lower Number Guessing Web App
# Description: A Flask-based web application where users guess a randomly generated number by changing the URL route.
# Module Name: Main
# Module Purpose: This program serves as the entry point for the Higher or Lower Number Guessing Web App. It generates a random number and starts the Flask server so users can guess the number through browser routes.
# Collaborators: None
# Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
# Date: 4/28/2026
# Last Modified: 4/28/2026



# Imports the built-in random module for generating random numbers
import random

# Imports the server file so we can access the Flask app and variables
import server


# Main function that starts the program
def main():

    # Generates a random number between 0 and 9
    # and stores it in the server.py variable called random_number
    server.random_number = random.randint(0,9)

    # Starts the Flask web server
    server.app.run()


# Checks if this file is being run directly
if __name__ == "__main__":

    # Calls the main function to start the program
    main()
