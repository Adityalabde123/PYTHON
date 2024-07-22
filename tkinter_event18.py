#change the label red,yellow,pink with radio button..

from tkinter import *
def show1():
    l1.config(bg="red")
def show2():
    l1.config(bg="pink")
def show3():
    l1.config(bg="yellow")




window=Tk()
window.geometry("300x300")

l1=Label(window,text="HII EVERYONE:")
r1=Radiobutton(window,text="red",command=show1,value=1)
r2=Radiobutton(window,text="pink",command=show2,value=2)
r3=Radiobutton(window,text="yellow",command=show3,value=3)


l1.grid(row=0,column=0)
r1.grid(row=1,column=0)
r2.grid(row=2,column=0)
r3.grid(row=3,column=0)


window.mainloop()