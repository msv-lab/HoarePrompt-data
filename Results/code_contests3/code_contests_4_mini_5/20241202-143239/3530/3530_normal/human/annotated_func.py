#State of the program right berfore the function call: N is an integer between 1 and 21 inclusive, and a is a 2D list of integers with dimensions N x N, where each element is either 0 or 1, representing the compatibility between Men and Women.
def func():
    MOD = 1000000007
    n = input()
    a = []
    for _ in range(n):
        a.append(map(int, raw_input().split()))
        
    #State of the program after the  for loop has been executed: `N` is an integer between 1 and 21 inclusive; `a` is a 2D list containing exactly `n` rows of integers from the input; `MOD` is 1000000007; `n` is a string that can be converted to an integer greater than 0.
    dp = [([0] * (1 << n)) for _ in range(n + 1)]
    for i in range(1 << n):
        dp[0][i] = 1
        
    #State of the program after the  for loop has been executed: `N` is an integer between 1 and 21 inclusive, `n` is a string convertible to an integer greater than 0, for all `i` in the range from 0 to (1 << n) - 1, `dp[0][i]` is 1.
    for i in range(1, n + 1):
        for mask in range(1, 1 << n):
            for j in range(n):
                if a[i - 1][j] == 1 and mask & 1 << j:
                    dp[i][mask] += dp[i - 1][mask ^ 1 << j]
                    dp[i][mask] %= MOD
        
    #State of the program after the  for loop has been executed: `N` is an integer between 1 and 21 inclusive, `n` is a string convertible to an integer greater than 0, `i` is `n + 1`, `mask` is `2^n - 1`, `j` has iterated through all values from 0 to `n - 1`, and `dp[n][mask]` has been updated based on the conditions met during all iterations of the nested loops.
    print(dp[n][(1 << n) - 1])
#Overall this is what the function does:The function accepts an integer `N` (1 ≤ N ≤ 21) and a 2D list `a` of integers (0 or 1) representing compatibility between `N` men and `N` women. It calculates the number of ways to pair each man with a woman such that only compatible pairs (indicated by 1 in the list) are chosen. The result is printed as the number of valid pairings modulo 1000000007.

