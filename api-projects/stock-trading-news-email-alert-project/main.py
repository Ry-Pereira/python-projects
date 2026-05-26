#Name: Ryan Pereira
#Project Name: Stock Trade News Alert Email Sender
#Module Name: Main
#Module Purpose: The moudle is the main entry point into the project, and is responsible for executing the main function, which is the main entry point into the program. The main function is responsible for calling other functions to add new stocks to track, check the stock list, get stock data, get news data, and send emails with news articles related to the stock if there is a significant change in the stock price. The main function also has a user input to ask if the user wants to add a new stock to track, and if so, it calls the add stock data function. The main function also calls the check stock list function to check the stock list and retrieve the latest stock data and news data for each stock in the list.
#Description: The program is designed to track stock data for specific stocks, and then send an email with news articles related to the stock if there is a significant change in the stock price. The program retrieves stock data from the Alpha Vantage API, and news data from the News API. The program also allows the user to add new stocks to track by inputting the stock ticker name and company name, which is then stored in a csv file. The program checks for duplicates before adding new stocks to the csv file. The program also has a function to check the stock list and retrieve the latest stock data and news data for each stock in the list. The program sends an email with the news articles if there is a significant change in the stock price, with the subject of the email indicating the percentage change in the stock price.
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 6/27/2026
#Last Modified: 6/29/2026 

#Importing the requests module, in order for API retrieval,storing, and accessing to be made possible.
from multiprocessing.dummy import connection
#Importing the requests module, in order for API retrieval,storing, and accessing to be made possible.
import requests
#Importing the pandas library for data manipulation and analysis, with primarily working on csv info
import pandas
#Importing the time module, in order for the program to have the ability to use time related functions, such as sleep, which is used to delay the execution of the program for a certain amount of time, which is used in the check stock list function to delay the execution of the program for 2 seconds between each stock in the stock list, to avoid hitting the API rate limit and to avoid overwhelming the user with too much information at once.
import time
#Importing the datetime and timedelta classes from the datetime module, in order for the program to have the ability to work with dates and times, such as getting the current date and time, and calculating the date for yesterday and the day before yesterday, which is used in the get stock data function to retrieve the stock data for yesterday and the day before yesterday, and in the get news data function to retrieve news articles from yesterday and the day before yesterday.
from datetime import datetime, timedelta
#Importing smtplib module, in order for Simple Mail Transfer protocol to work, in sending Emails
import smtplib




#EMAIL and PASSWORD variables are set to empty strings, which will be used to store the email address and app password for sending emails with the smtplib module. The user will need to input their email address and app password in these variables in order for the program to be able to send emails.
EMAIL = ""
PASSWORD = ""




#Stock data key and news api key variables are set to the API keys for the Alpha Vantage API and the News API, which are used to retrieve stock data and news data from the respective APIs. The user will need to input their own API keys in these variables in order for the program to be able to retrieve stock data and news data from the APIs.
stock_data_key = "KUMA43H9MFPK7SVE"
news_api_key = "ac096e631d564a83bed1ed2951d87969"




