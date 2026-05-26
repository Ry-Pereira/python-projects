#Name: Ryan Pereira
#Project Name: Birthday Wish Email Sender
#Module Name: Main
#Module Purpose: The moudle is the main entry into the program.
#Description: A Birthay Wish Email sender
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 6/23/2026
#Last Modified: 6/26/2026


#Importing the datetime module as dt, to get all the information for getting world time functions and variables
import datetime as dt
#Importing the pandas library for data manipulation and analysis, with primarily working on csv info
import pandas
#Importing the random module in order to be able to be randomly choose from the letters list
import random
#Importing smtplib module, in order for Simple Mail Transfer protocol to work, in sending Emails
import smtplib

#EMAIL constant variable set to empty string
EMAIL = ""
#PASSWORD constant variable set to empty string
PASSWORD = ""
#TO ADDRESS constant variable set to empty string
TO_ADDRESS = ""
#YOUR NAME constant variable set to empty string
YOUR_NAME = ""


#Letters list set to a list of letter text documents
letters_list = ["letter1.txt","letter2.txt","letter3.txt","letter4.txt"]


#Defining the store birthday info function
def store_birthday_info()-> None:
    #Birthday year is set to the integer casting of asking the user for the year of their birth of the person they want to log in
    birthday_year = int(input("Year of Birth: "))
    #Birthday month is set to the integer casting of asking the user for the month of their birth of the person they want to log in
    birthday_month = int(input("Month of Birth: "))
    #Birthday day is set to the integer casting of asking the user for the day of their birth of the person they want to log in
    birthday_day = int(input("Day of Birth: "))
    #Birthday first name is set to the string casting of asking the user for the first name of the birth of the person they want to log in 
    birthday_first_name = str(input("Birthday First Name: "))
    #Birthday last name is set to the string casting of asking the user for the last name of the birth of the person they want to log in 
    birthday_last_name = str(input("Birthday Last Name: "))
    #Birthday email is set to the string casting of asking the user for the email of the birth of the person they want to log in 
    birthday_email = str(input("Birthday Email To Send: "))

    
    #New birthday info is set to a pandas dataframe with the birthday information aquired, set to the data belongings
    new_birthday_info = pandas.DataFrame({
        "First_Name": [birthday_first_name],
        "Last_Name": [birthday_last_name],
        "Email": [birthday_email],
        "Year": [birthday_year],
        "Month":[birthday_month],
        "Day":[birthday_day]
    })
    #The new birthday infor executes the to csv method, with being appended to the birthdays.csv, as a row, with no exact index set
    new_birthday_info.to_csv("birthdays.csv",mode="a",header=False,index=False)
   
#Defining a check for birthdays function
def check_for_birthdays()-> pandas.DataFrame:
    #Date noew is set to the date and time that is today now
    date_now = dt.datetime.now()
    #Birtday dataframe is set to the dataframe object value of panadas executing the read csv function with birthdays.csv as input
    birthday_dataframe = pandas.read_csv("birthdays.csv")
    #Birthdays today is a datframe value taken from the condition from the birthdays dataframe where is there is a row where the year,month, and day match today
    birthdays_today = birthday_dataframe[(birthday_dataframe.Month == date_now.month) & (birthday_dataframe.Day == date_now.day)]
    #Returns the birthdays today dataframe
    return birthdays_today

    
#Defining a send email function with birthdays as input
def send_email(birthdays:pandas.DataFrame) -> None:
    #For birthday row in the  birthdays dataframe rows, with index hidden
    for birthday_row in birthdays.itertuples(index=False):
        #A random letter is randomly chosen from the letters list
        random_letter = random.choice(letters_list)
        #With open the random letter text document, in read mode, with alias as file
        with open(random_letter, "r") as file:
            #File lines is set to file readlines, to get tall the lines in the file as alist
            file_lines = file.readlines()
            #Message set to empty string
            message = ''
            #For line in file lines
            for line in file_lines:
                #Line is set to line,replace the string,[First Name], to birthday_row.First_Name value
                line = line.replace("[First Name]",birthday_row.First_Name)
                #Line is set to line,replace the string,[Last Name], to birthday_row.Last_Name value
                line = line.replace("[Last Name]",birthday_row.Last_Name)
                #Line is set to line,replace the string,[Your Name], to YOUR_Name value
                line = line.replace("[Your Name]",YOUR_NAME)
                #Line is set to line,replace the string,[Date], to birthday_row.Year value
                line = line.replace("[Date]",str(birthday_row.Year))
                #Line is set to line,replace the string,[Years turning], to (2026 - birthday_row.Year) value
                line = line.replace("[Years turning]",str(2026-birthday_row.Year))
                #Message is incremented with line string
                message += line
            
        #Full message is set to the f-string of subject set to birthday wish, with new linews, and the message
        full_message = f"Subject:Birthday Wish\n\n{message}"
        #Full message bytes is set to full message is encoded
        full_message_bytes = full_message.encode("utf-8")

        #Birthday mail provider list is set to birthday row Email splitted by the @ string character
        birthday_mail_provider_list = birthday_row.Email.split("@")
        #Valid email provider is set to False
        valid_email_provider = False
        #If the birthday mail provider at first index is set to gmail.com string
        if birthday_mail_provider_list[1] == "gmail.com":
            # A way to connect to connect to email provider.SMTP providerer is diffrent for very email rpiver, since mine ends in gmail, then it smtp.gmail.com
            connection = smtplib.SMTP("smtp.gmail.com")
            #Valid email provider set to true
            valid_email_provider = True
        #Elif the birthday mail provider at first index is set to yahoo.com string
        elif birthday_mail_provider_list[1] == "yahoo.com":
            # A way to connect to connect to email provider.SMTP providerer is diffrent for very email rpiver, since mine ends in gmail, then it smtp.yahoo.com
            connection = smtplib.SMTP("smtp.mail.yahoo.com")
             #Valid email provider set to true
            valid_email_provider = True
        #Elif the birthday mail provider at first index is set to outlook.com string
        elif birthday_mail_provider_list[1] == "outlook.com":
            # A way to connect to connect to email provider.SMTP providerer is diffrent for very email rpiver, since mine ends in gmail, then it smtp.office365.com
            connection = smtplib.SMTP("smtp.mail.office365.com")
             #Valid email provider set to true
            valid_email_provider = True

        #If the valid email provider is  True
        if valid_email_provider == True:
            #TLS starts for transport layer security
            connection.starttls()
            #Connection requring a login with user set to email address and password to app password
            connection.login(user=EMAIL,password=PASSWORD)
            #Conneection to send email from address to my email addres and to addres to my addres with mesg set to hello, have SUbject: to have subject in there
            connection.sendmail(from_addr=EMAIL,to_addrs=birthday_row.Email,msg=full_message_bytes)
            #Closes the connection
            connection.close()




#Defining the main function, the entry point into the project program
def main() -> None:
    #User_answer stores the input from the question if the user wants to store any birthday information
    user_answer = input("Do you want store any birthday information(y/n?")
    #If user answer is equal to y character string, 
    if user_answer == "y":
        #Exexcutes the store birthday info function to get birthday info to store into the birthdays csv
        store_birthday_info()
    #birthday holds the value of a datframe of the buirthdays that are current today from the check for birthdays function
    birthdays = check_for_birthdays()
    #Executes the send_email function with birthdays as input, to go through each birthday and send a eamil according to each of its own information
    send_email(birthdays)

    
    

    
       

#If the program is being run directly, then the main program will be executed        
if __name__ == "__main__":
    #Main function is executed
    main()
