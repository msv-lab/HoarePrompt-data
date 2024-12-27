from __future__ import division,print_function
from heapq import*
import sys
from math import*

le = sys.__stdin__.read().split("\n")[::-1]
af = []
for i in range(int(le.pop())):
    d,k=list(map(int,le.pop().split()))
    a=floor(d/(k*2**0.5))
    #print(a,d,k)
    if (a*k)**2+(k*(a+1))**2>d**2:
        af.append('Utkarsh')
    else:
        while (a*k)**2+(k*(a+2))**2>d**2 and a>0:
            a-=1
        if ((a+1)*k)**2+(k*(a+2))**2>d**2:
            #print("couc")
            af.append('Utkarsh')
        else:
            af.append("Ashish")
print("\n".join(map(str,af)))
