#State of the program right berfore the function call: n is a non-negative integer.**
def func():
    n = input()
    s = 0
    if (n % 10 != 0) :
        s = 1
    #State of the program after the if block has been executed: *n is a non-negative integer entered by the user. If the last digit of n is not 0, s is updated to 1. Otherwise, s remains 0.
    print(2 * (n / 10) + s)
#Overall this is what the function does:The function `func` prompts the user to input a non-negative integer `n`, checks if the last digit of `n` is not 0, updates the value of `s` accordingly, and then prints the result of the mathematical expression `2 * (n / 10) + s`. However, there is a potential issue with the division operation, as the input `n` obtained from the user is treated as a string, not as an integer, which may lead to unexpected results.

