#State of the program right berfore the function call: k is an integer such that 0 ≤ k ≤ min(n, b), n is an integer representing the number of buns, a is an integer representing the usual price of a bun, and b is an integer representing the price of the first bun to be sold at a modified price.
def func_1(k, n, a, b):
    return k * b - k * (k - 1) // 2 + (n - k) * a
    #The program returns the value of \( k \times b - \frac{k \times (k - 1)}{2} + (n - k) \times a \)
#Overall this is what the function does:The function accepts four parameters: `k`, `n`, `a`, and `b`. It calculates and returns the value of \( k \times b - \frac{k \times (k - 1)}{2} + (n - k) \times a \). This formula represents a specific computation involving the integers `k`, `n`, `a`, and `b`, where `k` is constrained by the range from 0 to the minimum of `n` and `b`.

#State of the program right berfore the function call: n is a positive integer representing the number of buns, a is a positive integer representing the usual price of a bun, and b is a positive integer representing the price of the first bun to be sold at a modified price, such that 1 ≤ n, a, b ≤ 10^9.
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
        
    #State: max_profit is the maximum value of profit calculated by `func_1(mid, n, a, b)` for any mid within the range [0, b].
    return max_profit
    #The program returns the maximum value of profit calculated by `func_1(mid, n, a, b)` for any mid within the range [0, b].
#Overall this is what the function does:The function accepts three parameters: `n`, `a`, and `b`, representing the number of buns, the usual price of a bun, and the price of the first bun to be sold at a modified price, respectively. It then calculates and returns the maximum profit that can be achieved by selling the buns using the `func_1(mid, n, a, b)` function for any midpoint `mid` within the range [0, `b`].

