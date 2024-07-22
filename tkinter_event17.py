#change the label arial bold italic with check boxes
from tkinter import *
def change_font():
    l1.config(font=('Gigi',20))
def change_font2():
    l1.config(font=('Gigi',20,'bold'))
def change_font3():
    l1.config(font=('Gigi',20,'italic'))




window=Tk()
window.geometry("300x300")

l1=Label(window,text="HII EVERYONE:")
c1=Checkbutton(window,text="GIGI",command=change_font)
c2=Checkbutton(window,text="BOLD",command=change_font2)
c3=Checkbutton(window,text="ITALIC",command=change_font3)


l1.grid(row=0,column=0)
c1.grid(row=1,column=0)
c2.grid(row=2,column=0)
c3.grid(row=3,column=0)


window.mainloop()