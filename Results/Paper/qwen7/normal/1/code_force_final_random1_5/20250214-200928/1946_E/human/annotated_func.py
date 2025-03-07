#State of the program right berfore the function call: a and b are positive integers where a >= b.
def func_1(a, b):
    if (b == 0) :
        return 1, 0
        #The program returns 1 and 0
    #State: a and b are positive integers where a >= b, and b is not equal to 0
    if (a < b) :
        c, d = func_1(b, a)
        return d, c
        #The program returns two values, 'd' and 'c', which are the return values of func_1(b, a)
    #State: a and b are positive integers where a >= b, and b is not equal to 0, and a is greater than or equal to b
    if (a % b == 0) :
        return 1, -(a // b - 1)
        #The program returns a tuple containing 1 and -(a // b - 1)
    #State: a and b are positive integers where a >= b, and b is not equal to 0, and a is not divisible by b
    c, d = func_1(b, a % b)
    return d, c - a // b * d
    #The program returns d, which is the second value returned by func_1(b, a % b), and c - a // b * d, where c is the first value returned by func_1(b, a % b)
#Overall this is what the function does:The function accepts two positive integers `a` and `b` where `a` is greater than or equal to `b`. It returns either a tuple `(1, 0)`, two values `d` and `c` from a recursive call, a tuple `(1, -(a // b - 1))`, or `d` and `c - a // b * d` from recursive calls.

#State of the program right berfore the function call: a is an integer, and b is a list of integers where the length of b is either equal to the number of prefix maximums (m_1) or the number of suffix maximums (m_2) from the problem description. Additionally, the elements of b are indices within the range [1, n].
def func_2(a, b):
    c, d = func_1(b, 1000000007)
    return c * a % 1000000007
    #The program returns the value of `c` multiplied by `a` modulo 1000000007.
#Overall this is what the function does:The function accepts an integer `a` and a list of integers `b`. It calls another function `func_1` with `b` and a large prime number `1000000007` as arguments. It then returns the result `c` from `func_1`, multiplied by `a` and taken modulo `1000000007`.

