from tkinter import *
from math import *

root = Tk(className = "Simple Calculaltor")

first_number = ""
math = ""
second_number =""

def button_click(number):
   current =  text_field.get()
   text_field.delete(0, END)
   text_field.insert(0, str(current) + str(number))

def clear():
   text_field.delete(0, END)

def add():
   global first_number, math
   math = "add"
   first_number = float(text_field.get())
   text_field.delete(0, END)
   
def subtract():
   global first_number, math
   math = "subtract"
   first_number = float(text_field.get())
   text_field.delete(0, END)
   
def multiply():
   global first_number,  math
   math = "multiply"
   first_number = float(text_field.get())
   text_field.delete(0, END)
   
def divide():
   global first_number, math
   math = "divide"
   first_number = float(text_field.get())
   text_field.delete(0, END)
   
def equal():
   global first_number, math, second_number
   second_number = float(text_field.get())
   text_field.delete(0, END)
   
   if math == "add":
      text_field.insert(0, first_number + second_number)
      
   elif math == "subtract":
      text_field.insert(0, first_number - second_number)

   elif math == "multiply":
      text_field.insert(0, first_number * second_number)

   elif math == "divide":
      text_field.insert(0, first_number / second_number)

   else:
      text_field.insert(0, text_field.get())

def square():
   ab = text_field.get()
   ab_i = float(ab)
   ab_s = ab_i**2
   text_field.delete(0, END)
   text_field.insert(0, str(ab_s))

def square_root():
   ab = text_field.get()
   ab_i = float(ab)
   text_field.delete(0, END)
   text_field.insert(0, str(sqrt(ab_i)))


# Defining buttons 
text_field        =  Entry(root, width=50, borderwidth=2)
button_1          =  Button(root, text="1", padx=40, pady =20, command=lambda: button_click(1))
button_2          =  Button(root, text="2", padx=40, pady =20, command=lambda: button_click(2))
button_3          =  Button(root, text="3", padx=40, pady =20, command=lambda: button_click(3))
button_4          =  Button(root, text="4", padx=40, pady =20, command=lambda: button_click(4))
button_5          =  Button(root, text="5", padx=40, pady =20, command=lambda: button_click(5))
button_6          =  Button(root, text="6", padx=40, pady =20, command=lambda: button_click(6))
button_7          =  Button(root, text="7", padx=40, pady =20, command=lambda: button_click(7))
button_8          =  Button(root, text="8", padx=40, pady =20, command=lambda: button_click(8))
button_9          =  Button(root, text="9", padx=40, pady =20, command=lambda: button_click(9))
button_0          =  Button(root, text="0", padx=40, pady =20, command=lambda: button_click(0))
button_add        =  Button(root, text="+", padx=20, pady =20, command= add)
button_multiply   =  Button(root, text="x", padx=20, pady =20, command= multiply)
button_divide     =  Button(root, text="/", padx=20, pady =20, command= divide)
button_subtract   =  Button(root, text="-", padx=20, pady =20, command= subtract)
button_equal      =  Button(root, text="=", padx=39, pady =20, command= equal)
button_square     =  Button(root, text ="^2", padx=35, pady=20, command= square)
button_squareRoot =  Button(root, text ="sqrt", padx=33, pady=20, command= square_root)
button_clear      =  Button(root, text="Clear", padx=82, pady =20, command= clear)



#Putting buttons on to the screen
text_field.grid(row=0, column = 0, columnspan=3, padx=10, pady=10) 

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_multiply.grid(row=3, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_divide.grid(row=2, column=3)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_subtract.grid(row=1, column=3)

button_0.grid(row=4, column=0)
button_square.grid(row=4, column=1)
button_squareRoot.grid(row=4, column=2)
button_add.grid(row=4, column=3)


button_clear.grid(row=5, column=0, columnspan=2)
button_equal.grid(row=5, column=2)




root.mainloop()