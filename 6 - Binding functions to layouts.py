from tkinter import *


def print_name(event):
    print("My name is Charles")


def main():
    root = Tk()
    button_1 = Button(root, text="Print my name")
    button_1.bind("<Button-1>", print_name)
    button_1.pack()

    root.mainloop()


if __name__ == "__main__":
    main()

