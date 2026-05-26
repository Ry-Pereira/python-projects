#Name: Ryan Pereira
#Project Name: Timer
#Description: A simple timer that lets user enter a time for hours, minutes, and seconds. Let the user start the timer, pause the timer, and reset the timer 
#Collaborators: None
#Sources: Github Copilot, Stack Overflow, ChatGPT, Python documentation
#Date: 6/10/2026
#Last Modified: 6/11/2026

#Stuff to Hash out: Need to work on formatting, becuase only the the left hand of the minute and seconds can sipport number 0-5


#From the tkinter module, importing everything
from tkinter import *
#From the tkinter module, importing messagebox functionality
from tkinter import messagebox




#Valid numbers for the timer, since the user will input the time in string format, there needs to be checking to see if they are putting numbers, not letters or any specual characters.
VALID_NUMBERS = ["0","1","2","3","4","5","6","7","8","9"]




#Global variables to keep track of time, since user can pause and unpause the timer, and even reset the timer, to keep track of time, and if the timer is paused or not.
#Set minutes is set to None at the start, since user has not inputed a time for minutes yet.
set_minutes = None
#Set seconds is set to None at the start, since user has not input a tiime for seconds yet.
set_seconds = None
#Is paused is set to False at the start, since the timer is not paused at the start of the program.
is_paused = False
#time_id is set to None at the start, since there is no timer running at the start of the progam, so there is no time_id to keep track of yet.
time_id = None




#Colors to use for the program, to make it look nice and appealing to the user, and to make it more enjoyable to use the program.
#WILLOW GREEN is a light green color, to use for the background of the program, and for the timer label when the timer is running.
WILLOW_GREEN = "#84B179"
#SPRING GREEN is a light green color, to use for the background of the entry and buttons, and for the timer label when the timer is paused.
SPRING_GREEN = "#A2CB8B"
#SPRING MIST is a light green color, to use for the background of the timer label when the timer is running.
SPRING_MIST = "#C7EABB"
#SPRING DEW is a light green color, to use for the background of the timer label when the timer is paused.
SPRING_DEW = "#E8F5BD"




