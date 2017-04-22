"""

Provides the file list element for the terminal ui.

"""

from function.configure import config
from function.save import Directories
from ui.terminal.card import CardPrinter, clearTerminal

import os
from textwrap import TextWrapper
import subprocess as subp


class DirectoryView(object):
    """
    Class that provides the directory view element.
    """

    def __init__(self, dirs):
        self.dirs = dirs
        self.dirs.readSaveFile()
        self.cardPrinter = CardPrinter()

        # Create validation dictionary:
        self.ranCheckDirs = False
        self.allValid = False
        self.valid = {}
        for k, v in self.dirs.dirs.items():
            self.valid[k] = {}
            self.valid[k]['src'] = False
            self.valid[k]['dest'] = False

        # Save the width since it needs to be altered:
        self.textWidth = int(config['terminal']['width']) - 5


    def checkDirs(self):
        self.allValid = True

        for k, v in self.dirs.dirs.items():
            self.valid[k]['src']  = os.path.exists(v['src'])
            self.valid[k]['dest'] = os.path.exists(v['dest'])
            self.allValid = ( self.allValid and 
                              self.valid[k]['src'] and 
                              self.valid[k]['dest'] )

        self.ranCheckDirs = True
        

    def printView(self):
        # Clear the terminal:
        clearTerminal()

        # Print header:
        print("")
        self.cardPrinter.header()
        self.cardPrinter.line()
        self.cardPrinter.lineCentered("Directories")
        self.cardPrinter.separator()

        # Print directories:
        self.printDirectories()

        # Print footer:
        self.cardPrinter.footer()
        print("")

    def printDirectories(self):
        # Get color settings:
        validColor   = config['terminal']['validDirectoryColor']
        invalidColor = config['terminal']['invalidDirectoryColor']

        # Print the directories:       
        first = True
        for k, v in sorted(self.dirs.dirs.items()):
            if not first:
                self.cardPrinter.line()

            nameColor = None
            srcColor  = None
            destColor = None

            if self.ranCheckDirs:
                nameColor = validColor
                srcColor  = validColor
                destColor = validColor

                if not self.valid[k]['src']:
                    srcColor  = invalidColor
                    nameColor = invalidColor

                if not self.valid[k]['dest']:
                    destColor = invalidColor
                    nameColor = invalidColor

            self.cardPrinter.line(k, nameColor)
            self.cardPrinter.line("Source      :: " + v["src"],  srcColor)
            self.cardPrinter.line("Destination :: " + v["dest"], destColor)
            first = False


    def addDir(self, name, src, dest, opt=""):
        self.dirs.addEntry(name, src, dest, opt)
        self.valid[name] = {}
        self.ranCheckDirs = False


    def removeDir(self, name):
        self.dirs.removeEntry(name)
        del self.valid[name]



if __name__ == "__main__":
    dirs = Directories()

    FL = DirectoryView(dirs)
    FL.printView()
    s = input('Initial print. Press enter to continue...')

    FL.checkDirs()
    FL.printView()
    s = input('Checked directories. Press enter to continue...')

    FL.addDir('Bad Directory', './test/badSrc', './test/badDest')
    FL.printView()
    s = input('Added bad directories. Press enter to continue...')

    FL.checkDirs()
    FL.printView()
    s = input('Checked directories. Press enter to continue...')

    FL.removeDir('Bad Directory')
    FL.printView()
    s = input('Removed bad directory. Press enter to continue...')


