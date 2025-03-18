#State of the program right berfore the function call: a and b are non-negative integers such that a >= b and b >= 0.
def func_1(a, b):
    if (b == 0) :
        return 1, 0
        #The program returns the tuple (1, 0)
    #State: a and b are non-negative integers such that a >= b and b >= 0, and b is not equal to 0.
    if (a < b) :
        c, d = func_1(b, a)
        return d, c
        #The program returns the values of `d` and `c` as they were returned by the function `func_1(b, a)`, where `a` and `b` are non-negative integers with `a` being less than `b`, and `b` is not equal to 0.
    #State: a and b are non-negative integers such that a >= b and b >= 0, and b is not equal to 0. Additionally, a is greater than or equal to b.
    if (a % b == 0) :
        return 1, -(a // b - 1)
        #The program returns a tuple (1, -(a // b - 1)), where the first element is 1 and the second element is the negative of the quotient of a divided by b, minus 1.
    #State: a and b are non-negative integers such that a >= b and b >= 0, and b is not equal to 0. Additionally, a is greater than or equal to b, and a is not divisible by b.
    c, d = func_1(b, a % b)
    return d, c - a // b * d
    #The program returns a tuple `(d, c - a // b * d)` where `d` and `c` are the values returned by `func_1(b, a % b)`. `d` is the second value returned by `func_1`, and `c - a // b * d` is calculated by subtracting the product of the integer division of `a` by `b` and `d` from `c`.
#Overall this is what the function does:The function `func_1` accepts two non-negative integers `a` and `b` where `a` is greater than or equal to `b` and `b` is greater than or equal to 0. It returns a tuple `(x, y)` based on the following conditions:
1. If `b` is 0, the function returns `(1, 0)`.
2. If `a` is less than `b` and `b` is not 0, the function returns the values of `d` and `c` as they were returned by the function `func_1(b, a)`, swapping their positions.
3. If `a` is greater than or equal to `b` and `a` is divisible by `b`, the function returns `(1, -(a // b - 1))`.
4. If `a` is greater than or equal to `b` and `a` is not divisible by `b`, the function returns `(d, c - a // b * d)`, where `d` and `c` are the values returned by `func_1(b, a % b)`.

#State of the program right berfore the function call: a is an integer, b is a list of integers, and the length of b is at least 1.
def func_2(a, b):
    c, d = func_1(b, 1000000007)
    return c * a % 1000000007
    #The program returns the result of (c * a) % 1000000007, where `c` is a value returned by `func_1(b, 1000000007)`, `a` is an integer, and `b` is a list of integers.
#Overall this is what the function does:The function `func_2` accepts an integer `a` and a list of integers `b` (with a minimum length of 1). It returns the result of `(c * a) % 1000000007`, where `c` is a value obtained from calling `func_1(b, 1000000007)`. The function does not modify the input parameters `a` or `b`.

