







class MoonTrackerBrain:
    def __init__(self):
        pass

    def display_menu(self):
        print("\nPlease select an option:")
        print("1. View today's moon phase")
        print("2. View moon phases for the week")
        print("3. Look Up a specific date")
        print("4. Exit\n")


    def get_moon_phase_for_today(self):
        # Placeholder for actual moon phase calculation
        return "" 
    

    def get_moon_phases_for_week(self):
        # Placeholder for actual moon phase calculation
        return []
    

    def get_moon_phase_for_date(self, date):
        # Placeholder for actual moon phase calculation
        return ""

    def run(self):
        self.display_menu()
        while True:
            user_choice = input("Enter your choice (1-4): ")
            if user_choice == "1":
                moon_phase = self.get_moon_phase_for_today()
            elif user_choice == "2":
                moon_phases = self.get_moon_phases_for_week()
            elif user_choice == "3":
                date = input("Enter a date (YYYY-MM-DD): ")
                moon_phase = self.get_moon_phase_for_date(date)
            elif user_choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")