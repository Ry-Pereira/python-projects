# Name: Ryan Pereira
# Project Name: Where Am I Locator Project
# Description: A program that uses an IP address API to determine a user's approximate geographic location and display information such as location, time zone, coordinates, and ISP details.
# Module Name: where_am_i_locator.py
# Module Purpose: Stores and displays visual text elements used throughout the program interface.
# Collaborators: None
# Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
# Date: 6/10/2026
# Last Modified: 6/12/2026






# Stores the program title banner and decorative ASCII art in a multi-line string.Decorative ASCII art graphic displayed below the title.
title_display = """
 ____      ____  ____  ____  ________  _______     ________         _       ____    ____    _____    _____       ___      ______       _     _________    ___   _______     
|_  _|    |_  _||_   ||   _||_   __  ||_   __ \   |_   __  |       / \     |_   \  /   _|  |_   _|  |_   _|    .'   `.  .' ___  |     / \   |  _   _  | .'   `.|_   __ \    
  \ \  /\  / /    | |__| |    | |_ \_|  | |__) |    | |_ \_|      / _ \      |   \/   |      | |      | |     /  .-.  \/ .'   \_|    / _ \  |_/ | | \_|/  .-.  \ | |__) |   
   \ \/  \/ /     |  __  |    |  _| _   |  __ /     |  _| _      / ___ \     | |\  /| |      | |      | |   _ | |   | || |          / ___ \     | |    | |   | | |  __ /    
    \  /\  /     _| |  | |_  _| |__/ | _| |  \ \_  _| |__/ |   _/ /   \ \_  _| |_\/_| |_    _| |_    _| |__/ |\  `-'  /\ `.___.'\ _/ /   \ \_  _| |_   \  `-'  /_| |  \ \_  
     \/  \/     |____||____||________||____| |___||________|  |____| |____||_____||_____|  |_____|  |________| `.___.'  `.____ .'|____| |____||_____|   `.___.'|____| |___| 


                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣄⠀⠀⠀⠀⣠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⣤⡀⠀⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⡀⣀⣤⣶⡟⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠈⣻⣾⣿⣿⣿⡿⠟⠛⠛⠛⠛⠻⢿⣿⣿⣿⡿⣻⡟⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⣴⣿⣿⣿⠟⠁⠀⠀⠀⠀⢀⣠⣴⣿⣿⡿⠋⣼⣿⣦⠀⠀⠀⠀⠀
                                                                ⠀⢠⣄⣀⣼⣿⣿⡿⠁⠀⠀⠀⣀⣤⣾⣿⣿⣿⡿⠋⢀⣼⢿⣿⣿⣧⣀⣠⡄⠀
                                                                ⠀⠀⠀⠙⣿⣿⣿⠁⠀⠀⠀⣼⠛⢿⣿⣿⡿⠋⠀⢀⡾⠃⠈⣿⣿⣿⠋⠀⠀⠀
                                                                ⠀⠀⠀⠀⣿⣿⣿⠀⠀⢀⣾⠃⠀⠀⢙⡋⠀⠀⢠⡿⠁⠀⠀⣿⣿⣿⠀⠀⠀⠀
                                                                ⠀⠀⠀⣠⣿⣿⣿⡀⢀⡾⠁⠀⢀⣴⣿⣿⣦⣠⡟⠁⠀⠀⢀⣿⣿⣿⣄⠀⠀⠀
                                                                ⠀⠘⠋⠉⢻⣿⣿⣷⡿⠁⢀⣴⣿⣿⣿⡿⠟⠋⠀⠀⠀⢀⣾⣿⣿⡟⠉⠙⠃⠀
                                                                ⠀⠀⠀⠀⠀⢻⣿⡟⢀⣴⣿⣿⠿⠋⠁⠀⠀⠀⠀⢀⣴⣿⣿⣿⡟⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⣼⢟⣴⣿⣿⣿⣷⣦⣤⣤⣤⣤⣴⣶⣿⣿⣿⡿⣯⡀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⣼⠿⠛⠉⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠀⠈⠛⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠋⠀⠉⠉⠀⠙⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                                                                                                                                                                 
"""



# Stores a decorative divider used to separate sections of output.
divider_display = """
O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()
O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()O()
"""