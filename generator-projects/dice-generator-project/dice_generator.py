#Name: Ryan Pereira
#Project Name: Dice Generator Program
#Module Name: Main
#Module Purpose: This module serves as the main entry point for the Dice Generator Program. It is responsible for introducing the user to the program, displaying the menu options, handling menu selections, generating random or user-selected numbered dice, and simulating dice rolls.
#Description: The program allows users to generate and roll different types of numbered dice. Users can either generate a random sided dice or choose the number of sides for the dice manually. The program then simulates rolling the dice and displays the results to the user through a simple menu-driven interface.
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 9/12/2024
#Last Modified: 9/13/2024



# Importing the random module to allow random number generation for dice creation and rolling
import random

# The function introduces the user to the program
def intro_to_program():
    # Printing a welcome message to introduce the user to the Dice Generator Program
    print("Welcome To The DICE GENERATOR PROGRAM\n\n")



# This function prints the menu to the screen
def print_menu():
    # Printing menu option 1 for generating a random numbered dice
    print("1) Generate a random numbered dice ")
    # Printing menu option 2 for choosing a numbered dice manually
    print("2) Choose a numbered dice")
    # Printing menu option 3 for exiting the program
    print("3) Exit Program\n\n")



# This function does the menu selection
def menu_choice(choice):
    # Checking if the user's choice is equal to 1
    if choice == 1:
        # Calling the roll function and passing in a randomly generated numbered dice
        roll(generate_random_numbered_dice())
    # Checking if the user's choice is equal to 2
    elif choice == 2:
        # Calling the roll function and passing in a user selected numbered dice
        roll(choosing_numbered_dice())
    # Checking if the user's choice is equal to 3
    elif choice ==3:
        # Printing a message indicating the program has exited
        print("Program Exited")
        # Printing a thank you message to the user
        print("Thankyou for Using")
    # Else statement for invalid menu choices
    else:
        # Printing a message informing the user to choose a valid option
        print("Choose a valid choice")
        # Calling the menu_choice function again recursively with a new user input
        menu_choice(choice = int(input("Choice: ")))



# This function generates a random number from the dice_values
def roll(dice_values):
    # Pass keyword placeholder until rolling functionality is implemented
    pass


        


# This function generates a randomly generated numbered sided dice
def generate_random_numbered_dice():
    # Creating an empty list to store dice side values
    dice_values = []
    # Generating a random integer between 0 and 144 for the number of dice sides
    type_of_numbered_dice = random.radint(0,144):
    # Printing the number of sides the generated dice has
    print(f"You have a {type_of_numbered_dice} sided dice")
    # Asking the user if they want to generate another random dice
    generate_dice_again = input("Generate a new numbered dice(Y/N)")
    # Checking if the user entered Y
    if generate_dice_again == "Y":
        # Calling the function again recursively to generate another dice
        generate_random_numbered_dice()
    # Else statement if the user does not want another dice generated
    else:
        # Looping through all numbers from 0 up to the number of dice sides
        for number in range(0,type_of_numbered_dice + 1):
            # Appending each number into the dice values list
            dice_values.append(number)
        # Printing a message letting the user know the dice is ready
        print("Already get ready to roll that dice")
        # Returning the completed dice values list
        return dice_values




    
# This function generates a numbered sided dice based on user preference
def choosing_numbered_dice():
    # Creating an empty list to store dice side values
    dice_values = []
    # Asking the user how many sides the dice should have and converting input into an integer
    type_of_numbered_dice = int(input("How many sides should the dice have: "))
    # Printing the number of sides the chosen dice has
    print(f"You have a {type_of_numbered_dice} sided dice")
    # Looping through all numbers from 0 up to the number of dice sides
    for number in range(0,type_of_numbered_dice + 1):
        # Appending each number into the dice values list
        dice_values.append(number)
    # Printing a message letting the user know the dice is ready
    print("Already get ready to roll that dice")
    # Returning the completed dice values list
    return dice_values
    






# This the main function of the program.
def main():
    # Calling the introduction function to welcome the user
    intro_to_program()
    # Calling the print menu function to display the menu options
    print_menu()
    # Calling the menu_choice function with the user's menu selection
    menu_choice(choice = int(input("Choice: ")))





# Main function is called
main()
