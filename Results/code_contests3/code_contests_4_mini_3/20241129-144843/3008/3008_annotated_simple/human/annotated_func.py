#State of the program right berfore the function call: n is a non-negative integer such that 0 ≤ n ≤ 10^18.
def func():
    n = input()
    s = 0
    if (n % 10 != 0) :
        s = 1
    #State of the program after the if block has been executed: *`n` is a non-negative integer such that 0 ≤ n ≤ 10^18. If `n` is not a multiple of 10, `s` is set to 1. Otherwise, `s` remains 0.
    print(2 * (n / 10) + s)
#Overall this is what the function does:The function accepts a non-negative integer input `n`, checks if `n` is a multiple of 10, and then calculates and prints the value of `2 * (n / 10) + 1` if `n` is not a multiple of 10, or `2 * (n / 10)` if `n` is a multiple of 10. However, the function does not handle invalid input scenarios (e.g., non-integer inputs) and should convert the input to an integer before performing calculations.

