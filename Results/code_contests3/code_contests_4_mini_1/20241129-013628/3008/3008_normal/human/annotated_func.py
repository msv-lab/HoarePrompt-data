#State of the program right berfore the function call: n is a non-negative integer such that 0 ≤ n ≤ 10^18.
def func():
    n = input()
    s = 0
    if (n % 10 != 0) :
        s = 1
    #State of the program after the if block has been executed: *`n` is a non-negative integer such that 0 ≤ `n` ≤ 10^18 and `s` is 0. If `n` is not divisible by 10, then `s` is set to 1. Otherwise, `s` remains 0.
    print(2 * (n / 10) + s)
#Overall this is what the function does:The function accepts a non-negative integer `n` (input as a string), checks if `n` is not divisible by 10, and initializes `s` to 1 if true (or 0 otherwise). It then prints the result of the expression `2 * (n / 10) + s`. The function, however, does not handle invalid inputs (e.g., non-integer values) and assumes `n` will always be a valid non-negative integer as per the given constraints.

