#State of the program right berfore the function call: N is an integer such that 1 <= N <= 21, and a is a 2D list of integers where each element is either 0 or 1, with dimensions N x N.
def func():
    MOD = 1000000007
    n = input()
    a = []
    for _ in range(n):
        a.append(map(int, raw_input().split()))
        
    #State of the program after the  for loop has been executed: `N` is an integer such that 1 <= `N` <= 21, `a` is a 2D list containing `n` lists of integers from input, `MOD` is 1000000007, `n` is the number of lines read from input.
    dp = [([0] * (1 << n)) for _ in range(n + 1)]
    for i in range(1 << n):
        dp[0][i] = 1
        
    #State of the program after the  for loop has been executed: `N` is an integer such that 1 <= `N` <= 21, `n` is valid, `dp[0][i]` is 1 for all `i` in the range from 0 to (1 << n) - 1.
    for i in range(1, n + 1):
        for mask in range(1, 1 << n):
            for j in range(n):
                if a[i - 1][j] == 1 and mask & 1 << j:
                    dp[i][mask] += dp[i - 1][mask ^ 1 << j]
                    dp[i][mask] %= MOD
        
    #State of the program after the  for loop has been executed: `N` is an integer such that 1 <= `N` <= 21, `n` is valid, `i` is `n`, `mask` is 2^n - 1, and `dp[n][mask]` contains the accumulated values based on the conditions evaluated during all iterations of `i`, `mask`, and `j`.
    print(dp[n][(1 << n) - 1])
#Overall this is what the function does:The function accepts an integer `N` (1 <= N <= 21) and a 2D list `a` of integers (0 or 1) with dimensions N x N. It calculates a value stored in `dp[N][(1 << N) - 1]`, which represents the count of specific configurations based on the input matrix. Finally, it prints this value. However, the function does not return any value; it only prints the result, which may lead to confusion regarding its output.

