#Name: Ryan Pereira
#Project Name: Kanye West Quote Generator
#Description:# A Tkinter-based program that fetches api data from a Kanye Quote source that distributes a random quote,quoted by Kanye West himself. Everytime the user clicks on the Kany West memoji icon, a new quote will appear in a random color speech bubble.
#Module Name: Main
#Module Purpose: This porgram file is the entyr point into the project program itself.
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 6/19/2026
#Last Modified: 6/21/2026


#From the ui module,imports the KanyeWestGeneratorUI class to 
from ui import KanyeWestGeneratorUI


#The function main, is the main entry point into the program
def main() -> None:
    #The kanywestui variable stores the object of the KanywestGeneratorUI class constructor
    kanywestui = KanyeWestGeneratorUI()
    

#If the progrma is being run directly, then the main function will be called
if __name__=="__main__":
    #The main function will be called
    main()