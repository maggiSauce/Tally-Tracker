'''
This is an afternoon project I made because I was too bored to count on my fingers
'''

from tkinter import *
import sys

COUNTER = 0

# create Window 
window = Tk()
window.title("Tally Tracker")
window.geometry("250x200")
window.tk.call('tk', 'scaling', 2.0)
window.attributes('-topmost', True)

TALLYFONT = ("Arial", 35)

def btnExitClicked():
    window.destroy()

def btnUpClicked():
    global COUNTER 
    COUNTER = COUNTER + 1
    updateTally()

def btnDownClicked():
    global COUNTER 
    COUNTER -= 1
    updateTally()

def btnResetClicked():
    global COUNTER
    COUNTER = 0
    updateTally()

def updateTally():
    tally.config(text=str(COUNTER))

#  Create a label
tally = Label(window, text=COUNTER, font=TALLYFONT)
tally.place(x=50,y=0)

upButton = Button(window, text='+', command=btnUpClicked)
upButton.grid(column=0, row=0)
downButton = Button(window, text='-', command=btnDownClicked)
downButton.grid(column=0, row=1)
resetButton = Button(window, text='Reset', command=btnResetClicked)
resetButton.grid(column=1, row=2)

exitButton = Button(window, text='Exit', command = btnExitClicked)
exitButton.grid(column=2, row=2)

# scanner that scans to see what is happening in the GUI
window.mainloop()
