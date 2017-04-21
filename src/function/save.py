
"""

Module that defines the save format. Also handles the reading and writing of
the save file. 

"""

from function.configure import config
import os.path


class Directories(object):
    """
    Class that manages the directory information.
    """

    def __init__(self):
        self.saveFile = config['general']['saveFile']
        self.saveDirs = {}


    def changeSaveFile(self, saveFile):
        self.saveFile = saveFile


    def addEntry(self, name, source, dest, option=""):
        self.saveDirs[name] = {'source' : source,
                               'dest'   : dest,
                               'opt'    : option}


    def removeEntry(self, name):
        del self.saveDirs[name]


    def writeSaveFile(self):
        f = open(self.saveFile, 'w')

        for k, v in self.saveDirs.items():
            f.write("\n" + k + "\n")
            f.write(v['source'] + "\n")
            f.write(v['dest'] + "\n")
            f.write(v['opt'] + "\n")

        f.close()


    def readSaveFile(self):
        # Check if file exists:
        if os.path.isfile(self.saveFile):
            # Read the file:
            f = open(self.saveFile, 'r')

            for line in f:
                if line.strip():
                    name = line.strip()
                    source = f.readline().strip()
                    dest   = f.readline().strip()
                    opt    = f.readline().strip()

                    self.addEntry(name, source, dest, opt)

            f.close()


    def printEntries(self):
        for k, v in self.saveDirs.items():
            print("\n")
            print("Name        :: " + k)
            print("source      :: " + v['source'])
            print("destination :: " + v['dest'])
            if v['opt']:
                print("options     :: " + v['opt'])



if __name__ == "__main__":
    newSaveFile = r'function/testSaveFormat.save'

    dirs1 = Directories()
    dirs1.addEntry('e1', r'/path/to/source1', r'/path/to/dest1')
    dirs1.addEntry('e2', r'/path/to/source2', r'/path/to/dest2', 'b')
    dirs1.changeSaveFile(newSaveFile)
    dirs1.writeSaveFile()

    dirs2 = Directories()
    dirs2.changeSaveFile(newSaveFile)
    dirs2.readSaveFile()
    dirs2.printEntries()





