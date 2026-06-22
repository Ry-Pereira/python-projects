#Name: Ryan Pereira 
#Project Name: Weather Tracker Project
#Description:
#Module Name: weather_tracker_requests.py
#Module Purpose:
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation.
#Date: 6/15/2026
#Last Modified: 6/18/2026








from requests import *
import requests

from datetime import date, timedelta
from prettytable import PrettyTable







api_key = ""



def get_lat_and_lat_coordinates_info(city_name,state):
    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state},US&limit=1&appid={api_key}"
    geo_response = requests.get(geo_url)
    data = geo_response.json()
    return [data[0]["lat"],data[0]["lon"]]




def get_weather_for_today_info():
    lat,lon = get_lat_and_lat_coordinates_info()
    current_weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    current_weather_response = requests.get(current_weather_url)
    current_weather_data = current_weather_response.json()
    date = date.today()
    current_weather_data_table = PrettyTable()
    current_weather_data_table.title = date
    current_weather_data_table.field_names = ["Temperature","Temperature Min","Temperature Max","Pressure","Humidity","Weather","Weather Description"]
    current_weather_data_table.add_row([current_weather_data["main"]["temp"],current_weather_data["main"]["temp_min"],current_weather_data["main"]["temp_max"],current_weather_data["main"]["pressure"],current_weather_data["main"]["humidity"],current_weather_data["weather"][0]["main"],current_weather_data["weather"][0]["description"]])
    return current_weather_data





def get_weather_for_five_days_info():
    lat,lon = get_lat_and_lat_coordinates_info("Lenexa","Kansas")
    five_day_forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}"
    five_day_forecast_response = requests.get(five_day_forecast_url)
    five_day_forecast_data = five_day_forecast_response.json()
    five_day_forecast_data_tables = {}
    for forecast_day in five_day_forecast_data["list"]:
        forecast_date = forecast_day["dt_txt"].split(" ")[0]
        forecast_time = forecast_day["dt_txt"].split(" ")[1]
        if forecast_date not in five_day_forecast_data_tables :
            five_day_forecast_data_tables[forecast_date] = PrettyTable()
            five_day_forecast_data_tables[forecast_date].title = forecast_date
            five_day_forecast_data_tables[forecast_date].field_names = ["Time","Temperature","Temperature Min","Temperature Max","Pressure","Humidity","Weather","Weather Description"]
        five_day_forecast_data_tables[forecast_date].add_row([forecast_time,forecast_day["main"]["temp"],forecast_day["main"]["temp_min"],forecast_day["main"]["temp_max"],forecast_day["main"]["pressure"],forecast_day["main"]["humidity"],forecast_day["weather"][0]["main"],forecast_day["weather"][0]["description"]])
    return five_day_forecast_data_tables

