#place x and y cordinates
import tkinter
window=tkinter.Tk()
window.geometry("500x500")
b1=tkinter.Button(window,text='cdj')

b1.place(x=300,y=10)#another side top,bottom,left,right
window.mainloop()