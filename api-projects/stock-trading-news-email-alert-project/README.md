# 📈📰📧 Stock Trading News Email Alert 📧📰📈

## 📌 Overview

This project is a Python-based stock tracking and news alert application that monitors stock price data and retrieves related news articles for tracked companies. The program uses financial and news APIs to gather stock information and sends email alerts containing recent news articles related to the tracked stocks.

Users can:
- Add new stocks to track  
- Store stock information in a CSV file  
- Retrieve daily stock price data  
- Retrieve related company news articles  
- Send stock news alerts through email  
- Check for duplicate stock entries  

---

## 🧱 Project Structure

```text
project-folder/
│
├── main.py            # Main application logic
├── stock_list.csv     # CSV file storing tracked stock data
│
└── README.md
```

---

## 🚀 Features

- Stock market data retrieval using APIs  
- News article retrieval for tracked companies  
- Email alert system using SMTP  
- CSV-based stock tracking system  
- Duplicate stock checking  
- Automated stock list processing  
- Daily stock comparison support  
- Object and function-based program structure  

---

## 🛠️ Technologies Used

- Python  
- Requests  
- Pandas  
- SMTP  
- CSV File Handling  
- Datetime Module  

---

## 📡 APIs Used

This project uses the following APIs:

- Alpha Vantage API  
  - Retrieves stock market data  
  - Provides stock open and close prices  

- News API  
  - Retrieves recent news articles  
  - Provides article titles, descriptions, authors, and URLs  

---

## ▶️ How to Run the Project

1. Install dependencies:

```bash
pip install requests pandas
```

2. Add your email and app password inside `main.py`:

```python
EMAIL = "your_email@gmail.com"
PASSWORD = "your_app_password"
```

3. Add your API keys inside `main.py`:

```python
stock_data_key = "YOUR_ALPHA_VANTAGE_KEY"
news_api_key = "YOUR_NEWS_API_KEY"
```

4. Run the application:

```bash
python main.py
```

---

## 🌐 Program Functions

| Function | Description |
|----------|-------------|
| `get_stock_data()` | Retrieves stock market data |
| `add_stock_data()` | Adds a new stock to track |
| `check_stock_list()` | Checks all tracked stocks |
| `check_for_stock_duplicates()` | Prevents duplicate entries |
| `get_news_data()` | Retrieves related news articles |
| `send_email()` | Sends stock news email alerts |
| `main()` | Main program execution |

---

## 📄 CSV File Structure

| Column | Description |
|--------|-------------|
| Ticker | Stock ticker symbol |
| Company | Company name |
| Open_Price_Yesterday | Previous open price |
| Close_Price_Yesterday | Previous close price |
| Open_Price_Yesterday_Before | Earlier open price |
| Close_Price_Yesterday_Before | Earlier close price |

---

## 📅 Project Info

- **Author:** Ryan Pereira  
- **Created:** 6/27/2026  
- **Last Modified:** 6/29/2026  

---

## 📬 Contact

Feel free to open an issue or submit suggestions for improvements or new features.
