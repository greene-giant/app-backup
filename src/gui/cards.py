import tkinter as tk
from tkinter import ttk

from settings import *

sticky_all = (tk.N, tk.S, tk.E, tk.W)



class CardHolder(tk.Frame):
    def __init__(self, *arg, **kwargs):
        # Call original __init__:
        tk.Frame.__init__(self, *arg, **kwargs)

        # Create a scrollable canvas to hold the content frame:
        self.canvas = tk.Canvas(self)
        self.canvas.pack(side="left", fill="both", expand=True)

        # Add a scroll bar:
        scroll = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.canvas.yview)
        scroll.pack(side="right", fill="y")
        self.canvas['yscrollcommand'] = scroll.set



        # Add content frame:
        self.content = tk.Frame(self.canvas, height=40, width=40, background=COLOR_PADDING)
        self.canvas.create_window((0,0), window=self.content, anchor='nw')




        self.content.bind("<Configure>", self.onFrameConfigure)

        self.populate()

    def populate(self):
        '''Put in some fake data'''
        for row in range(100):
            tk.Label(self.content, text="%s" % row, width=3, borderwidth="1", 
                     relief="solid").grid(row=row, column=0)
            t="this is the second column for row %s" %row
            tk.Label(self.content, text=t).grid(row=row, column=1)


    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))



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

