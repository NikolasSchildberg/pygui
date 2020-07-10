from tkinter import *

root = Tk()

def myClick():
	myLabel = Label(root, text="Look!\n You clicked a button!\n")
	myLabel.pack()

#myButton = Button(root, text="click Here!", state=DISABLED)
myButton = Button(root, text="Click Here!!!", padx=50, pady=15, command=myClick, bg="#aaaaff", fg="#000000")
myButton.pack()

 
root.mainloop()
