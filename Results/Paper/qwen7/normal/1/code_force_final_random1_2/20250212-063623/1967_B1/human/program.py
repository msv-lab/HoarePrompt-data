t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    count=2
    ans=n
    while count<=m:
        countmins=int(count -1)
        g=int(n/count)
        if g<countmins: break
        g-=countmins
        ans+=(int(g/count)+1)
        count+=1
    print(int(ans))