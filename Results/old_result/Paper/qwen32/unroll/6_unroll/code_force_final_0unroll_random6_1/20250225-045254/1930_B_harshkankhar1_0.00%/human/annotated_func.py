#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^3, and for each test case, n is an integer such that 3 <= n <= 10^5. The sum of all n across all test cases does not exceed 10^5.
def func_1():
    a = list(range(1, int(input()) + 1))
    a[::2] = a[::2][::-1]
    print(a)
    #This is printed: a (where a is the list of integers from 1 to n with elements at even indices reversed)
#Overall this is what the function does:The function `func_1` reads an integer `n` from the input, creates a list of integers from 1 to `n`, reverses the elements at even indices, and prints the modified list. This process is repeated for multiple test cases, with the constraint that the sum of all `n` across all test cases does not exceed 10^5.

