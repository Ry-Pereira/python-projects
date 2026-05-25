# 🎲🔢 Higher or Lower Number Guessing Web App 🐍🌐

## 📌 Overview

This project is a Flask-based web application where users try to guess a randomly generated number between **1️⃣ and 9️⃣** by changing the URL in the browser.

When the user visits a route like `/number/5`, the application checks whether the guessed number matches the randomly selected number and displays either a ✅ correct or ❌ incorrect message.

---

## 🚀 Features

- 🎲 Random number generation on startup  
- 🔢 Number guessing through URL routes  
- 🌐 Flask-based web server  
- 💻 Simple browser interaction  
- ⚡ Dynamic responses based on guesses  
- 🐍 Beginner-friendly Python project  

---

## 🧱 Project Structure

```text
project-folder/
│
├── main.py       # 🚀 Application entry point
├── server.py     # 🌐 Flask routes and game logic
│
└── README.md     # 📄 Project documentation
```

---

## 🛠️ Technologies Used

- 🐍 Python  
- 🌐 Flask  

---

## ▶️ How to Run the Project

### 1️⃣ Install dependencies

```bash
pip install flask
```

### 2️⃣ Run the application

```bash
python main.py
```

### 3️⃣ Open your browser and go to

```text
http://127.0.0.1:5000/
```

---

## 🌐 Available Routes

| 🌍 Route | 📖 Description |
|------|-------------|
| `/` | 🏠 Home page with instructions |
| `/number/1` | 1️⃣ Guess the number 1 |
| `/number/2` | 2️⃣ Guess the number 2 |
| `/number/3` | 3️⃣ Guess the number 3 |
| `/number/4` | 4️⃣ Guess the number 4 |
| `/number/5` | 5️⃣ Guess the number 5 |
| `/number/6` | 6️⃣ Guess the number 6 |
| `/number/7` | 7️⃣ Guess the number 7 |
| `/number/8` | 8️⃣ Guess the number 8 |
| `/number/9` | 9️⃣ Guess the number 9 |

---

## 🎮 How to Play

1️⃣ Start the Flask server  
2️⃣ Open the browser homepage  
3️⃣ Change the URL to a number route like:

```text
http://127.0.0.1:5000/number/4
```

4️⃣ Try to guess the correct random number 🎯  

- ✅ Correct guess → You win! 🎉  
- ❌ Wrong guess → Try again 🔄  

---

## ⚠️ Notes / Improvements

- ♻️ Routes are repetitive and could be simplified using dynamic Flask routes  
- 🔄 The random number resets whenever the server restarts  
- 🎨 HTML responses are minimal and can be styled with templates and CSS  
- 🛡️ Error handling and user feedback can be improved  
- 🧠 A score tracker or leaderboard could be added  

---

## 📅 Project Info

- 👨‍💻 **Author:** Ryan Pereira  
- 📆 **Created:** 5/12/2026  

---

## 📬 Contact

💡 Feel free to improve the project by adding:
- 🎨 Better styling  
- 🏆 A scoring system  
- 📱 Responsive design  
- 🔥 More game features  


