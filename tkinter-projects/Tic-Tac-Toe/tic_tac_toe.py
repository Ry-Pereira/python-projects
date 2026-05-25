#Name: Ryan Pereira
#Project Name: Tic-Tac-Toe
#Description:# A Tkinter-based Tic-Tac-Toe game where two players take turns placing X or O on a 3x3 grid.The program manages turns, checks for wins or ties, and allows restarting or quitting after the game ends.
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 6/16/2026
#Last Modified: 6/18/2026

#From tkinter import all the classes and functions, which allows us to use them without prefixing them with tkinter.
from tkinter import *
#From functools import partial, which allows us to use the partial function, which is used to pass arguments to the command of the button, without using lambda functions.
from functools import partial
#Import random, which allows us to use the random.choice function to randomly select a symbol for the player to start with.
import random

#Symbols is a list that contains the two symbols used in the game, X and O.
symbols=["X","O"]
#Symbol is set to None
symbol = None
#Winner is set to None
winner = None
#Buttons is set to None
buttons = None
#Window is set to None
window = None

#Continue_button is set to None
continue_button = None
#Quit_button is set to None
quit_button = None

#Tic_tac_toe_turn_label is set to None
tic_tac_toe_turn_label = None
#Tic_tac_toe_label is set to None
tic_tac_toe_label = None


#The remove reset all buttons, is a function that removes all the buttons from the grid, which is used when the game is over, and the player has to choose whether to restart or quit the game.
def remove_reset_all_buttons():
        #Buttons is set to global
        global buttons
        #For button in buttons loop, for every button in the buttons list, the following code is executed
        for button in buttons:
            #Buttons is removed from the grid, which makes it invisible in the window, until the game is restarted
            button.grid_remove()

#The quit game function, is a function that destroys the window, which is used when the player chooses to quit the game.
def quit_game():
        #Window is set to global
        global window
        #Window destroy function is executed, which closes the window and ends the game.
        window.destroy()


#The restart or quit function, is a function that makes the continue button and quit button visible in the window, which is used when the game is over, and the player has to choose whether to restart or quit the game.
def restart_or_quit():
        #Continue_button and quit_button is set to global, so they can be accessed and modified in this function
        global continue_button
        #Quit_button is set to global, so they can be accessed and modified in this function
        global quit_button
        #Continue_button and quit_button are gridded to the window, which makes them visible in the window, so the player can choose whether to restart or quit the game.
        continue_button.grid()
        #QUit_button is gridded to the window, which makes it visible in the window, so the player can choose whether to restart or quit the game.
        quit_button.grid()


# The restart game function is used to restart the game, back to the original when the user first started playing the program game
def restart_game():
        #Symbol set to global
        global symbol
        #Quit button set to global
        global quit_button
        #Continue button set to global
        global continue_button
        #Tic-tac-toe-turn-label set to global
        global tic_tac_toe_turn_label

        #Symbol set to the random choise of the symbols list
        symbol = random.choice(symbols)
        #Quit button is removed from the grid, but remembered of its position
        quit_button.grid_remove()
        #Continue button is removed from the grid, but remembered of its position
        continue_button.grid_remove()
        #Iterating over each button in buttons list, following code is executed below for each iteration
        for button in buttons:
            #Buttons is gridded back to its position
            button.grid()
            #Buttons is updated with text,background and state set to functioning as before
            button.config(text="-",bg="white",state=NORMAL)
        
        #If the symbol is set to X, following code is executed
        if symbol == "X":
            #Tic-Tac-Toe turn labl is upated with the text to say who;s turn it is, the font,width,foreground and background specification
            tic_tac_toe_turn_label.config(text=f"{symbol}'s Turn:",font=("Arial",15),width=15,fg="red",bg='black')
        #If the symbol is set to O, following code is executed
        if symbol == "O":
            #Tic-Tac-Toe turn labl is upated with the text to say who;s turn it is, the font,width,foreground and background specification
            tic_tac_toe_turn_label.config(text=f"{symbol}'s Turn:",font=("Arial",15),width=15,fg="blue",bg="black")


