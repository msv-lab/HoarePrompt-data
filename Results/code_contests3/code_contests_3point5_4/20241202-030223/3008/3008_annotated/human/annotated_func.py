#State of the program right berfore the function call: n is a non-negative integer.**
def func():
    n = input()
    s = 0
    if (n % 10 != 0) :
        s = 1
    #State of the program after the if block has been executed: *n is the input value. If the last digit of n is not 0, s is updated to 1. Otherwise, s remains 0.
    print(2 * (n / 10) + s)
#Overall this is what the function does:The function `func` prompts the user for input, calculates `s` based on whether the last digit of the input `n` is not 0, and then prints the result of the mathematical expression `2 * (n / 10) + s`. The code does not explicitly specify the type of `n` after the input, so there could be issues with division if the input is not an integer. Additionally, the function does not return any value.

