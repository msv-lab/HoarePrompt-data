#State of the program right berfore the function call: n is an integer such that 3 <= n <= 10^5.
def func_1():
    a = list(range(1, int(input()) + 1))
    a[::2] = a[::2][::-1]
    print(*a)
    #This is printed: [n, 2, n-2, 3, n-4, 4, ..., 1] (where the elements at even indices are reversed in the list `a` from 1 to `n`)
#Overall this is what the function does:The function `func_1` does not accept any parameters. It reads an integer `n` from user input where 3 <= n <= 10^5, creates a list `a` containing integers from 1 to `n`, reverses the elements at even indices (0, 2, 4, ...) of the list, and prints the modified list. The final state of the program after the function concludes is that the list `a` is printed in the format [n, 2, n-2, 3, n-4, 4, ..., 1] where the elements at even indices are reversed.

