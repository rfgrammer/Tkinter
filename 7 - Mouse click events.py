from tkinter import *


def click_left(event):
    print("Left")


def click_middle(event):
    print("Middle")


def click_right(event):
    print("Right")


def main():
    root = Tk()
    frame = Frame(root, width=300, height=250)
    frame.bind("<Button-1>", click_left)
    frame.bind("<Button-2>", click_middle)
    frame.bind("<Button-3>", click_right)
    frame.pack()

    root.mainloop()


if __name__ == '__main__':
    main()
