#State of the program right berfore the function call: N is a positive integer such that 1 <= N <= 21, and a is a 2D list of integers where each element is either 0 or 1, representing the compatibility between N men and N women.
def func():
    MOD = 1000000007
    n = input()
    a = []
    for _ in range(n):
        a.append(map(int, raw_input().split()))
        
    #State of the program after the  for loop has been executed: `N` is a positive integer such that 1 <= `N` <= 21; `a` contains `n` map objects of integers from user input; `MOD` is 1000000007; `n` is a positive integer greater than 0.
    dp = [([0] * (1 << n)) for _ in range(n + 1)]
    for i in range(1 << n):
        dp[0][i] = 1
        
    #State of the program after the  for loop has been executed: `N` is a positive integer such that 1 <= `N` <= 21, `a` contains `n` map objects of integers from user input, `MOD` is 1000000007, `n` is a positive integer greater than 0, `dp[0][i]` is 1 for all `i` in the range [0, 2^n - 1].
    for i in range(1, n + 1):
        for mask in range(1, 1 << n):
            for j in range(n):
                if a[i - 1][j] == 1 and mask & 1 << j:
                    dp[i][mask] += dp[i - 1][mask ^ 1 << j]
                    dp[i][mask] %= MOD
        
    #State of the program after the  for loop has been executed: `N` is a positive integer such that 1 <= `N` <= 21, `a` contains `n` map objects of integers from user input, `MOD` is 1000000007, `n` is a positive integer; `dp[n][mask]` contains the cumulative results for all masks in the range [0, 2^n - 1] after processing all valid combinations of masks and j values, with each value taken modulo `MOD`.
    print(dp[n][(1 << n) - 1])
#Overall this is what the function does:The function accepts a positive integer `N` (where 1 <= N <= 21) and a 2D list `a` representing the compatibility between `N` men and `N` women. It computes the number of ways to pair each man with a woman such that only compatible pairs (indicated by `1` in the list) are considered. The result is returned as the count of valid pairings modulo `1000000007`. The function handles all valid combinations of pairings and ensures that the compatibility data is processed correctly to yield the final count.

