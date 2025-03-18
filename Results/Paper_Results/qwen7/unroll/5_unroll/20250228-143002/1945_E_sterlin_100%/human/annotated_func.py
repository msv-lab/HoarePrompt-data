#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 2⋅10^4, n is an integer such that 1 ≤ n ≤ 2⋅10^5, x is an integer such that 1 ≤ x ≤ n, and p is a list of integers representing a permutation of length n.
def func_1():
    return int(input())
    #The program returns an integer input by the user.
#Overall this is what the function does:The function accepts no parameters and returns an integer input by the user.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 2⋅10^4. Each test case consists of n and x where 1 ≤ x ≤ n ≤ 2⋅10^5, and p is a list of n integers representing a permutation of numbers from 1 to n.
def func_2():
    return map(int, input().split())
    #The program returns a map object containing integers split from the input, where the input is two space-separated values: t and another value.
#Overall this is what the function does:The function reads two space-separated integers from the standard input, converts them to a map object, and returns this object. The first integer represents the number of test cases (t), and the second integer is an additional value associated with each test case.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 2⋅10^4, n is an integer such that 1 ≤ n ≤ 2⋅10^5, x is an integer such that 1 ≤ x ≤ n, and p is a list of n integers which is a permutation of [1, 2, ..., n].
def func_3():
    return list(map(int, input().split()))
    #The program returns a list of integers read from input, split by spaces.
#Overall this is what the function does:The function reads a list of integers from standard input, split by spaces, and returns this list.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 2⋅10^4. Each test case consists of two integers n and x such that 1 ≤ x ≤ n ≤ 2⋅10^5, and a permutation p of length n consisting of distinct integers from 1 to n.
def func_4():
    return input()
    #The program returns a string containing two integers separated by a space, followed by another string containing a permutation of distinct integers from 1 to n.
#Overall this is what the function does:The function processes an external set of inputs (t, n, x, p) where t is an integer between 1 and 20,000, n and x are integers between 1 and 200,000 with 1 ≤ x ≤ n, and p is a permutation of distinct integers from 1 to n. After processing, it returns a string containing two integers separated by a space, followed by another string containing a permutation of distinct integers from 1 to n.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 2⋅10^4, representing the number of test cases. Each test case consists of two integers n and x such that 1 ≤ x ≤ n ≤ 2⋅10^5, where n is the length of the permutation and x is the number to be found. The second line of each test case contains a list of integers p representing the permutation of length n.
def func_5():
    return input().split()
    #The program returns a list of strings representing the input for each test case. This list includes the number of test cases 't', followed by pairs of integers 'n' and 'x', and finally the permutation list 'p' for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `t` (number of test cases), pairs of integers `n` and `x`, and a permutation list `p`. It reads the input for these test cases and returns a list of strings, where each string represents the input for one test case. The returned list includes the number of test cases, followed by pairs of integers `n` and `x`, and the permutation list `p` for each test case.

