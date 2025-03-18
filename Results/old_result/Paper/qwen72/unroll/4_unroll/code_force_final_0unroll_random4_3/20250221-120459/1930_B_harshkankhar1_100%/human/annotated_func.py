#State of the program right berfore the function call: n is an integer such that 3 <= n <= 10^5.
def func_1():
    a = list(range(1, int(input()) + 1))
    a[::2] = a[::2][::-1]
    print(*a)
    #This is printed: [n, 2, n-1, 4, n-2, 6, ..., n%2+1, n-1, n%2] (where the elements at even indices are in descending order from n to 1, and the elements at odd indices are in ascending order from 2 to n-1)
#Overall this is what the function does:The function `func_1` does not accept any parameters. It reads an integer from the user input, constructs a list `a` containing integers from 1 to the input integer (inclusive), and then reverses the elements at even indices of the list. Finally, it prints the modified list. The list `a` is printed such that elements at even indices are in descending order starting from the input integer, and elements at odd indices are in ascending order starting from 2. The function does not return any value.

