# 🔴🟠🟡🟢🔵🟣🟤⚫⚪🌈 Background Color Changer Through Request Project 🌈⚪⚫🟤🟣🔵🟢🟡🟠🔴

## 📌 Overview

This project is a Flask-based web application that changes the background color of a webpage based on a color name entered into a form request. 🎨✨

Users can:
- 🌈 Enter a color name into the input field  
- 🎨 Dynamically change the webpage background color  
- 📝 View instruction messages on the page  
- 🔍 Retrieve real hexadecimal color values from an API  

---

## 🧱 Project Structure

```text
background-color-changer-through-request-project/
│
├── main.py                 # Application entry point
├── server.py               # Flask routes and server logic
├── color_data.py           # API helper functions (color lookup)
│
├── templates/
│   └── index.html          # Frontend template (Jinja2)
│
└── README.md
```

---

## 🚀 Features

- 🎨 Dynamic background color changing  
- 📨 Form-based POST request input  
- 🌈 API-based color hex lookup  
- 🌶️ Simple Flask routing system  
- 🖥️ Jinja2 template rendering  
- ⚠️ Invalid color handling  

---

## 🛠️ Technologies Used

- 🐍 Python  
- 🌶️ Flask  
- 🌐 HTML  
- 🧩 Jinja2  
- 📡 Requests  

---

## 📡 API Used

This project uses a CSS Colors API to retrieve hexadecimal values for color names. 🌈

- 🔍 Converts color names into hex codes  
- 🎨 Returns matching color values from the dataset  
- ⚡ Dynamically updates webpage background colors  

---

## ▶️ How to Run the Project

1. Install dependencies:  

```bash
pip install flask requests
```

2. Run the application:  

```bash
python main.py
```

3. Open your browser and go to:  

```text
http://127.0.0.1:5000/
```

---

## 🌐 Available Routes

| Route | Description |
|------|-------------|
| `/` | Home page with form input and instructions |

Example color inputs:

```text
red
blue
green
purple
orange
black
white
```

---

## ⚠️ Notes / Improvements

- 📡 `color_data.py` depends on external API availability  
- 🎨 Additional UI styling could be added  
- ⚠️ API error handling could be improved  
- 🌈 More color validation could be implemented  
- 📱 Responsive design enhancements could be added  

---

## 📅 Project Info

- **👨‍💻 Author:** Ryan Pereira  
- **📅 Created:** 5/27/2026  
- **🛠️ Last Modified:** 5/27/2026  

---

## 📬 Contact

Feel free to open an issue or reach out with suggestions or improvements. 🚀✨
