# 🔴🟠🟡🟢🔵🟣🟤⚫⚪🌈 Background Color Changer 🌈⚪⚫🟤🟣🔵🟢🟡🟠🔴

## 📌 Overview

This project is a Flask-based web application that changes the background color of a webpage based on a color name provided in the URL.

Users can:
- Enter a color name in the URL
- View the page background change dynamically
- See the color name displayed on the page

---

## 🧱 Project Structure

project-folder/
│
├── server.py # Flask routes and server logic
├── colordata.py # API helper functions (color lookup)
│
├── templates/
│ └── index.html # Frontend template (Jinja2)
│
└── README.md

---

## 🚀 Features

- Dynamic background color changing  
- URL-based color input  
- API-based color hex lookup  
- Simple Flask routing system  
- Jinja2 template rendering  

---

## 🛠️ Technologies Used

- Python  
- Flask  
- HTML  
- Jinja2  
- Requests  

---

## 📡 API Used

This project uses a CSS Colors API to retrieve hex values for color names.

- Converts color names into hex codes  
- Returns matching color values from dataset  

---

## ▶️ How to Run the Project

1. Install dependencies:  
   pip install flask requests  

2. Run the application:  
   python server.py  

3. Open your browser and go to:  
   http://127.0.0.1:5000/

---

## 🌐 Available Routes

| Route | Description |
|------|-------------|
| `/` | Home page with instructions |
| `/color/<color>` | Changes background to specified color |

Example:
/color/red
/color/blue
/color/green


---

## ⚠️ Notes / Improvements

- `colordata.py` works but depends on external API availability  
- In `server.py`, `background_color` should likely use `color_hex` instead of raw `color`  
- Error handling for API failures could be improved  
- UI is minimal and can be enhanced  

---

## 📅 Project Info

- **Author:** Ryan Pereira  
- **Created:** 4/19/2026  
- **Last Modified:** 4/21/2026  

---

## 📬 Contact

Feel free to open an issue or reach out with suggestions or improvements.






