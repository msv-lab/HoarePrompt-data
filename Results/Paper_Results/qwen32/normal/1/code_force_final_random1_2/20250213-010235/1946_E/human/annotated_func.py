#State of the program right berfore the function call: a and b are non-negative integers.
def func_1(a, b):
    if (b == 0) :
        return 1, 0
        #The program returns the tuple (1, 0)
    #State: a and b are non-negative integers, and b is not equal to 0
    if (a < b) :
        c, d = func_1(b, a)
        return d, c
        #The program returns the values `d` and `c` as returned by `func_1(b, a)`.
    #State: a and b are non-negative integers, b is not equal to 0, and a is greater than or equal to b
    if (a % b == 0) :
        return 1, -(a // b - 1)
        #The program returns (1, 1 - q) where q is the integer quotient of a divided by b.
    #State: a and b are non-negative integers, b is not equal to 0, a is greater than or equal to b, and a is not divisible by b
    c, d = func_1(b, a % b)
    return d, c - a // b * d
    #The program returns `d`, which is the remainder when `b` is divided by `(a % b)`, and `c - a // b * d`, where `c` is the quotient when `b` is divided by `(a % b)`
#Overall this is what the function does:The function `func_1` takes two non-negative integers `a` and `b` as input and returns a tuple of two integers. The function computes and returns the coefficients of Bézout's identity, which are the integers `x` and `y` such that `ax + by = gcd(a, b)`, where `gcd(a, b)` is the greatest common divisor of `a` and `b`.

#State of the program right berfore the function call: a and b are integers.
def func_2(a, b):
    c, d = func_1(b, 1000000007)
    return c * a % 1000000007
    #The program returns the value of (c * a) % 1000000007, where c and d are the values returned by func_1(b, 1000000007), and a and b are integers.
#Overall this is what the function does:The function `func_2` takes two integer parameters `a` and `b`. It computes the product of `a` and the first value returned by `func_1(b, 1000000007)`, then returns the result modulo 1000000007.

