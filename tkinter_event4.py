#Write Python GUI program that takes input string and change letter to upper case when a button is pressed.
import tkinter
def disp_upr():
    n=t1.get()
    n1=n.upper()
    t2.insert(0,n1)
Window=tkinter.Tk()
l1=tkinter.Label(Window,text="enter sentence:")
l1.grid(row=0,column=0)
t1=tkinter.Entry(Window)
t1.grid(row=0,column=1)
l2=tkinter.Label(Window,text="uppercase:")
l2.grid(row=1,column=0)
t2=tkinter.Entry(Window)
t2.grid(row=1,column=1)

b1=tkinter.Button(Window,text="convert",command=disp_upr,fg="red")
b1.grid(row=2,column=0)
b2=tkinter.Button(Window,text="exit",fg="red")
b2.grid(row=2,column=1)
Window.mainloop()
