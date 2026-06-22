# Name: Ryan Pereira 
# Project Name: Weather Tracker Project
# Description: A command-line weather application that allows users to retrieve current weather and a five-day forecast using the OpenWeather API.
# Module Name: weather_tracker_brain.py
# Module Purpose: Handles user interaction, program flow, and connects the UI logic with the weather data retrieval functions.
# Collaborators: None
# Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation.
# Date: 6/15/2026
# Last Modified: 6/18/2026


#Imports
from weather_tracker_requests import get_weather_for_today_info, get_weather_for_five_days_info
from weather_tracker_art import *


class WeatherTrackerBrain:
    """
    The WeatherTrackerBrain class manages the user interface and program flow
    for the Weather Tracker application. It connects user inputs to weather
    data retrieval functions and displays results in a structured format.
    """

    def display_welcome_message(self):
        """
        Displays a welcome message and program title to the user when the program starts.
        """
        print(title_display)
        print("\nWELCOME TO THE WEATHER FORECAST TRACKER")
        print("PLEASE FOLLOW DIRECTIONS TO USE PROGRAM")

    def display_goodbye_message(self):
        """
        Displays a goodbye message when the user exits the program.
        """
        print("\nTHANK YOU SO MUCH FOR USING THIS PROGRAM!")
        print("GOODBYE!")

    def display_menu(self):
        """
        Displays the main menu options for the Weather Tracker program.
        Allows the user to choose between current weather, 5-day forecast, or exit.
        """
        print("\n1. DISPLAY CURRENT WEATHER")
        print("2. DISPLAY FIVE DAY FORECAST")
        print("3. EXIT")

    def get_current_weather(self, city, state, country_code):
        """
        Retrieves the current weather data for a given location.

        Parameters:
            city (str): Name of the city
            state (str): State abbreviation or name
            country_code (str): Country code (e.g., US)

        Returns:
            PrettyTable: Formatted table containing current weather information
        """
        return get_weather_for_today_info(city, state, country_code)

    def get_five_day_forecast(self, city, state, country_code):
        """
        Retrieves the 5-day weather forecast for a given location.

        Parameters:
            city (str): Name of the city
            state (str): State abbreviation or name
            country_code (str): Country code (e.g., US)

        Returns:
            dict: Dictionary of PrettyTable objects keyed by forecast date
        """
        return get_weather_for_five_days_info(city, state, country_code)

    def play_program(self):
        """
        Runs the main program loop.
        Displays the menu, processes user input, and calls the appropriate
        weather functions until the user chooses to exit.
        """
        while True:
            self.display_menu()
            user_menu_choice = input("\nPLEASE INPUT CHOICE: ")

            if user_menu_choice == "1":
                print("Please fill out at least one of the fields:\n")
                user_city_input = input("City: ")
                user_state_input = input("State: ")
                user_country_code = input("Country Code: ")

                current_weather_data_table = self.get_current_weather(
                    user_city_input, user_state_input, user_country_code
                )

                print(current_weather_data_table)
                print(divider_display, "\n")

            elif user_menu_choice == "2":
                print("Please fill out at least one of the fields:\n")
                user_city_input = input("City: ")
                user_state_input = input("State: ")
                user_country_code = input("Country Code: ")

                five_day_forecast_data_tables = self.get_five_day_forecast(
                    user_city_input, user_state_input, user_country_code
                )

                for forecast_table in five_day_forecast_data_tables.values():
                    print(forecast_table)

                print(divider_display, "\n")

            elif user_menu_choice == "3":
                break

            else:
                print("PLEASE INPUT A VALID CHOICE")
                print(divider_display, "\n")

    def run(self):
        """
        Starts the Weather Tracker program by displaying the welcome message,
        running the main program loop, and then displaying the goodbye message.
        """
        self.display_welcome_message()
        self.play_program()
        self.display_goodbye_message()