#The function did win, with symbol to compare put in as parameter argument. To to see if the tic tac board has a win, a tie, or not
def did_win(symbol_to_compare):
        #Buttons set to global
        global buttons
        
        #LEft and right
        #If the button at index 0,1,2 if the text is set to the symbol to compare, then its a win
        if buttons[0]["text"] == symbol_to_compare and buttons[1]["text"] == symbol_to_compare and buttons[2]["text"] == symbol_to_compare:
            #Return win string to indicate there is a winner
            return "win"
        #Elif the button at index 3,4,5 if the text is set to the symbol to compare, then its a win
        elif buttons[3]["text"] == symbol_to_compare and buttons[4]["text"] == symbol_to_compare and buttons[5]["text"] == symbol_to_compare:
            #Return win string to indicate there is a winner
            return "win"
        #Elif the button at index 6,7,8 if the text is set to the symbol to compare, then its a win
        elif buttons[6]["text"] == symbol_to_compare and buttons[7]["text"] == symbol_to_compare and buttons[8]["text"] == symbol_to_compare:
            #Return win string to indicate there is a winner
            return "win"

        #Up and Down
        #Elif the button at index 0,3,6 if the text is set to the symbol to compare, then its a win
        elif buttons[0]["text"] == symbol_to_compare and buttons[3]["text"] == symbol_to_compare and buttons[6]["text"] == symbol_to_compare:
            #Return win string to indicate there is a winner
            return "win"
        #Elif the button at index 1,4,7 if the text is set to the symbol to compare, then its a win
        elif buttons[1]["text"] == symbol_to_compare and buttons[4]["text"] == symbol_to_compare and buttons[7]["text"] == symbol_to_compare:
            #Return win string to indicate there is a winner
            return "win"
        #Elif the button at index 2,5,8 if the text is set to the symbol to compare, then its a win
        elif buttons[2]["text"] == symbol_to_compare and buttons[5]["text"] == symbol_to_compare and buttons[8]["text"] == symbol_to_compare:
            #Return win string to indicate there is a winner
            return "win"


        #Across
        #Elif the button at index 0,4,8 if the text is set to the symbol to compare, then its a win
        elif buttons[0]["text"] == symbol_to_compare and buttons[4]["text"] == symbol_to_compare and buttons[8]["text"] == symbol_to_compare:
             #Return win string to indicate there is a winner
             return "win"
        #Elif the button at index 2,4,6 if the text is set to the symbol to compare, then its a win
        elif buttons[2]["text"] == symbol_to_compare and buttons[4]["text"] == symbol_to_compare and buttons[6]["text"] == symbol_to_compare:
            #Return win string to indicate there is a winner
            return "win"
        #Else if all condition fail, following code will execute it
        else:
            #Is tie variable set to to True to idnicate no winner was set from the board
            is_tie = True
            #Iterate over each button in buttons list, code executes per iteration
            for button in buttons:
                #If the button text is set - string, following code is executed
                if button["text"] == "-":
                    #Then is tie variable is set to False
                    is_tie = False
            #If is tie variable set to True, there is a tie, code below is executed
            if is_tie == True:
                #Returns tie string to indicate, there is a tie in the board, no one won
                return "tie"
            #Returns continue string, to indicate no winner has been reached, no tie has occured, there are still buttons to press for the game to continue
            return "continue"

