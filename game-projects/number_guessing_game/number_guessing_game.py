# Name: Ryan Pereira
# Project Name: Number Guessing Game
# Description: A Python-based number guessing game where the player tries to guess a randomly selected number within a chosen range, with either limited or unlimited lives depending on user input.
# Module Name: number_guessing_game
# Module Purpose: This module runs a command-line game that generates a random number, prompts the user for guesses, provides feedback (too high/too low), and tracks win/loss conditions based on remaining lives or unlimited attempts.
# Collaborators: None
# Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
# Date: 7/11/2023
# Last Modified: 7/12/2023


# Import the random module to allow random number selection
import random
# Create an empty list that will store possible numbers for guessing
number_list = []


# Main function that runs the Number Guessing Game
def main():
    # Display welcome message
    print("Welcome to the Number Guessing Game\n")
    # Ask the user for the upper limit of the number range
    range_indicate = int(input("From 0 to what number shall you guess the secret number"))
    # Ask the user if they want limited or unlimited lives
    want_lives = input("Do you want to have unlimited lives or limited lives (y/n)")
    # Fill the number list with values from 0 up to the selected range
    for number in range(0,range_indicate):
        # Add each number into the list
        number_list.append(number)
    # Randomly select the secret number from the list
    selected_number = random.choice(number_list)
    # Print the selected number (debug/testing purpose)
    print("Slected number: ", str(selected_number))
    # Track whether the player has won
    player_won = False
    # Check if the player wants limited lives
    if want_lives == "y":
        # Ask the user how many lives they want
        lives_amount = int(input("How many lives do you want: "))
        # Get the first guess from the player
        guess = int(input("Guess: "))
        # Loop until the player runs out of lives
        while lives_amount != 0:
            # Print remaining lives
            print(lives_amount)
            # Check if guess is too high
            if guess > selected_number:
                # Player has not won yet
                player_won = False
                # Inform player guess is too big
                print("Guess is too big")
                # Reduce lives by 1
                lives_amount -=1
                # Ask for another guess
                guess = int(input("Guess: "))
            # Check if guess is too low
            if guess < selected_number:
                # Player has not won yet
                player_won = False
                # Inform player guess is too small
                print("Guess is too small")
                # Reduce lives by 1
                lives_amount -=1
                # Ask for another guess
                guess = int(input("Guess: "))
            # Check if the guess is correct
            if guess == selected_number:
                # Inform player they are correct
                print("Correct")
                # Mark player as winner
                player_won = True
                # End the game loop by setting lives to 0
                lives_amount == 0
    # If player chose unlimited lives mode
    else:
        # Assume player will eventually win unless proven otherwise
        player_won = True
        # Get first guess
        guess = int(input("Guess: "))
        # Keep looping until correct number is guessed
        while guess != selected_number:
            # If guess is too high
            if guess > selected_number:
                # Tell player guess is too big
                print("Guess is too big")
            # If guess is too low
            else :
                # Tell player guess is too small
                print("Guess is too small")
            # Ask for another guess
            guess = int(input("Guess: "))
    # Check if player has won the game
    if player_won == True:
        # Print win message
        print("Player has won")
    # If player did not win
    else:
        # Print lose message
        print("Player has lost")


# Call the main function to start the program
main()
