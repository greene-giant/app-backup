import tkinter as tk
from tkinter import ttk

import color.wombat

COLOR_COPY  = color.wombat.green
COLOR_CLEAN = color.wombat.red
COLOR_CARD  = color.wombat.black
COLOR_PADDING = color.wombat.gray

CARD_PADDING = 8
CARD_BAR_WIDTH = 10
CARD_TITLE_PADDING = 20

sticky_all = (tk.N, tk.S, tk.E, tk.W)

class TitleCard(tk.Frame):

    def __init__(self, *args, titleText, color, **kwargs):
        tk.Frame.__init__(self, *args, background=COLOR_PADDING, **kwargs)

        # Add right and left padding:
        leftPadding = tk.Frame(self, width=CARD_PADDING, background=COLOR_PADDING)
        leftPadding.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))

        center = tk.Frame(self)
        center.grid(column=1, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))

        rightPadding = tk.Frame(self, width=CARD_PADDING, background=COLOR_PADDING)
        rightPadding.grid(column=2, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=0)

        self.rowconfigure(0, weight=1)

        # Add center padding:
        topPadding    = tk.Frame(center, height=CARD_PADDING, background=COLOR_PADDING)
        bottomPadding = tk.Frame(self, height=CARD_PADDING, background=COLOR_PADDING)
        content       = tk.Frame(center, background=COLOR_CARD)

        topPadding.grid(   column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        content.grid(      column=0, row=1, sticky=(tk.N, tk.S, tk.E, tk.W))
        bottomPadding.grid(column=0, row=2, sticky=(tk.N, tk.S, tk.E, tk.W))

        center.columnconfigure(0, weight=1)
        center.rowconfigure(0, weight=0)
        center.rowconfigure(1, weight=1)
        center.rowconfigure(2, weight=0)


        # Add vertical bar:
        verticalBar = tk.Frame(content, background=color, width=CARD_BAR_WIDTH)
        verticalBar.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))

        titleLabel = tk.Label(content,
                              text=titleText,
                              foreground=color,
                              background=COLOR_CARD,
                              font=("DejaVu Sans Mono", 16),
                              width=50,
                              anchor=tk.CENTER,
                              pady=CARD_TITLE_PADDING)
        titleLabel.grid(column=1, row=0, sticky=sticky_all)

        content.columnconfigure(0, weight=0)
        content.columnconfigure(1, weight=1)
        content.rowconfigure(0, weight=1)






class TestApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Cards Test")
        self.geometry("1000x400")

        startBackupCard = TitleCard(self, titleText="Starting Backup", color=COLOR_COPY)
        startBackupCard.grid(column=0, row=0, sticky=(tk.N, tk.E, tk.W))

        startBackupCard = TitleCard(self, titleText="Backup Complete", color=COLOR_COPY)
        startBackupCard.grid(column=0, row=1, sticky=(tk.N, tk.E, tk.W))

        startBackupCard = TitleCard(self, titleText="Starting Clean", color=COLOR_CLEAN)
        startBackupCard.grid(column=0, row=2, sticky=(tk.N, tk.E, tk.W))

        startBackupCard = TitleCard(self, titleText="Clean Complete", color=COLOR_CLEAN)
        startBackupCard.grid(column=0, row=3, sticky=(tk.N, tk.E, tk.W))

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)



if __name__ == "__main__":
    app = TestApp()
    app.mainloop()

