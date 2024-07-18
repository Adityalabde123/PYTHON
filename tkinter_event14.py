#change the letter into uppercase..
import tkinter
def uppercase():
    s=t1.get()
    s1=""
    for ch in s:
        if ch>='a' and ch<='z':
            s1=s1+ch.upper()
    t2.insert(0,s1)
Window=tkinter.Tk()
Window.geometry("500x500")
l1=tkinter.Label(Window,text="enter string:")
l1.grid(row=0,column=0)
t1=tkinter.Entry(Window,width="10")
t1.grid(row=0,column=1)
l2=tkinter.Label(Window,text="uppercase string:")
l2.grid(row=1,column=0)
t2=tkinter.Entry(Window,width="10")
t2.grid(row=1,column=1) 
b1=tkinter.Button(Window,text="ok",fg="red",command=uppercase)
b1.grid(row=4,column=0)
Window.mainloop()