"""

Simple script to generate the backup test case.

"""

import shutil
import os

# Delete current dest directories:
shutil.rmtree("./dest1", ignore_errors=True)
shutil.rmtree("./dest2", ignore_errors=True)

# Create dest directories:
os.mkdir("./dest1")
os.mkdir("./dest2")


# Create sample files:
for d in ['./src1', './src2']:
    if not os.path.isdir(d):
        os.mkdir(d)

        for n in range(10):
            f = open(d + "/file" + str(n) + '.txt', 'w')
    
            for l in range(n+1):
                for m in range(2000):
                    f.write(50*str(l) + '\n')
    
            f.close()


