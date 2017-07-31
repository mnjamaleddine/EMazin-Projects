from Tkinter import *       #importing Tkinter library that enables you to create GUI
import tkFont               #importing font library to be able to specify font in GUI
import RPi.GPIO as GPIO     #importing GPIO library and setting is as GPIO 

GPIO.setwarnings(False)     #Turning off unnecessary warnings in terminal

GPIO.setmode(GPIO.BOARD)    #this command enables you to use the GPIO pins on the pi by their numbers
GPIO.setup(40,GPIO.OUT)     #defining pin number 40 as an output pin
GPIO.output(40,GPIO.LOW)    #setting pin number 40 to output low (0V)

win = Tk()                  #creating the window for our GUI and naming it "win"

myFont = tkFont.Font(family = 'Helvetica', size = 36, weight = 'bold')      #defining a font for future uses in the GUI


def motorsON():                                                             #creating a function that will be called when the user presses Motors On or Motors off
                                                                            
    if GPIO.input(40):
        print("Tchou Tchou train is resting")                                       #prints out in the terminal that the SpiderBOT has stopped
        GPIO.output(40,GPIO.LOW)                                            #turns off the motors
        motorButton["text"] = "Motor ON"                                    #diplays Motor ON on the button when they are turned off so that when the button is pressed, motors turn on
    else:                                                                   
        GPIO.output(40,GPIO.HIGH)                                           #turns on motors
        print("Tchou Tchou train is on the run")                                    #prints out in the terminal that the SpiderBOT is moving
        motorButton["text"] = "Motors Off"                                  #diplays Motor OFF on the button when they are turned on so that when the button is pressed, motors turn off

def exitProgram():                                                          #creating a function that will be called when the exit button is pressed
    print("Tchou Tchou train is off for now")                                       #prints out in the terminal that Exit Button is pressed
    GPIO.cleanup()                                                          #cleans up all the pins used in the code (only pins that have been set in the code will be affected)
    win.quit()                                                              #quits the GUI

win.title("Tchou Tchoub train GUI")                                                  #giving the GUI a title that will appear at the top of it
win.geometry('800x480')                                                     #giving the GUI an inital creation size that can be adjusted by user

exitButtonn =  Button(win, text = 'Exit', font = myFont, command = exitProgram, height = 2, width = 6)      #defining a button called exitButton giving it the style attributes text/font/height/width.
                                                                                                            #The command is when the action taken when the button is pressed -> calls exitProgram function
exitButtonn.pack(side = BOTTOM)                                                                             #packs the button into the GUI and defines a location for it (bottom in this case)

motorButton = Button(win, text="Motors ON", font = myFont, command = motorsON ,height = 2, width = 8)       #defining a button called motorButton giving it the style attributes text/font/height/width
                                                                                                            #The command is when the action taken when the button is pressed -> calls motorsON function
motorButton.pack()                                                                                          #packs the button into the GUI and defines a location for it (by default top middle)

mainloop()                                                                                                  #infinite loop that runs the code
                                                                                                            #!! only to be called once and only when you are ready to run your application!!
