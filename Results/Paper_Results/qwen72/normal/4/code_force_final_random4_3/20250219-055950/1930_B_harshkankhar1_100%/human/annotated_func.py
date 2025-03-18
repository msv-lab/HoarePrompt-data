#State of the program right berfore the function call: n is an integer such that 3 <= n <= 10^5.
def func_1():
    a = list(range(1, int(input()) + 1))
    a[::2] = a[::2][::-1]
    print(*a)
    #This is printed: - The `print(*a)` statement will print the elements of the list `a` separated by spaces.
    #
    #Let's illustrate this with a few examples:
    #
    #- If `n = 3`, the initial list `a` is `[1, 2, 3]`. Reversing the odd-indexed elements results in `[1, 2, 3]` (since there's only one odd-indexed element, it remains the same).
    #- If `n = 4`, the initial list `a` is `[1, 2, 3, 4]`. Reversing the odd-indexed elements results in `[1, 4, 3, 2]`.
    #- If `n = 5`, the initial list `a` is `[1, 2, 3, 4, 5]`. Reversing the odd-indexed elements results in `[1, 4, 3, 2, 5]`.
    #
    #Given the general case, the output will be the list `a` with the odd-indexed elements reversed. The exact values will depend on the value of `n`.
    #
    #Output:
#Overall this is what the function does:The function `func_1` does not accept any parameters. It reads an integer `n` from user input, where 3 <= n <= 10^5, and creates a list `a` containing integers from 1 to `n`. It then reverses the elements at odd indices in the list `a`. Finally, it prints the modified list `a` with elements separated by spaces. The function does not return any value.

