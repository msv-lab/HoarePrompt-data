from __future__ import division,print_function
from heapq import*
import sys
le = sys.__stdin__.read().split("\n")[::-1]
af=[]
for zorg in range(int(le.pop())):
    n=int(le.pop())
    l= sorted(list(map(int,le.pop().split())))
    s=sum(k==l[n//2] for k in l)
    af.append(max(n%2,s-(n-s)))
print("\n".join(map(str,af)))
