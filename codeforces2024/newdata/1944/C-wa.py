for t in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    hash=[0 for _ in range(n)]
    for a in arr:
        hash[a]+=1
    unique=[]
    for a in range(n):
        if hash[a]>=1:
            unique.append(a)
    ans=0
    for a in range(n):
        if hash[a]==0:
            ans=a
            break
        elif hash[a]==1 and a>0:
            ans=a
            break
        else:
            ans+=1
    print(ans)