#pack method..
 
import tkinter
window=tkinter.Tk()
window.geometry("500x500")
b1=tkinter.Button(window,text='cdj')

b1.pack(side='top',pady=5)#another side top,bottom,left,right
window.mainloop()