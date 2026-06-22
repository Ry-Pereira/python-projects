# Name: Ryan Pereira 
# Project Name: Weather Tracker Project
# Description: A module that handles all API requests to OpenWeather, including geolocation lookup, current weather retrieval, and 5-day forecast data processing.
# Module Name: weather_tracker_requests.py
# Module Purpose: Communicates with the OpenWeather API, converts user input into geographic coordinates, and returns structured weather data using PrettyTable.
# Collaborators: None
# Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation.
# Date: 6/15/2026
# Last Modified: 6/18/2026

#Imports
from requests import *
import requests
from datetime import date
from prettytable import PrettyTable


api_key = "YOUR_API_KEY_HERE"


def get_lat_and_lat_coordinates_info(city_name, state, country_code):
    """
    Converts a city/state/country input into geographic coordinates using the OpenWeather Geocoding API.

    Parameters:
        city_name (str): Name of the city
        state (str): State name or abbreviation
        country_code (str): Country code (e.g., US)

    Returns:
        list | None: A list containing [latitude, longitude] if found, otherwise None.
    """
    query_parts = []

    if city_name:
        query_parts.append(city_name)
    if state:
        query_parts.append(state)
    if country_code:
        query_parts.append(country_code)

    query_location = ",".join(query_parts)

    geo_url = (
        f"http://api.openweathermap.org/geo/1.0/direct"
        f"?q={query_location}&limit=1&appid={api_key}"
    )

    response = requests.get(geo_url)
    data = response.json()

    if not data:
        return None

    return [data[0]["lat"], data[0]["lon"]]


def get_weather_for_today_info(city_name, state, country_code):
    """
    Retrieves current weather data for a given location and formats it into a PrettyTable.

    Parameters:
        city_name (str): Name of the city
        state (str): State name or abbreviation
        country_code (str): Country code (e.g., US)

    Returns:
        PrettyTable: A formatted table containing current weather data.
    """
    coords = get_lat_and_lat_coordinates_info(city_name, state, country_code)

    if coords is None:
        return "Location not found."

    current_weather_url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?lat={coords[0]}&lon={coords[1]}&appid={api_key}"
    )

    current_weather_response = requests.get(current_weather_url)
    current_weather_data = current_weather_response.json()

    today = date.today()

    current_weather_data_table = PrettyTable()
    current_weather_data_table.title = str(today)

    current_weather_data_table.field_names = [
        "Temperature",
        "Temperature Min",
        "Temperature Max",
        "Pressure",
        "Humidity",
        "Weather",
        "Weather Description"
    ]

    current_weather_data_table.add_row([
        current_weather_data["main"]["temp"],
        current_weather_data["main"]["temp_min"],
        current_weather_data["main"]["temp_max"],
        current_weather_data["main"]["pressure"],
        current_weather_data["main"]["humidity"],
        current_weather_data["weather"][0]["main"],
        current_weather_data["weather"][0]["description"]
    ])

    return current_weather_data_table


def get_weather_for_five_days_info(city_name, state, country_code):
    """
    Retrieves a 5-day weather forecast and organizes it into separate PrettyTables by date.

    Parameters:
        city_name (str): Name of the city
        state (str): State name or abbreviation
        country_code (str): Country code (e.g., US)

    Returns:
        dict: A dictionary where each key is a date and each value is a PrettyTable
              containing forecast data for that day.
    """
    coords = get_lat_and_lat_coordinates_info(city_name, state, country_code)

    if coords is None:
        return "Location not found."

    five_day_forecast_url = (
        f"https://api.openweathermap.org/data/2.5/forecast"
        f"?lat={coords[0]}&lon={coords[1]}&appid={api_key}"
    )

    five_day_forecast_response = requests.get(five_day_forecast_url)
    five_day_forecast_data = five_day_forecast_response.json()

    five_day_forecast_data_tables = {}

    for forecast_day in five_day_forecast_data["list"]:
        forecast_date = forecast_day["dt_txt"].split(" ")[0]
        forecast_time = forecast_day["dt_txt"].split(" ")[1]

        if forecast_date not in five_day_forecast_data_tables:
            five_day_forecast_data_tables[forecast_date] = PrettyTable()
            five_day_forecast_data_tables[forecast_date].title = forecast_date
            five_day_forecast_data_tables[forecast_date].field_names = [
                "Time",
                "Temperature",
                "Temperature Min",
                "Temperature Max",
                "Pressure",
                "Humidity",
                "Weather",
                "Weather Description"
            ]

        five_day_forecast_data_tables[forecast_date].add_row([
            forecast_time,
            forecast_day["main"]["temp"],
            forecast_day["main"]["temp_min"],
            forecast_day["main"]["temp_max"],
            forecast_day["main"]["pressure"],
            forecast_day["main"]["humidity"],
            forecast_day["weather"][0]["main"],
            forecast_day["weather"][0]["description"]
        ])

    return five_day_forecast_data_tables