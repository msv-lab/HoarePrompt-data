#State of the program right berfore the function call: a and b are integers such that b >= 0.
def func_1(a, b):
    if (b == 0) :
        return 1, 0
        #The program returns 1 and 0.
    #State: a and b are integers such that b > 0.
    if (a < b) :
        c, d = func_1(b, a)
        return d, c
        #The program returns `d` and `c`, which are the values returned by `func_1(b, a)`, where `a` is an integer less than `b` and `b` is a positive integer.
    #State: a and b are integers such that b > 0, and a is greater than or equal to b.
    if (a % b == 0) :
        return 1, -(a // b - 1)
        #The program returns 1 and a negative value that is one less than the result of integer division of `a` by `b`.
    #State: a and b are integers such that b > 0, a is greater than or equal to b, and a % b is not equal to 0
    c, d = func_1(b, a % b)
    return d, c - a // b * d
    #The program returns `d` and the result of `c - a // b * d`, where `c` and `d` are the values returned by `func_1(b, a % b)`.
#Overall this is what the function does:The function `func_1` accepts two integers `a` and `b` (where `b` is non-negative) and returns a pair of integers. Depending on the input conditions, the function can return one of the following pairs:
1. If `b` is 0, it returns (1, 0).
2. If `a` is less than `b` and `b` is positive, it returns the results of calling `func_1(b, a)` with the arguments swapped.
3. If `a` is greater than or equal to `b` and `a` is divisible by `b`, it returns (1, -(a // b - 1)).
4. If `a` is greater than or equal to `b` and `a` is not divisible by `b`, it returns `d` and `c - a // b * d`, where `c` and `d` are the results of calling `func_1(b, a % b)`.

#State of the program right berfore the function call: a is an integer, b is a list of integers, and the length of b is non-negative.
def func_2(a, b):
    c, d = func_1(b, 1000000007)
    return c * a % 1000000007
    #The program returns the result of `c * a % 1000000007`, where `c` is one of the values returned by `func_1(b, 1000000007)`, and `a` is an integer.
#Overall this is what the function does:The function `func_2` accepts an integer `a` and a list of integers `b`. It returns the result of multiplying `a` by a value `c` (where `c` is the first value returned by `func_1(b, 1000000007)`) and then taking the result modulo 1000000007. The function does not modify the input parameters `a` or `b`.

