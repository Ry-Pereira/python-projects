#Name: Ryan Pereira
#Project Name: Kanye West Quote Generator
#Description:# A Tkinter-based program that fetches api data from a Kanye Quote source that distributes a random quote,quoted by Kanye West himself. Everytime the user clicks on the Kany West memoji icon, a new quote will appear in a random color speech bubble.
#Module Name: kanye_west_quote_data
#Module Purpose: The kany_west_quote_data is resposible for the repsonse fetching and storing to be used in the UI
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 6/19/2026
#Last Modified: 6/21/2026

#Importing the requests module, in order for API retrieval,storing, and accessing to be made possible.
import requests



#The function get response will get a response from the API address that contains a random quote from Kanye West and return the response and quote
def get_response() -> tuple:
    #Reponse is set to thhe API repsonse of getting the API info from the url address
    response = requests.get(url="https://api.kanye.rest")
    #Quote is seto the reponse, as the JSON file accessed, with the quote data being accessed
    quote = response.json()["quote"]
    #Status code of the response is stored
    status = response.status_code
    #Returns the response and quote,status
    return response,quote,status


