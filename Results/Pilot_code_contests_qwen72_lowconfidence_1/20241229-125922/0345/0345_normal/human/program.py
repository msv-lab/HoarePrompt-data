""" 
3
0 3
1 3
3 8
"""

import sys
import bisect
import heapq
import math

sys.setrecursionlimit(10**9+7)

def fi():
    return int(sys.stdin.readline())
def fi2():
    return map(int, sys.stdin.readline().split())
def fi3():
    return sys.stdin.readline().rstrip()
def fo(*args):
    for s in args:
        sys.stdout.write(str(s)+' ')
    sys.stdout.write('\n')
##    sys.stdout.flush()
def puts(*args):
    for s in args:
        sys.stdout.write(str(s))

##
OUT = []
def bfo(*args):
    for s in args:
        OUT.append(str(s)+' ')
    OUT.append('\n')
def bputs(*args):
    for s in args:
        OUT.append(str(s))        
def flush():
    sto = ''.join(OUT)
    fo(sto)
##

alpha = 'abcdefghijklmnopqrstuvwxyz'
nax = 101010
mod = 10**9+7
inf = 10**18+5

##


##
#main

n = fi()
T = []
M = []
for i in range(n):
    a, b = fi2()
    T.append((a, b))
    M.append(a)
    M.append(b)

M.sort()

f = {}
invf = {}

for x in M:
    if x not in f:
        f[x] = len(f)
        invf[len(f)-1] = x

comp = len(f)

F = [0 for i in range(comp+5)]
E = [0 for i in range(comp+5)]

for t in T:
    a, b = t
    a = f[a]
    b = f[b]
    E[b] += 1
    F[a] += 1
    F[b+1] -= 1

for i in range(1, len(F)):
    F[i] = F[i-1]+F[i]

res = [0 for i in range(n+1)]

for i in range(comp):
    k = F[i]
    res[k] += 1

for i in range(comp-1):
    k = F[i] - E[i]
    res[k] += (invf[i+1]-invf[i]-1)

for i in range(1, n+1):
    bputs(res[i],' ')

flush()
