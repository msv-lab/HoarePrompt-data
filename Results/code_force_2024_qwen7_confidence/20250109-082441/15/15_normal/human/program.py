for t in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    hash=[0 for _ in range(n)]
    for a in arr:
        hash[a]+=1
    ans1,ans2=n,n
    c=0
    for a in range(n):
        if hash[a]==0:
            ans1=min(a,ans1)
        elif hash[a]==1:
            if c==1:
                ans2=a
            c+=1


    print(min(ans1,ans2))