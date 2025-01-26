from tkinter import *
import sys

COUNTER = 0
# create Window 
window = Tk()
window.title("Tally Tracker")

# set Window size
window.geometry("480x270")

#scales a window
window.tk.call('tk', 'scaling', 2.0)

def btnExitClicked():
    window.destroy()

def btnUpClicked():
    counter = counter + 1
    print(COUNTER)

def btnDownClicked():
    COUNTER -= 1

def btnResetClicked():
    COUNTER = 0

#  Create a label
label = Label(window, text='Tally: ')
label.grid(column=0, row=0)

tally = Label(window, text=COUNTER)
tally.grid(column=1, row=0)

upButton = Button(window, text='+', command=btnUpClicked)
upButton.grid(column=0, row=2)
downButton = Button(window, text='-', command=btnDownClicked)
downButton.grid(column=0, row=3)
resetButton = Button(window, text='Reset', command=btnResetClicked)
resetButton.grid(column=1, row=5)

exitButton = Button(window, text='Exit', command = btnExitClicked)
exitButton.grid(column=2, row=5)


# scanner that scans to see what is happening in the GUI
window.mainloop()