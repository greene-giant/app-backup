
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




if __name__ == "__main__":
    arg = parser.parse_args()
    print("ui = " + str(arg.ui))
    print("saveFile = " + str(arg.saveFile))

