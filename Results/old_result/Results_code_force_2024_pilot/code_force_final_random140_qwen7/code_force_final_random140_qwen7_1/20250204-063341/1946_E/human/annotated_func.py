#State of the program right berfore the function call: a and b are non-negative integers where b is non-zero (b > 0).
def func_1(a, b):
    if (b == 0) :
        return 1, 0
        #The program returns a tuple containing 1 and 0
    #State: a and b are non-negative integers where b is non-zero (b > 0)
    if (a < b) :
        c, d = func_1(b, a)
        return d, c
        #The program returns the second return value of func_1(b, a) and the result of func_1(b, a)
    #State: a and b are non-negative integers where b is non-zero (b > 0), and a is greater than or equal to b
    if (a % b == 0) :
        return 1, -(a // b - 1)
        #The program returns 1 and -1
    #State: a and b are non-negative integers where b is non-zero (b > 0), and a is greater than or equal to b, and a is not divisible by b
    c, d = func_1(b, a % b)
    return d, c - a // b * d
    #The program returns the tuple (d, c - a // b * d), where `d` is the result of `func_1(b, a % b)`, `c` is `a % b`, and `a` is not divisible by `b`.
#Overall this is what the function does:The function accepts two parameters, `a` and `b`, where both are non-negative integers and `b` is non-zero. It returns one of four possible tuples: (1, 0), (the second return value of `func_1(b, a)` and the result of `func_1(b, a)`), (1, -1), or (d, c - a // b * d), where `d` is the result of `func_1(b, a % b)` and `c` is `a % b` when `a` is not divisible by `b`.

#State of the program right berfore the function call: a is an integer, and b is a list of integers representing the indices of prefix maximums and suffix maximums. The length of b is equal to the sum of the number of prefix maximums and suffix maximums for the given permutation problem.
def func_2(a, b):
    c, d = func_1(b, 1000000007)
    return c * a % 1000000007
    #The program returns the value of c multiplied by a, modulo 1000000007.
#Overall this is what the function does:The function accepts two parameters: an integer `a` and a list of integers `b`. The list `b` represents the indices of prefix maximums and suffix maximums in a permutation problem. The function calls another function `func_1` with `b` and a large prime number `1000000007`. It then returns the product of the result `c` from `func_1` and `a`, modulo `1000000007`.

