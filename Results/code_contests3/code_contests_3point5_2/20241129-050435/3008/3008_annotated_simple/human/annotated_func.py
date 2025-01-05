#State of the program right berfore the function call: n is a non-negative integer.**
def func():
    n = input()
    s = 0
    if (n % 10 != 0) :
        s = 1
    #State of the program after the if block has been executed: *`n` is a non-negative integer, `s` is 1. If the last digit of `n` is not 0, then `s` is updated to 1.
    print(2 * (n / 10) + s)
#Overall this is what the function does:The function `func` reads an input integer `n`, checks if the last digit of `n` is not 0, updates the variable `s` to 1 accordingly, and then prints the result of the expression `2 * (n / 10) + s`. The function does not explicitly return any value. However, there is a potential issue with the division operation if `n` is not divisible by 10, leading to a possible loss of precision in the output. It should be noted that the code does not handle invalid input cases if `n` is not an integer.

