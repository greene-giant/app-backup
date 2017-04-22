"""

A class providing the menu functionality.

"""

from ui.terminal.card import CardPrinter, clearTerminal
from ui.terminal.directoryManager import DirectoryManager


dirOptions = {"1" : "Add",
              "2" : "Save",
              "3" : "Check",
              "4" : "Change"}

backupOptions = {"a" : "Start",
                 "b" : "Clean",
                 "c" : "Clear"}


class Menu(object):
    """
    The menu class.
    """

    def __init__(self):
        self.DM = DirectoryManager()
        self.CP = CardPrinter()

        # Create a dictionary relating options to functions:
        self.functions = {}

        for d in [dirOptions, backupOptions]:
            for k, v in d.items():
                self.functions[v] = getattr(self, "opt_" + v.lower())


    def printMenu(self):
        CP = self.CP
        DM = self.DM

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
        CP.footer()
        print("")

        opt = input("Your selection (q to quit) : ")

        while (opt not in dirOptions and opt not in backupOptions and opt != "q"):
            opt = input("Invalid option. Please select again (q to quit) : ")

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



    def optionToFunction(self, opt):
        if opt in dirOptions:
            func = dirOptions[opt]

        elif opt in backupOptions:
            func = backupOptions[opt]

        else:
            func = None

        return func



    def opt_add(self):
        print("Add option selected.")

    def opt_save(self):
        print("Save option selected.")

    def opt_check(self):
        print("Check option selected.")

    def opt_change(self):
        print("Change option selected.")

    def opt_start(self):
        print("Start option selected.")

    def opt_clean(self):
        print("Clean option selected.")

    def opt_clear(self):
        print("Clear option selected.")





if __name__ == "__main__":
    m = Menu()
    m.run()

