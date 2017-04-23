"""

Simple script to generate the backup test case.

"""

import shutil
import os

# Delete current dest directories:
shutil.rmtree("./test/dest1", ignore_errors=True)
shutil.rmtree("./test/dest2", ignore_errors=True)
shutil.rmtree("./test/dest3", ignore_errors=True)
shutil.rmtree("./test/src3", ignore_errors=True)

# Create dest directories:
os.mkdir("./test/dest1")
os.mkdir("./test/dest2")
os.mkdir("./test/dest3")


# Create sample files:
for d in ['./test/src1', './test/src2']:
    if not os.path.isdir(d):
        os.mkdir(d)

        for n in range(10):
            f = open(d + "/file" + str(n) + '.txt', 'w')
    
            for l in range(n+1):
                for m in range(2000):
                    f.write(50*str(l) + '\n')
    
            f.close()


# Create subdirectories in src3:
os.mkdir('./test/src3')
os.mkdir('./test/src3/srcA')
os.mkdir('./test/src3/srcB')
os.mkdir('./test/src3/srcB/srcC')

os.mkdir('./test/dest3/srcA')
os.mkdir('./test/dest3/srcB')
os.mkdir('./test/dest3/srcB/srcC')

f = open('./test/src3/file3.txt', 'w')
f.write('aaa')
f.close()

f = open('./test/src3/srcA/file3A.txt', 'w')
f.write('aaa')
f.close()

f = open('./test/src3/srcB/file3B.txt', 'w')
f.write('aaa')
f.close()

f = open('./test/src3/srcB/srcC/file3BC.txt', 'w')
f.write('aaa')
f.close()


# Create old files:
d = "./test/dest2"
for n in range(20):
    f = open(d + "/oldFile" + str(n) + ".txt", 'w')

    for l in range(n+1):
        f.write(str(l))

    f.close()

f = open('./test/dest3/file3bad.txt', 'w')
f.write('aaa')
f.close()

f = open('./test/dest3/srcB/srcC/fileBad.txt', 'w')
f.write('aaa')
f.close()


