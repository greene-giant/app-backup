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
        self.width = int(config['terminal']['width']) - 6
        self.colorUI = terminal.get_color()

        self.colorConvert = {}
        self.colorConvert['black']    = terminal.black
        self.colorConvert['blue']     = terminal.blue
        self.colorConvert['green']    = terminal.green
        self.colorConvert['cyan']     = terminal.cyan
        self.colorConvert['red']      = terminal.red
        self.colorConvert['magenta']  = terminal.magenta
        self.colorConvert['yellow']   = terminal.yellow
        self.colorConvert['grey']     = terminal.grey
        self.colorConvert['none']     = terminal.get_color()


    def setColorUI(self, color):
        self.colorUI = self.colorConvert[color]


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

            terminal.set_color(self.colorUI)
            printFlush(" " + vert, end = "")
            terminal.set_color(resetColor)

            if color:
                terminal.set_color(self.colorConvert[color])
            
            printFlush(" " + line + " ", end = "")

            if color:
                terminal.set_color(resetColor)

            terminal.set_color(self.colorUI)
            printFlush(vert)
            terminal.set_color(resetColor)


    def lineCentered(self, line, color = None):
        self.line(line.center(self.width), color, indent="")


    def separator(self):
        horiz = config['terminal']['horizontalMark']
        vert  = config['terminal']['verticalMark']
        resetColor = terminal.get_color()

        terminal.set_color(self.colorUI)
        print(" " + vert + (self.width + 2)*horiz + vert)
        terminal.set_color(resetColor)


    def header(self):
        horiz = config['terminal']['horizontalMark']
        left  = config['terminal']['upperLeftMark']
        right = config['terminal']['upperRightMark']
        resetColor = terminal.get_color()

        terminal.set_color(self.colorUI)
        print(" " + left + (self.width + 2)*horiz + right)
        terminal.set_color(resetColor)


    def footer(self):
        horiz = config['terminal']['horizontalMark']
        left  = config['terminal']['lowerLeftMark']
        right = config['terminal']['lowerRightMark']
        resetColor = terminal.get_color()

        terminal.set_color(self.colorUI)
        print(" " + left + (self.width + 2)*horiz + right)
        terminal.set_color(resetColor)



