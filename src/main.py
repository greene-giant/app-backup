
import os

from settings import *
from dirs import *
from gui.guiSettings import COLOR_DIRCHECK, COLOR_COPY
import gui.main

import subprocess as subp
import threading as thd
import time

class ThreadedDirectoryCheck(thd.Thread):
    def __init__(self, tree, card):
        thd.Thread.__init__(self)
        self.tree = tree
        self.card = card
        self.allExist = True

    def run(self):
        backupList = self.tree.get_children()

        for e in backupList:
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

            if e != backupList[-1]:
                time.sleep(BACK_PAUSE)


class BackupThread(thd.Thread):
    def __init__(self, tree, CH):
        thd.Thread.__init__(self)
        self.tree = tree
        self.CH = CH

    def run(self):
        backupList = self.tree.get_children()

        # Start card:
        self.CH.add_title_card("Starting Backup",
                               COLOR_COPY)

        # Backup
        for e in backupList:
            [name, src, dest] = self.tree.item(e)['values']

            # Create card:
            self.CH.add_output_card(name, src, dest, COLOR_COPY)
            card = self.CH.get_current_card()

            # Create cmd:
            cp = 'xcopy '
            flags = r' /s /D /y'
            cmd = cp + r'"' + src + r'" "' + dest + r'" ' + flags

            # Run backup:
            proc = subp.Popen(cmd, 
                              shell=True,
                              bufsize=0,
                              stdout=subp.PIPE,
                              stderr=subp.STDOUT)

            while True:
                line = proc.stdout.readline().decode("utf-8")
                if line == "" and proc.poll() != None:
                    break
                elif line != "":
                    card.write_output(line.rstrip(), "normal")
                    self.CH.move_scrollbar_to_bottom()


            # Add space for remove check:
            card.write_output(" ", "normal")

            # Find old files:
            numOldFiles = 0

            for fullDirName, subDirList, fileList in os.walk(dest):
                lenDest = len(dest)
                dirName = fullDirName[lenDest:]

                if os.path.exists(src + dirName):
                    for f in fileList:
                        if os.path.exists(src + dirName + "\\" + f):
                            pass
                        else:
                            if dirName:
                                fileName = dirName[1:] + '\\' + f
                            else:
                                fileName = f

                            numOldFiles += 1
                            card.write_output(fileName, "clean")

                else:
                    if fileList:
                        for f in fileList:
                            fileName = dirName[1:] + '\\' + f
                            numOldFiles += 1
                            card.write_output(fileName, "clean")
                    else:
                        numOldFiles += 1
                        card.write_output(dirName[1:] + '\\', "clean")

            card.write_output("{} Old file(s)".format(numOldFiles), "normal")

            
            # Add a pause between cards:
            if e != backupList[-1]:
                time.sleep(BACK_PAUSE)

        # End card:
        self.CH.add_title_card("Backup Completed",
                               COLOR_COPY)
            



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
        if self.dirs_all_found:
            t = BackupThread(self.FT.tree, self.CH)
            t.start()

        else:
            self.CH.add_title_card("Directory check must pass before backup",
                                   COLOR_DIRCHECK)




    def _on_clean_press(self):
        print("** New clean pressed **")

    def _on_cancel_press(self):
        print("** New cancel pressed **")

    def _on_clear_press(self):
        self.CH.clear_output()


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()

