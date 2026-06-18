#Name: Ryan Pereira 
#Project Name: Weather Tracker Project
#Description:
#Module Name: main.py
#Module Purpose: The main module is the main entry point into entire project. It instnaces a WeatherTrackerBrain class object in order to handle all program and user interactions from now on.
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation.
#Date: 6/15/2026
#Last Modified: 6/18/2026




#From the weather_tracker_brain module, importing the WeatherTrackerBrain class.
from weather_tracker_brain import WeatherTrackerBrain



#Defining a main function, the main entry point into project program.
def main():
  #weather_tracker_program is set to the instant object of the WeatherTrackerBrain.
  weather_tracker_program = WeatherTrackerBrain()
  #Executing the run method of the weather_tracker_program, as all user and program interaction happens in this class object.
  weather_tracker_program.run()



#If this program is being run directly, then the following code will be executed.
if __name__ == "__main__":
  #The main function is called and executed.
  main()
