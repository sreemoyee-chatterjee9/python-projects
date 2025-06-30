#STEP_1: importing
from tkinter import *

#STEP_2: GUI Interaction
window = Tk()
window.geometry('600x600')

#STEP_3: Adding Inputs

#ENTRY BOX
entry_box=Entry(window,width=60,borderwidth=6)
entry_box.place(x=0,y=0)

#BUTTONS

def click(num):
    result=entry_box.get()
    entry_box.delete(0,END)
    entry_box.insert(0,str(result) + str(num))

button_1=Button(window, text='0',width=12, command=lambda:click(0))
button_1.place(x=0,y=60)
button_1=Button(window, text='1',width=12, command=lambda:click(1))
button_1.place(x=100,y=60)
button_1=Button(window, text='2',width=12, command=lambda:click(2))
button_1.place(x=200,y=60)
button_1=Button(window, text='3',width=12, command=lambda:click(3))
button_1.place(x=300,y=60)
button_1=Button(window, text='4',width=12, command=lambda:click(4))
button_1.place(x=400,y=60)
button_1=Button(window, text='5',width=12, command=lambda:click(5))
button_1.place(x=0,y=90)
button_1=Button(window, text='6',width=12, command=lambda:click(6))
button_1.place(x=100,y=90)
button_1=Button(window, text='7',width=12, command=lambda:click(7))
button_1.place(x=200,y=90)
button_1=Button(window, text='8',width=12, command=lambda:click(8))
button_1.place(x=300,y=90)
button_1=Button(window, text='9',width=12, command=lambda:click(9))
button_1.place(x=400,y=90)

#OPERATORS
def add():
    n1=entry_box.get()
    global math
    math = "Addition"
    global i
    i = int(n1)
    entry_box.delete(0,END)

def subtract():
    n1=entry_box.get()
    global math
    math = "Subtraction"
    global i
    i = int(n1)
    entry_box.delete(0,END)

def multiply():
    n1=entry_box.get()
    global math
    math = "Multiply"
    global i
    i = int(n1)
    entry_box.delete(0,END)

def division():
    n1=entry_box.get()
    global math
    math = "Division"
    global i
    i = int(n1)
    entry_box.delete(0,END)

def equal():
    n2=entry_box.get()
    entry_box.delete(0,END)
    if math == "Addition":
        entry_box.insert(0,i+int(n2))
    elif math == "Subtraction":
        entry_box.insert(0, i - int(n2))
    elif math == "Multiply":
        entry_box.insert(0, i * int(n2))
    elif math == "Division":
        entry_box.insert(0, i / int(n2))

def clear():
    entry_box.delete(0,END)

button_1=Button(window, text='+',width=12,command=add)
button_1.place(x=0,y=120)
button_1=Button(window, text='-',width=12,command=subtract)
button_1.place(x=100,y=120)
button_1=Button(window, text='*',width=12,command=multiply)
button_1.place(x=200,y=120)
button_1=Button(window, text='/',width=12,command=division)
button_1.place(x=300,y=120)
button_1=Button(window, text='=',width=12,command=equal)
button_1.place(x=400,y=120)
button_1=Button(window, text='Clear',width=12,command=clear)
button_1.place(x=0,y=150)

#STEP_4: mainloop
mainloop()
