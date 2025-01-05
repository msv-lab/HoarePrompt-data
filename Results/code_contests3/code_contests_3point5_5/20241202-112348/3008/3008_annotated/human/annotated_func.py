#State of the program right berfore the function call: n is a non-negative integer.**
def func():
    n = input()
    s = 0
    if (n % 10 != 0) :
        s = 1
    #State of the program after the if block has been executed: *`n` is a non-negative integer entered by the user, `s` is 0. If the last digit of `n` is not 0, then `s` is updated to 1. Otherwise, `s` remains 0.
    print(2 * (n / 10) + s)
#Overall this is what the function does:The function `func` prompts the user to input a non-negative integer `n`, calculates `s` based on whether the last digit of `n` is not zero, and then prints the result of the expression `2 * (n / 10) + s`. The function does not explicitly return any value, and it assumes that the user will input a valid non-negative integer. However, there is a missing functionality where the input should be converted to an integer type for proper arithmetic operations.

