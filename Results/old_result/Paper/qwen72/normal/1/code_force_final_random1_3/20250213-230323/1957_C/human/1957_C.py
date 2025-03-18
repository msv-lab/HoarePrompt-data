import sys
 
sys.setrecursionlimit(400000)
 
dp = [-1 for _ in range(300007)]
 
def go(n):
    # if n <= 1:
    #     return 1
 
    # if dp[n] != -1:
    #     return dp[n]
 
    # dp[n] = (go(n - 1) + 2 * (n - 1) * go(n - 2)) % 1000000007
 
    # return dp[n]
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + 2 * (i - 1) * dp[i - 2]) % 1000000007
 
go(300000)
t = int(input())
 
for _ in range(t):
    n, k = map(int, input().split())
    invalid = set([])
 
    for _ in range(k):
        r, c = map(int, input().split())
        invalid.add(r)
        invalid.add(c)
 
 
    print(max(1, dp[n - len(invalid)]))