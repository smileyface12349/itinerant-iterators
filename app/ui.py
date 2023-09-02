from tkinter import Tk, ttk


def main():
    """Main entry point for the UI"""
    # TODO: implement a proper UI
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    root.mainloop()


if __name__ == "__main__":
    main()
