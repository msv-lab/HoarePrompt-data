from math import *
from Queue import *
from sys import *
from random import *





n = int(raw_input())
h = map(int, raw_input().split())
l = [0 for i in range(n)]
r = [0 for i in range(n)]
l[0] = 1
for i in range(1,n):
    l[i] = min(l[i-1]+1, h[i])
r[-1] = 1
for i in range(n-2,-1,-1):
    r[i] = min(r[i+1]+1, h[i])
res = 0
for i in range(n):
    res = max(res, min(l[i],r[i]))
print(res)