#Defining a function to get stock data, with the parameter of stock ticker name, which is the stock ticker symbol for the stock that is being tracked, such as AAPL for Apple, MSFT for Microsoft, etc.
def get_stock_data(stock_ticker_name: str) -> dict:
    #Stock API is set to a string with the url for the stock API, with the function of TIME_SERIES_DAILY, and the symbol set to the stock ticker name parameter, and the apikey set to the key variable
    stock_api = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_ticker_name}&apikey={key}'
    #Response is set to the result of the requests get function with the url parameter set to the stock API variable
    response = requests.get(url=stock_api)
    #Data is set to the result of the response json function, which converts the response to a json format
    data = response.json()
    
    #Yesterday is set to the result of the datetime now function minus the result of the timedelta function with days set to 1, and then the date function is called on that result, which gives the date for yesterday
    yesterday = datetime.now() - timedelta(days=1).date()
    #Yesterday before is set to the result of the datetime now function minus the result of the timedelta function with days set to 2, and then the date function is called on that result, which gives the date for the day before yesterday
    yesterday_before = datetime.now() - timedelta(days=2).date()
    #Time series data yesterday is set to the result of the response json function with the key of "Time Series (Daily)" and then the key of yesterday, which gives the stock data for yesterday
    time_series_data_yesterday = response.json()["Time Series (Daily)"][str(yesterday)]
    #Time series data yesterday before is set to the result of the response json function with the key of "Time Series (Daily)" and then the key of yesterday before, which gives the stock data for the day before yesterday
    time_series_data_yesterday_before = response.json()["Time Series (Daily)"][str(yesterday_before)]
    #Stock tracker list is set to the result of the pandas read csv function with the parameter of the stock list csv file, which gives a dataframe of the stock list csv file
    stock_tracker_list = pandas.read_csv('stock_list.csv')
    #The stock tracker list dataframe is updated with the new stock data for yesterday and the day before yesterday, with the loc function to locate the row with the stock ticker name, and then the columns for open price yesterday, close price yesterday, open price yesterday before, and close price yesterday before are set to the corresponding values from the time series data for yesterday and the day before yesterday
    stock_tracker_list.loc[stock_tracker_list['Ticker'] == stock_ticker_name,"Open_Price_Yesterday","Close_Price_Yesterday","Open_Price_Yesterday_Before","Close_Price_Yesterday_Before"] = time_series_data_yesterday["1. open"],time_series_data_yesterday["4. close"],time_series_data_yesterday_before["1. open"],time_series_data_yesterday_before["4. close"]
    #The stock tracker list dataframe is then saved back to the stock list csv file with the to csv function, with the header set to false and the index set to false to avoid adding an index column and a header row to the csv file
    stock_tracker_list.to_csv("stock_list.csv",header=False,index=False)






#Defining a function to add stock data, which is used to add new stocks to track by inputting the stock ticker name and company name, which is then stored in a csv file. The function also checks for duplicates before adding new stocks to the csv file, by calling the check for stock duplicates function with the stock ticker name and company name as parameters, and if there are no duplicates, it adds the new stock data to the csv file with the to csv function, with the mode set to "a" to append the new stock data to the existing csv file, and with the header set to false and the index set to false to avoid adding an index column and a header row to the csv file.
def add_stock_data() -> None:
    #Stock ticker name is set to the result of the input function with the prompt "Stock Ticker Name: ", which allows the user to input the stock ticker name for the stock they want to track
    stock_ticker_name = str(input("Stock Ticker Name: "))
    #Stock company name is set to the result of the input function with the prompt "Stock Company Name: ", which allows the user to input the stock company name for the stock they want to track
    stock_company_name = str(input("Stock Company Name: "))

    #New stock list info is set to a new dataframe with the columns of Ticker, Company, Open Price, Close Price, High Price, and Low Price, and the values for the Ticker and Company columns are set to the stock ticker name and stock company name variables, and the values for the Open Price, Close Price, High Price, and Low Price columns are set to 0.00 as placeholders until the stock data is retrieved from the API in the get stock data function
    new_stock_list_info = pandas.DataFrame({
        "Ticker":[stock_ticker_name],
        "Company":[stock_company_name],
        "Open Price":[0.00],
        "Close Price":[0.00],
        "High Price":[0.00],
        "Low Price":[0.00]
    })
    #The check for stock duplicates function is called with the stock ticker name and stock company name as parameters, and if the function returns false, which means there are no duplicates, the new stock list info dataframe is appended to the stock list csv file with the to csv function, with the mode set to "a" to append the new stock data to the existing csv file, and with the header set to false and the index set to false to avoid adding an index column and a header row to the csv file.
    if check_for_stock_duplicates(stock_ticker_name,stock_company_name) == False:
        #New stock list info dataframe is appended to the stock list csv file with the to csv function, with the mode set to "a" to append the new stock data to the existing csv file, and with the header set to false and the index set to false to avoid adding an index column and a header row to the csv file.
        new_stock_list_info.to_csv("stock_list.csv",mode="a",header=False,index=False)





