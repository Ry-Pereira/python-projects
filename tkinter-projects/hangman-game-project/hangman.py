# Name: Ryan Pereira
# Project Name: Hangman
# Description: A simple hangman game where the user tries to guess a word
# Collaborators: None
# Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
# Date: 4/11/2026
# Last Modified: 4/11/2026



# From tkinter module import everything (GUI toolkit)
from tkinter import *

# From tkinter module import messagebox (popup alerts)
from tkinter import messagebox

# Import hangman ASCII art stages
from hangman_art import stage_0, stage_1, stage_2, stage_3, stage_4, stage_5, stage_6

# Import partial to pass arguments into button commands
from functools import partial

# Import random module for word selection
import random


# List of possible hangman words
hangman_words = ["python", "variable", "function", "loop", "string","integer", "boolean", "list", "tuple", "dictionary","computer", "keyboard", "monitor", "program", "debug","compile", "execute", "syntax", "library", "package",
    "network", "server", "client", "database", "algorithm","puzzle", "mystery", "adventure", "galaxy", "treasure",
    "castle", "dragon", "wizard", "knight", "kingdom","forest", "desert", "ocean", "island", "volcano","planet", "asteroid", "comet", "nebula", "universe"
]

# Alphabet list for button creation
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

# Starting stage of hangman drawing
stage_number = 0

# List of hangman ASCII stages
hangman_stages = [stage_0, stage_1, stage_2, stage_3, stage_4, stage_5, stage_6]

# Number of lives at start
lives = 6


# Selected word stored as list of letters
hangman_selected_word = None

# Blanked-out version of word (underscores)
hangman_blanked_out_word = None


# Function to select a random word
def select_word():
    # Choose random word from list
    selected_word = random.choice(hangman_words)
    # Convert word to uppercase
    selected_word = selected_word.upper()
    # Return word as list of letters
    return list(selected_word)


# Function to create blank word display
def blankout_word(word):
    # Create empty list
    blankout_word = []
    # Replace each letter with underscore
    for letter in word:
        blankout_word.append("_")
    # Return blanked word
    return blankout_word


# Main game function
def main():
    # Use global variables
    global hangman_selected_word
    global hangman_blanked_out_word


    # Disable all letter buttons
    def disbale_all_buttons():
        for button in buttons:
            button.config(state=DISABLED)


    # Enable all letter buttons
    def enable_all_buttons():
        for button in buttons:
            button.grid()
        for button in buttons:
            button.config(state=NORMAL)


    # Restart the game
    def restart():
        global hangman_selected_word
        global hangman_blanked_out_word
        global lives
        global stage_number
        # Select new word
        hangman_selected_word = select_word()
        # Reset blank word
        hangman_blanked_out_word = blankout_word(hangman_selected_word)
        # Reset lives
        lives = 7
        # Reset stage
        stage_number = 0
        # Hide continue button
        continue_button.grid_remove()
        # Hide quit button
        quit_button.grid_remove()
        # Enable letter buttons
        enable_all_buttons()
        # Reset hangman art
        canvas.itemconfig(hangman_art, text=hangman_stages[stage_number])
        # Reset word display
        canvas.itemconfig(hangman_word, text=hangman_blanked_out_word)


    # Quit game
    def quit_game():
        window.destroy()


    # Show continue/quit screen
    def continue_or_leave():
        for button in buttons:
            button.grid_remove()

        continue_button.grid(row=2,column=0,rowspan=2,columnspan=5,pady=5)
        quit_button.grid(row=2,column=10,rowspan=2,columnspan=5,pady=5)


    # Lose screen
    def lose_screen():
        disbale_all_buttons()
        canvas.itemconfig(hangman_art,text="YOU LOSE")
        canvas.itemconfig(hangman_word,text=hangman_selected_word)
        window.after(4000,continue_or_leave)


    # Win screen
    def win_screen():
        disbale_all_buttons()
        canvas.itemconfig(hangman_art,text="YOU WIN")
        window.after(4000,continue_or_leave)


    # Switch hangman stage
    def switch_stage(stage):
        canvas.itemconfig(hangman_art,text=hangman_stages[stage])


    # Handle letter button click
    def type_letter(letter,letter_button):
        letter_button.config(state=DISABLED)
        type_in_letter(letter)


    # Process guessed letter
    def type_in_letter(letter):
        global stage_number
        global lives
        is_there = False
        # Check if letter exists in word
        for num in range(len(hangman_selected_word)):
            if hangman_selected_word[num] == letter:
                is_there = True
                hangman_blanked_out_word[num] = letter
                canvas.itemconfig(hangman_word,text=hangman_blanked_out_word)
        # Wrong guess handling
        if is_there == False:
            stage_number += 1
            lives -= 1
        # Update hangman stage
        if stage_number <= 6:
            switch_stage(stage_number)
        # Win condition
        if hangman_blanked_out_word == hangman_selected_word:
            win_screen()
        # Lose condition
        if lives == 0:
            lose_screen()
    # Initialize game word
    hangman_selected_word = select_word()
    # Initialize blank word
    hangman_blanked_out_word = blankout_word(hangman_selected_word)
    # Create main window
    window = Tk()
    # Set window title
    window.title("Hangman Game")
    # Add padding to window
    window.config(padx=50,pady=50)
    # Create title label
    hangman_title = Label(text="HANGMAN",font=("Arial",20))
    hangman_title.grid(row=0,column=0,columnspan=13)
    # Create canvas
    canvas = Canvas(width=320,height=200,bg="blue")
    # Add hangman ASCII text
    hangman_art = canvas.create_text(160,90,text=stage_0,font=("Arial",13),anchor="center")
    # Add word display text
    hangman_word = canvas.create_text(160,180,text=hangman_blanked_out_word,font=("Arial",20),anchor="center")
    # Place canvas
    canvas.grid(row=1,column=0,columnspan=13)
    # Create restart button
    continue_button = Button(text="RESTART",command=restart,width=21,height=3)
    # Create quit button
    quit_button = Button(text="QUIT",command=quit_game,width=21,height=3)
    # Store letter buttons
    buttons = []
    # Create alphabet buttons
    for alphabet_letter in alphabet:
        # Create button
        button = Button(text=alphabet_letter,width=2)
        # Assign button action
        button.config(command=partial(type_letter,alphabet_letter,button))
        # Add to list
        buttons.append(button)
        # Place button in grid
        if buttons.index(button) < 13:
            buttons[buttons.index(button)].grid(row=2,column=buttons.index(button),padx=0,pady=20)
        else:
            buttons[buttons.index(button)].grid(row=3,column=(buttons.index(button)-13),padx=0,pady=20)
    # Start GUI loop
    window.mainloop()


# Run program
main()
