#Name: Ryan Pereira
#Project Name: Color Mixer
#Description:# A Tkinter-based program that allows users to mix colors by clicking on buttons representing different colors. The mixed color is displayed on a canvas, and users can reset the canvas to start over.
#Module Name: Main
#Module Purpose: This program serves as the entry point for the Color Mixer application. It imports the ColorMixerUI class from the ui module and initializes the user interface when the program is run.
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 4/4/2026
#Last Modified: 4/9/2026




#Importing the ColorMixerUI class from the ui module
from ui import ColorMixerUI


#The main function is the entry point of the program. It initializes the ColorMixerUI class, which sets up the user interface for the color mixer application.
def main() -> None:
    #Initializing the ColorMixerUI class, which sets up the user interface for the color mixer application.
    color_mixer_ui = ColorMixerUI()




#If the program is being run directly, then the main function will be called
if __name__ == "__main__":
    #Main function is called
    main()