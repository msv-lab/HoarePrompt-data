#State of the program right berfore the function call: k, n, a, and b are non-negative integers such that 0 <= k <= min(n, b), 1 <= n, a, b <= 10^9.
def func_1(k, n, a, b):
    return k * b - k * (k - 1) // 2 + (n - k) * a
    #The program returns the value calculated as \( k \times b - \frac{k \times (k - 1)}{2} + (n - k) \times a \), where \( k \), \( n \), \( a \), and \( b \) are non-negative integers with \( 0 \leq k \leq \min(n, b) \), \( 1 \leq n, a, b \leq 10^9 \).
#Overall this is what the function does:The function `func_1` takes four parameters `k`, `n`, `a`, and `b`, which are non-negative integers with the constraints \( 0 \leq k \leq \min(n, b) \) and \( 1 \leq n, a, b \leq 10^9 \). It calculates and returns a value based on the formula \( k \times b - \frac{k \times (k - 1)}{2} + (n - k) \times a \). The final state of the program is that the function has returned this calculated value, and the input parameters remain unchanged.

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
        
    #State: The loop terminates when `low` becomes greater than `high`. At this point, `max_profit` holds the maximum value of `profit_mid` encountered during the loop iterations. The values of `n`, `a`, and `b` remain unchanged. `low` and `high` will have been adjusted based on the conditions within the loop, but their final values depend on the specific values of `n`, `a`, and `b` and the results of `func_1`.
    return max_profit
    #The program returns the maximum profit (`max_profit`) encountered during the loop iterations, which is the highest value of `profit_mid` found while adjusting `low` and `high`. The values of `n`, `a`, and `b` remain unchanged.
#Overall this is what the function does:The function `func_2` accepts three integers `n`, `a`, and `b` (where 1 <= n, a, b <= 10^9) and returns the maximum profit (`max_profit`) calculated during a binary search process. The function iterates through possible values of `mid` between 0 and `min(n, b)`, using a helper function `func_1` to compute the profit at each step. The final `max_profit` is the highest profit value encountered during these iterations. The input parameters `n`, `a`, and `b` remain unchanged throughout the function's execution.

