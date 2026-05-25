#Name: Ryan Pereira
#Project Name: Caesar Cipher Program
#Description: A Python-based Caesar Cipher application that allows users to encrypt and decrypt words by shifting letters through the alphabet.Users can choose to cipher or decipher text using a custom shift value through a menu-driven interface.
#Module Name: Caesar Cipher
#Module Purpose: This program serves as a Caesar Cipher encoder and decoder.It uses alphabet indexing and shift logic to transform text into encrypted or decrypted forms based on the user’s chosen shift amount.
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 2/10/2023
#Last Modified: 2/13/2023

# Import everything from the art_and_alphabet module
from art_and_alphabet import *



# Define a function to introduce the program
def intro_to_program():
    # Print the ASCII art or title text
    print(text)
    # Print welcome message
    print("Welcome to Caesar Cipher Program\n")
    # Print the index location of "z" in the alphabet list
    print(alphabet.index("z"))


# Define a function to display the menu
def print_menu():
    # Print menu option 1
    print("1. To Cipher Code")
    # Print menu option 2
    print("2. To Decipher Code\n")
    # Print menu option 3
    print("3. To Exit the Program")


# Define a function to handle menu choices
def menu_selection(choice):
    # If user chooses option 1
    if choice == 1:
        # Ask user for word and cipher it
        cypher_code(word_to_cypher=input("Word to Cipher: "))
    # If user chooses option 2
    elif choice == 2:
        # Ask user for word and decipher it
        decypher_code(word_to_decypher=input("Word to Decipher: "))
    # If user chooses option 3
    elif choice == 3:
        # Print goodbye message
        print("Goodbye")
    # If choice is invalid
    else:
        # Print error message
        print("Type in valid choice")
        # Ask user again for valid choice
        menu_selection(choice=int(input("Choice: ")))


# Define a function to cipher/encrypt text
def cypher_code(word_to_cypher):
    # Create an empty list for encrypted letters
    cyphered_word = []
    # Ask user for shift amount
    amount_of_shifts = int(input("Amount of shift: "))
    # Loop through every letter in the word
    for letter in word_to_cypher:
        # Find shifted index
        index_shift = alphabet.index(letter) + amount_of_shifts
        # Print shifted index before adjustment
        print(index_shift)
        # Adjust index if it goes beyond alphabet range
        while index_shift >= 25:
            index_shift -= 1
            index_shift -= 25
        # Print adjusted index
        print(index_shift)
        # Add shifted letter to encrypted list
        cyphered_word.append(alphabet[index_shift])
    # Create empty string for final encrypted word
    final_cyphered_word = ''
    # Combine letters into one string
    for letter in cyphered_word:
        final_cyphered_word += letter
    # Print encrypted result
    print(final_cyphered_word)


# Define a function to decipher/decrypt text
def decypher_code(word_to_decypher):
    # Create empty list for decrypted letters
    decyphered_word = []
    # Ask user for shift amount
    amount_of_shifts = int(input("Amount of shift: "))
    # Loop through every letter in encrypted word
    for letter in word_to_decypher:
        # Find shifted index
        index_shift = alphabet.index(letter) - amount_of_shifts
        # Print shifted index before adjustment
        print(index_shift)
        # Adjust index if it goes below alphabet range
        while index_shift <= 0:
            index_shift += 1
            index_shift += 25
        # Print adjusted index
        print(index_shift)
        # Add shifted letter to decrypted list
        decyphered_word.append(alphabet[index_shift])
    # Create empty string for final decrypted word
    final_decyphered_word = ''
    # Combine letters into one string
    for letter in decyphered_word:
        final_decyphered_word += letter
    # Print decrypted result
    print(final_decyphered_word)


# Define main function
def main():
    # Show introduction
    intro_to_program()
    # Display menu
    print_menu()
    # Ask user for menu choice
    menu_selection(choice=int(input("Choice: ")))


# Run the program
main()
