def nc(n,a):
    r=1
    s=1
    p=n
    g=1
    for i in range(a):
        r=r*p
        p-=1
        s=s*g
        g+=1
    return r/s
n=int(raw_input())
x=n*(n-4)*(n-3)*(n-2)*(n-1)*nc(n,5)
print(x)
