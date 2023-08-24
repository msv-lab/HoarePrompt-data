from collections import defaultdict

MOD = 998244353

def count_emotional_orders(n, a):
    # Sort the weights in descending order
    a.sort(reverse=True)
    
    # Initialize a dynamic programming table
    dp = [[0] * (n+1) for _ in range(n+1)]
    dp[0][0] = 1
    
    for i in range(n):
        for j in range(i+1):
            # If the current weight is less than or equal to twice the maximum weight
            if a[i] >= 2 * a[j]:
                # Add the number of emotional orders ending at the current weight
                dp[i+1][j+1] += dp[i][j]
                dp[i+1][j+1] %= MOD
            
            # Add the number of emotional orders without considering the current weight
            dp[i+1][j] += dp[i][j]
            dp[i+1][j] %= MOD
    
    # Sum up the number of emotional orders for each ending weight
    emotional_orders = sum(dp[n])
    
    return emotional_orders % MOD

n = int(input())
a = list(map(int, input().split()))

result = count_emotional_orders(n, a)
print(result)