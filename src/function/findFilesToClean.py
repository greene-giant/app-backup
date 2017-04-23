"""

A module providing methods related to finding old files in the destination 
directories.

"""
import os

def findFilesToClean(src, dest):
    oldFiles = []

    for fullDirName, subDirList, fileList in os.walk(dest):
        lenDest = len(dest)
        dirName = fullDirName[lenDest:]

        if os.path.exists(src + dirName):
            for f in fileList:
                if os.path.exists(src + dirName + "\\" + f):
                    pass
                else:
                    fileName = fullDirName + '\\' + f
                    oldFiles.append(fileName)

        else:
            if fileList:
                for f in fileList:
                    fileName = fullDirName + '\\' + f
                    oldFiles.append(fileName)
            else:
                oldFiles.append(fullDirName)

    return oldFiles


def findFilesToCleanInRootOnly(src, dest):
    oldFiles = []

    for f in os.listdir(dest):
        if os.path.isfile(dest + "/" + f):
            if not os.path.isfile(src + "/" + f):
                oldFiles.append(dest + "/" + f)

    return oldFiles

