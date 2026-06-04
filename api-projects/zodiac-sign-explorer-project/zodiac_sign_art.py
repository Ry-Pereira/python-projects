#Name: Ryan Pereira
#Project Name: Zodiac Sign Explorer Project
#Description: A program that scrapes zodiac sign data from a website and displays it to the user in a user-friendly way. The program allows the user to view information about different zodiac signs, including their birthday ranges, personality traits, and compatibility.
#Collaborators: None
#Module Name: zodiac_sign_art.py
#Module Purpose: This program serves as the user interface for the Zodiac Sign Explorer application. It defines the ASCII art representations for each zodiac sign.
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 6/1/2026
#Last Modified: 6/4/2026







zodiac_signs_display_dictionary = {
    "Aries": {
        "title": "Aries - The Ram",
        "ascii_art": r"""
   .-.   .-.
  (_  \ /  _)
       |
       |
"""
    },

    "Taurus": {
        "title": "Taurus - The Bull",
        "ascii_art": r"""
    .     .
    '.___.'
    .'   `.
   :       :
   :       :
    `.___.'
"""
    },

    "Gemini": {
        "title": "Gemini - The Twins",
        "ascii_art": r"""
    ._____.
      | |
      | |
     _|_|_
    '     '
"""
    },

    "Cancer": {
        "title": "Cancer - The Crab",
        "ascii_art": r"""
      .--.
     /   _`.
    (_) ( )
   '.    /
     `--'
"""
    },

    "Leo": {
        "title": "Leo - The Lion",
        "ascii_art": r"""
      .--.
     (    )
    (_)  /
        (_,
"""
    },

    "Virgo": {
        "title": "Virgo - The Virgin",
        "ascii_art": r"""
   _
  ' `:--.--.
     |  |  |_
     |  |  | )
     |  |  |/
          (J
"""
    },

    "Libra": {
        "title": "Libra - The Balance",
        "ascii_art": r"""
        __
   ___.'  '.___
   ____________
"""
    },

    "Scorpio": {
        "title": "Scorpio - The Scorpion",
        "ascii_art": r"""
   _
  ' `:--.--.
     |  |  |
     |  |  |
     |  |  |  ..,
           `---':
"""
    },

    "Sagittarius": {
        "title": "Sagittarius - The Archer",
        "ascii_art": r"""
          ...
          .':
        .'
    `..'
    .'`.
"""
    },

    "Capricorn": {
        "title": "Capricorn - The Goat",
        "ascii_art": r"""
            _
    \      /_)
     \    /`.
      \  /   ;
       \/ __.'
"""
    },

    "Aquarius": {
        "title": "Aquarius - The Water Bearer",
        "ascii_art": r"""
 .-"-._.-"-._.-
 .-"-._.-"-._.-
"""
    },

    "Pisces": {
        "title": "Pisces - The Fishes",
        "ascii_art": r"""
     `-.    .-'
        :  :
      --:--:--
        :  :
     .-'    `-.
"""
    }
}



zodiac_sign_title_display = """
.########..#######..########..####....###.....######......######..####..######...##....##....########.##.....##.########..##........#######..########..########.########.
......##..##.....##.##.....##..##....##.##...##....##....##....##..##..##....##..###...##....##........##...##..##.....##.##.......##.....##.##.....##.##.......##.....##
.....##...##.....##.##.....##..##...##...##..##..........##........##..##........####..##....##.........##.##...##.....##.##.......##.....##.##.....##.##.......##.....##
....##....##.....##.##.....##..##..##.....##.##...........######...##..##...####.##.##.##....######......###....########..##.......##.....##.########..######...########.
...##.....##.....##.##.....##..##..#########.##................##..##..##....##..##..####....##.........##.##...##........##.......##.....##.##...##...##.......##...##..
..##......##.....##.##.....##..##..##.....##.##....##....##....##..##..##....##..##...###....##........##...##..##........##.......##.....##.##....##..##.......##....##.
.########..#######..########..####.##.....##..######......######..####..######...##....##....########.##.....##.##........########..#######..##.....##.########.##.....##
"""



print(zodiac_signs_display_dictionary["Aries"]["title"])