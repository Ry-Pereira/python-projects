#Name: Ryan Pereira
#Project Name: Kanye West Quote Generator
#Description:# A Tkinter-based program that fetches api data from a Kanye Quote source that distributes a random quote,quoted by Kanye West himself. Everytime the user clicks on the Kany West memoji icon, a new quote will appear in a random color speech bubble.
#Module Name: ui
#Module Purpose: The UI python file contains all information for forming a UI this project program forms for, in order to interact with the user.
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 6/19/2026
#Last Modified: 6/21/2026


#Fromt the tkinter module, importing everything , functions and variables in order to create a graphical user interface
from tkinter import *
#From the kanye west quote data, importing everything, the function in order to retrieve a randome quote frome the API
from kanye_west_quote_data import *
#Importing the random function, in order to get a random speech bubble color everytime, a new quote is generated
import random

#Background color is constant and set to specified color
BACKGROUND_COLOR = "#8CC7C4"
#Window color is constant and set to specified color
WINDOW_COLOR = "#2C687B"
#Title color is constant and set to specified color
TITLE_COLOR = "white"

#Class KanyeWestGeneratorUI, is class constructor for the GUI for the project program
class KanyeWestGeneratorUI:
    #The init function is used for initialzing a UI object for the project program, with all the correct items
    def __init__(self) :
        #The UI object's window is set to the Tkinter GUI object
        self.window = Tk()
        #The Ui's window title is set to the project's purpose
        self.window.title("Kanye West Quote Generator")
        #The UI's window is updated with a padding of 20 for the x and y positions, with a background color set to the Window Color
        self.window.config(padx=20,pady=20,bg=WINDOW_COLOR)

        #The UI has a title label set to the program name, with specified font, and background color set to window color, and foreground color set to the title color
        self.title_label = Label(text="Kanye West Quote Generator",font=("Arial",24,"bold italic"),bg=WINDOW_COLOR,fg=TITLE_COLOR)
        #The Ui's title label is gridded at location row 0 and column 0, with a spand of the column to 2 
        self.title_label.grid(row=0,column=0,columnspan=2)

        #The UI has a canvas with a width and height of 600, with a background color to set background color value, with a highlighthickness of 0
        self.canvas = Canvas(width = 600,height=600,bg=BACKGROUND_COLOR,highlightthickness=0)
        #The Ui's canvas is gridded at row 1 and column 0 with a column span 2, and a paddying at the y position of 10
        self.canvas.grid(row=1,column=0,columnspan=2,pady=10)

        #The UI has a kanye image set to e Photo object, with file set to specific file name in project folder
        self.kanye_image = PhotoImage(file="images/kanye_faces/kanye.png")
        #The kanye image id is set to the Ui's canvas with a image of a specified x and y position, with the image set to eht UI's kanye image
        kanye_image_id = self.canvas.create_image(230,500,image = self.kanye_image)
        #The Ui bind the kanye image id and button that get sleft clicked, to the command to thingking of a quote
        self.canvas.tag_bind(kanye_image_id,"<Button-1>",self.thinkinking_quote)

        #The UI's intro text is set to a text to tell the user what to do, in order for the progrma to be used, and set at a specified x and y position and with text set, and font set. The width was set to 170 in order to be wrapped around
        self.intro_text = self.canvas.create_text(300,240,text="Click on Kanye West for Quote.",font=("Arial",18,"bold italic"),width=170)

        #The Ui's speech bubble set is set to all Photo Image objects, set to all colors included in the speech bubble files under images
        self.speech_bubbles = [PhotoImage(file="images/speech_bubbles/red_speech.png"),PhotoImage(file="images/speech_bubbles/orange_speech.png"),PhotoImage(file="images/speech_bubbles/yellow_speech.png"),PhotoImage(file="images/speech_bubbles/green_speech.png"),PhotoImage(file="images/speech_bubbles/blue_speech.png"),PhotoImage(file="images/speech_bubbles/purple_speech.png"),PhotoImage(file="images/speech_bubbles/pink_speech.png")]
        #Self bubble is set to None, becauase one the user visites the program, they will be introdcued first, no quote yet until they prompt to by clicking on the Kanye Image button
        self.bubble = None
        #Same thing with Ui's bubble text is set to None, becuase the user visites the program, they will be introdcued first, no quote yet until they prompt to by clicking on the Kanye Image button.
        self.bubble_text = None

        
        #The window envokes the mainloop function for the GUI window to keep running untilt the user wants to exit out
        self.window.mainloop()


    #The thinking quote function , requires and event parameter, because of the tag bind function to work. Whenver a new quote is wanted, the previous quote and text si removed including the intro text at the beginning
    def thinkinking_quote(self,event :Tk.Event ) -> None:
        #The UI's canvas deletes the intro text
        self.canvas.delete(self.intro_text)
        #The UI's canvas deletes the bubble
        self.canvas.delete(self.bubble)
        #The UI's canvas deletes the bubble text
        self.canvas.delete(self.bubble_text)
        #Adter hald a secongd, the window envokes the UI's generate random quote function
        self.window.after(500,self.generate_random_quote)
    


    #The function generate random quote functiom, will store the response and quote from the get response function that will retrieve a random quote form the API, get  abubble image at random and change the xt to the quote on the scrren for the user to see
    def generate_random_quote(self) -> None:
        #Response and quote is set to the get response function
        response,quote,status = get_response()
        #If the status code is 200, then the API was retrived well, and no error occurred
        if status == 200:
            #UI's bubble is set to the canvas creating and image with a image set to a random choice on the speech bubbles list, and at a x and y position
            self.bubble = self.canvas.create_image(300,250,image = random.choice(self.speech_bubbles))
            #Ui's bubble text is set to canvas crating text at x and y position, with specific font, and text set to the quote, with the width set to a specified number so it can wrap around.
            self.bubble_text= self.canvas.create_text(300,240,text=quote,font=("Arial",18,"bold italic"),width=170)
        #Elif the status code is not 200, then a error occurred when retrieving API information regarding to getting random quote from API.
        else:
            self.bubble_text= self.canvas.create_text(300,240,text="API Not Working At Moment.Try Later.",font=("Arial",18,"bold italic"),width=170)







