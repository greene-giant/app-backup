"""

A class providing the menu functionality.

"""

from function.backupThread import BackupThread

from ui.terminal.card import CardPrinter, clearTerminal
from ui.terminal.directoryManager import DirectoryManager
import color.terminal as terminal


dirOptions = {"1" : "Add",
              "2" : "Save",
              "3" : "Check",
              "4" : "Change"}

backupOptions = {"a" : "Backup",
                 "b" : "Clean",
                 "c" : "Clear"}


class Menu(object):
    """
    The menu class. Provided functionality for everything except the backup
    and cleaning. Hooks are left to add that functionality later. 
    """

    def __init__(self):
        self.DM = DirectoryManager()
        self.CP = CardPrinter()
        self.previousOpt = None

        # Create a dictionary relating options to functions:
        self.functions = {}

        for d in [dirOptions, backupOptions]:
            for k, v in d.items():
                self.functions[v] = getattr(self, "opt_" + v.lower())


    def printMenu(self):
        CP = self.CP
        DM = self.DM

        # Clear the terminal:
        clearTerminal()

        print("")

        # Print directories:
        CP.header()
        CP.lineCentered("Directories")
        CP.line()
        DM.printDirectories()
        CP.separator()

        # Print directory options:
        CP.lineCentered("Directory Options ")
        CP.line()
        space = 10*" "
        line = space

        for k, v in sorted(dirOptions.items()):
            line += k + ". " + v + space

        CP.lineCentered(line)
        CP.separator()

        # Print backup options:
        CP.lineCentered("Backup Options")
        CP.line()
        line = space

        for k, v in sorted(backupOptions.items()):
            line += k + ". " + v + space

        CP.lineCentered(line)

        if self.previousOpt:
            CP.separator()
            CP.lineCentered("Previous selection : " + self.previousOpt)
            self.previousOpt = None

        CP.footer()
        print("")

        opt = input(" Your selection (q to quit) : ")

        while (opt not in dirOptions and opt not in backupOptions and opt != "q"):
            opt = input(" Invalid option. Please select again (q to quit) : ")

        return opt


    def run(self):
        quit = False

        while (not quit):
            opt = self.printMenu()
            func = self.optionToFunction(opt)
            
            if func:
                self.functions[func]()
            else:
                quit = True
                clearTerminal()



    def optionToFunction(self, opt):
        if opt in dirOptions:
            func = dirOptions[opt]

        elif opt in backupOptions:
            func = backupOptions[opt]

        else:
            func = None

        return func



    def opt_add(self):
        print(" ")
        print(" Adding new directory")
        name = input(" Name :: ")

        src = input(" Path to source directory       :: ")
        while (not self.DM.dirExists(src)):
            print("")
            terminal.printColor(terminal.red, " Directory does not exists.")
            src = input(" Path to source directory       :: ")


        dest = input(" Path to destination directory :: ")
        while (not self.DM.dirExists(dest)):
            print("")
            terminal.printColor(terminal.red, " Directory does not exists.")
            dest = input(" Path to destination directory :: ")


        # Confirm the new directory:
        print("")
        self.CP.header()
        self.CP.lineCentered("Add Directory")
        self.CP.line(name)
        self.CP.line("Source      :: " + src)
        self.CP.line("Destination :: " + dest)
        self.CP.footer()
        y = input("Is this correct (y/n)? ")

        if y == 'y':
            self.DM.addDir(name, src, dest)

        self.previousOpt = "Add directory"




    def opt_save(self):
        self.DM.saveDirectories()
        self.previousOpt = "Save directories"



    def opt_check(self):
        self.DM.checkDirs()
        self.previousOpt = "Check directories"



    def opt_change(self):
        print("")
        terminal.printColor(terminal.red, "Changing directory prefix not currently implemented.")
        print("")

        self.waitForEnter()
        self.previousOpt = "Change directory prefixes"



    def opt_backup(self):
        DM = self.DM

        if DM.ranCheckDirs and DM.allValid:
            BT = BackupThread(self.CP, self.DM.dirs.dirs)
            BT.start()
            BT.join()
        elif not DM.ranCheckDirs:
            print("")
            terminal.printColor(terminal.red, "Check directories before backup")
            print("")
        else:
            print("")
            terminal.printColor(terminal.red, "Fix directories before backup")
            print()

        self.waitForEnter()
        self.previousOpt = "Backup"



    def opt_clean(self):
        self.previousOpt = "Clean destination directories"



    def opt_clear(self):
        clearTerminal()
        self.previousOpt = "Clear output"


    def waitForEnter(self):
        s = input("Press enter to return to menu.")





if __name__ == "__main__":
    m = Menu()
    m.run()

