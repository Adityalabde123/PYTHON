#genrate random password with ascii value...
from tkinter import *
from random import *
from string import *
def show():
    pas=""
    for i in range(0,8):
        pas=pas+choice(ascii_letters)
        t1.insert(0,pas)
        return
window=Tk()
window.geometry("300x300")

l1=Label(window,text="password:")
t1=Entry(window,width=20)
b1=Button(window,text="genrate password",command=show)

l1.grid(row=0,column=0)
t1.grid(row=0,column=1)
b1.grid(row=1,column=0)

window.mainloop()