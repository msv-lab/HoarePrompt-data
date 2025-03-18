#State of the program right berfore the function call: k, n, a, and b are integers such that 0 <= k <= n, and 1 <= n, a, b <= 10^9.
def func_1(k, n, a, b):
    return k * b - k * (k - 1) // 2 + (n - k) * a
    #The program returns \( k \times b - k \times \left( \frac{k - 1}{2} \right) + (n - k) \times a \)
#Overall this is what the function does:The function calculates and returns a specific value based on the input parameters `k`, `n`, `a`, and `b`. This value is determined by the formula \( k \times b - k \times \left( \frac{k - 1}{2} \right) + (n - k) \times a \).

#State of the program right berfore the function call: n is a non-negative integer representing the number of buns, a is a non-negative integer representing the usual price of a bun, and b is a non-negative integer representing the price of the first bun to be sold at a modified price.
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
        
    #State: low is greater than high, high is the optimal number of buns sold at the modified price, max_profit is the maximum achievable profit.
    return max_profit
    #The program returns max_profit, which is the maximum achievable profit.
#Overall this is what the function does:The function calculates and returns the maximum achievable profit by determining the optimal number of buns to sell at a modified price, given the total number of buns, the usual price of a bun, and the modified price of the first bun.

