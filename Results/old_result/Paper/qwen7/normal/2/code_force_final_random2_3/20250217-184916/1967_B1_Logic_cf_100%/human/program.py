# LUOGU_RID: 157640359
t=int(input())
for T in range(t):
    [n,m]=input().split()
    [n,m]=[int(n),int(m)]
    ans=n
    for b in range(2,min(n,m)+1):
        ans=ans+(n+b)//(b*b)
    print(ans)