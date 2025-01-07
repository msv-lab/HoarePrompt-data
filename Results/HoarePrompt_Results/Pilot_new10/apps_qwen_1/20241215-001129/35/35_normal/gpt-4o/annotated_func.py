#State of the program right berfore the function call: n, a, and b are positive integers such that 1 ≤ a, b ≤ 100 and 2 ≤ n ≤ a + b.
def func_1(n, a, b):
    low, high = 1, min(a, b) + 1
    while low < high:
        mid = (low + high) // 2
        
        if can_distribute(mid):
            low = mid + 1
        else:
            high = mid
        
    #State of the program after the loop has been executed: `n` is a positive integer such that \(2 \leq n \leq a + b\); `a` and `b` are positive integers such that \(1 \leq a \leq 100\) and \(1 \leq b \leq 100\); `low` is the smallest integer such that \(\text{can\_distribute(low)}\) is `True`, and `high` is the largest integer such that \(\text{can\_distribute(high)}\) is `False`; `mid` is \((\text{low} + \text{high}) // 2\).
    return low - 1
    #The program returns low - 1, where low is the smallest integer such that can_distribute(low) is True
#Overall this is what the function does:The function `func_1` accepts three parameters `n`, `a`, and `b`, and returns the smallest integer `low - 1` such that `can_distribute(low)` is `True`.

#State of the program right berfore the function call: a and b are positive integers representing the number of pieces of the first and second cake, respectively, and n is a positive integer representing the number of plates such that 1 ≤ a, b ≤ 100 and 2 ≤ n ≤ a + b.
def can_distribute(x):
    return a // x + b // x >= n
    #`a // x + b // x` is compared to `n`, and the program returns `True` if the sum is greater than or equal to `n`, otherwise `False`
#Overall this is what the function does:The function `can_distribute(x)` accepts a parameter `x` and returns `True` if distributing `a` and `b` pieces of cake among `n` plates results in each plate having at least `x` pieces of cake. Otherwise, it returns `False`.

