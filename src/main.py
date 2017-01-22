
import os

from settings import *
from gui.guiSettings import COLOR_DIRCHECK
import gui.main

import threading as thd

class ThreadedDirectoryCheck(thd.Thread):
    def __init__(self, tree, card):
        thd.Thread.__init__(self)
        self.tree = tree
        self.card = card
        self.allExist = True

    def run(self):
        for e in self.tree.get_children():
            [name, src, dest] = self.tree.item(e)['values']
            srcExist  = os.path.exists(src)
            destExist = os.path.exists(dest)

            self.allExist = self.allExist and srcExist and destExist
            
            if (srcExist and destExist):
                # Change the file tree row tag to ready:
                self.tree.item(e, tags="ready")
            else:
                # Change the file tree row tag to error:
                self.tree.item(e, tags="error")

                # Print the error message:
                self.card.write_output(name, ["normal", "center"])

                if not srcExist:
                    line = "Source does not exist      : " + src
                    tag = "error"
                else:
                    line = "Source                     : " + src
                    tag = "normal"
                self.card.write_output(line, tag)


                if not destExist:
                    line = "Destination does not exist : " + src
                    tag = "error"
                else:
                    line = "Destination                : " + src
                    tag = "normal"
                self.card.write_output(line, tag)

                self.card.write_output("\n")



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

        # Bindings:
        self.bind('<Delete>',
                lambda e: self.FT.delete_selected())

        # Flags:
        self.dirs_all_found = False


    def _on_add_press(self):
        print("** New add pressed **")

    def _on_save_press(self):
        print("** New save pressed **")

    def _on_check_press(self):
        # Checks that all the source and desitination directories exist

        # Print card header:
        self.CH.add_dirCheck_card(COLOR_DIRCHECK)
        card = self.CH.get_current_card()

        # Do check:
        #t = ThreadedDirectoryCheck(self.FT.tree, self.CH.get_current_card())
        #t.start()


        # Do check:
        allExist = True
        for e in self.FT.tree.get_children():
            [name, src, dest] = self.FT.tree.item(e)['values']
            srcExist  = os.path.exists(src)
            destExist = os.path.exists(dest)

            allExist = allExist and srcExist and destExist
            
            if (srcExist and destExist):
                # Change the file tree row tag to ready:
                self.FT.tree.item(e, tags="ready")
            else:
                # Change the file tree row tag to error:
                self.FT.tree.item(e, tags="error")

                # Print the error message:
                card.write_output(name, ["normal", "center"])

                if not srcExist:
                    line = "Source does not exist      : " + src
                    tag = "error"
                else:
                    line = "Source                     : " + src
                    tag = "normal"
                card.write_output(line, tag)


                if not destExist:
                    line = "Destination does not exist : " + src
                    tag = "error"
                else:
                    line = "Destination                : " + src
                    tag = "normal"
                card.write_output(line, tag)

                card.write_output("\n")

        # Print all good:
        if allExist:
            card.write_output("All directories found", ["dir check", "center"])
            self.dirs_all_found = True


    def _on_change_press(self):
        print("** New change pressed **")

    def _on_start_press(self):
        print("** New start pressed **")

    def _on_clean_press(self):
        print("** New clean pressed **")

    def _on_cancel_press(self):
        print("** New cancel pressed **")

    def _on_clear_press(self):
        self.CH.clear_output()


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()

