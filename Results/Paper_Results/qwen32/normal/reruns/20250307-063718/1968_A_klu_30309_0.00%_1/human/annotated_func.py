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
        
    #State: `max_val` is the largest divisor of `x` that is less than `x / 2`, or `1` if no such divisor exists.
    return max_val
    #The program returns `max_val`, which is the largest divisor of `x` that is less than `x / 2`, or `1` if no such divisor exists.
#Overall this is what the function does:The function takes an integer `x` such that 2 <= x <= 1000 and returns the largest divisor `y` of `x` that satisfies `2 * y >= x`. If no such divisor exists, it returns the largest divisor of `x` that is less than `x / 2`, or `1` if no such divisor exists.

