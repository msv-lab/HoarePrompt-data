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
        
    #State: max_val is 1.
    return max_val
    #The program returns 1
#Overall this is what the function does:The function accepts an integer `x` within the range 2 to 1000 (inclusive) and always returns 1. It searches for an integer `y` such that `2 * y >= x` and `gcd(x, y) + y` is maximized, but if no such `y` exists, it returns 1.

