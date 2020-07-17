from tkinter import *

# These boolean variables are here to decide on which operation to perform on hitting 'equal' button. They're
# to be called inside each of operation button's functions, once the corresponding operation button has been hit.
summing = False
subtracting = False
multiplying = False
dividing = False

# Flash memory for last shown value, to be updated in each operation
last_number = 0

# Standard values for buttons formatting
padx_std = 30
pady_std = 15
font_std = 8


# tkinter general starting and configuration
root = Tk()
root.title("Simple Calculator")
root.configure(background='#aaa')

# button functions definitions
def button_click(number):
    global last_number
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def button_clear():
    global last_number
    last_number = 0
    e.delete(0,END)

def button_adder():
    global summing
    global last_number
    last_number = e.get()
    e.delete(0,END)
    summing = True

def button_subtracter():
    global subtracting
    global last_number
    last_number = e.get()
    e.delete(0,END)
    subtracting = True

def button_multiplier():
    global multiplying
    global last_number
    last_number = e.get()
    e.delete(0,END)
    multiplying = True

def button_divider():
    global dividing
    global last_number
    last_number = e.get()
    e.delete(0,END)
    dividing = True

    
def button_equal():
    global summing, subtracting, multiplying, dividing
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
    elif dividing == True:
        diva = float(last_number) / float(e.get())
        e.delete(0,END)
        e.insert(0,str(round(diva,3)))
    summing = False
    subtracting = False
    multiplying = False
    dividing = False
    
# Calculator "screen": Defining, configuring and displaying
e = Entry(root, width = int(0.7*padx_std), borderwidth = 5, justify=RIGHT)
e.config(font=(25))
e.grid(row=0, column=0, columnspan = 3, ipadx=15, ipady=5, padx= 10, pady = 10)

# Buttons definition (both numbers and operations)
button_1 = Button(root, text="1", font=(font_std), padx= padx_std, pady= pady_std, command = lambda: button_click(1))
button_2 = Button(root, text="2", font=(font_std), padx= padx_std, pady= pady_std, command = lambda: button_click(2))
button_3 = Button(root, text="3", font=(font_std), padx= padx_std, pady= pady_std, command = lambda: button_click(3))
button_4 = Button(root, text="4", font=(font_std), padx= padx_std, pady= pady_std, command = lambda: button_click(4))
button_5 = Button(root, text="5", font=(font_std), padx= padx_std, pady= pady_std, command = lambda: button_click(5))
button_6 = Button(root, text="6", font=(font_std), padx= padx_std, pady= pady_std, command = lambda: button_click(6))
button_7 = Button(root, text="7", font=(font_std), padx= padx_std, pady= pady_std, command = lambda: button_click(7))
button_8 = Button(root, text="8", font=(font_std), padx= padx_std, pady= pady_std, command = lambda: button_click(8))
button_9 = Button(root, text="9", font=(font_std), padx= padx_std, pady= pady_std, command = lambda: button_click(9))
button_0 = Button(root, text="0", font=(font_std), padx= padx_std, pady= pady_std, command = lambda: button_click(0))
button_add = Button(root, text="+", font=(font_std), padx= padx_std-1, pady= pady_std, command = button_adder, bg="#fdd")
button_subtract = Button(root, text="-", font=(font_std), padx= int(1.05*padx_std), pady= pady_std, command = button_subtracter, bg="#ddf")
button_multiply = Button(root, text="x", font=(font_std), padx= padx_std, pady= pady_std, command = button_multiplier, bg="#ffd")
button_divide = Button(root, text="%", font=(font_std), padx= int(0.9*padx_std), pady= pady_std, command = button_divider, bg="#ecf")
button_equal = Button(root, text="=", font=(font_std), padx= int(3.8*padx_std), pady= pady_std, command = button_equal, bg="#cfc")
button_clear = Button(root, text="Clear", font=(font_std), padx= int(0.54*padx_std), pady= pady_std, command = button_clear, bg="#fff")

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
button_clear.grid(row=4, column=1)
button_add.grid(row=4, column=2)
button_multiply.grid(row=5, column=0)
button_divide.grid(row=5, column=1)
button_subtract.grid(row=5, column=2)
button_equal.grid(row=6, columnspan=3) 

root.mainloop()