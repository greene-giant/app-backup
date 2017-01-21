
import tkinter as tk
from tkinter import ttk

try:
    from guiSettings import *
except:
    from .guiSettings import *


class ButtonBar(tk.Frame):
    def __init__(self, *arg, **kwargs):
        tk.Frame.__init__(self, *arg, **kwargs)

        # Directories frame:
        dirGroup = tk.LabelFrame(self, 
                                 text = "Directories",
                                 font = (BUTTONBAR_BUTTON_FONT, BUTTONBAR_BUTTON_SIZE),
                                 padx = BUTTONBAR_FRAME_PADX_INNER,
                                 pady = BUTTONBAR_FRAME_PADY_INNER)

        dirGroup.pack(side = tk.LEFT, 
                      fill = tk.X, 
                      padx = BUTTONBAR_FRAME_PADX_OUTTER,
                      pady = BUTTONBAR_FRAME_PADY_OUTTER)

        # Add buttons:
        dir_addButton = ttk.Button(dirGroup, 
                                   text = "Add",
                                   command = self._on_add_press)
        dir_addButton.pack(side = tk.LEFT, padx = BUTTONBAR_BUTTON_PADX)


        # Save buttton:
        dir_saveButton = ttk.Button(dirGroup, 
                                    text = "Save",
                                    command = self._on_save_press)
        dir_saveButton.pack(side = tk.LEFT, padx = BUTTONBAR_BUTTON_PADX)


        # Check button:
        dir_checkButton = ttk.Button(dirGroup, 
                                     text = "Check",
                                     command = self._on_check_press)
        dir_checkButton.pack(side = tk.LEFT, padx = BUTTONBAR_BUTTON_PADX)


        # Change button:
        dir_changeButton = ttk.Button(dirGroup, 
                                      text = "Change",
                                      command = self._on_change_press)
        dir_changeButton.pack(side = tk.LEFT, padx = BUTTONBAR_BUTTON_PADX)

        

        # Backup frame:
        backGroup = tk.LabelFrame(self, 
                                  text = "Backup",
                                  font = (BUTTONBAR_BUTTON_FONT, BUTTONBAR_BUTTON_SIZE),
                                  padx = BUTTONBAR_FRAME_PADX_INNER,
                                  pady = BUTTONBAR_FRAME_PADY_INNER)

        backGroup.pack(side = tk.RIGHT, 
                       fill = tk.X, 
                       padx = BUTTONBAR_FRAME_PADX_OUTTER,
                       pady = BUTTONBAR_FRAME_PADY_OUTTER)

        # Start button:
        back_startButton = ttk.Button(backGroup, 
                                      text = "Start",
                                      command = self._on_start_press)
        back_startButton.pack(side = tk.LEFT, padx = BUTTONBAR_BUTTON_PADX)

        # Clean button:
        back_cleanButton = ttk.Button(backGroup, 
                                      text = "Clean",
                                      command = self._on_clean_press)
        back_cleanButton.pack(side = tk.LEFT, padx = BUTTONBAR_BUTTON_PADX)

        # Cancel button:
        back_cancelButton = ttk.Button(backGroup, 
                                       text = "Cancel",
                                       command = self._on_cancel_press)
        back_cancelButton.pack(side = tk.LEFT, padx = BUTTONBAR_BUTTON_PADX)

        # Clear button:
        back_clearButton = ttk.Button(backGroup, 
                                      text = "Clear",
                                      command = self._on_clear_press)
        back_clearButton.pack(side = tk.LEFT, padx = BUTTONBAR_BUTTON_PADX)


        # Configure buttons and frames:
        s = ttk.Style()
        s.configure("TButton", 
                    font = (BUTTONBAR_BUTTON_FONT, BUTTONBAR_BUTTON_SIZE))

        s.configure("Labelframe", 
                    font = (BUTTONBAR_BUTTON_FONT, BUTTONBAR_BUTTON_SIZE))

    def _on_add_press(self):
        print("Add pressed")

    def _on_save_press(self):
        print("Save pressed")

    def _on_check_press(self):
        print("Check pressed")

    def _on_change_press(self):
        print("Change pressed")

    def _on_start_press(self):
        print("Start pressed")

    def _on_clean_press(self):
        print("Clean pressed")

    def _on_cancel_press(self):
        print("Cancel pressed")

    def _on_clear_press(self):
        print("Clear pressed")


class TestApp(tk.Tk):
    def __init__(self, *arg, **kwargs):
        tk.Tk.__init__(self, *arg, **kwargs)

        self.title("Button Bar Test")
        self.geometry("1000x200")
        self.minsize(800, 200)

        filler = tk.Frame(self, height=50, background=COLOR_PADDING)
        filler.pack(fill=tk.BOTH, expand=True)

        buttonBar = ButtonBar(self)
        buttonBar.pack(fill=tk.X)

        filler = tk.Frame(self, height=50, background=COLOR_PADDING)
        filler.pack(fill=tk.BOTH, expand=True)


if __name__ == "__main__":
    app = TestApp()
    app.mainloop()

