#Name: 
#Project Name:
#Description: 
#Module Name: 
#Module Purpose: 
#Collaborators: 
#Sources: 
#Date:
#Last Modified: 


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
        pass

    def show_location(self):
        pass

    def show_time_zone(self):
        pass

    def show_isp(self):
        pass

    def save_report(self):
        pass


    def play_program(self):
        while(True):
            user_choice = input("\nInput in choice: ")
            if user_choice == "1":
                user_isp = self.show_isp()
            if user_choice == "2":
                user_location = self.show_location()
            if user_choice == "3":
                user_time_zone = self.show_time_zone()
            if user_choice == "4":
                user_isp = self.show_isp()
            if user_choice == "5":
                saved_report = self.save_report()
            if user_choice == "6":
                break
            else:
                print("\nPlease Input a valid choice")



    def run(self) -> None:
        self.display_welcome_message()
        self.display_menu()
        self.display_goodbye_message()