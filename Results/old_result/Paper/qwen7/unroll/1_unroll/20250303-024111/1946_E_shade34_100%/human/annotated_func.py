#State of the program right berfore the function call: a and b are positive integers such that a >= b and gcd(a, b) = 1.
def func_1(a, b):
    if (b == 0) :
        return 1, 0
        #The program returns 1 and 0
    #State: a and b are positive integers such that a >= b and gcd(a, b) = 1, and b is not equal to 0
    if (a < b) :
        c, d = func_1(b, a)
        return d, c
        #d and c, where c and d are returned from func_1(b, a)
    #State: a and b are positive integers such that a >= b, gcd(a, b) = 1, and b is not equal to 0, and a is greater than or equal to b
    if (a % b == 0) :
        return 1, -(a // b - 1)
        #The program returns 1 and -(a // b - 1)
    #State: a and b are positive integers such that a >= b, gcd(a, b) = 1, and b is not equal to 0, and a is not divisible by b
    c, d = func_1(b, a % b)
    return d, c - a // b * d
    #The program returns d and c - a // b * d, where d and c are the results of the function call func_1(b, a % b), gcd(a, b) = 1, a >= b, and both a and b are positive integers.
#Overall this is what the function does:The function `func_1` accepts two parameters `a` and `b`, where `a` and `b` are positive integers such that `a >= b` and gcd(`a`, `b`) = 1. It returns either 1 and 0, or d and c (where c and d are the results of calling `func_1(b, a)`), or 1 and -(a // b - 1), or d and c - a // b * d (where d and c are the results of the function call `func_1(b, a % b)`).

#State of the program right berfore the function call: a is an integer, b is a list of integers where the length of b is either equal to the number of prefix maximums (m_1) or the number of suffix maximums (m_2), and 1000000007 is a constant integer representing \(10^9 + 7\).
def func_2(a, b):
    c, d = func_1(b, 1000000007)
    return c * a % 1000000007
    #The program returns the value of `c` multiplied by `a` modulo 1000000007.
#Overall this is what the function does:The function accepts an integer `a` and a list of integers `b`. It calls another function `func_1` with `b` and a constant integer \(10^9 + 7\) as arguments to get values for `c` and `d`. Finally, it returns the value of `c` multiplied by `a` modulo \(10^9 + 7\).

