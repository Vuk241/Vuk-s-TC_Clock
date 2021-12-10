from tkinter import *
import datetime
import time

root=Tk ()

lbl: Label = Label (root, text='00:00:00')
lbl.pack()


font = ('Calibri' ,80, 'bold')
bg = 'orange'
fg = 'black'

lbl ['font'] = font
lbl ['bg'] = bg
lbl ['fg'] = fg

while True:
    time.sleep(1)

    currentTime = datetime.datetime.now() .strftime('%H:%M:%S')

    lbl['text'] = str(currentTime)
    lbl.update()

root.title ('Clock')
root.mainloop ()