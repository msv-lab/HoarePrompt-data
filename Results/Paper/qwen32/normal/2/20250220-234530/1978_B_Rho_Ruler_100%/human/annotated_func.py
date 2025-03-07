#State of the program right berfore the function call: k, n, a, and b are integers such that 0 <= k <= n, 1 <= n <= 10^9, 1 <= a <= 10^9, and 1 <= b <= 10^9.
def func_1(k, n, a, b):
    return k * b - k * (k - 1) // 2 + (n - k) * a
    #The program returns the calculated value of \( k \times b - \frac{k \times (k - 1)}{2} + (n - k) \times a \)
#Overall this is what the function does:The function takes four integer parameters `k`, `n`, `a`, and `b`, and returns the calculated value of \( k \times b - \frac{k \times (k - 1)}{2} + (n - k) \times a \).

#State of the program right berfore the function call: n is a positive integer representing the number of buns, a is a positive integer representing the usual price of a bun, and b is a positive integer representing the price of the first bun to be sold at a modified price.
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
        
    #State: `low` is greater than `high`, `max_profit` is the maximum profit found.
    return max_profit
    #The program returns max_profit, which is the maximum profit found.
#Overall this is what the function does:The function calculates and returns the maximum profit that can be achieved by selling a given number of buns (`n`), where the first `b` buns are sold at a modified price and the rest at a usual price (`a`).

