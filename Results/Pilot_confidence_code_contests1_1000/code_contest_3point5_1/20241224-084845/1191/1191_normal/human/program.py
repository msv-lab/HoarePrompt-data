import sys,math
from fractions import gcd
from bisect import bisect_left, bisect
from collections import defaultdict
from io import BytesIO
sys.stdin = BytesIO(sys.stdin.read())
input = lambda: sys.stdin.readline().rstrip('\r\n')
#n = int(input())
#s = input()
n,k,x = [int(_) for _ in input().split()]

arr = [int(_) for _ in input().split()]
if k > 1:
    rpr = {(x,1):0,(x-1,0):arr[0]}
else:
    rpr = {(x-1,0):arr[0]}
i = 1
while i < n and len(rpr):
    #print(i,rpr)
    pr = defaultdict(int)
    for ost,lag in rpr:
        if lag + 1 == k:
            if ost > 0:
                pr[(ost-1,0)] = max(pr[(ost-1,0)],rpr[(ost,lag)] + arr[i])
            else:
                continue
        else:
            pr[(ost,lag+1)] = max(pr[(ost,lag+1)], rpr[(ost,lag)])
            if ost > 0:
                pr[(ost-1,0)] = max(pr[(ost-1,0)],rpr[(ost,lag)] + arr[i])
    rpr = dict()
    for ke in pr:
        rpr[ke] = pr[ke]
    i += 1
if len(rpr):
    m = 0
    for k in rpr:
        m = max(m,rpr[k])
    print(m)
else:
    print(-1)