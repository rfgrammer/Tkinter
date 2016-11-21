from tkinter import *
from tkinter import messagebox


def main():

    root = Tk()

    messagebox.showinfo("Window Title", "Monkeys can live up to 300 years.")
    answer = messagebox.askquestion("Question 1", "Do you like silly faces?")

    if answer == 'yes':
        print(" 8===D-")

    root.mainloop()


if __name__ == "__main__":
    main()
