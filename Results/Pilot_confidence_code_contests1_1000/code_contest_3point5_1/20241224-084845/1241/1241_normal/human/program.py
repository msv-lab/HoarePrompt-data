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

flush = sys.stdout.flush
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
def lout(l, sep="\n", toStr=True):
    print(sep.join(map(str, l) if toStr else l))
    
# ############ ---- I/O Functions ---- ############

# from math import ceil
# from collections import defaultdict as ddict, Counter
# from heapq import *
# from Queue import Queue

def main():
    n = intin()
    a = intlin()
    if n == 1:
        return [1]
    if n == 2:
        if a[0] == a[1]:
            return [1,2]
        elif a[0] < a[1]:
            return [2]
        else:
            return [1]

    a = [(i,x) for i,x in enumerate(a)]
    a.sort(key=lambda x:(x[1], x[0]))
    pfs = [0]*(n+1)
    for i in xrange(n):
        pfs[i+1] = pfs[i] + a[i][1]
    i = n-1
    while i > 0:
        if pfs[i] < a[i][1]:
            break
        i -= 1
    ans = [a[j][0]+1 for j in xrange(i, n)]
    ans.sort()
    # print([x[1] for x in a])
    # print(pfs[1:])
    return ans




ans = []
for _ in xrange(intin()):
    tmp = main()
    ans.append(str(len(tmp)))
    ans.append(' '.join(map(str, tmp)))
lout(ans, toStr=False)

# main()

if testing:
    sys.stdout = cmd
    print(int(round(time() * 1000))  - start_time)