#State of the program right berfore the function call: a and b are positive integers where b is not zero.
def func_1(a, b):
    if (b == 0) :
        return 1, 0
        #The program returns a tuple containing 1 and 0
    #State: a and b are positive integers where b is not zero
    if (a < b) :
        c, d = func_1(b, a)
        return d, c
        #The program returns d and c, where c is the result of func_1(b, a) and d is the second return value of func_1(b, a)
    #State: a and b are positive integers where b is not zero, and a is greater than or equal to b
    if (a % b == 0) :
        return 1, -(a // b - 1)
        #The program returns 1 and -(a // b - 1)
    #State: a and b are positive integers where b is not zero, and a is greater than or equal to b, and a is not divisible by b
    c, d = func_1(b, a % b)
    return d, c - a // b * d
    #The program returns a tuple where the first element is the second return value from func_1(b, a % b), and the second element is the difference between c minus the floor division of a by b multiplied by the second return value from func_1(b, a % b)
#Overall this is what the function does:The function accepts two positive integers `a` and `b` (with `b` not being zero) and returns a tuple. Depending on the values of `a` and `b`, it can return one of four possible outcomes:
1. A tuple containing 1 and 0.
2. A tuple where the first element is the second return value from `func_1(b, a % b)` and the second element is the difference between `c` minus the floor division of `a` by `b` multiplied by the second return value from `func_1(b, a % b)`.
3. A tuple containing 1 and the negative of `(a // b - 1)`.
4. A tuple where the first element is the second return value from `func_1(b, a)` and the second element is `d`, where `c` and `d` are the results of `func_1(b, a)`.

#State of the program right berfore the function call: a is an integer, and b is a list of tuples where each tuple contains two integers (c, d) such that 1 ≤ c, d ≤ 10^9 + 6 and d ≠ 0.
def func_2(a, b):
    c, d = func_1(b, 1000000007)
    return c * a % 1000000007
    #The program returns the value of `c` multiplied by `a` modulo 1000000007.
#Overall this is what the function does:The function accepts an integer `a` and a list of tuples `b`, where each tuple contains two integers `(c, d)` within the range 1 to 10^9 + 6 (inclusive), and `d` is not zero. It then calls another function `func_1` with `b` and a large prime number (1000000007) as arguments. After obtaining the result `(c, d)` from `func_1`, it returns the product of `c` and `a` modulo 1000000007.

