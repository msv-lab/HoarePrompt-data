#State of the program right berfore the function call: a and b are non-negative integers, with a >= b > 0.
def func_1(a, b):
    if (b == 0) :
        return 1, 0
        #The program returns 1 and 0
    #State: a and b are non-negative integers, with a >= b > 0, and b is not equal to 0
    if (a < b) :
        c, d = func_1(b, a)
        return d, c
        #The program returns d and c, where c is the return value of func_1(b, a), and d is the second return value of func_1(b, a)
    #State: a and b are non-negative integers, with a >= b > 0, and b is not equal to 0, and a is greater than or equal to b
    if (a % b == 0) :
        return 1, -(a // b - 1)
        #The program returns 1 and -(a // b - 1)
    #State: a and b are non-negative integers, with a >= b > 0, b is not equal to 0, and a is not divisible by b
    c, d = func_1(b, a % b)
    return d, c - a // b * d
    #The program returns the remainder of b divided by (a % b) and the difference between c and the floor division of a by b multiplied by the remainder of b divided by (a % b)
#Overall this is what the function does:The function accepts two non-negative integers `a` and `b` with `a >= b > 0`. It returns either 1 and 0, or values `d` and `c` based on recursive calls, or 1 and a specific integer, or a pair of integers derived from the Euclidean algorithm.

#State of the program right berfore the function call: a is an integer, and b is a list of integers where the length of b is equal to the number of test cases. Each element in b is a tuple (m1, m2, n) representing the length of the permutation, the number of prefix maximums, and the number of suffix maximums, respectively. Additionally, m1, m2, and n satisfy the constraints 1 ≤ m1, m2, n ≤ 2⋅10^5 and the sum of n across all test cases does not exceed 2⋅10^5.
def func_2(a, b):
    c, d = func_1(b, 1000000007)
    return c * a % 1000000007
    #The program returns the value of `c` multiplied by `a` and then taken modulo 1000000007.
#Overall this is what the function does:The function accepts an integer `a` and a list of tuples `b`. Each tuple in `b` contains three integers representing the length of a permutation, the number of prefix maximums, and the number of suffix maximums. The function calls another function `func_1` with `b` and a prime number `1000000007` as arguments. It then returns the product of the result `c` from `func_1` and `a`, modulo `1000000007`.

