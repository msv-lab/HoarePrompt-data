#State of the program right berfore the function call: n is a non-negative integer such that 0 ≤ n ≤ 10^18.
def func():
    n = input()
    s = 0
    if (n % 10 != 0) :
        s = 1
    #State of the program after the if block has been executed: *`n` is a string input representing a non-negative integer. If the last digit of the integer represented by `n` is not 0, then `s` is set to 1. If the last digit is 0, `s` remains 0.
    print(2 * (n / 10) + s)
#Overall this is what the function does:The function accepts no parameters and reads a non-negative integer from user input as a string. It checks if the last digit of the integer is not zero and sets a variable `s` to 1 if true, otherwise `s` remains 0. Then, it attempts to print the result of the expression `2 * (n / 10) + s`. However, since `n` is a string, attempting to perform division will raise a TypeError, and the output is not defined due to this error. Thus, the function does not handle the conversion of `n` from a string to an integer, leading to a potential runtime error.

