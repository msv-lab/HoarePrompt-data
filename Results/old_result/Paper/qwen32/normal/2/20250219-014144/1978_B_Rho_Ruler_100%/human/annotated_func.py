#State of the program right berfore the function call: k, n, a, and b are integers where 0 <= k <= n, and 1 <= n, a, b <= 10^9.
def func_1(k, n, a, b):
    return k * b - k * (k - 1) // 2 + (n - k) * a
    #The program returns \( k \times b - \frac{k \times (k - 1)}{2} + (n - k) \times a \)
#Overall this is what the function does:The function calculates and returns a specific value based on the input parameters `k`, `n`, `a`, and `b`. The returned value is computed using the formula \( k \times b - \frac{k \times (k - 1)}{2} + (n - k) \times a \).

#State of the program right berfore the function call: n, a, and b are integers where 1 <= n, a, b <= 10^9.
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
        
    #State: low = X + 1, high = X, max_profit = maximum profit found.
    return max_profit
    #The program returns max_profit, which is the maximum profit found.
#Overall this is what the function does:The function `func_2` takes three integer parameters `n`, `a`, and `b`, each ranging from 1 to 10^9. It calculates and returns `max_profit`, which is the maximum profit achievable based on these inputs.

