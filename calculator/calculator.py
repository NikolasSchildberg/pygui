from tkinter import *

root = Tk()
butpad = 15
go = 'c '

e = Entry(root, borderwidth = 5)
e.grid(row=0,column=0, columnspan=3)
	
def myClick():
    e.insert(-1,go)
#	texttoprint = "Hoy!"
#	Label(root,text=texttoprint).grid(row=0,column=0)
		
	
#myButton = Button(root, text="click Here!", state=DISABLED)
b1 = Button(root, text="1", padx=butpad, pady=butpad, command=myClick, bg="#888888", fg="#ffffff")
b1.grid(row=1,column=0)
b2 = Button(root, text="2", padx=butpad, pady=butpad, command=myClick, bg="#888888", fg="#ffffff")
b2.grid(row=1,column=1)
b3 = Button(root, text="3", padx=butpad, pady=butpad, command=myClick, bg="#888888", fg="#ffffff")
b3.grid(row=1,column=2)
b4 = Button(root, text="4", padx=butpad, pady=butpad, command=myClick, bg="#888888", fg="#ffffff")
b4.grid(row=2,column=0)
b5 = Button(root, text="5", padx=butpad, pady=butpad, command=myClick, bg="#888888", fg="#ffffff")
b5.grid(row=2,column=1)
b6 = Button(root, text="6", padx=butpad, pady=butpad, command=myClick, bg="#888888", fg="#ffffff")
b6.grid(row=2,column=2)
b7 = Button(root, text="7", padx=butpad, pady=butpad, command=myClick, bg="#888888", fg="#ffffff")
b7.grid(row=3,column=0)
b8 = Button(root, text="8", padx=butpad, pady=butpad, command=myClick, bg="#888888", fg="#ffffff")
b8.grid(row=3,column=1)
b9 = Button(root, text="9", padx=butpad, pady=butpad, command=myClick, bg="#888888", fg="#ffffff")
b9.grid(row=3,column=2)


print("Got it!")
 
root.mainloop()
