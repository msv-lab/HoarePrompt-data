#State of the program right berfore the function call: k, n, a, and b are non-negative integers such that 0 <= k <= min(n, b), 1 <= n, a, b <= 10^9.
def func_1(k, n, a, b):
    return k * b - k * (k - 1) // 2 + (n - k) * a
    #The program returns the value of the expression `k * b - k * (k - 1) // 2 + (n - k) * a`, where `k`, `n`, `a`, and `b` are non-negative integers with the constraints 0 <= k <= min(n, b), 1 <= n, a, b <= 10^9.
#Overall this is what the function does:The function `func_1` accepts four parameters `k`, `n`, `a`, and `b`, which are non-negative integers with the constraints 0 <= k <= min(n, b) and 1 <= n, a, b <= 10^9. It returns a single integer value calculated as `k * b - k * (k - 1) // 2 + (n - k) * a`. The purpose of the function is to compute a specific mathematical expression based on the given parameters. After the function concludes, the input parameters remain unchanged, and the function's return value is the result of the expression.

#State of the program right berfore the function call: n, a, and b are integers such that 1 <= n, a, b <= 10^9.
def func_2(n, a, b):
    low, high = 0, min(n, b)
    max_profit = 0
    while low <= high:
        mid = (low + high) // 2
        
        profit_mid = func_1(mid, n, a, b)
        
        profit_next = func_1(mid + 1, n, a, b)
        
        max_profit = max(max_profit, profit_mid)
        
        if profit_next > profit_mid:
            low = mid + 1
        else:
            high = mid - 1
        
    #State: `low` is the value where the maximum profit is achieved, `high` is `low - 1`, and `max_profit` is the maximum profit value.
    return max_profit
    #The program returns the maximum profit value, which is the value of `max_profit`.
#Overall this is what the function does:The function `func_2` accepts three integers `n`, `a`, and `b` within the range 1 to 10^9. It calculates the maximum profit value by evaluating the profit at different points within the range `[0, min(n, b)]` using the function `func_1`. The function returns the maximum profit value found. After the function concludes, `low` is the value where the maximum profit is achieved, `high` is `low - 1`, and `max_profit` contains the maximum profit value.

