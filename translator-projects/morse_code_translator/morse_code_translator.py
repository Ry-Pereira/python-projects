#Name: Ryan Pereira
#Project Name: Morse Code Translator
#Description: A Python-based Morse Code Translator program that allows users to convert text into Morse code and decode Morse code back into readable text. The program uses a dictionary of Morse code mappings and a menu-driven interface for user interaction. It also includes a feature to display the full Morse code alphabet and numbers for reference.
#Module Name: Morse Code Translator
#Module Purpose: This program serves as a Morse code encoder and decoder. It uses a dictionary to map letters and numbers to Morse code equivalents and performs translation in both directions based on user input.
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 2/11/2024
#Last Modified: 3/3/2024


# Import everything (*) from the art_and_alphabet module
from art_and_alphabet import *


# Define a function to introduce the program
def intro_to_program():
    # Print the welcome ASCII art or banner text
    print(welcome_text)
    # Print a description of what the program does
    print("We can decipher morse code into text and ciypher text into morse code\n\n")


# Define a function to print menu options
def print_menu():
    # Function documentation string
    ''' Prints The Menu Options to Screen'''
    # Print menu option 1
    print("1. Cypher text to Morse Code")
    # Print menu option 2
    print("2. Decpher Morse Code to text")
    # Print menu option 3
    print("3. Print the Morse Code Alphabet and Numbers")
    # Print menu option 4 (currently labeled incorrectly as 3)
    print("3.Exit\n\n")


# Define a function to print all Morse code letters and numbers
def print_morse_code_alphabet_and_numbers():
    # Print heading
    print("MORSE CODE ALPHABET AND NUMBERS\n")
    # Loop through every key in the dictionary
    for morse_character in morse_code_alphabet_and_numbers.keys():
        # Print the letter/number and its Morse code value
        print(morse_character, ":", morse_code_alphabet_and_numbers[morse_character])
    # Print a blank line after the list
    print("\n")


# Define a function to convert normal text into Morse code
def cypher_text(text):
    # Create an empty string to store Morse code translation
    text_to_morse_code = ""
    # Loop through every character in lowercase text
    for character in text.lower():
        # If character is a space
        if character == " ":
            # Add "/" to represent a word space in Morse code
            text_to_morse_code += "/"
        # Otherwise process letters/numbers
        else:
            # Loop through all dictionary keys
            for morse_text in morse_code_alphabet_and_numbers.keys():
                # If character matches dictionary key
                if character == morse_text:
                    # Add Morse code equivalent to the string
                    text_to_morse_code += morse_code_alphabet_and_numbers[morse_text]
    # Print the translated Morse code
    print("Text to Morse Code:", text_to_morse_code)


# Define a function to convert Morse code back into text
def decypher(morse_code):
    # Create a string to store translated text
    morse_code_to_text = " "
    # Split Morse code into a list using spaces
    morse_code_list = morse_code.split(" ")
    # Loop through each Morse code symbol
    for code in morse_code_list:
        # If slash is found, add a space
        if code == "/":
            # Add a space between words
            morse_code_to_text += " "
        # Otherwise decode Morse code
        else:
            # Loop through dictionary keys
            for morse_character in morse_code_alphabet_and_numbers.keys():
                # If dictionary value matches Morse code
                if morse_code_alphabet_and_numbers[morse_character] == code:
                    # Add matching letter/number to output string
                    morse_code_to_text += morse_character
    # Print translated text
    print("Morse Code to Text:", morse_code_to_text)


# Define a function to handle menu choices
def menu_selection(menu_input):
    # Continue looping until user enters 4
    while menu_input != 4:
        # If user selects option 1
        if menu_input == 1:
            # Ask user for text and convert it to Morse code
            cypher_text(input("Text to Morse Code: "))
        # If user selects option 2
        elif menu_input == 2:
            # Ask user for Morse code and decode it
            decypher(input("Morse to Text: "))
        # If user selects option 3
        elif menu_input == 3:
            # Print Morse code alphabet and numbers
            print_morse_code_alphabet_and_numbers()
        # If invalid option entered
        else:
            # Print error message
            print("Please put a valid chopice")
        # Print menu again
        print_menu()
        # Ask user for another menu choice
        menu_input = int(input("Choice: "))


# Define function to print ending message
def end_message():
    # Print exit message
    print("Exit")
    # Thank the user
    print("Thankyou for using")


# Define the main function of the program
def main():
    # Show introduction screen
    intro_to_program()
    # Display menu options
    print_menu()
    # Ask user for menu choice and send it to menu_selection
    menu_selection(menu_input=int(input("Choice: ")))
    # Print ending message
    end_message()


# Call the main function to start the program
main()




    

    

    

    

    

    

    
