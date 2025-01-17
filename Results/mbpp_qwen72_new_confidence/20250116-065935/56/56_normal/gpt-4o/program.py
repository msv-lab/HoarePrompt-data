def eulerian_num(n, m):
    # Create a 2D table to store results of subproblems
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Base cases
    for i in range(n + 1):
        dp[i][0] = 1  # a(n, 0) = 1 for all n
    
    # Fill the table using the recurrence relation
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = (i - j) * dp[i - 1][j - 1] + (j + 1) * dp[i - 1][j]
    
    return dp[n][m]

# Test cases
assert eulerian_num(3, 1) == 4
assert eulerian_num(4, 1) == 11
assert eulerian_num(5, 3) == 26
