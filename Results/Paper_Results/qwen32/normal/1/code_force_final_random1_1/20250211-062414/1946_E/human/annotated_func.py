#State of the program right berfore the function call: a and b are non-negative integers.
def func_1(a, b):
    if (b == 0) :
        return 1, 0
        #The program returns the tuple (1, 0)
    #State: a and b are non-negative integers, and b is greater than 0
    if (a < b) :
        c, d = func_1(b, a)
        return d, c
        #The program returns the tuple (d, c), where d and c are the values returned by func_1(b, a)
    #State: a and b are non-negative integers, and b is greater than 0. Additionally, a is greater than or equal to b.
    if (a % b == 0) :
        return 1, -(a // b - 1)
        #The program returns (1, 1 - (a // b))
    #State: a and b are non-negative integers, and b is greater than 0. Additionally, a is greater than or equal to b. a is not divisible by b.
    c, d = func_1(b, a % b)
    return d, c - a // b * d
    #The program returns `d` and `c - (a // b) * d`, where `c` and `d` are the values returned by `func_1(b, a % b)`
#Overall this is what the function does:The function `func_1` accepts two non-negative integers `a` and `b`. It computes and returns a tuple `(x, y)` that represents the coefficients of Bézout's identity, i.e., `ax + by = gcd(a, b)`. Specifically, it returns `(1, 0)` if `b` is zero, and otherwise returns coefficients such that the linear combination of `a` and `b` equals their greatest common divisor (GCD).

#State of the program right berfore the function call: a and b are integers.
def func_2(a, b):
    c, d = func_1(b, 1000000007)
    return c * a % 1000000007
    #The program returns the value of (c * a) % 1000000007, where c and d are the values returned by func_1(b, 1000000007) and a is an integer.
#Overall this is what the function does:The function `func_2` takes two integer parameters `a` and `b`, computes a value using the first result from another function `func_1` called with `b` and a constant `1000000007`, and returns the result of multiplying this computed value by `a`, modulo `1000000007`.

