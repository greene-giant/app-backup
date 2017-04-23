"""

A threaded backup class. 

"""

import threading as thd
import subprocess as subp
import time

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
        colorClean = config['terminal']['colorCleanFile']

        out.setColorUI(colorUI)


        print("\n\n")
        out.header()
        out.line()
        out.lineCentered("Starting Backup", colorUI)
        out.line()
        out.footer()
        print("")

        for k, v in sorted(self.dirs.items()):
            print("")
            time.sleep(int(config['general']['backupPause']))

            # Print header:
            out.header()
            out.lineCentered(k, colorUI)
            out.line()

            # Print src and dest:
            out.line("Source      :: " + v['src'], colorUI)
            out.line("Destination :: " + v['dest'], colorUI)
            out.line()
            out.separator()
            out.line()


            # Create command:
            cp = 'xcopy '
            flags = r' /s /D /y'
            cmd  = ['xcopy']
            cmd += [r'"' + v['src'] + r'"']
            cmd += [r'"' + v['dest'] + r'"']
            cmd += [r'/s', r'/D', r'/y']
            cmd = cp + r'"' + v['src'] + r'" "' + v['dest'] + r'" ' + flags

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
                    out.line(line.rstrip(), colorCopy)

            # Get old files:
            filesToClean = findFilesToClean(v['src'], v['dest'])
            out.line()
            for f in filesToClean:
                out.line(f, colorClean)

            out.line("{} Old file(s)".format(len(filesToClean)))


            # Print footer:
            out.line()
            out.footer()
            print("")

        print("")
        out.header()
        out.line()
        out.lineCentered("Backup Complete", colorUI)
        out.line()
        out.footer()
        print("")

        out.setColorUI(config['terminal']['colorMenuUI'])
            

