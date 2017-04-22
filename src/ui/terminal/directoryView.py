"""

Provides the file list element for the terminal ui.

"""

from function.configure import config
from function.save import Directories
from textwrap import TextWrapper


class DirectoryView(object):
    """
    Class that provides the directory view element.
    """

    def __init__(self, dirs):
        self.dirs = dirs.dirs
        dirs.readSaveFile()

        # Create validation dictionary:
        self.valid = {}
        for k, v in self.dirs.items():
            self.valid[k] = None

        # Save the width since it needs to be altered:
        self.textWidth = int(config['terminal']['width']) - 5


    def checkDirs(self):
        pass


    def printLine(self, line = " "):
        vert  = config['terminal']['verticalMark']
        width = self.textWidth

        wrapper = TextWrapper(width = width,
                              break_long_words = True,
                              subsequent_indent = " ",
                              drop_whitespace = False)

        allLines = wrapper.wrap(line)

        for line in allLines:
            if len(line) < width:
                line += (width - len(line))*" "

            print(vert + " " + line + " " + vert)


    def printLineCenter(self, line):
        self.printLine(line.center(self.textWidth))


    def printSeparator(self):
        horiz = config['terminal']['horizontalMark']
        vert  = config['terminal']['verticalMark']

        print(vert + (self.textWidth + 2)*horiz + vert)


    def printHeader(self):
        horiz = config['terminal']['horizontalMark']
        left  = config['terminal']['upperLeftMark']
        right = config['terminal']['upperRightMark']

        print(left + (self.textWidth + 2)*horiz + right)


    def printFooter(self):
        horiz = config['terminal']['horizontalMark']
        left  = config['terminal']['lowerLeftMark']
        right = config['terminal']['lowerRightMark']

        print(left + (self.textWidth + 2)*horiz + right)
        


    def printView(self):
        vert  = config['terminal']['verticalMark']
        horiz = config['terminal']['horizontalMark']
        width = int(config['terminal']['width'])

        wrapper = TextWrapper(initial_indent = vert + " ",
                              subsequent_indent = vert + " ",
                              width = width,
                              drop_whitespace = False,
                              break_long_words = True)

        print("")
        self.printHeader()
        self.printLine()
        self.printLineCenter("Directories")
        self.printSeparator()
       
        first = True
        for k, v in sorted(self.dirs.items()):
            if not first:
                self.printLine()

            self.printLine("Name        :: " + k)
            self.printLine("Source      :: " + v["src"])
            self.printLine("Destination :: " + v["dest"])
            first = False

        self.printFooter()
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


