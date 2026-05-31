#Name: Ryan Pereira
#Project Name: Moon Phase Tracker Project
#Description: A program that scrapes moon phase data from a website and displays it to the user in a user-friendly way. The program allows the user to view the current moon phase, the moon phases for the current week, the moon phases for the next week, and the moon phase for a specific date. The program also includes ASCII art representations of each moon phase.
#Collaborators: None
#Module Name: art.py
#Module Purpose: This module contains ASCII art representations of different moon phases for display in the Moon Phase Tracker application.
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 5/28/2026
#Last Modified: 5/30/2026





#This dictionary contains ASCII art representations of each moon phase, which can be displayed to the user in the Moon Phase Tracker application.
moon_phases_image_display = {
    "New Moon": """
       _..._
     .:::::::.
    :::::::::::    NEW MOON
    :::::::::::
    `:::::::::'
      `':::'' 
    """,

    "Waxing Crescent": """
       _..._
     .::::. `.
    :::::::.  :    WAXING CRESCENT
    ::::::::  :
    `::::::' .'"
      `'::'-'
    """,

    "First Quarter": """
       _..._
     .::::  `.
    ::::::    :    FIRST QUARTER
    ::::::    :
    `:::::   .'
      `'::.-'
    """,

    "Waxing Gibbous": """
       _..._
     .::'   `.
    :::       :    WAXING GIBBOUS
    :::       :
    `::.     .'
      `':..-'
    """,

    "Full Moon": """
       _..._
     .'     `.
    :         :    FULL MOON
    :         :
    `.       .'
      `-...-'
    """,

    "Waning Gibbous": """
       _..._
     .'   `::.
    :       :::    WANING GIBBOUS
    :       :::
    `.     .::'
      `-..:''
    """,

    "Last Quarter": """
       _..._
     .'  ::::.
    :    ::::::    LAST QUARTER
    :    ::::::
    `.   :::::'
      `-.::''
    """,

    "Waning Crescent": """
       _..._
     .' .::::.
    :  ::::::::    WANING CRESCENT
    :  ::::::::
    `. '::::::'
      `-.::''
    """
}


#This variable contains ASCII art for the title of the Moon Phase Tracker application, which can be displayed to the user when the program starts.
moon_phase_tracker_title_art_display = """




**********************************************************************************************************************************                                                                                                                         
| m    m  mmmm   mmmm  mm   m        mmmmm  m    m   mm    mmmm  mmmmmm       mmmmmmm mmmmm    mm     mmm  m    m mmmmmm mmmmm   |
| ##  ## m"  "m m"  "m #"m  #        #   "# #    #   ##   #"   " #               #    #   "#   ##   m"   " #  m"  #      #   "#  |
| # ## # #    # #    # # #m #        #mmm#" #mmmm#  #  #  "#mmm  #mmmmm          #    #mmmm"  #  #  #      #m#    #mmmmm #mmmm"  |
| # "" # #    # #    # #  # #        #      #    #  #mm#      "# #               #    #   "m  #mm#  #      #  #m  #      #   "m  |
| #    #  #mm#   #mm#  #   ##        #      #    # #    # "mmm#" #mmmmm          #    #    " #    #  "mmm" #   "m #mmmmm #    "  |
*********************************************************************************************************************************
                                                                                                                              
                                                                                                                              





"""

#This variable contains ASCII art for a line separator, which can be used to separate different sections of the output in the Moon Phase Tracker application.
moon_phases_line_seperator_art_display = """
**********************************************************************************************************************************  
|        _..._          _..._          _..._          _..._          _..._          _..._          _..._          _..._          |
|      .:::::::.      .::::. `.      .::::  `.      .::'   `.      .'     `.      .'   `::.      .'  ::::.      .' .::::.        |
|     :::::::::::    :::::::.  :    ::::::    :    :::       :    :         :    :       :::    :    ::::::    :  ::::::::       |
|     :::::::::::    ::::::::  :    ::::::    :    :::       :    :         :    :       :::    :    ::::::    :  ::::::::       |
|     `:::::::::'    `::::::' .'    `:::::   .'    `::.     .'    `.       .'    `.     .::'    `.   :::::'    `. '::::::'       |
|       `':::''        `'::'-'        `'::.-'        `':..-'        `-...-'        `-..:''        `-.::''        `-.::''         |
********************************************************************************************************************************** 
  
  """
