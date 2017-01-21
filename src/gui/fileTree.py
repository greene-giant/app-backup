
import tkinter as tk
from tkinter import ttk

try:
    from guiSettings import *
except:
    from .guiSettings import *


class FileTree(tk.Frame):
    def __init__(self, *arg, **kwargs):
        tk.Frame.__init__(self, *arg, background = COLOR_CARD, **kwargs)

        # Create scroll bar:
        scroll = ttk.Scrollbar(self, orient=tk.VERTICAL)
        scroll.pack(side = tk.RIGHT, fill = tk.Y, expand = False)

        # Create treeview:
        self.tree = tree = ttk.Treeview(self,
                                        yscrollcommand = scroll.set)
        tree.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)

        scroll.config(command = tree.yview)

        # Configure tree:
        tree["columns"] = ("name", "src", "dst")
        tree["show"] = 'headings'
        tree.heading("name", text = "Name")
        tree.heading("src", text = "Source")
        tree.heading("dst", text = "Destination")

        tree.column("name", anchor = tk.CENTER, 
                            stretch = False,
                            width = TREE_NAME_WIDTH,
                            minwidth = TREE_NAME_WIDTH)
        tree.column("src", anchor = tk.W)
        tree.column("dst", anchor = tk.W)

        s = ttk.Style()
        s.configure("Treeview.Heading", 
                    font = (TREE_HEADING_FONT, TREE_HEADING_SIZE))
        s.configure("Treeview", 
                    background = COLOR_CARD,
                    fieldbackground = COLOR_CARD,
                    font = (TREE_HEADING_FONT, TREE_HEADING_SIZE))


        # Create tags:
        tree.tag_configure("normal", 
                           background = COLOR_CARD,
                           foreground = COLOR_NORMAL,
                           font = (TREE_FONT, TREE_SIZE),
                           anchor = tk.CENTER)

        tree.tag_configure("error", 
                           background = COLOR_CARD,
                           foreground = COLOR_ERROR,
                           font = (TREE_FONT, TREE_SIZE),
                           anchor = tk.CENTER)

        tree.tag_configure("ready", 
                           background = COLOR_CARD,
                           foreground = COLOR_READY,
                           font = (TREE_FONT, TREE_SIZE),
                           anchor = tk.CENTER)


    def delete_selected(self):
        try:
            selected = self.tree.selection()
            print(selected)
            for s in selected:
                self.tree.delete(s)

            for s in self.tree.get_children():
                print(self.tree.item(s))
        except:
            pass


    def add_dummy_entry(self):
        self.tree.insert("", tk.END, iid=None, tags = "normal",
                    values=("Name",
                            "Source",
                            "Destination"))
        self.tree.yview_moveto(1)


    def add_entry(self, name, src, dest):
        self.tree.insert("", tk.END, iid=None, tags="normal",
                    values=(name, src, dest))
        self.tree.yview_moveto(1)


class TestApp(tk.Tk):
    def __init__(self, *arg, **kwargs):
        tk.Tk.__init__(self, *arg, **kwargs)

        self.title("File Tree Test")
        self.geometry("1000x400")
        self.minsize(800, 400)

        fileTree = FileTree(self)
        fileTree.pack(fill = tk.BOTH, expand = True)

        self.bind('a',
                lambda e: fileTree.add_dummy_entry())

        self.bind('<Delete>',
                lambda e: fileTree.delete_selected())



if __name__ == "__main__":
    app = TestApp()
    app.mainloop()