#Defining a function to check the stock list, which is used to check the stock list and retrieve the latest stock data and news data for each stock in the list. The function reads the stock list csv file with the pandas read csv function, and then iterates through each stock in the stock list with a for loop, and for each stock, it prints the stock ticker name, company name, and close price, and then calls the get stock data function with the stock ticker name as a parameter to retrieve the latest stock data for that stock, and then calls the get news data function with the company name as a parameter to retrieve the latest news data for that company. The function also has a time sleep of 2 seconds between each stock in the stock list to avoid hitting the API rate limit and to avoid overwhelming the user with too much information at once.
def check_stock_list() -> None:
    #Stock dataframe is set to a dataframe from pandas executing the read csv function on the stock list csv file, which gives a dataframe of the stock list csv file
    stock_dataframe = pandas.read_csv("stock_list.csv")
    #For loop in iterating through the stock tuple rows with no regard of index inclusion, and for each stock, it prints the stock ticker name, company name, and close price, and then calls the get stock data function with the stock ticker name as a parameter to retrieve the latest stock data for that stock, and then calls the get news data function with the company name as a parameter to retrieve the latest news data for that company. The function also has a time sleep of 2 seconds between each stock in the stock list to avoid hitting the API rate limit and to avoid overwhelming the user with too much information at once.
    for stock in stock_dataframe.itertuples(index=False):
        #Time sleep of 2 seconds between each stock in the stock list to avoid hitting the API rate limit and to avoid overwhelming the user with too much information at once.
        time.sleep(2)
        #Gets the stock ticker name, company name, and close price for each stock in the stock list and prints them to the console
        get_stock_data(stock.Ticker)
        #Gets the news data for each stock in the stock list by calling the get news data function with the company name as a parameter to retrieve the latest news data for that company.
        get_news_data(stock.Company)





#Defining a function to check the stock track list, to see if the paramater input for Ticker name and company name to check make any duplicates, returns true or false
def check_for_stock_duplicates(ticker_name_to_check: str,stock_company_to_check: str) -> bool:
    #Stock datafram is set to a dtarame from pandas executing the read csv function on the csv file
    stock_dataframe = pandas.read_csv("stock_list.csv")
    #For loop in iterating through the stcok tuple rows with no regard of index inclusion
    for stock in stock_dataframe.itertuples(index=False):
        #If the stocker Ticker or Company value is equal to either the ticker or stock company to check, there is a duplicate
        if stock.Ticker == ticker_name_to_check or stock.Company == stock_company_to_check:
            #Returns True to indicate there is a duplicate
            return True
    #Returns False to indicate there is no duplicate
    return False
        




#Defining a function to get news data, with the parameter of company name, which is the company name for the stock that is being tracked, such as Apple for AAPL, Microsoft for MSFT, etc. The function retrieves news articles from yesterday and the day before yesterday, and then formats the news articles into a message string that can be sent in an email.
def get_news_data(company_name: str) -> str:
    #Yesterday is set to the result of the datetime now function minus the result of the timedelta function with days set to 1, and then the date function is called on that result, which gives the date for yesterday
    yesterday = (datetime.now() - timedelta(days=1)).date()
    #Yesterday before is set to the result of the datetime now function minus the result of the timedelta function with days set to 2, and then the date function is called on that result, which gives the date for the day before yesterday
    yesterday_before = (datetime.now() - timedelta(days=2)).date()
    #News API previous days is set to a string with the url for the news API, with the q parameter set to the company name parameter, and the from parameter set to yesterday before, and the to parameter set to yesterday, and the sort by parameter set to popularity, and the api key parameter set to the news api key variable
    news_api_previous_days = f"https://newsapi.org/v2/top-headlines?q={company_name}&from={yesterday_before}&to={yesterday}&sortBy=popularity&apiKey={news_api_key}"
    #Response is set to the result of the requests get function with the url parameter set to the news API previous days variable
    response = requests.get(url=news_api_previous_days)
    #Data is set to the result of the response json function, which converts the response to a json format
    data = response.json()
    #News message is set to an empty string, which will be used to store the formatted news articles that can be sent in an email
    news_message = ""

    #For loop in iterating through the article info sections in the data with the key of "articles", and for each article info section, it formats the news article into a message string that can be sent in an email, with the source name, author, title, description, and url of the news article, and then adds a newline character to separate each news article in the message string.
    for article_info_section in data["articles"]:
        #Formats the news article into a message string that can be sent in an email, with the source name, author, title, description, and url of the news article, and then adds a newline character to separate each news article in the message string.
        news_message+= "Source: " + article_info_section["source"]["name"] + "\n"
        #Adds the author of the news article to the news message string with the key of "author" in the article info section, and then adds a newline character to separate each news article in the message string.
        news_message += "Author: " + article_info_section["author"] + "\n"
        #Adds the title of the news article to the news message string with the key of "title" in the article info section, and then adds a newline character to separate each news article in the message string.
        news_message += "Title: " + article_info_section["title"] + "\n"
        #Adds the description of the news article to the news message string with the key of "description" in the article info section, and then adds a newline character to separate each news article in the message string.
        news_message += "Description: " + article_info_section["description"] + "\n"
        #Adds the url of the news article to the news message string with the key of "url" in the article info section, and then adds a newline character to separate each news article in the message string.
        news_message += "URL: " + article_info_section["url"] + "\n"
        #Adds a newline character to separate each news article in the message string.
        news_message += "\n\n"
    #Returns the news message string that contains the formatted news articles that can be sent in an email.
    return news_message
    




