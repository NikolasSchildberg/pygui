from tkinter import *

root = Tk()

for i in range(10):
    for j in range(10):
        if (((i+j) % 2)==0): color = "black"
        if (((i+j) % 2)==1): color = "white"
        squaredd = Button(root,width = 4, height = 2, bg=color, state=DISABLED)
        squaredd.grid(row=i, column = j, padx = 0, pady = 0)
Button(root,text="Quit!",command=root.destroy).grid(columnspan=10, padx=20, pady=20)
root.mainloop()