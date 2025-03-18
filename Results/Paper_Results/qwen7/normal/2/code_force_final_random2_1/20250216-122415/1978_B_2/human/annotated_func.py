#State of the program right berfore the function call: k is an integer such that 0 ≤ k ≤ min(n, b), n is an integer representing the number of buns, a is an integer representing the usual price of a bun, and b is an integer representing the price of the first bun to be sold at a modified price.
def func_1(k, n, a, b):
    return k * b - k * (k - 1) // 2 + (n - k) * a
    #The program returns the value of \( k \times b - k \times (k - 1) // 2 + (n - k) \times a \)
#Overall this is what the function does:The function accepts four parameters: `k`, `n`, `a`, and `b`. It calculates and returns the value of \( k \times b - k \times (k - 1) // 2 + (n - k) \times a \).

#State of the program right berfore the function call: n is a positive integer representing the number of buns, a is a positive integer representing the usual price of a bun, and b is a positive integer representing the price of the first bun to be sold at a modified price, such that 1 <= n, a, b <= 10^9.
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
        
    #State: Output State: The final value of `max_profit` is the highest profit obtained during any iteration of the loop. After all iterations, `low` will be exactly one more than `high`, indicating that the binary search has completed. The variable `mid` will hold the last midpoint value considered in the search, and `profit_mid` and `profit_next` will be the profits calculated for `mid` and `mid + 1` respectively in the last iteration. However, since the loop condition `low <= high` ensures that the search continues until `low` exceeds `high`, the exact values of `profit_mid` and `profit_next` in the last iteration are not specified but are used to update `max_profit`.
    #
    #In simpler terms, after all iterations, `max_profit` will contain the highest profit found throughout the entire binary search process, and the search range will no longer satisfy the condition `low <= high`.
    return max_profit
    #The program returns the highest profit obtained during the binary search process.
#Overall this is what the function does:The function accepts three parameters: `n`, `a`, and `b`, where `n` represents the number of buns, `a` represents the usual price of a bun, and `b` represents the price of the first bun to be sold at a modified price. It performs a binary search to find the optimal number of buns to sell at the modified price in order to maximize profit. The function returns the highest profit obtained during this process.

