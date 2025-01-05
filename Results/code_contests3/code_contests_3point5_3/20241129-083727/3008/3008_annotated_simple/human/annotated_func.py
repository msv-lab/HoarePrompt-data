#State of the program right berfore the function call: n is a non-negative integer.**
def func():
    n = input()
    s = 0
    if (n % 10 != 0) :
        s = 1
    #State of the program after the if block has been executed: *`n` is a non-negative integer. If n % 10 != 0, then `s` is updated to 1. Otherwise, `s` remains 0.
    print(2 * (n / 10) + s)
#Overall this is what the function does:The function `func` reads an input `n`, checks if `n % 10` is not equal to 0, updates the value of `s` to 1 if true, and then prints the result of the expression `2 * (n / 10) + s`. The function does not accept any parameters and performs basic arithmetic operations on the input `n`. It does not handle error cases such as non-integer inputs or division by zero.

