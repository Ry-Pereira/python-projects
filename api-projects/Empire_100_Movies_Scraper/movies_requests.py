#Name: Ryan Pereira
#Project Name: Empire's Best Movies of All Time
#Description: A program that scrapes movie titles from Empire Online's list of best movies of all time.
#Module Name: Movies Requests
#Module Purpose: This module contains functions for making HTTP requests to scrape movie data from Empire Online.
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 4/11/2026
#Last Modified: 4/12/2026


#From tge requests library, we import everything to make HTTP requests to the Empire Online website. This allows us to retrieve the HTML content of the page, which we can then parse to extract movie titles.
from requests import *
import requests





#The function get_movie_titles_url is defined to make an HTTP GET request to the specified URL, which contains the list of best movies of all time. The function sets a user-agent header to mimic a browser request and returns the text content of the response, which is the HTML of the page. This HTML will later be parsed to extract the movie titles.
def get_movie_titles_url() -> list:
    #Url variable is assigned the URL of the Empire Online page that lists the best movies of all time. The headers variable is a dictionary that contains a user-agent string to identify the request as coming from a web browser. The requests.get function is called with the URL and headers to make the HTTP request, and the response is stored in the response variable. Finally, the function returns the text content of the response, which is the HTML of the page.
    url = "https://www.empireonline.com/movies/features/best-movies-of-all-time-us/"
    #Headers is set to mimic a browser request, which can help avoid being blocked by the website. The requests.get function is used to send a GET request to the specified URL with the provided headers, and the response is stored in the response variable. The function then returns the text content of the response, which contains the HTML of the page that will be parsed to extract movie titles.
    headers = {"User-Agent": "Mozilla/5.0"}
    #Response variable is assigned the result of the HTTP GET request made to the specified URL with the provided headers. The requests.get function is used to send the request, and the response is stored in the response variable. Finally, the function returns the text content of the response, which contains the HTML of the page that will be parsed to extract movie titles.
    response = requests.get(url,headers=headers)
    #Returns the text content of the response, which is the HTML of the page that contains the list of best movies of all time. This HTML will be parsed later to extract the movie titles.
    return response.text
