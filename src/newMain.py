
import function.configure as config

print("FILE = " + config.filename)

for sec in config.config:
    print("\n[" + sec + "]")

    for key in config.config[sec]:
        print(key + " = " + config.config[sec][key])

