from tkinter import *
from tkinter import messagebox
def show():
  s1=val.get()
  messagebox.showinfo("ok",s1)
         
window=Tk()
window.geometry("400x300")
val=StringVar()
r1=Radiobutton(window,text="FY",value="FYBCA",variable=val)   
r2=Radiobutton(window,text="SY",value="SYBCA",variable=val)   
r3=Radiobutton(window,text="TY",value="TYBCA",variable=val)
b1=Button(window,text="OK",command=show)
r1.grid(row=0,column=0) 
r2.grid(row=0,column=1) 
r3.grid(row=0,column=2) 
b1.grid(row=1,column=2) 
window.mainloop()