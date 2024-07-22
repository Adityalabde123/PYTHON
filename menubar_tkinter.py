#create color selecter...
from tkinter import *
def c1():
    window.config(bg="pink")
def c2():
    window.config(bg="yellow")
def c3():
    window.config(bg="orange")
window =Tk()

menubar=Menu(window)
color=Menu(menubar)
color=Menu(menubar)

color.add_command(label="pink",command=c1)
color.add_command(label="yellow",command=c2)
color.add_command(label="orange",command=c3)

menubar.add_cascade(label="COLOR",menu=color)
window.config(menu=menubar)
window.mainloop()