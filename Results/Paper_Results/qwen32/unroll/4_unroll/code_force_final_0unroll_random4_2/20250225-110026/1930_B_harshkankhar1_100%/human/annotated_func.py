#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^3, and for each of the t test cases, n is an integer such that 3 <= n <= 10^5. The sum of all n across the test cases does not exceed 10^5.
def func_1():
    a = list(range(1, int(input()) + 1))
    a[::2] = a[::2][::-1]
    print(*a)
    #This is printed: the transformed list `a` where elements at even indices are reversed, and elements at odd indices remain the same
#Overall this is what the function does:The function `func_1` reads an integer `n` from the input, creates a list of integers from 1 to `n`, reverses the elements at even indices, and prints the transformed list. This process is repeated for `t` test cases, where `t` is specified before the function call.

