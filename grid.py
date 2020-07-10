from tkinter import *

root = Tk()

# Creating label widgets
myLabel1 = Label(root,text="Hello World!")
myLabel2 = Label(root,text="My Name is Nikolas")

#Shoving them onto the screen
#my_label3 = Label(root,text="And this is my first\npython app")

myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=8)

root.mainloop()