#The symbol mark function is used to mark the button that was pressed by the user, with the symbol assigned, and making the button unsuable, as its already marked
def symbol_mark(button):
        #Symbol set to global
        global symbol
        #Tic-Tac-Toe turn label set to global
        global tic_tac_toe_turn_label
        
        #If the symbol is set to X string
        if symbol == "X":
            #Button is configered with text set to symbol, background is set to red
            button.config(text=symbol,bg="red")
            #Did won variable is set to the value return of did win with symbol given as argument
            did_won = did_win(symbol)
            #If did won is equal to win string
            if did_won == "win":
                #Tic-Tac-Toe turn label is configure with following specific values
                tic_tac_toe_turn_label.config(text="X WINS!",font=("Arial",15),width=15,fg="red")
                #Remove reset all buttons is executed
                remove_reset_all_buttons()
                #Restart or quite function is called
                restart_or_quit()
            #If did won is equal to tie string
            elif did_won == "tie":
                #Tic-Tac-Toe turn label is configure with following specific values
                tic_tac_toe_turn_label.config(text="TIE",font=("Arial",15),width=15,fg="GREEN")
                #Remove reset all buttons is executed
                remove_reset_all_buttons()
                #Restart or quite function is called
                restart_or_quit()

            else:
                #Symbol is set to O string
                symbol = "O"
                #Tic-Tac-Toe turn label is configure with following specific values
                tic_tac_toe_turn_label.config(text=f"{symbol}'s Turn:",font=("Arial",15),width=15,fg="blue")
         
        #If the symbol is set to O string
        else:
            #Button is configered with text set to symbol, background is set to blue
            button.config(text=symbol,bg="blue")
            #Did won variable is set to the value return of did win with symbol given as argument
            did_won = did_win(symbol)
            #If did won is equal to win string
            if did_won == "win":
                #Tic-Tac-Toe turn label is configure with following specific values
                tic_tac_toe_turn_label.config(text="O WINS!",font=("Arial",15),width=15,fg="blue")
                #Remove reset all buttons is executed
                remove_reset_all_buttons()
                #Restart or quite function is called
                restart_or_quit()
            #If did won is equal to tie string
            elif did_won == "tie":
                #Tic-Tac-Toe turn label is configure with following specific values
                tic_tac_toe_turn_label.config(text="TIE",font=("Arial",15),width=15,fg="GREEN")
                #Remove reset all buttons is executed
                remove_reset_all_buttons()
                #Restart or quite function is called
                restart_or_quit()
            else:
                #Symbol is set to X string
                symbol = "X"
                #Tic-Tac-Toe turn label is configure with following specific values
                tic_tac_toe_turn_label.config(text=f"{symbol}'s Turn:",font=("Arial",15),width=15,fg="red")

        #Button is configured the state to be disbaled, so the buttons can be used anymore, until reset
        button.config(state=DISABLED)


#The window setup function, sets up the main window of the game
def window_setup():
    #Window variable is set to global, so it can be accessed and modified in other functions
    global window
    #Window variable is set to the Tk object, which creates a new window for the game
    window = Tk()
    #Window title is set to "Tic-Tac-Toe"
    window.title("Tic-Tac-Toe")
    #Window config the padx and pady to 50, which adds padding around the window, making it look better and more spacious
    window.config(padx=50,pady=50)
    #The function returns the window variable, which is the main window of the game, and can be used to start the main loop of the game
    return window

