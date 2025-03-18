#State of the program right berfore the function call: n is a positive integer representing the size of the chessboard, and it is guaranteed that 1 ≤ n ≤ 3 · 10^5.
def func_1(n):
    dp = [1, 1]
    for i in range(2, n + 1):
        dp += [(dp[-1] + 2 * (i - 1) * dp[-2]) % (7 + 10 ** 9)]
        
        dp.pop(0)
        
    #State: `n` is a positive integer representing the size of the chessboard, and it is guaranteed that 1 ≤ n ≤ 3 · 10^5; `dp` is a list with two elements: [dp[n-2], dp[n-1]]; `i` is n.
    return dp[-1]
    #The program returns the value of `dp[n-1]`, which is the second element in the list `dp` representing the dynamic programming state for the (n-1)th position on the chessboard.
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` (where 1 ≤ n ≤ 3 · 10^5) and returns the value of `dp[n-1]`, which represents the dynamic programming state for the (n-1)th position on a chessboard. The function maintains a list `dp` of two elements, updating it in each iteration to store the current and previous dynamic programming states. After the function concludes, the list `dp` contains the states for the (n-2)th and (n-1)th positions, and the final state of the program includes the returned value `dp[n-1]`.

