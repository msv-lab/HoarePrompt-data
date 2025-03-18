#State of the program right berfore the function call: k, n, a, and b are non-negative integers such that 0 <= k <= min(n, b), 1 <= n, a, b <= 10^9.
def func_1(k, n, a, b):
    return k * b - k * (k - 1) // 2 + (n - k) * a
    #The program returns the result of the expression `k * b - k * (k - 1) // 2 + (n - k) * a`, where `k`, `n`, `a`, and `b` are non-negative integers with the constraints 0 <= k <= min(n, b), 1 <= n, a, b <= 10^9.
#Overall this is what the function does:The function `func_1` accepts four non-negative integer parameters `k`, `n`, `a`, and `b` with the constraints 0 <= k <= min(n, b) and 1 <= n, a, b <= 10^9. It returns a single integer value, which is the result of the expression `k * b - k * (k - 1) // 2 + (n - k) * a`. After the function concludes, the input parameters `k`, `n`, `a`, and `b` remain unchanged, and the program state is unaffected beyond the return value.

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
        
    #State: `low` is the smallest integer such that `profit` does not increase anymore, `high` is `low - 1`, and `max_profit` is the maximum profit found.
    return max_profit
    #The program returns the maximum profit found, which is stored in the variable `max_profit`.
#Overall this is what the function does:The function `func_2` accepts three integers `n`, `a`, and `b` (each between 1 and 10^9) and returns the maximum profit that can be achieved. The function uses a binary search approach to find the optimal value within the range [0, min(n, b)], and the final state of the program is such that the variable `max_profit` holds the maximum profit found.

