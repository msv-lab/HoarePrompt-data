#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^3, and for each test case, n is an integer such that 3 <= n <= 10^5. The sum of n over all test cases does not exceed 10^5.
def func_1():
    a = list(range(1, int(input()) + 1))
    a[::2] = a[::2][::-1]
    print(a)
    #This is printed: a (where elements at even indices are reversed compared to their original order, while elements at odd indices remain unchanged)
#Overall this is what the function does:The function `func_1` reads an integer `n` from the input, creates a list `a` containing integers from 1 to `n`, reverses the elements at even indices of this list, and prints the modified list. This process is repeated for multiple test cases, with the total number of test cases not exceeding 1000 and the sum of all `n` values across all test cases not exceeding 100,000.

