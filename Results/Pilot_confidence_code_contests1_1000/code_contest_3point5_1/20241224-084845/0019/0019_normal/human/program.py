from __future__ import division
from sys import stdin, stdout
import math
n, m = map(int, stdin.readline().rstrip().split())
x=n
s=0
while n%m==0 or n>m:
        if n/m>=1:
           r=n/m
           r=r%1
           s=s+r
        n=math.floor(n/m)
        x=x+n    
x=x+math.ceil(s)
print(int(x)) 