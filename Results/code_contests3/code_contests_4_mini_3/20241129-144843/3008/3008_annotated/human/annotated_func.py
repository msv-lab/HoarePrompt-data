#State of the program right berfore the function call: n is a non-negative integer such that 0 ≤ n ≤ 10^18.
def func():
    n = input()
    s = 0
    if (n % 10 != 0) :
        s = 1
    #State of the program after the if block has been executed: *`n` is a non-negative integer such that 0 ≤ `n` ≤ 10^18; `s` is 0. If `n` is not divisible by 10, then `s` is set to 1. Otherwise, `s` remains 0.
    print(2 * (n / 10) + s)
#Overall this is what the function does:The function accepts a non-negative integer input `n` and calculates a result based on its divisibility by 10. Specifically, it prints the value of `2 * (n / 10) + 1` if `n` is not divisible by 10, and `2 * (n / 10)` if `n` is divisible by 10. However, the function does not return any value and it does not handle the case where `n` is input as a string, which can lead to a TypeError when performing arithmetic operations.

