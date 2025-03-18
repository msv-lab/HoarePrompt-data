#State of the program right berfore the function call: n is an integer representing the size of the chessboard, such that 1 ≤ n ≤ 3 · 10^5.
def func_1(n):
    dp = [1, 1]
    for i in range(2, n + 1):
        dp += [(dp[-1] + 2 * (i - 1) * dp[-2]) % (7 + 10 ** 9)]
        
        dp.pop(0)
        
    #State: `n` is an integer representing the size of the chessboard, such that 1 ≤ n ≤ 3 · 10^5; `dp` is a list containing the values [dp[n], dp[n-1]].
    return dp[-1]
    #The program returns the value of `dp[n-1]`, which is the second last element in the list `dp` that contains the values [dp[n], dp[n-1]].
#Overall this is what the function does:The function `func_1` accepts an integer `n` (1 ≤ n ≤ 3 · 10^5) representing the size of a chessboard and returns the value of `dp[n]`, which is the number of ways to place non-attacking rooks on an n x n chessboard, modulo (7 + 10^9). The function maintains a rolling list `dp` of the last two computed values to achieve this.

