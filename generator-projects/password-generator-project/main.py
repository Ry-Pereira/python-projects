#Name: Ryan Pereira
#Project Name: Password Generator Program
#Module Name: Main
#Module Purpose: This module serves as the main entry point for the Password Generator Program. It is responsible for displaying the menu, collecting user input, generating randomized passwords using numbers, letters, and special characters, and allowing users to regenerate passwords if desired.
#Description: The program generates customizable passwords based on the number of letters, numbers, and special characters selected by the user. The generated password is randomized to improve password security and uniqueness. The application runs through a command-line interface and uses Python's random module for random selection functionality.
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 8/3/2024
#Last Modified: 8/4/2024



# Importing the random module to allow random selections and password generation
import random

# Creating a list of number characters as strings to use in password generation
number_list = ["1","2","3","4","5","6","7","8","9","0"]

# Creating a list of uppercase and lowercase alphabet letters to use in password generation
letter_list = ["A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k",
                "L","l","M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","v",
                "W","w","X","x","Y","y","Z","z"]

# Creating a list of special characters to use in password generation
special_characters_list = ["!","@","#","$","%","^","&","*","<","(",")","<",">","?"]


# Defining the generate_password function with parameters for numbers, letters, and special characters
def generate_password(number_of_numbers,number_of_letters,number_of_special_characters):
    # Printing stage message for debugging purposes
    print("Stage 1")
    # Creating an empty list to temporarily store password characters
    password_heap = []
    # Creating an empty string to store the final generated password
    generated_password = ""
    # Initializing a counter variable for loops
    amount_counter = 0
    # Printing another debugging message
    print("Stage 2: Varibles are good")

    # While loop runs until the desired number of numbers are added
    while amount_counter != number_of_numbers:
        # Selecting a random number from the number list
        v = random.choice(number_list)
        # Printing the selected random number
        print(v)
        # Adding the selected number into the password heap list
        password_heap.append(v)
        # Printing the current password heap contents
        print(password_heap)
        
        # Incrementing the counter variable
        amount_counter +=1

    # Resetting the counter variable back to 0
    amount_counter = 0

    # While loop runs until the desired number of letters are added
    while amount_counter != number_of_letters:
        # Appending a randomly selected letter into the password heap
        password_heap.append(random.choice(letter_list))
        
        # Incrementing the counter variable
        amount_counter +=1

    # Resetting the counter variable back to 0
    amount_counter = 0

    # While loop runs until the desired number of special characters are added
    while amount_counter != number_of_special_characters:
        # Appending a randomly selected special character into the password heap
        password_heap.append(random.choice(special_characters_list))
       
        # Incrementing the counter variable
        amount_counter +=1

        
    # Printing the full password heap before shuffling
    print(password_heap)

    # While loop runs while there are still characters inside the password heap
    while len(password_heap):
        # Selecting a random item from the password heap
        random_heap_item = random.choice(password_heap)
        # Adding the randomly selected item into the generated password string
        generated_password +=  random_heap_item
        # Removing the selected item from the password heap
        password_heap.remove( random_heap_item)

        
    # Printing debugging message after loops complete
    print("Stage3: we got ouf while loops")

    # Printing the final generated password
    print("Your generated password will be:",generated_password)

    # Asking the user if they are satisfied with the generated password
    is_password_good = input("Do you want to generate a new password(y/n)")

    # Checking if the user entered y
    if is_password_good == "y":
        # Printing a message confirming the generated password
        print("ALrighty, have a good day with your new password",generated_password)

    # Checking if the user entered n
    elif is_password_good == "n":
        # Calling the generate_password function again with new user inputs
        generate_password(number_of_numbers = int(input("How many numbers do you want to put in the password: "))
                      ,number_of_letters = int(input("How many letters do you want to put in the password: ")),
                      number_of_special_characters = int(input("How many special characters do you want to put in the password: ")))
    


# Defining the print_menu function
def print_menu():
    # Printing menu option 1 for generating a password
    print("Press 1: To generate a random password\n")
    # Printing menu option 2 for future password strength checker functionality
    print("Press 2: Check to see if password if strong- Feature to be coming soon\n")


    
# Defining the main function of the program
def main():
    # Printing a welcome message to the user
    print("Welcome to the Password Generator Program")
    # Calling the print_menu function to display menu options
    print_menu()
    # Calling the generate_password function with user inputs
    generate_password(number_of_numbers = int(input("How many numbers do you want to put in the password: "))
                      ,number_of_letters = int(input("How many letters do you want to put in the password: ")),
                      number_of_special_characters = int(input("How many special characters do you want to put in the password: ")))


# Calling the main function to start the program
main()
