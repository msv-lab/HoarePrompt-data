#State of the program right berfore the function call: n is an integer such that 3 ≤ n ≤ 10^5.
def func_1():
    a = list(range(1, int(input()) + 1))
    a[::2] = a[::2][::-1]
    print(a)
    #This is printed: [2, 1, 4, 3, 5, ..., n-1, n-2, n] (where the elements at even indices are swapped with the elements at the next odd indices, and the last element remains unchanged if `n` is odd)
#Overall this is what the function does:The function `func_1` does not accept any parameters. It reads an integer `n` from user input, where `3 ≤ n ≤ 10^5`, and creates a list `a` containing integers from 1 to `n`. It then reverses the elements at even indices (0, 2, 4, ...) and prints the modified list. The final state of the program is that the list `a` is printed, where the elements at even indices are swapped with the elements at the next odd indices, and the last element remains unchanged if `n` is odd.

