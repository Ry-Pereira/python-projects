#Name: Ryan Pereira
#Project Name: Empire 100 Movies Scraper
#Description: A python program that scrapes the top 100 movies of all time from the Empire Online website and stores the movie titles in a text file. The program also defines a Movie class to represent each movie with its name, position, and year made. The MovieScraper class is responsible for scraping the data, writing it to a text file, and providing a menu for users to view the movies or search for specific movies by position, name, or year.
#Module Name: Movie List Brain
#Module Purpose: This program serves as the user interface for the Color Mixer application. It defines the ColorMixerUI class, which sets up the Tkinter window, canvas, and buttons for mixing colors. The class includes methods for adding colors to the mix and resetting the color mix.
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 4/11/2026
#Last Modified: 4/12/2026


#From the movie_class module, we import the Movie class, which represents a movie with its name, position, and year made. This allows us to create Movie objects to store information about each movie scraped from the Empire Online website.
from movie_class import Movie



#The EmpireMovieBrain class is defined to take a list of movie titles as input and provide various methods for interacting with the movie data. The class includes methods for displaying a menu of options, writing movie titles to a text file, reading movies from the text file, printing the list of movies, and searching for movies by position, name, letter, or year. The run method serves as the main loop for the program, allowing users to interact with the menu and perform various actions based on their input.
class EmpireMovieBrain:
    #The constructor (__init__ method) of the EmpireMovieBrain class takes a list of movie titles as input. It initializes the movie_titles attribute with the provided list, sets the movie_text_file attribute to an empty string, and initializes an empty list for movies. This setup allows the class to store the movie titles, manage the text file for storing movie data, and maintain a list of Movie objects that can be used for various operations such as searching and displaying movie information.
    def __init__(self,movie_titles):
        #Objec'ts movie titles is set to the movie_titles input paramater value
        self.movie_titles = movie_titles
        #Movie text file is initialized as an empty string, which will later be used to specify the name of the text file where movie titles will be stored. This allows for flexibility in naming the text file and managing the storage of movie data.
        self.movie_text_file = ""
        #Movies is initialized as an empty list, which will later be populated with Movie objects created from the movie titles. This list will allow for easy access and manipulation of movie data, such as searching for movies by various criteria or displaying the list of movies to the user.
        self.movies = []

    
    #The menu method is defined to display a menu of options to the user. This menu provides various choices for interacting with the movie data, such as viewing the movies text file, getting movies by position, name, letter, or year, and exiting the program. The method simply prints the menu options to the console, allowing the user to make a selection based on their desired action.
    def menu(self) -> None:
        #Press 1 to view movies text file
        print("1) Press 1 to View Movies text file")
        #Press 2 to get movie by position
        print("2) Press 2 To get movie by position")
        #Press 3 to get movies by position range
        print("3) Press 3 To get movies by position range")
        #Press 4 to get movie by name
        print("4) Press 4 To get movie by name")
        #Press 5 to get movies by letter
        print("5) Press 5 To get movies by letter")
        #Press 6 to get movies by year
        print("6) Press 6 To get movies by year")
        #Press 7 to get movies by year range
        print("7) Press 7 To get movies by year range")
        #Press 8 to exit the program
        print("8) Press 8 To Exit")
     

    #Defining a method to write movies into a text file. This method takes the name of the text file as a parameter and writes the movie titles from the movie_titles attribute into the specified text file, with each title on a new line. This allows for easy storage and retrieval of movie data in a structured format.
    def write_into_moves_text_file(self, movie_text_file: str) -> None:
        #With statement to open the movies text file in write mode with alias as file.
        with open("movies.txt","w") as file:
            #Looping through object's movie titles
            for title in self.movie_titles:
                #File write this title text with new line
                if len(title.text) > 1 and ")" in title.text and title.text[0].isdigit():
                    file.write(title.text + "\n")

    #Defining a method to read movies from a text file. This method opens the specified text file in read mode, reads the lines of the file, and processes each line to create Movie objects. The lines are split based on the expected format of the movie data (position, name, year), and the resulting Movie objects are stored in the movies list attribute for later use in searching and displaying movie information.
    def read_movies_from_text_file(self) -> None:
        #With statement to open the movies text file in read mode with alias as file.
        with open("movies.txt","r") as file:
            #Lines is set to file.readlines(), which reads all lines from the text file and stores them in a list called lines. This allows for processing each line of the file to extract movie information and create Movie objects.
            lines = file.readlines()
            #Looping though each line in lines
            for line in lines:
                #Line is process by replacing all right parantheses with left parentheses and splitting that line, createing as a list
                line = line.replace(")","(").split("(")
                #Self movies list appends the a Movie object created with the name, position, and year extracted from the processed line. The line[1] is assumed to be the movie name, line[0] is the position, and line[2] is the year made. This allows for structured storage of movie data in the movies list for later retrieval and display.
                self.movies.append(Movie(line[1].strip(),line[0],line[2]))
    

    #Defining a method to print the list of movies.
    def print_movies_list(self) -> None:
        #Looping through each movie in object's movie list
        for movie in self.movies:
            #Print the movie's position, name, and year made in a formatted string. The output is structured to display the position followed by the movie name and the year it was made, allowing for easy reading and understanding of the movie information.
            print(f"{movie.position}) {movie.name} ({movie.year_made})")

    #Defining a method to get a movie by its position. This method takes a position as input and searches through the movies list to find a movie that matches the specified position. If a matching movie is found, its information is printed in a formatted string. This allows users to quickly retrieve information about a specific movie based on its position in the list.
    def get_movie_by_position(self,position : str) -> None:
        #Is there a movie variable is initialized as False, which will be used to track whether a movie matching the specified position was found in the movies list. This allows for providing feedback to the user if no movie is found at the given position.
        is_there_a_movie = False
        #Looping through each movie in object's movie list
        if position.isdigit() and int(position) > 0 and int(position) <= len(self.movies):
            for movie in self.movies:
                #If the movie's position matches the input position, print the movie's position, name, and year made in a formatted string. This allows users to quickly retrieve information about a specific movie based on its position in the list.
                if movie.position == position:
                    is_there_a_movie = True
                    #Print the movie's position, name, and year made in a formatted string. The output is structured to display the position followed by the movie name and the year it was made, allowing for easy reading and understanding of the movie information.
                    print(f"{movie.position}) {movie.name} ({movie.year_made})")
        #Elif the is there a movie variable is still False after looping through the movies list, it means that no movie was found at the specified position. In this case, a message is printed to inform the user that there is no movie at that position. This provides feedback to the user about the search results.
        elif is_there_a_movie == False:
            print("There is no movie at that position.")
        #Else statement to handle invalid input, such as non-digit input or positions that are out of range. If the input is invalid, a message is printed to inform the user to enter a valid position. This helps ensure that the user provides appropriate input for searching movies by position.
        else:
            print("Invalid input. Please enter a valid position.")
            


    #Defining a method to get movies by a range of positions. This method takes two positions as input and searches through the movies list to find movies that fall within the specified range of positions. If a movie's position is greater than or equal to the first position and less than or equal to the second position, its information is printed in a formatted string. This allows users to retrieve information about multiple movies based on their positions in the list.
    def get_move_by_position_range(self,position1 : str, position2 : str) -> None:
        #Is there a movie variable is initialized as False, which will be used to track whether any movies matching the specified position range were found in the movies list. This allows for providing feedback to the user if no movies are found within the given position range.
        is_there_a_movie = False
        #Looping through each movie in object's movie list
        if position1.isdigit() and position2.isdigit() and int(position1) > 0 and int(position2) > 0 and int(position1) <= int(position2):
            for movie in self.movies:
                #If the movie's position is greater than or equal to the first input position and less than or equal to the second input position, print the movie's position, name, and year made in a formatted string. This allows users to retrieve information about multiple movies based on their positions in the list.
                if int(movie.position) >= int(position1) and int(movie.position) <= int(position2):
                    #Print the movie's position, name, and year made in a formatted string. The output is structured to display the position followed by the movie name and the year it was made, allowing for easy reading and understanding of the movie information.
                    print(f"{movie.position}) {movie.name} ({movie.year_made})")
                    is_there_a_movie = True
        elif is_there_a_movie == False:
            print("There is no movie at that position.")        
        else:
            print("Invalid input. Please enter valid positions.")
        

            
    


    #Defining a method to get a movie by its name. This method takes a movie name as input and searches through the movies list to find a movie that matches the specified name. If a matching movie is found, its information is printed in a formatted string. This allows users to quickly retrieve information about a specific movie based on its name.
    def get_movie_by_name(self,name : str) -> None:
        #Is there a movie variable is initialized as False, which will be used to track whether a movie matching the specified name was found in the movies list. This allows for providing feedback to the user if no movie is found with the given name.
        is_there_a_movie = False
        #Looping through each movie in object's movie list
        for movie in self.movies:
            #If the movie's name matches the input name, print the movie's position, name, and year made in a formatted string. This allows users to quickly retrieve information about a specific movie based on its name.
            if movie.name == name:
                #Print the movie's position, name, and year made in a formatted string. The output is structured to display the position followed by the movie name and the year it was made, allowing for easy reading and understanding of the movie information.
                print(f"{movie.position}) {movie.name} ({movie.year_made})")
                is_there_a_movie = True

        if is_there_a_movie == False:
            print("Movie not found.")

    #Defining a method to get movies by the first letter of their name. This method takes a letter as input and searches through the movies list to find movies whose names start with the specified letter. If a movie's name starts with the input letter, its information is printed in a formatted string. This allows users to retrieve information about movies based on the first letter of their names.
    def get_movie_by_letter(self,letter : str) -> None:
        #Is there a movie variable is initialized as False, which will be used to track whether any movies matching the specified first letter were found in the movies list. This allows for providing feedback to the user if no movies are found that start with the given letter.
        is_there_a_movie = False
        #Looping through each movie in object's movie list
        for movie in self.movies:
            #If the movie's name starts with the input letter, print the movie's position, name, and year made in a formatted string. This allows users to retrieve information about movies based on the first letter of their names.
            if movie.name[0] == letter.upper():
                #Print the movie's position, name, and year made in a formatted string. The output is structured to display the position followed by the movie name and the year it was made, allowing for easy reading and understanding of the movie information.
                print(f"{movie.position}) {movie.name} ({movie.year_made})")
                is_there_a_movie = True
        if is_there_a_movie == False:
            print("There are no movies that start with that letter.")
    

    #Defining a method to get movies by their release year. This method takes a year as input and searches through the movies list to find movies that were released in the specified year. If a movie's release year matches the input year, its information is printed in a formatted string. This allows users to retrieve information about movies based on their release year.
    def get_movie_by_year(self,year : str) -> None:
        #Is there a movie variable is initialized as False, which will be used to track whether any movies matching the specified release year were found in the movies list. This allows for providing feedback to the user if no movies are found that were released in the given year.
        is_there_a_movie = False

        #Looping through each movie in object's movie list
        for movie in self.movies:
            #If the movie's release year matches the input year, print the movie's position, name, and year made in a formatted string. This allows users to retrieve information about movies based on their release year.
            if int(movie.year_made) == int(year):
                #Print the movie's position, name, and year made in a formatted string. The output is structured to display the position followed by the movie name and the year it was made, allowing for easy reading and understanding of the movie information.
                print(f"{movie.position}) {movie.name} ({movie.year_made})")
                is_there_a_movie = True
        if is_there_a_movie == False:
            print("There are no movies that were made in that year.")
                

    #Defining a method to get movies by a range of release years. This method takes two years as input and searches through the movies list to find movies that were released within the specified range of years. If a movie's release year is greater than or equal to the first input year and less than or equal to the second input year, its information is printed in a formatted string. This allows users to retrieve information about movies based on their release years.
    def get_movie_by_year_range(self,year1 : str, year2 : str) -> None:
        #Is there a movie variable is initialized as False, which will be used to track whether any movies matching the specified release year range were found in the movies list. This allows for providing feedback to the user if no movies are found that were released within the given year range.
        is_there_a_movie = False
        #Looping through each movie in object's movie list
        for move in self.movies:
            #If the movie's release year is greater than or equal to the first input year and less than or equal to the second input year, print the movie's position, name, and year made in a formatted string. This allows users to retrieve information about movies based on their release years.
            if int(move.year_made) >= int(year1) and int(move.year_made) <= int(year2):
                #Print the movie's position, name, and year made in a formatted string. The output is structured to display the position followed by the movie name and the year it was made, allowing for easy reading and understanding of the movie information.
                print(f"{move.position}) {move.name} ({move.year_made})")
                is_there_a_movie = True
        if is_there_a_movie == False:
            print("There are no movies that were made in that year range.")

    

    




    
    #Defining the run method, which serves as the main loop for the program. This method first writes the movie titles into a text file, then displays the menu to the user and waits for input. Based on the user's input, it calls the appropriate method to perform the desired action, such as viewing the movies list, searching for movies by position, name, letter, or year, or exiting the program. The loop continues until the user chooses to exit by entering "8".
    def run(self) -> None:
        # Write the movie titles into a text file using the write_into_movies_text_file method, passing the movie_text_file attribute as an argument. This allows for storing the movie titles in a text file for later retrieval and display.
        self.write_into_moves_text_file(self.movie_text_file)
        # Read the movies from the text file using the read_movies_from_text_file method. This populates the movies list with Movie objects created from the data in the text file, allowing for easy access and manipulation of movie information in subsequent operations.
        self.read_movies_from_text_file()
        # Display the menu and wait for user input.
        self.menu()
        #User input is taken to determine the user's choice from the menu. The program will continue to loop and process user input until the user chooses to exit by entering "8". Based on the user's input, the program will call the appropriate method to perform the desired action, such as viewing the movies list, searching for movies by position, name, letter, or year.
        user_input = input("Enter your choice: ")
        #While the user input is not equalt o "8", which is the option to exit the program, the loop continues to process user input and call the appropriate methods based on the user's choice from the menu. This allows for interactive functionality, enabling users to view and search for movies based on various criteria until they decide to exit the program.
        while user_input != "8":
            #Based on the user's input, the program checks which option was selected and calls the corresponding method to perform the desired action. For example, if the user input is "1", it calls the print_movies_list method to display the list of movies. If the user input is "2", it prompts the user to enter a position and then calls the get_movie_by_position method with the provided position. This structure allows for a responsive and interactive user experience, enabling users to easily access movie information based on their preferences.
            if user_input == "1":
                self.print_movies_list()
            elif user_input == "2":
                position = input("Enter the position of the movie: ")
                self.get_movie_by_position(position)
            elif user_input == "3":
                position1 = input("Enter the first position: ")
                position2 = input("Enter the second position: ")
                self.get_move_by_position_range(position1,position2)
            elif user_input == "4":
                name = input("Enter the name of the movie: ")
                self.get_movie_by_name(name)
            elif user_input == "5":
                letter = input("Enter the letter: ")
                self.get_movie_by_letter(letter)
            elif user_input == "6":
                year = input("Enter the year: ")
                self.get_movie_by_year(year)
            elif user_input == "7":
                year1 = input("Enter the first year: ")
                year2 = input("Enter the second year: ")
                self.get_movie_by_year_range(year1,year2)
            else:
                print("Invalid input. Please try again.")
            
            #After processing the user's choice and calling the appropriate method, the menu is displayed again to allow the user to make another selection. The program continues to loop and process user input until the user chooses to exit by entering "8". This structure provides a seamless and interactive experience for users to explore the movie data based on their preferences.
            self.menu()
            user_input = input("Enter your choice: ")
        