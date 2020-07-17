from tkinter import *

i = 0

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width = 35, borderwidth = 5)
e.grid(row=0, column=0, columnspan = 3, padx=10, pady=10)
e.insert(0,"Message")
	
def myClick():
    global i
    texttoprint = "Hoy!"
    Label(root,text=texttoprint+str(i)).grid(column = i%2)
    i += 1
			
myButton = Button(root, text="click Here!", command=myClick)
myButton.grid(row=2,column=2)

print("Got it!")
 
root.mainloop()
