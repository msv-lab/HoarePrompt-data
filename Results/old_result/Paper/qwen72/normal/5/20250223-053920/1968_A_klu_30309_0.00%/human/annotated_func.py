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
        
    #State: `x` is an integer such that 2 <= x <= 1000, `max_val` is the largest integer divisor of `x` that is less than `x` and greater than 1, but if there is a divisor `y` such that 2 * y >= x, then `max_val` is that divisor.
    return max_val
    #The program returns the largest integer divisor of `x` that is less than `x` and greater than 1, but if there is a divisor `y` such that 2 * y >= x, then the program returns that divisor `y`.
#Overall this is what the function does:The function `func_1` accepts an integer `x` (where 2 <= x <= 1000) and returns the largest integer divisor of `x` that is less than `x` and greater than 1. If there is a divisor `y` such that 2 * y >= x, it returns that divisor `y`. If no such divisor exists, it returns 1.

