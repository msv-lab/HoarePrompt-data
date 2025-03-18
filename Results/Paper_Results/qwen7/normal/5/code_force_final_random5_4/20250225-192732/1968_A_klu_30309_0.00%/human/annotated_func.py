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
        
    #State: x is an integer, y is 1, and max_val remains unchanged.
    return max_val
    #The program returns max_val which remains unchanged from its initial state.
#Overall this is what the function does:The function accepts an integer x within the range of 2 to 1000 and returns an integer y. The function aims to find the y that maximizes the expression gcd(x, y) + y. Specifically, it returns:
- y if x is divisible by y and 2 * y is greater than or equal to x,
- x - 1 if no such y is found,
- x - 2 if no suitable y is found and y cannot be x - 1,
- 1 if no suitable y is found and y cannot be x - 1 or x - 2.

