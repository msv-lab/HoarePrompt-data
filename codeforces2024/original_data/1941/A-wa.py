t = int(input())
for _ in range(t):
    n,m,k = map(int,input().split())
    left = list(map(int,input().split()))
    right = list(map(int,input().split()))
    ans = 0
    for i in left:
        for j in right:
            if i+j < k:
                ans+=1
    print(ans)