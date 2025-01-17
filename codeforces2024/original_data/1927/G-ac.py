import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    # Initialize the dp array with a large number (infinity)
    dp = [10 ** 18] * (n + 1)
    dp[0] = 0  # No charges needed to paint zero cells
    
    for i in range(n):
        # Update dp for the left usage of the charge at i
        for j in range(i - 1, -1, -1):
            dp[j] = min(dp[j], dp[j + 1])
        
        # Consider using the charge at i to the left
        dp[i + 1] = min(dp[i + 1], dp[max(0, i + 1 - a[i])] + 1)
        
        # Temporary variable to track the minimum charges needed
        x = dp[i]
        
        # Consider using the charge at i to the right
        for j in range(i + 1, min(n, i + a[i])):
            x = min(x, dp[min(i, max(0, j - a[j] + 1))] + 1)
            dp[j + 1] = min(dp[j + 1], x + 1)
    
    # Output the minimum number of charges needed for this test case
    print(dp[-1])