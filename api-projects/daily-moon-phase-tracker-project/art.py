moon_phases = {
    "new_moon": """
       _..._
     .:::::::.
    :::::::::::    NEW MOON
    :::::::::::
    `:::::::::'
      `':::'' 
    """,

    "waxing_crescent": """
       _..._
     .::::. `.
    :::::::.  :    WAXING CRESCENT
    ::::::::  :
    `::::::' .'
      `'::'-'
    """,

    "first_quarter": """
       _..._
     .::::  `.
    ::::::    :    FIRST QUARTER
    ::::::    :
    `:::::   .'
      `'::.-'
    """,

    "waxing_gibbous": """
       _..._
     .::'   `.
    :::       :    WAXING GIBBOUS
    :::       :
    `::.     .'
      `':..-'
    """,

    "full_moon": """
       _..._
     .'     `.
    :         :    FULL MOON
    :         :
    `.       .'
      `-...-'
    """,

    "waning_gibbous": """
       _..._
     .'   `::.
    :       :::    WANING GIBBOUS
    :       :::
    `.     .::'
      `-..:''
    """,

    "last_quarter": """
       _..._
     .'  ::::.
    :    ::::::    LAST QUARTER
    :    ::::::
    `.   :::::'
      `-.::''
    """,

    "waning_crescent": """
       _..._
     .' .::::.
    :  ::::::::    WANING CRESCENT
    :  ::::::::
    `. '::::::'
      `-.::''
    """
}


zodiac_signs = {
    "aries": r"""
   .-.   .-.
  (_  \ /  _)
       |
       |
Aries - The Ram
""",

    "taurus": r"""
    .     .
    '.___.'
    .'   `.
   :       :
   :       :
    `.___.'
Taurus - The Bull
""",

    "gemini": r"""
    ._____.
      | |
      | |
     _|_|_
    '     '
Gemini - The Twins
""",

    "cancer": r"""
      .--.
     /   _`.
    (_) ( )
   '.    /
     `--'
Cancer - The Crab
""",

    "leo": r"""
      .--.
     (    )
    (_)  /
        (_,
Leo - The Lion
""",

    "virgo": r"""
   _
  ' `:--.--.
     |  |  |_
     |  |  | )
     |  |  |/
          (J
Virgo - The Virgin
""",

    "libra": r"""
        __
   ___.'  '.___
   ____________
Libra - The Balance
""",

    "scorpius": r"""
   _
  ' `:--.--.
     |  |  |
     |  |  |
     |  |  |  ..,
           `---':
Scorpius - The Scorpion
""",

    "sagittarius": r"""
          ...
          .':
        .'
    `..'
    .'`.
Sagittarius - The Archer
""",

    "capricorn": r"""
            _
    \      /_)
     \    /`.
      \  /   ;
       \/ __.'
Capricorn - The Goat
""",

    "aquarius": r"""
 .-"-._.-"-._.-
 .-"-._.-"-._.-
Aquarius - The Water Bearer
""",

    "pisces": r"""
     `-.    .-'
        :  :
      --:--:--
        :  :
     .-'    `-.
Pisces - The Fishes
"""
}

title = """


                                                                                                                              
 m    m  mmmm   mmmm  mm   m        mmmmm  m    m   mm    mmmm  mmmmmm       mmmmmmm mmmmm    mm     mmm  m    m mmmmmm mmmmm 
 ##  ## m"  "m m"  "m #"m  #        #   "# #    #   ##   #"   " #               #    #   "#   ##   m"   " #  m"  #      #   "#
 # ## # #    # #    # # #m #        #mmm#" #mmmm#  #  #  "#mmm  #mmmmm          #    #mmmm"  #  #  #      #m#    #mmmmm #mmmm"
 # "" # #    # #    # #  # #        #      #    #  #mm#      "# #               #    #   "m  #mm#  #      #  #m  #      #   "m
 #    #  #mm#   #mm#  #   ##        #      #    # #    # "mmm#" #mmmmm          #    #    " #    #  "mmm" #   "m #mmmmm #    "
________________________________________________________________________________________________________________________________
                                                                                                                              
                                                                                                                              





"""

print(moon_phases["full_moon"])
print(zodiac_signs["leo"])

print(title)