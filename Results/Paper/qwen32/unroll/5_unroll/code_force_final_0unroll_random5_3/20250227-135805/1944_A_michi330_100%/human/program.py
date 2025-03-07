t=int(input())
import math
for i in range(0,t,1):
    n,k=map(int,input().split())
    if k>=n-1:
        print(1)
    else:
        print(n)