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
        
    #State: `x` is an integer such that 2 <= x <= 1000, `max_val` is the largest integer `y` such that 2 <= y < x and `x % y == 0`, and `y` is 2. If no such `y` exists, `max_val` remains 1.
    return max_val
    #The program returns the largest integer `max_val` such that 2 <= `max_val` < `x` and `x % max_val == 0`. If no such `max_val` exists, the program returns 1.
#Overall this is what the function does:The function `func_1` accepts an integer `x` (where 2 <= x <= 1000) and returns the largest integer `y` such that 2 <= y < x and `x % y == 0`. If no such `y` exists, the function returns 1. The function aims to find the `y` that maximizes `gcd(x, y) + y` under the given constraints.

