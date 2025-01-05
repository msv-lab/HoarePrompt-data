t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    cards=list(map(int,input().split()))
    ans=n
    for i in cards:
        if cards.count(i)>=k:
            ans=k-1
            break
    print(ans)