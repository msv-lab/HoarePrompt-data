#coding:utf-8
from math import *
N,H=map(int,raw_input().split())
A=[];B=[]
for i in range(N):
    a,b=map(int,raw_input().split())
    A.append(a);B.append(b)
am=max(A)
B.sort()
B.reverse()
B.append(-1)
h=0
c=0
bi=0
while h<H:
    b=B[bi]
    if b<am:
        c+=int(ceil((H-h)*1.0/am))
        break
    else:
        h+=b
        c+=1
        bi+=1
print(c)
        



