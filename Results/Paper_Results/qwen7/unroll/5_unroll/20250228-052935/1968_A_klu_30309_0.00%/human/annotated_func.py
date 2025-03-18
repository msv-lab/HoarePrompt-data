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
        
    #State: Output State: `max_val` is the largest divisor of `x` that is less than or equal to half of `x`, and `x` remains an integer such that 2 <= x <= 1000.
    return max_val
    #The program returns the largest divisor of `x` that is less than or equal to half of `x`, given that `x` is an integer between 2 and 1000.
#Overall this is what the function does:The function accepts an integer `x` such that 2 ≤ x ≤ 1000, and returns the largest divisor of `x` that is less than or equal to half of `x`. It iterates through possible values of `y` starting from `x - 1` down to 2, checking if `y` is a divisor of `x` and if `2 * y` is greater than or equal to `x`. If both conditions are met, it returns `y`; otherwise, it continues the search and updates the maximum value found. If no suitable `y` is found, it returns the maximum value found during the iteration.

