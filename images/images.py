# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 14:41:15 2020

@author: nschildberg
"""

from tkinter import *
from PIL import ImageTk, Image

# first stuff
root = Tk()
root.title("Niko's Image Viewer")

# setting an icon for your window
icon_img = PhotoImage(file='icon1.png')
root.tk.call('wm', 'iconphoto', root._w, icon_img)

my_img = ImageTk.PhotoImage(Image.open("icon3.png"))
my_label = Label(image=my_img)
my_label.pack()

# defining the button
button_quit = Button(root,text="Click Here!",command=root.destroy)

# displaying the button
button_quit.pack()

root.mainloop()