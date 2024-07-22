#create all arithmatic opration...
from tkinter import *
def add():
    t3.delete(0,"end")
    a=t1.get()
    b=t2.get()
    a=int(a)
    b=int(b)
    c=a+b
    t3.insert(0,c)   
def sub():
    t3.delete(0,"end")
    a=t1.get()
    b=t2.get()
    a=int(a)
    b=int(b)
    c=a-b
    t3.insert(0,c)   
def mul():
    t3.delete(0,"end")
    a=t1.get()
    b=t2.get()
    a=int(a)
    b=int(b)
    c=a*b
    t3.insert(0,c)   

def div():
    t3.delete(0,"end")
    a=t1.get()
    b=t2.get()
    a=int(a)
    b=int(b)
    c=a/b
    t3.insert(0,c)   



window=Tk()
window.geometry("500x500")
menubar=Menu(window)
Arithmetic=Menu(menubar)
Arithmetic.add_command(label="ADD",command=add)
Arithmetic.add_command(label="SUB",command=sub)
Arithmetic.add_command(label="MUL",command=mul)
Arithmetic.add_command(label="DIV",command=div)
menubar.add_cascade(label="OPERATIONS",menu=Arithmetic)
window.config(menu=menubar)

l1=Label(text="enter number1:")
l1.grid(row=0,column=0)
t1=Entry(width="10")
t1.grid(row=0,column=1)
l2=Label(text="enter number2:")
l2.grid(row=1,column=0)
t2=Entry(width="10")
t2.grid(row=1,column=1)
l3=Label(text="result:")
l3.grid(row=2,column=0)
t3=Entry(width="10")
t3.grid(row=2,column=1)


window.mainloop()
