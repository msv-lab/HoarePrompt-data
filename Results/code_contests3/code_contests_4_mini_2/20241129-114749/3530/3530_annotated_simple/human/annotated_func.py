#State of the program right berfore the function call: N is an integer such that 1 <= N <= 21, and a is a 2D list of integers where each element is either 0 or 1, with dimensions N x N.
def func():
    MOD = 1000000007
    n = input()
    a = []
    for _ in range(n):
        a.append(map(int, raw_input().split()))
        
    #State of the program after the  for loop has been executed: `N` is an integer such that 1 <= `N` <= 21; `a` is a list containing `n` lists of integers obtained from input; `MOD` is 1000000007.
    dp = [([0] * (1 << n)) for _ in range(n + 1)]
    for i in range(1 << n):
        dp[0][i] = 1
        
    #State of the program after the  for loop has been executed: `N` is an integer such that 1 <= `N` <= 21, `a` contains at least 1 list, `n` is the length of `a`, `dp[0]` is a list of length `2^n` where each element is 1.
    for i in range(1, n + 1):
        for mask in range(1, 1 << n):
            for j in range(n):
                if a[i - 1][j] == 1 and mask & 1 << j:
                    dp[i][mask] += dp[i - 1][mask ^ 1 << j]
                    dp[i][mask] %= MOD
        
    #State of the program after the  for loop has been executed: `N` is an integer such that 1 <= `N` <= 21, `a` contains at least 1 list, `n` is the length of `a`, `dp[N][mask]` contains the accumulated values based on the conditions met during all iterations of the loop for each possible `mask`, taken modulo `MOD`, and `i` is `N`, `mask` is in the range from 1 to `2^n - 1`, and `j` is in the range from 0 to `n - 1`.
    print(dp[n][(1 << n) - 1])
#Overall this is what the function does:The function accepts an integer `N` (where 1 <= N <= 21) and a 2D list `a` of integers (0s and 1s) with dimensions N x N. It calculates a dynamic programming table to determine the number of ways to select a set of items such that no two selected items are in conflict, as represented in the input list. Finally, it prints the total number of valid selections modulo 1000000007.

