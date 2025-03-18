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
        
    #State: max_val is the largest value of y such that 1 < y < x and x % y == 0 and 2 * y >= x, or max_val remains 1 if no such y exists.
    return max_val
    #max_val which is the largest value of y such that 1 < y < x and x % y == 0 and 2 * y >= x, or max_val remains 1 if no such y exists.
#Overall this is what the function does:The function accepts an integer \( x \) where \( 2 \leq x \leq 1000 \). It searches for the largest integer \( y \) such that \( x \) is divisible by \( y \) and \( 2y \geq x \). If no such \( y \) exists, it returns \( x - 2 \) or \( x - 3 \) depending on the values found during the search. If no valid \( y \) is found through these checks, it returns the largest \( y \) satisfying the conditions or 1 if no such \( y \) exists.

