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
        
    #State: `x` remains the same, `max_val` is the largest divisor of `x` that is less than `x / 2` if no `y` satisfies `2 * y >= x`.
    return max_val
    #The program returns `max_val`, which is the largest divisor of `x` that is less than `x / 2` if no `y` satisfies `2 * y >= x`.
#Overall this is what the function does:The function `func_1` accepts an integer `x` such that 2 <= x <= 1000. It returns the largest integer `y` that divides `x` perfectly and satisfies `2 * y >= x`. If no such `y` exists, it returns the largest divisor of `x` that is less than `x / 2`.

