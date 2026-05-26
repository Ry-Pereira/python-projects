# 🎮🪢 Hangman Game 🪢🎮

## 📌 Description

This project is a graphical **Hangman Game** built using **Python** and **Tkinter** 🐍🖥️.  
Players try to guess a hidden word one letter at a time before the hangman drawing is completed.

The game includes interactive letter buttons, ASCII hangman art, win/lose screens, restart functionality, and randomly selected words 🎲.

---

## ✨🚀 Features

✅ Random word selection 🎲  
✅ Interactive Tkinter GUI 🖥️  
✅ Letter button input 🔠  
✅ ASCII hangman stages 🪢  
✅ Win and lose game screens 🏆💀  
✅ Restart game option 🔄  
✅ Quit game button ❌  
✅ Beginner-friendly Python project 🐍  

---

## ⚙️🧠 How It Works

1️⃣ A random word is selected from the word list 🎲  

2️⃣ The word is hidden using underscores `_` 🔤  

3️⃣ Player clicks letter buttons to guess letters 🔠  

4️⃣ Correct guesses reveal letters in the word ✅  

5️⃣ Incorrect guesses increase the hangman stage ❌  

6️⃣ The game ends when:
- The player guesses the full word 🏆
- The player runs out of lives 💀

7️⃣ Player can restart or quit the game 🔄❌

---

## 🛠️💻 Technologies Used

- 🐍 Python 3  
- 🖼️ Tkinter GUI Library  
- 🎲 Random Module  
- 🪢 ASCII Art  

---

## 📂🧱 Project Structure

```text
project-folder/
│
├── hangman.py       # Main Hangman game
├── hangman_art.py   # ASCII hangman stages
│
└── README.md
```

---

## 🎮 Gameplay Features

### 🔠 Word Guessing
- Players guess letters using on-screen buttons
- Correct letters are revealed automatically

### 🪢 Hangman Stages
The hangman drawing progresses with each incorrect guess:

```text
Stage 0 → Empty gallows
Stage 6 → Full hangman
```

### 🏆 Win Condition
Reveal all letters before losing all lives.

### 💀 Lose Condition
The full hangman is drawn after too many incorrect guesses.

---

## 🖼️ Example Hangman Stage

```text
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
```

---

## ▶️🚀 How to Run

1️⃣ Save all files inside the same folder 📂  

2️⃣ Run the game:

```bash
python hangman.py
```

3️⃣ Click letters to guess the hidden word 🔠  

4️⃣ Restart or quit after the game ends 🔄❌  

---

## 📋📝 Requirements

✅ Python 3.x  
✅ Tkinter (usually pre-installed with Python)

---

## ⚠️📌 Notes

- 🔠 Letter buttons become disabled after being clicked
- 🎲 Words are randomly selected each game
- 💀 Incorrect guesses reduce lives
- 🔄 Restart resets the game completely

---

## 🎯📚 Learning Concepts

This project demonstrates:

- 🐍 Python GUI programming  
- 🖼️ Tkinter widgets and layouts  
- 🎲 Random word generation  
- 🔠 String and list manipulation  
- 🔁 Event-driven programming  
- 🧠 Functions and state management  
- 🎮 Game development fundamentals  

---

## 👨‍💻📅 Author

Created as an interactive **Hangman Game** using **Python** and **Tkinter** 🐍🎮
