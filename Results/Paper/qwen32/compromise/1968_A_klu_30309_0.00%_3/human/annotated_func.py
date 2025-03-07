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
        
    #State: max_val is the largest proper divisor of x such that 2 * max_val < x.
    return max_val
    #The program returns max_val, which is the largest proper divisor of x such that 2 * max_val < x.
#Overall this is what the function does:The function accepts an integer `x` where 2 <= x <= 1000 and returns the largest proper divisor `y` of `x` such that 2 * `y` is less than `x`.

