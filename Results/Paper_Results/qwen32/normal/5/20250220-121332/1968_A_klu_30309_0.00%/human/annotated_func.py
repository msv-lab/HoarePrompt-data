#State of the program right berfore the function call: x is an integer such that 2 <= x <= 1000.
def func_1(x):
    """Finds the y that maximizes gcd(x, y) + y.

  Args:
    x: The given integer.

  Returns:
    The optimal y.
  """
    max_val = 1
    for y in range(x - 1, 1, -1):
        if x % y == 0:
            if 2 * y >= x:
                return y
            max_val = y
        
    #State: The largest divisor of `x` that is less than `x / 2`, or the first divisor `y` found such that `2 * y >= x`.
    return max_val
    #The program returns `max_val` which is the largest divisor of `x` that is less than `x / 2`, or the first divisor `y` found such that `2 * y >= x`.
#Overall this is what the function does:The function accepts an integer `x` such that 2 <= x <= 1000 and returns an integer `y` that maximizes the expression `gcd(x, y) + y`. Specifically, it returns the first divisor `y` of `x` such that `2 * y >= x`, or the largest divisor of `x` that is less than `x / 2` if no such `y` exists.

