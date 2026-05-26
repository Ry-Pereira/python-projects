# Name: Ryan Pereira
# Project Name: Etch-A-Sketch
# Description: A Python turtle graphics program that allows users to draw on the screen using keyboard controls,similar to a digital Etch-A-Sketch toy.
# File Name: Etch-A-Sketch.py
# File Purpose: This file creates a turtle graphics window and binds keyboard controls for movement, rotation, clearing the drawing, and resetting the turtle to the center of the screen.
# Collaborators: None
# Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
# Date: 4/24/2026
# Last Modified: 5/11/2026



# Import everything from the turtle graphics module
from turtle import *

# Create a Turtle object (the drawing pen)
turtle = Turtle()

# Create a Screen object (the drawing window)
screen = Screen()


# Function to move the turtle forward
def move_forward():
    # Move 5 steps forward
    turtle.forward(5)


# Function to move the turtle backward
def move_backward():
    # Move 5 steps backward
    turtle.backward(5)
    

# Function to clear all drawings on the screen
def clear_board():
    # Erase everything drawn by the turtle
    turtle.clear()
    

# Function to move turtle back to origin (center)
def move_to_origin():
    # Lift pen so movement doesn't draw
    turtle.penup()
    # Move turtle to center (0,0) and reset direction
    turtle.home()
    # Put pen back down to resume drawing
    turtle.pendown()
    

# Function to rotate turtle left
def turn_left():
    # Turn 5 degrees to the left
    turtle.left(5)


# Function to rotate turtle right
def turn_right():
    # Turn 5 degrees to the right
    turtle.right(5)
    

# Bind Up arrow key to move forward function
screen.onkeypress(move_forward, "Up")

# Bind Left arrow key to turn left function
screen.onkeypress(turn_left, "Left")

# Bind Right arrow key to turn right function
screen.onkeypress(turn_right, "Right")

# Bind Down arrow key to move backward function
screen.onkeypress(move_backward, "Down")

# Bind 'z' key to clear screen function
screen.onkeypress(clear_board, "z")

# Bind 'r' key to reset turtle position
screen.onkeypress(move_to_origin, "r")

# Start listening for keyboard input
screen.listen()

# Keep window open until it is clicked
screen.exitonclick()




