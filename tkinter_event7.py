#all messege boxes..
from tkinter import *
from tkinter import messagebox
def show():
   k=messagebox.askyesno("HELLO","are YOU SURE?")
   if k==1:
      a=messagebox.showinfo("ALEART..","yes continue")
   else:
    messagebox.showerror("error","nothing")
   if a==1:
      messagebox.askokcancel("redirecr","you are redirecting")
   else:
      messagebox.askretrycancel("fine","thank you")
 
window=Tk()
window.geometry("400x500")

b1=Button(window,text="ok",command=show)
b1.grid(row=1,column=2)
window.mainloop()