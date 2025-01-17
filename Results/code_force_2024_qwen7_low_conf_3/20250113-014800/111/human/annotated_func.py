#State of the program right berfore the function call: n and k are integers such that 1 <= n <= 2500 and 1 <= k <= n, and the sum of all n values over all test cases does not exceed 2500.
def func_1(n, k):
    dp = [([0] * (n + 1)) for _ in range(k + 1)]
    dp[1][1] = 1
    for i in range(2, k + 1):
        for j in range(1, n + 1):
            dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1]) % MOD
        
    #State of the program after the  for loop has been executed: `i` is `k + 1`, `k` is a positive integer, `n` is a positive integer, `dp[i][j]` is the cumulative sum of binomial coefficients modulo `MOD` for all `j` from 1 to `n` for all valid `i` where `1 <= i <= k`.
    result = sum(dp[i][n] for i in range(1, k + 1)) % MOD
    return result
    #The program returns result which is the sum of dp[i][n] for all i from 1 to k modulo MOD
#Overall this is what the function does:The function `func_1` accepts two parameters: `n` and `k`, both of which are integers such that \(1 \leq n \leq 2500\) and \(1 \leq k \leq n\). It constructs a dynamic programming table `dp` where `dp[i][j]` represents the sum of binomial coefficients \(\binom{j}{r}\) for all \(r\) from 0 to \(j\), modulo `MOD`. After populating the `dp` table, the function computes the sum of `dp[i][n]` for all `i` from 1 to `k`, and returns this sum modulo `MOD`.

