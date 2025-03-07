#State of the program right berfore the function call: n is an integer such that 3 <= n <= 10^5.
def func_1():
    a = list(range(1, int(input()) + 1))
    a[::2] = a[::2][::-1]
    print(a)
    #This is printed: [5, 2, 3, 4, 1] (where the elements at even indices of the list are reversed, and the list contains integers from 1 to n inclusive)
#Overall this is what the function does:The function `func_1` does not accept any parameters. It reads an integer `n` from the user input, where `3 <= n <= 10^5`. It then creates a list `a` containing integers from 1 to `n` inclusive. The elements at even indices of the list are reversed, and the modified list is printed. The function does not return any value. After the function concludes, the list `a` is printed in a modified form where the elements at even indices are reversed, and the program state is unchanged except for the printed output.

