#Name: Ryan Pereira
#Project Name: Empire 100 Movies Scraper
#Description: A program that scrapes movie titles from Empire Online's list of best movies of all time.
#Module Name: Main
#Module Purpose: This program serves as the user interface for the Empire 100 Movies Scraper application. It defines the EmpireMovieScraperUI class, which sets up the Tkinter window, canvas, and buttons for scraping movie titles. The class includes methods for adding movie titles to the list and resetting the list.
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 4/6/2026
#Last Modified: 4/12/2026


#From the movies_requests module, we import the get_movie_titles_url function, which is responsible for making an HTTP request to the Empire Online website and retrieving the HTML content of the page that contains the list of best movies of all time. This HTML will later be parsed to extract movie titles.
from movies_requests import get_movie_titles_url
#From the movie_title_scraper module, we import the MovieTitleScraper class, which is responsible for parsing the HTML content retrieved from the Empire Online website and extracting the movie titles. The class uses BeautifulSoup to navigate the HTML structure and find the relevant elements that contain the movie titles.
from movie_title_scraper import MovieTitleScraper
#From the movie_list_brain module, we import the EmpireMovieBrain class, which is responsible for managing the list of movies, including writing movie titles to a text file, reading movies from the text file, and providing a menu for users to view and search for movies. This class serves as the main logic for handling movie data and user interactions in the application.
from movie_list_brain import EmpireMovieBrain



#The main function is defined to serve as the entry point of the program. It first retrieves the HTML content of the Empire Online page using the get_movie_titles_url function, then creates an instance of the MovieTitleScraper class to parse the HTML and extract movie titles. Finally, it creates an instance of the EmpireMovieBrain class, passing the extracted movie titles, and calls the run method to start the program's main loop and user interface.
def main() -> None:
    #Html variable is assigned the result of the get_movie_titles_url function, which retrieves the HTML content of the Empire Online page that contains the list of best movies of all time. This HTML will be parsed later to extract movie titles.
    html = get_movie_titles_url()
    #Movie_titles variable is assigned the result of creating an instance of the MovieTitleScraper class with the retrieved HTML and accessing its movie_titles attribute. This extracts the movie titles from the HTML content, which will be used to populate the movie list in the EmpireMovieBrain class.
    movie_titles = MovieTitleScraper(html).movie_titles
    #Empire movie brain is created as an instance of the EmpireMovieBrain class, passing the extracted movie titles as an argument. This initializes the movie list and prepares the program to run its main loop and user interface for displaying and searching movies.
    empire_movie_brain = EmpireMovieBrain(movie_titles)
    #The run method of the empire_movie_brain instance is called to start the program's main loop and user interface. This method will handle displaying the menu, processing user input, and allowing users to view and search for movies based on the extracted movie titles.
    empire_movie_brain.run()
    




#The if __name__ == "__main__": block is used to ensure that the main function is only executed when the script is run directly, and not when it is imported as a module in another script. This allows for better modularity and reusability of the code, as the main function will not be executed if the script is imported elsewhere.
if __name__ == "__main__":
    #The main function is called to start the program when the script is run directly. This will execute the logic defined in the main function, which includes retrieving HTML content, extracting movie titles, initializing the EmpireMovieBrain class, and starting the user interface for displaying and searching movies.
    main()
