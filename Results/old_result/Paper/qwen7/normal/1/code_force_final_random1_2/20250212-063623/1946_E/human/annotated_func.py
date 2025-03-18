#State of the program right berfore the function call: a and b are positive integers.
def func_1(a, b):
    if (b == 0) :
        return 1, 0
        #The program returns 1 and 0
    #State: a and b are positive integers, and b is not equal to 0
    if (a < b) :
        c, d = func_1(b, a)
        return d, c
        #The program returns d and c, where d is the result of func_1(b, a) with b as the first argument, and c is the result of func_1(b, a) with a as the second argument.
    #State: a and b are positive integers, and b is not equal to 0, and a is greater than or equal to b
    if (a % b == 0) :
        return 1, -(a // b - 1)
        #The program returns 1 and -(a // b - 1)
    #State: a and b are positive integers, b is not equal to 0, a is greater than or equal to b, and (a % b != 0)
    c, d = func_1(b, a % b)
    return d, c - a // b * d
    #The program returns the tuple (d, c - a // b * d)
#Overall this is what the function does:The function accepts two positive integer parameters `a` and `b`. It returns a tuple. Depending on the values of `a` and `b`, it can return one of the following: (1, 0), (d, c) where `d` and `c` are results from recursive calls, (1, -(a // b - 1)), or (d, c - a // b * d).

#State of the program right berfore the function call: a is an integer, b is a list of integers where the length of b is equal to the number of test cases, and each element of b is a tuple (m1, m2, n) representing the length of the permutation, the number of prefix maximums, the number of suffix maximums, and the number of test cases respectively.
def func_2(a, b):
    c, d = func_1(b, 1000000007)
    return c * a % 1000000007
    #The program returns the value of `c` multiplied by `a` and then taken modulo 1000000007.
#Overall this is what the function does:The function accepts an integer `a` and a list `b` of tuples, each containing four integers. It calls another function `func_1` with `b` and a large prime number `1000000007`. It then returns the product of the result `c` from `func_1` and `a`, modulo `1000000007`.

