#State of the program right berfore the function call: a and b are non-negative integers.
def func_1(a, b):
    if (b == 0) :
        return 1, 0
        #The program returns the tuple (1, 0)
    #State: a and b are non-negative integers, and b is not equal to 0
    if (a < b) :
        c, d = func_1(b, a)
        return d, c
        #The program returns the values `d` and `c` which are the values returned by `func_1(b, a)` in that order.
    #State: a and b are non-negative integers, b is not equal to 0, and a is greater than or equal to b
    if (a % b == 0) :
        return 1, -(a // b - 1)
        #The program returns the tuple (1, -(a // b - 1)), where a // b is the integer division of a by b.
    #State: a and b are non-negative integers, b is not equal to 0, a is greater than or equal to b, and a is not divisible by b
    c, d = func_1(b, a % b)
    return d, c - a // b * d
    #The program returns (d, c - a // b * d), where d is b and c is a % b.
#Overall this is what the function does:The function `func_1` accepts two non-negative integer parameters `a` and `b`. It returns a tuple of two integers based on the relationship between `a` and `b`. Specifically, it calculates and returns the coefficients (x, y) such that `a*x + b*y = gcd(a, b)`, where `gcd(a, b)` is the greatest common divisor of `a` and `b`.

#State of the program right berfore the function call: a and b are integers.
def func_2(a, b):
    c, d = func_1(b, 1000000007)
    return c * a % 1000000007
    #The program returns the value of \( c \times a \mod 1000000007 \), where \( c \) and \( d \) are the values returned by `func_1(b, 1000000007)` and \( a \) is an integer.
#Overall this is what the function does:The function `func_2` takes two integer parameters `a` and `b`. It computes the value of \( c \times a \mod 1000000007 \), where \( c \) is the first value returned by `func_1(b, 1000000007)`, and returns this computed value.

