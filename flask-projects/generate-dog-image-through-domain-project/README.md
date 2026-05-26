# 🐶 Dog Image Web App

## 📌 Overview

This project is a Flask-based web application that retrieves and displays dog images using the Dog CEO API.

Users can:
- View a random dog image  
- View images by specific breed  
- View images by sub-breed  

The application dynamically renders results in a web interface using Flask and Jinja templates.

---

## 🚀 Features

- Random dog image generator  
- Breed-specific image retrieval  
- Sub-breed image support  
- Dynamic HTML rendering with Flask  
- Integration with external API (Dog CEO API)

---

## 🧱 Project Structure

project-folder/
│
├── main.py # Application entry point
├── server.py # Flask routes and server logic
├── colordata.py # API helper functions
│
├── templates/
│ └── index.html # Frontend template (Jinja2)
│
└── README.md

---

## 🛠️ Technologies Used

- Python  
- Flask  
- HTML  
- Jinja2 (templating engine)  
- Requests (HTTP library)  

---

## 📡 API Used

This project uses the Dog CEO API to fetch dog images and breed data:
- Random images  
- Breed-specific images  
- Sub-breed images  
- Breed lists  

---

## ▶️ How to Run the Project

1. Install dependencies:
2. pip install flask requests
3. Run the application:
4. 4. python main py
   5.  Open your browser and go to:



---

## 🌐 Available Routes

| Route | Description |
|------|-------------|
| `/` | Home page with instructions |
| `/Dog/Random` | Random dog image |
| `/Dog/<breed>/Random` | Random image by breed |
| `/Dog/<breed>/<sub_breed>/Random` | Random image by sub-breed |

---

## ⚠️ Notes / Improvements

- `colordata.py` currently ignores the `dog_breed` parameter in one function  
- Duplicate Flask app initialization in `server.py` should be removed  
- Error handling for API requests can be improved  
- UI styling is minimal and can be enhanced  

---

## 📅 Project Info

- **Author:** Ryan Pereira  
- **Created:** 4/22/2026  
- **Last Modified:** 4/25/2026  

---

## 📬 Contact

Feel free to open an issue or reach out with suggestions or improvements.



