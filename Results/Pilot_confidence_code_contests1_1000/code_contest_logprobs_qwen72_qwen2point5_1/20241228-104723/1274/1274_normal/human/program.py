from __future__ import print_function,division
import sys#log min est tolérable
le=sys.__stdin__.read().split("\n")[::-1]
af=[]
n=int(le.pop())
def loga(m):
    lo=0
    p=1
    while p<=m:
        p*=2
        lo+=1
    return lo-1
lo=loga(n)
l=list(map(int,le.pop().split()))
for k in range(n):
    if l[k]==-1:
        moi=k

li=loga(moi+1)
s=0
for tour in range(lo,li,-1):
    #print(l[2**tour-1:])
    mi=min(l[2**tour-1:])
    l[2**tour-1+l[2**tour-1:].index(mi)]=10**9
    s+=mi
print(s)
