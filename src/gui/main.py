
import tkinter as tk
from tkinter import ttk


try:
    from guiSettings import *
    import buttonBar, cards, fileTree
except:
    from .guiSettings import *
    from . import buttonBar, cards, fileTree


class MainAppGUI(tk.Tk):
    def __init__(self, *arg, **kwargs):
        tk.Tk.__init__(self, *arg, **kwargs)

        # Get screen dimensions:
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()

        # Calculate window position:
        xpos = int(ws/2 - APP_WIDTH/2)
        ypos = int(hs/2 - APP_HEIGHT/2)

        # Window settings:
        self.title("Full GUI Test")
        self.geometry("{}x{}+{}+{}".format(APP_WIDTH, APP_HEIGHT,
                                           xpos, ypos))
        self.minsize(APP_MIN_WIDTH, APP_MIN_HEIGHT)

        # Build app GUI:
        FT = fileTree.FileTree(self, height=int(TREE_FRACTION_HEIGHT*APP_HEIGHT))
        FT.pack(fill = tk.X, expand = False)

        BB = buttonBar.ButtonBar(self)
        BB.pack(fill = tk.X)

        CH = cards.CardHolder(self)
        CH.pack(fill = tk.BOTH, expand = True)


if __name__ == "__main__":
    app = MainAppGUI()
    app.mainloop()

