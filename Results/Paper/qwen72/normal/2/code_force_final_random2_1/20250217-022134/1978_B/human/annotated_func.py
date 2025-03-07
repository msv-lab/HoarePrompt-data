#State of the program right berfore the function call: k, n, a, and b are non-negative integers such that 0 <= k <= min(n, b), 1 <= n, a, b <= 10^9.
def func_1(k, n, a, b):
    return k * b - k * (k - 1) // 2 + (n - k) * a
    #The program returns the value calculated as `k * b - k * (k - 1) // 2 + (n - k) * a`, where `k`, `n`, `a`, and `b` are non-negative integers such that `0 <= k <= min(n, b)`, `1 <= n, a, b <= 10^9`.
#Overall this is what the function does:The function `func_1` accepts four non-negative integer parameters `k`, `n`, `a`, and `b`, with the constraints `0 <= k <= min(n, b)` and `1 <= n, a, b <= 10^9`. It calculates and returns the value `k * b - k * (k - 1) // 2 + (n - k) * a`. After the function concludes, the program state includes the returned value, which is the result of the specified arithmetic operation.

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
        
    #State: `n`, `a`, and `b` are integers such that 1 <= `n`, `a`, `b` <= 10^9; `low` is the final value of `mid` where `profit_next` <= `profit_mid` or `low` is one more than `high`; `high` is the final value of `mid` - 1 where `profit_next` > `profit_mid` or `high` is one less than `low`; `max_profit` is the maximum profit calculated during the loop iterations.
    return max_profit
    #The program returns the maximum profit (`max_profit`) calculated during the loop iterations, which is the highest value of profit observed when comparing `profit_next` and `profit_mid` throughout the process.
#Overall this is what the function does:The function `func_2` accepts three integer parameters `n`, `a`, and `b` (where 1 <= n, a, b <= 10^9) and returns the maximum profit (`max_profit`). This profit is determined by iteratively calculating and comparing the profit at different points within a specified range, using a binary search approach. The final state of the program includes the unchanged values of `n`, `a`, and `b`, and the returned `max_profit` represents the highest profit observed during the iterations.

