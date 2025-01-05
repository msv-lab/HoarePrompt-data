#State of the program right berfore the function call: n is a positive integer representing the side length of the square, x1, y1, x2, y2 are non-negative integers such that 0 <= x1, y1, x2, y2 <= n.**
def func_1(x, y):
    if (y == 0) :
        return x
        #The program returns the value of 'x' which is a non-negative integer
    #State of the program after the if block has been executed: *n is a positive integer representing the side length of the square, x1, y1, x2, y2 are non-negative integers such that 0 <= x1, y1, x2, y2 <= n. (y != 0)
    if (x == n) :
        return y + n
        #The program returns the sum of y and n, where n is a positive integer representing the side length of a square, and y is a non-negative integer such that 0 <= y <= n.
    #State of the program after the if block has been executed: *n is a positive integer representing the side length of the square, x1, y1, x2, y2 are non-negative integers such that 0 <= x1, y1, x2, y2 <= n. (y != 0). x is not equal to n
    if (y == n) :
        return n - x + n + n
        #The program returns 2n - x
    #State of the program after the if block has been executed: *n is a positive integer representing the side length of the square, x1, y1, x2, y2 are non-negative integers such that 0 <= x1, y1, x2, y2 <= n. (y != 0). x is not equal to n. y is not equal to n
    return n - y + n + n + n
    #The program returns 3n - y
#Overall this is what the function does:The function `func_1` accepts two non-negative integers `x` and `y`. It then checks various conditions based on the values of `x`, `y`, and a positive integer `n` representing the side length of a square. The function returns different values depending on these conditions:
- If `y` is 0, it returns the value of `x`.
- If `x` is equal to `n`, it returns the sum of `y` and `n`.
- If `y` is equal to `n`, it returns `2n - x`.
- Otherwise, it returns `3n - y`.
Therefore, the functionality of the function is to perform calculations based on the input parameters and return specific values according to the conditions specified in the code.

