#State of the program right berfore the function call: a and b are non-negative integers.
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State of the program after the loop has been executed: `b` is 0, `a` is the greatest common divisor (GCD) of the original values of `a` and `b`, and `a` and `b` are both non-negative integers.
    return a
    #The program returns the greatest common divisor (GCD) of the original values of a and b, where b is 0 and a is a non-negative integer.
#Overall this is what the function does:The function accepts two non-negative integer parameters `a` and `b`, and returns the greatest common divisor (GCD) of the original values of `a` and `b`. The function handles the case where either `a` or `b` is zero, as the GCD is well-defined in those scenarios. If both `a` and `b` are zero, the function will return 0 as per convention.

#State of the program right berfore the function call: n is a positive integer such that 2 <= n <= 10^6.
def func_2(n):
    res = 0
    for i in range(1, n + 1):
        res = max(res, func_1(res, i))
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 2 <= n <= 10^6, `res` is the maximum value returned by `func_1` across all iterations from 1 to `n`, `i` is `n`.
    return res
    #The program returns the maximum value returned by func_1 across all iterations from 1 to n, where n is a positive integer such that 2 <= n <= 10^6
#Overall this is what the function does:The function accepts a positive integer `n` (where 2 <= n <= 10^6) and returns the maximum value obtained from calling `func_1` with parameters `res` and `i` for each `i` from 1 to `n`. The variable `res` is initialized to 0 and is updated with the maximum value returned by `func_1` during the iterations.

#State of the program right berfore the function call: n is a positive integer such that 2 <= n <= 10^6, and f_max_n is a non-negative integer that represents the maximum value of f(p) for permutations of integers 1 to n.
def func_3(n, f_max_n):
    MOD = 10 ** 9 + 7
    dp = [0] * (f_max_n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(f_max_n, 0, -1):
            dp[j] += dp[j - 1]
            dp[j] %= MOD
        
    #State of the program after the  for loop has been executed: `dp` contains the number of combinations up to `f_max_n` based on the original values, `n` is a positive integer such that 2 <= n <= 10^6, and `f_max_n` is at least 1.
    return dp[f_max_n]
    #The program returns the number of combinations up to `f_max_n` based on the original values stored in `dp`
#Overall this is what the function does:The function accepts a positive integer `n` (between 2 and 10^6) and a non-negative integer `f_max_n`, and it calculates the number of combinations of permutations of integers from 1 to `n` that sum to at most `f_max_n`. The result is returned modulo 10^9 + 7. The function does not handle cases where `f_max_n` is 0, as the initial state of `dp` is set for `f_max_n` starting from 1.

