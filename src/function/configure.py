"""

This is the config.ini file parser. After importing, the configure values can
be found in the 'config' variable. The module will parse the command line and
make the appropriate changes to 'config'.

"""
import configparser
import os.path
from function.argument import args

# Create parser object:
config = configparser.ConfigParser()
config.optionxform = str # Make the parser case sensitive


# Config file name:
filename = 'config.ini'


# Search for the config file, starting in the current directory and 
# moving up N directories:
N = 2

for n in range(N):
    if os.path.isfile(filename):
        break
    else:
        filename = r"../" + filename


# Parse config file:
config.read(filename)



# Update the config settings with the command line values from arg:
sec = 'general' # Only general values can be changed

for key in config[sec]:
    argsValue = getattr(args, key, None)

    if argsValue:
        config[sec][key] = argsValue



if __name__ == '__main__':
    print("***** Inside configure.py *****\n")
    print("FILE = " + filename)

    for sec in config:
        print("\n[" + sec + "]")

        for key in config[sec]:
            print(key + " = " + config[sec][key])

