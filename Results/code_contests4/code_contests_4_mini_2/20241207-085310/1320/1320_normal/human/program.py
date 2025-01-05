'''input
8
3 3 4
10 20 30
5 5 5
2 4 3
1 1000000000 1000000000
1 1000000000 999999999
3 2 5
3 2 6
'''

import sys
debug = 1
readln = sys.stdin.readline

def write(s):
    sys.stdout.write(str(s))

def writeln(s):
    sys.stdout.write(str(s))
    sys.stdout.write('\n')

def readint():
    return int(readln())

def readints():
    return map(int, readln().split())

def readstr():
    return readln()

def readstrs():
    return readln().split()

def dprint(*args):
    if debug: print(' '.join(map(str, args)))

def solve(X):
    minX = min(X)
    maxX = max(X)
    return max(0, (maxX - minX - 2) * 2)

t = readint()
for _ in xrange(t):
    X = readints()
    writeln(solve(X))