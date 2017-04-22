"""

Provides the file list element for the terminal ui.

"""

from function.configure import config
from function.save import Directories
from ui.terminal.card import CardPrinter

import os
from textwrap import TextWrapper
import subprocess as subp


class DirectoryView(object):
    """
    Class that provides the directory view element.
    """

    def __init__(self, dirs):
        self.dirs = dirs.dirs
        dirs.readSaveFile()
        self.cardPrinter = CardPrinter()

        # Create validation dictionary:
        self.allValid = False
        self.valid = {}
        for k, v in self.dirs.items():
            self.valid[k] = {}
            self.valid[k]['src'] = None
            self.valid[k]['dest'] = None

        # Save the width since it needs to be altered:
        self.textWidth = int(config['terminal']['width']) - 5


    def checkDirs(self):
        self.allValid = True

        for k, v in self.dirs.items():
            self.valid[k]['src']  = os.path.exists(v['src'])
            self.valid[k]['dest'] = os.path.exists(v['dest'])
            self.allValid = ( self.allValid and 
                              self.valid[k]['src'] and 
                              self.valid[k]['dest'] )
        


    def printView(self):
        # Get color settings:

        # Clear the terminal:
        subp.run(["reset"])

        # Print the directories:
        print("")
        self.cardPrinter.header()
        self.cardPrinter.line()
        self.cardPrinter.lineCentered("Directories")
        self.cardPrinter.separator()
       
        first = True
        for k, v in sorted(self.dirs.items()):
            if not first:
                self.cardPrinter.line()

            self.cardPrinter.line("Name        :: " + k)
            self.cardPrinter.line("Source      :: " + v["src"])
            self.cardPrinter.line("Destination :: " + v["dest"])
            first = False

        self.cardPrinter.footer()
        print("")


    def addDir(self, name, src, dest, opt=""):
        pass


    def removeDir(self, name):
        pass



if __name__ == "__main__":
    dirs = Directories()

    FL = DirectoryView(dirs)
    FL.printView()

    FL.checkDirs()

    FL.addDir('Bad Dir', './test/badSrc', './test/badDest')
    FL.checkDirs()

    FL.removeDir('Bad Dir')
    FL.printView()


