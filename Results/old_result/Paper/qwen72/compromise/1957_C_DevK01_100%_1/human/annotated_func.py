#State of the program right berfore the function call: n is an integer where 1 ≤ n ≤ 3 · 10^5.
def func_1(n):
    dp = [1, 1]
    for i in range(2, n + 1):
        dp += [(dp[-1] + 2 * (i - 1) * dp[-2]) % (7 + 10 ** 9)]
        
        dp.pop(0)
        
    #State: `n` is an integer where 2 ≤ n ≤ 3 · 10^5, `dp` is a list with two elements: [dp[n-1], dp[n]], `i` is n + 1.
    return dp[-1]
    #The program returns the value of `dp[n]`, which is the second element in the list `dp` that contains two elements: [dp[n-1], dp[n]].
#Overall this is what the function does:The function `func_1` accepts an integer `n` within the range 1 ≤ n ≤ 3 · 10^5 and returns the value of `dp[n]`, which is the result of a specific computation involving the previous values in the `dp` list. The final state of the program after the function concludes is that `n` remains unchanged, and the function returns the computed value `dp[n]`.