#Main function, the main entry point into the program
def main():


    #Close window function will ask the user with a message box pop up if they wish to leave the program, since they clicked the x button to leave
    def close_window():
        #A messagebox aks ok cancel will pop up, asking the user if they wish to leave, if they click ok, then window will be destroyed, if they click cancel, then the program will continue to run and the window will not be destroyed.
        if messagebox.askokcancel(title="Wish to Leave",message="Are you sure you want to leave"):
            #If the user clicks ok, then the window will be destroyed, and the program will end.
            window.destroy()
    
    
    
    #Cuntdown function will take in the minutes and seconds argument from the user, and will update the timer label every second, and will check if the timer is done, if the timer is done, then it will show a messagebox to the user saying that the timer is done, and will reset the timer back to the entry for the user to input a new time.
    def countdown(minutes,seconds):
        #Since the user can pause the timer, and unpause the timer, and even reset the timer, there needs to be a global variable to keep track of the time_id, so that when the user pauses the timer, the program can cancel the after function using the time_id, and when the user unpauses the timer, the program can start a new after function using the time_id.
        global time_id
        
        #This will print the minutes and seconds to the console for testing purposes, to make sure the program is counting down correctly, and to make sure if the pause,unpause, and reset function are working correctly, since the user can pause the timer, and unpause the timer, and even reset the timer, there needs to be a way to keep track of the time, and to make sure the time is counting down correctly, and to make sure the time is updating correctly when the user pauses, unpauses, and resets the timer.
        #print("In countdown",minutes,seconds)
        
        #timer_label will be updated to show the current minutes and seconds, and will be formatted to show two digits for minutes and seconds, like any clock format is, so if the minutes is less than 10, it will show a 0 before the minutes, and if the seconds is less than 10, it will show a 0 before the seconds, to make it look like a clock format.
        timer_label.config(text=f"{minutes:02}:{seconds:02}")
        #If seconds is greate than 0, then the program will call the after function to call the countdown function again after 1000 milliseconds or a second, and will pass in the same minutes and seconds -1, since the seconds will be counting down by 1 every second, and the minutes will stay the same until the seconds reaches 0, and then the minutes will start counting down by 1, and the seconds will reset to 59.
        if seconds > 0:
            time_id = window.after(1000,countdown,minutes,seconds-1)
        #If seconds is 0 and minutes is greater than 0, then the program will call the after function to call the countdonwn function after 1000 milliseconds or a second, and will pass in the minutes - 1, since the minutes will be counting down by 1 every time the seconds reaches 0, and the seconds will reset to 59, since the seconds will be counting down by 1 every second, and when the seconds reaches 0, it will reset to 59, and the minutes will start counting down by 1.
        elif seconds == 0 and minutes > 0:
            time_id = window.after(1000,countdown,minutes-1,seconds + 59)
        #If the seocnds is 0 and minutes is also 0, the timer is done, so the program will show a messagebox to the user saying that the timer is done, and will reset the timer back to the entry for the user to input a new time, and will also disable the pause and unpause button, since there is no timer running, and will also disable the restart button, since there is no timer running, and will also hide the timer label, since there is no timer running, and will show the entry for the user to input a new time.
        elif seconds == 0 and minutes == 0:
            #Timer label will be hidden, since the timer is no longer running
            timer_label.grid_forget()
            #Timer entry will be shown again, in the same place as the timer label, with same configuration
            timer_entry.grid(column = 1, row = 1, pady = 10)
            #Start button will be updated to be normal, since the timer is no longer running
            start_button.config(state=NORMAL)
            #Restart button will be updated to be disabled, ince the timer is no longer running, ther is no time to restart, so the restart button will be disabled
            restart_button.config(state=DISABLED)
            #Message bow will show info with the title and message to indicate that the timer is done, to let user know the timer is finished, and to let user know they can input a new time if they wish to start a new timer.
            messagebox.showinfo(title="Timer is Done",message="Timer is Done")

        



    #The function start timer will be called when the user clicks the start button, and will get the time from the entry, and will check if the time is in the correct format, and if it is in the correct format, it will start the timer by calling the countdown function with the minutes and seconds that the user inputed, and will also update the buttons and labels to reflect that the timer is running, and will also disable the start button, since there is a timer running, and will enable the pause and unpause button, since there is a timer running, and will enable the restart button, since there is a timer running, and will also hide the entry for the user to input a new time, since there is already a timer running, and will show the timer label to show the time counting down.
    def start_timer():
        #Timter time is set to the value of the timer entry, which is the time that the user inputed, and will be in string format, since the entry is in string format, so the time will be in string format, and will need to be checked to make sure it is in the correct format, and will need to be converted to integers for minutes and seconds to be used in the countdown function.
        timer_time = timer_entry.get()
        #if the length of timer time is greater than 5 or lesser than 5, then the program will show a messagebox to the user saying to input a a valid time, since the correct format only supports minutes and seconds occupied by 5 characters, with a colon in the middle, so if the length is greater than 5 or lesser than 5, then it is not in the correct format, and the program will show a messagebox to the user saying to input a valid time.
        if len(timer_time) > 5 or len(timer_time) < 5 :
            messagebox.showinfo(title="Error",message="Sorry Please Input a valid time")
        #If the timer time is 00:00, then the program will show a messagebox to the user saying to input a valid time, since 00:00 is not a valid time to start a timer, since it is already at 0, so the program will show a messagebox to the user saying to input a valid time.
        elif timer_time == "00:00":
            #Message box will show info with the title and message to indicate that the user needs to input a valid time, since 00:00 is not a valid time to start a timer, since it is already at 0, so the program will show a messagebox to the user saying to input a valid time.
            messagebox.showinfo(title="Error",message="Sorry Please Input a valid time")
        #If the timer time is not in the correct format, which means that the first two characters are not numbers, or the third character is not a colon, or the last two characters are not numbers, then the program will show a messagebox to the user saying to input a valid time, since the correct format only supports minutes and seconds occupied by 5 characters, with a colon in the middle, so if the first two characters are not numbers, or the third character is not a colon, or the last two characters are not numbers, then it is not in the correct format, and the program will show a messagebox to the user saying to input a valid time.
        elif timer_time[0] not in VALID_NUMBERS or timer_time[1] not in VALID_NUMBERS or timer_time[2] != ":" or timer_time[3] not in VALID_NUMBERS or timer_time[4] not in VALID_NUMBERS:
            #Message box will show info with the title and message to indicate that the user needs to input a valid time, since the correct format only supports minutes and seconds occupied by 5 characters, with a colon in the middle, so if the first two characters are not numbers, or the third character is not a colon, or the last two characters are not numbers, then it is not in the correct format, and the program will show a messagebox to the user saying to input a valid time.
            messagebox.showinfo(title="Error",message="Sorry please input in valud format")
        #Else if all conditions are passed, which means the timer is in correct format and characters used, then the program will start the timer by calling the countdown function with the minutes and seconds that the user inputed, and will also update the buttons and labels to reflect that the timer is running, and will also disable the start button, since there is a timer running, and will enable the pause and unpause button, since there is a timer running, and will enable the restart button, since there is a timer running, and will also hide the entry for the user to input a new time, since there is already a timer running, and will show the timer label to show the time counting down.
        else:
            #Set minutes is set to the first two characters of the timer time, which is the minutes that the user inputed, and will be converted to an integer, since the entry is in string format, so the time will be in string format, and will need to be converted to integers for minutes and seconds to be used in the countdown function.
            set_minutes = int(timer_time[0:2])
            #Set seconds is set to the last two characters of the timer time, which is the seconds that the user inputed, and will be converted to an integer, since the entry is in string format, so the time will be in string format, and will need to be converted to integers for minutes and seconds to be used in the countdown function.
            set_seconds = int(timer_time[3:5])
            #Start button will be updated to be disabled, since there is a timer running, so the user should not be able to start another timer while there is already a timer running.
            start_button.config(state=DISABLED)
            #Pause and unpause button will be updated to be normal, since there is a timer running, so the user should be able to pause and unpause the timer while there is a timer running.
            pause_and_unpause_button.config(state=NORMAL)
            #Restart button will be updated to be normal, since there is a timer running, so the user should be able to restart the timer while there is a timer running.
            restart_button.config(state=NORMAL)
            #Timer entry will be hidden, since there is already a timer running, so the user should not be able to input a new time while there is already a timer running.
            timer_entry.grid_forget()
            #Timer label will be shown, in the same place as the timer entry, with same configuration, to show the time counting down, since there is a timer running, so the user should be able to see the time counting down while there is a timer running.
            timer_label.grid(column = 1, row = 1, pady = 10)
            #Timer label will be configured to have the foreground color of WILLOW GREEN, and the background color of SPRING MIST, to indicate that the timer is running, since there is a timer running, so the timer label should be configured to indicate that the timer is running.
            timer_label.config(fg = '#6A7E3F' ,bg=SPRING_MIST)
            #Countdown function will be called with the set minutes and set seconds that the user inputed, to start the timer counting down, since there is a timer running, so the countdown function should be called to start the timer counting down.
            countdown(set_minutes,set_seconds)

            
    #Function pause timer will be called when the user clicks the pause and unpause button, and will check if the timer is currently paused or not, if the timer is not paused, then it will pause the timer by canceling the after function using the time_id, and will update the buttons and labels to reflect that the timer is paused, and will also disable the start button, since there is a timer running, but it is paused, so the user should not be able to start another timer while there is already a timer running, even if it is paused, and will also disable the restart button, since there is a timer running, but it is paused, so the user should not be able to restart the timer while there is already a timer running, even if it is paused, and will also update the pause and unpause button to say "Unpause", since the timer is now paused, so the button should indicate that clicking it will unpause the timer, and will also update the timer label to have a different foreground color and background color to indicate that the timer is paused. If the timer is currently paused, then it will unpause the timer by calling the countdown function with the current minutes and seconds that are showing on the timer label, and will update the buttons and labels to reflect that the timer is running again, and will also disable the start button, since there is a timer running again, so the user should not be able to start another timer while there is already a timer running again, and will also enable the restart button, since there is a timer running again, so the user should be able to restart the timer while there is a timer running again, and will also update the pause and unpause button to say "Pause", since the timer is now running again, so the button should indicate that clicking it will pause the timer again, and will also update the timer label to have a different foreground color and background color to indicate that the timer is running again.
    def pause_timer():
        #GLobal variables to keep track of if the timer is paused or not, and to keep track of the time_id, since the user can pause and unpause the timer, and even reset the timer, to keep track of time, and if the timer is paused or not.
        global is_paused, time_id
        #If is_paused set to False, which means the timer is currently not paused, then the program will pause the timer by canceling the after function using the time_id, and will update the buttons and labels to reflect that the timer is paused, and will also disable the start button, since there is a timer running, but it is paused, so the user should not be able to start another timer while there is already a timer running, even if it is paused, and will also disable the restart button, since there is a timer running, but it is paused, so the user should not be able to restart the timer while there is already a timer running, even if it is paused, and will also update the pause and unpause button to say "Unpause", since the timer is now paused, so the button should indicate that clicking it will unpause the timer, and will also update the timer label to have a different foreground color and background color to indicate that the timer is paused. If is_paused set to True, which means the timer is currently paused, then the program will unpause the timer by calling the countdown function with the current minutes and seconds that are showing on the timer label, and will update the buttons and labels to reflect that the timer is running again, and will also disable the start button, since there is a timer running again, so the user should not be able to start another timer while there is already a timer running again, and will also enable the restart button, since there is a timer running again, so the user should be able to restart the timer while there is a timer running again, and will also update the pause and unpause button to say "Pause", since the timer is now running again, so the button should indicate that clicking it will pause the timer again, and will also update the timer label to have a different foreground color and background color to indicate that the timer is running again.
        if is_paused == False:
            #Window after cancel will be called with the time_id, to cancel the after function that is currently running, to pause the timer, since there is a timer running, and it is not paused, so the after function should be canceled to pause the timer.
            window.after_cancel(time_id)
            #Pause and unpause button will be updated to say "Unpause", since the timer is now paused, so the button should indicate that clicking it will unpause the timer.
            pause_and_unpause_button.config(text="Unpause")
            #Start button will be updated to be disabled, since there is a timer running, but it is paused, so the user should not be able to start another timer while there is already a timer running, even if it is paused.
            start_button.config(state=DISABLED)
            #Restart button will be updated to be disabled, since there is a timer running, but it is paused, so the user should not be able to restart the timer while there is already a timer running, even if it is paused.
            restart_button.config(state=DISABLED)
            #Is paused will be set to True, since the timer is now paused, so the is_paused variable should be updated to reflect that the timer is paused.
            is_paused = True
            #Timer label will be configured to have the foreground color of SPRING MIST, and the background color of '#6A7E3F', to indicate that the timer is paused, since there is a timer running, but it is paused, so the timer label should be configured to indicate that the timer is paused.
            timer_label.config(fg = SPRING_MIST ,bg='#6A7E3F')
        #Else if is_paused set to True, which means the timer is currently paused, then the program will unpause the timer by calling the countdown function with the current minutes and seconds that are showing on the timer label, and will update the buttons and labels to reflect that the timer is running again, and will also disable the start button, since there is a timer running again, so the user should not be able to start another timer while there is already a timer running again, and will also enable the restart button, since there is a timer running again, so the user should be able to restart the timer while there is a timer running again, and will also update the pause and unpause button to say "Pause", since the timer is now running again, so the button should indicate that clicking it will pause the timer again, and will also update the timer label to have a different foreground color and background color to indicate that the timer is running again.
        else:
            #Pause and unpause button will be updated to say "Pause", since the timer is now running again, so the button should indicate that clicking it will pause the timer again.
            pause_and_unpause_button.config(text="Pause")
            #Start button will be updated to be disabled, since there is a timer running again, so the user should not be able to start another timer while there is already a timer running again.
            start_button.config(state=DISABLED)
            #Restart button will be updated to be normal, since there is a timer running again, so the user should be able to restart the timer while there is a timer running again.
            restart_button.config(state=NORMAL)
            #Is paused will be set to False, since the timer is now running again, so the is_paused variable should be updated to reflect that the timer is running again.
            is_paused = False
            #Set minutes will be set to the first two characters of the timer label, which is the minutes that are currently showing on the timer label, and will be converted to an integer, since the timer label is in string format, so the time will be in string format, and will need to be converted to integers for minutes and seconds to be used in the countdown function.
            set_minutes = int(timer_label['text'][0:2])
            #Set seconds will be set to the last two characters of the timer label, which is the seconds that are currently showing on the timer label, and will be converted to an integer, since the timer label is in string format, so the time will be in string format, and will need to be converted to integers for minutes and seconds to be used in the countdown function.
            set_seconds = int(timer_label['text'][3:5])
            #Timer label will be configured to have the foreground color of WILLOW GREEN, and the background color of SPRING MIST, to indicate that the timer is running again, since there is a timer running again, so the timer label should be configured to indicate that the timer is running again.
            timer_label.config(fg = '#6A7E3F' ,bg=SPRING_MIST)
            #Countdown function will be called with the set minutes and set seconds that are currently showing on the timer label, to unpause the timer and start it counting down again, since there is a timer running again, so the countdown function should be called to start the timer counting down again.
            countdown(set_minutes,set_seconds-1)



    #Function restart timer will be called when the user clicks the restart button, and will restart the timer by canceling the after function using the time_id, and will update the buttons and labels to reflect that the timer is restarted, and will also disable the pause and unpause button, since there is no timer running, so there is no timer to pause or unpause, and will also disable the restart button, since there is no timer running, so there is no timer to restart, and will also update the start button to be normal, since there is no timer running, so the user should be able to start a new timer, and will also hide the timer label, since there is no timer running, and will show the entry for the user to input a new time.
    def restart_timer():
        #Global variable to keep track of the time_id, since the user can pause and unpause the timer, and even reset the timer, to keep track of time, and if the timer is paused or not.
        global time_id
        window.after_cancel(time_id)
        #Timer label will be hidden, since there is no timer running, so the user should not be able to see the timer label when there is no timer running.
        timer_label.grid_forget()
        #Timer entry will be shown again, in the same place as the timer label, with same configuration, to show the entry for the user to input a new time, since there is no timer running, so the user should be able to input a new time when there is no timer running.
        timer_entry.grid(column = 1, row = 1, pady = 10)
        #start button will be updated to be normal, since there is no timer running, so the user should be able to start a new timer when there is no timer running.
        start_button.config(state=NORMAL)
        #Pause and unpause button will be updated to be disabled, since there is no timer running, so there is no timer to pause or unpause, so the pause and unpause button should be disabled.
        pause_and_unpause_button.confug(state=DISABLED)
        #Restart button will be updated to be disabled, since there is no timer running, so there is no timer to restart, so the restart button should be disabled.
        restart_button.config(state=DISABLED)
        
        

    #Window setup, creating the window for the program, and setting the title, size, and background color of the window, to make it look nice and appealing to the user, and to make it more enjoyable to use the program.
    window = Tk()
    #Window title will be set to "Timer", since this is a timer program, so the title should reflect that it is a timer program.
    window.title("Timer")
    #Window minsize will be set to width of 220 and height of 220, since the program does not need to be very big, and this size is enough to fit all the buttons, labels, and entry, and also looks nice and appealing to the user, and also prevents the user from making the window too small to see the buttons, labels, and entry.
    window.minsize(width = 220, height = 220)
    #Window config will be set to have a padding of 25 on the x and y axis, and will have a background color of WILLOW GREEN, to make it look nice and appealing to the user, and to make it more enjoyable to use the program.
    window.config(padx = 25, pady= 25, bg = "#84B179")
   



    #Labels
    #Title label will be created with the text "A Simple Timer", and will have a font of Arial with size 12, and will be configured to have a background color of SPRING GREEN, to make it look nice and appealing to the user, and to make it more enjoyable to use the program, and will be placed in the first column and first row of the grid, to be at the top of the window, and to be centered above the timer entry and timer label.
    title_label = Label(text="A Simple Timer",font=("Arial",12))
    #Title label will be configured to have a background color of SPRING GREEN, to make it look nice and appealing to the user, and to make it more enjoyable to use the program.
    title_label.config(bg = "#A2CB8B")
    #Title label will be placed in the first column and first row of the grid, to be at the top of the window, and to be centered above the timer entry and timer label.
    title_label.grid(column = 1,row = 0)
    #Timer label will be created with the text "00:00", and will have a font of Arial with size 12, and will be configured to have a background color of SPRING MIST, to make it look nice and appealing to the user, and to make it more enjoyable to use the program, and will be placed in the first column and first row of the grid, to be in the same place as the timer entry, but will be hidden at the start of the program, since there is no timer running at the start of the program, so the timer label should be hidden at the start of the program, and will only be shown when there is a timer running.
    timer_label = Label(text = "00:00",font=("Arial",12),width = 10)


    #Entry
    #Timer entry will be created with a width of 10, and a font of Arial with size 12, and will be configured to have a background color of SPRING GREEN, to make it look nice and appealing to the user, and to make it more enjoyable to use the program, and will be placed in the first column and first row of the grid, to be in the same place as the timer label, but will be shown at the start of the program, since there is no timer running at the start of the program, so the timer entry should be shown at the start of the program, and will only be hidden when there is a timer running.
    timer_entry = Entry(width = 10,font=("Arial",12))
    #Timer entry will be placed in the first column and first row of the grid, to be in the same place as the timer label, but will be shown at the start of the program, since there is no timer running at the start of the program, so the timer entry should be shown at the start of the program, and will only be hidden when there is a timer running.
    timer_entry.grid(column = 1, row = 1, pady = 10)
    #Timer entry will be configured to have a background color of SPRING GREEN, to make it look nice and appealing to the user, and to make it more enjoyable to use the program.
    timer_entry.insert(0,"00:00")
    #Timer entry wil be configured to have a background color of SPRING GREEN, to make it look nice and appealing to the user, and to make it more enjoyable to use the program.
    timer_entry.config(bg = "#A2CB8B")
    #Timer entry will be focused, so the user can immediately start typing in it.
    timer_entry.focus()




    #Button
    #Start button will be created with the text "Start", and will have a font of Arial with size 12, and will be configured to have a background color of SPRING GREEN, to make it look nice and appealing to the user, and to make it more enjoyable to use the program, and will be placed in the first column and second row of the grid, to be below the timer entry and timer label, and to be on the left side of the window, and will have a command of start_timer, so that when the user clicks the start button, the start_timer function will be called to start the timer.
    start_button = Button(text = "Start", command = start_timer,font=("Arial",12))
    #Start button will be configured to have a background color of SPRING GREEN, to make it look nice and appealing to the user, and to make it more enjoyable to use the program.
    start_button.config(bg = "#A2CB8B")
    #Start button will be placed in the first column and second row of the grid, to be below the timer entry and timer label, and to be on the left side of the window, and will have a command of start_timer, so that when the user clicks the start button, the start_timer function will be called to start the timer.
    start_button.grid(column=0,row=2, pady = 10)
    #Pause and unpause button will be created with the text "Pause", and will have a font of Arial with size 12, and will be configured to have a background color of SPRING GREEN, to make it look nice and appealing to the user, and to make it more enjoyable to use the program, and will be placed in the first column and second row of the grid, to be below the timer entry and timer label, and to be in the middle of the window, and will have a command of pause_timer, so that when the user clicks the pause and unpause button, the pause_timer function will be called to pause or unpause the timer depending on if the timer is currently paused or not.
    pause_and_unpause_button = Button(text="Pause", command = pause_timer,font=("Arial",12))
    #Pause and unpause button will be configured to have a background color of SPRING GREEN, to make it look nice and appealing to the user, and to make it more enjoyable to use the program.
    pause_and_unpause_button.config(bg = "#A2CB8B")
    #Pause and unpause button will be placed in the first column and second row of the grid, to be below the timer entry and timer label, and to be in the middle of the window, and will have a command of pause_timer, so that when the user clicks the pause and unpause button, the pause_timer function will be called to pause or unpause the timer depending on if the timer is currently paused or not.
    pause_and_unpause_button.grid(column=1,row=2, pady = 10)
    #Restart button will be created with the text "Restart", and will have a font of Arial with size 12, and will be configured to have a background color of SPRING GREEN, to make it look nice and appealing to the user, and to make it more enjoyable to use the program, and will be placed in the first column and second row of the grid, to be below the timer entry and timer label, and to be on the right side of the window, and will have a command of restart_timer, so that when the user clicks the restart button, the restart_timer function will be called to restart the timer.
    restart_button = Button(text="Restart", command = restart_timer,font=("Arial",12))
    #Restart button will be configured to have a background color of SPRING GREEN, to make it look nice and appealing to the user, and to make it more enjoyable to use the program.
    restart_button.config(bg = "#A2CB8B")
    #Restart button will be placed in the first column and second row of the grid, to be below the timer entry and timer label, and to be on the right side of the window, and will have a command of restart_timer, so that when the user clicks the restart button, the restart_timer function will be called to restart the timer.
    restart_button.grid(column=2,row=2, pady = 10)
    #At the start of the program, the pause and unpause button will be disabled, since there is no timer running at the start of the program, so there is no timer to pause or unpause, so the pause and unpause button should be disabled at the start of the program, and will only be enabled when there is a timer running.
    restart_button.config(state=DISABLED)
    #Pause and unpause button will be disabled, since there is no timer running at the start of the program, so there is no timer to pause or unpause, so the pause and unpause button should be disabled at the start of the program, and will only be enabled when there is a timer running.
    pause_and_unpause_button.config(state=DISABLED)

    #If the user clicks the x buttons on the window, which meaning they want to leave, the function close window will be called, to ask if the user really want to leave the program.
    window.protocol("WM_DELETE_WINDOW",close_window)


    #Window will kepp on looping until the user themselves exit the program.
    window.mainloop()


#Calling the main function for the whole program to start
main()