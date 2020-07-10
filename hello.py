from tkinter import *

root = Tk()

my_label1 = Label(root,text="Hello World!")
my_label2 = Label(root,text="My Name is Nikolas")
my_label3 = Label(root,text="And this is my first\npython app")

my_label1.pack()
my_label2.pack()
my_label3.pack()

root.mainloop()
