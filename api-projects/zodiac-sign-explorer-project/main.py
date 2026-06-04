#Name: Ryan Pereira
#Project Name: Zodiac Sign Explorer Project
#Description: A program that scrapes zodiac sign data from a website and displays it to the user in a user-friendly way. The program allows the user to view information about different zodiac signs, including their birthday ranges, personality traits, and compatibility.
#Collaborators: None
#Module Name: main.py
#Module Purpose: This program serves as the user interface for the Zodiac Sign Explorer application. It defines the main function, which creates an instance of the ZodiacSignExplorerBrain class and starts the program. The program displays a menu to the user and allows them to select different options to view zodiac sign information.
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 6/1/2026
#Last Modified: 6/4/2026





from zodiac_sign_explorer_brain import ZodiacSignExplorerBrain











def main():
    zodiac_explorer = ZodiacSignExplorerBrain()
    zodiac_explorer.run()




if __name__ == "__main__":
    main()