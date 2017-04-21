"""

This is the command line parser for the backup app. After importing, the command
line arguments are in the 'arg' variable.

"""

import argparse

# Create command line parser:
parser = argparse.ArgumentParser(
        description='A backup program for Windows that utilizes the xcopy command.',
        epilog="* Option overwrites value specified in config.ini")


# Add ui:
parser.add_argument("--ui", 
                    dest='ui', 
                    choices=['terminal'],
                    help='Specify the ui to be used*')


# Add save file location:
parser.add_argument('-s', '--save', 
                    dest='saveFile',
                    help='Save file for backup directories list*')


# Parse the command line:
args = parser.parse_args()

if __name__ == "__main__":
    print("ui = " + str(args.ui))
    print("saveFile = " + str(args.saveFile))

