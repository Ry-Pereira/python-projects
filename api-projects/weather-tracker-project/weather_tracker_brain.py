#Name: Ryan Pereira 
#Project Name: Weather Tracker Project
#Description:
#Module Name: weather_tracker_brain.py
#Module Purpose:
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation.
#Date: 6/15/2026
#Last Modified: 6/18/2026

from weather_tracker_requests import get_weather_for_today_info,get_weather_for_five_days_info
from weather_tracker_art import *

#Defining a class for WeatherTrackerBrain
class WeatherTrackerBrain:

    def display_welcome_message(self):
        """Defining a display_welcome_message function. The purpose of the this function is to provide a welcome message to the user."""
        print(title_display)
        print("\nWELCOME TO THE WEATHER FOREACAST TRACKER")
        print("PLEASE FOLLOW DIRECTIONS TO USE PROGRAM")


    def display_goodbye_message(self):
        """Defining a display_goodbye_message function. The purpose of the this function is to provide a goodbye message to the user."""
        print("\nTHANKYOU SO MUCH FOR USING PROGRAM!")
        print("GOODBYE!")


    def display_menu(self):
        """Defining a display_menu function. The purpose of this is to print out a menu with options, and corresponding executed functions based on thos options."""
        print("\n1.DISPLAY CURRENT WEATHER")
        print("2.DISPLAY FIVE DAY FORECAST")
        print("3.EXIT")


    def get_current_weather(self):
        return get_weather_for_today_info()


    def get_five_day_forecast(self):
        return get_weather_for_five_days_info()

 



    def play_program(self):
        while(True):
            self.display_menu()
            user_menu_choice = input("\nPLEASE INPUT CHOICE: ")
            if user_menu_choice == "1":
                current_weather_data_table = self.get_current_weather()
                print(current_weather_data_table)
                print(divider_display,"\n")
            elif user_menu_choice == "2":
                five_day_forecast_data_tables = self.get_five_day_forecast()
                for forecast_table in five_day_forecast_data_tables.values():
                    print(forecast_table)
                print(divider_display,"\n")
            elif user_menu_choice == "3":
                break
            else:
                print("PLEASE INPUT A VALID CHOICE")
                print(divider_display,"\n")


            






    def run(self):
        self.display_welcome_message()
        self.play_program()
        self.display_goodbye_message()
        
