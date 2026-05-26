# 🎂📧 Birthday Wish Email Sender 📧🎂

## 📌 Description

This project is an automated **Birthday Wish Email Sender** built using **Python** 🐍.  
The program checks a `birthdays.csv` file daily and automatically sends personalized birthday emails 🎉 to people whose birthday matches the current date.

The application randomly selects a birthday letter template from multiple text files and customizes the message using the recipient’s information.

---

## ✨🚀 Features

✅ Store birthday information in a CSV file  
✅ Automatically detect birthdays for the current day 📅  
✅ Send personalized birthday emails 📧  
✅ Randomly choose from multiple birthday templates 🎲  
✅ Replace placeholders dynamically 🔄  
✅ Supports Gmail, Yahoo, and Outlook SMTP servers 🌐  
✅ Beginner-friendly Python automation project 🐍  

---

## ⚙️🧠 How It Works

1️⃣ User stores birthday information in `birthdays.csv`  

2️⃣ Program checks today's date using Python `datetime` 📅  

3️⃣ If a birthday matches today's month and day:
- A random birthday template is selected 🎲
- Placeholders are replaced with actual data 📝
- A personalized email is generated 📧

4️⃣ The email is sent automatically using SMTP 🌐

---

## 🛠️💻 Technologies Used

- 🐍 Python 3
- 📊 Pandas
- 📅 Datetime
- 🎲 Random
- 📧 SMTP (Simple Mail Transfer Protocol)

---

## 📂🧱 Project Structure

```text
project-folder/
│
├── main.py             # Main program file
├── birthdays.csv       # Stores birthday data
├── letter1.txt         # Birthday template 1
├── letter2.txt         # Birthday template 2
├── letter3.txt         # Birthday template 3
├── letter4.txt         # Birthday template 4
│
└── README.md
```

---

## 📄 birthdays.csv Format

The CSV file must contain the following columns:

```text
First_Name,Last_Name,Email,Year,Month,Day
```

### Example

```csv
First_Name,Last_Name,Email,Year,Month,Day
John,Doe,johndoe@gmail.com,2000,6,26
Jane,Smith,janesmith@yahoo.com,1998,12,15
```

---

## ✉️ Letter Template Format

Each letter template (`letter1.txt`, `letter2.txt`, etc.) can contain placeholders:

```text
Happy Birthday [First Name]!

Wishing you an amazing birthday and a wonderful year ahead 🎉

You are turning [Years turning] today!

Best wishes,
[Your Name]
```

---

## ▶️🚀 How to Run

1️⃣ Install required libraries:

```bash
pip install pandas
```

2️⃣ Configure your email credentials inside `main.py`

```python
EMAIL = "your_email@gmail.com"
PASSWORD = "your_app_password"
YOUR_NAME = "Your Name"
```

3️⃣ Run the program:

```bash
python main.py
```

---

## 📋📝 Requirements

✅ Python 3.x  
✅ Pandas Library  
✅ Internet connection 🌐  
✅ Valid email credentials 📧  

---

## ⚠️📌 Important Notes

- 📧 Gmail users should use an **App Password**
- ❌ Invalid email providers will not send emails
- 📅 Birthdays are checked using the current system date
- 🔒 Never share your email password publicly

---

## 🎯📚 Learning Concepts

This project demonstrates:

- 🐍 Python automation
- 📊 CSV file handling with Pandas
- 📧 Sending emails using SMTP
- 📅 Working with dates and time
- 🎲 Random template selection
- 🔄 String replacement and formatting
- 🧠 Functions and modular programming

---

## 👨‍💻📅 Author

Created as an automated birthday email sender project using **Python** 🐍📧🎂
