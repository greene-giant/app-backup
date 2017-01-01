import tkinter as tk
from tkinter import ttk

import verticalScrolledFrame as vsw
from settings import *

sticky_all = (tk.N, tk.S, tk.E, tk.W)



class CardHolder(vsw.VerticalScrolledFrame):
    def __init__(self, *arg, **kwargs):
        # Call original __init__:
        vsw.VerticalScrolledFrame.__init__(self, *arg, **kwargs)

        # Create a scrollable canvas to hold the content frame:
        title = tk.Label(self.interior, text="Stuff", background=COLOR_PADDING)
        title.pack(fill=tk.X, expand=True)
        



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

