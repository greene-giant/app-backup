"""

Provides a class for printing output cards to terminal.

"""

from textwrap import TextWrapper
import color.terminal as color
from function.configure import config


class CardPrinter(object):
    """
    Class that provides an easy way to print output to cards.
    """

    def __init__(self):
        self.width = int(config['terminal']['width']) - 5


    def line(self, line = " "):
        vert  = config['terminal']['verticalMark']
        width = self.width

        wrapper = TextWrapper(width = width,
                              break_long_words = True,
                              subsequent_indent = " ",
                              drop_whitespace = False)

        allLines = wrapper.wrap(line)

        for line in allLines:
            if len(line) < width:
                line += (width - len(line))*" "

            print(vert + " " + line + " " + vert)


    def lineCentered(self, line):
        self.line(line.center(self.width))


    def separator(self):
        horiz = config['terminal']['horizontalMark']
        vert  = config['terminal']['verticalMark']

        reset = color.get_color()
        color.set_color(color.red)
        print(vert + (self.width + 2)*horiz + vert)
        color.set_color(reset)


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



