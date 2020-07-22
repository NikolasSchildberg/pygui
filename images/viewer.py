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

# Creating the image objects
my_img1 = ImageTk.PhotoImage(Image.open("img1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("img2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("img3.jpg"))

img_list = [my_img1,my_img2,my_img3]

# Passing the iamge objects to the labes
my_label = Label(image=my_img1)
my_label.grid(row = 0,column = 0)

# defining the buttons
button_prev = Button(root,text="Click Here!")
button_quit = Button(root,text="Click Here!",command=root.destroy)
button_next = Button(root,text="Click Here!")

# displaying the button
button_prev.grid(row = 1,column =0)
button_quit.grid(row = 1,column =1)
button_next.grid(row = 1,column =2)

root.mainloop()