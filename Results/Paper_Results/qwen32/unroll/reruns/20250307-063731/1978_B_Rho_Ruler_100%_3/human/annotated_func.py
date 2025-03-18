#State of the program right berfore the function call: k, n, a, and b are integers such that 0 <= k <= n, and 1 <= n, a, b <= 10^9.
def func_1(k, n, a, b):
    return k * b - k * (k - 1) // 2 + (n - k) * a
    #The program returns the value of the expression \( k \times b - k \times \frac{(k - 1)}{2} + (n - k) \times a \)
#Overall this is what the function does:The function calculates and returns a specific value based on the input integers `k`, `n`, `a`, and `b` using the formula \( k \times b - k \times \frac{(k - 1)}{2} + (n - k) \times a \).

#State of the program right berfore the function call: n is an integer representing the number of buns, a is an integer representing the usual price of a bun, and b is an integer representing the price of the first bun to be sold at a modified price. All of n, a, and b are positive integers such that 1 <= n, a, b <= 10^9.
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
        
    #State: max_profit is the maximum profit achievable by selling a certain number of buns at the modified price.
    return max_profit
    #The program returns max_profit, which is the maximum profit achievable by selling a certain number of buns at the modified price.
#Overall this is what the function does:The function calculates and returns the maximum profit achievable by selling `n` buns, where the first `b` buns can be sold at a modified price, potentially different from the usual price `a`.

