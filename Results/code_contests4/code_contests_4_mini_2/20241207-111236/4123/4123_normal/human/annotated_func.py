#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 1000, and x1, y1, x2, y2 are integers representing coordinates on the sides of a square with vertices at (0, 0), (n, 0), (0, n), and (n, n), satisfying 0 ≤ x1, y1, x2, y2 ≤ n.
def func_1(x, y):
    if (y == 0) :
        return x
        #The program returns the value of x, which is an integer representing the x-coordinate on the side of the square.
    #State of the program after the if block has been executed: *n is a positive integer such that 1 ≤ n ≤ 1000, and x1, y1, x2, y2 are integers representing coordinates on the sides of a square with vertices at (0, 0), (n, 0), (0, n), and (n, n), satisfying 0 ≤ x1, y1, x2, y2 ≤ n. The value of y is greater than 0.
    if (x == n) :
        return y + n
        #The program returns y that is greater than 0 plus n, where n is a positive integer between 1 and 1000.
    #State of the program after the if block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 1000, and `x1`, `y1`, `x2`, `y2` are integers representing coordinates on the sides of a square with vertices at (0, 0), (n, 0), (0, n), and (n, n), satisfying 0 ≤ `x1`, `y1`, `x2`, `y2` ≤ `n`. The value of `y` is greater than 0, and `x` is less than `n`.
    if (y == n) :
        return n - x + n + n
        #The program returns the value of n minus x plus 3n, where n is a positive integer between 1 and 1000, and x is less than n
    #State of the program after the if block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 1000, and `x1`, `y1`, `x2`, `y2` are integers representing coordinates on the sides of a square with vertices at (0, 0), (n, 0), (0, n), and (n, n), satisfying 0 ≤ `x1`, `y1`, `x2`, `y2` ≤ `n`. The value of `y` is greater than 0, `x` is less than `n`, and `y` is less than `n`.
    return n - y + n + n + n
    #The program returns n - y + 3n, where n is a positive integer between 1 and 1000, and y is greater than 0 and less than n.
#Overall this is what the function does:The function accepts two integer parameters, `x` and `y`, which represent coordinates on the sides of a square with a defined size `n`. It returns `x` if `y` is 0; if `x` equals `n`, it returns `y + n`; if `y` equals `n`, it returns `n - x + 3n`; otherwise, it returns `n - y + 3n`. The function does not handle cases where `x` or `y` are outside the specified range of 0 to `n`, which could lead to unexpected results.