#Defining a function to send an email with the news articles related to the stock if there is a significant change in the stock price, with the parameters of company name and news message, which are used to format the email message with the subject indicating the percentage change in the stock price, and the body containing the news articles related to the stock. The function uses the smtplib module to send an email from the specified email address to the specified email address with the formatted message.
def send_email(company_name: str, news_message: str) -> None:
    #Connection is set to the result of the smtplib SMTP function with the parameter of the smtp server for gmail and the port number for tls, which creates a connection to the smtp server for sending emails
    stock_and_company_dataframe = pandas.read_csv("stocks_list.csv")
    #Stock and company dataframe is set to the result of filtering the stock and company dataframe with the condition that the Date column is equal to the company name parameter, which gives a dataframe of the stock and company information for the specified company name
    stock_and_company = stock_and_company_dataframe[(stock_and_company_dataframe.Date == "company_name")]
    #For loop in iterating through the stock and company tuple rows with no regard of index inclusion, and for each stock info section, it formats the email message with the subject indicating the percentage change in the stock price, and the body containing the news articles related to the stock, and then sends an email from the specified email address to the specified email address with the formatted message using the smtplib module.
    for stock_info_section in stock_and_company.ittrtuples(index=False):
        #TLS starts for transport layer security
        full_message = f"Subject:{company_name} has a ({stock_info_section.Close_Price_Yesterday}-{stock_info_section.Close_Price_Yesterday_Before})\n\n{news_message}"
        #Full message bytes is set to full message is encoded
        full_message_bytes = full_message.encode("utf-8")
        #Conection starts for transport layer security
        connection.starttls()
        #Connection requring a login with user set to email address and password to app password
        connection.login(user=EMAIL,password=PASSWORD)
        #Conneection to send email from address to my email addres and to addres to my addres with mesg set to hello, have SUbject: to have subject in there
        connection.sendmail(from_addr=EMAIL,to_addrs=EMAIL,msg=full_message_bytes)
        #Closes the connection
        connection.close()
    

    
    
#Defining the main function, the main enry point into the project program.
def main() -> None:
    #User question is set to the result of the input function with the prompt "Do you wish to add a new stock to track(y/n?)", which allows the user to input whether they want to add a new stock to track or not, and if they input "y", the add stock data function is called to allow them to add a new stock to track.
    user_question = input("Do you wish to add a new stock to track(y/n?)")
    #If the user input is "y", the add stock data function is called to allow them to add a new stock to track.
    if user_question == "y":
        #The add stock data function is called to allow the user to add a new stock to track by inputting the stock ticker name and company name, which is then stored in a csv file. The function also checks for duplicates before adding new stocks to the csv file, by calling the check for stock duplicates function with the stock ticker name and company name as parameters, and if there are no duplicates, it adds the new stock data to the csv file with the to csv function, with the mode set to "a" to append the new stock data to the existing csv file, and with the header set to false and the index set to false to avoid adding an index column and a header row to the csv file.
        add_stock_data()

    #Check stock list function is called to check the stock list and retrieve the latest stock data and news data for each stock in the list, and then send an email with the news articles related to the stock if there is a significant change in the stock price, with the subject of the email indicating the percentage change in the stock price.
    check_stock_list()

    



#If the program is being run directly, the main function will be executed
if __name__ == "__main__":
    #The main function is executed
    main()
