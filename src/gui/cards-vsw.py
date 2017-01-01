import tkinter as tk
from tkinter import ttk

import verticalScrolledFrame as vsw
from settings import *

sticky_all = (tk.N, tk.S, tk.E, tk.W)



class CardHolder(vsw.VerticalScrolledFrame):
    def __init__(self, *arg, **kwargs):
        # Call original __init__:
        vsw.VerticalScrolledFrame.__init__(self, 
                                           *arg, 
                                           frameBackground=COLOR_PADDING,
                                           **kwargs)

        # Add left padding:
        paddingL = tk.Frame(self.interior, 
                            background=COLOR_PADDING,
                            width=CARD_PADDING_X)
        paddingL.pack(side=tk.LEFT, fill=tk.Y, expand=False)


        # Add content frame:
        self.content = tk.Frame(self.interior,
                                background=COLOR_PADDING)
        self.content.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        
        # Add right padding:
        paddingR = tk.Frame(self.interior, 
                            background=COLOR_PADDING,
                            width=CARD_PADDING_X)
        paddingR.pack(side=tk.LEFT, fill=tk.Y, expand=False)

        # Add initial vertical padding:
        padding = tk.Frame(self.content,
                           height=CARD_PADDING_Y,
                           background=COLOR_PADDING)
        padding.pack(fill=tk.X)

    def add_title_card(self, text, color):
        label = tk.Label(self.content,
                         text=text,
                         foreground=color,
                         background=COLOR_CARD,
                         font=("DejaVu Sans Mono", 16),
                         anchor=tk.CENTER,
                         pady=CARD_TITLE_PADDING)
        label.pack(fill=tk.X)

        padding = tk.Frame(self.content,
                           height=CARD_PADDING_Y,
                           background=COLOR_PADDING)
        padding.pack(fill=tk.X)

        self.move_scrollbar_to_bottom()

        



class TestApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Card Test")
        self.geometry("1000x400")

        cardHolder = CardHolder(self)
        cardHolder.grid(column=0, row=0, sticky=sticky_all)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.bind('a', lambda e: cardHolder.add_title_card("Insert Text", COLOR_COPY))


if __name__ == "__main__":
    app = TestApp()
    app.mainloop()

