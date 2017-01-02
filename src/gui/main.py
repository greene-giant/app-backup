
import tkinter as tk
from tkinter import ttk

from settings import *
import buttonBar, cards, fileTree

APP_HEIGHT = 1000
APP_WIDTH = 1000

APP_MIN_HEIGHT = 800
APP_MIN_WIDTH = 800

class MainApp(tk.Tk):
    def __init__(self, *arg, **kwargs):
        tk.Tk.__init__(self, *arg, **kwargs)

        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()

        xpos = int(ws/2 - APP_WIDTH/2)
        ypos = int(hs/2 - APP_HEIGHT/2)

        self.title("Full GUI Test")
        self.geometry("{}x{}+{}+{}".format(APP_WIDTH, APP_HEIGHT,
                                           xpos, ypos))
        self.minsize(APP_MIN_WIDTH, APP_MIN_HEIGHT)

        FT = fileTree.FileTree(self, height=int(0.3*APP_HEIGHT))
        FT.pack(fill = tk.X, expand = False)

        BB = buttonBar.ButtonBar(self)
        BB.pack(fill = tk.X)

        CH = cards.CardHolder(self)
        CH.pack(fill = tk.BOTH, expand = True)


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()

