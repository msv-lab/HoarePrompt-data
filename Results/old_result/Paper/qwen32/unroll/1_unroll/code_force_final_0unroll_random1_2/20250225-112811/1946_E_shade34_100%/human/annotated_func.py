#State of the program right berfore the function call: a and b are integers.
def func_1(a, b):
    if (b == 0) :
        return 1, 0
        #The program returns the tuple (1, 0)
    #State: a and b are integers, and b is not equal to 0
    if (a < b) :
        c, d = func_1(b, a)
        return d, c
        #The program returns the values `d` and `c` which are the values returned by `func_1(b, a)` in that order.
    #State: a and b are integers, b is not equal to 0, and a is greater than or equal to b
    if (a % b == 0) :
        return 1, -(a // b - 1)
        #The program returns (1, -(a // b - 1)) where 'a' is an integer greater than or equal to 'b', and 'b' is a non-zero integer that divides 'a' without a remainder.
    #State: a and b are integers, b is not equal to 0, a is greater than or equal to b, and a is not divisible by b
    c, d = func_1(b, a % b)
    return d, c - a // b * d
    #The program returns `d` and `c - a // b * d`, where `c` and `d` are the values returned by `func_1(b, a % b)`.
#Overall this is what the function does:The function `func_1` takes two integer parameters `a` and `b` and returns a tuple of two integers. The returned tuple depends on the relationship between `a` and `b`. If `b` is zero, it returns `(1, 0)`. If `a` is less than `b`, it recursively calls itself with `b` and `a` swapped and returns the swapped result. If `a` is divisible by `b`, it returns `(1, -(a // b - 1))`. Otherwise, it recursively calls itself with `b` and `a % b`, and returns a tuple derived from the result of that call.

#State of the program right berfore the function call: a and b are integers, where b is used as an input to another function func_1 which returns a tuple (c, d), and c is then multiplied by a modulo 1000000007.
def func_2(a, b):
    c, d = func_1(b, 1000000007)
    return c * a % 1000000007
    #The program returns the value of `c * a % 1000000007`, where `c` is the first element of the tuple returned by `func_1(b, 1000000007)` and `a` is an integer.
#Overall this is what the function does:The function `func_2` takes two integer parameters, `a` and `b`. It computes a value `c` by calling `func_1` with `b` and `1000000007`, then returns the result of `(c * a) % 1000000007`.

