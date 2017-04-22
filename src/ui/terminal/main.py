"""

The main class for the terminal UI.

"""

from function.configure import config
from ui.terminal.card import CardPrinter, clearTerminal
from directoryManger import DirectoryManager

class MainTerminal(object):
    """
    The main class for the terminal UI.
    """

    def __init__(self):
        self.DM = DirectoryManager()
        self.cardPrinter = CardPrinter()



    def run(self):
        quit = False

        while (not quit):
            if True:
                quit = True

