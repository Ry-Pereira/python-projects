#Name: Ryan Pereira
#Project Name: Graph Pixel Tracker
#Module Name: Main
#Module Purpose: The moudle is the main entry into the program. It will ask the user for all the necessary information to create a graph and update it. It will also allow the user to edit and delete pixels from the graph.
#Description: A Graph Pixel Tracker is a tool that allows users to track their habits and activities by creating a graph of pixels. Each pixel represents a day and the color of the pixel represents the quantity of the activity. The user can update the graph by adding new pixels, editing existing pixels, and deleting pixels. The graph can be used to visualize the user's progress and motivate them to continue their habits.
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 6/30/2026
#Last Modified: 6/30/2026

#This program uses the Pixela API to create a graph and track habits. The user will be prompted to enter their username, token, and other necessary information to create a graph. The user can then update the graph by adding new pixels, editing existing pixels, and deleting pixels. The program will use the requests library to make API calls to the Pixela API.
import requests
#The datetime module is used to get the current date in the format of YYYYMMDD, which is required by the Pixela API when creating and updating pixels.
import datetime as dt

#The user is prompted to enter their username, token, and whether they are a minor. This information is necessary to create a user account on the Pixela platform and to authenticate API requests. The token is a unique identifier that allows the user to access their account and manage their graphs and pixels.
DATE_TODAY = dt.datetime.now().strftime("%Y%m%d")
USERNAME = input("Enter you username: ")
TOKEN = input("Enter your own custom token: ")
IS_MINOR = input("Are you minor? (yes/no): ")

#Pixela API endpoint for creating a user. The user will be created with the provided username and token. The user must agree to the terms of service and confirm that they are not a minor to create an account.
pixela_endpoint = "https://pixe.la/v1/users"
#The user parameters are stored in a dictionary that will be sent as a JSON payload in the API request to create a user. The parameters include the token, username, agreement to terms of service, and confirmation of not being a minor.
user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":IS_MINOR
}


#Running the response again, you will get error, because you already initialized the user with same username and token.
response = requests.post(url=pixela_endpoint, json=user_parameters)

# Prompts user to enter a unique graph ID for Pixela
GRAPH_ID = input("Give your graph an id: ")
# Prompts user to enter a name for the graph
GRAPH_NAME = input("Give your graph a name: ")
# Prompts user to define the type of data stored in the graph (int or float)
GRAPH_TYPE = input("Give a type for your graph (int/float): ")
# Prompts user to define the unit of measurement for the graph data
GRAPH_DATA_UNIT = input("Give a unit for your graph: ")
# Prompts user to choose a color for the graph visualization
GRAPH_COLOR = input("Give a color for your graph: ")
# Builds the API endpoint URL for creating a new graph under the user account
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# Dictionary containing configuration settings for the new graph


graph_config = {
    "id": GRAPH_ID,
    "name": GRAPH_NAME,
    "unit": GRAPH_DATA_UNIT,
    "type": GRAPH_TYPE,
    "color": GRAPH_COLOR
}


# Headers used for authentication when sending requests to Pixela API
headers ={
    "X-USER-TOKEN": TOKEN
}


# Sends a POST request to create the graph using provided configuration
response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# Prints the response from the graph creation request
print(response)
# Prompts user to enter the quantity value for today's pixel
GRAPH_PIXEL_UPDATED_QUANTITY = input("Give a quantity for your graph pixel: ")
# Builds endpoint URL for updating/adding today's pixel value
update_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# Dictionary containing pixel data for today's entry
update_graph_config ={
    "date": DATE_TODAY,
    "quantity": GRAPH_PIXEL_UPDATED_QUANTITY
}


# Sends POST request to add a new pixel entry to the graph
response = requests.post(url=update_graph_endpoint,json=update_graph_config,headers=headers)
# Prints response from pixel creation request
print(response)
# Prompts user to enter a new quantity value to edit today's pixel
GRAPH_PIXEL_EDIT_PIXEL_QUANTITY = input("Give a quantity for your graph pixel: ")
# Builds endpoint URL for updating an existing pixel entry
update_graph_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE_TODAY}"
# Dictionary containing updated pixel quantity
update_graph_pixel_config = {
    "quantity": GRAPH_PIXEL_EDIT_PIXEL_QUANTITY
}


# Sends PUT request to update an existing pixel value
response = requests.put(url=update_graph_pixel,json=update_graph_pixel_config,headers=headers)
# Prints response from pixel update request
print(response)
# Prompts user to enter a date for the pixel they want to delete
GRAPH_DATE_PIXEL_TO_DELETE = input("Give a date for your graph pixel to delete (YYYYMMDD): ")
# Builds endpoint URL for deleting a specific pixel
delete_graph_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{GRAPH_DATE_PIXEL_TO_DELETE}"
# Sends DELETE request to remove the selected pixel
response = requests.delete(url=delete_graph_pixel, headers=headers)
# Prints response from delete request
print(response)
