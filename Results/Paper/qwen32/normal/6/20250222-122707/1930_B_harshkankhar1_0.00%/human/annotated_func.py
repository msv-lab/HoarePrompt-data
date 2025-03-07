#State of the program right berfore the function call: Each test case contains a single integer n (3 ≤ n ≤ 10^5) representing the length of the permutation p. The first line of the input contains a single integer t (1 ≤ t ≤ 10^3) indicating the number of test cases. The sum of n over all test cases does not exceed 10^5.
def func_1():
    a = list(range(1, int(input()) + 1))
    a[::2] = a[::2][::-1]
    print(a)
    #This is printed: a (where a is the list of integers from 1 to n with elements at even indices reversed)
#Overall this is what the function does:The function `func_1` processes multiple test cases, each defined by an integer `n` (3 ≤ n ≤ 10^5). For each test case, it creates a list of integers from 1 to `n`, reverses the elements at even indices, and prints the modified list. The first line of the input specifies the number of test cases `t` (1 ≤ t ≤ 10^3). The sum of `n` across all test cases does not exceed 10^5.

