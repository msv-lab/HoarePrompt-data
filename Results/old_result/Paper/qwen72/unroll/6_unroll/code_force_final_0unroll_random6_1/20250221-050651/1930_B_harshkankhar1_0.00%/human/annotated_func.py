#State of the program right berfore the function call: n is an integer such that 3 <= n <= 10^5.
def func_1():
    a = list(range(1, int(input()) + 1))
    a[::2] = a[::2][::-1]
    print(a)
    #This is printed: [n, 2, n-2, 4, n-4, 6, ..., 3, n-1, 1] (where the elements at even indices are reversed and the elements at odd indices remain in their original positions)
#Overall this is what the function does:The function `func_1` does not accept any parameters. It reads an integer from user input, creates a list of integers from 1 to the input integer (inclusive), reverses the elements at even indices, and prints the modified list. The final state of the program after the function concludes is that the list is printed in the format [n, 2, n-2, 4, n-4, 6, ..., 3, n-1, 1], where elements at even indices are in reverse order and elements at odd indices remain in their original positions. The function does not return any value.

