import math

def solve():
    n,k=list(map(int,input().split()))
    lst=[1]*(k-1)
    for i in range(k+1,n+1):
        lst+=[i]
    
    print(len(lst))
    for l in lst:
       print(l,end=" ")
    print()

t = int(input())
for _ in range(t):
    solve()