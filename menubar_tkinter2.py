#create an notepad..
from tkinter import *
def close():
    window.destroy()

window =Tk()

menubar=Menu(window)
file=Menu(menubar)
edit=Menu(menubar)
help=Menu(menubar)


file.add_command(label="new")
file.add_command(label="open")
file.add_command(label="save")
file.add_command(label="save as")
file.add_command(label="close",command=close)
file.add_command(label="exit")


menubar.add_cascade(label="file",menu=file)
menubar.add_cascade(label="edit",menu=edit)
menubar.add_cascade(label="help",menu=help)
window.config(menu=menubar)
window.mainloop()