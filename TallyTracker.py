from tkinter import *

# create Window 
window = Tk()
window.title("Tally Tracker")

# set Window size
window.geometry("480x270")

#scales a window
window.tk.call('tk', 'scaling', 10.0)

# scanner that scans to see what is happening in the GUI
window.mainloop()'

#  Create a label
label = Label(window, text='Click to increment your tally: ')
label.grid(column=0, row=0)
sb = Spinbox(window, from_=0, to=100)
sb.grid(column=1, row=0)

upButton = Button(window, text='+')
upButton.grid(column=0, row=2)
downButton = Button(window, text='-')
downButton.grid(column=0, row=3)

exitButton = Button(window, text='Exit')
exitButton.grid(column=1, row=2)