#State of the program right berfore the function call: k, n, a, and b are non-negative integers such that 0 <= k <= min(n, b), 1 <= n, a, b <= 10^9.
def func_1(k, n, a, b):
    return k * b - k * (k - 1) // 2 + (n - k) * a
    #The program returns the value calculated as \( k \times b - \frac{k \times (k - 1)}{2} + (n - k) \times a \), where \( k \), \( n \), \( a \), and \( b \) are non-negative integers with \( 0 \leq k \leq \min(n, b) \), \( 1 \leq n, a, b \leq 10^9 \).
#Overall this is what the function does:The function `func_1` accepts four parameters `k`, `n`, `a`, and `b`, which are non-negative integers with constraints \( 0 \leq k \leq \min(n, b) \) and \( 1 \leq n, a, b \leq 10^9 \). It calculates and returns a value based on the formula \( k \times b - \frac{k \times (k - 1)}{2} + (n - k) \times a \). After the function concludes, the returned value represents the result of this calculation, and the input parameters remain unchanged.

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
        
    #State: After the loop has executed all its iterations, `n`, `a`, and `b` remain integers such that 1 <= `n`, `a`, `b` <= 10^9. The variable `low` is greater than `high`, indicating that the loop has terminated. The variable `mid` is the last calculated midpoint before the loop terminated. The variable `profit_mid` holds the profit value at the last midpoint `mid`. The variable `profit_next` holds the profit value at `mid + 1`. The variable `max_profit` holds the maximum profit value encountered during all iterations of the loop.
    return max_profit
    #The program returns the maximum profit value (`max_profit`) encountered during all iterations of the loop, which is an integer between 1 and 10^9.
#Overall this is what the function does:The function `func_2` takes three integer parameters `n`, `a`, and `b`, each within the range 1 to 10^9. It calculates and returns the maximum profit value (`max_profit`) that can be achieved based on these inputs. The function uses a binary search approach to find the optimal value, ensuring that the returned `max_profit` is the highest profit encountered during the search process. The original values of `n`, `a`, and `b` remain unchanged. The returned `max_profit` is an integer between 1 and 10^9.

