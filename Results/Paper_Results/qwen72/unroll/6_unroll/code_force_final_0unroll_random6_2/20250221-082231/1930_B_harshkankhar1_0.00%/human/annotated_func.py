#State of the program right berfore the function call: n is an integer such that 3 ≤ n ≤ 10^5.
def func_1():
    a = list(range(1, int(input()) + 1))
    a[::2] = a[::2][::-1]
    print(a)
    #This is printed: [n, 2, n-2, 4, n-4, 6, ..., 1] (where n is the value of `n` and the list is structured such that elements at even indices are in reverse order while elements at odd indices remain in their original positions)
#Overall this is what the function does:The function `func_1` does not accept any parameters. It reads an integer `n` from user input, where `3 ≤ n ≤ 10^5`, and creates a list `a` containing integers from 1 to `n`. It then reverses the elements at even indices (0, 2, 4, ...) of the list while keeping the elements at odd indices (1, 3, 5, ...) in their original positions. Finally, it prints the modified list. The function does not return any value. After the function concludes, the list `a` is printed in a format where elements at even indices are in reverse order, and elements at odd indices remain in their original positions.

