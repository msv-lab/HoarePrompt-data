MOD = 998244353

def count_balanced_striped_trees(n):
    if n == 1:
        return 1
    if n == 2:
        return 0
    
    # Initialize DP arrays
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1  # Only one tree with one node
    dp[2] = 0  # No valid tree with two nodes due to striped condition
    
    # Precompute powers of two up to n for efficiency
    power_of_two = [1] * (n + 1)
    for i in range(1, n + 1):
        power_of_two[i] = (power_of_two[i - 1] * 2) % MOD
    
    # Fill dp array
    for i in range(3, n + 1):
        # Calculate number of balanced striped trees with i nodes
        half = (i - 1) // 2
        if (i - 1) % 2 == 0:
            dp[i] = (dp[half] * dp[half] * 2) % MOD
        else:
            dp[i] = (dp[half] * dp[half + 1] * 2) % MOD
    
    return dp[n]

# Read input
import sys
input = sys.stdin.read
n = int(input().strip())

# Output the result
print(count_balanced_striped_trees(n))
