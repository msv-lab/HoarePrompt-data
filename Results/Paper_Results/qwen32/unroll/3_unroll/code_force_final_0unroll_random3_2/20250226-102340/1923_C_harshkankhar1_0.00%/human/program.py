from itertools import accumulate
def solve():
    n,q=map(int,input().split())
    a=[0]+[int(x) for x in input().split()]
    b=[0]*(n+1)
    for i in range(1,n+1):
        x = 1 if a[i]>1 else 2
        b[i]=b[i-1] + x
    a=list(accumulate(a))
    print(*a)
    for _ in range(q):
        x,y=map(int,input().split())
        print("NO") if a[y]-a[x-1]<b[y]-b[x-1] or x==y else print("YES") 
   
   
 
for _ in range(int(input())):
    solve()