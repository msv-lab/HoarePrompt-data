MOD = 998244353

def count_binary_strings(n, k):
    # Initialize dp array
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    
    # Base case: For k = 1, there is only one good substring "1"
    dp[1][1] = 1
    
    # Fill the dp array
    for i in range(2, k + 1):
        for j in range(1, n + 1):
            # Transition: Adding a '0' or '1' to the previous state
            dp[i][j] = (dp[i-1][j] + dp[i-1][j-1]) % MOD
    
    # Sum up all possible counts for n good substrings
    result = sum(dp[i][n] for i in range(1, k + 1)) % MOD
    return result

# Input reading
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(count_binary_strings(n, k))