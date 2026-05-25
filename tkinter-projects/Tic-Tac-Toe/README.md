# 🎮 Tic-Tac-Toe (Tkinter) 🐍

## 📌 Overview

This repository contains a **Python-based Tic-Tac-Toe game built using Tkinter** 🧩🖥️.

It is a simple two-player GUI game where players take turns placing **X** and **O** on a 3×3 grid. The program manages turns, checks for wins or ties, and allows restarting or quitting after the game ends.

---

## 👤 Project Details

- **Name:** Ryan Pereira  
- **Project Name:** Tic-Tac-Toe  
- **Description:** A Tkinter-based Tic-Tac-Toe game where two players take turns placing X or O on a 3x3 grid. The program manages turns, checks for wins or ties, and allows restarting or quitting after the game ends.  
- **Collaborators:** None  
- **Sources:** GitHub Copilot, Stack Overflow, ChatGPT, Python Documentation  
- **Date:** 6/16/2026  
- **Last Modified:** 6/18/2026  

---

## 🎯 Features

* 🎮 Two-player gameplay (X vs O)
* 🧠 Automatic win detection (rows, columns, diagonals)
* 🤝 Tie detection when the board is full
* 🔄 Restart game option after completion
* 🚪 Quit game option
* 🎨 Interactive Tkinter GUI interface

---

## 🧱 Project Structure

This project is a single Python file built with Tkinter and includes:

### 🪟 GUI Setup
- Creates the main window using `Tkinter`
- Displays game title and turn label
- Arranges widgets using grid layout

### 🎲 Game Logic
- Alternating turns between X and O
- Win detection for:
  - Rows
  - Columns
  - Diagonals
- Tie detection when no empty spaces remain

### 🔘 Controls
- 3×3 grid of buttons for gameplay
- Restart button resets the board
- Quit button closes the application

---

## 🛠️ Technologies Used

- Python 3.x  
- Tkinter (GUI library)  
- random (to choose starting player)  
- functools.partial (to pass button arguments)

---

## ▶️ How to Run

### 1️⃣ Install Python
Make sure Python 3.x is installed.

### 2️⃣ Run the program

```bash
python main.py
```

### 3️⃣ Play the game
A window will open where you can start playing Tic-Tac-Toe 🎮

---

## 🧠 How It Works

- A random player (X or O) starts first
- Players click empty cells to place their symbol
- After each move, the game checks:
  - If someone won 🏆
  - If the game is a tie 🤝
- When the game ends:
  - Restart resets the board
  - Quit closes the window

---

## 📁 File Structure

```
📦 Tic-Tac-Toe Project
 ┣ 📜 main.py
 ┗ 📜 README.md
```

---

## 📬 Contact

If you have suggestions or feedback:

- Open an issue 🐛  
- Start a discussion 💬  
- Contribute improvements 🚀  

---
```
