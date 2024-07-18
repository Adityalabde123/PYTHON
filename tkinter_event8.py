#slips..
from tkinter import *
from tkinter import messagebox
def show():
     v = int(t1.get())
     if val.get() == 1:
            flag = 0
            if v < 2:
                flag = 1
            else:
                for i in range(2, int(v / 2) + 1):
                    if v % i == 0:
                        flag = 1
                        break
            if flag == 1:
                messagebox.showinfo("Prime Number", "The number is not prime")
            else:
                messagebox.showinfo("Prime Number", "The number is prime")
        
     elif val.get() == 2:
            Sum = 0
            for i in range(1, v):
                if v % i == 0:
                    Sum += i
            if Sum == v:
                messagebox.showinfo("Perfect Number", "The number is perfect")
            else:
                messagebox.showinfo("Perfect Number", "The number is not perfect")
        
     elif val.get() == 3:
            s = 0
            num = v
            while v > 0:
                d = v % 10
                s = s + (d ** 3)
                v = v // 10
            if num == s:
                messagebox.showinfo("Armstrong Number", "The number is an Armstrong number")
            else:
                messagebox.showinfo("Armstrong Number", "The number is not an Armstrong number")
window=Tk()
window.geometry("400x300")
val=IntVar()

l1=Label(window,text="enter number")
t1=Entry(window,width="10")
r1=Radiobutton(window,text="prime",value=1,variable=val)   
r2=Radiobutton(window,text="perfect",value=2,variable=val)   
r3=Radiobutton(window,text="armstrong",value=3,variable=val)
b1=Button(window,text="OK",command=show)

l1.grid(row=0,column=0)
t1.grid(row=0,column=1)
r1.grid(row=1,column=0) 
r2.grid(row=2,column=0) 
r3.grid(row=3,column=0) 
b1.grid(row=4,column=2) 
window.mainloop()