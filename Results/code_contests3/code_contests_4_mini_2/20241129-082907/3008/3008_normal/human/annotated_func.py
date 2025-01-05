#State of the program right berfore the function call: n is a non-negative integer such that 0 ≤ n ≤ 10^18.
def func():
    n = input()
    s = 0
    if (n % 10 != 0) :
        s = 1
    #State of the program after the if block has been executed: *`n` is a string input. If the last digit of `n` is not 0, then `s` is set to 1. If the last digit of `n` is 0, no changes are made to `s`, which remains 0.
    print(2 * (n / 10) + s)
#Overall this is what the function does:The function accepts a string input representing a non-negative integer, checks if the last digit is not zero, and attempts to print an expression based on `n`; however, it will raise a `TypeError` during execution due to incorrect handling of string input in the arithmetic operation.

