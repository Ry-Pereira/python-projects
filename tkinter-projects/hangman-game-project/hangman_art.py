# Name: Ryan Pereira
# Project Name: Hangman
# Description: ASCII art stages used to visually represent the hangman game progress
# Collaborators: None
# Sources: ChatGPT, Python documentation
# Date: 4/11/2026
# Last Modified: 4/11/2026


# Stage 0: starting state (no wrong guesses yet)
stage_0 = """
  +---+   # top of gallows
  |   |   # vertical support + rope area
      |   # empty head position
      |   # empty body
      |   # empty legs
      |   # empty base area
========="""  # ground line


# Stage 1: first wrong guess (head appears)
stage_1 = """
  +---+   # gallows structure
  |   |   # support beam
  O   |   # head added (first mistake)
      |   # body not yet drawn
      |   # legs not yet drawn
      |   # base area
========="""


# Stage 2: second wrong guess (body added)
stage_2 = """
  +---+   # gallows top
  |   |   # support structure
  O   |   # head
  |   |   # torso begins
      |   # legs missing
      |   # base
========="""


# Stage 3: third wrong guess (one arm added)
stage_3 = """
  +---+   # gallows top
  |   |   # frame
  O   |   # head
 /|   |   # one arm added
      |   # legs still missing
      |   # base
========="""


# Stage 4: fourth wrong guess (both arms added)
stage_4 = """
  +---+   # gallows top
  |   |   # frame
  O   |   # head
 /|\  |   # both arms added
      |   # legs missing
      |   # base
========="""


# Stage 5: fifth wrong guess (one leg added)
stage_5 = """
  +---+   # gallows top
  |   |   # frame
  O   |   # head
 /|\  |   # full arms
 /    |   # one leg added
      |   # second leg missing
========="""


# Stage 6: final stage (full hangman complete - game over)
stage_6 = """
  +---+   # gallows top
  |   |   # frame
  O   |   # head
 /|\  |   # full body arms
 / \  |   # both legs added (game over state)
      |   # base
========="""