#The button setup function, sets up all the buttons in the window
def button_setup():
    #Buttons set to global
    global buttons
    #Continue_button set to global
    global continue_button
    #Quit_button set to global
    global quit_button
    #Buttons is set to an empty list, initially, and then store all buttons
    buttons = []

    #For num in range 9 loop, to loop through all number from 0 to 9, for each number, the following code is executed
    for num in range(9):
        #Button variable is set to the Button object with text, height, and width set to specific value
        button = Button(text="-",height=4,width=7)
        #Button config function is executed to set the command of the button to the symbol_mark function with the button as an argument, using partial to pass the button as an argument to the function
        button.config(command=partial(symbol_mark,button))
        #If number is less than 3, the button is gridded to the window with specific row,column, padx, and pady values
        if num < 3:
             #Button is gridded to the window with specific row,column, padx, and pady values
             button.grid(row=2,column=num,padx=0,pady=0)
        #Elif number is greater than or equal to 3 and less than 6, the button is gridded to the window with specific row,column, padx, and pady values
        elif num >=3 and num < 6:
             #Button is gridded to the window with specific row,column, padx, and pady values
             button.grid(row=3,column=num-3,padx=0,pady=0)
        #Elif number is greater than or equal to 6, the button is gridded to the window with specific row,column, padx, and pady values
        elif num >= 6:
             #Button is gridded to the window with specific row,column, padx, and pady values
             button.grid(row=4,column=num-6,padx=0,pady=0)
        #The button is appended to the buttons list
        buttons.append(button)


    #Continue_button and quit_button are set to the Button object with text, command, width, and height set to specific value
    continue_button = Button(text="Restart",command=restart_game,width=11,height=2)
    #Quit_button is set to the Button object with text, command, width, and height set to specific value
    quit_button = Button(text="Quit",command=quit_game, width = 11,height=2)
    #Continue_button and quit_button are gridded to the window with specific row,column, rowspan, columnspan, and padx values
    continue_button.grid(row=2,column=0,rowspan=3,columnspan=2,padx=0)
    #Quit_button is gridded to the window with specific row,column, rowspan, columnspan, and padx values
    quit_button.grid(row=2,column=2,rowspan=3,columnspan=2,padx=0)
    #Continue_button and quit_button are removed from the grid, so they are not visible in the window, until the game is over
    continue_button.grid_remove()
    #Quit_button is removed from the grid, so they are not visible in the window, until the game is over
    quit_button.grid_remove()
    #The function returns the buttons, continue_button, and quit_button
    return buttons,continue_button,quit_button



#The Label Setup function, sets up all the labels in the window
def label_setup():
    #Symbol set to global
    global symbol
    #Tic_tac_toe_label set to global
    global tic_tac_toe_label
    #Tic_tac_toe_turn_label set to global
    global tic_tac_toe_turn_label

    #Tic_tac_toe_label is set to the Label object with text,font, and width set to specific value
    tic_tac_toe_label = Label(text="TIC-TAC-TOE",font=("Arial",15),width=15)
    #Tic_tac_toe_label is gridded to the window with specific row,column, columnspan, and pady values
    tic_tac_toe_label.grid(row=0,column=0,columnspan=4,pady = 10)
    #If the symbol is X
    if symbol == "X":
        #Tic_tac_toe_turn_label is set to the Label object with text,font, width, fg, and bg set to specific value
        tic_tac_toe_turn_label = Label(text=f"{symbol}'s Turn:",font=("Arial",15),width=15,fg="red",bg='black')
    #If the symbol is O
    if symbol == "O":
        #Tic_tac_toe_turn_label is set to the Label object with text,font, width, fg, and bg set to specific value
        tic_tac_toe_turn_label = Label(text=f"{symbol}'s Turn:",font=("Arial",15),width=15,fg="blue",bg="black")
    #tic_tac_toe_turn_label is gridded to the window with specific row,column, columnspan, and pady values
    tic_tac_toe_turn_label.grid(row=1,column=0,columnspan=4,pady = 10)
    #The function returns the tic_tac_toe_label and tic_tac_toe_turn_label
    return tic_tac_toe_label,tic_tac_toe_turn_label
     
     
#The main function, is the main entry pointo the program
def main():

    #Symbol set to global
    global symbol
    #Tic_tac_toe_turn_label set to global
    global tic_tac_toe_turn_label
    #Continue_button set to global
    global continue_button
    #Quit_button set to global
    global quit_button
    #Tic_tac_toe_label set to global
    global tic_tac_toe_label

    #Window variable is set to the return value of window setup function
    window = window_setup()
    #Symbol variable is set to a random choice of list of symbols which gives you either X or O
    symbol = random.choice(symbols)
    #Tic_tac_toe_label and Tic_tac_toe_turn_label is set to label setup function return values
    tic_tac_toe_label,tic_tac_toe_turn_label = label_setup()
    #Buttons,continue button, and quit button is set to the return values of button setup
    buttons,continue_button,quit_button = button_setup()
    #Winow main loop function is executed which continues the life of the window, until the quit button is marked by the user
    window.mainloop()



#If the program is run directly, then the following code below will commence
if __name__ == "__main__":
    #Main function, the main entyr point into the program is executed
    main()
