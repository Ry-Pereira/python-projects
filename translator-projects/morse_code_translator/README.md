# 📡 Morse Code Translator Program

## 📌 Overview

This project is a Python-based Morse Code Translator that allows users to convert normal text into Morse code and decode Morse code back into readable text. The program uses a dictionary-based mapping system along with a menu-driven interface to interact with the user.

Users can:
* 🔤 Convert text into Morse code  
* 📡 Convert Morse code back into text  
* 📖 View the full Morse code alphabet and numbers  
* 🚪 Exit the program safely  

The project also includes an external module that stores:
* 🎨 ASCII welcome banner  
* 🔤 Morse code dictionary (alphabet and numbers mapping)  

---

## 🧱 Project Structure

```text
project-folder/
│
├── morse_code_translator.py   # Main program (logic + menu system)
├── art.py                     # ASCII art + Morse code dictionary
└── README.md                  # Project documentation
```

---

## 🚀 Features

* 🔤 Convert text → Morse code  
* 📡 Convert Morse code → text  
* 📖 Display full Morse code alphabet & numbers  
* 🧠 Dictionary-based encoding system  
* 🔁 Loop-based menu navigation  
* 🎨 ASCII art welcome screen  

---

## 🛠️ Technologies Used

* 🐍 Python  
* 📚 Dictionaries (key-value mapping)  
* 🔁 Loops (for iteration and menu handling)  
* ⌨️ Console input/output (`input()` and `print()`)  
* 📦 Modular programming (separate `art.py` file)  

---

## 📡 Program Logic

### 🔤 Text → Morse Code

1. Program reads user input text  
2. Converts text to lowercase  
3. Checks each character in dictionary  
4. Replaces letters/numbers with Morse code equivalents  
5. Uses `/` to represent spaces between words  
6. Outputs full Morse code string  

---

### 📡 Morse Code → Text

1. Program splits Morse code input by spaces  
2. Reads each Morse symbol  
3. Matches it back to dictionary keys  
4. Converts `/` back into spaces  
5. Outputs readable text  

---

### 📖 Morse Code Reference Feature

* Displays all letters and numbers stored in the dictionary  
* Helps users learn Morse code easily  

---

## ▶️ How to Run the Project

1. Make sure Python is installed 🐍  

2. Ensure both files are in the same folder:
   * `morse_code_translator.py`
   * `art.py`

3. Run the program:

```bash
python morse_code_translator.py
```

4. Choose an option from the menu:
   * `1` → 🔤 Text to Morse Code  
   * `2` → 📡 Morse Code to Text  
   * `3` → 📖 Show Morse Code Alphabet & Numbers  
   * `4` → 🚪 Exit Program  

5. Follow the prompts to enter your input  

---

## 📅 Project Info

**👨‍💻 Author:** Ryan Pereira  
**📅 Created:** 5/10/2026  
**🛠️ Last Modified:** 5/10/2026  

---

## 📬 Contact

Feel free to open an issue or suggest improvements 🚀
