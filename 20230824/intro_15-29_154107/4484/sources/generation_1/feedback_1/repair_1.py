def count_arrangements(N, M):
    mod = 10**9 + 7
    
    # Base cases
    if N == 0 and M == 0:
        return 0
    
    # Calculate the count of arrangements using dynamic programming
    dp = [[0] * (M+1) for _ in range(N+1)]
    dp[0][0] = 1
    
    for i in range(1, N+1):
        dp[i][0] = dp[i-1][0] + dp[i-2][0]
        dp[i][0] %= mod
        
    for j in range(1, M+1):
        dp[0][j] = dp[0][j-1] + dp[0][j-2]
        dp[0][j] %= mod
        
    for i in range(1, N+1):
        for j in range(1, M+1):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + dp[i][j-1] + dp[i-2][j-2] + dp[i][j-2]
            dp[i][j] %= mod
    
    return dp[N][M]


# Read input
N, M = map(int, input().split())

# Calculate and print the count of arrangements
print(count_arrangements(N, M))