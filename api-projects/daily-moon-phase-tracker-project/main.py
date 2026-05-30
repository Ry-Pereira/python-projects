#Name: Ryan Pereira
#Project Name: Moon Phase Tracker Project
#Description: A program that scrapes moon phase data from a website and displays it to the user in a user-friendly way. The program allows the user to view the current moon phase, the moon phases for the current week, the moon phases for the next week, and the moon phase for a specific date. The program also includes ASCII art representations of each moon phase.
#Collaborators: None
#Module Name: main.py
#Module Purpose: This program serves as the user interface for the Moon Phase Tracker application. It defines the main function, which creates an instance of the MoonTrackerBrain class and starts the program. The program displays a menu to the user and allows them to select different options to view moon phase information.
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 5/28/2026
#Last Modified: 5/30/2026




#From the art module, import everything. This is where the ASCII art is stored.
from art import *
#From the moon_tracker_brain module, import the MoonTrackerBrain class. This is where the main logic of the program is stored.
from moon_tracker_brain import MoonTrackerBrain


#Defining the main function. This the main entry point of the program. 
def main():
    #Creates an instance of the MoonTrackerBrain class and stores it in moon_tracker variable.
    moon_tracker = MoonTrackerBrain()
    #The moon_tracker instant object calls the run function, which starts the program and displays the menu to the user.
    moon_tracker.run()




#If the program is being run directly, then the main function is called, which starts the program.
if __name__ == "__main__":
    #The main function is called which starts the program.
    main()
