test=int(input())
while test:
    test-=1
    n,x=map(int,input().split())
    p=list(map(int,input().split()))
    p=[0]+p
    st=p.index(x)

    l=1
    r=n+1
    while l+1<r:
        m=(l+r)>>1
        if p[m]<=x:
            l=m
        else:
            r=m
    if l==st:
        print(0)
    else:
        print(1)
        print(str(l)+' '+str(st))