#Name: Ryan Pereira
#Project Name: Higher or Lower Number Guessing Web App
#Description: A Flask-based web application where users guess a randomly generated number between 1 and 9 by changing the URL. The app returns a response indicating whether the guess is correct or incorrect.
#Module Name: Server
#Module Purpose: This module defines the Flask web server and all URL routes for the number guessing game. It compares user-entered URL values against a randomly generated number stored at runtime and returns corresponding HTML responses.
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 4/28/2026
#Last Modified: 4/28/2026



# Imports the Flask class from the flask module
from flask import Flask
# Stores the randomly generated number (set later from main.py)
random_number = None
# Creates the Flask application instance
app = Flask(__name__)
# Home route (instructions page)




@app.route("/")
def home():
    # Returns instructions to the user
    return "<p> Change the url to have /number/1 to /number/9"


# Route for guessing number 1
@app.route("/number/1")
def one_page():
    # Checks if the random number equals 1
    if random_number == 1:
        return "<h1>CORRECT!!!1!</h1>"
    else:
        return "<h1>INCORRECT!!!1!</h1>"


# Route for guessing number 2
@app.route("/number/2")
def two_page():
    # Checks if the random number equals 2
    if random_number == 2:
        return "<h1>CORRECT!!!2!</h1>"
    else:
        return "<h1>INCORRECT!!!2!</h1>"


# Route for guessing number 3
@app.route("/number/3")
def three_page():
    # Checks if the random number equals 3
    if random_number == 3:
        return "<h1>CORRECT!!!3!</h1>"
    else:
        return "<h1>INCORRECT!!!3!</h1>"


# Route for guessing number 4
@app.route("/number/4")
def four_page():
    # Checks if the random number equals 4
    if random_number == 4:
        return "<h1>CORRECT!!!4!</h1>"
    else:
        return "<h1>INCORRECT!!!4!</h1>"


# Route for guessing number 5
@app.route("/number/5")
def five_page():
    # Checks if the random number equals 5
    if random_number == 5:
        return "<h1>CORRECT!!!5!</h1>"
    else:
        return "<h1>INCORRECT!!!5!</h1>"


# Route for guessing number 6
@app.route("/number/6")
def six_page():
    # Checks if the random number equals 6
    if random_number == 6:
        return "<h1>CORRECT!!!6!</h1>"
    else:
        return "<h1>INCORRECT!!!6!</h1>"


# Route for guessing number 7
@app.route("/number/7")
def seven_page():
    # Checks if the random number equals 7
    if random_number == 7:
        return "<h1>CORRECT!!!7!</h1>"
    else:
        return "<h1>INCORRECT!!!7!</h1>"


# Route for guessing number 8
@app.route("/number/8")
def eight_page():
    # Checks if the random number equals 8
    if random_number == 8:
        return "<h1>CORRECT!!!8!</h1>"
    else:
        return "<h1>INCORRECT!!!8!</h1>"


# Route for guessing number 9
@app.route("/number/9")
def nine_page():
    # Checks if the random number equals 9
    if random_number == 9:
        return "<h1>CORRECT!!!9!</h1>"
    else:
        return "<h1>INCORRECT!!!9!</h1>"
