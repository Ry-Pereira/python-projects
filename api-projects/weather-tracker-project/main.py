# Name: Ryan Pereira 
# Project Name: Weather Tracker Project
# Description: Entry point of the Weather Tracker application. This module initializes the WeatherTrackerBrain class and starts the program execution loop.
# Module Name: main.py
# Module Purpose: Serves as the entry point of the application and delegates control to the WeatherTrackerBrain class, which manages all user interaction and program logic.
# Collaborators: None
# Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation.
# Date: 6/15/2026
# Last Modified: 6/18/2026


from weather_tracker_brain import WeatherTrackerBrain


def main():
    """
    Main entry point of the Weather Tracker program.

    This function creates an instance of WeatherTrackerBrain and
    starts the application by calling its run() method.
    """
    weather_tracker_program = WeatherTrackerBrain()
    weather_tracker_program.run()


if __name__ == "__main__":
    main()