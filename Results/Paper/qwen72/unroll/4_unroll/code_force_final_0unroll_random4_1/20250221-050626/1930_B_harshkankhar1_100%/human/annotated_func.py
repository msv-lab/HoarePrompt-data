#State of the program right berfore the function call: n is an integer such that 3 <= n <= 10^5.
def func_1():
    a = list(range(1, int(input()) + 1))
    a[::2] = a[::2][::-1]
    print(*a)
    #This is printed: [5, 2, 3, 4, 1] (where the elements at even indices of the list are reversed, and the list is printed as a space-separated sequence of integers)
#Overall this is what the function does:The function `func_1` reads an integer from user input, creates a list of integers from 1 to the input integer (inclusive), reverses the elements at even indices of the list, and prints the modified list as a space-separated sequence of integers. The function does not accept any parameters and does not return any value.

