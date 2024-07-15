import tkinter
def disp_square():
    n=t1.get()
    n=int(n)
    s=n*n
    t2.insert(0,s)
Window=tkinter.Tk()
l1=tkinter.Label(Window,text="enter number1:")
l1.grid(row=0,column=0)
t1=tkinter.Entry(Window)
t1.grid(row=0,column=1)
l2=tkinter.Label(Window,text="Result:")
l2.grid(row=1,column=0)
t2=tkinter.Entry(Window)
t2.grid(row=1,column=1)

b1=tkinter.Button(Window,text="Square",command=disp_square,fg="red")
b1.grid(row=2,column=0)
b2=tkinter.Button(Window,text="exit",fg="red")
b2.grid(row=2,column=1)
Window.mainloop()
