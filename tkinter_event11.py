#coverting digit into words..

import tkinter
def num_words():
    n=t1.get()
    d={"0":"zero","1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine","10":"ten"}
    s1=""
    for digit in n:
        s1=s1+" "+d[digit]
    t2.insert(0,s1)


Window=tkinter.Tk()
Window.geometry("500x500")
l1=tkinter.Label(Window,text="enter number1:")
l1.grid(row=0,column=0)
t1=tkinter.Entry(Window,width="10")
t1.grid(row=0,column=1)
l2=tkinter.Label(Window,text="convert in words:")
l2.grid(row=1,column=0)
t2=tkinter.Entry(Window,width="10")
t2.grid(row=1,column=1) 
b1=tkinter.Button(Window,text="ok",fg="red",command=num_words)
b1.grid(row=4,column=0)
Window.mainloop()
