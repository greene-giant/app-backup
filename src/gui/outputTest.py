
import random
import time, sys


N = random.randrange(2,6,1)

for n in range(N):
    print("File {} of {}".format(n+1, N))
    sys.stdout.flush()
    time.sleep(3)

print(30*"Done ")
sys.stdout.flush()

sys.stderr.write("Error written to stderr\n")
sys.stderr.flush()

