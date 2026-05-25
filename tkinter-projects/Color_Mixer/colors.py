#Name: Ryan Pereira
#Project Name: Color Mixer
#Description:# A Tkinter-based program that allows users to mix colors by clicking on buttons representing different colors. The mixed color is displayed on a canvas, and users can reset the canvas to start over.
#Module Name: Colors
#Module Purpose: This program serves as a module that defines various colors as RGB tuples. These color definitions are used in the Color Mixer application to allow users to mix colors and see the resulting color on a canvas.
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 4/4/2026
#Last Modified: 4/9/2026







#Colors with associated rgb value tuples to represent them
RED = (214, 33, 33)
ORANGE = (214, 103, 33)
YELLOW = (214, 211, 33)
LIME = (151, 214, 33)
GREEN = (63, 214, 33)
TEAL = (33, 214, 178)
LIGHT_BLUE = (33, 208, 214)
INDIGO = (33, 118, 214)
BLUE = (33, 54, 214)
PURPLE = (118, 33, 214)
VIOLET = (175, 33, 214)
PINK = (214, 33, 193)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (107, 107, 107)


#Function to convert rgb color values to hex color values
def convert_rgb_to_hex_color(rgb_color_value: tuple) -> str:
        #The function takes a tuple of RGB color values and returns a string representing the corresponding hex color value. The RGB values are formatted as two-digit hexadecimal numbers and concatenated together with a "#" prefix to create the hex color code.
        return f"#{rgb_color_value[0]:02X}{rgb_color_value[1]:02X}{rgb_color_value[2]:02X}"