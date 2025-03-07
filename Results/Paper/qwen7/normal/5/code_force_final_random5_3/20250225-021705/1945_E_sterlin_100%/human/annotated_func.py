#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 2⋅10^4, n is an integer such that 1 ≤ n ≤ 2⋅10^5, x is an integer such that 1 ≤ x ≤ n, and the input consists of t test cases where each test case starts with two integers n and x followed by a permutation of integers from 1 to n.
def func_1():
    return int(input())
    #The program returns an integer input provided by the user, which is part of a test case consisting of two integers n and x followed by a permutation of integers from 1 to n.
#Overall this is what the function does:The function processes input data consisting of multiple test cases. Each test case includes two integers \( n \) and \( x \), followed by a permutation of integers from 1 to \( n \). The function reads an integer input from the user, which is part of one of these test cases, and returns this integer.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 2⋅10^4. Each test case consists of two integers n and x such that 1 ≤ x ≤ n ≤ 2⋅10^5, and a permutation p of length n consisting of distinct integers from 1 to n.
def func_2():
    return map(int, input().split())
    #The program returns a map object containing two integers, which are the values of variables 'n' and 'x' separated by a space, converted to integers.
#Overall this is what the function does:The function reads a line of input, splits it into two integers 'n' and 'x', converts them to integer type, and returns a map object containing these two integers. This function effectively processes a single test case by extracting and preparing the values of 'n' and 'x' for further use.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 2⋅10^4. Each test case consists of two integers n and x such that 1 ≤ x ≤ n ≤ 2⋅10^5, and a permutation p of size n consisting of distinct integers from 1 to n.
def func_3():
    return list(map(int, input().split()))
    #The program returns a list of two integers, where the first integer is 'x' and the second integer is 'n', obtained from user input.
#Overall this is what the function does:The function reads two integers from user input and returns them as a list, where the first element is 'x' and the second element is 'n'.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 2⋅10^4, each test case consists of n (1 ≤ n ≤ 2⋅10^5) and x (1 ≤ x ≤ n), and p is a list of n integers representing a permutation of size n.
def func_4():
    return input()
    #The program returns input from the user
#Overall this is what the function does:The function accepts no parameters and returns input from the user.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 2⋅10^4, representing the number of test cases. Each test case consists of two integers n and x such that 1 ≤ x ≤ n ≤ 2⋅10^5, where n is the length of the permutation and x is the number to be found. The second line of each test case contains a list of integers p representing the permutation of length n.
def func_5():
    return input().split()
    #The program returns a list of strings containing the values of t, n, and x for each test case.
#Overall this is what the function does:The function reads input from the standard input, processes multiple test cases, and returns a list of strings. Each string in the list contains the values of `t`, `n`, and `x` for each test case. The function does not accept any parameters and directly processes the input provided through the standard input.

