# 🔐🔑 Caesar Cipher Program 🔑🔐

## 📌 Overview

This project is a Python-based Caesar Cipher application that allows users to encrypt 🔒 and decrypt 🔓 words using a shift-based substitution cipher. The program uses a menu-driven interface where users can choose to cipher text, decipher text, or exit the program 🚪.

The project also includes a supporting module that stores:
* 🔤 The alphabet list used for shifting letters  
* 🎨 ASCII art displayed at program startup  

Users can:
* 🔐 Encrypt words using a custom shift amount  
* 🔓 Decrypt encrypted words  
* 🖥️ Interact with the program through a simple console menu  

---

## 🧱 Project Structure 🗂️

```text
project-folder/
│
├── caesar_cipher.py        # 🔐 Main Caesar Cipher program
├── art_and_alphabet.py     # 🔤 Module containing alphabet list and ASCII art
└── README.md               # 📘 Project documentation
```

---

## 🚀 Features ✨

* 🔐 Encrypts words using Caesar Cipher logic  
* 🔓 Decrypts ciphered words  
* 🔢 Customizable shift amount  
* 📋 Menu-driven user interface  
* 🔁 Uses lists, loops, functions, and indexing  
* 🎨 Displays ASCII art banner at startup  

---

## 🛠️ Technologies Used 💻

* 🐍 Python  
* ⌨️ Console input/output (`input()` and `print()`)  
* ⚙️ Functions and loops  
* 🔤 Lists and string manipulation  

---

## 📡 Program Logic 🧠

### 🔐 Ciphering Process

The program works by:

1. ⌨️ Asking the user for a word to encrypt  
2. 🔢 Asking for a shift amount  
3. 🔍 Finding each letter’s index in the alphabet list  
4. ➡️ Shifting the index forward by the shift amount  
5. 🔄 Wrapping around the alphabet if needed  
6. 🧩 Building and displaying the encrypted word  

### 🔓 Deciphering Process

The decipher function:

1. 📥 Takes an encrypted word  
2. ⬅️ Subtracts the shift amount from each letter index  
3. 🔄 Wraps around the alphabet if needed  
4. 🧩 Rebuilds and prints the decrypted word  

---

## ▶️ How to Run the Project 🚀

1. 🐍 Make sure Python is installed on your computer  

2. 📂 Place both files in the same project folder:
   * `caesar_cipher.py`
   * `art_and_alphabet.py`

3. ▶️ Run the program:

```bash
python caesar_cipher.py
```

4. 📋 Choose one of the menu options:
   * `1` → 🔐 Cipher Code
   * `2` → 🔓 Decipher Code
   * `3` → 🚪 Exit Program

5. ⌨️ Enter the word and shift amount when prompted

---

## 📅 Project Info 📌

**👨‍💻 Author:** Ryan Pereira  
**📅 Created:** 2/10/2023  
**🛠️ Last Modified:** 2/13/2023  

---

## 📬 Contact ✉️

Feel free to open an issue or suggest improvements 💡
