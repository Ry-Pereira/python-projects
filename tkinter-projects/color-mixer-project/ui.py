#Name: Ryan Pereira
#Project Name: Color Mixer
#Description:# A Tkinter-based program that allows users to mix colors by clicking on buttons representing different colors. The mixed color is displayed on a canvas, and users can reset the canvas to start over.
#Module Name: UI
#Module Purpose: This program serves as the user interface for the Color Mixer application. It defines the ColorMixerUI class, which sets up the Tkinter window, canvas, and buttons for mixing colors. The class includes methods for adding colors to the mix and resetting the color mix.
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 4/4/2026
#Last Modified: 4/9/2026



#Importig everything from the tkinter module, to create the user interface for the color mixer application. 
from tkinter import *
# The partial function from the functools module is imported to allow for passing arguments to button commands. 
from functools import partial
# The colors module is imported to access the defined colors and the function for converting RGB values to hex color codes.
from colors import *


# The ColorMixerUI class is defined to create the user interface for the color mixer application. It initializes the main window, canvas, and buttons for mixing colors. The class includes methods for adding colors to the mix and resetting the color mix.
class ColorMixerUI:
    def __init__(self):
        #The Ui's window is the main window of the application, which is created using the Tk() function from the tkinter module.
        self.window = Tk()
        #The Ui's title is set that encapsulates the purpose of the project program.
        self.window.title("Color Mixer")
        #The Ui's background color is set to white.
        self.canvas_background_color = "#FFFFFF"
        #The Ui's window is configured with padding and a white background color to create a visually appealing layout for the color mixer application.
        self.window.config(padx=20,pady=20,bg="white")
        #The UI has a color mix list of colors that the user has added to the mix, which is initialized as an empty list.
        self.color_mix = []
        #The Ui's title label is created to display the title of the application, and it is placed at the top of the window using the grid layout manager. The label has a specific font and background color to enhance the visual appeal of the application.
        self.title_label = Label(text="COLOR MIXER", font=("Arial",18),bg="white")
        #Tge Ui's title label is placed at the top of the window using the grid layout manager. It spans across 5 columns and has padding to create space around it, making it visually appealing and easy to read for users of the color mixer application.
        self.title_label.grid(row=0,column=0,columnspan=5,pady=10)

        #The Ui's author label is created to display the name of the author of the application, and it is placed below the title label using the grid layout manager. The label has a specific font and background color to enhance the visual appeal of the application and provide credit to the creator.
        self.author_label = Label(text="By: Ryan Pereira", font=("Arial",16),bg="white")
        #The Ui's author label is placed below the title label using the grid layout manager. It spans across 5 columns and has padding to create space around it, making it visually appealing and easy to read for users of the color mixer application while also giving credit to the creator.
        self.author_label.grid(row=1,column=0,columnspan=5,pady=10)


        #The Ui's canvas is created to display the mixed color based on the user's selections. It is initialized with a specific width, height, background color, and border style. The canvas is placed below the author label using the grid layout manager, spanning across 5 columns and having padding to create space around it. This allows users to visually see the resulting color mix as they select different colors in the color mixer application.
        self.canvas = Canvas(width=850,height=300,bg=self.canvas_background_color,highlightthickness=0,bd=3,relief="solid")
        #The Ui's canvas is placed below the author label using the grid layout manager, spanning across 5 columns and having padding to create space around it. This allows users to visually see the resulting color mix as they select different colors in the color mixer application.
        self.canvas.grid(row=2,column=0,columnspan=5,padx=15,pady=15)
                            
        #The Ui's buttons are created for each color option, allowing users to add colors to the mix by clicking on them. Each button is configured with specific text, size, background color, and a command that calls the add_color_to_background_color method with the corresponding RGB color value when clicked. The buttons are placed in a grid layout below the canvas, with padding to create space around them and enhance the visual appeal of the application.
        self.red_button = Button(text="RED",width=17,pady=15,padx=15,bg="red",command=partial(self.add_color_to_background_color,RED))
        #The Ui's red button is created to allow users to add the color red to the mix. It is configured with specific text, size, background color, and a command that calls the add_color_to_background_color method with the corresponding RGB color value when clicked. The button is placed in the grid layout below the canvas, with padding to create space around it and enhance the visual appeal of the application.
        self.red_button.grid(row=3,column=0,pady=10,padx=15)

        #The Ui's orange button is created to allow users to add the color orange to the mix. It is configured with specific text, size, background color, and a command that calls the add_color_to_background_color method with the corresponding RGB color value when clicked. The button is placed in the grid layout below the canvas, with padding to create space around it and enhance the visual appeal of the application.
        self.orange_button = Button(text="ORANGE",width=17,pady=15,padx=15,bg="orange",command=partial(self.add_color_to_background_color,ORANGE))
        #The Ui's orange button is created to allow users to add the color orange to the mix. It is configured with specific text, size, background color, and a command that calls the add_color_to_background_color method with the corresponding RGB color value when clicked. The button is placed in the grid layout below the canvas, with padding to create space around it and enhance the visual appeal of the application.
        self.orange_button.grid(row=3,column=1,pady=10,padx=15)

        #The Ui's yellow button is created to allow users to add the color yellow to the mix. It is configured with specific text, size, background color, and a command that calls the add_color_to_background_color method with the corresponding RGB color value when clicked. The button is placed in the grid layout below the canvas, with padding to create space around it and enhance the visual appeal of the application.
        self.yellow_button = Button(text="YELLOW",width=17,pady=15,padx=15,bg="yellow",command=partial(self.add_color_to_background_color,YELLOW))
        #The Ui's yellow button is created to allow users to add the color yellow to the mix. It is configured with specific text, size, background color, and a command that calls the add_color_to_background_color method with the corresponding RGB color value when clicked. The button is placed in the grid layout below the canvas, with padding to create space around it and enhance the visual appeal of the application.
        self.yellow_button.grid(row=3,column=2,pady=10,padx=15)

        #The Ui's lime button is created to allow users to add the color lime to the mix. It is configured with specific text, size, background color, and a command that calls the add_color_to_background_color method with the corresponding RGB color value when clicked. The button is placed in the grid layout below the canvas, with padding to create space around it and enhance the visual appeal of the application.
        self.lime_button = Button(text="LIME",width=17,pady=15,padx=15,bg="lime",command=partial(self.add_color_to_background_color,LIME))
        #The Ui's lime button is created to allow users to add the color lime to the mix. It is configured with specific text, size, background color, and a command that calls the add_color_to_background_color method with the corresponding RGB color value when clicked. The button is placed in the grid layout below the canvas, with padding to create space around it and enhance the visual appeal of the application.
        self.lime_button.grid(row=3,column=3,pady=10,padx=15)

        #The Ui's green button is created to allow users to add the color green to the mix. It is configured with specific text, size, background color, and a command that calls the add_color_to_background_color method with the corresponding RGB color value when clicked. The button is placed in the grid layout below the canvas, with padding to create space around it and enhance the visual appeal of the application.
        self.green_button = Button(text="GREEN",width=17,pady=15,padx=15,bg="green",command=partial(self.add_color_to_background_color,GREEN))
        #The Ui's green button is created to allow users to add the color green to the mix. It is configured with specific text, size, background color, and a command that calls the add_color_to_background_color method with the corresponding RGB color value when clicked. The button is placed in the grid layout below the canvas, with padding to create space around it and enhance the visual appeal of the application.
        self.green_button.grid(row=3,column=4,pady=10,padx=15)

        #The Ui's teal button is created to allow users to add the color teal to the mix. It is configured with specific text, size, background color, and a command that calls the add_color_to_background_color method with the corresponding RGB color value when clicked. The button is placed in the grid layout below the canvas, with padding to create space around it and enhance the visual appeal of the application.
        self.teal_button = Button(text="TEAL",width=17,pady=15,padx=15,bg="teal",command=partial(self.add_color_to_background_color,TEAL))
        #The Ui's teal button is created to allow users to add the color teal to the mix. It is configured with specific text, size, background color, and a command that calls the add_color_to_background_color method with the corresponding RGB color value when clicked. The button is placed in the grid layout below the canvas, with padding to create space around it and enhance the visual appeal of the application.
        self.teal_button.grid(row=4,column=0,pady=10,padx=15)


        #The Ui's light blue button is created to allow users to add the color light blue to the mix. It is configured with specific text, size, background color, and a command that calls the add_color_to_background_color method with the corresponding RGB color value when clicked. The button is placed in the grid layout below the canvas, with padding to create space around it and enhance the visual appeal of the application.
        self.light_blue_button = Button(text="LIGHT-BLUE",width=17,pady=15,padx=15,bg="light blue",command=partial(self.add_color_to_background_color,LIGHT_BLUE))
        #The Ui's light blue button is created to allow users to add the color light blue to the mix. It is configured with specific text, size, background color, and a command that calls the add_color_to_background_color method with the corresponding RGB color value when clicked. The button is placed in the grid layout below the canvas, with padding to create space around it and enhance the visual appeal of the application.
        self.light_blue_button.grid(row=4,column=1,pady=10,padx=15)


        #The Ui's indigo button is created to allow users to add the color indigo to the mix. It is configured with specific text, size, background color, and a command that calls the add_color_to_background_color method with the corresponding RGB color value when clicked. The button is placed in the grid layout below the canvas, with padding to create space around it and enhance the visual appeal of the application.
        self.indigo_button = Button(text="INDIGO",width=17,pady=15,padx=15,bg="indigo",command=partial(self.add_color_to_background_color,INDIGO))
        #The Ui's indigo button is created to allow users to add the color indigo to the mix. It is configured with specific text, size, background color, and a command that calls the add_color_to_background_color method with the corresponding RGB color value when clicked. The button is placed in the grid layout below the canvas, with padding to create space around it and enhance the visual appeal of the application.
        self.indigo_button.grid(row=4,column=2,pady=10,padx=15)

        #The Ui's blue button is created to allow users to add the color blue to the mix. It is configured with specific text, size, background color, and a command that calls the add_color_to_background_color method with the corresponding RGB color value when clicked. The button is placed in the grid layout below the canvas, with padding to create space around it and enhance the visual appeal of the application.
        self.blue_button = Button(text="BLUE",width=17,pady=15,padx=15,bg="blue",command=partial(self.add_color_to_background_color,BLUE))
        #The Ui's blue button is created to allow users to add the color blue to the mix. It is configured with specific text, size, background color, and a command that calls the add_color_to_background_color method with the corresponding RGB color value when clicked. The button is placed in the grid layout below the canvas, with padding to create space around it and enhance the visual appeal of the application.
        self.blue_button.grid(row=4,column=3,pady=10,padx=15)

        #The Ui's purple button is created to allow users to add the color purple to the mix. It is configured with specific text, size, background color, and a command that calls the add_color_to_background_color method with the corresponding RGB color value when clicked. The button is placed in the grid layout below the canvas, with padding to create space around it and enhance the visual appeal of the application.
        self.purple_button = Button(text="PURPLE",width=17,pady=15,padx=15,bg="purple",command=partial(self.add_color_to_background_color,PURPLE))
        #The Ui's purple button is created to allow users to add the color purple to the mix. It is configured with specific text, size, background color, and a command that calls the add_color_to_background_color method with the corresponding RGB color value when clicked. The button is placed in the grid layout below the canvas, with padding to create space around it and enhance the visual appeal of the application.
        self.purple_button.grid(row=4,column=4,pady=10,padx=15)

        #The Ui's violet button is created to allow users to add the color violet to the mix. It is configured with specific text, size, background color, and a command that calls the add_color_to_background_color method with the corresponding RGB color value when clicked. The button is placed in the grid layout below the canvas, with padding to create space around it and enhance the visual appeal of the application.
        self.violet_button = Button(text="VIOLET",width=17,pady=15,padx=15,bg="violet",command=partial(self.add_color_to_background_color,VIOLET))
        #The Ui's violet button is created to allow users to add the color violet to the mix. It is configured with specific text, size, background color, and a command that calls the add_color_to_background_color method with the corresponding RGB color value when clicked. The button is placed in the grid layout below the canvas, with padding to create space around it and enhance the visual appeal of the application.
        self.violet_button.grid(row=5,column=0,pady=10,padx=15)

        #The Ui's pink button is created to allow users to add the color pink to the mix. It is configured with specific text, size, background color, and a command that calls the add_color_to_background_color method with the corresponding RGB color value when clicked. The button is placed in the grid layout below the canvas, with padding to create space around it and enhance the visual appeal of the application.
        self.pink_button = Button(text="PINK",width=17,pady=15,padx=15,bg="pink",command=partial(self.add_color_to_background_color,PINK))
        #The Ui's pink button is created to allow users to add the color pink to the mix. It is configured with specific text, size, background color, and a command that calls the add_color_to_background_color method with the corresponding RGB color value when clicked. The button is placed in the grid layout below the canvas, with padding to create space around it and enhance the visual appeal of the application.
        self.pink_button.grid(row=5,column=1,pady=10,padx=15)

        #The Ui's white button is created to allow users to add the color white to the mix. It is configured with specific text, size, background color, and a command that calls the add_color_to_background_color method with the corresponding RGB color value when clicked. The button is placed in the grid layout below the canvas, with padding to create space around it and enhance the visual appeal of the application.
        self.white_button = Button(text="WHITE",width=17,pady=15,padx=15,bg="white",command=partial(self.add_color_to_background_color,WHITE))
        #The Ui's white button is created to allow users to add the color white to the mix. It is configured with specific text, size, background color, and a command that calls the add_color_to_background_color method with the corresponding RGB color value when clicked. The button is placed in the grid layout below the canvas, with padding to create space around it and enhance the visual appeal of the application.
        self.white_button.grid(row=5,column=2,pady=10,padx=15)

        #The Ui's black button is created to allow users to add the color black to the mix. It is configured with specific text, size, background color, and a command that calls the add_color_to_background_color method with the corresponding RGB color value when clicked. The button is placed in the grid layout below the canvas, with padding to create space around it and enhance the visual appeal of the application.
        self.black_button = Button(text="BLACK",width=17,pady=15,padx=15,bg="black",command=partial(self.add_color_to_background_color,BLACK))
        #The Ui's black button is created to allow users to add the color black to the mix. It is configured with specific text, size, background color, and a command that calls the add_color_to_background_color method with the corresponding RGB color value when clicked. The button is placed in the grid layout below the canvas, with padding to create space around it and enhance the visual appeal of the application.
        self.black_button.grid(row=5,column=3,pady=10,padx=15)


        #The Ui's gray button is created to allow users to add the color gray to the mix. It is configured with specific text, size, background color, and a command that calls the add_color_to_background_color method with the corresponding RGB color value when clicked. The button is placed in the grid layout below the canvas, with padding to create space around it and enhance the visual appeal of the application.
        self.gray_button = Button(text="GRAY",width=17,pady=15,padx=15 ,bg="gray",command=partial(self.add_color_to_background_color,GRAY))
        #The Ui's gray button is created to allow users to add the color gray to the mix. It is configured with specific text, size, background color, and a command that calls the add_color_to_background_color method with the corresponding RGB color value when clicked. The button is placed in the grid layout below the canvas, with padding to create space around it and enhance the visual appeal of the application.
        self.gray_button.grid(row=5,column=4,pady=10,padx=15)

        #The Ui's reset button is created to allow users to reset the color mix and start over. It is configured with specific text, size, background color, and a command that calls the reset_color_mix method when clicked. The button is placed in the grid layout below the canvas, spanning across 5 columns and having padding to create space around it and enhance the visual appeal of the application.
        self.reset_button = Button(text="RESET COLOR MIX",width=17,pady=15,padx=15,bg="white",command=self.reset_color_mix)
        #The Ui's reset button is created to allow users to reset the color mix and start over. It is configured with specific text, size, background color, and a command that calls the reset_color_mix method when clicked. The button is placed in the grid layout below the canvas, spanning across 5 columns and having padding to create space around it and enhance the visual appeal of the application.
        self.reset_button.grid(row=6,column=0,columnspan=5,pady=15)

        

    
        #The Ui's main loop is started to run the application and display the window to the user. This allows users to interact with the color mixer application and see the resulting color mix on the canvas as they select different colors.
        self.window.mainloop()

    #The add_color_to_background_color method is defined to add a selected color to the color mix and update the canvas background color accordingly. It takes an RGB color value as an argument, adds it to the color mix list, calculates the average RGB values of the colors in the mix, converts the average RGB values to a hex color code, and updates the canvas background color to reflect the new mixed color.
    def add_color_to_background_color(self,rgb_color: tuple[int, int, int]) -> None:
        #The add_color_to_background_color method is defined to add a selected color to the color mix and update the canvas background color accordingly. It takes an RGB color value as an argument, adds it to the color mix list, calculates the average RGB values of the colors in the mix, converts the average RGB values to a hex color code, and updates the canvas background color to reflect the new mixed color.
        self.color_mix.append(rgb_color)
        #R value set to 0
        r_value = 0
        #G value set to 0
        g_value = 0
        #B value set to 0
        b_value = 0
        #Iterating through color in Ui's color mix list
        for color in self.color_mix:
            #R value is incremented byt the r value of the color mix at index 0
            r_value += color[0]
            #G value is incremented byt the g value of the color mix at index 1
            g_value += color[1]
            #B value is incremented byt the b value of the color mix at index 2
            b_value += color[2]
        #The average RGB values are calculated by dividing the total R, G, and B values by the number of colors in the mix. This gives the average color that results from mixing the selected colors together.
        self.canvas_background_color = (r_value//len(self.color_mix),g_value//len(self.color_mix),b_value//len(self.color_mix))
        #Hex number of color is obtained by converting the average RGB values to a hex color code using the convert_rgb_to_hex_color function from the colors module. This hex color code is then used to update the background color of the canvas, allowing users to see the resulting mixed color as they select different colors in the color mixer application.
        hex_number_of_color = convert_rgb_to_hex_color(self.canvas_background_color)
        #The canvas background color is updated to reflect the new mixed color by configuring the canvas with the new hex color code. This allows users to visually see the resulting color mix on the canvas as they select different colors in the color mixer application.
        self.canvas.config(bg=hex_number_of_color)

    #The reset_color_mix method is defined to reset the color mix and start over. It clears the color mix list, resets the canvas background color to white, and updates the canvas to reflect the reset state of the color mixer application.
    def reset_color_mix(self) -> None:
        #The Ui's color mix list is reset to be empty
        self.color_mix = []
        #The Ui's canvas background color is reset to white, and the canvas is updated to reflect the reset state of the color mixer application. This allows users to start over and create new color mixes without any previous colors affecting the resulting mix.
        self.canvas_background_color = "#FFFFFF"
        #The canvas background color is reset to white, and the canvas is updated to reflect the reset state of the color mixer application. This allows users to start over and create new color mixes without any previous colors affecting the resulting mix.
        self.canvas.config(bg=self.canvas_background_color)



    
    
    










testui = ColorMixerUI()