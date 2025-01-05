#State of the program right berfore the function call: n, x1, y1, x2, y2 are non-negative integers such that 1 ≤ n ≤ 1000 and 0 ≤ x1, y1, x2, y2 ≤ n.**
def func_1(x, y):
    if (y == 0) :
        return x
        #The program returns the value of x
    #State of the program after the if block has been executed: *n, x1, y1, x2, y2 are non-negative integers such that 1 ≤ n ≤ 1000 and 0 ≤ x1, y1, x2, y2 ≤ n. y is not equal to 0
    if (x == n) :
        return y + n
        #The program returns the sum of y and n, where n is a non-negative integer between 1 and 1000 inclusive, and y is a non-negative integer between 1 and n inclusive.
    #State of the program after the if block has been executed: *n, x1, y1, x2, y2 are non-negative integers such that 1 ≤ n ≤ 1000 and 0 ≤ x1, y1, x2, y2 ≤ n. y is not equal to 0. x is not equal to n
    if (y == n) :
        return n - x + n + n
        #The program returns 3n - x
    #State of the program after the if block has been executed: *n, x1, y1, x2, y2 are non-negative integers such that 1 ≤ n ≤ 1000 and 0 ≤ x1, y1, x2, y2 ≤ n. y is not equal to 0. x is not equal to n. y is not equal to n
    return n - y + n + n + n
    #The program returns 3n - y
#Overall this is what the function does:The function `func_1` accepts two non-negative integer parameters `x` and `y`. It returns different values based on the following cases:
Case 1: If `y` is 0, the function returns the value of `x`.
Case 2: If `x` is equal to a non-negative integer `n`, the function returns the sum of `y` and `n`, where `n` ranges from 1 to 1000 inclusive.
Case 3: If `y` is equal to a non-negative integer `n`, the function returns the value of 3n - x.
Case 4: If none of the above conditions are met, the function returns the value of 3n - y, where `n` is a non-negative integer between 1 and 1000 inclusive.

