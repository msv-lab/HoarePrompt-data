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
        
    #State: x remains an integer such that 2 <= x <= 1000, max_val is the largest integer y such that 2 <= y < x and x % y == 0, or 1 if no such y exists.
    return max_val
    #The program returns the largest integer `max_val` such that 2 <= `max_val` < `x` and `x` % `max_val` == 0, or 1 if no such `max_val` exists.
#Overall this is what the function does:The function `func_1` accepts an integer `x` (where 2 <= x <= 1000) and returns the largest integer `y` that is less than `x` and divides `x` evenly. If no such `y` exists, it returns 1.

