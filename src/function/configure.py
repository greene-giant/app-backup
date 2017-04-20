
import configparser
import os.path


# Create parser object:
config = configparser.ConfigParser()


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





if __name__ == '__main__':
    print("FILE = " + filename)

    for sec in config:
        print("\n[" + sec + "]")

        for key in config[sec]:
            print(key + " = " + config[sec][key])

