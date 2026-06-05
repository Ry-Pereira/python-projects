#Name: Ryan Pereira
#Project Name: Zodiac Sign Explorer Project
#Description: A program that scrapes zodiac sign data from a website and displays it to the user in a user-friendly way. The program allows the user to view information about different zodiac signs, including their birthday ranges, personality traits, and compatibility.
#Collaborators: None
#Module Name: zodiac_sign_explorer_brain.py
#Module Purpose: This program serves as the user interface for the Zodiac Sign Explorer application. It defines the main function, which creates an instance of the ZodiacSignExplorerBrain class and starts the program. The program displays a menu to the user and allows them to select different options to view zodiac sign information.
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 6/1/2026
#Last Modified: 6/4/2026





#From zodiac_sign_art module, importing everything.
from zodiac_sign_art import *
#From zodiac_sign_requests module, importing everything.
from zodiac_sign_requests import *




# Main class that manages the Zodiac Sign Explorer application.
class ZodiacSignExplorerBrain:

    # Displays the welcome message shown when the program starts.
    def display_welcome_messaege(self):
        print("\nWelcome to the Zodiac Sign Explorer!")
        print("Discover the traits and characteristics of your zodiac sign.")




    # Displays the application's menu options.
    def display_menu(self):
        print("\nZodiac Explorer Menu:")
        print("1. List all Zodiac Signs")
        print("2. Get Zodiac Sign Details")
        print("3. Find your Zodiac Sign")
        print("4. Zodiac Sign Compatibility")
        print("5. Exit")



    # Displays a goodbye message when the program exits.
    def display_goodbye_message(self):
        print("\nThank you for using the Zodiac Sign Explorer. Goodbye!")




    # Displays all zodiac signs along with their titles and ASCII art.
    def list_all_zodiac_signs(self):
        # Retrieve all zodiac signs from the website.
        zodiac_signs = get_all_zodiac_signs()
        print("\nZodiac Signs:")
        # Display information for each zodiac sign.
        for sign in zodiac_signs:
            print("Sign: ", sign.text.strip())
            print("Title: ", zodiac_signs_display_dictionary[sign.text]["title"])
            print("Zodiac Symbol: ", zodiac_signs_display_dictionary[sign.text]["ascii_art"])




    # Verifies that a zodiac sign entered by the user exists.
    def verify_zodiac_sign(self, zodiac_sign_to_verify):
        # Retrieve all zodiac signs.
        zodiac_signs = get_all_zodiac_signs()
        # Check whether the user's zodiac sign exists.
        for zodiac_sign in zodiac_signs:
            if zodiac_sign.text.strip() == zodiac_sign_to_verify:
                return True
        # Return False if no match is found.
        return False




    # Retrieves and displays detailed information about a zodiac sign.
    def get_zodiac_sign_details(self, user_zodiac_sign):
        # Validate the zodiac sign entered by the user.
        if self.verify_zodiac_sign(user_zodiac_sign) == False:
            print("Please input a valid Zodiac Sign")
            return
        # Retrieve zodiac sign details.
        zodiac_sign_details = get_zodiac_sign_information(user_zodiac_sign)
        print("\nGeneral Information:")
        # Display general zodiac sign information.
        for general_zodiac_sign_info_detail in zodiac_sign_details["general_details"]:
            print(general_zodiac_sign_info_detail + ":" + zodiac_sign_details["general_details"][general_zodiac_sign_info_detail])
        print("\nPersonal Information:")

        # Display zodiac sign personality traits.
        for personal_zodiac_sign_info_detail in zodiac_sign_details["personal_traits"]:
            print(personal_zodiac_sign_info_detail + ":" + zodiac_sign_details["personal_traits"][personal_zodiac_sign_info_detail])




    # Determines a user's zodiac sign from their birth date.
def find_zodiac_sign(self, birthday_date):
    try:
        # Convert the user-entered date string into a datetime object.
        valid_date = datetime.strptime(birthday_date, "%Y-%m-%d")
        # Check if the birth month is December.
        if valid_date.month == 12:
            # Create a new date in January of the following year.
            next_date = valid_date.replace(year=valid_date.year + 1, month=1)
        else:
            # Create a new date with the month increased by one.
            next_date = valid_date.replace(month=valid_date.month + 1)
        # Convert the birth month into its full month name.
        month = valid_date.strftime("%B")
        # Extract the day portion of the birth date.
        day = str(valid_date.day)
        # Convert the next month's date into its full month name.
        next_month = next_date.strftime("%B")
        # Extract the day portion of the next month's date.
        next_day = str(next_date.day)
        # Retrieve all zodiac sign birthday ranges.
        birthday_ranges = get_zodiac_sign_birthday_ranges()
        # Loop through each zodiac sign and its birthday range.
        for zodiac_sign in birthday_ranges:
            # Check whether the birth date falls within the zodiac sign's range.
            if ((birthday_ranges[zodiac_sign][0][0] == month and birthday_ranges[zodiac_sign][0][1] >= day) or (birthday_ranges[zodiac_sign][1][0] == next_month and birthday_ranges[zodiac_sign][0][1] <= next_day)):
                # Display the matching zodiac sign.
                print("Your Zodiac Sign is: ", zodiac_sign)
    # Handle invalid date formats entered by the user.
    except ValueError:
        # Return an error message explaining the required format.
        return "Invalid date format. Please enter a date in the format YYYY-MM-DD."




    # Displays zodiac signs that are most compatible with the user's sign.
    def zodiac_sign_compatibility(self, user_zodiac_sign):
        # Validate the zodiac sign entered by the user.
        if self.verify_zodiac_sign(user_zodiac_sign) == False:
            print("Please input a valid Zodiac Sign")
            return
        # Retrieve compatible zodiac signs.
        compatable_zodiac_signs = get_zodiac_sign_compatibility(user_zodiac_sign)
        # Display compatible zodiac signs.
        print("\nYour Compatible Signs: " + (",").join(compatable_zodiac_signs))




    # Main application loop.
    def run(self):
        # Display the application title banner.
        print(zodiac_sign_title_display)
        # Display the welcome message.
        self.display_welcome_messaege()
        # Continue running until the user chooses to exit.
        while True:
            # Display the menu.
            self.display_menu()
            # Prompt the user for a menu choice.
            user_choice = input("Please enter your choice from the menu (1-5): ")
            # List all zodiac signs.
            if user_choice == "1":
                self.list_all_zodiac_signs()
            # Display zodiac sign details.
            elif user_choice == "2":
                zodiac_sign_to_get_details = input("\nZodiac Sign To Get Info Details: ")
                self.get_zodiac_sign_details(zodiac_sign_to_get_details)
            # Find a zodiac sign from a birth date.
            elif user_choice == "3":
                birthday_to_find_zodiac_sign = input("\nGive your Birthday Date-YYYY-MM-DD To Find Your Zodiac Sign: ")
                self.find_zodiac_sign(birthday_to_find_zodiac_sign)
            # Display zodiac sign compatibility.
            elif user_choice == "4":
                zodiac_sign_to_get_compatability_info = input("\nZodiac Sign To Check Compatibility: ")
                self.zodiac_sign_compatibility(zodiac_sign_to_get_compatability_info)
            # Exit the application.
            elif user_choice == "5":
                break
            # Handle invalid menu selections.
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
            # Display a divider after each operation.
            print(zodiac_sign_divider_display)
        # Display the goodbye message.
        self.display_goodbye_message()

