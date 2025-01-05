#State of the program right berfore the function call: n is a non-negative integer such that 0 ≤ n ≤ 10^18.
def func():
    n = input()
    s = 0
    if (n % 10 != 0) :
        s = 1
    #State of the program after the if block has been executed: *`n` is a non-negative integer such that 0 ≤ `n` ≤ 10^18. If `n` is not divisible by 10, then `s` is set to 1. If `n` is divisible by 10, `s` remains 0.
    print(2 * (n / 10) + s)
#Overall this is what the function does:The function accepts no parameters and reads a non-negative integer `n` from input, where `0 ≤ n ≤ 10^18`. It calculates and prints the result of `2 * (n / 10) + s`, where `s` is set to 1 if `n` is not divisible by 10, and remains 0 if `n` is divisible by 10. The function does not return any value.

