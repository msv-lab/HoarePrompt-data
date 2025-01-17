t=int(input())
for i in range(t):
    n,k,x=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    q=[0]
    p=-10**5
    for i in range(n):
        q.append(q[-1]+a[i])
    for i in range(n-k,n+1):
        if i-x<1:
            l=0
        else:
            l=i-x    
        m=2*q[l]-q[i] 
        if m>p:
            p=m
    print(p)        