#Name: Ryan Pereira
#Project Name: Zodiac Sign Explorer Project
#Description: A program that scrapes zodiac sign data from a website and displays it to the user in a user-friendly way. The program allows the user to view information about different zodiac signs, including their birthday ranges, personality traits, and compatibility.
#Collaborators: None
#Module Name: zodiac_sign_explorer_brain.py
#Module Purpose: This program serves as the user interface for the Zodiac Sign Explorer application. It defines the main function, which creates an instance of the ZodiacSignExplorerBrain class and starts the program. The program displays a menu to the user and allows them to select different options to view zodiac sign information.
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 6/1/2026
#Last Modified: 6/4/2026












from zodiac_sign_art import *
from zodiac_sign_requests import *














class ZodiacSignExplorerBrain:
    

    def display_welcome_messaege(self):
        print("Welcome to the Zodiac Sign Explorer!")
        print("Discover the traits and characteristics of your zodiac sign.")

    def display_menu(self):
        print("\nZodiac Explorer Menu:")
        print("1. List all Zodiac Signs")
        print("2. Get Zodiac Sign Details")
        print("3. Find your Zodiac Sign")
        print("4. Zodiac Sign Compatibility")
        print("5. Exit")




    def display_goodbye_message(self):
        print("\nThank you for using the Zodiac Sign Explorer. Goodbye!")




    def list_all_zodiac_signs(self):
        zodiac_signs = get_all_zodiac_signs()
        print("\nZodiac Signs:")
        for sign in zodiac_signs:
            print("Sign: ",sign.text.strip())
            print("Title: ",zodiac_signs_display_dictionary[sign.text]["title"])
            print("Zodiac Symbol: ",zodiac_signs_display_dictionary[sign.text]["ascii_art"])
    



    def get_zodiac_sign_details(self,zodiac_sign):
        zodiac_sign_details = get_zodiac_sign_details(zodiac_sign)
        print("\nGeneral Information:")
        for general_zodiac_sign_info_detail in zodiac_sign_details["general_details"]:
            print(general_zodiac_sign_info_detail + ":" + zodiac_sign_details["general_details"][general_zodiac_sign_info_detail])

        print("\nPersonal Information:")
        for personal_zodiac_sign_info_detail in zodiac_sign_details["personal_traits"]:
            print(personal_zodiac_sign_info_detail + ":" + zodiac_sign_details["personal_traits"][personal_zodiac_sign_info_detail])
        



    def find_zodiac_sign(self,birthday_date):
        try:
            # Convert the string entered by the user into a datetime object.
            valid_date = datetime.strptime(birthday_date, "%Y-%m-%d")
            # Retrieve and return moon phase information for the validated date.
            month = valid_date.strftime("%B")  
            day = str(valid_date.day)   
            birthday_ranges = get_zodiac_sign_birthday_ranges()
            for zodiac_sign in birthday_ranges:
                if (birthday_ranges[zodiac_sign][0][0] == month and birthday_ranges[zodiac_sign][0][1] >= day) or (birthday_ranges[zodiac_sign][1][0] == month and birthday_ranges[zodiac_sign][1][1] <= day):
                    print("Your Zodiac Sign is: ",zodiac_sign)



        # If the date format is invalid, handle the error gracefully.
        except ValueError:
            # Return an error message explaining the required format.
            return "Invalid date format. Please enter a date in the format YYYY-MM-DD."



    def zodiac_sign_compatibility(self,zodiac_sign):
        compatable_zodiac_signs = get_zodiac_sign_compatibility(zodiac_sign)
        print("\nYour Compatible Signs:")
        print(compatable_zodiac_signs)







    def run(self):
        print(zodiac_sign_title_display)
        self.display_welcome_messaege()
        while True:
            self.display_menu()
            user_choice = input("Please enter your choice from the menu (1-5): ")
            if user_choice == "1":
                self.list_all_zodiac_signs()
            elif user_choice == "2":
                self.get_zodiac_sign_details()
            elif user_choice == "3":
                self.find_zodiac_sign()
            elif user_choice == "4":
                self.zodiac_sign_compatibility()
            elif user_choice == "5":
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

        self.display_menu()
        self.display_goodbye_message()


test = ZodiacSignExplorerBrain()

test.find_zodiac_sign("2026-02-18")