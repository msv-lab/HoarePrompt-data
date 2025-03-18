#State of the program right berfore the function call: a and b are non-negative integers.
def func_1(a, b):
    if (b == 0) :
        return 1, 0
        #The program returns the tuple (1, 0)
    #State: a and b are non-negative integers, and b is not equal to 0
    if (a < b) :
        c, d = func_1(b, a)
        return d, c
        #The program returns a tuple where the first element is the remainder of `b` divided by `a` (which is `d`), and the second element is the quotient of `b` divided by `a` (which is `c`).
    #State: `a` and `b` are non-negative integers, `b` is not equal to 0, and `a` is greater than or equal to `b`
    if (a % b == 0) :
        return 1, -(a // b - 1)
        #The program returns the tuple (1, -(a // b - 1)), where 'a' is divisible by 'b' and 'a' is greater than or equal to 'b'.
    #State: `a` and `b` are non-negative integers, `b` is not equal to 0, `a` is greater than or equal to `b`, and `a` is not divisible by `b`
    c, d = func_1(b, a % b)
    return d, c - a // b * d
    #The program returns `d` and `c - a // b * d`, where `c` and `d` are the values returned by `func_1(b, a % b)`
#Overall this is what the function does:The function `func_1` accepts two non-negative integers `a` and `b` and returns a tuple. Depending on the values of `a` and `b`, the function returns either (1, 0) if `b` is 0, or a tuple representing the coefficients of Bézout's identity for `a` and `b`. Specifically, it returns a tuple `(x, y)` such that `ax + by = gcd(a, b)`, where `gcd(a, b)` is the greatest common divisor of `a` and `b`.

#State of the program right berfore the function call: a and b are integers.
def func_2(a, b):
    c, d = func_1(b, 1000000007)
    return c * a % 1000000007
    #The program returns the value of `c * a % 1000000007`, where `c` is the first value returned by `func_1(b, 1000000007)` and `a` is an integer.
#Overall this is what the function does:The function `func_2` takes two integer parameters `a` and `b`. It computes a value by multiplying `a` with the first value returned from `func_1(b, 1000000007)` and then takes the result modulo 1000000007. The function returns this computed value.

