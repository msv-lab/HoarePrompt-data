MOD = 998244353

def count_bsts(n, C, vertices):
    # Initialize dp array
    dp = [[0] * (C + 1) for _ in range(n + 1)]
    for i in range(1, C + 1):
        dp[1][i] = 1
    
    for i in range(2, n + 1):
        for val in range(1, C + 1):
            L, R, _ = vertices[i]
            for lval in range(1, val):
                if L != -1:
                    dp[i][val] += dp[L][lval]
            for rval in range(val, C + 1):
                if R != -1:
                    dp[i][val] += dp[R][rval]
            dp[i][val] %= MOD
    
    return sum(dp[n]) % MOD

# Input reading
t = int(input())
for _ in range(t):
    n, C = map(int, input().split())
    vertices = [None] * (n + 1)
    for i in range(1, n + 1):
        L, R, val = map(int, input().split())
        vertices[i] = (L, R, val)
    print(count_bsts(n, C, vertices))