#Name: Ryan Pereira
#Project Name: Where Am I Locator Project
#Description: A program that retrieves location information from a user's public IP address and allows the user to view details such as location, coordinates, time zone, ISP information, and save reports.
#Module Name: where_am_i_locator_brain.py
#Module Purpose: Contains the WhereAmILocatorBrain class, which manages user interaction, menu navigation, data retrieval, report generation, and overall program functionality.
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 6/10/2026
#Last Modified: 6/12/2026

# Import function that retrieves the user's public IP address
# and function that retrieves location information from an IP address
from where_ami_i_locator_requests import get_ip_address, get_location_information_from_ip
#Importing art from where_am_i_locator_art.py
from where_am_i_locator_art import *
# Import datetime for displaying current time
from datetime import datetime
# Import ZoneInfo for timezone support
from zoneinfo import ZoneInfo


# Main class that controls the Where Am I Locator Program
class WhereAmILocatorBrain:

    # Displays the welcome message
    def display_welcome_message(self) -> None:
        #Print the welcome message to display for user.
        print("\nWelcome to the Where Am I Locator Program")
        print("Follow Directions to understnad how to use program.")


    # Displays the menu options
    def display_menu(self) -> None:
        #Print the menu for the display for the user.
        print("\n1.SHOW MY IP: ")
        print("2.SHOW MY LOCATION: ")
        print("3.SHOW MY COORDINATES: ")
        print("4.SHOW MY TIME ZONE: ")
        print("5.SHOW MY ISP: ")
        print("6.SAVE REPORT : ")
        print("7.EXIT OUT OF PROGRAM: ")


    # Displays a goodbye message
    def display_goodbye_message(self) -> None:
        #Print goodbye message for the display for the user.
        print("\nThankyou So much for using my program.")
        print("Please leave any feedback in the discussion r contact me otherwise. ")
        print("Goodbye!")



    # Returns the user's IP address
    def show_ip(self):
        #Ip address stores the result of the get ip address function call.
        ip_address = get_ip_address()
        #Reurns the ip address.
        return ip_address


    # Retrieves country, region, city, and zip code information
    # Retrieves address-related location information from the user's IP address
    def get_address_location_information(self):
        # Calls the function to obtain the user's public IP address
        ip_address = get_ip_address()
        # Uses the IP address to retrieve location information from the API
        user_location_address_infromation = get_location_information_from_ip(ip_address)
        # Extracts the country from the location information dictionary
        country_location = user_location_address_infromation["country"]
        # Extracts the state/region from the location information dictionary
        region_location = user_location_address_infromation["regionName"]
        # Extracts the city from the location information dictionary
        city_location = user_location_address_infromation["city"]
        # Extracts the ZIP/postal code from the location information dictionary
        zip_location = user_location_address_infromation["zip"]
        # Returns the country, region, city, and ZIP code as a tuple
        return country_location, region_location, city_location, zip_location


    # Retrieves latitude and longitude coordinates
    def get_coordinate_location_information(self):
        # Calls the function to obtain the user's public IP address
        ip_address = get_ip_address()
        # Uses the IP address to retrieve coordinate information from the API
        coordinates_location_infromation = get_location_information_from_ip(ip_address)
        # Extracts the latitude value from the location information dictionary
        latitude_coordinate_location = coordinates_location_infromation["lat"]
        # Extracts the longitude value from the location information dictionary
        longitude_coordinate_location = coordinates_location_infromation["lon"]
        # Returns the latitude and longitude coordinates as a tuple
        return latitude_coordinate_location, longitude_coordinate_location


    # Retrieves timezone and formatted local time
    def get_time_information(self):
        # Calls the function to obtain the user's public IP address
        ip_address = get_ip_address()
        # Uses the IP address to retrieve timezone information from the API
        time_infromation = get_location_information_from_ip(ip_address)
        # Extracts the timezone string from the location information dictionary
        timezone_location = time_infromation["timezone"]
        # Gets the current time in the retrieved timezone and formats it as HH:MM AM/PM
        formatted_time = datetime.now(ZoneInfo(time_infromation["timezone"])).strftime("%I:%M %p")
        # Returns the timezone and formatted local time as a tuple
        return timezone_location, formatted_time


    # Retrieves ISP information
    def get_isp_information(self):
        # Calls the function to obtain the user's public IP address
        ip_address = get_ip_address()
        # Uses the IP address to retrieve ISP-related information from the API
        isp_infromation = get_location_information_from_ip(ip_address)
        # Extracts the Internet Service Provider name
        isp = isp_infromation["isp"]
        # Extracts the ISP organization name
        isp_organization = isp_infromation["org"]
        # Extracts the Autonomous System Number (ASN)
        isp_autnomous_systems_number = isp_infromation["as"]
        # Returns the ISP name, organization, and ASN as a tuple
        return isp, isp_organization, isp_autnomous_systems_number




    # Saves all collected information to a report file
    def save_report(self):
        # Get user's IP address
        user_ip = self.show_ip()
        # Get location information
        user_country_location, user_region_location, user_city_location, user_zip_locaion = self.get_address_location_information()
        # Get coordinate information
        user_latitude_coordinate_location, user_longitude_coordinate_location = self.get_coordinate_location_information()
        # Get time information
        user_timezone_location, user_formatted_time = self.get_time_information()
        # Get ISP information
        user_isp, user_isp_organization, user_isp_autnomous_systems_number = self.get_isp_information()
        # Open report file in write mode
        with open("where_am_i_report.txt", "w") as report_file:
            # Write location information
            report_file.write(f"Country: {user_country_location}\n\n")
            report_file.write(f"Region: {user_region_location}\n\n")
            report_file.write(f"City: {user_city_location}\n\n")
            report_file.write(f"Zip Code: {user_zip_locaion}\n\n")
            # Write coordinate information
            report_file.write(f"Latitude: {user_latitude_coordinate_location}\n\n")
            report_file.write(f"Longitude: {user_longitude_coordinate_location}\n\n")
            # Write time information
            report_file.write(f"Time Zone: {user_timezone_location}\n\n")
            report_file.write(f"Time Display: {user_formatted_time}\n\n")
            # Write ISP information
            report_file.write(f"ISP: {user_isp}\n\n")
            report_file.write(f"Organization: {user_isp_organization}\n\n")
            report_file.write(f"Autonomous System Number: {user_isp_autnomous_systems_number}\n")




    # Main program loop
    def execute_program(self):
        # Continue looping until user exits
        print(title_display)
        while True:
            # Display menu
            self.display_menu()
            # Get user's menu choice
            user_choice = input("\nInput in choice: ")
            # Option 1 - Display IP Address
            if user_choice == "1":
                user_isp = self.show_ip()
                print(f"\nIP ADDRESS: {user_isp}\n")
            # Option 2 - Display location information
            elif user_choice == "2":
                user_country_location, user_region_location, user_city_location, user_zip_locaion = self.get_address_location_information()
                print(f"\nCountry: {user_country_location}")
                print(f"Region: {user_region_location}")
                print(f"City: {user_city_location}")
                print(f"Zip Code: {user_zip_locaion}\n")
            # Option 3 - Display coordinates
            elif user_choice == "3":
                user_latitude_coordinate_location, user_longitude_coordinate_location = self.get_coordinate_location_information()
                print(f"\nLatitude: {user_latitude_coordinate_location}")
                print(f"Longitude: {user_longitude_coordinate_location}\n")
            # Option 4 - Display timezone information
            elif user_choice == "4":
                user_timezone_location, user_formatted_time = self.get_time_information()
                print(f"\nTime Zone: {user_timezone_location}")
                print(f"Time Display: {user_formatted_time}\n")
            # Option 5 - Display ISP information
            elif user_choice == "5":
                user_isp, user_isp_organization, user_isp_autnomous_systems_number = self.get_isp_information()
                print(f"\nISP: {user_isp}")
                print(f"Organization: {user_isp_organization}")
                print(f"Autonomous System Number: {user_isp_autnomous_systems_number}\n")
            # Option 6 - Save report
            elif user_choice == "6":
                self.save_report()
                print("Report Saved to Text File")
            # Option 7 - Exit program
            elif user_choice == "7":
                break
            # Invalid choice
            else:
                print("\nPlease Input a valid choice")
            print("\n",divider_display,"\n")



    # Starts the program
    def run(self) -> None:
        #Self calls the display welcome message method.
        self.display_welcome_message()
        #Self calls the execute program method.
        self.execute_program()
        #Self. calls the display goodbye message method.
        self.display_goodbye_message()




