#State of the program right berfore the function call: n is an integer between 1 and 1000, and x1, y1, x2, y2 are integers such that 0 <= x1, y1, x2, y2 <= n, representing coordinates on the sides of a square with side length n.
def func_1(x, y):
    if (y == 0) :
        return x
        #The program returns the value of x, which is an integer representing one of the coordinates on the sides of a square with side length n.
    #State of the program after the if block has been executed: *`n` is an integer between 1 and 1000, and `x1`, `y1`, `x2`, `y2` are integers such that 0 <= `x1`, `y1`, `x2`, `y2` <= `n`. The value of `y` is not equal to 0.
    if (x == n) :
        return y + n
        #The program returns the value of y, which is not equal to 0, added to the integer n that is between 1 and 1000.
    #State of the program after the if block has been executed: *`n` is an integer between 1 and 1000, and `x1`, `y1`, `x2`, `y2` are integers such that 0 <= `x1`, `y1`, `x2`, `y2` <= `n`. The value of `y` is not equal to 0. The value of `x` is not equal to `n`.
    if (y == n) :
        return n - x + n + n
        #The program returns the result of the expression n - x + n + n, where n is an integer between 1 and 1000 and x is not equal to n.
    #State of the program after the if block has been executed: *`n` is an integer between 1 and 1000, and `x1`, `y1`, `x2`, `y2` are integers such that 0 <= `x1`, `y1`, `x2`, `y2` <= `n`. The value of `y` is not equal to 0, the value of `x` is not equal to `n`, and the value of `y` is not equal to `n`.
    return n - y + n + n + n
    #The program returns 3n - y, where n is an integer between 1 and 1000 and y is not equal to 0.
#Overall this is what the function does:The function accepts two integer parameters, x and y, which represent coordinates on a square with side length n (where n is between 1 and 1000). It returns x if y is 0; if x equals n, it returns y + n; if y equals n, it returns 3n - x; otherwise, it returns 3n - y. The function does not handle cases where both x and y are equal to n, as it will default to the last return statement.

