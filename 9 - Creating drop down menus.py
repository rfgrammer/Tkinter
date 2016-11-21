from tkinter import *


def do_nothing():
    print("ok ok I won't...")


def main():
    root = Tk()

    main_menu = Menu(root)
    root.config(menu=main_menu)

    file_menu = Menu(main_menu)
    main_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New Project...", command=do_nothing)
    file_menu.add_command(label="New...", command=do_nothing)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=main_menu.quit)

    edit_menu = Menu(main_menu)
    main_menu.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Redo", command=do_nothing)

    root.mainloop()


if __name__ == "__main__":
    main()

