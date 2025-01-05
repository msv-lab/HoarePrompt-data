#State of the program right berfore the function call: N is a positive integer such that 1 <= N <= 21, and a is a 2D list of integers where each element is either 0 or 1, with dimensions N x N.
def func():
    MOD = 1000000007
    n = input()
    a = []
    for _ in range(n):
        a.append(map(int, raw_input().split()))
        
    #State of the program after the  for loop has been executed: `N` is a positive integer such that 1 <= `N` <= 21; `a` is a list containing `n` lists of integers from the input; `MOD` is 1000000007.
    dp = [([0] * (1 << n)) for _ in range(n + 1)]
    for i in range(1 << n):
        dp[0][i] = 1
        
    #State of the program after the  for loop has been executed: `N` is a positive integer such that 1 <= `N` <= 21, `a` is a list containing `n` lists of integers from the input, `MOD` is 1000000007, `dp[0][i]` is 1 for all `i` in the range from 0 to `(1 << n) - 1`, and `dp` has (n + 1) lists each containing (1 << n) zeros.
    for i in range(1, n + 1):
        for mask in range(1, 1 << n):
            for j in range(n):
                if a[i - 1][j] == 1 and mask & 1 << j:
                    dp[i][mask] += dp[i - 1][mask ^ 1 << j]
                    dp[i][mask] %= MOD
        
    #State of the program after the  for loop has been executed: `N` is a positive integer such that 1 <= `N` <= 21, `n` is equal to `N`, `i` is `N`, `mask` is in the range from 1 to \(2^n - 1\), and `dp[N][mask]` contains the sum of valid `dp[N - 1][mask ^ 1 << j]` values taken modulo `MOD` for all valid `j` where `a[N - 1][j] == 1` and `mask & 1 << j` holds true.
    print(dp[n][(1 << n) - 1])
#Overall this is what the function does:The function accepts a positive integer `N` (1 <= N <= 21) and a 2D list `a` of integers with dimensions N x N, where each element is either 0 or 1. It calculates and prints the number of distinct ways to select a subset of elements from the last row of `a`, subject to specific constraints defined by the values in the 2D list. The result is taken modulo 1000000007. The function does not handle input errors or cases where the input does not meet the expected format.

