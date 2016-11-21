from tkinter import *


def do_nothing():
    print("ok ok I won't...")


def main():
    root = Tk()

# Create Menu

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

# Create Toolbar

    toolbar = Frame(root, bg="blue")

    insert_button = Button(toolbar, text="Insert Image", command=do_nothing)
    insert_button.pack(side=LEFT, padx=2, pady=2)
    print_button = Button(toolbar, text="Print", command=do_nothing)
    print_button.pack(side=LEFT, padx=2, pady=2)

    toolbar.pack(side=TOP, fill=X)

    root.mainloop()


if __name__ == "__main__":
    main()

