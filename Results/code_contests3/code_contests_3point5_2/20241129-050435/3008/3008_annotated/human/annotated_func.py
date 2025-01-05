#State of the program right berfore the function call: n is a non-negative integer.**
def func():
    n = input()
    s = 0
    if (n % 10 != 0) :
        s = 1
    #State of the program after the if block has been executed: *`n` is a string, `s` is 1. If the last digit of `n` is not 0, `s` is updated to 1. Otherwise, there is no change in the values of `n` and `s`.
    print(2 * (n / 10) + s)
#Overall this is what the function does:The function `func` reads an input as a string `n`, checks if the last digit of `n` is not 0, updates the variable `s` to 1 accordingly, and then prints the result of the mathematical expression 2 * (n / 10) + s. However, there are potential issues in the code like handling the conversion of the string input `n` to an integer for mathematical operations.

