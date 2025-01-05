from __future__ import print_function,division

import sys

le=sys.__stdin__.read().split("\n")[::-1]
def f():
    n,m=list(map(int,le.pop().split()))
    a=list(map(int,le.pop().split()))
    if m<n or n==2:
        af.append(-1)
        return None

    af.append(2*sum(a))
    for k in range(n):
        af.append(str(k+1)+" "+str(((k+1)%n)+1))
af=[]
for zor in range(int(le.pop())):
    f()
print("\n".join(map(str,af)))
