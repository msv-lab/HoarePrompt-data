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
def dout(*args, **kargs):
    if not testing: return
    if args: print(args[0] if len(args)==1 else args)
    if kargs: print([(k,v) for k,v in kargs.items()])
    
# ############ ---- I/O Functions ---- ############

# from math import ceil
# from collections import defaultdict as ddict, Counter
# from heapq import *
# from Queue import Queue

"""
a b c d
ad b c d
ad b c -a
d b c -a
d-a b c -a
d-a b c -a-d+a=-d
-a b c -d
"""

def main():
    n = intin()
    a = intlin()
    ans = []
    for i in xrange(n):
        ans.append("1 %d %d" % (a[i], a[n-i-1]))
        ans.append("2 %d %d" % (a[i], a[n-i-1]))
        ans.append("1 %d %d" % (a[i], a[n-i-1]))
        ans.append("1 %d %d" % (a[i], a[n-i-1]))
        ans.append("2 %d %d" % (a[i], a[n-i-1]))
        ans.append("1 %d %d" % (a[i], a[n-i-1]))
    return str(len(ans))+ '\n' + '\n'.join(ans)


anss = []
for _ in xrange(intin()):
    anss.append(main())
    # anss.append("YES" if main() else "NO")
lout(anss)

if testing:
    sys.stdout = cmd
    print(int(round(time() * 1000))  - start_time)