from __future__ import division,print_function
from heapq import*
from random import*
import sys
n=int(input())
def ask(i):
    print("?",i+1)
    sys.__stdout__.flush()
    return list(map(int,raw_input().split()))
se=set(k for k in range(n))
ar=[[] for k in range(n)]
d={}
while se:
    u=min(se)
    d[u] = ask(u)
    for k in range(n):
        if d[u][k]<2:
            if k in se:
                se.remove(k)
            if k!=u:
                ar[u].append(k)
                ar[k].append(u)
def untiersdeuxtiers(k,i):#to apply between point at distance 3 and both asked to know who is on the path between them
    for j in range(n):
        if d[k][j]==1 and d[i][j]==2:
            return j
for k in d:
    for i in d:
        if d[k][i]==3:
            u=untiersdeuxtiers(k,i)
            v=untiersdeuxtiers(i,k)
            ar[u].append(v)
            ar[v].append(u)
for k in range(n):
    ar[k]=list(set(ar[k]))
print('!')
for k in range(n):
    for i in ar[k]:
        if i>k:
            print(k+1,i+1)
