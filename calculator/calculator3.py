from tkinter import *

summing = False
subtracting = False
multiplying = False

last_number = 0

#starting the stuff
root = Tk()
root.title("Simple Calculator")

# button functions definitions
def button_click(number):
    global last_number
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
    #last_number = e.get()

def button_clear():
    global last_number
    last_number = 0
    e.delete(0,END)

def button_add():
    global summing
    global last_number
    last_number = e.get()
    e.delete(0,END)
#    e.insert(0,str(last_number)+"+")
    summing = True

def button_subtract():
    global subtracting
    global last_number
    last_number = e.get()
    e.delete(0,END)
#    e.insert(0,str(last_number)+"+")
    subtracting = True

def button_multiply():
    global multiplying
    global last_number
    last_number = e.get()
    e.delete(0,END)
#    e.insert(0,str(last_number)+"+")
    multiplying = True
    
def button_equal():
    global summing, subtracting, multiplying
    global last_number
    if summing == True:
        suma = float(last_number) + float(e.get())
        e.delete(0, END)
        e.insert(0,str(round(suma,1)))
    elif subtracting == True:
        suba = float(last_number) - float(e.get())
        e.delete(0, END)
        e.insert(0,str(round(suba,1)))
    elif multiplying == True:
        multa = float(last_number) * float(e.get())
        e.delete(0,END)
        e.insert(0,str(round(multa,1)))
    summing = False
    subtracting = False
    multiplying = False

# the little field where typed things appear
e = Entry(root, width = 35, borderwidth = 5)
e.grid(row=0, column=0, columnspan = 3, padx=10, pady=10)

padx_std = 40
pady_std = 20

# defining the buttons
button_1 = Button(root, text="1", padx= padx_std, pady= pady_std, command = lambda: button_click(1))
button_2 = Button(root, text="2", padx= padx_std, pady= pady_std, command = lambda: button_click(2))
button_3 = Button(root, text="3", padx= padx_std, pady= pady_std, command = lambda: button_click(3))
button_4 = Button(root, text="4", padx= padx_std, pady= pady_std, command = lambda: button_click(4))
button_5 = Button(root, text="5", padx= padx_std, pady= pady_std, command = lambda: button_click(5))
button_6 = Button(root, text="6", padx= padx_std, pady= pady_std, command = lambda: button_click(6))
button_7 = Button(root, text="7", padx= padx_std, pady= pady_std, command = lambda: button_click(7))
button_8 = Button(root, text="8", padx= padx_std, pady= pady_std, command = lambda: button_click(8))
button_9 = Button(root, text="9", padx= padx_std, pady= pady_std, command = lambda: button_click(9))
button_0 = Button(root, text="0", padx= padx_std, pady= pady_std, command = lambda: button_click(0))
button_add = Button(root, text="+", padx= padx_std, pady= pady_std, command = button_add)
button_subtract = Button(root, text="-", padx= padx_std, pady= pady_std, command = button_subtract)
button_mult = Button(root, text="x", padx= padx_std, pady= pady_std, command = button_multiply)
button_equal = Button(root, text="=", padx= padx_std-3, pady= pady_std, command = button_equal)
button_clear = Button(root, text="Clear", padx= padx_std-9, pady= pady_std, command = button_clear)

# displaying buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
button_add.grid(row=4, column=1)
button_subtract.grid(row=4, column=2)
button_equal.grid(row=5, column=2)
button_clear.grid(row=5, column = 1)
button_mult.grid(row=5, column=0)
 
root.mainloop()