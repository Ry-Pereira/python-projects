#Name: Ryan Pereira
#Project Name: Empire 100 Movies Scraper
#Description:# A python program that scrapes the top 100 movies of all time from the Empire Online website and stores the movie titles in a text file. The program also defines a Movie class to represent each movie with its name, position, and year made. The MovieScraper class is responsible for scraping the data, writing it to a text file, and providing a menu for users to view the movies or search for specific movies by position, name, or year.
#Module Name: Movie Class
#Module Purpose: This module defines the Movie class, which represents a movie with a name, position, and year made.
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 4/4/2026
#Last Modified: 4/12/2026


#Class to represent a movie with its name, position, and year made
class Movie:
    #Constructor to initialize the Movie object with its name, position, and year made
    def __init__(self,name,position,year_made):
        #Initialize the Movie object with its name, position, and year made
        self.name = name
        self.position = position
        self.year_made = year_made