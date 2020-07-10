from tkinter import *
count = 1
root = Tk()

e = Entry(root, width=50, borderwidth = 5, )
e.pack()


def myClick():
	myLabel = Label(root, text="Button pressed!")
	myLabel.pack()
	
#myButton = Button(root, text="click Here!", state=DISABLED)
myButton = Button(root, text="Enter your name", padx=50, pady=15, command=myClick, bg="#aaaaff", fg="#000000")
myButton.pack()

 
root.mainloop()
