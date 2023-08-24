def count_subsequences(s, t):
    m, n = len(s), len(t)
    
    dp = [[0] * (n+1) for _ in range(m+1)]
    
    for i in range(m+1):
        dp[i][0] = 1
        
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s[i-1] != t[j-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                
    return dp[m][n]

s = input()
t = input()
result = count_subsequences(s, t)
print(result)