# 🌎 Where Am I Locator Project

## 📌 Overview

The **Where Am I Locator Project** is a Python application that determines a user's approximate geographic location using their public IP address. The program retrieves information from online IP lookup services and presents useful details such as location, coordinates, time zone, and ISP information through an interactive menu system.

Users can view their location information, save a report containing all collected data, and explore details about their internet connection.

---

## ✨ Features

✅ Display Public IP Address

✅ Display Country, Region, City, and ZIP Code

✅ Display Latitude and Longitude Coordinates

✅ Display Time Zone and Local Time

✅ Display Internet Service Provider (ISP) Information

✅ Generate and Save a Location Report

✅ Interactive Menu-Driven Interface

✅ Decorative ASCII Art User Interface

---

## 🛠 Technologies Used

* Python 3
* Requests Library
* BeautifulSoup4
* IP-API
* ZoneInfo
* Datetime Module

---

## 📂 Project Structure

```text
WhereAmILocatorProject/
│
├── main.py
├── where_am_i_locator_brain.py
├── where_am_i_locator_requests.py
├── where_am_i_locator_art.py
├── where_am_i_report.txt
└── README.md
```

### Module Descriptions

#### main.py

Program entry point that creates and runs the `WhereAmILocatorBrain` object.

#### where_am_i_locator_brain.py

Contains the main program logic, menu system, data retrieval methods, report generation, and user interaction.

#### where_am_i_locator_requests.py

Handles web requests for retrieving the user's public IP address and location information from APIs.

#### where_am_i_locator_art.py

Stores ASCII art banners and decorative dividers used throughout the program.

---

## 🚀 How to Run

### 1. Install Required Libraries

```bash
pip install requests
pip install beautifulsoup4
```

### 2. Run the Program

```bash
python main.py
```

---

## 📋 Menu Options

| Option | Description                   |
| ------ | ----------------------------- |
| 1      | Show Public IP Address        |
| 2      | Show Location Information     |
| 3      | Show Coordinates              |
| 4      | Show Time Zone and Local Time |
| 5      | Show ISP Information          |
| 6      | Save Report                   |
| 7      | Exit Program                  |

---

## 📄 Sample Report Output

```text
Country: United States

Region: Kansas

City: Lawrence

Zip Code: 66045

Latitude: 38.9717

Longitude: -95.2353

Time Zone: America/Chicago

Time Display: 03:45 PM

ISP: Example ISP

Organization: Example Organization

Autonomous System Number: AS12345
```

---

## 🎯 Learning Objectives

This project demonstrates:

* Working with APIs
* Web Scraping with BeautifulSoup
* Object-Oriented Programming
* File Handling
* Dictionaries and JSON Data
* User Input Validation
* Modular Programming
* Time Zone Handling

---

## ⚠️ Notes

* Location data is approximate and based on the public IP address.
* VPNs and proxies may affect the reported location.
* An active internet connection is required.
* API availability may impact program functionality.

---

## 👨‍💻 Author

**Ryan Pereira**

Computer Science Student

University of Kansas

---

## 📚 Sources

* Python Documentation
* BeautifulSoup Documentation
* Requests Documentation
* IP-API
* Stack Overflow
* GitHub Copilot
* ChatGPT


