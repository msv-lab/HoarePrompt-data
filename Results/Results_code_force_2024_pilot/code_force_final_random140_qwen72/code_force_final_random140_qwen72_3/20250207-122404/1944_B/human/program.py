t=int(input())
for q in range(t):
    n,k=list(map(int,input().split(' ')))
    a=list(map(int,input().split(' ')))
    b=a[:n]
    c=a[n:]
    b.sort()
    c.sort()
    ans1=[]
    ans2=[]
    k=2*k
    req=k
    l=[]
    for i in range(1,n):
        if(k==0):
            break
        if(b[i]==b[i-1]):
            ans1.append(b[i])
            ans1.append(b[i])
            k-=2
        else:
            if(b[i-1] not in ans1):
                l.append(b[i-1])
    if(b[n-1] not in ans1):
        l.append(b[n-1])
    k=req
    for i in range(1,n):
        if(k==0):
            break
        if(c[i]==c[i-1]):
            ans2.append(c[i])
            ans2.append(c[i]) 
            k-=2  
    for i in range(len(l)):
        if(k==0):
            break
        ans1.append(l[i])
        ans2.append(l[i])
    print(*ans1)
    print(*ans2)