"""

Provides the file list element for the terminal ui.

"""

from function.configure import config
from function.save import Directories


class FileList(object):
    """
    Class that provides the file list element.
    """

    def __init__(self, entries):
        self.entries = entries
        self.valid = {}


    def checkEntries(self):
        pass


    def printEntries(self):
        pass


    def addEntry(self, name, src, dest, opt=""):
        pass


    def removeEntry(self, name):
        pass



if __name__ == "__main__":
    testSave = "testSave.save"
    entries = Directories()
    entries.addEntry()
    entries.addEntry()
    entries.addEntry()

    FL = FileList(entries)
    FL.printEntries()
    FL.checkEntries()
    FL.printEntries()

    FL.addEntry()
    FL.printEntries()
    FL.checkEntries()
    FL.printEntries()

    FL.removeEntry()
    FL.print()


