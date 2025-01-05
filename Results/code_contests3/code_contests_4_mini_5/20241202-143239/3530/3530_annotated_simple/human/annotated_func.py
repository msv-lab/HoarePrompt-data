#State of the program right berfore the function call: N is an integer between 1 and 21 inclusive, and a is a 2D list of integers where each element is either 0 or 1, representing the compatibility between N men and N women.
def func():
    MOD = 1000000007
    n = input()
    a = []
    for _ in range(n):
        a.append(map(int, raw_input().split()))
        
    #State of the program after the  for loop has been executed: `N` is an integer between 1 and 21 inclusive, `a` is a 2D list containing `n` rows of integers from user input, and `_` is `n - 1` after all iterations.
    dp = [([0] * (1 << n)) for _ in range(n + 1)]
    for i in range(1 << n):
        dp[0][i] = 1
        
    #State of the program after the  for loop has been executed: `N` is an integer between 1 and 21 inclusive; `dp[0][i]` is 1 for all `i` in the range from 0 to `2^N - 1`; `i` is `2^N - 1`.
    for i in range(1, n + 1):
        for mask in range(1, 1 << n):
            for j in range(n):
                if a[i - 1][j] == 1 and mask & 1 << j:
                    dp[i][mask] += dp[i - 1][mask ^ 1 << j]
                    dp[i][mask] %= MOD
        
    #State of the program after the  for loop has been executed: `N` is an integer between 1 and 21 inclusive, `dp` reflects the final results based on all updates made during the loop iterations for all `i` from 1 to `N`, where `mask` spans all values from 1 to \(2^N - 1\), and for each `j` from 0 to `N-1`, `a[i - 1][j]` influences the values in `dp[i][mask]` based on the condition involving `mask & (1 << j)`.
    print(dp[n][(1 << n) - 1])
#Overall this is what the function does:The function reads an integer `N` (1 ≤ N ≤ 21) and a 2D list `a` of compatibility data (0 or 1) representing the compatibility between `N` men and `N` women. It calculates the number of perfect matchings using a dynamic programming approach and prints the result. The function does not return any value, but it prints the number of valid pairings based on the input compatibility matrix. The function assumes valid input from the user for `N` and the compatibility matrix.

