t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    dp = [0 for i in range(n)]
    dp[-1] = min(a[-1],b[-1])
    for i in range(n-2,m-1,-1):
        dp[i] = dp[i + 1] + min(a[i],b[i])
    dp[0] = a[0]
    for i in range(1,m):
        dp[i] = min(a[i],dp[i-1]+b[i])
    if m == n:
        print(dp[m-1])
    else:
        print(dp[m-1]+dp[m])