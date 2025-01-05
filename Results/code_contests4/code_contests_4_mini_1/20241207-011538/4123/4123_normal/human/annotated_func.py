#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 1000, and x1, y1, x2, y2 are non-negative integers such that 0 ≤ x1, y1, x2, y2 ≤ n, representing coordinates of points on the sides of a square.
def func_1(x, y):
    if (y == 0) :
        return x
        #The program returns the value of x, which is a non-negative integer between 0 and n
    #State of the program after the if block has been executed: *`n` is a positive integer such that 1 ≤ n ≤ 1000, and `x1`, `y1`, `x2`, `y2` are non-negative integers such that 0 ≤ `x1`, `y1`, `x2`, `y2` ≤ `n`, representing coordinates of points on the sides of a square. The value of `y` is greater than 0.
    if (x == n) :
        return y + n
        #The program returns the value of y, which is greater than 0, added to the positive integer n, which is between 1 and 1000
    #State of the program after the if block has been executed: *`n` is a positive integer such that 1 ≤ n ≤ 1000, and `x1`, `y1`, `x2`, `y2` are non-negative integers such that 0 ≤ `x1`, `y1`, `x2`, `y2` ≤ `n`, representing coordinates of points on the sides of a square. The value of `y` is greater than 0, and `x` is less than n.
    if (y == n) :
        return n - x + n + n
        #The program returns the value calculated as n - x + n + n, where n is a positive integer between 1 and 1000, y is equal to n and greater than 0, and x is less than n.
    #State of the program after the if block has been executed: *`n` is a positive integer such that 1 ≤ n ≤ 1000, and `x1`, `y1`, `x2`, `y2` are non-negative integers such that 0 ≤ `x1`, `y1`, `x2`, `y2` ≤ `n`, representing coordinates of points on the sides of a square. The value of `y` is greater than 0, `x` is less than `n`, and `y` is less than `n`.
    return n - y + n + n + n
    #The program returns 3n - y, where n is a positive integer between 1 and 1000 and y is a non-negative integer greater than 0 and less than n
#Overall this is what the function does:The function accepts two non-negative integer parameters `x` and `y`, where `x` is between 0 and `n` and `y` is between 0 and `n`, with `n` being a positive integer between 1 and 1000. It returns `x` if `y` is 0, `y + n` if `x` is equal to `n`, `n - x + 3n` if `y` is equal to `n`, and `3n - y` in all other cases, where `y` is greater than 0 and less than `n`. The function does not handle cases where `y` is equal to 0 and `x` is equal to `n` simultaneously, which may lead to unexpected behavior.

