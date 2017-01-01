import tkinter.ttk.tix as tk
#from tkinter import ttk

from settings import *

sticky_all = (tk.N, tk.S, tk.E, tk.W)



class CardHolder(tk.Frame):
    def __init__(self, *arg, **kwargs):
        # Call original __init__:
        tk.Frame.__init__(self, *arg, **kwargs)

        # Add content frame:
        content = tk.ScrolledWindow(self, background=COLOR_PADDING, scrollbar=tk.Y)
        content.pack(fill=tk.BOTH, expand=True)


class TestApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Card Test")
        self.geometry("1000x400")

        cardHolder = CardHolder(self)
        cardHolder.grid(column=0, row=0, sticky=sticky_all)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)


if __name__ == "__main__":
    app = TestApp()
    app.mainloop()

