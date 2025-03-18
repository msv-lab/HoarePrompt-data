#State of the program right berfore the function call: k, n, a, and b are integers such that 0 <= k <= n, and 1 <= n, a, b <= 10^9.
def func_1(k, n, a, b):
    return k * b - k * (k - 1) // 2 + (n - k) * a
    #The program returns the value of the expression \( k \times b - k \times \left(\frac{k - 1}{2}\right) + (n - k) \times a \)
#Overall this is what the function does:The function calculates and returns the value of the expression \( k \times b - k \times \left(\frac{k - 1}{2}\right) + (n - k) \times a \) using the input integers \( k \), \( n \), \( a \), and \( b \) with the constraints \( 0 \leq k \leq n \) and \( 1 \leq n, a, b \leq 10^9 \).

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
        
    #State: - `low` will be greater than `high`.
    #- `high` will be the last value that was checked and found to not yield a higher profit than the next value.
    #- `max_profit` will be the maximum profit found during the binary search.
    #
    #Given the above explanation, the final output state can be described as follows:
    #
    #Output State:
    return max_profit
    #The program returns max_profit, which is the maximum profit found during the binary search.
#Overall this is what the function does:The function `func_2` takes three integer parameters `n`, `a`, and `b`, each ranging from 1 to 10^9 inclusive. It calculates and returns `max_profit`, which represents the maximum profit achievable through a binary search process based on the given inputs.

