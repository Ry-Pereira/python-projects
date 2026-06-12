#Name: Ryan Pereira
#Project Name: Where Am I Locator Project
#Description: A program that uses an IP address API to determine a user's approximate geographic location and display information such as location, time zone, coordinates, and ISP details.
#Module Name: main.py
#Module Purpose: Serves as the entry point of the program by creating an instance of the WhereAmILocatorBrain class and starting program execution.
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 6/10/2026
#Last Modified: 6/12/2026




#Importing the WhereAmILocatorBrain class from the where_am_i_locator_brain module.
from where_am_i_locator_brain import WhereAmILocatorBrain


#Defining the main function, main entry point into the project program.
def main():
  #where_am_i_locator_program set to the instance of WhereAmILocatorBrain class. 
  where_am_i_locator_program = WhereAmILocatorBrain()
  #Executing the run fucntion of the where_am_i_locator_program variable that is class object of WhereAmILocatorBrain class.
  where_am_i_locator_program.run()


#If the program being run directly, this program will be run directly.
if __name__ == "__main__":
  #Main function being executed
  main()
