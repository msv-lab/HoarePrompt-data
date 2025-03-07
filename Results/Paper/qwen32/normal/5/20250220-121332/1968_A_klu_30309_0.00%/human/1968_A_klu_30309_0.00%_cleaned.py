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
    return max_val
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        x = int(input())
        y = func_1(x)
        print(y)