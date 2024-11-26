from __future__ import division,print_function
from heapq import*
import sys
le = sys.__stdin__.read().split("\n")[::-1]
af=[]
for zorg in range(int(le.pop())):
    n=int(le.pop())
    l= le.pop()
    l=[k for k in range(n) if l[k]=="*"]
    l=[b-a for a,b in enumerate(l)]
    if l:
        med=l[len(l)//2]
        af.append(sum(abs(k-med) for k in l))
    else:
        af.append(0)
print("\n".join(map(str,af)))
