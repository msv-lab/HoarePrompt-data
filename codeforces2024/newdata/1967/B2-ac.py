# LUOGU_RID: 157647140
import sys
sys.setrecursionlimit(2000000)
from math import sqrt

def gcd(x,y):
    if x!=0:
        return gcd(y%x,x)
    return y

t=int(input())
for T in range(t):
    [n,m]=input().split()
    [n,m]=[int(n),int(m)]
    ans=0
    for i in range(1,int(sqrt(n))+1):
        for j in range(1,int(sqrt(m))+1):
            if gcd(i,j)==1:
                ans=ans+(min(n//i,m//j)//(i+j))
    print(ans)
