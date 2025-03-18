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
        
    #State: The output state after the loop executes all iterations is that `max_val` is set to the largest value of `y` (where `2 * y` is less than or equal to `x`) found during the loop's execution. If no such `y` exists, `max_val` remains 1.
    return max_val
    #The program returns max_val which is set to the largest value of y where 2 * y is less than or equal to x, if no such y exists, max_val remains 1.
#Overall this is what the function does:The function accepts an integer \( x \) such that \( 2 \leq x \leq 1000 \). It returns the largest integer \( y \) that satisfies one of the following conditions:
1. \( y \) is a divisor of \( x \) and \( x > 1 \) and \( x \leq 2y \).
2. \( x \) is divisible by \( y-1 \) and \( 2(y-1) < x \).
3. \( y = x - 2 \) when \( x > 2 \).
If no such \( y \) exists, it returns 1.

