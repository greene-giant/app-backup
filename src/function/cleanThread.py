"""

A threaded class to clean old files.

"""

import threading as thd
import os, time

from function.configure import config
from function.findFilesToClean import findFilesToClean



class CleanThread(thd.Thread):
    def __init__(self, output, dirs):
        thd.Thread.__init__(self)
        self.output = output
        self.dirs = dirs


    def run(self):
        out = self.output

        colorUI    = config['terminal']['colorCleanUI']
        colorClean = config['terminal']['colorCleanFile']

        out.setColorUI(colorUI)

        print("\n\n")
        out.header()
        out.line()
        out.lineCentered("Starting Clean", colorUI)
        out.line()
        out.footer()
        print("")

        for k, v in sorted(self.dirs.items()):
            if k[-1] == "*":
                # Clean root directory:
                filesToClean = []
                for f in os.listdir(v['dest']):
                    if os.path.isfile(v['dest'] + "/" + f):
                        if not os.path.isfile(v['src'] + "/" + f):
                            filesToClean.append(v['dest'] + "/" + f)

                self.cleanSingleDirectory(k[:-1] + " (just files)",
                                          v['src'],
                                          v['dest'],
                                          filesToClean,
                                          colorUI,
                                          colorClean)

                # Clean subdirectories:
                for d in os.listdir(v['src']):
                    if os.path.isdir(v['src'] + "/" + d):
                        filesToClean = findFilesToClean(v['src'] + "/" + d,
                                                        v['dest'] + "/" + d)

                        self.cleanSingleDirectory(k[:-1] + " (" + d + ")", 
                                                  v['src'] + "/" + d,
                                                  v['dest'] + "/" + d,
                                                  filesToClean, 
                                                  colorUI, 
                                                  colorClean)
            else:
                filesToClean = findFilesToClean(v['src'], v['dest'])

                self.cleanSingleDirectory(k, 
                                          v['src'], 
                                          v['dest'],
                                          filesToClean,
                                          colorUI,
                                          colorClean)


        print("")
        out.header()
        out.line()
        out.lineCentered("Clean Complete", colorUI)
        out.line()
        out.footer()
        print("")

        out.setColorUI(config['terminal']['colorMenuUI'])





    def cleanSingleDirectory(self, name, src, dest, filesToClean, colorUI, colorClean):
        out = self.output

        print("")
        time.sleep(int(config['general']['backupPause']))

        # Print header:
        out.header()
        out.lineCentered(name, colorUI)
        out.line()

        # Print src and dest:
        out.line("Source      :: " + src, colorUI)
        out.line("Destination :: " + dest, colorUI)
        out.line()
        out.separator()
        out.line()


        # Do clean:
        numFiles = 0

        for f in filesToClean:
            if f[0] != 'C' and f[0] != 'c':
                if os.path.isdir(f):
                    os.removedirs(f)

                elif os.path.isfile(f):
                    os.remove(f)

                f = f[len(dest)+1:]
                f = f.replace("\\", "/")

                out.line(f, colorClean)
                numFiles += 1

        out.line("{} File(s) removed".format(numFiles))

        # Print footer:
        out.line()
        out.footer()
        print("")



