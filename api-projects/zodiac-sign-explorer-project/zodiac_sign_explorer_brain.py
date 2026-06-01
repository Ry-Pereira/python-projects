















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




    def run(self):
        self.display_welcome_message()
        self.display_menu()
        self.display_goodbye_message()