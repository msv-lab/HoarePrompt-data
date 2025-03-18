#State of the program right berfore the function call: k is an integer such that 0 ≤ k ≤ min(n, b), n is an integer representing the number of buns, a is an integer representing the usual price of a bun, and b is an integer representing the price of the first bun to be sold at a modified price.
def func_1(k, n, a, b):
    return k * b - k * (k - 1) // 2 + (n - k) * a
    #The program returns the value of \( k \times b - k \times \frac{(k - 1)}{2} + (n - k) \times a \)
#Overall this is what the function does:The function calculates and returns the total cost of selling `n` buns, where the first `k` buns are sold at a modified price `b`, and the remaining `n-k` buns are sold at the usual price `a`. The modified price applies a discount that decreases the price of each subsequent bun by 1 unit compared to the previous one.

#State of the program right berfore the function call: n is an integer representing the number of buns, a is an integer representing the usual price of a bun, and b is an integer representing the price of the first bun to be sold at a modified price. Additionally, both a and b are positive integers, and 1 <= n, a, b <= 10^9.
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
        
    #State: The value of `max_profit` is the maximum profit calculated by `func_1` for any `mid` value within the range of `low` to `high`.
    return max_profit
    #The program returns the maximum profit calculated by func_1 for any mid value within the range of low to high.
#Overall this is what the function does:The function accepts three parameters: `n`, `a`, and `b`, where `n` represents the number of buns, `a` represents the usual price of a bun, and `b` represents the price of the first bun to be sold at a modified price. It calculates and returns the maximum profit possible by selling some of the buns at the modified price (`b`) and the rest at the usual price (`a`).

