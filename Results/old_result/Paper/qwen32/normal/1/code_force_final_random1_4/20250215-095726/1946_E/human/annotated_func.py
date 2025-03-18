#State of the program right berfore the function call: a and b are non-negative integers.
def func_1(a, b):
    if (b == 0) :
        return 1, 0
        #The program returns the tuple (1, 0)
    #State: a and b are non-negative integers, and b is greater than 0
    if (a < b) :
        c, d = func_1(b, a)
        return d, c
        #The program returns the values `d` and `c`, which are the results of `func_1(b, a)` in that order.
    #State: a and b are non-negative integers, b is greater than 0, and a is greater than or equal to b
    if (a % b == 0) :
        return 1, -(a // b - 1)
        #The program returns (1, -(a // b - 1))
    #State: a and b are non-negative integers, b is greater than 0, a is greater than or equal to b, and a is not divisible by b
    c, d = func_1(b, a % b)
    return d, c - a // b * d
    #The program returns (d, c - a // b * d)
#Overall this is what the function does:The function `func_1` takes two non-negative integers `a` and `b` as input and returns a tuple of two integers. Depending on the values of `a` and `b`, the function returns either `(1, 0)` if `b` is zero, or computes a result based on the Euclidean algorithm, ultimately returning a tuple that represents the coefficients of Bézout's identity for `a` and `b`.

#State of the program right berfore the function call: a and b are integers.
def func_2(a, b):
    c, d = func_1(b, 1000000007)
    return c * a % 1000000007
    #The program returns the result of (c * a) % 1000000007, where c and a are integers and c is the first value returned by func_1(b, 1000000007)
#Overall this is what the function does:The function `func_2` takes two integer parameters `a` and `b`. It computes the product of `a` and the first value `c` returned by `func_1(b, 1000000007)`, then returns this product modulo 1000000007.

