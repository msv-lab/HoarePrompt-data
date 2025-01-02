from math import *
from Queue import *


m = [0 for i in range(51)]
n = int(raw_input())
results = []
for i in range(n*(n-1)/2-1):
    l = map(int, raw_input().split())
    results.append((l[0], l[1]))
    m[l[0]] += 1
    m[l[1]] += 1
l = []
for i in range(1,n+1):
    if m[i] == n-2:
        l.append(i)
b = True
for i in range(1,n+1):
    if ((l[0],i) in results) and ((i,l[0]) in results):
        print(str(l[0]) + ' ' + str(l[1]))
        b = False
if b:
    print(str(l[1]) + ' ' + str(l[0]))
