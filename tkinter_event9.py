from tkinter import *
def show():
    window.config(bg="red")
    
 
window=Tk()
window.geometry("400x500")

b1=Button(window,text="ok",command=show)
b1.grid(row=1,column=2)
window.mainloop()