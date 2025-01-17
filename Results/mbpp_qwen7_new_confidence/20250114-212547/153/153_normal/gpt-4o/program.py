from math import comb, isclose

def count_binary_seq(n):
    def binomial_coeff(n, k):
        if k > n:
            return 0
        return comb(n, k)

    # Initialize an array to store the results of subproblems
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = dp[0][i] = 1

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    result = sum(dp[n][i] * dp[n][i] for i in range(n + 1))
    return result

# Test cases
assert isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
assert isclose(count_binary_seq(2), 6.0, rel_tol=0.001)
assert isclose(count_binary_seq(3), 20.0, rel_tol=0.001)
