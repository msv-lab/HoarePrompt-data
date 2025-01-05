def fun(n):
    f=0
    s=0
    p=1
    if n==0:
        return 0
    for i in range(100):
        if i%2:
            s+=min(p,n)
        else:
            f+=min(p,n)
        n-=p
        if n<=0:
            break
        p*=2
    return f*f+s*(s+1)
l,r=[int(i) for i in raw_input().split()]
print  (fun(r)-fun(l-1))%1000000007

