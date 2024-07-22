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


l1.place(x=100,y=0)
r1.place(x=50,y=80)
r2.place(x=50,y=100)
r3.place(x=50,y=120)

window.mainloop()