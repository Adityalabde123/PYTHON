import tkinter

def add_num():
    n1=t1.get()
    n2=t2.get()
    a1=int(n1)
    a2=int(n2)

    s=a1+a2
    t3.insert(0,s)

Window=tkinter.Tk()
Window.geometry("500x500")
l1=tkinter.Label(Window,text="enter number1:")
l1.grid(row=0,column=0)
t1=tkinter.Entry(Window,width="10")
t1.grid(row=0,column=1)
l2=tkinter.Label(Window,text="enter number2:")
l2.grid(row=1,column=0)
t2=tkinter.Entry(Window,width="10")
t2.grid(row=1,column=1)
l3=tkinter.Label(Window,text="result:")
l3.grid(row=2,column=0)
t3=tkinter.Entry(Window,width="10")
t3.grid(row=2,column=1)

b1=tkinter.Button(Window,text="add",fg="red",command=add_num)
b1.grid(row=3,column=0)
b2=tkinter.Button(Window,text="exit",fg="red")
b2.grid(row=3,column=1)
Window.mainloop()
