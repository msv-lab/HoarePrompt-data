#State of the program right berfore the function call: n is a non-negative integer such that 0 ≤ n ≤ 10^18.
def func():
    n = input()
    s = 0
    if (n % 10 != 0) :
        s = 1
    #State of the program after the if block has been executed: *`n` is a non-negative integer; if `n` is not divisible by 10, then `s` is set to 1. If `n` is divisible by 10, `s` remains 0.
    print(2 * (n / 10) + s)
#Overall this is what the function does:The function accepts a non-negative integer `n` (input as a string), checks if `n` is not divisible by 10, and sets `s` to 1 if that is the case. It then prints the result of the expression `2 * (n / 10) + s`. Since `n` is input as a string, it must be converted to an integer before performing operations, and any non-integer input would lead to a runtime error. The function does not handle any errors that may arise from invalid input, such as non-numeric characters or excessively large values beyond 10^18.

