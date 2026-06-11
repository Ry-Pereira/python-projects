#Name: Ryan Pereira
#Project Name: Where Am I Locator Project
#Description: 
#Module Name: main.py
#Module Purpose: 
#Collaborators: None
#Sources:  Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 6/10/2026
#Last Modified: 6/11/2026


from where_ami_i_locator_requests import get_ip_address,get_additional_ip_location
from datetime import datetime
from zoneinfo import ZoneInfo

class WhereAmILocatorBrain:





    def display_welcome_message(self) -> None:
        print("\nWelcome to the Where Am I Locator Program")
        print("Follow Directions to understnad how to use program.")



    def display_menu(self) -> None:
        print("\n1.SHOW MY IP: ")
        print("2.SHOW MY LOCATION: ")
        print("3.SHOW MY TIME ZONE: ")
        print("4.SHOW MY ISP: ")
        print("5.SAVE REPORT : ")
        print("6.EXIT OUT OF PROGRAM: ")



    def display_goodbye_message(self) -> None:
        print("\nThankyou So much for using my program.")
        print("Please leave any feedback in the discussion r contact me otherwise. ")
        print("Goodbye!")


    def show_ip(self):
        return get_ip_address()


    def show_location(self):
        ip_address =  get_ip_address()
        other_location_infromation = get_additional_ip_location(ip_address)

        print("Country: ",other_location_infromation["country"])
        print("Region: ",other_location_infromation["regionName"])
        print("City: ",other_location_infromation["city"])
        print("Zip Code: ",other_location_infromation["zip"])

    def show_coordinate_location(self):
        ip_address =  get_ip_address()
        other_location_infromation = get_additional_ip_location(ip_address)

        print("Latitude: ",other_location_infromation["lat"])
        print("Longitude: ",other_location_infromation["lon"])
  


    def show_time_zone(self):
        ip_address =  get_ip_address()
        other_location_infromation = get_additional_ip_location(ip_address)


        t_time = datetime.now(ZoneInfo(other_location_infromation["timezone"]))
        formatted_time = t_time.strftime("%I:%M %p")




        print("Time Zone: ",other_location_infromation["timezone"])
        print("Time Display: ",formatted_time)

    def show_isp(self):
        ip_address =  get_ip_address()
        other_location_infromation = get_additional_ip_location(ip_address)


        print("ISP: ",other_location_infromation["isp"])
        print("Organization: ",other_location_infromation["org"])
        print("Autonomous System Number",other_location_infromation["as"]))

    def save_report(self):
        ip_address =  get_ip_address()
        other_location_infromation = get_additional_ip_location(ip_address)

        t_time = datetime.now(ZoneInfo(other_location_infromation["timezone"]))
        formatted_time = t_time.strftime("%I:%M %p")




        

       

      
      

        with open("where_am_i_reports.txt","w") as report_file:
            report_file.write("Country: ",other_location_infromation["country"])
            report_file.write("City: ",other_location_infromation["city"])
            report_file.write("Zip Code: ",other_location_infromation["zip"])
            report_file.write("Latitude: ",other_location_infromation["lat"])
            report_file.write("Longitude: ",other_location_infromation["lon"])
            report_file.write("Time Zone: ",other_location_infromation["timezone"])
            report_file.write("Time Display: ",formatted_time)
            report_file.write("ISP: ",other_location_infromation["isp"])
            report_file.write("Organization: ",other_location_infromation["org"])
            report_file.write("Autonomous System Number",other_location_infromation["as"])



    def play_program(self):
        while(True):
            self.display_menu()
            user_choice = input("\nInput in choice: ")
            if user_choice == "1":
                user_isp = self.show_ip()
                print(f"IP ADDRESS: {user_isp}")

            elif user_choice == "2":
                user_location = self.show_location()
            elif user_choice == "3":
                user_time_zone = self.show_time_zone()
            elif user_choice == "4":
                user_isp = self.show_isp()
            elif user_choice == "5":
                saved_report = self.save_report()
            elif user_choice == "6":
                break
            else:
                print("\nPlease Input a valid choice")



    def run(self) -> None:
        self.display_welcome_message()
        self.play_program()
        self.display_goodbye_message()





