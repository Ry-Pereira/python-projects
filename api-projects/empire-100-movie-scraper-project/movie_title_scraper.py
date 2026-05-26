#Name: Ryan Pereira
#Project Name: Empire 100 Movies Scraper
#Description:# A python program that scrapes the top 100 movies of all time from the Empire Online website and stores the movie titles in a text file. The program also defines a Movie class to represent each movie with its name, position, and year made. The MovieScraper class is responsible for scraping the data, writing it to a text file, and providing a menu for users to view the movies or search for specific movies by position, name, or year.
#Module Name: Movie Title Scraper
#Module Purpose: This module defines the MovieTitleScraper class, which is responsible for parsing
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 4/11/2026
#Last Modified: 4/12/2026


#From the bs4 library, we import the BeautifulSoup class, which is used for parsing HTML content. This allows us to extract specific elements from the HTML, such as movie titles, by using CSS selectors or other methods provided by BeautifulSoup.
from bs4 import BeautifulSoup



#The MovieTitleScraper class is defined to take HTML content as input and parse it to extract movie titles. The constructor (__init__ method) initializes the class with the provided HTML, creates a BeautifulSoup object to parse the HTML, and uses a CSS selector to find all strong elements within h2 tags, which are assumed to contain the movie titles. The extracted movie titles are stored in the movie_titles attribute of the class for later use.
class MovieTitleScraper:
    #The constructor (__init__ method) of the MovieTitleScraper class takes a string of HTML as input. It creates a BeautifulSoup object by parsing the HTML, which allows for easy navigation and extraction of elements from the HTML structure. The movie_titles attribute is then populated by selecting all strong elements that are children of h2 tags, which are expected to contain the movie titles on the Empire Online page.
    def __init__(self, html:str):
        #The constructor (__init__ method) of the MovieTitleScraper class takes a string of HTML as input. It creates a BeautifulSoup object by parsing the HTML, which allows for easy navigation and extraction of elements from the HTML structure. The movie_titles attribute is then populated by selecting all strong elements that are children of h2 tags, which are expected to contain the movie titles on the Empire Online page.
        soup = BeautifulSoup(html,'html.parser')
        #Select all strong elements that are children of h2 tags from the parsed HTML and store them in the movie_titles attribute. This is done using the select method of the BeautifulSoup object, which allows for CSS-style selectors to find specific elements in the HTML. The assumption is that the movie titles on the Empire Online page are contained within strong tags that are children of h2 tags.
        self.movie_titles = soup.select("h2")
