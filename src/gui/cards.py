import tkinter as tk
from tkinter import ttk

try:
    import verticalScrolledFrame as vsw
    from guiSettings import *
except:
    from . import verticalScrolledFrame as vsw
    from .guiSettings import *

import subprocess as subp
import threading as thd


class ThreadedProcWrite(thd.Thread):
    def __init__(self, cardHolder, textBox, proc, tag):
        thd.Thread.__init__(self)
        self.cardHolder = cardHolder
        self.textBox = textBox
        self.proc = proc
        self.tag = tag

    def run(self):
        while True:
            line = self.proc.stdout.readline().decode("utf-8")
            if line == "" and self.proc.poll() != None:
                break
            elif line != "":
                print(line.rstrip())
                self.cardHolder.cards[-2].write_output(line.rstrip(), self.tag)
                self.cardHolder.move_scrollbar_to_bottom()




class OutputCard(tk.Frame):
    def __init__(self, *arg, title, source=None, destination=None, color, **kwargs):
        # Call original __init__:
        tk.Frame.__init__(self, *arg, background=COLOR_CARD, **kwargs)


        # Add vertical bar:
        bar = tk.Frame(self,
                       background=color,
                       width=CARD_BAR_WIDTH)
        bar.pack(side=tk.LEFT, fill=tk.Y)


        # Add content holder:
        content = tk.Frame(self,
                           background=COLOR_CARD)
        content.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


        # Add title:
        title = tk.Label(content,
                         text = title,
                         foreground = color,
                         background = COLOR_CARD,
                         font = (CARD_OUTPUT_TITLE_FONT, CARD_OUTPUT_TITLE_SIZE),
                         anchor = tk.CENTER,
                         pady = CARD_OUTPUT_TITLE_PADDING)
        title.pack(fill=tk.X)


        # Add directories:
        if source and destination:
            dirs = tk.Text(content,
                           height = 2,
                           foreground = color,
                           background = COLOR_CARD,
                           font = (CARD_OUTPUT_FONT, CARD_OUTPUT_SIZE),
                           padx = CARD_OUTPUT_PADDING_X,
                           pady = CARD_OUTPUT_PADDING_Y,
                           borderwidth = 0)
            dirsText  = "Source      :: " + source + "\n"
            dirsText += "Destination :: " + destination

            dirs.insert(tk.END, dirsText)
            dirs["state"] = "disabled"
            dirs.pack(fill=tk.X)


        # Add horizontal bar:
        bar = tk.Frame(content,
                       background = color,
                       height = CARD_HBAR_WIDTH)
        bar.pack(fill = tk.X)


        # Add output:
        self.output = output = tk.Text(content,
                                       height = 2,
                                       foreground = COLOR_NORMAL,
                                       background = COLOR_CARD,
                                       font = (CARD_OUTPUT_FONT, CARD_OUTPUT_SIZE),
                                       padx = CARD_OUTPUT_PADDING_X,
                                       pady = CARD_OUTPUT_PADDING_Y,
                                       borderwidth = 0,
                                       wrap=tk.NONE)

        output.insert(tk.END, "\n")
        output["state"] = "disabled"
        output.tag_config("normal", foreground = COLOR_NORMAL)
        output.tag_config("clean", foreground = COLOR_CLEAN)
        output.tag_config("error", foreground = COLOR_ERROR)
        output.tag_config("dir check", foreground = COLOR_DIRCHECK)
        output.tag_config("center", justify='center')

        output.pack(fill = tk.BOTH, expand=True)


    def write_output(self, line, tag="normal"):
        self.output["state"] = "normal"
        self.output["height"] += 1
        self.output.insert(tk.END, line + "\n", tag)
        self.output["state"] = "disabled"
        self.output.update()



class TitleCard(tk.Frame):
    def __init__(self, *arg, text, color, **kwargs):
        # Call original __init__:
        tk.Frame.__init__(self, *arg, **kwargs)

        # Add vertical bar:
        bar = tk.Frame(self,
                       background=color,
                       width=CARD_BAR_WIDTH)
        bar.pack(side=tk.LEFT, fill=tk.Y)

        # Add title label:
        label = tk.Label(self, 
                         text=text,
                         foreground=color,
                         background=COLOR_CARD,
                         font=(CARD_TITLE_FONT, CARD_TITLE_SIZE),
                         anchor=tk.CENTER,
                         pady=CARD_TITLE_PADDING)
        label.pack(side=tk.LEFT, fill=tk.X, expand=True)




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

        # widget reference holder:
        self.cards = []


    def add_card_spacing(self):
        self.cards.append(tk.Frame(self.content,
                                   height=CARD_PADDING_Y,
                                   background=COLOR_PADDING))

        self.cards[-1].pack(fill=tk.X)



    def add_title_card(self, text, color):
        self.cards.append(TitleCard(self.content, 
                                    text=text, 
                                    color=color))

        self.cards[-1].pack(fill=tk.X)

        self.add_card_spacing()
        self.move_scrollbar_to_bottom()


    def clear_output(self):
        for c in self.cards:
            c.destroy()

        self.cards = []
        self.move_scrollbar_to_top()


    def add_dirCheck_card(self, color):
        self.cards.append(OutputCard(self.content,
                                     title="Checking Directories",
                                     color=color))
        self.cards[-1].pack(fill=tk.X)

        self.add_card_spacing()
        self.move_scrollbar_to_bottom()


    def get_current_card(self):
        return self.cards[-2]


    def start_test_output(self, title, source, destination, color):
        self.cards.append(OutputCard(self.content,
                                     title=title,
                                     source=source,
                                     destination=destination,
                                     color=color))
        self.cards[-1].pack(fill=tk.X)

        self.add_card_spacing()
        self.move_scrollbar_to_bottom()


        # Run test script:
        cmd = "python outputTest.py"
        proc = subp.Popen(cmd, 
                          shell=True, 
                          bufsize=0, 
                          stdout=subp.PIPE, 
                          stderr=subp.STDOUT)

        t = ThreadedProcWrite(self, self.cards[-2], proc, "normal")
        t.start()






class TestApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Card Test")
        self.geometry("1000x400")
        self.minsize(800,200)

        cardHolder = CardHolder(self)
        cardHolder.grid(column=0, row=0, sticky=sticky_all)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.bind('a', 
                lambda e, t="Starting Backup", c=COLOR_COPY: 
                cardHolder.add_title_card(t, c))

        self.bind('s',
                lambda e: 
                cardHolder.start_test_output(
                    title="Test Output",
                    source="the/source/directory",
                    destination="the/destination/directory",
                    color=COLOR_COPY))

        self.bind('d', 
                lambda e, t="Backup Complete", c=COLOR_COPY: 
                cardHolder.add_title_card(t, c))

        self.bind('x',
                lambda e: cardHolder.clear_output())


if __name__ == "__main__":
    app = TestApp()
    app.mainloop()

