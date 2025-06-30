# STEP1: import tkinter
from tkinter import *

from pyexpat.errors import messages

# STEP2: GUI interaction
window = Tk()
'''
# STEP3: Adding inputs
inp = Label(window,text = "Hello World!")
inp.pack()
# STEP4: Main loop
window.mainloop()
'''
'''
#Title - Dimension & Color for the Window Pop-up
#Default Title: tk
window.title("SIMPLE")
window.geometry("600x600")
window.config(bg="Skyblue")


#Create Frame and Buttons
#frame1=Frame(window,bg="Navy",width=450,height=300,cursor="dot")
frame1=Frame(window,width=450,height=300,cursor="dot")
#frame2=Frame(window,bg="Blue",width=450,height=300,cursor="dotbox")
frame2=Frame(window,width=450,height=300,cursor="dotbox")
button_1=Button(frame1,text="Button_1",bg="yellow")
button_2=Button(frame2,text="Button_2",bg="green")
button_3=Button(frame1,text="Logged",fg="Red")
frame1.pack(side=TOP)
frame2.pack(side=BOTTOM)
button_1.pack()
button_2.pack()
button_3.pack()
mainloop()
'''
'''
#entry box creation and locate them properly
window.title("SIMPLE")
window.geometry("600x600")

label_1=Label(window,text="Mail : ")
label_2=Label(window,text="Password : ")

e1=Entry(window,width=36,borderwidth=3)
e2=Entry(window,width=36,borderwidth=3)
label_1.grid(row=0,column=1)
label_2.grid(row=1,column=1)
e1.grid(row=0,column=2)
e2.grid(row=1,column=2)
#label_1.pack()
mainloop()
'''
'''
#allocate using pack
window.title("SIMPLE")
window.geometry("600x600")

label_1=Label(window,text="Label-1 : ",bg="Blue",fg="White")
label_2=Label(window,text="Label-2 : ",bg="Yellow",fg="Brown")
label_3=Label(window,text="Label-3 : ",bg="White",fg="Green")

label_1.pack(side=TOP,fill=X,expand=False)
label_2.pack(side=LEFT,fill=Y,expand=False)
label_3.pack(side=RIGHT,fill=Y,expand=False)
mainloop()
'''
'''
#handling button
window.title("SIMPLE")
window.geometry("600x600")

def log_entry():
    print("Logged IN")

button=Button(window, text="LOGIN",command=log_entry, width=12, bg="Navy",fg="White",font=("BOLD",12), activebackground="RED", activeforeground="Yellow")
button.pack()
mainloop()
'''
'''
#MENUBAR
menu=Menu(window)
file=Menu(menu, tearoff=0)
file.add_command(label="New")
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Save As")
file.add_separator()
file.add_command(label="Exit")

menu.add_cascade(label="File",menu=file)
window.config(menu=menu)

mainloop()
'''
'''
#MessageBox
import tkinter.messagebox
#STEP 3: Adding inputs
tkinter.messagebox.showinfo("Info","Running out of time")
#tkinter.messagebox.showwarning("Info","Running out of time")
#tkinter.messagebox.showerror("Info","Running out of time")
question=tkinter.messagebox.askyesno("Weather","Will it rain?")
#question=tkinter.messagebox.askokcancel("Weather","Will it rain?")
if question==True:
    print("Take an umbrella.")
else:
    print("Okay")
#STEP 4:main loop
mainloop()
'''
'''
#DRAWING
#STEP 3: Adding inputs
c=Canvas(window,width=600,height=600)
c.pack()

c.create_line(0,0,600,600,width=5,fill="Blue",dash=(1,1))
c.create_line(0,600,600,0,width=5,fill="Blue",dash=(1,1))

c.create_rectangle(150,125,450,375,fill="Yellow",outline="Red",width=5)

#STEP 4:main loop
mainloop()
'''
#Message Box 2
#window.geometry('600x600')
'''
message=Message(window,text="Python")
message.pack()
'''
'''
var=StringVar()
message=Message(window, textvariable=var, relief=RAISED,padx=15,pady=15)
var.set("Welcome")
message.pack()
mainloop()
'''
'''
#entrybox
var=StringVar()
ent_var=StringVar()

def insert():
    result=ent_var.get()
    var.set(result)

message=Message(window,textvariable=var,relief=RAISED,padx=60,pady=60)
entry=Entry(window, textvariable=ent_var)
button = Button(window,text="OK", command=insert)
message.pack()
entry.pack()
button.pack()
mainloop()
'''
'''
#checkbox
checkbox_1=IntVar()
checkbox_2=IntVar()
checkbox_3=IntVar()

check_button_1=Checkbutton(window,text="Apple",onvalue=1,offvalue=0, height=3,width=9)
check_button_2=Checkbutton(window,text="Mango",onvalue=1,offvalue=0, height=3,width=9)
check_button_3=Checkbutton(window,text="Plum",onvalue=1,offvalue=0, height=3,width=9)

check_button_1.pack()
check_button_2.pack()
check_button_3.pack()

mainloop()
'''
#Place :
window.geometry('600x600')

button=Button(window,text="Button", width=12)
button.place(x=240,y=30)
#STEP 4:main loop
mainloop()
