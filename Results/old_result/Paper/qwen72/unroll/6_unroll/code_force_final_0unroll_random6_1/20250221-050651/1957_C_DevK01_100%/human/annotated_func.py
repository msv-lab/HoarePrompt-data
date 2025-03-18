#State of the program right berfore the function call: n is an integer where 1 ≤ n ≤ 3 · 10^5.
def func_1(n):
    dp = [1, 1]
    for i in range(2, n + 1):
        dp += [(dp[-1] + 2 * (i - 1) * dp[-2]) % (7 + 10 ** 9)]
        
        dp.pop(0)
        
    #State: `dp` is a list with values [dp[n-1], dp[n]].
    return dp[-1]
    #The program returns the value of `dp[n]`.
#Overall this is what the function does:The function `func_1` accepts an integer `n` within the range 1 to 300,000 and returns the value of `dp[n]`, where `dp` is a list that dynamically computes and stores values based on a specific formula. After the function concludes, the list `dp` contains the last two computed values, but only the value at `dp[n]` is returned. The function effectively calculates a sequence value using a rolling array technique to optimize memory usage.

