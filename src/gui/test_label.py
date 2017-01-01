import tkinter as tk
from tkinter import ttk


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.button = tk.Label(text="Checking Directories", 
                               foreground="#f6f3e8", 
                               background="#242424", 
                               font=("DejaVu Sans Mono", 16),
                               width=50,
                               anchor=tk.CENTER,
                               pady=5)
        self.button.pack()

    def start(self):
        pass


app = SampleApp()
app.mainloop()
