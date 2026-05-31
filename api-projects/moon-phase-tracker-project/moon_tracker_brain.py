#Name: Ryan Pereira
#Project Name: Moon Phase Tracker Project
#Description: A program that scrapes moon phase data from a website and displays it to the user in a user-friendly way. The program allows the user to view the current moon phase, the moon phases for the current week, the moon phases for the next week, and the moon phase for a specific date. The program also includes ASCII art representations of each moon phase.
#Collaborators: None
#Module Name: moon_tracker_brain.py
#Module Purpose: This module contains the main logic of the Moon Phase Tracker application. It defines the MoonTrackerBrain class, which includes methods for displaying the menu, retrieving moon phase information for different time periods, and displaying the moon phase information to the user. The run method serves as the main loop of the program, allowing the user to interact with the menu and view moon phase information based on their selections.
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 5/28/2026
#Last Modified: 5/30/2026





#From the datetime library, import the date, datetime, and timedelta classes. These are used to work with dates and times in the program, allowing for calculations of moon phases based on specific dates and time periods.
from datetime import date, datetime, timedelta, timedelta
#From the moon_phase_requests module, import the get_moon_phase function. This function is used to retrieve moon phase information from the moongiant.com website for specific dates, which is then displayed to the user in the Moon Phase Tracker application.
from moon_phase_requests import get_moon_phase
#From the art module, import everything. This is where the ASCII art is stored, which is used to display visual representations of the moon phases to the user in a user-friendly way.
from moon_phase_art import *




