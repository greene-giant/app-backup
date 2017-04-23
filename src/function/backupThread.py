"""

A threaded backup class. 

"""

import threading as thd
import subprocess as subp
import time, os

from function.configure import config
from function.findFilesToClean import findFilesToClean

class BackupThread(thd.Thread):
    def __init__(self, output, dirs):
        thd.Thread.__init__(self)
        self.output = output
        self.dirs = dirs

    def run(self):
        out = self.output

        colorUI    = config['terminal']['colorCopyUI']
        colorCopy  = config['terminal']['colorCopyFile']
        colorClean = config['terminal']['colorNeedCleanFile']

        out.setColorUI(colorUI)


        print("\n\n")
        out.header()
        out.line()
        out.lineCentered("Starting Backup", colorUI)
        out.line()
        out.footer()
        print("")

        for k, v in sorted(self.dirs.items()):
            if k[-1] == "*":
                # Copy files in root:
                self.copySingleDirectory(k[:-1] + " (just files)",
                                         v['src'],
                                         v['dest'],
                                         colorUI, 
                                         colorCopy,
                                         colorClean,
                                         includeSubDir = False)

                # Copy subdirectories:
                for d in os.listdir(v['src']):
                    if os.path.isdir(v['src'] + "/" + d):
                        self.copySingleDirectory(k[:-1] + " (" + d + ")",
                                                 v['src'] + "/" + d,
                                                 v['dest'] + "/" + d,
                                                 colorUI, 
                                                 colorCopy, 
                                                 colorClean)
                                                 
            else:
                self.copySingleDirectory(k, 
                                         v['src'], 
                                         v['dest'], 
                                         colorUI, 
                                         colorCopy, 
                                         colorClean)

        print("")
        out.header()
        out.line()
        out.lineCentered("Backup Complete", colorUI)
        out.line()
        out.footer()
        print("")

        out.setColorUI(config['terminal']['colorMenuUI'])




    def copySingleDirectory(self, name, src, dest, colorUI, colorCopy, colorClean, includeSubDir = True):
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


        # Create command:
        cp = 'xcopy '
        if includeSubDir:
            flags = r' /s'
        else:
            flags = ''
        flags += r' /D /y /v'
        cmd = cp + r'"' + src + r'" "' + dest + r'" ' + flags

        # Run backup:
        proc = subp.Popen(cmd,
                          shell = True,
                          bufsize = 0,
                          stdout = subp.PIPE,
                          stderr = subp.STDOUT)

        while True:
            line = proc.stdout.readline().decode("utf-8")
            if line == "" and proc.poll() != None:
                break
            elif line != "":
                if line[0:len(src)] == src:
                    line = line[len(src)+1:]

                line = line.replace("\\", "/")
                out.line(line.rstrip(), colorCopy)


        # Get old files:
        filesToClean = findFilesToClean(src, dest)
        rootFiles = 0
        out.line()
        for f in filesToClean:
            if f[0:len(dest)] == dest:
                f = f[len(dest)+1:]

            f = f.replace("\\", "/")

            if includeSubDir:
                out.line(f, colorClean)
            elif "/" not in f:
                out.line(f, colorClean)
                rootFiles += 1
                

        if includeSubDir:
            numCleanFiles = len(filesToClean)
        else:
            numCleanFiles = rootFiles

        out.line("{} Old file(s)".format(numCleanFiles))


        # Print footer:
        out.line()
        out.footer()
        print("")

            

