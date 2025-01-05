#State of the program right berfore the function call: n is a non-negative integer.**
def func():
    n = input()
    s = 0
    if (n % 10 != 0) :
        s = 1
    #State of the program after the if block has been executed: *n is a non-negative integer as a string, s is either 1 or 0 based on whether n is divisible by 10 or not. If n % 10 != 0, s is 1. Otherwise, s is 0.
    print(2 * (n / 10) + s)
#Overall this is what the function does:The function `func` prompts the user to input a value `n`, converts it to an integer, and calculates a result based on whether `n` is divisible by 10. If `n` is not divisible by 10, it computes `2 * (n / 10) + 1`, otherwise it computes `2 * (n / 10)`. However, there is a missing logic in the code where the input should be converted to an integer before performing arithmetic operations. This missing functionality could lead to unexpected results or errors when processing the input.

