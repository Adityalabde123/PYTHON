#importing check button,radio button..
import tkinter
Window=tkinter.Tk()
l1=tkinter.Label(Window,text="enter number1:")
l1.grid(row=0,column=0)
t1=tkinter.Entry(Window,bg="yellow")
t1.grid(row=0,column=1)
l2=tkinter.Label(Window,text="enter number2:")
l2.grid(row=1,column=0)
t2=tkinter.Entry(Window,bg="pink")
t2.grid(row=1,column=1)

b1=tkinter.Button(Window,text="ok",fg="red")
b1.grid(row=2,column=0)
b2=tkinter.Button(Window,text="exit",fg="red")
b2.grid(row=2,column=1)

c1=tkinter.Checkbutton (Window,text="java")
c1.grid(row=3,column=0)
c2=tkinter.Checkbutton (Window,text="python")
c2.grid(row=3,column=1)
c3=tkinter.Checkbutton (Window,text="C++")
c3.grid(row=3,column=2)

r1=tkinter.Radiobutton (Window,text="male")
r1.grid(row=4,column=0)
r2=tkinter.Radiobutton (Window,text="female")
r2.grid(row=4,column=1)
Window.mainloop()