#Defined a MoonTrackerBrain class that contains methods for displaying the menu, retrieving moon phase information for different time periods, and displaying the moon phase information to the user. The run method serves as the main loop of the program, allowing the user to interact with the menu and view moon phase information based on their selections.
class MoonTrackerBrain:
    #Defined a display_menu method that prints the menu options to the user. This method is called at the beginning of the run method to display the menu when the program starts, and it can also be called again if the user wants to view the menu options after making a selection.
    def display_menu(self):
        #Print the menu options to the user, allowing them to select different options to view moon phase information for today, the current week, the next week, or a specific date. The user can also choose to exit the program.
        print("\nPlease select an option:")
        print("1. View today's moon phase")
        print("2. View moon phases for the week")
        print("3. View moon phases for the next week")
        print("4. Look Up a specific date")
        print("5. Exit\n")





    #Defined a get_moon_phase_for_today method that retrieves the moon phase information for the current date. This method uses the get_moon_phase function from the moon_phase_requests module to retrieve the moon phase data for today's date, which is then returned as a dictionary containing all the relevant moon phase information.
    def get_moon_phase_for_today(self):
        #Returns the moon phase information for today's date by calling the get_moon_phase function with the current date as an argument. The get_moon_phase function retrieves the moon phase data from the moongiant.com website and returns it in a structured format, which can then be displayed to the user in a user-friendly way, including the ASCII art representations of each moon phase.
        return get_moon_phase(date.today())
    


    #Defined a get_moon_phases_for_week method that retrieves the moon phase information for each day of the current week. This method calculates the dates for the current week, retrieves the moon phase information for each date using the get_moon_phase function, and returns a list of tuples containing the date and corresponding moon phase information for each day of the week.
    def get_moon_phases_for_week(self):
        #Moon_phases_for_week list is initialized to store the moon phase information for each day of the current week. The monday variable is calculated by finding the date of the most recent Monday, and then a loop iterates through each day of the week (7 days) to calculate the current date and retrieve the moon phase information for that date using the get_moon_phase function. Each date and its corresponding moon phase information are stored as a tuple in the moon_phases_for_week list, which is then returned at the end of the method.
        moon_phases_for_week = []
        #Monday date is calculated and is the starting date of the week.
        monday_date = date.today() - timedelta(days=date.today().weekday())
        #Loops through the day index from range till 7, as to go through each day of the week.
        for day_index in range(7):
            #Calculates the current date with monday date andding the days of the day index to get to the next date, which is tomorrow.
            current_date = monday_date + timedelta(days=day_index)
            #Moon phase is set to the api infromaten retrieved from the get moon phase function with current date as input.
            moon_phase = get_moon_phase(current_date)
            #Moon phases for week list appends the current date and moon phase.
            moon_phases_for_week.append((current_date, moon_phase))
        #Returns the moon phases for week list.
        return moon_phases_for_week
    



     # Defined a get_moon_phases_for_next_week method that retrieves moon phase information for each day of the next calendar week. The method calculates the upcoming Monday, retrieves moon phase data for seven consecutive days, and returns the results as a list of tuples.
    def get_moon_phases_for_next_week(self):
        # Initialize an empty list to store moon phase data for each day of the next week.
        moon_phases_for_next_week = []
        # Calculate the date of the upcoming Monday.
        monday = date.today() + timedelta(days=(7 - date.today().weekday()))
        # Calculate the Monday after the upcoming Monday.
        next_monday = monday + timedelta(days=7)
        # Loop through each day of the next week.
        for day_index in range(7):
            # Calculate the current date by adding the loop index to the Monday date.
            current_date = monday + timedelta(days=day_index)
            # Retrieve moon phase information for the current date.
            moon_phase = get_moon_phase(current_date)
            # Store the date and moon phase data as a tuple.
            moon_phases_for_next_week.append((current_date, moon_phase))
        # Return the completed list of moon phase data.
        return moon_phases_for_next_week





    # Defined a get_moon_phase_for_date method that retrieves moon phase information for a user-specified date entered in YYYY-MM-DD format.
    def get_moon_phase_for_date(self, date):
        # Use a try block to validate the user's date input.
        try:
            # Convert the string entered by the user into a datetime object.
            valid_date = datetime.strptime(date, "%Y-%m-%d")
            # Retrieve and return moon phase information for the validated date.
            return get_moon_phase(valid_date)
        # If the date format is invalid, handle the error gracefully.
        except ValueError:
            # Return an error message explaining the required format.
            return "Invalid date format. Please enter a date in the format YYYY-MM-DD."
        



    # Defined a display_moon_phase method that displays moon phase information and the corresponding ASCII art representation to the user.
    def display_moon_phase(self, moon_phase):
        # Display the name of the moon phase.
        print(f"Moon phase: {moon_phase['moon_phase']}")
        # Display the ASCII art associated with the moon phase.
        print(moon_phases_image_display[moon_phase['moon_phase']])
        # Print a blank line for readability.
        print("\n")
        # Display additional moon phase details retrieved from the website.
        print("Illumination: " + moon_phase["illumination"] + "\nMoon Age: " + moon_phase["moon_age"] + " days" + "\nMoon Angle: " + moon_phase["moon_angle"] + "\nMoon Distance: " + moon_phase["moon_distance"] + " km" + "\nMoon-Sun Angle: " + moon_phase["moon_sun_angle"] + "\nMoon-Sun Distance: " + moon_phase["moon_sun_distance"] + " km")
        # Print a blank line for readability.
        print("\n")




     # Defined a run method that serves as the main program loop.
    def run(self):
        #Prints the moon phase tacker title art display for user.
        print(moon_phase_tracker_title_art_display)
        # Continue running until the user chooses to exit.
        while True:
            # Display the menu when the program starts.
            self.display_menu()
            # Prompt the user to select a menu option.
            user_choice = input("Enter your choice (1-5): ")
            # Option 1: Display today's moon phase.
            if user_choice == "1":
                # Retrieve today's moon phase information.
                moon_phase = self.get_moon_phase_for_today()
                # Display the moon phase information.
                self.display_moon_phase(moon_phase)
            # Option 2: Display moon phases for the current week.
            elif user_choice == "2":
                # Retrieve moon phase data for the current week.
                moon_phases = self.get_moon_phases_for_week()
                # Loop through each day and display its moon phase.
                for date, moon_phase in moon_phases:
                    #Print Date of the moon phase
                    print("Date: ",date)
                    #Calls the the display moon phase, taking the moon phase variable as input
                    self.display_moon_phase(moon_phase)
            # Option 3: Display moon phases for the next week.
            elif user_choice == "3":
                # Retrieve moon phase data for the next week.
                moon_phases = self.get_moon_phases_for_next_week()
                # Loop through each day and display its moon phase.
                for date, moon_phase in moon_phases:
                    #Print Date of the moon phase
                    print("Date: ",date)
                    #Calls the the display moon phase, taking the moon phase variable as input
                    self.display_moon_phase(moon_phase)
            # Option 4: Look up a moon phase for a specific date.
            elif user_choice == "4":
                # Prompt the user to enter a date.
                date = input("\nEnter a date (YYYY-MM-DD): ")
                # Retrieve moon phase information for the entered date.
                moon_phase = self.get_moon_phase_for_date(date)
                # Display the moon phase information.
                self.display_moon_phase(moon_phase)
            # Option 5: Exit the program.
            elif user_choice == "5":
                # Display a goodbye message.
                print("\nGoodbye!\n\n")
                #Prints the seperator.
                print(moon_phases_line_seperator_art_display + "\n\n")
                # Exit the loop and terminate the program.
                break
            # Handle invalid menu selections.
            else:
                # Inform the user that the input was invalid.
                print("Invalid choice. Please enter a number between 1 and 5.")
            #Prints the seperator.
            print("\n\n" + moon_phases_line_seperator_art_display + "\n\n")





