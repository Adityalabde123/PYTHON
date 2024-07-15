import tkinter as t
from tkinter import *
def add_item():
   v=t1.get()
   lst1.insert(lst1.size(),v)  #inserting at line by line 
  ## lst1.insert(0,v)#another way

def remove_item():
   pos=lst1.curselection() #selecting an item..
   lst1.delete(pos,pos)  #selected item deleted

def remove_all():
   lst1.delete(0,lst1.size())
window=Tk()
window.geometry("500x500")
l1=Label(window,text="enter item")
l2=Label(window,text="All setup")
t1=Entry(window,width="10")
lst1=Listbox(window)
b1=Button(window,text="add",command=add_item)
b2=Button(window,text="remove",command=remove_item)
b3=Button(window,text="remove all",command=remove_all)
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
t1.grid(row=0,column=1)
lst1.grid(row=1,column=1)
b1.grid(row=2,column=1)
b2.grid(row=2,column=2)
b3.grid(row=2,column=3)
window.mainloop()