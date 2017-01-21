
from settings import *
import gui.main

class MainApp(gui.main.MainAppGUI):
    def __init__(self, *arg, **kwargs):
        gui.main.MainAppGUI.__init__(self, *arg, **kwargs)
        self.title("Backup")


        # Load files from settings file:
        for e in BACKUP_DIRS:
            self.FT.add_entry(e[0], e[1], e[2])

        # Change button commands:
        self.BB.dir_addButton.configure(   command = self._on_add_press)
        self.BB.dir_saveButton.configure(  command = self._on_save_press)
        self.BB.dir_checkButton.configure( command = self._on_check_press)
        self.BB.dir_changeButton.configure(command = self._on_change_press)
        
        self.BB.back_startButton.configure( command = self._on_start_press)
        self.BB.back_cleanButton.configure( command = self._on_clean_press)
        self.BB.back_cancelButton.configure(command = self._on_cancel_press)
        self.BB.back_clearButton.configure( command = self._on_clear_press)


    def _on_add_press(self):
        print("** New add pressed **")

    def _on_save_press(self):
        print("** New save pressed **")

    def _on_check_press(self):
        print("** New check pressed **")

    def _on_change_press(self):
        print("** New change pressed **")

    def _on_start_press(self):
        print("** New start pressed **")

    def _on_clean_press(self):
        print("** New clean pressed **")

    def _on_cancel_press(self):
        print("** New cancel pressed **")

    def _on_clear_press(self):
        print("** New clear pressed **")


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()

