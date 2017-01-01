import tkinter as tk
from tkinter import ttk


FOREGROUND_COLOR = "#cae682"
BACKGROUND_COLOR = "#242424"
TEXT_COLOR = "#f6f3e8"


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Title Card Test")

        verticalBar = tk.Frame(self, background=FOREGROUND_COLOR, width=10)
        verticalBar.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.S, tk.E))



        titleLabel = tk.Label(self,
                              text="Starting Backup",
                              foreground=FOREGROUND_COLOR,
                              background=BACKGROUND_COLOR,
                              font=("DejaVu Sans Mono", 16),
                              width=50,
                              anchor=tk.CENTER,
                              pady=5)

        titleLabel.grid(column=1, row=0, stick=(tk.N, tk.W, tk.S, tk.E))


        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

    def start(self):
        pass


app = SampleApp()
app.mainloop()
