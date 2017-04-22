"""

Provides a class for printing output cards to terminal.

"""

from textwrap import TextWrapper
import color.terminal as terminal
from function.configure import config
import sys
import subprocess as subp


def printFlush(*arg, **kwargs):
    """
    A wrapper for print that flushes the output after every call. Needed when
    changing terminal colors multiple times in a single line. 
    """
    print(*arg, **kwargs)
    sys.stdout.flush()


def clearTerminal():
    subp.run(["reset"])


class CardPrinter(object):
    """
    Class that provides an easy way to print output to cards.
    """

    def __init__(self):
        self.width = int(config['terminal']['width']) - 5

        self.colorConvert = {}
        self.colorConvert['green'] = terminal.green
        self.colorConvert['red']   = terminal.red


    def line(self, line = " ", color = None, indent = " "):
        vert  = config['terminal']['verticalMark']
        width = self.width
        resetColor = terminal.get_color()

        wrapper = TextWrapper(width = width,
                              break_long_words = True,
                              subsequent_indent = indent,
                              drop_whitespace = False)

        allLines = wrapper.wrap(line)

        for line in allLines:
            if len(line) < width:
                line += (width - len(line))*" "

            printFlush(vert, end = "")

            if color:
                terminal.set_color(self.colorConvert[color])
            
            printFlush(" " + line + " ", end = "")

            if color:
                terminal.set_color(resetColor)

            printFlush(vert)


    def lineCentered(self, line):
        self.line(line.center(self.width), indent="")


    def separator(self):
        horiz = config['terminal']['horizontalMark']
        vert  = config['terminal']['verticalMark']

        print(vert + (self.width + 2)*horiz + vert)


    def header(self):
        horiz = config['terminal']['horizontalMark']
        left  = config['terminal']['upperLeftMark']
        right = config['terminal']['upperRightMark']

        print(left + (self.width + 2)*horiz + right)


    def footer(self):
        horiz = config['terminal']['horizontalMark']
        left  = config['terminal']['lowerLeftMark']
        right = config['terminal']['lowerRightMark']

        print(left + (self.width + 2)*horiz + right)



