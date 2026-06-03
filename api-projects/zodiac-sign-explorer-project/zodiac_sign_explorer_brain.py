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
        pass



    def find_zodiac_sign(self,birthday_date):
        pass



    def zodiac_sign_compatibility(self):
        pass







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

test.list_all_zodiac_signs()