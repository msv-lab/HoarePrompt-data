from typing import List

MOD = int(1e9) + 7

def solve(n: int, q: int, l: List[int], r: List[int]) -> int:
    dp = [[0]*(n+1) for _ in range(q+1)]
    dp[0][0] = 1
    cnt = [0]*(n+1)
    
    for i in range(1, q+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i-1][j]
            if j > l[i-1]:
                dp[i][j] -= cnt[j-l[i-1]]
            dp[i][j] += dp[i][j-1]
            dp[i][j] %= MOD
            cnt[j] = (cnt[j-1]+dp[i][j])%MOD
            
    ans = 0
    for j in range(1, n+1):
        if j <= r[-1]:
            ans = (ans+dp[q][j])%MOD
    return ans

# Test cases
print(solve(6, 3, [6, 4, 4], [5, 5, 2])) # Expected output: 30
print(solve(10, 1, [10], [9])) # Expected output: 1814400
print(solve(4, 1, [2], [4])) # Expected output: 8