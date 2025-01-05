#State of the program right berfore the function call: x is an integer such that -109 <= x <= 109.**
def func():
    n = abs(input())
    d = int(ceil((sqrt(1 + 8 * n) - 1) / 2))
    print[[0, 2, 1, 0], [1, 0, 0, 2]][n % 2][d % 4] + d
#Overall this is what the function does:The function `func` takes no input parameters. It calculates the absolute value of an input, performs a mathematical operation involving square root and ceiling functions, and then prints a value based on the result of a nested list lookup. The function does not have a specified return value.

