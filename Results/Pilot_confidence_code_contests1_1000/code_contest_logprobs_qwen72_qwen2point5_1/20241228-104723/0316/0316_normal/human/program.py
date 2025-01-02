import sys
testing = len(sys.argv) == 4 and sys.argv[3] == "myTest"
if testing:
    cmd = sys.stdout
    from time import time
    start_time = int(round(time() * 1000)) 
    readAll = open(sys.argv[1], 'r').read
    sys.stdout = open(sys.argv[2], 'w')
else:
    readAll = sys.stdin.read

# ############ ---- I/O Functions ---- ############

class InputData:
    def __init__(self):
        self.lines = readAll().split('\n')
        self.n = len(self.lines)
        self.ii = -1
    def input(self):
        self.ii += 1
        assert self.ii < self.n
        return self.lines[self.ii]
inputData = InputData()
input = inputData.input

def intin():
    return(int(input()))
def intlin():
    return(list(map(int,input().split())))
def chrin():
    return(list(input()))
def strin():
    return input()
def lout(l, sep="\n"):
    print(sep.join(l))
    
# ############ ---- I/O Functions ---- ############

# from math import ceil
# from collections import defaultdict as ddict, Counter
# from heapq import *
# from Queue import Queue

def main():
    n,k = intlin()
    h = intlin()
    if n == 1:
        print(-1)
        return
    while k > 0:
        i = 1
        while i < n:
            if h[i-1] >= h[i]:
                i += 1
            else:
                h[i-1] += 1
                k -= 1
                break
        if i == n:
            print(-1)
            return
    print(i)



for _ in xrange(intin()):
    main()
    # print("YES" if main() else "NO")
# main()

if testing:
    sys.stdout = cmd
    print(int(round(time() * 1000))  - start_time)