# 🎬🍿🎥⭐ Empire 100 Movies Scraper ⭐🎥🍿🎬

## 📌 Overview

This project is a Python-based web scraping application that collects movie titles from Empire Online’s list of the **100 Best Movies of All Time**. The program retrieves movie data from the website, parses the HTML content, stores movie information in a text file, and allows users to search through the movies using a command-line menu system.

Users can:
- Scrape movie titles from Empire Online  
- Store movies in a text file  
- View all movies  
- Search movies by:
  - Position  
  - Position range  
  - Name  
  - First letter  
  - Release year  
  - Release year range  

---

## 🧱 Project Structure

```text
project-folder/
│
├── main.py                  # Main entry point of the application
├── movie_class.py           # Movie class definition
├── movie_list_brain.py      # Main application logic and menu system
├── movie_title_scraper.py   # HTML parsing and movie extraction
├── movies_requests.py       # HTTP requests for movie webpage
│
├── movies.txt               # Generated movie text file
│
└── README.md
```

---

## 🚀 Features

- Scrapes movie data from Empire Online  
- Extracts movie titles using BeautifulSoup  
- Stores movie data in a text file  
- Command-line interactive menu system  
- Search movies by multiple criteria  
- Organized object-oriented structure  
- Modular Python files for readability and maintainability  

---

## 🛠️ Technologies Used

- Python  
- BeautifulSoup4  
- Requests  
- File Handling  
- Object-Oriented Programming (OOP)  

---

## 📡 Data Source

This project retrieves movie information from:

- Empire Online’s “Best Movies of All Time” webpage

The scraper:
- Sends an HTTP request to the webpage  
- Parses HTML content  
- Extracts movie title information  

---

## ▶️ How to Run the Project

1. Install dependencies:

```bash
pip install requests beautifulsoup4
```

2. Run the application:

```bash
python main.py
```

3. Follow the menu prompts in the terminal.

---

## 🌐 Menu Options

| Option | Description |
|--------|-------------|
| 1 | View all movies |
| 2 | Get movie by position |
| 3 | Get movies by position range |
| 4 | Get movie by name |
| 5 | Get movies by first letter |
| 6 | Get movies by year |
| 7 | Get movies by year range |
| 8 | Exit program |

---

## 📅 Project Info

- **Author:** Ryan Pereira  
- **Created:** 4/6/2026  
- **Last Modified:** 4/12/2026  

---

## 📬 Contact

Feel free to open an issue or submit suggestions for improvements or new features.
