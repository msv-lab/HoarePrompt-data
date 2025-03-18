#State of the program right berfore the function call: k is an integer such that 0 ≤ k ≤ min(n, b), n is an integer representing the number of buns, a is an integer representing the usual price of a bun, and b is an integer representing the price of the first bun to be sold at a modified price.
def func_1(k, n, a, b):
    return k * b - k * (k - 1) // 2 + (n - k) * a
    #The program returns the expression k * b - k * (k - 1) // 2 + (n - k) * a, where k is an integer such that 0 ≤ k ≤ min(n, b), n is the number of buns, a is the usual price of a bun, and b is the price of the first bun to be sold at a modified price.
#Overall this is what the function does:The function calculates and returns the total cost of selling buns. It considers the first k buns to be sold at a modified price b, and the remaining (n - k) buns to be sold at the usual price a. The function also accounts for the discount applied to the first k buns using the formula k * b - k * (k - 1) // 2.

#State of the program right berfore the function call: n is an integer representing the number of buns, a is an integer representing the usual price of a bun, and b is an integer representing the price of the first bun to be sold at a modified price. Additionally, 1 ≤ n, a, b ≤ 10^9, and 0 ≤ k ≤ min(n, b), where k is an integer chosen by Bob to maximize his profit.
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
        
    #State: Output State: `low` is greater than `high`, `max_profit` is the maximum profit found during the iterations, `mid` is the last calculated midpoint, `profit_mid` and `profit_next` are the profits at `mid` and `mid + 1` respectively, and `high` is the minimum of `n` and `b`.
    #
    #Explanation: After all iterations of the loop, the condition `low <= high` will no longer be satisfied, meaning `low` will be greater than `high`. The variable `max_profit` will hold the highest profit found during the entire process of narrowing down the range. `mid` will be the last midpoint calculated, and `profit_mid` and `profit_next` will be the profits corresponding to `mid` and `mid + 1` in the final iteration. The value of `high` will be the minimum of `n` and `b`, as it is not changed once the loop terminates.
    return max_profit
    #The program returns the maximum profit found during the iterations, which is stored in the variable `max_profit`.
#Overall this is what the function does:The function accepts three parameters: `n` (the number of buns), `a` (the usual price of a bun), and `b` (the price of the first bun to be sold at a modified price). It calculates and returns the maximum profit that can be achieved by selling some of the buns at the modified price (`b`). The function uses a binary search approach to find the optimal number of buns to sell at the modified price, ensuring the maximum profit is determined.

