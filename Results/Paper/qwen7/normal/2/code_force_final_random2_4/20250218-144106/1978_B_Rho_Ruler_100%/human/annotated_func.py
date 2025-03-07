#State of the program right berfore the function call: k is an integer such that 0 ≤ k ≤ min(n, b), n is an integer representing the number of buns, a is an integer representing the usual price of a bun, and b is an integer representing the price of the first bun to be sold at a modified price.
def func_1(k, n, a, b):
    return k * b - k * (k - 1) // 2 + (n - k) * a
    #The program returns the value calculated as k times b minus half of k times (k minus 1), plus (n minus k) times a.
#Overall this is what the function does:The function accepts four parameters: `k`, `n`, `a`, and `b`. It calculates and returns a value based on these parameters using the formula `k * b - k * (k - 1) // 2 + (n - k) * a`. This value represents a computed cost or revenue related to selling buns, where the first `k` buns are sold at a modified price `b`, and the remaining buns are sold at the usual price `a`.

#State of the program right berfore the function call: n is an integer representing the number of buns, a is an integer representing the usual price of a bun, and b is an integer representing the price of the first bun to be sold at a modified price. Additionally, 1 ≤ n, a, b ≤ 10^9, and 0 ≤ b ≤ min(n, b).
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
        
    #State: Output State: `low` is the final lower bound where the maximum profit is found, `high` is the final upper bound which is either `low` or one step above it, `max_profit` is the highest profit found during the iterations, `mid` is the last midpoint calculated, and `profit_next` is the profit calculated at `mid + 1`.
    #
    #In this final state, the algorithm has iteratively narrowed down the range `[low, high]` to find the optimal `mid` that maximizes the profit as determined by the function `func_1(mid, n, a, b)`. The variable `max_profit` holds the highest profit encountered throughout these iterations. The values of `low`, `high`, and `mid` reflect the last comparison made within the loop, with `low` being the best lower bound and `high` being the corresponding upper bound.
    return max_profit
    #The program returns the highest profit (`max_profit`) found during the iterations, with `low` being the final lower bound and `high` being the final upper bound which is either `low` or one step above it.
#Overall this is what the function does:The function `func_2` accepts three parameters: `n` (the number of buns), `a` (the usual price of a bun), and `b` (the price of the first bun to be sold at a modified price). It uses a binary search approach to find the optimal number of buns to sell at the modified price (`b`) in order to maximize profit. The function returns the highest profit found during the iterations, along with the final lower and upper bounds (`low` and `high`) of the search range.

