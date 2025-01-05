#State of the program right berfore the function call: n is a non-negative integer such that 0 ≤ n ≤ 10^18.
def func():
    n = input()
    s = 0
    if (n % 10 != 0) :
        s = 1
    #State of the program after the if block has been executed: *`n` is a non-negative integer such that 0 ≤ `n` ≤ 10^18 and `s` is initialized to 0. If `n` is not divisible by 10, then `s` is set to 1. If `n` is divisible by 10, `s` remains 0.
    print(2 * (n / 10) + s)
#Overall this is what the function does:The function accepts a non-negative integer input `n` (from user input) and computes a value based on whether `n` is divisible by 10. It prints `2 * (n / 10) + 1` if `n` is not divisible by 10, and `2 * (n / 10)` if it is. However, it does not return any value and the input is taken as a string, which may lead to a `TypeError` if `n` is not converted to an integer.

