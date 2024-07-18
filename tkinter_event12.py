#genrate random strong password
import tkinter
import random
def random_password():
     s="abcdefghijklmnopqrstuvwxyz0123456789"
     p=""
     for i in range(0,10):
          p=p+random.choice(s)
     t1.insert(0,p) 


Window=tkinter.Tk()
Window.geometry("500x500")
l1=tkinter.Label(Window,text="PASSWORD:")
l1.grid(row=0,column=0)
t1=tkinter.Entry(Window,width="10")
t1.grid(row=0,column=1)
b1=tkinter.Button(Window,text="ok",fg="red",command=random_password)
b1.grid(row=4,column=0)
Window.mainloop()