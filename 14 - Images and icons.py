from tkinter import *

root = Tk()

photo = PhotoImage(file="linux.png")
label = Label(root, image=photo)
label.pack()

root.mainloop()

